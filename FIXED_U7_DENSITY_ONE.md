# Fixed `u=7` Gives a Density-One Family

**Date:** 2026-08-29  
**Status:** Unconditional density theorem; presented as a clean rederivation, not a novelty claim.

## 1. Statement

Among integers

\[
 n\equiv1\pmod4,
\]

the set solved by the one-factor `u=7` short relation has relative natural density **1**.

Equivalently, the set of `n ≡ 1 (mod 4)` for which this particular `u=7` one-factor route fails has relative natural density zero.

This does **not** say that `u=7` solves every such `n`; the exceptional set may be infinite.

## 2. Proof

Write

\[
 x=\frac{n+7}{4},
\]

so that

\[
 n=4x-7.
\]

Suppose `x` has a prime factor `p` satisfying

\[
 p\equiv6\pmod7.
\]

Then

\[
 p\equiv-1\pmod7,
\]

and because `p|x`, the one-factor centered relation applies at `u=7`. Thus `n` has an explicit Erdős--Straus decomposition.

Therefore a failure of this one-factor route requires that `x` have **no** prime divisor in the arithmetic progression

\[
 p\equiv6\pmod7.
\]

By the classical prime-number theorem / Mertens theorem for arithmetic progressions,

\[
\sum_{\substack{p\le X\\p\equiv6\ (7)}}\frac1p
\]

diverges as `X -> infinity`. Hence

\[
\prod_{\substack{p\le X\\p\equiv6\ (7)}}\left(1-\frac1p\right)
\longrightarrow0.
\]

The standard sieve consequence is that the set of positive integers `x` divisible by none of the primes `p ≡ 6 (mod 7)` has natural density zero.

Since `x -> n=4x-7` is a bijection from positive integers to the sufficiently large integers `n ≡ 1 (mod 4)`, the corresponding exceptional `n` also have relative density zero inside that lattice.

Thus the `u=7` one-factor route solves a relative density-one subset of `n ≡ 1 (mod 4)`.

## 3. Explicit decomposition

If

\[
p\mid x,
\qquad p\equiv-1\pmod7,
\]

let

\[
M=nx.
\]

Then

\[
 y=\frac{M(p+1)}7,
 \qquad
 z=\frac{M(p+1)}{7p}
\]

are positive integers and

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

## 4. Relation to the finite cascade

This theorem explains structurally why `u=7` is the dominant gate in the corrected finite computations. The finite tables are not needed for the density proof.

It also explains why a fixed-gate argument can be simultaneously:

- asymptotically overwhelming, and
- insufficient for a proof of the full conjecture.

A density-zero exceptional set can still contain infinitely many integers.

## 5. Literature positioning

Almost-all results for Erdős--Straus are classical, including work of Vaughan, and recent semi-constructive work by Christopher Farah uses closely related prime-factor/CRT independence ideas. In particular:

- Christopher Farah, *Semi-Constructive Approach to the Erdős--Straus Conjecture*, SSRN 5378462 (posted 2025; revised 2026).

Accordingly, this note records the fixed-`u=7` argument as a concise consequence of the corrected short-relation framework, **not** as a claim of a new almost-all theorem.

## 6. Strategic consequence

The full conjecture lives entirely in a thin exceptional set from the point of view of this gate. A useful deterministic proof program is therefore to characterize integers `x=(n+7)/4` whose prime factors all avoid `6 mod 7`, then combine those restrictions with the `u=11,15,19,...` short-relation families.
