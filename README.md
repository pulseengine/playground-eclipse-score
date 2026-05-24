# `eclipse-score-fork` — eclipse-score in pulseengine shape

A trackable, rebase-friendly fork of four
[Eclipse S-CORE](https://github.com/eclipse-score) repositories,
converted from sphinx-needs RST into rivet typed YAML.

The point of this workspace is **falsification**: eclipse-score is real
ASIL-rated safety work at meaningful scale (2752 traceable artifacts
across 757 RST files in four repos). If pulseengine's typed-traceability
toolchain (rivet) can round-trip eclipse-score's model losslessly, then
rivet's scope is proven on real-world data — not on bespoke examples. If
the round-trip *fails*, that's binary evidence of what's missing.

## Workspace layout

```
eclipse-score-fork/
├── upstream/                            # raw upstream working copies
│   ├── eclipse-score-score/             # platform reqs + arch
│   ├── eclipse-score-process-description/   # workflows, roles, gd_*, std_*
│   ├── eclipse-score-persistency/       # component example (kvs)
│   └── eclipse-score-docs-as-code/      # the sphinx-needs metamodel
├── rivet/                               # generated rivet projects
│   ├── eclipse-score-score/
│   │   ├── rivet.yaml
│   │   ├── artifacts/imported.yaml      # generated; do not hand-edit
│   │   └── coverage.md                  # falsification report
│   ├── eclipse-score-process-description/  …
│   ├── eclipse-score-persistency/          …
│   └── eclipse-score-docs-as-code/         …
├── tools/
│   └── score_import.py                  # RST → rivet YAML converter
├── vendor/
│   └── rivet-schemas/                   # pinned snapshot of rivet schemas
├── rivet.yaml                           # combined corpus view
├── Makefile                             # convert / validate / rebase
└── README.md                            # you are here
```

## Naming

Each `upstream/<dir>` and `rivet/<dir>` follows
`eclipse-score-<upstream-repo-name>` so a single `eclipse-score-*` glob
filters the entire forked surface area (in `git`, in `ripgrep`, in IDE
file pickers, anywhere). The doubled-name case (`eclipse-score-score`,
where the upstream repo is just called `score`) is intentional — keeping
the upstream name verbatim makes the rebase target obvious.

## Status: GREEN

```
$ make validate
# rivet validate
Result: PASS (2507 warnings)
# rivet variant check-all
4/4 variants passed (0 failed)
```

- 2985 artifacts converted across 58 active eclipse-score repos
- 0 errors, 2507 warnings (all about lifecycle gaps in eclipse data,
  not schema issues)
- 4/4 named variants in `variants/bindings.yaml` solve cleanly
- All gaps fed back into `chore/score-schema-eclipse-comparison-update`
  in rivet — two rounds of deltas, the second one driven entirely by
  this corpus oracle.

See [`tools/falsification-journey.md`](tools/falsification-journey.md)
for the path from "naïve conversion = 1476 errors" to "PASS."

## Reproducibility — `rivet externals` pins every upstream

The fork uses rivet's own `externals:` machinery (see `rivet docs cross-repo`)
to pin all 58 upstream eclipse-score repos by exact commit SHA. The
authoritative pin source is the `externals:` block at the bottom of
`rivet.yaml` plus the generated `rivet.lock`. Anyone with a checkout
and internet access can materialise the exact corpus state this fork
was validated against:

```sh
git clone <fork-url>
cd eclipse-score-fork
make sync         # rivet sync + create upstream/ symlinks
make convert      # run the RST→YAML converter
make validate     # mechanical oracle: PASS (2507 warnings)
```

The 58 upstream clones land under `.rivet/repos/<short-name>/` (rivet-
managed cache, gitignored). The Makefile creates `upstream/eclipse-score-<X>/`
symlinks pointing at them so the converter's paths stay readable.

## Rebase / reconvert workflow

Once a quarter (or whenever upstream cuts a release):

```sh
# 1. Pull each upstream repo to its remote HEAD.
make rebase                                 # equivalent to:
git -C upstream/eclipse-score-score fetch origin
git -C upstream/eclipse-score-score merge --ff-only origin/main
# …repeat for the other 57. Or write the new SHAs into rivet.yaml
# directly and re-run `make sync`.

# 2. Write the new HEADs back into the pin file.
make update-pins                            # rivet lock --update

# 3. Re-run the converter against the new RST.
make convert

# 4. Mechanical oracle — should still pass.
make validate

# 4. If it does NOT pass, the corpus oracle just falsified our schema or
#    converter against new upstream content. The failure modes are the
#    interesting data — they tell us either:
#      • eclipse added a new need type / link / option we don't cover
#        (→ schema delta in rivet/schemas/score.yaml)
#      • eclipse changed an existing predicate's semantic / target type
#        (→ converter mapping update in tools/score_import.py)
#      • eclipse fixed something we were working around
#        (→ remove the workaround)
#    Land the fix in rivet (PR against schemas/score.yaml) and/or in this
#    repo's tools/, re-run, commit a new snapshot.
```

## Schema sourcing

`vendor/rivet-schemas/` is a pinned copy of `rivet/schemas/` at the SHA
that this workspace was last validated against. It's vendored so:

1. This workspace is self-contained — `make validate` works without
   needing a local `pulseengine/rivet` checkout at a specific branch.
2. The pinning protects the corpus oracle from being silently invalidated
   by upstream rivet schema changes.

The current pin came from rivet branch
`chore/score-schema-eclipse-comparison-update` (commits `64e9bc5` +
`4a2890f`). To refresh from a newer rivet:

```sh
cp /Users/r/git/pulseengine/rivet/schemas/*.yaml vendor/rivet-schemas/
make validate                             # confirm corpus still goes green
```

## Why this is a fork and not a mirror

We deliberately **do not** mirror upstream RST into the rivet
artifacts — that would create a second source of truth that drifts.
Instead:

- `upstream/` stays a verbatim clone of eclipse-score, ready to rebase.
- `rivet/` holds *generated* artifacts that are regenerated on every
  `make convert`. Hand-edits will be overwritten.
- The fork's value is the **converter + schema delta + falsification
  record**, all of which live in this repo's overlay (`tools/`,
  `vendor/`, the per-repo `rivet.yaml` files, this README).

