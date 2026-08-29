# Two-Factor Centered Cascade Through 10^7

**Date:** 2026-08-28  
**Status:** Exact finite computation; conjectural as a global theorem

This note sharpens the corrected classical-core cascade by minimizing centered witness support over all gates

\[
u=7,11,15,\ldots,299.
\]

The population is the 3,649 prime cases below `10^7` remaining after:

1. restricting to the six classical residue classes modulo 840;
2. applying the corrected A=3/hard gate;
3. applying the exact `n+1` / `n+4` shift-divisor reduction.

For each gate set

\[
x_u=\frac{n+u}{4},\qquad M_u=n x_u.
\]

A centered support-k witness uses k distinct prime factors of `M_u` with nonzero signed exponents and multiplies to `-1 mod u`.

## Main finite result

Every one of the 3,649 corrected residual cases admits a centered witness with support at most **two** for some `u <= 299`.

| minimal route | count |
|---|---:|
| one factor, `|c|=1` | 2,784 |
| one factor, `|c|=3` | 3 |
| two factors, total `L1=2` | 862 |

There are no cases requiring support 3 or more once the gate is allowed to vary through 299.

The coverage thresholds are:

| maximum u | cases having support <=2 witness |
|---:|---:|
| 31 | 2,784 |
| 59 | 3,127 |
| 107 | 3,394 |
| 127 | 3,445 |
| 159 | 3,508 |
| 199 | 3,568 |
| 239 | 3,607 |
| 299 | 3,649 |

The largest gate needed in this finite minimization is `u=299`.

## Exact route shapes

### One-factor route

For 2,784 cases there is a prime `p|M_u` with

\[
p\equiv-1\pmod u.
\]

For three further cases, a prime with sufficient valuation satisfies

\[
p^3\equiv-1\pmod u.
\]

### Two-factor routes

All 862 support-two witnesses have coefficients only `±1`. Up to inversion and exchanging the two primes, there are only two forms.

#### Product form

\[
pq\equiv-1\pmod u.
\]

Count: **468**.

#### Opposite-residue / quotient form

\[
pq^{-1}\equiv-1\pmod u,
\]

which is equivalent to

\[
p\equiv-q\pmod u.
\]

Count: **394**.

Among these 862 two-factor routes, 377 involve the prime `n` itself and 485 use only other prime factors of `M_u` (normally factors of `x_u`). Thus both sources matter.

## First-gate versus best-gate distinction

Three cases require support 4 at their **first** successful gate, so the statement "the first successful gate always has support <=3" is false. However each has a later support-two gate:

- `n=1,450,849`: first success `u=47` uses support 4; `u=59` has support 2 via `3^{-1} 983^{-1}`;
- `n=4,935,361`: first success `u=11` uses support 4; `u=23` has support 2 via `2^{-1} n`;
- `n=7,200,481`: first success `u=11` uses support 4; `u=15` has support 2 via `2^{-1} 37^{-1}`.

This distinction matters: the theorem target should quantify over the choice of gate rather than insist on the first successful gate.

## Proposed deterministic theorem target

The corrected finite data suggest replacing the old divisor-distribution conjecture with the following much sharper statement.

> **Two-Factor Cascade Conjecture.** For every prime `n` in the classical residual Erdős--Straus core, there exists `u ≡ 3 (mod 4)` with bounded size, and prime factors `p,q` of `M_u=n(n+u)/4`, such that one of
> \[
> p\equiv-1,\qquad p^3\equiv-1,\qquad pq\equiv-1,\qquad p\equiv-q\pmod u
> \]
> holds, with the required prime valuations available.

Any one of these four relations gives an exact centered witness and hence an explicit Erdős--Straus decomposition.

This target is finite-support, deterministic, directly auditable, and far stronger than merely asserting that a large divisor set becomes equidistributed.
