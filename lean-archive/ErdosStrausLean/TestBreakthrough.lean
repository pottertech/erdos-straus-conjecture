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

theorem qr_prod_of_qr_factors (a b : ℕ)
    (hqr_a : legendreSym 7 (a : ℤ) = 1) (hqr_b : legendreSym 7 (b : ℤ) = 1) :
    legendreSym 7 ((a * b : ℕ) : ℤ) = 1 := by
  have h : ((a * b : ℕ) : ℤ) = (a : ℤ) * (b : ℤ) := Int.cast_mul a b
  rw [h, legendreSym.mul, hqr_a, hqr_b]; ring

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
      have hge2 : m.minFac ≥ 2 := hpr.two_le
      have hqr_p : legendreSym 7 (m.minFac : ℤ) = 1 := hqr m.minFac hpr hdvd
      have hlt : m / m.minFac < m := Nat.div_lt_self (by omega) (by omega)
      have hfac : m = m.minFac * (m / m.minFac) := by
        have h1 : m = m / m.minFac * m.minFac := (Nat.div_mul_cancel hdvd).symm
        exact mul_comm (m / m.minFac) m.minFac ▸ h1
      have hqr_rest : ∀ q : ℕ, q.Prime → q ∣ (m / m.minFac) → legendreSym 7 (q : ℤ) = 1 := by
        intro q qpr qdvd
        apply hqr q qpr
        rw [hfac]
        exact dvd_mul_of_dvd_right qdvd m.minFac
      -- Use Nat.div_pos instead of omega to avoid coercion issues
      have hrest_pos : m / m.minFac ≥ 1 := by
        have h1 : m / m.minFac * m.minFac = m := Nat.div_mul_cancel hdvd
        have hm_pos : m > 0 := by omega
        have hmf_pos : m.minFac > 0 := by omega
        -- If m/minFac = 0, then 0 * minFac = m → m = 0, contradiction
        have : m / m.minFac ≠ 0 := by
          intro h0
          rw [h0, zero_mul] at h1
          exact absurd h1 (Ne.symm (ne_of_gt hm_pos))
        exact Nat.pos_iff_ne_zero.mpr this
      have hih := ih (m / m.minFac) hlt hrest_pos hqr_rest
      rw [hfac]
      exact qr_prod_of_qr_factors m.minFac (m / m.minFac) hqr_p hih
