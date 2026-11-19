# v10 Submission Status

**Date:** 2026-08-31

## Current manuscript

`paper/composite_exact_typeii_depths_v10.tex`

This supersedes v9 for eventual arXiv/journal submission. v9 remains the short draft already sent to external reviewers.

## What changed from v9

1. The complete prime Type-II square coordinate is now proved explicitly from Pomerance--Weingartner Corollary 2.4.
2. The canonical no-reuse theorem is now proved in the manuscript in all four classes `s mod 8`; it no longer says only "proof idea" or depends on a GitHub side note.
3. The reinforced `s == 1 (mod 8)` witness is retained:

   `d_s = 2^(v2(s-1)-3) (s-1)`.
4. The finite-exception and double-Dirichlet steps are stated explicitly.
5. The corrected finite-certificate bound remains

   `liminf N_infty(X) log X / X >= 3.0353080580213976...`.

## Verification completed

- internal adversarial proof audit of the repaired fixed-cofactor chain;
- explicit `k=0` no-reuse repair;
- one-million cofactor regression/certificate;
- primary-source equivalence audit against Pomerance--Weingartner;
- targeted priority searches against Elsholtz--Tao, Pomerance--Weingartner, Dahan, and public FCF/CENTL exact-depth/square-completion material;
- external review requests sent to Christian Elsholtz and Carl Pomerance.

## External-review status

- Christian Elsholtz: v9 sent; no reply recorded as of this status note.
- Carl Pomerance: v9 sent to current Dartmouth faculty address; no reply recorded as of this status note.

Do not interpret silence as approval.

## Remaining gates before arXiv

1. Compile `v10` from the exact committed source and visually inspect the resulting PDF.
2. Run one final line-by-line mathematical audit of the newly inlined no-reuse proof, especially the congruence lower bounds for `a,b` in the four cases.
3. Integrate any external reviewer corrections if they arrive before submission.
4. Freeze title, abstract, MSC codes, keywords, bibliography, and source archive.
5. Re-run the priority search immediately before posting.

## Remaining gates before journal submission

In addition to the arXiv gates:

- choose target journal (current first choice: Acta Arithmetica);
- adapt formatting only if required by the journal;
- use the conservative cover letter in `COVER_LETTER_DRAFT.md`;
- cite the arXiv identifier after posting;
- preserve the claim boundary: exact square-completed Type-II depth, not universal Type-II and not the full Erdos--Straus conjecture.

## Current publication assessment

The paper is now structurally self-contained enough for serious external review. The two largest remaining uncertainties are external correctness review and historical priority, not missing computational evidence.