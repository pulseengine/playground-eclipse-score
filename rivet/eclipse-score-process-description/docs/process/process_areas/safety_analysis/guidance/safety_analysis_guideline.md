---
id: DOC-SAFETY-ANALYSIS-GUIDELINE-69377
title: Safety Analysis Guideline
type: specification
status: approved
tags: [eclipse-score]
---

# Safety Analysis Guidelines

### Safety Analysis (DFA and FMEA) Guideline

{{artifact:GD_GUIDL__SAFETY_ANALYSIS:status,safety-level,security}}}}

This document describes the general guidances for Safety Analysis (DFA and FMEA) based on the concept which is defined Safety Analysis Concept<doc_concept__safety_analysis>.
Use the Platform DFA as an input so that general Safety Mechanisms are only defined once and not in every single Safety Analysis.

# Workflow for Safety Analysis

The workflows of the Safety Analysis are described in workflow_safety_analysis. The single steps in these workflows are described in detail in the following sections.

#### Step-by-Step-approach FMEA:

The analysis is done by using the template FMEA_templates on the feature or component architectural diagrams. By using the fault models <[[GD_GUIDL__FAULT_MODELS]]>
it can be ensured that the analysis is done in a structured way.
Apply the fault model to the diagram and document the results in the template. Use the content of the document `Feature FMEA Template <https://eclipse-score.github.io/module_template/main/docs/features/feature_example/safety_analysis/fmea.html>`__, `Component FMEA Template <https://eclipse-score.github.io/module_template/main/score/component_example/docs/safety_analysis/fmea.html>`__
to describe e.g. why a fault model is not applicable for the diagram. If a FMEA can't be applied, the reason has to be documented in the
content of the document, so it can be recognized.

The attributes of the template are described in process_requirements_safety_analysis_attributes.

**Steps:**

#. For each of the safety functions realized by an architecture element check if a fault from the fault model [[GD_GUIDL__FAULT_MODELS]] applies.
#. If a fault model applies, use the template [[GD_TEMP__FEAT_SAF_FMEA]] or [[GD_TEMP__COMP_SAF_FMEA]] to perform the analysis.
#. The title of the analysis should be easily recognizable e.g. "Component xy unintended triggered".
#. Link the violated architecture with the "violates" attribute.
#. Replace the placeholders in the "id" attribute with the name of the feature or component and a short description of the element so that it can be easily identified.
#. Document the fault ID from the fault model [[GD_GUIDL__FAULT_MODELS]] that applies to the element in the "fault_id" attribute.
#. Describe the failure effect of the fault model on the element in the "failure_effect" attribute. Use the failure mode description and enlarge the if it's applicable to the considered element.
#. You may document the root cause of the failure in the "failure_root_cause" attribute.
#. You may indicate whether the analysed failure is safety relevant using the "safety_relevant" attribute (<yes> or <no>).
#. Document the safety mitigation. This can be a detection, prevention or mitigation of the fault. If only testability is defined as mitigation measure, complexity requirements shall be allocated to the feature/component.
#. If there is no mitigation or existing mitigation is not sufficient a mitigation issue has to be created in the Issue Tracking system and linked in the "mitigation_issue" attribute.
#. The analysis is finished, if for each identified fault a sufficient mitigation exists.
#. Unless the attribute sufficient is yes, mitigation and argument attribute can be still empty.
#. Continue the analysis until all applicable fault models are checked.
#. The verification is done by applying the checklist [[GD_CHKLST__SAFETY_ANALYSIS]].

#### Step-by-Step-approach DFA:

The analysis is done by using the template dfa_templates on the feature or component architectural diagrams using a list of DFA failure initiators <[[GD_GUIDL__DFA_FAILURE_INITIATORS]]>.
Use the content of the document `Feature DFA Template <https://eclipse-score.github.io/module_template/main/docs/features/feature_example/safety_analysis/dfa.html>`__, `Component DFA Template <https://eclipse-score.github.io/module_template/main/score/component_example/docs/safety_analysis/dfa.html>`__ to describe e.g. why
a failure initiator is not applicable for the diagram. If a DFA can't be applied, the reason has to be documented in the content of the document, so it
can be recognized.

The attributes of the template are described in process_requirements_safety_analysis_attributes.

**Steps:**

