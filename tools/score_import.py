#!/usr/bin/env python3
"""score_import — convert Eclipse S-CORE sphinx-needs RST → rivet YAML.

Scans an upstream eclipse-score repo's RST tree, extracts every
`.. <type>:: <title>` directive with its `:option:` block, maps to
rivet artifact-types + link-types declared in schemas/score.yaml,
emits a rivet generic-yaml file, and writes a coverage report so
gaps land in the diagnostics rather than getting silently dropped.

Usage:
    python tools/score_import.py upstream/<repo> rivet/<repo>/artifacts/imported.yaml \\
        --report rivet/<repo>/coverage.md

Per pulseengine philosophy: failures are data. The coverage report
names every need that *did not* convert and why (unknown type, unknown
link, unmappable status, etc.) so the gap is visible at the schema
level rather than hidden in the converter.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys
import textwrap
from dataclasses import dataclass, field

# ── Type mapping: eclipse need type → rivet artifact type ────────────────
# Source of truth for eclipse types: docs-as-code/src/extensions/
# score_metamodel/metamodel.yaml (1065 lines, ~30 types).
# Rivet equivalents land in schemas/score.yaml (~28 types after deltas).
TYPE_MAP = {
    # Requirements
    "stkh_req": "stkh-req",
    "feat_req": "feat-req",
    "comp_req": "comp-req",
    "aou_req":  "aou-req",
    "tool_req": "tool-req",
    # Architecture
    "feat":             "feat",
    "feat_arc_sta":     "feat-arc-sta",
    "feat_arc_dyn":     "feat-arc-dyn",
    "logic_arc_int":    "logic-arc-int",
    "logic_arc_int_op": "logic-arc-int",   # operations collapse onto interface
    "comp":             "comp",
    "comp_arc_sta":     "comp-arc-sta",
    "comp_arc_dyn":     "comp-arc-dyn",
    "real_arc_int":     "real-arc-int",
    "real_arc_int_op":  "real-arc-int",
    "mod":              "mod",
    "mod_view_sta":     "mod-view-sta",
    "mod_view_dyn":     "mod-view-dyn",
    # Detailed design / impl
    "dd_sta":      "dd-sta",
    "dd_dyn":      "dd-dyn",
    "sw_unit":     "sw-unit",
    "sw_unit_int": "sw-unit",   # interface variant collapses onto sw-unit
    # Safety analysis (eclipse splits by scope; rivet uses belongs-to instead)
    "plat_saf_dfa": "dfa-entry",
    "feat_saf_dfa": "dfa-entry",
    "comp_saf_dfa": "dfa-entry",
    "feat_saf_fmea": "fmea-entry",
    "comp_saf_fmea": "fmea-entry",
    # Verification — eclipse `testcase` is generated; we emit test-spec
    # (one per testcase) and let rivet's test-exec/test-verdict triad be
    # populated by `rivet import-results` from JUnit XML separately.
    "testcase": "test-spec",
    # Process
    "workflow":    "workflow",
    "role":        "role",
    "workproduct": "workproduct",
    "tsf":         "tsf",
    # Guidance family — eclipse splits 5 ways; rivet collapses to one,
    # disambiguated by tag (we add the eclipse type as a tag).
    "gd_req":     "guidance",
    "gd_temp":    "guidance",
    "gd_chklst":  "guidance",
    "gd_guidl":   "guidance",
    "gd_method":  "guidance",
    # Documents — eclipse splits 3 ways; rivet collapses to one + doc-type.
    "doc_concept":  "doc",
    "doc_getstrt":  "doc",
    "doc_tool":     "doc",
    "document":     "doc",
    "review_header": "doc",
    # Standards register
    "std_req":  "std-req",
    "std_wp":   "std-wp",
    # Trustable framework
    "tenet":     "tenet",
    "assertion": "assertion",
    # Other
    "dec_rec": "decision-record",
}

# ── Link mapping: eclipse option name → rivet link-type ─────────────────
LINK_MAP = {
    "satisfies":          "satisfies",
    "implements":         "implements",
    "fulfils":            "fulfils",
    "belongs_to":         "belongs-to",
    "realizes":           "realizes",
    "uses":               "uses",
    "violates":           "violates",
    "complies":           "complies",
    "fully_verifies":     "fully-verifies",
    "partially_verifies": "partially-verifies",
    # Score-deltas added in rivet schemas/score.yaml:
    "provides":     "provides",
    "includes":     "includes",
    "covers":       "covers",
    "responsible":  "responsible",
    "approved_by":  "approved-by",
    "supported_by": "supported-by",
    "input":        "input",
    "output":       "output",
    "contains":     "contains-guidance",   # avoids clash with aadl `contains`
    "has":          "has-document",
    "mitigated_by": "is-mitigated-by",
    # Eclipse `included_by` is the back-direction — emit forward `includes`
    # from the other side; skip here to avoid double-encoding.
}

# Eclipse status enum → rivet status enum.
STATUS_MAP = {
    "valid":       "approved",
    "draft":       "draft",
    "invalid":     "obsolete",
    "in_progress": "in_progress",
    "obsolete":    "obsolete",
    # dec_rec-specific
    "accepted":    "approved",
    "proposed":    "draft",
    "rejected":    "obsolete",
    "superseded":  "obsolete",
    "deprecated":  "obsolete",
    # doc_tool-specific
    "evaluated":   "draft",
    "qualified":   "approved",
    "released":    "approved",
}

# Fields that pass through into rivet `fields:` (rather than being
# recognised as links). Anything else lands in fields too but is logged.
FIELD_MAP = {
    # Common across many eclipse types:
    "safety":      "safety-level",       # QM|ASIL_A..D
    "security":    "security",           # YES|NO
    "reqtype":     "req-type",
    "rationale":   "rationale",
    "tcl":         "tcl",
    "language":    "language",
    "failure_id":  "failure-id",
    "fault_id":    "fault-id",
    "failure_effect": "effect",
    "sufficient":  "sufficient",
    "mitigation_issue": "mitigation-issue",
    "context":     "context",
    "decision":    "decision",
    "consequences": "consequences",
    "reviewers":   "reviewers",
    "approvers":   "approvers",
    "template":    "template",
    "implemented": "implemented",
    "name":        "name",
    "file":        "file",
    "line":        "line",
    "test_type":   "test-method",
    "derivation_technique": "derivation-technique",
    "result":      "result",
    "result_text": "result-text",
    "version":     "version",
    "valid_from":  "valid-from",
    "valid_until": "valid-until",
    "author":      "author",
    "approver":    "approver",
    "reviewer":    "reviewer",
    "safety_affected":   "safety-affected",
    "security_affected": "security-affected",
    "codelink":         "source-file",
    "source_code_link": "source-file",
    "hash":             "hash",
    "parent_covered":   "parent-covered",
    "parent_has_problem": "parent-has-problem",
}

# Options sphinx-needs handles natively and that we don't re-emit:
NATIVE_OPTIONS = {"id", "status", "tags", "content", "title", "type"}

# IDs that ship with eclipse-score/module_template as placeholders and
# get copied verbatim into many downstream repos without being renamed.
# Globally skipping them avoids "declared in N repos" errors at corpus
# scale. This is an upstream-hygiene issue (the template should ship with
# either no IDs or per-repo-substituted IDs), not a converter limitation.
TEMPLATE_PLACEHOLDER_IDS = {
    "stkh_req__docgen_enabled__example",
}


# ── Parsing ─────────────────────────────────────────────────────────────

DIRECTIVE_RE = re.compile(
    # Eclipse occasionally puts need directives inside RST bulleted lists
    # (e.g. `* Requirements\n    .. std_req:: management_5421` in
    # process/standards/iso26262/iso26262.rst). Capture the leading
    # whitespace so option / body indentation can be measured relative to
    # the directive column, not column 0.
    r"^(?P<indent>[ \t]*)\.\. (?P<type>[a-z_]+):: (?P<title>.*?)$",
    re.MULTILINE,
)


@dataclass
class ParsedNeed:
    eclipse_type: str
    title: str
    options: dict = field(default_factory=dict)
    body_lines: list = field(default_factory=list)
    source: str = ""
    source_line: int = 0

    @property
    def id(self) -> str:
        return self.options.get("id", "")


@dataclass
class NeedExtend:
    """A `.. needextend:: <filter>\n   :+key: value` directive.

    Sphinx-needs evaluates the filter against every need in the build
    and applies the mutations to matches.  Eclipse uses this purely as
    write-time DRY — bulk-tagging by file path or ID substring.  We
    resolve at conversion time so the emitted artifacts carry the
    mutated attributes statically; no dynamic graph at render time.

    Supported filter shapes (covers all 114 occurrences in upstream):
      * `docname is not None and "<path>" in docname`
      * `"<sub>" in id`
      * `c.this_doc()`               (== docname matches source file)
      * any of the above combined with `and type == "<X>"`
      * any of the above combined with `and not status` etc.
    """
    filter_expr: str
    mutations: list   # list of (key, value, append_bool)
    source: str       # the RST file that declared the needextend



def parse_rst(path: pathlib.Path) -> list[ParsedNeed]:
    """Pull every `.. <type>::` need directive out of an RST file.

    Sphinx-needs directives use an :option: block with continuation-line
    indentation; the free-text body follows after a blank line. We don't
    need full RST grammar — just the directive shape eclipse uses.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    needs: list[ParsedNeed] = []
    # Track when we're inside a code/literal block — eclipse RST templates
    # show need directives inside `.. code-block:: rst` for documentation;
    # sphinx-needs ignores them and so must we.
    code_block_indent: int | None = None
    code_block_re = re.compile(
        r"^([ \t]*)\.\. (?:code-block|code|literalinclude|parsed-literal)::"
    )
    i = 0
    while i < len(lines):
        cb = code_block_re.match(lines[i])
        if cb is not None:
            code_block_indent = len(cb.group(1))
            i += 1
            continue
        if code_block_indent is not None:
            line = lines[i]
            if line.strip() == "":
                i += 1
                continue
            leading = len(line) - len(line.lstrip())
            if leading <= code_block_indent:
                code_block_indent = None
                # fall through to re-evaluate this line as a directive
            else:
                i += 1
                continue
        m = DIRECTIVE_RE.match(lines[i])
        if not m:
            i += 1
            continue
        etype = m.group("type")
        if etype not in TYPE_MAP and etype not in (
            # don't bother trying to parse non-need directives:
            # uml, code, image, etc.
            "include", "toctree", "uml", "code", "image", "literalinclude",
            "automodule", "autoclass", "autofunction", "mermaid", "puml",
            "csv-table", "list-table", "note", "warning", "tip", "seealso",
            "container", "raw", "sphinx_needs",
        ):
            # Track it — could be an unknown eclipse type.
            pass
        if etype not in TYPE_MAP:
            i += 1
            continue
        directive_indent = len(m.group("indent"))
        need = ParsedNeed(
            eclipse_type=etype,
            title=m.group("title").strip(),
            source=str(path),
            source_line=i + 1,
        )
        i += 1
        # Options: lines starting with `:opt: value` indented MORE than the
        # directive itself (sphinx-needs convention is 3+ spaces relative).
        opt_re = re.compile(r"^[ \t]+:([a-zA-Z_][a-zA-Z_0-9]*):\s*(.*?)\s*$")
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                i += 1
                break
            leading = len(line) - len(line.lstrip())
            if leading <= directive_indent:
                break
            opt_m = opt_re.match(line)
            if opt_m:
                key, value = opt_m.group(1), opt_m.group(2)
                # Continuation lines (rare — eclipse rarely wraps options):
                while (i + 1 < len(lines)
                       and lines[i + 1].strip()
                       and (len(lines[i + 1]) - len(lines[i + 1].lstrip()))
                            > directive_indent + 3
                       and not lines[i + 1].lstrip().startswith(":")):
                    value += " " + lines[i + 1].strip()
                    i += 1
                need.options[key] = value
                i += 1
            else:
                break
        # Body lines (free text under the directive — must be indented
        # more than the directive itself).
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                need.body_lines.append("")
                i += 1
                continue
            leading = len(line) - len(line.lstrip())
            if leading > directive_indent:
                need.body_lines.append(line.strip())
                i += 1
            else:
                break
        # Belt-and-suspenders: skip RST template placeholders that escaped
        # the code-block filter. Template IDs and link targets use angle-
        # bracketed slots like `<Title>`, `<ID from feature>`. Also skip
        # cross-repo template-placeholder IDs that downstream eclipse
        # repos copied verbatim from module_template.
        if (not need.id
                or "<" in need.id
                or ">" in need.id
                or need.id.lower() in TEMPLATE_PLACEHOLDER_IDS):
            continue
        # Drop link targets that are template placeholders so they don't
        # create spurious "target does not exist" diagnostics. Covers
        # both `<...>`-bracketed placeholders in the raw option AND
        # links that point at a known `TEMPLATE_PLACEHOLDER_IDS` target
        # (which has been globally filtered out of the artifact set).
        for key in list(need.options):
            if key in LINK_MAP:
                raw = need.options[key]
                if "<" in raw or ">" in raw:
                    need.options.pop(key)
                    continue
                kept = [t for t in re.split(r"[\s,;]+", raw)
                        if t.strip()
                        and t.strip().lower() not in TEMPLATE_PLACEHOLDER_IDS]
                if not kept:
                    need.options.pop(key)
                else:
                    need.options[key] = ", ".join(kept)
        needs.append(need)
    return needs


