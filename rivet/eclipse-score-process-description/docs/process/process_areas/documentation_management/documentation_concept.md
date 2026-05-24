---
id: DOC-DOCUMENTATION-CONCEPT-66878
title: Documentation Concept
type: specification
status: approved
tags: [eclipse-score]
---

## Concept

### Documentation Management Concept

{{artifact:DOC_CONCEPT__DOCUMENTATION_PROCESS:status,safety-level,security}}}}

In this section a concept for the documentation management will be discussed.
Inputs for this concepts are mainly the requirements of ISO26262 "Part 2: Management of functional safety"
and "Part 8: Supporting processes".

#### Key concept

The Documentation Management Plan should define the strategy to manage the identified documentations
in an effective and repeatable way for the project life cycle.

#### Inputs

#. Stakeholders for the documentation work products?
#. What tooling do we need?
#. Which guidance for the work products do we have?

#### Stakeholders

#. Contributor <rl__contributor>

   * contributing documents

#. Committer <rl__committer>

   * contributing and approving documents

#. Project Lead <rl__project_lead>

   * planning and status reporting of work products and their documentation for the platform

#. Module Lead <rl__project_lead>

   * planning and status reporting of work products and their documentation for modules

#. Safety Manager <rl__safety_manager>

   * wants to know when the safety related documents are ready for a release
   * wants to know who was the author and approver of a document in case of safety issues

#. Security Manager <rl__security_manager>

   * wants to know when the security related documents are ready for a release
   * wants to know who was the author and approver of a document in case of security issues

#. Quality Manager <rl__quality_manager>

   * wants to know when the quality related documents are ready for a release
   * wants to know who was the author and approver of a document in case of quality issues

#### Document Management Tooling

For the document attributes to be manually set, `sphinx-needs <https://www.sphinx-needs.com/>`_ will be used.

For the versioning and version history `github <https://github.com/>`_ is used.

For the automated attributes additional tooling is created (see guidance/documentation_process_reqs)

For the scheduling and tracking of the documentation `GitHub issues <https://github.com/features/issues>`_  will be used.

#### Guidance

The document management guideline can be found here [[GD_GUIDL__DOCUMENTATION]].
