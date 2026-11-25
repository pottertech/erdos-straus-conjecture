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

**Status:** empirical association — open. Not a proved causal relationship.

**Supporting data (as reported).** Review-computed grouped rates, 2.73× ratio;
consistent with the Paper-1 mod-840 observation (classes {1, 121, 361} are the
`+1 (mod 5)` group; {169, 289, 529} the `−1 (mod 5)` group; delicate rates
2.53%/1.94%/2.60% vs 2.14%/0.96%/2.26% respectively in Lane L1).

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
`|D_u(M)| > φ(u)/2`. Empirical support: 99.49% of first-working parameters
already satisfy it. This is the L4/R6/R8 objective — a theorem candidate, not
an established result; it does NOT enter the registry until proved.
