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
| R8 | Attempt a universal reachability theorem | complete (E-011..E-019: the u = 3 and u = 7 layers classified (the E-014 5-divisibility span reading was falsified by the E-015 depth census: 381,652 depth-0 spanners are 5-free); the composition-level iff census-verified 0-mismatch across the 795,913 tested failing-class records (the v5(x') = 0 population) and machine-checked in U7Layer.lean (13 theorems, joint audited 15 + 31 = 46); E-020: R9 validation (the rho-based re-implementation: the census invariants re-derived; the independent evidence is the 2,400-record from-scratch opposite-pair checks, in agreement; the 9,223-record re-derivation sweep counted 6,915 records in the iff cells (2,888 span + 4,027 fail), its other 2,308 records being 5-divisible and outside the domain, and its span test is defined from the condition under test, so its zero cells are structural, not independent); next: the paper-v1.7 assembly); E-021: the u = 11 layer class structure landed (engine v0.15: the class-8 gap structural (11 | (p+3)/4 forced, the predicate forbids it), the span tiers 17.4%/15.3%/8%-ish across 9 classes, and 1,413,291 = 67.80% of the fail records carrying a collision while the span criterion fails - the pair-vs-span distinction populated; part 2 (engine v0.16): the Legendre-split condition census - the necessary direction span => x' has a quadratic-non-residue odd prime divisor is 0-mismatch population-wide (nocond_span = 0, all 9 classes), span => collision likewise, the sufficiency falsified with the failure split by the QR status of n-bar (the non-QR classes trivially fire, the QR classes split ~52/48 with a class-constant ~116.3k non-firing fail population) |
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
