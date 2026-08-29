# Corrected Classical-Core Cascade Through 10^7

**Date:** 2026-08-28  
**Status:** Exact centered-criterion computation; finite evidence only

This note records the corrected cascade after applying the classical modular front end and the exact centered u-method criterion.  It supersedes older large-range summaries that began from the nonminimal `n ≡ 1 (mod 12)` population or used the obsolete `{-x,-xn,-xn^2}` shortcut.

## 1. Canonical population

For prime `n <= 10^7`:

1. retain only the six classical residue classes
   \[
   n\equiv1,121,169,289,361,529\pmod{840};
   \]
2. apply the repository's A=3 / hard-case gate;
3. apply the exact `n+1` / `n+4` shift-divisor reduction.

Counts:

- primes in the six classes: **20,513**;
- after the A=3/hard gate: **11,923**;
- after shift-divisor reduction: **3,649**.

The 3,649 cases are the corrected finite population entering the centered u-cascade.

## 2. Exact cascade

For every gate, `x=(n+u)/4`, `M=nx`, and success is tested using the exact centered product-set criterion when `gcd(M,u)=1`.

| u | entering | success | failure |
|---:|---:|---:|---:|
| 7 | 3,649 | 1,512 | 2,137 |
| 11 | 2,137 | 1,083 | 1,054 |
| 15 | 1,054 | 373 | 681 |
| 19 | 681 | 293 | 388 |
| 23 | 388 | 238 | 150 |
| 27 | 150 | 41 | 109 |
| 31 | 109 | 74 | 35 |
| 35 | 35 | 12 | 23 |
| 39 | 23 | 9 | 14 |
| 43 | 14 | 2 | 12 |
| 47 | 12 | 8 | 4 |
| 51 | 4 | 1 | 3 |
| 55 | 3 | 1 | 2 |
| 59 | 2 | 1 | 1 |
| 67 | 1 | 0 | 1 |
| 71 | 1 | 0 | 1 |
| 79 | 1 | 0 | 1 |
| 83 | 1 | 0 | 1 |
| 87 | 1 | 0 | 1 |
| 95 | 1 | 0 | 1 |
| 103 | 1 | 0 | 1 |
| 107 | 1 | 1 | 0 |

Thus the corrected cascade has **zero failures** in this finite range.  The final survivor before `u=107` is again

\[
\boxed{n=8,803,369}.
\]

This is computational evidence only; it is not a proof for arbitrary n.

## 3. Quadratic-nonresidue profiles at prime gates

For prime `u ≡ 3 (mod 4)`, the shifted product

\[
M_u=n(n+u)/4
\]

is itself a quadratic residue modulo u.  Therefore the total valuation of QNR prime factors of `M_u` is even.

Among the failures at the prime gates in this finite cascade:

| u | failures | QNR total 0 | QNR total 2 | QNR total 4 |
|---:|---:|---:|---:|---:|
| 7 | 2,137 | 2,137 | 0 | 0 |
| 11 | 1,054 | 909 | 145 | 0 |
| 19 | 388 | 282 | 104 | 2 |
| 23 | 150 | 142 | 8 | 0 |
| 31 | 35 | 23 | 12 | 0 |
| 43 | 12 | 6 | 6 | 0 |
| 47 | 4 | 4 | 0 | 0 |
| 59 | 1 | 0 | 1 | 0 |
| 67 | 1 | 0 | 1 | 0 |
| 71 | 1 | 1 | 0 | 0 |
| 79 | 1 | 0 | 1 | 0 |
| 83 | 1 | 0 | 1 | 0 |
| 103 | 1 | 0 | 1 | 0 |

The dominant obstruction is factorwise quadratic-residue purity.  The next most common failure type has the minimum possible nonzero QNR valuation, namely 2.

## 4. Important counterexample to an over-strong conjecture

The data **do not** support the universal statement

> QNR valuation at least 4 forces success.

At `u=19` there are two failures with total QNR valuation 4:

### n = 4,622,209

Observed capacity vector:

\[
(0,0,2,0,2,0,0,0,0),
\]

with

\[
M_{19}\text{ having prime factors }\{13,103,863,4,622,209\}.
\]

### n = 6,088,009

Observed capacity vector:

\[
(3,0,1,0,0,0,0,0,0),
\]

with

\[
M_{19}\text{ having prime factors }\{29,31,1693,6,088,009\}.
\]

These cases should be retained as regression tests for any proposed character-only theorem.

## 5. The 8,803,369 path

The last finite survivor has the following prime-gate QNR profile before its success at 107:

- `u=7`: QNR total 0;
- `u=11`: 0;
- `u=19`: 0;
- `u=23`: 0;
- `u=31`: 0;
- `u=43`: 2;
- `u=47`: 0;
- `u=59`: 2;
- `u=67`: 2;
- `u=71`: 0;
- `u=79`: 2;
- `u=83`: 2;
- `u=103`: 2;
- `u=107`: succeeds with QNR total 2.

This makes it a useful stress test for any finite-state or character-based cascade theorem.

## 6. Interpretation

The corrected data support a substantially narrower research question than the earlier divisor-distribution heuristic:

> Why can the shifted products `M_u=n(n+u)/4` not remain inside the exact finite-state failure profiles for every successive u?

At prime gates, the dominant profile is factorwise QR purity plus a small set of bounded-capacity QNR exceptions.  At composite gates, the analogous obstruction is subgroup purity inside `(Z/uZ)^*`.

The next exact step is to formulate the capacity criterion uniformly for arbitrary finite abelian unit groups, so all prime, prime-power, and composite gates can be analyzed in the same language.
