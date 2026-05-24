---
id: DOC-MODULE-SAFETY-PLAN-86827
title: Module Safety Plan
type: specification
status: approved
tags: [eclipse-score]
---

# Module Safety Plan

### Communication Safety Plan

{{artifact:DOC__COMMUNICATION_SAFETY_PLAN:status,safety-level,security}}

# Functional Safety Management Context

This Safety Plan adds to the [[DOC__SCORE_PLATFORM_SAFETY_PLAN]] all the module development relevant work products needed for ISO 26262 conformity.

# Functional Safety Management Scope

This Safety Plan's scope is a SW module of the SW platform communication_module_docs.
The module consists of one or more SW components and will be qualified as a SEooC.

# Functional Safety Management Roles

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Alexander Schemmel

        * - Module Project Manager (= Feature team lead)
          - Committers of feature team see `Communication FT <https://github.com/eclipse-score/communication/blob/main/.github/CODEOWNERS>`_

# Tailoring

Additional to the tailoring in the SW platform project as defined in the [[DOC__SCORE_PLATFORM_SAFETY_PLAN]] we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):

  - [[WP__REQUIREMENTS_INSPECT]]: in version 0.5 the inspections have to be done by the user
  - [[WP__SW_ARCH_VERIFICATION]]: in version 0.5 the inspections have to be done by the user
  - [[WP__FDR_REPORTS]] (module's Safety Analyses & DFA): in version 0.5 the reviews have to be done by the user

# Functional Safety Module Work products

One set of work products for the module and one set for each component of the module:

## Module Work products List

.. list-table:: Module Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__MODULE_SAFETY_PLAN]]
          - [[GD_GUIDL__SAF_PLAN_DEFINITIONS]]
          - copy('status', need_id='gd_guidl__saf_plan_definitions')
          - this document

        * - [[WP__MODULE_SAFETY_PACKAGE]]
          - [[GD_GUIDL__SAF_PACKAGE]]
          - copy('status', need_id='gd_guidl__saf_package')
          - this document (including the linked documentation)

        * - [[WP__FDR_REPORTS]] (module Safety Plan)
          - [[GD_CHKLST__SAFETY_PLAN]]
          - copy('status', need_id='gd_chklst__safety_plan')
          - [[DOC__COMMUNICATION_SAFETY_PLAN_FDR]]

        * - [[WP__FDR_REPORTS]] (module Safety Package)
          - [[GD_CHKLST__SAFETY_PACKAGE]]
          - copy('status', need_id='gd_chklst__safety_package')
          - [[DOC__COMMUNICATION_SAFETY_PACKAGE_FDR]]

        * - [[WP__FDR_REPORTS]] (module's Safety Analyses & DFA)
          - [[GD_CHKLST__SAFETY_ANALYSIS]]
          - copy('status', need_id='gd_chklst__safety_analysis')
          - tailored

        * - [[WP__AUDIT_REPORT]]
          - performed by external experts
          - n/a
          - <Link to WP>

        * - [[WP__MODULE_SAFETY_MANUAL]]
          - [[GD_TEMP__SAFETY_MANUAL]]
          - copy('status', need_id='gd_temp__safety_manual')
          - [[DOC__COMMUNICATION_SAFETY_MANUAL]]

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - [[GD_TEMP__MOD_VER_REPORT]]
          - copy('status', need_id='gd_temp__mod_ver_report')
          - [[DOC__COMMUNICATION_VERIFICATION_REPORT]]

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - [[GD_TEMP__REL_MOD_REL_NOTE]]
          - copy('status', need_id='gd_temp__rel_mod_rel_note')
          - [[DOC__COMMUNICATION_RELEASE_NOTE]]

## Component lola Work products List

.. list-table:: Component lola Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__LOLA_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__COMMUNICATION_AOU]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - tailored

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__LOLA_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - tailored

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__LOLA_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__LOLA_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `lola/.h/.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_, [[DOC__LOLA_DETAILED_DESIGN]]

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `lola/test.cpp <https://github.com/eclipse-score/communication/blob/main/score/mw/com>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - External process

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to WP>

        * - [[WP__SW_COMPONENT_CLASS]]
          - [[GD_GUIDL__COMPONENT_CLASSIFICATION]]
          - copy('status', need_id='gd_guidl__component_classification')
          - [[DOC__LOLA_COMP_CLASS]]

# Module Safety Package

To create the safety package (according to [[GD_GUIDL__SAF_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Module Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_modules_communication_docs

## Component Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_modules_communication_components

## Component Requirements Status

not documented as needs, `lola trlc <https://github.com/eclipse-score/communication/blob/main/score/mw/com/requirements/component_requirements/component_requirements_ipc.trlc>`_
shows no status attribute

## Component AoU Status

.. needtable::
   :filter: "communication" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: communication
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component Architecture Status

see document link [[DOC__LOLA_ARCHITECTURE]] (as above)

## Deviations from Module Safety Plan

The following deviations from the module safety plan are present in the module safety package.
These are deviations from planned processes execution and/or work product results,
safety anomalies in the sense of known bugs in the software are reported in the release notes.

<Describe here the deviations, whether they have an impact on module's safety functions,
how these can be mitigated or argued and if and when a resolution is planned.>
