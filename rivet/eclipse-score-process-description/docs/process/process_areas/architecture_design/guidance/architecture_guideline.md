---
id: DOC-ARCHITECTURE-GUIDELINE-36127
title: Architecture Guideline
type: specification
status: approved
tags: [eclipse-score]
---

.. _arch_design_guideline:

# Architecture Guideline

### Architectural Design Guideline

{{artifact:GD_GUIDL__ARCH_DESIGN:status,safety-level,security}}

The guideline focuses on the steps which need to be performed in order to create the architectural design. The concept behind those steps is described in the [[title]] <doc_concept__arch_process>.

# General Hints

## Attributes

For all architectural elements, the following mandatory attributes are defined:

## Checks

For architectural elements, the following checks are defined:

# Workflow for creating an architectural design

This chapter describes the general guideline for architectural design within the project. In general, the workflow for creating an architectural design is shown in architecture_workflow_fig.

Those steps are:

.. list-table:: Definition of the static architectural elements
   :header-rows: 1
   :widths: 10,60,30

   * - Step
     - Description
     - Responsible
   * - 1.
     - Create platform architecture (Concept) <create_platform_architecture>
     - [[title]] <rl__contributor>
   * - 2.
     - Model platform architecture <model_platform_architecture>
     - [[title]] <rl__contributor>
   * - 3.
     - Allocate stakeholder requirements to architectural elements <allocate_stakeholder_requirements>
     - [[title]] <rl__contributor>
   * - 4.
     - Review platform architecture <review_platform_architecture>
     - [[title]] <rl__committer>
   * - 5.
     - Merge platform architecture into score delivery container
     - [[title]] <rl__committer>
   * - 6.
     - Create feature architecture (Concept) <create_feature_architecture>
     - [[title]] <rl__contributor>
   * - 7.
     - Model feature architecture <model_feature_architecture>
     - [[title]] <rl__contributor>
   * - 8.
     - Allocate feature requirements to architectural elements <allocate_feature_requirements>
     - [[title]] <rl__contributor>
   * - 9.
     - Review feature architecture <review_architectural_design>
     - [[title]] <rl__committer>
   * - 10.
     - Merge feature architecture into score delivery container
     - [[title]] <rl__committer>
   * - 11.
     - | Create component architecture (Concept) <create_component_architecture>
       | Allocate component requirements to architectural elements <allocate_component_requirements>
     - [[title]] <rl__contributor>
   * - 12.
     - Model component architecture <model_component_architecture>
     - [[title]] <rl__contributor>
   * - 13.
     - Review component architecture <review_component_architecture>
     - [[title]] <rl__committer>
   * - 14.
     - Merge component architectural design into module's delivery container
     - [[title]]  <rl__committer>

.. _create_platform_architecture:

## Create platform architecture (Concept)

The platform architecture (= top-level architecture) shall be created in the platform delivery container. It provides the overall decomposition of the platform into features and defines the logical interfaces at the platform boundary.

The platform architecture shall describe the concept of the platform, including supporting figures and drawings. If multiple solutions are possible, these should be documented here with the rationale for the final decision. A design decision template is provided in Decision Record Template <gd_temp__change_decision_record>.

Additionally, you should consult your project's specific guidelines, e.g., for using the version management tooling or architecture element naming conventions, which should be defined (or linked) in the Project SW development Plan <wp__sw_development_plan>.

.. _model_platform_architecture:

## Model platform architecture

Based on the concept description, a model of the platform architecture shall be designed. It shall provide an overview of the features within the platform and their logical interfaces at the platform boundary. Therefore, the following elements shall be used:

.. list-table:: Architectural Elements of the Platform Architecture
   :header-rows: 1
   :widths: 10,30

   * - Element
     - Sphinx directive
   * - Feature
     - feat
   * - Logical Interface
     - logic_arc_int
   * - Logical Interface Operation
     - logic_arc_int_op

The relations of the static elements are described in metamodel_architectural_design.

.. _allocate_stakeholder_requirements:

## Allocate stakeholder requirements to architectural elements

In this step, the stakeholder requirements shall be allocated to the platform architectural elements depending on their content. These links shall be established from architectural elements to stakeholder requirements via the attribute *fulfils*.

If needed, additional feature requirements derived from architectural decisions should be created and allocated to the respective feature.

.. _review_platform_architecture:

## Review platform architecture

As soon as the design is in a mature state, it can be reviewed according to [[DOC_CONCEPT__WP_INSPECTIONS]]
and merged into the main branch of the platform delivery container. See also the document life-cycle guideline [[GD_GUIDL__DOCUMENTATION]] for more information about the documentation for the platform architecture [[WP__PLATFORM_ARCH]].

For the review process, a checklist template is available: Architecture Inspection Checklist Template <gd_chklst__arch_inspection_checklist>.

The following roles should be included in the review:

* [[title]] <rl__safety_manager>
* [[title]] <rl__security_manager>
* [[title]] <rl__project_lead>
* [[title]] <rl__committer>

.. _create_feature_architecture:

## Create feature architecture (Concept)

The feature architecture (= high-level architecture) shall be created in the feature tree of the platform delivery container.

For this step, the following guidance is available: Feature Architecture Template <gd_temp__arch_feature>. Based on this template, the feature architecture shall describe the concept of the feature, including supporting figures and drawings. If multiple solutions are possible, these should be documented here with the rationale for the final decision. A design decision template is provided in Decision Record Template <gd_temp__change_decision_record>.

