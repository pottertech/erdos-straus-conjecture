# Exact Density of the Finite `p ≡ -1` Progression Cover

**Date:** 2026-08-29  
**Status:** Unconditional density statement for a finite set of explicit Erdős--Straus families. Novelty relative to the literature is not asserted.

## 1. Setup

For every admissible pair `(u,p)` with

\[
u\equiv3\pmod4,
\qquad u\mid p+1,
\]

the progression theorem in `DOMINANT_P_MINUS_ONE_PROGRESSIONS.md` proves every

\[
 n\equiv-u\pmod{4p}
\]

has an explicit Erdős--Straus decomposition.

The corrected short-relation computation through `10^8` produced **6,386 distinct `(u,p)` pairs** of this type among the minimal `p=-1` certificates. These pairs involve **5,140 distinct primes `p`**. Every such `p` is coprime to `840`.

The finite computation is used only to *select* this finite list of proven progressions. Once selected, coverage of those progressions is an unconditional CRT statement for all integers, not a finite-range extrapolation.

## 2. Density inside each classical residual class

Fix any one of the six classical residual classes

\[
 n\equiv r\pmod{840},
 \qquad
 r\in\{1,121,169,289,361,529\}.
\]

Each such `r` is `1 mod 4`. Since `u ≡ 3 mod 4`, the condition

\[
 n\equiv-u\pmod{4p}
\]

is compatible with the fixed mod-840 class. Because `gcd(p,840)=1`, after fixing `r mod 840` the progression imposes exactly one residue class modulo `p`.

For a fixed prime `p`, let `k_p` be the number of **distinct residues modulo p** supplied by the selected admissible `u` values:

\[
 -u\pmod p.
\]

Then the fraction of integers in the fixed mod-840 class *not* covered by the families attached to `p` is

\[
1-\frac{k_p}{p}.
\]

Conditions for distinct primes are independent by the Chinese remainder theorem. Therefore the exact natural density of the union inside **each** of the six residual classes is

\[
\boxed{
\delta
=1-\prod_p\left(1-\frac{k_p}{p}\right).
}
\]

## 3. Top-20 progression cover

For the 20 most frequent `(u,p)` pairs in the `10^8` finite sample, grouping the two distinct progressions with `p=139`, the exact density is

\[
\delta_{20}
=
\frac{10494737988230535041574314623}
{36244481733228158112294314623}
\approx
\boxed{0.2895540917}.
\]

Thus those twenty explicit progression families alone solve **28.9554%** of every classical residual mod-840 lattice.

The strongest single family,

\[
(u,p)=(7,13),
\]

is

\[
 n\equiv-7\pmod{52},
\]

and covers exactly

\[
\boxed{1/13\approx7.6923\%}
\]

of each residual mod-840 class.

## 4. Full finite selected family

Using all 6,386 distinct progression classes selected from the corrected `10^8` run, grouped across 5,140 distinct primes, gives

\[
\boxed{
\delta_{6386}
=1-\prod_{p\in P}\left(1-\frac{k_p}{p}\right)
\approx 0.6869852813.
}
\]

Therefore this **finite list of explicit, algebraically proven progressions** covers approximately

\[
\boxed{68.6985\%}
\]

of the integers in every one of the six classical residual classes modulo 840.

This is a global statement about all integers in those progressions. It is not the statement that 68.7% of cases up to `10^8` happened to pass a test.

## 5. What this does and does not prove

It proves a positive-density constructive cover of the classical residual lattice using a finite collection of short-relation identities.

It does **not** prove:

- that the 6,386 selected progressions are optimal;
- that a finite collection of `p=-1` families can cover 100%;
- that the remaining 31.3015% are counterexamples or even difficult for the other short relations;
- novelty relative to prior Erdős--Straus covering-family literature.

The remaining theorem problem is to combine this progression cover with the cubic and two-factor short relations, or to characterize the complement sufficiently strongly that another deterministic identity applies.

## 6. Strategic implication

The computation has now produced a finite mathematical object with a global consequence:

> a finite CRT cover by exact Erdős--Straus progressions.

This suggests a proof program based on enlarging a rigorously certified covering family while tracking the complement symbolically, instead of extending brute-force verification ranges alone.
