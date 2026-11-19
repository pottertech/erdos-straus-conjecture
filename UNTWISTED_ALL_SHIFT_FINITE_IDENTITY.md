# All-Shift Finite Identity for the Untwisted Unit-Partner Branch

**Status:** exact algebraic theorem

Let

\[
K=\frac{n+u}{4}=ad,
\qquad u\equiv3\pmod4,
\]

and suppose the untwisted unit-partner branch succeeds:

\[
d+1=ur
\]

for positive integers `a,d,r`.

Since

\[
u=4ad-n,
\]

we have

\[
(4ad-n)(4ar-1)
=u(4ar-1).
\]

Using `ur=d+1`,

\[
u(4ar-1)
=4a(ur)-u
=4a(d+1)-(4ad-n)
=n+4a.
\]

Therefore every untwisted unit-partner certificate satisfies the exact factorization

\[
\boxed{(4ad-n)(4ar-1)=n+4a.}
\]

Conversely, if positive integers `a,d,r` satisfy

\[
(4ad-n)(4ar-1)=n+4a
\]

with

\[
u:=4ad-n>0,
\qquad u\equiv3\pmod4,
\]

then expanding and cancelling gives

\[
u r=d+1,
\]

so `d | K=ad` and `d == -1 (mod u)`. Hence the factorization identity is equivalent to the untwisted unit-partner branch.

## Finite bound

Because `u=4ad-n` is a positive integer congruent to `3 mod 4`,

\[
u\ge3.
\]

The second factor satisfies

\[
4ar-1\ge4a-1.
\]

Hence

\[
n+4a
=(4ad-n)(4ar-1)
\ge3(4a-1).
\]

Therefore

\[
n+3\ge8a,
\]

so every untwisted certificate satisfies

\[
\boxed{a\le\left\lfloor\frac{n+3}{8}\right\rfloor.}
\]

Thus for any fixed `n`, permanent failure of the untwisted unit-partner branch is decidable by a finite exact search.

A convenient search form comes from rearranging

\[
(4ad-n)r=d+1:
\]

\[
\boxed{d(4ar-1)=nr+1.}
\]

So for each

\[
1\le a\le\left\lfloor\frac{n+3}{8}\right\rfloor,
\]

one may enumerate the finitely many possible `r` for which `u>=3`, test

\[
4ar-1\mid nr+1,
\]

and reconstruct

\[
d=\frac{nr+1}{4ar-1},
\qquad
u=4ad-n.
\]

This is the untwisted analogue of the twisted identity

\[
(4ad-n)(4ar-n)=n^2+4a,
\]

which gives the finite bound `a <= n/2` for the twisted branch.