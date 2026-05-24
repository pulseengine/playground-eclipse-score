---
id: DOC-MODULE-SAFETY-PLAN-14087
title: Module Safety Plan
type: specification
status: approved
tags: [eclipse-score]
---

# Module Safety Plan

### Orchestrator Safety Plan

{{artifact:DOC__ORCHESTRATOR_SAFETY_PLAN:status,safety-level,security}}

# Functional Safety Management Context

This Safety Plan adds to the project's [[WP__PLATFORM_SAFETY_PLAN]] all the module development relevant work products needed for ISO 26262 conformity.

# Functional Safety Management Scope

This Safety Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
The module consists of one or more SW components and will be qualified as a SEooC.

# Functional Safety Management Roles

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Volker Häussler

        * - Module Project Manager
          - Naveen Mohanan

# Tailoring

Additional to the tailoring in the SW platform project as defined in the project's [[WP__PLATFORM_SAFETY_PLAN]] we define here the additional tailoring on module level.

- Excluded for this module are additionally the following work products (and their related requirements):

  - <work product/requirement> - <Argumentation why it is not needed or replaced by another work product or activity.>

# Functional Safety Module Work products

One set of work products for the module and one set for each component of the module:

## Module Work products List

.. list-table:: Module Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - [[WP__MODULE_SAFETY_PLAN]]
          - [[GD_GUIDL__SAF_PLAN_DEFINITIONS]]
          - copy('status', need_id='gd_guidl__saf_plan_definitions')
          - <Link to issue>
          - this document
          - see above

        * - [[WP__MODULE_SAFETY_PACKAGE]]
          - [[GD_GUIDL__SAF_PACKAGE]]
          - copy('status', need_id='gd_guidl__saf_package')
          - <Link to issue>
          - this document (including the linked documentation)
          - see above (and below)

        * - [[WP__FDR_REPORTS]] (module Safety Plan)
          - [[GD_CHKLST__SAFETY_PLAN]]
          - copy('status', need_id='gd_chklst__safety_plan')
          - <Link to issue>
          - [[DOC__MODULE_NAME_SAFETY_PLAN_FDR]]
          - copy('status', need_id='doc__module_name_safety_plan_fdr')

        * - [[WP__FDR_REPORTS]] (module Safety Package)
          - [[GD_CHKLST__SAFETY_PACKAGE]]
          - copy('status', need_id='gd_chklst__safety_package')
          - <Link to issue>
          - [[DOC__MODULE_NAME_SAFETY_PACKAGE_FDR]]
          - copy('status', need_id='doc__module_name_safety_package_fdr')

        * - [[WP__FDR_REPORTS]] (module's Safety Analyses & DFA)
          - Safety Analysis FDR tbd
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__AUDIT_REPORT]]
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - [[WP__MODULE_SAFETY_MANUAL]]
          - [[GD_TEMP__SAFETY_MANUAL]]
          - copy('status', need_id='gd_temp__safety_manual')
          - <Link to issue>
          - [[DOC__MODULE_NAME_SAFETY_MANUAL]]
          - copy('status', need_id='doc__module_name_safety_manual')

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - [[GD_TEMP__MOD_VER_REPORT]]
          - copy('status', need_id='gd_temp__mod_ver_report')
          - <Link to issue>
          - [[DOC__MODULE_NAME_VERIFICATION_REPORT]]
          - copy('status', need_id='doc__module_name_verification_report')

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - [[GD_TEMP__REL_MOD_REL_NOTE]]
          - copy('status', need_id='gd_temp__rel_mod_rel_note')
          - <Link to issue>
          - [[DOC__MODULE_NAME_RELEASE_NOTE]]
          - copy('status', need_id='doc__module_name_release_note')

## Component <name> Work products List

