---
id: DOC-SCORE-REVIEW-CONCEPT-19208
title: Score Review Concept
type: specification
status: approved
tags: [eclipse-score]
---

.. _review_concept:

# Review and Inspection Concept

### Work product Inspections Concept

{{artifact:DOC_CONCEPT__WP_INSPECTIONS:status,safety-level,security}}

#### Inspection Definition

Inspections are formal reviews supported by a checklist with documented conduct and outcome.
In this project there are inspections on the following work products, which are generally performed in the same way:

.. list-table:: Work products subject to inspection
        :header-rows: 1

        * - inspected work product Id
          - Link to checklist

        * - [[WP__REQUIREMENTS_STKH]]
          - [[GD_CHKLST__REQ_INSPECTION]]

        * - [[WP__REQUIREMENTS_FEAT]]
          - [[GD_CHKLST__REQ_INSPECTION]]

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_CHKLST__REQ_INSPECTION]]

        * - [[WP__REQUIREMENTS_SW_PLATFORM_AOU]]
          - [[GD_CHKLST__REQ_INSPECTION]]

        * - [[WP__REQUIREMENTS_FEAT_AOU]]
          - [[GD_CHKLST__REQ_INSPECTION]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_CHKLST__REQ_INSPECTION]]

        * - [[WP__FEATURE_ARCH]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]

Note that for test cases also a review checklist is provided for guidance, but no formal inspection is required.
The same is true for Safety Analysis and DFA.
The independence of testing respectively of test case review is covered by the use of version management tool also for the review of test cases.
Which means that at least the test case definition or the test case review is performed by
another person as the author of the verified work product (see [[GD_REQ__VERIFICATION_INDEPENDENCE]]).

#### Inspection Conduct

Inspections are conducted by using version management tooling mechanisms and files based on inspection templates.
We expect that the requirement and architecture work products need to mature during implementation and testing
and that the inspection checklists also contain questions which can not be answered already at creation of the work product,
because also other work products content also has to be taken into account (which is not available at the beginning),
therefore we use a two-step approach for the review and inspection for these.

The detailed design and coding inspection is also done in this two-step approach, at least for the
initial development of a feature/component. This is also to have a unified approach for the inspections
and reduce initial tooling support effort.

The initial activity for review and inspection is the (informal) version management tooling review on every Pull-Request
(resp. Change Request, see [[GD_GUIDL__CHANGE_CHANGE_REQUEST]])
which creates or modifies one of these work products (subject to inspection).
After this review the work products are in status "valid", which means they can be used
for further development and verification steps (note that merged code is always "valid").

The next activity is the formal inspection, which follows the following workflow (see illustration below):

1. Inspection initiation

The inspection is initiated by the safety manager, security manager or quality manager who will be the moderator for the inspection.
He sets the work product's status to "valid(inspected)" and starts a Pull-Request (PR).
This marks the scope of the inspection but also the work product's version.
For documentation of the review either the PR comments are used (based on latest inspection templates),
or the safety manager creates/updates an inspection documentation file based on the latest respective templates in the same PR
containing the same information (role assignment = author/reviewer(s)/moderator and checklist items).
The latter option is not preferred but needs to be used in case the PR data can/could not be stored.
When opening the PR, Version management tooling will automatically ask for a review by the defined one or more reviewer
implemented by the codeowner mechanism of the work product.
In the PR (resp. inspection documentation file) the inspection result will be documented for each checklist item
(pass/fail - with link to a ticket for the corrections).

2. Inspection review

The reviewers will fill out the checklist and add their findings on the work product in the PR (by adding an own commit into the PR).
They close their review activity by documenting their verdict as "Approve" or "Request Changes".
Any "Request Changes" will block the PR from being merged. Note that the PR author cannot "Approve" or "Request Changes" (his own PR).

3. Inspection corrections

After all requested reviewers are done, the author answers the findings and/or performs corrections of the work products
- either directly or by creating a Bug ticket to resolve.

4. Inspection approval

The reviewer(s) re-review and adapt their verdict accordingly (to "Approve").
In case the author or the reviewer(s) cannot agree on a solution, the safety/security/quality manger
who initiated the inspection will be asked to moderate this.
After all the required reviewers approved including the CODEOWNER of the work product, the PR is merged.

In future the project will try to establish (also) incremental inspections based on version management tooling only,
i.e. the inspection template, findings documentation and storage will be part of this tooling.
But this is currently not implemented.

The following picture shall illustrate how a status lifecycle of a requirement work product will look like.
The lifecycle for other work product should be similar.

#. Create requirement
#. (Informal) Pull-Request Review
#. Merge valid requirement to main
#. During development and verification steps the requirement is reworked and again put to PR Review
#. Implementation and verification work products are linked
#. Safety manager initiates a (formal) Pull-Request Inspection
#. After finding resolution, the requirement is merged in valid(inspected) state
#. In case of changes the requirement returns in the valid state

Note: This workflow can be shortcut in case an already mature work product (in this case requirement)
is part of a Pull-Request including already the relevant verification and implementation.
This could be the case when for example merging a development branch back into the main line.
In this case the workflow starts with step 6.

#### Inspection Know-How

For work products with ASIL rating the safety manager shall initiate the inspections,
for those which are QM but are security related the security manger may request this,
but also the quality manager may ask for inspection for critical QM work products.

Judging if the maturity of a work product is already enough to request an inspection
can be based for example for the requirements on their "Implemented by", "Verified by" and "Requirement Covered" attribute.
For example when requesting a new feature by filling out the [[GD_TEMP__CHANGE_FEATURE_REQUEST]]
you are asked to also specify the feature's requirements
- it is not expected that the maturity of the requirements is already enough at this time to make a good inspection.
On the other end of a development "lifecycle",
of course all the ASIL rated work products must be in status "inspected" before release,
this is checked as part of the release_management.

Checklist Templates contain hints how to understand the checkpoints or ideas how to check,
these hints are not replicated in every PR documented, but only the checklist questions.
Reviewers shall comment also the checklist items which they mark as passed, as a memory aid,
to be able to later explain what they considered during review
(for example in case a requirement is found to be wrong after the release, to be able to do a lessons learned).

Any work product which is subject to inspection and is modified after an inspection
shall transition from "valid(inspected)" back to "valid" state. This shall be automatically checked.

#### Process Requirements

### Version for inspected requirements

{{artifact:GD_REQ__GENERAL_REQUIREMENTS_VERSION:status,safety-level,security}}

### Version for inspected architecture

{{artifact:GD_REQ__GENERAL_ARCHITECTURE_VERSION:status,safety-level,security}}

### Checklist templates in pull requests

{{artifact:GD_REQ__GENERAL_CHECKLIST_TEMPLATES:status,safety-level,security}}

### Status Set Check

{{artifact:GD_REQ__GENERAL_STATUS_SET_CHECK:status,safety-level,security}}

### Status Reset Check

{{artifact:GD_REQ__GENERAL_STATUS_RESET_CHECK:status,safety-level,security}}

