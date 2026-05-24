---
id: DOC-INDEX-48394
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _roles:

# Roles

## Project Management Roles

### Project Lead

{{artifact:RL__PROJECT_LEAD:status,safety-level,security}}

## Project Process Roles

### Process Community Member

{{artifact:RL__PROCESS_COMMUNITY:status,safety-level,security}}

## Project Development Roles

### Infrastructure Tooling Community Member

{{artifact:RL__INFRASTRUCTURE_TOOLING_COMMUNITY:status,safety-level,security}}

### Contributor

{{artifact:RL__CONTRIBUTOR:status,safety-level,security}}

### Committer

{{artifact:RL__COMMITTER:status,safety-level,security}}

### Testing Community Member

{{artifact:RL__TESTING_COMMUNITY:status,safety-level,security}}

### Architecture Community Member

{{artifact:RL__ARCHITECTURE_COMMUNITY:status,safety-level,security}}

### Project Security Team

{{artifact:RL__SECURITY_TEAM:status,safety-level,security}}

## Project Teams

### Platform Team

{{artifact:RL__PLATFORM_TEAM:status,safety-level,security}}

### Delivery Team

{{artifact:RL__DELIVERY_TEAM:status,safety-level,security}}

### Release Team

{{artifact:RL__RELEASE_TEAM:status,safety-level,security}}

## Project Roles List

.. needtable::
   :style: table
   :columns: title;id;tags
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["role"]):
         if need['is_external'] == False:
                results.append(need)