#. For each architectural element check if a failure from the failure initiators [[GD_GUIDL__DFA_FAILURE_INITIATORS]] applies.
#. If a failure initiator applies, use the template [[GD_TEMP__FEAT_SAF_DFA]] or [[GD_TEMP__COMP_SAF_DFA]] to perform the analysis.
#. The title of the analysis should be easily recognizable e.g. "Component xy unintended triggered".
#. Link the violated architecture with the "violates" attribute.
#. Replace the placeholders in the "id" attribute with the name of the feature or component and a short description of the element so that it can be easily identified.
#. Document the failure ID from the failure initiator [[GD_GUIDL__DFA_FAILURE_INITIATORS]] that applies to the element in the "failure_id" attribute.
#. Describe the failure effect of the failure initiator on the element in the "failure_effect" attribute. Use the violation cause description and enlarge the if it's applicable to the considered element.
#. Indicate whether the analysed failure is safety relevant using the "safety_relevant" attribute (<yes> or <no>).
#. Document the safety mitigation. This can be a detection, prevention or mitigation of the fault. If only testability is defined as mitigation measure, complexity requirements shall be allocated to the feature/component.
#. If there is no mitigation or the mitigation is not sufficient a mitigation issue has to be created in the Issue Tracking system and linked in the "mitigation_issue" attribute.
#. The analysis is finished, if for each identified fault a sufficient mitigation exists.
#. Unless the attribute sufficient is yes, mitigation and argument attribute can be still empty.
#. Continue the analysis until all applicable failure initiators are checked.
#. The verification is done by applying the checklist [[GD_CHKLST__SAFETY_ANALYSIS]].

.. _examples_fmea_dfa:

# Examples for FMEA and DFA at feature level

For the examples the architectural diagrams safety_analysis_feature_example are used.

**FMEA:**

In the dynamic view of the example the "flow component 1" to the user realizes a safety requirement. If we apply the fault model we may
find possible failures. Therefore we need a mitigation.

.. code-block:: rst

### Component 1 Call message not received

{{artifact:FEAT_SAF_FMEA__MAB__COMP1_CALL_NRECEIVED:status,safety-level,security}}}}

For all fault models that are not applicable, the reason has to be documented in the content of the document, so it can be recognized. An example could be that

* Fault model FM_01_07 "Message is unintended sent. Component 1 will be unintended triggered." is not applicable, because the component is ASIL B developed, non complex and sufficiently tested.
* Fault model FX_01_04 "loss of execution" is not applicable, because feature is completely deterministic. Other failures like HW failures are not considered in this analysis because it's developed as a SEooC.

**DFA:**

In the static view of the example could be seen that component 1 uses component 2. If we apply the failure initiators we may find the possible failures.

.. code-block:: rst

### Mab data corruption

{{artifact:FEAT_SAF_DFA__MAB__DATA_CORRUPTION:status,safety-level,security}}}}

* Failure initiator SR_01_01 "reused software components" is not applicable, no software components are reused in the feature.
* Failure initiator SI_01_03 "constants, or variables, being global to the two software functions" is not applicable, because it's not possible to create constants or variables that being global to the two software functions in Rust.

# Examples for FMEA and DFA at component level

For the examples the architectural diagrams safety_analysis_feature_example are used.

**FMEA:**

There is no need to do a FMEA on component 3 as it offers the same as component 1 (which we already analysed in the feature analysis). So we can skip this component.
But please note it in the content of the document.

It has to be considered if a FMEA has to be done on component 4 or if it's covered by the DFA.

**DFA:**

In the dynamic view we see that Component 4 is returning a message to component 3. If we apply the failure initiators we may find the possible
failure: "message corruption" of "flow component 3" - but we find out that this is a flow which is not contributing to the safety function.
Additionally in the static view we see Component 4 is a library used by Component 3. Therefore we have to apply the failure initiators again.

.. code-block:: rst

### Allocated memory

{{artifact:COMP_SAF_DFA__COMPONENT4__ALLOCATED_MEMORY:status,safety-level,security}}}}

For all failure initiators that are not applicable, the reason has to be documented in the content of the document, so it can be recognized. An example could be that

* Failure initiator CO_01_02 "Data or message corruption" of "flow component 3" is not applicable, this flow is not contributing to the safety function.

# Tailoring

### Analysis Tailored

{{artifact:GD_GUIDL__ANALYSIS_TAILORED:status,safety-level,security}}}}

