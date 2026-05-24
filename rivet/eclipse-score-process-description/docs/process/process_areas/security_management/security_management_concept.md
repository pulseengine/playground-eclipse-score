---
id: DOC-SECURITY-MANAGEMENT-CONCEPT-4458
title: Security Management Concept
type: specification
status: approved
tags: [eclipse-score]
---

.. _process_security_management:

# Concept Description

### Concept Description

{{artifact:DOC_CONCEPT__SECURITY_MANAGEMENT_PROCESS:status,safety-level,security}}

In this section a concept for the security management will be discussed. Inputs for this concepts
are mainly the requirements of ISO SAE 21434 Clause 5, 6 and 8.

# Key concept

The Security Management Plan establishes a comprehensive strategy for managing all identified security activities throughout the entire project life cycle.
It ensures that these activities are executed in a systematic, effective, and repeatable manner, providing clear guidance on responsibilities, processes, and control measures.
This approach supports risk mitigation, regulatory compliance, and continuous improvement, enabling the project team to maintain secrity standards consistently from initiation to completion.

# Inputs

#. Stakeholders for the security management work products?
#. Which security plans do we have?
#. Which other work products of security management are important?
#. What tooling do we need?

# Stakeholders for the Security Management

#. Security Manager <rl__security_manager>

   * is the main responsible for the security management work products (as in security_management_workproducts).
     See also role definition in security_management_roles.

#. Security Engineer <rl__security_engineer>

   * is the main responsible for the security engineering work products (as in ../security_analysis/security_analysis_workproducts).
     See also role definition in Security Engineer <rl__security_engineer>.

#. Project Lead <rl__project_lead>

   * is overall approver for security management activities.
   * For more details refer the role definition in Project Lead <rl__project_lead>.

#. Committer <rl__committer>

   * creates and maintains SBOM
   * reports weaknesses and vulnerabilities

#. Committer <rl__contributor>

   * reports weaknesses and vulnerabilities

#. External Security Auditor <rl__security_external_auditor>

   * understand activities planning, processes definition and execution (needs review, if we consider that)

#. Safety Manager <rl__safety_manager>

   * Supports activities

#. Infrastructure/Tooling community <rl__infrastructure_tooling_community>, Process community <rl__process_community>, Process community <rl__security_team>

   * Supports the creation and maintenance of the SBOM

# Security Plans

This SW platform project defines two levels of planning: platform and module. There will be one Security Plan on platform level and several Security Plans on module level (one for each module).
This is how we organize our development teams and repositories. Each of these Security Plan "creates" one component OoC.
The [[WP__PLATFORM_SECURITY_PLAN]] exists only once and is part of the [[WP__PLATFORM_MGMT]] of the development project.

# Security Management Work Products

Apart from the security plans the main work products of security management are (see also the link to workflows below):

* Security Manual <wp__platform_security_manual> - the Security Manual defines the requirements for safe and secure usage or integration of the SW platform (or its individual modules)
* Reviews <wp__fdr_reports_security> - on Security Plan, Security Package and Security Analyses, according to ISO SAE 21434 requirements
* Security Package <wp__platform_security_package> - the Security Package does not contain the security argumentation. By this the development project ensures it does not take over liability for the SW platform (or its individual modules). But it enables the distributors to integrate the SW platform (or its individual modules) in their Security Package.

# Security Management Tooling

For the security planning and security manual a “docs-as-code” approach is used and within that approach Id will be used for referencing.

For the activities planning (who, when) we use [[WP__ISSUE_TRACK_SYSTEM]] to create and manage issues, and monitor progress through a project management dashboard.

Also, refer [[WF__MR_SEC_ANALYSES]] for the monitoring of security analyses.

For the reporting (e.g. displaying the status of the work products) additional tooling is created (see guidance/security_management_process_reqs).
