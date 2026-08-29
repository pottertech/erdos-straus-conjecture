# Quadratic-Character Obstruction for Prime u

**Date:** 2026-08-28  
**Status:** Exact general lemma for prime `u ≡ 3 (mod 4)`

## Setup

Let

\[
x=\frac{n+u}{4},\qquad M_u=nx,
\]

where `u` is an odd prime, `u ≡ 3 (mod 4)`, and `gcd(n,u)=1`.  Modulo `u`,

\[
x\equiv \frac n4\pmod u.
\]

Therefore

\[
\boxed{M_u\equiv \frac{n^2}{4}\equiv (n/2)^2\pmod u.}
\]

Thus `M_u` is always a quadratic residue modulo `u`.

## Lemma 1 (even QNR multiplicity)

Write

\[
M_u=\prod p^{e_p}.
\]

Then

\[
\prod_p\left(\frac pu\right)^{e_p}
=
\left(\frac{M_u}{u}\right)=1.
\]

Hence the total valuation

\[
\sum_{(p/u)=-1}e_p
\]

of quadratic-nonresidue prime factors is even.

This is visible in the prime-capacity formulation as: the sum of capacities in odd discrete-log classes is even.

## Lemma 2 (pure-QR obstruction)

Suppose every prime factor `p|M_u` satisfies

\[
\left(\frac pu\right)=1.
\]

Then every centered signed product

\[
\prod p^{c_p}
\]

is also a quadratic residue modulo `u`.  But because `u ≡ 3 (mod 4)`,

\[
\left(\frac{-1}{u}\right)=-1.
\]

Therefore

\[
-1\notin\mathcal S_u(M_u),
\]

and the exact centered u-method **must fail** at this `u`.

So prime-factorwise quadratic-residue purity is a deterministic obstruction, not a probabilistic event.

## What QNR factors mean

Since the total QNR multiplicity is even, the smallest non-pure case has total QNR multiplicity 2.  The centered method can nevertheless succeed by selecting an odd signed subcombination of QNR factors and using QR factors to correct the remaining discrete-log offset.

Thus a useful classification for each prime `u` is:

1. **pure QR:** automatic failure;
2. **two-QNR exceptional vectors:** finite small-capacity problem;
3. **larger/mixed QNR capacity:** typically forced success by the bounded capacity congruence.

The word “typically” in item 3 is empirical until a modulus-specific capacity theorem is proved; items 1 and 2's parity restriction are exact.

## Corrected cascade evidence below 10^6

### u=11

After the corrected u=7 layer, 178 cases fail u=11:

- 152 are pure-QR modulo 11;
- 26 have the single exceptional capacity vector `(2,1,0,0,0)`, with total QNR capacity 2.

### u=19

After the u=15 layer, 68 cases fail u=19:

- 49 are pure-QR modulo 19;
- 19 have QNR factors, and every one has total QNR valuation exactly 2.

No u=19 failure in this finite sample has QNR multiplicity 4 or larger.

## Research direction

The corrected prime-u cascade can now be viewed as repeatedly testing whether the shifted product

\[
M_u=n(n+u)/4
\]

is **factorwise** quadratic-residue-pure modulo `u`, plus a small explicitly classifiable two-QNR exceptional set.

A strong deterministic theorem would show that a prime n in the classical six residue classes cannot make `M_u` remain pure-QR (or one of the tiny two-QNR exceptions) for every u in a suitable finite or growing cascade.

This formulation is substantially sharper than an independence/Chebotarev heuristic: it identifies the exact local obstruction that must persist simultaneously across shifts.
