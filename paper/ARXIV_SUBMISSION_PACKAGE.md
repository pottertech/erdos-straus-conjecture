# arXiv / Journal Submission Package for v9

**Current manuscript:** `paper/composite_exact_typeii_depths_v9.tex`

**Current reviewer PDF:** `Skip_Potter_Prime_Cofactor_Hierarchies_v9.pdf`

**Status:** publication-preparation checklist. Do not submit until the external proof review has been considered or the author explicitly chooses to submit before receiving it.

## Proposed title

**Prime-Cofactor Hierarchies in the Exact Type-II Erdős--Straus Depth Spectrum**

## Author

Skip Potter

## Proposed arXiv category

Primary: `math.NT` (Number Theory)

## Suggested abstract

For primes `p ≡ 1 (mod 4)`, define the square-completion depth to be the least positive integer `A` for which there is a divisor `D | A^2` satisfying `4A-1 | p+4D`. This is a classical coordinate for prime Type-II Erdős--Straus solutions; the paper studies exact first occurrence rather than the parametrization itself.

Every depth trap has Jacobi sign `-1`, and a parity-vector calculation identifies the prime and `3q` target moduli as the first occurrences of new global Jacobi-character directions. We then introduce a finer fixed-cofactor construction. When the target has one nonsquare variable-prime coordinate, all earlier layers not containing that prime are eliminated simultaneously. Collisions in the remaining layers satisfy a fixed Diophantine equation, while a separate divisor-reuse lemma handles the degenerate case. This proves that for every fixed prime cofactor `s>3`, an explicit progression of variable primes `r` has only finitely many exceptional parameters; for every remaining parameter, `A=(sr+1)/4` occurs as exact square-completion depth for infinitely many primes.

The resulting convergent hierarchy gives an explicit lower bound for the number of depth values realized infinitely often. A finite certificate using fixed prime cofactors `s<=10^6` yields

`liminf_{X->infinity} N_infty(X) log X / X >= 3.0353080580213976...`.

The result concerns the exact Type-II depth spectrum and does not prove universal Type-II solvability or the Erdős--Straus conjecture.

## Suggested keywords

- Erdős--Straus conjecture
- Egyptian fractions
- Type-II solutions
- exact depth
- quadratic reciprocity
- arithmetic progressions
- Diophantine equations

## Suggested MSC 2020 codes

- **11D68** — Diophantine equations (general)
- **11A07** — Congruences; primitive roots; residue systems
- **11N13** — Primes in progressions

MSC codes should be verified against the journal/arXiv interface before final submission.

## Files to include in a minimal arXiv source bundle

Required:

- `composite_exact_typeii_depths_v9.tex`

Recommended supporting files in a separate repository / supplementary archive rather than the arXiv TeX bundle:

- `V9_REFEREE_AUDIT.md`
- `CANONICAL_NO_REUSE_LEMMA.md`
- repaired fixed-cofactor theorem notes
- hierarchy constant calculator and one-million certificate
- reduced `A=649` and `A=22339` verifiers

The arXiv paper should remain short and symbolic; large computational artifacts should be linked as reproducibility material.

## Pre-submission verification gates

- [x] v9 compiles without LaTeX errors.
- [x] PDF visually inspected page by page.
- [x] No unresolved references reported in the local build.
- [x] Internal adversarial proof audit completed after the `k=0` repair.
- [x] Current numeric coefficient recomputed after the repaired `s ≡ 1 (mod 8)` witness.
- [x] Targeted priority search recorded in `PRIORITY_AUDIT_V9.md`.
- [x] Current manuscript sent to Christian Elsholtz for adversarial review.
- [ ] External mathematical feedback received and addressed.
- [ ] Bibliography checked against DOI/journal metadata line by line.
- [ ] Final wording of Proposition 1 (complete prime Type-II coordinate) cross-checked against a primary source.
- [ ] Decide whether to place the one-million certificate in a permanent DOI archive (Zenodo or similar) before journal submission.
- [ ] Add final arXiv identifier / DOI to repository after posting.

## Journal strategy

The paper is currently short, focused, and number-theoretic. A reasonable journal target should accept concise analytic/elementary number theory notes. Journal selection should be made only after external feedback clarifies perceived novelty and strength.

Potential classes of venues to investigate:

- specialized number theory journals;
- journals accepting short communications / notes;
- broader elementary/Diophantine number theory venues if the contribution is judged primarily structural.

Do not select a journal based only on speed; match the paper's novelty and depth after external review.

## Submission statement / claim boundary

The cover letter and abstract should explicitly state:

1. the divisor-square coordinate is prior mathematics;
2. local quadratic/Jacobi tools have substantial antecedents;
3. the paper's claimed contribution is the exact-first-hit fixed-cofactor finite-exception synthesis;
4. the work does not prove the Erdős--Straus conjecture.
