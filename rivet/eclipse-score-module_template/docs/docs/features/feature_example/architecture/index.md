---
id: DOC-INDEX-97333
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _feature_architecture_template:

# Feature Architecture

### [Your Feature Name] Architecture

{{artifact:DOC__FEATURE_EXAMPLE_ARCHITECTURE:status,safety-level,security}}

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

The requirements for the feature architecture are defined in the `requirements` section of the feature documentation in the project repository.

# Rationale Behind Architecture Decomposition

Mandatory: A motivation for the decomposition

## Static Architecture

The live feature architecture template snippets are maintained in the
`module template documentation <https://eclipse-score.github.io/module_template/main/>`__.

.. code-block:: rst

### Feature Static View

{{artifact:FEAT_ARC_STA__FEATURE_NAME__STATIC_VIEW:status,safety-level,security}}

## Dynamic Architecture

.. code-block:: rst

### Dynamic View

{{artifact:FEAT_ARC_DYN__FEATURE_NAME__DYNAMIC_VIEW:status,safety-level,security}}

## Logical Interfaces

The logical interfaces of the feature are defined in the `logical interfaces` section of the feature documentation in the project repository.

## Module Viewpoint

The following modules are needed to be defined to be able to draw the static feature view.
They will be replaced by linking the proper module definitions in the used module's repositories as soon as those exist.

The rendered module and used-component examples are maintained in the
`module template documentation <https://eclipse-score.github.io/module_template/main/>`_.

.. code-block:: rst

### Module Name

{{artifact:MOD__MODULE_NAME:status,safety-level,security}}

### Module Name Static View

{{artifact:MOD_VIEW_STA__FEATURE_NAME__MODULE_NAME:status,safety-level,security}}

## Used Components

The following components are needed to be defined to be able to draw the static feature view.
They will be replaced by linking the proper SW component definitions in the used module's repositories as soon as those exist.

.. code-block:: rst

### Component Name

{{artifact:COMP__COMPONENT_NAME_TEMPLATE:status,safety-level,security}}

.. note::
   Architecture can be split into multiple files, it is an high level architecture design
   which can be shown without actual c++/rust interfaces and data types
   and there will be link to internal architecture till code to get actual api descriptions.

.. attention::
    The above directives must be updated according to your feature architecture.

    - Replace the example content by the real content (according to [[GD_GUIDL__ARCH_DESIGN]])
    - Set the status to valid and start the review/merge process
