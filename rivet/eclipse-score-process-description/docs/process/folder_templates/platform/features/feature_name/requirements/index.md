---
id: DOC-INDEX-36802
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Feature Requirements

### [Your Feature Name] Requirements

{{artifact:DOC__FEATURE_NAME_REQUIREMENTS:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__`` and followed by ``_requirements``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

# <Headlines (for the list of requirements if structuring is needed)>

.. code-block:: rst

### Some Title

{{artifact:FEAT_REQ__FEATURE_NAME__SOME_TITLE:status,safety-level,security}}

.. code-block:: rst

### Some Other Title

{{artifact:AOU_REQ__FEATURE_NAME__SOME_OTHER_TITLE:status,safety-level,security}}

.. attention::
    The above directives must be updated according to your feature requirements.

    - Replace the example content by the real content for your first requirement (according to [[GD_GUIDL__REQ_ENGINEERING]])
    - Set ``satisfied_by`` with a link to feature ID
    - Set ``reqtype`` with a link to the right value (<Functional|Interface|Process|Non-Functional>)
    - Set ``derived_from`` with a link to the right stakeholder requirement
    - Adjust ``safety`` and ``security`` to the right value (ASIL B/QM; YES/NO)
    - Add other needed requirements for your feature
    - Adjust ``valid_from`` and ``valid_until`` to the right version numbers
    - Set ``status`` to ``valid`` and start the review/merge process

