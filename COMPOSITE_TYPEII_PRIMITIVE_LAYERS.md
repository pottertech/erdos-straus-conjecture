# Primitive Composite Layers in the Square-Completed Type-II Search

**Status:** exact structural pruning lemma plus finite exploratory statistics; not a proof of Type-II universality.

For square depth `A`, write

\[
m_A=4A-1
\]

and define the complete square-completed Type-II trap set

\[
T_A=\{-4D\pmod{m_A}: D\mid A^2\}.
\]

A prime `p` has a Type-II witness at depth `A` exactly when its residue modulo `m_A` lies in `T_A` (subject to the usual `p \nmid D` condition, automatic for fixed small `D` once `p>A^2`).

## Exact divisor-modulus inheritance lemma

Let `B<A` and suppose

\[
m_B\mid m_A.
\]

If a residue `r in T_A` also satisfies

\[
r\pmod{m_B}\in T_B,
\]

then every integer

\[
n\equiv r\pmod{m_A}
\]

already lies in a depth-`B` Type-II trap.  Therefore the progression `r mod m_A` contributes no genuinely new global coverage at depth `A`.

This implication is immediate from `m_B | m_A`.

Call such a residue **divisor-modulus inherited**.  Define the primitive part

\[
P_A=T_A\setminus\bigcup_{\substack{B<A\\m_B\mid m_A}}
\{r\in T_A:r\bmod m_B\in T_B\}.
\]

If `P_A` is empty, the entire depth-`A` layer is globally redundant relative to smaller divisor moduli and can be deleted from any covering search without changing the covered set.

The accompanying script `composite_typeII_layer_pruner.py` computes these sets exactly.

## Why this isolates the composite core

If `m_A=4A-1` is prime, there is no nontrivial earlier modulus `m_B>1` dividing it.  Thus prime-modulus layers have no divisor-modulus inheritance and form the familiar prime backbone.

Composite moduli behave differently.  Their trap sets can contain large inherited pieces, and some composite layers are completely redundant.  The only composite layers relevant to a genuinely new rescue mechanism are those with

\[
P_A\ne\varnothing.
\]

This gives an exact first pruning of the proposed composite-rescue program.

## Finite exploratory audit

An independent run of the exact algorithm through `A=2000` produced:

- 1493 composite-modulus layers;
- 572 completely divisor-modulus redundant composite layers;
- 921 composite layers with at least one primitive residue;
- redundant fraction approximately `0.3831`;
- mean primitive-residue fraction among composite layers approximately `0.3319`.

These numbers are **finite exploratory statistics**, not asymptotic claims.  They show that a substantial part of the nominal composite search space is provably redundant before any primes are examined.

Early examples of completely redundant composite layers include

\[
A=7,13,16,19,23,29,31,34,37,43,44,47,\ldots
\]

while early composite layers with genuinely primitive residue classes include

\[
A=4,9,10,14,22,24,25,28,30,36,39,40,\ldots
\]

## Important limitation

`P_A` is a conservative structural notion.  An earlier modulus `m_B` that does **not** divide `m_A` can still cover some subprogressions inside a residue class modulo `m_A` after CRT refinement.  Therefore `P_A != empty` does not mean every point of those primitive residue classes is genuinely new relative to the full earlier union.

The next stage should refine each primitive composite residue by CRT against the earlier primitive system and retain only survivor subprogressions.  That produces a finite-state residual graph rather than the raw layer list.

## Proposed next theorem target

The useful global target is not another density estimate.  It is a structural statement of the form:

> Every CRT survivor of the prime backbone eventually enters a primitive composite Type-II trap under a controlled depth transition.

A proof could arise from one of three mechanisms:

1. a monotone descent invariant on survivor states;
2. impossibility of cycles in the composite residual graph;
3. a finite transition grammar whose terminal states are all Type-II traps.

Any such statement would address the arithmetic rigidity missing from the existing sieve estimates.  Until one is proved, the composite-rescue program remains exploratory.