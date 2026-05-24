---
id: DOC-SAFETY-MANAGEMENT-77483
title: Safety Management
type: specification
status: approved
tags: [eclipse-score]
---


### Platform Safety Plan

{{artifact:DOC__SCORE_PLATFORM_SAFETY_PLAN:status,safety-level,security}}

.. _score_platform_safety_plan:

## Safety management / Platform Safety Plan

#### Purpose

The main purpose of the safety plan is to:

* adhere to ISO 26262 where applicable for the project according to the defined tailoring

And:

* to define and assign the roles and responsibilities regarding safety activities
* to define the tailored safety activities, to provide the corresponding rationales for tailoring and to review the provided rationales
* to plan the safety activities
* to coordinate and track the progress of safety activities in accordance with the safety plan
* to ensure a correct progression of the safety activities throughout the safety lifecycle
* to plan to create a comprehensible safety case (collection of the safety related work products)
* to judge whether the SW achieves functional safety process conformance (i.e. the functional safety audit, confirmation reviews)

#### Objectives and Scope

#### Functional Safety Management Goals

* Adherence to the ISO 26262 according to the defined tailoring

in detail

* to plan all functional safety related activities and work products
* to monitor and facilitate all activities
* to measure and report functional safety status based on well-defined metrics

#### Functional Safety Management Scope

There is no deviation from the scope presented in the `S-CORE project page <https://eclipse-score.github.io/>`_ .
The platform and its components are developed, and integrated for an assumed technical system as Safety Element out of Context (SEooC).
The development of the platform and its components follows the defined processes.
Responsibilities for development, implementation, integration and verification are also defined in the processes.

Regarding the platform specifics:

* the highest ASIL in the project is ASIL B
* all safety activities from a procedural point of view are developed according to ASIL B
* all safety related SW in the project is developed according to ISO 26262 ASIL B

The SW platform functionality consists of features, which are based on a set of requirements and are developed in parallel.
These features are developed into SW components contained in "modules", which are another set of SEooCs (initiated by a change request).
A template exists to guide this: [[GD_TEMP__MODULE_SAFETY_PLAN]].

#### Tailoring

Tailoring of safety activities:

* The tailoring is divided into project wide and module specific rules.
* Project wide tailoring is documented in this document - this is based on development of a platform SEooC.
* Module SEooC specific tailoring is documented in the module development Safety Plans - this may be based on SEooC specifics or because component qualification according to ISO 26262 part 8 clause 12 (or ISO PAS 8926) is selected.
* In case of a change request on an existing feature (i.e. a change request), the subsequent safety planning will be done based on an impact analysis.

The following  ISO 26262 defined safety work products are not relevant for the S-CORE SW platform development:

* Because these are in responsibility of the system integrator: [[STD_WP__ISO26262__MANAGEMENT_751]],
  [[STD_WP__ISO26262__SYSTEM_652]], [[STD_WP__ISO26262__SYSTEM_653]], [[STD_WP__ISO26262__SYSTEM_654]],
  [[STD_WP__ISO26262__SYSTEM_655]], [[STD_WP__ISO26262__SYSTEM_656]], [[STD_WP__ISO26262__SYSTEM_657]],
  [[STD_WP__ISO26262__SYSTEM_751]], [[STD_WP__ISO26262__SYSTEM_752]], [[STD_WP__ISO26262__SYSTEM_851]],
  [[STD_WP__ISO26262__SYSTEM_852]]

  Note that stakeholder requirements ([[STD_WP__ISO26262__SYSTEM_651]]) are in scope of the project,
  to be able to address System and HW related failures which are typically mitigated by SW (e.g. end-to-end protection for ECU external communication).
  However, these are considered "Assumed Technical Safety Requirements" of the SW platform SEooC and do not require testing by the SEooC supplier.
  Thus, system-level testing is out of scope. S-CORE will implement Platform Integration Tests of stakeholder requirements for demonstration purposes,
  but these are not intended to provide complete coverage of the stakeholder requirements.
  There will be SW integration tests of feature requirements as specified in ISO 26262 part 6-10.
  These tests may be reused by users on their HW platform to address Technical Safety Requirements for the SW platform.
  Whether these are sufficient to cover the TSRs must be analyzed and decided by the user.

  Therefore and as S-CORE only delivers source code, [[STD_WP__ISO26262__SOFTWARE_1052]] is tailored out.

