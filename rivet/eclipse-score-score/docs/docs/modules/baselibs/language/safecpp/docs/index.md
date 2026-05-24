---
id: DOC-INDEX-11861
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# safecpp

### Safecpp Library

{{artifact:DOC__SAFECPP:status,safety-level,security}}}}

.. toctree::
   :hidden:

   architecture/index.rst
   architecture/chklst_arc_inspection.rst
   requirements/index.rst
   requirements/chklst_req_inspection.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst
   detailed_design/chklst_impl_inspection.rst

# Abstract

SafeCPP is a collection of utilities that helps developers write safer C++ code.

# Motivation and Rationale

The C++ standard library targets general-purpose software and often lacks the stricter semantics needed in safety-critical code. SafeCPP fills these gaps with small, opt-in utilities that make failure modes explicit and are easy to adopt incrementally.

Following components are provided by SafeCPP:

- **aborts_upon_exception**: Globally replaces C++ exception handling with ``std::abort()`` calls for safety compliance.
- **coverage_termination_handler**: Ensures coverage data is preserved in GoogleTest death tests.
- **safe_atomics**: Prevents overflow when adding numbers to atomic variables (thread-safe addition with `TryAtomicAdd`).
- **safe_math**: Provides overflow-safe arithmetic operations for integral and floating-point types.
- **scoped_function**: Offers controlled callable execution with explicit lifetime guarantees.
- **string_view**: Provides null-terminated string view types and safety utilities for secure string handling.
