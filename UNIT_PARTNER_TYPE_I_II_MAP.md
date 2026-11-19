# Unit-Partner Branches Inside the Standard Type I / Type II Dichotomy

**Status:** exact algebraic map; terminology alignment

For prime `n`, the Erdős--Straus solutions split into the standard Type I / Type II dichotomy. The two unit-partner branches developed in this repository sit on opposite sides of that dichotomy.

## 1. Untwisted unit partner = Type II slice

At shift `c`, put

\[
K=\frac{n+c}{4}.
\]

The untwisted unit-partner condition is

\[
d\mid K,
\qquad
1+d\equiv0\pmod c.
\]

This is Lopez Type A and a special case of the untwisted fixed-shift branch. The resulting two remaining denominators are both multiples of `n`, so it is a Type II solution.

Writing

\[
K=a d
\]

and eliminating `c` gives the shift-divisor / complementary-cofactor form

\[
\boxed{
q\mid n+4a,
\qquad
q\equiv-1\pmod{4a}.
}
\]

This is a one-dimensional depth family in the cofactor `a`.

## 2. Twisted unit partner = Type I slice

The twisted unit-partner condition is

\[
d\mid K,
\qquad
nd+1=cr.
\]

Again write

\[
K=a d,
\qquad
c=4ad-n.
\]

Then

\[
nd+1=cr
\]

implies

\[
4ad^2+1
=d(n+c)+1
=nd+cd+1
=c(r+d).
\]

Hence

\[
\boxed{c\mid4d^2a+1}
\]

and, trivially from `n+c=4ad`,

\[
\boxed{4da\mid n+c.}
\]

The standard closed Type-I criterion is

\[
\exists u,D,f>0:
\qquad
f\mid4u^2D+1,
\qquad
4uD\mid n+f.
\]

The twisted unit-partner branch is exactly its slice

\[
\boxed{
u=d,
\qquad
D=a,
\qquad
f=c.
}
\]

Only one denominator produced by this branch is forced to contain `n`, so it is Type I.

## 3. Why the analytic behavior differs

The complementary-cofactor untwisted subsystem can be restricted to prime witnesses

\[
q\mid n+4a,\qquad q\equiv-1\pmod{4a},
\]

where fixing `a` gives one explicit forbidden residue class for `n` modulo `q`. The number of such classes at depth `J` is the one-parameter divisor count

\[
\rho_J(q)=\#\{a\le J:4a\mid q+1\}.
\]

This is why the one-parameter large-sieve analysis transfers cleanly.

By contrast the Type-I form still contains the effective pair `(d,a)` through

\[
c\mid4d^2a+1.
\]

Bounding only the complementary cofactor `a` does not freeze `d`. Consequently a one-dimensional growing-depth theorem for the twisted slice does not follow automatically from the untwisted argument.

This agrees with the computational/algorithmic asymmetry emphasized in Dahan (2026): the complete Type-II pass is quasi-linear on intervals in his factorization-free procedure, while the Type-I pass carries the quadratic divisor-extraction cost.

## 4. Example: 66529

`66529` is permanently exceptional to the untwisted / Type-A family, but succeeds in the twisted branch with

\[
c=19,
\qquad
K=16637,
\qquad
d=131,
\qquad
a=127.
\]

The Type-I identification is therefore

\[
u=131,
\qquad
D=127,
\qquad
f=19.
\]

Indeed

\[
19\mid4\cdot131^2\cdot127+1
\]

and

\[
4\cdot131\cdot127=66529+19.
\]

## 5. Endgame implication

A universal proof need not force one single family to work everywhere. A logically natural hierarchy is:

1. Type-II / untwisted cofactor witnesses cover an overwhelming set and admit strong sieve control;
2. Type-I / twisted unit-partner witnesses rescue some permanent Type-II-slice exceptions such as `66529`;
3. the complete fixed-shift binary criterion allows non-unit pairs and closes `2521`.

The remaining global task is to prove that this hierarchy leaves no prime uncovered, without importing an unproved global covering hypothesis.