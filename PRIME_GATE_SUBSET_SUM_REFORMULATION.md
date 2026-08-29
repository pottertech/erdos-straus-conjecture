# Prime-Gate Subset-Sum Reformulation

**Date:** 2026-08-28  
**Status:** Exact for prime `u ≡ 3 (mod 4)` with `gcd(nx,u)=1`

Let

\[
x=\frac{n+u}{4},\qquad M=nx,
\]

and let `u` be prime with `u ≡ 3 (mod 4)`. Choose a primitive root `g (mod u)` and write

\[
N=u-1.
\]

For each prime power `p^{a_p} || M`, write

\[
p\equiv g^{d_p}\pmod u,
\qquad d_p\in \mathbb Z/N\mathbb Z.
\]

The exact centered criterion is

\[
\sum_{p\mid M} c_p d_p \equiv N/2 \pmod N,
\qquad -a_p\le c_p\le a_p.
\]

## Exact subset-sum form

Set

\[
b_p=c_p+a_p,
\qquad 0\le b_p\le 2a_p.
\]

Then success is equivalent to

\[
\sum b_p d_p \equiv T\pmod N,
\]

where

\[
T=\frac N2+\sum a_p d_p.
\]

Equivalently, form the sequence `S` in `Z/NZ` containing exactly `2a_p` copies of `d_p` for every prime `p|M`. The `u`-method succeeds iff the target `T` occurs as a subsequence sum of `S`.

Thus a prime gate is an exact structured subsequence-sum problem.

## Square constraint

Modulo prime `u`,

\[
x\equiv n/4,
\]

so

\[
M=nx\equiv n^2/4=(n/2)^2\pmod u.
\]

Hence `M` is always a quadratic residue modulo `u`. Since `u ≡ 3 (mod 4)`, `N/2` is odd. Therefore, with the primitive-root logarithm convention, `L=\sum a_p d_p` is even and

\[
T=N/2+L
\]

is an odd logarithm, i.e. a quadratic-nonresidue target.

The total sum of the sequence `S` is `2L`, and

\[
2L-T\equiv T\pmod N.
\]

So every successful subsequence has a complementary successful subsequence. This is the subset-sum version of the complementary-divisor symmetry.

## Additive-combinatorics interpretation

This formulation makes available the theory of subsequence sums in finite abelian groups, including Kneser-type and DeVos--Goddyn--Mohar type tools. Kneser's theorem explains periodic/small-subgroup failure states, but it is not sufficient by itself for the late capacity exceptions: the extremal `n=8,803,369` has prime-gate failures whose centered/subset-sum sets have trivial stabilizer but still miss the specific target.

The remaining analytic task is therefore target-sensitive:

> Given the repeated-log sequence `S`, prove that the distinguished target `T` must be a subsequence sum for some sufficiently small prime gate `u`.

A natural exact counting route is Fourier inversion on `Z/NZ`. If `R(T)` is the number of centered representations, then

\[
R(T)=\frac1N\sum_{r=0}^{N-1}e^{-2\pi i rT/N}
\prod_{p\mid M}\left(\sum_{c=-a_p}^{a_p}e^{2\pi i r c d_p/N}\right).
\]

The `r=0` contribution is

\[
\frac1N\prod_{p\mid M}(2a_p+1).
\]

Hence any bound showing that the total magnitude of the nontrivial Fourier terms is strictly smaller than the main term proves `R(T)>0` and therefore proves the gate succeeds.

This gives a rigorous analytic replacement for the earlier independence heuristic: no random-prime assumption is needed; the problem is to control explicit finite character sums determined by the actual prime-factor logarithms.
