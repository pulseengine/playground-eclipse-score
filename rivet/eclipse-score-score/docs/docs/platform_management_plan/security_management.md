---
id: DOC-SECURITY-MANAGEMENT-94824
title: Security Management
type: specification
status: approved
tags: [eclipse-score]
---

### Platform Security Plan

{{artifact:DOC__SCORE_PLATFORM_SECURITY_PLAN:status,safety-level,security}}

## Security management / Platform Security Plan

#### Purpose

The main purpose of the security plan is to:

* adhere to ISO SAE 21434 where applicable for the project according to the defined tailoring

And:

* to define and assign the roles and responsibilities regarding security activities
* to define the tailored security activities, to provide the corresponding rationales for tailoring and to review the provided rationales
* to plan the security activities
* to coordinate and track the progress of security activities in accordance with the security plan
* to ensure a correct progression of the security activities throughout the security lifecycle
* to plan to create a comprehensible security package (collection of the security related work products)
* to judge whether the SW achieves security process conformance

The term security is used here synonymously for the term cybersecurity as defined in ISO SAE 21434.

#### Objectives and Scope

#### Security Management Goals

* Adherence to the ISO SAE 21434 according to the defined tailoring

in detail

* to plan all security related activities and work products
* to monitor and facilitate all activities
* to measure and report security status based on well-defined metrics

#### Security Management Scope

There is no deviation from the scope presented in the `S-CORE project page <https://eclipse-score.github.io/>`_ .
The platform and its components are developed, and integrated for an assumed technical system as platform and components Out of Context (OoC).
The development of the platform and its components follows the defined processes.
Responsibilities for development, implementation, integration and verification are also defined in the processes.

Regarding the platform specifics:

* SW in the project is either security relevant or not
* if relevant, security activities from a procedural point of view and SW are developed using additional rigour

The SW platform functionality consists of features, which are based on a set of requirements and are developed in parallel.
These features are developed into SW components contained in "modules", which are another set of OoCs (initiated by a change request).
A template exists to guide this: [[GD_TEMP__MODULE_SECURITY_PLAN]].

#### Tailoring

Tailoring of security activities:

* The tailoring is divided into project wide and module specific rules.
* Project wide tailoring is documented in this document - this is based on development of a platform OoC.
* Module OoC specific tailoring is documented in the module development Security Plans - this may be based on OoC specifics
* In case of a change request on an existing feature (i.e. a feature modification request), the subsequent security planning will be done based on an impact analysis.

The following ISO SAE 21434 defined security work products are not relevant for the S-CORE SW platform development:

Because Eclipse OSS project handbook applies and all content is public: [[STD_WP__ISOSAE21434__ORG_MANAGEMENT_551]],

Because these are in responsibility of the system integrator: [[STD_WP__ISOSAE21434__ORG_MANAGEMENT_551]],
[[STD_WP__ISOSAE21434__ORG_MANAGEMENT_555]], [[STD_WP__ISOSAE21434__PRJ_MANAGEMENT_653]],
[[STD_WP__ISOSAE21434__ASSESSMENT_15331]], [[STD_WP__ISOSAE21434__ASSESSMENT_15332]],
[[STD_WP__ISOSAE21434__ASSESSMENT_15431]], [[STD_WP__ISOSAE21434__ASSESSMENT_15531]]

Summary: [[WP__TAILORING_WORK_PRODUCTS]] links to all the work products which are tailored out in the platform security plan,
to be able to demonstrate completeness in `REPLACE_external_standards`

#### Approach

#### Security Culture

The security of the project S-CORE is inherent. It relies on the personal dedication and integrity of every person who is involved in the project.
The security thinking in the project allows a questioning attitude and fosters the taking of responsibility.
Every participation, e.g. with the raise up of an improvement or by asking questions in the discussion section of GitHub is welcomed.
The processes, guidelines and templates define the organizational framework.
Adherence is verified by automated checks and manual inspections.
All the aspects of ISO SAE 21434 are directly implemented in the development process to ensure a proper communication and high understanding of security.
With continuous improvements, an integral aspect in all processes, we want to achieve excellence.

#### Security Management Organization

It is the project strategy to qualify the platform or components of the platform to the appropriate international standards and directives.
Therefore the project approach to facilitate a common culture regarding safety and security is part of our documentation.
The project will be under the Eclipse Foundation and so the `Eclipse Foundation Project Handbook: <https://www.eclipse.org/projects/handbook/>`_ applies.

