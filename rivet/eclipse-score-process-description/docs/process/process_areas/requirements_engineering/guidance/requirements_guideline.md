---
id: DOC-REQUIREMENTS-GUIDELINE-17167
title: Requirements Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Guideline

### Requirements Guideline

{{artifact:GD_GUIDL__REQ_ENGINEERING:status,safety-level,security}}

This document describes the general guidances for requirements based on the concept which is defined in [[title]]<doc_concept__req_process>.

# General Hints

## Templates

*Need* templates displaying the correct syntax and attribute definition are provided for each requirement type. For VScode, code snippets are included in the workspace settings which will provide in-place the definition of requirements including all mandatory attributes:

.. list-table:: Overview
   :header-rows: 1
   :widths: 37, 37, 25

   * - Requirement Level
     - Template
     - VS Code Snippet
   * - Stakeholder Requirements
     - [[title]] <gd_temp__req_stkh_req>
     - ``stkh_req__``
   * - Feature Requirements
     - [[title]] <gd_temp__req_feat_req>
     - ``feat_req__``
   * - Component Requirements
     - [[title]] <gd_temp__req_comp_req>
     - ``comp_req__``
   * - AoU Requirements
     - [[title]] <gd_temp__req_aou_req>
     - ``aou_req__``
   * - Tool Requirements
     - [[title]] <gd_temp__req_tool_req>
     - ``tool_req__``

Additionally for the formulation of requirements following template is available: [[title]]<gd_temp__req_formulation>

## Attributes

For all requirements following mandatory attributes are defined:

