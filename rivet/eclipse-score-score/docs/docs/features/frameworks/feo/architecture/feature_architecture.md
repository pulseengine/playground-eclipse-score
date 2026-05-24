---
id: DOC-FEATURE-ARCHITECTURE-57372
title: Feature Architecture
type: specification
status: approved
tags: [eclipse-score]
---


### FEO Feature Architecture

{{artifact:DOC__FRAMEWORKS_FEO_FEAT_ARCH:status,safety-level,security}}

# FEO Feature Architecture

## Overview

The current implementation of the feature "FEO" (Fixed Execution Order Framework) consists of a main
component and a set of auxiliary components that will be either replaced by or turned into
wrappers to components from other S-CORE features. In the latter case, these wrappers will possibly
become sub-components of the main component.

## Description

# Feature Components

* feo: The main component

* feo_com: Interface to inter-activity data communication

  Will be replaced by or become a wrapper of the interface `mw::com` provided by the feature
  "Communication".

* feo_log: Logging macros (Rust and C++) and logger implementation

  Consists of the following sub-components:
  - feo_log: Logging macros (Rust and C++)
  - feo_logger: Logger implementation (Rust and C++)

  Will be replaced by or become a wrapper of an interface provided by the feature "Logging".

* feo_time: Interface to system clocks

  Will be replaced by or become a wrapper of an interface provided by the feature "Time".

* feo_tracing: Subscriber for Rust tracing API

  Will be replaced by or become a wrapper of an interface provided by the feature "Logging".

# Utility and Example Applications

* feo_tracer: A simple tracing daemon receiving trace messages from all feo agents

  Consists of the following sub-components:
  - feo_tracer: Tracing daemon
  - perfetto-model: Support for the Perfetto trace file format

  Will be replaced by an alternative solution provided by the feature "Tracing".

* logd: A simple logging daemon receiving log output from all feo agents

  Will be replaced by an alternative solution provided by the feature "Logging".

* mini-adas: Example of a minimal dummy ADAS activity set

* cycle-benchmark: A simple configurable benchmarking application to measure the FEO cycle time

# Rationale Behind Architecture Decomposition

The feature has been split into a main component, auxiliary components as well as utility and
example applications. The main component implements the functionality that is expected to
be required by most systems making use of FEO. Auxiliary components are parts of the code
that are likely to be replaced by components from other features in the future. They have been
split according to their functionalities. Utility applications are optional
pieces of software that can be run to test or demonstrate the feature functionality but are not
expected to be used directly in a productive system. They may become obsolete in future.

## Static Architecture

### Feature FEO

{{artifact:FEAT__FEO:status,safety-level,security}}

### Static Architecture

{{artifact:FEAT_ARC_STA__FEO__MAIN:status,safety-level,security}}

## Dynamic Architecture

### Dynamic Architecture

{{artifact:FEAT_ARC_DYN__FEO__MAIN:status,safety-level,security}}

## Logical Interfaces

### Activity

{{artifact:LOGIC_ARC_INT__FEO__ACTIVITY:status,safety-level,security}}

### Primary Agent

{{artifact:LOGIC_ARC_INT__FEO__PRIM_AGENT:status,safety-level,security}}

### Secondary Agent

{{artifact:LOGIC_ARC_INT__FEO__SEC_AGENT:status,safety-level,security}}

### Lifecycle Listener

{{artifact:LOGIC_ARC_INT__FEO__LIFECYCLE:status,safety-level,security}}

