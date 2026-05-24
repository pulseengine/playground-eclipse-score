---
id: DOC-INDEX-48845
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# filesystem

### Filesystem Library

{{artifact:DOC__FILESYSTEM:status,safety-level,security}}

.. toctree::
   :hidden:

   requirements/index.rst
   requirements/chklst_req_inspection.rst
   architecture/index.rst
   architecture/chklst_arc_inspection.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst
   detailed_design/chklst_impl_inspection.rst

# Abstract

The Filesystem Library provides a set of APIs for file and directory manipulation, including creation, deletion, and traversal of the filesystem. It aims to offer a consistent and safe interface for filesystem operations across different platforms.

# Motivation and Rationale

The Filesystem Library is essential for applications that require interaction with the underlying filesystem. It provides a standardized way to perform file operations, ensuring safety and reliability.
The library is designed to handle various filesystem tasks while adhering to safety standards required for critical systems.

# Specification

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

## General considerations

The Filesystem Library should provide robust and safe APIs for filesystem operations:

* [[COMP_REQ__FILESYSTEM__API_ABSTRACTION]]
* [[COMP_REQ__FILESYSTEM__PATH_UTILITIES]]
* [[COMP_REQ__FILESYSTEM__DIRECTORY_ITERATORS]]
* [[COMP_REQ__FILESYSTEM__FILE_IO]]
* [[COMP_REQ__FILESYSTEM__FULL_TESTABILITY]]
* [[COMP_REQ__FILESYSTEM__FILE_UTILS]]
* [[COMP_REQ__FILESYSTEM__MOCK_FAKE]]

The library should ensure that all filesystem operations are performed safely, with appropriate error handling and resource management to prevent leaks and ensure system stability.
