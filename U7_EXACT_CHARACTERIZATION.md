# Exact u=7 Characterization for the Two Residual Prime Classes

**Date:** 2026-08-28

Consider a prime hard-case candidate in one of the two residual classes

\[
n\equiv1,49\pmod{120}.
\]

Then \(n\equiv1\pmod8\), so for \(u=7\)

\[
x=\frac{n+7}{4}
\]

is even.  Since \(n\ne7\), we also have \(7\nmid nx\).

The exact u-method asks for a divisor \(d\mid(nx)^2\) such that

\[
d\equiv -nx\pmod7.
\]

## Theorem

For these two residue classes, the exact \(u=7\) method fails if and only if

\[
\left(\frac n7\right)=1
\]

and every odd prime divisor \(r\mid x\) satisfies

\[
\left(\frac r7\right)=1.
\]

Equivalently,

\[
\boxed{
 u=7\text{ fails}
 \iff
 n\in\mathrm{QR}_7
 \text{ and every odd prime factor of }(n+7)/4\text{ lies in }\mathrm{QR}_7.
}
\]

## Proof: the failure direction

Assume \(n\) is a quadratic residue modulo 7 and every odd prime divisor of \(x\) is a quadratic residue modulo 7.  The prime 2 is also a quadratic residue modulo 7.  Hence every prime divisor of \(nx\) is a quadratic residue modulo 7, so every divisor of \((nx)^2\) is a quadratic residue modulo 7.

But \(-1\) is a quadratic nonresidue modulo 7.  Since \(nx\) is a quadratic residue,

\[
-nx
\]

is a quadratic nonresidue.  Therefore no divisor of \((nx)^2\) can be congruent to \(-nx\pmod7\), and the exact \(u=7\) method fails.

## Proof: the success direction when n is QNR

The quadratic nonresidues modulo 7 are

\[
3,5,6.
\]

Because \(x\) is even, the centered divisor exponent of 2 may be shifted by \(-1,0,+1\).  For the three QNR residues:

\[
3\cdot2\equiv-1\pmod7,
\]

\[
5\cdot2^{-1}\equiv-1\pmod7,
\]

and

\[
6\equiv-1\pmod7.
\]

Thus if \((n/7)=-1\), a centered product using \(n\) and the guaranteed factor 2 reaches \(-1\), so a divisor \(d\mid(nx)^2\) with \(d\equiv-nx\pmod7\) exists.

## Proof: the success direction when x has a QNR factor

Now assume \((n/7)=1\), but let an odd prime \(r\mid x\) satisfy \((r/7)=-1\).  Again \(r\equiv3,5\), or \(6\pmod7\), and the same three identities give

\[
r\cdot2\equiv-1,
\qquad
r\cdot2^{-1}\equiv-1,
\qquad\text{or}\qquad
r\equiv-1\pmod7,
\]

according as \(r\equiv3,5,6\pmod7\).  Since both 2 and \(r\) divide \(x\), the required centered exponent shifts are allowed inside the divisor range of \((nx)^2\).  Hence the target \(-nx\) is reached and \(u=7\) succeeds.

This proves the characterization.

## Computational audit

The characterization was checked against the exact complementary-divisor verifier for every applicable prime hard case through \(10^7\), with **no mismatches**.

Among the 23,759 applicable hard primes through \(10^7\):

- exact \(u=7\) successes: **16,615**;
- exact \(u=7\) failures: **7,144**.

Thus \(u=7\) alone resolves about 70% of the two residual modulo-120 classes in this range, and the failures are no longer opaque: they are precisely numbers for which both \(n\) and every odd prime factor of \((n+7)/4\) lie in the quadratic-residue subgroup modulo 7.

## Why this matters

The remaining obstruction has become a shifted-factorization problem:

\[
\boxed{
 n\equiv1,49\pmod{120},
 \quad n\in\mathrm{QR}_7,
 \quad \operatorname{Supp}_{\rm odd}\!\left(\frac{n+7}{4}\right)\subseteq\mathrm{QR}_7.
}
\]

A full proof can now target this explicit semigroup condition rather than an informal probability that divisors are well distributed.
