---
id: DOC-INDEX-64220
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _feature_architecture_template:

# Feature Architecture

.. note::
   The complete feature architecture template as shown here is intended to document the idea about the architecture of a feature (if needed) when a CR is created. After the CR is granted, it is moved and further detailed / maintained in the module where the feature resides. See `module template documentation <https://eclipse-score.github.io/module_template/main/>`__. Only the logical interfaces remains in the feature architecture platform documentation, as they are relevant for the overall platform architecture. The detailed architecture of the feature is documented in the module documentation, and the logical interfaces are linked from there to the platform documentation. This is to avoid that the platform documentation becomes too detailed and hard to maintain, while still providing the necessary information about the feature architecture in the platform documentation. Depending from the project it might be that in the reference integration of the platform the full feature architecture including the implementation of the features and its components becomes visible in the platform documentation. See Deployment example <deployment_example>.

### [Your Feature Name] Architecture

{{artifact:DOC__FEATURE_NAME_ARCHITECTURE:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``doc__`` and followed by ``_architecture``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

## Overview

<Brief summary>

## Description

<General Description>

<Design Decisions - For the documentation of the decision the [[GD_TEMP__CHANGE_DECISION_RECORD]] can be used.>

<Design Constraints>

## Requirements

.. code-block:: none

# Rationale Behind Architecture Decomposition

Mandatory: A motivation for the decomposition

## Static Architecture

The live feature architecture template snippets are maintained in the
`module template documentation <https://eclipse-score.github.io/module_template/main/>`__.

## Logical Interfaces

.. code-block:: rst

### Interface Name

{{artifact:LOGIC_ARC_INT__FEATURE_NAME__INTERFACE_NAME1:status,safety-level,security}}

### Operation

{{artifact:LOGIC_ARC_INT_OP__FEATURE_NAME__OPERATION:status,safety-level,security}}

