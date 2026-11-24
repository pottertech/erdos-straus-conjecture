#!/usr/bin/env bash
# Nanoda independent-kernel release gate (v1.6+).
# Automated chain for the sixth-review acceptance items V15-01/V15-02:
#   1. lake build (all Lean modules, 0 errors)
#   2. print_axioms + CI axiom-audit gate (13 principal results)
#   3. lean4export closure export (pinned a3e35a5, toolchain v4.30.0)
#   4. nanoda strict mode (unpermitted_axiom_hard_error=true, permitted =
#      propext/Classical.choice/Quot.sound only, unsafe_permit_all=false)
#   5. evidence files into verification_nano/ + SHA256SUMS refresh
# Documented as a manually executed, fully scriptable release gate
# (per sixth review item V15-03: "a manually executed release gate is
# acceptable if documented as such").
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
INDEP="${NANODA_INDEP:-$HOME/repos/verification-indep}"
EXPORT="$REPO/verification_nano/principal_export.ndjson"
CFG="$REPO/verification_nano/nanoda_config_strict.json"
LOG="$REPO/verification_nano/nanoda_execution_strict.log"
NANODA_BIN="$INDEP/nanoda_lib/target/release/nanoda_bin"
LEAN4EXPORT="$INDEP/lean4export/.lake/build/bin/lean4export"
THMS=(
  ErdosStrausConjecture.scaling
  ErdosStrausConjecture.mod8_of_12
  ErdosStrausConjecture.prime_non24_isErdosStraus
  ErdosStrausConjecture.full_conjecture_of_h24
  ErdosStrausConjecture.erdos_straus_except_residual_open_class
  ErdosStrausConjecture.residue_classification
  ErdosStrausConjecture.u_method_core
  ErdosStrausConjecture.u_method_witness
  ErdosStrausConjecture.witness_extraction
  ErdosStrausConjecture.finite_search_equivalence
  ErdosStrausConjecture.parametric_divisibility
  ErdosStrausConjecture.param_exists_iff_onesided
  ErdosStrausConjecture.theorem2
)
MODULES=(
  ErdosStrausConjecture.Reduction
  ErdosStrausConjecture.CenteredCriterion
  ErdosStrausConjecture.FiniteSearch
  ErdosStrausConjecture.CenteredEquivalence
  ErdosStrausConjecture.MainTheorem
)

cd "$REPO"
echo "[1/5] lake build" && lake build
lake env lean scripts/print_axioms.lean | tee /tmp/print_axioms_gate.out | \
  python3 scripts/check_axioms_audit.py
cp /tmp/print_axioms_gate.out verification_nano/axiom_audit.log

echo "[3/5] lean4export"
lake env "$LEAN4EXPORT" "${MODULES[@]}" -- "${THMS[@]}" > "$EXPORT"

echo "[4/5] nanoda strict"
sed -e "s|^\"export_file_path.*$|\"export_file_path\": \"$EXPORT\",|" "$CFG" \
    -i '' 2>/dev/null || sed -i "s|^\"export_file_path.*$|\"export_file_path\": \"$EXPORT\",|" "$CFG"
"$NANODA_BIN" "$CFG" | tee "$LOG"

echo "[5/5] evidence refresh"
gzip -9 -c "$EXPORT" > verification_nano/principal_export.ndjson.gz
shasum -a 256 \
  verification_nano/principal_export.ndjson.gz \
  verification_nano/nanoda_config_strict.json \
  verification_nano/nanoda_config.json \
  verification_nano/nanoda_execution_strict.log \
  verification_nano/nanoda_run.log \
  verification_nano/export_axioms.json \
  verification_nano/axiom_audit.log \
  verification_nano/lean_build.log \
  results/layer4_certificates.jsonl \
  sweep_exact/nonparametric_1e7_1e9.jsonl \
  > verification_nano/SHA256SUMS
shasum -a 256 "$EXPORT" >> verification_nano/SHA256SUMS
echo "NANODA GATE: PASS"