This means upstream can adopt none of this and the fork still serves its
purpose: it's our binary evidence that rivet's typed traceability
covers eclipse-score-scale work.

## Coverage reports

Each per-repo conversion emits a `coverage.md` report at
`rivet/<repo>/coverage.md` listing:

- RST files scanned
- Needs converted
- Needs skipped (with reason: unknown type, no id, template placeholder)
- Unknown option keys encountered (stashed as raw fields)
- Per-rivet-type counts

The reports are the falsification surface — any non-zero "skipped" line
is a discrete gap that can be closed by a schema delta or a converter
mapping. The current numbers (run `make convert` to refresh):

**Headline** (all 58 active non-archived eclipse-score repos, excluding 3
external forks `nlohmann_json` / `bazel_registry_ui` / `rules_rust`):

| Stat | Value |
|---|---:|
| Upstream repos forked | 58 |
| RST files scanned | 919 |
| Sphinx-needs needs converted | **2985** |
| Repos with at least one need | 14 |
| Repos with zero needs (toolchain / CI / pure Doxygen) | 44 |
| Unknown eclipse need types | 0 |
| Unknown option keys | 7 |
| `needextend` rules processed | 114 |
| `needextend` mutations baked into artifacts | **2504** |
| Markdown documents emitted (alongside YAML) | **634** |
| Feature-model dimensions captured (safety / security / req-type / process-area / standard / component) | 6 |
| Named variants in `variants/bindings.yaml` | 4 |
| `rivet variant check-all` | **4/4 PASS** |
| `rivet validate` errors | **0** |
| `rivet validate` warnings (all lifecycle gaps in eclipse data) | 2507 |

**Per-repo (top 14 by need count):**

| Repo | RST files | Needs converted |
|---|---:|---:|
| eclipse-score-score | 404 | 1373 |
| eclipse-score-process-description | 299 | 1257 |
| eclipse-score-baselibs_rust | 21 | 76 |
| eclipse-score-module_template | 39 | 65 |
| eclipse-score-persistency | 30 | 61 |
| eclipse-score-docs-as-code | 24 | 61 |
| eclipse-score-inc_security_crypto | 10 | 38 |
| eclipse-score-lifecycle | 19 | 28 |
| eclipse-score-inc_someip_gateway | 14 | 12 |
| eclipse-score-baselibs | 5 | 9 |
| eclipse-score-reference_integration | 3 | 2 |
| eclipse-score-score-crates | 1 | 1 |
| eclipse-score-logging | 2 | 1 |
| eclipse-score-inc_os_autosd | 1 | 1 |

The remaining 44 repos report 0 needs — legitimate, not converter misses.
They split into:

- **Pure Doxygen docs** (eclipse-score-communication, feo, kyron,
  orchestrator, …) — eclipse uses sphinx-needs for *requirements* and
  Doxygen for *API reference*. These repos contain only the latter.
- **Bazel toolchain / CI infrastructure** (toolchains_gcc, toolchains_qnx,
  toolchains_rust, bazel_platforms, bazel-tools-*, cicd-*, etc.) — no
  requirements RST, just build rules and CI config.
- **Website / GitHub Pages** (eclipse-score-website variants,
  eclipse-score.github.io) — published site assets, no source needs.
- **Eclipse Foundation metadata** (.eclipsefdn, .github) — repo
  templates and org config.

These are kept in the corpus so cross-repo ID references that target
them resolve cleanly, and so any future addition of sphinx-needs
content lands automatically in the next `make convert`.

## Sphinx-needs feature parity

The converter resolves three operational features beyond directive-only
extraction:

### `needextend` resolution (baked into artifacts)

