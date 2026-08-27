import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

-- QR ≠ QNR mod 7 ✅
theorem qr_ne_qnr_mod_p (a b : ℤ) (ha : legendreSym 7 a = 1) (hb : legendreSym 7 b = -1) :
    a % 7 ≠ b % 7 := by
  intro h
  have hmod_a : legendreSym 7 a = legendreSym 7 (a % 7) := legendreSym.mod (p := 7) a
  have hmod_b : legendreSym 7 b = legendreSym 7 (b % 7) := legendreSym.mod (p := 7) b
  -- From ha: legendreSym 7 (a % 7) = 1
  rw [hmod_a] at ha
  -- From hb: legendreSym 7 (b % 7) = -1
  rw [hmod_b] at hb
  -- But a % 7 = b % 7
  rw [h] at ha
  -- ha : legendreSym 7 (b % 7) = 1, hb : legendreSym 7 (b % 7) = -1
  rw [hb] at ha
  norm_num at ha

-- No QR divisor can match a QNR target ✅
theorem no_qr_divisor_matches_qnr_target (D : ℕ) (target : ℤ)
    (h_all_qr : ∀ d : ℕ, d ∣ D → d ≥ 1 → legendreSym 7 (d : ℤ) = 1)
    (h_target_qnr : legendreSym 7 target = -1) :
    ¬ ∃ d : ℕ, d ∣ D ∧ d ≥ 1 ∧ (d : ℤ) % 7 = target % 7 := by
  intro ⟨d, hdvd, hdpos, hdmod⟩
  have hqr_d := h_all_qr d hdvd hdpos
  exact qr_ne_qnr_mod_p (d : ℤ) target hqr_d h_target_qnr hdmod
