---
id: DOC-FMEA-16006
title: Fmea
type: specification
status: approved
tags: [eclipse-score]
---

# FMEA (Failure Modes and Effects Analysis)

### result FMEA

{{artifact:DOC__RESULT_FMEA:status,safety-level,security}}

## Failure Mode List

Fault Models for sequence diagrams
  .. list-table:: Fault Models for sequence diagrams
     :header-rows: 1
     :widths: 10,20,10,20

    * - ID
      - Failure Mode
      - Applicability
      - Rationale
    * - MF_01_01
      - message is not received (is a subset/more precise description of MF_01_05)
      - no
      - If set result was not received before the get value/error are called, this will lead to an exception/terminate. In case of the get value user defined defaults are provided.
    * - MF_01_02
      - message received too late (only relevant if delay is a realistic fault)
      - no
      - Do not see this as a problem for result lib, would lead to the same consideration as in MF_01_01
    * - MF_01_03
      - message received too early (usually not a problem)
      - no
      - No problem for result lib
    * - MF_01_04
      - message not received correctly by all recipients (different messages or messages partly lost). Only relevant if the same message goes to multiple recipients.
      - no
      - No multiple recipients (maybe from different threads?)
    * - MF_01_05
      - message is corrupted
      - yes
      - The error message carried within the error object does not own the underlying data. If the data source is destroyed before the error message is accessed by the user, the message reference becomes invalid (see [[COMP_SAF_FMEA__RESULT__ERROR_MESSAGE_LIFE]]).
    * - MF_01_06
      - message is not sent
      - yes
      - Value or error are not returned - see [[COMP_SAF_FMEA__RESULT__UNCHECKED]]
    * - MF_01_07
      - message is unintended sent
      - no
      - not applicable for a library
    * - CO_01_01
      - minimum constraint boundary is violated
      - yes
      - The error code returned is not bound to a specific error domain at the type level. A user may interpret the code against the wrong domain, violating the constraint that error codes are only meaningful within their originating domain (see [[COMP_SAF_FMEA__RESULT__ERROR_CODE]]).
    * - CO_01_02
      - maximum constraint boundary is violated
      - yes
      - same as above
    * - EX_01_01
      - Process calculates wrong result(s) (is a subset/more precise description of MF_01_05 or MF_01_04). This failure mode is related to the analysis if e.g. internal safety mechanisms are required (level 2 function, plausibility check of the output, …) because of the size / complexity of the feature.
      - no
      - Due to low complexity of the component this error is completely eliminated by testing. Low complex architecture according to criteria in [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]] ARC_03_03 and design complexity below numbers as in [[GD_REQ__IMPL_COMPLEXITY_ANALYSIS]]
    * - EX_01_02
      - processing too slow (only relevant if timing is considered)
      - no
      - Due to the small functionality, being too slow is no likely issue.
    * - EX_01_03
      - processing too fast (only relevant if timing is considered)
      - no
      - Get functions only deliver data when called, no "too fast" is possible.
    * - EX_01_04
      - loss of execution
      - yes
      - Loss of execution leads to the same error as MF_01_06
    * - EX_01_05
      - processing changes to arbitrary process
      - no
      - Not a problem of result lib as this is a library and not a process
    * - EX_01_06
      - processing is not complete (infinite loop)
      - yes
      - The Result library accepts user-provided operations for value and error transformation. If such an operation does not complete, the calling execution is halted (see [[COMP_SAF_FMEA__RESULT__STOP_USER]]).

## FMEA

For all identified applicable failure initiators, the FMEA is performed in the following section.

### Result Error Code Cross-Domain Misinterpretation

{{artifact:COMP_SAF_FMEA__RESULT__ERROR_CODE:status,safety-level,security}}

### Result Error Message Lifetime Violation

{{artifact:COMP_SAF_FMEA__RESULT__ERROR_MESSAGE_LIFE:status,safety-level,security}}

### Result Unchecked Value or Error Access

{{artifact:COMP_SAF_FMEA__RESULT__UNCHECKED:status,safety-level,security}}

### Result Stop User

{{artifact:COMP_SAF_FMEA__RESULT__STOP_USER:status,safety-level,security}}

