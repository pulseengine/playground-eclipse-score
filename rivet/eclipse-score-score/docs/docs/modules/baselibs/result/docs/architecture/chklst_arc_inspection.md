---
id: DOC-CHKLST-ARC-INSPECTION-19869
title: Chklst Arc Inspection
type: specification
status: approved
tags: [eclipse-score]
---

### Result Library Architecture Inspection Checklist

{{artifact:DOC__RESULT_LIB_ARC_INSPECTION:status,safety-level,security}}

# Architecture Inspection Checklist

No need for component architecture inspection, as there is no additional information as in the
feature architecture [[DOC__BASELIBS_ARCHITECTURE]] and this is to be inspected.

The following static views in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: "result" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_sta
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

and the following dynamic views:

.. needtable::
   :filter: "result" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_dyn
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
