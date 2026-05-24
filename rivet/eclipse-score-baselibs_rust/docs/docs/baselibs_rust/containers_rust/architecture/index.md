---
id: DOC-INDEX-12405
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Rust Containers Architecture

### Rust Containers Architecture

{{artifact:DOC__CONTAINERS_RUST_ARCHITECTURE:status,safety-level,security}}

## Overview

The implementation of the containers library comprises two main parts:

- The generic storage abstraction for elements, with two concrete implementations:
  heap-allocated and inline storage
- The generic logic for each container type, each of which has two specializations:
  one using heap-allocated storage, and one using inline storage

## Static Architecture

### Rust Containers

{{artifact:COMP_ARC_STA__BASELIBS_RUST__CONTAINERS_RUST:status,safety-level,security}}

## Interfaces

### Fixed-Capacity Vector

{{artifact:LOGIC_ARC_INT__B_R__FIXVEC:status,safety-level,security}}

### Push

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXVEC_PUSH:status,safety-level,security}}

### Pop

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXVEC_POP:status,safety-level,security}}

### Clear

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXVEC_CLEAR:status,safety-level,security}}

### Index

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXVEC_INDEX:status,safety-level,security}}

### Iterate

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXVEC_ITERATE:status,safety-level,security}}

### Inline-Storage Vector

{{artifact:LOGIC_ARC_INT__B_R__INLINEVEC:status,safety-level,security}}

### Push

{{artifact:LOGIC_ARC_INT_OP__CONT__INLINEVEC_PUSH:status,safety-level,security}}

### Pop

{{artifact:LOGIC_ARC_INT_OP__CONT__INLINEVEC_POP:status,safety-level,security}}

### Clear

{{artifact:LOGIC_ARC_INT_OP__CONT__INLINEVEC_CLEAR:status,safety-level,security}}

### Index

{{artifact:LOGIC_ARC_INT_OP__CONT__INLINEVEC_INDEX:status,safety-level,security}}

### Iterate

{{artifact:LOGIC_ARC_INT_OP__CONT__INLINEVEC_ITERATE:status,safety-level,security}}

### Fixed-Capacity Queue

{{artifact:LOGIC_ARC_INT__B_R__FIXQUEUE:status,safety-level,security}}

### Push Front

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXQUEUE_PUSHFRONT:status,safety-level,security}}

### Push Back

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXQUEUE_PUSHBACK:status,safety-level,security}}

### Pop Front

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXQUEUE_POPFRONT:status,safety-level,security}}

### Pop Back

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXQUEUE_POPBACK:status,safety-level,security}}

### Clear

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXQUEUE_CLEAR:status,safety-level,security}}

### Iterate

{{artifact:LOGIC_ARC_INT_OP__CONT__FIXQUEUE_ITERATE:status,safety-level,security}}

### Inline-Storage Queue

{{artifact:LOGIC_ARC_INT__B_R__INLQUEUE:status,safety-level,security}}

### Push Front

{{artifact:LOGIC_ARC_INT_OP__CONT__INLQUEUE_PUSHFRONT:status,safety-level,security}}

### Push Back

{{artifact:LOGIC_ARC_INT_OP__CONT__INLQUEUE_PUSHBACK:status,safety-level,security}}

### Pop Front

{{artifact:LOGIC_ARC_INT_OP__CONT__INLQUEUE_POPFRONT:status,safety-level,security}}

### Pop Back

{{artifact:LOGIC_ARC_INT_OP__CONT__INLQUEUE_POPBACK:status,safety-level,security}}

### Clear

{{artifact:LOGIC_ARC_INT_OP__CONT__INLQUEUE_CLEAR:status,safety-level,security}}

### Iterate

{{artifact:LOGIC_ARC_INT_OP__CONT__INLQUEUE_ITERATE:status,safety-level,security}}

