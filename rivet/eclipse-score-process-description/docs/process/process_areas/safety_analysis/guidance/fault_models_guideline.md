---
id: DOC-FAULT-MODELS-GUIDELINE-71866
title: Fault Models Guideline
type: specification
status: approved
tags: [eclipse-score]
---

.. _fault_models:

# FMEA Fault Models

### FMEA Fault Models

{{artifact:GD_GUIDL__FAULT_MODELS:status,safety-level,security}}

Fault Models for sequence diagrams
  .. list-table:: Fault Models for sequence diagrams
     :header-rows: 1
     :widths: 15,15,45,15

    * - Element
      - ID
      - Failure Mode
      - Importance (can be used for prioritization)
    * - message
      - MF_01_01
      - message is not received (is a subset/more precise description of MF_01_05)
      - High
    * - message
      - MF_01_02
      - message received too late (only relevant if delay is a realistic fault)
      - Medium
    * - message
      - MF_01_03
      - message received too early (usually not a problem)
      - Low
    * - message
      - MF_01_04
      - message not received correctly by all recipients (different messages or messages partly lost). Only relevant if the same message goes to multiple recipients.
      - High
    * - message
      - MF_01_05
      - message is corrupted
      - High
    * - message
      - MF_01_06
      - message is not sent
      - High
    * - message
      - MF_01_07
      - message is unintended sent
      - High
    * - duration/time constraint
      - CO_01_01
      - minimum constraint boundary is violated
      - Medium
    * - duration/time constraint
      - CO_01_02
      - maximum constraint boundary is violated
      - High
    * - execution
      - EX_01_01
      - Process calculates wrong result(s) (is a subset/more precise description of MF_01_05 or MF_01_04). This failure mode is related to the analysis if e.g. internal safety mechanisms are required (level 2 function, plausibility check of the output, …) because of the size / complexity of the feature.
      - High
    * - execution
      - EX_01_02
      - processing too slow (only relevant if timing is considered)
      - Medium
    * - execution
      - EX_01_03
      - processing too fast (only relevant if timing is considered)
      - Medium
    * - execution
      - EX_01_04
      - loss of execution
      - High
    * - execution
      - EX_01_05
      - processing changes to arbitrary process
      - Medium
    * - execution
      - EX_01_06
      - processing is not complete (infinite loop)
      - High
