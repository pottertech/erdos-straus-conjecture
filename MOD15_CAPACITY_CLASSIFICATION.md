# Exact Mod-15 Capacity Classification

**Date:** 2026-08-28  
**Status:** Exact finite-group classification for the centered criterion

Let

\[
x=\frac{n+15}{4},\qquad M=nx,
\]

and assume `gcd(M,15)=1`.  The unit group is

\[
(\mathbb Z/15\mathbb Z)^\times\cong C_4\times C_2.
\]

Use `2` as an order-4 generator and `11` as an independent order-2 generator.  The units have coordinates

\[
\begin{array}{c|c}
1&(0,0)\\
2&(1,0)\\
4&(2,0)\\
8&(3,0)\\
11&(0,1)\\
7&(1,1)\\
14&(2,1)\\
13&(3,1).
\end{array}
\]

The target `-1=14` is `(2,1)`.

## Capacity compression

Count prime valuations of `M` in the following inverse/self-inverse classes:

- `A`: residues `{2,8}`;
- `B`: residues `{7,13}`;
- `C`: residue `4`;
- `D`: residue `11`;
- `E`: residue `14=-1`.

Residue `1` is irrelevant.

The centered signed box reaches `(2,1)` exactly when there are bounded aggregate coefficients.  Eliminating those coefficients gives the following closed form.

## Theorem (exact u=15 criterion)

The u-method succeeds at `u=15` if and only if

\[
\boxed{
E\ge1
\quad\text{or}\quad
\bigl(D\ge1\ \text{and}\ (C\ge1\text{ or }A+B\ge2)\bigr)
\quad\text{or}\quad
\bigl(D=0\ \text{and}\ A\ge1\ \text{and}\ B\ge1\bigr).
}
\]

### Proof sketch

Assume first `E=0`; otherwise a factor `14 mod 15` is already `-1`.

Let `a` and `b` be aggregate signed coefficients from the inverse pairs `{2,8}` and `{7,13}`.  Let `c,d` be coefficients on the self-inverse classes `4,11`.  In `C4 x C2` the target equations are

\[
a+b+2c\equiv2\pmod4,
\]

\[
b+d\equiv1\pmod2.
\]

If `D>=1`, `d` can correct the second coordinate for any chosen `b`.  The first coordinate is then solvable if `C>=1` (choose `a=b=0,c=1`) or if `A+B>=2` (choose a bounded sum equal to 2 mod 4).

If `D=0`, the second equation forces an odd `b`, so `B>=1`.  The first equation has even target, hence an odd contribution from `a` is also required; `A>=1` is both necessary and sufficient (choose `a=b=1`).

These alternatives are exactly the displayed criterion. ∎

## Corrected cascade data below 10^6

After the classical modular reduction, exact A=3/hard gate, shift-divisor reduction, u=7 failure, and u=11 failure, **178** prime cases remain below `10^6`.

At `u=15`:

- **59** succeed;
- **119** fail.

Every one of the 119 failures has

\[
\boxed{B=D=E=0.}
\]

Thus every prime factor of `M=n(n+15)/4` in those cases lies in

\[
\{1,2,4,8\}=\langle2\rangle\subset(\mathbb Z/15\mathbb Z)^\times.
\]

Their observed capacity vectors are of the form `(A,0,C,0,0)` only.

This finite observation is evidence about the residual population; the displayed u=15 capacity theorem is exact.

## Structural interpretation

The first three corrected layers now have a common form:

- u=7 failure constrains factor residues to a small multiplicative pattern;
- u=11 failure is dominated by the quadratic-residue subgroup plus one tiny exceptional vector;
- u=15 failure, on the surviving tail, forces all factors into the index-2 subgroup `<2>`.

This suggests proving the cascade by showing that simultaneous subgroup purity for the shifted products

\[
M_u=n(n+u)/4
\]

cannot persist through enough distinct u-values.
