---
id: DOC-INDEX-36547
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_detailed_design_hm:

# Detailed Design

### HealthMonitor Detailed Design

{{artifact:DOC__HEALTH_MONITOR_DETAILED_DESIGN:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Component.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and followed by ``_detailed_design``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

# Detailed Design for Component: HealthMonitor

## Description

HealthMonitor component consists of these units:

- `deadline_monitor`
- `logic_monitor`
- `health_monitor`

| Design Decisions - For the documentation of the decision the [[GD_TEMP__CHANGE_DECISION_RECORD]] can be used.
| Design Constraints

## Implementation structure

.. code-block:: bash

    src
    └── health_monitoring_lib
        ├── cpp             # C++ API using Rust FFI
        │   ├── include     # C++ public header files.
        │   │   └── ...
        │   └── tests
        └── rust            # Rust implementation + FFI for C++
            └── deadline

# Implementation approach for multi language

The implementation is done primarily in `Rust` language to leverage its memory safety features and concurrency model.
Due to a need to interface with existing C++ codebases, a C-compatible Foreign Function Interface (FFI) is provided by this `Rust` implementation.
`C++` API is designed to be idiomatic wrapping around the `Rust` FFI, ensuring ease of use for C++ developers while maintaining the safe usage.

# Rationale Behind Decomposition into Units

| mandatory: a motivation for the decomposition into one or more units.

## Static Diagrams for Unit Interactions

### Class Diagram

{{artifact:DD_STA__HEALTH_MONITOR__CLASS_DIAGRAM:status,safety-level,security}}

## Dynamic Diagrams for Unit Interactions

.. code-block:: rst

### <Title>

{{artifact:DD_DYN__<FEATURE>__<TITLE>:status,safety-level,security}}

