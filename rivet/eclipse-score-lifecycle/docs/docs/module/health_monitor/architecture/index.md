---
id: DOC-INDEX-11231
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_architecture_hm:

# Component Architecture

### HealthMonitor Architecture

{{artifact:DOC__HEALTH_MONITOR_ARCHITECTURE:status,safety-level,security}}}}

.. attention::
    The above directive must be updated according to your needs.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and followed by ``_architecture``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

## Overview

Document describes HealthMonitor component architecture.

### Health Monitor

{{artifact:COMP__HEALTH_MONITOR:status,safety-level,security}}}}

## Description

This component provides a set of functionalities to manage the lifecycle of programs running on the S-CORE platform.

## Requirements Linked to Component Architecture

TODO

# Rationale Behind Architecture Decomposition

Architecture is not decomposed.

## Static Architecture

### Deadline Monitor

{{artifact:COMP_ARC_STA__DEADLINE_MONITOR__STATIC_VIEW:status,safety-level,security}}}}

### Logic Monitor

{{artifact:COMP_ARC_STA__LOGIC_MONITOR__STATIC_VIEW:status,safety-level,security}}}}

### Health Monitor

{{artifact:COMP_ARC_STA__HEALTH_MONITOR__STATIC_VIEW:status,safety-level,security}}}}

## Dynamic Architecture

### HealthMonitor Creation

{{artifact:COMP_ARC_DYN__HEALTH_MONITOR__DYNAMIC_VIEW:status,safety-level,security}}}}

### HealthMonitor background thread

{{artifact:COMP_ARC_DYN__HEALTH_LIB_THREAD__DYNAMIC_VIEW:status,safety-level,security}}}}

### DeadlineMonitor Usage

{{artifact:COMP_ARC_DYN__DEADLINE_MONITOR__DYNAMIC_VIEW:status,safety-level,security}}}}

### LogicMonitor Usage

{{artifact:COMP_ARC_DYN__LOGIC_MONITOR__DYNAMIC_VIEW:status,safety-level,security}}}}

### HeartbeatMonitor Usage

{{artifact:COMP_ARC_DYN__HEARTBEAT_MONITOR__DYNAMIC_VIEW:status,safety-level,security}}}}

### Health Monitoring Startup Interaction

{{artifact:COMP_ARC_DYN__HEALTH_MONITOR__STARTUP_VIEW:status,safety-level,security}}}}

### Health Monitoring Shutdown Interaction

{{artifact:COMP_ARC_DYN__HEALTH_MONITOR__SHUTDOWN_VIEW:status,safety-level,security}}}}

## Interfaces

### DeadlineMonitor Interface

{{artifact:REAL_ARC_INT__DEADLINE_MONITOR__INTERFACE:status,safety-level,security}}}}

### LogicMonitor Interface

{{artifact:REAL_ARC_INT__LOGIC_MONITOR__INTERFACE:status,safety-level,security}}}}

### HeartbeatMonitor Interface

{{artifact:REAL_ARC_INT__HEARTBEAT_MONITOR__INTERFACE:status,safety-level,security}}}}

### HealthMonitor Interface

{{artifact:REAL_ARC_INT__HEALTH_MONITOR__INTERFACE:status,safety-level,security}}}}

