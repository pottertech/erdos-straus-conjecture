# Exact Parametric Form of the Unit-Partner Branches

**Status:** exact algebraic reduction; not a global existence theorem

Let

\[
K=\frac{n+u}{4},\qquad u\equiv3\pmod4,
\]

and suppose `K = a d` with positive integers `a,d`.

The two unit-partner branches admit the following exact forward parametrizations.

## Untwisted branch

The condition

\[
d\mid K,\qquad d\equiv-1\pmod u
\]

is equivalent to

\[
d+1=ur
\]

for some positive integer `r`. Hence

\[
\boxed{n=4a(ur-1)-u=4aur-(4a+u).}
\]

For fixed `(u,a)`, this is the arithmetic progression

\[
\boxed{n\equiv-(4a+u)\pmod{4au}.}
\]

The explicit Erdős--Straus denominators are

\[
X=K=ad,
\]
\[
Y=nK r=nadr,
\]
\[
Z=na r.
\]

Direct cross multiplication gives

\[
4XYZ=n(XY+XZ+YZ).
\]

The classical `n+4` divisor criterion is the special case `a=1`.

## Twisted branch

The condition

\[
d\mid K,\qquad nd\equiv-1\pmod u
\]

is equivalent to

\[
nd+1=ur.
\]

Using `n=4ad-u`, this becomes

\[
(4ad-u)d+1=ur,
\]

or

\[
\boxed{u\mid 4ad^2+1.}
\]

Thus the twisted unit-partner branch has the exact forward form

\[
\boxed{n=4ad-u,\qquad u\mid 4ad^2+1.}
\]

The explicit denominators are

\[
X=K=ad,
\]
\[
Y=nK r=nadr,
\]
\[
Z=a r,
\]

where `r=(nd+1)/u`.

Again, direct cross multiplication verifies the Erdős--Straus identity exactly.

## Why this matters

Both branches can therefore be generated without factoring a given `K`:

- untwisted: choose `(u,a,r)` and set `d=ur-1`, `n=4ad-u`;
- twisted: choose `(u,a,d)` satisfying `4ad^2 == -1 (mod u)` and set `n=4ad-u`.

This is the natural parameter space for a factorization-free sieve over varying small shifts `u`.

The unresolved global step is an existence statement: prove that every remaining prime lies in at least one such family (apart from finitely many explicitly handled non-unit binary pairs, if necessary).