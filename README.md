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
Result: PASS (2289 warnings)
```

- 2752 artifacts converted
- 0 errors, 2289 warnings (all about lifecycle gaps in eclipse data,
  not schema issues)
- All gaps fed back into `chore/score-schema-eclipse-comparison-update`
  in rivet — two rounds of deltas, the second one driven entirely by
  this corpus oracle.

See [`tools/falsification-journey.md`](tools/falsification-journey.md)
for the path from "naïve conversion = 1476 errors" to "PASS."

## Rebase / reconvert workflow

Once a quarter (or whenever upstream cuts a release):

```sh
# 1. Pull each upstream repo (origin remote points at eclipse-score org).
make rebase                                 # equivalent to:
git -C upstream/eclipse-score-score fetch origin
git -C upstream/eclipse-score-score merge --ff-only origin/main
# …repeat for the other three.

# 2. Re-run the converter against the new RST.
make convert

# 3. Mechanical oracle — should still pass.
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

## Archived repos

16 eclipse-score repos marked `archived: true` on GitHub are *excluded*
from the fork by user policy (see commit messages). The skip list (in
`tools/score_import.py`'s clone block, run manually) is:

`examples, inc_abi_compatible_datatypes, inc_ai_platform,
inc_config_management, inc_feo, inc_gen_ai, inc_json, inc_mw_com,
inc_mw_log, inc_process_test_management, inc_process_variant_management,
inc_score_codegen, operating_system, test_integration, test_module_a,
test_module_b`
