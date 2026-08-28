# Exact Centered Product-Set Criterion for the u-Method

**Date:** 2026-08-28  
**Status:** Algebraically exact when `gcd(nx,u)=1`

## 1. Setup

Let

\[
x=\frac{n+u}{4},\qquad M=nx,
\]

so the u-method factorization is

\[
(uy-M)(uz-M)=M^2.
\]

A candidate `u` succeeds if there are positive divisors `d_1,d_2` with

\[
d_1d_2=M^2,
\]

and

\[
d_1\equiv d_2\equiv -M\pmod u.
\]

Assume throughout this note that

\[
\gcd(M,u)=1.
\]

## 2. One-divisor reduction

Because `M` is a unit modulo `u`, the complementary-divisor congruence is automatic.

### Theorem 1 (Exact one-divisor criterion)

Under `gcd(M,u)=1`, the u-method succeeds if and only if there is a divisor

\[
d\mid M^2
\]

such that

\[
d\equiv -M\pmod u.
\]

### Proof

If the u-method succeeds, take `d=d_1`.

Conversely, suppose `d|M^2` and `d\equiv -M (mod u)`. Let

\[
d'=M^2/d.
\]

Since `M` and `d` are units modulo `u`,

\[
d'\equiv M^2d^{-1}
   \equiv M^2(-M)^{-1}
   \equiv -M\pmod u.
\]

Thus `d,d'` are the required complementary divisors. Setting

\[
y=\frac{d+M}{u},\qquad z=\frac{d'+M}{u}
\]

produces positive integers satisfying the u-method factorization and therefore the Erdős--Straus equation. ∎

## 3. Centering the divisor exponents

Write

\[
M=\prod_{p\mid M}p^{a_p}.
\]

Every divisor of `M^2` has the form

\[
d=\prod_{p\mid M}p^{b_p},\qquad 0\le b_p\le 2a_p.
\]

Define centered exponents

\[
c_p=b_p-a_p.
\]

Then

\[
-a_p\le c_p\le a_p
\]

and

\[
\frac dM=\prod_{p\mid M}p^{c_p}.
\]

Because `M` is invertible modulo `u`, the congruence `d\equiv -M (mod u)` is equivalent to

\[
\frac dM\equiv -1\pmod u.
\]

This gives the exact centered formulation.

### Theorem 2 (Centered signed-exponent criterion)

Let `x=(n+u)/4`, `M=nx`, and assume `gcd(M,u)=1`. Write

\[
M=\prod_{p\mid M}p^{a_p}.
\]

Then the u-method succeeds if and only if there exist integers `c_p` satisfying

\[
-a_p\le c_p\le a_p
\]

for every prime `p|M`, such that

\[
\boxed{\prod_{p\mid M}p^{c_p}\equiv -1\pmod u.}
\]

### Proof

By Theorem 1, success is equivalent to a divisor `d|M^2` with `d\equiv -M (mod u)`. Writing its exponent vector as `b_p` and setting `c_p=b_p-a_p` gives the displayed signed bounds and

\[
dM^{-1}\equiv \prod p^{c_p}\pmod u.
\]

Thus `d\equiv -M` is equivalent to the centered product being `-1`. The correspondence `b_p=c_p+a_p` is bijective between `0\le b_p\le2a_p` and `-a_p\le c_p\le a_p`, so the implication works in both directions. ∎

## 4. Product-set formulation

For each prime-power factor `p^{a_p}||M`, define

\[
S_p=\{p^{-a_p},p^{-a_p+1},\ldots,1,\ldots,p^{a_p}\}\subseteq (\mathbb Z/u\mathbb Z)^\times.
\]

Then define the bounded product set

\[
\mathcal S_u(M)=\prod_{p\mid M}S_p.
\]

Theorem 2 is equivalently

\[
\boxed{u\text{-method succeeds}\iff -1\in\mathcal S_u(M).}
\]

This is the preferred theorem target for the project. It avoids the incorrect `{-x*n^j}` reduction and does not require `u` to be prime or `(Z/uZ)^*` to be cyclic.

## 5. Immediate deterministic corollaries

Several useful sufficient conditions follow immediately.

### Corollary 3 (Order-two factor)

If some prime factor `p|M` satisfies

\[
p^c\equiv -1\pmod u
\]

for an integer `c` with `|c|\le a_p`, then the u-method succeeds.

In particular, if `p\equiv-1 (mod u)` and `a_p\ge1`, success is immediate.

### Corollary 4 (Two-factor route)

If primes `p,q|M` admit integers `r,s` with

\[
|r|\le a_p,\qquad |s|\le a_q,
\]

and

\[
p^rq^s\equiv-1\pmod u,
\]

then the u-method succeeds.

### Corollary 5 (Full product-set coverage)

If

\[
\mathcal S_u(M)=(\mathbb Z/u\mathbb Z)^\times,
\]

then the u-method succeeds.

## 6. Why this is stronger than the old three-target reduction

The old verifier reduced divisors of `n^2x^2` to divisors of `x^2` and tested the three residues

\[
-x,\ -xn,\ -xn^2\pmod u.
\]

That reduction is not equivalent in general. The exact centered formulation keeps all prime factors of `M=nx` symmetrically and asks only whether bounded signed products reach `-1`.

For prime `n`, separating the exponent of `n` from those of `x` is still possible, but doing so correctly introduces inverse powers in one of the reduced cases. The centered formulation avoids that asymmetry entirely.

## 7. Computational cross-check

The centered criterion was independently cross-checked against the exact direct-divisor criterion on 47,479 admissible `(n,u)` pairs with prime `n<100,000` and `u<80`, restricted to `gcd(nx,u)=1`. There were zero mismatches.

This is a validation of the implementation of the algebraic equivalence, not a proof of the global Erdős--Straus conjecture.

## 8. Next proof target

For the residual prime hard cases, the problem is now:

> Prove that for every relevant `n`, there exists a sufficiently small `u≡3 (mod 4)` with `gcd(nx,u)=1` such that the bounded product set `S_u(nx)` contains `-1`.

The corrected computation through `10^7` shows zero failures with `u<=300`, while the cases whose first-working value changed under the corrected verifier occur only for `n≡1` or `49 (mod 120)`.

The next deterministic analysis should therefore compare the bounded product sets for those two residue classes against the unaffected classes and identify which local factor guarantees force `-1` into the product set.
