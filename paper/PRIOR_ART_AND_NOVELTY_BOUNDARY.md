# Prior Art and Novelty Boundary for the Composite Exact-Depth Preprint

**Date:** 2026-08-30

This note records what must be treated as prior mathematics and what remains the candidate contribution of `composite_exact_typeii_depths_v3.tex`.

## Historical divisor-square mechanism

The condition

\[
D\mid A^2,
\qquad
4A-1\mid p+4D
\]

must not be claimed as new.

Mizony and Gardes, *Un point sur la conjecture d'Erdös et Straus* (Université Claude Bernard Lyon 1, December 2012), explicitly discuss a theorem attributed to Léon Thépault from a 1979 letter in *Pour la Science*, no. 19. Their historical formulation states that if positive integers `a,b` satisfy

\[
b\mid a^2
\]

and

\[
4a-1\mid bn+a,
\]

then an Erdős--Straus decomposition exists.

The present square-completed coordinate is equivalent to that divisor-square mechanism after the divisor-complement involution.

Mizony--Gardes also give a direct program which, for prime `p==1 (mod 4)`, searches divisors `d|m^2` and returns the least `m` satisfying

\[
p+4d\equiv0\pmod{4m-1}.
\]

Thus the *minimal square-completion coordinate itself* was already computationally considered in that literature.

## Modern complete Type-II criteria

The standard Type-I/Type-II framework and complete Type-II parametrizations are prior mathematics. Relevant modern sources include:

- Elsholtz--Tao, *Counting the number of solutions to the Erdős--Straus equation on unit fractions*;
- Pomerance--Weingartner, *Exceptions to the Erdős--Straus--Schinzel conjecture*;
- Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n congruent 1 mod 24*.

The preprint must present the square-divisor coordinate as a convenient exact coordinate for standard prime Type II, not as a new Type-II criterion.

## Current 2026 depth-spectrum work

The public FCF/CENTL program already contains:

- a prime-modulus exact-depth backbone;
- structural shadow/gap theorems;
- square-completion trap geometry;
- a finite square-completion census;
- a composite residual/core program;
- explicit warnings that the divisor-square mechanism itself is prior art.

Therefore the claims

> exact depths are unbounded,

> composite exact depths exist,

or

> the square-divisor criterion gives a depth spectrum

are not sufficient novelty claims.

## Candidate contribution of the present preprint

The current candidate contribution is the synthesis proved in the branch:

### 1. Structural composite 3q exact-depth theorem

For prime

\[
q\equiv1\pmod4,
\qquad
A_q=\frac{3q+1}{4},
\]

if `A_q` has a divisor `D|A_q^2` with

\[
D\equiv2\pmod3,
\]

then infinitely many primes have exact square-completion depth `A_q`, with deliberately composite target modulus

\[
4A_q-1=3q.
\]

### 2. Prime-factor criterion

It is enough that `A_q` have a prime divisor

\[
\ell\equiv2\pmod3.
\]

### 3. Density-one theorem

Among primes `q==1 (mod 4)`, the preceding factor condition holds with relative natural density `1`.

### 4. Quantitative lower bound

If `N_comp(X)` counts composite-target depths at most `X` that are realized by infinitely many prime denominators, then

\[
N_{\rm comp}(X)
\ge
\left(\frac23+o(1)\right)\frac{X}{\log X}.
\]

### 5. Fixed-witness families

Every fixed `d==2 (mod 3)`, `3\nmid d`, determines a reduced prime progression in `q` for which `d` is the target witness.

### 6. General finite exact-depth certificate

The CRT reduction of an arbitrary target progression to finitely many forbidden parameter congruences, together with reducedness and Dirichlet, gives a reusable exact-depth certificate theorem.

The certified full-layer examples at `649` and `22339` are best treated as supporting examples/supplementary material rather than the primary novelty claim.

## Priority status

Targeted searches on 2026-08-30 did not locate the exact `3q` structural theorem, density-one result, or `(2/3) X/log X` lower bound in the Erdős--Straus literature reviewed so far.

This is **not** a proof of novelty or publication priority.

Before submission, the bibliography/prior-art review should still include:

1. the original 1979 Thépault letter if obtainable;
2. Rosati and Yamamoto historical parametrizations;
3. Schinzel and Mordell-era literature;
4. non-arXiv French/German literature around divisor-square formulas;
5. the full FCF/CENTL square-completion corpus;
6. recent 2025--2026 Type-II/search-depth papers.

## Safe language for the manuscript

Use:

> We prove the following composite-modulus exact-depth family...

and

> We have not located this exact density statement in the literature reviewed to date.

Do not use:

> This is the first composite exact-depth theorem.

or

> We discovered the square-divisor Type-II criterion.

or

> This proves Erdős--Straus.
