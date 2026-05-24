---
id: DOC-INDEX-62062
title: Index
type: specification
status: approved
tags: [eclipse-score]
---

# Requirements

### JSON Wrapper Requirements

{{artifact:DOC__JSON_WRAPPER_REQUIREMENTS:status,safety-level,security}}

Due to low complexity, the requirements of the JSON component were not split into the "sub" components
"JSON Wrapper" and "nlohman_json". Reasoning is the low number of requirements (only about ten).
The component split was done nevertheless, because "JSON Wrapper" is implemented as part of the S-CORE project and
"nlohman_json" is reused from open source.

So the requirements for "JSON Wrapper" are documented in [[DOC__JSON_REQUIREMENTS]]
(all requirements which are "fulfilled_by" [[COMP__BASELIBS_JSON_WRAPPER]])
