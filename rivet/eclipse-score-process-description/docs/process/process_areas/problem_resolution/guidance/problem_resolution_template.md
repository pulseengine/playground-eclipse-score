---
id: DOC-PROBLEM-RESOLUTION-TEMPLATE-87749
title: Problem Resolution Template
type: specification
status: approved
tags: [eclipse-score]
---

.. _prm_templates:

# Problem Report Template

### Problem Template

{{artifact:GD_TEMP__PROBLEM_TEMPLATE:status,safety-level,security}}

This template defines the content to be implemented in the selected Issue Tracking System
of the project.

## Problem status

[“open”, “in review”, “in implementation”, “closed”, “rejected”]

| (to be filled out during [[WF__PROBLEM_CREATE_PR]])
| (to be updated during [[WF__PROBLEM_ANALYZE_PR]])
| (to be updated during [[WF__PROBLEM_INITIATE_MONITOR_PR]])
| (to be updated during [[WF__PROBLEM_CLOSE_PR]])

## Problem submitter

[Who is the reporter of the problem?]

(to be filled out during [[WF__PROBLEM_CREATE_PR]])

## Problem description

[What is the problem?]

| Determine the cause of the problem, if possible.
| Determine the impact of the problem, if possible.
| Is notification required due to determined impact on affected parties?

| (to be filled out during [[WF__PROBLEM_CREATE_PR]])
| (to be updated during [[WF__PROBLEM_ANALYZE_PR]])

## Problem supporting information

[How to reproduce the problem?]

| Add additional information, e.g.
| add which operational state the problem occurred?
| observations, screenshots, debug traces, etc.

[Error occurrence rate?]

| Select one [None | Single Event | Sporadic | Highly Intermittent | Reproducible]

| (to be filled out during [[WF__PROBLEM_CREATE_PR]])
| (to be updated during [[WF__PROBLEM_ANALYZE_PR]])

## Problem category

[Safety affected, Security affected]

Safety, Security: Additional qualifiers to highlight, if safety or security is affected

They qualifiers have to be filled. If not filled out, a quality problem is assumed as
default category.

In addition to the category Safety affected, the ASIL classification may be added in the
documentation, if applicable.

| (to be filled out during [[WF__PROBLEM_CREATE_PR]])
| (to be updated during [[WF__PROBLEM_ANALYZE_PR]])

## Problem classification

[minor, major, critical, blocker]

Classify the problem severity

| Use **minor**, if the impact is not significant of the project

* The problem does not restrict usage of features in a significant manner

| Resolution may be scheduled to any planned future SW release

| Use **major**, if the impact does effect the quality of the project

* The problem can be solved with workarounds for affected features

| Resolution shall be scheduled to next planned future SW release

| Use **critical**, if the impact does not prohibit to use the project, but quality cannot be guaranteed

* The problem affects a complete feature, that they are partly or complete not behave as expected

| Resolution shall be scheduled to next planned future SW release or to a new planned intermediate release, if urgent resolution is required

| Use **blocker**, if the impact prohibits using the project

* The problem affects more than one feature, that they are partly or complete not behave as expected OR
* Safety or Security risks identified

| Resolution shall be provided upon availability

.. note::
  In case of doubt, a safety or security relevant problem shall always classified as **blocker**.

Determine if Urgent resolution is required? (yes, no, only valid for critical, blocker)

| (to be filled out during [[WF__PROBLEM_CREATE_PR]])
| (to be updated during [[WF__PROBLEM_ANALYZE_PR]])

## Problem affected version

[What version of the release is affected?]

Document the version of the release where the problem was detected.

| (to be filled out during [[WF__PROBLEM_CREATE_PR]])

## Problem analysis results

[What is the problem analysis result? Accepted or Rejected?]

| Especially document rejection reason, if applicable

In addition the safety/security relevance is confirmed or disconfirmed by safety/Security
Experts.

| Especially document disconfirming reason, if applicable

(to be filled out during [[WF__PROBLEM_ANALYZE_PR]])

## Problem stakeholder

[What are the potential stakeholder to resolve the problem?]

Add affected features, if applicable

(to be filled out during [[WF__PROBLEM_ANALYZE_PR]])

## Problem expected closure version

[Version when the problem should be resolved]

Document the version of the release where the problem should be resolved.

Optionally add a concrete Milestone, if applicable.

(to be filled out during [[WF__PROBLEM_ANALYZE_PR]])

## Problem solutions

[What are measures to solve the problem?]

Specify the measures to resolve the problem, based on a rationale

Verify the effectiveness of the implemented measure

Report the results of the verification, if applicable

Are all arguments convincing

| (to be filled out during [[WF__PROBLEM_INITIATE_MONITOR_PR]])
| (to be updated during [[WF__PROBLEM_CLOSE_PR]])

## Problem escalations

[Document escalation activities, if applicable]

| (to be filled out during [[WF__PROBLEM_INITIATE_MONITOR_PR]])
| (to be updated during [[WF__PROBLEM_CLOSE_PR]])
