---
id: DOC-INDEX-34892
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

.. _external_tsf:

# Trustable Software Framework

.. note::
   The copyright check ignores all files in trustable and its subdirectories.
   Modified BUILD file in process repository to be reverted after reuse implementation
   is implemented in tooling.

*The* `Trustable Software Framework (TSF) <https://codethinklabs.gitlab.io/trustable/trustable/index.html>`_
*approach is designed for consideration of software where factors such as safety, security,
performance, availability and reliability are considered critical. Broadly it asserts that any
consideration of trust must be based on evidence.*

The tenets and assertions defined in the Trustable Software Framework can be used to measure an (OSS) project trust score.
To calculate the score link evidences to the Trustable Assertions (TA).

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   tenets/tenets
   assertions/assertions

### TRUSTABLE SOFTWARE

{{artifact:TSF__TRUST__TRUSTABLE-SOFTWARE:status,safety-level,security}}

## XYZ Trustable Overview

### Trustable Software Framework

.. needtable::
   :style: table
   :columns: title;id;status;links
   :colwidths: 25,25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["tsf"]):
                results.append(need)

### Trustable Tenets Overview

.. needtable::
   :style: table
   :columns: title;id;status;links
   :colwidths: 25,25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["tenet"]):
                results.append(need)

### Trustable Assertions Overview

.. needtable::
   :style: table
   :columns: title;id;status;links
   :colwidths: 25,25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["assertion"]):
                results.append(need)
