# One-Divisor Collapse Through 10^8

**Date:** 2026-08-28  
**Status:** exact finite computation plus exact constructive lemma; not a global proof

Consider the corrected classical-core residual population used by `short_relation_miner.py`:

1. prime `n` in the six classical residue classes modulo 840;
2. surviving the corrected A=3/hard gate;
3. surviving the exact `n+1` / `n+4` shift-divisor reductions.

There are **26,399** such primes with `n <= 100,000,000`.

For each gate `u ≡ 3 (mod 4)`, define

\[
x_u=\frac{n+u}{4},\qquad M_u=n x_u.
\]

## Exact one-divisor endpoint

Suppose there is any positive divisor `s | M_u` such that

\[
\boxed{s\equiv-1\pmod u.}
\]

Write

\[
M_u=s k,\qquad s+1=u r.
\]

Then

\[
X=x_u,\qquad Y=M_u r,\qquad Z=k r
\]

are positive integers and satisfy

\[
\boxed{\frac4n=\frac1X+\frac1Y+\frac1Z.}
\]

Equivalently,

\[
4XYZ=n(XY+XZ+YZ).
\]

This is exactly the already-formalized generic endpoint `short_product_endpoint`; importantly, `s` need not be prime.

## Finite result through 10^8

Searching all gates

\[
u=3,7,11,\ldots,299
\]

for an arbitrary divisor `s | M_u` gives:

- corrected residual primes: **26,399**;
- primes with a one-divisor certificate: **26,398**;
- failures of the one-divisor test: **1**;
- all 26,398 explicit decompositions independently checked by exact integer cross multiplication;
- bad certificates: **0**.

Thus

\[
\boxed{\frac{26,398}{26,399}=99.9962\%}
\]

of the corrected residual population is already captured by the single condition `s = -1 mod u` once `s` is allowed to be any divisor of `M_u`, rather than a single prime factor.

## Unique finite exception

The sole one-divisor exception below `10^8` is

\[
\boxed{n=2521.}
\]

It nevertheless has a two-factor opposite-residue certificate at `u=31`:

\[
x=\frac{2521+31}{4}=638=2\cdot11\cdot29,
\]

and

\[
2+29=31.
\]

Taking `p=2`, `q=29`, and

\[
k=\frac{2521\cdot638}{2\cdot29}=27,731
\]

gives the explicit denominators

\[
\boxed{X=638,\qquad Y=55,462,\qquad Z=804,199.}
\]

Direct integer verification gives

\[
4XYZ=2521(XY+XZ+YZ).
\]

## Research consequence

The previous support-two conjecture can be sharpened drastically for the tested range.
The dominant theorem target is now:

> **One-Divisor Cascade Target.** After the classical reductions, prove that for every remaining prime `n` other than finitely many explicitly handled exceptions, there exists some `u ≡ 3 (mod 4)` and some divisor
> \[
> s\mid n\frac{n+u}{4}
> \]
> such that
> \[
> s\equiv-1\pmod u.
> \]

This is a bounded divisor-residue problem, but it is substantially simpler than the earlier full centered product-set statement: it asks for a positive divisor of `M_u` in one residue class, not a signed product of prime factors.

The unique finite exception `2521` is already explicitly solved by the opposite-residue endpoint, so a theorem of this form would close the corrected residual class once the finite exception is included.

No global claim is made from the finite computation alone.