Additionally, you should consult your project's specific guidelines, e.g., for using the version management tooling or architecture element naming conventions, which should be defined (or linked) in the Project SW development Plan <wp__sw_development_plan>.

.. _model_feature_architecture:

## Model feature architecture

Based on the concept description, a model of the feature architecture shall be designed. It shall consist of the logical interfaces which the user of the feature can access, including the modules which provide the interfaces. Therefore, the following elements shall be used:

.. list-table:: Architectural Elements of the Feature Architecture
   :header-rows: 1
   :widths: 10,30

   * - Element
     - Sphinx directive
   * - Feature Architecture
     - feat, feat_arc_sta, feat_arc_dyn
   * - Logical Interface
     - logic_arc_int
   * - Logical Interface Operation
     - logic_arc_int_op

The relations of the static elements are described in metamodel_architectural_design.

.. note::
  For the modelling of the architecture a sphinx extension is available: arch_gen_sphinx

  An example of modelling the architecture can be found in the
  `module template documentation <https://eclipse-score.github.io/module_template/main/>`_.

.. _allocate_feature_requirements:

## Allocate feature requirements to architectural elements

In the next step, the already derived feature requirements shall be allocated to the architectural elements depending on the content of the requirement. Functional requirements may either be allocated to static or dynamic architecture. Interface requirements shall only be allocated to the interface architecture.

If needed, additional feature requirements, which may arise due to architectural decisions, should be created and allocated to the feature architecture itself.

These links may be established from architectural views to feature requirements via the attribute *fulfills*
but all the feature requirements must be allocated to the feature element via the attribute *satisfied_by*.

.. _review_architectural_design:

## Review architectural design

As soon as the design is in a mature state, it can be reviewed according to [[DOC_CONCEPT__WP_INSPECTIONS]]
and merged into the main branch of the platform delivery container. See also the document life-cycle guideline [[GD_GUIDL__DOCUMENTATION]] for more information about the documentation for the feature architecture [[WP__FEATURE_ARCH]].

For the review process, a checklist template is available: Architecture Inspection Checklist Template <gd_chklst__arch_inspection_checklist>.

The following roles should be included in the review:

* [[title]] <rl__safety_manager>
* [[title]] <rl__security_manager>
* [[title]] <rl__project_lead>
* [[title]] <rl__committer>

.. _create_component_architecture:

## Create component architecture (Concept)

Based on the *feature architecture*, the concept for the *component architecture* shall be created in the module's delivery container. It shall describe which components need to be created and how they correlate with each other in order to provide the required functionality. As a starting point, a template <gd_temp__arch_comp> is provided.

For this step, the following guidance is available: Feature Architecture Template <gd_temp__arch_feature>. Additionally, you should consult your project's specific guidelines, e.g., for using the version management tooling or architecture element naming conventions, which should be defined (or linked) in the Project SW development Plan <wp__sw_development_plan>.

.. _allocate_component_requirements:

## Allocate component requirements to architectural elements

In this step, the component requirements shall be derived (see [[title]] <gd_guidl__req_engineering>) and allocated to the respective component element via the attribute *satisfied_by*.

.. _model_component_architecture:

## Model component architecture

According to the architecture design description, the model for the component architecture shall be created. It shall consist of components, real interfaces and real interface operations. Depending on the size of the component, it can also be split into multiple (lower-level) components.

.. list-table:: Architectural Elements of the Component Architecture
   :header-rows: 1
   :widths: 10,30

   * - Element
     - Sphinx directive
   * - Component Architecture
     - comp, comp_arc_sta, comp_arc_dyn
   * - (Real) Interface
     - real_arc_int
   * - (Real) Interface Operation
     - real_arc_int_op

The relations of the static elements are described in metamodel_architectural_design.

.. _review_component_architecture:

## Review component architecture

As soon as the design is in a mature state, it can be reviewed <review_concept> and merged into the main branch of the module's delivery container. See also the document life-cycle guideline [[GD_GUIDL__DOCUMENTATION]] for more information about the documentation for the component architecture [[WP__COMPONENT_ARCH]].

Following roles should be included in the review:

* [[title]] <rl__safety_manager>
* [[title]] <rl__security_manager>
* [[title]] <rl__committer>

For the review process, a checklist template is available: Architecture Inspection Checklist Template <gd_chklst__arch_inspection_checklist>.

.. _uml_diagram_selection:

# UML diagram selection

## Static architecture

As can be seen from the rendered feature and the component example in the
`module template documentation <https://eclipse-score.github.io/module_template/main/>`__,
for the static architecture a UML component diagram is expected (and supported  by the tooling).

## Dynamic architecture

The [[DOC_CONCEPT__ARCH_PROCESS]] shows the usage of UML sequence diagrams to describe dynamic
behavior. This is also the expected default diagram. Alternatively, state machine diagrams can be used
to describe stateful behavior. Other types like the activity diagram are not encouraged to use,
if an activity diagram is used instead of a sequence diagram, this has to be argued as part of the
architecture description.

Generally dynamic views are expected in the feature view and the component view based on the following considerations:

- Do not use dynamic views, if the fulfillment of the requirements by the architecture is already understandable with the static view.
- Simple caller/callee relation is not expected to be modelled (this would mean that the examples would be too simple for modelling).
- There should be more than two components involved.
- In case of safety-related calls/communication, the error cases shall also be displayed (see the "alt" boxes in the examples).
- If there is only a small difference between the feature and the component view, one can be omitted, preferably the feature view.
- If the described feature or components support multiple use cases (e.g., in different life-cycle phases), these should also be described in multiple dynamic views.
