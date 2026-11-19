# Twisted Shift-Divisor Criterion

**Status:** exact equivalence

The twisted unit-partner branch admits a one-divisor reformulation parallel to the untwisted shift-divisor family.

Let `n` be an odd prime in the residual class and write

\[
K=ad,
\qquad
c=4ad-n>0.
\]

The twisted unit-partner condition is

\[
nd+1=cr.
\]

The exact factorization identity is

\[
(4ad-n)(4ar-n)=n^2+4a.
\]

Every twisted certificate satisfies

\[
1\le a\le\lfloor n/2\rfloor.
\]

## One-divisor form

Put

\[
q=4ar-n.
\]

Then

\[
q\mid n^2+4a
\]

and

\[
q\equiv-n\pmod{4a}.
\]

Conversely, suppose

\[
1\le a\le n/2
\]

and there is a positive divisor

\[
q\mid n^2+4a
\]

such that

\[
\boxed{q\equiv-n\pmod{4a}.}
\]

Let

\[
c=\frac{n^2+4a}{q}.
\]

Because `a < n` for prime `n`, we have `gcd(n,4a)=1`. Hence `q == -n (mod 4a)` is invertible modulo `4a`, and

\[
cq\equiv n^2\pmod{4a}
\]

gives

\[
c\equiv n^2(-n)^{-1}\equiv-n\pmod{4a}.
\]

Therefore

\[
d=\frac{c+n}{4a},
\qquad
r=\frac{q+n}{4a}
\]

are positive integers. Substituting into

\[
cq=n^2+4a
\]

and expanding yields

\[
nd+1=cr.
\]

Thus `d | K=ad` is a twisted unit-partner certificate at shift `c`.

We obtain the exact equivalence

\[
\boxed{
\text{twisted unit-partner success}
\iff
\exists\,1\le a\le\lfloor n/2\rfloor,
\ \exists q\mid n^2+4a:
\ q\equiv-n\pmod{4a}.
}
\]

## Parallel with the untwisted family

The two all-shift one-divisor families are now:

### Untwisted / Lopez Type A

\[
\boxed{
q\mid n+4a,
\qquad
q\equiv-1\pmod{4a}.
}
\]

### Twisted unit-partner

\[
\boxed{
q\mid n^2+4a,
\qquad
q\equiv-n\pmod{4a}.
}
\]

Both are finite decision problems for fixed `n` because their cofactor parameters satisfy explicit linear bounds in `n`.

## Example: n = 66529

The integer `66529` is permanently exceptional to the untwisted/Type-A family, but the twisted criterion succeeds with

\[
a=127,
\qquad
q=19.
\]

Indeed

\[
19\mid66529^2+4\cdot127
\]

and

\[
19\equiv-66529\pmod{508}.
\]

The complementary factor reconstructs the same twisted unit-partner certificate recorded elsewhere at shift `c=19` with `K=16637`, `d=131`.

## Structural interpretation

A permanent exception to the entire unit-partner slice must simultaneously avoid, for every admissible cofactor layer,

1. divisors of `n+4a` in the residue `-1 mod 4a`; and
2. divisors of `n^2+4a` in the residue `-n mod 4a`.

The integer `2521` is proved elsewhere to satisfy both avoidance conditions for every allowed layer. This two-family formulation is a cleaner global rigidity target than searching over moving shifts directly.