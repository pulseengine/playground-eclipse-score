---
id: DOC-REQUIREMENTS-3107
title: Requirements
type: specification
status: approved
tags: [eclipse-score]
---

.. _docs_tool_requirements:

=================================
# Tool Requirements

# 📈 Status

This section provides an overview of current process requirements and their clarification & implementation status.

.. note::
  All open issues and pull requests in the process repository are considered as if they
  are already part of the process requirements. They address a lot of the
  requirements that are referenced in this document, so we would be blocked if we would
  not consider them as part of the process requirements.

# 🗂️ Common Attributes

.. note::
  To stay consistent with sphinx-needs (the tool behind docs-as-code), we'll use `need`
  for any kind of model element like a requirement, an architecture element or a
  feature description.

----------------------
## 🔢 ID

### Enforces need ID uniqueness

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_ID:status,safety-level,security}}

### Enforces need ID scheme

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_ID_SCHEME:status,safety-level,security}}

----------------------
## 🏷️ Title

### Enforces title wording rules

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_TITLE:status,safety-level,security}}

---------------------------
## 📝 Description

### Enforces presence of description

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_DESCRIPTION:status,safety-level,security}}

### Enforces description wording rules

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_DESC_WORDING:status,safety-level,security}}

----------------------------
## 🔒 Security Classification

### Security: enforce classification

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_SECURITY:status,safety-level,security}}

---------------------------
## 🛡️ Safety Classification

### Safety: enforce classification

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_SAFETY:status,safety-level,security}}

----------
## 🚦 Status

### Status: enforce attribute

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_STATUS:status,safety-level,security}}

----------
## Versioning

### Versioning: enforce attribute

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_VERSION:status,safety-level,security}}

### Suspicious: Enforce attribute

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_SUSPICIOUS:status,safety-level,security}}

# 📚 Documents

### Document Types

{{artifact:TOOL_REQ__DOCS_DOC_TYPES:status,safety-level,security}}

### Mandatory attributes of Generic Documents

{{artifact:TOOL_REQ__DOCS_DOC_GENERIC_MANDATORY:status,safety-level,security}}

### Mandatory Document attributes

{{artifact:TOOL_REQ__DOCS_DOC_ATTR:status,safety-level,security}}

### Document author is autofilled

{{artifact:TOOL_REQ__DOCS_DOC_ATTR_AUTHOR_AUTOFILL:status,safety-level,security}}

### Document approver is autofilled

{{artifact:TOOL_REQ__DOCS_DOC_ATTR_APPROVER_AUTOFILL:status,safety-level,security}}

### Document reviewer is autofilled

{{artifact:TOOL_REQ__DOCS_DOC_ATTR_REVIEWER_AUTOFILL:status,safety-level,security}}

--------
## Mapping

.. needtable::
   :style: table
   :types: gd_req
   :columns: id;satisfies_back as "tool_req"
   :filter: "gd_req__doc" in id

# 📋 Requirements

-------------------------
## 🔢 Requirement Types

### Requirements Types

{{artifact:TOOL_REQ__DOCS_REQ_TYPES:status,safety-level,security}}

-------------------------
## 🏷️ Attributes

### Enforces rationale attribute

{{artifact:TOOL_REQ__DOCS_REQ_ATTR_RATIONALE:status,safety-level,security}}

### Enforces requirement type classification

{{artifact:TOOL_REQ__DOCS_REQ_ATTR_REQTYPE:status,safety-level,security}}

### Enables marking requirements as "covered"

{{artifact:TOOL_REQ__DOCS_REQ_ATTR_REQCOV:status,safety-level,security}}

### Support requirements test coverage

{{artifact:TOOL_REQ__DOCS_REQ_ATTR_TESTCOV:status,safety-level,security}}

### Enforce validity attribute correctness

{{artifact:TOOL_REQ__DOCS_REQ_ATTR_VALIDITY_CORRECTNESS:status,safety-level,security}}

### Enforce validity start is before end

{{artifact:TOOL_REQ__DOCS_REQ_ATTR_VALIDITY_CONSISTENCY:status,safety-level,security}}

-------------------------
## 🔗 Links

### Enables needs linking via satisfies attribute

{{artifact:TOOL_REQ__DOCS_REQ_LINK_SATISFIES_ALLOWED:status,safety-level,security}}

### Safety: enforce safe linking

{{artifact:TOOL_REQ__DOCS_COMMON_ATTR_SAFETY_LINK_CHECK:status,safety-level,security}}

### Requirement linkage to AoU via covers

{{artifact:TOOL_REQ__DOCS_REQ_LINK_COVERS_AOU:status,safety-level,security}}

# 🏛️ Architecture

----------------------
## 🔢 Architecture Types

### Architecture Types

{{artifact:TOOL_REQ__DOCS_ARCH_TYPES:status,safety-level,security}}

--------------------------
## Architecture Attributes

### Architecture Mandatory Attributes

{{artifact:TOOL_REQ__DOCS_ARCH_ATTR_MANDATORY:status,safety-level,security}}

------------------------
## 🔗 Linkage

### Mandatory Architecture Attribute: fulfils

{{artifact:TOOL_REQ__DOCS_ARCH_LINK_FULFILS:status,safety-level,security}}

### Architecture fulfils linkage to AoU

{{artifact:TOOL_REQ__DOCS_ARCH_LINK_FULFILS_AOU:status,safety-level,security}}

