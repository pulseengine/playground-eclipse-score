#!/usr/bin/env python3
"""regen_docs_paths.py — rewrite docs: blocks to enumerate leaf dirs.

rivet.yaml's `docs:` directive does not recurse — it loads markdown
from each listed directory at one level only. After `make convert`
emits new markdown trees under rivet/<repo>/docs/, this script
rewrites both:

  - each rivet/<repo>/rivet.yaml's `docs:` block to enumerate every
    leaf dir under <repo>/docs/ that contains .md files (paths
    relative to the per-repo rivet.yaml)
  - the top-level rivet.yaml's `docs:` block to enumerate every
    leaf dir across all repos (paths relative to the workspace root)

Idempotent. Safe to run after every `make convert`.

Usage:
    python3 tools/regen_docs_paths.py
"""
from __future__ import annotations

import pathlib
import re
import sys


WORKSPACE = pathlib.Path(__file__).resolve().parent.parent
DOCS_BLOCK_RE = re.compile(r"docs:\n(?:  - [^\n]+\n?)+")


def rewrite(yaml_path: pathlib.Path, leafs: list[str]) -> bool:
    """Replace the `docs:` block in `yaml_path` with the leaf list.

    Returns True iff the file was modified.
    """
    if not leafs:
        return False
    block = "docs:\n" + "\n".join(f"  - {d}" for d in leafs)
    text = yaml_path.read_text()
    if DOCS_BLOCK_RE.search(text):
        new = DOCS_BLOCK_RE.sub(block + "\n", text)
    else:
        new = text.rstrip() + "\n\n" + block + "\n"
    if new != text:
        yaml_path.write_text(new)
        return True
    return False


def main() -> int:
    per_repo_updated = 0
    total_per_repo_paths = 0

    for ry in sorted((WORKSPACE / "rivet").glob("eclipse-score-*/rivet.yaml")):
        repo_dir = ry.parent
        docs_dir = repo_dir / "docs"
        if not docs_dir.exists():
            continue
        leafs = sorted({
            p.parent.relative_to(repo_dir).as_posix()
            for p in docs_dir.rglob("*.md")
        })
        if rewrite(ry, leafs):
            per_repo_updated += 1
            total_per_repo_paths += len(leafs)

    # Top-level rivet.yaml — paths relative to workspace root.
    top_yaml = WORKSPACE / "rivet.yaml"
    all_leafs = sorted({
        p.parent.relative_to(WORKSPACE).as_posix()
        for p in (WORKSPACE / "rivet").rglob("*.md")
    })
    top_changed = rewrite(top_yaml, all_leafs)

    print(
        f"per-repo rivet.yaml: {per_repo_updated} updated, "
        f"{total_per_repo_paths} total leaf paths"
    )
    print(
        f"top-level rivet.yaml: "
        f"{'updated' if top_changed else 'unchanged'}, "
        f"{len(all_leafs)} total leaf paths"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
