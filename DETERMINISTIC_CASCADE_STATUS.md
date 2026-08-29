# Deterministic Corrected Cascade Status

**Date:** 2026-08-28

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

The inherited restriction `n ≡ 1 or 4 (mod 15)` is now proved, not empirical.

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

Thus these deterministic layers reduce the corrected hard-prime sample by

\[
1-\frac{283}{48711}\approx99.42\%.
\]

Among the final 283 cases at the u=23 failure stage:

- 268 are QR-pure modulo 23;
- 15 have the exact small exceptional non-QR shape.

The finite counts are computational cross-checks. The layer descriptions themselves are algebraic finite-group results.

## Next layer

Applying `u=31` to these 283 cases in the corrected data solves 190 and leaves 93.

Unlike `u=23`, `x_31` forces only the factor 2, so the mod-31 obstruction has a larger exceptional set. The next task is to determine whether inherited purity from the 7, 11, 15, and 23 layers collapses that larger abstract obstruction to a small finite family.

That is the current proof target.