---
id: DOC-HEALTH-MONITOR-51126
title: Health Monitor
type: specification
status: approved
tags: [eclipse-score]
---

# Health Monitor

The Health Monitor is library, that together with the Launch Manager provide a way to monitor
the application health in similar fashion as the AUTOSAR `Platform Health Manager` (PHM).

The main features of the Health Monitor are the following monitoring functions:

- Alive supervision
  - Periodic monitoring of checkpoints, which must fit the pre-configured expected number of notifications in the given interval (not too many, not too few)
  - Protecting from running checks too often or too rarely
- Deadline supervision
  - Timing requirement between two checkpoints.
- Logical
  - Specifies in which order two or more checkpoints must be called

The Health Monitor itself is monitored via the Launch Manager with via alive supervision only.

# Overview

- Inter process communication (IPC) only needed for the alive monitoring between Health Monitor and Launch Manager
- Easier configuration
    - The monitoring rules can be configured dynamically on demand basis
    - The monitoring can be started and stopped dynamically
- Debugging of problems possibly easier
    - Mapping of the events from a single process vs. the monitored application and the monitor

## Drawbacks over classical external process monitoring

- Harder safety argumentation. The following chapter describes the issues and the possible solutions.

## Safety

As the Health Monitor is linked as part of the monitored application, it raises the following concerns
with respect to safety:

- How can it be ensured, that the monitored application does not interfere with the monitoring functionality?
- How can it be ensured, that the Health Monitor does not incorrectly report alive to the Launch Manager when it has detected
  a supervision error?

These concerns are valid, but can be addressed using the following techniques:

- Hiding of the internal data from the user:
    - For example, if the monitoring is implemented in a thread, the thread ID must not be exposed to the calling application.
    - Hide the implementation for example with the pImpl-approach
- Protecting the memory of the library by using guard pages where the application memory is located, and protect it with mprotect()
   - possibly with a help of a custom allocator
- Protecting the data with a checksum and possibly a sequence counter
   - The internal data of the library can be checksum'ed every operation cycle, and by adding for example, a sequence
     counter (or some more complex mathematical function), further checkpoints for detecting misbehavior can be implemented
- Using a safe programming language, which does not allow a raw pointer access
- Testing the application with Valgrid etc.
- Redundant monitoring, if the self monitoring with above is not sufficient, an another library in another memory location can detect sporadic corruption of the other.

## Error Reactions

- When the Health Monitor detects a failed supervision, it shall stop triggering alive notifications to the Launch Manager.
- Additionally, when the error occurs, the Health Monitor triggers a failure notification to the Launch Manager to reduce the time
  to react on the error. This obviously will only work if the Health Monitor is still working and correctly scheduled. Thus the
  worst case reaction time calculations must be made on the monitoring rules specified in the Launch Manager for the monitored application.

# Deadline Monitor API

## Static Architecture

### Deadline Monitor API

{{artifact:LOGIC_ARC_INT__LIFECYCLE__DEADLINE_MONITOR_IF:status,safety-level,security}}

### configure_minimum_time

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__MIN_TIME:status,safety-level,security}}

### configure_maximum_time

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__MAX_TIME:status,safety-level,security}}

### link_condition

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__LINK_COND_DL:status,safety-level,security}}

### mark_start

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__START:status,safety-level,security}}

### mark_end

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__END:status,safety-level,security}}

### on_timer_expiry

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__TIMER_EXPIRY:status,safety-level,security}}

### enable_monitoring

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__ENABLE_MON:status,safety-level,security}}

### disable_monitoring

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__DISABLE_MON:status,safety-level,security}}

### check_configuration

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__CHECK_CFG:status,safety-level,security}}

## Dynamic Architecture

### Application health monitoring

{{artifact:FEAT_ARC_DYN__LIFECYCLE__APP_HEALTH_MONI:status,safety-level,security}}

The most important interactions are the following:

.. list-table:: Sequence diagram Description
   :widths: 10 90
   :header-rows: 1

   * - Sequence number
     - Description
   * - 001
     - Launch Manager configuration for the alive monitoring of the `Monitored application` is parsed. This contains for example, what is the expected interval of alive notifications,
       how long grace period is given before failing to a missed (never received) alive notification etc.
   * - 002
     - Start the startup grace period timer to allow the application to startup, before timing out to a missed alive notification
   * - 003
     - The `Monitored application` is started. (To simplify, no startup checks drawn here)
   * - 004
     - The `Monitored application` instantiate and configure the HealthMonitor
   * - 006
     - Cyclic reporting aliveness to the monitor.
   * - 007
     - HealthMonitor waking up and checking if the checkpoint(s) have been called
   * - 008
     - Report aliveness to the LM's application specific supervision, observing the health of the HealthMonitor itself
   * - 009
     - Checkpoint sent, but not on time
   * - 010
     - Wake up and check if the checkpoint(s) have been triggered. In this case it was not, and thus actions 011 and 012 are triggered.
   * - 011
     - Trigger a failure event to the Launch Manager. This event allows the monitor react faster than waiting for the timeout to expire.
   * - 012
     - Additionally, triggering alive must be stopped

# Logical Monitor API

## Static Architecture

### Logical Monitor API

{{artifact:LOGIC_ARC_INT__LIFECYCLE__LOGICAL_MONITOR_IF:status,safety-level,security}}

### add_entry_point

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__ENTRY_POINT:status,safety-level,security}}

### add_exit_point

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__EXIT_POINT:status,safety-level,security}}

### add_allowed_transition

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__ALLOWED_TRANS:status,safety-level,security}}

### link_condition

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__LINK_COND_LG:status,safety-level,security}}

### record_checkpoint

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__REC_CHECKPOINT:status,safety-level,security}}

### enable

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__ENABLE:status,safety-level,security}}

### disable

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__DISABLE:status,safety-level,security}}

### verify

{{artifact:LOGIC_ARC_INT_OP__LIFECYCLE__VERIFY:status,safety-level,security}}

## Dynamic Architecture

### Logical control flow monitoring

{{artifact:FEAT_ARC_DYN__LIFECYCLE__APP_CTRL_FLOW_MONI:status,safety-level,security}}

