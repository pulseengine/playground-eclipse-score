---
id: DOC-COMPONENT-ARCHITECTURE-48496
title: Component Architecture
type: specification
status: approved
tags: [eclipse-score]
---

### FEO Component Architecture

{{artifact:DOC__COMPONENT_FEO_ARCHITECTURE:status,safety-level,security}}}}

# FEO Component Architecture

## Overview

The current implementation of the feature "FEO" (Fixed Execution Order Framework) consists of a main
component (called "FEO" component) and a set of auxiliary components that will be either replaced by or
turned into wrappers to components from other S-CORE features. In the latter case, these wrappers will
possibly become sub-components of the main component.

This document describes the architecture of the main component "FEO".

## Description

# Sub-Components

The main component "FEO" consists of the following sub-components:

* feo: Implements activities, threads, agents, and scheduling
* feo-cpp-build: C++ and Rust Code simplifying the integration of C++ components
* feo-cpp-macros: Rust proc-macros simplifying the integration of C++ components.

Rust requires proc-macros to reside in their own crate, therefore the latter two
sub-components cannot easily be combined into a single one.

# Rationale Behind Architecture Decomposition

The main component "FEO" has been split into three sub-components mainly according to usability
considerations and Rust compiler constraints. (Rust proc-macros must reside in their own crate.)

## Static Architecture

### FEO Main

{{artifact:COMP__FEO_MAIN:status,safety-level,security}}}}

### Static Architecture

{{artifact:COMP_ARC_STA__FEO__MAIN:status,safety-level,security}}}}

## Dynamic Architecture

### Dynamic Architecture

{{artifact:COMP_ARC_DYN__FEO__MAIN:status,safety-level,security}}}}

## Interfaces

### feo::agent::PrimaryConfig

{{artifact:REAL_ARC_INT__FEO__PRIMARY_CONFIG:status,safety-level,security}}}}

### feo::agent::Primary

{{artifact:REAL_ARC_INT__FEO__PRIMARY:status,safety-level,security}}}}

### feo::agent::SecondaryConfig

{{artifact:REAL_ARC_INT__FEO__SECONDARY_CONFIG:status,safety-level,security}}}}

### feo::agent::Secondary

{{artifact:REAL_ARC_INT__FEO__SECONDARY:status,safety-level,security}}}}

### feo::activity::Activity

{{artifact:REAL_ARC_INT__FEO__ACTIVITY:status,safety-level,security}}}}

