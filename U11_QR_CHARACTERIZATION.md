# Exact u=11 Characterization on the n ≡ 25 (mod 36) Slice

**Date:** 2026-08-28

Let \(n\) be a prime hard-case candidate in one of the two residual classes

\[
n\equiv1,49\pmod{120},
\]

and suppose additionally that

\[
n\equiv25\pmod{36}.
\]

For \(u=11\), set

\[
x=\frac{n+11}{4}.
\]

Then \(n\equiv25\pmod{36}\) implies \(36\mid n+11\), hence

\[
9\mid x.
\]

## Theorem

On this congruence slice, the exact \(u=11\) method fails if and only if \(n\) and every prime divisor of \(x\) are quadratic residues modulo 11:

\[
\boxed{
 u=11\text{ fails}
 \iff
 \left(\frac n{11}\right)=1
 \text{ and }
 \left(\frac r{11}\right)=1\text{ for every prime }r\mid x.
}
\]

## Proof

The multiplicative group \((\mathbb Z/11\mathbb Z)^\times\) is cyclic of order 10.  Take primitive root \(g=2\).  Then

\[
3=g^8=g^{-2},
\qquad
-1=g^5.
\]

Because \(9\mid x\), the centered exponent of the factor 3 in a divisor of \((nx)^2\) may range at least over

\[
-2,-1,0,1,2.
\]

Suppose a prime factor \(r\) of \(nx\) is a quadratic nonresidue modulo 11.  Its discrete logarithm \(R=\log_g r\) is odd, so

\[
R\in\{1,3,5,7,9\}\pmod{10}.
\]

For every odd \(R\) there is a \(k\in[-2,2]\) such that

\[
R-2k\equiv5\pmod{10}.
\]

Explicitly:

\[
(R,k)=(1,-2),(3,-1),(5,0),(7,1),(9,2).
\]

Thus a centered product of \(r\) and an allowed power of 3 is congruent to \(-1\pmod{11}\).  By the centered divisor criterion, the exact target \(-nx\) is hit and \(u=11\) succeeds.

Conversely, if \(n\) and every prime factor of \(x\) are quadratic residues modulo 11, then every divisor of \((nx)^2\) is a quadratic residue.  Since \(-1\) is a quadratic nonresidue modulo 11 and \(nx\) is a quadratic residue, the target \(-nx\) is a nonresidue and cannot be represented by any divisor.  Hence \(u=11\) fails.

## Computational audit

The theorem was checked against the exact complementary-divisor verifier for every applicable prime hard case through \(10^7\):

- applicable hard primes: **7,904**;
- exact \(u=11\) failures: **2,373**;
- mismatches with the characterization: **0**.

This supplies a second exact factor-support obstruction, complementary to the \(u=7\) characterization.
