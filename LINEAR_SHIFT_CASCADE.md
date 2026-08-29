# Linear-Shift Structure of the Corrected u-Method Cascade

**Date:** 2026-08-28

## Residual congruence sharpening

A hard case already satisfies

\[
n\equiv1\pmod{12}.
\]

After the shift-divisor reduction, the exact mod-7 analysis shows that

\[
x_7=\frac{n+7}{4}
\]

is even. Therefore

\[
n+7\equiv0\pmod8,
\]

hence

\[
\boxed{n\equiv1\pmod{24}.}
\]

Write

\[
n=24m+1.
\]

## Every u-layer is a neighboring linear form

For any `u ≡ 3 (mod 4)`, write

\[
u=4a+3.
\]

Then

\[
x_u=\frac{n+u}{4}
=\frac{24m+1+4a+3}{4}
=6m+a+1.
\]

Thus the corrected cascade is not a collection of unrelated factorizations. As `u` increases by 4, `x_u` increases by exactly 1.

Starting at `u=7`, if

\[
t=\frac{n+7}{4}=6m+2,
\]

then

\[
x_{7+4j}=t+j.
\]

The cascade therefore studies the consecutive integers

\[
t,t+1,t+2,t+3,\ldots
\]

with a different modulus `u=7+4j` attached to each term.

## Forced small factors

From

\[
x_u=6m+a+1,
\]

we get two immediate deterministic divisibility rules.

### Forced factor 2

If `a` is odd, then `a+1` is even, so

\[
2\mid x_u.
\]

Equivalently,

\[
u\equiv7\pmod8.
\]

Thus `u=7,15,23,31,39,47,55,...` have a mandatory factor 2 in `x_u`.

### Forced factor 3

If

\[
a+1\equiv0\pmod3,
\]

then

\[
3\mid x_u.
\]

This occurs for `a ≡ 2 (mod 3)`, giving

\[
u=11,23,35,47,59,71,\ldots
\]

### Both 2 and 3

The two conditions coincide at

\[
u=23,47,71,95,\ldots
\]

so these layers force

\[
6\mid x_u.
\]

## First layers

| u | x_u | forced factor |
|---:|---|---|
| 7  | `6m+2`  | 2 |
| 11 | `6m+3`  | 3 |
| 15 | `6m+4`  | 2 |
| 19 | `6m+5`  | none from 2/3 |
| 23 | `6m+6`  | 2 and 3 |
| 27 | `6m+7`  | none from 2/3 |
| 31 | `6m+8`  | 2 |
| 35 | `6m+9`  | 3 |
| 39 | `6m+10` | 2 |
| 43 | `6m+11` | none from 2/3 |
| 47 | `6m+12` | 2 and 3 |
| 51 | `6m+13` | none from 2/3 |
| 55 | `6m+14` | 2 |
| 59 | `6m+15` | 3 |

## Proof strategy implication

At each layer the centered product set for

\[
M_u=n x_u
\]

contains deterministic small-prime generators whenever the table forces 2 or 3. The mod-7 and mod-11 exact reductions already exploit precisely this phenomenon.

A promising deterministic strategy is therefore:

1. carry forward the residue-purity obstruction from earlier failed layers;
2. add the forced small-prime generator(s) at the next `x_u`;
3. classify the finite residue configurations that can still avoid `-1` modulo `u`;
4. iterate.

This reframes the cascade as a finite sequence of increasingly restrictive residue obstructions on consecutive linear forms, rather than as a probabilistic divisor-distribution problem.