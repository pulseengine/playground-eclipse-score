---
id: DOC-VERIFICATION-GETSTRT-67702
title: Verification Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Verification Get Started

{{artifact:DOC_GETSTRT__VERIFICATION_PROCESS:status,safety-level,security}}

# Relevant Documents

Key documents to get an understanding about verification activities are:

* **Concept Document:** [[DOC_CONCEPT__VERIFICATION_PROCESS]] provides a high-level overview of the verification concept.
* **Verification Guideline:** [[GD_GUIDL__VERIFICATION_GUIDE]] details test case development, execution, and reporting procedures.
* **Verification Plan:** [[WP__VERIFICATION_PLAN]] implementation outlines the overall verification strategy and objectives.
  (Note that the implementation of the verification plan can be found in the platform management plan.)

# General Workflow

The workflows can be split into 4 major parts:

* Test planning filling the template [[GD_TEMP__VERIFICATION_PLAN]].
* Test specification and implementation for the respective testing level
* Test execution by the CI.
  (Manual test cases are treated as automated test with user interaction and timeouts.)
* Test reports are created when all verification artifacts on a module and platform level are
  available for a specific baseline.

The details of what needs to be done in each part are described in the verification_workflows.
