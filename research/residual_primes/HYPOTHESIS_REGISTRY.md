# HYPOTHESIS_REGISTRY.md — Paper 2

Hypotheses are separated from theorems. Each carries: statement, current
status, supporting data, candidate mechanisms, and **falsification criteria**
(the observation that would kill or downgrade it). A hypothesis is promoted
to the THEOREM_REGISTRY only via the discipline gates.

## H-1 — The modulo-5 separation (twelfth review, twelfth-review §3)

**Statement.** The nonparametric-only witness rate at first-working parameters
differs by the prime's residue modulo 5: `p ≡ 1 (mod 5)` at 4.09% vs
`p ≡ 4 (mod 5)` at 1.50% (2.73×) over the review's independently verified
populations.

**Status:** open, reformulated by E-004 (2026-11-25): the aggregate 2.73x
separation is a layer-composition artifact — it localizes to the u = 11
layer (7.42% vs 0.00%, with 5 | x identically for p = 4 (mod 5) at u = 11,
and ord(5) = 5 in (Z/11)* so the isolated 5-window never reaches -1). The
aggregate framing is retained for continuity; the research target is the
u=11-layer mechanism (R3 flagship).

**Supporting data (as reported).** Review-computed grouped rates, 2.73× ratio;
consistent with the Paper-1 mod-840 observation (classes {1, 121, 361} are the
`+1 (mod 5)` group; {169, 289, 529} the `−1 (mod 5)` group; delicate rates
2.54%/1.94%/2.60% vs 2.15%/0.96%/2.26% respectively in Lane L1).
Percentages in this registry are rounded to two decimals from the
committed counts; the engine's `rate_del` fields are truncated
percent-times-100 values and are not quoted directly.

**R2 quantification plan.** Independently recompute, per `p mod 5` group and
crossed with mod-840 class and first-working layer:
1. the nonparametric-only rate (intrinsic classification per the verified
   procedure),
2. the delicate rate (`|D| ≤ φ(u)/2`),
3. the first-working-parameter distribution,
4. the margin histogram `2|D| − φ(u)`.

**Candidate mechanisms (to be tested, not assumed).**
- *Layer composition.* The mod-5 residue may shift the first-working-parameter
  distribution (e.g. via `x = (p+u)/4 mod 5` steering which admissible
  parameters have 5 ∣ x or small-factor structure), and aggregate rates then
  differ only because the layer populations differ. Test: condition the rate
  on the layer — does the mod-5 gap survive within layers?
- *Per-layer mechanism.* For a fixed layer, the mod-5 residue may change
  `M`'s factorization (e.g. 5 ∣ x for specific sub-classes, changing
  `|D_u(M)|` by merging residue orbits, or changing parametric-witness
  availability via the `x`-factorization).
- *Character-structure artifact.* `p ≡ ±1 (mod 5)` both have
  `(p/5) = 1`, so this is not a Legendre-symbol split; if no mechanism
  survives conditioning, the association is a composition artifact.

**Falsification criteria.**
- If the rate gap vanishes within every first-working-parameter layer, H-1 is
  downgraded to a layer-composition artifact (moved to §Rejected with the
  cross-tab).
- If the gap persists across layers but vanishes under `|D|-marginal`
  balancing, the mechanism is cardinality-mediated (record; H-1 survives in
  reduced form).
- If it persists under both conditionings, H-1 is upgraded to a structural
  hypothesis and R6 pursues its proof.

## H-2 — Delicate-class mechanism (Lane L1)

**Statement.** The 16,589 delicate primes (collision present, `|D| ≤ φ(u)/2`)
achieve their collisions through small-residue divisor pairs (e.g. a divisor
`≡ −1 (mod u)` paired with 1) rather than cardinality, and concentrate at
higher first-working layers (17.4% delicate at `u = 19`, 77.6% at `u = 43`,
100% at `u = 67, 79, 83`).

**Status:** empirical pattern — open mechanism.

**Supporting data.** `analysis/collision_v01/` (margin histogram heavy-tailed;
both `u = 83` record primes delicate with margin −58 and pair `(1, 82)`).

