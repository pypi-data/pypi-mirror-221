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

import time
from . import images, image_copies
from .version import version

def get_images_by_provider_instance_with_asset_details(providerInstanceId: str, org_id: str):
    all_images = images.list(org_id)
    copies = image_copies.list(org_id, include_catalog_details=True,
                      search=f"providerInstanceId $eq {providerInstanceId}")
    ret = []
    for copy in copies:
        imageId = copy["catalogDetails"]["imageId"]
        for image in all_images:
            if image['id'] == imageId:
                # add additional info
                image['_assetDetails'] = copy['assetDetails']
                ret.append(image)
                break
    return ret

def delete_images(image_ids: list[str], org_id: str, timeout: int | str):
    import httpx
    
    
    def del_impl(image_id: str, tolerant: bool):
        version_api = version(image_id, org_id)
        versions = version_api.list()
        everything_ok = True
        for v in versions:
            if v['status'] == 'DELETING':
                continue
            try:
                version_api.delete(v['id'])
            except httpx.HTTPStatusError:
                if tolerant:
                    everything_ok = False
                    pass
                else:
                    raise
        return everything_ok

    for image_id in image_ids:
        if not del_impl(image_id, tolerant=True):
            time.sleep(1)
            del_impl(image_id, tolerant=False)
    
    if timeout == '0':
        return
    
    for image_id in image_ids:
        images.wait_for_deleted(image_id, org_id, timeout)  # todo: timeout