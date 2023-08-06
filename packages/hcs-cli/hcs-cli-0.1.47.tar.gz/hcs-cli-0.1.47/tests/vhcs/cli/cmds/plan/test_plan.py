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

import yaml
import os
import re
import unittest
from test_utils import CliTest
from vhcs.common.util import deep_get_attr

class _blueprints:
    d10_basic = """
deploymentId: d10
resources:
  r1:
    kind: dev/dummy
"""

    d11_basic_dep = """
deploymentId: d11
vars:
    guestName: Alice
resources:
  r1:
    kind: dev/dummy
    data:
        text: ${vars.guestName}
        delay: 1s
  r2:
    kind: dev/dummy
    data:
        text: ${r1.outputText}
"""

    d12_basic_parallel = """
deploymentId: d12
resources:
  r1:
    kind: dev/dummy
    data:
        delay: 2s
  r2:
    kind: dev/dummy
"""

    d13_basic_error_sequential = """
deploymentId: d13
resources:
  r1:
    kind: dev/dummy
    data:
        error: A simulated error
  r2:
    kind: dev/dummy
    data:
        text: ${r1.outputText}
"""

    d14_basic_error_parallel = """
deploymentId: d14
resources:
  r1:
    kind: dev/dummy
    data:
        error: A simulated error
        delay: 1s
  r2:
    kind: dev/dummy
"""

    d30_basic_statement_after = """
deploymentId: d30
resources:
  r1:
    kind: dev/dummy
    data:
        delay: 1s
  r2:
    kind: dev/dummy
    after:
    - r1
"""

    d40_basic_statement_for = """
deploymentId: d40
vars:
  userEmails:
    - a@t.com
    - b@t.com
resources:
  r1:
    kind: dev/dummy
    for: text in vars.userEmails
"""
    d50_list_map_expression = """
deploymentId: d50
vars:
  userEmails:
    - a@t.com
    - b@t.com
resources:
  r1:
    kind: dev/dummy
    for: text in vars.userEmails
  r2:
    kind: dev/dummy
    data:
      agg: "${[for r in r1: r.outputText]}"
"""

    d60_basic_condition = """
deploymentId: d60
vars:
  guest1: Alice
  guest2:
resources:
  r1:
    kind: dev/dummy
    conditions:
      has_guest1: ${vars.guest1}
    data:
      text: hello
  r2:
    kind: dev/dummy
    conditions:
      has_guest2: ${vars.guest2}
    data:
      text: hello
  r11:
    kind: dev/dummy
    conditions:
      has_r1: ${r1.outputText}
  r21:
    kind: dev/dummy
    conditions:
      has_r2: ${r2.outputText}
"""
class TestPlan(CliTest):
    @classmethod
    def setUpClass(cls):
        _cleanup_states()

    @classmethod
    def tearDownClass(cls):
        _cleanup_states()

    def test10_basic(self):
        self.verify_deploy(_blueprints.d10_basic)
        self.verify_destroy(_blueprints.d10_basic)

    def test11_basic_dep(self):
        self.verify_deploy(_blueprints.d11_basic_dep)
        self.verify_execution_log('d11', 'create', "r2 must be deployed after r1", precise_order=['start/r1', 'success/r1', 'start/r2', 'success/r2'])
        self.verify_destroy(_blueprints.d11_basic_dep)
        self.verify_execution_log('d11', 'delete', "r2 must be destroyed before r1", precise_order=['start/r2', 'success/r2', 'start/r1', 'success/r1'])

    def test12_basic_parallel(self):
        self.verify_deploy(_blueprints.d12_basic_parallel)
        self.verify_execution_log('d12', 'create', "success of r2 must before success of r1", partial_order=['success/r2', 'success/r1'])
        self.verify_destroy(_blueprints.d12_basic_parallel)
        self.verify_execution_log('d12', 'delete', "both r1 and r2 must be destroyed", any_order=['success/r2', 'success/r1'])
        
    def test13_basic_error_sequential(self):
        self.verify_deploy(_blueprints.d13_basic_error_sequential, expected_return_code=1)
        self.verify_execution_log('d13', 'create', "r2 must not be deployed, due to failure in r1", precise_order=['start/r1', 'error/r1'])
        self.verify_destroy(_blueprints.d13_basic_error_sequential)
        self.verify_execution_log('d13', 'delete', "r2 must not be destroyed, since it's not deployed", precise_order=['skip/r2', 'start/r1', 'success/r1'])

    def test14_basic_error_parallel(self):
        self.verify_deploy(_blueprints.d14_basic_error_parallel, expected_return_code=1)
        self.verify_execution_log('d14', 'create', "success of r2 must before error of r1", partial_order=['success/r2', 'error/r1'])
        self.verify_destroy(_blueprints.d14_basic_error_parallel)
        self.verify_execution_log('d14', 'delete', "both r1 and r2 must be cleaned up", any_order=['success/r2', 'success/r1'])

    def test30_basic_statement_after(self):
        self.verify_deploy(_blueprints.d30_basic_statement_after)
        self.verify_execution_log('d30', 'create', "r2 must be deployed after r1", precise_order=['start/r1', 'success/r1', 'start/r2', 'success/r2'])
        self.verify_destroy(_blueprints.d30_basic_statement_after)
        self.verify_execution_log('d30', 'delete', "r2 must be destroyed before r1", precise_order=['start/r2', 'success/r2', 'start/r1', 'success/r1'])


    def test40_basic_statement_for(self):
        self.verify_deploy(_blueprints.d40_basic_statement_for)
        self.verify_execution_log('d40', 'create', "r1 must be deployed twice with an additional one for the group", partial_order=['success/r1', 'success/r1', 'success/r1'])
        self.verify_destroy(_blueprints.d40_basic_statement_for)
        self.verify_execution_log('d40', 'delete', "r1 must be destroyed twice with an additional one for the group", any_order=['success/r1', 'success/r1', 'success/r1'])

    def test50_list_map_expression(self):
        self.verify_deploy(_blueprints.d50_list_map_expression)
        self.verify_execution_log('d50', 'create', "three r1 instances must be created before r2 start", partial_order=['success/r1', 'success/r1', 'success/r1', 'start/r2', 'success/r2'])
        self.verify_output('d50', "output.r2.agg", ['a@t.com', 'b@t.com'])
        self.verify_destroy(_blueprints.d50_list_map_expression)
        self.verify_execution_log('d50', 'delete', "three r1 must be deleted after r2", partial_order=['start/r2', 'success/r2', 'start/r1', 'start/r1', 'start/r1'])

    def test60_basic_condition(self):
        self.verify_deploy(_blueprints.d60_basic_condition)
        self.verify_execution_log('d60', 'create', "r1 and r11 are deployed. r2 and r21 are not.", partial_order=['success/r1', 'success/r11'], any_order=['skip/r2', 'skip/r21'])
        self.verify_destroy(_blueprints.d60_basic_condition)
        self.verify_execution_log('d60', 'delete', "r1 and r11 are destroyed. r2 and r22 are not.", partial_order=['success/r11', 'success/r1'], any_order=['skip/r2', 'skip/r21'])

    def verify_deploy(self, stdin_payload: str, expected_return_code: int = 0):
        self.verify("hcs plan deploy -f -", expected_data = '', expected_return_code = expected_return_code, expect_stderr_empty = False, stdin_payload = stdin_payload)
    
    def verify_destroy(self, stdin_payload: str, expected_return_code: int = 0):
        self.verify("hcs plan destroy -f -", expected_data = '', expected_return_code = expected_return_code, expect_stderr_empty = False, stdin_payload = stdin_payload)

    def verify_output(self, deployment_id: str, res_path: str, expected_value):
        with open(f'{deployment_id}.state.yml', 'rt') as file:
            state = yaml.safe_load(file)
        v = deep_get_attr(state, res_path)
        self.assertEqual(v, expected_value)

    def verify_execution_log(self, deployment_id: str, method: str, description: str, precise_order: list[str] = None, partial_order: list[str] = None, any_order: list[str] = None):
        with open(f'{deployment_id}.state.yml', 'rt') as file:
            state = yaml.safe_load(file)
        exec_logs = state['log'][method]

        actual_execution_order = []
        for entry in exec_logs:
            actual_execution_order.append(entry['action'] + '/' + entry['name'])
        
        if precise_order:
            self.assertEqual(actual_execution_order, precise_order, description)
        elif partial_order:
            filtered_order = [x for x in actual_execution_order if x in partial_order]
            self.assertEqual(filtered_order, partial_order, description)
        elif any_order:
            s1 = set(actual_execution_order)
            s2 = set(any_order)
            try:
                self.assertTrue(s1 > s2, description)
            except:
                print('DUMP actual_execution_order: ', actual_execution_order)
                print('DUMP expectation (any_order): ', any_order)
                raise
        else:
            raise Exception("One of the following must be specified: precise_order, partial_order, any_order")

def _cleanup_states():
    names = filter(lambda name: not name.startswith('__'), dir(_blueprints))
    pattern = r"deploymentId:\s+(\w+)"
    for name in names:
        value = getattr(_blueprints, name)
        m = re.search(pattern, value)
        deployment_id = m.group(1)

        state_file_name = f'{deployment_id}.state.yml'
        if os.path.exists(state_file_name):
            os.unlink(state_file_name)

if __name__ == "__main__":
    unittest.main()
