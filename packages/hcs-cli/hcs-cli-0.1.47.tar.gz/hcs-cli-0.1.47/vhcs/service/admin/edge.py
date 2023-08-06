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

import httpx
import logging
from .._util import hdc_service_client, default_crud, wait_for_res_status
from . import edge

log = logging.getLogger(__name__)

_client = hdc_service_client("admin")
_crud = default_crud(_client, "/v2/edge-deployments", 'edge')

get = _crud.get
list = _crud.list
delete = _crud.delete
create = _crud.create
wait_for_deleted = _crud.wait_for_deleted
def wait_for(id: str, org_id: str, is_ready, timeout: str | int = '20m'):
    def fn_get():
        ret = get(id, org_id)
        #log.info("Edge status: %s", ret['status'])
        return ret
    is_error = lambda t: t['status'] in ['CREATE_FAILED']
    name = 'edge/' + id
    return wait_for_res_status(fn_get, name, is_ready, is_error, timeout, polling_interval_seconds=60)

def safe_delete(id: str, org_id: str, timeout: str | int = '20m'):

    try:
        edge.delete(id, org_id=org_id)
    except httpx.HTTPStatusError as e:
        if e.response.status_code != 409:
            raise
        _wait_for_terminal_state(id, org_id, timeout)
        edge.delete(id, org_id=org_id)

    edge.wait_for_deleted(id, org_id, "10m")

def _wait_for_terminal_state(id, org_id, timeout):
    name = 'edge/' + id
    terminal_status = ['CREATE_FAILED', 'DELETED', 'DELETE_FAILED', 'MIGRATE_FAILED', 'READY', 'REPAIR_FAILED', 'UPDATE_FAILED', 'UPGRADE_FAILED']
    transition_status = [
        'CONNECT_PENDING', 
        'CREATE_ACCEPTED', 
        'CREATE_PENDING', 
        'CREATING',  
        'DELETE_PENDING', 
        'DELETING', 
        'FORCE_DELETE_PENDING', 
        'FORCE_DELETING', 
        'FORCE_REPAIR_ACCEPTED', 
        'FORCE_REPAIR_PENDING', 
        'MIGRATE_PENDING', 
        'MIGRATING', 
        'POST_PROVISIONING_CONFIG_IN_PROGRESS', 
        'REPAIRING', 
        'REPAIR_ACCEPTED', 
        'REPAIR_PENDING',
        'UPDATE_PENDING', 
        'UPDATING', 
        'UPGRADE_PENDING', 
        'UPGRADING'
    ]
    def fn_get():
        return get(id, org_id)
    status_map = {
        'ready': terminal_status,
        'error': [],
        'transition': transition_status
    }
    
    wait_for_res_status(name, fn_get, 'status', status_map, timeout)