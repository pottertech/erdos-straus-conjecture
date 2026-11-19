import Mathlib

example : (7 : ℕ).Prime := by norm_num
example : Fact (7 : ℕ).Prime := ⟨by norm_num⟩
