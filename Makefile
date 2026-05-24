# eclipse-score-fork — convert / validate / rebase helpers.
#
# Tracked workflow:
#   make rebase        Fetch+ff-only-merge each upstream remote
#   make convert       Run tools/score_import.py against every upstream
#   make validate      Run rivet's mechanical oracle over the corpus
#   make all           rebase + convert + validate
#   make clean         Delete generated rivet/*/artifacts/ + coverage reports

REPOS := \
  eclipse-score-.eclipsefdn eclipse-score-.github \
  eclipse-score-apt-install eclipse-score-baselibs \
  eclipse-score-baselibs_rust eclipse-score-bazel-tools-cc \
  eclipse-score-bazel-tools-python eclipse-score-bazel_cpp_toolchains \
  eclipse-score-bazel_platforms eclipse-score-bazel_registry \
  eclipse-score-cicd-actions eclipse-score-cicd-workflows \
  eclipse-score-communication eclipse-score-config_management \
  eclipse-score-dash-license-scan eclipse-score-dev_playground \
  eclipse-score-devcontainer eclipse-score-docs-as-code \
  eclipse-score-eclipse-score-website eclipse-score-eclipse-score-website-preview \
  eclipse-score-eclipse-score-website-published eclipse-score-eclipse-score.github.io \
  eclipse-score-feo eclipse-score-ferrocene_toolchain_builder \
  eclipse-score-inc_daal eclipse-score-inc_diagnostics \
  eclipse-score-inc_os_autosd eclipse-score-inc_security_crypto \
  eclipse-score-inc_someip_gateway eclipse-score-inc_time \
  eclipse-score-infrastructure eclipse-score-itf \
  eclipse-score-kyron eclipse-score-lifecycle \
  eclipse-score-logging eclipse-score-mcp-servers \
  eclipse-score-module_template eclipse-score-more-disk-space \
  eclipse-score-orchestrator eclipse-score-os_images \
  eclipse-score-persistency eclipse-score-process-description \
  eclipse-score-qnx_unit_tests eclipse-score-reference_integration \
  eclipse-score-rules_imagefs eclipse-score-sbom-tool \
  eclipse-score-score eclipse-score-score-crates \
  eclipse-score-score_cpp_policies eclipse-score-score_rust_policies \
  eclipse-score-scrample eclipse-score-testing_tools \
  eclipse-score-toolchains_gcc eclipse-score-toolchains_gcc_packages \
  eclipse-score-toolchains_qnx eclipse-score-toolchains_rust \
  eclipse-score-tooling eclipse-score-tools

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
	    --docs-out rivet/$*/docs \
	    --report rivet/$*/coverage.md

# ── Mechanical oracle — corpus-scale rivet validate + variant gate ─────
#
# Two gates: rivet schema validation across all 58 repos AND the
# variant model's check-all over the named worked variants. Both must
# pass for the falsification claim to hold.
validate: validate-corpus validate-variants

validate-corpus:
	@$(RIVET) --schemas $(SCHEMAS) validate

validate-variants:
	@$(RIVET) variant check-all \
	    --model   variants/feature-model.yaml \
	    --binding variants/bindings.yaml

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

# ── Variant feature-model checks ────────────────────────────────────────
#
# Eclipse-score declares variant management as a stakeholder requirement
# but ships no variant model.  variants/feature-model.yaml + bindings.yaml
# fill that gap using rivet's existing PLE machinery — see the README's
# "Variant / feature-model handling" section.

variant-check:
	@$(RIVET) variant check-all \
	    --model   variants/feature-model.yaml \
	    --binding variants/bindings.yaml

variant-matrix:
	@$(RIVET) variant matrix \
	    --model   variants/feature-model.yaml \
	    --binding variants/bindings.yaml

# ── Cleanup ─────────────────────────────────────────────────────────────
clean:
	@rm -f rivet/*/artifacts/imported.yaml rivet/*/coverage.md
