# lean-archive — retired 2026-11-18

Two parallel Lean projects retired in favor of the maintained root
formalization `ErdosStrausConjecture/` (Lean/Mathlib v4.30.0). Their content is
preserved as-is for the historical record; do not build from these directories
or cite their results.

- **ErdosStrausLean/** — Lean 4.33.1 "Test*" exploration project. Contains 8
  unfinished `sorry` proof terms (TestFactor 1, TestXqrFinal 3, Chebotarev 1,
  Omega3 3) while its `LEAN_PROGRESS.md` claims "0 sorrys / 0 admits" — the
  census contradicts the log. Its exploratory results that matter were
  superseded by `OmegaCases.lean` and `StructuralLemmas.lean` in the root
  project.
- **ErdosStraus/** — older mini-project (one module with 1 `sorry`, stub
  README).

The census above was verified on 2026-11-18 by line-based counting of actual
`sorry`/`admit` proof terms (comments excluded).