* Also tailored out is the SW testing on the target, as the S-CORE project can only test on reference HW
  (part of SW integration testing). So these are not relevant: [[STD_WP__ISO26262__SOFTWARE_1151]], [[STD_WP__ISO26262__SOFTWARE_1152]]

* Because there is no calibration used for the S-CORE SW platform components, only configuration: [[STD_WP__ISO26262__SOFTWARE_APP_C_52]],
  [[STD_WP__ISO26262__SOFTWARE_APP_C_54]], [[STD_WP__ISO26262__SOFTWARE_APP_C_57]]

* Because distributed development is not how the project is organized. All contributors are seen as part of the project team.
  When used, OSS components are qualified and external SEooCs are integrated in the project scope: [[STD_WP__ISO26262__SUPPORT_551]],
  [[STD_WP__ISO26262__SUPPORT_552]], [[STD_WP__ISO26262__SUPPORT_553]], [[STD_WP__ISO26262__SUPPORT_554]], [[STD_WP__ISO26262__SUPPORT_555]], [[STD_REQ__ISO26262__MANAGEMENT_64610]]

* Because in the S-CORE SW platform HW elements are out of scope: [[STD_WP__ISO26262__SUPPORT_1351]], [[STD_WP__ISO26262__SUPPORT_1352]], [[STD_WP__ISO26262__SUPPORT_1353]], [[STD_REQ__ISO26262__MANAGEMENT_6454]]

* Because in the S-CORE SW platform a proven in use argument will not be applied: [[STD_WP__ISO26262__SUPPORT_1451]], [[STD_WP__ISO26262__SUPPORT_1452]], [[STD_REQ__ISO26262__MANAGEMENT_6453]]

* Because in the S-CORE SW platform interfacing of out of scope of ISO 26262 applications is not planned: [[STD_WP__ISO26262__SUPPORT_1551]]

* Because in the S-CORE SW platform integration of safety-related systems not developed according to ISO 26262 is not planned: [[STD_WP__ISO26262__SUPPORT_1651]]

* Because in the S-CORE SW platform no ASIL decomposition is planned: [[STD_WP__ISO26262__ANALYSIS_551]], [[STD_WP__ISO26262__ANALYSIS_552]].
  According to that also [[STD_REQ__ISO26262__ANALYSIS_641]], [[STD_REQ__ISO26262__ANALYSIS_642]], [[STD_REQ__ISO26262__ANALYSIS_643]], [[STD_REQ__ISO26262__ANALYSIS_644]] are tailored out for safety analyses.

* Because HSI is coming from HW (and systems) engineering which are not part of S-CORE
  and the standard only asks for refinement during SW development. As the input is missing, there is nothing to refine.
  Expectations towards the HW/Environment are covered by AoUs. Additionally S-CORE only provides reference HW integration,
  so every user of the platform would have to redo the effort anyway: [[STD_WP__ISO26262__SOFTWARE_652]]

* Because the SW platform is not an safety item but an element: [[STD_WP__ISO26262__MANAGEMENT_651]], hence impact analysis of the item level is tailored out

But also some activities based on requirements defining what has to be done to create a workproduct which is in scope of the S-CORE platform are tailored:

* Because those are not relevant for ASIL_B: [[STD_REQ__ISO26262__SYSTEM_6423]],
  [[STD_REQ__ISO26262__SYSTEM_6424]], [[STD_REQ__ISO26262__SYSTEM_6425]]

* Because S-CORE is not planning to do a safety assessment: [[STD_REQ__ISO26262__MANAGEMENT_64121]], [[STD_REQ__ISO26262__MANAGEMENT_64122]], [[STD_REQ__ISO26262__MANAGEMENT_64123]],
  [[STD_REQ__ISO26262__MANAGEMENT_64124]], [[STD_REQ__ISO26262__MANAGEMENT_64125]], [[STD_REQ__ISO26262__MANAGEMENT_64126]], [[STD_REQ__ISO26262__MANAGEMENT_64127]], [[STD_REQ__ISO26262__MANAGEMENT_64128]],
  [[STD_REQ__ISO26262__MANAGEMENT_64129]], [[STD_REQ__ISO26262__MANAGEMENT_641210]], [[STD_REQ__ISO26262__MANAGEMENT_641211]], [[STD_REQ__ISO26262__MANAGEMENT_641212]], [[STD_REQ__ISO26262__MANAGEMENT_641213]]

