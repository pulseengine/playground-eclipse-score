---
id: DOC-MODULE-SAFETY-PLAN-82430
title: Module Safety Plan
type: specification
status: approved
tags: [eclipse-score]
---

# Module Safety Plan

### Persistency Safety Plan

{{artifact:DOC__PERSISTENCY_SAFETY_PLAN:status,safety-level,security}}}}

# Functional Safety Management Context

This Safety Plan adds to the [[WP__PLATFORM_SAFETY_PLAN]] all the module development relevant workproducts needed for ISO 26262 conformity.

# Functional Safety Management Scope

This Safety Plan's scope is a SW module of the SW platform persistency_module_documentation.
The module consists of one or more SW components and will be qualified as a SEooC.

# Functional Safety Management Roles

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Volker Häussler

        * - Module Project Manager (= Feature team lead)
          - Lars Bauhofer

# Tailoring

Additional to the tailoring in the SW platform project as defined in the [[WP__PLATFORM_SAFETY_PLAN]] we define here the additional tailoring on module level.

| - Excluded for this module are additionally the following workproducts (and their related requirements):
|   - Safety Analysis will not be performed on module level, because they are identical to the feature level.

# Functional Safety Module Workproducts

One set of workproducts for the module and one set for each component of the module:

## Module Workproducts List

.. list-table:: Module Workproducts
        :header-rows: 1

        * - Workproduct Id
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
          - [[DOC__PERSISTENCY_SAFETY_PLAN_FDR]]

        * - [[WP__FDR_REPORTS]] (module Safety Package)
          - [[GD_CHKLST__SAFETY_PACKAGE]]
          - copy('status', need_id='gd_chklst__safety_package')
          - [[DOC__PERSISTENCY_SAFETY_PACKAGE_FDR]]

        * - [[WP__FDR_REPORTS]] (module's Safety Analyses & DFA)
          - [[GD_GUIDL__SAFETY_ANALYSIS]]
          - copy('status', need_id='gd_guidl__safety_analysis')
          - n/a because no safety analysis performed for the components. They will be overtaken from the feature.

        * - [[WP__AUDIT_REPORT]]
          - performed by external experts
          - n/a
          - <Link to WP>

        * - [[WP__MODULE_SAFETY_MANUAL]]
          - [[GD_TEMP__SAFETY_MANUAL]]
          - copy('status', need_id='gd_temp__safety_manual')
          - [[DOC__PERSISTENCY_SAFETY_MANUAL]]

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - [[GD_TEMP__MOD_VER_REPORT]]
          - copy('status', need_id='gd_temp__mod_ver_report')
          - [[DOC__PERSISTENCY_VERIFICATION_REPORT]]

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - [[GD_TEMP__REL_MOD_REL_NOTE]]
          - copy('status', need_id='gd_temp__rel_mod_rel_note')
          - [[DOC__PERSISTENCY_RELEASE_NOTE]]

## Component KVS Workproducts List

.. list-table:: Component KVS Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__KVS_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__KVS_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - Checklist used in Pull Request Review

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__KVS_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - Checklist used in Pull Request Review

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[WP__SW_COMPONENT_FMEA]]
          - copy('status', need_id='gd_guidl__safety_analysis')
          - [[DOC__KVS_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[WP__SW_COMPONENT_DFA]]
          - copy('status', need_id='gd_guidl__safety_analysis')
          - [[DOC__KVS_DFA]]

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
          - Checklist used in Pull Request Review

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to WP>

        * - [[WP__SW_COMPONENT_CLASS]]
          - [[GD_GUIDL__COMPONENT_CLASSIFICATION]]
          - copy('status', need_id='gd_guidl__component_classification')
          - [[DOC__JSON_COMP_CLASS]]

# OSS (sub-)component qualification plan

For the selected OSS component the following workproducts will be implemented (and why):

If the OSS element is classified as
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no workproducts additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component Tiny JSON Workproducts
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Reasoning for tailoring

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - <Reasoning for tailoring>

        * - [[WF__CR_MT_COMPARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - [[WP__SW_IMPLEMENTATION]]
          - n/a
          - Tailored - If source code is modified, this is not a OSS qualification any more.

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - Always needed (for Q and QR classification)

        * - [[WP__SW_COMPONENT_CLASS]]
          - [[GD_GUIDL__COMPONENT_CLASSIFICATION]]
          - Always needed as basis for tailoring.

## Link to project planning

<add here a link to your module's planning for the above work products, e.g. a link to a ticket.>

# Module Safety Package

To create the safety package (according to [[GD_GUIDL__SAF_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Module Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See <add here the section reference to the documentation management plan>

## Component Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See <add here the section reference to the documentation management plan>

## Component Requirements Status

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: comp_req
   :tags: component_name
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component AoU Status

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: component_name
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component Architecture Status

.. needtable::
   :filter: docname is not None and "persistency" in docname and "architecture" in docname
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: component_name
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

.. _persistency_safety_package_deviations:

## Deviations from Module Safety Plan

The following deviations from the module safety plan are present in the module safety package.
These are deviations from planned processes execution and/or work product results,
safety anomalies in the sense of known bugs in the software are reported in the release notes.

<Describe here the deviations, whether they have an impact on module's safety functions,
how these can be mitigated or argued and if and when a resolution is planned.>
