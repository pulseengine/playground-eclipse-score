# Falsification journey

The corpus oracle path from "naïve conversion" to GREEN, kept as a
record because the **shape** of the journey is the most informative
artifact — it shows exactly where rivet's typed-traceability model
needed to bend to fit a real ASIL-rated corpus, and exactly where
eclipse-score's own metamodel doesn't match its data.

| Step | Errors | Δ | What changed |
|---|---:|---:|---|
| 0. Per-repo conversion, single-repo oracle | 154 | — | First validation against just the persistency conversion. All errors were "target not found" — cross-repo references (`FEAT_REQ__PERSISTENCY__*` lives in the score repo, not persistency). Not a schema gap; just externals not wired. |
| 1. Combined corpus oracle (`rivet.yaml` loads all 4 repos) | 1476 | +1322 | Cross-repo references now resolve. New errors surface real schema and converter limitations. |
| 2. Converter fix: parse indented `.. <type>::` directives | 1476 | 0 | Eclipse uses RST bulleted lists for ISO 26262 / ASPICE clause registers (`.. std_req::` at column 4). Recovered 522 std_req/std_wp needs that were silently dropped. (Net error count stays similar because the recovered std_req entries now act as link *targets* that other artifacts reach — closing some "target not found" errors while opening new validity ones.) |
| 3. Switch from main rivet schema to vendored `chore/score-schema-eclipse-comparison-update` | 370 | -1106 | The round-1 schema deltas (new artifact types, new link types, missing field fixes) drop ~1100 errors. The schema previously declared `mitigated-by` as a link-field but the link-type itself didn't exist; renamed to `is-mitigated-by`. Added `role`, `workproduct`, `std-req`, `std-wp`, 8 arch refinement types, etc. |
| 4. Converter: filter code-block templates + `<...>` placeholders | 370 | 0 | Eclipse's RST docs include literal `.. feat_saf_fmea:: <Title>` template snippets inside `.. code-block:: rst`. Sphinx-needs ignores them; so must we. |
| 5. Schema round 2 — required-field relaxations | 320 | -50 | `fmea-entry.failure-mode`, `dfa-entry.analysis`, `decision-record.rationale` made optional. **These were rivet schema mistakes** — eclipse's metamodel never required them. |
| 6. Schema round 2 — required-link relaxations | 263 | -57 | `feat-req.satisfies`, `comp-req.satisfies`, `comp.realizes`, `mod.belongs-to` softened from `required: true / cardinality: one-or-many` → `cardinality: zero-or-many`. **Half my rivet mistake, half eclipse-corpus reality** — eclipse's metamodel says these are mandatory_links but ~17 of their own artifacts don't have them. The traceability-rules still flag them (severity downgraded `error → warning`). |
| 7. Schema round 2 — link target-type widenings | 138 | -125 | `violates` and `uses` widened to accept arch types. Rivet was narrower than eclipse's actual metamodel here (eclipse's `comp_saf_fmea.violates: comp_arc_dyn, comp_arc_sta`). |
| 8. Schema round 2 — `tool-req.satisfies` + `workproduct.complies` target widenings | 5 | -133 | Eclipse `tool_req` artifacts `:satisfies:` gd_req entries (now allowed); eclipse `wp` artifacts `:complies:` std_req entries (now allowed). |
| 9. Converter: `;` separator + skip eclipse's own metamodel test fixtures | **0** | -5 | One eclipse RST uses `;` instead of `,` to separate link targets. Eclipse's `docs-as-code/src/extensions/score_metamodel/tests/rst/` is a test corpus for the metamodel itself; those needs are intentionally broken examples. Excluded. |

Final state: `Result: PASS (2289 warnings)` over **2752 artifacts**.

## What the 2289 warnings are

All lifecycle coverage gaps in eclipse's own data:

- Feature requirements without a downstream test-spec / comp-req
- Component requirements without a downstream dd-sta / dd-dyn / test-spec
- FMEA entries without an `is-mitigated-by` link
- etc.

These are **eclipse's reality** — work in progress, artifacts being
authored ahead of their downstream peers. We log them as warnings
rather than errors per the round-6 reasoning above.

## What this proves

- Rivet's typed-traceability model has *enough scope* to losslessly
  represent eclipse-score-scale ASIL work.
- The schema's predictive power was off in five categorical ways, all
  cheap to fix once the corpus oracle measured them.
- Eclipse-score's own metamodel is itself imperfect — declaring
  mandatory links that ~17 of their own artifacts don't have. The
  pulseengine philosophy ("falsification, not prediction") would call
  for either tightening eclipse's CI or relaxing their metamodel; we
  chose to mirror eclipse's *behaviour* (warnings, not errors) rather
  than their *claims*.
