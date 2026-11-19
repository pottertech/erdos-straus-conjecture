# Consecutive-Window Form of the Unit-Partner Cascade

**Status:** exact reparametrization plus unconditional fixed-window density theorem

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

## Unconditional fixed-window theorem

Let `F_J(N)` be the number of primes `n=4m+1 <= N` for which the **untwisted** unit-partner branch fails at every one of the first `J` positions

\[
m+1,\ldots,m+J,
\]

with attached shifts

\[
3,7,11,\ldots,4J-1.
\]

Applying the certified fixed finite multi-shift sieve in `UNIT_PARTNER_MULTI_SHIFT_SIEVE.md` to the `J` distinct shifts gives

\[
\boxed{
F_J(N)
\ll_J
\frac{N}{(\log N)^{1+J/2}}.
}
\]

This is unconditional for every fixed `J`.

Because failure of both unit-partner branches, or failure of the complete centered binary criterion, implies failure of the untwisted branch, the same upper bound holds for either of those smaller exceptional sets.

## The 75-position / u <= 299 theorem

The computational search uses

\[
u\le299=4\cdot75-1,
\]

so it is exactly the window length

\[
J=75.
\]

The theorem above therefore gives the explicit asymptotic bound

\[
\boxed{
F_{75}(N)
\ll
\frac{N}{(\log N)^{77/2}}.
}
\]

Equivalently,

\[
\boxed{
F_{75}(N)
\ll
\frac{N}{(\log N)^{38.5}}.
}
\]

Thus the primes for which none of the first 75 consecutive-window positions supplies even an **untwisted** unit-partner certificate form an exceptionally thin set. The set failing both branches, and the set failing the full binary criterion at all 75 shifts, are thinner still and satisfy the same rigorous upper bound.

This is a theorem-level asymptotic companion to the finite computation through `10^9`.

## The audited 10^9 observation

The exact computation gives a different and much stronger finite statement:

> For every corrected residual prime `n=4m+1 <= 10^9` except `2521`, at least one of the 75 consecutive integers `m+1,...,m+75` contains a divisor satisfying the untwisted or twisted position-dependent unit-partner congruence.

The unique unit-partner exception `2521` is permanent, not a depth-75 artifact, and is solved by the full binary pair `(2,29)` at shift `31`.

The asymptotic sieve theorem does **not** prove that `2521` is the only permanent exception globally. It proves that any further failures of the 75-position mechanism are logarithmically extremely sparse.

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

Hence `m` is always divisible by 6 in the classical core. Restricting to these six progressions changes only the implied constant in the fixed-window sieve estimate; it does not change the logarithmic exponent.

## What the consecutive-window theorem does and does not buy

The consecutive-window formulation upgrades the empirical `u <= 299` phenomenon to an explicit unconditional density theorem with exponent `38.5`.

It does **not** imply finiteness of the exceptional set. A fixed-length window, however large, is compatible with infinitely many exceptions of sufficiently low density.

To obtain a finiteness statement from sieve theory alone one would need substantially more than a fixed-dimensional upper-bound sieve: for example a uniform growing-window theorem with constants strong enough to make the exceptional counting function eventually less than one, or an independent structural argument closing the remaining thin set. Neither is currently established here.
