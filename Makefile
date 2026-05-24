# eclipse-score-fork — convert / validate / rebase helpers.
#
# Tracked workflow:
#   make rebase        Fetch+ff-only-merge each upstream remote
#   make convert       Run tools/score_import.py against every upstream
#   make validate      Run rivet's mechanical oracle over the corpus
#   make all           rebase + convert + validate
#   make clean         Delete generated rivet/*/artifacts/ + coverage reports

REPOS := eclipse-score-score eclipse-score-process-description \
         eclipse-score-persistency eclipse-score-docs-as-code

RIVET   := /Users/r/.cargo/bin/rivet
SCHEMAS := vendor/rivet-schemas
PYTHON  := python3

.PHONY: all rebase convert validate clean schemas-refresh

all: convert validate

# ── Convert every upstream RST tree → rivet YAML ─────────────────────────
convert: $(addprefix convert-,$(REPOS))

convert-%:
	@echo "→ converting upstream/$* …"
	@$(PYTHON) tools/score_import.py \
	    upstream/$* \
	    rivet/$*/artifacts/imported.yaml \
	    --report rivet/$*/coverage.md

# ── Mechanical oracle — corpus-scale rivet validate ─────────────────────
validate:
	@$(RIVET) --schemas $(SCHEMAS) validate

# Per-repo validation (each isolated; expect cross-repo dangling links).
validate-each: $(addprefix validate-,$(REPOS))

validate-%:
	@echo "→ rivet validate rivet/$* …"
	@cd rivet/$* && $(RIVET) --schemas $(CURDIR)/$(SCHEMAS) validate || true

# ── Rebase every upstream against its origin ────────────────────────────
rebase: $(addprefix rebase-,$(REPOS))

rebase-%:
	@echo "→ rebasing upstream/$* …"
	@git -C upstream/$* fetch origin
	@git -C upstream/$* merge --ff-only origin/HEAD || \
	    echo "  (no ff-only path — inspect upstream/$* manually)"

# ── Refresh the pinned rivet schemas from a local rivet checkout ───────
schemas-refresh:
	@echo "→ refreshing vendor/rivet-schemas from /Users/r/git/pulseengine/rivet"
	@cp /Users/r/git/pulseengine/rivet/schemas/*.yaml $(SCHEMAS)/
	@$(RIVET) --schemas $(SCHEMAS) schema validate

# ── Cleanup ─────────────────────────────────────────────────────────────
clean:
	@rm -f rivet/*/artifacts/imported.yaml rivet/*/coverage.md
