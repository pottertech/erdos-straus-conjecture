# V11 Submission Freeze

**Status:** publication gate closed for the current internal submission candidate.

## Frozen manuscript

- Source: `paper/composite_exact_typeii_depths_v11.tex`
- Source commit: `4fa08c8738e96c8d7fed7dc147f7dfa5540dc056`
- Git blob SHA-1: `82a2945efb44c0858960ea5429d210223860da04`
- Source SHA-256: `6054b499fd009fb33cb8342703c81b1180bdf746ef6aefef5e387a8249528af1`

The local source used for compilation was verified byte-for-byte against the committed Git blob by recomputing the Git blob SHA-1 locally; it matches `82a2945efb44c0858960ea5429d210223860da04` exactly.

## Compiled PDF

- Reviewer/submission filename: `Skip_Potter_Prime_Cofactor_Hierarchies_v11.pdf`
- Pages: 7
- PDF SHA-256: `801e4d1f7df20f1e7dbf553c30936b77a16e2213adc6d1e07f4f852e915dc206`
- Size: 235,737 bytes

## Build verification

Compiled from the exact frozen source with two `pdflatex` passes using `-interaction=nonstopmode -halt-on-error`.

Final pass status:

- no LaTeX errors;
- no unresolved references;
- no overfull boxes;
- no underfull boxes;
- no warning lines returned by the final log filter.

## Visual QA

The 7-page PDF was rendered at 180 dpi and inspected page by page.

Verified:

- no clipping;
- no overlaps;
- no broken equations;
- no missing glyphs;
- table on the canonical prime progressions renders cleanly;
- dense four-case no-reuse proof is readable and remains inside margins;
- references and final claim-boundary section render cleanly.

## Final exposition repair

V11 incorporates the remaining audit clarification in the `s ≡ 3 (mod 8)` no-reuse case:

> Because `s>3`, one has `m>1`, hence `u_0>1`.

This makes explicit why the strict inequality

`16u_0 - 8 > 8u_0`

is valid in that case. The excluded edge case `u_0=1` would force `s=3`.

## Submission boundary

The manuscript is internally frozen as an arXiv/journal submission candidate. The mathematical claim remains restricted to exact square-completed Type-II depth; it does not claim universal Type-II solvability or prove the Erdős--Straus conjecture.

External correctness/priority review from Christian Elsholtz and Carl Pomerance remains pending. A negative literature search is not treated as proof of novelty.
