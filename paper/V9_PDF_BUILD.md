# v9 PDF build record

**Source:** `paper/composite_exact_typeii_depths_v9.tex`

**Branch:** `research/short-relation-100m`

**Compiled:** 2026-08-31

**Pages:** 6

**PDF SHA-256:**

`0f9f518c9f24939f5fd2ea767ca294ef84b1136dffad463d0cc899670618f118`

The PDF was built with pdfLaTeX in two passes and visually inspected page-by-page after rasterization. No LaTeX errors, unresolved references, overfull boxes, clipping, overlap, or broken glyphs were found.

The reviewer-ready filename is:

`Skip_Potter_Prime_Cofactor_Hierarchies_v9.pdf`

The exact PDF was sent to Prof. Christian Elsholtz in the existing review-request email thread on 2026-08-31.

## Reproduction

From the repository root:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error composite_exact_typeii_depths_v9.tex
pdflatex -interaction=nonstopmode -halt-on-error composite_exact_typeii_depths_v9.tex
sha256sum composite_exact_typeii_depths_v9.pdf
```

Expected SHA-256 for the reviewed build:

`0f9f518c9f24939f5fd2ea767ca294ef84b1136dffad463d0cc899670618f118`

## Status

The source and build record are versioned on the research branch. Binary PDF upload through the current GitHub connector is not available as a direct local-file operation, so this record preserves the exact reviewed artifact hash until the PDF binary is added through a normal Git checkout or a default-branch-enabled build workflow.
