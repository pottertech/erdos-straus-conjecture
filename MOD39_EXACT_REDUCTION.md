# Exact Mod-39 Reduction: Coupled Span in C2 × C12, Forced Factor 2

**Date:** 2026-11-19 (corrected-cohort semantics from the start; stage counts
are the true ones of `FIRST_A_STRUCTURE.md` — no deprivation to correct)
**Status:** exact criterion stated and verified with 0 mismatches on all 48
stage entrants ≤ 10^7; reduced parity-coupled form verified 0/48;
compact closed form deferred (factorization-dependent, as at u = 35).

## Setup

u = 39 = 3 · 13, composite, ≡ 3 (mod 4). For the residual class
n ≡ 1 (mod 24), n = 24m + 1:

$$x = \frac{n + 39}{4} = 6m + 10 = 2(3m + 5),$$

so the **forced factor is 2** (v₂(x) ≥ 1 always); 3 ∤ x in general —
3 ∣ x ⟺ m ≡ 2 (mod 3) ⟺ n ≡ 49 (mod 72), which is a conditional
factorization event, not forced. If 39 ∣ n·x the criterion succeeds
trivially (d₁ = d₂ = nx); if gcd(nx, 39) = 1 the centered/divisor-pair
criterion applies directly; the mixed cases use the exact divisor search.

## Dual structure and logs

$(\mathbb{Z}/39\mathbb{Z})^\times \cong (\mathbb{Z}/3\mathbb{Z})^\times \times (\mathbb{Z}/13\mathbb{Z})^\times \cong C_2 \times C_{12},$

with generators 2 in both components. The component logs of −1 are
log₃(−1) = 1 (of C₂) and log₁₃(−1) = 6 (of C₁₂; 2⁶ = 64 ≡ 12 mod 13),
so the **target pair is (1, 6)**. A prime factor q ∣ n·x contributes the
component log pair

$$q \mapsto (\log_3(q \bmod 3), \log_{13}(q \bmod 13)) \in C_2 \times C_{12},$$

weighted by its exponent, and the criterion is a signed subset-sum reach
with per-factor coefficient bounds.

## Verified results (corrected cohort, analysis/u39_layer.py)

- Cohort: **48 entrants (first-A ≥ 39), 22 solve at u = 39, 26 fail**
  (first-A ≥ 43).
- **Exact criterion vs the verified dataset: 0 mismatches (48/48).**
- **Coupled span criterion vs exact: 0 mismatches (48/48).**
- 47 distinct fingerprint patterns, **0 mixed-outcome**: the verdict is a
  function of the log-pair multiset.
- Failure slices by n mod 72: {1: 11, 25: 8, 49: 7}; failure first-A
  histogram {43: 5, 47: 15, 51: 1, 55: 2, 59: 2, 107: 1}.

## The reduced criterion (checked 48/48)

Because C₂ has only two elements and the forced factor 2 has log pair
** (1, 1)** — present with exponent ≥ 1 in every record — the 3-component
is reachable by the forced factor alone in one sign; the obstruction is
therefore a *parity-coupled* condition on the 13-span:

> **u = 39 succeeds for n ⟺ there exist signed integers cᵢ with
> |cᵢ| ≤ mᵢ such that**
> 1. $\sum_i c_i \log_{13}(q_i) \equiv 6 \pmod{12}$, and
> 2. $\sum_{q_i \equiv 2 \pmod 3} c_i$ is odd.

**Verified 48/48 against the exact criterion** (and against the verified
dataset, 0 mismatches). The second condition is the coupling: the same
coefficients must make the 13-part hit −1's log *and* have odd total
weight on the primes that are non-trivial mod 3.

## Saturation and the subgroup relaxation

The a-component is periodic with period 2 and the b-component with period
12; their lcm is 12, so **every coefficient may be replaced by min(mᵢ, 6)**
(saturation lemma; identical in shape to the u = 35 case, where the bound
is also 6 via periods 4 and 6). With every exponent ≥ 6 the criterion
collapse-check reaches the subgroup test: the generated subgroup of
C₂ × C₁₂ contains (1, 6) on **46 of the 48 records**; the two exceptions —
n = 118,801 (first-A 59) and n = 1,915,201 (first-A 47) — fail only
through exponent bounds.

## Purity note

As at u = 35, parity-purity is structurally dead here: **no record —
success or failure — is QR-pure at 13** (and not at 3 either), because the
forced factor 2 has log pair (1, 1), odd in both components
((2/39): the C₂-component is non-trivial and the 13-leg is odd). The
discriminator is the parity coupling above, not purity.

## What remains

The compact residue-class closed form is deferred for the same reason as at
u = 35: the criterion depends on the factorization structure of n(n+39)/4
(the log pairs and their exponents), not only on a residue of n. The exact
bounded span check, with the reduced parity form and the saturation
reduction, is the working criterion — verified 0/48 — and feeds the hybrid
termination route (ROADMAP #3) with one more layer under corrected
dataset-grounded semantics.
