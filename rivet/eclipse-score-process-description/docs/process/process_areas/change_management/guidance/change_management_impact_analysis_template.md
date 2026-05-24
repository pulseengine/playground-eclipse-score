---
id: DOC-CHANGE-MANAGEMENT-IMPACT-ANALYSIS-TEMPLATE-70614
title: Change Management Impact Analysis Template
type: specification
status: approved
tags: [eclipse-score]
---

.. _chm_impact_analysis_templates:

# Impact Analysis Template

### Impact Analysis Template

{{artifact:GD_TEMP__CHANGE_IMPACT_ANALYSIS:status,safety-level,security}}}}

## Type of Change Request

[New Feature/Component, Modification of an existing Feature/Component]

## Dependencies on other Change Requests

[List all dependencies on other Change Requests]

## Estimates for Realization

[List all work products and elements affected by the Change Request]

    .. note::
     For the identification of the affected work products use the Traceability Analysis approach.
     Traceability analysis uses the existing links between different elements (requirements, architecture, implementation, etc.)
     for the identification of the affected work products and elements.

[Describe here which work products to be modified by the Change Request]

[Describe here the verification methods used for the changed work products or elements]

[Estimate the effort, resources, risk for the realization]

[Describe here which stakeholder and which roles of the stakeholder are involved to execute the Change Request]

   .. note::
      Typically the Project Leads <rl__project_lead> are involved
      for planning and approval activities. As well as Safety Manager <rl__safety_manager> or Security Manager <rl__security_manager>
      are responsible for Change Request which has impact on functional safety or security.

[Describe here which Milestones are considered to realize the Change Request]

    .. note::
     A draft realization plan may support the realization proposal.

## Potential Impact on Security

Add the potential impact in the chapter Security Impact of the concerned Feature Request
(compare Feature Request Template <gd_temp__change_feature_request>) or Component Request
(compare Component Request Template <gd_temp__change_component_request>).

## Potential Impact on Safety

Add the potential impact in the chapter Safety Impact of the concerned Feature Request
(compare Feature Request Template <gd_temp__change_feature_request>) or Component Request
(compare Component Request Template <gd_temp__change_component_request>).
