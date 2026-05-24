---
id: DOC-MODULE-SECURITY-PLAN-9444
title: Module Security Plan
type: specification
status: approved
tags: [eclipse-score]
---

# Security Plan

### [Your Module Name] Security Plan

{{artifact:DOC__MOD_TEMP_MODULE_NAME_SECURITY_PLAN:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in upper snake case preceded by ``doc_`` and succeeded by ``security_plan``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

  | **1. Security Management Context**
  | This Security Plan adds to the process security management guidance all the module development relevant work products needed for ISO SAE 21434 conformity.
   |
   | **2. Security Management Scope**
   | This Security Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
   | The module consists of one or more SW components and will be qualified as a OoC.
   |
   | **3. Security Management Roles**

   +---------------------------+--------------------------------------------------------------+
   | Security Manager          | <link to Module's Security Manager assignment or name>       |
   +---------------------------+--------------------------------------------------------------+
   | Project Manager           | <link to Module's Project Lead assignment or name>           |
   +---------------------------+--------------------------------------------------------------+

  | **4. Tailoring**
  | Additional to the tailoring in the SW platform project as defined in the process security management guidance we define here the additional tailoring on module level.
   |
   | - Excluded for this module are additionally the following work products (and their related requirements):
   |   - <ISO SAE 21434 reference>: <work product/requirement> - <Argumentation why it is not needed or replaced by another work product or activity.>
   |
   | **5. Security Module Work Products**
   | One set of work products for the module and one set for each component of the module:

.. list-table:: Module Work Products
        :header-rows: 1

        * - Work Product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - [[WP__MODULE_SECURITY_PLAN]]
          - Security management guideline
          - <automated>
          - <Link to issue>
          - this document
          - see above

        * - [[WP__MODULE_SECURITY_PACKAGE]]
          - Security management guideline
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__FDR_REPORTS]] (Module Security Plan)
          - [[GD_CHKLST__SECURITY_PLAN]]
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__FDR_REPORTS]] (Module Security Package)
          - Security Package Formal Review Checklist <gd_chklst__security_package>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__FDR_REPORTS]] (Module's Security Analyses)
          - Security Analysis FDR tbd
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__AUDIT_REPORT_SECURITY]]
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - Software Development Plan Template <gd_temp__software_development_plan>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__MODULE_SECURITY_MANUAL]]
          - [[GD_TEMP__MODULE_SECURITY_MANUAL]]
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - Verification process guidance
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - Release management guidance
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_MODULE_SBOM]]
          - Security management guidance
          - not started
          - <Link to issue>
          - <Link to WP>
          - <automated>

.. list-table:: Component <name> Work Products
        :header-rows: 1

        * - Work Product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - [[WP__REQUIREMENTS_COMP]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__REQUIREMENTS_INSPECT]]
          - <Link to process>
          - <automated>
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - [[WP__COMPONENT_ARCH]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_COMPONENT_SECURITY_ANALYSIS]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_ARCH_VERIFICATION]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_IMPLEMENTATION]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>
