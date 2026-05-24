---
id: DOC-INDEX-48837
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_architecture_template:

# Component Architecture

### [Your Component Name] Architecture

{{artifact:DOC__MOD_TEMP_COMPONENT_NAME_ARCHITECTURE:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your needs.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and followed by ``_architecture``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

## Overview

<Brief summary>

## Requirements Linked to Component Architecture

.. code-block:: none

## Description

<General Description>

<Design Decisions - For the documentation of the decision the [[GD_TEMP__CHANGE_DECISION_RECORD]] can be used.>

<Design Constraints>

# Rationale Behind Architecture Decomposition

Mandatory: A motivation for the decomposition or reason for not further splitting it into internal components.

## Static Architecture

The components are designed to cover the expectations from the feature architecture
(i.e. if already exists a definition it should be taken over and enriched).

A component can optional also consist of lower level components to further structure the architecture. The component and its static views can also optionally use interfaces provided by other components.

### Component Name

{{artifact:COMP__MOD_TEMP_COMPONENT_NAME_TEMPLATE:status,safety-level,security}}

### Component Name (Static View)

{{artifact:COMP_ARC_STA__MOD_TEMP_COMPONENT_NAME__SV:status,safety-level,security}}

## Dynamic Architecture

### Dynamic View

{{artifact:COMP_ARC_DYN__MOD_TEMP_COMPONENT_NAME__DV:status,safety-level,security}}

## Interfaces

.. code-block:: rst

### <Title>

{{artifact:REAL_ARC_INT__<COMPONENT>__<TITLE>:status,safety-level,security}}

## Internal Components

### Component Name Static View

{{artifact:COMP_ARC_STA__MOD_TEMP_COMPONENT_NAME__2:status,safety-level,security}}

.. note::
   Architecture can be split into multiple files. At component level the public interfaces to be used by the user and tester to be shown.

.. attention::
    The above directives must be updated according to your component architecture.

    - Replace the example content by the real content (according to [[GD_GUIDL__ARCH_DESIGN]])
    - Set the status to valid and start the review/merge process
