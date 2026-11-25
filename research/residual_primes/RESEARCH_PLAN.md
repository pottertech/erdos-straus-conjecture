# RESEARCH_PLAN.md — Paper 2 (Residual Prime Structure)

Standing banner: the Erdős–Straus conjecture is open; this plan pursues
structural research toward universal opposite-residue reachability. Claim
discipline per the Paper-1 review program: exact criteria verified 0-mismatch
both directions; no claim from a single hand derivation; computation never
closes a universal claim; parity-slip audits on every odd-factor filter.

| Phase | Objective | Status |
| --- | --- | --- |
| R1 | Freeze and inventory the research datasets (SHA-256 manifest, re-runnable check) | complete (the fleet-hardened verifier: digest + byte-size + git-tracking checks) |
| R2 | Analyze the modulo-5 separation (verify the review's 4.09% / 1.50% / 2.73× figures independently; decompose into layer-composition vs per-layer mechanism) | complete (E-002: the aggregate is a layer-composition artifact localizing to u = 11; H-1 reformulated) |
| R3 | Exact structural classifications for individual parameter layers | complete (E-004 conditioning; E-005 u=11 classification); p=3 (mod 5) zero remains |
| R4 | Formalize the opposite-residue collision equivalence in Lean (`−1 ∈ S_u(M) ⟺ D ∩ (−D) ≠ ∅`) | complete (E-003; D·D⁻¹ form; window form is the extension) |
| R5 | Formalize the sufficient cardinality theorem (`|D| > φ(u)/2 ⟹` collision) in Lean | complete (E-003; `pigeonhole_reachability`) |
| R6 | Derive stronger structural sufficient conditions | complete (E-009: the delicate class mechanized — 82.8% unit-pair / 17.2% small-residue tail; H-5) |
| R7 | Coverage across multiple parameter layers | complete (E-010: the witness-shape table over all 40 populated slices; H-6; the small-layer p-free statement) |
| R8 | Attempt a universal reachability theorem | complete (E-011..E-019: the u = 3 and u = 7 layers classified; the composition-level iff census-verified 0-mismatch across all 1,194,364 failing-class records and machine-checked in U7Layer.lean (13 theorems, joint audited 15 + 31 = 46); E-020: R9 independent validation PASSED (the rho-based re-implementation: the census invariants, the 9,223-record re-derivation sweep, the 2,400-record from-scratch opposite-pair checks - all in agreement); next: the paper-v1.7 assembly) |
| R9 | Independently validate and publish established results | open |

## Claim-discipline gates (applies to every phase)

1. Every criterion stated as an exact definition AND verified 0-mismatch
   (both directions) against the committed datasets.
2. Every published count independently recomputed or hash-pinned to a
   verified artifact (`DATA_MANIFEST.md`).
3. Registry separation (see `THEOREM_REGISTRY.md` / `HYPOTHESIS_REGISTRY.md`):
   proved theorems, computational observations, open hypotheses, and rejected
   hypotheses are never mixed.
4. Parity-slip audit on every filter over odd prime factors (factor 2 exempt).
5. New formal results compile 0-`sorry`, keep the axiom census, and enter the
   CI axiom gate before any count depends on them.
