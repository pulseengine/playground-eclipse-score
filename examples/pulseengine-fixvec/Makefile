# Worked example — eclipse-score FixVec interface, pulseengine treatment.
#
#   make validate   rivet validates the typed artifacts (always available)
#   make aadl       spar validates the AADL package (requires spar in PATH)
#   make wit        spar emits WIT from AADL and diffs against arch/fixvec.wit

RIVET ?= rivet
SPAR  ?= spar
SCHEMAS := ../../vendor/rivet-schemas

.PHONY: all validate aadl wit clean

all: validate

validate:
	@$(RIVET) --schemas $(SCHEMAS) validate

aadl:
	@command -v $(SPAR) >/dev/null 2>&1 || { \
	    echo "spar not in PATH — install from https://github.com/pulseengine/spar"; \
	    exit 0; }
	@$(SPAR) validate arch/fixvec.aadl

wit:
	@command -v $(SPAR) >/dev/null 2>&1 || { \
	    echo "spar not in PATH — skipping AADL→WIT round-trip check"; \
	    exit 0; }
	@$(SPAR) emit --format wit arch/fixvec.aadl > /tmp/fixvec.spar.wit
	@diff -u arch/fixvec.wit /tmp/fixvec.spar.wit \
	    && echo "AADL → WIT round-trip matches arch/fixvec.wit"

clean:
	@rm -f /tmp/fixvec.spar.wit
