# HCS Plan

- [HCS Plan](#hcs-plan)
  - [File Types](#file-types)
    - [Blueprint](#blueprint)
    - [Variable File](#variable-file)
    - [Plan File](#plan-file)
    - [State File](#state-file)
  - [Principles](#principles)
    - [Provider](#provider)
  - [Syntax](#syntax)
    - [Sections Explained](#sections-explained)
    - [Resource Dependency](#resource-dependency)
      - [Example - No dependency](#example---no-dependency)
      - [Example - Implicit dependency](#example---implicit-dependency)
      - [Example - Explicit dependency](#example---explicit-dependency)
    - [Conditional Resource](#conditional-resource)
    - [Map list to a new list](#map-list-to-a-new-list)
    - [Referencing profile value](#referencing-profile-value)
  - [Cheatsheet](#cheatsheet)


HCS Plan is the deployment engine to manage HCS resources in a declarative way.

## File Types

### Blueprint
A file that consists of the resources to be deployed, normally with varieties of variables.

### Variable File
A file that contains all the variables that required by a blueprint file.

### Plan File
- Plan file is the simple composition of blueprint file and the related variable file.
- Plan file is the deployment input of HCS plan engine.

### State File
- The deployment related states of a plan.

## Principles
### Provider
- Each provider should focus on a single API
- Resources should represent a single API object
- Resource and attribute schema should closely match the underlying API


## Syntax
### Sections Explained

```yml
# ------------
# deploymentId
# ------------
# The unique deployment ID to distinguish one deployment 
# from another. Resources will be tagged based on the deploymentId 
# if possible, and smart refresh should also consider deploymentId 
# to identify related resource, upon missing previous state.
deploymentId: myCustomer1

# ------------
# vars
# ------------
# The vars section is the input of the blueprint. All top-level variables are specified here.
# 
vars:
  provider: 0123
  userEmails:
  - a@b.com
  - c@d.com


# ------------------------
# Custom sections
# ------------------------

# Custom sections can be defined to manipulate the variables.
# For example, the common 'defaults' section is used to define
# shared variable calculation, to avoid duplicated calculation
# in each resource.
# Variables are quoted by "${}"
defaults:
  name: titan-lite-${deploymentId}

# ------------------------
# The resources section
# ------------------------
# The resources to be created. A map from unique resource 
# name to resource definition.

resources:
  myAADGroup:
    kind: azure/aad-group
    data:
        tenant: ${vars.tenantId}
  myAADUsers:
    kind: azure/aad-user
    for: email in vars.userEmails
    data:
      group: ${myAADGroup.id}
# In azure/aad-user resource handler, the received data object
# will have 'email' added, as declared in the 'for' statement:
#    {
#        'group': '<group-id>'
#        'email': '<one-of-the-emails>
#    }
```

### Resource Dependency

By default, dependency between resources are automatically calculated, as long as a resource uses the output of another resource.

#### Example - No dependency
```yaml
# Resource r1 and r2 has no dependency, so they may be deployed in parallel
resources:
  r1:
    kind: dev/dummy
  r2:
    kind: dev/dummy
```

#### Example - Implicit dependency
```yaml
# Resource r2 references output of r1. So it will be deployed after r1.
resources:
  r1:
    kind: dev/dummy
    data:
        text: hello
        delay: 1s
  r2:
    kind: dev/dummy
    data:
        text: ${r1.outputText}
```

#### Example - Explicit dependency
```yaml
# Resource r2 has no reference of r1. By specifying the "after" property,
# it's explicitly specified to be deployed after r1.
resources:
  r1:
    kind: dev/dummy
    data:
        delay: 1s
  r2:
    kind: dev/dummy
    after:
    - r1
```

### Conditional Resource
```yaml
# Resouces can be deployed only under certain condition.
vars:
  guest1: Alice
  guest2:
resources:
  r1:
    kind: dev/dummy
    conditions:
      # A logical condition named 'has_guest1' is defined.
      # Since vars.guest1 has value Alice, r1 will be deployed.
      has_guest1: ${vars.guest1}
    data:
      text: hello
  r2:
    kind: dev/dummy
    conditions:
      # This 'has_guest2' logical condition checks the value 
      # of vars.guest2. Since it's empty, resource r2 will not
      # be deployed.
      has_guest2: ${vars.guest2}
    data:
      text: hello
  r11:
    kind: dev/dummy
    conditions:
      # r11 will be deployed, after r1 is deployed.
      has_r1: ${r1.outputText}
  r21:
    kind: dev/dummy
    conditions:
      # r21 will not be deployed, because r2 is not deployed.
      has_r2: ${r2.outputText}
```

### Map list to a new list
```yaml
vars:
  tenantId: <the-tenant-id>
  userEmails:
  - u1@mydomain.com
  - u2@mydomain.com
resources:
  myAADGroup:
    kind: azure/aad-group
    data:
        tenant: ${vars.tenantId}
  myAADUsers:
    kind: azure/aad-user
    # Based on the array, multiple "aad-user" objects will be created.
    # The output of 'myAADUsers' will be an array, matching input from vars.userEmails.
    for: email in vars.userEmails
    data:
      group: ${myAADGroup.id}
  myEntitlement:
    kind: hcs/entitlement
    data:
      orgId: ${vars.orgId}
      poolIds:
      - ${myPoolGroup.id}
      resourceDetails:
      - poolId: ${myPoolGroup.id}
      # Mapping array to array
      userIds: ${[for u in myAADUser: u.id]}
```

The resource myEntitlement will receive data object with field 'userIds' as an string array:
```json
{
  'userIds': [ 'user-id1', 'user-id2' ],
  ...
}
```
### Referencing profile value
```yaml
resources:
  myLaunchItem:
    kind: hcs/launch-item
    data:
      users: ...
      entitlementId: ...
      domainName: ...
      stackUrl: ${profile.hcs.url}
```


## Cheatsheet
| Command | Description |
| ------- | ----------- |
| hcs plan deploy -f \<filename\> --sequential | Deploy resources sequentially, for debugging |
| hcs play deploy -f \<filename\> --resource \<resource-id\> | Deploy only the specified resource (and dependencies). |