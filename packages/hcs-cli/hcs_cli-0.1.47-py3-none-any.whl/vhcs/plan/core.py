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

import threading
import typing
import inspect
import re
from subprocess import CalledProcessError
from copy import deepcopy
import vhcs.common.util as util
from . import dag
from . import context
from .helper import PlanException, process_template
from .actions import actions
from .kop import KOP
from importlib import import_module

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def _prepare_data(data: dict, additional_context: dict, resource_name: str):
    if additional_context:
        common_items = util.get_common_items(additional_context.keys(), data.keys())
        if common_items:
            raise PlanException("blueprint and context have conflict keys: " + str(common_items))
        data.update(additional_context)
    blueprint, pending = process_template(data)
    if resource_name and resource_name not in blueprint['resources']:
        raise PlanException("Resource target not found: " + resource_name)
    
    for k, v in pending.items():
        if v.startswith('defaults.') or v.startswith('vars.'):
            raise PlanException(f"Invalid blueprint. Unresolved static references. Variable not found: {v}. Required by {k}")
    deployment_id = blueprint['deploymentId']
    state_file = deployment_id + '.state.yml'
    prev = _load_state(state_file)
    state = {'pending': pending}
    state.update(blueprint)
    state.update(prev)

    context.set('deploymentId', state['deploymentId'])
    
    # try solving more variables
    # for k, v in state['output'].items():
    #     if not v:
    #         continue
    #     if not _has_successful_deployment(state, k):
    #         continue
    #     _resolve_pending_keys(state, k)
    
    return blueprint, state, state_file

# def _has_successful_deployment(state, name):
#     for v in state['log']['create']:
#         if v['name'] != name:
#             continue
#         if v['action'] == 'success':
#             return True
        
def deploy(data: dict, additional_context: dict = None, resource_name: str = None, include_related_resources: bool = True, concurrency: int = 4):
    
    blueprint, state, state_file = _prepare_data(data, additional_context, resource_name)
    state['log']['create'] = []    # clear deploy log

    def process_resource(name: str):
        # ignore functional nodes (defaults, providers)
        if name not in blueprint['resources']:
            return
        res_data = blueprint['resources'][name]
        
        if resource_name:
            if name == resource_name or include_related_resources:
                need_deploy = True
            else:
                need_deploy = False
        else:
            need_deploy = True
        if need_deploy:
            _deploy_res(name, res_data, state)
            util.save_data_file(state, state_file)
        if resource_name and name == resource_name:
            return False    # quit dag.process_blueprint

    try:
        dag.process_blueprint(blueprint, process_resource, False, concurrency)
    except CalledProcessError as e:
        raise PlanException(str(e))
    finally:
        util.save_data_file(state, state_file)

def _load_state(state_file):
    state = util.load_data_file(state_file, default={})
    if 'output' not in state:
        state['output'] = {}
    if 'destroy_output' not in state:
        state['destroy_output'] = {}
    if 'log' not in state:
        state['log'] = {}
    exec_log = state['log']
    if 'deploy' not in exec_log:
        exec_log['deploy'] = []
    if 'destroy' not in exec_log:
        exec_log['destroy'] = []
    return state

def _parse_statement_for(name, state) -> typing.Tuple[str, list]:
    # for: email in vars.userEmails
    res = state['resources'][name]
    for_statement = res.get('for')
    if not for_statement:
        return None, None
    pattern = r'(.+?)\s+in\s+(.+)'
    matcher = re.search(pattern, for_statement)

    def _raise_error(reason):
        raise PlanException(f"Invalid for statement: {reason}. Resource={name}, statement={for_statement}")
    
    if not matcher:
        _raise_error('Invalid syntax')
    var_name = matcher.group(1)
    values_name = matcher.group(2)
    values = _get_value_by_path(state, values_name, f"resources.{name}.for")
    if not isinstance(values, list):
        reason = 'The referencing value is not a list. Actual type=' + type(values).__name__
        _raise_error(reason)

    return var_name, values

def _get_value_by_path(state, var_name, required_by_attr_path):
    i = var_name.find('.')
    if i < 0:
        resource_name = var_name
    else:
        resource_name = var_name[:i]

    def _raise(e):
        msg = f"Plugin error: '{var_name}' does not exist in the output of resource '{resource_name}', which is required by '{required_by_attr_path}'"
        raise PlanException(msg) from e
    
    if resource_name in state['resources']:
        try:
            return util.deep_get_attr(state, "output." + var_name)
        except Exception as e:
            _raise(e)
    if resource_name in state:
        try:
            return util.deep_get_attr(state, var_name)
        except Exception as e:
            _raise(e)

