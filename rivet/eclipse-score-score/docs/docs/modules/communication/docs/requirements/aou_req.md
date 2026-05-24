---
id: DOC-AOU-REQ-44184
title: Aou Req
type: specification
status: approved
tags: [eclipse-score]
---

# Assumptions of Use

### Communication Assumptions of Use

{{artifact:DOC__COMMUNICATION_AOU:status,safety-level,security}}

### Monotonic Semi-Dynamic Memory Allocation

{{artifact:AOU_REQ__COMMUNICATION__1:status,safety-level,security}}

### Correctly Configured Maximum Number of Subscribers

{{artifact:AOU_REQ__COMMUNICATION__2:status,safety-level,security}}

### Correctly configured maximum number of maximum elements per subscriber

{{artifact:AOU_REQ__COMMUNICATION__3:status,safety-level,security}}

### Correctly configured ASIL Level

{{artifact:AOU_REQ__COMMUNICATION__4:status,safety-level,security}}

### Only LoLa supported types

{{artifact:AOU_REQ__COMMUNICATION__5:status,safety-level,security}}

### No APIs from Implementation Namespace

{{artifact:AOU_REQ__COMMUNICATION__6:status,safety-level,security}}

### No guarantees for notifications

{{artifact:AOU_REQ__COMMUNICATION__7:status,safety-level,security}}

### Checking for possible message overflow

{{artifact:AOU_REQ__COMMUNICATION__8:status,safety-level,security}}

### Different user for ASIL and QM processes

{{artifact:AOU_REQ__COMMUNICATION__9:status,safety-level,security}}

### Config on a safe filesystem

{{artifact:AOU_REQ__COMMUNICATION__10:status,safety-level,security}}

### No static context support

{{artifact:AOU_REQ__COMMUNICATION__11:status,safety-level,security}}

### No guarantee in availability of services

{{artifact:AOU_REQ__COMMUNICATION__12:status,safety-level,security}}

### No notification on termination of producer

{{artifact:AOU_REQ__COMMUNICATION__13:status,safety-level,security}}

### Check for nullptr on Allocate()

{{artifact:AOU_REQ__COMMUNICATION__14:status,safety-level,security}}

### One producer only one AllocateePtr

{{artifact:AOU_REQ__COMMUNICATION__15:status,safety-level,security}}

### No Copy-Send() while holding AllocateePtr.

{{artifact:AOU_REQ__COMMUNICATION__16:status,safety-level,security}}

### None reentrant methods per event instance

{{artifact:AOU_REQ__COMMUNICATION__17:status,safety-level,security}}

### Skeleton alive while its AllocateePtr being used

{{artifact:AOU_REQ__COMMUNICATION__18:status,safety-level,security}}

### Event Subscription active while holding SamplePtr

{{artifact:AOU_REQ__COMMUNICATION__19:status,safety-level,security}}

### Non-Terminating callbacks

{{artifact:AOU_REQ__COMMUNICATION__20:status,safety-level,security}}

### Valid callbacks while proxy alive

{{artifact:AOU_REQ__COMMUNICATION__21:status,safety-level,security}}

### Quality of data is dependent on producer

{{artifact:AOU_REQ__COMMUNICATION__22:status,safety-level,security}}

### Validity of pointer on LoLa pointer

{{artifact:AOU_REQ__COMMUNICATION__23:status,safety-level,security}}

### LoLa Memory only accessed through LoLa

{{artifact:AOU_REQ__COMMUNICATION__24:status,safety-level,security}}

### No shared memory allocation in namespace lola

{{artifact:AOU_REQ__COMMUNICATION__25:status,safety-level,security}}

### LoLa specific QNX Messaging End-Points only accessed through LoLa

{{artifact:AOU_REQ__COMMUNICATION__26:status,safety-level,security}}

### aragen not safe

{{artifact:AOU_REQ__COMMUNICATION__27:status,safety-level,security}}

### unsupported data-types

{{artifact:AOU_REQ__COMMUNICATION__28:status,safety-level,security}}

### No guarantee on execution time

{{artifact:AOU_REQ__COMMUNICATION__29:status,safety-level,security}}

### Usage of configuration "oversubscription"

{{artifact:AOU_REQ__COMMUNICATION__30:status,safety-level,security}}

### Same compiler settings for provider and consumer side

{{artifact:AOU_REQ__COMMUNICATION__31:status,safety-level,security}}

### Event or Field reception via GenericProxy needs specific care

{{artifact:AOU_REQ__COMMUNICATION__32:status,safety-level,security}}

### Correctly configured events/fields per service type

{{artifact:AOU_REQ__COMMUNICATION__34:status,safety-level,security}}

