---
id: DOC-MODULE-SAFETY-PACKAGE-FDR-37590
title: Module Safety Package Fdr
type: specification
status: approved
tags: [eclipse-score]
---

# Safety Package Formal Review Report

### [Your Module Name] Safety Package Formal Review

{{artifact:DOC__MOD_TEMP_MODULE_NAME_SAFETY_PACKAGE_FDR:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Module.

    - Modify ``Your Module Name`` to be your Module Name
    - Modify ``id`` to be your Module Name in upper snake case preceded by ``doc_`` and succeeded by ``safety_package_fdr``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

**Purpose**

The purpose of this review checklist is to report status of the formal review for the safety package.

**Conduct**
As described in [[WF__P_FORMAL_RV]], the formal document review is performed by an "external" safety manager:

- reviewer: <committer with safety manager skills explicitly named here>

**Checklist**

See also the review concept for further information about reviews in general and inspection in particular.

.. list-table:: Safety Package Checklist
        :header-rows: 1

        * - Id
          - Safety package activity
          - Compliant to ISO 26262?
          - Reference
          - Comment

        * - 1
          - Is a safety package provided which matches the safety plan (i.e. all planned work products referenced)?
          - [YES | NO ]
          - [[title]] <std_req__iso26262__management_6481>
          - <Rationale for result>

        * - 2
          - Is the argument how functional safety is achieved, provided in the safety package, plausible and sufficient?
          - NO
          - [[title]] <std_req__iso26262__management_6481>
          - The argument is intentionally not provided by the project.

        * - 3
          - Are the referenced work products available?
          - [YES | NO ]
          - [[title]] <std_req__iso26262__management_6482>
          - <Rationale for result>

        * - 4
          - Are the referenced work products in released state, including the process safety audit?
          - [YES | NO ]
          - [[title]] <std_req__iso26262__management_6482>
            [[title]] <std_req__iso26262__management_6469>
          - <Rationale for result>

        * - 5
          - If safety related deviations from the process or safety concept are documented, are these argued understandably?
          - [YES | NO ]
          - [[title]] <std_req__iso26262__management_6481>
          - <Rationale for result>
