---
id: DOC-INDEX-17903
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Feature Safety Work Products List

### FEO Safety Work Products

{{artifact:DOC__FEO_SAFETY_WP:status,safety-level,security}}

.. list-table:: FEO Feature Work Products
    :header-rows: 1

    * - Work product Id
      - Link to process
      - Process status
      - Link to WP

    * - [[WP__FEAT_REQUEST]]
      - [[GD_TEMP__CHANGE_FEATURE_REQUEST]]
      - copy('status', need_id='gd_temp__change_feature_request')
      - [[DOC__FRAMEWORKS_FEO]]

    * - [[WP__REQUIREMENTS_FEAT]]
      - [[GD_TEMP__REQ_FEAT_REQ]]
      - copy('status', need_id='gd_temp__req_feat_req')
      - [[DOC__FRAMEWORKS_FEO_FEAT_REQS]]

    * - [[WP__REQUIREMENTS_FEAT_AOU]]
      - [[GD_TEMP__REQ_AOU_REQ]]
      - copy('status', need_id='gd_temp__req_aou_req')
      - [[DOC__FRAMEWORKS_FEO_AOU_REQS]]

    * - [[WP__FEATURE_ARCH]]
      - [[GD_TEMP__ARCH_FEATURE]]
      - copy('status', need_id='gd_temp__arch_feature')
      - [[DOC__FRAMEWORKS_FEO_FEAT_ARCH]]

    * - [[WP__FEATURE_FMEA]]
      - [[GD_TEMP__FEAT_SAF_FMEA]]
      - copy('status', need_id='gd_temp__feat_saf_fmea')
      - [[DOC__FRAMEWORKS_FEO_FMEA]]

    * - [[WP__FEATURE_DFA]]
      - [[GD_TEMP__FEAT_SAF_DFA]]
      - copy('status', need_id='gd_temp__feat_saf_dfa')
      - [[DOC__FRAMEWORKS_FEO_DFA]]

    * - [[WP__FDR_REPORTS]] (Features's Safety Analyses & DFA)
      - [[GD_CHKLST__SAFETY_ANALYSIS]]
      - copy('status', need_id='gd_chklst__safety_analysis')
      - [[DOC__SAF_ANA_INSPEC_FRAMEWORKS_FEO]]

    * - [[WP__REQUIREMENTS_INSPECT]]
      - [[GD_CHKLST__REQ_INSPECTION]]
      - copy('status', need_id='gd_chklst__req_inspection')
      - [[DOC__REQ_INSPECTION_FRAMEWORKS_FEO]]

    * - [[WP__SW_ARCH_VERIFICATION]]
      - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
      - copy('status', need_id='gd_chklst__arch_inspection_checklist')
      - [[DOC__ARCH_INSPECTION_FRAMEWORKS_FEO]]

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

See documents_docs_features_frameworks

## FEO Requirements Status

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: feat_req
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## FEO AoU Status

.. needtable::
   :filter: docname is not None and "feo" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## FEO Architecture Status

.. needtable::
   :filter: docname is not None and "feo" in docname and "architecture" in docname
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: frameworks_feo
   :columns: id;status
   :colwidths: 25,25
   :sort: title
