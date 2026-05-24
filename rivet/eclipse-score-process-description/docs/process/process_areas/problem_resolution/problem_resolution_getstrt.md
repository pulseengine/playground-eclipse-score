---
id: DOC-PROBLEM-RESOLUTION-GETSTRT-57246
title: Problem Resolution Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Getting Started on Problem Resolution

{{artifact:DOC_GETSTRT__PROBLEM_PROCESS:status,safety-level,security}}

This document describes the steps to create a problem report, and further to analyze,
resolve, and to control the problem until closure. Where a problem is defined as a
deviation of an expected result.

Examples for problem origins:

* Deviations relating to requirements, architecture, implementation or code found by user of the platform.
* Deviations found by contributor based on component, feature or Platform Integration Tests.
* Deviations found by Quality Management activities as defined in the Quality Management Plan.

Therefore guidelines [[GD_TEMP__PROBLEM_TEMPLATE]],
[[GD_GUIDL__PROBLEM_PROBLEM]] and a [[DOC_CONCEPT__PROBLEM_PROCESS]]
are available.

# General Workflow

The workflows are defined in the problem_workflows section.

For every problem identified, the following workflows are executed:

* Create your problem report according to [[WF__PROBLEM_CREATE_PR]]
* Analyze your problem report according to [[WF__PROBLEM_ANALYZE_PR]]
* Initiate problem resolution and monitor it until closure according to [[WF__PROBLEM_INITIATE_MONITOR_PR]]
* Close the problem resolution according to [[WF__PROBLEM_CLOSE_PR]]

In addition create a problem resolution plan as part of the platform management plan according to [[WF__PLATFORM_CR_MT_PLATFORM_MGMT_PLAN]].
