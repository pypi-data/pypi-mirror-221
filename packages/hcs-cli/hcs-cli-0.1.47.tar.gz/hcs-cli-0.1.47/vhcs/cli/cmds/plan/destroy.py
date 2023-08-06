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

import click
import vhcs.plan as plan
import vhcs.support.plan_util as util

@click.command()
@click.option("--file", "-f", type=click.File("rt"), required=False, help="Specified the combined plan file.")
@click.option("--force/--fail-fast", type=bool, default=True, required=False, help="Force mode: try deleting everything and continue on error. Fail-fast mode: Stop on the first error.")
@click.option("--resource", "-r", type=str, required=False, help="Specify a single resource in the plan to deploy.")
@click.option("--include-related-resources/--single-resource-only", type=bool, default=False, required=False, help="Used with --resource. Specify whether to process related resources, or just the target resource.")
@click.option("--parallel/--sequential", type=bool, default=True, required=False, help="Specify deployment mode, parallel or sequential.")
def destroy(file, resource: str, include_related_resources: bool, parallel: bool, force: bool):

    data, extra = util.load_plan(file)
    concurrency = 10 if parallel else 1
    try:
        return plan.destroy(data, force, resource, include_related_resources, concurrency, extra)
    except (FileNotFoundError, plan.PlanException, plan.PluginException) as e:
        return str(e), 1
    