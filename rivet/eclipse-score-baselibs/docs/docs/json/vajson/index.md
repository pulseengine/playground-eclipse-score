---
id: DOC-INDEX-46218
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# VaJson

### vajson

{{artifact:DOC__VAJSON:status,safety-level,security}}}}

# Abstract

This component request proposes adding VaJson as a JSON parser backend for Eclipse S-CORE.

This component request describes a JSON parser to be used within applications of the Eclipse S-CORE project.

This requests adds VaJson, a SAX-based JSON parser for Eclipse S-CORE applications that enables parsing of JSON data for configuration and data exchange.

# Motivation

VaJson provides a safety-qualified JSON parser designed for automotive environments.
It has passed Vector's internal ASIL D qualification process and comes with supporting safety artifacts.

Artifacts such as the safety manual, safety analysis, cybersecurity analysis, and detailed design significantly reduce the effort needed to adapt the component to S-CORE qualification processes.
Its API follows established automotive patterns, which improves integration consistency and reduces project risk.

# Rationale

VaJson was selected because it already has ASIL D qualification evidence (within Vector processes) and includes safety and cybersecurity artifacts.
This reduces the effort to satisfy S-CORE internal process requirements.

The SAX-based design is efficient for embedded systems and avoids the memory overhead of fully materialized document models.

Its API style is familiar in automotive projects, making adoption easier and less risky than introducing a new or generic parser.

# Specification

VaJson meets the generic requirements for a JSON deserialization library.

* [[COMP_REQ__JSON__DESERIALIZATION]]
* [[COMP_REQ__JSON__USER_FORMAT]]

In addition, VaJson satisfies the extended requirements defined in [[DOC__VAJSON_REQUIREMENTS]]:

* [[COMP_REQ__VAJSON__VALIDATION]]
* [[COMP_REQ__VAJSON__TRAILING_COMMAS]]
* [[COMP_REQ__VAJSON__HEX_INTEGERS]]
* [[COMP_REQ__VAJSON__UNICODE]]

# Backward Compatibility

VaJson is integrated as an optional backend through the existing S-CORE JSON wrapper.
Users can select the JSON backend (for example, VaJson or nlohmann), so existing functionality remains backward compatible.

# Security Impact

Potential security concerns and mitigations for VaJson:

- Malformed JSON Attacks

  Threat: Supplying intentionally malformed or deeply nested JSON to cause excessive CPU or memory consumption.
  Mitigation: Handled by design in VaJson. The SAX-based streaming parser detects malformed input during parsing and stops processing invalid data early.

- Schema Abuse

  Threat: Using oversized keys/values or unexpected schema elements to bypass validation or trigger buffer overflows.
  Mitigation: Handled by design in VaJson. Input size and structure are validated during parsing.

# Safety Impact

A full safety analysis for VaJson exists in an external format and addresses all identified concerns with appropriate measures.
Example:

FM-VaJson-NumberConversion

Details: Number conversion from textual JSON representation to a numerical value could change the value.
Effect: Incorrect numerical values may violate safety requirements.
Measure: Use only well-known standard library functions for number conversion, verified through unit testing.

All concerns listed in the external safety analysis have been implemented and verified in the source code and tests.

**Expected ASIL Level:**

ASIL B.

**Classification:**

Safety-relevant component.

**Safety Related Functionality Required From Other Components**

The Assumptions of Use which apply to the JSON modules public interface also apply to VaJson:

* [[AOU_REQ__JSON__DATA_INTEGRITY]]
* [[AOU_REQ__JSON__ACCESS_CONTROL]]

# License Impact

None. VaJson was previously released under a commercial license, but is now open sourced under the Apache License Version 2.0.

# How to Teach This

- Update baselibs/README.md

  Clearly document the available JSON parser configuration options.
  This component introduces an additional backend, so users must understand the selectable configurations.

# Rejected Ideas

None.

# Open Issues

- S-CORE process compliance and Vector's role

  The task of adapting the new component to be S-CORE-process-compliant is currently unassigned.
  Vector will not create the required S-CORE process documentation (for example, safety and security analysis).

# Footnotes

.. toctree::

   architecture/index.rst
   requirements/index.rst
