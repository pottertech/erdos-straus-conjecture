# One-Divisor Criterion for the Binary-Sum Family

**Status:** exact algebraic criterion; derived from `BINARY_SUM_POLYNOMIAL_FAMILY.md` and the complete centered binary endpoint. No novelty claim.

## Theorem

Let `n,q,r` be positive integers and set

\[
N=4qr^2n+1,
\qquad
m=4qr.
\]

Suppose there is a positive divisor `R | N` such that

\[
\boxed{R\equiv-1\pmod m}.
\]

Let

\[
S=N/R.
\]

Then automatically

\[
\boxed{S\equiv-1\pmod m}.
\]

Hence there are positive integers

\[
A=\frac{R+1}{4qr},
\qquad
B=\frac{S+1}{4qr}.
\]

Moreover

\[
A+B=r(4ABq-n),
\]

so

\[
u:=4ABq-n=\frac{A+B}{r}
\]

is a positive integer. Therefore

\[
K=ABq=\frac{n+u}{4}
\]

and the explicit denominators

\[
\boxed{x=ABq},
\qquad
\boxed{y=Anqr},
\qquad
\boxed{z=Bnqr}
\]

satisfy

\[
\boxed{
\frac4n=\frac1x+\frac1y+\frac1z.
}
\]

## Proof of the complementary congruence

Since

\[
N=RS\equiv1\pmod m
\]

and

\[
R\equiv-1\pmod m,
\]

we have

\[
-S\equiv1\pmod m,
\]

therefore

\[
S\equiv-1\pmod m.
\]

No modular inverse machinery beyond the fact that `-1` is its own inverse is needed.

## The r = 1 specialization

For `r=1`, it is enough to find `q>0` and a divisor

\[
R\mid 4qn+1
\]

such that

\[
\boxed{R\equiv-1\pmod{4q}}.
\]

The complementary divisor automatically has the same residue.

This converts the non-unit binary rescue problem into a one-divisor search on a linear polynomial in `n`.

## Example: n = 2521

Take

\[
q=11,
\qquad
r=1.
\]

Then

\[
N=4\cdot11\cdot2521+1=110925.
\]

Choose

\[
R=87.
\]

We have

\[
87\mid110925
\]

and

\[
87\equiv-1\pmod{44}.
\]

The complementary divisor is

\[
S=110925/87=1275,
\]

and indeed

\[
1275\equiv-1\pmod{44}.
\]

Thus

\[
A=(87+1)/44=2,
\qquad
B=(1275+1)/44=29,
\]

and

\[
u=A+B=31.
\]

This recovers

\[
x=638,
\qquad
y=55462,
\qquad z=804199.
\]

## Relation to the unit-partner slice

The ordinary unit-partner/cofactor family searches divisors of shifted quantities such as `(n+u)/4` or their twisted analogues. The criterion here searches instead for a `-1` divisor of

\[
4qr^2n+1.
\]

Thus it supplies a natural second sieve after the unit-partner family has been exhausted.

The finite `n=2521` example demonstrates that this second sieve is genuinely stronger: `2521` is a permanent failure of the entire unit-partner slice but succeeds immediately here with `(q,r,R)=(11,1,87)`.

## Revised global target

A sufficient global theorem would be:

> Every prime in the corrected residual Erdős--Straus core either admits a unit-partner certificate, or there exist positive integers `q,r` for which `4 q r^2 n + 1` has a divisor congruent to `-1 mod 4 q r`.

This is still an open number-theoretic statement. The finite computation does not prove it, but it is substantially simpler to state and audit than a generic bounded centered-product condition.
