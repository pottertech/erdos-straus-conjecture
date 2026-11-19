# Multi-Shift Unit-Partner Sieve Audit

**Status:** rigorous proof skeleton reduced to a standard upper-bound sieve theorem; citation-level analytic audit still required before journal-style theorem status

This note separates the elementary part of the multi-shift argument from the single standard analytic input.

## 1. Fixed finite set of shifts

Let `U` be a fixed finite set of distinct positive integers

\[
u\equiv3\pmod4.
\]

For prime `n == 1 (mod 4)`, define

\[
K_u(n)=\frac{n+u}{4}.
\]

Suppose the untwisted unit-partner branch fails for every `u in U`:

\[
\nexists d\mid K_u(n):\quad d\equiv-1\pmod u.
\]

By the exact half-group lemma, for each `u` the residue classes occupied by prime divisors of `K_u(n)` lie in some independent set for `r -> -r^{-1}`. Enlarging if necessary, they lie in a set

\[
A_u\subseteq(\mathbb Z/u\mathbb Z)^\times,
\qquad |A_u|=\varphi(u)/2.
\]

There are finitely many such choices for fixed `u`.

Let

\[
B_u=(\mathbb Z/u\mathbb Z)^\times\setminus A_u.
\]

Then every prime divisor `q` of `K_u(n)` must satisfy

\[
q\bmod u\notin B_u.
\]

## 2. Residues removed modulo a sieving prime

Since `4K_u(n)=n+u`, an odd prime `q` divides `K_u(n)` exactly when

\[
n\equiv-u\pmod q.
\]

For a prime `q` outside the finite set dividing the shifts or their pairwise differences, the residue classes

\[
0,-u_1,-u_2,\ldots
\]

are pairwise distinct modulo `q`.

For a fixed tuple `(A_u)`, define

\[
\rho(q)=1+\#\{u\in U:q\bmod u\in B_u\}.
\]

The first removed residue is `n == 0 (mod q)` (the primality sieve); the remaining terms remove `n == -u (mod q)` whenever `q` belongs to the forbidden half of the unit classes modulo `u`.

## 3. Dimension calculation

For each fixed `u`, the prime number theorem in arithmetic progressions gives

\[
\sum_{\substack{q\le z\\ q\bmod u\in B_u}}
\frac{\log q}{q}
=
\frac{|B_u|}{\varphi(u)}\log z+O_u(1)
=
\frac12\log z+O_u(1).
\]

Also

\[
\sum_{q\le z}\frac{\log q}{q}=\log z+O(1).
\]

Therefore

\[
\sum_{q\le z}\frac{\rho(q)\log q}{q}
=
\left(1+\frac{|U|}{2}\right)\log z+O_U(1).
\]

Thus the local system has sieve dimension

\[
\boxed{\kappa=1+|U|/2.}
\]

The finitely many collision primes change only the implied constant.

## 4. Standard analytic input needed

A standard Selberg/Rosser upper-bound sieve for a finite-dimensional residue-class system with the above dimension estimate yields

\[
\#E_{U,(A_u)}(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
\]

Summing over the finitely many independent-set tuples `(A_u)` preserves the exponent:

\[
\boxed{
E_U(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
}
\]

The remaining audit task is not algebraic: it is to attach this step to a precise published upper-bound-sieve theorem with hypotheses written in the same normalization and verify the local product condition term-by-term.

## 5. Relation to Dahan 2026

Benjamin Dahan proves the same dimension-addition mechanism for a broader fixed finite witness system. In the introduction to arXiv:2608.24035, his Theorem 4.3 is summarized as

\[
|E_{\mathcal P}(N)|\ll_{\mathcal P}N(\log N)^{-1-|\mathcal P|/2},
\]

and Lemma 4.2 is described as the same fixed-point-free involution `x -> -x^{-1}` giving the half-unit-group obstruction.

That strongly supports the present calculation, but this repository should not claim that Dahan's theorem literally specializes to the unit-partner system until the parameter mapping is written explicitly.

## 6. Twisted branch

The twisted target is `-n^{-1}`. By `TWISTED_UNIT_PARTNER_OBSTRUCTION.md`, at prime shift `u == 3 (mod 4)` the twisted pairing is fixed-point-free exactly when `(n/u)=+1`.

Therefore one may add a second half-dimensional local restriction only on those `n`-residue classes where the target is a nonsquare. A full two-branch sieve must stratify by the Legendre/Jacobi profile of `n` across the chosen shifts; it is incorrect to double the dimension uniformly.

## 7. Current rigorous status

The following pieces are exact:

1. the untwisted half-group lemma;
2. the twisted fixed-point criterion;
3. the collision lemma for distinct shifted linear forms;
4. the dimension calculation above, assuming a fixed tuple of allowed half-sets.

The remaining task before theorem status is a citation-level verification of the standard upper-bound sieve application and, for the two-branch version, a residue-profile stratification of the twisted fixed-point cases.
