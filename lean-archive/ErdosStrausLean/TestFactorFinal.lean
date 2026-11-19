import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

theorem legendre_mul_eq_one (a b : ℤ)
    (ha : legendreSym 7 a = 1) (hb : legendreSym 7 b = 1) :
    legendreSym 7 (a * b) = 1 := by
  rw [legendreSym.mul, ha, hb]; ring

theorem legendre_pow_eq_one (p : ℤ) (k : ℕ) (hqr : legendreSym 7 p = 1) :
    legendreSym 7 (p ^ k) = 1 := by
  induction k with
  | zero => norm_num
  | succ k ih => rw [pow_succ, legendreSym.mul, ih, hqr]; ring

-- Product of two QR naturals is QR (using push_cast to normalize)
theorem qr_prod_of_qr_factors (a b : ℕ)
    (hqr_a : legendreSym 7 (a : ℤ) = 1) (hqr_b : legendreSym 7 (b : ℤ) = 1) :
    legendreSym 7 ((a * b : ℕ) : ℤ) = 1 := by
  push_cast [legendreSym.mul, hqr_a, hqr_b]
  ring

-- Strong induction: all prime factors QR → m is QR
theorem all_qr_factors_implies_qr : ∀ m : ℕ, m ≥ 1 →
    (∀ p : ℕ, p.Prime → p ∣ m → legendreSym 7 (p : ℤ) = 1) →
    legendreSym 7 (m : ℤ) = 1 := by
  intro m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    intro hm hqr
    by_cases hm1 : m = 1
    · rw [hm1]; exact legendreSym.at_one 7
    · have hm2 : m ≥ 2 := by omega
      have hdvd : m.minFac ∣ m := Nat.minFac_dvd m
      have hpr : m.minFac.Prime := Nat.minFac_prime (by omega)
      have hqr_p : legendreSym 7 (m.minFac : ℤ) = 1 := hqr m.minFac hpr hdvd
      have hlt : m / m.minFac < m := Nat.div_lt_self (by omega) (by omega)
      have hqr_rest : ∀ q : ℕ, q.Prime → q ∣ (m / m.minFac) → legendreSym 7 (q : ℤ) = 1 := by
        intro q qpr qdvd
        apply hqr q qpr
        have hfac : m = m.minFac * (m / m.minFac) := by
          have := Nat.div_mul_cancel hdvd
          exact (mul_comm _ _ ▸ this : m = _)
        rw [← hfac]
        have hqdvd_mul : q ∣ m.minFac * (m / m.minFac) := by
          apply dvd_mul_of_dvd_right qdvd _
        exact hqdvd_mul
      have hrest_pos : m / m.minFac ≥ 1 := by
        have hfac : m = m.minFac * (m / m.minFac) := by
          have := Nat.div_mul_cancel hdvd
          exact (mul_comm _ _ ▸ this : m = _)
        have hprod : m.minFac * (m / m.minFac) ≥ 2 := by
          rw [← hfac]; exact hm2
        omega
      have hih := ih (m / m.minFac) hlt hrest_pos hqr_rest
      -- Use push_cast to handle the Nat→Int coercion on the product
      have hfac : m = m.minFac * (m / m.minFac) := by
        have := Nat.div_mul_cancel hdvd
        exact (mul_comm _ _ ▸ this : m = _)
      -- push_cast should expand (m : ℤ) = (minFac * (m/minFac) : ℤ) = (minFac : ℤ) * ((m/minFac) : ℤ)
      push_cast [hfac, legendreSym.mul, hqr_p, hih]
      ring
