---
id: DOC-LAUNCH-MANAGER-CONFIGURATION-14706
title: Launch Manager Configuration
type: specification
status: approved
tags: [eclipse-score]
---

# Launch Manager Configuration

The Launch Manager supports a set of configuration parameters, which are grouped in the following categories:

# Component Configuration Parameters

These parameters specify the arguments needed for spawning a process.

- [[FEAT_REQ__LIFECYCLE__UID_GID_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__SUPPLEMENTARY_GROUPS]]
- [[FEAT_REQ__LIFECYCLE__RUNMASK_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__LAUNCH_PRIORITY_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__CWD_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_LAUNCH_ARGS]]
- [[FEAT_REQ__LIFECYCLE__STD_HANDLE_REDIR]]
- [[FEAT_REQ__LIFECYCLE__ASLR_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_RLIMIT_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__SUPPORT_SECPOL_TYPE]]

# Dependency parameters

These parameters specify how the components depend on each other.

# Recovery parameters

These parameters specify the recovery actions for a component, when it fails.

# Alive monitoring parameters

These parameters specify the alive monitoring rules for the application.

# Requirements related to the external monitoring

These parameters specify how the Launch Manager itself is monitored.

- [[FEAT_REQ__LIFECYCLE__LM_SELF_HEALTH_CHECK]]
- [[FEAT_REQ__LIFECYCLE__LM_EXT_WATCHDOG_NOTIFY]]
- [[FEAT_REQ__LIFECYCLE__LM_EXT_WDG_FAILED_TEST]]
- [[FEAT_REQ__LIFECYCLE__LM_EXT_WATCHDOG_CFG]]

# Static Architecture

### Configuration parameters static architecture

{{artifact:LOGIC_ARC_INT__LIFECYCLE__CFG_PARAMS_STATIC:status,safety-level,security}}

