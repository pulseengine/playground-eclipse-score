---
id: DOC-REQUIREMENTS-81764
title: Requirements
type: specification
status: approved
tags: [eclipse-score]
---

# TC8 Conformance Test Requirements

## Feature Requirement

The following feature requirement establishes TC8 SOME/IP conformance testing
as a formal verification activity for the SOME/IP Gateway's protocol stack.

### TC8 SOME/IP Protocol Conformance

{{artifact:FEAT_REQ__TC8_CONFORMANCE__CONFORMANCE:status,safety-level,security}}

## Component Requirements — Service Discovery

The following component requirements define the high-priority TC8 conformance
tests for SOME/IP Service Discovery (SD), aligned with SOME/IP-SD Protocol
Specification (AUTOSAR PRS_SOMEIP_SD).

### TC8 SD Offer Entry Format Validation

{{artifact:COMP_REQ__TC8_CONFORMANCE__SD_OFFER_FORMAT:status,safety-level,security}}

### TC8 SD Cyclic Offer Timing

{{artifact:COMP_REQ__TC8_CONFORMANCE__SD_CYCLIC_TIMING:status,safety-level,security}}

### TC8 SD FindService Response

{{artifact:COMP_REQ__TC8_CONFORMANCE__SD_FIND_RESPONSE:status,safety-level,security}}

### TC8 SD Subscribe Eventgroup Lifecycle

{{artifact:COMP_REQ__TC8_CONFORMANCE__SD_SUB_LIFECYCLE:status,safety-level,security}}

### TC8 SD Initial Delay and Repetitions Phase

{{artifact:COMP_REQ__TC8_CONFORMANCE__SD_PHASES_TIMING:status,safety-level,security}}

## Component Requirements — SOME/IP Message Format

### TC8 SOME/IP Response Header Validation

{{artifact:COMP_REQ__TC8_CONFORMANCE__MSG_RESP_HEADER:status,safety-level,security}}

### TC8 SOME/IP Error Return Codes

{{artifact:COMP_REQ__TC8_CONFORMANCE__MSG_ERROR_CODES:status,safety-level,security}}

## Component Requirements — Event Notification

### TC8 Event Notification Subscription Lifecycle

{{artifact:COMP_REQ__TC8_CONFORMANCE__EVT_SUBSCRIPTION:status,safety-level,security}}

## Traceability Summary

The following table links each component requirement to the SOME/IP
specification section it verifies.

.. list-table:: TC8 Requirement Traceability Matrix
   :widths: 30 20 30 20
   :header-rows: 1

   * - Requirement ID
     - TC8 Test IDs
     - SOME/IP Spec Reference
     - Safety
   * - ``comp_req__tc8_conformance__sd_offer_format``
     - TC8-SD-001, -002
     - SOME/IP-SD §4.1.2.1, §4.1.2.3
     - QM
   * - ``comp_req__tc8_conformance__sd_cyclic_timing``
     - TC8-SD-003
     - SOME/IP-SD §4.1.1 (Main Phase)
     - QM
   * - ``comp_req__tc8_conformance__sd_find_response``
     - TC8-SD-004, -005
     - SOME/IP-SD §4.1.2.2
     - QM
   * - ``comp_req__tc8_conformance__sd_sub_lifecycle``
     - TC8-SD-006, -007, -008
     - SOME/IP-SD §4.1.2.4–4.1.2.6
     - QM
   * - ``comp_req__tc8_conformance__sd_phases_timing``
     - TC8-SD-009, -010
     - SOME/IP-SD §4.1.1 (Phases)
     - QM
   * - ``comp_req__tc8_conformance__msg_resp_header``
     - TC8-MSG-001, -002, -005, -008
     - SOME/IP §4.1.3, §4.1.4, §4.1.6
     - QM
   * - ``comp_req__tc8_conformance__msg_error_codes``
     - TC8-MSG-003, -004, -006
     - SOME/IP §4.1.7 (Table 4.14)
     - QM
   * - ``comp_req__tc8_conformance__evt_subscription``
     - TC8-EVT-001–004, -006
     - SOME/IP §5.1, SOME/IP-SD §4.1.2.4
     - QM
