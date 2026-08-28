# Shift-Divisor Reduction from the Exact Centered Criterion

**Date:** 2026-08-28

## Exact setup

Let `n ≡ 1 (mod 4)` and let `u ≡ 3 (mod 4)` be positive. Define

\[
x=\frac{n+u}{4},\qquad M=nx.
\]

The exact u-method factorization is

\[
(uy-M)(uz-M)=M^2.
\]

If `gcd(M,u)=1`, the centered criterion says that the u-method succeeds iff the bounded signed divisor-product set of `M` contains `-1 (mod u)`.

## Two aggregate-factor families

The aggregate factors `n` and `x` alone already give two universal sufficient conditions.

### Family A: `u | n+1`

If

\[
n\equiv -1\pmod u,
\]

then the centered ratio `n` itself is `-1 mod u`. Choose

\[
d_1=n^2x,\qquad d_2=x.
\]

Since `d_1 d_2=M^2`, both factors satisfy

\[
d_i\equiv -M\pmod u.
\]

The resulting denominators are

\[
X=x,\qquad
Y=\frac{nx(n+1)}u,\qquad
Z=\frac{x(n+1)}u.
\]

Therefore every `n ≡ 1 (mod 4)` for which `n+1` has a divisor `u ≡ 3 (mod 4)` has an explicit Erdős--Straus decomposition. This recovers the classical Obláth-type divisor criterion.

### Family B: `u | n+4`

If

\[
n\equiv -4\pmod u,
\]

then

\[
x\equiv -1\pmod u.
\]

Choose

\[
d_1=nx^2,\qquad d_2=n.
\]

The resulting denominators are

\[
X=x,\qquad
Y=\frac{nx(x+1)}u,\qquad
Z=\frac{n(x+1)}u.
\]

Thus every `n ≡ 1 (mod 4)` for which `n+4` has a divisor `u ≡ 3 (mod 4)` is also solved explicitly.

## Immediate u=7 corollary

Taking `u=7` gives two unconditional arithmetic progressions:

- `n ≡ 13 (mod 28)` (equivalently `n ≡ -1 (mod 7)`),
- `n ≡ 17 (mod 28)` (equivalently `n ≡ -4 (mod 7)`).

These are exact infinite families, with the closed-form denominators above.

## Counterexample rigidity

Consequently, any counterexample with `n ≡ 1 (mod 4)` must satisfy both:

1. every odd prime factor of `n+1` is `1 (mod 4)`;
2. every prime factor of `n+4` is `1 (mod 4)`.

Indeed, any prime factor congruent to `3 (mod 4)` can itself be chosen as `u`.

This is a useful deterministic reduction because it replaces a search over many u-values by explicit arithmetic restrictions on two neighboring shifts.

## Corrected computational effect on prime hard cases below 10^6

Among the 6,246 prime hard cases below `10^6`:

- 5,160 are eliminated by the `n+1` or `n+4` shift-divisor criteria;
- 1,086 survive both restrictions.

Thus the two shift criteria remove approximately **82.6%** of the prime hard cases in this range.

For the 1,086 residual cases, the exact centered/direct u-method still found a solution with the following first-working distribution (searching `u = 3,7,11,...,159`):

| u | count |
|---:|------:|
| 7 | 744 |
| 11 | 164 |
| 15 | 59 |
| 19 | 51 |
| 23 | 39 |
| 27 | 7 |
| 31 | 15 |
| 35 | 1 |
| 39 | 2 |
| 43 | 1 |
| 47 | 1 |
| 51 | 1 |
| 59 | 1 |

No residual failure occurred below `10^6`; the largest first-working value there is `u=59`, at `n=806521`.

These finite computations are evidence only; the shift-divisor families themselves are unconditional algebraic results.

## Next theorem target

After imposing the shift-divisor rigidity, the remaining problem becomes substantially narrower. A residual counterexample must simultaneously satisfy:

- the standard Erdős--Straus hard-case restrictions;
- 1-mod-4 purity of the odd part of `n+1`;
- 1-mod-4 purity of `n+4`;
- failure of the bounded centered product set to contain `-1` for every tested `u`.

The next useful goal is to combine these purity conditions with the exact centered product-set obstruction for `u=7,11,15,...` and derive an incompatibility or a further deterministic residue/factor reduction.
