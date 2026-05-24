---
id: DOC-INDEX-77344
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _platform_assumptions:

# SW-platform Assumptions

### SW-platform Assumptions

{{artifact:DOC__PLATFORM_ASSUMPTIONS:status,safety-level,security}}

## Assumptions on Environment

In this section assumptions are described which need to be fulfilled by the architecture level below the SW-platform,
i.e. by the elements or organizations outside of S-CORE, but used by S-CORE platform components. These include elements like
the operating system, programming language libraries, hypervisor or processing hardware.
For "organizations" two roles are used in the AoU text:

- Supplier: is the provider of an element the S-CORE SW-platform is using but which is developed and maintained externally.
- System Integrator: uses the S-CORE SW-platform as a part of a system they provide to a customer. The system integrator can be for example a Tier1 providing an electronic control unit to a OEM or an OEM providing a car to their end-customer. S-CORE does not know which.

To fulfill these assumptions is the responsibility of the mentioned roles.

Note that the "supplier" AoUs were created with an OS supplier in mind but are really general AoUs for any external SW element S-CORE uses.

### POSIX Operating System

{{artifact:AOU_REQ__PLATFORM__POSIX_OPERATING_SYSTEM:status,safety-level,security}}

.. _integration_assumptions:

## Assumptions on the external SW element integration

#### Community Level

This is the lowest level of integration, the higher levels will build on this.
It also contains expectations towards an supplier which can be used as criteria for supplier selection
by the system integrator. Building and running of external SW element is enabled, but no pro-active support from S-CORE
is provided for e.g. build or test problems. No guarantees that S-CORE builds or runs with the external SW element.

### Integration assistance

{{artifact:AOU_REQ__PLATFORM__INTEGRATION_ASSISTANCE:status,safety-level,security}}

### Integration manual

{{artifact:AOU_REQ__PLATFORM__OS_INTEGRATION_MANUAL:status,safety-level,security}}

### Bug interface

{{artifact:AOU_REQ__PLATFORM__BUG_INTERFACE:status,safety-level,security}}

There are no AoUs on the system integrator on this level,
as this level is not expected sufficient for a product release, only for incubation/prototype.

#### Functional Level

This is the middle level of integration, the higher level will build on this.
It is the level where the S-CORE SW-platform will functionally "work" with the external SW element.

### Bazel tooling

{{artifact:AOU_REQ__PLATFORM__BAZEL_TOOLING:status,safety-level,security}}

### Bug fixing

{{artifact:AOU_REQ__PLATFORM__BUG_FIXING:status,safety-level,security}}

### SW-platform testing

{{artifact:AOU_REQ__PLATFORM__TESTING:status,safety-level,security}}

### SW-platform integration bug reporting

{{artifact:AOU_REQ__PLATFORM__BUG_REPORT:status,safety-level,security}}

#### Certifiable Level

This is the highest level of integration. This is the level where the S-CORE SW-platform will be certifiable with an external SW element.

### Integration levels

{{artifact:AOU_REQ__PLATFORM__LEVELS:status,safety-level,security}}

### Safety AoU

{{artifact:AOU_REQ__PLATFORM__SAFETY_AOU:status,safety-level,security}}

### Safety functions

{{artifact:AOU_REQ__PLATFORM__SAFETY_FUNCTIONS:status,safety-level,security}}

### Safety anomaly reporting

{{artifact:AOU_REQ__PLATFORM__SAFETY_ANOMALY:status,safety-level,security}}

### Safety matching

{{artifact:AOU_REQ__PLATFORM__SAFETY_MATCHING:status,safety-level,security}}

### Safety integration

{{artifact:AOU_REQ__PLATFORM__SAFETY_INTEGRATION:status,safety-level,security}}

### SW-platform test completion

{{artifact:AOU_REQ__PLATFORM__TEST_COMPLETION:status,safety-level,security}}

### Integrator safety anomaly reporting

{{artifact:AOU_REQ__PLATFORM__INTEGRATION_SAFETY_ANOMALY:status,safety-level,security}}

## Assumptions on Applications

In this section assumptions are described which need to be fulfilled by the applications running on top of the SW-platform.

### Avoidance of Exceptions

{{artifact:AOU_REQ__PLATFORM__NO_EXCEPTIONS:status,safety-level,security}}

### Avoidance of heap allocations after initialization

{{artifact:AOU_REQ__PLATFORM__NO_HEAP_ALLOC_AFTER_INIT:status,safety-level,security}}

### Error Reaction

{{artifact:AOU_REQ__PLATFORM__ERROR_REACTION:status,safety-level,security}}

### No mixed ASIL

{{artifact:AOU_REQ__PLATFORM__NO_MIXED_ASIL:status,safety-level,security}}

### Program Flow Monitoring

{{artifact:AOU_REQ__PLATFORM__FLOW_MONITORING:status,safety-level,security}}

## Assumptions on Safety System

In this section assumptions are described which need to be fulfilled by the system or system integrator.

### Safe HW platform

{{artifact:AOU_REQ__PLATFORM__HARDWARE_SAFETY:status,safety-level,security}}

### External Health Management

{{artifact:AOU_REQ__PLATFORM__EXTERNAL_HEALTH_MANAGEMENT:status,safety-level,security}}

### Process Isolation

{{artifact:AOU_REQ__PLATFORM__PROCESS_ISOLATION:status,safety-level,security}}

### OS safety functions

{{artifact:AOU_REQ__PLATFORM__OS_SAFETY_FUNCTIONS:status,safety-level,security}}

