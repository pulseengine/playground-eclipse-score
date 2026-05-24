---
id: DOC-LAUNCH-MANAGER-1684
title: Launch Manager
type: specification
status: approved
tags: [eclipse-score]
---

# Launch manager

The Launch Manager is a component that provides a framework for managing
the lifecycle of processes in the S-CORE platform. It allows for launching,
monitoring, and controlling processes based on defined configurations and
requirements. As such, it is a central part of the lifecycle management in
S-CORE and knows about the state of all processes in the system.

It's foreseen ECU projects will need a custom state management to fulfill ECU-project specific requirements.  The S-CORE stack will offer a framework to control application lifecycle, but will not specify the State Manager.

# Overview

The functionality of the Launch Manager is defined by configuration data, which spawns a directed acyclic graph (DAG) of Components <Component> and so called Run Targets <Run Target>.
The Run Targets <Run Target> are virtual nodes in the DAG and represent Run States <Run State> of the system.
The Launch Manager is responsible for starting and stopping the processes in the correct order, based on the dependencies defined in the configuration data.

E.g. the configuration below consists of three Run Targets <Run Target> managing 9 components. If the user selects e.g. the Run Target "debug" the Launch Manager will start the components in the following order defined by the dependencies.

1. flash driver
2. filesystem
3. setup filesystems
4. networking
5. ssh

The [[COMP__LIFECYCLE_LAUNCH_MANAGER]] implements the following interfaces,for the selection of Run Target s, starting and stopping of components and monitoring of the processes.

## Switching between Run Targets

The Launch Manager allows switching between different Run Targets <Run Target>. When a switch is requested, the Launch Manager evaluates the current state and the target state,
determining which components need to be started or stopped based on their dependencies.

When a component is started the Launch Manager will start the corresponding process and monitor its state via Ready Conditions <Ready Condition>.

Ready Conditions <Ready Condition> are essential mechanisms that determine when a component has successfully completed its startup phase and is ready to fulfill its intended role in the system. These conditions provide flexibility in defining what constitutes a "ready" state for different types of components. For SCORE applications, components can actively report their readiness through the Lifecycle Interface by signaling specific states or custom conditions. For native applications, the Launch Manager relies on external indicators such as process existence, file creation, network socket availability, or successful process termination. This dual approach ensures that both modern SCORE-aware applications and legacy native applications can participate in the dependency management system, allowing the Launch Manager to orchestrate complex startup sequences where components depend on each other's readiness rather than just their launch order.

# Control Interface

This interface provides control functionality for activating and managing run targets.It allows users to trigger execution of configured Run targets <Run target> through a standardized activation mechanism.

## Static architecture

### Control Interface

{{artifact:LOGIC_ARC_INT__LIFECYCLE__CONTROLIF:status,safety-level,security}}}}

**Operations**

### Activate Run Target

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__ACTIVATE_TARGET:status,safety-level,security}}}}

The Launch Manager shall provide an interface, which allows an external State Manager application to request the Launch Manager to start, stop or restart applications or groups of applications,
which allows the implementation of a state management applications to support dynamic state control.

## Dynamic architecture

The following use cases are supported by the `ControlInterface` provided by the Launch Manager.

**Activating a Run Target**

When a request to activate a run target is received via the `ControlInterface`, the Launch Manager shall perform the following operations:

1. **Validation**: Evaluate if the conditions are correct for activating the requested run target:
   - The run target exists in the configuration
   - All dependencies for the run target are resolvable
   - Required resources are available

2. **Transition Logic**: Determine the transition from the current state to the target state:
   - If a different run target is active, perform a switch operation (stop current, start requested)
   - If the same run target is already active, verify its state and potentially restart failed components

3. **Execution**: Execute the transition in the correct dependency order:
   - Stop components that are not part of the new run target
   - Start components that are required for the new run target
   - Respect dependency relationships during both stop and start operations

4. **Response**: Return status to the caller:
   - Success if all components transitioned correctly
   - Failure with detailed error information if any component failed to transition

This unified approach allows external state managers to request any run target activation without needing to know the current system state, as the Launch Manager handles the transition logic internally.

### Control interface dynamic architecture activate run target

{{artifact:FEAT_ARC_DYN__LIFECYCLE__CONTROL_IF_ACTIVATE:status,safety-level,security}}}}

## Requirements

- [[FEAT_REQ__LIFECYCLE__CONTROL_COMMANDS]]
- [[FEAT_REQ__LIFECYCLE__REQUEST_RUN_TARGET_START]]
- [[FEAT_REQ__LIFECYCLE__SWITCH_RUN_TARGETS]]

# Lifecycle Interface

The Launch Manager provides interfaces for communication with launched applications, supporting two distinct application types:

1. **SCORE Applications**: Implement the full Lifecycle Interface for bidirectional communication with state reporting, liveliness indication, and conditional signaling
2. **Native Applications**: Controlled exclusively via POSIX signals (SIGTERM, SIGKILL, etc.) without direct API communication

This dual approach enables the Launch Manager to manage both legacy native applications and SCORE-aware applications within the same system.

The Lifecycle Interface serves as the communication channel between applications and the Launch Manager:

**For SCORE Applications:**
- Application state reporting (started, running, stopped)
- Conditional signaling for application dependencies

**For Native Applications:**
- Process lifecycle control via POSIX signals
- Basic process monitoring (PID-based status checking)
- Exit code evaluation for failure detection

## Static architecture

### Lifecycle Interface

{{artifact:LOGIC_ARC_INT__LIFECYCLE__LIFECYCLE_IF:status,safety-level,security}}}}

### run

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__RUN:status,safety-level,security}}}}

### terminate

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__TERMINATE:status,safety-level,security}}}}

