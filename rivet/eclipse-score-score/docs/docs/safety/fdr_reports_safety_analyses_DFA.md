---
id: DOC-FDR-REPORTS-SAFETY-ANALYSES-DFA-98793
title: Fdr Reports Safety Analyses Dfa
type: specification
status: approved
tags: [eclipse-score]
---

# Safety Analysis Formal Review Report

### Safety Analysis Formal Review Report

{{artifact:DOC__SCORE_PLATFORM_SAFETY_ANALYSIS_FDR:status,safety-level,security}}}}

**Purpose**
The purpose of this Safety Analysis checklist template is to collect the topics to be checked during verification of the Platform Safety Analyses.

**Conduct**
As described in [[WF__P_FORMAL_RV]], the formal document review is performed by an "external" safety manager:

- reviewer: <committer with safety manager skills explicitly named here>

**Checklist**

Please note that it is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additional to add in the remarks why it is passed or not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column. See also [[DOC_CONCEPT__WP_INSPECTIONS]] for further information about reviews in general and inspection in particular.

.. list-table:: Safety Analysis Checklist
      :header-rows: 1
      :widths: 10,30,30,15,8,8

      * - Review ID
        - Acceptance Criteria
        - Guidance
        - Passed
        - Remarks
        - Issue link
      * - REQ_01_01
        - Is / are the attribute sufficient set correctly?
        - The mitigations shall have a direct influence ont the violation by prevention, detection or mitigation to reduce the risk to an acceptable level.
        - The mitigations are sufficient.
        - <yes|no>
        -
      * - REQ_01_02
        - Are the templates for Safety Analysis used?
        - See [[DOC__PLATFORM_DFA]]
        - Templates are used to generate the Safety Analysis.
        - <yes|no>
        -
      * - REQ_01_03
        - Were the failure initiators / fault models applied?
        - See [[GD_GUIDL__DFA_FAILURE_INITIATORS]] / [[GD_GUIDL__FAULT_MODELS]]
        - The applicable items of the failure initiators / fault models are used to ensure a structured analysis. For all not applicable items an argument shall be given in the content of the document.
        - <yes|no>
        -
      * - REQ_01_04
        - Are the failure effects clearly and completely described?
        - Use the generic failure effect descriptions and enlarge the description if it's applicable to the considered element.
        - The effects of the failure is described completely. The effect can be recognized easily.
        - <yes|no>
        -
      * - REQ_01_06
        - Is the attribute "mitigated by" linked correct?
        - Check if the correct failure effect is linked via "mitigated by".
        - The "mitigated by" link is correct.
        - <yes|no>
        -
      * - REQ_01_07
        - Is the sufficiency of the "mitigated by" (prevention, detection or mitigation) described or can it be recognized easily?
        - The sufficiency of the "mitigated by" is described in the content of the document. It can be recognized easily.
        - The "mitigated by" shows clearly that a fault / failure can be mitigated by the linked requirement by prevention, detection or mitigation. It shall be described in the contend.
        - <yes|no>
        -
      * - REQ_01_08
        - Is the overall result of the Safety Analysis described in the report?
        - It shall be shown in the report if the Safety Analysis are finished and if all artifacts are "valid" and "sufficient".
        - The results of the Safety Analysis are described in the report. The report is available [[WP__VERIFICATION_PLATFORM_VER_REPORT]].
        - <yes|no>
        -
