import Mathlib

open Nat

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

-- Test: what does ZMod.χ₄ 7 look like in context?
example (n : ℤ) (hn : true) : legendreSym 7 (-n) = -1 → True := by
  intro h
  trivial

-- Test: χ₄ with Nat vs Int
example : ZMod.χ₄ (7 : ℕ) = -1 := by
  exact ZMod.χ₄_nat_three_mod_four (by norm_num : (7 : ℕ) % 4 = 3)

-- Test: does χ₄ work with Int 7?
example : ZMod.χ₄ (↑(7 : ℕ) : ℤ) = -1 := by
  have h := ZMod.χ₄_nat_three_mod_four (by norm_num : (7 : ℕ) % 4 = 3)
  -- h : ZMod.χ₄ (7 : ℕ) = -1
  -- Need: ZMod.χ₄ (↑7 : ℤ) = -1
  -- These should be defequal since χ₄ takes ℕ and ↑7 = 7
  exact h
