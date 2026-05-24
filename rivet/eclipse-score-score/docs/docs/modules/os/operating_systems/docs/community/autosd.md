---
id: DOC-AUTOSD-80219
title: Autosd
type: specification
status: approved
tags: [eclipse-score]
---

### AutoSD

{{artifact:COMP__OS_AUTOSD:status,safety-level,security}}

# AutoSD

AutoSD is the upstream binary distribution that serves as the public, in-development preview and functional precursor
of the Red Hat In-Vehicle Operating System (OS).

AutoSD is downstream of CentOS Stream, so it retains most of the CentOS Stream code with a few divergences,
such as an optimized automotive-specific kernel rather than CentOS Stream's kernel package.

Red Hat In-Vehicle OS is based on both AutoSD and RHEL, both of which are downstreams of CentOS Stream.

## OS Maintainers/Integration Assistance

GitHub Handles of the target maintainers.

- Leonardo Rossetti - @odra

## Integration Assistance

The following fulfills [[AOU_REQ__PLATFORM__INTEGRATION_ASSISTANCE]]

+----------------+-----------------------------+
| .. centered:: Leonardo Rossetti              |
+----------------+-----------------------------+
| Github Handler | @odra                       |
+----------------+-----------------------------+
| Slack Handler  | @lrossett                   |
+----------------+-----------------------------+

## Integration Manual

The following fulfills [[AOU_REQ__PLATFORM__OS_INTEGRATION_MANUAL]]

#### Supported Architectures

+----------------------+----------------------------+
| Target Architecture  | Comments                   |
+----------------------+----------------------------+
| x86_64               | Native Only                |
+----------------------+----------------------------+
| aarch64              | Native Only                |
+----------------------+----------------------------+

#### Build Instructions

Building an AutoSD image can be done by using `aib <https://gitlab.com/CentOS/automotive/src/automotive-image-builder>`_.

Sample usage:

As an alternative, you can replace the bare metal "aib" usage with a bash script that runs the tool inside an OCI container:

You can then replace the usage of "aib" with "auto-image-builder.sh" (requires sudo):

If using QEMU, you can run the image using the following command:

#### Toolchain

Refer to the `upstream toolchain repository <https://github.com/eclipse-score/inc_os_autosd/tree/main/toolchain>`_ for detailed instructions.

A Bazel toolchain defintion is provided for users to build their Bazel modules and components with AutoSD's tooling (compilers, libraries, etc).

Sample usage (MODULE.bazel file):

**NOTE:** AutoSD's tooling does not support cross compilation.

#### Mixed Critical Orchestration

Refer to the `upstream CentOS automotive documentation <https://sigs.centos.org/automotive/features-and-concepts/con_mixed-criticality/>`_ for detailed information.

Mixed Critical Orchestration, aka MCO, can be achieved with the following components:

* Systemd: the init system that is responsible for workload orchestration
* Eclise BlueChi: extends Systemd to enable multi-node and multi domain orchestration
* QM: Quality management environment that is composed of two sub-systems: a dedicated rootfs partition + container isolation

ASIL and QM connectivity is done either via an IPC socket or shared memory (/dev/shm).

## Bug Interface

The following fulfills [[AOU_REQ__PLATFORM__BUG_INTERFACE]]

+------------------------------------+---------------------------------------------------------------------------+
|                                                                                                                |
+------------------------------------+---------------------------------------------------------------------------+
| CentOS SIG Automotive Mailing List | https://lists.centos.org/hyperkitty/list/automotive-sig@lists.centos.org/ |
+------------------------------------+---------------------------------------------------------------------------+
| Gitlab Issue Tracker               | https://gitlab.com/CentOS/automotive/sig                                  |
+------------------------------------+---------------------------------------------------------------------------+
| CentOS SIG Matrix Channel          | https://app.element.io/#/room/#centos-automotive-sig:fedoraproject.org    |
+------------------------------------+---------------------------------------------------------------------------+
| Eclipse SDV Slack Channel          | #autosd (https://sdvworkinggroup.slack.com/archives/C0986LJ9EJH)          |
+------------------------------------+---------------------------------------------------------------------------+
