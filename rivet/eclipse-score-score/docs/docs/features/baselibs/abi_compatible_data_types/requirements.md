---
id: DOC-REQUIREMENTS-71588
title: Requirements
type: specification
status: approved
tags: [eclipse-score]
---

# Requirements

# ABI Compatibility

## Restrictions on Native Types

### Restrict boolean size

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__BOOL_SZ:status,safety-level,security}}

### Fixed-width integers

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__INT_FIX:status,safety-level,security}}

### Limit floating-point sizes

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__FLT_SZ:status,safety-level,security}}

### Characters

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__CHAR:status,safety-level,security}}

### Fixed-size arrays

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ARR_FIX:status,safety-level,security}}

### Struct and tuple ABI layout

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ST_TPL:status,safety-level,security}}

### Explicit enum representation

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ENUM_UDR:status,safety-level,security}}

### Disallow pointers and metadata

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__NOP_MT:status,safety-level,security}}

### Compiler-agnostic ABI

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__COMPABI:status,safety-level,security}}

## Custom Types

#### Vector

### Provide AbiVec<T,N>

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__PRV_ABV:status,safety-level,security}}

### AbiVec field semantics

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABV_FLD:status,safety-level,security}}

### AbiVec API

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABV_NOA:status,safety-level,security}}

### AbiVec overflow check

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABV_OVF:status,safety-level,security}}

#### String

### Provide AbiString<N>

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__PRV_ABS:status,safety-level,security}}

### AbiString field semantics

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABS_FLD:status,safety-level,security}}

### AbiString API

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABS_NOA:status,safety-level,security}}

### AbiString overflow check

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABS_OVF:status,safety-level,security}}

#### Option

### Provide AbiOption<T>

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__PRV_ABO:status,safety-level,security}}

### AbiOption is_some flag

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABO_FLG:status,safety-level,security}}

### AbiOption API

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ABO_API:status,safety-level,security}}

#### Result

### Provide AbiResult<T,E>

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__PRV_ARI:status,safety-level,security}}

### AbiResult is_err flag

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ARI_FLG:status,safety-level,security}}

### AbiResult API

{{artifact:FEAT_REQ__ABI_COMPATIBLE_DATA_TYPES__ARI_API:status,safety-level,security}}

