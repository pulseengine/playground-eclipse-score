---
id: DOC-INDEX-51226
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Requirements

### Orchestration Requirements

{{artifact:DOC__ORCHESTRATION_REQUIREMENTS:status,safety-level,security}}

# Executor

## Task Management

### Async Cooperative Task Runtime

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_ASYNC_RT:status,safety-level,security}}

### Yielding Guidelines for Long Operations

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_YIELDING:status,safety-level,security}}

### Dedicated Threads for Blocking Operations

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_BLOCK_THREADS:status,safety-level,security}}

## Special Tasks and Preemption

### Preemptive Scheduling for Safety Tasks

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_PREEMPT_SAFETY:status,safety-level,security}}

### Separate Priority for Safety Tasks

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_SAFE_TASK_PRIO:status,safety-level,security}}

## Thread Pool Configuration

### Fixed-Size Thread Pool

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_FIXED_POOL:status,safety-level,security}}

### Uniform OS Priority for Non-Safety Threads

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_OS_PRIO:status,safety-level,security}}

### Configurable Thread Affinity

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_THREAD_AFF:status,safety-level,security}}

### Isolated Thread Pools

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_POOL_ISOLATION:status,safety-level,security}}

## Task Scheduling

### No Internal Priorities for Cooperative Tasks

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_NO_INT_PRIOS:status,safety-level,security}}

### FIFO or Fairness Scheduling

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_FIFO_FAIR_SCHED:status,safety-level,security}}

### Scale via Additional Executors

{{artifact:FEAT_REQ__ORCHESTRATION__EXEC_SCALE_INSTANCES:status,safety-level,security}}

# Orchestrator Requirements

## Program Definition

### Static Program Execution Graphs

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_STATIC_GRAPHS:status,safety-level,security}}

### Explicit Control Flows and Timing

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_CTRL_FLOWS:status,safety-level,security}}

### Event-Based Synchronization

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_EVENT_SYNC:status,safety-level,security}}

### Fault-Handling and Monitors

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_FAULT_MON:status,safety-level,security}}

## API Design

### Code-First Integration API

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_CODE_API:status,safety-level,security}}

## Execution Model

### Single-Executor Deployment

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_SINGLE_DEPLOY:status,safety-level,security}}

### Multi-Program Support per Executor

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_MULTI_PROG:status,safety-level,security}}

### Event-Only Communication

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_EVENT_COMM:status,safety-level,security}}

## Special Safety Task Integration

### Safety Tasks in Programs

{{artifact:FEAT_REQ__ORCHESTRATION__ORCH_SAFETY_TASKS:status,safety-level,security}}

# Observability Requirements

### Trace Correlation Points

{{artifact:FEAT_REQ__ORCHESTRATION__OBSV_TRACE_CORR:status,safety-level,security}}

### Task Lifecycle and Queue Metrics

{{artifact:FEAT_REQ__ORCHESTRATION__OBSV_LIFECYCLE_QM:status,safety-level,security}}

### Program Flow and Timing Visibility

{{artifact:FEAT_REQ__ORCHESTRATION__OBSV_FLOW_VIS:status,safety-level,security}}

### Integration with Tracing Frameworks

{{artifact:FEAT_REQ__ORCHESTRATION__OBSV_FW_INTEG:status,safety-level,security}}

# External Supervision Requirements

### Health Indicators Export

{{artifact:FEAT_REQ__ORCHESTRATION__EXT_HEALTH_INDS:status,safety-level,security}}

### Internal Task Health Verification

{{artifact:FEAT_REQ__ORCHESTRATION__EXT_TASK_HEALTH:status,safety-level,security}}

# General Constraints

### Determinism and Scalability

{{artifact:FEAT_REQ__ORCHESTRATION__GEN_DET_SCALE:status,safety-level,security}}

### Explicit Preemption Activation

{{artifact:FEAT_REQ__ORCHESTRATION__GEN_PREEMPT_ACT:status,safety-level,security}}

### Exclusive Use of IPC Feature for Inter Process Synchronization

{{artifact:FEAT_REQ__ORCHESTRATION__GEN_EXCL_IPC:status,safety-level,security}}

