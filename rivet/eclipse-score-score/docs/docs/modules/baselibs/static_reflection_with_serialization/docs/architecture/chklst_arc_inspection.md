---
id: DOC-CHKLST-ARC-INSPECTION-92369
title: Chklst Arc Inspection
type: specification
status: approved
tags: [eclipse-score]
---

### Static Reflection Architecture Inspection Checklist

{{artifact:DOC__STATIC_REFLECTION_ARC_INSPECTION:status,safety-level,security}}

# Architecture Inspection Checklist

Component is missing in feature architecture [[DOC__BASELIBS_ARCHITECTURE]] and this has to be corrected.

The following static views in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: "static_reflection" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_sta
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

and the following dynamic views:

.. needtable::
   :filter: "static_reflection" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_dyn
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
