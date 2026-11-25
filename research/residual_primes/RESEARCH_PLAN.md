# RESEARCH_PLAN.md — Paper 2 (Residual Prime Structure)

Standing banner: the Erdős–Straus conjecture is open; this plan pursues
structural research toward universal opposite-residue reachability. Claim
discipline per the Paper-1 review program: exact criteria verified 0-mismatch
both directions; no claim from a single hand derivation; computation never
closes a universal claim; parity-slip audits on every odd-factor filter.

| Phase | Objective | Status |
| --- | --- | --- |
| R1 | Freeze and inventory the research datasets (SHA-256 manifest, re-runnable check) | in progress: `DATA_MANIFEST.md`, `tests/verify_manifest.py` |
| R2 | Analyze the modulo-5 separation (verify the review's 4.09% / 1.50% / 2.73× figures independently; decompose into layer-composition vs per-layer mechanism) | running (engine v0.2) |
| R3 | Exact structural classifications for individual parameter layers (the `MOD31_EXACT_REDUCTION.md` pattern) | open |
| R4 | Formalize the opposite-residue collision equivalence in Lean (`−1 ∈ S_u(M) ⟺ D ∩ (−D) ≠ ∅`) | open |
| R5 | Formalize the sufficient cardinality theorem (`|D| > φ(u)/2 ⟹` collision) in Lean | open |
| R6 | Derive stronger structural sufficient conditions | open |
| R7 | Coverage across multiple parameter layers | open |
| R8 | Attempt a universal reachability theorem | open (the paper's central problem) |
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
