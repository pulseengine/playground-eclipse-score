---
id: DOC-CLIPPY-53315
title: Clippy
type: specification
status: approved
tags: [eclipse-score]
---

### clippy

{{artifact:DOC_TOOL__CLIPPY:status,safety-level,security}}

# Clippy Verification Report

## Introduction

### Scope and purpose

Clippy is a linter tool (performs static code analysis) for the Rust programming language.
It provides a collection of lints to catch common mistakes and improve code quality.
Clippy helps developers identify potential issues in their Rust code, such as performance pitfalls,
stylistic inconsistencies, and potential bugs.

### Inputs and outputs

| Inputs: Software sources (Rust), Lint configuration
| Outputs: Report with detected rules violations

### Available information

- Version: >= 1.90.0 [1]_
- Official repository: https://github.com/rust-lang/rust-clippy
- Official documentation: https://github.com/rust-lang/rust-clippy
- Clippy configuration in S-CORE module repository: https://github.com/eclipse-score/score_rust_policies/tree/main/clippy

## Installation and integration

### Installation

| To add the Clippy Bazel targets to your project or module follow guidelines in `here <https://github.com/eclipse-score/score_rust_policies>`_

### Integration

Integrated in bazel.

### Environment

Requires Rust toolchain and Bazel build environment.

## Safety evaluation

This section outlines the safety evaluation of clippy for its use within the S-CORE project.

.. list-table:: Safety evaluation
   :header-rows: 1
   :widths: 1 2 8 2 6 4 2 2

   * - Malfunction identification
     - Use case description
     - Malfunctions
     - Impact on safety?
     - Impact safety measures available?
     - Impact safety detection sufficient?
     - Further additional safety measure required?
     - Confidence (automatic calculation)
   * - 1
     - False-negative: Fail to detect non-compliance with the consistency rules
     - | Diverging from consistency rules.
       | However lints are not involved in ensuring correctness of code, but only a measure of quality of the source code.

     - no
     - no
     - yes
     - no
     - high
   * - 2
     - False-positive: Report non-compliance, although the code is compliant
     - | No in code malfunction.
       | However this will cause an failure in CI/CD checks that needs to be resolved before merging code by author through manual inspection and explanation
     - no
     - no
     - yes
     - no
     - high

## Security evaluation

This section outlines the security evaluation of Rustfmt for its use within the S-CORE project.

.. list-table:: Security evaluation
   :header-rows: 1

   * - Threat identification
     - Use case description
     - Threats
     - Impact on security?
     - Impact security measures available?
     - Impact security detection sufficient?
   * - 1
     - TBD
     - TBD
     - TBD
     - TBD
     - TBD

### Result

Clippy does not require qualification for use in safety-related software development according to ISO 26262.

