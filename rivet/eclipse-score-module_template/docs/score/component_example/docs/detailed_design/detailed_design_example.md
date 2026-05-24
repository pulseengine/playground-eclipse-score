---
id: DOC-DETAILED-DESIGN-EXAMPLE-9331
title: Detailed Design Example
type: specification
status: approved
tags: [eclipse-score]
---

# Example: Detailed Design

## Description

 - component is split into two units unit1 and unit2 based on single responsibility principle.
 - unit2 is injected to unit1 one via dependency injection for testability.

## Static Diagrams for Unit Interactions

### dd example static

{{artifact:DD_STA__EXAMPLE_FEATURE__APPROVER:status,safety-level,security}}

## Dynamic Diagrams for Unit Interactions

### dd example dynamic

{{artifact:DD_DYN__EXAMPLE_FEATURE__DYNAMIC:status,safety-level,security}}

## Units within the Component

From here onwards the needs are defined in the source code and will be automatically generated and linked via doxygen.

# SW Unit

The unit description is generated from the source code and linked with
the need ID sw_unit__example_feature__unit1.

# Interface

The interface description is generated from the source code and linked with
the need ID sw_unit_int__example_feature__u1_i1.

# SW Unit

The unit description is generated from the source code and linked with
the need ID sw_unit__example_feature__unit2.

# Interface

The interface description is generated from the source code and linked with
the need ID sw_unit_int__example_feature__u2_i2.
