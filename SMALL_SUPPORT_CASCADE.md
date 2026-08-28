# Small-Support Centered Cascade

**Date:** 2026-08-28

This note records a structural feature of the corrected exact u-method that is much stronger than the earlier generic divisor-distribution heuristic.

## Setup

For `n ≡ 1 (mod 4)`, choose `u ≡ 3 (mod 4)` and set

\[
x=(n+u)/4,\qquad M=nx.
\]

When `gcd(M,u)=1`, the exact centered criterion is

\[
\prod_{p^e\parallel M}p^{c_p}\equiv-1\pmod u,
\qquad -e\le c_p\le e.
\]

Define the **support** of a centered witness to be the number of primes with `c_p != 0`, and define its `L1` size as `sum |c_p|`.

## Corrected residual sample

Start with the 6,246 prime hard cases below `10^6`.

1. Apply the exact `n+1` and `n+4` shift-divisor criteria.
2. This removes 5,160 cases.
3. The remaining **1,086** form the corrected residual hard core.
4. Search `u = 3,7,11,15,...,159` with the exact centered criterion and select the first successful u.

Every one of the 1,086 residual cases has a first-success witness supported on at most **three distinct prime factors**.

| support | L1 | count |
|---:|---:|---:|
| 1 | 1 | 323 |
| 1 | 3 | 16 |
| 2 | 2 | 697 |
| 2 | 3 | 18 |
| 3 | 3 | 31 |
| 3 | 4 | 1 |

Thus **1,036 / 1,086 (95.4%)** of the residual cases are solved by either a single prime residue or two prime residues with coefficients only `±1`.

Only one residual case in the range requires support 3 with total `L1=4` at its first successful u:

\[
n=757201,\qquad u=31,
\]

with one centered witness

\[
2^{-2}\,7^{-1}\,6761\equiv-1\pmod{31}.
\]

## Generic deterministic route lemmas

The dominant finite patterns correspond to very small exact congruence statements.

### One-factor route

If some prime factor `p | M` satisfies

\[
p\equiv-1\pmod u,
\]

then support 1, `L1=1` succeeds.

More generally, if `v_p(M) >= k` and

\[
p^k\equiv-1\pmod u,
\]

then support 1 with `|c_p|=k` succeeds.

### Two-factor route

If distinct prime factors `p,q | M` satisfy any of

\[
pq\equiv-1\pmod u,
\qquad pq^{-1}\equiv-1\pmod u,
\qquad p^{-1}q\equiv-1\pmod u,
\qquad p^{-1}q^{-1}\equiv-1\pmod u,
\]

then support 2 with total `L1=2` succeeds.

Equivalently, after orientation, it is enough that

\[
q\equiv-p\pmod u
\quad\text{or}\quad
q\equiv-p^{-1}\pmod u.
\]

These tiny routes account for the overwhelming majority of corrected residual successes below `10^6`.

## Research implication

The empirical problem is therefore not primarily that a large divisor set must become equidistributed. The data instead suggest a much sharper statement:

> For each residual hard case, some small `u ≡ 3 (mod 4)` admits a centered representation of `-1` using at most a bounded number of prime factors of `nx`, with very small signed exponents.

A useful proof target would be a **bounded-support centered residue theorem**, ideally with support at most 3 and a controlled finite set of u-values.

Such a theorem would be much easier to formalize in Lean and to audit than the previous probabilistic Chebotarev/divisor-distribution route.