#### Approach

#### Safety Culture

The safety of the project S-CORE is inherent. It relies on the personal dedication and integrity of every person who is involved in the project.
The safety thinking in the project allows a questioning attitude and fosters the taking of responsibility.
Every participation, e.g. with the raise up of an improvement or by asking questions in the discussion section of GitHub is welcomed.
The processes, guidelines and templates define the organizational framework.
Adherence is verified by automated checks and manual inspections.
All the aspects of ISO 26262 are directly implemented in the development process to ensure a proper communication and high understanding of functional safety.
With continuous improvements, an integral aspect in all processes, we want to achieve excellence.

#### Cybersecurity Interface

Cybersecurity is a critical aspect of the overall safety culture and is recognized as an essential element in the development and operation of the S-CORE platform.
While functional safety and cybersecurity have distinct objectives, their interaction is managed through coordinated processes and shared responsibilities.

The project acknowledges the need to address cybersecurity risks that may impact safety. To this end, the following measures are implemented:

* Regular collaboration between the safety and cybersecurity teams to identify and assess potential cyber threats that could affect safety functions.
* Integration of cybersecurity considerations into safety analyses, including risk assessments, to ensure that cyber risks are systematically evaluated.
* Alignment of safety and cybersecurity requirements in the development lifecycle, with traceability between stakeholder safety requirements and relevant cybersecurity controls.
* Participation in cross-functional reviews and audits to ensure that both safety and cybersecurity requirements are met and that any conflicts are resolved.
* Continuous monitoring of emerging cybersecurity threats and updating the security plan accordingly; update the safety plan only if safety-related impacts are identified.

The project is committed to further strengthening the interface between safety and cybersecurity, and will regularly review and update its processes to reflect best practices and regulatory requirements.
This approach ensures that cybersecurity is not treated in isolation, but as an integral part of the platform's safety culture and management system.
The security management aspects are defined in the security_management.

#### Functional Safety Management Organization

It is the project strategy to qualify the platform or components of the platform to the appropriate international standards and directives.
Therefore the project approach to facilitate a common culture regarding safety and security is part of our documentation.
The project will be under the Eclipse Foundation and so the `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_ applies.

*Eclipse Roles*

* `Contributors <https://www.eclipse.org/projects/handbook/#contributing-contributors>`_ can be everyone and we will not discourage the open source community from this. As the contributor cannot merge code (or any other work product) into the project's codebase, the safety development competence of the contributor is irrelevant.
* `Committers <https://www.eclipse.org/projects/handbook/#contributing-committers>`_ play the main development role in the project, as only these are allowed to merge, so they are the ultimate responsible for the project's repository content.
* The Eclipse `Project Lead(s) <https://www.eclipse.org/projects/handbook/#roles-pl>`_ has the ISO 26262 project manager role.

*Project Roles*

Roles are defined in every process and in a generic roles section. All those are matched to Eclipse roles.
Project role assignment is documented in dedicated documents.

*Critical dependencies*

The project has not implemented a quality management system yet.
But it aims to be conform to ASPICE, as defined in the management system.
Continuous improvement is part to all processes. Improvements are handled in the scope of Quality Management.

*Risk*

Organization and management system has not a mature level yet.

*Skills*

The main safety related project roles are the project manager, the safety manager and the safety engineer, these also have to have the (Eclipse) committer role.
As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the committers are elected in a meritocratic manner, meaning those have to show their skills and understanding of the project processes in several previous pull requests.

For the [[RL__PROJECT_LEAD]], the [[RL__SAFETY_MANAGER]] and the [[RL__SAFETY_ENGINEER]] the required skills and experience are described
in these project role definitions. They are also elected in a meritocratic way and this election is documented including the evidences checked to prove the experience.

