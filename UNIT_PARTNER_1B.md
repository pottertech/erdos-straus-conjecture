# Unit-Partner Verification Through 10^9

**Date:** 2026-08-28  
**Status:** exact finite computation; not a global proof

This extends the corrected unit-partner search through

\[
 n\le 10^9.
\]

The population is restricted exactly as in the earlier corrected work:

1. prime `n` in the six classical residue classes modulo 840;
2. surviving the corrected A=3/hard gate;
3. surviving the exact `n+1` / `n+4` shift-divisor reductions.

The factorization helper was widened to trial primes through 40,000 before this run. This is required because `shift_reduced()` factors `n+1` and `n+4`; the earlier 12,000-prime table was not range-safe above roughly `1.44e8` and could silently treat a composite residual as prime. The 1e9 result below uses the corrected range-safe factorizer and was rerun from the beginning.

## Audited population

Through `n <= 1,000,000,000`:

- primes in the six classical residue classes: **1,587,581**;
- after the corrected hard gate: **807,836**;
- after exact shift reductions: **195,271**;
- unit-partner certificates with `u <= 299`: **195,270**;
- unit-partner failures: **1**;
- reconstructed certificates failing exact cross multiplication: **0**.

Thus

\[
\boxed{195270/195271}
\]

of the corrected residual population has a unit-partner certificate with `u <= 299`.

The unique failure is still

\[
\boxed{n=2521}.
\]

As recorded elsewhere, `2521` is explicitly solved by the non-unit-partner untwisted pair `2,29` at shift `u=31`.

## Branch counts

Among the 195,270 unit-partner certificates:

- untwisted/unit-partner branch `d | K`, `d == -1 (mod u)`: **111,002**;
- twisted/unit-partner branch `d | K`, `n*d == -1 (mod u)`: **84,268**.

Here

\[
K=\frac{n+u}{4}.
\]

## Most common gates

The first successful unit-partner gates in ascending `u` order begin:

| `u` | certificates |
|---:|---:|
| 7 | 94,013 |
| 11 | 56,244 |
| 15 | 19,808 |
| 19 | 10,006 |
| 23 | 8,363 |
| 31 | 2,804 |
| 27 | 1,836 |
| 39 | 745 |
| 35 | 645 |
| 47 | 308 |
| 43 | 126 |
| 55 | 92 |
| 51 | 72 |
| 59 | 62 |
| 63 | 43 |

The largest first successful unit-partner gate observed is

\[
\boxed{u=191}
\]

at

\[
\boxed{n=294,707,449}.
\]

For this case

\[
K=73,676,910=2\cdot3\cdot5\cdot2,455,897,
\]

and a valid unit-partner divisor is

\[
s=24,558,970\equiv -1\pmod{191}.
\]

With

\[
r=\frac{s+1}{191}=128,581,
\qquad
k=\frac{nK}{s}=884,122,347,
\]

the explicit denominators are

\[
X=73,676,910,
\]

\[
Y=2,791,896,508,094,783,324,790,
\]

\[
Z=113,681,335,499,607,
\]

and exact integer arithmetic verifies

\[
4XYZ=n(XY+XZ+YZ).
\]

## Research interpretation

The strongest finite observation is now:

> **Unit-Partner Cascade Observation through 10^9.** After the corrected classical and shift reductions, every residual prime `n <= 10^9` except `2521` has some shift `u <= 299`, `u == 3 (mod 4)`, for which the complete fixed-shift binary criterion succeeds with one divisor equal to `1`.

Equivalently, for every such prime except `2521`, there are `u <= 299` and `d | K_u` such that either

\[
d\equiv-1\pmod u
\]

or

\[
nd\equiv-1\pmod u.
\]

This is a finite computational statement only. Benjamin Dahan's 2026 sieve results show in particular that a single fixed shift can have an infinite blind set, so the observed phenomenon must genuinely use a varying cascade of shifts.
