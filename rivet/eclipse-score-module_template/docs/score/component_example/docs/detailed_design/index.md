---
id: DOC-INDEX-95357
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_detailed_design_template:

# Detailed Design

### [Your Component Name] Detailed Design

{{artifact:DOC__MOD_TEMP_COMPONENT_NAME_DETAILED_DESIGN:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Component.

    - Modify ``Your Component Name`` to be your Component Name
    - Modify ``id`` to be your Component Name in upper snake case preceded by ``doc__`` and followed by ``_detailed_design``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

# Detailed Design for Component: <Component Name>

## Description

| Design Decisions - For the documentation of the decision the [[GD_TEMP__CHANGE_DECISION_RECORD]] can be used.
| Design Constraints

# Rationale Behind Decomposition into Units

| mandatory: a motivation for the decomposition into one or more units.

## Static Diagrams for Unit Interactions

.. code-block:: rst

### <Title>

{{artifact:DD_STA__<COMPONENT>__<TITLE>:status,safety-level,security}}

## Dynamic Diagrams for Unit Interactions

.. code-block:: rst

### <Title>

{{artifact:DD_DYN__<COMPONENT>__<TITLE>:status,safety-level,security}}

## Units within the Component

In your rst file:

.. code-block:: rst

### cpp unit

{{artifact:SW_UNIT__<COMPONENT>__<TITLE>:status,safety-level,security}}

In your source file, any programming language, here with C++:

.. code-block:: cpp

   # need-Id: sw_unit__<Component>__<title>
   class <class name> {
      public:

   };

## Interface View

In your rst file:

.. code-block:: rst

### <here InterfaceDemo - change it>

{{artifact:SW_UNIT_INT__<COMPONENT>__<TITLE>:status,safety-level,security}}

In your source file, any programming language, here with C++:

.. code-block:: cpp

   # need-Id: sw_unit__<Component>__<title>
   class InterfaceDemo
   {
      public:
         virtual ~InterfaceDemo() {}
         virtual void OverrideMe() = 0;
   };

-  For cpp using doxygen comments

.. code-block:: cpp

   /**
      * @rst
      * .. sw_unit_int:: cpp unit
      *    :id: sw_unit_int__<Component>__<title>
      *    :belongs_to: <link to sw_unit id>
      *    :implements: <real_arc_int, real_arc_int_op>
      *
      *    This implements the ....
      * @endrst
   */

-  For rust

.. code-block:: rust

   //! .. sw_unit_int:: rust unit
   //!     :id: sw_unit_int__<Component>__<title>
   //!     :belongs_to: <link to sw_unit id>
   //!     :implements: <real_arc_int, real_arc_int_op>
   //!
   //!     This implements the ....
