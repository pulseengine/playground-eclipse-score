---
id: DOC-SAFETY-MANUAL-36279
title: Safety Manual
type: specification
status: approved
tags: [eclipse-score]
---

# Safety Manual

### Baselibs Safety Manual

{{artifact:DOC__BASELIBS_SAFETY_MANUAL:status,safety-level,security}}

## Introduction/Scope

This is the safety manual for baselibs module which is a collection of several utilities of common use.

## Assumed Platform Safety Requirements

For the Baselibs module the following safety related stakeholder requirements are assumed to define the top level functionality (purpose) of the module. I.e. from these all the feature and component requirements implemented are derived.

- [[STKH_REQ__FUNCTIONAL_REQ__BASE_LIBRARIES]] - is QM, but some of the libraries combine this with the next requirement
- [[STKH_REQ__DEPENDABILITY__AUTOMOTIVE_SAFETY]]
- [[STKH_REQ__DEV_EXPERIENCE__PROG_LANGUAGES]] - is QM, but some of the libraries combine this with the previous requirement

This means that not all baselibs libraries and language API are provided in ASIL B.
So for Baselibs the definition of the assumed safety requirement(s) of each of the ASIL B libraries are defined in the following feature requirements:

- bitmanipulation library: [[FEAT_REQ__BASELIBS__BITMANIPULATION]]
- concurrency library: [[FEAT_REQ__BASELIBS__CONCURRENCY_LIBRARY]]
- containers library: [[FEAT_REQ__BASELIBS__CONTAINERS_LIBRARY]]
- filesystem library: [[FEAT_REQ__BASELIBS__FILESYSTEM_LIBRARY]]
- flatbuffers library: [[FEAT_REQ__BASELIBS__FLATBUFFERS_LIBRARY]]
- json library: [[FEAT_REQ__BASELIBS__JSON_LIBRARY]]
- memory library: [[FEAT_REQ__BASELIBS__MEMORY_LIBRARY]]
- result library: [[FEAT_REQ__BASELIBS__RESULT_LIBRARY]]
- safecpp, static_reflection_with_serialization, utils [[FEAT_REQ__BASELIBS__CORE_UTILITIES]]

## Assumptions of Use

#### Assumptions on the Environment

| Generally the assumption of the project platform SEooC is that it is integrated in a safe system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's safety concept.
| The platform-wide AoUs are collected in [[DOC__PLATFORM_ASSUMPTIONS]]
|
| To support [[AOU_REQ__PLATFORM__SAFETY_MATCHING]]:
| <List here all the OS/libcxx calls the module expects to be safe.>

List of additional AoUs expected from the environment the module runs on:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" in need["tags"] and "baselibs" in need["tags"]:
                results.append(need)

#### Assumptions on the User

| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform SEooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform SEooC safety case.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (including appropriate ASIL level)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a safety mechanism realized by some other project platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module SEooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe project platform persistency feature.

List of AoUs on the user of the module of this safety manual:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" not in need["tags"] and "baselibs" in need["tags"]:
                results.append(need)

## Safety concept of the SEooC

| <Describe here the safety concept incl. which faults are taken care of, reactions of the implemented functions under anomalous operating conditions ... if this is not already documented sufficiently in the feature documentation "safety impact" section of all the features the module is used in.>

## Safety Anomalies

| Anomalies (bugs in ASIL SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.

## References

| <link to the user manual>
| <other links>
