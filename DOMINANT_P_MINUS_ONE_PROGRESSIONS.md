# Dominant `p ≡ -1 (mod u)` Progression Families Through 10^8

**Date:** 2026-08-29  
**Status:** Exact theorem plus finite frequency data; not a proof of the full conjecture

## 1. Exact progression theorem

Let

\[
u\equiv 3\pmod 4,
\qquad p>0,
\qquad u\mid p+1.
\]

Suppose

\[
 n\equiv -u\pmod{4p}.
\]

Then

\[
 x=\frac{n+u}{4}
\]

is a positive integer divisible by `p`. Hence `p|M=nx`, and

\[
 p\equiv -1\pmod u.
\]

Therefore the one-factor centered relation applies. Writing

\[
 m=\frac{x}{p}=\frac{n+u}{4p},
\qquad r=\frac{p+1}{u},
\]

we obtain the explicit Erdős--Straus decomposition

\[
\boxed{
 x=pm,
 \qquad
 y=npm(p+1)/u=npmr,
 \qquad
 z=nm(p+1)/u=nmr.
}
\]

Equivalently,

\[
\frac4n=rac1x+\frac1y+\frac1z.
\]

Thus every admissible pair `(u,p)` with `u|(p+1)` yields an unconditional arithmetic progression of solved `n` values:

\[
\boxed{n\equiv-u\pmod{4p}.}
\]

Primality of `p` is not required for the algebraic identity, although the computational short-relation miner records prime factors.

## 2. Connection with the finite data

In the corrected classical-core computation through `10^8`, 21,399 of the 26,399 residual primes have a minimal-support certificate of the form

\[
 p\equiv-1\pmod u.
\]

Each such certificate belongs to one of the exact progressions above.

The most frequent observed `(u,p)` pairs are:

| rank | u | p | progression | occurrences through 10^8 |
|---:|---:|---:|---|---:|
| 1 | 7 | 13 | `n ≡ -7 (mod 52)` | 2,202 |
| 2 | 7 | 41 | `n ≡ -7 (mod 164)` | 635 |
| 3 | 15 | 29 | `n ≡ -15 (mod 116)` | 630 |
| 4 | 11 | 43 | `n ≡ -11 (mod 172)` | 501 |
| 5 | 19 | 37 | `n ≡ -19 (mod 148)` | 405 |
| 6 | 7 | 83 | `n ≡ -7 (mod 332)` | 308 |
| 7 | 15 | 59 | `n ≡ -15 (mod 236)` | 301 |
| 8 | 27 | 53 | `n ≡ -27 (mod 212)` | 263 |
| 9 | 7 | 97 | `n ≡ -7 (mod 388)` | 241 |
| 10 | 31 | 61 | `n ≡ -31 (mod 244)` | 207 |
| 11 | 11 | 109 | `n ≡ -11 (mod 436)` | 178 |
| 12 | 15 | 89 | `n ≡ -15 (mod 356)` | 174 |
| 13 | 7 | 139 | `n ≡ -7 (mod 556)` | 169 |
| 14 | 7 | 167 | `n ≡ -7 (mod 668)` | 157 |
| 15 | 11 | 131 | `n ≡ -11 (mod 524)` | 146 |
| 16 | 19 | 113 | `n ≡ -19 (mod 452)` | 136 |
| 17 | 7 | 181 | `n ≡ -7 (mod 724)` | 130 |
| 18 | 15 | 149 | `n ≡ -15 (mod 596)` | 112 |
| 19 | 27 | 107 | `n ≡ -27 (mod 428)` | 101 |
| 20 | 7 | 251 | `n ≡ -7 (mod 1004)` | 99 |

The top 20 pairs account for 7,095 of the 21,399 `p=-1` certificates, about **33.2%** of that route in the finite sample.

## 3. Gate frequencies for the dominant route

The most common gates among the 21,399 `p=-1` certificates are:

| u | count |
|---:|---:|
| 7 | 6,557 |
| 15 | 2,930 |
| 11 | 2,703 |
| 19 | 1,361 |
| 27 | 926 |
| 23 | 612 |
| 31 | 601 |
| 39 | 532 |
| 35 | 416 |
| 55 | 305 |

The dominance of small gates is strong, but no finite list is asserted to be globally sufficient.

## 4. Why this reformulation matters

The statement

> `x_u` happens to contain a prime factor `p ≡ -1 (mod u)`

looks like a factor-distribution assertion. But once a particular pair `(u,p)` is fixed, it is exactly the deterministic congruence family

\[
 n\equiv-u\pmod{4p}.
\]

This converts a large fraction of the empirical dominant route into explicit infinite families that can be combined using CRT and ordinary covering-system methods.

The next proof question is therefore:

> Can a finite or structurally controlled collection of admissible pairs `(u,p)` cover a provably positive-density portion of the six classical residual classes modulo 840, and can the uncovered set be shown to satisfy extra arithmetic restrictions that force one of the two-factor routes?

This is narrower than the original divisor-distribution program and is fully constructive.
