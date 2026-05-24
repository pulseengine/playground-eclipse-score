---
id: DOC-AOU-REQ-QNX-2615
title: Aou Req Qnx
type: specification
status: approved
tags: [eclipse-score]
---

# Assumptions of Use - QNX

### QNX Assumptions of Use

{{artifact:DOC__OS_AOU_QNX:status,safety-level,security}}

Note: Document is draft until all relevant restrictions from the QNX safety manual(s) are included.

The assumption of use identifiers below are extracted from all QNX safety manual restrictions for the relevant
components of the "OS". Recommendations are not extracted because S-CORE does not implement these.

The list enables feature teams with access to the QNX safety manual to link to their architecture
(static or dynamic views) the AoUs which their module's components cover.
This can be used by the system integrator as a starting point to show compliance to the QNX AoU.
In the below list all AoU/Restrictions are set to "invalid" if those are not applicable to the S-CORE
SW platform, including an argumentation why.

The verification for such an AoU is done in the same way as for other requirements, i.e. if these are
non-functional and "non-testable" then a "requirement analysis" is done as described in
[[DOC__COMPONENT_NAME_REQ_INSPECTION]] checklist item REQ_08_02. To document this a PR is created
to modify the component architecture "fulfils" attribute, add the respective requirements to the
requirements inspection checklist's scope and document findings like for other inspections.

### RST-0001

{{artifact:AOU_REQ__OS__RST0001:status,safety-level,security}}

### RST-0002

{{artifact:AOU_REQ__OS__RST0002:status,safety-level,security}}

more to come ...
