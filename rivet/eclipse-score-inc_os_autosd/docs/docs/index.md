---
id: DOC-INDEX-52788
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# CentOS AutoSD 9 Development Target

This documentation describes the structure, usage and configuration of AutoSD in Eclipse S-CORE.

## Overview

This repsotory provides the recommended setup to build and run S-CORE in an AutoSD image.

This repository provides a standardized setup for projects using **C++** or **Rust** and **Bazel** as a build system.
It integrates best practices for build, test, CI/CD and documentation.

## Requirements

### CentOS AutoSD 9 Development Target

{{artifact:STKH_REQ__SUPPORTED_PLATFORMS__AUTOSD_DEV:status,safety-level,security}}

## Project Layout

+---------------------------------------------+------------------------------------------------------------+
| File/Folder                                 | Description                                                |
+=============================================+============================================================+
| ``README.md``                               | Repository short description and instructions              |
+---------------------------------------------+------------------------------------------------------------+
| ``toolchain/``                              | Bazel toolchain to build modules using AutoSD's tooling    |
+---------------------------------------------+------------------------------------------------------------+
| ``tests/``                                  | Build files for testing the toolchain on top of S-Core     |
+---------------------------------------------+------------------------------------------------------------+
| ``docs/``                                   | Documentation                                              |
+---------------------------------------------+------------------------------------------------------------+
| ``.github/workflows/``                      | CI/CD pipelines                                            |
+---------------------------------------------+------------------------------------------------------------+
| ``.vscode/``                                | Recommended VS Code settings                               |
+---------------------------------------------+------------------------------------------------------------+
| ``.bazelrc``, ``MODULE.bazel``, ``BUILD``   | Bazel configuration & settings                             |
+---------------------------------------------+------------------------------------------------------------+
| ``project_config.bzl``                      | Project-specific metadata for Bazel macros                 |
+---------------------------------------------+------------------------------------------------------------+
| ``LICENSE``                                 | Licensing information                                      |
+---------------------------------------------+------------------------------------------------------------+
| ``CONTRIBUTION.md``                         | Contribution guidelines                                    |
+---------------------------------------------+------------------------------------------------------------+

## Quick Start

### Documentation

Documentation is dealt as a top level "folder" and bazel should be used to build it by running:

.. code-block:: shell

   bazel run //:docs

You can then proceed to open ``_build/index.html`` in a web browser.

In case you want to run a clean build from scratch, run the following command before triggering a new build:

.. code-block:: shell

   bazel clean --expunge && \
   rm -rf .cache/ && \
   rm MODULE.bazel.lock && \
    rm -rf _build

### Toolchain

TBD

## Configuration

The `project_config.bzl` file defines metadata used by Bazel macros.

Example:

.. code-block:: python

   PROJECT_CONFIG = {
       "asil_level": "QM"
   }
