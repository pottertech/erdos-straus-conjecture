# Independent proof-kernel verification (Nanoda) — v1.5 gate record

**Gate:** fully independent re-verification of the principal theorem
dependency closure by a second implementation of the Lean 4 type-checking
kernel (not Lean itself), per the reviewer's requirement 1–9 and the
standing "independent Lean compilation" acceptance item.

## What ran

1. **Exporter:** [lean4export](https://github.com/leanprover/lean4export)
   pinned at `a3e35a5` (2026-05-26) — the upstream commit whose
   `lean-toolchain` is exactly `leanprover/lean4:v4.30.0`, matching the
   repository's toolchain/Mathlib pin (all upstream later commits bump to
   v4.31.0-rc1). Built standalone (`lake build`, 6 jobs, 0 errors).
2. **Checker:** [nanoda](https://github.com/ammkrn/nanoda_lib) pinned at
   `0da9f98` (2026-11-07, v0.4.32, `cargo build --release`, Rust 1.97.1).
3. **Export** (lean4export NDJSON, format 3.1.0, Lean githash
   `d024af099ca4bf2c86f649261ebf59565dc8c622`, Lean "4.30.0"):

   ```sh
   lake env ../verification-indep/lean4export/.lake/build/bin/lean4export \
     ErdosStrausConjecture.Reduction ErdosStrausConjecture.CenteredCriterion \
     ErdosStrausConjecture.FiniteSearch ErdosStrausConjecture.CenteredEquivalence \
     ErdosStrausConjecture.MainTheorem -- \
     ErdosStrausConjecture.scaling ErdosStrausConjecture.mod8_of_12 \
     ErdosStrausConjecture.prime_non24_isErdosStraus \
     ErdosStrausConjecture.full_conjecture_of_h24 \
     ErdosStrausConjecture.erdos_straus_except_residual_open_class \
     ErdosStrausConjecture.residue_classification \
     ErdosStrausConjecture.u_method_core ErdosStrausConjecture.u_method_witness \
     ErdosStrausConjecture.witness_extraction \
     ErdosStrausConjecture.finite_search_equivalence \
     ErdosStrausConjecture.theorem2 > principal_export.ndjson
   ```

   Export: 1,097,786 NDJSON lines, 53,696,217 bytes,
   SHA-256 `b424d34a87069e5726d91585ea7c9b07cbf23912770c8024d324e208c5a808cf`.
4. **Check** (config `nanoda_config.json` committed beside this file;
   `permitted_axioms` = `propext`, `Classical.choice`, `Quot.sound` only;
   Nat/String kernel extensions on; 1 GB stack/worker):

   ```sh
   nanoda_bin nanoda_config.json
   ```

## Result

- Exit code **0**; independent Rust kernel type-checked the **13,076
  declarations** of the exported principal-theorem closure
  ("Checked 13076 declarations with no typechecker errors").
- All **11 principal theorems** are present in the closure as
  `thm`-declarations (verified by name resolution over the intern table),
  including `witness_extraction` and the composed
  `finite_search_equivalence`.
- Export axiom set (**by construction**, resolved from `axiom` records):
  **exactly** `propext`, `Quot.sound`, `Classical.choice`. No `sorryAx`,
  no `Lean.trustCompiler` reference, and neither documented project axiom
  appears.
- Pretty-printer note: nanoda reports "1 pretty printer errors: Unable to
  print axioms" — cosmetic (pretty printing is not verification); the
  exit code and zero typechecker errors are the gate conditions.

## Interpretation

This closes the "Independent Lean compilation / Independent proof-term
audit" acceptance items at the strongest available standard: the proof
terms were re-checked by a second implementation of the Lean kernel,
independent of Lean's own C++ checker, restricted to the exact axiom
baseline the paper's Appendix A declares. Reproduction: clone the two
pinned revisions, rebuild both, re-run the export from the tagged
repository state (`paper-v1.5`), re-check, and compare the export
SHA-256 above byte-for-byte.