Committers in the S-CORE project can work on the development of safety related or non-safety related SW modules.
If they work on safety related modules they have to prove (additionally to their committer election, which already shows they are skilled developers):

* two years practice of safety related SW development (or management) relevant for the section content (includes trainings in safety standards like ISO 26262)
* training on the S-CORE processes

To ensure this, the platform and module repositories folders (and files) are protected by "CODEOWNER" sections.
These "CODEOWNERS" need to approve any pull request modifying a file in their area before it is merged.

The successful checking of CODEOWNERS experience is ensured by the safety manager and documented in the role assignment document.
One important aspect to this is, that we ensure the identity of the committer by applying the GitHub digital signature mechanism.

#### Functional Safety Resources

A dedicated safety manager is elected for all the S-CORE SEooCs development - see [[DOC__PLATFORM_SAFETY_MANAGER]].

The safety manager, supported by the project manager ([[RL__PROJECT_LEAD]]) or the assigned Feature team leads, will ensure that
safety activities are actively planned, developed, analyzed, verified and tested and managed throughout the life cycle of the project.
As all the implementation of safety functions takes place within module development, there is a responsible safety manager documented in the module's safety plan.

Resources and milestones are planned in Github Issues for all activities.
There are issue templates for sagas (covering one feature development) and for epics (covering one development work product each).
Resource and milestone planning is done as defined in the project_management

*Tools*

The whole development and thus all work products are located in Github. The development is automated as much as possible and follows the defined processes.
Github issues are used as planning tool.
The issue types and issue types workflows are described in the platform management plan.
For safety relevant issues types a "safety" label is used.

#### Functional Safety Management Communication

To exchange general information and to clarify general topics the following communication channels are used:

* Regular (online) meetings, at least every month.
* E-Mails
* Messenger Services e.g., Slack, Microsoft Teams, Github Notifications
* Ad hoc safety related meetings are set up for clarification topics.

*Reporting*

The safety management status is reported in the Project Lead Circle Meeting which is defined in [[DOC__PROJECT_MGT_PLAN]].
The status report is based on safety plans work product lists (see below) and verification reports on platform and module level:

* [[WP__PLATFORM_SAFETY_PLAN]]
* [[WP__MODULE_SAFETY_PLAN]]
* [[WP__VERIFICATION_PLATFORM_VER_REPORT]]
* [[WP__VERIFICATION_MODULE_VER_REPORT]]

*Escalation*

* [[RL__SAFETY_MANAGER]] to [[RL__PROJECT_LEAD]] (in the Project Lead Circle)

The Project Lead Circle is the ultimate decision instance within the S-CORE project.
But as in every Eclipse project the rules and committee decisions of Eclipse have to be followed.

Examples for valid escalation causes are:

* Safety issues cannot be resolved on module level or with the available resources.
* There are conflicting points-of-view between the module project manager (= Feature team lead) and any safety manager
* Safety anomalies detected by the safety manager are not accepted by the module project manager

#### Functional Safety Management Life Cycle

The safety lifecycle of the S-CORE project is initiated at the project set-up and driven and maintained by the safety manager supported by the [[RL__PROCESS_COMMUNITY]].
Note that the Eclipse Foundation also defines `project phases <https://www.eclipse.org/projects/handbook/#starting-project-phases>`_.
Eclipse definition is more about the process maturity for the whole project, if we are in Mature Phase, we latest will have the project lifecycle as defined in our process description.
Nevertheless, Safety Development and even Safety Case release is independent from Mature and Incubation Phase as the completeness and appropriateness of the platform process and artifacts
is determined by Safety Audit and not be Eclipse project reviews.
The S-CORE project implements a reduced ISO 26262 safety lifecycle, covering only those phases relevant to software SEooC development.
All omitted phases (e.g., HARA, system/hardware development, calibration, proven-in-use) are justified and documented in the Tailoring section.
All safety activities, planning, and evidence generation are tracked via the Platform Safety Plan, Module Safety Plans, and associated GitHub Issues.
This approach ensures compliance with ISO 26262 for software SEooC, while avoiding unnecessary activities not applicable to the S-CORE context.

#### Functional Safety Requirements

Requirement Engineering is defined in the process description. See [[DOC__PROJECT_MGT_PLAN]].