Eclipse uses sphinx-needs' `.. needextend::` directive as a write-time
DRY shortcut to bulk-tag needs by file-path filter (e.g. "every need
declared under `process_areas/safety_analysis/` also gets `+tags:
safety_analysis`"). 114 such rules across the upstream corpus produce
2504 tag/`belongs_to` mutations on the converted artifacts. The
converter resolves the filter expressions at conversion time and bakes
the mutations into the static YAML — so `rivet coverage --tag iso26262`
queries match what eclipse's `needpie` shows.

Supported filter shapes (covers all 114 occurrences):
- `docname is not None and "<path>" in docname`
- `"<sub>" in id`
- `c.this_doc()`
- combinations with `and type == "<X>"` and `and not status`

Mutation keys supported: `+tags`, `+belongs_to` (the only two eclipse
actually uses).

### Markdown documents (alongside YAML)

For every RST file containing at least one need directive, the
converter emits a parallel markdown file under
`rivet/<repo>/docs/<same-path>.md`. Section structure is preserved
(`#` for RST `#` / `*` underlines, `##` for `=`, `###` for `-`),
need directives become `### {title}` headings followed by an
`{{artifact:ID:status,safety-level,security}}` embed, and inline
sphinx-needs `:need:`X`` roles are rewritten to rivet's `[[X]]`
syntax. 634 documents in total.

Rivet's `rivet serve` dashboard picks them up via the `docs:` block
in each per-repo `rivet.yaml`, and `rivet export --format html`
includes them in the static compliance bundle.

### Compliance rendering — rivet's existing surface

Eclipse uses `.. needtable::` and `.. needpie::` directives to embed
filtered tables and coverage pies directly in their RST docs. Rivet's
equivalents already exist and need no converter changes:

- `{{coverage}}` / `{{coverage:rule-name}}` → coverage bars per rule
- `{{matrix}}` / `{{matrix:source:target}}` → traceability matrices
- `{{table:TYPE:FIELDS}}` → filtered tables of artifacts by type
- `{{stats}}` / `{{stats:types}}` / `{{stats:status}}` → metrics
- `/api/v1/{stats,coverage,artifacts,diagnostics}` → Grafana JSON API
  with permissive CORS (`FEAT-073`)
- `rivet export --format html` → 11+ self-contained pages including
  `matrix.html`, `coverage.html`, `validation.html`

Authors who want eclipse-style "tables and pies in the doc" should
use these built-in rivet embeds inside the emitted markdown.

## Variant / feature-model handling

Eclipse-score declares variant management as a stakeholder requirement:

```rst
.. stkh_req:: Variant management
   :id: stkh_req__overall_goals__variant_management
   :rationale: tbd
   :status: valid

   The SW-platform shall provide variant management support.
   ...
```

But ships **no metamodel construct for variants** — no `variant` need
type, no `:variant:` option, no binding file format. The `:rationale:
tbd` is explicit acknowledgement that this requirement is unsolved
upstream.

This fork fills the gap using rivet's existing product-line-engineering
machinery (`rivet variant ...`, see `rivet docs schemas-overview`).
The `variants/` directory holds:

- `feature-model.yaml` — declares the variant axes already implicit in
  eclipse's data: safety-classification (qm / asil-a..d), security
  (yes/no), requirement-category (functional / non-functional /
  interface / process), process-area (15 areas, or-group),
  standards-compliance (iso26262 / iso-sae-21434 / aspice-40, or-group),
  components (one leaf per upstream repo with needs, or-group). Plus
  attribute-schema for typed attributes (asil-numeric, iso-clauses,
  std-id, upstream-repo).
- `bindings.yaml` — maps features to representative artifacts + source
  globs, and declares 4 named variants demonstrating realistic build
  configurations.

Validate the model + all named variants:

```sh
$ make variant-check
PASS  persistency-qm
PASS  persistency-asil-b-secure
PASS  platform-only
PASS  aspice-assessment
4/4 variants passed (0 failed)
```

Emit a GitHub Actions CI matrix from the named variants:

```sh
$ make variant-matrix
matrix:
  include:
    - variant: persistency-asil-b-secure
      features: "asil-b,components,iso-sae-21434,iso26262,persistency,..."
      runner: ubuntu-latest
    - ...
```

The named variants serve as worked starter examples; real consumers
add their own `variants:` entries naming the build configuration they
ship. Constraints in the feature model enforce eclipse's metamodel
graph_checks (e.g. ASIL-B implies ISO 26262 compliance, security-
required implies ISO/SAE 21434).

**What this demonstrates**: rivet's variant subsystem (REQ-085, FEAT-106
through FEAT-114) is the solved-form answer to eclipse-score's open
stakeholder requirement. Pulseengine doesn't just round-trip eclipse's
existing data — it offers a model for the part of eclipse's process
that's currently TBD.

## Archived repos

16 eclipse-score repos marked `archived: true` on GitHub are *excluded*
from the fork by user policy (see commit messages). The skip list (in
`tools/score_import.py`'s clone block, run manually) is:

`examples, inc_abi_compatible_datatypes, inc_ai_platform,
inc_config_management, inc_feo, inc_gen_ai, inc_json, inc_mw_com,
inc_mw_log, inc_process_test_management, inc_process_variant_management,
inc_score_codegen, operating_system, test_integration, test_module_a,
test_module_b`
