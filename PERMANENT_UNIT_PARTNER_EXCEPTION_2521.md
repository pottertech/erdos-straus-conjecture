# 2521 Is a Permanent Exception to the Unit-Partner Slice

**Status:** exact finite theorem for the unit-partner criterion; `2521` is still an Erdős--Straus number via a non-unit binary pair

The audited searches through `10^9` found exactly one corrected residual prime with no unit-partner certificate for `u <= 299`:

\[
\boxed{n=2521}.
\]

This note shows that increasing the unit-partner shift bound can never fix this particular integer: `2521` has **no untwisted or twisted unit-partner certificate at any admissible shift**.

It is nevertheless solved by the full binary criterion at `u=31`, with

\[
K=(2521+31)/4=638=2\cdot11\cdot29,
\]

and the non-unit pair

\[
2+29=31.
\]

## 1. Untwisted branch is a finite check

Write

\[
2521=4\cdot630+1.
\]

Every admissible shift is

\[
u=4j-1,
\]

and

\[
K_u=\frac{2521+u}{4}=630+j.
\]

The untwisted unit-partner branch requires a divisor

\[
d\mid K_u,
\qquad d\equiv-1\pmod u.
\]

If `u > K_u+1`, this is impossible because every positive divisor satisfies `d <= K_u`, while the least positive integer congruent to `-1 mod u` is `u-1`.

Now

\[
4j-1>631+j
\]

as soon as `j >= 211`. Therefore only

\[
1\le j\le210
\]

can possibly work.

Exact enumeration of the divisors of `630+j` for those 210 values finds no divisor congruent to `-1 mod (4j-1)`.

Hence `2521` has no untwisted unit-partner certificate for any shift.

## 2. Twisted branch has a universal cofactor bound

Suppose a twisted unit-partner certificate exists for a general positive `n`.

Write

\[
K=ad,
\qquad
u=4ad-n>0,
\]

and

\[
nd+1=ur
\]

with positive integers `a,d,r`.

Then

\[
nd+1=r(4ad-n),
\]

so

\[
4adr=n(d+r)+1.
\]

A direct expansion gives the factorization identity

\[
\boxed{
(4ad-n)(4ar-n)=n^2+4a.
}
\]

Both factors on the left are positive. If `a > n/4`, then `d,r >= 1` imply

\[
4ad-n\ge4a-n,
\qquad
4ar-n\ge4a-n.
\]

Therefore

\[
(4a-n)^2\le n^2+4a.
\]

Expanding and cancelling `n^2` gives

\[
16a^2-(8n+4)a\le0,
\]

hence

\[
a\le\frac{2n+1}{4}<\frac n2+1.
\]

Together with the trivial case `a <= n/4`, every twisted unit-partner solution satisfies

\[
\boxed{a\le\lfloor n/2\rfloor.}
\]

## 3. Exact finite check for n=2521

For `n=2521`, it is therefore enough to check

\[
1\le a\le1260.
\]

For a fixed `a`, any twisted solution must satisfy

\[
\nu=4ad-n
\]

and the factorization identity above, so in particular

\[
\boxed{u\mid n^2+4a}
\]

and

\[
\boxed{u\equiv-n\pmod{4a}}.
\]

Thus the check is finite and exact:

1. for each `a=1,...,1260`, factor `2521^2+4a`;
2. enumerate its positive divisors `u` with `u == 3 (mod 4)`;
3. require `u == -2521 (mod 4a)`;
4. reconstruct `d=(2521+u)/(4a)`;
5. test `u | 2521*d+1`.

No value succeeds.

Hence `2521` has no twisted unit-partner certificate at any shift.

## Conclusion

\[
\boxed{
2521\text{ is a permanent exception to the unit-partner criterion.}
}
\]

This is **not** an exception to the Erdős--Straus conjecture. The full binary fixed-shift criterion solves it at `u=31` with pair `(2,29)`.

The computational observation through `10^9` can therefore be sharpened conceptually:

> every corrected residual prime through `10^9` other than the one permanent unit-partner exception `2521` is solved by the unit-partner slice; `2521` is solved by a two-nonunit divisor pair.
