# V11 Submission Freeze

**Status:** publication gate closed for the current internal submission candidate.

## Frozen manuscript

- Source: `paper/composite_exact_typeii_depths_v11.tex`
- Manuscript date: **August 31, 2026**
- Date-update commit: `904c9692c9eef59470895bfceab1ad0f84b3e89f`
- Git blob SHA-1: `34f750585932154dbf545197e8a9955aa7e92f15`
- Source SHA-256: `653e426489d50c45d728ccea0846bf0856b9fb30c271cb3a9194039c632dc8aa`

The local source used for compilation was rebuilt after changing only the manuscript date from `August 2026` to `August 31, 2026`.

## Compiled PDF

- Reviewer/submission filename: `Skip_Potter_Prime_Cofactor_Hierarchies_v11.pdf`
- Pages: 7
- PDF SHA-256: `036d2e2cd77e6c963361033769082e83314c6164377bcbf3cbdcec2e16cb6ebc`
- Size: 236,204 bytes

## Build verification

Compiled from the updated source with two `pdflatex` passes using `-interaction=nonstopmode -halt-on-error`.

Final pass status:

- no LaTeX errors;
- no unresolved references;
- no overfull boxes;
- no underfull boxes;
- no warning lines returned by the final log filter.

## Visual QA

The rebuilt 7-page PDF was rendered and inspected. The title page now displays exactly **August 31, 2026**. The longer date line does not disturb the title block or pagination.

Verified:

- no clipping;
- no overlaps;
- no broken equations;
- no missing glyphs;
- table on the canonical prime progressions renders cleanly;
- dense four-case no-reuse proof remains inside margins;
- references and final claim-boundary section render cleanly.

## Final exposition repair

V11 incorporates the audit clarification in the `s ≡ 3 (mod 8)` no-reuse case:

> Because `s>3`, one has `m>1`, hence `u_0>1`.

This makes explicit why the strict inequality `16u_0 - 8 > 8u_0` is valid in that case.

## Submission boundary

The manuscript is internally frozen as an arXiv/journal submission candidate. The mathematical claim remains restricted to exact square-completed Type-II depth; it does not claim universal Type-II solvability or prove the Erdős--Straus conjecture.

External correctness/priority review from Christian Elsholtz and Carl Pomerance remains pending. A negative literature search is not treated as proof of novelty.
