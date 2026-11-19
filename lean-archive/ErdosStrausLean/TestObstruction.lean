import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩
instance : Fact (11 : ℕ).Prime := ⟨by norm_num⟩

-- QNR facts mod 7 ✅
theorem five_is_qnr_mod_7 : legendreSym 7 (5 : ℤ) = -1 := by
  rw [legendreSym.eq_neg_one_iff]; exact by decide

theorem three_is_qnr_mod_7 : legendreSym 7 (3 : ℤ) = -1 := by
  rw [legendreSym.eq_neg_one_iff]; exact by decide

theorem six_is_qnr_mod_7 : legendreSym 7 (6 : ℤ) = -1 := by
  rw [legendreSym.eq_neg_one_iff]; exact by decide

-- QR facts mod 7 ✅
theorem one_is_qr_mod_7 : legendreSym 7 (1 : ℤ) = 1 := legendreSym.at_one 7

theorem two_is_qr_mod_7 : legendreSym 7 (2 : ℤ) = 1 := by
  have hne0 : ((2 : ℤ) : ZMod 7) ≠ 0 := by decide
  apply (legendreSym.eq_one_iff (p := 7) hne0).mpr
  use 3
  show ((3 : ℤ) : ZMod 7) ^ 2 = 2
  decide

theorem four_is_qr_mod_7 : legendreSym 7 (4 : ℤ) = 1 := by
  have hne0 : ((4 : ℤ) : ZMod 7) ≠ 0 := by decide
  apply (legendreSym.eq_one_iff (p := 7) hne0).mpr
  use 2
  show ((2 : ℤ) : ZMod 7) ^ 2 = 4
  decide

-- QNR facts mod 11 ✅
theorem two_is_qnr_mod_11 : legendreSym 11 (2 : ℤ) = -1 := by
  rw [legendreSym.eq_neg_one_iff]; exact by decide

-- QR facts mod 11 ✅
theorem one_is_qr_mod_11 : legendreSym 11 (1 : ℤ) = 1 := legendreSym.at_one 11

theorem three_is_qr_mod_11 : legendreSym 11 (3 : ℤ) = 1 := by
  have hne0 : ((3 : ℤ) : ZMod 11) ≠ 0 := by decide
  apply (legendreSym.eq_one_iff (p := 11) hne0).mpr
  use 5
  show ((5 : ℤ) : ZMod 11) ^ 2 = 3
  decide

theorem four_is_qr_mod_11 : legendreSym 11 (4 : ℤ) = 1 := by
  have hne0 : ((4 : ℤ) : ZMod 11) ≠ 0 := by decide
  apply (legendreSym.eq_one_iff (p := 11) hne0).mpr
  use 2
  show ((2 : ℤ) : ZMod 11) ^ 2 = 4
  decide

theorem five_is_qr_mod_11 : legendreSym 11 (5 : ℤ) = 1 := by
  have hne0 : ((5 : ℤ) : ZMod 11) ≠ 0 := by decide
  apply (legendreSym.eq_one_iff (p := 11) hne0).mpr
  use 4
  show ((4 : ℤ) : ZMod 11) ^ 2 = 5
  decide

theorem nine_is_qr_mod_11 : legendreSym 11 (9 : ℤ) = 1 := by
  have hne0 : ((9 : ℤ) : ZMod 11) ≠ 0 := by decide
  apply (legendreSym.eq_one_iff (p := 11) hne0).mpr
  use 3
  show ((3 : ℤ) : ZMod 11) ^ 2 = 9
  decide
