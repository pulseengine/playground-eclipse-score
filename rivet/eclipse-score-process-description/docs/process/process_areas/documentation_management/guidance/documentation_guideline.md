---
id: DOC-DOCUMENTATION-GUIDELINE-41883
title: Documentation Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Guideline

### Documentation

{{artifact:GD_GUIDL__DOCUMENTATION:status,safety-level,security}}

The planning for the documents is part of the [[WP__DOCUMENT_MGT_PLAN]] within the Platform Management Plan.
This plan includes the configuration item list containing all work products created in the project
as well as additional artifacts as defined in [[DOC_CONCEPT__CONFIGURATION_PROCESS]].

For manual review of the formal elements the
Documentation Review Checklist <gd_chklst__documentation_review> may used.

The review of each document is done as defined for this type of work product in the respective
process description.

## Document lifecycle models

Each released document shall have the status: “VALID”.

Depending on the document assigned lifecycle Model, as defined here
work_products_overview_list, the document can either reach this state directly,
or some prior states are required.

Thus different document lifecycle models exists (as defined in
[[GD_REQ__DOC_ATTR_STATUS]]):

* Model1: "VALID"
* Model2: "DRAFT" -> "VALID"
* Model3: "DRAFT" -> "VALID" -> "VALID(INSPECTED)"

**Guidance for lifecycle model 1:**

Example: [[WP__ISSUE_TRACK_SYSTEM]]

The document has the state “VALID” after creation.

Recommendation: Author should do a self verification for the correctness and completeness
of the content and th fulfillment of required formal aspects.

**Guidance for lifecycle model 2:**

Example: [[WP__FEAT_REQUEST]]

The document has the state “VALID” after creation and a reviewer as confirmed
the correctness and completeness of the content and th fulfillment of required formal
aspects.

The figure below shows an overview of the review workflow for lifecycle model 2 (Simple
Workflow) based on Pull Requests.

Nevertheless, it is still recommended for author to do a self verification for the
correctness and completeness of the content and the fulfillment of required formal
aspects before asking for a review.

In case of any discussions are needed between author and reviewer, or still some ambiguities
exists, the document can also be published first with the status "DRAFT".

This indicates, that the document is created, may have no mature structure yet, content
is not complete and correct or formal aspects are not considered.

The figure below shows an overview of the review workflow for lifecycle model 2
(Extended Workflow) based on Pull Requests.

After some iterations between author and reviewer, the document can be set to status
"VALID", when all issues are resolved.

Due to updates, findings, other issues or change request, the document status may set
back from "VALID" to "DRAFT". This triggers a new review cycle.

**Guidance for lifecycle model 3:**

In principle same as lifecycle model 2, but an additional inspection step is required,
as described here: review_concept.

Example: [[WP__REQUIREMENTS_STKH]]
