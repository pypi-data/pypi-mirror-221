"""
Copyright 2023-2023 VMware Inc.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from copy import deepcopy
import time
import threading
from graphlib import TopologicalSorter
from graphviz import Digraph
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable


class Node:
    id: str
    dependencies: list[str] = []
    data: Any = None

class DAG:
    graph: dict[str, set[str]]
    data: dict[str, Any]

    def __init__(self):
        self.graph = {}
        self.data = {}

    def add(self, id: str, data: Any, dependencies = None):
        if id in self.data:
            raise Exception('Node already added to graph: ' + id)
        self.data[id] = data
        self.graph[id] = set(dependencies) if dependencies else set()


    def validate(self):
        all_keys = self.data.keys()
        for k, v in self.graph.items():
            for d in v:
                if d not in all_keys:
                    raise Exception(f"Blueprint error: target dpendency not found: from={k}, target={d}")
    
def process_blueprint(blueprint, fn_process_node: Callable, reverse: bool, concurrency: int = 3):
    dag = _build_graph(blueprint)

    if reverse:
        _reverse_dag(dag)

    return _walkthrough(dag, fn_process_node, concurrency)

def _build_graph(blueprint):
    dag = DAG()

    from vhcs.common import util
    def add_node(name, obj):
        dependencies = set()
        variables = util.deep_find_variables(obj)
        for v in variables:
            i = v.find('.')
            resource_name = v if i < 0 else v[:i]
            dependencies.add(resource_name)
        after = obj.get('after')
        if after:
            def _add(t):
                if t in dependencies:
                    raise Exception("Invalid blueprint: statement after contains a dependency that is already implicitly created. This is not necessary. Key: " + t)
                dependencies.add(t)
            if isinstance(after, str):
                _add(after)
            else:
                for v in after:
                    _add(v)
        dag.add(name, obj, dependencies)
    
    for k,v in blueprint['resources'].items():
        add_node(k, v)
    defaults = blueprint.get('defaults')
    if defaults:
        add_node('defaults', defaults)
    vars = blueprint.get('vars')
    if vars:
        add_node('vars', vars)
    providers = blueprint.get('providers')
    if providers:
        for p in providers:
            add_node(p['type'], p)
    
    dag.validate()
    return dag

def _walkthrough(dag: DAG, fn_process_node: Callable, concurrency: int):
    topological_sorter = TopologicalSorter(dag.graph)
    topological_sorter.prepare()
    lock = threading.Lock()

    flags = {
        'err': None,
        'stop': False
    }

    def process_node(node_id):
        err = None
        try:
            ret = fn_process_node(node_id)
            if ret == False:
                flags['stop'] = True
        except Exception as e:
            err = e

        with lock:
            if err:
                flags['err'] = err
            else:
                topological_sorter.done(node_id)

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        while topological_sorter.is_active():
            with lock:
                if flags['err'] or flags['stop']:
                    break
                read_nodes = topological_sorter.get_ready()
            if not len(read_nodes):
                time.sleep(1)
                continue
            for node in read_nodes:
                executor.submit(process_node, node)
        executor.shutdown(wait=True)
        if flags['err']:
            raise flags['err']
        
def _has_indirect_dependency(tree: dict, from_node: str, to_node: str):
    deps = list(tree[from_node])
    deps.remove(to_node)
    while deps:
        n = deps.pop()
        new_deps = tree[n]
        if to_node in new_deps:
            return True
        deps += new_deps
    return False

def graph(blueprint: dict, state: dict, simplify: bool) -> Digraph:
    dag = _build_graph(blueprint)
    topological_sorter = TopologicalSorter(dag.graph)
    sorted_nodes = list(topological_sorter.static_order())
    graph = Digraph(name=f"Deployment {blueprint['deploymentId']}", comment="Simplified" if simplify else None)
    
    class styles:
        deployed = {
            'style': 'filled',
            'fillcolor': 'lightgrey'
        }
        runtime = {
            'shape': 'hexagon'
        }
        provider = {
            'shape': 'component'
        }
        resource = {
        }
        vars = {
            'shape': 'note'
        }

    def _is_deployed(node_name):
        data = state['output'].get(node_name)
        if isinstance(data, list):
            return any(d for d in data)
        return data

    def _get_node_style(node_name):
        n = dag.data[node_name]
        attr = {}
        if 'type' in n:
            attr |= styles.provider
        elif node_name in blueprint['resources']:
            if n['kind'].startswith('runtime/'):
                attr |= styles.runtime
            else:
                attr |= styles.resource
        elif node_name in state:
            attr |= styles.vars
        if _is_deployed(node_name):
            attr |= styles.deployed
        return attr
        
    
    for node in sorted_nodes:
        attrs = _get_node_style(node)
        graph.node(node, **attrs)

    # Add the edges based on the dependencies
    for node, dependencies in dag.graph.items():
        for dependency in dependencies:
            if simplify and _has_indirect_dependency(dag.graph, from_node=node, to_node=dependency):
                continue    #simplify the diagram by removing ommitable 
            graph.edge(dependency, node)

    return graph

def _reverse_dag(dag: DAG):
    old_dep = deepcopy(dag.graph)
    dag.graph = {}
    for k, h in old_dep.items():
        dag.graph[k] = set()

    def add_dep(from_node: str, to_node: str):
        holder = dag.graph[from_node]
        holder.add(to_node)
    
    for k, h in old_dep.items():
        for t in h:
            add_dep(t, k)



def _test(reverse):
    print('reverse=', reverse)
    dag = DAG()
    dag.add("a", "a")
    dag.add("b1", "b1", {"a"})
    dag.add("b2", "b2", {"a"})
    dag.add("c", "c", {"b1"})
    dag.add("d", "d", {"b2", "c"})

    if reverse:
        _reverse_dag(dag)

    def fn_proc(id):
        print("-> ", id)
        print('sleeping', id)
        time.sleep(2)
        print("<- ", id)

    _walkthrough(dag, fn_proc, 3)
    print('exit')

if __name__ == '__main__':
    _test(False)
    _test(True)