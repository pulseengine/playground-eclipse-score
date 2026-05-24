---
id: DOC-EBCLFSA-76210
title: Ebclfsa
type: specification
status: approved
tags: [eclipse-score]
---

### EBcLfSA

{{artifact:COMP__OS_EBCLFSA:status,safety-level,security}}

# EB corbos Linux for Safety Applications (EBcLfSA)

EB corbos Linux for Safety Applications (also EBcLfSA and Linux for Safety Applications), a product of Elektrobit, is a special operating system based on Linux.
It allows to run HI Applications (High Integrity Applications) for safety-related functions on top of the Linux kernel.

The full and qualified stack uses a hypervisor to separate HI Applications from other applications and from the Linux kernel.
To ensure spatial isolation even from the Linux kernel, a limited sub-set of system calls shall not be executed by an HI Application.
These system calls let the Linux kernel perform unsupervised operations on the HI Application's memory.
Linux for Safety Applications protects an HI Application from such operations and guarantees its execution integrity.

The public variant of EBcLfSA (which is the variant currently integrated in S-CORE) uses a single Linux kernel and is intended for use in development.
It is capable to analyze HI Applications in a so-called "fastdev" (fast development) environment.

It contains a Linux user-space which is geared towards the development of HI Applications.
And it provides feedback if an HI Application makes unsupervised system calls on the Linux kernel.

## OS Maintainers/Integration Assistance

GitHub Handles of the target maintainers.

- Oliver Pajonk - @opajonk

## Integration Assistance

The following fulfills [[AOU_REQ__PLATFORM__INTEGRATION_ASSISTANCE]]

+----------------+-----------------------------+
| .. centered:: Oliver Pajonk                  |
+----------------+-----------------------------+
| Github Handler | @opajonk                    |
+----------------+-----------------------------+
| Slack Handler  | @opajonk                    |
+----------------+-----------------------------+

## Integration Manual

The following fulfills [[AOU_REQ__PLATFORM__OS_INTEGRATION_MANUAL]]

#### Supported Architectures

+----------------------+-----------------------------+
| Target Architecture  | Comments                    |
+----------------------+-----------------------------+
| aarch64              | Cross-compilation supported |
+----------------------+-----------------------------+

#### Build Instructions

Currently, there are no build instructions for EBcLfSA, as relevant parts of the public variant are available only as binaries at the moment.
Especially, the base image for the "fastdev" environment is only available as a binary.
A sysroot (or sometimes called SDK, toolchain, etc.) for cross-compilation is available as a binary as well.
These can be used to build HI Applications for EBcLfSA for development purposes, e.g. to build Eclipse S-CORE.
Additional user-space components are deployed via running a QEMU emulator and then installing the components via SCP.
See the `reference_integration <https://github.com/eclipse-score/reference_integration/tree/main/images/ebclfsa_aarch64>`_ repository for details on this activity.
This will change in the future, and then the build instructions will be added here.

#### Toolchain

Refer to the `upstream repository <https://github.com/Elektrobit/eb_corbos_toolkit>`_ for detailed, generic instructions.

For Eclipse S-CORE, a Bazel toolchain defintion is provided for users to build their Bazel modules and components with EBcLfSA's tooling (compilers, libraries, etc).

Sample usage (MODULE.bazel file):

## Bug Interface

The following fulfills [[AOU_REQ__PLATFORM__BUG_INTERFACE]]

+------------------------------------+-------------------------------------------------------------------------------------+
|                                                                                                                          |
+------------------------------------+-------------------------------------------------------------------------------------+
| GitHub Issue Tracker               | https://github.com/Elektrobit/eb_corbos_toolkit?tab=readme-ov-file#reporting-issues |
+------------------------------------+-------------------------------------------------------------------------------------+
| Eclipse SDV Slack Channel          | #ebclfsa (https://sdvworkinggroup.slack.com/archives/C0A33SCH8U9)                   |
+------------------------------------+-------------------------------------------------------------------------------------+
