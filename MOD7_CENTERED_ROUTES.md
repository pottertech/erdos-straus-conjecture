# Exact Mod-7 Centered Routes

**Date:** 2026-08-28

This note analyzes the exact centered product-set criterion for `u=7` without using the obsolete three-target shortcut.

Let

\[
x=\frac{n+7}{4},\qquad M=nx,
\]

with `n ≡ 1 (mod 4)` and `7 ∤ M`. The exact centered criterion is

\[
-1\in\mathcal S_7(M),
\]

where

\[
\mathcal S_7(M)=\left\{\prod_{p^e\parallel M}p^{c_p}\pmod7:\ -e\le c_p\le e\right\}.
\]

Because `(Z/7Z)^*` is cyclic of order 6, this can be expressed as a bounded signed sum of discrete logs with target `3 mod 6`. The following sufficient routes are immediate and completely deterministic.

## Route 1: a factor congruent to -1

If some prime factor `p | M` satisfies

\[
p\equiv6\pmod7,
\]

then choose centered exponent `c_p=1`; this directly gives `p ≡ -1 (mod 7)`. Hence `u=7` succeeds.

## Route 2: a repeated factor in residues 3 or 5

If `p | M`, `v_p(M) >= 3`, and

\[
p\equiv3\text{ or }5\pmod7,
\]

then

\[
p^3\equiv-1\pmod7.
\]

Thus choosing `c_p=3` gives a valid centered witness.

## Route 3: two one-step factors

If two distinct prime factors `p,q | M` have one of the following residue patterns, centered exponents `±1` already reach `-1`:

- `(p mod 7,q mod 7) = (2,3)` or `(4,5)`: `pq ≡ -1 (mod 7)`;
- `(p mod 7,q mod 7) = (2,5)` or `(3,4)`: `p q^{-1} ≡ -1 (mod 7)` or its inverse orientation.

Pairs involving residue 6 reduce to Route 1.

These are exact sufficient conditions and require no probabilistic distribution assumption.

## Aggregate-factor special cases

The aggregate centered ratios `n` and `x` give two particularly simple families:

- `n ≡ -1 (mod 7)` gives `u=7` immediately;
- `x ≡ -1 (mod 7)`, equivalently `n ≡ -4 (mod 7)`, gives `u=7` immediately.

Together with `n ≡ 1 (mod 4)`, these are the unconditional progressions

\[
n\equiv13,17\pmod{28}.
\]

## Corrected finite classification after shift-divisor reduction

Among the 6,246 prime hard cases below `10^6`, the `n+1` / `n+4` shift-divisor criteria leave 1,086 residual cases. On these residual cases:

- `u=7` succeeds for **744**;
- `u=7` fails for **342**.

Every one of the 744 successes has a shortest centered witness with support at most two prime factors:

| shortest centered route | count |
|---|---:|
| one factor, `|c|=1` | 244 |
| one factor, `|c|=3` | 16 |
| two factors, total `L1=2` | 484 |

Thus, in this finite range, all residual `u=7` successes are explained by the explicit local residue routes above. No large product-set expansion is needed at the mod-7 layer.

## What an exact u=7 failure must avoid

A genuine `u=7` failure must simultaneously avoid:

1. every prime factor `≡ 6 (mod 7)`;
2. any factor `≡ 3 or 5 (mod 7)` with exponent at least 3;
3. every two-factor residue pair from Route 3;
4. the aggregate cases `n ≡ -1,-4 (mod 7)`.

This is a finite combinatorial restriction on the residue multiset of the prime factors of `M=nx`, with multiplicity bounds retained exactly.

## Next layer

Of the 342 cases that survive `u=7` after the shift-divisor reduction, the exact `u=11` centered criterion resolves 164 below `10^6`. Their shortest centered representations are also small:

- 31 use one factor with `|c|=1`;
- 118 use two factors with total `L1=2`;
- 4 use two factors with total `L1=3`;
- 11 use three factors with total `L1=3`.

This suggests building a deterministic finite-state cascade of bounded centered residue routes for `u=7,11,15,19,...`, rather than relying on asymptotic independence heuristics.
