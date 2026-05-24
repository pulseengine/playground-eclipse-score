---
id: DOC-OS-ONBOARD-TEMPLATE-47359
title: Os Onboard Template
type: specification
status: approved
tags: [eclipse-score]
---

# OS Name

### [OS Name]

{{artifact:DOC__OS_ONBOARDING:status,safety-level,security}}

The following component needs to be defined at the top of the page (modify accordingly):

.. code-block:: rst

### [OS Name]

{{artifact:COMP__OS_[OS_NAME]:status,safety-level,security}}

Short overview of the operating system and why it is relevant for S-CORE.
Keep this to 3-6 lines. Mention what the OS is and the intended usage context.

## Target Maintainers/Integration Assistance

GitHub Handles of the target maintainers.

## Integration Assistance

The following fulfills [[AOU_REQ__PLATFORM__INTEGRATION_ASSISTANCE]]

- Provide the names or mailing lists that users can contact for help with S‑CORE integration.
- Use bullet points for multiple contacts.

## Integration Manual

The following fulfills [[AOU_REQ__PLATFORM__OS_INTEGRATION_MANUAL]]

- Summarise how to obtain and use the integration manual for this operaring system.
- Link to external documentation if it exists.

## Supported Architectures

+-----------------------+--------------------------------+
| Target Architecture   | Comments                       |
+-----------------------+--------------------------------+
| <target_arch>         | <Native Only, Cross Compile>   |
+-----------------------+--------------------------------+

## Build Instructions

Explain how to build an image (or how to retrieve a pre-built one) of this OS and how to build Eclipse S-CORE for it.

Provide any architecture specific details based on the architecture table.

.. code-block:: console

  # example commands to build an image
  curl -o /tmp/image-builder.sh https://example.com/image-builder.sh
  chmod +x /tmp/image-builder.sh
  sudo bash /tmp/image-builder.sh --distro <distro> --target <target>

Provide any additional context, such as how to boot or run the image (e.g. with QEMU), supported architectures, etc.

Describe any additional distinctions that need to be made based on the "Supported Architectures" section.

## Toolchain

- Any details worth mentioning
- Provide any architecture specific details based on the architecture table.
- Explain how to set up Bazel toolchains for this OS.
- Include a short example ``MODULE.bazel`` snippet.
- Describe any additional distinctions that need to be made based on the "Supported Architectures" section.

## Bug Interface

The following fulfills [[AOU_REQ__PLATFORM__BUG_INTERFACE]]

- Explain how users can report bugs (mailing lists, issue trackers, Matrix/Slack channels etc.).
