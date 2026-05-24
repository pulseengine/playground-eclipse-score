---
id: DOC-INDEX-11491
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Requirements

## Launching Processes

### Support for launching processes

{{artifact:FEAT_REQ__LIFECYCLE__LAUNCH_SUPPORT:status,safety-level,security}}

### Process dependency handling

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_ORDERING:status,safety-level,security}}

### Launching processes in parallel

{{artifact:FEAT_REQ__LIFECYCLE__PARALLEL_LAUNCH_SUPPORT:status,safety-level,security}}

### Control interface support

{{artifact:FEAT_REQ__LIFECYCLE__CUSTOM_COND_SUPPORT:status,safety-level,security}}

### Forward process information

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_INPUT_OUTPUT:status,safety-level,security}}

### Handling process args

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_LAUNCH_ARGS:status,safety-level,security}}

### Launching process in debug mode

{{artifact:FEAT_REQ__LIFECYCLE__DEBUG_SUPPORT:status,safety-level,security}}

### Launching process in state waiting for a debugger connection

{{artifact:FEAT_REQ__LIFECYCLE__SUPPORT_HELD_STATE:status,safety-level,security}}

### Process user, group IDs support

{{artifact:FEAT_REQ__LIFECYCLE__UID_GID_SUPPORT:status,safety-level,security}}

### Process priority support

{{artifact:FEAT_REQ__LIFECYCLE__LAUNCH_PRIORITY_SUPPORT:status,safety-level,security}}

### CWD support

{{artifact:FEAT_REQ__LIFECYCLE__CWD_SUPPORT:status,safety-level,security}}

### Launching terminal

{{artifact:FEAT_REQ__LIFECYCLE__TERMINAL_SUPPORT:status,safety-level,security}}

### Standard handle redirection

{{artifact:FEAT_REQ__LIFECYCLE__STD_HANDLE_REDIR:status,safety-level,security}}

### Non-root support

{{artifact:FEAT_REQ__LIFECYCLE__SECPOL_NON_ROOT:status,safety-level,security}}

### Configurable amount of retries

{{artifact:FEAT_REQ__LIFECYCLE__RETRIES_CONFIGURABLE:status,safety-level,security}}

### Process capability support

{{artifact:FEAT_REQ__LIFECYCLE__CAPABILITY_SUPPORT:status,safety-level,security}}

### File descriptor inheritance support

{{artifact:FEAT_REQ__LIFECYCLE__FD_INHERITANCE:status,safety-level,security}}

### Security policy support

{{artifact:FEAT_REQ__LIFECYCLE__SUPPORT_SECPOL_TYPE:status,safety-level,security}}

### Supplementary group support

{{artifact:FEAT_REQ__LIFECYCLE__SUPPLEMENTARY_GROUPS:status,safety-level,security}}

### Scheduling support

{{artifact:FEAT_REQ__LIFECYCLE__SCHEDULING_POLICY:status,safety-level,security}}

### CPU runmask support

{{artifact:FEAT_REQ__LIFECYCLE__RUNMASK_SUPPORT:status,safety-level,security}}

### ASLR support

{{artifact:FEAT_REQ__LIFECYCLE__ASLR_SUPPORT:status,safety-level,security}}

### Resource limit support

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_RLIMIT_SUPPORT:status,safety-level,security}}

### Process detach from parent support

{{artifact:FEAT_REQ__LIFECYCLE__DETACH_PARENT_PROCESS:status,safety-level,security}}

## Conditional Launching

### Conditional launching

{{artifact:FEAT_REQ__LIFECYCLE__WAITFOR_SUPPORT:status,safety-level,security}}

### Conditionally launch of processes

{{artifact:FEAT_REQ__LIFECYCLE__COND_PROCESS_START:status,safety-level,security}}

### Condition timeout

{{artifact:FEAT_REQ__LIFECYCLE__TOTAL_WAIT_TIME_SUPPORT:status,safety-level,security}}

### Conditional launch polling interval

{{artifact:FEAT_REQ__LIFECYCLE__POLLING_INTERVAL:status,safety-level,security}}

### Pre-start validation

{{artifact:FEAT_REQ__LIFECYCLE__VALIDATE_CONDITIONS:status,safety-level,security}}

### post-start validation

{{artifact:FEAT_REQ__LIFECYCLE__VALIDATION_CONDITIONS:status,safety-level,security}}

### Launched Process status

{{artifact:FEAT_REQ__LIFECYCLE__LAUNCHER_STATUS_STORAGE:status,safety-level,security}}

### Condition check based on status

{{artifact:FEAT_REQ__LIFECYCLE__CONDITION_CHECK_METHOD:status,safety-level,security}}

