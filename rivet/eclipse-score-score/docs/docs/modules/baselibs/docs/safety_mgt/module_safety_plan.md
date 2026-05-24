---
id: DOC-MODULE-SAFETY-PLAN-17316
title: Module Safety Plan
type: specification
status: approved
tags: [eclipse-score]
---

# Module Safety Plan

### Baselibs Safety Plan

{{artifact:DOC__BASELIBS_SAFETY_PLAN:status,safety-level,security}}

# Functional Safety Management Context

This Safety Plan adds to the [[DOC__SCORE_PLATFORM_SAFETY_PLAN]] all the module development relevant work products needed for ISO 26262 conformity.

# Functional Safety Management Scope

This Safety Plan's scope is a SW module of the SW platform baselibs_module_docs.
The module consists of one or more SW components and will be qualified as a SEooC.

# Functional Safety Management Roles

.. list-table:: Module roles
        :header-rows: 1

        * - Role
          - Assignee

        * - Safety Manager
          - Alexander Schemmel

        * - Module Project Manager (= Feature team lead)
          - Andrey Babanin

# Tailoring

Additional to the tailoring in the SW platform project as defined in the [[DOC__SCORE_PLATFORM_SAFETY_PLAN]]  we define here the additional tailoring on module level.

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
          - [[DOC__BASELIBS_SAFETY_PLAN_FDR]]

        * - [[WP__FDR_REPORTS]] (module Safety Package)
          - [[GD_CHKLST__SAFETY_PACKAGE]]
          - copy('status', need_id='gd_chklst__safety_package')
          - [[DOC__BASELIBS_SAFETY_PACKAGE_FDR]]

        * - [[WP__FDR_REPORTS]] (module's Safety Analyses & DFA)
          - [[GD_CHKLST__SAFETY_ANALYSIS]]
          - copy('status', need_id='gd_chklst__safety_analysis')
          - [[DOC__BASELIBS_SAFETY_ANALYSIS_FDR]]

        * - [[WP__AUDIT_REPORT]]
          - performed by external experts
          - n/a
          - see platform safety plan

        * - [[WP__MODULE_SAFETY_MANUAL]]
          - [[GD_TEMP__SAFETY_MANUAL]]
          - copy('status', need_id='gd_temp__safety_manual')
          - [[DOC__BASELIBS_SAFETY_MANUAL]]

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - [[GD_TEMP__MOD_VER_REPORT]]
          - copy('status', need_id='gd_temp__mod_ver_report')
          - [[DOC__BASELIBS_VERIFICATION_REPORT]]

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - [[GD_TEMP__REL_MOD_REL_NOTE]]
          - copy('status', need_id='gd_temp__rel_mod_rel_note')
          - [[DOC__BASELIBS_RELEASE_NOTE]]

## Component bitmanipulation Work products List

.. list-table:: Component bitmanipulation Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__BITMANIPULATION_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__BITMANIPULATION_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__BITMANIPULATION_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__BITMANIPULATION_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__BITMANIPULATION_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__BITMANIPULATION_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__BITMANIPULATION_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `.h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/bitmanipulation>`_, `design <https://github.com/eclipse-score/baselibs/tree/main/score/bitmanipulation/design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/bitmanipulation>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__BITMANIPULATION_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component concurrency Work products List

.. list-table:: Component concurrency Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__CONCURRENCY_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__CONCURRENCY_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__CONCURRENCY_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__CONCURRENCY_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__CONCURRENCY_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__CONCURRENCY_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__CONCURRENCY_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `concurrency .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/concurrency>`_, `concurrency/design <https://github.com/eclipse-score/baselibs/tree/main/score/concurrency/design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `concurency/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/concurrency>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__CONCURRENCY_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component containers Work products List

.. list-table:: Component containers Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__CONTAINERS_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__CONTAINERS_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__CONTAINERS_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__CONTAINERS_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__CONTAINERS_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__CONTAINERS_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__CONTAINERS_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `containers .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/containers>`_, `containers/design <https://github.com/eclipse-score/baselibs/tree/main/score/containers/design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `containers/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/containers>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__CONTAINERS_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component filesystem Work products List

.. list-table:: Component filesystem Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__FILESYSTEM_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__FILESYSTEM_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__FILESYSTEM_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__FILESYSTEM_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__FILESYSTEM_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__FILESYSTEM_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__FILESYSTEM_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `filesystem .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/filesystem>`_, `filesystem/design <https://github.com/eclipse-score/baselibs/tree/main/score/filesystem/design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `filesystem/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/filesystem>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__FILESYSTEM_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component result Work products List

.. list-table:: Component result Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__RESULT_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__RESULT_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__RESULT_LIBRARY_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__RESULT_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__RESULT_LIB_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__RESULT_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__RESULT_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `result .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/result>`_, `result/design <https://github.com/eclipse-score/baselibs/tree/main/score/result/design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `result/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/result>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__RESULT_LIB_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component SafeCpp Work products List

.. list-table:: Component SafeCpp Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__SAFECPP_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__SAFECPP_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__SAFECPP_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__SAFECPP_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__SAFECPP_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__SAFECPP_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__SAFECPP_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `safecpp .h/.cpp <https://github.com/eclipse-score/baselibs/blob/main/score/language/safecpp>`_, `safecpp/design <https://github.com/eclipse-score/baselibs/blob/main/score/language/safecpp/Readme.md>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `safecpp/test.cpp <https://github.com/eclipse-score/baselibs/blob/main/score/language/safecpp/Readme.md>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__SAFECPP_ARC_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component Static Reflection Work products List

.. list-table:: Component Static Reflection Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__STATIC_REFLECT_SERIAL_LIB_REQ]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__STATIC_REFLECT_SERIAL_LIB_REQ]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__STATIC_REFLECTION_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__STATIC_REFL_WITH_SERIAL_ARCH]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__STATIC_REFLECTION_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__STATIC_REFLECTION_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__STATIC_REFLECTION_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `static_reflection .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/static_reflection_with_serialization>`_, `static_reflection/design <https://github.com/eclipse-score/baselibs/blob/main/score/static_reflection_with_serialization/serialization/ser_dser_lib.md>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `static_reflection/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/static_reflection_with_serialization>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__STATIC_REFLECTION_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component utils Work products List

