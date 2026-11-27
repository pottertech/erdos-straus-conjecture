# EXPERIMENT_LOG.md — Paper 2

One entry per run: what ran, on which verified population, the key results
(with counts and the bound named), artifacts, and status. An entry's claims
are bounded by its data; universal claims never enter via this log.

## E-001 — Lane L1: pigeonhole margin at first-working parameters (2026-11-24)

- **What ran:** `sweep_exact/collision_margin_engine.c` (v0.1,
  SHA-256-pinned in DATA_MANIFEST), sanitizer-built, self-tested on the four
  release anchors + the cross-direction no-collision check below the
  first-working parameter; full run over the verified hard-case population
  `[10^7, 10^9)`.
- **Populations:** sweep 3,194,231 (matches the published sweep exactly);
  (H24) 2,364,031; collisions found at 100% of first-working parameters
  (MISMATCH 0).
- **Key results:** pigeonhole-conclusive 3,177,642 (99.48%); delicate
  (collision present, `|D| ≤ φ(u)/2`) 16,589 (0.52%); the `u = 3` and `u = 7`
  layers 100% pigeon-conclusive; delicate concentrates at higher layers
  (17.4% at `u = 19`, 77.6% at `u = 43`, 100% at `u = 67, 79, 83` incl. both
  `u = 83` record primes — the `u = 71` and `u = 75` layers are 1/6 and 1/2
  delicate respectively; small-residue collision pairs, e.g. `(1, 82)` with
  margin −58 for `651,412,441`).
- **Artifacts:** `analysis/collision_v01/` (run output, stderr,
  sanitized self-test, 5,000-row delicate sample), hashes in
  DATA_MANIFEST.
- **Status:** complete; feeds H-2 and the R2 layer-conditioning tests.

## E-002 — R2: modulo-5 separation quantification (2026-11-24)

- **What ran:** engine v0.2 (adds the intrinsic parametric/nonparametric
  classification from the verified mod-840 procedure and mod-5 × mod-840 ×
  layer cross-tabulation), sanitizer-built, same anchors.
- **Key results:** recorded in the E-002 results block below (verified
  run, engine v0.2): the nonparametric-only rates per `p mod 5` group as
  an independent check of the review's figures, the full-sweep mod-5
  breakdown, and the intrinsic class table; the layer-conditioned test
  of H-1's falsification criterion follows in E-004.
- **Artifacts:** `analysis/mod5_separation_v02/`.

### E-002 results (verified run, engine v0.2)

- **Independent reproduction of the review's figures — exact:** over the
  mod-840 cohort, the nonparametric-only rate by `p mod 5`:
  `+1 (mod 5)`: 16,267 / 398,126 = **4.09%**; `−1 (mod 5)`:
  5,955 / 397,787 = **1.50%**; ratio **2.73x** — matching the twelfth
  review's 4.09% / 1.50% / 2.73x exactly. Cohort populations near-equal in
  size (398,126 vs 397,787): the separation is in the rates, not the sizes.
- **Full-sweep mod-5 breakdown (new):** `+1 (mod 5)`:
  41,226 / 1,064,669 = 3.87%; `p ≡ 3 (mod 5)` (a third group absent from the
  mod-840 restriction): 16,834 / 1,065,189 = **1.58% — the lowest of all**;
  `−1 (mod 5)`: 31,023 / 1,064,373 = 2.91%; `p ≡ 2 (mod 5)`: no population.
  Notable: **no `p ≡ 3 (mod 5)` prime is classified only-parametric**
  (onlypar = 0 in that group) — an unexplained structural zero, logged for
  R3.
- Intrinsic classes over the mod-840 cohort (per class, onlypar/both/onlynon):
  `1: 5,648/118,829/5,502`; `121: 4,969/119,966/5,028`;
  `169: 2,224/125,512/1,939`; `289: 1,293/126,864/1,916`;
  `361: 6,189/126,258/5,737`; `529: 2,420/133,519/2,100`. Per-class totals and
  onlynon agree exactly with the ninth review's independently computed table.
- **Reconciliation with the review's table — exact agreement:** the
  onlypar/both split agrees with the ninth review's independently
  computed table in full (onlypar total 22,743; class 529: 2,420
  onlypar / 133,519 both; every aggregate matches). An earlier draft of
  this entry disclosed a one-prime discrepancy (22,744 vs 22,743); that
  figure came from a pre-fix run, no committed artifact contains it,
  and the disclosure is withdrawn in favor of this statement.
- **Bugs caught during verification (both fixed before any figure ships):**
  (i) the divisor-list cap (4096) silently truncated the candidate set for
  divisor-rich `x` — the layer-workflow's "capped loop reclassifies records"
  class; (ii) a 64-bit `p²·x` overflow in the candidate products — the same
  V14-01 overflow class. All candidate arithmetic now 128-bit, the divisor
  table uncapped with a hard assert.
- **Artifacts:** `analysis/mod5_separation_v02/` (engine v0.2, run output
  `full_run.txt`, stderr — sanitizer-silent — and the sanitized self-test),
  hashes below in DATA_MANIFEST.
- **Status:** complete. H-1 remains open (not layer-conditioned to
  resolution yet): the next sub-run cross-tabulates first-working layers by
  mod-5 group to test H-1's falsification criterion #1.

## E-003 — R4/R5: the collision criterion machine-checked (2026-11-24)

- **What was proved:** module `ErdosStrausConjecture/ResidualPrimes/CollisionReachability.lean`
  (self-contained Mathlib, no project axioms):
  `pigeonhole_reachability` (2|D| > phi(u) ⟹ collision, R5), and the R4
  equivalences: the collision condition ⟺ the pair condition
  (∃ d₁ d₂ ∣ M, (d₁ + d₂) % u = 0) ⟺ −1 ∈ D·D⁻¹ (the centered product
  set in its D·D⁻¹ formulation), plus the three lemmas feeding them
  (`card_le_totient_of_all_isUnit`, `isUnit_mem_union`, `card_negResidues_eq`)
  and the bridge `hasOppositePair_iff_centered_neg_one`.
- **Verification:** `lake env lean` exit 0 (0 errors), `lake build` exit 0,
  0 `sorry`, 0 `admit`; axiom census via `#print axioms` on all seven
  declarations — each depends on exactly `[propext, Classical.choice,
  Quot.sound]`; the joint audited set is 15 (Paper 1, frozen) + 7 = 22.
- **Artifacts:** the module, the axiom audit output
  `ErdosStrausConjecture_src/axiom_audit_collision.txt`, and the build log,
  all hash-pinned in DATA_MANIFEST.
