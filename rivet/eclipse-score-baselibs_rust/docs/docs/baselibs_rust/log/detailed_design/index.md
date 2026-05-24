---
id: DOC-INDEX-17630
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_detailed_design_log:

# Detailed Design

### Log Detailed Design

{{artifact:DOC__LOG_DETAILED_DESIGN:status,safety-level,security}}

# Detailed Design for Component: Log

## Description

Log component consists of three units:

- `score_log` - modelled after `log` Rust library.
- `score_log_fmt` - replacement for `core::fmt` provided by Rust core library.
- `score_log_fmt_macro` - replacement for macros provided by Rust compiler:
  - `score_log_format_args!` - replacement for `format_args!`
  - `ScoreDebug` - replacement for `Debug`

Most common approach in Rust is that formatting always results in a string.
This means that the `log` library always receives a pre-formatted string.

Such approach is incompatible with the expectation that log sink is not always text-based.
Log component design is no longer string-based, and data frames can consist of multiple types.
Value is passed along with formatting options to the backend.

# Rationale Behind Decomposition into Units

All units provide an interface or an implementation to a well defined functionality.
Those units are not described in architecture, as they all form a monolithic logging frontend.

Such frontend shall remain transparent replacement to common functionalities provided by Rust.

## Static Diagrams for Unit Interactions

### Log class diagram

{{artifact:DD_STA__LOG__CLASS_DIAGRAM:status,safety-level,security}}

## Dynamic Diagrams for Unit Interactions

### Log operation

{{artifact:DD_DYN__LOG__LOG_OP:status,safety-level,security}}

### Log to level

{{artifact:DD_DYN__LOG__LOG_TO_LEVEL:status,safety-level,security}}

