# QR-Subgroup Coverage Theorem for the Exact u-Method

**Date:** 2026-08-28

This theorem unifies the exact local characterizations found for \(u=7,11,23\).

## Setup

Let \(u\equiv3\pmod4\) be prime, let

\[
x=\frac{n+u}{4},
\qquad
N=nx,
\]

and assume \(u\nmid N\).  The exact u-method succeeds precisely when a divisor of \(N^2\) is congruent to \(-N\pmod u\).  In centered form, this asks whether a bounded product of prime-factor residues of \(N\) can equal \(-1\pmod u\).

Let

\[
H=\mathrm{QR}_u\subset(\mathbb Z/u\mathbb Z)^\times.
\]

Because \(u\equiv3\pmod4\), \(-1\notin H\).

Suppose a collection of guaranteed quadratic-residue prime factors of \(x\), with their available centered exponent ranges, has centered product set equal to all of \(H\).

## Theorem

Under the subgroup-coverage hypothesis above,

\[
\boxed{
 u\text{ fails}
 \iff
 \text{every prime factor of }N=nx\text{ is a quadratic residue modulo }u.
}
\]

## Proof

If every prime factor of \(N\) lies in \(H\), then every divisor of \(N^2\) also lies in \(H\).  Since \(N\in H\) and \(-1\notin H\), the exact target

\[
-N
\]

lies in the nonresidue coset and cannot be a divisor residue.  Hence \(u\) fails.

Conversely, suppose some prime factor \(r\mid N\) is a quadratic nonresidue.  Then \(r^{-1}\) is also a nonresidue, so

\[
(-1)r^{-1}\in H.
\]

By hypothesis, the centered products of the guaranteed QR factors cover every element of \(H\).  Therefore one such centered product \(h\) satisfies

\[
h\equiv(-1)r^{-1}\pmod u.
\]

Using centered exponent \(+1\) for \(r\) and the exponents producing \(h\), we obtain

\[
rh\equiv-1\pmod u.
\]

The centered divisor criterion then gives a divisor \(d\mid N^2\) with

\[
d\equiv-N\pmod u,
\]

so the exact u-method succeeds.

## Examples

### u = 7

For the two residual classes \(n\equiv1,49\pmod{120}\), the number \((n+7)/4\) is even.  The centered powers of the guaranteed factor 2 cover all of \(H=\mathrm{QR}_7\), which has order 3.  The theorem gives the exact \(u=7\) characterization in `U7_EXACT_CHARACTERIZATION.md`.

### u = 11

On the slice \(n\equiv25\pmod{36}\), one has \(9\mid(n+11)/4\).  With primitive root 2 modulo 11, \(3=2^{-2}\), and centered exponents \([-2,2]\) of 3 cover the order-5 subgroup \(H=\mathrm{QR}_{11}\).  The theorem gives `U11_QR_CHARACTERIZATION.md`.

### u = 23

For the residual classes, \(6\mid(n+23)/4\).  If either \(4\mid(n+23)/4\) or \(9\mid(n+23)/4\), the centered powers of 2 and 3 cover the order-11 QR subgroup modulo 23.  The theorem then gives `U23_QR_CHARACTERIZATION.md`.

## Research consequence

The proof problem separates into two deterministic tasks for each candidate modulus \(u\):

1. **QR subgroup coverage:** find small forced factors of \((n+u)/4\) whose bounded centered powers cover \(\mathrm{QR}_u\);
2. **QNR existence:** prove that at least one prime factor of \(n(n+u)/4\) is a quadratic nonresidue modulo \(u\).

This decomposition is stronger and cleaner than assigning independent probabilities to prime factors.  The first task is finite group arithmetic; the second is an arithmetic statement about prime support of shifted integers.
