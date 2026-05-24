---
id: DOC-SAFETY-MANUAL-2340
title: Safety Manual
type: specification
status: approved
tags: [eclipse-score]
---


### FEO Module Safety Manual

{{artifact:DOC__FEO_SAFETY_MANUAL:status,safety-level,security}}

# FEO Module Safety Manual

## Introduction/Scope

This is a first *partial draft* version of the FEO (Fixed Order Execution Environment) module safety manual.
For now it only contains Assumptions of Use related to the use of Rust libraries.

## Assumed Platform Safety Requirements

For FEO module the following safety related stakeholder requirements are assumed to define the top level functionality (purpose). I.e. from these all the feature and component requirements implemented are derived.

- [[STKH_REQ__APP_ARCHITECTURES__SUPPORT_TIME]]
- [[STKH_REQ__APP_ARCHITECTURES__SUPPORT_DATA]]
- [[STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_1]]
- [[STKH_REQ__DEPENDABILITY__SAFETY_FEATURES_4]]

## Assumptions of Use

#### Assumptions on the Environment

| Generally the assumption of the S-CORE platform SEooC is that it is integrated in a safe system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's safety concept.

### on_target_crates

{{artifact:AOU_REQ__FEO__ON_TARGET_CRATES:status,safety-level,security}}

### rust_core_lib

{{artifact:AOU_REQ__FEO__RUST_CORE_LIB:status,safety-level,security}}

### rust_std_lib_modules

{{artifact:AOU_REQ__FEO__RUST_STD_LIB_MODULES:status,safety-level,security}}

List of AoUs expected from the environment the platform / module runs on:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" in need["tags"]:
                results.append(need)

#### Assumptions on the User

| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform SEooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform SEooC safety case.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (including appropriate ASIL level)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a safety mechanism realized by some other S-CORE platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module SEooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe S-CORE platform persistency feature.

List of AoUs on the user of the platform features or the module of this safety manual:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" not in need["tags"]:
                results.append(need)

## Safety concept of the SEooC

| <Describe here the safety concept incl. which faults are taken care of, reactions of the implemented functions under anomalous operating conditions ... if this is not already documented sufficiently in the feature documentation "safety impact" section of all the features the module is used in.>

## Safety Anomalies

| Anomalies (bugs in ASIL SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.

## References

| <link to the user manual>
| <other links>
