# Constructive Erdős--Straus Identities from Short Centered Relations

**Date:** 2026-08-28  
**Status:** Exact algebraic corollaries of the centered criterion

Let

\[
u\equiv3\pmod4,\qquad x=\frac{n+u}{4},\qquad M=nx,
\]

with `gcd(M,u)=1`. The u-method factorization is

\[
(uy-M)(uz-M)=M^2.
\]

Suppose a centered ratio `r` satisfies

\[
r\equiv-1\pmod u
\]

and both

\[
d=Mr,\qquad d'=M/r
\]

are positive integers. Then `dd'=M^2` and both are congruent to `-M mod u`, so

\[
y=\frac{d+M}{u},\qquad z=\frac{d'+M}{u}
\]

are positive integers and

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

The short-support relations observed in the corrected cascade therefore give the following explicit formulas.

## 1. One-factor relation p ≡ -1 (mod u)

Assume `p|M` and

\[
p\equiv-1\pmod u.
\]

Take `r=p`. Then

\[
\boxed{
 y=\frac{M(p+1)}u,
 \qquad
 z=\frac{M(p+1)}{up}.
}
\]

The second denominator is integral because `p|M` and `u|(p+1)`.

## 2. One-factor cubic relation p^3 ≡ -1 (mod u)

Assume `p^3|M` and

\[
p^3\equiv-1\pmod u.
\]

Take `r=p^3`. Then

\[
\boxed{
 y=\frac{M(p^3+1)}u,
 \qquad
 z=\frac{M(p^3+1)}{u p^3}.
}
\]

This is the exact constructive form of the rare one-factor `|c|=3` route seen in the finite cascade.

## 3. Two-factor product relation pq ≡ -1 (mod u)

Assume distinct primes `p,q|M` and

\[
pq\equiv-1\pmod u.
\]

Take `r=pq`. Since `pq|M`,

\[
\boxed{
 y=\frac{M(pq+1)}u,
 \qquad
 z=\frac{M(pq+1)}{u pq}.
}
\]

Thus every product-route witness immediately yields a closed-form Erdős--Straus decomposition.

## 4. Two-factor opposite-residue relation p ≡ -q (mod u)

Assume distinct primes `p,q|M` and

\[
p\equiv-q\pmod u.
\]

Equivalently,

\[
pq^{-1}\equiv-1\pmod u.
\]

Take

\[
r=p/q.
\]

Since `p,q|M`, both `Mp/q` and `Mq/p` are integers. The denominators simplify to

\[
\boxed{
 y=\frac{M(p+q)}{u q},
 \qquad
 z=\frac{M(p+q)}{u p}.
}
\]

Integrality follows from `u|(p+q)`.

## 5. Symmetry

Replacing `r` by `r^{-1}` exchanges `y` and `z`. Therefore the signs/orientations of the centered exponents do not produce essentially different decompositions.

## 6. Proof target

The corrected finite data through `10^7` show that every one of the 3,649 classical-core residual prime cases has, for some `u<=299`, one of exactly these four short relations:

\[
p\equiv-1,
\qquad
p^3\equiv-1,
\qquad
pq\equiv-1,
\qquad
p\equiv-q
\pmod u.
\]

Thus a proof of the Two-Factor Cascade Conjecture would immediately become a constructive proof: the formulas above produce `x,y,z` explicitly once the short relation is found.
