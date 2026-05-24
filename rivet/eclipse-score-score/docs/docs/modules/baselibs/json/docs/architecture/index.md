---
id: DOC-INDEX-34930
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# JSON Component Architecture

### JSON Architecture

{{artifact:DOC__JSON_ARCHITECTURE:status,safety-level,security}}

## Overview

The component JSON implements functionality for reading/parsing JSON data and also to write.
It provides currently only a C++ API.

## Requirements Linked to Component Architecture

See the "fulfils" links in static and dynamic architecture below.

## Description

JSON provides an abstraction layer to underlying implementations, in first iteration there is only one
implementation provided. But generally there is a "Wrapper" and an "Implementation" lower-level component.

Design Decisions:

It was decided to use the nlohman_json OSS library (see `nlohman/json <https://github.com/nlohmann/json>`_). This decision still has to be documented (TBD).

JSON writing functionality is implemented in the "Wrapper", i.e. the nlohman_json OSS library is not used for this.
Reasoning is that this functionality is reused from an already qualified baselibs implementation.

Design Constraints:

The feature description states that this component provides a "JSON abstraction layer that can switch between different parsers/serializers under the hood."

# Rationale Behind Architecture Decomposition

The decomposition in a wrapper and an implemetation component already comes from the feature definition,
the main driver is to re-use existing implementation(s), enable switch of implementation but providing a stable API.

## Static Architecture

### JSON

{{artifact:COMP__BASELIBS_JSON:status,safety-level,security}}

### JSON Static view

{{artifact:COMP_ARC_STA__BASELIBS__JSON:status,safety-level,security}}

## Dynamic Architecture

### JSON dynamic arch

{{artifact:COMP_ARC_DYN__BASELIBS__JSON_DYNAMIC_VIEW:status,safety-level,security}}

## Interfaces

### IJson

{{artifact:LOGIC_ARC_INT__BASELIBS__JSON:status,safety-level,security}}

### Parse

{{artifact:LOGIC_ARC_INT_OP__BASELIBS__PARSE:status,safety-level,security}}

### Write

{{artifact:LOGIC_ARC_INT_OP__BASELIBS__WRITE:status,safety-level,security}}

## Lower Level Components

### JSON-Wrapper

{{artifact:COMP__BASELIBS_JSON_WRAPPER:status,safety-level,security}}

### nlohman-JSON

{{artifact:COMP__BASELIBS_NLOHMAN_JSON:status,safety-level,security}}