*Eclipse Roles*

* `Contributors <https://www.eclipse.org/projects/handbook/#contributing-contributors>`_ can be everyone and we will not discourage the open source community from this. As the contributor cannot merge code (or any other work product) into the project's codebase, the security development competence of the contributor is irrelevant.
* `Committers <https://www.eclipse.org/projects/handbook/#contributing-committers>`_ play the main development role in the project, as only these are allowed to merge, so they are the ultimate responsible for the project's repository content.
* `Eclipse Foundation Security Team <https://www.eclipse.org/projects/handbook/#vulnerability-team>`_ provides help and advice to Eclipse projects on security issues and is the first point of contact for handling security vulnerabilities.

*Project Roles*

Roles are defined in every process and in a generic roles section. All those are matched to Eclipse roles.
Project role assignment is done in every feature development Security Plan.

*Critical dependencies*

The project has implemented a quality management system, aiming to be conform to ASPICE, as defined in the management system.
Continuous improvement is part to all processes. Improvements are handled in the scope of Quality Management.

*Risk*

Organization and management system has not a compliant mature level yet.

*Skills*

The main security related project roles are the project manager and the security manager and these also have to have the (Eclipse) committer role.
As defined in `Committer Training <https://www.eclipse.org/projects/training/>`_ the committers are elected in a meritocratic manner, meaning those have to show their skills and understanding of the project processes in several previous pull requests.

As each project can adopt additional criteria for the committers election, we define the following:

each committer has to prove their knowledge in security SW development by

* an absolved training in ISO SAE 21434 (or equivalent standard, at least 16h of SW development specific training by a trusted training provider) OR
* by attending the projects's ISO SAE 21434 SW development training (given by a security team member)

Additionally, the project repository shall be organized in a way that independent roles (to the technical solution) have to approve any pull request before it’s merged.

In case of security related sections (e.g. a file containing feature requirements with a security relevance) the persons having approver rights need to have:
* One year of professional practice of security related SW development (or management) relevant for the section content

The successful checking of committers and independent role skills is ensured by the security manager and documented in the role assignment document.
One important aspect to this is, that we ensure the identity of the committer by applying the GitHub digital signature mechanism.

*Policies*
The `Eclipse Foundation Security Policy <https://www.eclipse.org/security/policy/>`_ apply for S-CORE.

#### Security Resources

Security managers are elected by [[RL__PROJECT_LEAD]] for all the S-CORE OoCs development.

The security manager, supported by the project manager (i.e. the [[RL__PROJECT_LEAD]]),  will ensure that
security activities are actively planned, developed, analyzed, verified and tested and managed throughout the life cycle of the project.
As all the implementation of security functions takes place within module development, there is a security manager appointed in the module's security plan.

Resources and milestones are planned in Github Issues for all activities.
There are issue templates covering one feature development and for covering one development work product each.
Resource and milestone planning is done as defined in the project_management

*Tools*

The whole development and thus all work products are located in Github. The development is automated as much as possible and follows the defined processes.
Github issues are used as planning tool as well as security information (weakness, vulnerability) reporting and managing tool.
The issue types and issue types workflows are described in the platform management plan.
For security relevant issues types a "security" label is used.

Reporting of vulnerabilities is supported here: `Eclipse general vulnerability tracker <https://gitlab.eclipse.org/security>`_.

#### Security Management Communication

To exchange general information and to clarify general topics the following communication channels are used:

* Regular (online) meetings, at least every month.
* E-Mails
* Messenger Services e.g., Slack, Microsoft Teams, Github Notifications
* Ad hoc security related meetings are set up for clarification topics.

*Reporting*

The security management status is reported in the Technical Lead Circle Meeting which is defined in [[DOC__PROJECT_MGT_PLAN]].
The status report is based on security plans work product lists (see below) and verification reports on platform and module level:

* [[WP__PLATFORM_SECURITY_PLAN]]
* [[WP__MODULE_SECURITY_PLAN]]
* [[WP__VERIFICATION_PLATFORM_VER_REPORT]]
* [[WP__VERIFICATION_MODULE_VER_REPORT]]

*Escalation*

* Security Manager [[RL__SECURITY_MANAGER]] to steering committee documented in [[DOC__PROJECT_MGT_PLAN]].

