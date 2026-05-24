---
id: DOC-INDEX-5232
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _feature_security_analysis_template:

# Feature Security Work Products List

### [Your Feature Name] Security WPs

{{artifact:DOC__FEATURE_EXAMPLE_SECURITY_ANALYSIS_WP:status,safety-level,security}}

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``Your Feature Name`` to be your Feature Name
    - Modify ``id`` to be your Module Name in upper snake case preceded by ``doc__`` and succeeded by ``_security_wp``
    - Adjust ``status`` to be ``valid``
    - Adjust ``safety`` and ``tags`` according to your needs

# Tailoring

Additional to the tailoring in the SW platform project as defined in the project's [[WP__PLATFORM_SECURITY_PLAN]] we define here the additional tailoring on feature level.

- Excluded for this feature are additionally the following work products (and their related requirements):

  - <work product/requirement> - <Argumentation why it is not needed or replaced by another work product or activity.>

# Security Work products List

.. list-table:: Feature <feature_name> Work products
    :header-rows: 1

    * - Work product Id
      - Link to process
      - Process status
      - Link to WP

    * - [[WP__FEAT_REQUEST]]
      - [[GD_TEMP__CHANGE_FEATURE_REQUEST]]
      - copy('status', need_id='gd_temp__change_feature_request')
      - [[DOC__FEATURE_NAME]]

    * - [[WP__REQUIREMENTS_FEAT]]
      - [[GD_TEMP__REQ_FEAT_REQ]]
      - copy('status', need_id='gd_temp__req_feat_req')
      - [[DOC__FEATURE_NAME_REQUIREMENTS]]

    * - [[WP__REQUIREMENTS_FEAT_AOU]]
      - [[GD_TEMP__REQ_AOU_REQ]]
      - copy('status', need_id='gd_temp__req_aou_req')
      - [[DOC__FEATURE_NAME_REQUIREMENTS]]

    * - [[WP__FEATURE_ARCH]]
      - [[GD_TEMP__ARCH_FEATURE]]
      - copy('status', need_id='gd_temp__arch_feature')
      - [[DOC__FEATURE_NAME_ARCHITECTURE]]

    * - [[WP__REQUIREMENTS_INSPECT]]
      - [[GD_CHKLST__REQ_INSPECTION]]
      - copy('status', need_id='gd_chklst__req_inspection')
      - [[DOC__FEATURE_NAME_REQ_INSPECTION]]

    * - [[WP__SW_ARCH_VERIFICATION]]
      - [[GD_CHKLST__ARCH_INSPECTION_CHECKLIST]]
      - copy('status', need_id='gd_chklst__arch_inspection_checklist')
      - [[DOC__FEATURE_NAME_ARC_INSPECTION]]

    * - [[WP__VERIFICATION_FEAT_INT_TEST]]
      - [[GD_GUIDL__VERIFICATION_GUIDE]]
      - copy('status', need_id='gd_guidl__verification_guide')
      - <Link to WP>

.. attention::
    The above table must be updated according to your feature security planning.

    - Fill the work producs links

# Feature Security Package

To create the security package (according to [[GD_GUIDL__SECURITY_PACKAGE]]) the following
documents and work products status have to go to "valid" (after the relevant verification were performed).

## Feature Documents Status

For all the work product documents the status can be seen by following the "Link to WP".
A summary of the status is also documented in the project's documentation management plan.

See <add here the section reference to the documentation management plan>

## Feature Requirements Status

.. needtable::
   :filter: docname is not None and "feature_name" in docname and "requirements" in docname
   :style: table
   :types: feat_req
   :tags: feature_name
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature AoU Status

.. needtable::
   :filter: docname is not None and "feature_name" in docname and "requirements" in docname
   :style: table
   :types: aou_req
   :tags: feature_name
   :columns: id;status
   :colwidths: 25,25
   :sort: title

## Feature Architecture Status

.. needtable::
   :filter: docname is not None and "feature_name" in docname and "architecture" in docname
   :style: table
   :types: feat_arc_sta; feat_arc_dyn
   :tags: feature_name
   :columns: id;status
   :colwidths: 25,25
   :sort: title
