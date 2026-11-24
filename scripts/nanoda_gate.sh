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
  ErdosStrausConjecture.parametric_divisibility_iff
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
echo "[1/5] tool revision assertions (V16-03)"
NANODA_REV="${NANODA_EXPECT:-0da9f98}"
LEAN4EXPORT_REV="${LEAN4EXPORT_EXPECT:-a3e35a5}"
ACTUAL_NANODA="$(git -C "$INDEP/nanoda_lib" rev-parse --short HEAD)"
ACTUAL_LEAN4EXPORT="$(git -C "$INDEP/lean4export" rev-parse --short HEAD)"
[ "$ACTUAL_NANODA" = "$NANODA_REV" ] || { echo "nanoda_lib HEAD $ACTUAL_NANODA != pinned $NANODA_REV"; exit 1; }
[ "$ACTUAL_LEAN4EXPORT" = "$LEAN4EXPORT_REV" ] || { echo "lean4export HEAD $ACTUAL_LEAN4EXPORT != pinned $LEAN4EXPORT_REV"; exit 1; }

echo "[2/5] lake build (log captured)"
lake build 2>&1 | tee temp_lean_build.log
cp temp_lean_build.log verification_nano/lean_build.log
lake env lean scripts/print_axioms.lean > /tmp/print_axioms_gate.out || {
  echo "print_axioms execution failed"; exit 1; }
NAMECOUNT=$(grep -c "depends on axioms" /tmp/print_axioms_gate.out)
[ "$NAMECOUNT" -eq 14 ] || { echo "expected 13 audited results, got $NAMECOUNT"; exit 1; }
python3 scripts/check_axioms_audit.py < /tmp/print_axioms_gate.out
cp /tmp/print_axioms_gate.out verification_nano/axiom_audit.log

echo "[3/5] lean4export"
lake env "$LEAN4EXPORT" "${MODULES[@]}" -- "${THMS[@]}" > "$EXPORT"

echo "[4/5] nanoda strict (V16-02: structural JSON edit; export SHA recorded pre-run)"
EXPORT_SHA="$(shasum -a 256 "$EXPORT" | awk '{print $1}')"
echo "export SHA-256 (pre-check): $EXPORT_SHA" > "$LOG"
python3 - "$CFG" "$EXPORT" <<'PY'
import json, pathlib, sys
cfg = pathlib.Path(sys.argv[1])
export = pathlib.Path(sys.argv[2]).resolve()
assert export.is_file(), f"missing export {export}"
data = json.loads(cfg.read_text())
data["export_file_path"] = str(export)
assert data["unpermitted_axiom_hard_error"] is True
assert data["unsafe_permit_all_axioms"] is False
assert set(data["permitted_axioms"]) == {"propext", "Classical.choice", "Quot.sound"}
cfg.write_text(json.dumps(data, indent=2) + "\n")
PY
"$NANODA_BIN" "$CFG" >> "$LOG"
NANODA_EXIT=$?
grep -q "no typechecker errors" "$LOG" || { echo "nanoda reported typechecker errors"; exit 1; }

echo "[5/5] evidence refresh"
# regenerate the export-axiom enumeration from the fresh export bytes (V16-03/V16-04)
python3 scripts/extract_export_axioms.py "$EXPORT" verification_nano/export_axioms.json
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
RAW_SHA="$(shasum -a 256 "$EXPORT" | awk '{print $1}')"
echo "# uncompressed export: SHA-256 $RAW_SHA (zipped above)" >> verification_nano/SHA256SUMS
echo "NANODA GATE: PASS"
