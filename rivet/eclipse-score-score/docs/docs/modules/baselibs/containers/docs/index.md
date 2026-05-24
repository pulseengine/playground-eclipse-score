---
id: DOC-INDEX-23240
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# containers

### Containers Library

{{artifact:DOC__CONTAINERS:status,safety-level,security}}

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

This component request proposes the integration of a safe Containers library for common data structures like dynamic arrays and linked lists.

# Motivation and Rationale

The Containers library shall provide safe and efficient implementations of common data structures, such as dynamic arrays and linked lists.
Containers library shall enable developers to manage collections of data in a type-safe manner, reducing the risk of runtime errors and improving code quality.
A Containers library with type-safe data structures is needed in the S-CORE software platform due to the frequent use of collections in various features and the need for reliable data management.
There are multiple use-cases like managing lists of sensor readings, storing configuration parameters, or handling dynamic data sets.

# Specification

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

## General considerations

The Containers library should provide type-safe data structures and efficient memory management capabilities:

* [[COMP_REQ__CONTAINERS__DYNAMIC_ARRAY]]
* [[COMP_REQ__CONTAINERS__INTRUSIVE_LIST]]
* [[COMP_REQ__CONTAINERS__TYPE_SAFETY]]
* [[COMP_REQ__CONTAINERS__DETERMINISTIC_BEHAVIOR]]

The component should be extensible in the future to support additional data structures and algorithms as needed.
