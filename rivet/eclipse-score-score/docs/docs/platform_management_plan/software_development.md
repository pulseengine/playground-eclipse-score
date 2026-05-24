---
id: DOC-SOFTWARE-DEVELOPMENT-59076
title: Software Development
type: specification
status: approved
tags: [eclipse-score]
---

.. _sw_development:

## Software Development Plan

### Software Development Plan

{{artifact:DOC__SOFTWARE_DEVELOPMENT_PLAN:status,safety-level,security}}

#### Purpose

The main purpose of the software development plan is to define several software development related conditions:

* selection of design and programming language
* design guideline
* coding guideline (e.g. MISRA, can also include style guide or naming convention)
* SW configuration guideline
* development tools

#### Objectives and Scope

Objective is to define the main SW development policies as defined in the "Purpose" in an ISO 26262 and ASPICE compliant manner.
Scope is the complete SW platform and the development parts of the process.

#### Approach

#### Selection of design and programming language

For the selection of design and programming language a stakeholder requirement is defined in [[STKH_REQ__DEV_EXPERIENCE__PROG_LANGUAGES]],
which is based on experience. The criteria for selection are based on the following aspects:

* Unambiguous definition of syntax and semantics
* Suitability for specifying and managing for safety related requirements and design
* Support of modularity, abstraction and encapsulation
* Support of the use of structured constructs

The selected languages form the stakeholder requirements were analysed in the following table:

.. list-table:: Selection of design and programming language
   :header-rows: 1
   :widths: 33,33,33

   * - Criteria
     - C++
     - Rust
   * - Unambiguous definition of syntax and semantics
     - Standardized, strict syntax, strong tooling
     - Strict syntax, single compiler, strong tooling
   * - Suitability for safety related programming
     - Certified tools, MISRA, static analysis, traceability
     - Compiler-enforced safety, strong type system, documentation, emerging safety support, certified tools
   * - Support of modularity, abstraction and encapsulation
     - Classes, templates, modules, access control
     - Modules, crates, traits, strong visibility control
   * - Support of the use of structured constructs
     - Full support for structured programming
     - Full support, enforced by language design

S-CORE allows the use of two programming languages:

**C++ with the language set of C++17** - in case additional elements from C++20 are needed this will be considered by
[[RL__SAFETY_MANAGER]], [[RL__SECURITY_MANAGER]] and [[RL__QUALITY_MANAGER]]
and based on their analysis decided by the project lead circle ([[RL__PROJECT_LEAD]]).

**Rust - in Edition 2021** - selection of language edition has still to be done in the S-CORE project.
For the Rust code of ASIL rated units the "safe subset" shall be used (which is checked by the compiler by configuration of #![forbid(unsafe_code)] in lib.rs)

C language is allowed in incubation phase, as long it is compilable be the selected compiler, but not for a S-CORE release.

For specifying **Detailed Design** (like for the Architecture) a mixture of UML diagrams and natural language is used.
Additionally for the Detailed Design linking to code, Doxygen style comments are used.
This is described in [[DOC_CONCEPT__IMP_CONCEPT]] and guided by [[GD_TEMP__DETAILED_DESIGN]]

#### Design guideline

The design guideline is defined in [[DOC_CONCEPT__IMP_CONCEPT]] and [[GD_GUIDL__IMPLEMENTATION]].

#### API guidelines

To provide the user with a consistent approach on the use of APIs, there are guidelines documented in [[DOC__API_GUIDELINES]]
and [[DOC__RUST_API_DESIGN]], this defines for example the error handling concept or rules to improve user experience.

#### Coding guidelines

**C++** - see [[DOC__CPP_CODING_GUIDELINES]]

**Rust** - see [[DOC__RUST_CODING_GUIDELINES]]

#### SW configuration guideline

The configuration of the software is done by the code. Which means that there are no external configuration files.

#### SW development tools

This list will evolve into the complete "Tool List" tools for the S-CORE project used for
tool evaluation and qualification. In the moment the [[DOC__VERIFICATION_PLAN]]
contains additional tools used in verification.

Additional tools for static and dynamic analysis (in addition to compilers and Clang-Tidy) are currently evaluated: `#244 <https://github.com/eclipse-score/score/issues/244>`_

is used for hosting, versioning and contribution of the software. Within
pull requests it's possible to contribute. For contribution a separate process description is
[[DOC__CONTR_GUIDELINE]] available. In the discussion section the information regarding meeting
minutes and Working Sections were stored. Within issues can bugfixes, improvements, blank issues
set up. It's also possible to report there Security vulnerabilities. GitHub Actions is used
as a support for continuous integration.

The following GitHub features are activated to improve security [[DOC__PLATFORM_VULNERABILITY_MGT_PLAN]] and quality for software development:
* **GitHub Dependabot** - Automated dependency vulnerability detection and update pull requests
* **GitHub Advanced Security** - Code scanning and secret scanning capabilities where available (CodeQL)

is used for software documentation to generate html-sides from reStructuredText.

is used for docs-as-code [[DOC_TOOL__DOC_AS_CODE]] based documentation that is created
and managed by the sphinx documentation generator. With "needs" objects, created in rst-files,
requirements, static architecture views and other Sw development documentation is generated. Sphinx-Needs is 100% compliant to
Sphinx and reStructuredText.

this UML drawing tool is used for dynamic and static diagrams for unit interaction. Also for dynamic architecture views.

this drawing tool is used to create flowcharts and diagrams for all uses where PlantUML is not suited
e.g. in process or concept descriptions

GCC is used as host C++ compiler with its associated linker. It's used as a development (compilation and linking) and verification tool
as it generates compiler warnings and builds unit tests and binaries for SW integration testing.

QCC the qualify-able compiler/linker from Blackberry offered together with its Posix conform Operating System QNX is planned to be used for target compilation.

is used in conjunction with the Clang compiler to perform static analysis.

There is currently no selection of a Rust compiler for S-CORE. Pick your own favourite.

The qualified `Ferrocene <https://github.com/ferrocene>`__ compiler is planned to be used.

The main build environment of the project is based on `Bazel <https://bazel.build>`__. It it used to build software
components, documentation, and automated tests.
