# lean-archive/orphan-modules — retired 2026-11-19

Modules moved out of the maintained root Lean project (`ErdosStrausConjecture/`).
These were **not** part of the root library's import closure and were imported by
no other module, so retirement changes nothing that CI certifies.

- **StructuralLemmas.lean** — 5 unfinished `sorry` proof terms (lines 233-278 in
  the file as archived) and tactic errors on the pinned toolchain (rewrite step
  failures at lines 210/218/220; authored/tested on Lean 4.33.1). Formally
  retired rather than fixed: reviving it means resolving the three rewrite
  breakages under Lean/Mathlib v4.30.0 and completing the five goals — see
  ROADMAP.md #3 for where such lemmas would serve the termination theorem.

Content preserved as-is; do not build from these files or cite them.
