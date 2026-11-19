# arXiv Metadata for v10

**Manuscript:** `paper/composite_exact_typeii_depths_v10.tex`

## Title

Prime-Cofactor Hierarchies in the Exact Type-II Erdos--Straus Depth Spectrum

## Author

Skip Potter

## Primary arXiv category

`math.NT` (Number Theory)

## Suggested MSC 2020 codes

- 11D68 — Rational numbers as sums of fractions
- 11N36 — Applications of sieve methods
- 11A15 — Power residues, reciprocity
- 11P82 — Unitary and Egyptian fractions

Use `11D68` as the primary MSC code if a single primary code is requested.

## Keywords

Erdos--Straus conjecture; Egyptian fractions; Type-II solutions; exact depth; quadratic reciprocity; Chinese remainder theorem; sieve methods; arithmetic progressions.

## Abstract

For primes $p\equiv1\pmod4$, define
\[
\delta_{\rm sq}(p)=\min\{A\ge1:\exists D\mid A^2,\ 4A-1\mid p+4D\},
\]
the first-hit depth in a classical divisor-square coordinate for prime Type-II Erdos--Straus solutions. We study its exact-depth spectrum. Every depth-$B$ trap residue has Jacobi sign $-1$ modulo $4B-1$, and the first new global Jacobi-character directions occur only at prime target moduli and at target moduli $3q$. We then introduce a finer fixed-cofactor mechanism. For every fixed prime cofactor $s>3$, explicit congruence data produce, apart from finitely many variable-prime parameters $r$, exact depths $A=(sr+1)/4$ realized by infinitely many primes. The remaining earlier collisions reduce to a finite Diophantine equation
\[
r(kh-dc^2)+k+dh-2dc=0,
\]
with a separate no-reuse argument excluding the degenerate case $k=0$. The resulting convergent hierarchy gives
\[
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}\ge\frac83+C_{\rm all},
\]
where $N_\infty(X)$ counts exact depth values realized by infinitely many primes. A finite certificate using fixed prime cofactors $s\le10^6$ yields the explicit bound $3.0353080580213\ldots$. These results concern exact Type-II depth and do not prove universal Type-II solvability or the Erdos--Straus conjecture.

## Comments field

Self-contained manuscript. The divisor-square Type-II coordinate and standard analytic/reciprocity tools are treated as prior work. The candidate contribution is the fixed-cofactor finite-exception exact-depth mechanism and the resulting prime-cofactor hierarchy. Computational certificates and supporting scripts are available in the accompanying repository but are not required for the main hierarchy theorem.

## Source files for arXiv freeze

Minimum source set:

- `composite_exact_typeii_depths_v10.tex`

No external figures are required.

Recommended supporting archive outside the arXiv source bundle:

- `TYPEII_COORDINATE_PRIMARY_SOURCE_AUDIT.md`
- `CANONICAL_NO_REUSE_LEMMA.md`
- `V10_INLINE_PROOF_AUDIT.md`
- `hierarchy_constant_certificate.py`
- exact finite-computation/certificate scripts for the repository supplement.

## Claim boundary to preserve

Do **not** use any of the following in the arXiv title, abstract, comments, or announcement:

- "proof of the Erdos--Straus conjecture";
- "all primes are Type II";
- "universal Type-II solvability";
- "new parametrization" for the divisor-square coordinate.

Preferred description:

> new structure in the exact first-hit Type-II depth spectrum, with an unconditional fixed-prime-cofactor hierarchy.

## Pre-submission gates

Before upload:

1. compile the exact committed v10 source;
2. visually inspect every page;
3. make the small `u_0=1 => s=3` exposition edit noted in `V10_INLINE_PROOF_AUDIT.md`;
4. re-run the priority search;
5. check for replies from Elsholtz and Pomerance;
6. freeze a versioned PDF/source checksum.