---
id: DOC-INDEX-51126
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _baselibs_architecture:

# Architecture

### Baselibs Architecture

{{artifact:DOC__BASELIBS_ARCHITECTURE:status,safety-level,security}}}}

## Overview

A brief overview of Baselibs is described baselibs_feature.

## Description

A detailed description of the Baselibs module requirements is located [[FEAT_REQ__BASELIBS__CORE_UTILITIES]].

The Baselibs module provides foundational software utilities, safety mechanisms and robust infrastructure components. It comprises essential libraries organized into functional categories:

**Core Utility Libraries**

- **bitmanipulation**: Utilities for bit manipulation operations
- **containers**: Specialized container implementations including ``DynamicArray`` and intrusive linked lists
- **utils**: Reusable utilities including type traits, mathematical utilities and string manipulation helpers

**Threading and Concurrency**

- **concurrency**: Interface for parallel execution of C++ callables with thread pool management

**Data Processing and Serialization**

- **json**: JSON abstraction layer with pluggable backend support
- **static_reflection_with_serialization**: Binary serialization/deserialization with compile-time type reflection

**File System and I/O Operations**

- **filesystem**: Filesystem manipulation library similar to ``std::filesystem``

**Memory Management**

- **memory**: Memory handling utilities for safety-critical applications with shared memory support

**Operating System Abstraction**

- **os**: OS Abstraction Layer (OSAL) for POSIX-like systems including Linux and QNX

**Error Handling and Safety**

- **result**: Error handling without exceptions, conforming to C++23 ``std::expected`` specification
- **safecpp**: Safety framework including exception prevention and overflow-safe implementations

**Modern C++ Extensions and Logging**

- **futurecpp**: C++14 Standard Library extensions with backported components
- **mw::log**: Logging library for automotive systems with structured logging and multiple backends

These libraries form an integrated ecosystem designed for code reuse, consistency and safety throughout the platform.

# Rationale Behind Architecture Decomposition

The decomposition of Baselibs into modular libraries is motivated by the need for code reuse, maintainability and consistent APIs across the platform. This approach enables platform modules to leverage common infrastructure, reduces duplication and supports safety and security requirements.

## Static Architecture

### Baselibs

{{artifact:FEAT__BASELIBS:status,safety-level,security}}}}

### Baselibs Static View

{{artifact:FEAT_ARC_STA__BASELIBS__STATIC_VIEW_ARCH:status,safety-level,security}}}}

### Baselibs Dynamic View

{{artifact:FEAT_ARC_DYN__BASELIBS__DYNAMIC_VIEW_ARCH:status,safety-level,security}}}}

## Logical Interfaces

The Baselibs feature exposes the following logical interfaces:

.. needtable::
   :style: table
   :columns: title;id;status
   :sort: title
   :filter: id in ['logic_arc_int__baselibs__json', 'logic_arc_int__baselibs__memory_shared', 'logic_arc_int__baselibs__result', 'logic_arc_int__baselibs__bit_manipulation', 'logic_arc_int__baselibs__bit_mask_operator', 'logic_arc_int__baselibs__dynamic_array', 'logic_arc_int__baselibs__intrusive_list', 'logic_arc_int__baselibs__filesystem', 'logic_arc_int__baselibs__utils_base64', 'logic_arc_int__baselibs__utils_scoped_op', 'logic_arc_int__baselibs__promise', 'logic_arc_int__baselibs__future', 'logic_arc_int__baselibs__shared_future', 'logic_arc_int__baselibs__executor', 'logic_arc_int__baselibs__task', 'logic_arc_int__baselibs__task_result', 'logic_arc_int__baselibs__synchronized_queue', 'logic_arc_int__baselibs__condition_variable', 'logic_arc_int__safecpp__aborts_upon_ex', 'logic_arc_int__safecpp__coverage_termination', 'logic_arc_int__baselibs__safemath', 'logic_arc_int__baselibs__safeatomics', 'logic_arc_int__baselibs__scoped_function', 'logic_arc_int__baselibs__string_view']
