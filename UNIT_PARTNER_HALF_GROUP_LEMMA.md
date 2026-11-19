# Half-Group Lemma for Unit-Partner Failure

**Status:** exact deterministic theorem; analytic counting consequence still to be developed

Let

\[
u\equiv3\pmod4,
\qquad
K=\frac{n+u}{4},
\]

with `gcd(n,u)=1`. Since `u` is odd,

\[
K\equiv 4^{-1}n\pmod u,
\]

so `gcd(K,u)=1`; every prime divisor of `K` is therefore a unit modulo `u`.

Let

\[
R_u(K)=\{q\bmod u:q\text{ prime},\ q\mid K\}
\subseteq (\mathbb Z/u\mathbb Z)^\times.
\]

## The involution

Define

\[
\iota(r)=-r^{-1}.
\]

This is an involution on the unit group.

It has no fixed point. A fixed point would satisfy

\[
r=-r^{-1}\pmod u,
\]

hence

\[
r^2\equiv-1\pmod u.
\]

But if `u == 3 (mod 4)`, its prime factorization contains at least one prime `p == 3 (mod 4)` to an odd exponent. Reduction modulo `p` would give a square root of `-1 mod p`, impossible.

Therefore the unit group is partitioned into disjoint two-element pairs

\[
\{r,-r^{-1}\}.
\]

## Theorem

If `K` has no divisor

\[
d\equiv-1\pmod u,
\]

then `R_u(K)` contains at most one member of every involution pair. Consequently

\[
\boxed{|R_u(K)|\le \frac{\varphi(u)}2.}
\]

Equivalently,

\[
\boxed{|R_u(K)|>\frac{\varphi(u)}2
\Longrightarrow
\exists d\mid K:\ d\equiv-1\pmod u.}
\]

### Proof

If both `r` and `-r^{-1}` occurred in `R_u(K)`, there would be prime divisors `q1,q2|K` with

\[
q_1\equiv r,\qquad q_2\equiv-r^{-1}\pmod u.
\]

The two residue classes are distinct because the involution has no fixed points, so the corresponding prime divisors can be chosen as distinct prime factors. Hence `q1*q2 | K` and

\[
q_1q_2\equiv-1\pmod u,
\]

contradicting failure of the untwisted unit-partner branch.

## Twisted analogue

For the target

\[
t=-n^{-1}\pmod u,
\]

use

\[
\iota_t(r)=t r^{-1}.
\]

If the congruence

\[
r^2\equiv t\pmod u
\]

has no unit solution, then the same argument gives

\[
|R_u(K)|\le\frac{\varphi(u)}2
\]

whenever the twisted unit-partner branch fails.

For prime `u == 3 (mod 4)`, `t=-n^{-1}` is a quadratic nonresidue exactly when `n` is a quadratic residue modulo `u`.

## Research implication

Unit-partner failure at a fixed shift forces all prime factors of the linear form

\[
K_u=(n+u)/4
\]

into at most half of the available unit residue classes. This is the local input expected of a half-dimensional upper-bound sieve. The remaining analytic task is to combine these restrictions across several varying shifts while correctly treating the finitely many collision primes dividing differences between the linear forms.
