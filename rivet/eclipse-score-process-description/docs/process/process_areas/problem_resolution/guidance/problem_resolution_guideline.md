---
id: DOC-PROBLEM-RESOLUTION-GUIDELINE-86484
title: Problem Resolution Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Guideline

### Problem Resolution Guideline

{{artifact:GD_GUIDL__PROBLEM_PROBLEM:status,safety-level,security}}

This document describes the general guidances for Problem Resolution based on the concept which is defined [[title]]<doc_concept__problem_process>.

# General Hints

The detailed implementation of the Problem Resolution for the project shall be described in the Workflow Platform Management <workflow_platform_management>.

## Templates

To create problem reports, the project shall provide the content of the following template
in project's selected Issue Tracking System: [[title]]<gd_temp__problem_template>.

.. note::
  An example template for the Issue Tracking System in GitHub (`GitHub Issues <https://github.com/features/issues>`_)
  can be found here:
  `Issue Template Bugfix <https://github.com/eclipse-score/.github/blob/main/.github/ISSUE_TEMPLATE/5_Bug.yml>`_

## Attributes

For all Problems following mandatory attributes need to be defined:

A more detailed description can be found here: prm_process_requirements

.. _workflow_prm_requirements:

# Activities for Problem Resolution

This section describes in detail which steps need to be performed for a Problem Resolution.

.. list-table:: Activities for Problem Resolution
   :header-rows: 1
   :widths: 10,60,30,30

   * - Step
     - Description
     - Responsible
     - Approver
   * - 1. <prm_create_problem_report>
     - Create Problem Report
     - [[title]] <rl__contributor>
     - [[title]] <rl__committer>
   * - 2. <prm_analyze_problem_report>
     - Analyze Problem Report
     - [[title]] <rl__contributor>
     - [[title]] <rl__committer>
   * - 3. <prm_initiate_problem_resolution>
     - Initiate and Monitor Problem Resolution
     - [[title]] <rl__contributor>
     - [[title]] <rl__committer>
   * - 4. <prm_monitor_problem_resolution>
     - Close Problem Resolution
     - [[title]] <rl__committer>
     - [[title]] <rl__project_lead>

.. _prm_create_problem_report:

## Create Problem Report

[[title]] <rl__contributor> (as author, submitter, reporter) creates the Problem
Report in the defined Issue Tracking System of the project based on the content of the
provided template:
[[title]]<gd_temp__problem_template>.

It is expected that the select Issue Tracking system supports template definition. Best
practice is to define a template with the required content, so that it can be copied
from the different users.

.. note::
  For the Issue Tracking System in GitHub, there is a template created, which can be
  be found here:
  `Issue Template Bugfix <https://github.com/eclipse-score/.github/blob/main/.github/ISSUE_TEMPLATE/5_Bug.yml>`_

.. note::
  A Problem Report Example based on that template is here:
  `Example Problem Report <https://github.com/eclipse-score/process_description/issues/631>`_

.. note::
  A Problem Report Example 2 based on an older version template is here:
  `Example Problem Report 2 <https://github.com/eclipse-score/process_description/issues/126>`_

It is expected, that the UID will be provided automatically by the Issue Tracking System.

It is expected, that the status of the problem report is set to "open" automatically.
As long as the content is updated, the status of the Problem is kept "open".

It is expected, that the problem submitter will be set automatically by the Issue
Tracking System.

The title of the Problem Report should reflect the topic accordingly.

The description should reflect the problem root cause and impact in detail.

If applicable affected parties should be notified.

Further supporting information should ge given, especially how to reproduce the problem,
and what is the error occurrence rate?

If the problem affects safety or security it should be stated explicitly.
If safety is affected, the ASIL classification should be added, if applicable.

The problem should be classified according minor, major, critical or blocker.

The affected versions of the release should be documented. After detection of the
problem, checking the affected versions is critical to understand the impact of the
problem. Thus document the first affected version and the last affected version.

.. note::
  | For the Problem Report Example:
  | * The UID is provided by the Issue Tracking System as: **#631**
  | * The status of the issue is provided by the Issue Tracking System as: **Open**
  | * The submitter is provided by the Issue Tracking System as: **masc2023**
  | * The title contains the main root cause, missing safety/security attribute
  | * The descriptions has a section for the **Root cause** and **Impact**
  | * The description has a section for notification: **Notification required?**
  | * Further supporting information is added as the link to the official feature request template which makes it reproducible
  | * Checkboxes are selected to highlight, that Safety and Security is affected, no further classification, as the project is defined as ASIL B
  | * The problem classification is provided as minor
  | * The first affected version is provided: *pre-0.5*
  | * The last affected version is provided: *0.5*

When ready to review and to analyze, the author sets the status to "in review" manually.

.. note::
  | For the Problem Report Example:
  | * The "Process Development Community" dashboard is added and the status must be changed to **Todo**
  | * The combination of the issue**Open** and **Todo** defines the status **in review**

.. _prm_analyze_problem_report:

## Analyze Problem Report

