---
id: DOC-MODULE-SAFETY-PLAN-93755
title: Module Safety Plan
type: specification
status: approved
tags: [eclipse-score]
---


### FEO Module Safety Plan

{{artifact:DOC__FEO_SAFETY_PLAN:status,safety-level,security}}

# FEO Module Safety Plan

# Functional Safety Management Context

This Safety Plan adds to the [[DOC__SCORE_PLATFORM_SAFETY_PLAN]] all the module development relevant work products needed for ISO 26262 conformity.

# Functional Safety Management Scope

This Safety Plan's scope is a SW module feo_module_documentation of the SW platform.
The module consists of one or more SW components and will be qualified as a SEooC.

# Functional Safety Management Roles

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Markus Schu

        * - Module Project Manager (= Feature team lead)
          - Johannes Glamsch

# Tailoring

Additional to the tailoring in the SW platform project as defined in the [[DOC__SCORE_PLATFORM_SAFETY_PLAN]] we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):
  - No work products excluded

# Functional Safety Module Work Products

One set of work products for the module and one set for each component of the module:

## FEO Module Work Products List

.. list-table:: Module Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__MODULE_SAFETY_PLAN]]
          - [[GD_GUIDL__SAF_PLAN_DEFINITIONS]], [[GD_TEMP__MODULE_SAFETY_PLAN]]
          - copy('status', need_id='gd_guidl__saf_plan_definitions')
          - this document

        * - [[WP__MODULE_SAFETY_PACKAGE]]
          - [[GD_GUIDL__SAF_PACKAGE]]
          - copy('status', need_id='gd_guidl__saf_package')
          - this document (including the linked documentation)

        * - [[WP__FDR_REPORTS]] (module Safety Plan)
          - [[GD_CHKLST__SAFETY_PLAN]]
          - copy('status', need_id='gd_chklst__safety_plan')
          - [[DOC__FEO_SAFETY_PLAN_FDR]]

        * - [[WP__FDR_REPORTS]] (module Safety Package)
          - [[GD_CHKLST__SAFETY_PACKAGE]]
          - copy('status', need_id='gd_chklst__safety_package')
          - [[DOC__FEO_SAFETY_PACKAGE_FDR]]

        * - [[WP__FDR_REPORTS]] (module's Safety Analyses & DFA)
          - [[GD_CHKLST__SAFETY_ANALYSIS]]
          - copy('status', need_id='gd_chklst__safety_analysis')
          - [[DOC__SAFETY_ANALYSIS_INSPECTION_COMPONENT_FEO]]

        * - [[WP__AUDIT_REPORT]]
          - performed by external experts
          - n/a
          - <Link to WP>

        * - [[WP__MODULE_SAFETY_MANUAL]]
          - [[GD_TEMP__SAFETY_MANUAL]]
          - copy('status', need_id='gd_temp__safety_manual')
          - [[DOC__FEO_SAFETY_MANUAL]]

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - [[GD_TEMP__MOD_VER_REPORT]]
          - copy('status', need_id='gd_temp__mod_ver_report')
          - [[DOC__FEO_VERIFICATION_REPORT]]

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - [[GD_TEMP__REL_MOD_REL_NOTE]]
          - copy('status', need_id='gd_temp__rel_mod_rel_note')
          - [[DOC__FEO_RELEASE_NOTE]]

## FEO Component Work Products List

.. list-table:: FEO Component Work Products List
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__COMPONENT_FEO_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__COMPONENT_FEO_AOU_REQS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__REQ_INSPECTION_COMPONENT_FEO]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__COMPONENT_FEO_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__ARCH_INSPECTION_COMPONENT_FEO]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__COMPONENT_FEO_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__COMPONENT_FEO_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - <Link to WP>

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to WP>

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__IMPL_INSPECTION_COMPONENT_FEO]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to WP>

As feo is using score-crates as OSS component, the following section should be filled out
accordingly.
This section is currently only a placeholder and needs to be adapted based on the progress of the
OSS qualification.

# OSS score-crates component qualification plan

For the selected OSS component the following work products will be implemented (and why):

If the OSS element is classified as a
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no work products additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component score-crates Work products
        :header-rows: 1

        * - Work product Id
          - Reasoning for tailoring

        * - [[WP__REQUIREMENTS_COMP]]
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - [[WP__REQUIREMENTS_INSPECT]]
          - <Reasoning for tailoring>

        * - [[WF__CR_MT_COMPARCH]]
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - [[WP__SW_COMPONENT_FMEA]]
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - [[WP__SW_ARCH_VERIFICATION]]
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - [[WP__SW_IMPLEMENTATION]]
          - Tailored - If source code is modified, this is not a OSS qualification any more.

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - Always needed (for Q and QR classification)

        * - [[WP__SW_COMPONENT_CLASS]]
          - Always needed as basis for tailoring.

# Module Safety Package

To create the safety package (according to [[GD_GUIDL__SAF_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Module Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_modules_feo_docs

## Component Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_modules_feo_components

## Component Requirements Status

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: comp_req
   :tags: component_feo
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component AoU Status

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: component_feo
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component Architecture Status

.. needtable::
   :filter: docname is not None and "feo" in docname and "architecture" in docname
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: component_feo
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
