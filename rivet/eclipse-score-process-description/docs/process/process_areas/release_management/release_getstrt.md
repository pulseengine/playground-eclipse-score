---
id: DOC-RELEASE-GETSTRT-96803
title: Release Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Getting Started on Release Management

{{artifact:DOC_GETSTRT__RELEASE_PROCESS:status,safety-level,security}}

This document describes the steps to create a release of the SW and collaterals (test, documentation).

Releases can be done in every repository, mainly:

* Platform (Main project/Integration) repository
* Module (platform's components) repositories

For these are available: templates [[GD_TEMP__REL_PLAT_REL_NOTE]] & [[GD_TEMP__REL_MOD_REL_NOTE]]
or `Combined Release Template <https://github.com/eclipse-score/process_description/blob/main/.github/RELEASE_TEMPLATE.md>`_,
guidelines [[GD_GUIDL__REL_MANAGEMENT]] and a [[DOC_CONCEPT__REL_PROCESS]]
are available.

# General Workflow

The workflows are defined in the release_workflows section.

The following workflows are executed:

* Create a release plan for the platform according to [[WF__REL_PLAT_REL_PLAN]]
* Create a release plan for the module according to [[WF__REL_MOD_REL_PLAN]]
* According to the planning create release notes for modules [[WF__REL_MOD_REL_NOTE]] and platform [[WF__REL_PLATFORM_REL_NOTE]]
* According to the planning create the platform handbook [[WF__REL_PLATFORM_HANDBOOK]]

In addition create a release management plan as part of the platform management plan according to [[WF__PLATFORM_CR_MT_PLATFORM_MGMT_PLAN]].
