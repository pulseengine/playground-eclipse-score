---
id: DOC-PROCESS-MANAGEMENT-GUIDELINE-143
title: Process Management Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Guideline

### Process Management Guideline

{{artifact:GD_GUIDL__PROCESS_MANAGEMENT:status,safety-level,security}}

This document describes the general guidances for Process Management based on the concept which is defined [[title]]<doc_concept__process_management>.

# General Hints

The detailed implementation of all process areas defined in the process description for
the project shall be described in the
Workflow Platform Management <workflow_platform_management>.

## Templates

The process and strategy description shall use the following templates:
process_management_templates.

## Requirements

For the process descriptions the following mandatory requirements exist:

.. _workflow_process_management_requirements:

# Activities for Process Management

This section describes in detail which steps need to be performed for the process
Management.

.. list-table:: Activities for Process Management
   :header-rows: 1
   :widths: 10,60,30,30

   * - Step
     - Description
     - Responsible
     - Approver
   * - 1. <pm_create_maintain_strategy>
     - Create/Maintain Process Management Strategy
     - [[title]] <rl__contributor>
     - [[title]] <rl__process_community>
   * - 2. <pm_define_approve_process_description>
     - Define/Approve Process Description
     - [[title]] <rl__contributor>
     - [[title]] <rl__process_community>
   * - 3. <pm_monitor_improve_process>
     - Monitor/Control Process Implementation
     - [[title]] <rl__contributor>
     - [[title]] <rl__process_community>

.. _pm_create_maintain_strategy:

## Create/Maintain Process Strategy

[[title]] <rl__contributor> (as author, submitter) creates and maintains the
process management strategy. They create Pull request (PR) for contributions.

The potential contribution is discussed during the public Process Community Meetings
or standard pull request reviews and if decided to implement,
[[title]] <rl__process_community> approves the Pull Request to include
the contribution in the process strategy.

.. _pm_define_approve_process_description:

## Define/Approve Process Description

[[title]] <rl__contributor> (as author, submitter) creates and maintains the
process description. They create Pull request (PR) for contributions.

The potential contribution is discussed during the public Process Community Meetings
or standard pull request reviews and if decided to implement,
[[title]] <rl__process_community> approves the Pull Request to include
the contribution in the process description.

.. _pm_monitor_improve_process:

## Monitor/Improve Process

If potential improvements are detected, the [[title]] <rl__contributor> triggers
an ISSUE for improvement by using the
`Issue Template Improvement <https://github.com/eclipse-score/.github/blob/main/.github/ISSUE_TEMPLATE/4_Task.yml>`_.

The potential improvement is discussed during the public Process Community Meetings
and if decided to implement, a pull request to follow pm_create_maintain_strategy
or pm_define_approve_process_description must be created.

# Tailoring

### IIC Requirements Tailored

{{artifact:GD_GUIDL__IIC_REQ_TAILORED:status,safety-level,security}}

