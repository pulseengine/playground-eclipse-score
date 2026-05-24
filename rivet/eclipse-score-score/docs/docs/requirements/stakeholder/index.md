---
id: DOC-INDEX-11077
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _stakeholder_requirements:

# Stakeholder Requirements

### SW-platform stakeholder requirements

{{artifact:DOC__STAKEHOLDER_REQUIREMENTS:status,safety-level,security}}}}

## Overall goals

### Reuse of application software via managed APIs

{{artifact:STKH_REQ__OVERALL_GOALS__REUSE_OF_APP_SOFT:status,safety-level,security}}}}

### Enable cooperation via standardized APIs

{{artifact:STKH_REQ__OVERALL_GOALS__ENABLE_COOPERATION:status,safety-level,security}}}}

### Variant management

{{artifact:STKH_REQ__OVERALL_GOALS__VARIANT_MANAGEMENT:status,safety-level,security}}}}

### IP protection

{{artifact:STKH_REQ__OVERALL_GOALS__IP_PROTECTION:status,safety-level,security}}}}

## Functional requirements

### File Based Configuration

{{artifact:STKH_REQ__FUNCTIONAL_REQ__FILE_BASED:status,safety-level,security}}}}

### Support of safe Key/Value store

{{artifact:STKH_REQ__FUNCTIONAL_REQ__SUPPORT_OF_STORE:status,safety-level,security}}}}

### Safe Configuration

{{artifact:STKH_REQ__FUNCTIONAL_REQ__SAFE_CONFIG:status,safety-level,security}}}}

### Safe Computation

{{artifact:STKH_REQ__FUNCTIONAL_REQ__SAFE_COMPUT:status,safety-level,security}}}}

### Base Libraries

{{artifact:STKH_REQ__FUNCTIONAL_REQ__BASE_LIBRARIES:status,safety-level,security}}}}

### Hardware Accelerated Computation

{{artifact:STKH_REQ__FUNCTIONAL_REQ__HARDWARE_COMPUT:status,safety-level,security}}}}

### Data Persistency

{{artifact:STKH_REQ__FUNCTIONAL_REQ__DATA_PERSISTENCY:status,safety-level,security}}}}

### Operating System

{{artifact:STKH_REQ__FUNCTIONAL_REQ__OPERATING_SYSTEM:status,safety-level,security}}}}

### Video subsystem

{{artifact:STKH_REQ__FUNCTIONAL_REQ__VIDEO_SUBSYSTEM:status,safety-level,security}}}}

### Compute subsystem

{{artifact:STKH_REQ__FUNCTIONAL_REQ__COMP_SUBSYSTEM:status,safety-level,security}}}}

### Communication with external MCUs/standby controllers

{{artifact:STKH_REQ__FUNCTIONAL_REQ__COMM_WITH_CONTROL:status,safety-level,security}}}}

## Dependability

### Automotive Safety Integrity Level

{{artifact:STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY:status,safety-level,security}}}}

### Health Management

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_1:status,safety-level,security}}}}

### E2E Protection

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_2:status,safety-level,security}}}}

### HW Self-Test

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_3:status,safety-level,security}}}}

### Safe Startup and Reset

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_4:status,safety-level,security}}}}

### DMA Protection

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_5:status,safety-level,security}}}}

### Memory Protection

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_6:status,safety-level,security}}}}

### Cache Protection

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_7:status,safety-level,security}}}}

### Memory Error Correction

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_8:status,safety-level,security}}}}

### SW Lockstep

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_9:status,safety-level,security}}}}

### External Supervision

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_10:status,safety-level,security}}}}

### Safe Mode Switch

{{artifact:STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_11:status,safety-level,security}}}}

### SW-platform error reaction

{{artifact:STKH_REQ__DEPENDABILITY__ERROR_REACTION:status,safety-level,security}}}}

### Safe SW-platform state

{{artifact:STKH_REQ__DEPENDABILITY__SAFE_STATE:status,safety-level,security}}}}

### Error report timing

{{artifact:STKH_REQ__DEPENDABILITY__ERROR_REPORT_TIMING:status,safety-level,security}}}}

### No mixed ASIL

{{artifact:STKH_REQ__DEPENDABILITY__NO_MIXED_ASIL:status,safety-level,security}}}}

