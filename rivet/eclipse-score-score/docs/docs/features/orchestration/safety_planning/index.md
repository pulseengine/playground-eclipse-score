---
id: DOC-INDEX-17399
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Feature Safety Planning

### Orchestration Safety WPs

{{artifact:DOC__ORCHESTRATION_SAFETY_WP:status,safety-level,security}}}}

.. list-table:: Feature Orchestration Work products
    :header-rows: 1

    * - Work product Id
      - Link to process
      - Process status
      - Link to issue
      - Link to WP
      - WP/doc status

    * - [[WP__FEAT_REQUEST]]
      - [[GD_TEMP__CHANGE_FEATURE_REQUEST]]
      - copy('status', need_id='gd_temp__change_feature_request')
      - https://github.com/eclipse-score/score/pull/1293
      - [[DOC__ORCHESTRATION]]
      - copy('status', need_id='doc__orchestration')

    * - [[WP__REQUIREMENTS_FEAT]]
      - [[GD_TEMP__REQ_FEAT_REQ]]
      - copy('status', need_id='gd_temp__req_feat_req')
      - https://github.com/eclipse-score/score/pull/1293
      - [[DOC__ORCHESTRATION_REQUIREMENTS]]
      - doc copy('status', need_id='doc__orchestration') & WP below

    * - [[WP__REQUIREMENTS_FEAT_AOU]]
      - [[GD_TEMP__REQ_AOU_REQ]]
      - copy('status', need_id='gd_temp__req_aou_req')
      - https://github.com/eclipse-score/score/pull/1293
      - [[DOC__ORCHESTRATION_REQUIREMENTS]]
      - doc copy('status', need_id='doc__orchestration') & WP below

    * - [[WP__FEATURE_ARCH]]
      - [[GD_TEMP__ARCH_FEATURE]]
      - copy('status', need_id='gd_temp__arch_feature')
      - <link to issue>
      - [[DOC__ORCHESTRATION_ARCHITECTURE]]
      - doc copy('status', need_id='doc__orchestration_architecture') & WP below

    * - [[WP__FEATURE_FMEA]]
      - [[GD_TEMP__FEAT_SAF_FMEA]]
      - copy('status', need_id='gd_temp__feat_saf_fmea')
      - <link to issue>
      - [[DOC__ORCHESTRATION_FMEA]]
      - doc copy('status', need_id='doc__orchestration_fmea') & WP below

    * - [[WP__FEATURE_DFA]]
      - [[GD_TEMP__FEAT_SAF_DFA]]
      - copy('status', need_id='gd_temp__feat_saf_dfa')
      - <Link to issue>
      - [[DOC__ORCHESTRATION_DFA]]
      - doc copy('status', need_id='doc__orchestration_dfa') & WP below

    * - [[WP__REQUIREMENTS_INSPECT]]
      - [[GD_CHKLST__REQ_INSPECTION]]
      - copy('status', need_id='gd_chklst__req_inspection')
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - [[WP__SW_ARCH_VERIFICATION]]
      - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
      - copy('status', need_id='gd_chklst__arch_inspection_checklist')
      - n/a
      - Checklist used in Pull Request Review
      - n/a

    * - [[WP__VERIFICATION_FEAT_INT_TEST]]
      - [[GD_GUIDL__VERIFICATION_GUIDE]]
      - copy('status', need_id='gd_guidl__verification_guide')
      - <link to issue>
      - <Link to WP>
      - <automated>

## Feature Requirements Status

.. needtable::
   :filter: docname is not None and "orchestration" in docname and "requirements" in docname
   :style: table
   :types: feat_req
   :tags: orchestration
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature AoU Status

.. needtable::
   :filter: docname is not None and "orchestration" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: orchestration
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature Architecture Status

.. needtable::
   :filter: docname is not None and "orchestration" in docname and "requirements" in docname
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: orchestration
   :columns: id;status
   :colwidths: 25,25
   :sort: title
