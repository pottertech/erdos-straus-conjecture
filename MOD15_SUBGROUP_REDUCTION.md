# Mod-15 Subgroup Reduction

**Date:** 2026-08-28

## Scope

This note gives an exact theorem for the `u=15` layer under explicit congruence hypotheses, then records that those hypotheses hold for every case reaching this layer in the corrected computation through `10^7`.

The inherited congruence restriction `n ≡ 1 or 4 (mod 15)` is **not yet claimed as a global theorem** from the previous layers.

## Setup

Assume

\[
n\equiv1\pmod{24},
\]

and take

\[
u=15,\qquad x=\frac{n+15}{4},\qquad M=nx.
\]

Since `n ≡ 1 (mod 24)`, `x` is even, so the prime factor `2` is present in `M`.

The unit group modulo 15 is

\[
(\mathbb Z/15\mathbb Z)^\times=\{1,2,4,7,8,11,13,14\}.
\]

Let

\[
H=\langle2\rangle=\{1,2,4,8\}.
\]

This is an index-two subgroup. The target is

\[
-1\equiv14\pmod{15},
\]

which lies in the other coset

\[
14H=\{7,11,13,14\}.
\]

## Exact theorem under n ≡ 1 or 4 mod 15

Assume in addition

\[
n\equiv1\text{ or }4\pmod{15}.
\]

Then

\[
\boxed{u=15\text{ succeeds iff some prime divisor of }M\text{ lies outside }H.}
\]

### Obstruction

If every prime divisor of `M` lies in `H`, every bounded signed product also lies in `H`, since `H` is a subgroup. The target `14` lies outside `H`, so `u=15` fails.

### Converse

Because `2|M`, the centered set contains `2` and `2^{-1}=8`.

We also always have an aggregate centered factor equal to `4 mod 15`:

- if `n ≡ 4 (mod 15)`, use the centered factor `n`;
- if `n ≡ 1 (mod 15)`, then `x ≡ 4n ≡ 4 (mod 15)`, so use the centered factor `x`.

Thus the available centered products contain all of

\[
H=\{1,2,4,8\}.
\]

If a prime factor `q|M` lies outside `H`, then `q` lies in the coset `14H`. Hence for some `h∈H`,

\[
hq\equiv14\pmod{15}.
\]

Since every `h∈H` is already available as a centered product, adjoining `q` gives the target `-1`.

Therefore any factor outside `H` forces success.

## Corrected computational layer through 10^7

After the shift-divisor, exact mod-7, and exact mod-11 filters, 1,054 prime hard cases remain below `10^7`.

All 1,054 satisfy

\[
n\equiv1\text{ or }4\pmod{15}.
\]

For this finite set:

- 373 have at least one prime factor of `M=n(n+15)/4` outside `H` and all 373 succeed at `u=15`;
- 681 have every prime factor of `M` in `H` and all 681 fail at `u=15`.

There are zero mismatches.

The six residue-support sets observed among the failures are subsets of `{1,2,4,8}` only, exactly as the subgroup theorem predicts.

## Remaining proof task

To promote this layer to a fully deterministic cascade theorem, one still needs to derive the inherited restriction

\[
n\equiv1\text{ or }4\pmod{15}
\]

from earlier proven obstruction conditions, or replace it with a more general mod-15 theorem that treats the other possible residue classes directly.

This distinction is important: the subgroup criterion itself is exact; the fact that all computed survivors enter it in the favorable residue classes is currently finite evidence.