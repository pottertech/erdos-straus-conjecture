# V6 Scope Correction

In `composite_exact_typeii_depths_v6.tex`, the generic theorem titled **fixed-cofactor finite-exception theorem** should read with `s` assumed **odd and squarefree** (or, more generally, with squarehood required modulo each full prime-power factor of `s`).

The reason is that Legendre-symbol conditions at the distinct primes dividing `s` guarantee a square target modulo `s` only in the squarefree case. The canonical hierarchy theorem immediately following it assumes `s` is prime, so the headline infinite hierarchy, its finite-exception proof, and all counting consequences are unaffected.

The authoritative corrected abstract theorem is `ADMISSIBLE_FIXED_COFACTOR_THEOREM.md` at commit `5aa8082`.

This correction should be folded directly into the next LaTeX version before circulation.