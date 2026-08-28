# Deterministic QNR Cascade for the Corrected u-Method

**Date:** 2026-08-28

For the two residual prime hard-case classes

\[
n\equiv1,49\pmod{120},
\]

we have \(n\equiv1\pmod{24}\).  The exact u-method criterion asks for a divisor
\(d\mid (nx)^2\) with \(d\equiv-nx\pmod u\), where \(x=(n+u)/4\).

## u = 7

Since \(n\equiv1\pmod8\),

\[
x_7=(n+7)/4
\]

is even.  Using only guaranteed divisors of the form

\[
n^a x_7^b2^c,\qquad a,b,c\in\{0,1,2\},
\]

the exact target fails precisely for the quadratic residues modulo 7:

\[
\{1,2,4\}.
\]

Hence

\[
\left(\frac n7\right)=-1\Longrightarrow u=7\text{ succeeds}.
\]

## u = 11

Since \(n\equiv1\pmod{12}\),

\[
x_{11}=(n+11)/4
\]

is divisible by 3.  Using only guaranteed divisors

\[
n^a x_{11}^b3^c,
\]

the exact failure residues are exactly

\[
\mathrm{QR}_{11}=\{1,3,4,5,9\}.
\]

Therefore

\[
\left(\frac n{11}\right)=-1\Longrightarrow u=11\text{ succeeds}.
\]

## u = 23

Because the residual classes satisfy \(n\equiv1\pmod{24}\),

\[
x_{23}=(n+23)/4
\]

is divisible by both 2 and 3.  Using only guaranteed divisors

\[
n^a x_{23}^b2^c3^d,
\qquad a,b,c,d\in\{0,1,2\},
\]

the exact failure set is exactly the quadratic-residue subgroup modulo 23:

\[
\mathrm{QR}_{23}=\{1,2,3,4,6,8,9,12,13,16,18\}.
\]

Thus

\[
\left(\frac n{23}\right)=-1\Longrightarrow u=23\text{ succeeds}.
\]

## Deterministic residual condition

Any prime in the two residual modulo-120 classes that survives all three exact routes must satisfy

\[
\boxed{
\left(\frac n7\right)=
\left(\frac n{11}\right)=
\left(\frac n{23}\right)=1.
}
\]

This is a deterministic theorem obtained by finite arithmetic in the three multiplicative groups; it does not assume random or independent Legendre symbols.

Modulo

\[
\operatorname{lcm}(120,7,11,23)=212520,
\]

there are 2640 admissible prime residue classes above \(1\) and \(49\pmod{120}\), and exactly 330 satisfy all three QR conditions.  Thus these three exact routes reduce the residual congruence problem by a factor of eight before any factorization-specific information is used.

The next target is to find a fourth exact route, or a forced-factor refinement, that breaks the simultaneous subgroup

\[
\mathrm{QR}_7\cap\mathrm{QR}_{11}\cap\mathrm{QR}_{23}.
\]