### Configuration of action based on condition evaluation

{{artifact:FEAT_REQ__LIFECYCLE__CONFIG_ACTIONS_COND:status,safety-level,security}}

### Condition check based on path

{{artifact:FEAT_REQ__LIFECYCLE__PATH_CONDITION_CHECK:status,safety-level,security}}

### Condition check based on ENV

{{artifact:FEAT_REQ__LIFECYCLE__ENV_VARIABLE_COND_CHECK:status,safety-level,security}}

### Condition check based on all dependency

{{artifact:FEAT_REQ__LIFECYCLE__DEPENDENCY_CHECK:status,safety-level,security}}

### Condition check based on at least one dependency

{{artifact:FEAT_REQ__LIFECYCLE__CHECK_DEPENDENCY_EXEC:status,safety-level,security}}

### Condition check for each SWC its dependencies

{{artifact:FEAT_REQ__LIFECYCLE__DEFINE_SWC_DEPENDENCIES:status,safety-level,security}}

### Condition check for each SWC its stop sequence

{{artifact:FEAT_REQ__LIFECYCLE__STOP_SEQUENCE:status,safety-level,security}}

## Process Management

### Process adoption

{{artifact:FEAT_REQ__LIFECYCLE__RUNNING_PROCESSES:status,safety-level,security}}

### Dropping process responsibility

{{artifact:FEAT_REQ__LIFECYCLE__DROP_SUPERVSION:status,safety-level,security}}

### Multiple instance of executable

{{artifact:FEAT_REQ__LIFECYCLE__MULTI_START_SUPPORT:status,safety-level,security}}

### Invalid dependency

{{artifact:FEAT_REQ__LIFECYCLE__CONSISTENT_DEPENDENCIES:status,safety-level,security}}

### Dangling dependency

{{artifact:FEAT_REQ__LIFECYCLE__STOP_PROCESS_DEPENDENTS:status,safety-level,security}}

### Coordination stop dependency

{{artifact:FEAT_REQ__LIFECYCLE__STOP_ORDER_SPEC:status,safety-level,security}}

### OCI Compliant

{{artifact:FEAT_REQ__LIFECYCLE__OCI_COMPLIANT:status,safety-level,security}}

## Run targets

### Run target support

{{artifact:FEAT_REQ__LIFECYCLE__RUN_TARGET_SUPPORT:status,safety-level,security}}

### Launching run target

{{artifact:FEAT_REQ__LIFECYCLE__START_NAMED_RUN_TARGET:status,safety-level,security}}

### Switch between run targets

{{artifact:FEAT_REQ__LIFECYCLE__SWITCH_RUN_TARGETS:status,safety-level,security}}

### Process state

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_STATE_COMM:status,safety-level,security}}

## Terminating Processes

### Stop timeout

{{artifact:FEAT_REQ__LIFECYCLE__CONFIGURABLE_TIMEOUT:status,safety-level,security}}

### Terminating process

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_TERMINATION:status,safety-level,security}}

### Handling process dependency in termination

{{artifact:FEAT_REQ__LIFECYCLE__TERMINATIONN_DEPENDENCY:status,safety-level,security}}

### Configurable delay between SIGTERM and SIGKILL

{{artifact:FEAT_REQ__LIFECYCLE__TIME_TO_WAIT_CONFIG:status,safety-level,security}}

### Normal shutdown

{{artifact:FEAT_REQ__LIFECYCLE__LAUNCH_MANAGER_SHUTDOWN:status,safety-level,security}}

### Slow shutdown

{{artifact:FEAT_REQ__LIFECYCLE__SLOW_SHUTDOWN_SUPPORT:status,safety-level,security}}

### Fast shutdown

{{artifact:FEAT_REQ__LIFECYCLE__FAST_SHUTDOWN_SUPPORT:status,safety-level,security}}

### Launch Manager shutdown

{{artifact:FEAT_REQ__LIFECYCLE__LAUNCHER_EXIT_SHUTDOWN:status,safety-level,security}}

### Shutdown signal handling

{{artifact:FEAT_REQ__LIFECYCLE__SHUTDOWN_SIGNAL:status,safety-level,security}}

## Control Interface

### Control commands

{{artifact:FEAT_REQ__LIFECYCLE__CONTROL_COMMANDS:status,safety-level,security}}

### Query commands

{{artifact:FEAT_REQ__LIFECYCLE__QUERY_COMMANDS:status,safety-level,security}}

### Report "started/running/degraded"

{{artifact:FEAT_REQ__LIFECYCLE__CONTROLIF_STATUS:status,safety-level,security}}

