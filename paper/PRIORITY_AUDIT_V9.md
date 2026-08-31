# Priority Audit for v9 Fixed-Cofactor Hierarchy

**Date:** 2026-08-31

**Status:** targeted literature comparison. A negative search is not proof of novelty or priority.

## Candidate contribution under review

The current v9 manuscript studies the exact first-hit depth

\[
\delta_{\rm sq}(p)=\min\{A\ge1:\exists D\mid A^2,\ 4A-1\mid p+4D\}
\]

in the classical divisor-square coordinate for prime Type-II Erdős--Straus solutions.

The main candidate contribution is the fixed-prime-cofactor hierarchy:

- fix a prime cofactor `s>3`;
- choose an explicit witness `d_s` and an explicit progression for a variable prime `r`;
- put `A=(sr+1)/4`;
- use a single nonsquare target coordinate at `r` to eliminate all earlier layers not divisible by `r`;
- reduce every remaining collision at an earlier modulus `cr` to

\[
r(kh-dc^2)+k+dh-2dc=0;
\]

- handle the degenerate `k=0` divisor-reuse case separately;
- conclude that only finitely many parameter primes `r` are bad for each fixed `s`, and that all remaining parameters produce exact depth `A` for infinitely many prime denominators.

## Strongly overlapping prior mathematics

The following ingredients are **not** claimed as new:

1. The divisor-square Type-II coordinate `D|A^2`, `4A-1 | p+4D` is classical and belongs to the Thépault/Mordell/Mizony lineage. The CENTL prior-art audit explicitly identifies the same coordinate and its divisor-complement equivalence.
2. Complete Type-I/Type-II descriptions and modern parametrizations are available in Elsholtz--Tao and Pomerance--Weingartner.
3. Quadratic reciprocity, Jacobi-character obstructions, Dirichlet, PNT in progressions, Bombieri--Vinogradov, and half-dimensional sieve machinery are standard/prior inputs.
4. Current FCF/CENTL work already contains extensive exact-depth, square-completion, Legendre/Jacobi-signature, ancestry, shadow, survivor, and finite CRT realization machinery.

## Closest current neighboring results

### FCF/CENTL exact-depth program

The current CENTL `DIAMOND.md` framework proves that for a **fixed admissible exact-depth candidate**, exact realization can be reduced to finitely many forbidden residue classes in a CRT parameter; an avoiding reduced class then gives infinitely many prime realizations by Dirichlet.

This is methodologically close to v9, but the object quantified over is different. The v9 claim is a uniform-in-parameter statement for each fixed cofactor `s`: all but finitely many variable-prime parameters in a canonical progression work. The current targeted search has not located that exact theorem in CENTL's public notes.

CENTL also has external-nonresidue, fixed-shift, square-lift, and signature machinery. These should be cited/discussed as close conceptual antecedents.

### Benjamin Dahan (2026)

Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035, studies explicit search depth and exceptional sets for prime inputs. The paper proves fixed-depth sieve bounds and a two-sided obstruction at a fixed shift `c=7`; it does not, in the portions checked, state an exact-first-hit fixed-cofactor theorem of the v9 form with target modulus `sr` and finitely many bad variable-prime parameters.

Dahan explicitly relates recent parametrizations to one common divisor-based search space, so v9 should avoid novelty claims about parametrization itself.

### Pomerance--Weingartner (2026)

Their Type-II criteria and results on exceptions to the generalized Erdős--Straus--Schinzel equation provide modern structural context. Their results emphasize that universal Type-II coverage is a stronger and generally false phenomenon in generalized settings. Nothing located in the targeted pass gives the v9 fixed-prime-cofactor exact-depth hierarchy.

## Search signatures used

Targeted searches included combinations of:

- `Erdos Straus exact depth fixed cofactor Type II`
- `Erdos Straus fixed cofactor variable prime`
- `Erdos Straus finite exception Type II exact depth`
- `4A-1 exact depth Erdős Straus`
- `square completion fixed shift prime parameter`
- `all but finitely many prime parameters Erdős Straus`

The searches were run against general web/arXiv-indexed material and current public CENTL/FCF notes.

## Current priority conclusion

**Encouraging but not dispositive.** The targeted search found substantial overlap in local machinery and exact-depth methodology, but did **not** locate the exact theorem:

> for every fixed prime cofactor `s>3`, an explicit variable-prime progression has only finitely many exceptional parameters, with exact first-hit Type-II depths `A=(sr+1)/4` realized by infinitely many primes for all remaining parameters.

Nor did it locate the specific master-equation/no-reuse synthesis used in v9.

This should be described in the paper only as a **candidate contribution** pending external expert review. Do not use words such as "first", "new", or "novel" in the title/abstract unless a referee or a much broader literature audit supports them.

## Publication-facing claim boundary

Safe wording:

- "We prove a fixed-prime-cofactor finite-exception theorem in the exact square-completed Type-II depth spectrum."
- "The divisor-square parametrization and local quadratic tools are classical/prior; the contribution is the exact-first-hit synthesis and hierarchy theorem."
- "Targeted searches did not locate an equivalent statement; this does not establish priority."

Unsafe wording at present:

- "first proof"
- "new parametrization"
- "novel Type-II criterion"
- any implication that the Erdős--Straus conjecture or universal Type-II solvability is proved.
