---
id: DOC-COMPONENT-ARCHITECTURE-TEMPLATE-75825
title: Component Architecture Template
type: specification
status: approved
tags: [eclipse-score]
---

# Component Architecture Template

This page contains the component architecture template snippets that belong to the
module template repository.

## Overview

Use these snippets as the starting point for documenting component architecture in
the module template.

## Static Architecture

.. code-block:: rst

### Component Name

{{artifact:COMP__MOD_TEMP_COMPONENT_NAME_TEMPLATE:status,safety-level,security}}

### Component Name (Static View)

{{artifact:COMP_ARC_STA__MOD_TEMP_COMPONENT_NAME__SV:status,safety-level,security}}

## Dynamic Architecture

.. code-block:: rst

### Dynamic View

{{artifact:COMP_ARC_DYN__MOD_TEMP_COMPONENT_NAME__DV:status,safety-level,security}}

## Component Interface

The rendered component-interface example is maintained here so the module template
repository owns the live ``real_arc_int`` example.

### Component Interface 1

{{artifact:REAL_ARC_INT__MOD_TEMP_COMPONENT_NAME__IF_1:status,safety-level,security}}

## Internal Components

.. code-block:: rst

### Component Name Static View

{{artifact:COMP_ARC_STA__MOD_TEMP_COMPONENT_NAME__2:status,safety-level,security}}

### Internal Component 1

{{artifact:COMP__COMPONENT_NAME_INTERNAL_1:status,safety-level,security}}

### Internal Component 2

{{artifact:COMP__COMPONENT_NAME_INTERNAL_2:status,safety-level,security}}

### Internal Component 3

{{artifact:COMP__COMPONENT_NAME_INTERNAL_3:status,safety-level,security}}

