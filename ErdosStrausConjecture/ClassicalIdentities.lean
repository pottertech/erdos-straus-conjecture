import ErdosStrausConjecture.Basic

namespace ErdosStrausConjecture

-- Classical modular identities used to reduce the prime problem to the
-- six residue classes 1,121,169,289,361,529 (mod 840).
-- This module is intentionally not imported by the root module yet; compile
-- it independently first in the repository's Lean 4.30 environment.

-- n = 8k + 5
-- (x,y,z) = ((n+3)/4, n(n+3)/8, n(n+3)/4)
theorem mod_8_five (n : ℕ) (hn : n ≥ 5) (hmod : n % 8 = 5) :
    IsErdosStraus n := by
  set k := n / 8
  have hn_eq : n = 8 * k + 5 := by omega
  refine ⟨2 * k + 2,
          (8 * k + 5) * (k + 1),
          2 * (8 * k + 5) * (k + 1), ?_, ?_, ?_, ?_⟩
  · omega
  · exact Nat.mul_pos (by omega) (by omega)
  · positivity
  · rw [hn_eq]
    ring

-- Residual n ≡ 1 (mod 3), n ≡ 2 (mod 5) gives n ≡ 7 (mod 15).
-- n = 15k + 7
theorem mod_15_seven (n : ℕ) (hn : n ≥ 7) (hmod : n % 15 = 7) :
    IsErdosStraus n := by
  set k := n / 15
  have hn_eq : n = 15 * k + 7 := by omega
  refine ⟨4 * k + 2,
          4 * (15 * k + 7),
          4 * (15 * k + 7) * (2 * k + 1), ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · positivity
  · rw [hn_eq]
    ring

-- Residual n ≡ 1 (mod 3), n ≡ 3 (mod 5) gives n ≡ 13 (mod 15).
-- n = 15k + 13
theorem mod_15_thirteen (n : ℕ) (hn : n ≥ 13) (hmod : n % 15 = 13) :
    IsErdosStraus n := by
  set k := n / 15
  have hn_eq : n = 15 * k + 13 := by omega
  refine ⟨4 * k + 4,
          4 * (15 * k + 13),
          2 * (15 * k + 13) * (k + 1), ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · positivity
  · rw [hn_eq]
    ring

-- n = 7k + 3
-- Correct third denominator has the factor 2.
theorem mod_7_three (n : ℕ) (hn : n ≥ 3) (hmod : n % 7 = 3) :
    IsErdosStraus n := by
  set k := n / 7
  have hn_eq : n = 7 * k + 3 := by omega
  refine ⟨2 * k + 1,
          2 * (7 * k + 3),
          2 * (7 * k + 3) * (2 * k + 1), ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · positivity
  · rw [hn_eq]
    ring

-- n = 7k + 5
theorem mod_7_five (n : ℕ) (hn : n ≥ 5) (hmod : n % 7 = 5) :
    IsErdosStraus n := by
  set k := n / 7
  have hn_eq : n = 7 * k + 5 := by omega
  refine ⟨2 * k + 2,
          2 * (7 * k + 5),
          (7 * k + 5) * (k + 1), ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · exact Nat.mul_pos (by omega) (by omega)
  · rw [hn_eq]
    ring

-- n = 7k + 6
theorem mod_7_six (n : ℕ) (hn : n ≥ 6) (hmod : n % 7 = 6) :
    IsErdosStraus n := by
  set k := n / 7
  have hn_eq : n = 7 * k + 6 := by omega
  refine ⟨2 * k + 2,
          2 * (7 * k + 6),
          2 * (7 * k + 6) * (k + 1), ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · positivity
  · rw [hn_eq]
    ring

-- A particularly simple known progression recovered independently from the
-- centered u=7 analysis: n ≡ 13 (mod 20).
-- n = 20k + 13, with
-- x = (n+7)/4 = 5k+5,
-- y = n(3n+1)/4 = n(15k+10),
-- z = (n+7)(3n+1)/80 = 5(k+1)(3k+2).
theorem mod_20_thirteen (n : ℕ) (hn : n ≥ 13) (hmod : n % 20 = 13) :
    IsErdosStraus n := by
  set k := n / 20
  have hn_eq : n = 20 * k + 13 := by omega
  refine ⟨5 * k + 5,
          (20 * k + 13) * (15 * k + 10),
          5 * (k + 1) * (3 * k + 2), ?_, ?_, ?_, ?_⟩
  · omega
  · positivity
  · positivity
  · rw [hn_eq]
    ring

end ErdosStrausConjecture
