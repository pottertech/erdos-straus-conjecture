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
  -- Use the fact that in Z/7Z: x*4 = 1 and 2*4 = 1, so x = 2
  -- Prove (x-2) % 7 = 0 by showing (x-2)*4 ≡ 0 mod 7 and using that 4 is invertible
  have h4dvd : (4 : ℤ) ∣ ((n : ℤ) + 7) := by
    have hn4 : n % 4 = 1 := by
      have h12 : n % 12 = 1 := hn12
      have : n % 12 % 4 = n % 4 := by
        have : 12 = 4 * 3 := by norm_num
        rw [this]; exact Nat.mod_mul_right_mod n 4 3
      omega
    have hnp4 : ((n : ℤ) + 7) % 4 = 0 := by omega
    exact Int.dvd_iff_emod_eq_zero.mpr hnp4
  have hdiv : ((n : ℤ) + 7) / 4 * 4 = (n : ℤ) + 7 := Int.ediv_mul_cancel h4dvd
  have hn7_int : (n : ℤ) % 7 = 1 := by
    have h := Int.natCast_mod n 7
    have h7eq : ↑(7 : ℕ) = (7 : ℤ) := rfl
    rw [h7eq] at h
    rw [← h, hn7]; push_cast
  -- (x*4) % 7 = (n+7) % 7 = 1
  have hx4_mod7 : (((n : ℤ) + 7) / 4 * 4) % 7 = 1 := by
    rw [hdiv, show ((n : ℤ) + 7) % 7 = 1 from by omega]
  -- (2*4) % 7 = 1
  have h24_mod7 : (2 * 4 : ℤ) % 7 = 1 := by norm_num
  -- (x*4 - 2*4) % 7 = 0
  have hdiff_mod7 : (((n : ℤ) + 7) / 4 * 4 - 2 * 4) % 7 = 0 := by
    rw [Int.sub_emod, hx4_mod7, h24_mod7]; norm_num
  -- (x - 2) * 4 ≡ 0 mod 7
  have hfac : (((n : ℤ) + 7) / 4 - 2) * 4 = ((n : ℤ) + 7) / 4 * 4 - 2 * 4 := by ring
  have hprod_mod7 : ((((n : ℤ) + 7) / 4 - 2) * 4) % 7 = 0 := by rw [hfac]; exact hdiff_mod7
  -- 7 | (x-2)*4, and gcd(7,4) = 1, so 7 | (x-2)
  have h7dvd : (7 : ℤ) ∣ (((n : ℤ) + 7) / 4 - 2) * 4 := Int.dvd_iff_emod_eq_zero.mpr hprod_mod7
  -- Use Int.dvd_gcd or manual: 7 | 4*(x-2), 7 is prime, 7 ∤ 4 → 7 | (x-2)
  -- Actually, simplest: use Nat.Coprime.dvd_of_dvd_mul_right on the Nat version
  have h7dvd_nat : (7 : ℕ) ∣ (4 : ℕ) * Int.natAbs (((n : ℤ) + 7) / 4 - 2) := by
    sorry
  have hcoprime : Nat.Coprime 7 4 := by norm_num
  have h7dvd_x2_nat : (7 : ℕ) ∣ Int.natAbs (((n : ℤ) + 7) / 4 - 2) := by
    sorry
  have h7dvd_x2 : (7 : ℤ) ∣ (((n : ℤ) + 7) / 4 - 2) := by
    sorry
  have hval : ((n + 7) / 4 : ℤ) % 7 = 2 := by
    have : (((n : ℤ) + 7) / 4 - 2) % 7 = 0 := Int.emod_eq_zero_of_dvd h7dvd_x2
    omega
  rw [hval]
  exact two_qr_mod_7
