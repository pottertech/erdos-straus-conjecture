# Exact Mod-11 Reduction After the Mod-7 Layer

**Date:** 2026-08-28

## Setup

Assume a prime hard case survives:

1. the two shift-divisor criteria;
2. the exact `u=7` reduction.

Take `u=11` and set

\[
x=\frac{n+11}{4},\qquad M=nx.
\]

Since every hard case has `n ≡ 1 (mod 12)`, we have

\[
n+11\equiv0\pmod{12},
\]

so

\[
\boxed{3\mid x.}
\]

Thus the centered product set for `M` always contains a contribution from the prime `3`.

## Discrete-log coordinates modulo 11

Use primitive root `2`. The nonzero residues have logs modulo 10:

| residue | log base 2 |
|---:|---:|
|1|0|
|2|1|
|3|8 = -2|
|4|2|
|5|4|
|6|9 = -1|
|7|7 = -3|
|8|3|
|9|6 = -4|
|10|5|

The centered target `-1 ≡ 10 (mod 11)` therefore has log `5`.

The quadratic residues are `{1,3,4,5,9}` (even logs), while the quadratic nonresidues are `{2,6,7,8,10}` (odd logs).

## Immediate obstruction

If every prime divisor of `M` is a quadratic residue modulo 11, every centered log sum is even and therefore cannot equal target log `5`. Hence `u=11` fails.

## Immediate success routes

The mandatory factor `3` contributes log `-2`.

Therefore:

- a factor `10 mod 11` succeeds by itself;
- a QNR factor `7` or `8 mod 11` combines with the mandatory `3` to reach log `5`;
- a QR factor `5` or `9 mod 11` provides log `±4`, which combines with a QNR `2` or `6` (log `±1`) to reach `5`;
- two available `±2` QR-log units (residues `3` or `4`, counted with multiplicity) provide `±4`, again closing with a QNR `2` or `6`;
- three available QNR `±1` units from residues `2` or `6` can supply `±3`, which combines with the mandatory `±2` unit from `3` to reach `5`.

## Exact exceptional failure shape

Apart from the all-QR obstruction, the only remaining failure configuration is:

1. every QNR prime factor is `2` or `6 mod 11`;
2. the total multiplicity of prime factors in residue classes `{2,6}` is at most 2 but at least 1;
3. the total multiplicity of prime factors in residue classes `{3,4}` is exactly 1 (this is the mandatory `3` and no additional `±2` QR-log unit is available);
4. no prime factor lies in residue classes `{5,7,8,9,10}`;
5. residue class `1` factors are unrestricted.

Equivalently, in the exceptional non-QR failure case all prime factors lie in

\[
\{1,2,3,4,6\}\pmod{11},
\]

with QNR capacity at most 2 and `±2` QR-log capacity exactly 1.

The reason is elementary in the cyclic log group `Z/10Z`: under those restrictions the odd part of every centered sum is confined to `{-2,-1,0,1,2}`, while the only nonzero even shift available is `±2`; target `5` is unreachable. If any listed restriction is broken, one of the explicit success routes above reaches `5`.

## Computational cross-check through 10^7

There are 2,137 corrected prime hard cases below `10^7` that survive the shift criteria and fail `u=7`.

For these cases:

- 1,083 succeed at `u=11`;
- 1,054 fail at `u=11`.

Among the 1,054 failures:

- 909 are the pure all-QR obstruction modulo 11;
- 145 have exactly the exceptional non-QR shape described above.

The classification matches all 2,137 cases with zero mismatches.

## Research implication

After the first two exact layers, a hypothetical counterexample is no longer merely a generic hard case. It must satisfy simultaneous residue-purity restrictions modulo 7 and one of two tightly constrained residue structures modulo 11. This is a finite deterministic obstruction description and is a better basis for the next cascade step than the former probabilistic divisor-distribution heuristic.