.. list-table:: Component utils Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__UTILS_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__UTILS_LIB_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__UTILS_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__UTILS_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__UTILS_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__UTILS_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__UTILS_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `utils .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/utils>`_, `utils/design <https://github.com/eclipse-score/baselibs/tree/main/score/utils/design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `utils/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/utils>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__UTILS_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - component integration not needed (no sub-components and units are independent)

## Component json Work products List

.. list-table:: Component json Work products
        :header-rows: 1

        * - Work product Id
          - Link to process
          - Process status
          - Link to WP

        * - [[WP__REQUIREMENTS_COMP]]
          - [[GD_TEMP__REQ_COMP_REQ]]
          - copy('status', need_id='gd_temp__req_comp_req')
          - [[DOC__JSON_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - [[GD_TEMP__REQ_AOU_REQ]]
          - copy('status', need_id='gd_temp__req_aou_req')
          - [[DOC__JSON_REQUIREMENTS]]

        * - [[WP__REQUIREMENTS_INSPECT]]
          - [[GD_CHKLST__REQ_INSPECTION]]
          - copy('status', need_id='gd_chklst__req_inspection')
          - [[DOC__JSON_REQ_INSPECTION]]

        * - [[WP__COMPONENT_ARCH]]
          - [[GD_TEMP__ARCH_COMP]]
          - copy('status', need_id='gd_temp__arch_comp')
          - [[DOC__JSON_ARCHITECTURE]]

        * - [[WP__SW_ARCH_VERIFICATION]]
          - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__arch_inspection_checklist')
          - [[DOC__JSON_ARC_INSPECTION]]

        * - [[WP__SW_COMPONENT_FMEA]]
          - [[GD_TEMP__COMP_SAF_FMEA]]
          - copy('status', need_id='gd_temp__comp_saf_fmea')
          - [[DOC__JSON_FMEA]]

        * - [[WP__SW_COMPONENT_DFA]]
          - [[GD_TEMP__COMP_SAF_DFA]]
          - copy('status', need_id='gd_temp__comp_saf_dfa')
          - [[DOC__JSON_DFA]]

        * - [[WP__SW_IMPLEMENTATION]]
          - [[GD_GUIDL__IMPLEMENTATION]]
          - copy('status', need_id='gd_guidl__implementation')
          - `json .h/.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/json>`_, `json/design <https://github.com/eclipse-score/baselibs/tree/main/score/json/detailed_design>`_

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - `json/test.cpp <https://github.com/eclipse-score/baselibs/tree/main/score/json>`_

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - [[GD_CHKLST__IMPL_INSPECTION_CHECKLIST]]
          - copy('status', need_id='gd_chklst__impl_inspection_checklist')
          - [[DOC__JSON_IMPL_INSPECTION]]

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - [[GD_GUIDL__VERIFICATION_GUIDE]]
          - copy('status', need_id='gd_guidl__verification_guide')
          - <Link to WP>

        * - [[WP__SW_COMPONENT_CLASS]]
          - [[TSF__TRUST__TRUSTABLE-SOFTWARE]]
          - copy('status', need_id='gd_guidl__component_classification')
          - `TSF Report on nlohman/json <https://eclipse-score.github.io/inc_nlohmann_json/main/report.html>`_

All other components of the baselibs module as released in the [[DOC__BASELIBS_RELEASE_NOTE]]
are not planned to be qualifiable stand alone (as SEooC), but only in context, for example as they are used
in other S-CORE modules (e.g. communication). To be qualifiable in context those come with unit tests,
are implemented according to defined coding and detailed design guidelines, achieve the required structural coverage
and fulfill the AoUs of the reference OS (e.g. don’t use banned functions).

## Link to project planning

see epic `Baselibs safety work product issue for V1.0 <https://github.com/eclipse-score/baselibs/issues/148>`_

# Module Safety Package

To create the safety package (according to [[GD_GUIDL__SAF_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Module Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_modules_baselibs_docs

## Component Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_modules_baselibs_components

## Component Requirements Status

.. needtable::
   :filter: docname is not None and "baselibs" in docname and "requirements" in docname
   :style: table
   :types: comp_req
   :tags: baselibs
   :columns: id;status;tags;fulfilled by
   :colwidths: 25,5,20,25
   :sort: tags

## Component AoU Status

.. needtable::
   :filter: docname is not None and "baselibs" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: baselibs
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: tags

## Component Architecture Status

.. needtable::
   :filter: docname is not None and "baselibs" in docname
   :style: table
   :types: comp_arc_sta; comp_arc_dyn
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

## Deviations from Module Safety Plan

The following deviations from the module safety plan are present in the module safety package.
These are deviations from planned processes execution and/or work product results,
safety anomalies in the sense of known bugs in the software are reported in the release notes.

<Describe here the deviations, whether they have an impact on module's safety functions,
how these can be mitigated or argued and if and when a resolution is planned.>