The application of ISO 26262 standards requirements is realized by defining process guidances and matching those to the ISO 26262 requirements (see e.g. for example [[GD_REQ__SAFETY_DOC_STATUS]]).

#### Functional Safety Schedule

The schedule is defined in section "Platform Safety Plan" below, but also within each module safety plan. See linked issues below and in [[GD_TEMP__MODULE_SAFETY_PLAN]].

#### Functional Safety Development

The SW development is defined in the project-wide software development plan. See software_development

#### Functional Safety Verification

The platform management plan defines the software_verification

#### Functional Safety Tool Management

The platform management plan defines tool_management

#### Functional Safety Work Products

The work products relevant for a module development is defined within each module safety management plan. See [[GD_TEMP__MODULE_SAFETY_PLAN]].
Generic project wide work products are defined below.

#### Functional Safety Quality Criteria

The platform management plan defines quality_management

#### Platform Safety Plan / Package

.. _sw_platform_wp_list:

#### Functional Safety/Security Management SW Platform Work Products

.. list-table:: SW Platform work products
    :header-rows: 1

    * - work product Id
      - Process status
      - Link to WP
      - WP status

    * - [[WP__POLICIES]]
      - n/a (comes from outside the project)
      - `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_
      - RELEASED

    * - [[WP__QMS_PLAN]]
      - copy('status', need_id='wf__cr_mt_qlm_plan')
      - [[DOC__PLATFORM_QUALITY_PLAN]]
      - copy('status', need_id='doc__platform_quality_plan')

    * - [[WP__ISSUE_TRACK_SYSTEM]]
      - copy('status', need_id='wf__platform_mr_im_platform_mgmt_plan')
      - `Project issues <https://github.com/eclipse-score/score/issues>`_
      - established

    * - [[WP__PLATFORM_MGMT]]
      - copy('status', need_id='wf__platform_cr_mt_platform_mgmt_plan')
      - index
      - copy('status', need_id='doc__platform_mgt_plan')

    * - [[WP__PROCESS_DESCRIPTION]]
      - copy('status', need_id='wf__def_app_process_description')
      - `Process description <https://eclipse-score.github.io/process_description/main/index.html>`_
      - Maturity Level 1-2

    * - [[WP__PROCESS_IMPR_REPORT]]
      - copy('status', need_id='wf__mon_imp_process_description')
      - `Process issues <https://github.com/eclipse-score/process_description/issues>`_
      - see issues

    * - [[WP__PROCESS_STRATEGY]]
      - copy('status', need_id='wf__cr_mt_process_mgt_strategy')
      - `Process development community planning <https://github.com/orgs/eclipse-score/projects/21>`_
      - see planning board

    * - [[WP__PLATFORM_HANDBOOK]]
      - copy('status', need_id='wf__rel_platform_handbook')
      - [[DOC__PLATFORM_HANDBOOK]]
      - copy('status', need_id='doc__platform_handbook')

    * - [[WP__PLATFORM_SW_RELEASE_NOTE]]
      - copy('status', need_id='wf__rel_platform_rel_note')
      - [[DOC__SCORE_V05_ALPHA_RELEASE_NOTE]]
      - copy('status', need_id='doc__score_v05_alpha_release_note')

    * - [[WP__VERIFICATION_PLATFORM_VER_REPORT]]
      - copy('status', need_id='wf__verification_platform_ver_report')
      - [[DOC__SCORE_PLATFORM_VERIFICATION_REPORT]]
      - copy('status', need_id='doc__score_platform_verification_report')

    * - [[WP__REQUIREMENTS_STKH]]
      - copy('status', need_id='wf__req_stkh_req')
      - [[DOC__STAKEHOLDER_REQUIREMENTS]]
      - copy('status', need_id='doc__stakeholder_requirements')

    * - [[WP__REQUIREMENTS_SW_PLATFORM_AOU]]
      - copy('status', need_id='wf__req_stkh_req')
      - [[DOC__PLATFORM_ASSUMPTIONS]]
      - copy('status', need_id='doc__platform_assumptions')

    * - [[WP__SW_DEVELOPMENT_PLAN]]
      - copy('status', need_id='wf__sw_development_plan')
      - [[DOC__SOFTWARE_DEVELOPMENT_PLAN]]
      - copy('status', need_id='doc__software_development_plan')

    * - [[WP__VERIFICATION_PLAN]]
      - copy('status', need_id='wf__verification_plan')
      - [[DOC__VERIFICATION_PLAN]]
      - copy('status', need_id='doc__verification_plan')

    * - [[WP__TOOL_VERIFICATION_REPORT]]
      - copy('status', need_id='wf__tool_create_tool_verification_report')
      - [[DOC__TOOL_EVALUATION_LIST]]
      - copy('status', need_id='doc__tool_evaluation_list')

