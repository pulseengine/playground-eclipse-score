---
id: DOC-CHANGE-MANAGEMENT-DECISION-RECORD-TEMPLATE-23523
title: Change Management Decision Record Template
type: specification
status: approved
tags: [eclipse-score]
---

.. _decision_record_template:

# Decision Record Template

### Decision Record Template

{{artifact:GD_TEMP__CHANGE_DECISION_RECORD:status,safety-level,security}}

This template is used to create new Decision Records (DRs) in the project.

Suggest to store close to the artefact which is affected by the DR. For example for platform wide decisions store close to the platform's stakeholder requirements.

In each DR file, include the following sections:

.. code-block:: rst

### <Title>

{{artifact:DEC_REC__<PLATFORM|FEATURE|COMPONENT>__<TITLE>:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your decision record.

    - Modify ``dec_rec`` to provide a descriptive and concise title. Summarizing the decision. (mandatory)
    - Modify ``id`` to contain the Platform/Feature/Component name the DR belongs to and the title, in upper snake case preceded by ``dec_rec__`` (mandatory)
    - Adjust ``status`` according to your needs (mandatory)
    - Modify ``affects`` to point to the work product it affects, mostly this will be requirements, architecture or design (recommended)
    - Provide ``Description`` (mandatory)
    - Add ``Context`` to describe the issue or motivation behind this decision or change (mandatory)
    - Add ``decision`` to detail the proposed change or decision (mandatory)
    - Add ``consequences`` to explain the impact of this change, including what becomes easier or more difficult (recommended)
