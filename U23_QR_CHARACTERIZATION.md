# Exact u=23 Characterization on High-Valuation Slices

**Date:** 2026-08-28

Let \(n\) be a prime hard-case candidate in one of the two residual classes

\[
n\equiv1,49\pmod{120}.
\]

For \(u=23\), define

\[
x=\frac{n+23}{4}.
\]

Since the residual classes satisfy \(n\equiv1\pmod{24}\), the integer \(x\) is always divisible by \(6\).

Assume in addition that

\[
4\mid x\qquad\text{or}\qquad 9\mid x.
\]

Equivalently, it is enough that

\[
n\equiv9\pmod{16}
\qquad\text{or}\qquad
n\equiv13\pmod{36}.
\]

## Theorem

On this union of congruence slices, the exact \(u=23\) method fails if and only if \(n\) and every prime divisor of \(x\) are quadratic residues modulo 23:

\[
\boxed{
 u=23\text{ fails}
 \iff
 \left(\frac n{23}\right)=1
 \text{ and }
 \left(\frac r{23}\right)=1\text{ for every prime }r\mid x.
}
\]

## Proof

The group \((\mathbb Z/23\mathbb Z)^\times\) is cyclic of order 22.  Take primitive root \(g=5\).  Then

\[
2=g^2,
\qquad
3=g^{16}=g^{-6},
\qquad
-1=g^{11}.
\]

A quadratic nonresidue has odd discrete logarithm.  To move an arbitrary odd logarithm to \(11\pmod{22}\), it is enough that the centered powers of 2 and 3 realize every even logarithm.

After dividing by 2, the even-log subgroup is \(\mathbb Z/11\mathbb Z\), and the available shifts are

\[
a-3b\pmod{11},
\]

where

\[
|a|\le v_2(x),
\qquad
|b|\le v_3(x).
\]

If \(v_2(x)\ge2\) and \(v_3(x)\ge1\), the set

\[
\{a-3b:|a|\le2,\ |b|\le1\}
\]

is all of \(\mathbb Z/11\mathbb Z\).  The same is true when \(v_2(x)\ge1\) and \(v_3(x)\ge2\).  Therefore, under \(4\mid x\) or \(9\mid x\), any QNR prime factor of \(nx\) can be shifted to \(-1\), giving a centered divisor product that hits the exact target.

Conversely, if \(n\) and every prime factor of \(x\) are quadratic residues modulo 23, then every divisor of \((nx)^2\) is a quadratic residue.  Since \(-1\) is a nonresidue modulo 23, \(-nx\) is a nonresidue and cannot be a divisor residue.  Thus \(u=23\) fails.

## Computational audit

The theorem was checked against the exact complementary-divisor verifier for all applicable prime hard cases through \(10^7\):

- applicable hard primes: **15,887**;
- exact \(u=23\) failures: **4,360**;
- mismatches with the characterization: **0**.

Together with the exact \(u=7\) theorem and the \(u=11\) theorem on \(n\equiv25\pmod{36}\), this gives a growing family of deterministic local characterizations in which failure is equivalent to the complete prime support of \(nx\) lying in a quadratic-residue subgroup.
