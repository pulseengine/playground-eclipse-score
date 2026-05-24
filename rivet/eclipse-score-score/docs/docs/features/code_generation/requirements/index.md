---
id: DOC-INDEX-79597
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _codegen_requirements:

# Requirements

### The system uses a human-readable definition language.

{{artifact:FEAT_REQ__CODE_GENERATION__DEFINITIONLANGUAGE:status,safety-level,security}}}}

### Software Compute Units signal initialization failures by returning an Error indicating failure.

{{artifact:FEAT_REQ__CODE_GENERATION__INITIALIZATION:status,safety-level,security}}}}

### Software Compute Units correctly deallocate any dynamically allocated memory in the onShutdown function.

{{artifact:FEAT_REQ__CODE_GENERATION__DEINITIALIZATION:status,safety-level,security}}}}

### Software Compute Units do not spawn a variable number of threads.

{{artifact:FEAT_REQ__CODE_GENERATION__NOMULTITHREADING:status,safety-level,security}}}}

### Software Compute Units do not throw exceptions or "panic".

{{artifact:FEAT_REQ__CODE_GENERATION__ERROR_HANDLING1:status,safety-level,security}}}}

### Software Compute Units do not attempt to trigger program termination.

{{artifact:FEAT_REQ__CODE_GENERATION__ERROR_HANDLING2:status,safety-level,security}}}}

### Software Compute Units do not call their own standard interface methods.

{{artifact:FEAT_REQ__CODE_GENERATION__ERROR_HANDLING3:status,safety-level,security}}}}

### Software Compute Units implement transient error recovery mechanisms in onReset.

{{artifact:FEAT_REQ__CODE_GENERATION__ERROR_HANDLING4:status,safety-level,security}}}}

### Software Compute Units signal reset and recovery failures via the Error return value of onReset.

{{artifact:FEAT_REQ__CODE_GENERATION__ERROR_HANDLING5:status,safety-level,security}}}}

