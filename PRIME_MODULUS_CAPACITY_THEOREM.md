# Prime-Modulus Capacity-Vector Form of the Centered Criterion

**Date:** 2026-08-28  
**Status:** Exact reformulation for prime `u` with `gcd(nx,u)=1`

## Setup

Let

\[
x=\frac{n+u}{4},\qquad M=nx,
\]

with `u` an odd prime and `gcd(M,u)=1`.  The exact centered criterion is

\[
\prod_{p^a\parallel M}p^{c_p}\equiv -1\pmod u,
\qquad -a\le c_p\le a.
\]

Choose a primitive root `g` modulo `u`, and write

\[
u-1=2m.
\]

For `1 <= j < m`, define the **capacity**

\[
A_j=\sum_{\substack{p^a\parallel M\\ \log_g p\equiv \pm j\ (\bmod\ 2m)}}a,
\]

and define

\[
A_m=\sum_{\substack{p^a\parallel M\\ p\equiv -1\ (\bmod\ u)}}a.
\]

The class `j=0` (prime factors congruent to `1 mod u`) is irrelevant for hitting `-1`.

## Theorem (exact capacity-vector criterion)

The `u`-method succeeds if and only if there exist integers

\[
a_1,\ldots,a_m
\]

such that

\[
|a_j|\le A_j
\]

for every `j`, and

\[
\boxed{\sum_{j=1}^{m}j a_j\equiv m\pmod{2m}.}
\]

### Proof

Write each prime residue as `p ≡ g^{s_p} (mod u)`.  The centered criterion becomes

\[
\sum_p s_p c_p\equiv m\pmod{2m},
\]

because `-1 = g^m`.

Pair each log class `j` with its inverse class `-j`.  A centered exponent on a prime in the `-j` class contributes the same as changing the sign of its coefficient in the `j` class.  For all prime powers in the pair, the possible aggregate coefficients are every integer in

\[
[-A_j,A_j],
\]

because a sum of integer intervals `[-e_i,e_i]` is the full interval whose radius is the sum of the radii.  The order-two class `m` is self-inverse and has the same interval property.  Thus the original prime-by-prime signed box is equivalent exactly to the displayed bounded congruence. ∎

## Corollary: exact mod-7 criterion

For `u=7`, use primitive root `g=3`.  The inverse-paired residue classes are

- log `±1`: residues `{3,5}`;
- log `±2`: residues `{2,4}`;
- log `3`: residue `{6}`.

Define, counting prime factors with multiplicity,

\[
T_1=\sum_{p^a\parallel M,\ p\equiv3,5\ (7)}a,
\]

\[
T_2=\sum_{p^a\parallel M,\ p\equiv2,4\ (7)}a,
\]

\[
T_3=\sum_{p^a\parallel M,\ p\equiv6\ (7)}a.
\]

Then `u=7` succeeds if and only if

\[
\exists |a|\le T_1,\ |b|\le T_2,\ |c|\le T_3:
\quad a+2b+3c\equiv3\pmod6.
\]

This has the closed form

\[
\boxed{
T_3\ge1\quad\text{or}\quad
T_1\ge3\quad\text{or}\quad
(T_1\ge1\text{ and }T_2\ge1).
}
\]

Indeed, `T_3>=1` gives `c=1`; `T_1>=3` gives `a=3`; and `T_1,T_2>=1` gives `a=b=1`.  Conversely, if `T_3=0`, `T_1=0` leaves only even residues, while `T_2=0` and `T_1<=2` cannot reach `3 mod 6`.

Thus `u=7` failure is characterized exactly by

\[
T_3=0
\]

and either

\[
T_1=0,
\]

or

\[
T_2=0\text{ and }T_1\le2.
\]

## Why this matters

For each fixed prime `u`, arbitrary factorization data now compress to a finite-dimensional integer vector.  This supports a deterministic finite-state cascade:

1. factor `M=n(n+u)/4`;
2. compute the capacity vector;
3. solve a short bounded linear congruence;
4. record the minimal support and coefficient size of a witness.

This is exact and avoids probabilistic divisor-distribution assumptions.
