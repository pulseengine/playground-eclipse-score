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

| Repo | RST files | Needs converted | Unknown types | Unknown options |
|---|---:|---:|---:|---:|
| eclipse-score-score | 404 | 1373 | 0 | 4 |
| eclipse-score-process-description | 299 | 1257 | 0 | 3 |
| eclipse-score-persistency | 30 | 61 | 0 | 0 |
| eclipse-score-docs-as-code | 24 | 61 | 0 | 0 |
| **Total** | **757** | **2752** | **0** | **7** |