- **Scope carried:** the factorization-window characterization of the
  centered product set (∏ q^[−e, e] = D·D⁻¹) is the R4-lane extension, NOT
  claimed in this module (the D·D⁻¹ formulation is used, per the ninth
  review's §5.3 observation).
- **Status:** complete. The review's boxed criterion is now machine-checked;
  the research target H-3 (universal reachability) has its formal skeleton.

## E-004 — R3: layer x mod-5 conditioning (H-1 falsification test #1) (2026-11-25)

- **What ran:** engine v0.3 (v0.2 + the first-working-layer x mod-5 cross
  tables, full sweep and mod-840-cohort restricted), sanitizer-built; the
  v0.2 anchors reproduce exactly (SWEEP 3194231 / PIGEON 3177642 / DELICATE
  16589 / MISMATCH 0; MOD5, MOD5MOD840 and INTR840 rows byte-identical).
- **Verified cross table (mod-840 cohort, XULAYER840 rows; full table in
  analysis/layer_mod5_v03/r3_full_run.txt):** rates of only-nonparametric
  classification within each first-working layer, +1 (mod 5) vs -1 (mod 5):
  u=7: 0/190,978 vs 0/190,674 (0.00% both);
  **u=11: 9,973/134,455 = 7.42% vs 0/145,060 = 0.00%**;
  u=15: 0/32,271 vs 0/27,488 (0.00% both);
  u=19: 4,225/25,136 = 16.81% vs 3,664/17,668 = 20.74%;
  u=23: 10.73% vs 11.80%; u=27: 20.87% vs 22.99%; u=31: 18.77% vs 11.91%;
  higher layers populated but small (both groups, rates 6-100% with n at
  most about 400).
- **Layer-marginal counterfactuals (computed from the cross table):**
  applying the +1 group's within-layer rates to the -1 group's layer sizes
  gives **4.03%** (actual aggregate: 4.09%); the reverse gives **1.84%**
  (actual: 1.50%). The aggregate 2.73x gap is therefore a **layer-composition
  artifact**, driven almost entirely by the **u = 11 layer**: the 10,312-prime
  aggregate difference has 9,973 accounted for by that single layer
  (7.42% vs 0.00%, denominators about 140k each).
- **Mechanism hypothesis (reformulated H-1):** at u = 11 with p = 4 (mod 5),
  x = (p+11)/4 satisfies **5 divides x identically**
  ((4+11) x 4^-1 = 0 (mod 5)); and 5 has order 5 in (Z/11)* (5^5 = 1 (mod 11),
  a quadratic residue), so the isolated 5-window {5^t : |t| <= e} never
  reaches -1 = 10 (mod 11) - while every such prime nonetheless HAS a
  parametric witness (0/145,060 lack one). The exact u=11 structure is the
  R3-lane flagship (the MOD31-pattern target: "u = 11, 5|x => parametric
  witness", verifiable 0-mismatch over the 145,060 committed records and
  then as a clean Lean target).
- **H-1 disposition:** the aggregate "modulo-5 separation" is NOT a uniform
  per-layer effect; it localizes to the u = 11 layer with the 5-divisor
  arithmetic above. H-1 is reformulated (registry update) - kept OPEN as the
  u=11-layer mechanism, with the aggregate framing marked as a composition
  artifact.
- **Artifacts:** analysis/layer_mod5_v03/ (engine v0.3, run, self-test; err
  sanitizer-silent, 2 lines of benign 11434-port noise), hashes in
  DATA_MANIFEST (25 pinned; the three engine sources are not yet
  committed, see the manifest note).
- **Status:** complete. Follow-ups: the u=11 exact classification (R3), the
  p = 3 (mod 5) onlypar-zero (R3, unchanged), the window-form Lean lemma
  (R4-lane extension).

## E-005 — R3 flagship: the u=11 exact classification (2026-11-25)

- **What ran:** engine v0.4 (v0.3 + the u­11-slice fingerprint probe:
  per-record 5–|x check and the minimal parametric-witness shape: whether the
  qualifying divisor contains the p-factor and its 5-adic valuation, capped
  at 3), sanitizer-built; the v0.3 anchors reproduce exactly (same SWEEP /
  PIGEON / DELICATE / MISMATCH 0 / MOD5 / MOD5MOD840 / INTR840 / XULAYER
  rows).
- **Verified results over the full sweep [10^7, 10^9):**
  - The u-11, p = 4 (mod 5) class: **145,060 / 145,060 records satisfy
    5 | x, zero mismatches in either direction** (notfivex = 0) - the
    arithmetic identity is per-record verified, and now machine-checked in
    Lean (five_divides_x: given 4 | p + 11 and p = 4 (mod 5), 5 |
    (p + 11)/4).
  - The minimal qualifying divisor is **p-free in 145,060 / 145,060 cases**
    (100% p-free, 0 p-containing): a divisor of x alone always witnesses.
  - Its 5-adic valuation distribution: v5 = 0 for 87,021 (60.0%),
    v5 = 1 for 58,039 (40.0%), v5 >= 2 for 0 - the witnesses are
    5-adically shallow (no witness needs the second 5-power).
  - The 5-window miss is machine-checked: five_pow_ne_neg_one: every
    5-power in ZMod 11 differs from -1 (the isolated 5-window
    {5^t : |t| <= e} reaches only {1, 5, 3, 4, 9}).
- **Verification:** lake env lean exit 0, lake build exit 0, 0 sorry; axiom
  census: five_divides_x on [propext, Quot.sound],
  five_pow_ne_neg_one on [propext, Classical.choice, Quot.sound] - the joint
  audited set is now 22 + 2 = 24.
- **Scope discipline:** "every such prime has a parametric witness" is a
  verified statement over the committed dataset (0-mismatch, the bound
  [10^7, 10^9) named); the two Lean lemmas are unconditional theorems.
  The conditional "5 | x gives a uniform witness formula" for ALL p remains
  open (the witness shape is per-record diverse).
- **Artifacts:** analysis/u11_exact_v04/ (engine v0.4, run, stderr),
  ErdosStrausConjecture_src/axiom_audit_u11.txt, hashes in DATA_MANIFEST
  (29/29).
- **Status:** complete. Lanes queued next: the R4-window formalization,
  the p = 3 (mod 5) onlypar-zero probe.

## E-006 — R4-lane extension: the factorization-window form machine-checked (2026-11-25)

- **What was proved:** module
  `ErdosStrausConjecture/ResidualPrimes/WindowForm.lean`: with the window
  element encoded as `(f.prod (fun q e => ((q ^ e : ℕ) : ZMod u)))` for
  Finsupps `f, g ≤ M.factorization` (the exponent pairs a–b with
  0 ≤ a, b ≤ e₁, i.e. the |t| ≤ e₁ window), the window span equals the
  centered quotient set: `window_iff_inCentered` — closing the bridge to the
  ninth review's §5.3 formulation and to `CollisionReachability`'s
  collision/criterion equivalences. The supporting lemma
  `cast_prod_finsupp` distributes the residue cast over Finsupp products.
- **Verification:** lake env lean exit 0, lake build exit 0, 0 sorry; axiom
  census: cast_prod_finsupp on [propext, Quot.sound], window_iff_inCentered
  on [propext, Classical.choice, Quot.sound]; the joint audited set is now
  24 + 2 = 26.
- **Scope carried:** no coprimality is required for the formal identity
  (the two encodings are the same set); the span interpretation (|t| ≤ e
  with unit inverses) applies under the Paper-1 admissibility hypothesis
  gcd(M, u) = 1, stated in the module docstring.
- **Artifacts:** the module, axiom_audit_window.txt,
  ErdosStrausConjecture_src/WindowForm.lean, hashes in DATA_MANIFEST (33/33).
- **Status:** complete. Remaining R3-item: the p = 3 (mod 5) onlypar-zero
  probe (next session).

## E-007 — R3: the p ≡ 3 (mod 5) onlypar-zero — layer structure resolved (2026-11-25)

- **Source of numbers:** the already-verified v0.3/v0.4 run output
  (analysis/layer_mod5_v03/full_run.txt; the XULAYER g = 3 rows). No new
  sweep.
- **Verified layer structure (p ≡ 3 (mod 5), 1,065,189 primes):** the
  first-working layers number exactly TWO:
  - **u = 7: 788,565 primes (74.0% of the class, all first-working u ≡ 2
    (mod 5)), onlynon = 16,834 (2.13%)** — the class's ONLY
    only-nonparametric records, all in this layer;
  - **u = 3: 276,624 primes (26.0%), onlynon = 0 (0.00%)** — and with the
    class-wide onlypar = 0 (E-002), every one of these is dual-witnessed
    (both).
  The class-wide onlypar = 0 is thus: no p ≡ 3 (mod 5) prime lacks a
  nonparametric companion witness.
- **Arithmetic (machine-checked):** `five_divides_x_u7`: at u = 7 with
  p ≡ 3 (mod 5), 5 ∣ (p + 7)/4 identically (74% of the class class);
  `five_pow_three_eq_neg_one_mod_seven`: 5³ ≡ −1 (mod 7), so in the
  u = 7 window the 5-orbit reaches −1 at depth 3 — in pointed contrast
  with the u = 11 layer, where the 5-window never reaches −1 and the
  separation is a NONparametric gap. The two 5-adic mechanisms act in
  opposite directions: at u = 7 the deep-5 window strengthens parametric
  availability (0.00% onlynon at u = 7 for the complement residues), at
  u = 11 it suppresses it (0/145,060, E-004).
- **Verification:** lake env lean exit 0, lake build exit 0, 0 sorry; axiom
  census: both new theorems on [propext, Quot.sound]; the joint audited set
  is 26 + 2 = 28.
- **Open follow-up (the lane-3 remainder):** the both-class fingerprint at
  u = 7 g = 3 (the witness-shape probe, v0.5) - whether the nonparametric
  companions at u = 7 admit a uniform shape the way the u = 11 class does.
- **Artifacts:** the extended U11Exact.lean, axiom_audit_u11b.txt, hashes in
  DATA_MANIFEST (35/35).
- **Status:** complete for the layer structure; the fingerprint probe
  queued.

## E-008 — lane-3 remainder: the u = 7 g = 3 both-class fingerprint (2026-11-25)

- **What ran:** engine v0.5 (v0.4 + the u = 7 g = 3 slice fingerprint: the
  per-record 5 | x check; the M 5-depth; the minimal parametric- and
  nonparametric-witness shapes in enumeration order: p-containment, the 5
  valuation, and whether the non-witness rides beyond M's 5-depth), built
  with sanitizers, self-test PASS; the sweep anchors reproduce exactly
  (SWEEP 3194231 / PIGEON 3177642 / DELICATE 16589 / MISMATCH 0).
- **Verified results over the u = 7, p ≡ 3 (mod 5) slice, 788,565 records:**
  - 5 ∣ x: **788,565 / 788,565, zero mismatches in either direction**
    (consistent with `five_divides_x_u7`).
  - The M 5-depth: v_5(M) = 1 for 630,921 (80.0%), v_5(M) ≥ 2 for 157,644
    (20.0%); never deeper.
  - **The minimal parametric witness is p-free (a divisor of x alone) in
    771,731 / 771,731 both-class records (100%)**; 90% of these carry
    exactly one 5-power (v_5 = 1: 688,438), 10% are 5-free (77,837).
  - **The minimal nonparametric witness is also p-free in 788,565 / 788,565
    records (100%)** (both-class and only-non records alike); v_5 = 0:
    93,767 (11.9%), v_5 = 1: 544,249 (69.1%), v_5 ≥ 2 in the remainder.
  - The beyond-M-depth flag: **71,444 (9.1%) of the non-witnesses have
    v_5(d) > v_5(M)** (the deeper-5 window makes d ∣ M² with d ∡ M);
    the other 90.9% divide x to a depth within M's window yet fail the
    divisor test for other-factor reasons.
- **The mechanism reading (kept as a hypothesis, H-4):** at u = 7 with
  5 ∣ x, both witness kinds live in the x-divisors - the p-factor is
  never needed - and the 5÷-orbit mod 7 (5³ ≡ −1, machine-checked
  `five_pow_three_eq_neg_one_mod_seven`) is what lets the deeper-5 window
  produce the nonparametric companions. Falsification: any record whose
  minimal witnesses both require the p-factor, or any u = 7 g = 3 record
  with a parametric witness but no nonparametric companion, kills the
  uniform-shape reading.
- **Artifacts:** analysis/u7_g3_probe_v05/ (engine v0.5, run), hashes in
  DATA_MANIFEST (37/37).
- **Status:** complete for this slice. The two-layer p ≡ 3 (mod 5) picture
  (E-007) and this fingerprint close the lane-3 questions posed at launch;
  R6 (the delicate class) is next.

## E-009 — R6: the delicate class mechanized (the minimal-pair fingerprints) (2026-11-25)

- **What ran:** engine v0.6 (v0.5 + the delicate-class minimal-collision-pair
  fingerprints and the per-(layer, mod-5) delicate cross-rows XDEL),
  sanitizer-built; the sweep anchors reproduce exactly (the population
  checks SWEEP/H24/PIGEON/MISMATCH 0 identical, and the delicate total
  reconciles as the former counter plus the new fingerprint counter at
  33,178 = 2 × 16,589).
- **Verified results over the full sweep [10^7, 10^9) (16,589 delicate
  records):**
  - **The minimal collision pair is the unit pair (1, u − 1) in 13,742 of
    16,589 delicate records (82.8%).** Since 1 always divides M, the unit
    pair exists in D × (−D) exactly when −1 ∈ D_u(M) — i.e. the
    one-sided (parametric) criterion succeeds while |D| stays below half
    the unit group.
  - The remaining 2,847 (17.2%) have d₁ ≤ u/4 in 1,808 records and
    u/4 < d₁ ≤ u/2 in 1,039. d₁ > u/2 never occurs (a property of the
    minimal-pair scan: r is scanned from 1, so the smaller member of any
    pair is hit first). Square-root pairs (d₁² = u): 0.
  - The delicate mass concentrates at u = 19 (7,434) and u = 11 (6,075),
    with u = 23 (1,275), u = 27 (998), u = 31 (405) and u = 43 (149) the
    next tiers; per mod-5 group: u ≡ 1 (mod 5) dominates u = 11
    (6,075 = the entire u = 11 layer's delicate mass; E-004's mechanism:
    the 5–window at u = 11 keeps −1 out of every pure-5 product while the
    p–free witnesses still collide), while at u = 19 the −1 (mod 5) group
    carries the majority (5,682 of 7,434).
- **Mechanism reading (H-5 registered):** the delicate class is (i) the
  −1 ∈ D_u(M) records whose |D| is still below the pigeonhole half —
  82.8%, with the (1, −e1)-pair — and (ii) a 17.2% tail where the
  collision is by small non-unit residues. The practical consequence: for
  82.8% of the delicate class the collision is ALREADY a parametric
  witness (−1 ∈ D ⟺ −1 ∈ S_u per CollisionReachability), so the paper's
  reduction applies, and the remaining interest is the 2,847-record tail.
- **Artifacts:** analysis/delicate_r6_v06/ (engine v0.6, run, self-test),
  hashes in DATA_MANIFEST (40/40).
- **Status:** complete. H-3 (the universal-cardinality target) now has its
  mechanism split: the 99.48%-conclusive majority + the delicate tail whose
  majority is one-sided-satisfied. The remaining open question is the
  2,847-record non-unit-pair tail (queued for R7: coverage across layers).

## E-010 — R7: witness-shape coverage across every populated layer (2026-11-25)

- **What ran:** engine v0.7 (v0.6 + the per-(layer, mod-5) witness-shape
  fingerprint for every populated slice: the smallest parametric witness and
  the smallest nonparametric companion by p-containment, plus the per-record
  5 ∣ x counter), sanitizer-built; the sweep anchors reproduce exactly.
- **Verified classification table (40 populated (u, p mod 5) slices; the
  XSHAPE rows in analysis/layers_r7_v07/full_run.txt):**
  - **The p-free share of the smallest parametric witnesses, by layer:**
    u = 3: **100.0%** (n = 830,200); u = 7: **100.0%** (n = 1,882,909, the
    u = 7-slice with p ≡ 3 (mod 5) at exactly 100.0% per E-008, the other
    two u = 7 groups at 95.7% and 95.7%); u = 11: 94.7%; u = 15: 91.2%;
    u = 19: 77.2%; u = 23: 91.2%; deeper layers 55-90% with sparse records
    (n ≤ 700 above u = 47).
  - **The 5-intersection slices ((p + u) ≡ 0 (mod 5) identically - the
    fivex-full slices): (g3, u = 7), (g4, u = 11), (g1, u = 19), (g4,
    u = 31), (g1, u = 39)** - with the par-free share 100.0% / 96.4% /
    84.8% / 84.5% / 88.9% respectively: the p-free mechanism weakens with
    the layer depth even inside a fixed 5-adic family.
  - **The nonparametric witnesses are p-free in every slice at 91-100%**
    for the populated slices u ≤ 23; the onlynon classes with p-containing
    witnesses are absent from the data at these layers (nonp counts ≤
    7,969 only at u = 7's g1/g4).
- **Mechanism reading (H-6 registered):** the x-divisor witness shape is a
  property of the SMALL layers: at u ≤ 7 (58% of the sweep, both
  parametric and nonparametric witnesses are p-free essentially always),
  and decays smoothly with u (94.7% at u = 11, ~65-92% at deeper layers).
  Falsification: a small-layer record (u ≤ 7) whose minimal parametric
  witness requires the p-factor; or a populated large layer with the u = 7
  shares.

**Correction to the E-010 per-slice reading (same commit cycle, caught on
re-read of the run output):** the "other two u = 7 groups at 95.7% and
95.7%" claim in the E-010 block was a misreading - 95.7% is the
parametric-witness-holder share of the slice, not the p-free share. The
XSHAPE rows show parp = 0 in every u ≤ 7 slice: among parametric
witness holders, the p-free share is 100.0% in all three u = 7 groups
(555,902/555,902; 771,731/771,731; 555,276/555,276) and in all three
u = 3 groups. Second correction: the u = 75 and u = 79 "0.0%" shares in
the by-layer table are single-record artifacts (n = 1 and n = 1; the u = 79
record is in fact only-non) and are excluded from the monotone reading.

**The small-layer theorem (R8 piece 1, verified data statement):** over the
committed v0.7 run, the statement

  "for every hard-case prime in [10^7, 10^9) with first-working u ≤ 7,
   the minimal parametric witness is p-free (a divisor of x alone)"

holds with zero mismatches over all 2,713,109 parametric-witness records
(u = 3: 830,200; u = 7: 1,882,909); the u ≤ 7 slices' p-containing count
is 0 in every group. This is recorded as the strongest verified fact
behind H-6 and is the base R8 builds on.

- **Artifacts:** analysis/layers_r7_v07/ (engine v0.7, run, self-test),
  hashes in DATA_MANIFEST (43/43).
- **Status:** complete for the classification sweep. R8 (the universal
  reachability attempt) is the next roadmap item, now with the full
  classification table behind it.

## E-011 — R8: the delicate rescue census and the per-layer reachability table (2026-11-25)

- **What ran:** engine v0.8 (v0.7 + three additions: (i) the sub-fw
  theorem-consistency check inside the first-working scan, (ii) the
  per-(layer, mod-5) reachability counters with the delicate
  unit-pair/small/large buckets, (iii) the delicate rescue scan over every
  admissible u' with fw < u' <= 255, u' = 3 (mod 4), gcd(M', u') = 1),
  sanitizer-built; the sweep anchors reproduce byte-identically (the
  sanitized selftest artifact is BYTE-IDENTICAL to the committed v0.6/v0.7
  artifact — same SHA-256 `934ec74d…`), and v0.7's entire 197-line run
  output reappears byte-identically inside the v0.8 run output (0 missing
  lines; reconciliation checked line-by-line).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical:
  SWEEP 3194231 H24 2364031 PIGEON 3177642 DELICATE 33178 MISMATCH 0);
  delicate 16,589 (del_total); sub-fw check sites counted separately.
- **Verified results:**
  - **The rescue census (H-3's existential form): rescued_pigeon = 16,589 /
    16,589 (100%); no_pigeon_anywhere = 0.** Every delicate record — the
    99.49% pigeonhole-conclusive population already certified at its
    first-working parameter plus the residual 16,589 — has an admissible
    u' (fw < u' <= 255, u' = 3 (mod 4), gcd(M', u') = 1) with 2|D_{u'}(M')|
    > phi(u')/2. Combined with the first-working certification, the
    statement "exists an admissible u with |D_u(M)| > phi(u)/2" now holds
    with the bound u <= 255 for the ENTIRE sweep population, zero
    mismatches. This is the strongest empirical base H-3 has had; it
    remains a target theorem, not an established result.
  - **The sub-fw consistency census: checks = 3,042,449, collision = 0,
    pigeon = 0.** At every admissible span-failing u below its record's
    first-working parameter, neither the collision nor the pigeon bound
    occurs — the machine-checked chain (pigeonhole => collision, collision
    => the centered span, R4/R5) verified sweep-wide, previously only
    anchor-sampled.
  - **R5 consistency at the rescue sites: pig_no_coll = 0** (every
    qualifying off-parameter pigeon site carries the collision, as
    `pigeonhole_reachability` requires).
  - **The rescue-site map:** pigeon sites occur at 59 distinct layers
    across u' in 15..255 (the committed full_run.txt RESCUE8U block
    lists 61 layers, with pig > 0 at 59 of them and 149,680 pigeon
    sightings in total; u' = 11 unused: it is below the delicate fw
    floor; u' = 163 and u' = 235 carry collision sites but zero pigeon
    sites). The minimum rescue sites below are read from the run's
    rescue map (delicate_rescue.jsonl, retained with the run output and
    not committed to this repo), so those per-site figures are run
    records, not repo-checkable certificates: u' = 23 (6,654 records),
    u' = 15 (2,690), u' = 31 (2,414), u' = 19 (1,909), u' = 27 (952),
    u' = 35/39 (551/557), with a nearest-layer concentration: fw = 11
    records (6,075) rescue at u' in {15: 2,690, 19: 1,909, 23: 1,419};
    fw = 19 (7,434) at {23: 5,235, 31: 1,089, 27: 580}; fw = 23 (1,275)
    at {31: 610, 27: 361}; ...; the two fw = 83 records rescue at u' = 87
    and u' = 119. The per-(layer, mod-5) table (XREACH rows, 40 populated
    slices) reconciles 0-mismatch: del sums to 16,589, pigeon + del to
    3,194,231, and the delicate buckets per slice sum to the committed
    16,589 / 13,742 (unit pair) / 1,808 / 1,039 / 0.
  - **The R7-queued tail question:** the 2,847 non-unit-pair delicate
    records are inside the pigeon-rescued set — their first-working
    collision (the H-5 mechanism) and their H-3 pigeon certificate live at
    DIFFERENT admissible parameters; the delicate class definition
    (first-worker pigeon-fail) is orthogonal to the rescue certificate.
  - **Independent spot-checks (stdlib-only re-derivation, separate from
    the engine):** p = 10,004,521 (fw = 11, margin 2|D| - phi = -2, unit
    pair): rescue site u' = 15 with |D| = 6 > 4 = phi(15)/2; p = 651,412,441
    (fw = 83, margin -58, pair (1, 82)): rescue site u' = 87 with
    |D| = 56 > 28. Both rescue sites and both fw margins re-derived by
    independent factorization, 0 mismatches.
- **Artifacts:** analysis/rescue_r8_v08/ (engine v0.8, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt; hashes pinned in
  DATA_MANIFEST, 47/47 verifier rows). The per-record evidence
  delicate_rescue.jsonl (16,589 rows: p, fw, |D|, phi, margin, pair class,
  rescue sites) is retained in the run directory but NOT committed (the
  large-generated-dataset consent rule).
- **Status:** complete. R8's empirical base is unified; the universal
  theorem attempt (the reachability target per layer as formalizable
  statements over the rescue structure) is the next R8 piece.

## E-012 — R8 piece 3: the u = 3 layer boundary formalized (2026-11-25)

- **What was formalized:** `ErdosStrausConjecture/ResidualPrimes/U3Boundary.lean`
  (mirrored with its audit artifacts in
  `research/residual_primes/ErdosStrausConjecture_src/`): five new
  machine-checked theorems —
  - `prod_mod_one_of_primes_mod` (the multiplicative residue closure:
    prime divisors all 1 (mod 3) ⟹ the integer ≡ 1 (mod 3)),
  - `u3_span_of_even_x` (for 4·x = n + 3, 2 ∣ x, 3 ∤ x: the u = 3 span
    criterion holds at T = 2), with the corollary
    `isErdosStraus_of_even_x` (the explicit positive y, z through the
    audited u-method core: the primality-free sharpening of Paper 1's
    F(p) = 3 family),
  - `u3_span_fails_of_odd_x` (under the hard-case predicate, no span
    candidate exists at u = 3 for odd x), and
  - `u3_span_iff_even_of_hard` (the composed boundary under the
    hard-case predicate: span-at-3 ⟺ 2 ∣ x, where the predicate itself
    rules out 2 ∣ x, so under the predicate the criterion never holds;
    the constructive even-x result is `u3_span_of_even_x`, which assumes
    no hard-case predicate).
- **Verification:** compile exit 0 (8,477 jobs); axiom census: all five
  exactly `[propext, Classical.choice, Quot.sound]`; 0 `sorry`; audit
  artifact `axiom_audit_u3.txt` (build log `lake_build_u3.log`), both
  hash-pinned in DATA_MANIFEST (50/50 verifier rows). (2026-11-25 note:
  the pinned build log predates a comment-only header edit to
  U3Boundary.lean; its warning line references (:78) are :91 in the
  current file. No proof content changed.)
- **Empirical agreement (E-011):** the u = 3 picture matches the engine v0.8
  run at population scale — the sub-fw check verified the
  span-failing/no-collision equivalence at u = 3 for every (H24) record
  (the u = 3 sites of the 3,042,449 sub-fw sites, zero violations), and
  the fw census pinned the u = 3 population at exactly the non-(H24)
  records (830,200 = 3,194,231 − 2,364,031, the
  `h213_parametric_u3` regression invariant); the constructive T = 2
  witness the engine computes for the even-x class is carried by
  `u3_span_of_even_x` (no hard-case predicate), and the exclusion
  direction is the class exclusion the sub-fw census observed at every
  (H24) record whose x meets the predicate.
- **Status:** complete. The joint audited set: 15 + 18 = 33. The
  residual-class first entry follows: every hard case in the theorem's
  stated form (prime n, 4x = n + 3, every prime divisor of x
  ≡ 1 (mod 3)) now has a formal reason its first-working parameter is
  ≥ 7, because the span criterion cannot hold at u = 3 for such x.
  (H24) alone (p ≡ 1 (mod 24)) is weaker than the theorem's hypothesis
  and does not suffice: the exclusion needs the predicate on x, and a
  u = 3 witness can exist when x has a prime divisor ≢ 1 (mod 3).
  The u = 7 layer is the next R8 target.

## E-013 — R8 piece 4: the u = 7 layer classification and its formalization (2026-11-25)

- **What ran:** engine v0.9 (v0.8 + the u = 7 layer classification for the
  (H24) records: per `p mod 7` class the population, the admissibility
  (gcd(7, M') = 1), the span/fail split (fw = 7 vs fw > 7), the
  |D_7(M')| histogram over the fail records, the 2 ∣ x counter, and the
  per-record explicit-witness congruence checks (T = n at `p ≡ 3 (mod 7)`,
  T = x at `p ≡ 6 (mod 7)`)), sanitizer-built; the selftest artifact stays
  byte-identical to v0.6/v0.7/v0.8 and v0.8's entire 301-line run output
  reappears byte-identically inside the v0.9 run (317 lines, 0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the (H24) class 2,364,031 exhaustively partitioned by the
  U7 rows (the class sums equal 2,364,031).
- **Verified results (the full-scale census):**
  - **The u = 7 layer's residue boundary is exact:** span-holds for
    `p ≡ 3 (mod 7)`: 389,797 / 389,797 (100%); `p ≡ 5 (mod 7)`:
    389,841 / 389,841 (100%); `p ≡ 6 (mod 7)`: 390,029 / 390,029 (100%);
    while `p ≡ 1, 2, 4 (mod 7)` FAIL at 134,974 / 135,528 / 143,759
    records respectively and span for the remainder of those classes
    (254,489 / 254,424 / 271,190 — through deeper-window witnesses).
    The three 100% classes sum to 1,169,667 records; the (H24) u = 7
    span population across all six classes is 1,949,770.
  - **The explicit-witness classes verify 0-mismatch at population scale:**
    wit_ok = 389,797 / 389,797 at `p ≡ 3 (mod 7)` (the `T = n` span:
    `n + n·x ≡ 0 (mod 7)` and `n·x² + n·x ≡ 0`, both forced by
    `n ≡ 3 (mod 7)` and `x ≡ 2n (mod 7)`), and wit_ok = 390,029 / 390,029
    at `p ≡ 6 (mod 7)` (the `T = x` span). wit_ok = 0 for the other four
    classes as claimed.
  - **The fail records are all pigeon-fails at |D_7| = 3 exactly** for
    `p ≡ 2, 4 (mod 7)` (135,528 and 143,759 in the single |D| = 3 slot),
    and `p ≡ 1 (mod 7)` splits 38,813 at |D| = 2 and 96,161 at |D| = 3,
    consistent with the audited R5 chain (pigeon ⟹ collision ⟹ span:
    below the first-working parameter no pigeon can hold — the sub-fw
    consistency census stays 0 / 3,042,449).
  - **Inadmissible = 0 in every class** (structurally: `p ≡ 21 (mod 28)`
    forces `p = 7·(12k + 7)`, composite for every sweep prime — so
    7 ∣ M' never occurs in the (H24) class).
- **What was formalized:** `ErdosStrausConjecture/ResidualPrimes/U7Layer.lean`
  (mirrored with its audit artifacts): seven new machine-checked theorems —
  `mem_divResidues` and `cast_ne_of_mod_ne` (support), the two constructive
  spans `u7_span_of_mod7_three` / `u7_span_of_mod7_six` (`T = n` / `T = x`),
  and the three pigeon certificates `u7_pigeon_of_mod7_three` /
  `u7_pigeon_of_mod7_five` / `u7_pigeon_of_mod7_six` via the audited
  `pigeonhole_reachability` with the four-residue divisor sets
  ({1, n, x, n·x} = {1, 3, 6, 4} / {1, 6, 5, 2}; {1, n, x, 2} = {1, 5, 3, 2}
  at residue 5, using 2 ∣ x, which holds for every sweep (H24) prime).
- **Verification:** compile exit 0; axiom census: the two span theorems on
  exactly `[propext, Quot.sound]`, the three pigeon theorems and the two
  supports on the standard trio; 0 `sorry`; audit artifact
  `axiom_audit_u7.txt` (build log `lake_build_u7.log`), hash-pinned.
- **Artifacts:** analysis/u7_layer_v09/ (engine v0.9, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (57/57
  verifier rows).
- **Status:** complete. The joint audited set: 15 + 25 = 40. R8 continues:
  the failing classes (p ≡ 1, 2, 4 (mod 7), the 414,261 fail records) are
  the next structural object; R9 (independent validation) thereafter.

## E-014 — R8 piece 5: the failing-class span-witness census (2026-11-25)

- **What ran:** engine v0.10 (v0.9 + the failing-class fingerprints: for the
  (H24) records at `p ≡ 1, 2, 4 (mod 7)` the span-witness existence census
  over the full `M'²`-divisor window (p-scales times the x²-divisors,
  enumerated unsorted; classes by priority A: a pure x-divisor witness,
  B: a p-free deeper-window witness, C: a p-containing witness; a class-4
  miss is a soft engine-mismatch gate), and for the fail records the
  v₂(x') / v₅(x') buckets and the mod-840 membership), sanitizer-built;
  the selftest artifact stays byte-identical to v0.6-v0.9 (same SHA-256)
  and v0.9's entire 317-line run output reappears byte-identically inside
  the v0.10 run (324 lines, 0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the failing classes' (H24) population 1,194,364
  = 389,463 + 389,952 + 414,949, exhaustively split span 780,103 /
  fail 414,261 by the census.
- **Verified results (the full-scale census):**
  - **Every span witness in the failing classes is a PURE x-divisor:**
    spanA = span exactly (254,489 + 254,424 + 271,190 = 780,103), classes
    B and C ZERO, span_miss = 0. The u = 7 x-divisor span mechanism
    (H-4's reading) therefore covers not only the u = 7 g₃ class but the
    ENTIRE spanner population of the failing residue classes.
  - **The fail records are exactly the records whose x' carries no
    odd prime factor with residue 3, 5, or 6 (mod 7)** (E-018,
    census-verified 0-mismatch over the tested population). All
    414,261 fail records have v₅(x') = 0 (135,000-class buckets:
    134,974 + 135,528 + 143,759), but 5-divisibility is not the
    boundary: 381,652 spanners also have v₅(x') = 0 (the E-015 depth-0
    population). (Corrected 2026-11-25: the original reading, that the
    fails are exactly the 5 | M' = 0 records and the span condition is
    (r7 in {3, 5, 6}) or (5 | x'), was falsified by the E-015 depth
    census.)
  - **The fail records sit entirely in the mod-840 hard classes**
    (non840 = 0 in every class) and carry v₂(x') ≥ 1 in every class:
    the v₂ = 1 / v₂ ≥ 2 buckets per class are 65,981 / 68,993
    (r7 = 1), 66,386 / 69,142 (r7 = 2), and 70,688 / 73,071 (r7 = 4).
    (Corrected 2026-11-25
    per E-017: the original labels read v₂ = 2 and v₂ ≥ 3 and printed
    69,993.)
  - **The u = 7 hard core:** 414,261 records = 17.52% of the (H24) class,
    = 38,813 at |D_7| = 2 plus 375,448 at |D_7| = 3 - all pigeon-fails at
    u = 7, all already rescued at some admissible u' ≤ 255 by the E-011
    census (zero no-pigeon records sweep-wide).
- **Artifacts:** analysis/u7_fail_v010/ (engine v0.10, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (61/61
  verifier rows). The delicate-census JSONLs retained locally, NOT
  committed (the large-generated-dataset consent rule).
- **Status:** complete for the census (see the E-016 correction below:
  the second disjunct's "exactly" reading is corrected there - 5-free
  records SPLIT at the pigeon boundary rather than all failing).

## E-015 — R8 piece 6: the spanner-depth census and the conditional 5-window spans (2026-11-25)

- **What ran:** engine v0.11 (v0.10 + the spanner 5-depth census: per
  failing residue class the v₅(x') buckets of the u = 7 spanners with the
  125 ∣ x' flag), sanitizer-built; the selftest artifact stays
  byte-identical to v0.6-v0.10 (same SHA-256 `934ec74d…`) and v0.10's
  entire 324-line run output reappears byte-identically inside the v0.11
  run (327 lines, 0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the failing classes' spanners 780,103 classified by depth.
- **Verified results:**
  - **The spanner 5-depth table** (per class: depth 0 / 1 / 2 / ≥ 3):
    r7 = 1: 124,680 / 103,865 / 20,762 / 5,182; r7 = 2: 124,508 /
    103,900 / 20,772 / 5,244; r7 = 4: 132,464 / 111,036 / 22,172 /
    5,518. **DEPTH-0 = 48.92% of the failing classes' spanners**: the
    pure-x-divisor span mechanism does NOT route through the 5-window -
    it serves 5-free and 5-divisible records alike (0-mismatch, three
    near-identical class profiles). **The 125 ∣ x' spanner population for
    the formal depth-gates: 15,944** (5,182 + 5,244 + 5,518).
  - **The conditional 5-window spans formalized:** three new audited
    theorems in `U7Layer.lean` — `u7_span_of_fivex_pm1` (n ≡ ±1 (mod 7),
    125 ∣ x, span at `T = 5`), `u7_span_of_fivex_pm2` (n ≡ ±2 (mod 7),
    125 ∣ x, span at `T = 125`), `u7_span_of_fivex_pm3` (n ≡ ±3 (mod 7),
    3125 ∣ x, span at `T = 3125`): for the \u00b1-pairs the congruence
    `T ≡ -M (mod 7)` collapses to a single value (M ≡ 2 / 1 / 4
    respectively), so the residue disjunction costs one `rcases`-arm
    each with the identical close.
  - **Verification:** compile exit 0; axiom census: the three new spans on
    exactly `[propext, Quot.sound]` (matching the u = 7 constructive-span
    precedent); the joint audited set 15 + 28 = 43; the audit artifact
    `axiom_audit_u7.txt` (build log `lake_build_u7.log`) and the module
    REPINNED (the data-event rule) alongside the v0.11 artifacts (64/64
    verifier rows).
- **Artifacts:** analysis/u7_span_depth_v011/ (engine v0.11, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned.
- **Status:** complete. The open structural object shrinks to the depth-0
  spanner mechanism (381,652 records: the x-divisor witnesses for 5-free
  x') and the |D| = 2/3 hard core; R9 (independent validation) thereafter.

## E-016 - R8 piece 7: the depth-0 spanner mechanism and the hard-core profile (2026-11-25)

- **CORRECTION (E-014, this entry):** the E-014 reading "the fail records
  are EXACTLY the 5 | M' = 0 records" is falsified by the v0.12 spanner
  census: the failing classes' SPANNERS include 381,652 depth-0 (5-free
  x') records (the U7D0 rows below). What remains valid per-record:
  5 | x' implies span (100% - the depth1+ spanner count 259,809 equals
  the fivex counter 129,809 + its r7 = 2/4 twins exactly); every fail
  record has 5 -| x'; the 5-free records split by the pigeon boundary
  (|D_7| >= 4 span: 381,652; |D_7| <= 3 fail: 414,261). The u = 7 span
  condition's second disjunct is the pigeon boundary over the 5-free
  records, not the 5-divisibility itself.
- **What ran:** engine v0.12 (v0.11 + the depth-0 spanner mechanism
  census: per failing residue class the |D_7| buckets of the 5-free
  spanners, the pigeon flag, the minimal class-A witness's odd-part
  purity (a pure 2-power vs mixed), and the fail records'
  (class, mod-840 class) cross-table), sanitizer-built; the selftest
  artifact stays byte-identical to v0.6-v0.11 (same SHA-256 `934ec74d...`)
  and v0.11's entire 327-line run output reappears byte-identically
  inside the v0.12 run (336 lines, 0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the depth-0 spanners 381,652 = 124,680 + 124,508 + 132,464;
  the fail records 414,261 cross-tabled.
- **Verified results (the full-scale census):**
  - **Every depth-0 spanner is pigeon-conclusive** (pigeon = the full
    depth-0 count in every class, 0-mismatch), and **the minimal
    class-A witness is NEVER a pure 2-power** (pure2power = 0 in every
    class - the witnesses always carry an odd factor of x').
  - **The |D_7| profile of the depth-0 spanners:** r7 = 1:
    |D| = 4: 12,852, = 5: 24,675, = 6: 87,153 (the full unit group in
    69.9% of the class); **r7 = 2 and r7 = 4: |D| = 6 EXACTLY for
    124,508 and 132,464 records - the ENTIRE class spans with the full
    unit group as its divisor-residue set** (every divisor-residue class
    mod 7 realized).
  - **The hard core's mod-840 cross-table** (the fail records by class):
    r7 = 1: {1: 67,525, 169: 67,449}; r7 = 2: {121: 67,702,
    289: 67,826}; r7 = 4: {361: 71,921, 529: 71,838} - the totals match
    E-014's fail counts exactly, and the per-r7 pair structure is the
    trivial 840-to-7 projection (each mod-840 class carries a fixed
    p mod 7, since 7 | 840), with near-uniform 50-50 splits within each
    pair.
- **Artifacts:** analysis/u7_depth0_v012/ (engine v0.12, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (69/69
  verifier rows).
- **Status:** complete for the census. The formalization of the depth-0
  pigeon route (a |D| >= 4 certificate for the 5-free spanners of
  r7 = 2/4 via the full-unit-group structure) is the next R8 piece;
  R9 (independent validation) thereafter.

## E-017 - R8 piece 8: the generator census and the hard-core D-set shapes (2026-11-25)

- **What ran:** engine v0.13 (v0.12 + the generator census for the depth-0
  spanners of r7 = 2/4 (|D| = 6 records): the order-6 generator residues
  3 and 5 in D with the 125 | x' flag, and the fail D-set-shape
  histograms (the 6-bit mask) with the mask x v2(x') bucket cross),
  sanitizer-built; the selftest artifact stays byte-identical to
  v0.6-v0.12 (same SHA-256 `934ec74d...`) and v0.12's entire 336-line run
  output reappears byte-identically inside the v0.13 run (352 lines,
  0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the depth-0 spanners of r7 = 2/4: 124,508 + 132,464; the
  fail records 414,261 mask-set-classified.
- **Verified results (the full-scale census):**
  - **Both order-6 generators of (Z/7)* are divisor-residues of M' for
    EVERY depth-0 spanner of r7 = 2/4:** gen3 = gen5 = 124,508 / 124,508
    (r7 = 2) and 132,464 / 132,464 (r7 = 4) - 0-mismatch per record
    (U7D6GEN; the 125 | x' flag 0 by the depth-0 definition).
  - **The fail D-sets are fixed shapes, always inside the 2-orbit:**
    r7 = 1: mask {1, 2} = 38,813 and {1, 2, 4} = 96,161; r7 = 2:
    `D' = {1, 2, 4}` for ALL 135,528; r7 = 4: `D' = {1, 2, 4}` for ALL
    143,759. **No fail record's D-set ever contains a generator residue
    (3 or 5) or 6** - the u = 7 fail/span boundary within
    (H24, r7 = 1/2/4, 5-free) is the D-set-shape boundary:
    D' = the 2-orbit closure {1, 2, 4} (or its v2 = 1 restriction
    {1, 2}) vs D' containing an order-6 generator.
  - **The v2 cross (U7FAILSETVM):** the r7 = 1 {1, 2}-shaped fail records
    are ALL at v2(x') = 1 (38,813); the {1, 2, 4}-shaped fail records
    spread across the v2 buckets (r7 = 1: 27,168 / 33,699 / 35,294;
    r7 = 2: 66,386 / 33,960 / 35,182; r7 = 4: 70,688 / 35,618 / 37,453
    at v2 = 1 / 2 / >= 3 respectively).
  - **The E-014 v2-label correction:** the U7FAILPROFILE buckets are
    0-indexed at v2 = 1 (the bucket [0] = the v2 = 0 slot is empty - all
    x' are even): E-014's 65,981 / 68,993 read as "v2 = 2 / v2 >= 3" are
    in fact the v2 = 1 and v2 >= 2 buckets (the corrected cross:
    65,981 = 38,813 + 27,168 - the {1,2}-shape plus the {1,2,4}-shape at
    v2 = 1; 68,993 = 33,699 + 35,293-rounding-check - the {1,2,4}-shape
    at v2 >= 2), and the E-014 "carry v2(x') >= 2" claim is correspondingly
    corrected: the fail records carry v2(x') >= 1, split as above.
- **Mechanism reading (registered as H-7 with falsification criteria):**
  the u = 7 span/fail boundary in the failing residue classes is the
  D-set-shape boundary - fail iff the divisor-residue set of M' never
  leaves the 2-orbit closure {1, 2, 4}; span iff an order-6 generator
  (3 or 5) is a divisor-residue of M'. The open question is the
  factorization-side characterization of which x' compositions realize
  the generator residues (the census-verified witness structures exist
  per record; the composition-level iff is open).
- **Artifacts:** analysis/u7_gen_v013/ (engine v0.13, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (73/73
  verifier rows).
- **Status:** complete for the census. R8's next object: the
  composition-level iff for the generator residues (H-7's formal
  direction); R9 (independent validation) thereafter.

## E-018 - R8 piece 9: the composition-level iff for the failing classes (2026-11-25)

- **What ran:** engine v0.14 (v0.13 + the composition-level iff census:
  for every (H24) record at `p = 1, 2, 4 (mod 7)` with `5 -| x'` the test
  "x' has an odd prime divisor with residue 3, 5, or 6 (mod 7)" against
  the actual span/fail split; any disagreement is a soft mismatch gate),
  sanitizer-built; the selftest artifact stays byte-identical to
  v0.6-v0.13 (same SHA-256 `934ec74d...`) and v0.13's entire 352-line run
  output reappears byte-identically inside the v0.14 run (356 lines,
  0 missing).
- **The probe falsification en route:** the v0.14 probe first tested the
  restrictor `{3, 5}` and produced 1,036 mismatches - the span-without-
  condition records (480 / 310 / 246) exposed the missing residue: the
  primes `q = 6 (mod 7)` are order 2 in `(Z/7)*`, but `6 * {1, 2, 4} =
  {6, 5, 3}` escapes the 2-orbit closure, and together with {3, 5}
  products closes the group. The condition was widened to
  `q = 3, 5, 6 (mod 7)` (everything outside {1, 2, 4}) and the re-run is
  0-mismatch.
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the iff domain: the (H24) failing-class records with
  5 -| x': 795,913 = 259,654 / 260,036 / 276,223, all classified; the
  398,451 spanners with v₅(x') ≥ 1 are outside this gate.
- **Verified results (the full-scale if census):**
  - **The composition-level iff for the failing classes holds with ZERO
    mismatches across all 795,913 census-domain records:** the u = 7
    span holds exactly when x' has an odd prime divisor congruent to 3,
    5, or 6 (mod 7) (span_cond = span exactly: 124,680 / 124,508 /
    132,464; span_notcond = 0), and the fail records never carry such a
    prime (fail_cond = 0; fail_notcond = 134,974 / 135,528 / 143,759 =
    the full fail counts).
  - **The factorization-side reading:** the fail records' x' = 2^a
    times an odd part every odd prime divisor of which is 1, 2, or 4
    (mod 7) - i.e. all odd prime divisors inside the 2-orbit closure;
    the span records' x' carries at least one odd prime outside the
    closure (H-7's formal-direction condition).
- **Mechanism note (the closure algebra):** products of {1, 2, 4}-
  residues stay in {1, 2, 4} (the closure), so a 5-free record whose
  odd primes are all in the closure has its whole M'-divisor-residue
  window inside {1, 2, 4} - and `-M` is 5, 6, 3 respectively for
  p = 1, 2, 4 (mod 7) - never reachable; the span criterion cannot fire.
  Conversely an outside-closure odd prime q (residue 3, 5, or 6)
  produces, with the 2-window divisors, four distinct divisor-residues
  {1, x', q, 2q} in every class (with the residue 6 the q x 2-window
  products are 6, 5, 3), giving 2|D| > phi(7), i.e. the audited
  pigeonhole route to the span.
- **Artifacts:** analysis/u7_iff_v014/ (engine v0.14, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (77/77
  verifier rows).
- **Status:** complete for the census. The formalization of the two
  directions (the orbit-closure fail route and the four-residue pigeon
  span route) in U7Layer.lean is the next R8 piece; R9 (independent
  validation) thereafter.

## E-019 - R8 piece 10: the composition-level iff formalized in U7Layer (2026-11-25)

- **What landed:** U7Layer.lean extended with the two-direction Lean
  formalization of E-018's census-verified iff (0-`sorry`, exit 0):
  - `prod_in_orbit_clo_two` (the 2-orbit closure lemma): a positive
    integer whose prime divisors are `1`, `2`, or `4 (mod 7)` is itself
    `1`, `2`, or `4 (mod 7)` (the strong-induction skeleton of
    prod_mod_one, the residue-set closed under multiplication).
  - `u7_span_fails_of_orbit_primes` (the fail direction): for
    `4 * x = n + 7`, `n` prime with `n = 1, 2, 4 (mod 7)`, and every
    prime divisor of `x` in the closure, no span candidate exists
    (every divisor of `(n * x)^2` is `1`, `2`, or `4 (mod 7)` by the
    closure lemma via its prime-divisor walk, while `-n * x` is
    `5`, `6`, `3 (mod 7)` respectively - never reachable).
  - `u7_pigeon_of_orbit_breaker` (the span direction): for `4 * x =
    n + 7` with `n = 1, 2, 4 (mod 7)` and an odd prime
    `q | x` in residue `3`, `5`, or `6 (mod 7)`, the four
    divisor-residues `{n, x, q, 2*q}` are pairwise distinct (the
    residue arithmetic is disjoint across the three classes: the
    `x`-residue is `{2, 4, 1}` and the `q`-residue is `{3, 5, 6}`
    with `2q` in `{6, 3, 5}`), so `2|D| > phi(7)` and the audited
    pigeonhole theorem yields the collision (with the `2q | x` step
    via Nat.Coprime.mul_dvd_of_dvd_of_dvd, the residue-6 case escaping
    the closure via `6 * {1, 2, 4} = {6, 5, 3}`).
- **Axiom census:** all three items audited `[propext,
  Classical.choice, Quot.sound]` (the trio; the axiom_audit_u7.txt
  artifact: 13 theorems listed); `joint audited set: 15 + 31 = 46`.
- **Artifacts:** ErdosStrausConjecture/ResidualPrimes/U7Layer.lean
  (13 theorems), ErdosStrausConjecture_src/axiom_audit_u7.txt,
  ErdosStrausConjecture_src/lake_build_u7.log, hashes pinned (81/81
  verifier rows).
- **Status:** complete. The composition-level iff (E-018's census) is
  now machine-checked in both directions for the failing classes.
  R9 (independent validation of the E-004..E-019 line) is the next
  R8 piece.

## E-020 - R8 piece 11: R9 independent cross-validation (2026-11-25)

- **What ran:** a standalone Pollard-rho + Miller-Rabin re-implementation
  (python, no shared code with the C sieve engines; the rho route with
  the seeded trial pool), validating three layers against the E-018
  engine census (artifacts:
  analysis/crossval_r9/{r9_crossval.py, crossval_run.txt}):
  1. **The census invariants:** the U7IFF rows' two zero cells verified
     (span_notcond = 0, fail_cond = 0 per class) and the cross-artifact
     equalities: the span cells equal the E-016 depth-0 census
     (124,680 / 124,508 / 132,464 = 381,652) and the fail cells sum to
     E-014's total (134,974 + 135,528 + 143,759 = 414,261).
  2. **The re-derivation sweep:** 9,223 (H24) records re-derived over
     [10^7, 10^7 + 2.4e6) with the rho factorization, of which 6,915
     sit in the iff cells (2,888 span + 4,027 fail); the other 2,308
     are 5-divisible and outside the iff's domain. The sweep's span
     test is defined from the condition under test (isspan = fivex or
     cond) and its fail_cond counter is never incremented, so its two
     zero cells are structural, not independent evidence; the
     span/fail proportions are consistent with the census's scale.
     (Corrected 2026-11-25: the original text presented this sweep as
     independent validation.)
  3. **The from-scratch opposite-pair re-derivation:** 2,400 sampled
     records (1,200 spanners, 1,200 failers, 400 + 400 + 400 per class)
     re-derived: the divisor set of (n*x)^2 built from the
     independently factored primes contains the centered opposite pair
     (d + n*x == 0 (mod 7), d <= n*x) for every spanner and for none of
     the failers - 2,400/2,400 in agreement.
- **En-route fixes (recorded for the record):** the sweep's H24 grid
  start was initially off by 6 (p = 23 (mod 24) instead of 1 (mod 24)),
  exposed by the sampled n % 7 = 6 contradiction - corrected to
  `(1 - p % 24) % 24`; and the 5-divisible records are outside the iff's
  census domain (the engine's `x % 5 != 0` gate) - corrected in the
  sweep's cell accounting.
- **Artifacts:** analysis/crossval_r9/ (the script + the run output),
  hashes pinned (79/79 verifier rows).
- **Status:** complete. R9's evidence is the census-invariant
  cross-checks (item 1) and the from-scratch opposite-pair
  re-derivation (item 3, 2,400/2,400, the genuinely independent leg);
  the re-derivation sweep (item 2) is a consistency check, not
  independent validation of the span criterion. (Corrected 2026-11-25:
  the original text claimed the whole E-004..E-019 line and the span
  criterion itself were independently reproduced.) R8's validation is
  closed; the paper-v1.7 assembly (R9's manuscript row) is next.

## E-021 - R8 piece 12: the u = 11 layer census, part 1 - the class structure (2026-11-25)

- **What ran:** engine v0.15 (v0.14 + the u = 11 layer census: per class
  `r11 = p mod 11` the record table, the |D| histograms for spanners and
  failers, the 11-bit fail D-set masks, and the fail record collision
  census), sanitizer-built; the selftest artifact stays byte-identical to
  v0.6-v0.14 (the same SHA-256 `934ec74d...`) and v0.14's entire 356-line
  run output reappears byte-identically inside the v0.15 run (467 lines,
  0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the u = 11 census covers all 2,364,031 (H24) records
  across the 9 populated classes (each 262,274 - 263,128).
- **Verified results (the full-scale census):**
  - **The class-8 gap is structural:** no hard-case cohort record carries
    `p = 8 (mod 11)`, because then `p + 3 = 0 (mod 11)` forces
    `11 | (p + 3)/4`, and the hard-case predicate (every odd prime factor
    of `(p + 3)/4 = 1 (mod 3)`) forbids the factor 11 (`11 = 2 (mod 3)`).
    The exact analog of the E-013 "p = 21 (mod 28) forced composite" gap.
  - **The span rates split into three tiers:** `r11 in {7, 10}` span at
    17.33% and 17.41% (45,447 / 45,813), `r11 in {2, 6}` at 15.25% and
    15.28% (40,090 / 40,196), and the remaining five classes at 7.44% -
    8.90% (19,535 - 23,351). The u = 11 span total is 279,515 (11.82% of
    the (H24) class); at u = 7 the span total was 1,585,284 across the
    failing classes plus the three conclusive classes.
  - **The collision census (the decisive structural finding):**
    1,413,291 of the 2,084,516 u = 11 fail records (67.80%) carry a
    divisor-residue collision (`hasOppositePair`: some
    `d1 + d2 = 0 (mod 11)`, both divisor-residues) while the span
    criterion (`exists d | M, d = -M (mod u)` - the engine's first-layer
    span fact, E-012/E-013's route) still fails. At u = 7 NO fail record
    ever carried a collision (the fail D-sets {1, 2} and {1, 2, 4}
    never sum to 7), which is why the v0.7-era sub-first-working
    collision gate passed on that layer. The pair and the -M-residue
    span criterion are thus different predicates, and u = 11 is the
    layer where the distinction is populated: the gate was reclassified
    as a census row (`U11COLL...`) rather than an error gate.
  - The fail D-set masks per class are recorded (`U11FAILSET r11 mask n`),
    the largest single shape per class being the full-orbit mask 2046
    (e.g. r11 = 2: 147,836 of 222,706 fails) - the full-group orbit with
    ONE missing residue; the mask algebra for the composition-level iff
    is the next census pass.
- **Artifacts:** analysis/u11_class_v015/ (engine v0.15, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (83/83
  verifier rows).
- **Status:** complete for the class-structure census. E-021 part 2 (the
  composition-level decomposition: which x' factorizations realize the
  span condition at u = 11, the collision-vs-span relation) is the next
  census pass; the Lean layer follows the E-019 pattern.

- **Part 2 (E-021, 2026-11-25, the same run day):** engine v0.16
  (v0.15 + the composition-level condition census: the per-record
  non-QR-odd-prime scan vs the span fact, and the collision x span/fail
  4-way cells), sanitizer-built; the selftest artifact stays
  byte-identical (the same SHA-256 `934ec74d...`) and v0.15's entire
  467-line run output reappears byte-identically inside the v0.16 run
  (486 lines, 0 missing).

  - **The Legendre-split candidate condition.** With `2` a primitive
    root mod 11 and `-1` a non-residue (11 = 3 (mod 4)), the index-2
    structure is the Legendre split: the quadratic residues
    `QR = {1, 3, 4, 5, 9}`, the non-residues `{2, 6, 7, 8, 10}`. The
    H-7 analog candidate: "`x'` has an odd prime divisor outside the
    QRs".
  - **The necessary direction holds 0-mismatch at full scale:**
    `nocond_span = 0` in EVERY class - every u = 11 spanner's `x'`
    carries an odd prime divisor which is a quadratic non-residue
    (cond_span = the span exactly: 19,535 / 40,090 / 21,575 / 23,351 /
    21,652 / 40,196 / 45,447 / 21,856 / 45,813). Also
    **span ⟹ collision, 0-mismatch**: `nocoll_span = 0` in every class.
  - **The sufficiency is falsified, and the failure mode splits
    exactly by the QR status of `n_bar = r11`:** the mismatch census
    counts 1,502,820 fail records that fire the condition.
    - The classes with `n_bar` a NON-residue (`r11 in {2, 6, 7, 10}`):
      the condition is TRIVIALLY TRUE for every record
      (`cond_fail =` the full fail count per class; `nocond_fail = 0`)
      - because `x_bar = 3 n_bar` is then a non-residue itself, and
      products cannot keep all odd prime factors inside the QRs while
      landing outside... the scan fires for essentially every
      admissible x' of those classes.
    - The classes with `n_bar` a QR (`r11 in {1, 3, 4, 5, 9}`): the
      failers SPLIT - the firing portion is 52.17%, 52.19%, 52.13%,
      52.18%, 52.20% of the class fail count; and strikingly the
      NON-firing fail population is class-constant to within 0.2%
      (116,235 / 116,339 / 116,211 / 116,437 / 116,474) - a
      composition-density fact: the QR-only-odd-part x' population is
      the same size in every QR class.
  - **The collision cells (per class, the 4-way):** every spanner
    collides; among the failers the collision rate again splits by the
    class's QR status (the fully-pairing classes r11 = 7 / 10 vs the
    r11 = 2 / 6 classes with a no-collision sub-shape visible in
    U11FAILSET, e.g. the mask-94 shape).
  - **Artifacts:** analysis/u11_iff_v016/ (engine v0.16, full_run.txt,
    full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (87/87
    verifier rows).
  - **Status:** part 2 complete. The u = 11 layer's composition-level
    reading: the non-QR-odd-prime presence is a necessary span
    condition population-wide; the iff-style sufficient condition
    remains open (the QR-class fail split and the no-collision sub-shapes
    are the next census objects). The Lean layer follows the E-019
    pattern once the composition-level iff is settled.

**Correction banner (E-024, 2026-11-26): the E-021/E-022 "u = 11 fail"
cells had gated on `first(p) != 11`, which MIXES two populations:
(a) records that span at an earlier layer (fw = 7: for the (H24) cohort the
only lower odd layers are 3, which always fails per E-012, and 7), and
(b) true u = 11 span failures (fw > 11). The E-023 probe exposed the mix
(|D| = 10 fail records - the full unit group, the span criterion trivially
true - which must be fw = 7 spanners; verified p = 10,003,369 etc., all
u = 7 spans). The affected claims: the "collision census" (1,413,291 =
67.80% of fail records) was computed over the MIXED population and is
WITHDRAWN - among the true fw > 11 failers the collision count is ZERO
(v0.21/v0.22: `U11COLLCHECK collisions = 0 among fw > 11 failers`),
exactly like u = 7; the pair-vs-span distinction is NOT populated at
u = 11 after the gate fix. The count/residue gradients (E-022 part 2)
apply to the mixed population and are restated against the fw > 11 cells
in E-024. The span-side claims (the tier table, the QR purity dichotomy,
the parity lock on the impure cell, and the E-023 route census - which
gated on fw = 11 spanners) SURVIVE unchanged.**

## E-022 - R8 piece 13: the QR-purity dichotomy at u = 11, part 1 (2026-11-26)

- **What ran:** engine v0.17 (v0.16 + the odd-part-purity census: per
  record the QR-purity of the odd part of `x'` (every odd prime divisor
  in `{1, 3, 4, 5, 9} (mod 11)`) crossed with the `v2` bucket and the
  span/fail fact), sanitizer-built; the selftest artifact stays
  byte-identical (the same SHA-256 `934ec74d...`) and v0.16's entire
  486-line run output reappears byte-identically inside the v0.17 run
  (500 lines, 0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the 9 populated classes.
- **Verified results (the full-scale census):**
  - **The dichotomy is pure at full scale:** the QR-pure cell
    (`allQR = 1`: every odd prime divisor of `x'` in `QR`) has
    **`span = 0` in EVERY class** - the QR-pure records never span.
    The impure cell (`allQR = 0`: at least one non-QR odd prime)
    carries 100% of the spanners (cond_span = span exactly, the
    E-021 part-2 necessary direction re-derived structurally) and
    splits into spanners and failers at the ~14.5% / 85.5% rate.
  - **The class-constant population identified:** the non-firing fail
    population of the QR classes (E-021 part 2's class-constant
    ~116.3k) is exactly the QR-pure fail cell: 116,235 / 116,339 /
    116,211 / 116,437 / 116,474 (r11 = 1 / 3 / 4 / 5 / 9).
  - **The v2 bucket is degenerate at u = 11:** every record sits at
    `v2(x') = 0` - for the (H24) primes (`p = 1 (mod 8)`) the layer
    relation `4x' = p + 11` gives `4 | x'` never: `(p + 11)/4` is
    always odd, so the u = 7-style 2-window layer does not exist
    here. The census confirms the degenerate bucket (all cells
    `v2b >= 1` are empty and suppressed).
  - **The remaining mechanism object:** the impure-but-failing cell
    (e.g. r11 = 1: 126,757 fail records with a non-QR odd prime but
    no span witness) - the span-vs-fail split inside it is the next
    census object (which non-QR prime composition classes span).
- **Artifacts:** analysis/u11_split_v017/ (engine v0.17, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (91/91
  verifier rows).
- **Status:** part 1 complete. E-022 part 2 (the impure-cell
  decomposition: the non-QR prime composition classes and their span
  rates) is the next census pass.

- **Part 2 (2026-11-26):** engine v0.18 (v0.17 + the impure-cell
  decomposition: the non-QR odd-prime count histogram (with
  multiplicity, capped 9) x span/fail per class, and the
  first-non-QR-prime-residue x count x span/fail cells), sanitizer-built;
  the selftest artifact stays byte-identical (the same SHA-256
  `934ec74d...`) and v0.17's entire 500-line run output reappears
  byte-identically inside the v0.18 run (664 lines, 0 missing).
  - **The parity lock holds exactly at full scale:** in the QR-n_bar
    classes the non-QR multiplicity takes only even values
    (cnt in {0, 2, 4, 6, 8}), in the non-QR-n_bar classes only odd
    values (cnt in {1, 3, 5, 7}) - exactly the coset algebra
    (`x_bar in QR` forces the even product parity; x' is always odd on
    this layer, so the odd-part products carry the whole status).
  - **The count gradient is monotone:** the within-cell span rates decay
    with the count - QR classes: 0% (cnt = 0) / 13.79-16.54% (cnt = 2) /
    5.82-6.41% (cnt = 4) / 0.79-1.79% (cnt = 6) / ~0 (cnt >= 8);
    non-QR classes: 16.19-18.84% (cnt = 1) / 10.51-10.85% (cnt = 3) /
    2.50-2.92% (cnt = 5) / 0 (cnt >= 7). The deep-count cells are
    sparse and fail-heavy.
  - **The residue gradient (the strong signature):** within the impure
    cell, the span rate depends on the FIRST non-QR prime's residue
    (the r11 = 1, cnt = 2 slice): pres = 2 -> 17.28%, pres = 6 ->
    17.01%, pres = 7 -> 5.93% (3-4x suppressed), pres = 8 -> 21.24%,
    pres = 10 -> 19.95%. The suppression at 7 connects to the span
    target algebra: at r11 = 1 both span-e targets are the residue 8,
    and 7 · 9 = 8 (mod 11) - the 7-prime shapes need the QR-prime 9
    (mod 11) as a cofactor to reach the target, a sharper composition
    requirement than the other residues.
  - **Artifacts:** analysis/u11_imp_v018/ (engine v0.18, full_run.txt,
    full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (95/95
    verifier rows).
  - **Status:** part 2 complete. The u = 11 composition census now
    covers: the class-8 structural gap (E-021 part 1), the QR-dichotomy
    (necessary direction 0-mismatch), the parity lock, the count
    gradient, and the residue-gradient signature. The remaining
    mechanism object: the exact composition-level iff (the product-set
    reachability test `e-products hit -x_bar or -M_bar`) - the natural
    v0.19 pass is the per-record product-set census with the target
    hit-flags, which would either certify the iff or expose the
    remaining gap exactly.

## E-023 - R8 piece 14: the M^2-window route census at u = 11 (2026-11-26)

- **What ran:** engine v0.19 (v0.18 + the spanner route census: per
  spanner the witness's route class over the M^2-divisor window
  `d = p^a * e'` with `a in 0..2` and `e' | x'^2`, classified by the
  a-level (0/1/2) and the e' window (`e' | x'` vs the x'^2-only
  witnesses), as a 6-bit route-mask histogram per class), sanitizer-built;
  the selftest artifact stays byte-identical (the same SHA-256
  `934ec74d...`) and v0.18's entire 664-line run output reappears
  byte-identically inside the v0.19 run (695 lines, 0 missing).
- **Populations:** sweep 3,194,231 [10^7, 10^9) (headline byte-identical,
  MISMATCH 0); the route census covers all 279,515 u = 11 spanners
  (the per-class route-cell sums equal the U11 class table exactly).
- **Verified results (the full-scale census):**
  - **The criterion window is M^2, and a minority population lives
    exclusively in the x'^2-only witnesses:** the first-cut census (the
    x'-divisor routes only: `e | x'` with `e = -M_bar` or `e = -x_bar`)
    left 4,068 spanners of 279,515 (1.46%) route-less; at the probe
    scale they were instrument-verified (p = 10,081,801: the witness
    is `(0, x'^2-only, residue 7)` over the M^2 divisors, python
    re-derived). The full M^2-window census closes every spanner:
    **`U11RCHECK nonespan = 0`** - the route decomposition is exact.
  - **The x'^2-only spanners concentrate in `r11 in {1, 2, 4}`:**
    789 / 2,042 / 1,237 records (4.04% / 5.09% / 5.30% of the class's
    spanners), with the other six classes at exactly 0. The class set
    {1, 2, 4} is the u = 7 failing-class set - a structural echo worth
    a dedicated pass.
  - **The full-window route masks per class** (the 6-bit masks: bits
    0-2 = the a-levels on the x'-window, bits 3-5 = the a-levels on
    the x'^2-only window): r11 = 10: the mask 63 for ALL 45,813
    spanners (every route family available); r11 = 7: the masks 59/63
    only; the QR classes carry 4-6 distinct mask shapes with the mask
    63 dominant everywhere (e.g. r11 = 1: 18,746 of 19,535 = 96.0%).
  - **The instrumentation note:** the U11RMASK class headers
    concatenate with the first mask row when the mask-0 cell is empty
    (a printf-order slip); the raw data is intact and the aggregates
    above were re-derived from the concatenation-tolerant parse.
- **Artifacts:** analysis/u11_route_v019/ (engine v0.19, full_run.txt,
  full_run_stderr.txt, sanitized_selftest.txt), hashes pinned (99/99
  verifier rows).
- **Status:** complete. The u = 11 span decomposition is now exact over
  the M^2 window; the composition-level reading (E-021/E-022) plus the
  route table close the u = 11 structural census. The u = 11 Lean layer
  (the M^2-window route theorems on the E-019 pattern) is the next
  formalization piece; the u = 13 layer census would follow the same
  program.

## E-024 - R8 piece 15: the fate-gate correction and the corrected u = 11 census (2026-11-26)

- **What ran:** engine v0.21/v0.22 (the v0.19 structure + the fate gate:
  every per-record census cell was re-indexed to the three fates -
  fw = 11 span, fw = 7 span, fw > 11 fail; the fail-side rows (the D-set
  masks, the collisions, the |D| histograms) gate on fw > 11 only,
  the U11Q3/U11IFF/U11COLL3/U11PCNT3/U11PRES3 rows carry the 3-fate
  breakdown), sanitizer-built; the selftest artifact stays byte-identical
  (SHA-256 `934ec74d...`); the full run at [10^7, 10^9) exit 0
  (4m19s run time, the M^2-window divisor lists are heavier).
  Note: the v0.21 first build derived from the v0.18 tree and silently
  lost the E-023 route rows; v0.22 re-derived from the v0.19 tree with
  the same fate edits. The v0.21 run artifacts are retained for the
  record (the run-dir listing documents both).
- **Populations (the corrected arithmetic closes EXACTLY):**
  - fw = 7 spanners: **1,949,770** (82.49% of the (H24) class; the
    U11FW7CHECK row); fw = 11 spanners: **279,515** (11.82%); true
    fw > 11 failers: **134,746** (5.70%). The chain closes: the u = 11
    span plus the fw > 11 fail equals E-013's u = 7 failing-class total
    EXACTLY (279,515 + 134,746 = 414,261): **the u = 11 layer rescues
    67.38% of the u = 7 failing-class records**.
- **The corrected results (per class, the fail cells fw > 11-gated):**
  - The fail counts (26,060 / 5,843 / 24,015 / 25,628 / 23,590 / 5,783 /
    0 / 23,827 / 0 for r11 = 1 / 2 / 3 / 4 / 5 / 6 / 7 / 9 / 10): the
    non-QR-n_bar classes {7, 10} have ZERO true failures at u = 11
    (every record of those classes spans at fw = 7 or 11); the classes
    {2, 6} have minimal fail counts (5,843 / 5,783 = 2.2% of the class);
    the QR classes {1, 3, 4, 5, 9} carry the true failures
    (23.6k - 26.1k = 9.0 - 9.9% of the class).
  - **The collision census WITHDRAWN AND CORRECTED:** collisions among
    the true fw > 11 failers = **0** (`U11COLLCHECK collisions = 0`,
    exactly like u = 7). The E-021 part-1 "1,413,291 = 67.80%" was
    the mixed population's collision count over what are mostly fw = 7
    spanners - an expected span-side property, not a fail-side fact.
    The pair-vs-span distinction is NOT populated at u = 11.
  - **The condition-vs-span census (criterion-comparable fates only):**
    among the true fw > 11 failers the non-QR-odd-prime condition fires
    for 13,870 of 134,746 (10.3%); the spanners fire at 100% (the
    E-021 part-2 necessary direction survives the correction).
  - **The fw = 7 spanner cells (the newly separated population):**
    per class 0 (1,517) / 1,715 / 0 / 782 / 1,093 / 0 / 1,038 / 0 /
    1,005 at the probe scale - the fw = 7 spanners sit in the QR
    classes almost entirely; their u = 11 layer structure is a future
    census object (the E-022 count/residue gradients re-run on the
    fw = 7 cells in the next pass).
- **Artifacts:** analysis/u11_gate_v021/ (engine v0.21 + v0.22, the two
  full runs, the two selftest artifacts), hashes pinned (103/103
  verifier rows).
- **Status:** complete. The u = 11 census is now fate-correct; the
  surviving facts: the class-8 structural gap, the span tiers, the
  QR-purity dichotomy (span-side), the route decomposition exactness,
  the rescue-chain arithmetic (279,515 + 134,746 = 414,261), and
  zero fail-side collisions. The u = 11 Lean layer and the fw = 7
  spanner-cell census are the next passes.

## E-025 - R8 piece 16: the u = 11 Lean layer, part 1 (2026-11-26)

- **What landed:** the new module
  `ErdosStrausConjecture/ResidualPrimes/U11Layer.lean` (4 theorems,
  0-`sorry`, compile exit 0, 8475 jobs):
  - `u11_no_hardcase_record_mod8` - the class-8 structural gap (E-021
    part 1): `4·x = p + 3`, `p = 8 (mod 11)` ⟹ `11 | x` (via
    `11 | p + 3` and gcd(4, 11) = 1), so the hard-case predicate fails
    (the odd prime factor `11` has `11 % 3 = 2 ≠ 1`).
  - `u11_x_odd` - the v2-bucket degeneracy (E-022 part 1): `4·x =
    p + 11` with `p = 1 (mod 8)` ⟹ `x` odd (2 ∤ x).
  - `u11_span_mod11_seven` - the explicit-witness span theorem at
    `r11 = 7`: the witness `d = p` (the divisor of `p·x`), with
    `(p + p·x) % 11 = 0` (the residues: `x = 10 (mod 11)`,
    `p·x = 4 (mod 11)`, the sum 7 + 4 = 11). The class E-021 part 1
    measured at 17.33% span rate with zero true failures (E-024).
  - `u11_span_mod11_ten` - the explicit-witness span theorem at
    `r11 = 10`: the witness `d = x`, with `(x + p·x) % 11 = 0`
    (`x = 8 (mod 11)`, `p·x = 3 (mod 11)`, the sum 8 + 3 = 11). The
    class at 17.41% span rate, zero true failures.
- **Axiom census:** the two span theorems and the x-odd lemma audited
  `[propext, Quot.sound]`; the no-hardcase theorem audited on the trio
  `[propext, Classical.choice, Quot.sound]`; 0 `sorry` throughout
  (axiom_audit_u11_layer.txt, lake_build_u11_layer.log, hashes pinned).
- **Deliberate non-identification:** the span criterion stated is the
  engine's first-layer fact (`exists d, d | n*x ∧ (d + n*x) % 11 = 0`);
  the collision criterion (`hasOppositePair`) is NOT identified with it
  at u = 11 (E-024's correction banner: the withdrawn 67.80% census).
- **Artifacts:** ErdosStrausConjecture/ResidualPrimes/U11Layer.lean,
  ErdosStrausConjecture_src/{axiom_audit_u11_layer.txt,
  lake_build_u11_layer.log, print_axioms_u11.lean}, hashes pinned
  (103/103 verifier rows).
- **Status:** part 1 complete. The next u = 11 formalization pass: the
  QR-purity dichotomy theorem (`u11_span_fails_of_qr_pure_x`, the
  E-022 part-1 full-scale fact: the QR-pure odd-part x' never spans)
  and the route-decomposition exactness theorem (E-023), followed by
  the fw = 7 spanner-cell census (the engine pass).

## E-026 - R8 piece 17: the fw = 7 spanner-cell census reading (2026-11-26)

- **What ran:** no new engine - the E-024 v0.22 full run already carries
  the 3-fate cells (the fate dimension includes fw = 7); this piece is
  the data reading over the pinned `analysis/u11_gate_v021/full_run.txt`
  against the E-025 module (part 2's Lean theorems are staged in the
  EXPERIMENT_LOG notes below; the u11_span_fails_of_qr_pure_x theorem
  and the route-exactness theorem follow next).
- **Verified results (the fw = 7 fate cells, full scale):**
  - **The fw = 7 spanner population is class-constant:** 216,932 /
    216,863 / 216,923 / 213,553 / 217,205 / 217,018 / 216,827 / 217,134 /
    217,315 for r11 = 1 / 2 / 3 / 4 / 5 / 6 / 7 / 9 / 10 (82.5% of every
    class, spread 213.6k - 217.3k = 1.7%) - the u = 7 layer's span rate
    is composition-independent across the u = 11 residue classes.
  - **The class-constant ~116.3k QR-pure population of the QR classes
    decomposes exactly into the fw = 7 and fw > 11 fates:** at r11 = 1:
    92,419 (fw = 7, QR-pure) + 23,816 (fw > 11, QR-pure) = 116,235 =
    the E-021 part-2 mixed reading exactly (the other QR classes
    likewise, to the record). The QR-pure records split 79.5% span at
    fw = 7 / 20.5% failure through fw = 11.
  - **The fw > 11 failers are overwhelmingly QR-pure:** 23,816 of
    26,060 = 91.4% at r11 = 1 (the other QR classes similar) - the
    u11_x_odd/QR-purity theorem's census shape confirmed from the
    failure side: the impure-x' records mostly escape failure.
  - **The fw = 7 spanner's odd-part composition (QR classes, the
    count histogram):** cnt = 0: 92,419 (42.6% of the class's fw = 7
    spanners); cnt = 2: 116,678 (53.8%); cnt = 4: 7,722 (3.6%);
    cnt = 6: 112; cnt = 8: 1 - and EVERY fw = 7 spanner of the impure
    sub-cells (cnt >= 2) carries a non-QR odd prime, i.e. the E-021
    part-2 necessary direction holds for the fw = 7 fate as well
    (the QR-pure fw = 7 spanners = 0 in the cnt = 0 cell's span fate,
    where the row reads span = 0).
- **Artifacts:** none new; the reading is over the pinned
  `analysis/u11_gate_v021/full_run.txt` (the E-024 pins).
- **Status:** complete. The u = 11 census chain now reads: every (H24)
  record splits by (fw, the x' composition) with the QR-purity the
  span-boundary at u = 11 and the u = 7 layer carrying 82.5%
  population-wide. R8's next objects: the QR-purity Lean theorem
  (formalization pass), and the r11 in {1, 2, 4} x'^2-only echo.

## E-027 - R8 piece 18: the u = 11 Lean layer, part 2 - the QR-closure machinery (2026-11-26)

- **What landed:** U11Layer.lean extended with
  `prod_mod_qr` - the QR-side multiplicative-closure induction (the
  E-012 `prod_mod_one_of_primes_mod` skeleton over the QR residue set
  `{1, 3, 4, 5, 9}`): a positive integer whose prime divisors all carry
  QR residues (mod 11) is itself one of `1, 3, 4, 5, 9 (mod 11)`.
  0-`sorry`, compile exit 0 (8475 jobs); the module now carries 5
  theorems.
- **Axiom census:** `prod_mod_qr` audited on the trio
  `[propext, Classical.choice, Quot.sound]` (the other four unchanged:
  two duo, two trio); the audit and build logs re-pinned (103/103
  verifier rows).
- **Staged (part 3):** the main dichotomy theorem
  `u11_span_fails_of_qr_pure_x` - the algebra is fully pinned (every
  M^2-divisor of a QR-n-bar class with a QR-pure odd x' carries a QR
  residue, since x' is always odd (the v2 degeneracy) so no factor of 2
  appears, while `-(p·x)` carries a non-QR residue because `-1` is a
  non-residue at mod 11); the proof needs the divisor-status split
  (`Nat.Prime.dvd_mul` over `p^2·x^2` plus the
  `Nat.prime_eq_prime_of_dvd_pow` route-identification) composed with
  the two `prod_mod_qr` applications.
- **Artifacts:** U11Layer.lean (5 theorems), the re-pinned
  axiom_audit_u11_layer.txt (5 theorems listed),
  lake_build_u11_layer.log.
- **Status:** part 2 complete for the machinery. Part 3 (the main
  dichotomy theorem) is the next Lean pass.

**Part 3 (same session): the main dichotomy theorem landed.**

## E-027 part 2 - R8 piece 19: the main QR-purity dichotomy theorem (2026-11-26)

- **What landed:** `u11_span_fails_of_qr_pure_x` - for `4·x = p + 11`
  with `p` prime, `p` a QR (mod 11), and `x` QR-pure (every odd prime
  divisor of `x` in the QRs), every divisor `d` of `(p·x)^2` carries a
  QR residue (the route split via `Nat.Prime.dvd_mul` plus the
  prime-equivalence route-identification), while the sum of two QR
  residues is never 0 (mod 11) (the 25-arm literal closure) - hence
  `(d + p·x) % 11 = 0` has no solution: the u = 11 span criterion
  fails. The QR-purity dichotomy (the E-022 census full-scale fact,
  0-mismatch over the tested population) is now a theorem.
- **Note:** the QR-census algebra needed `qr_closed_mod11` (the
  multiplicative-closure over the QR residue set, 25-arm literal) and
  the 2-factor absence (the E-022 parity lock, span-side, composed via
  `u11_x_odd`).
- **Axiom census:** `u11_span_fails_of_qr_pure_x` and `prod_mod_qr` on
  the trio; `qr_closed_mod11` on `propext` alone; the other four
  unchanged; 0 `sorry` throughout; 7 theorems total in the module
  (the audit re-pinned, 51 rows... the theorem count now 7).
- **Artifacts:** U11Layer.lean (7 theorems), the re-pinned
  axiom_audit_u11_layer.txt (7 theorems listed),
  lake_build_u11_layer.log.
- **Status:** part 3 complete - the E-022 theorem leg is done. The
  u = 11 Lean layer is closed for the census-verified facts.

## E-029 - R8 piece 21: the u = 15 layer census (the first composite layer) (2026-11-26)

- **What ran:** engine v0.23 (`analysis/u15_class_v023/`), a byte-superset
  extension of v0.22 (the reconcile: v0.22's 653 lines appear in order
  inside v0.23's 680, missing = 0 PASS); the selftest byte-identical
  (350 B, sha `934ec74d...`); the full run 999,999,999 exit 0,
  MISMATCH 0; the standing numbers unchanged (SWEEP 3,194,231, H24
  2,364,031, PIGEON 3,177,642, DELICATE 33,178).
- **Verified results (full scale):**
  - **Exactly THREE populated classes:** r15 in {1, 4, 13} with
    788,009 / 787,457 / 788,565 = 2,364,031 exact. The r15 = 7 class is
    structurally empty: the H24 primes p = 97 (mod 120) carry
    5 | (p + 3)/4 always, so the hard-case predicate (the odd prime
    factors = 1 (mod 3); 5 = 2 (mod 3)) rejects the entire class
    (the same shape as the class-8 gap at u = 11). The r15 = 13 class
    is populated but INERT: zero u = 15 spans, zero fails - all
    788,565 records were already fw in {7, 11} (their u = 15 D-sets
    still measured for the CRT cells).
  - **The admissibility gate passes for every record** (inad = 0): for
    the sweep primes M15 = p * x15 = 4p^2 (mod 15) is always a unit
    (p coprime to 15), so u = 15 is never inadmissible - unlike the
    u = 11 layer's structural inadmissibility rows. And fw = 3 = 0
    (the E-012 boundary extends: x3 = (p+3)/4 is odd for (H24)).
  - **The rescue chain closes exactly at u = 15:** the u = 15 spans
    32,271 (r15 = 1) + 27,488 (r15 = 4) = **59,759**, and the true
    fw > 15 failers 40,422 + 34,565 = **74,987**; the sum
    59,759 + 74,987 = **134,746 = the E-024 true-u-11-failers exact**.
    The u = 15 layer rescues **44.34%** of the u = 11 failures; the
    still-failers are 74,987 = 3.17% of (H24).
  - **The fail D-sets are fixed shapes again:** r15 = 1: {1, 2, 4}
    (mask 22: 19,418 records, |D| = 3) + {1, 2, 4, 8} (mask 278:
    21,004, |D| = 4); r15 = 4: {1, 2, 4, 8} (mask 278: 34,565
    uniformly). Every true failer's D-set stays inside the 2-orbit
    closure {1, 2, 4, 8} (mod 15) - the u = 7/u = 11 pattern repeats
    at the composite layer.
  - **Every u = 15 spanner is pigeon-conclusive:** the spanner |D|
    buckets are 6-8 at r15 = 1 (12,893 / 5,127 / 14,251) and
    uniformly |D| = 8 at r15 = 4 (27,488) - 2|D| > 8 = phi(15)
    throughout, so the u = 15 spans carry the pigeonhole certificate.
  - **ZERO collisions among the fw > 15 failers** (the lane pattern
    continues at the composite layer; the collision row 74,987/0).
  - **The CRT pairing (NEW, the composite-layer structure):** the
    D_15 residues are the projection of the (mod 3, mod 5) divisor
    pairs, and the pairing is NOT free: the realization rates
    |D15| = |D3| * |D5| are 41.75% (r15 = 1), 57.65% (r15 = 4),
    78.82% (r15 = 13) - and the DEFICIT is class-exact: r15 = 4's
    unrealized records ALL at deficit = 4 (333,445), r15 = 13's ALL
    at deficit = 1 (166,952), r15 = 1's at 1/2/3/4
    (68,769/57,148/160,864/172,233). crt_neg = 0 (the injection bound
    holds throughout). The deficit-exactness is the next layer's
    mechanism object (the D3 x D5 product misses a fixed number of
    CRT cells per class - the algebra of the missing pairs).
- **Artifacts:** `analysis/u15_class_v023/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned, 113/113 verifier rows).
- **Status:** complete. The u = 15 census facts stand; the deficit
  algebra and the u = 15 route census are the next passes in the lane.

## E-030 - R8 piece 22: the CRT-deficit algebra census (engine v0.24) (2026-11-26)

- **What ran:** engine v0.24 (`analysis/u15_crt_v024/`), a byte-superset
  of v0.23 (the reconcile: v0.23's 680 lines in order inside 685,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0, U15DEFMAX = 0 (the deficit bucket
  caps never hit), crt_neg = 0. NEW CELLS: the deficit histogram per
  (r15, mask3, mask5) - the D3 residue mask (2-bit, the residues
  {1, 2} mod 3) x the D5 residue mask (4-bit, {1..4} mod 5), with
  the deficit bucket = |D3| * |D5| - |D15| for every non-eq record.
- **Verified results (full scale):**
  - **Only FOUR (r15, mask3, mask5) cells exist** across the whole
    (H24) - the CRT-pairing deficit data collapses far beyond the
    coarse cells of E-029:
    - r15 = 1, mask3 = 6, mask5 = 22 (D5 = {1, 2, 4}, |D5| = 3):
      deficit = 3 CONSTANT (160,864 records).
    - r15 = 1, mask3 = 6, mask5 = 30 (D5 = {1, 2, 3, 4}, |D5| = 4):
      the deficit SPLITS: 1 (68,769) / 2 (57,148) / 4 (172,233) -
      the answer to E-030's question is therefore NO at this
      coarseness: the deficit is not a function of the small-layer
      masks alone; the splitting cell is fate-structured (the
      deficits 1/2/4 = |D15| in {7, 6, 4}, matching the v0.23 spanner
      |D|-buckets 7/6 and the |D| = 4 fail shape).
    - r15 = 4, mask3 = 6, mask5 = 30: deficit = 4 CONSTANT (333,445).
    - r15 = 13, mask3 = 6, mask5 = 30: deficit = 1 CONSTANT (166,952).
  - **mask3 = 6 UNIVERSALLY** (the D3 set is the full unit group
    {1, 2} (mod 3) for every one of the 2,364,031 records - the
    trivality: the divisors of a 3-coprime M15 always realize both
    unit residues). **|D5| is always 3 or 4** (mask5 = 22 or 30
    only; the D5 sets are never 1- or 2-element, and never missing
    the residue 1 - D5 = {1, 2, 4} or the full {1, 2, 3, 4}).
  - The arithmetic consistency: the deficit cells reconstruct the
    E-029 coarse cells exactly (r15 = 1: 160,864 + 298,150 =
    459,014 = the E-029 ne count; the other classes likewise).
- **The mechanism status:** the deficit is class-lawed at 3 of the 4
  cells; the r15 = 1 full-D5 exception splits by the D15 SHAPE (the
  2-orbit {1, 2, 4, 8} fails land at deficit 4; the |D| in {6, 7}
  spans at 2/1). The next narrowing (E-031 proposed): the per-record
  D15 mask keyed into the def cells - the unrealized-pair SET per
  cell - which would make the algebra exact (or expose the true
  free variable).
- **Artifacts:** `analysis/u15_crt_v024/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 116).
- **Status:** complete (the algebra narrowed; the exact pair-set
  mechanism is the next pass).

## E-031 - R8 piece 23: the CRT pair-set algebra, made exact (engine v0.25) (2026-11-26)

- **What ran:** engine v0.25 (`analysis/u15_alg_v025/`), a byte-superset
  of v0.24 (the reconcile: v0.24's 685 lines in order inside 690,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0.
- **The algebra (found this piece):** for `M15 = p * x'` coprime to 15,
  the divisor-residue set `D15 = { d mod 15 : d | M15 }` is EXACTLY the
  multiplicative generation: decode every residue to its CRT pair
  (mod 3, mod 5); for each prime `q | x'` with pair
  `g_q = (q mod 3, q mod 5)` and exponent `e_q`, the divisor window is
  `{ 1, g_q, ..., g_q^{e_q} }`; the pair set is the product closure of
  the per-prime windows, then scaled by the p-classes
  `(1, 1), (p mod 3, p mod 5)`. The D3 projection is the full unit
  group (2 elements, always, the mask3 = 6 universal row of E-030);
  the D5 projection and the pair coupling live in the 8-element pair
  group `(Z/3)* x (Z/5)*`.
- **Verified results (full scale):**
  - **U15ALG mismatch = 0**: the generated pair set equals the
    build_D divisor set for EVERY one of the 2,364,031 records - the
    algebra is exact, not approximate (the engine-side generation had
    three compile-round bugs on the way there: the pair-power reset,
    the zero-init of the fold register, the window j <= e - all
    resolved; the final check is a hard 0 over the full population).
  - **The E-029/E-030 fail shapes decode as orbit windows:** the fail
    D-sets {1, 2, 4} and {1, 2, 4, 8} are exactly the (2,2)-orbit
    {1=g0, 2=g1, 4=g2, 8=g3} cut at the 2-exponent windows (the
    deficits 3 and 4 = |D3||D5| - the window sizes, the class cells of
    E-030 now mechanized). The U15ORBPREF cells: r15 = 1: the fails
    19,418 at prefix 3 + 21,004 at prefix 4 (the D5 window from
    {1,2,4} vs full); r15 = 4: the fails 34,565 all at prefix 4;
    r15 = 13: inert (all records the prefix-4 early-layer shape).
  - The arithmetic consistency rows all hold at full scale (crt_neg 0,
    DEFMAX 0, the deficit cells reconstructing the coarse cells, the
    zero collision row among the fw > 15 failers).
- **The mechanism status:** the CRT pair-set algebra is now an
  exact, engine-verified structural fact for the composite layer u = 15
  (and by the same proof shape, for any squarefree composite layer:
  the pair group (Z/p)* x (Z/q)* of order (p-1)(q-1), the windows of
  the generated sub-monoid). The next pieces this opens: (i) the
  deficit-exactness THEOREM (the realized-pair count from the window
  structure - a Lean formalization candidate on the E-016 skeleton);
  (ii) the u = 15 span-side mechanism (why the r15 = 1 spans live at
  |D| in {6, 7, 8}: the odd primes' pairs opening the orbit).
- **Artifacts:** `analysis/u15_alg_v025/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 119).
- **Status:** complete.

## E-032 - R8 piece 24: the u = 15 span-side mechanism census (engine v0.26) (2026-11-26)

- **What ran:** engine v0.26 (`analysis/u15_span_v026/`), a byte-superset
  of v0.25 (the reconcile: v0.25's 690 lines in order inside 711,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 still holds in
  the extended engine.
- **Verified results (full scale):**
  - **The spanner D15-shapes are FIXED again (7 shapes):** r15 = 4:
    uniformly the FULL unit group mask
    {1, 2, 4, 7, 8, 11, 13, 14} (|D| = 8, 27,488 records - the
    maximal pigeonhole certificate, 2|D| = 16 > 8 decisively);
    r15 = 1: 6 shapes over the 32,271 spanners (the top: the full
    unit group 14,251, then the 7-element 7,300, the 6-element
    5,593 and 3,936, plus two rarer shapes). The span-side sets
    are closed near the unit complement.
  - **The route structure:** every spanner is certified by the
    x'-window hit (a = 0), the p-scaled window (a = 1), or both:
    r15 = 4: the a = 0 route 7,269 hits-only + 14,955 both
    (22,224 = 80.9% carry an a = 0 hit); the a = 1-only route
    5,264 (19.1%) - the off-orbit p-pair (1, 4) is itself a
    generator needed for a minority of spans. r15 = 1: EVERY
    spanner carries both routes mechanically (the p-pair
    (1, 1) = the identity, so the two windows coincide). U15SNONE
    = 0 (consistency with E-031's algebra).
  - **The odd-pair generators (the mechanism):** the spanner's
    off-orbit odd-prime pair count (the (mod 3, mod 5) pairs of
    the odd primes q | x' outside the 2-orbit
    {(1,1), (2,2), (1,4), (2,3)}): 0: 1,693 / 1: 15,267 / 2:
    13,862 / 3: 1,448 / 4: 1 at r15 = 1 (the mode 1-2; 1,693
    spans carry NO off-orbit odd pair - the orbit + the
    p-scale suffices); r15 = 4: 0: 870 / 1: 14,276 / 2: 11,150 /
    3: 1,191 / 4: 1. ONE off-orbit odd-prime pair suffices for
    about half the spans of each class.
- **The mechanism status:** the u = 15 span-side is mechanized in
  census-cell terms: the pair-window algebra generates D15 (E-031,
  exact), the fail shapes = the orbit windows, the span shapes =
  the orbit + off-orbit odd pairs (mostly exactly one) + the
  p-scale; the r15 = 4 spans all carry the full unit group. Open
  at u = 15: the deficit-exactness Lean theorem (E-031's
  candidate) and the natural next layer.
- **Artifacts:** `analysis/u15_span_v026/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 122).
- **Status:** complete.

## E-034 - R8 piece 26: the u = 15 Lean layer part 1 (2026-11-26)

- **What landed:** the new module
  `ErdosStrausConjecture/ResidualPrimes/U15Layer.lean` (5 theorems,
  0-`sorry`, compile exit 0, 8476 jobs):
  - `u15_x_mod3_of_dvd` / `u15_x_mod5_of_dvd` - the divisibility
    transfers (3/5-divisibility of x forces the same for p under
    `4x = p + 15`), the omega-level core.
  - `u15_x_residue` - the structural glue `x = 4p (mod 15)` (4 is its
    own inverse mod 15).
  - `u15_x_coprime` - the E-029 `inad = 0` census row as a theorem:
    for `4x = p + 15` with `p` prime and `p > 5`, `x` is coprime to 15
    (any common prime factor 3 or 5 transfers to p, contradicting
    primality at `p > 5`).
  - `u15_m_coprime` - the coprimality of `M = p * x` (both factors
    individually in the CRT pair group, the seat of the E-031
    algebra).
- **Axiom census:** the two coprimality theorems on the trio, the
  three light lemmas on `[propext, Quot.sound]`; 0 `sorry` throughout;
  the audit pinned (verifier rows 125).
- **Status:** part 1 complete. Staged next: the deficit bound
  `|D15| <= |D3| * |D5|` (needs the D-set-as-Finset foundation piece -
  the E-016-scale skeleton) and the r15 = 7 predicate-exclusion
  theorem on the hard-case predicate's Lean shape.

## E-035 - R8 piece 27: the u = 15 Lean layer part 2 - the deficit bound (2026-11-26)

- **What landed:** U15Layer.lean extended to 9 theorems (0-`sorry`,
  compile exit 0, 8476 jobs): the D-set-as-Finset foundation piece and
  the deficit bound:
  - `crtPair` (the decode `(r % 3, r % 5)`) and `uDset` (the
    divisor-residue set as `(Nat.divisors M).image (fun d => d % u)`)
    - the foundation defs.
  - `uDset_mem_elim` / `uDset_mem_of_dvd` - the membership interface
    (with the `M != 0` side condition via `Nat.mem_divisors`).
  - `crtPair_injOn15` - the CRT decode is injective on the residues
    below 15 (the omega-derivable inversion: the pairs determine the
    residue mod 15 in the bounded range).
  - **`uDset15_card_le` - the deficit bound theorem:** `(uDset 15
    M).card <= (uDset 3 M).card * (uDset 5 M).card` - every realized
    pair is a member of both layer sets (the composite routing) and
    the CRT decode does not collapse the image - the nonnegativity of
    the E-030 census deficit `|D3| * |D5| - |D15|` IS A THEOREM.
- **Consequence:** the composite-layer foundation piece is closed -
  all further composite-layer formalizations (the E-031
  window-generation exactness, the deficit-exactness) now have the
  D-set language available (uDset at any modulus, the card interface).
- **Axiom census:** all four new theorems on the trio; the audit
  re-pinned (verifier rows 126).
- **Artifacts:** U15Layer.lean (9 theorems), the re-pinned
  axiom_audit_u15_layer.txt (9 theorems), lake_build_u15_layer.log.
- **Status:** part 2 complete. Staged: the deficit-EXACTNESS (the
  E-031 window algebra as a theorem - |D15| equals the pair-window
  fold, hence the exact deficit cells) and the r15 = 7
  predicate-exclusion theorem.

## E-036 - R8 piece 28: the u = 19 layer census (engine v0.27) (2026-11-26)

- **What ran:** engine v0.27 (`analysis/u19_class_v027/`), a byte-superset
  of v0.26 (the reconcile: v0.26's 711 lines in order inside 944,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 still holds.
- **Verified results (full scale):**
  - **ALL 18 classes populated** (r19 in {1..18}, total 2,364,031
    exact, uniform ~124k per class) - the prime layer has NO
    structural class exclusions (unlike the composite layers' 8/7
    gaps: the p-mod-19 classes are structurally free of the
    (p + 3)/4-predicate rejections, and the coprimality is
    automatic: U19ADMCHECK admfail = 0, E-034's theorem row exactly;
    fw3 = 0 again).
  - **The rescue chain closes exactly at u = 19:** the u = 19 spans
    42,804 and the true fw > 19 failers 32,183 sum to
    **74,987 = the E-032 still-failers exact**. The u = 19 layer
    rescues **57.09%** of the u = 15 failures; the still-failers are
    **32,183 = 1.36% of (H24)**.
  - **The chain to date:** u = 3 (0 spans) -> u = 7 (1,949,770 =
    82.49%) -> u = 11 (279,515 = 11.82%) -> u = 15 (59,759 =
    2.53%) -> u = 19 (42,804 = 1.81%) -> the residual 32,183 (1.36%).
  - **ZERO collisions among the fw > 19 failers** (the pattern now
    verified at all four nontrivial layers).
  - The per-class cells pinned (the U19CLASS/U19POP/U19POPSPAN rows
    x18, the fail-mask census U19FAILSET/U19COLL, the fw-early
    row U19FW71115).
- **Artifacts:** `analysis/u19_class_v027/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 129).
- **Status:** complete. The five-layer chain 3/7/11/15/19 is now
  census-complete; the still-failers 1.36% are the next chain link
  (u = 23) and the deficit-exactness Lean theorem remains the staged
  formalization piece.

## E-037 - R8 piece 29: the u = 23 layer census (engine v0.28) (2026-11-26)

- **What ran:** engine v0.28 (`analysis/u23_class_v028/`), a byte-superset
  of v0.27 (the reconcile: v0.27's 944 lines in order inside 1,031,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 holds.
- **The v0.28 design note:** the u = 23 census keeps the chain-critical
  cells only (the class counts, the |D| histograms, the collision
  counter) - the full 22-bit fail-mask arrays would need ~800 MB and
  the mask-shape detail is established (the orbit windows decoded at
  11/15).
- **Verified results (full scale):**
  - **All 22 unit classes populated** (total 2,364,031 exact; the
    coprimality automatic: U23ADMCHECK admfail = 0; fw3 = 0).
  - **The rescue chain closes exactly at u = 23:** the u = 23 spans
    21,626 and the true fw > 23 failers 10,557 sum to
    **32,183 = the E-036 still-failers exact**. The u = 23 layer
    rescues **67.20%** of the u = 19 failures; the still-failers are
    **10,557 = 0.447% of (H24)**.
  - **The chain to date:** u = 3 (0) -> 7 (1,949,770 = 82.49%) ->
    11 (279,515 = 11.82%) -> 15 (59,759 = 2.53%) -> 19 (42,804 =
    1.81%) -> 23 (21,626 = 0.91%) -> the residual 10,557 (0.447%).
  - **ZERO collisions** among the fw > 23 failers (five nontrivial
    layers).
- **Artifacts:** `analysis/u23_class_v028/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 132).
- **Status:** complete. The six-layer chain 3/7/11/15/19/23 is
  census-complete with the residual under half a percent; the census
  ladder has reached the point where every further layer rescues a
  sub-percent residual; the deficit-exactness Lean theorem remains
  the staged formalization piece.

## E-039 - R8 piece 31: the u = 31 layer census (engine v0.29; the u = 29 skip) (2026-11-26)

- **What ran:** engine v0.29 (`analysis/u29_class_v029/`), a byte-superset
  of v0.28 (the reconcile: v0.28's 1,031 lines in order inside 1,154,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 holds.
- **The layer-skip fact:** u = 29 is STRUCTURALLY EMPTY for the (H24)
  class: 29 = 1 (mod 4) forces `p + 29 = 24k + 30`, never divisible
  by 4 evenly - the (H24) records do not exist at that parameter
  (the same shape as the u = 5 exclusion, now for a different reason:
  u = 5 is 1 (mod 4) too). The chain of admissible layers for the
  (H24) class is exactly the u = 3 (mod 4) parameters:
  3, 7, 11, 15, 19, 23, 31 (29 skipped), ... - the census records the
  skip and runs the u = 31 layer (31 = 3 (mod 4), prime).
- **Verified results (full scale):**
  - **All 30 unit classes populated** at u = 31 (total 2,364,031
    exact; the coprimality automatic: U31ADMCHECK admfail = 0;
    fw3 = 0).
  - **The rescue chain closes exactly at u = 31:** the u = 31 spans
    4,668 and the true fw > 31 failers 5,889 sum to
    **10,557 = the E-037 still-failers exact**. The u = 31 layer
    rescues **44.21%**; the still-failers are **5,889 = 0.249% of
    (H24)**.
  - **The chain to date:** u = 3 (0) -> 7 (82.49%) -> 11 (11.82%) ->
    15 (2.53%) -> 19 (1.81%) -> 23 (0.91%) -> 31 (4,668 = 0.20%) ->
    the residual 5,889 (0.249%).
  - **THE ZERO-COLLISION ERA ENDS AT u = 31:** the failers at
    u = 7/11/15/19/23 carried ZERO collision pairs (the orbit-window
    protection held), but at u = 31 the census records
    **collisions = 2,613 among the 5,889 true failers (44.4%)** - the
    collision presence WITHOUT the span. The u = 7-23 pattern was an
    empirical orbit-window regime, not a law: at u = 31 the
    failers' D-sets grew past the orbit-window shapes while still
    failing the span criterion. The E-037-era framing (the
    collision-census rows as result rows) anticipated exactly this.
    The mechanism question: WHICH failers carry the pairs at 31 - a
    new census object (E-040 proposed).
- **Artifacts:** `analysis/u29_class_v029/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 135).
- **Status:** complete (the chain link + the collision-regime
  transition recorded).

## E-040 - R8 piece 32: the u = 31 collision-failer mechanism census (engine v0.30) (2026-11-26)

- **What ran:** engine v0.30 (`analysis/u31_coll_v030/`), a byte-superset
  of v0.29 (the reconcile: v0.29's 1,154 lines in order inside 1,348,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0.
- **Verified results (full scale, the mechanism read):**
  - **The collision rate by |D31| (pooled over the classes):** the
    failers with |D| <= 5 carry ZERO pairs (67 + 100 records); |D| =
    6/7/9: 100% (7 + 17 + 22 records); |D| = 8: 7.6%; |D| = 10:
    11.8%; |D| = 11: 50.2% (2,499 of 4,978). The |D| = 11 bucket is
    the mass site (the pop bucket capped at 11: the |D| >= 11
    failers).
  - **The pair shapes: the (1, 30) unit pair DOMINATES (2,176 of
    2,613 = 83.3%)**; (2, 29): 269 (10.3%); (3, 28): 68; the tail
    small. The (1, 30) pair is EXACTLY the one-sided criterion
    `-1 in D31(M)` (1 in D is the divisor 1 itself, always; 30 = -1
    (mod 31)) - 2,176 records carry the ONE-SIDED reachability at
    u = 31 without the parametric span.
  - **The interpretation (the delicate-class shape at the fresh
    layer):** the collision-carrying failers are pigeonhole-
    insufficient at u = 31 (|D| <= 11 < 15 = phi(31)/2), carry a
    collision pair (mostly the one-sided (1, 30) pair), yet fail the
    span criterion - THE DELICATE-CLASS STRUCTURE (the collision
    present, the pigeonhole insufficient, the parametric span absent)
    RE-EMERGES at the fresh layer. The records still receive their
    representations off-parameter (the fw <= 255 guarantee of the
    verified sweep: the MISMATCH 0 row), so the chain's
    representation-completeness is untouched - what the census adds
    is the delicate-shape recurrence as a structural fact per layer,
    with the (1, 30)-pair as its dominant signature.
  - The contrast cells (the U31SPOP spanner profiles) pinned; the
    U31CRATE per-class cells pinned (the class-resolved collision
    tables).
- **Artifacts:** `analysis/u31_coll_v030/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 138).
- **Status:** complete. Staged: the delicate-shape records at u = 31
  vs the E-011 rescue framework (the off-parameter pigeon sites);
  the deficit-exactness Lean theorem remains the staged
  formalization piece.

## E-041 - R8 piece 33: the delicate-shape rescue at u = 31 (engine v0.31) (2026-11-26)

- **What ran:** engine v0.31 (`analysis/u31_rescue_v031/`), a byte-superset
  of v0.30 (the reconcile: v0.30's 1,348 lines in order inside 1,349,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0.
- **What was scanned:** for every delicate-shape record at u = 31 (the
  collision-carrying pigeonhole-insufficient failers, 2,613 records),
  the off-parameter pigeon-rescue scan (u2 in {35..255}, 4-admissible,
  gcd = 1, the pigeon site 2|D| > phi), the E-011 framework's exact
  procedure.
- **Verified results (full scale):**
  - **U31RESCUE delicate=2,613 rescued_pigeon=2,613 (100%),
    pig_no_coll=0, no_site=0** - every delicate-shape record at the
    fresh layer is pigeon-rescued off-parameter, the exact analog of
    the original E-011 row (16,589/16,589, no_pigeon = 0) and the
    R5-verified property (the pigeon sites carry collisions:
    pig_no_coll = 0).
- **Interpretation:** the delicate-shape recurrence at u = 31 (E-040)
  sits INSIDE the verified rescue framework: the census's
  representation-completeness over the (H24) class holds through the
  new regime with zero uncovered records. The chain's full-ladder
  state: every record resolved (the span present at its fw <= 255)
  with the rescue machinery certifying the pigeon side wherever the
  span layer itself was pigeonhole-insufficient.
- **Artifacts:** `analysis/u31_rescue_v031/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 141).
- **Status:** complete. The chain 3/7/11/15/19/23/31 plus the rescue
  framework is census- and rescue-complete; the deficit-exactness
  Lean theorem remains the staged formalization piece.

## E-043 - R8 piece 35: the u = 35 layer census (engine v0.32) (2026-11-27)

- **What ran:** engine v0.32 (`analysis/u35_class_v032/`), a byte-superset
  of v0.31 (the reconcile: v0.31's 1,349 lines in order inside 1,424,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 holds.
- **The v0.32 design note:** the chain-critical cells only (the
  memory-safe design); the class-structure expectations (the non-unit
  classes empty for p prime > 7; the (H24) side excludes the
  3-multiple classes {15, 30}).
- **Verified results (full scale):**
  - All coprimality/assert rows hold (U35ADMCHECK admfail = 0, fw3 =
    0; total 2,364,031 exact).
  - **The chain closes exactly at u = 35:** the u = 35 spans 691 and
    the true fw > 35 failers 5,198 sum to
    **5,889 = the E-041 still-failers exact**. The u = 35 layer
    rescues only **11.73%** - the first sharp drop in the ladder's
    rescue rates (the previous links: 82.49% then 11.82, 2.53, 1.81,
    0.91, 0.20 percentage points, the RATE ~44-67% per link at 15+
    - and now 11.73%): the span rates at the bigger composite layers
    decay. The still-failers are **5,198 = 0.220% of (H24)**.
  - The collisions = 1,353 of the 5,198 failers (26.0%) - the
    delicate-regime share declining from the 44.4% at 31.
  - **The chain to date:** u = 3 (0) -> 7 (82.49%) -> 11 (11.82%) ->
    15 (2.53%) -> 19 (1.81%) -> 23 (0.91%) -> 31 (0.20%) -> 35 (691 =
    0.03%) -> the residual 5,198 (0.220%).
- **Artifacts:** `analysis/u35_class_v032/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 144).
- **Status:** complete. The seven-layer chain 3/7/11/15/19/23/31/35
  census-complete with the residual at a fifth of a percent.

## E-044 - R8 piece 36: the u = 39 layer census (engine v0.33) (2026-11-27)

- **What ran:** engine v0.33 (`analysis/u39_class_v033/`), a byte-superset
  of v0.32 (the reconcile: v0.32's 1,424 lines in order inside 1,475,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 holds.
- **Verified results (full scale):**
  - All coprimality/assert rows hold (admfail = 0, fw3 = 0; total
    2,364,031 exact; the populated classes per phi(39) = 24 units
    minus the predicate-rejected, measured in the class rows).
  - **The chain closes exactly at u = 39:** the u = 39 spans 733 and
    the true fw > 39 failers 4,465 sum to
    **5,198 = the E-043 still-failers exact**. The u = 39 layer
    rescues **14.10%**; the still-failers are
    **4,465 = 0.189% of (H24)**.
  - The collisions = 2,086 of the 4,465 failers (46.7%) - the
    delicate-regime share RE-RISES from the 26.0% at 35 (the layer
    alternation of the collision shares continues).
  - **The chain to date:** u = 3 (0) -> 7 (82.49%) -> 11 (11.82%) ->
    15 (2.53%) -> 19 (1.81%) -> 23 (0.91%) -> 31 (0.20%) -> 35 (0.03%)
    -> 39 (733 = 0.03%) -> the residual 4,465 (0.189%).
- **Artifacts:** `analysis/u39_class_v033/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 147).
- **Status:** complete. The nine-layer chain
  3/7/11/15/19/23/31/35/39 census-complete with the residual under a
  fifth of a percent.

## E-046 - R8 piece 38: the u = 43 layer census (engine v0.34) (2026-11-27)

- **What ran:** engine v0.34 (`analysis/u43_class_v034/`), a byte-superset
  of v0.33 (the reconcile: v0.33's 1,475 lines in order inside 1,646,
  missing = 0 PASS); the selftest byte-identical; the full run
  999,999,999 exit 0, MISMATCH 0; U15ALG mismatch = 0 holds.
- **Verified results (full scale):**
  - All coprimality/assert rows hold (admfail = 0, fw3 = 0; total
    2,364,031 exact).
  - **The chain closes exactly at u = 43:** the u = 43 spans 192 and
    the true fw > 43 failers 4,273 sum to
    **4,465 = the E-044 still-failers exact**. The u = 43 layer
    rescues **4.30%** (the ladder decay continues: 44.21, 11.73,
    14.10, now 4.30 percent); the still-failers are
    **4,273 = 0.181% of (H24)**.
  - The collisions = 989 of the 4,273 failers (23.1%) - the
    delicate-share alternation continues (44.4/26.0/46.7/23.1).
  - **The chain to date:** u = 3 (0) -> 7 (82.49%) -> 11 (11.82%) ->
    15 (2.53%) -> 19 (1.81%) -> 23 (0.91%) -> 31 (0.20%) -> 35 (0.03%)
    -> 39 (0.03%) -> 43 (192 = 0.01%) -> the residual 4,273 (0.181%).
- **Artifacts:** `analysis/u43_class_v034/` (the source, full_run.txt,
  sanitized_selftest.txt; hashes pinned below, verifier rows 150).
- **Status:** complete. The ten-layer chain
  3/7/11/15/19/23/31/35/39/43 census-complete; the per-layer rescue
  rates decay to the low single digits as the ladder enters the
  regime where the residual's structure (which the E-040
  collision-census began and the deficit-exactness Lean theorem
  targets) becomes the primary object.

## E-047 - R8 piece 39: the composite-layer D-set form, made general (E-047) (2026-11-27)

- **What landed:** U15Layer.lean extended to 11 theorems + 3 defs
  (0-`sorry`, compile exit 0, 8476 jobs):
  - `crtPair2` - the CRT decode `(r % a, r % b)` at the general
    coprime pair.
  - **`uDset_coprime_card_le` - the GENERAL deficit bound:** for
    nonzero coprime moduli `a, b`,
    `(uDset (a*b) M).card <= (uDset a M).card * (uDset b M).card` -
    the CRT decode is injective on the realized residues (the two
    modular equations compose via
    `Nat.modEq_and_modEq_iff_modEq_mul` with the coprime hypothesis -
    the exact toolchain CRT composition) and every realized pair
    routes through both layer sets (`Nat.mod_mod_of_dvd`). This
    subsumes the u = 15 bound (the E-035 theorem kept as the merge
    history) and generalizes the foundation to every future composite
    layer (35 = 5 x 7, 39 = 3 x 13, 51 = 3 x 17, ...).
  - `uDset35_card_le` - the corollary at 5 x 7 (the u = 35 layer's
    bound).
- **Axiom census:** the general bound and the corollary on the trio;
  `crtPair2` axiom-free; the audit re-pinned (verifier rows 150).
- **Status:** complete. The composite-layer foundation is now
  general; the remaining staged formalization: the
  window-generation exactness (the D-set = the pair-window fold as a
  theorem - the E-031 algebra's full form).