### Check Architecture linkage to AoU

{{artifact:TOOL_REQ__DOCS_ARCH_LINK_AOU_CHECK:status,safety-level,security}}

### Ensure safety architecture elements link a safety requirement

{{artifact:TOOL_REQ__DOCS_ARCH_LINK_SAFETY_TO_REQ:status,safety-level,security}}

### Ensure qm architecture elements do not fulfill safety requirements

{{artifact:TOOL_REQ__DOCS_ARCH_LINK_QM_TO_SAFETY_REQ:status,safety-level,security}}

### Restrict links for safety requirements

{{artifact:TOOL_REQ__DOCS_REQ_ARCH_LINK_SAFETY_TO_ARCH:status,safety-level,security}}

### Security: Restrict linkage

{{artifact:TOOL_REQ__DOCS_ARCH_LINK_SECURITY:status,safety-level,security}}

----------------------
## 🖼️ Diagram Related

### Support Diagram drawing of architecture

{{artifact:TOOL_REQ__DOCS_ARCH_VIEWS:status,safety-level,security}}

# 💻 Detailed Design & Code

----------------
## 🔗 Code Linkage

### Supports linking to source code

{{artifact:TOOL_REQ__DOCS_DD_LINK_SOURCE_CODE_LINK:status,safety-level,security}}

### Feature Flags

{{artifact:TOOL_REQ__DOCS_DD_FEATURE_FLAG:status,safety-level,security}}

### Static Diagram for Unit Interactions

{{artifact:TOOL_REQ__DOCS_DD_STA:status,safety-level,security}}

.. .. tool_req:: Dynamic Diagram for Unit Interactions
# Testing

### Supports linking to test cases

{{artifact:TOOL_REQ__DOCS_TEST_LINK_TESTCASE:status,safety-level,security}}

### Extract Metadata from Tests

{{artifact:TOOL_REQ__DOCS_TEST_METADATA_MANDATORY_1:status,safety-level,security}}

### Extract Metadata from Tests

{{artifact:TOOL_REQ__DOCS_TEST_METADATA_MANDATORY_2:status,safety-level,security}}

### Extract Metadata from Tests

{{artifact:TOOL_REQ__DOCS_TEST_METADATA_LINK_LEVELS:status,safety-level,security}}

# 🧪 Tool Verification Reports

### Enforce safety classification

{{artifact:TOOL_REQ__DOCS_TVR_SAFETY:status,safety-level,security}}

### Enforce security classification

{{artifact:TOOL_REQ__DOCS_TVR_SECURITY:status,safety-level,security}}

### Enforce status classification

{{artifact:TOOL_REQ__DOCS_TVR_STATUS:status,safety-level,security}}

### Enforce version attribute

{{artifact:TOOL_REQ__DOCS_TVR_VERSION:status,safety-level,security}}

### Enforce confidence level classification

{{artifact:TOOL_REQ__DOCS_TVR_CONFIDENCE_LEVEL:status,safety-level,security}}

# ⚙️ Process / Other

### Workflow Types

{{artifact:TOOL_REQ__DOCS_WF_TYPES:status,safety-level,security}}

### Standard Requirement Types

{{artifact:TOOL_REQ__DOCS_STDREQ_TYPES:status,safety-level,security}}

# 🛡️ Safety Analysis (DFA + FMEA)

### Safety Analysis Need Types

{{artifact:TOOL_REQ__DOCS_SAF_TYPES:status,safety-level,security}}

### Safety Analysis Mandatory Attributes

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_MANDATORY:status,safety-level,security}}

### Safety Analysis Mitigation Attribute

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_MITIGATED_BY:status,safety-level,security}}

### Safety Analysis Mitigation Issue Attribute

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_MITIGATION_ISSUE:status,safety-level,security}}

### Safety Analysis Sufficient Attribute

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_SUFFICIENT:status,safety-level,security}}

### Safety Analysis Sufficient Check

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_SUFFICIENT_CHECK:status,safety-level,security}}

### Safety Analysis Mandatory Content

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_CONTENT:status,safety-level,security}}

### Safety Analysis Linkage Violates

{{artifact:TOOL_REQ__DOCS_SAF_ATTRS_VIOLATES:status,safety-level,security}}

### FMEA: fault id attribute

{{artifact:TOOL_REQ__DOCS_SAF_ATTR_FMEA_FAULT_ID:status,safety-level,security}}

### DFA: failure id attribute

{{artifact:TOOL_REQ__DOCS_SAF_ATTR_DFA_FAILURE_ID:status,safety-level,security}}

### Failure Effect

{{artifact:TOOL_REQ__DOCS_SAF_ATTR_FMEA_FAILURE_EFFECT:status,safety-level,security}}

----------------------------------------------------------------
## Safety Analysis (DFA + FMEA) Process to Tool Requirement Mapping

.. needtable::
   :style: table
   :types: gd_req
   :columns: id;satisfies_back as "tool_req"
   :filter: "gd_req__saf" in id

# 🗺️ Full Mapping

Process to tools:

.. needtable::
   :style: table
   :types: gd_req
   :columns: id;satisfies_back as "tool_req"

# Overview of Tool to Process Requirements

.. needtable::
   :types: tool_req
   :filter: any(s.startswith("gd_req") for s in satisfies)
   :columns: satisfies as "Process Requirement" ;id as "Tool Requirement";implemented;source_code_link
   :style: table


