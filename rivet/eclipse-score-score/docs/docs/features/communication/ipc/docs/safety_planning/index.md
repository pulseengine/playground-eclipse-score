---
id: DOC-INDEX-37062
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _safety_planning_ipc:

# Feature Safety Work Products List

### Communication IPC Safety WPs

{{artifact:DOC__COM_IPC_SAFETY_WP:status,safety-level,security}}}}

# Tailoring

Additional to the tailoring in the SW platform project as defined in the [[DOC__PLATFORM_SAFETY_PLAN]] we define here the additional tailoring on feature level.

- Excluded for this feature are additionally the following work products (and their related requirements):

  - [[WP__REQUIREMENTS_INSPECT]]: in version 0.5 the inspections have to be done by the user
  - [[WP__SW_ARCH_VERIFICATION]]: in version 0.5 the inspections have to be done by the user

# Inter-process Communication Safety Work Products

.. list-table:: Feature Inter-process Communication Workproducts
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to WP

    * - [[WP__FEAT_REQUEST]]
      - [[GD_TEMP__CHANGE_FEATURE_REQUEST]]
      - copy('status', need_id='gd_temp__change_feature_request')
      - [[DOC__COM_IPC]]

    * - [[WP__REQUIREMENTS_FEAT]]
      - [[GD_TEMP__REQ_FEAT_REQ]]
      - copy('status', need_id='gd_temp__req_feat_req')
      - [[DOC__IPC_REQUIREMENTS]], [[DOC__COMMUNICATION_REQUIREMENTS]]

    * - [[WP__REQUIREMENTS_FEAT_AOU]]
      - [[GD_TEMP__REQ_AOU_REQ]]
      - copy('status', need_id='gd_temp__req_aou_req')
      - [[DOC__IPC_REQUIREMENTS]], [[DOC__COMMUNICATION_REQUIREMENTS]]

    * - [[WP__FEATURE_ARCH]]
      - [[GD_TEMP__ARCH_FEATURE]]
      - copy('status', need_id='gd_temp__arch_feature')
      - [[DOC__IPC_ARCHITECTURE]]

    * - [[WP__FEATURE_FMEA]]
      - [[GD_TEMP__FEAT_SAF_FMEA]]
      - copy('status', need_id='gd_temp__feat_saf_fmea')
      - [[DOC__IPC_FMEA]]

    * - [[WP__FEATURE_DFA]]
      - [[GD_TEMP__FEAT_SAF_DFA]]
      - copy('status', need_id='gd_temp__feat_saf_dfa')
      - [[DOC__IPC_DFA]]

    * - [[WP__REQUIREMENTS_INSPECT]]
      - [[GD_CHKLST__REQ_INSPECTION]]
      - copy('status', need_id='gd_chklst__req_inspection')
      - tailored

    * - [[WP__SW_ARCH_VERIFICATION]]
      - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
      - copy('status', need_id='gd_chklst__arch_inspection_checklist')
      - tailored

    * - [[WP__VERIFICATION_FEAT_INT_TEST]]
      - [[GD_GUIDL__VERIFICATION_GUIDE]]
      - copy('status', need_id='gd_guidl__verification_guide')
      - <Link to WP>

# Feature Safety Package

To create the safety package (according to [[GD_GUIDL__SAF_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Feature Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_features_communication

## Feature Requirements Status

.. needtable::
   :style: table
   :types: feat_req
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

.. needtable::
   :style: table
   :types: feat_req
   :tags: com
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature AoU Status

.. needtable::
   :style: table
   :types: aou_req
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

.. needtable::
   :style: table
   :types: aou_req
   :tags: com
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature Architecture Status

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: ipc
   :columns: id;status
   :colwidths: 25,25
   :sort: title

.. needtable::
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: com
   :columns: id;status
   :colwidths: 25,25
   :sort: title
