---
id: DOC-VERIFICATION-CONCEPT-23404
title: Verification Concept
type: specification
status: approved
tags: [eclipse-score]
---

# Concept Description

### Verification Concept

{{artifact:DOC_CONCEPT__VERIFICATION_PROCESS:status,safety-level,security}}

# Inputs

#. Stakeholders for the verification work products?
#. What kind of tests are developed?
#. How is traceability established?
#. What tooling do we use?

# Stakeholder

#. Project Lead <rl__project_lead>

   * Set the scope of platform and testing
   * Status reporting of verification activities
   * Defining release content
   * Judge the releasable software state in case of failing test cases.
   * Set the scope of platform and testing
   * Status reporting of verification activities
   * Defining release content

     This may need involvement of
     [[RL__SAFETY_MANAGER]] and [[RL__SECURITY_MANAGER]]

#. SW developer/Architects <rl__contributor>

   * Create work products based on the requirements
   * Provides the input work products for verification activities
   * SW developer create unit tests.

#. Test Contributors <rl__contributor>

   * Create verification artifacts

#. Test Committer <rl__committer>

   * Review and approve verification artifacts
   * Get support by the [[RL__SAFETY_MANAGER]] for safety-critical artifacts

#. Infrastructure/Tooling Developer <rl__infrastructure_tooling_community>

   * Enables execution of test cases in CI
   * Generation of verification reports
   * Provides tools for test generation
   * Integrates static analysis, linting, test frameworks into CI

#. Safety Manager <rl__safety_manager>

   * Supports the verification activities for safety-critical work products.

#. Safety External Auditor <rl__safety_external_auditor>

   * Understand safety activities, planning, processes definition, and execution reports for verification activities

#. "Distributor" (external role)

   * Re-execution of test cases
   * Testing OSS parts on product hardware
   * Integrate the test cases in their product (distribution)
   * Create issue reports and provide improvements

.. _verification_concept_types_methods:

# Verification Methods

A verification is based on different methods. An overview of the different methods that are
applicable are:

 * Control Flow Analysis (control-flow-analysis)
 * Data Flow Analysis (data-flow-analysis)
 * Fault Injection (fault-injection)
 * Inspection (inspection)
 * Interface Test (interface-test)
 * Requirements-based Test (requirements-based)
 * Resource Usage Evaluation (resource-usage)
 * Static Code Analysis (static-code-analysis)
 * Structural Statement coverage (structural-statement-coverage)
 * Structural Branch Coverage (structural-branch-coverage)
 * Walkthrough (walkthrough)

The derivation of test cases can also be based on certain methods.

 * Analysis of boundary values (boundary-values)
 * Analysis of equivalence classes (equivalence-classes)
 * Analysis of requirements (requirements-analysis)
 * Analysis of design (design-analysis)
 * Error guessing based on knowledge or experience (error-guessing)
 * Fuzzy testing (fuzz-testing)
 * Explorative testing (explorative-testing)

Usually the defined methods are not applied on each verification level between unit and platform level.
Also their execution may differ whether it is a QM or ASIL rated test case.
The rigor is described in the implementation of [[WP__VERIFICATION_PLAN]].

Automated test cases (as well as manual, where applicable) shall contain further information about which methods have been applied.
The corresponding guidance is given here: [[GD_GUIDL__VERIFICATION_GUIDE]].
The identifier of the respective method is to be used as meta data (*TestType* and *DerivationTechnique*).

# Test Case Development

Following aspect should be considered when developing test cases:

* **Comprehensive Coverage:** Test cases should cover all functional and tool requirements, including
  positive, negative, and boundary conditions. Specific attention should be given to corner cases and error handling.
* **Requirements Testing:** Guarantees testing of Component, Feature, and Stakeholder requirements.
* **Unit Testing:** Focus on testing individual units or components of the code.
  Strive for high code coverage for branches and lines.
  Coverage goals are defined in the [[WP__VERIFICATION_PLAN]].
  Consider not mocking away libraries the unit uses, as long as you can obtain sufficient
  structural coverage from the unit testing with included/integrated libraries,
  as this reduces effort on integration testing.
* **Integration Testing:** Verify the interaction between different components or modules.
  Depending on the implementation this can be on component, module or feature level.
* **Platform Integration Testing:** Test the platform with configured features as a whole.
* **Regression Testing:** Ensure that changes do not introduce new defects.
  Automate regression tests where possible as they will get executed as part of the CI.
* **Performance Testing (when applicable):** Evaluate the performance characteristics of the code,
  such as execution time, memory usage, and resource utilization.
* **Tool Qualification Testing:** Test the platform tools based on their tool requirements to achieve tool qualification.

# General Traceability Concept

To allow a traceability of code to a written requirement, unit tests are linked to other unit
tests or component tests. This linking is done using metatags. This is also true for component
integration tests linking to the component requirements and architecture.

Traceability of feature integration tests shall be established through linking those test cases to
feature requirements and architecture as features describe the integrated behaviour of all components.

Traceability of platform integration tests shall be established through linking those test cases to
stakeholder requirements as stakeholder requirements describe the platform behaviour.

Note that all the above tests shall only link to requirements of type "Functional" and "Interface".
The verification of requirements of types "Process" and "Non-Functional" will be done via Analysis,
which is part of the requirement inspection [[DOC__FEATURE_NAME_REQ_INSPECTION]] and `Component Requirements Inspection Checklist <https://eclipse-score.github.io/module_template/main/score/component_example/docs/requirements/chklst_req_inspection.html>`__.
Requirements always include Assumptions Of Use.

A more detailed description of how to link code to requirements is available here: [[GD_REQ__VERIFICATION_LINK_TESTS]]

## Workflow for Verification Guidance

.. _requirement_verification_workflow:

The requirement_verification_workflow above displays the whole workflow including the traceability concept for the
requirements where requirements shall be linked to test cases on the respective level. However also a statement
concerning the completeness of the test suite shall be generated. This means that also a linkage document shall be
generated including:

- the hash and UID of the requirement which was evaluated for test coverage
- the UIDs of the test cases which are required to fully cover the requirement.

So if the content of the requirement is altered also the hash will change making it necessary to
revisit the linkage of all test cases to the requirement again.

If the status of the linked test case and the linkage document is valid the attribute *testcovered* shall be set to *YES* during the SW Build.
Further information can also be depicted from the requirements_engineering process.

# Software Component Qualification

The qualification of pre-existing software (e.g. Open Source project) developed and maintained outside of the project scope,
requires various verification efforts to guarantee the quality matches the expectations of the project.

Existing requirements, specifications and documentation can be used to fill traceability gaps.
Existing test cases can be re-used and need to be linked against [[WP__REQUIREMENTS_COMP]] maintained within this project.

Also, details in external_tsf to collect evidence required for component qualification can be referred to rate the maturity
of the externally provided component.
Eclipse projects are further supposed to align with the Eclipse Functional Safety Process which is documented
in the `Eclipse Foundation Functional Safety Process GitLab <https://gitlab.eclipse.org/eclipsefdn/emo-team/policies/functional-safety-process>`_.
