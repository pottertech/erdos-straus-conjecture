import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas
import ErdosStrausLean.Obstruction

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

theorem n_qr_mod_7_of_n_eq_1 (n : ℕ) (hn7 : n % 7 = 1) :
    legendreSym 7 (n : ℤ) = 1 := by
  rw [legendreSym.mod (p := 7) (n : ℤ)]
  have h7 : ↑(7 : ℕ) = (7 : ℤ) := rfl
  rw [h7]
  have h : (n : ℤ) % 7 = ↑(n % 7) := Int.natCast_mod n 7
  rw [h, hn7]
  show legendreSym 7 ((1 : ℕ) : ℤ) = 1
  exact legendreSym.at_one 7

theorem two_qr_mod_7 : legendreSym 7 (2 : ℤ) = 1 := by
  have hne0 : ((2 : ℤ) : ZMod 7) ≠ 0 := by decide
  exact (legendreSym.eq_one_iff (p := 7) hne0).mpr ⟨3, by decide⟩

theorem x_qr_mod_7 (n : ℕ) (hn7 : n % 7 = 1) (hn12 : n ≡ 1 [MOD 12]) :
    legendreSym 7 ((n + 7) / 4 : ℤ) = 1 := by
  rw [legendreSym.mod (p := 7) ((n + 7) / 4 : ℤ)]
  have h7 : ↑(7 : ℕ) = (7 : ℤ) := rfl
  rw [h7]
  have hval : ((n + 7) / 4 : ℤ) % 7 = 2 := by
    have hn7_int : (n : ℤ) % 7 = 1 := by
      have h := Int.natCast_mod n 7
      have h7eq : ↑(7 : ℕ) = (7 : ℤ) := rfl
      rw [h7eq] at h
      rw [← h, hn7]; push_cast
    have hn4_int : (n : ℤ) % 4 = 1 := by
      have hn_mod4 : n % 4 = 1 := by
        have h12 : n % 12 = 1 := hn12
        have : n % 12 % 4 = n % 4 := by
          have : 12 = 4 * 3 := by norm_num
          rw [this]; exact Nat.mod_mul_right_mod n 4 3
        omega
      have h := Int.natCast_mod n 4
      have h4eq : ↑(4 : ℕ) = (4 : ℤ) := rfl
      rw [h4eq] at h
      rw [← h, hn_mod4]; push_cast
    have hnp7_mod7 : ((n : ℤ) + 7) % 7 = 1 := by omega
    have hnp7_mod4 : ((n : ℤ) + 7) % 4 = 0 := by omega
    have h4dvd : (4 : ℤ) ∣ ((n : ℤ) + 7) := Int.dvd_iff_emod_eq_zero.mpr hnp7_mod4
    have hx4_eq : ((n : ℤ) + 7) / 4 * 4 = (n : ℤ) + 7 := Int.ediv_mul_cancel h4dvd
    have hx4_mod7 : (((n : ℤ) + 7) / 4 * 4) % 7 = 1 := by
      rw [hx4_eq]; exact hnp7_mod7
    have h42_mod7 : (4 * 2 : ℤ) % 7 = 1 := by norm_num
    have hdiff : (((n : ℤ) + 7) / 4 * 4 - (4 * 2 : ℤ)) % 7 = 0 := by
      rw [Int.sub_emod, hx4_mod7, h42_mod7]
      norm_num
    have hfac : (((n : ℤ) + 7) / 4 - 2) * 4 = ((n : ℤ) + 7) / 4 * 4 - (4 * 2 : ℤ) := by ring
    have hprod_mod7 : ((((n : ℤ) + 7) / 4 - 2) * 4) % 7 = 0 := by
      rw [hfac]; exact hdiff
    -- Key: (x-2)*4 ≡ 0 mod 7. Since 4 is invertible mod 7 (4*2=8≡1),
    -- x-2 ≡ 0 mod 7, so x ≡ 2 mod 7.
    -- Use: x*4 ≡ 1 mod 7 (from hx4_mod7) and 2*4 ≡ 1 mod 7 (from h42_mod7)
    -- So x*4 ≡ 2*4 mod 7, and since 4 is invertible, x ≡ 2 mod 7.
    -- In Lean: (x*4 - 2*4) % 7 = 0 → (x - 2)*4 % 7 = 0
    -- And 4 % 7 = 4 ≠ 0, and 7 is prime → x-2 ≡ 0 mod 7
    -- Use Int.mul_emod and check by exhaustion
    rw [Int.mul_emod] at hprod_mod7
    have h4mod7 : (4 : ℤ) % 7 = 4 := by norm_num
    rw [h4mod7] at hprod_mod7
    -- hprod_mod7 : (((x-2) % 7) * 4) % 7 = 0
    -- Let r = (x-2) % 7. r ∈ {0,...,6}. r*4 % 7 = 0 only when r = 0.
    -- When r = 0: x-2 ≡ 0 mod 7 → x ≡ 2 mod 7 ✅
    -- When r ∈ {1,...,6}: r*4 % 7 ∈ {4,1,5,2,6,3} ≠ 0 → contradiction
    set r := (((n : ℤ) + 7) / 4 - 2) % 7
    have hr_nonneg : 0 ≤ r := Int.emod_nonneg _ (by norm_num)
    have hr_lt : r < 7 := Int.emod_lt _ (by norm_num : (7 : ℤ) ≠ 0)
    -- r * 4 % 7 = 0
    have hr_prod : (r * 4) % 7 = 0 := hprod_mod7
    -- Check: r must be 0
    have hr_zero : r = 0 := by
      omega
    -- x ≡ 2 mod 7
    have : ((n : ℤ) + 7) / 4 % 7 = (r + 2) % 7 := by
      have : ((n : ℤ) + 7) / 4 = (((n : ℤ) + 7) / 4 - 2) + 2 := by omega
      rw [this, Int.add_emod, hr_zero]
      norm_num
    exact this
  rw [hval]
  exact two_qr_mod_7
