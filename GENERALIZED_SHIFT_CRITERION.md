# Generalized Shift Criterion for the Dominant Short Relation

**Status:** exact algebraic equivalence; no probabilistic assumption

Let

\[
x=\frac{n+u}{4},\qquad u\equiv3\pmod4,
\]

and suppose `p` is a divisor of `x`.  Write

\[
x=a p.
\]

The dominant centered short relation is

\[
p\equiv-1\pmod u.
\]

Thus `p = u r - 1` for some positive integer `r`.  Substituting into
`n+u=4x` gives

\[
n+u=4a(ur-1),
\]

hence

\[
\boxed{n+4a=u(4ar-1).}
\]

Conversely, if positive integers `a,u,r` satisfy

\[
u\equiv3\pmod4,\qquad n+4a=u(4ar-1),
\]

then setting

\[
p=ur-1,
\qquad
x=a p=a(ur-1)
\]

gives

\[
4x=n+u,
\qquad
p\mid x,
\qquad
p\equiv-1\pmod u.
\]

Therefore the following are equivalent:

1. the `p = -1 mod u` centered route occurs with a divisor `p|x`;
2. for `a=x/p`, the shifted integer `n+4a` factors as
   \[
   n+4a=u v,
   \qquad
   v\equiv-1\pmod{4a},
   \]
   with `u ≡ 3 (mod 4)`.

Here `v=4ar-1`.

## Explicit Erdős--Straus decomposition

Under

\[
n+4a=u(4ar-1),
\]

set

\[
x=a(ur-1),
\qquad
y=n x r,
\qquad z=n a r.
\]

Then all three denominators are positive integers and

\[
\boxed{\frac4n=\frac1x+\frac1y+\frac1z.}
\]

Equivalently, cross multiplication gives

\[
4xyz=n(xy+xz+yz).
\]

## Interpretation

This removes the apparent circularity of the dominant short-relation search.  Instead of choosing `u`, forming `x=(n+u)/4`, factoring `x`, and asking whether a factor is `-1 mod u`, one may choose a positive shift parameter `a` and factor the ordinary shifted number

\[
\boxed{n+4a.}
\]

A successful factorization is

\[
n+4a=u v,
\qquad u\equiv3\pmod4,
\qquad v\equiv-1\pmod{4a}.
\]

The familiar `n+4` divisor criterion is the special case `a=1`.  Thus the dominant computational route through `10^8` is naturally viewed as a hierarchy of generalized shift-divisor criteria `n+4a`.

No claim of novelty is made here; the point is to record the exact equivalence in the corrected centered framework and expose a more useful deterministic proof target.
