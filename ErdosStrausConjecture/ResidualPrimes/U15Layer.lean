/-
Copyright (c) 2026 Potter's Quill research. All rights reserved.
Released under the research contract of the residual-primes program.
-/
import ErdosStrausConjecture.ResidualPrimes.U11Layer

/-!
# The u = 15 layer (the first squarefree-composite parameter)

The census facts for `u = 15 = 3 · 5` (E-029 through E-032, the composite
extension of the u = 11 program). This module formalizes the admissibility
side: for `4·x = p + 15` with `p` prime above 5, both `x` and `M = p·x` are
coprime to 15, so every hard-case record is admissible at the composite
layer — the E-029 census row `inad = 0` as a theorem. The residue transfer
`x ≡ 4·p (mod 15)` is included as the structural glue.
-/

namespace ResidualPrimes

/-- The 3-divisibility transfer: `4·x = p + 15` with `3 ∣ x` forces `3 ∣ p`
(`4x ≡ p` mod 3 because both 4 and 15 reduce to the identity mod 3). -/
theorem u15_x_mod3_of_dvd (p x : ℕ) (hx : 4 * x = p + 15) (h3 : x % 3 = 0) :
    p % 3 = 0 := by omega

/-- The 5-divisibility transfer: `4·x = p + 15` with `5 ∣ x` forces `5 ∣ p`
(`4x ≡ p + 15 ≡ p` mod 5). -/
theorem u15_x_mod5_of_dvd (p x : ℕ) (hx : 4 * x = p + 15) (h5 : x % 5 = 0) :
    p % 5 = 0 := by omega

/-- The residue glue: `4·x = p + 15` gives `x ≡ 4·p (mod 15)` (`4` is its own
inverse mod 15). -/
theorem u15_x_residue (p x : ℕ) (hx : 4 * x = p + 15) :
    x % 15 = (4 * p) % 15 := by omega

/-- **The u = 15 admissibility (E-029, `inad = 0` as a theorem).** For
`4·x = p + 15` with `p` prime and `p > 5`, `x` is coprime to 15: any prime
`q` dividing both `x` and 15 is 3 or 5, and the divisibility transfers to
`p` (above), contradicting primality at `p > 5`. -/
theorem u15_x_coprime (p x : ℕ) (hnp : Nat.Prime p) (hgt : 5 < p)
    (hx : 4 * x = p + 15) : Nat.Coprime x 15 := by
  have h3n : ¬ (3 ∣ p) := by
    intro hd
    rcases hnp.eq_one_or_self_of_dvd 3 hd with h | h
    · omega
    · omega
  have h5n : ¬ (5 ∣ p) := by
    intro hd
    rcases hnp.eq_one_or_self_of_dvd 5 hd with h | h
    · omega
    · omega
  have c3 : Nat.Coprime 3 x := by
    refine (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr ?_
    intro hd
    have hm : p % 3 = 0 := u15_x_mod3_of_dvd p x hx (Nat.mod_eq_zero_of_dvd hd)
    exact h3n (Nat.dvd_of_mod_eq_zero hm)
  have c5 : Nat.Coprime 5 x := by
    refine (Nat.Prime.coprime_iff_not_dvd Nat.prime_five).mpr ?_
    intro hd
    have hm : p % 5 = 0 := u15_x_mod5_of_dvd p x hx (Nat.mod_eq_zero_of_dvd hd)
    exact h5n (Nat.dvd_of_mod_eq_zero hm)
  exact (Nat.coprime_mul_iff_right).mpr ⟨Nat.coprime_comm.mp c3,
    Nat.coprime_comm.mp c5⟩

/-- **The composite-layer admissibility of M (E-031, the pair-group side).**
`M = p·x` is coprime to 15 - both factors individually (the p-classes are
themselves units in the CRT pair group `(Z/3)* x (Z/5)*`, the seat of the
E-031 algebra). -/
theorem u15_m_coprime (p x : ℕ) (hnp : Nat.Prime p) (hgt : 5 < p)
    (hx : 4 * x = p + 15) : Nat.Coprime (p * x) 15 := by
  have h1c : Nat.Coprime x 15 := u15_x_coprime p x hnp hgt hx
  have h3n : ¬ (3 ∣ p) := by
    intro hd
    rcases hnp.eq_one_or_self_of_dvd 3 hd with h | h
    · omega
    · omega
  have h5n : ¬ (5 ∣ p) := by
    intro hd
    rcases hnp.eq_one_or_self_of_dvd 5 hd with h | h
    · omega
    · omega
  have c3p : Nat.Coprime 3 p := by
    refine (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr ?_
    intro hd
    rcases hnp.eq_one_or_self_of_dvd 3 hd with h | h
    · omega
    · omega
  have c5p : Nat.Coprime 5 p := by
    refine (Nat.Prime.coprime_iff_not_dvd Nat.prime_five).mpr ?_
    intro hd
    rcases hnp.eq_one_or_self_of_dvd 5 hd with h | h
    · omega
    · omega
  have hpc : Nat.Coprime p 15 :=
    (Nat.coprime_mul_iff_right).mpr ⟨Nat.coprime_comm.mp c3p,
      Nat.coprime_comm.mp c5p⟩
  exact Nat.Coprime.mul_left hpc h1c

end ResidualPrimes
