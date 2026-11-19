import Mathlib
import ErdosStrausConjecture.Basic
import ErdosStrausConjecture.MainTheorem

/-!
# Reduction of the full conjecture to the prime class n ≡ 1 (mod 24)

Machine-checks the route-2 reduction:

1. **Scaling lemma.** A solution for `n` lifts to a solution for `n·k`
   (denominators scaled by `k`).

2. **Mod-chain helper.** For `n ≡ 1 (mod 12)` with `n ≢ 1 (mod 24)`, one has
   `n ≡ 5 (mod 8)` — proved by the explicit residues chain 12 ∣ 24, then
   `n ≡ 24·(n/24) + 13`.

3. **Conditional reduction.** If every prime `p ≡ 1 (mod 24)` satisfies
   `IsErdosStraus p`, then the full Erdős–Straus conjecture holds:
   a prime `n` uses the machine-verified 7-case partition
   (`erdos_straus_except_residual_open_class`) — the case it leaves is
   exactly `n ≡ 1 (mod 24)`, supplied by the hypothesis (primes
   `≡ 13 (mod 24)` are prime ∧ 5 mod 8, where `theorem2` applies inside);
   a composite `n` descends to a prime factor and scales.

Together with the documented axiom, this narrows what is *actually*
assumed: only the prime-`1 mod 24` class — composites follow by scaling,
primes `≡ 13 (mod 24)` by `theorem2`.
-/

namespace ErdosStrausConjecture

/-- Mod-chain: `n ≡ 1 (mod 12)` and `n ≢ 1 (mod 24)` forces `n ≡ 5 (mod 8)`. -/
theorem mod8_of_12 (n : ℕ) (h12 : n % 12 = 1) (h24 : n % 24 ≠ 1) : n % 8 = 5 := by
  have h12d24 : (12 : ℕ) ∣ 24 := by omega
  have hlink : (n % 24) % 12 = n % 12 := Nat.mod_mod_of_dvd n h12d24
  have hmod1 : (n % 24) % 12 = 1 := by rw [hlink, h12]
  have hlt : (n % 24) / 12 ≤ 1 := by
    have hlt24 : n % 24 < 24 := Nat.mod_lt (x := n) (by omega)
    have hr1 : 12 * ((n % 24) / 12) + (n % 24) % 12 = n % 24 :=
      Nat.div_add_mod (n % 24) 12
    rw [hmod1] at hr1
    omega
  have h13 : (n % 24) = 13 := by
    have hr1 : 12 * ((n % 24) / 12) + (n % 24) % 12 = n % 24 :=
      Nat.div_add_mod (n % 24) 12
    rw [hmod1] at hr1
    rcases Nat.lt_or_ge ((n % 24) / 12) 1 with h0 | h1
    · omega
    · omega
  have n_eq : 24 * (n / 24) + (n % 24) = n := Nat.div_add_mod n 24
  rw [h13] at n_eq
  have hshift : 5 + (1 + 3 * (n / 24)) * 8 = n := by
    linear_combination n_eq
  rw [← hshift, Nat.add_mul_mod_self_right]

/-- **Scaling lemma.** A solution for `n` lifts to a solution for `n * k`
by multiplying every denominator by `k`. -/
theorem scaling (n k : ℕ) (hk : 0 < k) (h : IsErdosStraus n) :
    IsErdosStraus (n * k) := by
  obtain ⟨x, y, z, hx, hy, hz, heq⟩ := h
  refine ⟨k * x, k * y, k * z, ?_, ?_, ?_, ?_⟩
  · positivity
  · positivity
  · positivity
  calc 4 * (k * x) * (k * y) * (k * z)
      = k ^ 3 * (4 * x * y * z) := by ring
    _ = k ^ 3 * (n * (x * y + x * z + y * z)) := by rw [heq]
    _ = (n * k) * ((k * x) * (k * y) + (k * x) * (k * z) + (k * y) * (k * z)) := by
        ring

/-- **Prime branch (unconditional).** Every prime `n ≢ 1 (mod 24)` has an
Erdős–Straus representation: the machine-verified 7-case partition covers it
(`n ≡ 13 (mod 24)` means `n % 8 = 5`, where `theorem2` applies inside). -/
theorem prime_non24_isErdosStraus {n : ℕ} (hpr : Nat.Prime n)
    (h24 : n % 24 ≠ 1) :
    IsErdosStraus n := by
  have hno : ¬(n % 12 = 1 ∧ n % 5 ≠ 0 ∧ n ≥ 13 ∧ ¬(Nat.Prime n ∧ n % 8 = 5)) := by
    intro hc
    by_cases hc1 : n % 12 = 1
    · exact hc.2.2.2 ⟨hpr, mod8_of_12 n hc1 h24⟩
    · omega
  exact erdos_straus_except_residual_open_class n hpr.two_le hno

/-- **Conditional reduction (route 2).** If every prime `p ≡ 1 (mod 24)`
has an Erdős–Straus representation, the full conjecture holds. -/
theorem full_conjecture_of_h24 (H24 : ∀ p : ℕ, Nat.Prime p → p % 24 = 1 →
    IsErdosStraus p) :
    ∀ n : ℕ, 2 ≤ n → IsErdosStraus n := by
  intro n hn
  have hn1 : n ≠ 1 := by omega
  have hn0 : 0 < n := by omega
  by_cases hpr : Nat.Prime n
  · by_cases h24 : n % 24 = 1
    · exact H24 n hpr h24
    · exact prime_non24_isErdosStraus hpr h24
  · -- composite: descend to a prime factor and scale
    obtain ⟨p, hp, hdvd⟩ := Nat.exists_prime_and_dvd hn1
    have hpcases : IsErdosStraus p := by
      by_cases hp24 : p % 24 = 1
      · exact H24 p hp hp24
      · exact prime_non24_isErdosStraus hp hp24
    have hnk : p * (n / p) = n := by
      rw [Nat.mul_comm, Nat.div_mul_cancel hdvd]
    rw [← hnk]
    exact scaling p (n / p) (Nat.div_pos (Nat.le_of_dvd hn0 hdvd) hp.pos) hpcases

end ErdosStrausConjecture
