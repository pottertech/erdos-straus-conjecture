# Strong-Survivor Prime-Extension Persistence

**Status:** unconditional theorem about the ambient proper-ancestor square-class system. It is not a Type-II universality theorem, and its direct relevance to actual square-completed Type-II layers requires an additional realization condition.

## Setup

Let

\[
d\equiv3\pmod4
\]

be odd, and let `s mod d` be a **strong unit-square survivor**, meaning:

1. `s` is a unit square modulo `d`;
2. for every divisor
   \[
   e\mid d,\qquad e\equiv3\pmod4,
   \]
   including `e=d`,
   \[
   s\pmod e\notin Q_{(e+1)/4},
   \]
   where
   \[
   Q_B=\{D\pmod{4B-1}:D\mid B^2\}.
   \]

Fix a prime

\[
p\equiv1\pmod4,
\qquad p\nmid d,
\]

and put

\[
m=dp.
\]

We ask whether `s` can be lifted to a unit-square class `r mod m` that is itself strong at `m`.

## Theorem

For every fixed strong survivor `(d,s)`, all sufficiently large primes

\[
p\equiv1\pmod4,
\qquad p\nmid d,
\]

admit a strong survivor lift `r mod dp` satisfying

\[
r\equiv s\pmod d.
\]

## Proof

Choose a nonzero quadratic residue

\[
y\in QR(p).
\]

By CRT there is a unique class

\[
r\pmod{dp}
\]

with

\[
r\equiv s\pmod d,
\qquad
r\equiv y\pmod p.
\]

Because `s` is a unit square modulo `d` and `y` is a nonzero square modulo `p`, `r` is a unit square modulo `dp`.

If

\[
e\mid d,
\qquad e\equiv3\pmod4,
\]

then `r == s (mod e)`, so the old strong-survivor conditions remain avoided.

Every new `3 mod 4` divisor has the form

\[
e=pt,
\]

where

\[
t\mid d,
\qquad t\equiv3\pmod4.
\]

For fixed `t`, put

\[
B_{p,t}=\frac{pt+1}{4}.
\]

A bad lift at `e=pt` requires some divisor

\[
D\mid B_{p,t}^2
\]

with

\[
r\equiv D\pmod{pt}.
\]

Reducing modulo `p` forces

\[
y\equiv D\pmod p.
\]

Hence the number of bad choices of `y` contributed by this `t` is at most

\[
\tau(B_{p,t}^2).
\]

Since the set of relevant `t` is fixed and `B_{p,t}=O_d(p)`, the divisor bound gives

\[
\sum_t \tau(B_{p,t}^2)=p^{o(1)}.
\]

There are exactly `(p-1)/2` nonzero quadratic residues modulo `p`, so for all sufficiently large `p` at least one choice survives every new condition. This proves the theorem.

## Critical distinction: abstract versus realized survivors

The theorem above lives in the **ambient unit-square class space**. That is larger than the actual square-completed Type-II divisor lattice.

For a modulus

\[
m=4A-1,
\]

an actual depth-`A` Type-II trap must come from a divisor

\[
D\mid A^2
\]

and therefore from a class

\[
r\equiv D\pmod m.
\]

Call such a class **realized** at depth `A`.

A strong unit-square survivor need not be realized. The prime-extension theorem does not preserve realization, and therefore does not by itself produce actual primitive Type-II layers.

This distinction was checked explicitly for the main counterexample states used during the 2026-08-30 audit:

- `m=12155`, `A=3039`, survivor `s=5526`: no divisor `D|A^2` has `D == s (mod m)`;
- `m=352495`, `A=88124`, survivor `r=224316`: no divisor `D|A^2` has `D == r (mod m)`;
- `m=6407731`, `A=1601933`, survivor `r=3990232`: no divisor `D|A^2` has `D == r (mod m)`.

Thus these examples refute ambient ancestry-cover conjectures, but they are **not themselves square-completed Type-II trap classes**.

## Correct role of the theorem

The theorem proves only that the ambient proper-ancestor square-class system has persistent survivor towers and no factor-count closure threshold.

It does **not** prove that actual primitive Type-II divisor classes persist to arbitrary factor complexity.

For Type-II research, the correct residual object is the realized set

\[
R_A=\{D\bmod(4A-1):D\mid A^2\}
\]

minus the classes inherited from earlier divisor-modulus ancestors.

The next research stage must therefore work in `R_A`, not in all of `QR(4A-1)`.

## Strategic consequence

The ambient ancestry analysis remains useful as an upper-level geometric model, but it is too large for direct Type-II conclusions.

The actual question is:

> Which **realized divisor classes** `D mod (4A-1)`, with `D|A^2`, survive all proper ancestry reductions, and how do those realized primitive classes behave across depth families?

That is the correct object for any theorem intended to say something about complete Type-II coverage.

## Claim boundary

No claim about Erdős--Straus or universal Type II follows from ambient strong-survivor persistence alone. Any future use of this theorem must explicitly verify realization by a divisor of the relevant square `A^2`.