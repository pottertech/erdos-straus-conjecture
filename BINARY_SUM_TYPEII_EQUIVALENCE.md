# Exact Type-II Equivalence of the Binary-Sum Criterion

**Status:** exact reparameterization of the classical Type-II criterion; no novelty claim.

This note identifies the repository's binary-sum polynomial/factorization criterion with the standard complete Type-II characterization used by Pomerance--Weingartner and restated in Dahan (2026).

## 1. Standard Type-II criterion

A positive integer `n` has a Type-II Erdős--Straus solution if and only if there exist positive integers `A,B,e` such that

\[
\boxed{e\mid A+B}
\]

and

\[
\boxed{4AB\mid n+e}.
\]

This criterion is classical.  We use `A,B,e` here to avoid overloading the repository's shift variable `u`.

## 2. From Type II to the binary-sum family

Given a Type-II triple `(A,B,e)`, define

\[
r=\frac{A+B}{e},
\qquad
q=\frac{n+e}{4AB}.
\]

The two Type-II divisibility conditions guarantee that `q,r` are positive integers.

Then

\[
A+B=er
\]

and

\[
n+e=4ABq,
\]

so

\[
\boxed{n=4ABq-e}
\]

with

\[
\boxed{e=\frac{A+B}{r}}.
\]

Thus the parameters satisfy exactly the general binary-sum family recorded in `BINARY_SUM_POLYNOMIAL_FAMILY.md`.

The corresponding denominators are

\[
\boxed{x=ABq},
\qquad
\boxed{y=Anqr},
\qquad
\boxed{z=Bnqr}.
\]

Both `y` and `z` are divisible by `n`, which is the standard Type-II shape.

## 3. Converse

Conversely, suppose positive `A,B,q,r,e,n` satisfy

\[
A+B=er,
\qquad
n=4ABq-e.
\]

Then immediately

\[
e\mid A+B
\]

and

\[
n+e=4ABq,
\]

so

\[
4AB\mid n+e.
\]

Therefore every member of the binary-sum family is Type II.

Hence:

\[
\boxed{
\text{binary-sum polynomial family}
\iff
\text{complete Type-II criterion}.
}
\]

This is an exact equivalence, not merely a sufficient subfamily.

## 4. Equivalent one-divisor factorization form

The identity

\[
(4Aqr-1)(4Bqr-1)=4qr^2n+1
\]

shows that Type II is equivalently encoded by a divisor of a linear polynomial in `n`.

Let

\[
N=4qr^2n+1,
\qquad
m=4qr.
\]

Then Type II implies that

\[
R=4Aqr-1
\]

is a divisor of `N` satisfying

\[
R\equiv-1\pmod m.
\]

Conversely, if there are positive integers `q,r` and a divisor

\[
R\mid 4qr^2n+1
\]

with

\[
R\equiv-1\pmod{4qr},
\]

then the complementary divisor `S=N/R` also satisfies

\[
S\equiv-1\pmod{4qr}.
\]

Writing

\[
A=\frac{R+1}{4qr},
\qquad
B=\frac{S+1}{4qr}
\]

recovers a Type-II triple.

Therefore the following are equivalent:

1. `n` has a Type-II Erdős--Straus solution;
2. there exist positive `A,B,e` with `e | A+B` and `4AB | n+e`;
3. there exist positive `q,r` such that `4 q r^2 n + 1` has a divisor congruent to `-1 mod 4 q r`.

This factorization language is useful computationally, but the underlying solvability criterion is classical Type II.

## 5. n = 2521

For

\[
n=2521,
\]

the complete Type-II solution is obtained from

\[
A=2,
\quad B=29,
\quad e=31,
\quad r=1,
\quad q=11.
\]

Indeed,

\[
e=A+B=31,
\]

and

\[
n+e=2552=4\cdot2\cdot29\cdot11.
\]

The one-divisor form is

\[
4qn+1=110925,
\]

with

\[
87\mid110925,
\qquad
87\equiv-1\pmod{44}.
\]

This is a genuine Type-II rescue beyond the unit-partner slice.

## 6. n = 66529 is the essential warning

The repository's exact all-shift untwisted classification proves that

\[
\boxed{n=66529}
\]

has no Type-II solution at all.

It is nevertheless solved by the twisted/Type-I branch at

\[
u=19,
\qquad K=16637,
\qquad d=131.
\]

Therefore the Type-II one-divisor formulation cannot be universal by itself.

Equivalently, for `n=66529` there do **not** exist positive integers `q,r` and a divisor

\[
R\mid4qr^2n+1
\]

with

\[
R\equiv-1\pmod{4qr}.
\]

This should be retained as a regression test for any attempted universal Type-II theorem.

## 7. Correct global hierarchy

The current finite evidence supports the following hierarchy rather than Type-II universality:

1. **Type-II unit-partner / cofactor slice** handles the overwhelming majority;
2. **Type-I twisted unit-partner slice** rescues cases such as `66529`;
3. **full non-unit Type II** rescues the unique permanent unit-partner exception `2521` in the audited range through `10^9`.

A global proof would still need to rule out integers requiring a genuinely non-unit Type-I solution outside these three slices.

## 8. Priority / literature note

The Type-II characterization itself is classical and appears in work of Pomerance--Weingartner and in Dahan's 2026 reformulation.  The factorization equation above is an algebraic reparameterization of that criterion.  No novelty or priority claim is made for the existence theorem.