### Program Flow Monitoring

{{artifact:STKH_REQ__DEPENDABILITY__FLOW_MONITORING:status,safety-level,security}}}}

### Availability

{{artifact:STKH_REQ__DEPENDABILITY__AVAILABILITY:status,safety-level,security}}}}

### Security features

{{artifact:STKH_REQ__DEPENDABILITY__SECURITY_FEATURES:status,safety-level,security}}}}

## Application architectures

In modern software systems, the architectural design plays a critical role in determining how components interact, how they process
data, and how they manage workloads. Each architectural pattern is tailored to address specific challenges in terms of execution
model, resource consumption, communication strategy, and discovery. The three major architectures that we'll focus on — **Time-based
(Deterministic, Polling-based)**, **Data-driven (Event-driven, High-throughput)**, and **Request-driven (Asynchronous, Sporadic
interaction)** — each emphasize different operational priorities.

1. **Time-based Architecture (Deterministic, Polling-based):** Time-based architecture operates by triggering actions
   at fixed intervals, using scheduled polling to ensure consistent, predictable behavior. This architecture ensures
   high availability and deterministic execution, meaning that actions always happen at a predefined time, making it
   ideal for systems that require reliability. However, it can lead to inefficient CPU usage, as the system continues
   to poll even when no new data is available. The communication is synchronous and unidirectional, with the system
   staying up-to-date by polling for new information. Discovery is data-centric, meaning that the application focuses
   only on the data being communicated and not on the identity of the data source.

2. **Data-driven Architecture (Event-driven, High-throughput):** In a data-driven architecture, actions are triggered
   by events or data changes. The system optimizes for high throughput and performance, making it well-suited for
   applications where responsiveness to data is critical. The execution is non-deterministic, meaning that timing
   depends on when data arrives, which can lead to unpredictable bottlenecks, especially during data surges. The
   communication is unidirectional and driven by updates to data, decoupling the producers and consumers of the data.
   Discovery is data-centric, as applications react to events regardless of their origin, optimizing for low latency
   and dynamic scalability.

3. **Request-driven Architecture (Asynchronous, Sporadic interaction):** A request-driven architecture is triggered
   only when a request is made, making it ideal for applications that handle sporadic, unpredictable workloads. The
   system remains idle during inactivity, saving resources until a task is triggered. This model does not provide
   deterministic behavior, and response times depend on when requests arrive. Communication is bi-directional, with
   requests and responses flowing between client and server. Discovery is service-instance-centric, requiring knowledge
   of specific server instances, especially for stateful systems where session continuity or state preservation is
   crucial.

### Support for Time-based Architectures

{{artifact:STKH_REQ__APP_ARCHITECTURES__SUPPORT_TIME:status,safety-level,security}}}}

### Support for Data-driven Architecture

{{artifact:STKH_REQ__APP_ARCHITECTURES__SUPPORT_DATA:status,safety-level,security}}}}

### Support for Request-driven Architecture

{{artifact:STKH_REQ__APP_ARCHITECTURES__SUPPORT_REQUEST:status,safety-level,security}}}}

## Execution model

### Processes and thread management

{{artifact:STKH_REQ__EXECUTION_MODEL__PROCESSES:status,safety-level,security}}}}

### Short application cycles

{{artifact:STKH_REQ__EXECUTION_MODEL__SHORT_APP_CYCLES:status,safety-level,security}}}}

### Realtime capabilities

{{artifact:STKH_REQ__EXECUTION_MODEL__REALTIME_CAP:status,safety-level,security}}}}

### Startup performance

{{artifact:STKH_REQ__EXECUTION_MODEL__STARTUP_PERF:status,safety-level,security}}}}

### Low power mode

{{artifact:STKH_REQ__EXECUTION_MODEL__LOW_POWER:status,safety-level,security}}}}

## Communication

### Inter-process Communication

{{artifact:STKH_REQ__COMMUNICATION__INTER_PROCESS:status,safety-level,security}}}}

### ABI Compatible Data Types

{{artifact:STKH_REQ__COMMUNICATION__ABI_COMPATIBLE:status,safety-level,security}}}}

### Intra-process Communication

