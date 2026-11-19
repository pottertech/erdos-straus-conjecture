import Mathlib
import ErdosStrausConjecture.Basic

-- STATUS (2026-11-19): compiles on the pinned toolchain (Lean/Mathlib
-- v4.30.0); included in the CI build set. A 2026-11-18 note had recorded a
-- false witness in `example_73` (Lean's `decide` rejected it, correctly:
-- 4·20·263·51180 ≠ 73·(20·263 + 20·51180 + 263·51180)). It was replaced with
-- the verified witness 4/73 = 1/20 + 1/210 + 1/30660 (checked with exact
-- Fraction arithmetic before the edit). The two unused Burgess axioms that
-- were declared here were removed on 2026-11-19: unproven analytic inputs
-- belong in the completed paper route (ROADMAP.md #2), not as dead Lean
-- axioms.

namespace ErdosStrausConjecture

-- ============================================
-- COMPUTATIONAL EXAMPLES (rfl-proven)
-- ============================================

theorem example_13 : IsErdosStraus 13 := by
  refine ⟨4, 18, 468, Nat.succ_pos 3, Nat.succ_pos 17, Nat.succ_pos 467, ?_⟩
  rfl

theorem example_37 : IsErdosStraus 37 := by
  refine ⟨10, 124, 22940, Nat.succ_pos 9, Nat.succ_pos 123, Nat.succ_pos 22939, ?_⟩
  rfl

theorem example_61 : IsErdosStraus 61 := by
  refine ⟨16, 326, 159088, Nat.succ_pos 15, Nat.succ_pos 325, Nat.succ_pos 159087, ?_⟩
  rfl

theorem example_73 : IsErdosStraus 73 := by
  refine ⟨20, 210, 30660, Nat.succ_pos 19, Nat.succ_pos 209, Nat.succ_pos 30659, ?_⟩
  rfl

-- ============================================
-- THEOREM 2: n ≡ 5 (mod 8) → A = 3 works
--
-- Construction: x = (n+3)/4, P = 2, y = (2 + nx)/3, z = ((nx)²/2 + nx)/3
-- Key facts:
--   - n ≡ 5 (mod 8) → n + 3 ≡ 0 (mod 8) → x = (n+3)/4 is even
--   - 2 | x → 2 | nx → P = 2 divides (nx)²
--   - nx ≡ 1 (mod 3) always:
--     If n ≡ 1 (mod 3): x = (n+3)/4 ≡ 1·1 = 1 (mod 3), nx ≡ 1 (mod 3)
--     If n ≡ 2 (mod 3): x = (n+3)/4 ≡ 2·2 = 4 ≡ 1 (mod 3), nx ≡ 2·2 = 1 (mod 3)
--   - 3 | (2 + nx) since nx ≡ 1 → 2 + nx ≡ 0 (mod 3)
--   - 3 | (nx²/2 + nx) since nx/2 + 1 ≡ 2 + 1 = 0 (mod 3)
-- ============================================

-- theorem2 (n ≡ 5 mod 8 → A = 3) is fully proven in CenteredEquivalence.lean
-- This file previously contained a duplicate stub with sorry; it has been removed.
-- The proven version uses linear_combination + Int.ofNat_inj (Zify strategy).

-- Note (2026-11-19): the two axiomatic Burgess statements (`C_burgess`,
-- `burgess_least_qnr_bound`) that were previously declared here were removed:
-- they were unused by every theorem in the project, and unproven analytic
-- inputs have no place in the certified build (see ROADMAP.md #2 — their
-- home is the completed conditional paper).

end ErdosStrausConjecture