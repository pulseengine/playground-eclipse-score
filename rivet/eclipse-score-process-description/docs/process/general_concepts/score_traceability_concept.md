---
id: DOC-SCORE-TRACEABILITY-CONCEPT-28224
title: Score Traceability Concept
type: specification
status: approved
tags: [eclipse-score]
---

.. _general_concepts_traceability:

## Traceability concept

### Traceability Concept

{{artifact:DOC_CONCEPT__GENERAL_TRACEABILITY:status,safety-level,security}}

.. attention::
   The traceability concept is not intended to be complete.
   The traceability concept is intended to give an overview about the traceability
   requirements in the platform.

Traceability is the key to ensure consistency between work products.
Furthermore, traceability supports impact analysis, dependency analysis, coverage determination
for requirements and verification, and tracking of implementation status.

Therefore the project requires at least for safety-relevant work products single-requirement
granularity of traceability.

The following figures gives an overview about the traceability between different work products
on different levels and detail.

#### High level traceability overview

The following figure shows the traceability between the major project work products on each
requirements level. Starting from top, the platform level, going down to feature, component
to the bottom the unit level. The concept is based on the classical V-model approach.
Note also that this describes the traceability of functional (and interface) type requirements.

Change request are traced to all affected work products.

The next figure sets the focus on the feature level and adds the traceability from the Feature
Requirements to the Feature Architecture, Feature Safety/Security Analysis and the Feature Assumption
of use. For convenience also the traceability to upper and lower lever requirements is shown.

The next figures sets the focus on the component level and adds the traceability from the
Component Requirements to the Component Architecture, Component Safety/Security Analysis
and the Component Assumption of use. Further the traceability to Assumptions of use
from external components is included.

Component Architecture may either built-up of other components, then the traceability may in
addition also needed to their architectures.

Or less complex components may not require a Component Architecture (and the derived work products
Component Safety/Security Analysis and AoUs). Then the traceability is not required for these.

