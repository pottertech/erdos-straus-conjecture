# Combined Finite Short-Relation Progression Cover

**Date:** 2026-08-29  
**Status:** Exact CRT density calculation for a finite set of explicit solution families. Novelty relative to the literature is not asserted.

## 1. Baseline linear cover

`PROGRESSION_COVER_DENSITY.md` records 6,386 explicit `p ≡ -1 (mod u)` progression classes extracted from the corrected `10^8` computation. They involve 5,140 distinct primes and give exact natural density

\[
\delta_{\rm linear}\approx0.6869852813
\]

inside each of the six classical residual classes modulo 840.

Thus the finite linear family alone covers

\[
\boxed{68.6985\%}
\]

of the classical residual lattice.

## 2. Fifteen explicit mixed-source families

The following 15 mixed `n+x` short-relation templates were selected because they give the largest exact incremental densities against the finite linear cover.

| u | relation | q | exact progression |
|---:|---|---:|---|
| 11 | `nq ≡ -1 (mod u)` | 5 | `n ≡ 189 (mod 220)` |
| 11 | `n ≡ -q (mod u)` | 5 | `n ≡ 149 (mod 220)` |
| 23 | `nq ≡ -1 (mod u)` | 3 | `n ≡ 61 (mod 276)` |
| 23 | `nq ≡ -1 (mod u)` | 2 | `n ≡ 57 (mod 184)` |
| 23 | `n ≡ -q (mod u)` | 2 | `n ≡ 113 (mod 184)` |
| 39 | `nq ≡ -1 (mod u)` | 5 | `n ≡ 421 (mod 780)` |
| 39 | `n ≡ -q (mod u)` | 5 | `n ≡ 541 (mod 780)` |
| 31 | `nq ≡ -1 (mod u)` | 2 | `n ≡ 201 (mod 248)` |
| 31 | `n ≡ -q (mod u)` | 2 | `n ≡ 153 (mod 248)` |
| 51 | `n ≡ -q (mod u)` | 5 | `n ≡ 709 (mod 1020)` |
| 19 | `n ≡ -q (mod u)` | 5 | `n ≡ 261 (mod 380)` |
| 47 | `nq ≡ -1 (mod u)` | 3 | `n ≡ 313 (mod 564)` |
| 47 | `nq ≡ -1 (mod u)` | 2 | `n ≡ 305 (mod 376)` |
| 47 | `n ≡ -q (mod u)` | 2 | `n ≡ 233 (mod 376)` |
| 7 | `nq ≡ -1 (mod u)` | 17 | `n ≡ 401 (mod 476)` |

Every row is an unconditional Erdős--Straus family by `SHORT_RELATION_PROGRESSION_FAMILIES.md`.

## 3. Exact overlap calculation

The union density is **not** obtained by summing the individual densities.

For the finite linear family, write the uncovered density as

\[
C
=
\prod_{p\in P}\left(1-\frac{k_p}{p}\right)
\approx0.3130147187.
\]

For each intersection of the 15 mixed progressions, generalized CRT determines whether the intersection is empty and, if nonempty, gives its exact modulus. The intersection is then combined with the finite linear-family complement prime by prime. Inclusion--exclusion across the 15 mixed progressions gives exact additional density

\[
\delta_{\rm extra}\approx0.1308967992.
\]

Therefore

\[
\boxed{
\delta_{\rm combined}
=(1-C)+\delta_{\rm extra}
\approx0.8178820805.
}
\]

Hence this finite collection of explicit short-relation progressions covers

\[
\boxed{81.7882\%}
\]

of the integers in the union of the six classical residual mod-840 lattices.

This is a global natural-density statement for all integers, not a finite-range success percentage.

## 4. Why the result is useful

The finite computation through `10^8` has now been converted into a finite set of exact theorem families with a global covering consequence.

The uncovered set is at most

\[
\boxed{18.2118\%}
\]

of the classical residual lattice relative to this finite family.

That complement is not arbitrary: it simultaneously avoids thousands of explicit residue classes modulo the primes used by the linear families and avoids the 15 displayed mixed-source CRT classes. These avoidance conditions can be used as deterministic hypotheses in the next cascade layer.

## 5. Next target

Two natural next steps are:

1. add further mixed and `x+x` progression families with exact overlap accounting, seeking a substantially smaller certified complement;
2. derive structural consequences of belonging to the complement, instead of merely adding more classes.

The second direction is more likely to lead to a proof: a counterexample would have to live in the intersection of all of these avoidance conditions.
