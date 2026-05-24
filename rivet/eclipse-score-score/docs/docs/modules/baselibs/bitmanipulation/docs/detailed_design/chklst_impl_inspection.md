---
id: DOC-CHKLST-IMPL-INSPECTION-51055
title: Chklst Impl Inspection
type: specification
status: approved
tags: [eclipse-score]
---


### Bitmanipulation Implementation Inspection Checklist

{{artifact:DOC__BITMANIPULATION_IMPL_INSPECTION:status,safety-level,security}}

# Implementation Inspection Checklist

## Purpose

The purpose of this checklist is to collect the topics to be checked during implementation,
i.e. in the detailed design and the source code of the units.

The checklist shall be agnostic to which programming language is used. Differences shall be treated
by linking to C++ or Rust specific documentation.

## Conduct

As described in the concept [[DOC_CONCEPT__WP_INSPECTIONS]] the following "inspection roles" are expected to be filled:

- content responsible (author): <contributor/committer explicitly named here, who is the main author, as can be seen in config mgt tooling>
- reviewer: <contributor/committer explicitly named here, who is the main content reviewer, must be different from content responsible>
- moderator: <committer explicitly named here, who is is the safety manager, security manager or quality manager initiating the inspection>

## Checklist

It is mandatory to fill in the "passed" column with "yes" or "no" for each checklist item and additionally to add in the remarks why it is passed or not passed.
In case of "no" an issue link to the issue tracking system has to be added in the last column (if not solved in the same issue).
See also [[DOC_CONCEPT__WP_INSPECTIONS]] for further information about reviews in general and inspection in particular.

.. list-table:: Implementation Checklist
   :header-rows: 1
   :widths: 10,30,50,6,6,8

   * - Review ID
     - Acceptance Criteria
     - Guidance
     - Passed
     - Remarks
     - Issue link
   * - IMPL_01_01
     - Is the design according to guidelines?
     - see [[GD_TEMP__DETAILED_DESIGN]] and [[DOC_CONCEPT__IMP_CONCEPT]]
       (e.g. are the views done with the proposed UML diagrams)
     -
     -
     -
   * - IMPL_01_02
     - Is the implementation according to specification?
     - Check if the linked component requirements are fulfilled
       and detailed design also matches architecture description.
     -
     -
     -
   * - IMPL_01_03
     - Are the design decisions and constraints documented?
     - Check also for plausibility of these.
     -
     -
     -
   * - IMPL_01_04
     - Are all external libraries used by the component specified in the detailed design?
     - Check the automated dependency analysis.
       Also make sure ASIL rated units also only use ASIL rated libraries.
     -
     -
     -
   * - IMPL_02_01
     - Are the static and dynamic code analysis reports verified for violations?
     - All violations in ASIL related code must be justified. This includes the checks of coding guidelines.
     -
     -
     -
   * - IMPL_02_02
     - Do manual checks, that are derived from the coding guideline, find no safety critical error?
     - Check this for the programming language used (e.g. C++ <link_to_checks_list>, Rust <link_to_checks_list>)
     -
     -
     -
   * - IMPL_02_03
     - Are detailed design and source code consistent?
     - Check if the static and dynamic design descriptions match the code (e.g. naming of elements)
       and that the respective traceability is established
     -
     -
     -
