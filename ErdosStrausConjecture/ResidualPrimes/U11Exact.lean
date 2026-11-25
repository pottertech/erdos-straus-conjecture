import Mathlib

/-!
# Residual Prime Structure: the u­11 layer arithmetic (Paper 2, R3 flagship)

Two machine-checked facts behind EXPERIMENT_LOG E-004/E-005:

1. **The 5-divisor identity.** For `p ≡ 4 (mod 5)` with `4 ∣ p + 11`, the
   span parameter `x = (p + 11)/4` satisfies `5 ∣ x`.

2. **The 5-window never reaches −1 mod 11.** The powers of 5 in `ZMod 11`
   cycle through `{1, 5, 3, 4, 9}` (period 5; 5 is a quadratic residue mod
   11 with `5^5 = 1`), so `5^t ≠ −1` for every `t : ℕ`. The isolated
   5-window `{5^t : |t| ≤ e}` therefore never reaches `−1 = 10`,
   independently of `e ≥ 0`.

Self-contained Mathlib; no project axioms.
-/

namespace ResidualPrimes

/-- With `4 ∣ p + 11` and `p ≡ 4 (mod 5)`, the span parameter
`x = (p + 11)/4` is divisible by 5. -/
theorem five_divides_x (p : ℕ) (h4 : 4 ∣ p + 11) (h5 : (p : ZMod 5) = 4) :
    (((p + 11) / 4 : ℕ) : ZMod 5) = 0 := by
  have hq0 : (p + 11) / 4 * 4 = p + 11 := Nat.div_mul_cancel h4
  have hunit : (((4 : ℕ)) : ZMod 5) * (((4 : ℕ)) : ZMod 5) = (1 : ZMod 5) := by
    decide
  calc (((p + 11) / 4 : ℕ) : ZMod 5)
      = (((p + 11) / 4 : ℕ) : ZMod 5) * (1 : ZMod 5) := by rw [mul_one]
    _ = (((p + 11) / 4 : ℕ) : ZMod 5) *
          ((((4 : ℕ)) : ZMod 5) * (((4 : ℕ)) : ZMod 5)) := by rw [hunit]
    _ = ((((p + 11) / 4 : ℕ) : ZMod 5) * (((4 : ℕ)) : ZMod 5)) *
          (((4 : ℕ)) : ZMod 5) := by ring
    _ = ((p + 11 : ℕ) : ZMod 5) * (((4 : ℕ)) : ZMod 5) := by
        rw [← Nat.cast_mul, hq0]
    _ = (0 : ZMod 5) := by rw [Nat.cast_add, h5]; decide

/-- Every power of 5 in `ZMod 11` differs from `−1`. -/
theorem five_pow_ne_neg_one (t : ℕ) : (5 : ZMod 11) ^ t ≠ (-1 : ZMod 11) := by
  have h5 : (5 : ZMod 11) ^ 5 = (1 : ZMod 11) := by decide
  obtain ⟨k, r, hr, hlt⟩ : ∃ k r, 5 * k + r = t ∧ r < 5 :=
    ⟨t / 5, t % 5, Nat.div_add_mod t 5, Nat.mod_lt t (by norm_num)⟩
  subst hr
  rw [pow_add, pow_mul 5 5 k, h5, one_pow, one_mul]
  interval_cases r <;> decide


/-- With `4 ∣ p + 7` and `p ≡ 3 (mod 5)`, the span parameter
`x = (p + 7)/4` is divisible by 5 (the u = 7 layer's identity, E-007). -/
theorem five_divides_x_u7 (p : ℕ) (h4 : 4 ∣ p + 7) (h5 : (p : ZMod 5) = 3) :
    (((p + 7) / 4 : ℕ) : ZMod 5) = 0 := by
  have hq0 : (p + 7) / 4 * 4 = p + 7 := Nat.div_mul_cancel h4
  have hunit : (((4 : ℕ)) : ZMod 5) * (((4 : ℕ)) : ZMod 5) = (1 : ZMod 5) := by
    decide
  calc (((p + 7) / 4 : ℕ) : ZMod 5)
      = (((p + 7) / 4 : ℕ) : ZMod 5) * (1 : ZMod 5) := by rw [mul_one]
    _ = (((p + 7) / 4 : ℕ) : ZMod 5) *
          ((((4 : ℕ)) : ZMod 5) * (((4 : ℕ)) : ZMod 5)) := by rw [hunit]
    _ = ((((p + 7) / 4 : ℕ) : ZMod 5) * (((4 : ℕ)) : ZMod 5)) *
          (((4 : ℕ)) : ZMod 5) := by ring
    _ = ((p + 7 : ℕ) : ZMod 5) * (((4 : ℕ)) : ZMod 5) := by
        rw [← Nat.cast_mul, hq0]
    _ = (0 : ZMod 5) := by rw [Nat.cast_add, h5]; decide

/-- `5³ ≡ −1 (mod 7)`: in the u = 7 layer the 5-orbit reaches ∑ at
depth 3, in contrast with the u = 11 case where the 5-window never reaches
− (E-007). -/
theorem five_pow_three_eq_neg_one_mod_seven : (5 : ZMod 7) ^ 3 = (-1 : ZMod 7) := by
  decide

end ResidualPrimes
