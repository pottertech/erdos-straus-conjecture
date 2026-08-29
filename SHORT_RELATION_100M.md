# Short-Relation Cascade Through 10^8

**Date:** 2026-08-28  
**Status:** Exact finite computation; not a proof for arbitrary `n`

## Population

For prime `n <= 100,000,000`:

1. retain only the six classical residual classes modulo 840,
2. apply the corrected A=3/hard gate,
3. apply the exact `n+1` / `n+4` shift-divisor reduction.

Counts:

- primes in the six classes: **179,468**
- after the A=3/hard gate: **97,374**
- after the shift-divisor reduction: **26,399**

## Short-relation search

For each residual `n`, search `u = 3,7,11,...,299`, with

\[
x=(n+u)/4,\qquad M=nx.
\]

A certificate is one of:

1. `p | M` and `p == -1 (mod u)`;
2. `p^3 | M` and `p^3 == -1 (mod u)`;
3. distinct `p,q | M` and `p*q == -1 (mod u)`;
4. distinct `p,q | M` and `p == -q (mod u)`.

The search minimizes support first (one factor before two), then exponent size, then `u`.

### Result

**All 26,399 residual primes have a support <= 2 certificate with `u <= 299`. There are zero failures.**

Minimal-support route counts:

| route | count |
|---|---:|
| `p == -1` | 21,399 |
| `p^3 == -1` | 16 |
| `p*q == -1` | 2,583 |
| `p == -q` | 2,401 |

The product/opposite split is tie-break dependent when more than one two-factor witness exists; the invariant statement is that **4,984** cases require two factors after all one-factor gates are exhausted.

### Witness source

| source | count |
|---|---:|
| one factor from `x` | 21,415 |
| one factor is `n`, one from `x` | 3,038 |
| both factors from `x` | 1,946 |

No one-factor certificate uses the prime `n` itself after the shift-divisor reduction, as expected: a congruence `n == -1 (mod u)` is already a shift-divisor route.

## Independent certificate verification

For each of the 26,399 certificates, the explicit denominators from the corresponding short-relation endpoint were constructed and checked against

\[
4xyz=n(xy+xz+yz)
\]

using exact integer arithmetic. Result: **26,399 / 26,399 pass; zero bad certificates.**

## Interpretation

The support-two phenomenon survives a tenfold extension from `10^7` to `10^8`. This strongly supports the **Two-Factor Cascade Conjecture**, but remains finite computational evidence.

The next proof target is not full product-set equidistribution. It is to force, for some small `u`, one of the four explicit relations above among prime factors of `M=n(n+u)/4`.
