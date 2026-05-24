---
id: DOC-FEATURE-DFA-39534
title: Feature Dfa
type: specification
status: approved
tags: [eclipse-score]
---

### FEO Feature DFA

{{artifact:DOC__FRAMEWORKS_FEO_DFA:status,safety-level,security}}

# FEO Feature DFA

For the DFA analysis where the failure initiators [[GD_GUIDL__DFA_FAILURE_INITIATORS]] are used. The analysis is done before the platform DFA is done.
Safety mechanisms that are used by many features are not considered here, but at the platform DFA. The analysis is only done for the needs of the FEO feature.

## Dependent Failure Initiators

.. code-block:: rst

### <Title>

{{artifact:FEAT_SAF_DFA__<FEATURE>__<ELEMENTDESCRIPTOR>:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your feature DFA.

    - The above "code-block" directive must be updated
    - Fill in all the needed information in the <brackets>
