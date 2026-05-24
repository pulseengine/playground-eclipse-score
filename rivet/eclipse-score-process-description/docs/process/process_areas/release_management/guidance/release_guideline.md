---
id: DOC-RELEASE-GUIDELINE-10770
title: Release Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Guideline

### Release Management Guideline

{{artifact:GD_GUIDL__REL_MANAGEMENT:status,safety-level,security}}

.. _workflow_release:

## Software Module Release

1. **Repository Management**:

   * Each software module is contained in one repository.
   * Ensure that the repository follows the standard naming conventions and structure.

2. **Release Planning**:

   * Create a release plan for each software module.
   * The release plan should include timelines, milestones, and deliverables.
   * Coordinate with other module owners and platform to align release schedules.

3. **Development and Testing**:

   * According process, cross functional teams implement and test.
   * Check the [[WP__VERIFICATION_MODULE_VER_REPORT]] to ensure that all tests pass before proceeding to the release.
   * In case of failed test, evaluate and possibly justify their failure.

4. **Release Preparation**:

   * Update the version number according to the versioning policy of your module's delivery container (defined in release management part of the [[GD_TEMP__PLATFORM_MGMT_PLAN]]).
   * Prepare release notes documenting the changes, improvements, and bug fixes.
   * Check if all planned configuration items are in correct state (i.e. work products are valid, external libraries/tools are used in the correct released version).
   * Ensure the module's safety package is available and complete.
   * Tag the release in the repository.

5. **Release Execution**:

   * Create a release in the repository release branch and attach the release notes. For this consider the `Howto Release <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository/>`_
   * Notify the project lead circle about the release for approval.
   * One of the project leads will give a review approval for the release note in the versioning tool, which is equivalent to his signing the release.

## Platform Release

1. **Integration of Software Modules**:

   * The platform release integrates various software modules.
   * Ensure that all software modules are released and tagged before the platform release.

2. **Platform Release Planning**:

   * Create a platform release plan that consumes the timelines from the software module release plans.
   * Define the overall release schedule, including major and minor releases.

3. **Development and Testing**:

   * Integrate the software modules release candidates into the platform.
   * Conduct comprehensive testing to ensure compatibility and stability.
   * Check the [[WP__VERIFICATION_PLATFORM_VER_REPORT]] to ensure that all tests pass before proceeding to the release.
   * Address any integration issues promptly to initiate bugfixing of the modules.
   * In case of still failed test, evaluate and possibly justify their failure.

4. **Release Preparation**:

   * Check if modules are released.
   * Update the platform version number according to the versioning policy (defined in release management part of the [[GD_TEMP__PLATFORM_MGMT_PLAN]]).
   * Prepare platform release notes summarizing the updates from all integrated software modules.
   * Check if all planned configuration items are in correct state (i.e. work products are valid, external libraries/tools are used in the correct released version).
   * Ensure the relevant safety packages are available and complete.
   * Create/Maintain Platform Handbook for the release.
   * Tag the platform release in the repository.

5. **Release Execution**:

   * Create a release in the repository release branch and attach the platform release notes. For this consider the `Howto Release <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository/>`_
   * Notify the project lead circle about the release for approval.
   * One of the project leads will give a review approval for the release note in the versioning tool, which is equivalent to his signing the release.
   * Publish within Eclipse SDV.

## Tracking and Communication

1. **Tracking**:

   * Use the project management tools to track the progress of software module releases and the platform release.
   * Maintain a release calendar to visualize the timelines and milestones.

2. **Communication**:

   * Regularly update all stakeholders on the release status as part of the project lead circle.
   * Hold periodic meetings to discuss progress, issues, and dependencies within the project lead circle.
   * meeting definition and schedule is defined in the projects's platform management plan, as defined in [[GD_GUIDL__PLATFORM_MGMT_PLAN]].

## Release Handbook

### Release Handbook

{{artifact:GD_GUIDL__REL_HANDBOOK:status,safety-level,security}}

# Templates

For the release note a template has been created for module level and for platform level.

.. list-table:: Overview
   :header-rows: 1
   :widths: 37, 37

   * - Project scope
     - Template
   * - Module Release Notes
     - [[title]] <gd_temp__rel_mod_rel_note>
   * - Platform Release Notes
     - [[title]] <gd_temp__rel_plat_rel_note>

The above templates shall be used
