# Independent proof-kernel verification (Nanoda) — v1.5/v1.6/v1.7 gate record

**Gate:** fully independent re-verification of the principal theorem
dependency closure by a second implementation of the Lean 4 type-checking
kernel (not Lean itself), per the reviewer's requirement 1–9 and the
standing "independent Lean compilation" acceptance item.

## Historical reproduction instructions (v1.5/v1.6 exports; retained as provenance — the CURRENT release reproduces via `scripts/nanoda_gate.sh`, which supersedes the manual commands below)

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

   Historical v1.5 export: 1,097,786 NDJSON lines, 53,696,217 bytes,
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

## Strict-mode evidence and artifact retention (sixth review V15-01/V15-02)

The sixth review noted that the committed v1.5 config used
`"unpermitted_axiom_hard_error": false` and asked for strict enforcement and
retained evidence. Both are now in place:

1. **Strict rerun (2026-11-24, first on the v1.5 export, then on the v1.6
   export).** Config `nanoda_config_strict.json` (committed beside this file):

   ```json
   {
     "permitted_axioms": ["propext", "Classical.choice", "Quot.sound"],
     "unpermitted_axiom_hard_error": true,
     "unsafe_permit_all_axioms": false,
     "nat_extension": true,
     "string_extension": true
   }
   ```

   Strict run on the v1.5 export: exit 0 (recorded before the v1.6 release).
   Strict run on the **v1.6 export** (principal_export SHA-256
   `c61d4ba4bb15ace630b849e5d808800c208592535ee7adb6a78d74f7d1c25d17`,
   53,820,117 bytes, 1,022,348 NDJSON lines): **exit 0,
   "Checked 13083 declarations with no typechecker errors"** — the increase
   over 13,076 is exactly the declarations added by the two sixth-review §4
   lemmas (`parametric_divisibility`, `param_exists_iff_onesided`). With
   `unpermitted_axiom_hard_error: true`, any axiom outside the trio used by
   any checked declaration aborts the run; zero typechecker errors under
   that policy is the strict gate condition. The "Unable to print axioms"
   pretty-printer notice remains cosmetic (printing is not verification).

2. **Independent axiom enumeration from the export bytes**
   (`export_axioms.json`, committed): parsed the NDJSON directly — exactly
   **3 axiom records** (`propext`, `Quot.sound`, `Classical.choice`) out of
   12,129 declaration records (8,166 `thm`, 3,509 `def`, 438 `inductive`,
   13 `opaque`, 3 `axiom`), and all **13** principal theorems present as
   `thm` declarations, including the two new sixth-review §4 lemmas.

3. **Retained artifacts** (this directory; digests in `SHA256SUMS`):
   `principal_export.ndjson.gz` (complete exported proof environment),
   `nanoda_config.json` + `nanoda_config_strict.json`,
   `nanoda_run.log` + `nanoda_execution_strict.log`,
   `lean_build.log`, `axiom_audit.log` (13-result proof-term audit),
   `export_axioms.json`.

4. **Gate automation** (`scripts/nanoda_gate.sh`): the chain above — build,
   axiom audit, export, strict check, evidence refresh — is fully scripted.
   Per the sixth review's V15-03 allowance, it is executed as a documented
   manual release gate at every Lean-bearing release rather than inside the
   GitHub workflow (the export requires the locally pinned lean4export
   + nanoda builds).

5. **CI enforcement**: the workflow's proof-term audit step remains the
   CI-enforced half (now covering 13 principal results); the Nanoda strict
   run record above is refreshed by `scripts/nanoda_gate.sh` per release.

## Interpretation

This closes the "Independent Lean compilation / Independent proof-term
audit" acceptance items at the strongest available standard: the proof
terms were re-checked by a second implementation of the Lean kernel,
independent of Lean's own C++ checker, restricted to the exact axiom
baseline the paper's Appendix A declares. Reproduction: clone the two
pinned revisions, rebuild both, re-run the export from the tagged
repository state — **`paper-v1.6` for the 13-theorem v1.6 export,
`paper-v1.7` for the current 14-theorem export** (V16-01's
`parametric_divisibility_iff` was added at v1.7) — re-check, and compare
the export SHA-256 above byte-for-byte. Or run `scripts/nanoda_gate.sh`,
which asserts both pinned tool revisions, rebuilds, audits, exports,
strict-checks, and refreshes every evidence file and `SHA256SUMS` in one
invocation.
