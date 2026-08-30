# Squarefree-Semiprime Mixed Rescue Core

**Status:** exact reduction plus finite census.  The underlying square-completed shadow geometry and the fact that `u^2,v^2` are the only mixed square divisors are aligned with the 2026 FCF/CENTL program; no novelty claim is made for that prior structure.

Let

\[
A=uv
\]

with distinct primes `u<v`, and put

\[
m_A=4uv-1.
\]

For the square-completed Type-II layer, the divisors of `A^2` are

\[
1,u,v,u^2,uv,v^2,u^2v,uv^2,u^2v^2.
\]

The López boundary orthants contain all except

\[
\boxed{u^2,\ v^2}.
\]

Thus the genuinely square-only part of a squarefree-semiprime layer is exactly the pair

\[
\boxed{-4u^2,\ -4v^2\pmod{m_A}},
\]

or equivalently

\[
\boxed{-u/v,\ -v/u\pmod{m_A}}.
\]

## Exact ancestry test

Let `B<A` satisfy

\[
m_B=4B-1\mid m_A.
\]

Then

\[
A\equiv B\pmod{m_B}.
\]

Define

\[
Q_B=\{E\pmod{m_B}:E\mid B^2\}.
\]

### Theorem

The mixed direction `u^2` is inherited from depth `B` iff

\[
\boxed{u^2\pmod{m_B}\in Q_B.}
\]

When this happens, `v^2` is inherited automatically.

### Proof of pairing

If `u^2 == E (mod m_B)` for some `E|B^2`, then

\[
v^2=\frac{A^2}{u^2}
\equiv
\frac{B^2}{E}
\pmod{m_B}.
\]

Because `B^2/E` is again a divisor of `B^2`, the second mixed direction is also in `Q_B`.  Symmetry gives the converse.

Therefore the squarefree-semiprime mixed rescue is an indivisible two-direction object along every divisor-modulus ancestry edge: **both directions are shadowed or neither is**.

The script `semiprime_mixed_rescue_analyzer.py` implements this test without searching primes `p`.

## Finite census through A = 100000

An exact exploratory run gives:

- squarefree semiprime indices: `23,313`;
- indices whose mixed pair is inherited by at least one smaller divisor-modulus ancestor: `15,433`;
- indices with a structurally primitive mixed pair: `7,880`;
- primitive fraction: approximately `0.3380`.

Thus about two thirds of squarefree-semiprime square-only layers in this range are already redundant before any denominator-prime search.

The most common **minimum** inheriting ancestors in this range begin:

- `B=1`: 9,860 indices;
- `B=2`: 2,115;
- `B=3`: 614;
- `B=6`: 436;
- `B=12`: 155;
- `B=8`: 104;
- `B=5`: 103;
- `B=14`: 90;
- `B=18`: 89;
- `B=24`: 75;
- `B=15`: 75.

These counts are finite data only.

## Small-ancestor interpretation

The first three filters are particularly transparent:

\[
A\equiv1\pmod3
\Rightarrow B=1\text{ shadows the mixed pair},
\]

\[
A\equiv2\pmod7
\Rightarrow B=2\text{ shadows the mixed pair},
\]

\[
A\equiv4\pmod{15}
\Rightarrow B=4\text{ shadows the mixed pair}.
\]

For `B=3`, the ancestor modulus is `11` and

\[
Q_3=\{1,3,9\}\pmod{11},
\]

which captures three of the five nonzero quadratic-residue classes.  For `B=6`, modulus `23`,

\[
Q_6=\{1,2,3,4,6,9,12,13,18\},
\]

capturing nine of the eleven quadratic-residue classes.  This explains why very small ancestors continue to eliminate many semiprime mixed layers even after the `3,7,15` filters.

## Research consequence

The correct semiprime composite-rescue object is no longer the full divisor lattice.  It is the residual set of pairs

\[
(A=uv,\ -u/v,\ -v/u)
\]

for which no smaller ancestry modulus accepts the square class of `u`.

The next useful question is therefore:

> What arithmetic property characterizes squarefree semiprimes `uv` for which `u^2` avoids every earlier ancestor set `Q_B`?

A theorem forcing one such ancestor, or forcing a controlled successor once all ancestors fail, would convert a large finite pruning effect into structural progress toward strong/Type-II universality.

## Claim boundary

This note does not prove that every prime denominator is rescued by a squarefree-semiprime layer.  It only gives an exact reduction and demonstrates that the truly new semiprime part is much smaller than the raw square-divisor search suggests.