{{artifact:STKH_REQ__COMMUNICATION__INTRA_PROCESS:status,safety-level,security}}}}

### Stable application interfaces

{{artifact:STKH_REQ__COMMUNICATION__STABLE_APP_INTER:status,safety-level,security}}}}

### Extensible External Communication

{{artifact:STKH_REQ__COMMUNICATION__EXTENSIBLE_EXTERNAL:status,safety-level,security}}}}

### Safe Communication

{{artifact:STKH_REQ__COMMUNICATION__SAFE:status,safety-level,security}}}}

### Secure Communication

{{artifact:STKH_REQ__COMMUNICATION__SECURE:status,safety-level,security}}}}

### Supported network protocols

{{artifact:STKH_REQ__COMMUNICATION__SUPPORTED_NET:status,safety-level,security}}}}

### Quality of service

{{artifact:STKH_REQ__COMMUNICATION__SERVICE_QUALITY:status,safety-level,security}}}}

### Automotive diagnostics

{{artifact:STKH_REQ__COMMUNICATION__AUTO_DIAGNOSTICS:status,safety-level,security}}}}

## Time

### Vehicle Time base Synchronization

{{artifact:STKH_REQ__TIME__VEHICLE_TIME_SYNC:status,safety-level,security}}}}

### Vehicle Time base API

{{artifact:STKH_REQ__TIME__VEHICLE_TIME_API:status,safety-level,security}}}}

### Synchronize the HW clock with Vehicle Time

{{artifact:STKH_REQ__TIME__HW_CLOCK_SYNC:status,safety-level,security}}}}

### Time Synchronization with external sources

{{artifact:STKH_REQ__TIME__ABSOLUTE_TIME_SYNC:status,safety-level,security}}}}

### Absolute time base API

{{artifact:STKH_REQ__TIME__ABSOLUTE_TIME_API:status,safety-level,security}}}}

### Local High precision Clock API

{{artifact:STKH_REQ__TIME__HIGH_PRECISION_CLOCK_API:status,safety-level,security}}}}

### Local Monotonic Clock API

{{artifact:STKH_REQ__TIME__MONOTONIC_CLOCK_API:status,safety-level,security}}}}

## AI SW-platform

### On-board ML Workloads

{{artifact:STKH_REQ__AI_PLATFORM__ENABLEMENT:status,safety-level,security}}}}

### Support for Safety-Critical ML

{{artifact:STKH_REQ__AI_PLATFORM__SAFETY_CRITICAL:status,safety-level,security}}}}

### Runtime Efficiency for Edge Devices

{{artifact:STKH_REQ__AI_PLATFORM__RUNTIME_EFFICIENCY:status,safety-level,security}}}}

### Platform Portability (QNX + Linux)

{{artifact:STKH_REQ__AI_PLATFORM__PLATFORM_PORTABILITY:status,safety-level,security}}}}

### Secure Model Execution

{{artifact:STKH_REQ__AI_PLATFORM__MODEL_SECURITY:status,safety-level,security}}}}

### Deterministic Execution Paths

{{artifact:STKH_REQ__AI_PLATFORM__RUNTIME_DETERMINISM:status,safety-level,security}}}}

### On-board GenAI Workloads

{{artifact:STKH_REQ__GEN_AI__ENABLEMENT:status,safety-level,security}}}}

### GenAI User Interaction

{{artifact:STKH_REQ__GEN_AI__INTERACTION:status,safety-level,security}}}}

### Action Safety and Governance

{{artifact:STKH_REQ__GEN_AI__SAFETY_FILTER:status,safety-level,security}}}}

### Seamless Integration with Vehicle Systems

{{artifact:STKH_REQ__GEN_AI__VEHICLE_COM:status,safety-level,security}}}}

## Diagnostics and Fault Management

### Diagnostic via SOVD

{{artifact:STKH_REQ__DIAGNOSTICS__VIA_SOVD:status,safety-level,security}}}}

### Fault Reporting Infrastructure

{{artifact:STKH_REQ__DIAGNOSTICS__FAULT_REPORTING:status,safety-level,security}}}}

### Readout DTCs via SOVD

{{artifact:STKH_REQ__DIAGNOSTICS__DTC_READ_SOVD:status,safety-level,security}}}}

### Extensibility of Diagnostic Services

