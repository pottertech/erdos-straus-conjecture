# Finite A-Layer Factorization Criteria

**Status:** exact equivalences

The two unit-partner branches can be reorganized without searching over the shift `u` directly. For a fixed residual integer `n == 1 (mod 4)`, write

\[
K=ad.
\]

Then the admissible shift is

\[
u=4ad-n.
\]

The all-shift identities turn the problem into factorization tests on two explicit sequences indexed by `a`.

## 1. Untwisted branch

The untwisted condition is

\[
d+1=ur.
\]

The exact identity is

\[
(4ad-n)(4ar-1)=n+4a.
\]

Define

\[
U=4ad-n,
\qquad
V=4ar-1.
\]

Then

\[
UV=n+4a,
\]

and

\[
U\equiv-n\pmod{4a},
\qquad
V\equiv-1\pmod{4a}.
\]

Conversely, suppose positive integers `U,V` satisfy

\[
UV=n+4a,
\]

\[
U\equiv-n\pmod{4a},
\qquad
V\equiv-1\pmod{4a}.
\]

Set

\[
d=\frac{U+n}{4a},
\qquad
r=\frac{V+1}{4a}.
\]

Then `d,r` are positive integers, `U=4ad-n`, and the product identity implies

\[
Ur=d+1.
\]

Thus `U` is precisely an admissible shift and `d | K=ad` is an untwisted unit-partner divisor.

Therefore:

\[
\boxed{
\text{untwisted success}
\iff
\exists a,U,V>0:
\begin{cases}
UV=n+4a,\\
U\equiv-n\pmod{4a},\\
V\equiv-1\pmod{4a}.
\end{cases}
}
\]

Moreover every such certificate satisfies

\[
\boxed{1\le a\le\lfloor(n+3)/8\rfloor.}
\]

So the criterion is finite for fixed `n`.

### Classical layer a = 1

For `a=1`,

\[
UV=n+4,
\qquad
U\equiv V\equiv3\pmod4
\]

because `n == 1 (mod 4)`.

This is exactly the classical `n+4` divisor criterion: a divisor `U == 3 (mod 4)` forces the complementary divisor `V` also to be `3 (mod 4)`.

Thus the classical criterion is simply the first layer of the full untwisted unit-partner cascade.

### Layer a = 2

For classical-core primes `n == 1 (mod 8)`, the next layer requires

\[
UV=n+8,
\qquad
U\equiv V\equiv7\pmod8.
\]

Higher `a` give analogous residue-constrained factorizations of

\[
n+4a.
\]

## 2. Twisted branch

The twisted condition is

\[
nd+1=ur.
\]

The exact identity is

\[
(4ad-n)(4ar-n)=n^2+4a.
\]

Define

\[
U=4ad-n,
\qquad
V=4ar-n.
\]

Then

\[
UV=n^2+4a,
\]

and now the two factors lie in the **same** residue class:

\[
U\equiv V\equiv-n\pmod{4a}.
\]

Conversely, if positive `U,V` satisfy

\[
UV=n^2+4a,
\qquad
U\equiv V\equiv-n\pmod{4a},
\]

then

\[
d=\frac{U+n}{4a},
\qquad
r=\frac{V+n}{4a}
\]

are positive integers and reconstruct a twisted unit-partner certificate.

Therefore:

\[
\boxed{
\text{twisted success}
\iff
\exists a,U,V>0:
\begin{cases}
UV=n^2+4a,\\
U\equiv V\equiv-n\pmod{4a}.
\end{cases}
}
\]

Every twisted certificate satisfies the previously derived finite bound

\[
\boxed{1\le a\le\lfloor n/2\rfloor.}
\]

## 3. Unified interpretation

The all-shift unit-partner problem is therefore equivalent to asking whether one of two finite families of integers admits a residue-constrained factorization:

- untwisted family: `n + 4a`;
- twisted family: `n^2 + 4a`.

The first family begins with the classical `n+4` criterion and extends it systematically through `n+8,n+12,...`.

This formulation is useful for a structural proof because it removes the moving shift from the search variables. The shift is reconstructed afterward as one factor

\[
u=U.
\]

A global theorem could therefore be attacked as a factorization theorem for these two short arithmetic families rather than as a divisor search over independently varying moduli.