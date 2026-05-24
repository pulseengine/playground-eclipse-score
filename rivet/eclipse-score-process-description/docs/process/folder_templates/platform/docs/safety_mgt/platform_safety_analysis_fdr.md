---
id: DOC-PLATFORM-SAFETY-ANALYSIS-FDR-49837
title: Platform Safety Analysis Fdr
type: specification
status: approved
tags: [eclipse-score]
---

# Platform Safety Analysis Formal Review Report

### Platform Safety Analysis Formal Review Report

{{artifact:DOC__PLATFORM_SAFETY_ANALYSIS_FDR:status,safety-level,security}}

**Purpose**
The purpose of this Safety Analysis (DFA and FMEA) formal review report template is to collect the topics to be checked during verification of the Platform Safety Analysis.

**Conduct**
As described in [[WF__P_FORMAL_RV]], the formal document review is performed by an "external" safety manager:

- reviewer: **<committer with safety manager skills explicitly named here>**
- scope: **<describe the scope of the review here, e.g. "the safety analysis of the module and its results">**

**Checklist**

Please note that it is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additional to add in the remarks why it is passed or not passed. In case of "no" an issue link to the issue tracking system has to be added in the last column. See also review_concept for further information about reviews in general and inspection in particular.

.. list-table:: General Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - Gen 1
        - Are the safety analysis performed according to the defined process and templates? See process_requirements_safety_analysis and also FMEA_templates and dfa_templates
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_841>, [[title]] <std_req__iso26262__analysis_849>, [[title]] <std_req__iso26262__analysis_8410>, [[title]] <std_req__iso26262__analysis_748>
        - <Rationale for result>

      * - Gen 2
        - Are the safety analysis performed in a systematic way to identify the potential dependent failures / failure modes and their effects? Are the failure effect and the mitigation described?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_849>, [[title]] <std_req__iso26262__analysis_8410>
        - <Ensured and checked by application of the defined templates and processes>

      * - Gen 3
        - Is the result of the safety analysis indicate if the safety requirements are complied?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_842>
        - <Rationale for result>

      * - Gen 4
        - Are the mitigations effective and implemented?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_844>
        - <Rationale for result>

      * - Gen 5
        - Are all AoU's that are used as mitigation's created and covered in the safety manual?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_845>
        - <Rationale for result>

      * - Gen 6
        - Are additional safety-related test cases determined by potential results of the safety analyses?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_847>
        - <Rationale for result>

.. list-table:: DFA Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - DFA 1
        - Are the potential dependent failures identified by performming a DFA?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_741>
        - <Rationale for result>

      * - DFA 2
        - Is it plausible that each potential identified dependent failure that has been identified, will lead to a dependent failure which cause a violation of FFI?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_742>
        - <Rationale for result>

      * - DFA 3
        - Are applicable operational situations and operating modes considered?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_743>
        - <Rationale for result>

      * - DFA 4
        - Are the failure initiators [[title]] <gd_guidl__dfa_failure_initiators> suitable and applied?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_744>
        - <Rationale for result>

      * - DFA 5
        - Is a rationale provided for each identified potential dependent failure?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_745>
        - <Rationale for result>

      * - DFA 6
        - Are measures defined to resolve the identified potential dependent failures?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_746>, [[title]] <std_req__iso26262__analysis_747>, [[title]] <std_req__iso26262__analysis_843>
        - <Rationale for result>

      * - DFA 7
        - Can be the required level of independence shown for the identified potential dependent failures?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_748>
        - <Rationale for result>

.. list-table:: FMEA Checklist
      :header-rows: 1
      :widths: 10,30,10,30,20

      * - ID
        - Safety analysis activity
        - Compliant to ISO 26262?
        - Reference
        - Comment

      * - FMEA 1
        - Are the fault models suitable and applied for the FMEA? See fault_models and also process_requirements_safety_analysis
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_846>
        - <Rationale for result>

      * - FMEA 2
        - Are measures defined to resolve the identified faults?
        - [YES | NO ]
        - [[title]] <std_req__iso26262__analysis_843>
        - <Rationale for result>