#### Functional Safety Specific SW Platform Work Products

.. list-table:: SW Platform safety work products
    :header-rows: 1

    * - work product Id
      - Process status
      - Link to WP
      - WP status

    * - [[WP__PLATFORM_SAFETY_PLAN]]
      - copy('status', need_id='wf__cr_mt_safety_plan')
      - this document
      - see above

    * - [[WP__PLATFORM_SAFETY_PACKAGE]]
      - copy('status', need_id='wf__cr_mt_safety_package')
      - this document
      - see above

    * - [[WP__FDR_REPORTS]] (platform Safety Plan)
      - copy('status', need_id='wf__p_formal_rv')
      - [[DOC__SCORE_PLATFORM_SAFETY_PLAN_FDR]]
      - copy('status', need_id='doc__score_platform_safety_plan_fdr')

    * - [[WP__FDR_REPORTS]] (platform Safety Package)
      - copy('status', need_id='wf__p_formal_rv')
      - [[DOC__SCORE_PLATFORM_SAFETY_PACKAGE_FDR]]
      - copy('status', need_id='doc__score_platform_safety_package_fdr')

    * - [[WP__FDR_REPORTS]] (feature's Safety Analyses & DFA)
      - copy('status', need_id='wf__p_formal_rv')
      - [[DOC__SCORE_PLATFORM_SAFETY_ANALYSIS_FDR]]
      - copy('status', need_id='doc__score_platform_safety_analysis_fdr')

    * - [[WP__AUDIT_REPORT]]
      - performed by external experts
      - `Audit findings <https://github.com/eclipse-score/process_description/issues/518>`_
      - intermediate

    * - [[WP__PLATFORM_DFA]]
      - copy('status', need_id='wf__analyse_platform_featarch')
      - [[DOC__PLATFORM_DFA]]
      - copy('status', need_id='doc__platform_dfa')

    * - [[WP__PLATFORM_SAFETY_MANUAL]]
      - copy('status', need_id='wf__cr_mt_safety_manual')
      - [[DOC__SCORE_PLATFORM_SAFETY_MANUAL]]
      - copy('status', need_id='doc__score_platform_safety_manual')

    * - [[WP__SAFETY_TAILORING]] (generic)
      - copy('status', need_id='wf__def_app_process_description')
      - [[WP__TAILORING_WORK_PRODUCTS]] & [[DOC__SCORE_PLATFORM_SAFETY_PLAN]]
      - copy('status', need_id='wp__tailoring_work_products')

Process status: Status of the workflow which "outputs" the work product, derived from the docs it "has" and guidances it "contains".

Link to project planning: `Platform safety work product issue for V1.0 <https://github.com/eclipse-score/score/issues/2465>`_

#### Platform Management Plan - Feature Work Product Lists

[[DOC__BASELIBS_SAFETY_WP]]

[[DOC__COM_IPC_SAFETY_WP]]

[[DOC__FEO_SAFETY_WP]]

[[DOC__ORCHESTRATION_SAFETY_WP]]

[[DOC__PERSISTENCY_SAFETY_WP]]

Note: list of features according to releases

#### Platform Management Plan - Documents Status Chart

See doc_platform_management_plan

#### Deviations from Platform Safety Plan

The following deviations from the platform safety plan are present in the platform safety package.
These are deviations from planned processes execution and/or work product results,
safety anomalies in the sense of known bugs in the software are reported in the release notes (of the platform's modules).

<Describe here the deviations, whether they have an impact on platform safety functions,
how these can be mitigated or argued and if and when a resolution is planned.>
