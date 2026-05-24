---
id: DOC-CHANGE-MANAGEMENT-GETSTRT-95195
title: Change Management Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Getting Started on Change Management

{{artifact:DOC_GETSTRT__CHANGE_PROCESS:status,safety-level,security}}

This document describes the steps to create a change request, and further to analyze,
implement, and to control the change until closure. Where a change is defined as an
introduction of a new feature/component or modification of an existing feature/component.

Examples for change requests:

* New feature e.g. communication, debugging, health management, cryptography introduced (feature request).
* Existing feature, e.g. communication supports new protocol (feature modification).
* New component for parsing a protocol introduced (component request).
* API change for an existing component (component modification).

Therefore guidelines [[GD_TEMP__CHANGE_FEATURE_REQUEST]] and
[[GD_TEMP__CHANGE_COMPONENT_REQUEST]], [[GD_GUIDL__CHANGE_CHANGE_REQUEST]] and
a [[DOC_CONCEPT__CHANGE_PROCESS]] are available.

# General Workflow

The workflows are defined in the chm_change_workflows section.

For every change identified, the following workflows are executed:

* Create your change request according to [[WF__CHANGE_CREATE_CR]]
* Analyze change request report according to [[WF__CHANGE_ANALYZE_CR]]
* Implement change request and monitor it until closure according to [[WF__CHANGE_IMPLEMENT_MONITOR_CR]]
* Close the change request according to [[WF__CHANGE_CLOSE_CR]]

In addition create a change management plan as part of the platform management plan according to [[WF__PLATFORM_CR_MT_PLATFORM_MGMT_PLAN]]
