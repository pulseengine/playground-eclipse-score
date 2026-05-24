---
id: DOC-INDEX-37727
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# result

### Result Library

{{artifact:DOC__RESULT:status,safety-level,security}}

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

This component request proposes the integration of a safe Result library for type-safe error handling and value propagation.

# Motivation and Rationale

The Result library shall provide a type-safe mechanism to represent and propagate either a successful value or an error.
Result library will enable explicit error management and support the development of safety-critical features by providing clear value or error propagation paths.
A Result library with type-safe error handling is needed in the S-CORE software platform due to functional dependencies of different features and the need for explicit, reliable error propagation.
There are multiple use-case like logging error messages or comparing on expected error states to trigger other countermeasures.

# Specification

The following details and requirements describe the aspects of the current feature in the context of S-CORE.

## General considerations

The Result library should provide value/error propagation and error handling capabilities:

* [[COMP_REQ__RESULT__ERROR_HANDLING]]
* [[COMP_REQ__RESULT__DOMAIN_ERROR_INFORMATION]]
* [[COMP_REQ__RESULT__TYPE_SAFETY]]
* [[COMP_REQ__RESULT__STD_INTEGRATION]]
* [[COMP_REQ__RESULT__DETERMINISTIC_BEHAVIOR]]
* [[COMP_REQ__RESULT__EXCEPTION_FREE_OPERATION]]

The component should be extensible in the future to support richer error information and integration with other platform components.