def _get_value_by_path2(state, var_name):
    i = var_name.find('.')
    if i < 0:
        resource_name = var_name
    else:
        resource_name = var_name[:i]

    if resource_name in state['resources']:
        try:
            return util.deep_get_attr(state, "output." + var_name), True
        except Exception as e:
            log.debug(e)
            return None, False
        
    if resource_name in state:
        try:
            return util.deep_get_attr(state, var_name), True
        except Exception as e:
            log.debug(e)
            return None, False
    return None, False

def _deploy_res(name, res, state):
    def fn_deploy1(handler, res_data: dict, res_state: dict, fn_set_state: typing.Callable, kop: KOP):
        if _is_runtime(res):
            kop.start(KOP.MODE.create)
            new_state = handler.process(res_data, deepcopy(state))
            if new_state:
                fn_set_state(new_state)
            return
        
        if not res_state:
            action = actions.create
        else:
            action = handler.decide(res_data, res_state)
            
        if action == actions.skip:
            kop.skip('Already deployed')
            return
        
        if action == actions.recreate:
            with KOP(state, res['kind'], name) as kop2:
                kop2.id = res_state.get('id')
                kop2.start(KOP.MODE.delete)
                handler.destroy(res_data, res_state)
            action = actions.create

        new_state = None
        if action == actions.create:
            kop.start(KOP.MODE.create)
            if _has_save_state(handler.deploy):
                new_state = handler.deploy(res_data, res_state, fn_set_state)
            else:
                new_state = handler.deploy(res_data, res_state)
            kop.id(None if not new_state else new_state.get('id'))
        elif action == actions.update:
            kop.id(res_state.get('id'))
            kop.start(KOP.MODE.update)
            if _has_save_state(handler.update):
                new_state = handler.update(res_data, res_state, fn_set_state)
            else:
                new_state = handler.update(res_data, res_state)
        else:
            raise PlanException(f"Unknown action. Plugin={name}, action={action}")
        
        if new_state:
            fn_set_state(new_state)
    _handle_resource(name, res, state, True, fn_deploy1)

def _is_runtime(res):
    kind = res.get('kind')
    return kind and kind.startswith('runtime/')

def _has_save_state(fn):
    signature = inspect.signature(fn)
    args = list(signature.parameters.keys())
    if len(args) < 3:
        return False
    name = args[2]
    if name == 'save_state':
        return True
    p = signature.parameters[args[2]]
    return p.annotation == typing.Callable

def _assert_all_vars_resolved(data, name):
    def fn_on_value(path, value):
        if isinstance(value, str) and value.find('${') >= 0:
            raise PlanException(f"Unresolved variable '{path}' for plugin '{name}'. Value={value}")
        return value
    util.deep_update_object_value(data, fn_on_value)

_providers = {}
_provider_lock = threading.Lock()
def _get_resource_handler(kind: str, state: dict):
    provider_type, res_handler_type = kind.split('/')
    res_handler_type = res_handler_type.replace('-', '_')
    # Ensure provider initialized
    with _provider_lock:
        if provider_type == 'runtime':
            return import_module(res_handler_type)
        if not provider_type in _providers:
            provider = import_module("vhcs.plan.provider." + provider_type)
            # Get provider data
            filter_by_type = lambda m: m['type'] == provider_type
            providers = state.get('providers', {})
            meta = next(filter(filter_by_type, providers), None)
            data = meta.get('data') if meta else None
            if data:
                _assert_all_vars_resolved(data, provider_type)
            log.info("[init] Provider: %s", provider_type)
            state['output'][provider_type] = provider.prepare(data)
            log.info("[ok  ] Provider: %s", provider_type)
            _providers[provider_type] = 1
    module_name = f"vhcs.plan.provider.{provider_type}.{res_handler_type}"
    return import_module(module_name)

def get_common_items(iter1, iter2):
    return set(iter1).intersection(set(iter2))

