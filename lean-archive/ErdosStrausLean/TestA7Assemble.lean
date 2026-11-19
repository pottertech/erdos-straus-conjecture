import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.UMethod
import ErdosStrausLean.StructuralLemmas
import ErdosStrausLean.Obstruction

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

-- n is QR mod 7 when n % 7 = 1
theorem n_qr_mod_7_of_n_eq_1 (n : ℕ) (hn7 : n % 7 = 1) :
    legendreSym 7 (n : ℤ) = 1 := by
  rw [legendreSym.mod (p := 7) (n : ℤ)]
  -- Goal: legendreSym 7 (↑n % ↑7) = 1
  -- ↑7 = (7 : ℤ), and Int.natCast_mod gives ↑n % 7 = ↑(n % 7)
  -- The issue is ↑7 vs 7 in the goal. They should be defequal.
  have h7 : ↑(7 : ℕ) = (7 : ℤ) := rfl
  rw [h7]
  have h : (n : ℤ) % 7 = ↑(n % 7) := Int.natCast_mod n 7
  rw [h, hn7]
  show legendreSym 7 (1 : ℤ) = 1
  exact legendreSym.at_one 7
