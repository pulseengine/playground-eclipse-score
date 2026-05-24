---
id: DOC-INDEX-99033
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _component_architecture_log:

# Component Architecture

### Log Architecture

{{artifact:DOC__LOG_ARCHITECTURE:status,safety-level,security}}

## Overview

Document describes Log component architecture.

## Description

Log component is modelled after the `log` library, which is ubiquitous in Rust ecosystem.
This provides familiar APIs and syntax - provided APIs can be replaced at compile time with `log`.

Component provides new formatting functionality (replacement to `core::fmt`) to ensure improved flexibility in formatting on backend side.
E.g., numeric types are formatted by the backend, and not by the core library.

Even though design is similar - existing `log` implementations are not compatible.

# Rationale Behind Architecture Decomposition

Architecture is not decomposed.
Log component is a monolithic frontend.

## Static Architecture

### Log (Static View)

{{artifact:COMP_ARC_STA__LOG__STATIC_VIEW:status,safety-level,security}}

## Dynamic Architecture

### Register global logger

{{artifact:COMP_ARC_DYN__LOG__REGISTER_GLOBAL_LOGGER:status,safety-level,security}}

### Log with global logger instance

{{artifact:COMP_ARC_DYN__LOG__LOG_WITH_GLOBAL_LOGGER:status,safety-level,security}}

### Log with local logger instance

{{artifact:COMP_ARC_DYN__LOG__LOG_WITH_LOCAL_LOGGER:status,safety-level,security}}

## Interfaces

### Log interface

{{artifact:REAL_ARC_INT__LOG__INTERFACE:status,safety-level,security}}