The following use cases are supported by the Lifecycle Interface, with different capabilities depending on the application type.

**SCORE Application State Communication**

SCORE applications implementing the Lifecycle Interface can communicate their internal state to the Launch Manager. The state information includes:

- **Started**: Application has successfully initialized and is ready to operate
- **Running**: Application is actively executing its main functionality
- **Stopped**: Application has terminated or is in the process of shutting down

The Launch Manager uses this state information for:

- Dependency resolution for other applications
- Recovery action decisions
- Status reporting to external state managers via the Control Interface

**SCORE Application Conditional Signaling**

SCORE applications can signal custom conditions to the Launch Manager via the Alive Interface. This enables:

- Complex dependency management beyond simple process startup
- Coordination between interdependent applications

Custom conditions can be used by other applications as launch dependencies, allowing for sophisticated startup orchestration.

**Native Application Control**

Native applications that do not implement the Lifecycle Interface are controlled through POSIX signals:

- **SIGTERM**: Graceful shutdown request
- **SIGKILL**: Forced termination (after timeout)
- **SIGUSR1/SIGUSR2**: Application-specific signals (if configured)

The Launch Manager monitors native applications through:

- Process ID (PID) tracking
- Exit code evaluation
- Resource usage monitoring via OS facilities
- Timeout-based failure detection

For native applications, the Launch Manager provides:

- Basic lifecycle control (start/stop)
- Simple dependency management based on process existence
- Configurable startup/shutdown timeouts
- Exit code-based success/failure determination

## Dynamic Architecture

### Lifecyle Interface

{{artifact:FEAT_ARC_DYN__LIFECYCLE__STATE_MACHINE:status,safety-level,security}}}}

## Requirements

- [[FEAT_REQ__LIFECYCLE__PROCESS_STATE_COMM]]
- [[FEAT_REQ__LIFECYCLE__CUSTOM_COND_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__SMART_WATCHDOG_CONFIG]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_MONITORING]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_TERMINATION]]
- [[FEAT_REQ__LIFECYCLE__SHUTDOWN_SIGNAL]]
- [[FEAT_REQ__LIFECYCLE__LAUNCH_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_ORDERING]]
- [[FEAT_REQ__LIFECYCLE__PARALLEL_LAUNCH_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__WAITFOR_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_INPUT_OUTPUT]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_LAUNCH_ARGS]]
- [[FEAT_REQ__LIFECYCLE__UID_GID_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__TOTAL_WAIT_TIME_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__POLLING_INTERVAL]]
- [[FEAT_REQ__LIFECYCLE__LAUNCH_PRIORITY_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__CWD_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__TERMINAL_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__STD_HANDLE_REDIR]]
- [[FEAT_REQ__LIFECYCLE__SECPOL_NON_ROOT]]
- [[FEAT_REQ__LIFECYCLE__RETRIES_CONFIGURABLE]]
- [[FEAT_REQ__LIFECYCLE__FD_INHERITANCE]]
- [[FEAT_REQ__LIFECYCLE__SUPPORT_SECPOL_TYPE]]
- [[FEAT_REQ__LIFECYCLE__SUPPLEMENTARY_GROUPS]]
- [[FEAT_REQ__LIFECYCLE__SCHEDULING_POLICY]]
- [[FEAT_REQ__LIFECYCLE__RUNMASK_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__ASLR_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__PROCESS_RLIMIT_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__DETACH_PARENT_PROCESS]]
- [[FEAT_REQ__LIFECYCLE__RUNNING_PROCESSES]]
- [[FEAT_REQ__LIFECYCLE__DROP_SUPERVSION]]
- [[FEAT_REQ__LIFECYCLE__MULTI_START_SUPPORT]]
- [[FEAT_REQ__LIFECYCLE__VALIDATE_CONDITIONS]]
- [[FEAT_REQ__LIFECYCLE__VALIDATION_CONDITIONS]]
- [[FEAT_REQ__LIFECYCLE__CONSISTENT_DEPENDENCIES]]
- [[FEAT_REQ__LIFECYCLE__STOP_PROCESS_DEPENDENTS]]
- [[FEAT_REQ__LIFECYCLE__STOP_ORDER_SPEC]]
- [[FEAT_REQ__LIFECYCLE__OCI_COMPLIANT]]

# Alive Interface

The Alive Interface provides a basic watchdog functionality interface that delivers essential monitoring capabilities for system health and responsiveness tracking.
It implements core watchdog operations including heartbeat signals to ensure reliable operation and automatic recovery from unresponsive states.

**SCORE Application Liveliness Reporting**

SCORE applications can periodically signal their liveliness to the Launch Manager through the Alive Interface. This mechanism allows the Launch Manager to:

- Detect application failures or hangs
- Trigger recovery actions when liveliness is lost
- Maintain accurate process health status

The liveliness mechanism includes:

- Configurable heartbeat intervals per application
- Timeout detection and failure handling

## Static architecture

### Alive API

{{artifact:LOGIC_ARC_INT__LIFECYCLE__ALIVE_IF:status,safety-level,security}}}}

**Operations**

### report_health_status

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__REPORT_HEALTH:status,safety-level,security}}}}

## Dynamic architecture

### Alive Monitoring

{{artifact:FEAT_ARC_DYN__LIFECYCLE__ALIVE_MONITORING:status,safety-level,security}}}}

## Requirements

- [[FEAT_REQ__LIFECYCLE__MONITORING_PROCESSES]]
- [[FEAT_REQ__LIFECYCLE__POLLING_INTERVAL]]
- [[FEAT_REQ__LIFECYCLE__FAILURE_DETECT]]
- [[FEAT_REQ__LIFECYCLE__LIVELINESS_DETECTION]]
