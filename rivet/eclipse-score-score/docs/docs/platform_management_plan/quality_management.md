---
id: DOC-QUALITY-MANAGEMENT-36011
title: Quality Management
type: specification
status: approved
tags: [eclipse-score]
---

# Quality Management / Platform Quality Management Plan

### Platform Quality Management Plan

{{artifact:DOC__PLATFORM_QUALITY_PLAN:status,safety-level,security}}

## Purpose

The purpose of this document is to define a quality strategy and an approach for the platform.
This includes an approach to providing an independent and objective assurance that work products and processes
comply with predefined provisions and plans and that non-conformance is resolved and further prevented.
This document includes quality assurance activities, roles and responsibilities, goals, schedule, etc. and a
general strategy to implement quality assurance process in this platform. The quality assurance is
ensured by automated checks and restrictions, manual checks which includes to proof that there is no manipulation
of the workflows.

## Statement of Independence

The [[RL__QUALITY_MANAGER]] provides support to the project by consulting on quality improvements
for the project/platform product. The Quality Manager is independent of the product delivery process. The quality report
is approved by the [[RL__PROJECT_LEAD]].

In S-CORE we have different Tier and OEM stakeholder involved: Every solution will be checked by the other stakeholders.
This is another strong independent mechanism to ensure quality.

## Objectives and scope

#### 3.1 Quality Objectives

.. list-table:: Standards to comply with
    :header-rows: 1
    :widths: 15,85,15

    * - #
      - **Standard Name**
      - **Version**
    * - 1
      - Automotive SPICE PAM
      - 4.0
    * - 2
      - ISO 262626:2018
      - 2018
    * - 3
      - ISO/SAE 21434:2021
      - 2021
    * - 4
      - ISO PAS 8926:2024 (will be integrated into ISO 26262 3rd edition as updated part 8 clause 12)
      - 2024

#### 3.2 Quality Performance Objectives

.. list-table:: Quality assurance activities and frequency of performing them
    :header-rows: 1

    * - #
      - **Activities**
      - **Cadence**
    * - 1
      - Platform process audit
      - Once for every platform release or on demand
    * - 2
      - Feature process conformance checks
      - Once for every feature release
    * - 3
      - Work product review
      - Once for every feature release
    * - 4
      - Platform release verification and approval
      - Once for every release
    * - 5
      - Process consulting / Quality trainings
      - Continuously
    * - 6
      - Process monitoring / Process improvement
      - Continuously

#### 3.3 Quantitative Quality Goals

.. list-table:: Quantitative Quality Goals
    :header-rows: 1

    * - #
      - **Quality Criteria**
      - **Source**
      - **Target value**
      - **Allowed variation**
      - **Metric**
    * - 1
      - One Platform process audit per release
      - [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]], ../requirements/stakeholder/index
      - 100% of the Platform process audit has be done for every release
      - Delta audit allowed to achieve 100%
      - Ensured by the process quality management, [[WF__EXE_PLTPROCESS_AUDIT]] - Platform process audit is available
    * - 2
      - One process conformance check for every feature release
      - [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]], ../requirements/stakeholder/index
      - One process conformance check has been done for every stable feature release
      - Feature is released as experimental
      - Ensured by the process quality and tool management, [[WP__QMS_REPORT]] - Process conformance is available
    * - 3
      - Only quality-assured project/platform work products are delivered to the community
      - [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]], ../requirements/stakeholder/index
      - 100% of project/platform work products are quality-assured
      - Feature is released as experimental
      - Ensured by the process quality and tool management, [[WP__VERIFICATION_PLATFORM_VER_REPORT]] - Work products contain the verification of the quality assurance
    * - 4
      - Only quality-assured project/platform releases are delivered to the community
      - [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]], ../requirements/stakeholder/index
      - 100% of project/platform releases delivered to the community are quality-assured
      - Feature is released as experimental
      - Ensured by the process release management, [[WP__PLATFORM_SW_RELEASE_NOTE]] contain the verification and approval of the quality-assurance
    * - 5
      - Only quality-trained personnel are part of the [[RL__COMMITTER]]
      - [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]], ../requirements/stakeholder/index
      - 100% of personnel are trained as per committer role description in [[RL__COMMITTER]]
      - None
      - Ensured by the process platform management, [[WP__TRAINING_PATH]] contain the training material and evidences for conducted trainings
    * - 6
      - No overdue quality assurance closure activities
      - [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]], ../requirements/stakeholder/index
      - 100% of the quality improvement, non-conformance issues are closed
      - None
      - Ensured by the process quality management, [[WP__ISSUE_TRACK_SYSTEM]] contain improvements and non-conformance

#### 3.4 Work Product Quality Goals

