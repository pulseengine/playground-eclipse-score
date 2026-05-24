---
id: DOC-TOOL-MANAGEMENT-CONCEPT-14992
title: Tool Management Concept
type: specification
status: approved
tags: [eclipse-score]
---

# Concept Description

### Concept Description

{{artifact:DOC_CONCEPT__TOOL_PROCESS:status,safety-level,security}}

In this section a concept for the Tool Management will be discussed. Inputs for this concepts
are the requirements of ISO 26262 Part-8, Clause 11, ASPICE PAM 4.0, SUP.8 and
ISO/SAE 21434 Clause 5, 5.4.5 additionally including the requirements of the different stakeholders
for the Tool Management Process.

# Key concept

In general all tools to generate the project product must be identified. As it is a project objective
to use tools wherever applicable to generate any kind of work product, the selection criteria for
any tool including OSS tools must include therefore the determination of the Tool Confidence Level
`(TCL) <https://www.validas.de/resources/glossary/tool-classification#b-what-is-the-tool-confidence-level-tcl>`_ for the tool under consideration.

Based on the resulting TCL additional Tool Qualification activities may required.

# Inputs

#. Stakeholders for the Tool Management?
#. Which documentations are required?
#. Which activities are required?

# Stakeholders for the Tool Management

#. Contributor <rl__contributor>
   Infrastructure, Tooling Community <rl__infrastructure_tooling_community>

   * Contributes tooling, infrastructure elements to grow and mature the project development environment

#. Safety Manager<rl__safety_manager>, Security Manager <rl__security_manager>,
   Committer <rl__committer>

   * Verifies and approves the the tool verification report

# Standard Requirements

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO/SAE 21434

# Required documentation

For each tool the [[GD_TEMP__TOOL_MANAGEMENT_VERIF_RPT_TEMPLATE]] shall be used to document
the relevant information.

# Activities for Tool Management

The main work product is the Tool Verification Report <wp__tool_verification_report>.
This work product is created and maintained until it is released. It contains the tool
evaluation results as well as the qualification results, if applicable.
For each tool the Workflows <tlm_workflows> applies.

# Attributes for Tool Management

The required attributes for the Tool Verification Report are defined here:
tlm_process_attributes.
