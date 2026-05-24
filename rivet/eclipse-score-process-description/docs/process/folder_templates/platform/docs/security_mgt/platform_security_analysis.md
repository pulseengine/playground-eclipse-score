---
id: DOC-PLATFORM-SECURITY-ANALYSIS-49331
title: Platform Security Analysis
type: specification
status: approved
tags: [eclipse-score]
---

# Platform Security Analysis

### Platform Security Analysis

{{artifact:DOC__PLATFORM_SECURITY_ANALYSIS:status,safety-level,security}}

.. ..  attention::
## Purpose

The purpose of this Security Analysis is to document the results of the platform security analysis.

## Platform Security Analysis

The following deliverables are the outcome of a security analysis on the platform.

#. Identification of threats and mitigations
#. Stakeholder security requirements definition
#. Security assumptions definition

### Threat and Risk Identification

.. ..  attention::
.. list-table:: Threat and Risk Identification
        :header-rows: 1

        * - Id
          - Identified Threat
          - Corresponding mitigation
          - Comment/Remark

        * - 1
          - Eg: A backend attacker performs MiTM between the OEM cloud and the platform component.
          - Eg: End to end TLS between the platform component and the OEM cloud service mitigates the MiTM attacks.
          - <Rationale for mitigation>

        * - 2
          - Eg: Unauthorized access to the onboard diagnostic stack from external interfaces.
          - Eg: Authentication and authorization mechanisms such as usage of tokens prevents such unauthorized access.
          - <Rationale for result>

        * - 3
          - Eg: Static configuration files are manipulated by an inside attacker.
          - Eg: OS specific access control mechanisms and least privilege principle prevents such unauthorized manipulation.
          - <Rationale for result>

### Stakeholder Security Requirements

.. list-table:: Stakeholder Security Requirements
        :header-rows: 1

        * - Id
          - Security Requirement
          - Comment/Remark

        * - 1
          - Eg: The platform shall use end to end mutual TLS and 2 factor authentication for communication between components and OEM cloud services.
          - <Rationale for the requirement>

        * - 2
          - Eg: Tokens shall be used for authorizing access to the onboard diagnostic APIs.
          - <Rationale for the requirement>

        * - 3
          - Eg: OS specific DAC (discretionary access control) and MAC (mandatory access control) shall be used for restricting access to assets such as configuration files.
          - <Rationale for the requirement>

### Security Assumptions

The assumptions of use shall be documented under [[WP__PLATFORM_SECURITY_MANUAL]].
