# Worked example — eclipse-score `FixVec` interface, pulseengine treatment

Eclipse-score declares the `FixVec` interface as a sphinx-needs typed-graph
of documents: one `logic_arc_int` + five `logic_arc_int_op` operations,
linked into a `comp_arc_sta` component. The actual Rust implementation
lives separately in `baselibs_rust/src/containers/inline/vec.rs` —
hand-written, with no automated connection to the interface need.

This directory shows what that same interface looks like when expressed
in the **pulseengine stack** (rivet typed artifacts + spar AADL + WIT
binary contract + Rust component). The goal is concrete demonstration,
not advocacy: every file here is the equivalent of something eclipse
already has, just expressed in a different vocabulary.

## What's the same

The data is the same. Five operations on a fixed-capacity vector:
push, pop, clear, index, iterate. Safety classification ASIL_B,
security YES. Both stacks model these as typed entities in a graph.

## What's different

The pulseengine treatment goes one step further: the AADL package
emits a WIT (WebAssembly Interface Type) file that is **link-time
enforced** by the Rust component. If the Rust implementation's
signature drifts from the declared interface, the build fails. In
eclipse's stack, the interface need and the source code are two
hand-maintained artifacts with no mechanical link — a developer can
rename `fn push` and the interface document stays unchanged.

This is the central operational difference: eclipse models the
interface as a *specification* (a document), pulseengine models it
as a *contract* (a binary obligation).

## Files

| File | What | Eclipse equivalent |
|---|---|---|
| `artifacts/fixvec.yaml` | rivet typed artifacts for the interface + 5 ops + safety classification | `logic_arc_int__b_r__fixvec` + 5× `logic_arc_int_op__cont__fixvec_*` need declarations in `baselibs_rust/docs/baselibs_rust/containers_rust/architecture/index.rst` |
| `arch/fixvec.aadl` | spar AADL package modelling the interface as a typed AADL `feature` with provider/consumer ports and ASIL property | None — eclipse has no architecture-model file; `draw_interface` walks the need-graph at sphinx-build time to produce a PlantUML diagram |
| `arch/fixvec.wit` | WIT file `spar` emits from the AADL — the binary contract | None — eclipse's interface stops at the rendered diagram |
| `rivet.yaml` | rivet project: declares schemas + sources + the cross-link namespace | per-repo eclipse `conf.py` plus the metamodel imported via `score_sphinx_bundle` |
| `Makefile` | `make validate` — rivet validates the typed artifacts and (when spar is installed) checks AADL→WIT consistency | `bazel run //:docs_check` — sphinx validates the need graph |

## Traceability — the same artifact, three forms

```
                           Eclipse                               Pulseengine
                          ─────────                             ─────────────

interface declaration      .. logic_arc_int:: Fixed-Capacity     artifacts/fixvec.yaml
                           Vector                                   id: LOGIC-ARC-INT-FIXVEC
                              :id: logic_arc_int__b_r__fixvec       type: logic-arc-int
                              :safety: ASIL_B                       fields:
                              :security: YES                          safety-level: ASIL_B
                                                                      security: "YES"

per-operation declaration  .. logic_arc_int_op:: Push             artifacts/fixvec.yaml
                              :id: ...__fixvec_push                  id: LOGIC-ARC-INT-OP-FIXVEC-PUSH
                              :included_by:                          type: logic-arc-int
                                logic_arc_int__b_r__fixvec           links:
                                                                       - type: belongs-to
                                                                         target: LOGIC-ARC-INT-FIXVEC

architecture model        none (graph IS the model)              arch/fixvec.aadl
                                                                    package FixVec public
                                                                      feature group FixVecOps
                                                                        push: provides subprogram
                                                                        ...
                                                                      properties
                                                                        ARP4761::SafetyLevel => ASIL_B;

binary contract            none                                  arch/fixvec.wit
                                                                    interface fix-vec {
                                                                      push: func(item: u32)
                                                                          -> result<_, vec-err>;
                                                                      pop:  func() -> option<u32>;
                                                                      ...
                                                                    }

implementation             baselibs_rust/src/containers/          src/lib.rs (sketch — same
                           inline/vec.rs                           shape as eclipse's vec.rs,
                              fn push(...) -> Result<...>          but link-time-checked
                              fn pop(...) -> Option<...>           against arch/fixvec.wit)
                              ...                                  via wit-bindgen
```

## Run the validation

```sh
# rivet validates the typed artifacts
rivet --schemas ../../vendor/rivet-schemas validate

# spar validates the AADL package (optional — requires spar installed)
spar validate arch/fixvec.aadl

# wit-bindgen verifies AADL→WIT consistency (optional)
spar emit --format wit arch/fixvec.aadl | diff - arch/fixvec.wit
```

When all three pass, the interface specification (rivet artifact) +
the architectural model (AADL) + the binary contract (WIT) are
provably aligned. Adding the Rust implementation behind a
`wit-bindgen`-generated trait gates the build on the same alignment.

## Why this is more than eclipse's `draw_interface`

Eclipse's `score_draw_uml_funcs.draw_interface` walks the typed need
graph and renders a PlantUML diagram. The diagram is the deliverable.

Pulseengine's spar + WIT does the same diagram render (spar can emit
PlantUML / Mermaid from the AADL model), **plus** generates the WIT
contract, **plus** has analysis passes for scheduling / latency /
ARINC 653 partitioning / EMV2 fault trees that ask
property-of-the-architecture questions the eclipse stack can only
ask via prose review.

The diagram is the same; the *gate* around the diagram is different.

## What this is *not*

- Not a working AADL build — `arch/fixvec.aadl` is a hand-written
  example. To compile it into a real WIT contract you need spar
  installed (see [`pulseengine/spar`](https://github.com/pulseengine/spar)).
- Not a complete Rust component — `arch/fixvec.wit` is the
  intended contract shape; the Rust implementation that links against
  it would live in a separate project (this example is about the
  modelling layer, not the runtime).
- Not a translation tool — the example was written by hand to
  illustrate the equivalence. A real `tools/score_to_spar.py`
  converter is future work; see the `kvs` full-stack example
  (planned) for the next step.

## What this *is*

Concrete answer to the question: *"if I took one piece of eclipse-
score's work and expressed it the way pulseengine does, what would
that look like?"* This: same interface, same operations, same safety
classification — plus an enforceable architectural model and a binary
contract the implementation has to honour. One worked example, one
page, real eclipse content as the input.