{{artifact:STKH_REQ__DIAGNOSTICS__CUSTOM_SERVICES:status,safety-level,security}}}}

### Compatibility with UDS Testers

{{artifact:STKH_REQ__DIAGNOSTICS__UDS_TESTER_COMPAT:status,safety-level,security}}}}

### Compatibility with UDS ECUs

{{artifact:STKH_REQ__DIAGNOSTICS__UDS_ECUS:status,safety-level,security}}}}

### Support for Distributed and Multi-ECU Diagnostics

{{artifact:STKH_REQ__DIAGNOSTICS__DISTRIBUTED_SUPPORT:status,safety-level,security}}}}

### Secure Access to Diagnostic Interfaces

{{artifact:STKH_REQ__DIAGNOSTICS__SECURE_ACCESS:status,safety-level,security}}}}

## Hardware support

### Chipset support for ARM64 and x64

{{artifact:STKH_REQ__HARDWARE_SUPPORT__CHIPSET_SUPPORT:status,safety-level,security}}}}

### Virtualization support for debug and testing

{{artifact:STKH_REQ__HARDWARE_SUPPORT__DEBUG_AND_TEST:status,safety-level,security}}}}

### Support of container technologies

{{artifact:STKH_REQ__HARDWARE_SUPPORT__CONTAINER_TECH:status,safety-level,security}}}}

## Developer experience

### IDL Support

{{artifact:STKH_REQ__DEV_EXPERIENCE__IDL_SUPPORT:status,safety-level,security}}}}

### Developer experience and development toolchain

{{artifact:STKH_REQ__DEV_EXPERIENCE__DEV_TOOLCHAIN:status,safety-level,security}}}}

### Performance analysis

{{artifact:STKH_REQ__DEV_EXPERIENCE__PERF_ANALYSIS:status,safety-level,security}}}}

### Tracing of execution

{{artifact:STKH_REQ__DEV_EXPERIENCE__TRACING_OF_EXEC:status,safety-level,security}}}}

### Tracing of communication

{{artifact:STKH_REQ__DEV_EXPERIENCE__TRACING_OF_COMM:status,safety-level,security}}}}

### Tracing of memory access

{{artifact:STKH_REQ__DEV_EXPERIENCE__TRACING_OF_MEMORY:status,safety-level,security}}}}

### Timing analysis

{{artifact:STKH_REQ__DEV_EXPERIENCE__TIMING_ANALYSIS:status,safety-level,security}}}}

### Debugging

{{artifact:STKH_REQ__DEV_EXPERIENCE__DEBUGGING:status,safety-level,security}}}}

### Mockup implementation for application testing

{{artifact:STKH_REQ__DEV_EXPERIENCE__MOCKUP_PUBLIC_APIS:status,safety-level,security}}}}

### Programming languages for application development

{{artifact:STKH_REQ__DEV_EXPERIENCE__PROG_LANGUAGES:status,safety-level,security}}}}

### Reprocessing and simulation support

{{artifact:STKH_REQ__DEV_EXPERIENCE__REPROCESSING:status,safety-level,security}}}}

### Logging support

{{artifact:STKH_REQ__DEV_EXPERIENCE__LOGGING_SUPPORT:status,safety-level,security}}}}

### Previous boot logging

{{artifact:STKH_REQ__DEV_EXPERIENCE__BOOT_LOGGING:status,safety-level,security}}}}

## Integration

### Multirepo integration

{{artifact:STKH_REQ__INTEGRATION__MULTI_REPO:status,safety-level,security}}}}

## Quality

### Document assumptions and design decisions

{{artifact:STKH_REQ__QUALITY__ASSUMPTIONS_AND_DD:status,safety-level,security}}}}

## Requirements Engineering

### Requirements traceability

{{artifact:STKH_REQ__RE_REQUIREMENTS__TRACEABILITY:status,safety-level,security}}}}

### Document requirements as code

{{artifact:STKH_REQ__REQUIREMENTS__AS_CODE:status,safety-level,security}}}}

## Safety Mechanisms

The following stakeholder requirements describe the assumed safety mechanisms which are needed due to complexity of the realizing
SW element(s) or due to dependency on HW. This is confirmed during safety analysis of the derived feature requirements and architecture.

