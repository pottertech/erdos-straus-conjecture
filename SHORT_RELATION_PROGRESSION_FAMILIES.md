# Arithmetic-Progression Families from All Four Short Relations

**Date:** 2026-08-29  
**Status:** Exact algebraic reformulation. Novelty relative to existing semi-constructive Erdős--Straus literature is not asserted.

Let

\[
u\equiv3\pmod4,
\qquad
x_u=\frac{n+u}{4},
\qquad
M_u=n x_u.
\]

The four short relations used in the corrected cascade can all be converted into explicit arithmetic progressions once the small factor parameters are fixed.

## 1. One-factor linear route

Fix `u,p` with

\[
u\mid p+1.
\]

If

\[
\boxed{n\equiv-u\pmod{4p}},
\]

then `p|x_u`, hence `p|M_u`, and `p ≡ -1 (mod u)`. The short-relation identity gives an Erdős--Straus decomposition.

This is the family developed in `DOMINANT_P_MINUS_ONE_PROGRESSIONS.md`.

## 2. One-factor cubic route

Fix `u,p` with

\[
p^3\equiv-1\pmod u.
\]

If

\[
\boxed{n\equiv-u\pmod{4p^3}},
\]

then `p^3|x_u`, so the cubic centered relation applies.

Thus every fixed cubic witness also seeds an unconditional arithmetic progression.

## 3. Two factors both from x: product route

Fix `u,p,q`, with `p != q`, such that

\[
pq\equiv-1\pmod u.
\]

If

\[
\boxed{n\equiv-u\pmod{4pq}},
\]

then both `p|x_u` and `q|x_u`, so `pq|M_u`; the product short relation applies.

Hence `(u,p,q)` produces a solved progression modulo `4pq`.

## 4. Two factors both from x: opposite-residue route

Fix `u,p,q`, with `p != q`, such that

\[
p+q\equiv0\pmod u.
\]

Again,

\[
\boxed{n\equiv-u\pmod{4pq}}
\]

forces `p,q|x_u`, and the opposite-residue short relation gives an explicit decomposition.

## 5. Mixed source n+x: product route

Now one centered factor is the variable `n` itself and the other is a fixed factor `q|x_u`.

Assume `gcd(q,u)=1`. The conditions are

\[
q\mid x_u
\]

and

\[
nq\equiv-1\pmod u.
\]

They are exactly

\[
\boxed{
 n\equiv-u\pmod{4q},
 \qquad
 n\equiv-q^{-1}\pmod u.
}
\]

Because `gcd(4q,u)=1` in the exact centered setting, CRT combines these into one residue class modulo

\[
\boxed{4qu}.
\]

Every integer in that CRT class has the corresponding short-relation decomposition.

### Most frequent observed example

For

\[
u=11,
\qquad q=5,
\]

we have

\[
n\equiv-11\pmod{20},
\qquad
5n\equiv-1\pmod{11}.
\]

Equivalently,

\[
\boxed{n\equiv189\pmod{220}}.
\]

This template occurred as the minimal witness 281 times in the corrected `10^8` residual sample, but the progression theorem holds for all integers in the class.

## 6. Mixed source n+x: opposite-residue route

The conditions are

\[
q\mid x_u
\]

and

\[
n+q\equiv0\pmod u.
\]

Equivalently,

\[
\boxed{
 n\equiv-u\pmod{4q},
 \qquad
 n\equiv-q\pmod u.
}
\]

Again CRT gives one solved class modulo `4qu`.

For the frequent template

\[
u=11,
\qquad q=5,
\]

this becomes

\[
\boxed{n\equiv149\pmod{220}}.
\]

This template occurred 193 times as the minimal witness through `10^8`.

## 7. Other frequent mixed-source templates through 10^8

| u | route | q | exact solved progression | minimal-witness occurrences |
|---:|---|---:|---|---:|
| 11 | `nq=-1` | 5 | `n ≡ 189 (mod 220)` | 281 |
| 11 | `n=-q` | 5 | `n ≡ 149 (mod 220)` | 193 |
| 7 | `nq=-1` | 17 | `n ≡ 401 (mod 476)` | 114 |
| 7 | `n=-q` | 17 | `n ≡ 333 (mod 476)` | 85 |
| 7 | `nq=-1` | 19 | `n ≡ 221 (mod 532)` | 76 |
| 7 | `n=-q` | 19 | `n ≡ 373 (mod 532)` | 74 |
| 19 | `n=-q` | 5 | `n ≡ 261 (mod 380)` | 70 |
| 23 | `nq=-1` | 2 | `n ≡ 57 (mod 184)` | 58 |
| 23 | `n=-q` | 2 | `n ≡ 113 (mod 184)` | 54 |
| 7 | `n=-q` | 31 | `n ≡ 613 (mod 868)` | 50 |

## 8. Finite-family counts extracted from the corrected 10^8 run

Among the 4,984 minimal two-factor certificates:

- 3,038 use source `n+x`;
- 1,946 use source `x+x`.

After grouping repeated witnesses by their fixed parameters, the sample contains:

- **902 distinct mixed-source `(u, route, q)` templates**;
- **735 distinct `x+x` `(u, route, p, q)` templates**.

Together with the 6,386 distinct linear `p=-1` progression classes and the rare cubic classes, the corrected `10^8` computation therefore selects a large finite library of unconditional arithmetic-progression solutions.

## 9. Proof-program consequence

The short-relation conjecture can now be restated as a covering problem:

> Can a finite or structurally generated collection of these exact progression families cover every remaining classical residual case?

Even when a finite cover is impossible, the complement of a large finite family is an explicit system of forbidden residue classes. Those restrictions can be fed into the next short-relation layer deterministically.
