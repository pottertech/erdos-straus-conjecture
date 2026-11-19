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

-- Key lemma: all prime factors QR → m is QR
-- Use a completely different strategy: instead of rewriting the cast,
-- use the fact that legendreSym is completely multiplicative (MulChar)
-- and use Finset.prod_induction with legendre_mul_eq_one as the step
theorem all_qr_factors_implies_qr (m : ℕ) (hm : m ≥ 1)
    (h_all_qr : ∀ p : ℕ, p.Prime → p ∣ m → legendreSym 7 (p : ℤ) = 1) :
    legendreSym 7 (m : ℤ) = 1 := by
  have hm0 : m ≠ 0 := ne_of_gt hm
  -- Use the factorization product
  have hfact : m = m.factorization.prod (fun p e => p ^ e) :=
    (Nat.prod_factorization_pow_eq_self hm0).symm
  -- Instead of fighting with cast_prod, use a different route:
  -- prove that legendreSym 7 (m : ℤ) = 1 by induction on the factorization
  -- using the fact that legendreSym is multiplicative
  
  -- Actually, let me just use the strong induction approach but with
  -- cleaner handling of the cast. The key insight: if m = a * b in ℕ,
  -- then (m : ℤ) = (a : ℤ) * (b : ℤ), and legendreSym.mul applies.
  
  -- Strong induction on m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    intro hm h_all_qr
    by_cases hm1 : m = 1
    · rw [hm1]; exact legendreSym.at_one 7
    · have hm2 : m ≥ 2 := by omega
      -- Get the smallest prime factor and decompose
      have hdvd : m.minFac ∣ m := Nat.minFac_dvd m
      have hprime : m.minFac.Prime := Nat.minFac_prime (by omega)
      -- Key: m = minFac * (m / minFac), and we can use mul_comm + div_mul_cancel
      have hfac : m = m.minFac * (m / m.minFac) := by
        have h := Nat.div_mul_cancel hdvd
        omega
      -- This won't work because div_mul_cancel gives (m / p) * p = m
      -- and we need p * (m / p) = m
      sorry
