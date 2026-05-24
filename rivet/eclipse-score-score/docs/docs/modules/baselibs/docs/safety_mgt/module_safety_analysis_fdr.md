---
id: DOC-MODULE-SAFETY-ANALYSIS-FDR-21599
title: Module Safety Analysis Fdr
type: specification
status: approved
tags: [eclipse-score]
---

# Safety Analysis Checklist

### Baselibs Safety Analysis Checklist

{{artifact:DOC__BASELIBS_SAFETY_ANALYSIS_FDR:status,safety-level,security}}}}

**Purpose**

The purpose of this Safety Analysis (DFA and FMEA) checklist template is to collect the topics to be checked during verification of the Safety Analysis.

**Conduct**

As described in [[WF__P_FORMAL_RV]], the formal document review is performed by an "external" safety manager:

- reviewer: <committer with safety manager skills explicitly named here>

**Checklist**

Please note that the "passed" column must contain "yes" or "no" for each checklist item. Additionally, the remarks column must explain why item passed or did not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column.

.. list-table:: Safety Analysis Checklist
      :header-rows: 1
      :widths: 10,10,30,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - 1
        - Is it plausible that each potential identified dependent failure that has been identified, will lead to a dependent failure which cause a violation of FFI?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_742>
        - <Rationale for result>

      * - 2
        - Are the failure initiators [[title]] <gd_guidl__dfa_failure_initiators> / fault models [[title]] <gd_guidl__fault_models> applied?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_744>
        - <Rationale for result>

      * - 3
        - Are measures defined to resolute the identified potential dependent failures?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_746>, [[title]] <std_req__iso26262__analysis_747>
        - <Rationale for result>

      * - 4
        - Is the result of the safety analysis indicate if the safety requirements are complied?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_842>
        - <Rationale for result>

      * - 5
        - Are for all not complied safety requirements mitigations defined to resolute the non-compliance? The mitigations shall have a direct influence on the violation by prevention, detection or mitigation to reduce the risk to an acceptable level.
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_843>
        - <Rationale for result>

      * - 6
        - Are the mitigations effective and implemented?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_844>
        - <Rationale for result>

      * - 7
        - Are the templates for DFA and/or FMEA used? See [[GD_TEMP__COMP_SAF_DFA]] and [[GD_TEMP__COMP_SAF_FMEA]]
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_748>, [[title]] <std_req__iso26262__analysis_849>, [[title]] <std_req__iso26262__analysis_8410>
        - <Rationale for result>
