---
id: DOC-INDEX-8756
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# bitmanipulation

### Bit Manipulation Library

{{artifact:DOC__BITMANIPULATION:status,safety-level,security}}

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

This component request proposes the integration of a safe Bit Manipulation library for constexpr bit operations and byte manipulation. It integrates a type-safe Bitmask Operator library.

# Motivation and Rationale

The Bit Manipulation library provides a type-safe mechanism to perform bitwise operations on integral types.
It enables safe and efficient bit operations and supports the development of safety-critical features by offering clear and reliable bit manipulation capabilities.
A Bit Manipulation library with constexpr operations is required in the S-CORE software platform to enable efficient, compile-time bit operations for embedded and automotive applications.
Typical use cases include setting control flags, extracting byte data from raw integers, and performing low-level bit operations with compile-time guarantees.
It integrates a type-safe Bitmask Operator library that extends enum class types to support standard bitmask operations ('|', '&', '^', '~', and their assignment forms).

# Specification

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

## General considerations

The Bit Manipulation library should provide bit operation and byte extraction capabilities:

* [[COMP_REQ__BITMANIPULATION__BIT_OPERATIONS]]
* [[COMP_REQ__BITMANIPULATION__BYTE_OPERATIONS]]
* [[COMP_REQ__BITMANIPULATION__BITMASK_OPERATORS]]
* [[COMP_REQ__BITMANIPULATION__BOUNDS_SAFETY]]
* [[COMP_REQ__BITMANIPULATION__HEADER_ONLY]]

The component should be extensible in the future to support richer error information and integration with other platform components.
