---
id: DOC-QUALITY-WORK-PRODUCT-REVIEW-GUIDELINE-57355
title: Quality Work Product Review Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Quality Work Product Review Guideline

### Quality work product review

{{artifact:GD_GUIDL__WP_REVIEW:status,safety-level,security}}

## Purpose

| Definition of a generic workflow to ensure the quality of work products.

## Objectives

| Check and assure the quality of the project/platform work products.

## Process

| Step  1: Create issue with label ``q_wp_review`` in status OPEN
| Step  2: Identify which work products will be checked during the review and document it in the created issue
| Step  3: Adjust [[GD_CHKLST__REVIEW_CHECKLIST]] based on specified work products to review, which contains acceptance criteria for all work products
| Step  4: Create PR, Link the stored checklist in the PR to the issue
| Step  5: Perform review according to checklist
| Step  6: Report deviations from the acceptance criteria in the issue tracking system with label ``bug`` and link it to the review issue and the checklist
| Step  7: Review result:
|         negative, in case of any deviation, continue with STEP 8
|         positive, in case of no deviations, continue with STEP 10
| Step  8: Trigger authors of WPs with deviations to resolve them in the same PR and close the corresponding bug issue
| Step  9: If all bug issues are resolved, continue with 5, otherwise continue with 8
| Step 10: Merge the PR and communicate the result, initial issue is now in status CLOSED
