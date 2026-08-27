import Mathlib

open Nat legendreSym

-- Proof 1 ✅
theorem neg_one_qnr_mod_4_3 (p : ℕ) [Fact p.Prime] (hp : p % 4 = 3) :
    ¬ IsSquare (-1 : ZMod p) := by
  intro h_sq
  have h : p % 4 ≠ 3 := ZMod.exists_sq_eq_neg_one_iff.mp h_sq
  exact absurd hp h

-- Proof 2 ✅
theorem qr_times_qnr_is_qnr (p : ℕ) [Fact p.Prime] (a b : ℤ)
    (ha : legendreSym p a = 1) (hb : legendreSym p b = -1) :
    legendreSym p (a * b) = -1 := by
  rw [legendreSym.mul, ha, hb]
  ring

-- Proof 3 ✅
theorem four_is_square_mod_p (p : ℕ) [Fact p.Prime] (hp : p > 2) :
    IsSquare (4 : ZMod p) := by
  use 2
  show (4 : ZMod p) = 2 * 2
  push_cast
  ring

-- Proof 4 ✅
theorem legendre_four_eq_one (u : ℕ) [Fact u.Prime] (hu : u > 2) :
    legendreSym u 4 = 1 := by
  have h4eq : (4 : ℤ) = (2 : ℤ) ^ 2 := by norm_num
  rw [h4eq]
  apply sq_one'
  have h2ne0 : ((2 : ℤ) : ZMod u) ≠ 0 := by
    intro h
    have hdvd : (u : ℤ) ∣ (2 : ℤ) :=
      (ZMod.intCast_zmod_eq_zero_iff_dvd (2 : ℤ) u).mp h
    have hfact : u.Prime := Fact.out
    -- u ∣ 2 and u > 2 is impossible
    have hle : (u : ℤ) ≤ 2 := Int.le_of_dvd (by positivity) hdvd
    omega
  exact h2ne0

-- Proof 5 ✅
theorem nqr_inheritance (u : ℕ) [Fact u.Prime] (hu : u > 2)
    (n : ℤ) (hn_qnr : legendreSym u n = -1) :
    legendreSym u (4 * n) = -1 := by
  rw [legendreSym.mul, legendre_four_eq_one u hu, hn_qnr]
  ring

-- Proof 6 ✅
theorem neg_n_qnr (u : ℕ) [Fact u.Prime] (hu3 : u % 4 = 3) (n : ℤ)
    (hn_qr : legendreSym u n = 1) :
    legendreSym u (-n) = -1 := by
  rw [legendreSym.at_neg (show u ≠ 2 from by omega), hn_qr]
  have hchi : ZMod.χ₄ u = -1 := ZMod.χ₄_nat_three_mod_four hu3
  rw [hchi]
  ring

-- Proof 7 ✅
theorem neg_four_n_qnr (u : ℕ) [Fact u.Prime] (hu3 : u % 4 = 3) (hu2 : u > 2)
    (n : ℤ) (hn_qr : legendreSym u n = 1) :
    legendreSym u (-4 * n) = -1 := by
  rw [legendreSym.mul]
  have h_neg4 : legendreSym u (-4) = -1 := by
    rw [legendreSym.at_neg (show u ≠ 2 from by omega)]
    have hchi : ZMod.χ₄ u = -1 := ZMod.χ₄_nat_three_mod_four hu3
    have h4 := legendre_four_eq_one u hu2
    rw [hchi, h4]
    ring
  rw [h_neg4, hn_qr]
  ring
