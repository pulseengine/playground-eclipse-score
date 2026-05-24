---
id: DOC-INDEX-12544
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Feature Safety Work Products List

### Persistency Safety WPs

{{artifact:DOC__PERSISTENCY_SAFETY_WP:status,safety-level,security}}

# Tailoring

Additional to the tailoring in the SW platform project as defined in the project's [[WP__PLATFORM_SAFETY_PLAN]] we define here the additional tailoring on feature level.

- Excluded for this feature are additionally the following work products (and their related requirements):

  - no tailoring is used for the feature

# Safety Work products List

.. list-table:: Feature persistency Work products
    :header-rows: 1

    * - Workproduct Id
      - Link to process
      - Process status
      - Link to WP

    * - [[WP__FEAT_REQUEST]]
      - [[GD_TEMP__CHANGE_FEATURE_REQUEST]]
      - copy('status', need_id='gd_temp__change_feature_request')
      - [[DOC__PERSISTENCY]]

    * - [[WP__REQUIREMENTS_FEAT]]
      - [[GD_TEMP__REQ_FEAT_REQ]]
      - copy('status', need_id='gd_temp__req_feat_req')
      - [[DOC__FEATURE_PERSISTENCY_REQUIREMENTS]]

    * - [[WP__REQUIREMENTS_FEAT_AOU]]
      - [[GD_TEMP__REQ_AOU_REQ]]
      - copy('status', need_id='gd_temp__req_aou_req')
      - [[DOC__FEATURE_PERSISTENCY_REQUIREMENTS]]

    * - [[WP__FEATURE_ARCH]]
      - [[GD_TEMP__ARCH_FEATURE]]
      - copy('status', need_id='gd_temp__arch_feature')
      - [[DOC__PERSISTENCY_ARCHITECTURE]]

    * - [[WP__FEATURE_FMEA]]
      - [[GD_GUIDL__SAFETY_ANALYSIS]]
      - copy('status', need_id='gd_guidl__safety_analysis')
      - [[DOC__PERSISTENCY_FMEA]]

    * - [[WP__FEATURE_DFA]]
      - [[GD_GUIDL__SAFETY_ANALYSIS]]
      - copy('status', need_id='gd_guidl__safety_analysis')
      - [[DOC__PERSISTENCY_DFA]]

    * - [[WP__REQUIREMENTS_INSPECT]]
      - [[GD_CHKLST__REQ_INSPECTION]]
      - copy('status', need_id='gd_chklst__req_inspection')
      - [[DOC__FEATURE_PERSISTENCY_REQUIREMENTS_CHKLST]]

    * - [[WP__SW_ARCH_VERIFICATION]]
      - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
      - copy('status', need_id='gd_chklst__arch_inspection_checklist')
      - [[DOC__PERSISTENCY_ARC_INSPECTION]]

    * - [[WP__VERIFICATION_FEAT_INT_TEST]]
      - [[GD_GUIDL__VERIFICATION_GUIDE]]
      - copy('status', need_id='gd_guidl__verification_guide')
      - <WP Link>

# Feature Safety Package

To create the safety package (according to [[GD_GUIDL__SAF_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Feature Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See documents_docs_features_persistency

## Feature Requirements Status

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: feat_req
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature AoU Status

.. needtable::
   :filter: docname is not None and "persistency" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature Architecture Status

.. needtable::
   :filter: docname is not None and "persistency" in docname and "architecture" in docname
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: persistency
   :columns: id;status
   :colwidths: 25,25
   :sort: title