For all generated work products, the following quality goals are defined:

**Quality Criteria**

All work products have to be available and valid. Templates, checklists, and guidelines shall be used.
Plans have to be up to date.

The training material shall be available in the training path.
The issues in the issue tracking system following the planning strategy.

**Target value**

The target value for all work products is 100%.

**Allowed variation**

There is no allowed variation for the work products.

**Metric**

The metric for the work products is ensured by the process that contains the work product. Only valid work products can be merged. Reviews are required and therefore checklists are prepared. If applicable, script based checks are implemented.

#### 3.5 Quality Management Scope

There is no deviation from the scope defined in the [[DOC__PROJECT_MGT_PLAN]]. The platform and it's
components are developed, and integrated for an assumed technical system, for functional safety purposes as
Safety Element out of Context (SEooC).

The development of the platform and it's components follows the defined processes. Responsibilities for management,
development, implementation, integration, and verification are also defined in the processes.

The SW platform consists of features, which are based on a set of requirements and are developed in parallel.

**Tailoring of quality assurance activities**

* The tailoring is divided into project wide and feature specific rules.
* Project wide tailoring is documented in `ASPICE 4.0 <https://eclipse-score.github.io/process_description/main/standards/aspice_40/aspice.html>`_ - this is based on the development of a SW element.

#### 3.6 Quality Management Organization

It is the project strategy to qualify the platform or components of the platform to the appropriate international
standards and directives. Therefore the project approach to facilitate a common culture regarding quality, safety
and security is part of the documentation. The project is stewarded by the Eclipse Foundation and so the
`Eclipse Foundation Project Handbook <https://www.eclipse.org/projects/handbook/>`_ applies.

**Project Roles**

The project roles are defined in the processes and are aligned to Eclipse roles.

.. needtable::
   :style: table
   :columns: title;id;tags
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["role"]):
                results.append(need)

**Skills**

The main quality related project roles are the [[RL__QUALITY_MANAGER]] and the [[RL__PROJECT_LEAD]]. These also have to have

the (Eclipse) committer role. As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the
committers are elected in a meritocratic manner, meaning those have to show their skills and understanding of the
project processes in several previous pull requests.

As each project can adopt additional criteria for the committers election, S-CORE defines that each committer has to prove
his knowledge in quality SW development by:

- by attending the project's ASPICE 4.0 SW management and development training.

The successful checking of the committers' skills and the independent roles is ensured by the [[RL__PROJECT_LEAD]]
and [[RL__QUALITY_MANAGER]] who record/check this in the role assignment document.

#### 4 Quality Management Planning

##### 4.1 Quality Resources

Dedicated [[RL__QUALITY_MANAGER]] are elected, following a methodology as done for the committers, which means in a meritocratic manner on project level.

The [[RL__QUALITY_MANAGER]], supported by the [[RL__PROJECT_LEAD]], and all other stakeholders,
will ensure that quality activities are actively planned, developed, analyzed, verified, tested, and managed throughout the life cycle of the project.

Resources and milestones are planned in Github Issues for all activities. Resource and
milestone planning is done as defined in the project_management.

**Tools**

The whole development and thus all work products are located in Github. The development is automated as much as
possible and follows the defined processes.

- Github issues are used for planning.
- The issue types and their workflows are described in the platform management plan.
- For quality relevant issue types the ``quality`` label is used.

##### 4.2 Quality Management Communication

To exchange general information and to clarify general topics, the following communication channels are used:
- Regular (online) meetings
- E-Mails
- Messenger Services e.g., Slack, Microsoft Teams, Github Notifications

Ad-hoc quality related meetings are set up for clarification topics.

**Reporting**

The quality management status [[WP__QMS_REPORT]] is reported as defined in the platform management plan.

**Escalation**

If needed a escalation can be done in three steps. First [[RL__QUALITY_MANAGER]] shall escalate to
the [[RL__PROJECT_LEAD]]. Then to the project lead circle, documented in [[DOC__PROJECT_MGT_PLAN]].
Finally to the Eclipse Foundation if the rules of the Eclipse handbook are not followed.

**Examples for valid escalation causes are:**

- Conflict between [[RL__QUALITY_MANAGER]] and [[RL__COMMITTER]] regarding quality issues.
- Quality issues cannot be resolved on feature level or with the available resources.
- There are conflicting points of view between the [[RL__PROJECT_LEAD]], [[RL__SAFETY_MANAGER]], [[RL__SECURITY_MANAGER]] and the [[RL__QUALITY_MANAGER]].

#### 4.3 Quality Management Specifics

None

#### 4.4 Quality Management Generic workproducts

