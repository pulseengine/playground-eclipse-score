---
id: DOC-VERIFICATION-SPECIFICATION-19275
title: Verification Specification
type: specification
status: approved
tags: [eclipse-score]
---

# Test Specification Guideline

### Test Specification Guideline

{{artifact:GD_GUIDL__VERIFICATION_SPECIFICATION:status,safety-level,security}}

## Test specification

A test specification contains the following attributes.

.. list-table:: Test specification properties
   :header-rows: 1
   :widths: 10 30 40 20

   * - Property
     - Type / Values
     - Description
     - Helpful links
   * - Partially and/or Fully Verifies
     - Docs-as-code Id(s) for traceable elements
     - Links to one or more requirement Ids. Can be partial or full coverage of a
       requirement, as per test property.
     -
   * - Description
     - Text
     - The description should include

       - The objective of the test.
       - Inputs
       - Expected outcome (e.g. "A success message is displayed.")
       - Test environment (e.g. network configuration, clean system state)
     -
   * - TestType
     - Examples are:

       - requirements-based
       - interface-test
       - coverage (various types apply, shall be tool supported)
     - These are example values and an incomplete list.
       A full list of test types is available in [[DOC_CONCEPT__VERIFICATION_PROCESS]] at
       verification_concept_types_methods.
     -
   * - DerivationTechnique
     - Examples are:

       - requirements-analysis
       - boundary-values
       - equivalence-classes
       - error-guessing
     - These are example values and an incomplete list.
       A full list of test methods is available in [[DOC_CONCEPT__VERIFICATION_PROCESS]] at
       verification_concept_types_methods.
     -

The implementation of [[WP__VERIFICATION_PLAN]] defines the full list of allowed types and methods.

## Test description

Following Given-When-Then is a preferred way to write test specifications.

* | Given (alternatively // Setup  )
  | This section contains the setup of the input.
* | Expected
  | This Section contains the expectation for calls to mocks or stubs
* | When (alternatively  // Call   )
  | This section contains the call to the software under test.
* | Then (alternatively // Expect )
  | This section contains the verification criteria of the test (e.g. all EXPECT statements).

.. code-block:: cpp

   TEST(CreateObjectHistory, GivenVehicleInFront_ExpectHistoryBehindFrontVehicle)
   {
      // Given
      const auto whatever_input_values = CreateVehicleInFront();

      // Expected
      EXPECT_CALL(..., ...);

      // When
      const auto history = CreateObjectHistory(whatever_input_values, ...);

      // Then
      for (const auto point : history)
      {
         EXPECT_EQ(..., ...);
      }
   }

Another example for a good test description could be:

  | Verify successful login with valid credentials.
  | Input:
  | - Username: testuser
  | - Password: password123
  | Expected Outcome:
  | - User is redirected to the home page and the welcome message "Hello, testuser!" is displayed.

A example for a bad test description could be:

   Test user login

Additional information can also be found in [[GD_GUIDL__VERIFICATION_GUIDE]].

The specification is part of the test implementation and has to comply to the requirements
specified in [[GD_REQ__VERIFICATION_LINK_TESTS]].
