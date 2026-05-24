---
id: DOC-INDEX-82526
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_architecture_PersistencyKvs:

# Architecture

### KVS Module Architecture

{{artifact:DOC__KVS_ARCHITECTURE:status,safety-level,security}}

## Overview

Brief summary

## Requirements Linked to Component Architecture

.. code-block:: none

## Description

<General Description>

<Design Decisions - For the documentation of the decision the [[GD_TEMP__CHANGE_DECISION_RECORD]] can be used.>

<Design Constraints>

# Rationale Behind Architecture Decomposition

mandatory: a motivation for the decomposition or reason for not further splitting it into sub components.

## Static Architecture

The components are designed to cover the expectations from the feature architecture
(i.e. if already exists a definition it should be taken over and enriched).

A component can optional also consist of subcomponents to further structure the architecture. The component and its static views can also optionally use interfaces provided by other components.

The live component architecture template is maintained in the
`module template documentation <https://eclipse-score.github.io/module_template/component_architecture_template.html>`_.

### Component Name (Static View)

{{artifact:COMP_ARC_STA__KVS__STATIC_VIEW:status,safety-level,security}}

## Dynamic Architecture

### Dynamic View

{{artifact:COMP_ARC_DYN__KVS__DYNAMIC_VIEW:status,safety-level,security}}

## Interfaces

.. code-block:: rst

### <Title>

{{artifact:REAL_ARC_INT__<COMPONENT>__<TITLE>:status,safety-level,security}}

## Internal Components

### Component Name 2

{{artifact:COMP_ARC_STA__KVS__2:status,safety-level,security}}

.. note::
   Architecture can be split into multiple files. At component level the public interfaces to be used by the user and tester to be shown.

.. attention::
    The above directives must be updated according to your component architecture.

    - Replace the example content by the real content (according to [[GD_GUIDL__ARCH_DESIGN]])
    - Set the status to valid and start the review/merge process


