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
- **Key results:** pigeonhole-conclusive 3,177,642 (99.49%); delicate
  (collision present, `|D| ≤ φ(u)/2`) 16,589 (0.52%); the `u = 3` and `u = 7`
  layers 100% pigeon-conclusive; delicate concentrates at higher layers
  (17.4% at `u = 19`, 77.6% at `u = 43`, 100% at `u ≥ 67` incl. both `u = 83`
  record primes — small-residue collision pairs, e.g. `(1, 82)` with margin
  −58 for `651,412,441`).
- **Artifacts:** `analysis/collision_v01/` (run output, stderr,
  sanitized self-test, 5,000-row delicate sample), hashes in
  DATA_MANIFEST.
- **Status:** complete; feeds H-2 and the R2 layer-conditioning tests.

## E-002 — R2: modulo-5 separation quantification (2026-11-24)

- **What ran:** engine v0.2 (adds the intrinsic parametric/nonparametric
  classification from the verified mod-840 procedure and mod-5 × mod-840 ×
  layer cross-tabulation), sanitizer-built, same anchors.
- **Key results:** see the E-002 result block once verified — target tables:
  (i) nonparametric-only rate per `p mod 5` group (independent check of the
  review's 4.09% / 1.50% / 2.73×), (ii) delicate rate per `p mod 5` group,
  (iii) first-working-parameter distribution per group, (iv) margin histogram
  per group; the layer-conditioned test of H-1's falsification criterion.
- **Artifacts:** `analysis/mod5_separation_v02/`.
- **Status:** complete (results recorded below and in
  `analysis/mod5_separation_v02/`).

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
- **Open reconciliation item (disclosed):** the onlyparam/both **split** —
  22,744 vs the review's 22,743 (one prime, class 529, classified
  only-parametric here; the review's engine aggregated it as both-type — or
  vice versa at aggregation). One prime in 795,913 (0.00013%); every other
  aggregate matches exactly. Tracked, not papered over: the two engines'
  candidate-enumeration orders differ in one corner (their structured
  `{1, p, p²} × {1, x, x²}` loop re-examines candidates the sorted-divisor
  loop also covers, with different early-break sequences), and the
  distinguishing prime can be isolated by a per-record diff once the review's
  per-record data is shared.
- **Bugs caught by the reconciliation (both fixed before any figure ships):**
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
  DATA_MANIFEST (25/25).
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
