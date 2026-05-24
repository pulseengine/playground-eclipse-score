---
id: DOC-TOOL-MANAGEMENT-GETSTRT-15608
title: Tool Management Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Getting Started on Tool Management

{{artifact:DOC_GETSTRT__TOOL_PROCESS:status,safety-level,security}}}}

This document describes the steps to evaluate tools and qualify them according to
ISO 26262 and ISO/SAE 21434 as used standards in the project.

Therefore guidelines [[GD_TEMP__TOOL_MANAGEMENT_VERIF_RPT_TEMPLATE]] and a
 [[DOC_CONCEPT__TOOL_PROCESS]] are available.

# General Workflow

The workflows are defined in the tlm_workflows section.

For every tool identified, the following workflows are executed:

* Create tool verification report according to [[WF__TOOL_CREATE_TOOL_VERIFICATION_REPORT]]
* Evaluate tool and update tool verification report according to [[WF__TOOL_EVALUATE_TOOL]]
* Qualify tool and update tool verification report according to [[WF__TOOL_QUALIFY_TOOL]]
* Approve tool verification report according to [[WF__TOOL_APPROVE_TOOL_VERIFICATION_REPORT]]

In addition create a tool management plan as part of the platform management plan according to [[WF__PLATFORM_CR_MT_PLATFORM_MGMT_PLAN]].
