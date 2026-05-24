---
id: DOC-MODULE-SECURITY-PLAN-91203
title: Module Security Plan
type: specification
status: approved
tags: [eclipse-score]
---

# Module Security Plan

### Persistency Security Plan

{{artifact:DOC__PERSISTENCY_SECURITY_PLAN:status,safety-level,security}}}}

# Security Management Context

This Security Plan adds to the [[GD_GUIDL__SECURITY_PLAN_DEFINITIONS]] all the module development relevant workproducts needed for ISO SAE 21434 conformity.

# Security Management Scope

This Security Plan's scope is a SW module of the SW platform persistency_module_documentation.
The module consists of one or more SW components and will be qualified as a EooC.

# Security Management Roles

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Security Manager
          - Karthik Vanka

        * - Module Project Manager (= Feature team lead)
          - TBD

# Tailoring

Additional to the tailoring in the SW platform project as defined in the [[GD_GUIDL__SECURITY_PLAN_DEFINITIONS]] we define here the additional tailoring on module level.

| - Excluded for this module are additionally the following workproducts (and their related requirements):
|   - No workproducts excluded

# Security Module Workproducts

.. list-table:: Module Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - [[WP__MODULE_SECURITY_PLAN]]
          - [[GD_GUIDL__SECURITY_PLAN_DEFINITIONS]]
          - copy('status', need_id='gd_guidl__security_plan_definitions')
          - <Link to issue>
          - this document
          - valid

        * - [[WP__MODULE_SECURITY_PACKAGE]]
          - [[GD_GUIDL__SECURITY_PACKAGE]]
          - copy('status', need_id='gd_guidl__security_package')
          - <Link to issue>
          - this document (including the linked documentation)
          - valid

        * - [[WP__FDR_REPORTS]] (module Security Plan)
          - [[GD_CHKLST__SECURITY_PLAN]]
          - copy('status', need_id='gd_chklst__security_plan')
          - <Link to issue>
          - [[DOC__PERSISTENCY_SECURITY_PLAN_FDR]]
          - copy('status', need_id='doc__persistency_security_plan_fdr')

        * - [[WP__FDR_REPORTS]] (module Security Package)
          - [[GD_CHKLST__SECURITY_PACKAGE]]
          - copy('status', need_id='gd_chklst__security_package')
          - <Link to issue>
          - [[DOC__PERSISTENCY_SEC_PKG_FDR]]
          - copy('status', need_id='doc__persistency_sec_pkg_fdr')

        * - [[WP__FDR_REPORTS]] (module's Security Analyses)
          - [[GD_GUIDL__SECURITY_ANALYSIS]]
          - copy('status', need_id='gd_guidl__security_analysis')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__AUDIT_REPORT_SECURITY]]
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - [[WP__MODULE_SECURITY_MANUAL]]
          - [[GD_TEMP__PLATFORM_SECURITY_MANUAL]]
          - copy('status', need_id='gd_temp__platform_security_manual')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - [[GD_TEMP__MOD_VER_REPORT]]
          - copy('status', need_id='gd_temp__mod_ver_report')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - [[GD_TEMP__REL_MOD_REL_NOTE]]
          - copy('status', need_id='gd_temp__rel_mod_rel_note')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_MODULE_SBOM]]
          - template not yet created
          - not started
          - <Link to issue>
          - <Link to WP>
          - <automated>

.. list-table:: Component Workproducts
        :header-rows: 1

        * - Workproduct Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - <Link to issue>
          - [[DOC__KVS_REQUIREMENTS]]
          - <automated>

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - <Link to issue>
          - [[DOC__KVS_REQUIREMENTS]]
          - <automated>

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - <Link to issue>
          - [[DOC__KVS_ARCHITECTURE]]
          - <automated>

        * - [[WP__SW_COMPONENT_SECURITY_ANALYSIS]]
          - [[WP__SW_COMPONENT_SECURITY_ANALYSIS]]
          - copy('status', need_id='wp__sw_component_security_analysis')
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - <Link to issue>
          - Checklist used in Pull Request Review
          - <automated>

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
          - Checklist used in Pull Request Review
          - <automated>

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to issue>
          - <Link to WP>
          - <automated>

# Special Note

Module security plan template will be refined and existing content will be synchronized as per new template.
