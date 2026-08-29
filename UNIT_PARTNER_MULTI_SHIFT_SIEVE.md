# Multi-Shift Half-Dimensional Sieve for the Untwisted Unit-Partner Branch

**Status:** analytic proposition / proof template; exact local lemma proved, global upper-bound-sieve step pending citation-level audit

This note records the proposed analytic consequence of `UNIT_PARTNER_HALF_GROUP_LEMMA.md`.

No priority is claimed for the sieve mechanism. Benjamin Dahan's August 2026 preprint proves an exact sieve-dimension theorem for a broader fixed-depth Erdős--Straus search and uses the same fixed-point-free involution idea. The statement below isolates the simpler untwisted unit-partner slice in the notation of this repository. Before publication, the upper-bound-sieve hypotheses and the precise correspondence with Dahan's theorem must be checked line by line.

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

## Exact local structure of failure

By the proved half-group lemma, failure at a fixed `u` implies that the distinct residue classes modulo `u` occupied by prime factors of `K_u(n)` lie in an independent set for

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

## Exact collision lemma for the shifted linear forms

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

## Proposed sieve dimension

For a prime `q` outside the finite exceptional set, the intended sieve removes:

1. the residue `n == 0 (mod q)` to enforce primality of `n`;
2. for each `u in U` with `q mod u in B_u`, the residue
   \[
   n\equiv-u\pmod q,
   \]
   because this would make `q|K_u(n)` with a forbidden factor residue.

The removed residues are distinct outside the collision primes.

By Dirichlet equidistribution of primes among the reduced residue classes modulo each fixed `u`, the expected/standard dimension contribution of the `u`-th forbidden set is

\[
\frac{|B_u|}{\varphi(u)}=\frac12.
\]

This leads to the candidate total sieve dimension

\[
\boxed{\kappa=1+\frac{|U|}{2}.}
\]

A standard Selberg/upper-bound-sieve application should then give, for each fixed tuple `(A_u)`,

\[
\#E_{U,(A_u)}(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}},
\]

and summing over the finitely many tuples should preserve the exponent.

## Proposition to audit

The intended final statement is

\[
\boxed{
|E_U(N)|
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
}
\]

The local half-group and collision lemmas above are proved exactly. The remaining task is to cite or reproduce an upper-bound-sieve theorem with hypotheses matching the residue-removal function here and verify the required Mertens/prime-in-progressions average uniformly for the fixed moduli involved.

## What it would prove and what it would not prove

Once the analytic audit is completed, the proposition would show that a finite collection of untwisted unit-partner shifts leaves an exceptional set of primes of arbitrarily strong logarithmic sparsity as more fixed shifts are added.

It would **not** prove that the exceptional set is finite or empty. The implied constant depends on `U`, and a fixed finite shift collection can still have infinitely many blind primes. Dahan's fixed-shift obstruction at `u=7` is a concrete warning of exactly this phenomenon.

The verified computation through `10^9` is stronger in a different direction: allowing both untwisted and twisted unit-partner branches over `u <= 299` leaves only the explicit integer `2521` in the corrected residual population. Turning that observation into a universal theorem requires control beyond fixed-`U` density decay.
