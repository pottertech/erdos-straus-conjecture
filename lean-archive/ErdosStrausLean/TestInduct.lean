import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

-- Product of two QR numbers is QR ✅
theorem legendre_mul_eq_one (a b : ℤ)
    (ha : legendreSym 7 a = 1) (hb : legendreSym 7 b = 1) :
    legendreSym 7 (a * b) = 1 := by
  rw [legendreSym.mul, ha, hb]; ring

-- p^k is QR when p is QR ✅
theorem legendre_pow_eq_one (p : ℤ) (k : ℕ) (hqr : legendreSym 7 p = 1) :
    legendreSym 7 (p ^ k) = 1 := by
  induction k with
  | zero => norm_num
  | succ k ih => rw [pow_succ, legendreSym.mul, ih, hqr]; ring

-- Key lemma: all prime factors QR → m is QR
theorem all_qr_factors_implies_qr (m : ℕ) (hm : m ≥ 1)
    (h_all_qr : ∀ p : ℕ, p.Prime → p ∣ m → legendreSym 7 (p : ℤ) = 1) :
    legendreSym 7 (m : ℤ) = 1 := by
  have hm0 : m ≠ 0 := ne_of_gt hm
  -- m = ∏ p^(factorization p)
  have hfact : m = m.factorization.prod (fun p e => p ^ e) := by
    exact (Nat.prod_factorization_pow_eq_self hm0).symm
  -- Cast to ℤ
  rw [hfact, Int.cast_prod]
  -- Distribute legendreSym over product
  simp only [legendreSym.hom]
  -- Each factor is 1
  apply Finset.prod_eq_one
  intro p hp
  simp only [legendre_pow_eq_one]
  exact h_all_qr p (Nat.factorization_mem_support.mp hp) (Nat.factorization_dvd_of_mem hp)
