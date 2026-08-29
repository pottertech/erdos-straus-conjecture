# Consecutive-Window Form of the Unit-Partner Cascade

**Status:** exact reparametrization

Write any residual integer `n == 1 (mod 4)` as

\[
n=4m+1.
\]

Every admissible shift has the form

\[
u=4j-1,
\qquad j\ge1.
\]

Then

\[
K_u=\frac{n+u}{4}
=\frac{4m+1+4j-1}{4}
=\boxed{m+j}.
\]

Therefore a bounded shift search

\[
3\le u\le4J-1
\]

is exactly a search over the consecutive block

\[
\boxed{m+1,m+2,\ldots,m+J}.
\]

The modulus attached to the `j`-th term is

\[
\boxed{u_j=4j-1}.
\]

## Unit-partner conditions at position j

At position `j`, put

\[
K_j=m+j,
\qquad u_j=4j-1.
\]

The untwisted branch succeeds iff

\[
\exists d\mid(m+j):\qquad
\boxed{d\equiv-1\pmod{4j-1}}.
\]

The twisted branch succeeds iff

\[
\exists d\mid(m+j):\qquad
\boxed{(4m+1)d\equiv-1\pmod{4j-1}}.
\]

Since

\[
4m+1\equiv4(m+j)\pmod{4j-1},
\]

the twisted condition can equivalently be written

\[
\boxed{4(m+j)d\equiv-1\pmod{4j-1}}.
\]

If `m+j = a d`, this becomes the parametric condition

\[
\boxed{4ad^2\equiv-1\pmod{4j-1}}.
\]

## The verified 299-shift window

The computation with `u <= 299` is exactly `J <= 75`, because

\[
299=4\cdot75-1.
\]

Thus the audited `10^9` observation can be restated as:

> For every corrected residual prime `n=4m+1 <= 10^9` except `2521`, at least one of the 75 consecutive integers `m+1,...,m+75` contains a divisor satisfying the untwisted or twisted position-dependent congruence above.

This form may be more useful for a universal argument because it replaces a family of shifted factorizations by one fixed-length consecutive window.

## Classical-core coordinates

For the six classical prime residue classes

\[
n\equiv1,121,169,289,361,529\pmod{840},
\]

we have

\[
m=\frac{n-1}{4}
\equiv0,30,42,72,90,132\pmod{210}.
\]

Hence `m` is always divisible by 6 in the classical core. The unresolved problem can therefore be studied as a divisor-placement problem in a length-75 window beginning at an integer in these six classes modulo 210.