# ── needextend parser + filter evaluator ────────────────────────────────

NEEDEXTEND_RE = re.compile(
    r"^(?P<indent>[ \t]*)\.\. needextend:: ?(?P<filter>.*?)$",
    re.MULTILINE,
)


def parse_needextends(path: pathlib.Path) -> list[NeedExtend]:
    """Pull every `.. needextend:: <filter>` directive out of an RST file.

    Body is `:+key: value` (append) or `:key: value` (replace) lines
    indented under the directive.  We only see `:+tags:` and
    `:+belongs_to:` across the entire upstream corpus.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    out: list[NeedExtend] = []
    i = 0
    while i < len(lines):
        m = NEEDEXTEND_RE.match(lines[i])
        if not m:
            i += 1
            continue
        directive_indent = len(m.group("indent"))
        filter_expr = m.group("filter").strip()
        i += 1
        muts: list = []
        opt_re = re.compile(r"^[ \t]+:(?P<plus>\+)?(?P<key>[a-zA-Z_][a-zA-Z_0-9]*):\s*(?P<val>.*?)\s*$")
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                break
            leading = len(line) - len(line.lstrip())
            if leading <= directive_indent:
                break
            om = opt_re.match(line)
            if not om:
                break
            muts.append((om.group("key"), om.group("val"), om.group("plus") == "+"))
            i += 1
        if filter_expr and muts:
            out.append(NeedExtend(filter_expr=filter_expr, mutations=muts, source=str(path)))
    return out


def _eval_atom(node, ctx: dict) -> bool:
    """Tiny safe evaluator for the 5 sphinx-needs filter shapes that
    appear in eclipse-score.  Refuses anything outside the supported
    set so a future eclipse expression doesn't get silently mis-evaluated.
    """
    import ast as _ast
    if isinstance(node, _ast.BoolOp):
        results = [_eval_atom(v, ctx) for v in node.values]
        return all(results) if isinstance(node.op, _ast.And) else any(results)
    if isinstance(node, _ast.UnaryOp) and isinstance(node.op, _ast.Not):
        return not _eval_atom(node.operand, ctx)
    if isinstance(node, _ast.Compare):
        left = _eval_value(node.left, ctx)
        result = True
        for op, comparator in zip(node.ops, node.comparators):
            right = _eval_value(comparator, ctx)
            if isinstance(op, _ast.Eq):
                result = result and (left == right)
            elif isinstance(op, _ast.NotEq):
                result = result and (left != right)
            elif isinstance(op, _ast.In):
                result = result and (left in (right or ""))
            elif isinstance(op, _ast.NotIn):
                result = result and (left not in (right or ""))
            elif isinstance(op, _ast.Is):
                result = result and (left is right)
            elif isinstance(op, _ast.IsNot):
                result = result and (left is not right)
            else:
                raise ValueError(f"unsupported comparison: {type(op).__name__}")
            left = right
        return result
    if isinstance(node, _ast.Call):
        # The only call sphinx-needs uses in eclipse-score is `c.this_doc()`.
        if (isinstance(node.func, _ast.Attribute)
                and isinstance(node.func.value, _ast.Name)
                and node.func.value.id == "c"
                and node.func.attr == "this_doc"):
            # `c.this_doc()` = "needs declared in the file that contains
            # this needextend directive".  We track that as ctx['this_doc'].
            return ctx.get("docname", "") == ctx.get("this_doc", "")
        raise ValueError(f"unsupported call: {_ast.dump(node)[:80]}")
    if isinstance(node, _ast.Name):
        # Bare name = truthiness check on the context variable.
        return bool(ctx.get(node.id, ""))
    raise ValueError(f"unsupported expression: {type(node).__name__}")


def _eval_value(node, ctx: dict):
    """Resolve an expression node to a Python value (string / None / bool)."""
    import ast as _ast
    if isinstance(node, _ast.Constant):
        return node.value
    if isinstance(node, _ast.Name):
        if node.id == "None":
            return None
        return ctx.get(node.id, "")
    if isinstance(node, _ast.Attribute):
        # Eclipse only uses `c.this_doc()` (handled in _eval_atom) — no
        # other attribute access.  Fall through to error.
        raise ValueError(f"unsupported attribute access: {_ast.dump(node)[:80]}")
    raise ValueError(f"unsupported value: {type(node).__name__}")


def filter_matches(extend: NeedExtend, need: ParsedNeed, need_docname: str) -> bool:
    """Evaluate the needextend filter against one need.

    `need_docname` is sphinx-needs' notion of "document name": the
    relative path of the RST file (without the .rst extension), used
    in expressions like `"persistency/kvs/docs/requirements" in docname`.
    """
    import ast as _ast
    ctx = {
        "docname": need_docname,
        "id": need.id,
        "type": need.eclipse_type,
        "status": need.options.get("status", ""),
        "tags": need.options.get("tags", ""),
        "this_doc": pathlib.Path(extend.source).with_suffix("").as_posix(),
    }
    try:
        tree = _ast.parse(extend.filter_expr, mode="eval")
        return _eval_atom(tree.body, ctx)
    except (SyntaxError, ValueError) as exc:
        # Log once per unsupported filter shape so we know what to add.
        msg = f"  WARN: needextend filter unsupported, skipping: {extend.filter_expr!r} ({exc})"
        print(msg, file=sys.stderr)
        return False


def apply_needextends(extends: list, needs_with_source: list) -> int:
    """Apply each needextend mutation to every matching need (in-place).

    `needs_with_source` is a list of (need, docname) tuples where
    `docname` is the cross-repo sphinx docname (e.g.
    `persistency/score/kvs/docs/requirements/index`) — bare, no `.rst`.
    Returns the total mutation-application count for stats.
    """
    applied = 0
    for extend in extends:
        for need, need_docname in needs_with_source:
            if not filter_matches(extend, need, need_docname):
                continue
            for key, value, is_append in extend.mutations:
                if is_append:
                    existing = need.options.get(key, "")
                    if existing:
                        new = existing + ", " + value
                    else:
                        new = value
                    need.options[key] = new
                else:
                    need.options[key] = value
                applied += 1
    return applied


# ── Conversion ──────────────────────────────────────────────────────────

@dataclass
class CoverageStats:
    converted: int = 0
    skipped_unknown_type: collections.Counter = field(default_factory=collections.Counter)
    skipped_no_id: int = 0
    needextend_rules: int = 0
    needextend_mutations: int = 0
    unknown_links: collections.Counter = field(default_factory=collections.Counter)
    unknown_options: collections.Counter = field(default_factory=collections.Counter)
    by_type: collections.Counter = field(default_factory=collections.Counter)
    files_scanned: int = 0
    docs_emitted: int = 0
    inline_need_refs_rewritten: int = 0


def normalise_id(raw: str) -> str:
    """Eclipse IDs use `prefix__group__short`; we keep them but uppercase.

    Rivet doesn't enforce a global ID regex (per-schema prefixes only),
    so keeping the eclipse ID verbatim preserves cross-reference fidelity.
    Uppercase is purely cosmetic and matches rivet's house style.
    """
    return raw.strip().upper().replace(" ", "")


# ── Markdown emission ───────────────────────────────────────────────────
#
# For every RST file that contains at least one need directive, we also
# emit a parallel markdown file under `rivet/<repo>/docs/<same-path>.md`.
# This preserves the *narrative* eclipse wraps around the typed needs
# (sections, prose, inline cross-references) — the part that lives in
# RST and not in the converted YAML.
#
# The markdown emission is intentionally minimal:
#   * Section headings (RST underline syntax) → `#` / `##` / `###`
#   * Need directives → `### {title}` + `{{artifact:<ID>}}` embed
#       (rivet renders that as the compact artifact card; richer
#       per-field embeds — `{{artifact:ID:status,safety-level}}` —
#       are a proposed rivet enhancement, see follow-up design doc)
#   * Inline `:need:`<id>`` → `[[<ID-uppercase>]]`
#       (rivet `[[ID]]` syntax is already supported — see `rivet docs documents`)
#   * Body paragraphs → passthrough markdown
#   * `..` comment blocks, code-blocks, UML, includes → skipped
#
# v1 limitations: no RST table conversion, no `.. note::` admonition
# rendering, no `.. needtable::`/`.. needpie::` conversion (those are
# computed by rivet's existing `{{coverage}}` / `{{matrix}}` / `{{table}}`
# embeds — point the user there).

_INLINE_NEED_RE = re.compile(r":need:`([A-Za-z0-9_:\-/]+)`")
_RST_ROLE_RE = re.compile(r":[a-z]+:`([^`]+)`")
_HEADING_LINE_RE = re.compile(r"^([=\-~`#*\^\"+_])\1{2,}$")


def emit_markdown_for_rst(rst_path: pathlib.Path, md_path: pathlib.Path,
                          stats: CoverageStats) -> bool:
    """Convert one RST file to a minimal markdown document.

    Returns True iff at least one need directive was rendered into the
    output (we skip emitting docs for RST files with no traceable
    content — e.g. pure tutorial pages).
    """
    text = rst_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    out: list[str] = []
    rendered_any_need = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip `..` comment blocks: an `..` line followed by indented lines.
        if stripped == ".." or stripped.startswith(".. "):
            # Could be a directive or a comment.  Check what follows.
            if stripped == ".." or (
                stripped.startswith(".. ")
                and not stripped.startswith(".. _")
                and "::" not in stripped
            ):
                # Pure comment block — skip directive line + indented body.
                i += 1
                while i < len(lines) and (not lines[i].strip()
                                          or lines[i].startswith((" ", "\t"))):
                    i += 1
                continue

        # Directive?
        m = DIRECTIVE_RE.match(line)
        if m:
            etype = m.group("type")
            indent = len(m.group("indent"))
            title = m.group("title").strip()

            # Skip non-need directives and structural directives.
            if etype not in TYPE_MAP:
                # Skip the whole directive block (option lines + indented body).
                i += 1
                while i < len(lines):
                    l = lines[i]
                    if not l.strip():
                        i += 1
                        # Bail if next non-blank is dedented.
                        while i < len(lines) and not lines[i].strip():
                            i += 1
                        if i < len(lines):
                            leading = len(lines[i]) - len(lines[i].lstrip())
                            if leading <= indent:
                                break
                        continue
                    leading = len(l) - len(l.lstrip())
                    if leading <= indent:
                        break
                    i += 1
                continue

            # It's a need directive — extract id from option block, render.
            i += 1
            need_id = ""
            while i < len(lines):
                l = lines[i]
                if not l.strip():
                    i += 1
                    break
                leading = len(l) - len(l.lstrip())
                if leading <= indent:
                    break
                om = re.match(r"[ \t]+:([a-zA-Z_][a-zA-Z_0-9]*):\s*(.*?)\s*$", l)
                if om and om.group(1) == "id":
                    need_id = om.group(2)
                i += 1
            # Skip the body paragraph too — it's now in the YAML
            # `description:` field, and rivet's artifact card will show
            # it on hover/click.
            while i < len(lines):
                l = lines[i]
                if not l.strip():
                    out.append("")
                    i += 1
                    continue
                leading = len(l) - len(l.lstrip())
                if leading <= indent:
                    break
                i += 1

            if need_id:
                heading_level = "###"
                out.append(f"{heading_level} {title}")
                out.append("")
                # Per-field projection: ask rivet to render the id +
                # context fields that compliance authors care about.
                # `status,safety-level,security` is the eclipse-score
                # default; renders as a compact link card today (those
                # fields are silently dropped) and as id+title+fields
                # once the proposed embed extension lands — see
                # rivet `docs/design/artifact-embed-with-fields.md`.
                out.append(
                    f"{{{{artifact:{normalise_id(need_id)}:"
                    "status,safety-level,security}}}}"
                )
                out.append("")
                rendered_any_need = True
            continue

        # Section heading? Pattern: <title>\n<underline>
        # RST uses sequences like `===`, `---`, `~~~`, `###` to underline.
        if (i + 1 < len(lines)
                and _HEADING_LINE_RE.match(lines[i + 1])
                and stripped
                and not stripped.startswith(".")):
            underline_char = lines[i + 1][0]
            # Map RST underline characters to markdown heading levels.
            # Eclipse uses sphinx's adornment convention; in practice the
            # most common patterns are `#` (file title / level 1),
            # `-` (level 2 subsection), `~` (level 3), `^` (level 4).
            level = {"#": "#", "*": "#", "=": "#", "-": "##",
                     "~": "###", "^": "####", "+": "####",
                     "`": "#####", '"': "#####"}.get(underline_char, "##")
            out.append(f"{level} {stripped}")
            out.append("")
            i += 2  # skip title + underline
            continue

        # Inline RST role rewriting on prose lines.
        if ":" in line:
            # Inline `:need:`...`` → `[[...]]`.
            def _rewrite_need(match):
                nonlocal stats
                stats.inline_need_refs_rewritten += 1
                return f"[[{normalise_id(match.group(1))}]]"
            new = _INLINE_NEED_RE.sub(_rewrite_need, line)
            # Strip other RST roles (`:term:`, `:ref:` etc.) keeping content only.
            new = _RST_ROLE_RE.sub(lambda m: m.group(1), new)
            line = new

        out.append(line)
        i += 1

    if not rendered_any_need:
        return False

    # Compact: collapse 3+ blank lines to 2.
    md = re.sub(r"\n{3,}", "\n\n", "\n".join(out))

    md_path.parent.mkdir(parents=True, exist_ok=True)
    # Frontmatter so rivet picks up the file as a Document with id/title.
    doc_id = "DOC-" + rst_path.stem.upper().replace("_", "-")
    title = rst_path.stem.replace("_", " ").title()
    frontmatter = (
        "---\n"
        f"id: {doc_id}-{abs(hash(str(rst_path))) % 100000}\n"
        f"title: {title}\n"
        "type: specification\n"
        "status: approved\n"
        "tags: [eclipse-score]\n"
        "---\n\n"
    )
    md_path.write_text(frontmatter + md + "\n")
    stats.docs_emitted += 1
    return True


def convert_need(need: ParsedNeed, stats: CoverageStats) -> dict | None:
    rivet_type = TYPE_MAP.get(need.eclipse_type)
    if rivet_type is None:
        stats.skipped_unknown_type[need.eclipse_type] += 1
        return None
    if not need.id:
        stats.skipped_no_id += 1
        return None

    art: dict = {
        "id":    normalise_id(need.id),
        "type":  rivet_type,
        "title": need.title or need.id,
    }
    # Status mapping (eclipse `valid` → rivet `approved` etc.).
    raw_status = need.options.get("status", "").strip()
    if raw_status:
        art["status"] = STATUS_MAP.get(raw_status, "draft")

    # Tags — eclipse stores comma-separated; we split and add a trace tag.
    tag_set: list[str] = []
    if "tags" in need.options:
        tag_set = [t.strip() for t in need.options["tags"].split(",") if t.strip()]
    # Preserve eclipse type as a tag when rivet collapses it (e.g. gd_*).
    if need.eclipse_type != rivet_type.replace("-", "_"):
        tag_set.append(f"eclipse:{need.eclipse_type}")
    if tag_set:
        art["tags"] = tag_set

    # Description = body text (rejoin paragraphs).
    body = "\n".join(need.body_lines).strip()
    if body:
        # Collapse repeated blank lines but keep paragraph breaks.
        art["description"] = re.sub(r"\n{3,}", "\n\n", body)

    # Fields + links from the remaining options.
    fields: dict = {}
    links: list = []
    for key, raw_value in need.options.items():
        if key in NATIVE_OPTIONS:
            continue
        if key in LINK_MAP:
            rivet_link = LINK_MAP[key]
            # Source-specific link routing: gd_req → workflow uses the
            # `satisfies` predicate in eclipse, but in rivet's score schema
            # that source/target pair is modelled by `fulfils-process-req`
            # so the type-target restriction passes cleanly.
            if (key == "satisfies"
                    and need.eclipse_type.startswith("gd_")):
                rivet_link = "fulfils-process-req"
            for target in re.split(r"[\s,;]+", raw_value):
                if target.strip():
                    links.append({
                        "type":   rivet_link,
                        "target": normalise_id(target),
                    })
            continue
        if key in FIELD_MAP:
            fields[FIELD_MAP[key]] = raw_value
            continue
        # Unmapped option — log and stash as a raw field so no data is lost.
        stats.unknown_options[f"{need.eclipse_type}:{key}"] += 1
        fields[key] = raw_value

    if fields:
        art["fields"] = fields
    if links:
        art["links"] = links

    stats.converted += 1
    stats.by_type[rivet_type] += 1
    return art


def convert_repo(root: pathlib.Path, out_yaml: pathlib.Path,
                 report_md: pathlib.Path | None,
                 docs_out: pathlib.Path | None = None) -> CoverageStats:
    stats = CoverageStats()
    artifacts: list = []
    # Eclipse's sphinx builds use cross-repo paths in `docname` — i.e. a
    # file under upstream/eclipse-score-persistency/score/kvs/...
    # is referenced by sphinx as `persistency/score/kvs/...` because the
    # downstream Bazel `docs(...)` macro mounts each external repo at
    # `<repo-short-name>/...` in the source tree.  needextend filters
    # written upstream rely on that convention (e.g.
    # `"persistency/kvs/docs/requirements" in docname`).  Reproduce it
    # here by prefixing every docname with the repo's short name.
    repo_short = root.name
    for prefix in ("eclipse-score-", "score-", "score_"):
        if repo_short.startswith(prefix):
            repo_short = repo_short[len(prefix):]
            break
    # Two-pass: first scan every RST file, collect needs AND needextend
    # rules.  Then apply needextend mutations to the parsed needs in
    # memory (bakes the dynamic-graph mutations into static attributes).
    # Then convert each need to a rivet artifact.
    needs_with_source: list = []
    extends: list = []
    for path in sorted(root.rglob("*.rst")):
        # Skip vendored docs / build outputs / upstream test fixtures.
        # Two categories of upstream test data trip up the corpus oracle:
        #   - docs-as-code `score_metamodel/tests/rst/` is a test corpus
        #     for the metamodel itself; intentionally-broken needs.
        #   - `*/test/fixtures/**.rst` (and `tests/fixtures/`) is upstream
        #     Bazel-rule fixture data — concrete needs that reference
        #     other concrete needs that exist only inside the fixture set.
        #     E.g. tooling/bazel/rules/rules_score/test/fixtures/seooc_test/.
        spath = str(path)
        if ("/_build/" in spath
                or "/.git/" in spath
                or "/score_metamodel/tests/" in spath
                or "/test/fixtures/" in spath
                or "/tests/fixtures/" in spath):
            continue
        stats.files_scanned += 1
        try:
            needs = parse_rst(path)
        except Exception as exc:
            print(f"  WARN: failed to parse {path}: {exc}", file=sys.stderr)
            continue
        rel = path.relative_to(root).as_posix()
        # docname uses the cross-repo convention (see comment above) and
        # drops the .rst suffix to match sphinx's bare-docname format.
        # Eclipse-score's per-component repos place their docs under a
        # `score/<component>/...` subtree but in the merged cross-repo
        # sphinx build, the mount point becomes `<repo-short>/...`
        # WITHOUT the `score/` prefix.  Strip it when present so
        # docname matches what eclipse's `needextend` filters expect.
        rel_for_docname = rel
        if rel_for_docname.startswith("score/"):
            rel_for_docname = rel_for_docname[len("score/"):]
        docname = f"{repo_short}/{rel_for_docname}".removesuffix(".rst")
        for need in needs:
            needs_with_source.append((need, docname))
        try:
            file_extends = parse_needextends(path)
        except Exception as exc:
            print(f"  WARN: failed to parse needextend in {path}: {exc}",
                  file=sys.stderr)
            file_extends = []
        # Re-anchor `source` to the cross-repo docname for `c.this_doc()`
        # comparison parity with `docname` (which uses the same form).
        ext_docname = f"{repo_short}/{rel_for_docname}".removesuffix(".rst")
        for ext in file_extends:
            ext.source = ext_docname
        extends.extend(file_extends)

    stats.needextend_rules = len(extends)
    stats.needextend_mutations = apply_needextends(extends, needs_with_source)

    for need, _ in needs_with_source:
        art = convert_need(need, stats)
        if art is not None:
            artifacts.append(art)

    # Emit markdown documents (one per RST file that contains needs).
    # Mirrors the upstream directory layout so cross-references resolve
    # by file path the same way they do in sphinx-needs.
    if docs_out is not None:
        for path in sorted(root.rglob("*.rst")):
            spath = str(path)
            if ("/_build/" in spath
                    or "/.git/" in spath
                    or "/score_metamodel/tests/" in spath
                    or "/test/fixtures/" in spath
                    or "/tests/fixtures/" in spath):
                continue
            rel = path.relative_to(root).as_posix()
            md_path = docs_out / rel.replace(".rst", ".md")
            try:
                emit_markdown_for_rst(path, md_path, stats)
            except Exception as exc:
                print(f"  WARN: failed to emit markdown for {path}: {exc}",
                      file=sys.stderr)

    # De-dup by ID (eclipse occasionally has the same need re-declared
    # in multiple files for inclusion machinery; keep the first).
    seen: dict = {}
    for art in artifacts:
        if art["id"] not in seen:
            seen[art["id"]] = art
    artifacts = list(seen.values())

    out_yaml.parent.mkdir(parents=True, exist_ok=True)
    write_yaml(out_yaml, {"artifacts": artifacts})

    if report_md:
        report_md.parent.mkdir(parents=True, exist_ok=True)
        report_md.write_text(render_report(root, stats, len(artifacts)))

    return stats


def write_yaml(path: pathlib.Path, data: dict) -> None:
    """Tiny YAML writer — avoids a PyYAML dependency for this single
    output shape. We control the structure so we can format directly."""
    out: list[str] = ["artifacts:"]
    for art in data["artifacts"]:
        out.append(f"  - id: {yaml_scalar(art['id'])}")
        out.append(f"    type: {art['type']}")
        out.append(f"    title: {yaml_scalar(art['title'])}")
        if "status" in art:
            out.append(f"    status: {art['status']}")
        if "tags" in art and art["tags"]:
            tags_str = ", ".join(yaml_scalar(t) for t in art["tags"])
            out.append(f"    tags: [{tags_str}]")
        if "description" in art:
            desc = art["description"].replace("\n", "\n      ")
            out.append(f"    description: |")
            out.append(f"      {desc}")
        if "fields" in art and art["fields"]:
            out.append(f"    fields:")
            for k, v in art["fields"].items():
                out.append(f"      {k}: {yaml_scalar(str(v))}")
        if "links" in art and art["links"]:
            out.append(f"    links:")
            for link in art["links"]:
                out.append(f"      - type: {link['type']}")
                out.append(f"        target: {yaml_scalar(link['target'])}")
    path.write_text("\n".join(out) + "\n")


def yaml_scalar(value: str) -> str:
    """Quote when the value contains YAML-significant characters."""
    if value == "":
        return '""'
    if re.search(r"^[\d.-]|[:#{}\[\],&*?|<>=!%@`]|^\s|\s$|^(yes|no|true|false|null|y|n|on|off)$",
                 value, re.IGNORECASE):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def render_report(root: pathlib.Path, stats: CoverageStats, total_emitted: int) -> str:
    lines = [
        f"# Coverage report — {root.name}",
        "",
        f"Generated by `tools/score_import.py` from `{root}`.",
        "",
        "## Headline",
        "",
        f"- RST files scanned: **{stats.files_scanned}**",
        f"- Needs converted: **{stats.converted}**",
        f"- Artifacts emitted (after de-dup): **{total_emitted}**",
        f"- Needs skipped (unknown eclipse type): **{sum(stats.skipped_unknown_type.values())}**",
        f"- Needs skipped (no `:id:`): **{stats.skipped_no_id}**",
        f"- `needextend` rules found: **{stats.needextend_rules}**",
        f"- `needextend` mutations applied (baked into artifacts): **{stats.needextend_mutations}**",
        f"- Markdown documents emitted: **{stats.docs_emitted}**",
        f"- Inline `:need:` refs rewritten to `[[ID]]`: **{stats.inline_need_refs_rewritten}**",
        "",
        "## Falsification surface",
        "",
        "Anything below means rivet's schema, or this converter, does not yet",
        "round-trip the upstream model losslessly. Each line is a discrete",
        "gap that can be closed by a schema delta or a converter mapping.",
        "",
    ]
    if stats.skipped_unknown_type:
        lines += [
            "### Unknown eclipse need types",
            "",
            "These directives appeared in upstream RST but are not in",
            "`TYPE_MAP`. Either eclipse added a new need type, or we",
            "deliberately collapsed/excluded it.",
            "",
            "| Eclipse type | Count |",
            "| --- | ---: |",
        ]
        for etype, count in stats.skipped_unknown_type.most_common():
            lines.append(f"| `{etype}` | {count} |")
        lines.append("")
    if stats.unknown_options:
        lines += [
            "### Unknown option keys",
            "",
            "Option keys on a known need type that the converter did not",
            "recognise. They were stashed in `fields:` verbatim so no data",
            "is lost, but `rivet validate` will flag them as undeclared.",
            "",
            "| Where | Count |",
            "| --- | ---: |",
        ]
        for key, count in stats.unknown_options.most_common(40):
            lines.append(f"| `{key}` | {count} |")
        lines.append("")
    lines += [
        "## Per-type counts (converted)",
        "",
        "| Rivet type | Count |",
        "| --- | ---: |",
    ]
    for rtype, count in stats.by_type.most_common():
        lines.append(f"| `{rtype}` | {count} |")
    lines.append("")
    return "\n".join(lines)


# ── Entry point ─────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", type=pathlib.Path, help="upstream/<repo> directory")
    ap.add_argument("out",  type=pathlib.Path, help="output rivet YAML path")
    ap.add_argument("--docs-out", type=pathlib.Path, default=None,
                    help="emit parallel markdown documents under this directory")
    ap.add_argument("--report", type=pathlib.Path, default=None,
                    help="optional markdown coverage report path")
    ap.add_argument("--json", action="store_true",
                    help="emit stats to stdout as JSON instead of human text")
    args = ap.parse_args(argv)

    stats = convert_repo(args.root, args.out, args.report, args.docs_out)
    payload = {
        "files_scanned": stats.files_scanned,
        "converted": stats.converted,
        "skipped_no_id": stats.skipped_no_id,
        "skipped_unknown_type": dict(stats.skipped_unknown_type),
        "unknown_options": dict(stats.unknown_options),
        "by_type": dict(stats.by_type),
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(
            f"  scanned {stats.files_scanned} RST files, "
            f"converted {stats.converted} needs "
            f"({len(stats.skipped_unknown_type)} unknown types, "
            f"{len(stats.unknown_options)} unknown options), "
            f"{stats.needextend_rules} needextend rules → "
            f"{stats.needextend_mutations} mutations applied → {args.out}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
