---
id: DOC-INDEX-73772
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Component Architecture

### Orchestrator Architecture

{{artifact:DOC__ORCHESTRATOR_ARCHITECTURE:status,safety-level,security}}

## Overview

Brief summary

## Requirements Linked to Component Architecture

.. code-block:: none

## Description

General Description

Design Decisions - For the documentation of the decision the [[GD_TEMP__CHANGE_DECISION_RECORD]] can be used.

Design Constraints

# Rationale Behind Architecture Decomposition

Mandatory: a motivation for the decomposition or reason for not further splitting it into lower level components.

# Component Architecture

## Static Architecture

The components are designed to cover the expectations from the feature architecture
(i.e. if already exists a definition it should be taken over and enriched).

### Orchestrator

{{artifact:COMP__ORCHESTRATOR:status,safety-level,security}}

### Orchestrator

{{artifact:COMP_ARC_STA__ORCH__ORCHESTRATOR:status,safety-level,security}}

## Dynamic Architecture

.. .. comp_arc_dyn:: Dynamic View
## Interfaces

### add_design

{{artifact:LOGIC_ARC_INT_OP__ORCH__ADD_DESIGN:status,safety-level,security}}

### desing_done

{{artifact:LOGIC_ARC_INT_OP__ORCH__DESING_DONE:status,safety-level,security}}

### get_deployment_mut

{{artifact:LOGIC_ARC_INT_OP__ORCH__GET_DEPLOYMENT_MUT:status,safety-level,security}}

### use_config

{{artifact:LOGIC_ARC_INT_OP__ORCH__USE_CONFIG:status,safety-level,security}}

### into_program_manager

{{artifact:LOGIC_ARC_INT_OP__ORCH__INTO_PROGRAM_MANAGER:status,safety-level,security}}

### get_programs

{{artifact:LOGIC_ARC_INT_OP__ORCH__GET_PROGRAMS:status,safety-level,security}}

### get_shutdown_notifier

{{artifact:LOGIC_ARC_INT_OP__ORCH__GET_SHUTDOWN_NOTIFIER:status,safety-level,security}}

### Design

{{artifact:COMP__ORCH_DESIGN_IMPL:status,safety-level,security}}

### Deployment

{{artifact:COMP__ORCH_DEPLOYMENT_IMPL:status,safety-level,security}}

### register_invoke_fn

{{artifact:LOGIC_ARC_INT_OP__ORCH__REGISTER_INVOKE_FN:status,safety-level,security}}

### register_invoke_method

{{artifact:LOGIC_ARC_INT_OP__ORCH__RIM:status,safety-level,security}}

### register_event

{{artifact:LOGIC_ARC_INT_OP__ORCH__REGISTER_EVENT1:status,safety-level,security}}

### register_if_else_condition

{{artifact:LOGIC_ARC_INT_OP__ORCH__REGISTER_IF_ELSE_COND:status,safety-level,security}}

### add_program

{{artifact:LOGIC_ARC_INT_OP__ORCH__ADD_PROGRAM1:status,safety-level,security}}

### bind_events_as_global

{{artifact:LOGIC_ARC_INT_OP__ORCH__BIND_EVENTS_AS_GLOBAL:status,safety-level,security}}

### bind_events_as_local

{{artifact:LOGIC_ARC_INT_OP__ORCH__BIND_EVENTS_AS_LOCAL:status,safety-level,security}}

### bind_events_as_timer

{{artifact:LOGIC_ARC_INT_OP__ORCH__BIND_EVENTS_AS_TIMER:status,safety-level,security}}

### bind_invoke_to_worker

{{artifact:LOGIC_ARC_INT_OP__ORCH__BIND_INVOKE_TO_WORKER:status,safety-level,security}}

### bind_shutdown_event_as_global

{{artifact:LOGIC_ARC_INT_OP__ORCH__BIND_SHUTDOWN_EVENT_G:status,safety-level,security}}

### bind_shutdown_event_as_local

{{artifact:LOGIC_ARC_INT_OP__ORCH__BIND_SHUTDOWN_EVENT_L:status,safety-level,security}}

.. .. code-block:: rst

..    .. real_arc_int:: <Title>
# Functional Requirements

### Error logging

{{artifact:COMP_REQ__ORCHESTRATOR__LOGGING:status,safety-level,security}}

### Error logging

{{artifact:COMP_REQ__ORCHESTRATOR__DEPLOY:status,safety-level,security}}

## Lower Level Components

.. .. comp_arc_sta:: Component Name 2
.. .. note::
.. .. attention::
