# Exact Mod-23 Reduction from Forced Factors 2 and 3

**Date:** 2026-08-28

## Setup

After the shift-divisor reduction we have

\[
n\equiv1\pmod{24}.
\]

Write `n=24m+1`. For `u=23`,

\[
x=\frac{n+23}{4}=6m+6.
\]

Hence

\[
\boxed{6\mid x},
\]

so both prime factors `2` and `3` occur in the centered product set for

\[
M=nx.
\]

## Discrete logs modulo 23

Use primitive root `5`. Then

\[
\log_5(2)=2,\qquad \log_5(3)=16\equiv-6\pmod{22},
\]

and

\[
\log_5(-1)=11.
\]

Thus the mandatory factors `2` and `3`, each with centered coefficient in `{-1,0,1}`, produce the even shifts

\[
B=\{0,\pm2,\pm4,\pm6,\pm8\}\pmod{22}.
\]

Among the even residues modulo 22, the only values missing from `B` are `\pm10`.

## Immediate obstruction

If every prime divisor of `M` is a quadratic residue modulo 23, every centered log sum is even, while target log `11` is odd. Therefore `u=23` fails.

## Generic QNR success

Let `q|M` be a quadratic nonresidue and write

\[
s=\log_5(q),
\]

so `s` is odd.

If `s` is not `\pm1 (mod 22)`, then

\[
11-s
\]

is an even residue other than `\pm10`, hence belongs to `B`. The mandatory factors `2` and `3` therefore supply the required adjustment and `u=23` succeeds.

The exceptional QNR logs `\pm1` correspond to residues

\[
5\quad\text{and}\quad14\pmod{23}.
\]

## Exceptional non-QR failure shape

Suppose QNR factors are present but all have residue `5` or `14 mod 23`.

The method still succeeds if either:

1. the total available multiplicity of these `\pm1` QNR logs is at least 3, because a centered QNR sum `\pm3` can combine with a forced even shift `\pm8` to reach 11; or
2. there is any additional nontrivial QR-log contribution beyond the mandatory single factors `2` and `3`, because an extra nonzero even log extends the forced even set to include `\pm10`.

Consequently the only non-QR failure configuration is:

- all QNR prime factors are `5` or `14 mod 23`;
- their total multiplicity is at most 2 (and at least 1);
- the only nontrivial QR factors modulo 23 are exactly one residue-2 factor and one residue-3 factor, namely the mandatory generators, each with total multiplicity one in its residue class;
- all remaining QR factors are `1 mod 23`.

Under those restrictions target log 11 is unreachable.

## Exact classification

For any `n ≡ 1 (mod 24)` with `gcd(M,23)=1`, failure at `u=23` occurs precisely in one of two situations:

1. **QR purity:** every prime divisor of `M` is a quadratic residue modulo 23;
2. **small exceptional shape:** the non-QR configuration described above.

Everything else succeeds by a centered product using the forced factors 2 and 3 plus at most a small number of additional prime factors.

## Corrected computational cross-check through 10^7

On the corrected residual samples tested through `10^7`, this classification has zero mismatches.

For the 388 cases that survived the earlier `u=19` layer in the sequential first-success cascade:

- 238 succeed at `u=23`;
- 150 fail;
- every failure is either QR-pure or has the exact small exceptional shape above.

If `u=19` is skipped and `u=23` is applied directly after the `u=15` layer, 681 cases enter and only 283 fail.

This makes `u=23` a particularly strong deterministic layer because its denominator factor `x=(n+23)/4` carries both forced generators 2 and 3.