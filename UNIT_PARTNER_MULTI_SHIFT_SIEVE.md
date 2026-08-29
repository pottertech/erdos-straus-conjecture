# Multi-Shift Half-Dimensional Sieve for the Untwisted Unit-Partner Branch

**Status:** unconditional density theorem at fixed finite shift set, using standard upper-bound sieve machinery; not a proof of the Erdős--Straus conjecture

This note records the analytic consequence of `UNIT_PARTNER_HALF_GROUP_LEMMA.md`.

No priority is claimed for the sieve mechanism. Benjamin Dahan's August 2026 preprint proves an exact sieve-dimension theorem for a broader fixed-depth Erdős--Straus search and uses the same fixed-point-free involution idea. The statement below isolates the simpler untwisted unit-partner slice in the notation of this repository.

## Setup

Let `U` be a fixed finite set of distinct positive integers

\[
u\equiv3\pmod4.
\]

For prime `n == 1 (mod 4)` and `u in U`, put

\[
K_u(n)=\frac{n+u}{4}.
\]

Let `E_U(N)` be the primes `n <= N`, excluding the finitely many primes dividing a member of `U`, for which **every** shift `u in U` fails the untwisted unit-partner condition

\[
\exists d\mid K_u(n):\qquad d\equiv-1\pmod u.
\]

## Local structure of failure

By the half-group lemma, failure at a fixed `u` implies that the distinct residue classes modulo `u` occupied by prime factors of `K_u(n)` lie in an independent set for

\[
r\mapsto-r^{-1}.
\]

Extend that independent set, if necessary, by choosing one member from each involution pair. Thus all prime factors of `K_u(n)` lie in one of finitely many sets

\[
A_u\subseteq(\mathbb Z/u\mathbb Z)^\times,
\qquad |A_u|=\varphi(u)/2.
\]

There are only finitely many possible choices of `A_u`, depending on `u` alone.

For a fixed tuple `(A_u)_{u in U}`, define the complementary forbidden residue sets

\[
B_u=(\mathbb Z/u\mathbb Z)^\times\setminus A_u,
\qquad |B_u|=\varphi(u)/2.
\]

Then failure requires

\[
q\mid K_u(n)\Longrightarrow q\bmod u\notin B_u
\]

for every prime divisor `q` of `K_u(n)`.

## Collision lemma for the shifted linear forms

For distinct `u,v in U`, if an odd prime `q` divides both `K_u(n)` and `K_v(n)`, then

\[
q\mid K_u(n)-K_v(n)=\frac{u-v}{4},
\]

and therefore

\[
q\mid u-v.
\]

Hence outside the finite set of primes dividing

\[
\Delta_U=\prod_{u\ne v}(u-v)\prod_{u\in U}u,
\]

a prime `q` can divide at most one of the shifted forms at any one residue class `n mod q`.

## Sieve dimension

For a prime `q` outside the finite exceptional set, the sieve removes:

1. the residue `n == 0 (mod q)` to enforce primality of `n`;
2. for each `u in U` with `q mod u in B_u`, the residue
   \[
   n\equiv-u\pmod q,
   \]
   because this would make `q|K_u(n)` with a forbidden factor residue.

The removed residues are distinct outside the collision primes.

By Dirichlet equidistribution of primes among the reduced residue classes modulo each fixed `u`, the mean contribution of the `u`-th forbidden set is

\[
\frac{|B_u|}{\varphi(u)}=\frac12.
\]

Thus the total sieve dimension is

\[
\boxed{\kappa=1+\frac{|U|}{2}.}
\]

Applying a standard Selberg/upper-bound sieve to each fixed tuple `(A_u)` gives

\[
\#E_{U,(A_u)}(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
\]

There are only finitely many tuples `(A_u)`, with a number depending on `U` alone, so summing over them preserves the exponent.

## Theorem

For every fixed finite set `U` of distinct shifts `u == 3 (mod 4)`,

\[
\boxed{
|E_U(N)|
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
}
\]

The estimate is unconditional for fixed `U`, modulo the standard cited upper-bound-sieve theorem and prime number theorem in fixed arithmetic progressions used in the dimension calculation.

## What this proves and does not prove

This proves that a finite collection of untwisted unit-partner shifts leaves an exceptional set of primes of arbitrarily strong logarithmic sparsity as more fixed shifts are added.

It does **not** prove that the exceptional set is finite or empty. The implied constant depends on `U`, and a fixed finite shift collection can still have infinitely many blind primes. Dahan's fixed-shift obstruction at `u=7` is a concrete warning of exactly this phenomenon.

The verified computation through `10^9` is stronger in a different direction: allowing both untwisted and twisted unit-partner branches over `u <= 299` leaves only the explicit integer `2521` in the corrected residual population. Turning that observation into a universal theorem requires control beyond fixed-`U` density decay.
