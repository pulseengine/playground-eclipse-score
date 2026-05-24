---
id: DOC-INDEX-63365
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Requirements

### Operating System Requirements

{{artifact:DOC__OS_REQUIREMENTS:status,safety-level,security}}

Generally the OS (as an external SW element) is expected by the S-CORE project to fulfill the following requirements,
defined in the SW-platform assumptions (and partly even in the Stakeholder requirements).

The system integrator integrating S-CORE with the OS to provide a safe product has to make sure

- the functional requirements below are matching the OS used - see also [[AOU_REQ__PLATFORM__SAFETY_MATCHING]]
- the non-functional (integration) requirements below are fulfilled by the OS supplier - see also integration_assumptions

# Integration Requirements

## Community Level

- [[AOU_REQ__PLATFORM__INTEGRATION_ASSISTANCE]]
- [[AOU_REQ__PLATFORM__OS_INTEGRATION_MANUAL]]
- [[AOU_REQ__PLATFORM__BUG_INTERFACE]]

## Functional Level

- [[AOU_REQ__PLATFORM__BAZEL_TOOLING]]
- [[AOU_REQ__PLATFORM__BUG_FIXING]]

## Certifiable Level

- [[AOU_REQ__PLATFORM__LEVELS]]
- [[AOU_REQ__PLATFORM__SAFETY_AOU]]
- [[AOU_REQ__PLATFORM__SAFETY_FUNCTIONS]]
- [[AOU_REQ__PLATFORM__SAFETY_ANOMALY]]

# OS Specific Functional Requirements

- [[AOU_REQ__PLATFORM__PROCESS_ISOLATION]]
- [[AOU_REQ__PLATFORM__OS_SAFETY_FUNCTIONS]]
- [[AOU_REQ__PLATFORM__POSIX_OPERATING_SYSTEM]]
