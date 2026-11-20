# Deterministic Corrected Cascade Status

**Date:** 2026-08-28

> **Independent replication (2026-11-19):** every table below was re-derived from scratch by `analysis/u31_layer_analysis.py` (shift-divisor + exact u = 7, 11, 15, 23, extended 31…63) with **identical counts at every stage**, including single residual survivor 8,803,369. Verification script: `analysis/u31_classification_verify.py`. The u=31 layer now has its own exact characterization: see `MOD31_EXACT_REDUCTION.md` (span criterion — 0 mismatches on all 283 stage entrants; QR-pure obstruction 60/93; cube-QNR rescue theorem with explicit witnesses). The u=35 layer is characterized as a **coupled-CRT span** — forced factor 3, 0 mismatches on all 93 stage entrants, all 67 failures non-QR-pure: see `MOD35_CRT_SPAN.md` (run via the OSR stack venv).

This document records the current proof-level cascade after replacing the invalid three-target shortcut with the exact centered product-set criterion.

## Exact starting point

For

\[
x_u=\frac{n+u}{4},\qquad M_u=n x_u,
\]

with `gcd(M_u,u)=1`, the corrected u-method succeeds exactly when the bounded signed prime-factor product set of `M_u` contains `-1 mod u`.

## Proven deterministic layers

### 1. Shift-divisor reduction

The exact `n+1` and `n+4` divisor criteria imply that any residual hard case must have:

- every odd prime factor of `n+1` congruent to `1 mod 4`;
- every prime factor of `n+4` congruent to `1 mod 4`.

These conditions force

\[
n\equiv1\pmod{24}.
\]

### 2. Exact u=7 layer

Because `2 | x_7`, `u=7` succeeds iff `M_7` has a quadratic-nonresidue prime factor modulo 7.

Thus failure forces every prime divisor of `M_7` into

\[
\{1,2,4\}\pmod7.
\]

This layer also implies, for a surviving hard case,

\[
n\equiv1\text{ or }4\pmod{15}.
\]

### 3. Exact u=11 layer

Because `3 | x_11`, the residue obstruction modulo 11 is completely classified.

Failure occurs only in either:

1. the all-QR case modulo 11; or
2. the explicit small exceptional configuration described in `MOD11_EXACT_REDUCTION.md`.

### 4. Exact u=15 layer

The inherited restriction `n ≡ 1 or 4 (mod 15)` is proved, not empirical.

With

\[
H=\langle2\rangle=\{1,2,4,8\}\subset(\mathbb Z/15\mathbb Z)^\times,
\]

failure at `u=15` is equivalent to every prime divisor of `M_15` lying in `H`.

### 5. Exact u=23 layer

Because `6 | x_23`, both 2 and 3 are forced centered generators.

Failure is exactly one of:

1. all prime divisors of `M_23` are quadratic residues modulo 23;
2. the explicit small exceptional QNR configuration described in `MOD23_EXACT_REDUCTION.md`.

## Corrected finite cross-check through 10^7

Starting from all corrected prime hard cases below `10^7`:

| stage | survivors |
|---|---:|
| corrected prime hard cases | 48,711 |
| after shift-divisor reduction | 7,272 |
| after exact u=7 | 2,137 |
| after exact u=11 | 1,054 |
| after exact u=15 | 681 |
| after exact u=23 | 283 |

> **⚠️ Correction (2026-11-19, `FIRST_A_STRUCTURE.md`):** two defects in this
> table's chain semantics, both confirmed against the verified certificate
> dataset: (1) the base 48,711 includes 12,961 theorem2-solved 13-mod-24
> primes (the b₃ test in `is_hard_prime` does not exclude them); the true
> residual base is 35,750. (2) The layer set omits the admissible stages
> u = 19 and u = 27, so every survivor count past u = 15 is inflated (the
> 174 cases with true first-A 19/27 are counted as late-stage survivors).
> The corrected chains — structured subclass 7,272 → 2,137 → 1,054 → 681 →
> 388 → 150 → 109 → 35 → 23 → 14 → 12 → 4 → 3 → 2 → 1, and full residual
> 35,750 → 7,144 → 2,681 → 1,732 → 849 → 308 → 217 → 65 → 48 → 26 → 21 →
> 6 → 5 → 3 → 1 — terminate at the same single survivor
> (n = 8,803,369, first works u = 107). Per-stage counts:
> `FIRST_A_STRUCTURE.md` §4.3. The per-record span/exact verifications in
> the layer documents remain valid for the entrant sets they checked.

Thus these deterministic layers reduce the corrected hard-prime sample by

\[
1-\frac{283}{48711}\approx99.42\%.
\]

Among the 283 cases at the u=23 failure stage:

- 268 are QR-pure modulo 23;
- 15 have the exact small exceptional non-QR shape.

The finite counts are computational cross-checks. The layer descriptions themselves are algebraic finite-group results.

## Extended corrected finite cascade

Continuing with the exact centered criterion, but without yet claiming new general theorems for these later moduli, the 283 finite survivors collapse as follows:

| next modulus | survivors after layer |
|---:|---:|
| 31 | 93 |
| 35 | 67 |
| 39 | 29 |
| 43 | 25 |
| 47 | 9 |
| 51 | 7 |
| 55 | 5 |
| 59 | 2 |
| 63 | 1 |

The single survivor after `u=63` is

\[
n=8,803,369.
\]

It also fails the tested values `u=67,71,75,79,83,87,91,95,99,103` and first succeeds at

\[
\boxed{u=107}.
\]

For this case,

\[
x_{107}=\frac{8,803,369+107}{4}=2,200,869
=3^2\cdot11^2\cdot43\cdot47.
\]

A particularly small centered witness is

\[
\boxed{3^{-2}43^{-1}47^{-1}\equiv-1\pmod{107}},
\]

because

\[
3^2\cdot43\cdot47\equiv-1\pmod{107}.
\]

Thus even the largest corrected first-working value below `10^7` has support 3 and total centered exponent size 4.

## Current proof target

The next proof-level task is the `u=31` obstruction. Here `x_31` forces the factor 2 but not 3, so the abstract exceptional set is larger than at `u=23`. The goal is to combine the inherited purity restrictions from the exact 7, 11, 15, and 23 layers with the finite mod-31 centered obstruction and show that only a much smaller set of residue patterns can survive.

The longer-term target remains a bounded-support deterministic cascade theorem, not an equidistribution heuristic.