def _handle_resource(name, res, state, for_deploy: bool, fn_process: typing.Callable):
    kind = res['kind']

    kop_mode = KOP.MODE.create if for_deploy else KOP.MODE.delete
    with KOP(state, kind, name, kop_mode) as kop:
        data = res.get('data', {})

        # resolve vars
        def _get_value(path):
            return _get_value_by_path2(state, path)
        
        if data:
            data = deepcopy(data)
            ret = util.process_variables(data, _get_value)
            if for_deploy:
                if ret['pending']:
                    msg = f"Fail resolving variables for resource '{name}'. Unresolvable variables: {ret['pending']}"
                    raise PlanException(msg)
        state['resources'][name] = dict(res)
        state['resources'][name]['data'] = data

        conditions = res.get('conditions')
        if conditions:
            conditions = deepcopy(conditions)
            ret = util.process_variables(conditions, _get_value)
            unsatisfied_condition_name = _get_unsatisfied_condition_name(conditions)
            if unsatisfied_condition_name:
                kop.skip('Condition not met: ' + unsatisfied_condition_name)
                return


        handler = _get_resource_handler(kind, state)
        def _handle_resource_1(resource_data, resource_state, fn_set_state, kop):
            if _is_runtime(res):   # runtime has no refresh
                pass
            else:
                new_state = handler.refresh(resource_data, resource_state)
                fn_set_state(new_state)
                resource_state = new_state

            fn_process(handler, resource_data, resource_state, fn_set_state, kop)

        for_var_name, values = _parse_statement_for(name, state)
        if for_var_name:
            if for_var_name in data:
                raise PlanException(f"Invalid blueprint: variable name defined in for-statement already exists in data declaration. Resource: {name}. Conflicting names: {common}")
            kop.id('(group)')
            kop.start()
            size = len(values)
            # ensure output array placeholder
            output = state['output'].setdefault(name, [])
            while len(output) < size:
                output.append(None)
            for i in range(size):
                v = values[i]
                with KOP(state, kind, name, kop_mode) as kop_per_item:
                    kop_per_item.id(str(i))
                    resource_state = output[i]
                    def _fn_set_state(o):
                        output[i] = deepcopy(o)
                    resource_data = deepcopy(data)
                    resource_data[for_var_name] = v
                    _handle_resource_1(resource_data, resource_state, _fn_set_state, kop_per_item)
        else:
            resource_state = state['output'].get(name)
            def _fn_set_state(o):
                state['output'][name] = deepcopy(o)
            resource_data = deepcopy(data)
            _handle_resource_1(resource_data, resource_state, _fn_set_state, kop)

def _get_unsatisfied_condition_name(conditions):
    if not conditions:
        return
    for condition_name, expr in conditions.items():
        if not expr:
            return condition_name
        if expr.find('${') >= 0: # still have unresolved variables
            return condition_name




def _destroy_res(name, res_node, state, force):
    def fn_destroy1(handler, res_data: dict, res_state: dict, fn_set_state: typing.Callable, kop: KOP):
        if not res_state:
            kop.skip('Not found')
            return
        
        kop.id(res_state.get('id'))
        kop.start(KOP.MODE.delete)
        try:
            ret = handler.destroy(res_data, res_state)
            state['destroy_output'][name] = deepcopy(ret)
            fn_set_state(None)
        except Exception as e:
            if force:
                kop.error(e)
                pass
            else:
                # add_log('error', e) will be handled by framework.
                raise
    _handle_resource(name, res_node, state, False, fn_destroy1)

def destroy(data, force: bool, resource_name: str = None, include_related_resources: bool = True, concurrency: int = 4, additional_context: dict = None):
    
    blueprint, state, state_file = _prepare_data(data, additional_context, resource_name)
    state['log']['delete'] = []    # clear destroy log

    def destroy_resource(node_name):
        # ignore functional nodes (defaults, providers)
        node = blueprint['resources'].get(node_name)
        if not node:
            return
        # skip runtime
        if node['kind'].startswith('runtime/'):
            return
        
        res_node = state['resources'].get(node_name)
        if not res_node:
            res_node = blueprint['resources'][node_name]

        if resource_name:
            if include_related_resources:
                pass
            else:
                if resource_name != node_name:
                    return
            _destroy_res(node_name, res_node, state, force)
            util.save_data_file(state, state_file)
            if resource_name == node_name:
                return True
        else:
            _destroy_res(node_name, res_node, state, force)
            util.save_data_file(state, state_file)

    try:
        dag.process_blueprint(blueprint, destroy_resource, True, concurrency)
    except CalledProcessError as e:
        raise PlanException(str(e))
    finally:
        util.save_data_file(state, state_file)

def graph(data: dict, additional_context: dict = None, simplify: bool = True):
    blueprint, state, state_file = _prepare_data(data, additional_context, None)
    g = dag.graph(blueprint, state, simplify)
    return g

