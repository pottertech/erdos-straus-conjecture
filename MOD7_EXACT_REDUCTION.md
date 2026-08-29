# Exact Mod-7 Reduction After Shift-Divisor Purity

**Date:** 2026-08-28

## Setup

Assume `n ≡ 1 (mod 12)` and that the shift-divisor residual conditions hold:

1. every odd prime divisor of `n+1` is `1 (mod 4)`;
2. every prime divisor of `n+4` is `1 (mod 4)`.

Take `u=7` and set

\[
x=\frac{n+7}{4},\qquad M=nx.
\]

The exact centered criterion is

\[
\prod_{p^e\parallel M} p^{c_p}\equiv -1\pmod 7,
\qquad -e\le c_p\le e.
\]

## Lemma 1: the shift residual forces x even

Because

\[
\frac{n+1}{2}=2x-3,
\]

and every odd prime divisor of `n+1` is `1 (mod 4)`, the odd number `2x-3` is itself `1 (mod 4)`. Hence

\[
2x-3\equiv1\pmod4,
\]

so `x` is even. Therefore the prime factor `2` is always present in `M`.

Modulo 7, `2` is a quadratic residue.

## Theorem: exact u=7 criterion on the shift residual

Under the setup above,

\[
\boxed{u=7\text{ succeeds if and only if }M\text{ has a quadratic-nonresidue prime factor modulo }7.}
\]

The nonzero quadratic residues modulo 7 are

\[
\{1,2,4\},
\]

and the nonresidues are

\[
\{3,5,6\}.
\]

### Forward obstruction

If every prime divisor of `M` lies in `{1,2,4} (mod 7)`, then every bounded signed product of those prime factors is again a quadratic residue. But `-1 ≡ 6 (mod 7)` is a quadratic nonresidue. Therefore the centered target `-1` is unreachable and `u=7` fails.

### Converse

Suppose some prime divisor `p|M` is a quadratic nonresidue modulo 7. Since `2|M`, one of the following gives a centered witness:

- if `p ≡ 6 (mod 7)`, then `p ≡ -1` directly;
- if `p ≡ 3 (mod 7)`, then `2p ≡ 6 (mod 7)`;
- if `p ≡ 5 (mod 7)`, then `2^{-1}p ≡ 4\cdot5 ≡ 6 (mod 7)`.

The exponents `+1` and `-1` are allowed by the centered bounds because both involved primes divide `M`.

Thus any QNR prime factor forces success.

## Consequence

Any shift-residual hard case that also fails `u=7` must satisfy

\[
\boxed{p\bmod7\in\{1,2,4\}\quad\text{for every prime }p\mid n(n+7)/4.}
\]

This is a deterministic purity condition, not a probabilistic statement.

## Computational cross-check through 10^7

Among the 48,711 corrected prime hard cases below `10^7`, 7,272 survive the two shift-divisor criteria. Of those:

- 5,135 succeed at `u=7`;
- 2,137 fail at `u=7`.

For all 7,272 cases, with zero exceptions,

\[
u=7\text{ succeeds}\iff M\text{ has a QNR prime factor mod }7.
\]

The computation is only a cross-check; the equivalence above follows algebraically from the forced factor `2` and the mod-7 residue table.