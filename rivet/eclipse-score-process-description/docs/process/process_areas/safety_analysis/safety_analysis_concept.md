---
id: DOC-SAFETY-ANALYSIS-CONCEPT-41587
title: Safety Analysis Concept
type: specification
status: approved
tags: [eclipse-score]
---

# Concept Description

### Safety Analysis Concept

{{artifact:DOC_CONCEPT__SAFETY_ANALYSIS:status,safety-level,security}}}}

This section discusses a concept for Safety Analysis. As methods for Safety Analysis are used DFA (Dependent Failure Analysis)
and FMEA (Failure Mode and Effects Analysis). Inputs for this concept are the requirements of ISO26262 Part 6 Chapter 7 and Part 9 Chapter 7 and 8.

The objective of the **DFA** is to show the absence of dependent failures. Dependent failures are split into common cause failures and cascading failures.
How to perform a Safety Analysis is described in [[GD_GUIDL__SAFETY_ANALYSIS]].
To have a structured DFA the failure initiators have to be applied [[GD_GUIDL__DFA_FAILURE_INITIATORS]]. These are separated into the following categories:

 | - Shared resources: Shared resources are resources that are used by two or more elements. If one element fails, it could lead to a failure in another element.
 | - Communication between the two elements: Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.
 | - DFA shared information inputs: Same information input used by multiple functions.
 | - Unintended impact: Unintended impacts to function due to various failures like deadlocks or memory depletion.
 | - Development failure initiators: Failures that occur during the development process, potentially leading to safety issues.

The objective of the **FMEA** is to show that the architecture created to fulfil the requirements does not introduce possible errors which would
break the safety requirements. Or rather that the possibility of these errors is reduced to an acceptable level. This can be achieved through detection, prevention or mitigation measures.
The FMEA is used to find possible failures and their effects. The possible failures are systematically identified by applying fault models [[GD_GUIDL__FAULT_MODELS]].

The DFA shall be performed once at platform level to analyse the dependencies between the features of the platform.
Typically, the FMEA and DFA are performed at feature level and component level.
If a component has no sub-components, the results of the analysis are the same as at feature level. So no additional consideration is needed.
In this case please document this in the content of the document.

# Inputs

#. Stakeholders for the Safety Analysis (DFA and FMEA)?
#. Who needs which information?
#. How to analyse existing safety mitigation?
#. How to add new safety mitigations?
#. What analysis shall be done in which level?
#. How to perform the analysis?

# Stakeholders for the Safety Analysis (DFA and FMEA)

#. Safety Engineer <rl__safety_engineer>

   * Analyse all the feature architectures together with a Platform DFA
   * Analyse the feature architecture with a Feature FMEA and Feature DFA
   * Analyse the component architecture with a Component FMEA and Component DFA
   * Monitor/verify the FMEA and DFA

#. Safety Manager <rl__safety_manager>

   * Approve the FMEA and DFA
   * Approve the verification of the FMEA and DFA

#. Contributor <rl__contributor>

   * Support the FMEA and DFA
   * Support the monitoring and verifying of the FMEA and DFA

#. Committer <rl__committer>

   * Support the FMEA and DFA
   * Support the monitoring and verifying of the FMEA and DFA

#. Security Manager <rl__security_manager>

   * Support the FMEA and DFA
   * Support the monitoring and verifying of FMEA and DFA

# Standard Requirements

Also requirements of standards need to be taken into consideration:

* ISO26262
* ISO SAE 21434

# How to analyse?

The Safety Analysis are done on the platform (DFA only), feature and component architecture. The Safety Analysis (DFA and FMEA) shall be done accompanying to the development.
So the results can directly be used for the development of the feature and component. With a iterative approach it is needed to proof
the evidence of the functional safety of the functions.

The analysis were applied at static and dynamic architecture diagrams. The following pictures showing the perspective of the User.

.. _safety_analysis_feature_example:

With the diagrams the dependencies and signal flows are shown. The analysis is performed by applying FMEA fault models
[[GD_GUIDL__FAULT_MODELS]] and DFA failure initiators [[GD_GUIDL__DFA_FAILURE_INITIATORS]] for DFA.
Some fault models and failure initiators may not be applicable for one safety function. In this case the reason shall
be documented in the FMEA/DFA documents. So it can be shown that the analysis is completely done.

FMEA: In the above example's dynamic view the "flow component 1" to the user realizes a safety requirement.
If we apply the fault model we may find the possible failure: "the message is not sent which leads to the user not being able to ..." - this
could be mitigated by telling the user in an AoU: "the feature can not guarantee that the message is sent"

DFA: Here we see in the static view that component 1 uses component 2. If we apply the failure initiators we may find the possible failure:
"Component 2 is using up all execution time available to Component 1" which could be avoided by an OS which reserves time for every component
or by running these components on different processors.

A step-by-step-approach is described in [[GD_GUIDL__SAFETY_ANALYSIS]]. There are also examples for FMEA and DFA are given
in examples_fmea_dfa to show how to use the templates, failure initiators and fault models.

At component level you can see inside of the component when the component consists of two or more sub-components. If a component has no sub-components,
the analysis results are the same as at feature level. So no additional consideration is needed. This should be also documented in the content of the document.
In the example the component "Component 1" consists of two sub-components, "Component 3" and "Component 4".

A step-by-step-approach is described in [[GD_GUIDL__SAFETY_ANALYSIS]]. There are also examples for FMEA and DFA are given in examples_fmea_dfa to show how to use the templates, failure initiators and fault models.

# How to add new safety mitigations?

Identified faults without a mitigation remain open and are tracked in the issue tracking system [[WP__ISSUE_TRACK_SYSTEM]] until they are resolved.
A new safety mitigation could be needed e.g. if it can't be shown that the feature or component is completely deterministic and testable. In this case an
additional safety mitigation is needed.

# What analysis shall be done in which level?

The Safety Analysis (DFA and FMEA) shall consider the architectural elements on different levels.

1. **Platform Level**: At this level, the focus is on the overall feature architecture to analyse if there are failures that effects more than one feature.

    | **Example DFA:** Dependencies between features shall be analysed. This could be the usage of feature interfaces by multiple features, shared libraries or shared services. A common cause failure could be a erroneous signal that effects the behaviour of several functions.

2. **Feature Level**: This level involves a more detailed analysis of individual components within the feature. The analysis shall consider the internal structure of components and their interactions with other components in the feature.

    | **Example DFA:** A dependent failure could be if two or more components share a common resource or if they are dependent on the same signal. If one component fails, it could lead to a failure in another component.
    | **Example FMEA:** The FMEA shall be used to analyse if the safety requirements of a feature can be violated. This might be an unintended sending of a message between two components.

3. **Component Level**: If a component consists of multiple sub-components, the analysis shall be extended to these sub-components. This level of detail is necessary to identify specific fault models that may not be apparent at higher levels.

    | **Example DFA:** Similar to the feature level, but with a focus on the interactions between sub-components within a single component.
    | **Example FMEA:** The FMEA shall used to analyse if the safety requirements of a component can be violated. This might be a unintended sent of a message between two sub-components.
