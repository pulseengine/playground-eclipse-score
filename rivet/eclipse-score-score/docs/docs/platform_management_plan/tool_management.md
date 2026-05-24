---
id: DOC-TOOL-MANAGEMENT-28999
title: Tool Management
type: specification
status: approved
tags: [eclipse-score]
---


### Tool Management Plan

{{artifact:DOC__PLATFORM_TOOL_MANAGEMENT_PLAN:status,safety-level,security}}}}

## Tool Management/ Tool Management Plan

This document implements parts of the [[WP__PLATFORM_MGMT]].

#### Purpose

The purpose of the Tool Management Plan is to guide the identification, evaluation and, if
applicable, the qualification (safe and secure use) of Tools for the S-CORE project.

S-CORE guideline is to use as much as possible Tools for the generation of all required work
products. Thus all Tools which will be used as part of the tool chain for the work product
generation must be identified, documented and evaluated and if applicable, qualified.

#### Objectives and Scope

#### Tool Management Goals

* Tools are identified and documented
* Tools are evaluated
* Tools are qualified, if applicable
* Tool Verification Reports are released

#### Approach

#### Tool Management Attributes

[[GD_REQ__TOOL_ATTR_UID]] are implemented as follows:

#### Identification

Each tool is identified by its name or UID and its version, independent where it is located.

The most important tools are stored in one GitHub repository,
`tooling repository <https://GitHub.com/eclipse-score/tooling/>`_.

But in general Tool can be stored all over the place.

For each Tool the [[GD_TEMP__TOOL_MANAGEMENT_VERIF_RPT_TEMPLATE]] shall be used to document
the relevant information.

[[GD_CHKLST__TOOL_CR_REVIEW]] shall be used to check that all relevant information is considered.

The configuration of tools is part of the [[DOC__CONFIG_MGT_PLAN]].

The output after this stage is the [[WP__TOOL_VERIFICATION_REPORT]] in status: `identified`.

#### Evaluation

The tool confidence level (TCL) must be determined as outlined in the
[[DOC_CONCEPT__TOOL_PROCESS]].

Step-by-Step guide:

1. Determine the tool impact
2. Determine the tool error detection
3. Determine the tool confidence level

**To Step 1**

Based on the found malfunctions or threats judge, if any safety or security requirements may violated.
If this is the case, determine tool impact to "YES" otherwise to "NO".

If tool impact is "NO", continue with 3, otherwise 2.

**To Step 2**

Based on the malfunctions or threats found, assess whether these can be detected or prevented.
Consider also potential safety measures and security controls to increase the detection and
prevention of these, if applicable.
If there is no guarantee to either detect or prevent these, judge tool error detection to "NO",
otherwise to "YES".

**To Step 3**

If tool impact is judged to "YES" and tool error detection judged to "NO", the tool confidence
level is determined to "LOW", otherwise "HIGH".

In case the tool confidence level is "LOW", tool qualification is required.

The output after this stage is the [[WP__TOOL_VERIFICATION_REPORT]] in status: `evaluated`.

#### Qualification

As method "validation of software tool" is applied.

Specify requirements for the tools purpose and usage in the S-CORE context.
Analyze the malfunctions and threats and specify additional safety measures and security controls
to increase the prevention and detection of them.
Specify test cases and tests to verify the requirements and generate a test report.
Update the Tool Verification Report accordingly to document the outcomes.

For the generation of requirements, verification and analyses the existing processes as defined
in the [[WP__PLATFORM_MGMT]] shall be used.

In detail:

* Use [[WF__REQ_COMP_REQ]] to create requirements for the software tool and [[WF__MONITOR_VERIFY_REQUIREMENTS]] for the verification

* Use [[WF__VERIFICATION_COMP_INT_TEST]] to test the requirements for the software tool and [[WF__VERIFICATION_MOD_VER_REPORT]] to report

* If applicable, use for the Analyses: (to be added, after Safety/Security Analyses have been merged)

The output after this stage is the [[WP__TOOL_VERIFICATION_REPORT]] in status: `qualified`.

#### Approval

Finally the tool may accepted for the S-CORE project. Thus the Tool Verification Report after this
stage is the [[WP__TOOL_VERIFICATION_REPORT]] in status: `released`.

If not, the tool is rejected, thus Tool Verification Report after this
stage is the [[WP__TOOL_VERIFICATION_REPORT]] in status: `rejected`.

#### Tailoring

Tailoring of safety activities for confidence in the use of software tools:

The following ISO 26262 defined safety requirements are not relevant for the S-CORE SW platform
development, as the respective methods are not used:

[[STD_REQ__ISO26262__SUPPORT_11471]], [[STD_REQ__ISO26262__SUPPORT_11472]],
[[STD_REQ__ISO26262__SUPPORT_11473]], [[STD_REQ__ISO26262__SUPPORT_11474]],
[[STD_REQ__ISO26262__SUPPORT_11481]], [[STD_REQ__ISO26262__SUPPORT_11482]],
[[STD_REQ__ISO26262__SUPPORT_11483]], [[STD_REQ__ISO26262__MANAGEMENT_6456]]

#### Tool List

The S-CORE tools overview can be found here: tools
