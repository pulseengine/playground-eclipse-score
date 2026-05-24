---
id: DOC-INDEX-58149
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _comp_doc_memory_shared:

# memory

### Memory Library

{{artifact:DOC__MEMORY:status,safety-level,security}}

.. toctree::
   :hidden:

   architecture/index
   requirements/index.rst

# Abstract

The Memory library provides APIs for memory management to facilitate inter-process communication (IPC) in the S-CORE software platform.

# Motivation and Rationale

The Memory library shall provide mechanisms for creating, accessing, and managing shared memory between different processes.
It includes support for polymorphic memory resource allocators using offset pointers and additional utilities to deal with memory use-cases.

The Memory library is needed in the S-CORE software platform because subsystems like Communication and Logging rely on shared memory for inter-process communication.

# Specification

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

## General considerations

The Memory Library should provide APIs for memory management:

* [[COMP_REQ__MEMORY__SHARED_MEMORY]]
* [[COMP_REQ__MEMORY__OFFSET_PTR]]
* [[COMP_REQ__MEMORY__SHARED_CONTAINER]]
* [[COMP_REQ__MEMORY__INTER_PROCESS_SYNC]]
* [[COMP_REQ__MEMORY__BOUNDS_CHECK]]
* [[COMP_REQ__MEMORY__ENDIANNESS]]
* [[COMP_REQ__MEMORY__SEALED_SHM]]
* [[COMP_REQ__MEMORY__TYPED_MEMORY]]
* [[COMP_REQ__MEMORY__RESOURCE_REGISTRY]]
* [[COMP_REQ__MEMORY__STRING_UTILS]]
* [[COMP_REQ__MEMORY__ATOMIC_OPS]]

The library should ensure that all memory operations are performed safely, with appropriate bounds checking and synchronization mechanisms to prevent memory corruption.