### Request run target launch

{{artifact:FEAT_REQ__LIFECYCLE__REQUEST_RUN_TARGET_START:status,safety-level,security}}

## Monitoring, Notification and Recovery

### Process crash monitoring

{{artifact:FEAT_REQ__LIFECYCLE__MONITOR_ABNORMAL_TERM:status,safety-level,security}}

### Process state notification

{{artifact:FEAT_REQ__LIFECYCLE__EXT_MONITOR_NOTIFY:status,safety-level,security}}

### Recovery action

{{artifact:FEAT_REQ__LIFECYCLE__RECOVERY_ACTION_SUPPORT:status,safety-level,security}}

### Run target switch as recovery action

{{artifact:FEAT_REQ__LIFECYCLE__RECOV_RUN_TARGET_SWITCH:status,safety-level,security}}

### Monitoring and recovery: watchdog support

{{artifact:FEAT_REQ__LIFECYCLE__SMART_WATCHDOG_CONFIG:status,safety-level,security}}

### Monitoring and recovery: recovery wait time

{{artifact:FEAT_REQ__LIFECYCLE__CONFIGURABLE_WAIT_TIME:status,safety-level,security}}

### Monitoring and recovery: adopted process monitoring

{{artifact:FEAT_REQ__LIFECYCLE__MONITORING_PROCESSES:status,safety-level,security}}

### Process launch monitoring

{{artifact:FEAT_REQ__LIFECYCLE__FAILURE_DETECT:status,safety-level,security}}

### Process liveliness detection

{{artifact:FEAT_REQ__LIFECYCLE__LIVELINESS_DETECTION:status,safety-level,security}}

### Process monitoring

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_MONITORING:status,safety-level,security}}

### Recovery

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_FAILURE_REACT:status,safety-level,security}}

### Multi-instance

{{artifact:FEAT_REQ__LIFECYCLE__MULTI_INSTANCE_SUPPORT:status,safety-level,security}}

### Launch manager self health check

{{artifact:FEAT_REQ__LIFECYCLE__LM_SELF_HEALTH_CHECK:status,safety-level,security}}

### Launch manager external watchdog notification

{{artifact:FEAT_REQ__LIFECYCLE__LM_EXT_WATCHDOG_NOTIFY:status,safety-level,security}}

### Launch manager external watchdog notification - failed test

{{artifact:FEAT_REQ__LIFECYCLE__LM_EXT_WDG_FAILED_TEST:status,safety-level,security}}

### Launch manager external monitoring configuration

{{artifact:FEAT_REQ__LIFECYCLE__LM_EXT_WATCHDOG_CFG:status,safety-level,security}}

## Logging

### Logging slog2 and file support

{{artifact:FEAT_REQ__LIFECYCLE__SLOG2_LOGGING:status,safety-level,security}}

### Logging state transitions

{{artifact:FEAT_REQ__LIFECYCLE__PROCESS_LOGGING_SUPPORT:status,safety-level,security}}

### Logging timestamp

{{artifact:FEAT_REQ__LIFECYCLE__LOG_TIMESTAMP:status,safety-level,security}}

### Logging DAG

{{artifact:FEAT_REQ__LIFECYCLE__DAG_LOGGING_CONTROLIF:status,safety-level,security}}

### Configuration dependency view

{{artifact:FEAT_REQ__LIFECYCLE__DEPENDENCY_VISU:status,safety-level,security}}

## Configuration file

### Configuration file support

{{artifact:FEAT_REQ__LIFECYCLE__MODULAR_CONFIG_SUPPORT:status,safety-level,security}}

### Runtime configuration compliance

{{artifact:FEAT_REQ__LIFECYCLE__RUNTIME_CONFIG_COMPAT:status,safety-level,security}}

### Updating configuration

{{artifact:FEAT_REQ__LIFECYCLE__SESSION_EXTENSION:status,safety-level,security}}

### Module support

{{artifact:FEAT_REQ__LIFECYCLE__CLUSTERING_MODULES_SUPP:status,safety-level,security}}

### Global process properties

{{artifact:FEAT_REQ__LIFECYCLE__CENTRAL_DEFAULT_DEFINES:status,safety-level,security}}

### Lazy check of configured commands

{{artifact:FEAT_REQ__LIFECYCLE__LAZY_CHECK:status,safety-level,security}}

### Configuration Dependency view

{{artifact:FEAT_REQ__LIFECYCLE__DEPS_VISUALIZATION:status,safety-level,security}}

### Configuration Verification tool

{{artifact:FEAT_REQ__LIFECYCLE__OFFLINE_CONFIG_VALID:status,safety-level,security}}