.. list-table:: Quality related work products
        :header-rows: 1

        * - Workproduct Id
          - Link to WP

        * - [[WP__CHM_PLAN]]
          - project_documents_list

        * - [[WP__CMPT_REQUEST]]
          - documents_docs_modules_components

        * - [[WP__COMPONENT_ARCH]]
          - documents_docs_modules_components

        * - [[WP__DOCUMENT_MGT_PLAN]]
          - project_documents_list

        * - [[WP__FDR_REPORTS]]
          - documents_docs_modules

        * - [[WP__FEAT_REQUEST]]
          - documents_docs_features

        * - [[WP__FEATURE_ARCH]]
          - documents_docs_features

        * - [[WP__FEATURE_DFA]]
          - documents_docs_features

        * - [[WP__MODULE_SAFETY_MANUAL]]
          - documents_docs_modules

        * - [[WP__MODULE_SAFETY_PACKAGE]]
          - documents_docs_modules

        * - [[WP__MODULE_SAFETY_PLAN]]
          - documents_docs_modules

        * - [[WP__MODULE_SW_RELEASE_NOTE]]
          - documents_docs_modules

        * - [[WP__MODULE_SW_RELEASE_PLAN]]
          - documents_docs_modules

        * - [[WP__PLATFORM_DFA]]
          - project_documents_list

        * - [[WP__PLATFORM_SAFETY_MANUAL]]
          - project_documents_list

        * - [[WP__PLATFORM_SAFETY_PLAN]]
          - project_documents_list

        * - [[WP__PLATFORM_SAFETY_PACKAGE]]
          - project_documents_list

        * - [[WP__PLATFORM_SW_RELEASE_NOTE]]
          - project_documents_list

        * - [[WP__PLATFORM_SW_RELEASE_PLAN]]
          - project_documents_list

        * - [[WP__PRM_PLAN]]
          - project_documents_list

        * - [[WP__PROCESS_DESCRIPTION]]
          - [[WP__PROCESS_DESCRIPTION]]

        * - [[WP__PROCESS_IMPR_REPORT]]
          - project_documents_list

        * - [[WP__PROCESS_STRATEGY]]
          - [[WP__PROCESS_STRATEGY]]

        * - [[WP__PROJECT_MGT]]
          - project_documents_list

        * - [[WP__QMS_PLAN]]
          - project_documents_list

        * - [[WP__QMS_REPORT]]
          - project_documents_list

        * - [[WP__REQUIREMENTS_COMP]]
          - documents_docs_modules_components

        * - [[WP__REQUIREMENTS_COMP_AOU]]
          - documents_docs_modules_components

        * - [[WP__REQUIREMENTS_FEAT]]
          - documents_docs_features

        * - [[WP__REQUIREMENTS_FEAT_AOU]]
          - documents_docs_features

        * - [[WP__REQUIREMENTS_INSPECT]]
          - project_documents_list, documents_docs_modules

        * - [[WP__REQUIREMENTS_STKH]]
          - project_documents_list

        * - [[WP__SW_ARCH_VERIFICATION]]
          - project_documents_list, documents_docs_modules

        * - [[WP__SW_COMPONENT_CLASS]]
          - documents_docs_modules_components

        * - [[WP__SW_COMPONENT_DFA]]
          - documents_docs_modules_components

        * - [[WP__SW_COMPONENT_FMEA]]
          - documents_docs_modules_components

        * - [[WP__SW_COMPONENT_DFA]]
          - documents_docs_modules_components

        * - [[WP__SW_DEVELOPMENT_PLAN]]
          - project_documents_list

        * - [[WP__SW_IMPLEMENTATION]]
          - documents_docs_modules_components

        * - [[WP__SW_IMPLEMENTATION_INSPECTION]]
          - documents_docs_modules_components

        * - [[WP__TAILORING_WORK_PRODUCTS]]
          - project_documents_list, documents_docs_features, documents_docs_modules_components

        * - [[WP__TLM_PLAN]]
          - project_documents_list

        * - [[WP__TOOL_VERIFICATION_REPORT]]
          - project_documents_list

        * - [[WP__VERIFICATION_COMP_INT_TEST]]
          - documents_docs_modules_components

        * - [[WP__VERIFICATION_FEAT_INT_TEST]]
          - documents_docs_features

        * - [[WP__VERIFICATION_MODULE_VER_REPORT]]
          - documents_docs_modules

        * - [[WP__VERIFICATION_PLAN]]
          - project_documents_list, documents_docs_features, documents_docs_modules_components

        * - [[WP__VERIFICATION_PLATFORM_INT_TEST]]
          - project_documents_list

        * - [[WP__VERIFICATION_PLATFORM_VER_REPORT]]
          - project_documents_list

        * - [[WP__VERIFICATION_SW_UNIT_TEST]]
          - documents_docs_modules_components