Examples for valid escalation causes are:

* Security issues cannot be resolved on module level or with the available resources.
* There are conflicting points of view between the Project Lead [[RL__PROJECT_LEAD]], Safety Manager [[RL__SAFETY_MANAGER]], Security Manager [[RL__SECURITY_MANAGER]] and the Quality Manager [[RL__QUALITY_MANAGER]]

#### Security Management Lifecycle

The security lifecycle of the S-CORE project is initiated at the project set-up and driven and maintained by the security manager supported by the [[RL__PROCESS_COMMUNITY]].
Note that the Eclipse Foundation also defines `project phases <https://www.eclipse.org/projects/handbook/#starting-project-phases>`_.
Eclipse definition is more about the process maturity for the whole project, if we are in Mature Phase, we latest will have the project lifecycle as defined in our process description.
Nevertheless, Security Development and even Security Package release is independent from Mature and Incubation Phase as the completeness and appropriateness of the platform process and artifacts
is determined by Security Audit and not be Eclipse project reviews.

#### Security Requirements

Requirement Engineering is defined in the process description. See See software_development.

The application of ISO SAE 21434 standards requirements is realized by defining process guidances and matching those to the ISO SAE 21434 requirements (see `REPLACE_processes_introduction`).

#### Security Schedule

The schedule is defined in section "Platform Security Plan" below, but also within each module security plan. See linked issues below and in need:`gd_temp__module_security_plan`.

#### Security SW Development

The SW development is defined in the project-wide software development plan. See software_development.

#### Security Verification

The platform management plan defines the software_verification

#### Security Tool Management

The platform management plan defines tool_management

#### Security Work Products

The work products relevant for a module development is defined within each module security management plan. See [[GD_TEMP__MODULE_SECURITY_PLAN]].
Generic project wide work products are defined below.

#### Security Quality Criteria

The platform management plan defines quality_management

#### Platform Security Plan

#### Functional Safety/Security Management SW Platform Work Products

see sw_platform_wp_list

#### Security Specific SW Platform Work Products

.. list-table:: SW Platform security work products
    :header-rows: 1

    * - work product Id
      - Process status
      - Link to WP
      - WP status

    * - [[WP__PLATFORM_SECURITY_PLAN]]
      - copy('status', need_id='wf__cr_mt_security_plan')
      - this document
      - see above

    * - [[WP__PLATFORM_SECURITY_PACKAGE]]
      - copy('status', need_id='wf__cr_mt_security_package')
      - <Link to WP>
      - <automated>

    * - [[WP__FDR_REPORTS_SECURITY]] (platform Security Plan)
      - copy('status', need_id='wf__p_formal_security_rv')
      - <Link to WP>
      - <automated>

    * - [[WP__FDR_REPORTS_SECURITY]] (platform Security Package)
      - copy('status', need_id='wf__p_formal_security_rv')
      - <Link to WP>
      - <automated>

    * - [[WP__FDR_REPORTS_SECURITY]] (feature's Security Analyses)
      - <Process Status>
      - <Link to WP>
      - <automated>

    * - [[WP__AUDIT_REPORT_SECURITY]]
      - performed by external experts
      - n/a
      - currently tailored out

    * - [[WP__PLATFORM_SECURITY_MANUAL]]
      - copy('status', need_id='wf__cr_mt_security_manual')
      - <Link to WP>
      - <automated>

    * - [[WP__TAILORING_WORK_PRODUCTS]] (generic)
      - copy('status', need_id='wf__def_app_process_description')
      - [[DOC__PLATFORM_SECURITY_PLAN]]
      - copy('status', need_id='doc__platform_security_plan')

    * - [[WP__SW_PLATFORM_SBOM]]
      - copy('status', need_id='wf__cr_mt_security_sbom')
      - <Link to WP>
      - <automated>

Process status: Status of the workflow which "outputs" the work product, derived from the docs it "has" and guidances it "contains".

#### Security Management Feature Specific Work Products

See feature tree documents (created by using [[DOC__FEATURE_NAME_SECURITY_WP]]):

<link to document for every feature>

#### Security Work Products Status Charts

.. needtable::
   :style: table
   :columns: title;id;status;realizes
   :colwidths: 25,25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["document"]):
      if need and "platform_management" in need["tags"]:
                results.append(need)
