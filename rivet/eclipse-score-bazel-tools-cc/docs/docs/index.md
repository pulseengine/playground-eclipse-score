---
id: DOC-INDEX-83189
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Module Template Documentation

This documentation describes the structure, usage and configuration of the Bazel-based C++/Rust module template.

## Overview

This repository provides a standardized setup for projects using **C++** or **Rust** and **Bazel** as a build system.
It integrates best practices for build, test, CI/CD and documentation.

## Requirements

### Example Functional Requirement

{{artifact:STKH_REQ__DOCGEN_ENABLED__EXAMPLE:status,safety-level,security}}

## Project Layout

The module template includes the following top-level structure:

- `src/`: Main C++/Rust sources
- `tests/`: Unit and integration tests
- `examples/`: Usage examples
- `docs/`: Documentation using `docs-as-code`
- `.github/workflows/`: CI/CD pipelines

## Quick Start

To build the module:

.. code-block:: bash

   bazel build //src/...

To run tests:

.. code-block:: bash

   bazel test //tests/...

## Configuration

The `project_config.bzl` file defines metadata used by Bazel macros.

Example:

.. code-block:: python

   PROJECT_CONFIG = {
       "asil_level": "QM",
       "source_code": ["cpp", "rust"]
   }

This enables conditional behavior (e.g., choosing `clang-tidy` for C++ or `clippy` for Rust).
