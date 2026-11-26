/-
Copyright (c) 2026. The Erdős–Straus research lane (Paper 2, R8).

The u = 11 layer of the u-method: the machine-checked companions of the
E-021..E-024 census (`research/residual_primes/`, engines v0.15-v0.22).

Facts established here:

1. `u11_no_hardcase_record_mod8` - the class-8 structural gap (E-021
   part 1): a cohort record cannot carry `p = 8 (mod 11)`, because then
   `11` divides `x = (p + 3)/4`, and the hard-case predicate forbids the
   odd prime factor `11` (`11 % 3 = 2 ≠ 1`).

2. `u11_x_odd` - the v2-bucket degeneracy (E-022 part 1): for the (H24)
   primes (`p = 1 (mod 8)`) the layer relation `4x = p + 11` gives
   `(p + 11) = 4 (mod 8)`, so `x` is always odd: the u = 7-style
   2-window layer does not exist on the u = 11 layer.

3. `u11_span_mod11_seven` / `u11_span_mod11_ten` - the explicit-witness
   span theorems for the non-QR-`n` classes `r11 = 7` (witness
   `d = p`: `(p + p·x) % 11 = 0`) and `r11 = 10` (witness `d = x`:
   `(x + p·x) % 11 = 0`) - the two classes E-021 part 1 measured at
   17.33% / 17.41% span rate with ZERO true failures at u = 11 (E-024:
   the fw > 11 fail count 0).

The span criterion stated is the engine's first-layer fact
(`exists d, d | n*x ∧ (d + n*x) % 11 = 0`), the R1-window form; the
collision criterion (`hasOppositePair`) is deliberately NOT identified
with it at u = 11 (E-024: the pair-vs-span distinction, the withdrawn
67.80% census, correction banner).

Standing banner: the Erdős–Straus conjecture is open and is not proved by
this program. Computation never closes a universal claim.
-/
import Mathlib

namespace ResidualPrimes

/-- **The u = 11 class-8 structural gap (E-021 part 1).** If
`4·x = p + 3` and `p = 8 (mod 11)`, then `11` divides `x` (since
`p + 3 = 0 (mod 11)` and gcd(4, 11) = 1), so `x` carries the odd prime
factor `11` with `11 % 3 = 2 ≠ 1`: the hard-case predicate - every odd
prime divisor of `x` congruent to `1 (mod 3)` - cannot hold for such a
record. -/
theorem u11_no_hardcase_record_mod8 (p x : ℕ) (hx0 : 0 < x)
    (hx : 4 * x = p + 3) (h8 : p % 11 = 8) :
    ¬ (∀ q : ℕ, q.Prime → q ∣ x → q % 3 = 1) := by
  intro hall
  have h11p3 : (11 : ℕ) ∣ p + 3 := Nat.dvd_of_mod_eq_zero (by omega)
  have hcop : Nat.Coprime 11 4 := by decide
  have h4x : (11 : ℕ) ∣ 4 * x := by rw [hx]; exact h11p3
  have h11x : (11 : ℕ) ∣ x := Nat.Coprime.dvd_of_dvd_mul_left hcop h4x
  have hviol : (11 : ℕ) % 3 = 1 := hall (11 : ℕ) (by norm_num) h11x
  norm_num at hviol

/-- **The u = 11 v2-bucket degeneracy (E-022 part 1).** For `4·x = p + 11`
with `p = 1 (mod 8)`, `x` is odd: `(p + 11)/4` is odd (since `p + 11 =
4 (mod 8)`), and the u = 7-style 2-window layer does not exist on the
u = 11 layer. -/
theorem u11_x_odd (p x : ℕ) (hx : 4 * x = p + 11) (h8 : p % 8 = 1) :
    ¬ (2 ∣ x) := by
  intro h2
  have h4x8 : (4 * x) % 8 = 4 := by omega
  omega

/-- **The u = 11 span witness at `r11 = 7`** (E-021 part 1 / E-024: the
class with ZERO true failures at u = 11). For `4·x = p + 11` with `p`
prime and `p = 7 (mod 11)`, the divisor `d = p` of `p·x` satisfies
`d + p·x = p + p·x = 0 (mod 11)` (the span criterion). -/
theorem u11_span_mod11_seven (p x : ℕ) (hx0 : 0 < x) (hnp : p.Prime)
    (hx : 4 * x = p + 11) (h7 : p % 11 = 7) :
    ∃ d : ℕ, d ∣ p * x ∧ (d + p * x) % 11 = 0 := by
  refine ⟨p, ⟨x, by ring⟩, ?_⟩
  have hex : (4 * x) % 11 = 7 := by rw [hx, Nat.add_mod_right, h7]
  have hxmod : x % 11 = 10 := by omega
  have hMmod : (p * x) % 11 = 4 := by
    rw [Nat.mul_mod, h7, hxmod]
  omega

/-- **The u = 11 span witness at `r11 = 10`** (E-021 part 1 / E-024: the
class with ZERO true failures at u = 11). For `4·x = p + 11` with `p`
prime and `p = 10 (mod 11)`, the divisor `d = x` of `p·x` satisfies
`d + p·x = x + p·x = x(1 + p) = 0 (mod 11)` since `p = 10 (mod 11)`
(the span criterion). -/
theorem u11_span_mod11_ten (p x : ℕ) (hx0 : 0 < x) (hnp : p.Prime)
    (hx : 4 * x = p + 11) (h10 : p % 11 = 10) :
    ∃ d : ℕ, d ∣ p * x ∧ (d + p * x) % 11 = 0 := by
  refine ⟨x, ⟨p, by ring⟩, ?_⟩
  have hxmod : x % 11 = 8 := by
    have hex : (4 * x) % 11 = 10 := by rw [hx, Nat.add_mod_right, h10]
    omega
  have hMmod : (p * x) % 11 = 3 := by
    rw [Nat.mul_mod, h10, hxmod]
  omega

end ResidualPrimes