The projects [[title]] <rl__committer> analyzes the problem together with the
[[title]] <rl__contributor> and takes a decision for accepting or rejecting it.

The analysis will start by reviewing all the information given during the creation of the
problem report. All topics are revisited and checked for correctness, completeness and
consistency.

If required, the information is updated accordingly.

If accepted, the stakeholder of the problem and the expected release, where the problem
should be closed, shall be defined. Optionally, the corresponding milestone can be set.

If applicable, the features affected should be identified too.

The description shall reflect the result of the analysis.

Topics to checked (critical topics are marked with x):

- [x] Is the problem description clear and detailed enough to understand the problem and its impact?
- [x] Is the problem root cause clearly described?
- [x] Is the problem impact clearly described?
- [ ] Is notification of affected parties required? If yes, are the affected parties notified?
- [ ] Are there any proposed solutions provided?
- [ ] Are there any further linked issues or pull requests provided?
- [x] Is the error occurrence rate provided? If yes, is it high enough to accept the problem?
- [x] Is the problem reproducible?
- [ ] Are there any further supporting information provided?
- [x] Is the problem classification correct?
- [x] Is information for the affected version of the release provided? If yes, is it correct?
- [ ] Is the information for the expected closure version provided? If yes, is it correct?
- [x] Is the problem affecting safety or security? If yes, is the classification correct?

The analysis phase can not be closed, until all critical topics are
clarified and provided in the description. If not, the problem report should be rejected
and closed with the reason "Closed as not planned".

.. note::
  | For the Problem Report Example:
  | * The descriptions has a section for the analysis results: **Accepted**
  | * The stakeholder are provided using Assignees field: **masc2023**
  | * The expected fix version is provided: *0.6*
  | * The "Milestone" is provided: **Release v0.6 - Maturity Level 2**
  | * Feature identification is not applicable for this example, so no label is set, beside **bug**

If accepted, [[title]] <rl__contributor> can start with the initiation of the
Problem Resolution.

The author has the freedom to cancel it at any time by setting the status to "rejected".

.. note::
  | For the Problem Report Example:
  | * For rejection the status of the issue must be changed to **Closed as not planned**
  | * The combination of **Closed as not planned** and any "Process Development Community" status defines the status **rejected**

.. _prm_initiate_problem_resolution:

## Initiate and Monitor Problem Resolution

If accepted, the projects [[title]] <rl__committer> initiates the resolution of
the problem together with the [[title]] <rl__contributor>.

The description shall reflect the proposed solutions, e.g. measure to resolve the problem.

.. note::
  | For the Problem Report Example:
  | * The descriptions has a section for the proposed **Solution**

The concrete implementation of the solution may require several additional activities.
In this case additional issues may created and linked to the Problem Report.

.. note::
  | For the Problem Report Example:
  | * The **Create sub-issue** should be used to create further linked issues.

Minimal a Pull Request is sufficient to resolve the problem, which shall be linked
to the Problem Report. It is expected, that the status of the Pull Request is set to
"draft" or "open" automatically.

When ready to implement, the author sets the status to "in implementation" manually.

.. note::
  | For the Problem Report Example:
  | * The "Process Development Community" status must be changed to **In Progress**
  | * The linked Pull Request status is either "Draft" or "Open"
  | * The combination of **Open** and any "Process Development Community" status **In Progress** and the Pull Request status **Draft** or **Open** defines the status **in implementation**

.. note::
  | For the Problem Report Example:
  | * The **Development** section should be used to link to an pull request
  | * The **Create a branch** action may used to create automatically a linked pull request
  | For the Problem Report Example 2:
  | * The **Create a branch** action was used to create a automatically linked Pull Request
  | * The automatically created branch name reflects the issue UID and the title as
  | * **126-bug-stkh_req__archdes_example_req-has-no-content**

During the resolution the responsible lead [[title]] <rl__project_lead>
reports regularly the status to the affected
projects teams.

Escalations topics should be documented in the description, if possible.

.. note::
  | For the Problem Report Example and Example 2:
  | * Their is no escalation topic documented

The author has the freedom to cancel it at any time by setting the status to "rejected".

.. _prm_monitor_problem_resolution:

## Close Problem Resolution

During the resolution the [[title]] <rl__contributor> monitors all activities linked to
the problem, until they are closed.

[[title]] <rl__committer> checks finally if the problem Resolution is sufficient before
the status is finally closed.
To check, if it is sufficient, Problem Checklist <gd_chklst__problem_cr_review> may used.
Further the effectiveness of the implemented measure is confirmed and the availability
of the required reports, as verification results, if applicable.

When confirmed, the author sets the status to "closed" manually, if not done automatically.

.. note::
  | For the Problem Report Example 2:
  | * The status of the issue is provided by the Issue Tracking System as: **Closed**
  | * The combination of **Closed** and any "Process Development Community" status **Done** and the Pull Request status **Merged** defines the status **closed**

[[title]] <rl__committer> has the freedom to reject it at any time by setting the status
to "reject".
