---
id: DOC-INDEX-47618
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _feature_architecture_persistency:

# Architecture

### Persistency KVS Feature Architecture

{{artifact:DOC__PERSISTENCY_ARCHITECTURE:status,safety-level,security}}

### Persistency

{{artifact:FEAT__PERSISTENCY:status,safety-level,security}}

### persistency::kvs

{{artifact:COMP__PERSISTENCY_KVS:status,safety-level,security}}

--------

The Key-Value-Storage (kvs) provides the capability to efficiently store,
retrieve, and manage key-value pairs in a persistent storage system.

## Description

- kvs organize data as pairs, where each unique key is associated with a specific value.
  The key acts as a unique identifier for getting the value.
- The data is persisted in JSON format to the file system, providing a human-readable,
  and widely supported way to store and manage key-value pairs.
- The JSON data persisted is according to RFC-8259.

# Rationale Behind Architecture Decomposition

- The architecture is decomposed to include a dedicated JSON parser component (json) to facilitate the persistent storage of data in JSON format.
- The architecture is decomposed to include a FileStorage component (fs) to read and write to the file system.

## Glossary

- User: Program code that is written by a person that initiates the given
  functionality call or receives a callback.

## Static Architecture

### Static Architecture

{{artifact:FEAT_ARC_STA__PERSISTENCY__STATIC:status,safety-level,security}}

## Dynamic Architecture

### Check if key contains default value

{{artifact:FEAT_ARC_DYN__PERSISTENCY__CHECK_KEY_DEFAULT:status,safety-level,security}}

### Delete key from KVS instance

{{artifact:FEAT_ARC_DYN__PERSISTENCY__DELETE_KEY:status,safety-level,security}}

### Flush to permanent storage

{{artifact:FEAT_ARC_DYN__PERSISTENCY__FLUSH:status,safety-level,security}}

### Read key value

{{artifact:FEAT_ARC_DYN__PERSISTENCY__READ_KEY:status,safety-level,security}}

### Read data from permanent storage

{{artifact:FEAT_ARC_DYN__PERSISTENCY__READ_FROM_STORAGE:status,safety-level,security}}

### Write value to key

{{artifact:FEAT_ARC_DYN__PERSISTENCY__WRITE_KEY:status,safety-level,security}}

### Restore snapshot

{{artifact:FEAT_ARC_DYN__PERSISTENCY__SNAPSHOT_RESTORE:status,safety-level,security}}

## Logical Interfaces

### Ikvs

{{artifact:LOGIC_ARC_INT__PERSISTENCY__INTERFACE:status,safety-level,security}}

