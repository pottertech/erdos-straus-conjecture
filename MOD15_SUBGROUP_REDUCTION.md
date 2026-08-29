# Exact Mod-15 Subgroup Reduction

**Date:** 2026-08-28

## Setup

Assume a hard case has survived the shift-divisor reduction and the exact `u=7` layer.

From the shift-divisor reduction,

\[
n\equiv1\pmod{24}.
\]

Take

\[
u=15,\qquad x=\frac{n+15}{4},\qquad M=nx.
\]

Because `n ≡ 1 (mod 24)`, `x` is even, so `2|M`.

## The inherited mod-15 restriction is deterministic

Every hard case satisfies `n ≡ 1 (mod 3)`.

The hard-case prime-factor condition also rules out

\[
n\equiv2\pmod5.
\]

Indeed, if `n ≡ 2 (mod 5)`, then `5 | n+3`, so `5` divides the odd part of

\[
\frac{n(n+3)}4.
\]

But `5 ≡ 2 (mod 3)`, contradicting the hard-case requirement that every odd prime factor of `n(n+3)/4` be `1 (mod 3)`.

Now suppose

\[
n\equiv3\pmod5.
\]

At `u=7`,

\[
x_7=\frac{n+7}{4}.
\]

Since `n+7 ≡ 0 (mod 5)`, we have `5|x_7`. But `5` is a quadratic nonresidue modulo 7. By the exact mod-7 theorem, any QNR prime factor forces `u=7` to succeed. Therefore a case that survives `u=7` cannot satisfy `n ≡ 3 (mod 5)`.

The remaining possibilities are

\[
n\equiv1\text{ or }4\pmod5.
\]

Together with `n ≡ 1 (mod 3)`, this gives

\[
\boxed{n\equiv1\text{ or }4\pmod{15}.}
\]

Thus the mod-15 input restriction is a theorem, not a computational observation.

## Subgroup structure modulo 15

The unit group is

\[
(\mathbb Z/15\mathbb Z)^\times=\{1,2,4,7,8,11,13,14\}.
\]

Let

\[
H=\langle2\rangle=\{1,2,4,8\}.
\]

This is an index-two subgroup. The centered target is

\[
-1\equiv14\pmod{15},
\]

which lies in the other coset

\[
14H=\{7,11,13,14\}.
\]

## Exact theorem

For every surviving hard case described above,

\[
\boxed{u=15\text{ succeeds iff some prime divisor of }M\text{ lies outside }H.}
\]

### Obstruction

If every prime divisor of `M` lies in `H`, every bounded signed product also lies in `H`, since `H` is a subgroup. Because `14` lies outside `H`, the target is unreachable and `u=15` fails.

### Converse

Because `2|M`, the centered set contains `2` and `2^{-1}=8`.

We also always have an aggregate centered factor equal to `4 mod 15`:

- if `n ≡ 4 (mod 15)`, use the centered factor `n`;
- if `n ≡ 1 (mod 15)`, then `x ≡ 4n ≡ 4 (mod 15)`, so use the centered factor `x`.

Hence the centered products already contain all of

\[
H=\{1,2,4,8\}.
\]

If a prime factor `q|M` lies outside `H`, then `q∈14H`. Therefore some `h∈H` satisfies

\[
hq\equiv14\pmod{15}.
\]

Since that `h` is already available as a centered product, adjoining `q` reaches `-1`.

## Computational cross-check through 10^7

After the shift-divisor, exact mod-7, and exact mod-11 filters, 1,054 corrected prime hard cases remain below `10^7`.

- 373 have a prime factor of `M=n(n+15)/4` outside `H` and all 373 succeed at `u=15`;
- 681 have every prime factor of `M` in `H` and all 681 fail at `u=15`.

There are zero mismatches.

The computation is now only a cross-check of the deterministic theorem above.