**Falsification criteria.** If the delicate class is fully explained by
`|D|`-distribution artifacts (e.g. small `u`-layers with large `φ(u)/2` from
few factors), the "mechanism" phrasing is dropped in favor of a
distributional description; if a structural invariant separates delicate
from pigeonhole-conclusive primes deterministically, H-2 upgrades.

## H-3 — Universal cardinality guarantee (target theorem, not a hypothesis)

**Target.** For every residual prime there exists an admissible `u` with
`|D_u(M)| > φ(u)/2`. Empirical support: 99.48%-plus-rescue = **100% over the
verified sweep [10^7, 10^9)** after E-011 — 3,177,642 (99.49%) certified at
the first-working parameter and the remaining 16,589 delicate records each
rescued at an admissible u' with fw < u' <= 255 (`rescued_pigeon` =
16,589/16,589, zero no-pigeon records; 29 distinct pigeon-site layers).
This is the L4/R6/R8 objective — a theorem candidate, not an established
result; it does NOT enter the registry until proved.


## H-4 — the u = 7 x-divisor witness shape (E-008 fingerprint)

**Statement.** For the u = 7, p ≡ 3 (mod 5) class (788,565 swept records,
[10^7, 10^9)): both witness kinds (parametric and the minimal
nonparametric companion) live in the x-divisors - the p-factor is never
required - with the 5-orbit mod 7 (5³ ≡ −1) letting the deeper-5 window
supply the nonparametric companions (9.1% beyond M's 5-depth).

**Status:** empirical fingerprint - open. Candidate for a conditional
theorem (a uniform-shape construction) after R6.

**Falsification criteria.** Any u = 7 g = 3 record whose minimal witnesses
both require the p-factor, or with a parametric witness but no
nonparametric companion (the onlypar-zero violated), or a deeper-5 window
that fails to supply the companion where the flag predicts one. A single
counterexample demotes the uniform-shape reading to per-record.


## H-5 — the delicate class is dominantly the one-sided-satisfied tail (E-009)

**Statement.** Of the 16,589 delicate records ([10^7, 10^9)), 82.8% carry
the unit collision pair (1, u − 1) — equivalently −1 ∈ D_u(M) — so the
collision already IS a parametric witness; the remaining 17.2% collide by
small non-unit residues (d₁ ≤ u/2 always; d₁ > u/2 never, by the minimal
scan).

**Status:** empirical fingerprint (0-mismatch, 16,589/16,589 classified) —
open as a mechanism claim. **R8 note (E-011):** all 16,589 delicate records,
including the 2,847-record tail, are pigeon-certifiable at another
admissible parameter (u <= 255); the tail's first-working small-residue
collision and its cardinality certificate are separate facts.

**Falsification criteria.** Any delicate record whose minimal pair is a
non-unit residue with d₁ ≤ u/2 AND −1 ∉ D_u(M) where the tail
classification predicts a unit pair; conversely a new sweep range whose
delicate share is NOT dominated by the unit-pair shape.


## H-6 — the small-layer x-divisor uniformity (E-010 classification)

**Statement.** The x-divisor witness shape is a small-layer property: at
u = 3 and u = 7 (58% of the sweep) the smallest parametric witnesses are
p-free at 100.0% in EVERY populated slice of those layers (2,713,109
parametric-witness records, zero mismatches; the E-010 correction: the
95.7% figures initially quoted were the holder rates, not the p-free
shares), decaying smoothly to ~65-92% at the deeper layers (the
single-record layers above u = 71 excluded); the
5-intersection slices ((p + u) ≡ 0 (mod 5)) carry the same weakening
(100.0% at u = 7, 96.4% at u = 11, 84.8% at u = 19, 84.5% at u = 31).

**Status:** empirical classification (0-mismatch, 40 populated slices) —
open as a monotone mechanism.

**Falsification criteria.** A populated layer u ≤ 7 whose minimal
parametric witness requires the p-factor (a single record); or a populated
deeper layer exhibiting the u = 7 shares.
