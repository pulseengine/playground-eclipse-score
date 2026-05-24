---
id: DOC-SECURITY-ANALYSIS-GETSTRT-22369
title: Security Analysis Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Getting Started on Security Analysis

{{artifact:DOC_GETSTRT__SECURITY_ANALYSIS:status,safety-level,security}}}}

This document outlines the steps for performing, monitoring, and verifying Security
Analysis. Security Analysis is used as an umbrella term for different methods.
The concept of performing Security Analysis is described in [[DOC_CONCEPT__SECURITY_ANALYSIS]].
The verification of the architecture is described in [[DOC_CONCEPT__ARCH_PROCESS]].

# Security Analysis Steps

The goal of the Security Analysis is to prove that the security requirements for
functions and security controls are not violated and that they are complete, consistent
and correct. The Security Analysis is performed in three steps.

* Analyze the architecture with provided methods.
* Monitor the Security Analyses and log any issues in the Issue Tracking system with the ``security`` label until the analysis is completed.
* Verify the Security Analyses results by using [[GD_CHKLST__SECURITY_ANALYSIS]]. The Security Analysis is completed when the verification is done, no issues are open and the status is "valid".

The details of what needs to be done in each step are described in the
[[GD_GUIDL__SECURITY_ANALYSIS]]. For the Security Analysis
templates are used. The templates are described in the
security_analysis_threat_templates and security_analysis_templates.
