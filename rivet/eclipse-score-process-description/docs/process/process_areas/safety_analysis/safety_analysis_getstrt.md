---
id: DOC-SAFETY-ANALYSIS-GETSTRT-88278
title: Safety Analysis Getstrt
type: specification
status: approved
tags: [eclipse-score]
---

# Getting Started

### Getting Started on Safety Analysis (FMEA and DFA)

{{artifact:DOC_GETSTRT__SAFETY_ANALYSIS:status,safety-level,security}}

This document outlines the steps for performing, monitoring, and verifying Safety Analysis. Safety Analysis is used as a umbrella term for the methods
DFA (Dependent Failure Analysis) and FMEA (Failure Mode and Effects Analysis).
The concept of performing Safety Analysis is described in [[DOC_CONCEPT__SAFETY_ANALYSIS]]. The verification of the architecture is described
in [[DOC_CONCEPT__ARCH_PROCESS]].

# Safety Analysis Steps

The goal of the Safety Analysis is to proof that the safety requirements for functions and safety mechanisms are not violated.
The Safety Analysis is performed in three steps.

* Analyse the architecture with a DFA and FMEA.
* Monitor the DFA and FMEA and log any issues in the Issue Tracking system with the ``safety`` label until the analysis is completed.
* Verify the FMEA and DFA results by using [[GD_CHKLST__SAFETY_ANALYSIS]]. The Safety Analysis are completed when the verification is done, no issues are open and the status is “valid”.

The details of what needs to be done in each step are described in the [[GD_GUIDL__SAFETY_ANALYSIS]]. For the Safety Analysis
templates are used. The templates are described in the FMEA_templates and DFA_templates.
