# Exact Real Fourier Formula for Prime Capacity Gates

**Date:** 2026-08-28  
**Status:** Exact identity

Let `u ≡ 3 (mod 4)` be prime, let `N=u-1=2m`, and choose a primitive root `g mod u`. Since `u ≡ 3 (mod 4)`, `m` is odd.

For

\[
M=n\frac{n+u}{4}=\prod p^{a_p},
\]

write

\[
p\equiv g^{d_p}\pmod u.
\]

The exact centered criterion asks for

\[
\sum c_p d_p\equiv m\pmod N,
\qquad -a_p\le c_p\le a_p.
\]

Let `R_u(n)` be the number of such centered exponent vectors.

## Fourier inversion

Define the real Dirichlet kernels

\[
D_a(\theta)=\sum_{c=-a}^{a}e^{ic\theta}
           =1+2\sum_{c=1}^{a}\cos(c\theta).
\]

Then

\[
R_u(n)=\frac1N\sum_{r=0}^{N-1}(-1)^r
\prod_{p\mid M}D_{a_p}\!\left(\frac{2\pi r d_p}{N}\right).
\]

The phase is exactly `(-1)^r` because the target is `m=N/2`. Since every local kernel is real and the terms for `r` and `N-r` agree, this becomes

\[
\boxed{
R_u(n)=\frac1N\left(Q-F_m+2\sum_{r=1}^{m-1}(-1)^r F_r\right),
}
\]

where

\[
Q=\prod_p(2a_p+1),
\qquad
F_r=\prod_p D_{a_p}\!\left(\frac{2\pi r d_p}{N}\right),
\]

and

\[
F_m=\prod_p\sum_{c=-a_p}^{a_p}(-1)^{c d_p}.
\]

## The special frequency r=m

If `d_p` is even, the corresponding factor in `F_m` is `2a_p+1`. If `d_p` is odd, it is `(-1)^{a_p}`.

But

\[
M\equiv(n/2)^2\pmod u,
\]

so the total weighted parity of the odd `d_p` is even. Hence the product of all odd-log signs is `+1`, and

\[
\boxed{
F_m=\prod_{d_p\ \mathrm{even}}(2a_p+1).
}
\]

Thus pure quadratic-residue factorizations have `F_m=Q`; mixed QR/QNR factorizations have a strictly smaller special-frequency term.

## Complement symmetry

If `c=(c_p)` represents the target `m`, then `-c` also represents `m` because `-m ≡ m (mod 2m)`. The zero vector cannot represent `m`. Therefore

\[
\boxed{R_u(n)\text{ is always even}.}
\]

So a successful prime gate has at least two centered witnesses, naturally paired by complementary divisors.

## Extremal case n=8,803,369

For the last corrected `10^7` survivor, the late prime capacity failures have trivial stabilizer, so Kneser periodicity does not explain them. The exact representation counts are zero at `u=43,59,67,79,83,103`.

At `u=107`,

\[
M=8,803,369\cdot2,200,869,
\]

with

\[
2,200,869=3^2\cdot11^2\cdot43\cdot47.
\]

There are exactly two centered representations, the complementary pair

\[
3^2\cdot43\cdot47\equiv-1\pmod{107}
\]

and its inverse. Equivalently, the exponent vectors use

\[
(c_3,c_{43},c_{47})=(2,1,1)
\]

or `(-2,-1,-1)`, while the factors `11` and `n` are unused.

This is important: even the extremal gate succeeds through a support-3 relation. Full product-set coverage at `u=107` is stronger than necessary.

## Consequence for proof strategy

There are now two rigorous analytic routes:

1. **short-support route:** prove that for some small gate one, two, or three prime-power residues multiply to `-1` within the available valuation bounds;
2. **Fourier route:** prove `R_u(n)>0` by controlling the explicit alternating finite Fourier sum above.

The first route is closer to the observed data; the second gives a target-sensitive analytic fallback that avoids the invalid independence assumptions of the earlier manuscript.