* Title and description: For formulating requirements, the following template shall be used [[title]]<gd_temp__req_formulation>
* ID: The naming convention for the ID is defined for every project in a central place (e.g. in the general contributor's guidelines)
* Furthermore the requirements need to be versioned. Therefore, a hash value of the requirement will to be calculated. The concept is described: traceability concept for requirements
* For the remaining attributes only predefined values can be used. A more detailed description can be found here: attributes of the requirements
* Note that "rationale" is only mandatory for Stakeholder Requirements.
* Process requirements do not need the security and safety attributes because these can be derived from the standards they comply with. Type attributes are also unnecessary, as these requirements are always non‑functional.

## Checks

During the docs build checks will be performed on the requirements. Those are specified via following process requirements:

.. _workflow_requirements:

# Workflow for Creating a Requirement

This section describes in detail which steps need to be performed to create a requirement based on requirements_workflow_fig

.. list-table:: Workflow for creating a requirement
   :header-rows: 1
   :widths: 10,60,30

   * - Step
     - Description
     - Responsible
   * - 1. <create_parent_requirement>
     - Create parent requirement
     - [[title]] <rl__contributor>
   * - 2. <review_parent_requirement>
     - Review parent requirement
     - [[title]] <rl__committer>
   * - 3. <review_parent_requirement>
     - Merge valid parent requirement to main branch
     - [[title]] <rl__committer>
   * - 4. <derive_child_requirement>
     - Derive child requirement and establish traceability
     - [[title]] <rl__contributor>
   * - 5. <review_child_requirement>
     - Review child requirement
     - [[title]] <rl__committer>
   * - 6. <review_child_requirement>
     - Merge valid child requirement to main branch
     - [[title]] <rl__committer>
   * - 7. <generate_linkage_document>
     - Generate linkage document
     - [[title]] <rl__contributor>
   * - 8. <formal_requirement_review>
     - Perform formal review of requirements
     - [[title]] <rl__committer>

.. _create_parent_requirement:

## Create parent requirement

In this step the parent requirements shall be created. Stakeholder- and feature requirements should be generated in the project's main repository.

For this the following templates are available:

* Requirement Templates <requirement templates>

Note: The project's way of contributing new content (how to branch, how to commit, how to merge with the selected version management tool)
has to be documented in a central place, stick to this guideline also for the requirement contributions.

.. _review_parent_requirement:

## Review parent requirement

As soon as the parent requirements are in a mature state, they can be reviewed <review_concept> and merged into the main branch of the main project's repository. However this is not the formal inspection of the requirements, this will follow in an upcoming step.

Following roles should be included in the review:

* [[title]] <rl__safety_manager>
* [[title]] <rl__security_manager>
* [[title]] <rl__committer>

.. _derive_child_requirement:

## Derive child requirement and establish traceability

In an upcoming step, the child requirements shall be derived from the parent requirements. Feature requirements shall be placed in the main project's repository, while component requirements shall be placed in the module's repository. During this process the derived requirements shall also be linked according to the defined traceability matrix to the parent requirements.

For this the following templates are available:

* Requirement Templates <requirement templates>

Note: For non-functional (and process) type requirements no children need to be derived (on lower requirement levels),
these can mostly be directly fulfilled and verified.
To ease verification a link to these ("process" type) requirements can be established from [[GD_TEMP__PROCESS_REQUIREMENT]].

.. _review_child_requirement:

## Review child requirement

As soon as also the child requirements are in a mature state they can be reviewed <review_concept> and merged into the main branch of the respective repository. Again this is not a formal inspection as it will be performed in a later step.

.. _generate_linkage_document:

## Generate linkage document

As parent and child requirements are now available, the linkage of the requirements can be established. This should be performed as described in coverage_of_requirements

.. _formal_requirement_review:

## Perform formal review of requirements

In a last step the requirements shall be formally inspected. Therefore a checklist exists: [[title]] <gd_chklst__req_inspection>

Following roles should be included in the review:

* [[title]] <rl__safety_manager>
* [[title]] <rl__security_manager>
* [[title]] <rl__committer>

.. _aou_workflow:

# Workflow for Creating and Linking Assumption of Use (AoU)

An AoU is a category of requirement which is part of a safety concept of an architectural element (and thus it is confirmed by a safety analysis).
As such a part of a safety concept it is aimed to avoid or detect safety relevant failures of the components.
The need for an AoU can arise in every development step, starting from requirements creation, but the main trigger for these is informal and formal safety analysis,
see [[DOC_CONCEPT__SAFETY_ANALYSIS]].
AoU handling is described in the requirements process mainly because AoU have very similar content and are treated almost like requirements,
i.e. they are inspected, fulfilled by architecture, mitigate failure modes from safety analysis and are verified by test.
Do not mistake AoUs to be more formal "user manuals", describing the proper use of a component's API so as to avoid error returns.
Error returns are perfectly ok from a safety point of view, if this does not mean that a safety requirement is violated.
As an AoU can not be fulfilled by the architecture element (e.g. component) itself, it needs to be fulfilled by the user of the element.
AoU created on SW-platform level are also coming from the scope of the project (i.e. the knowledge which safety activities are not part of a project)
or are defining general assumptions every user and/or every module in the platform has to fulfill.

In Safety Elements out of Context (SEooC) the AoUs are part of the safety manual.

In this workflow (as it describes SEooC development) these AoUs are created both project internal and project external

- internal:  For AoU which arise internally (i.e. from project specific architecture), the template is similar to the one for feature/component requirements. The main difference is that it is defined such that a requirement "satisfies" a parent requirement, but an AoU is not. Safety Analysis results must be "mitigated_by" an AoU or requirement (see picture below).
- external:  If externally provided SEooCs are integrated into the platform (e.g. a qualified Operating System). For these AoUs the sentence template cannot be taken into account, as these may be imported from an external safety manual. It is also not possible to link those to other platform development artifacts via the attribute "mitigates".

AoUs can be of different class and shall be handled by tracing those

* to Feature/Component (architecture) (via fulfils), if those are on (external) Component Level and can be fulfilled by (internal) Feature/Component
* to Stakeholder Requirements (via covers), if AoU are of general nature and can be fulfilled by platform
* or by containing those in Platform(s) Safety Manual(s), if AoU cannot be fulfilled by platform or its components (alone) but need to be fulfilled by the user of the platform

aou_traceability is an extension of the workproduct traceability to show the handling of AoU.
Note that the component level displayed in green shows two components - on the right (dark green) the one which is exporting AoU to be fulfilled by others,
on the left (light green) the component which fulfills and exports AoU.
Internal component's AoU can also be fulfilled (and linked) by other internal components, this is not depicted here, but would be quite the same with one exception:
External component's AoUs which cannot be fulfilled by the platform alone are contained in the platform safety manual, whereas the internal component's AoUs
are part of the module safety manual.

Note that it is not mandatory to have component architecture (in case the component has no "sub" components).
Therefore the "component" architecture element is depicted, which is used to link external Component Assumption of Use.

Like other requirements also an AoU needs to be verified - but by the user of the feature/component.
To improve the usability of a feature/component, its responsible team should already provide
integration tests the user has to run to prove the fulfillment of the AoU(s).

# Special cases

## Requirements for future (or past) milestones

A project release is always consistent, i.e. all linked development artifacts must be non-contradictory
and complete, i.e. all requirements are derived into dependent work products down to the implementation.
This is also the case for the selection of the scope of a platform by feature flags, as these
select a part of the platform but this part is complete.

In this chapter we cover a special use case where requirements not for the next milestone but for later milestones are specified.
This could be the case when a function is already specified but it is decided to delay its implementation.

A use case where the specification AND implementation of a new/modified feature is done
already during the development time of an earlier milestone than the feature is planned
can be realized by the feature flags (for new features) or by branching off.

For the "only specification" use case, the following attributes can be used:
- [[GD_REQ__REQ_ATTR_VALID_FROM]]
- [[GD_REQ__REQ_ATTR_VALID_UNTIL]]

These attributes can be used for stakeholder and feature requirements, but not for
the component requirements, as these are expected to be developed during small implementation cycles.

If an existing requirement needs to be reworked for the new function it will be split in two.
The requirement with the old specification will be valid_until the milestone before the
new function is planned and the requirement with the new specification is valid_from the planned milestone.

# Tailoring

### Requirements Tailored

{{artifact:GD_GUIDL__REQ_TAILORED:status,safety-level,security}}