.. list-table:: Component <name> Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP/doc status

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - <Link to issue>
          - [[DOC__COMPONENT_NAME_REQUIREMENTS]]
          - doc copy('status', need_id='doc__component_name_requirements') & WP below

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - <Link to issue>
          - [[DOC__COMPONENT_NAME_REQUIREMENTS]]
          - doc copy('status', need_id='doc__component_name_requirements') & WP below

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - <link to issue>
          - [[DOC__COMPONENT_NAME_REQ_INSPECTION]]
          - copy('status', need_id='doc__component_name_req_inspection')

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - <Link to issue>
          - [[DOC__COMPONENT_NAME_ARCHITECTURE]]
          - doc copy('status', need_id='doc__component_name_architecture') & WP below

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - <link to issue>
          - [[DOC__COMPONENT_NAME_ARC_INSPECTION]]
          - copy('status', need_id='doc__component_name_arc_inspection')

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - <Link to issue>
          - [[DOC__COMPONENT_NAME_FMEA]]
          - doc copy('status', need_id='doc__component_name_fmea') & WP below

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - <Link to issue>
          - [[DOC__COMPONENT_NAME_DFA]]
          - doc copy('status', need_id='doc__component_name_dfa') & WP below

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_COMPONENT_CLASS]]
          - [[GD_GUIDL__COMPONENT_CLASSIFICATION]]
          - copy('status', need_id='gd_guidl__component_classification')
          - <Link to issue>
          - [[DOC__COMPONENT_NAME_COMP_CLASS]]
          - copy('status', need_id='doc__component_name_comp_class')

Note: In case the component is a new development, [[WP__SW_COMPONENT_CLASS]] shall be removed from the above list (and also from the folders).
In case an OSS element is used in the module, part 6 has to be filled out.

# OSS (sub-)component qualification plan

For the selected OSS component the following work products will be implemented (and why):

If the OSS element is classified as a
    - component, then the below table shall match the above, adding the reasoning for tailoring of work products according to the OSS component classification.
    - lower level component, then no work products additional to the component’s will be planned and activities below are part of the component’s issues.

.. list-table:: OSS (sub-)component <name> Work products
        :header-rows: 1

        * - Work product Id
          - Link to issue
          - Reasoning for tailoring

        * - [[WP__REQUIREMENTS_COMP]]
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 2

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - <Link to issue>
          - Always needed (for Q and QR classification) and also improves process Id 5

        * - [[WP__REQUIREMENTS_INSPECT]]
          - n/a
          - Checklist used in Pull Request Review

        * - [[WF__CR_MT_COMPARCH]]
          - <Link to issue>
          - <Reasoning for tailoring, needed for example in case of deficits in process Id 3&4 and complexity Ids 1&4>

        * - [[WP__SW_COMPONENT_FMEA]]
          - <Link to issue>
          - <Reasoning for tailoring, could help arguing too high cyclomatic complexity covered by safety mechanisms>

        * - [[WP__SW_ARCH_VERIFICATION]]
          - <Link to issue>
          - <Reasoning for tailoring, needed if also wf__cr_mt_comparch is required>

        * - [[WP__SW_IMPLEMENTATION]]
          - n/a
          - If source code is modified, this is not a OSS qualification any more.

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 3>

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - <Link to issue>
          - <Reasoning for tailoring, can improve deficits in process Id 6 and complexity Id 2>

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - <Link to issue>
          - Always needed (for Q and QR classification)

        * - [[WP__SW_COMPONENT_CLASS]]
          - <Link to issue>
          - Always needed as basis for tailoring.

# Work Product Status (for Safety Package)

## Component Requirements Status

.. needtable::
   :filter: "orchestrator" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: comp_req
   :tags: orchestrator
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component AoU Status

.. needtable::
   :filter: "orchestrator" in docname and "requirements" in docname and docname is not None
   :style: table
   :types: aou_req
   :tags: orchestrator
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Component Architecture Status

.. needtable::
   :filter: "component_name" in docname and "architecture" in docname and docname is not None
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :tags: orchestrator
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
