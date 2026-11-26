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

theorem qr_closed_mod11 (a b : ℕ)
    (ha : a % 11 = 1 ∨ a % 11 = 3 ∨ a % 11 = 4 ∨ a % 11 = 5 ∨ a % 11 = 9)
    (hb : b % 11 = 1 ∨ b % 11 = 3 ∨ b % 11 = 4 ∨ b % 11 = 5 ∨ b % 11 = 9) :
    (a * b) % 11 = 1 ∨ (a * b) % 11 = 3 ∨ (a * b) % 11 = 4 ∨
      (a * b) % 11 = 5 ∨ (a * b) % 11 = 9 := by
  rcases ha with e | e | e | e | e
  · rcases hb with k | k | k | k | k
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
  · rcases hb with k | k | k | k | k
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
  · rcases hb with k | k | k | k | k
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
  · rcases hb with k | k | k | k | k
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
  · rcases hb with k | k | k | k | k
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num
    · rw [Nat.mul_mod, e, k]; norm_num

/-- **The QR-side membership closure**: a positive integer whose prime
divisors all carry QR residues is itself one of `1, 3, 4, 5, 9 (mod 11)`
(the quadratic residues; `-1` is a non-residue since `11 = 3 (mod 4)`). -/
theorem prod_mod_qr (T : ℕ) (hT0 : 0 < T)
    (hall : ∀ q : ℕ, q.Prime → q ∣ T →
      (q % 11 = 1 ∨ q % 11 = 3 ∨ q % 11 = 4 ∨ q % 11 = 5 ∨ q % 11 = 9)) :
    T % 11 = 1 ∨ T % 11 = 3 ∨ T % 11 = 4 ∨ T % 11 = 5 ∨ T % 11 = 9 := by
  have h5 : ∀ r : ℕ, (r % 11 = 1 ∨ r % 11 = 3 ∨ r % 11 = 4 ∨ r % 11 = 5 ∨ r % 11 = 9) →
      r % 11 ≠ 2 := by
    intro r h heq
    rcases h with e | e | e | e | e
    · omega
    · omega
    · omega
    · omega
    · omega
  have key : ∀ t : ℕ, t ≤ T → 0 < t →
      (∀ q : ℕ, q.Prime → q ∣ t →
        (q % 11 = 1 ∨ q % 11 = 3 ∨ q % 11 = 4 ∨ q % 11 = 5 ∨ q % 11 = 9)) →
      t % 11 = 1 ∨ t % 11 = 3 ∨ t % 11 = 4 ∨ t % 11 = 5 ∨ t % 11 = 9 := by
    intro t
    induction t using Nat.strongRecOn with | ind t ih
    · intro _hle ht0 hall'
      by_cases h1 : t = 1
      · subst h1; exact Or.inl rfl
      · have htgt1 : 1 < t := by omega
        by_cases hpr : Nat.Prime t
        · exact hall' t hpr (dvd_refl t)
        · obtain ⟨q, hqp, hqt⟩ := Nat.exists_prime_and_dvd (by omega)
          have hqne : q ≠ t := by rintro rfl; exact hpr hqp
          have hlq : q ≤ t := Nat.le_of_dvd ht0 hqt
          have htdq : t / q ∣ t := Nat.div_dvd_of_dvd hqt
          have hlt : t / q < t := Nat.div_lt_self ht0 hqp.one_lt
          have hlqT : t / q ≤ T := Nat.le_trans (Nat.le_of_dvd ht0 htdq) _hle
          have htq0 : 0 < t / q := Nat.div_pos hlq (by linarith [hqp.one_lt])
          have hall2 : ∀ r : ℕ, r.Prime → r ∣ t / q →
              (r % 11 = 1 ∨ r % 11 = 3 ∨ r % 11 = 4 ∨ r % 11 = 5 ∨ r % 11 = 9) :=
            fun r hr hrd => hall' r hr (hrd.trans htdq)
          have hrec := ih (t / q) hlt hlqT htq0 hall2
          have hqres := hall' q hqp hqt
          have hdiv : t = (t / q) * q := (Nat.div_mul_cancel hqt).symm
          rw [hdiv]
          rcases hrec with e | e | e | e | e
          · rcases hqres with k | k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
  exact key T (Nat.le_refl T) hT0 hall

/-- **The QR-purity dichotomy (E-022/E-026, full scale).** For
`4·x = p + 11` with `p` prime, `p` a QR (mod 11), and `x` QR-pure
(every odd prime divisor of `x` in the QRs), the u = 11 span criterion
fails: every divisor of `(p·x)^2` carries a QR residue (the x factors
are QR and `x` is odd, so no factor of 2 appears anywhere), while
`-(p·x)` carries a non-QR residue (`-1` is a non-residue because
`11 = 3 (mod 4)`). -/
theorem u11_span_fails_of_qr_pure_x (p x : ℕ) (hx0 : 0 < x) (hnp : p.Prime)
    (hx : 4 * x = p + 11) (h8 : p % 8 = 1)
    (hqr : p % 11 = 1 ∨ p % 11 = 3 ∨ p % 11 = 4 ∨ p % 11 = 5 ∨ p % 11 = 9)
    (hxp : ∀ q : ℕ, q.Prime → q ∣ x →
      (q % 11 = 1 ∨ q % 11 = 3 ∨ q % 11 = 4 ∨ q % 11 = 5 ∨ q % 11 = 9)) :
    ∀ d : ℕ, d ∣ p ^ 2 * x ^ 2 → (d + p * x) % 11 ≠ 0 := by
  have hxodd : ¬ (2 ∣ x) := u11_x_odd p x hx h8
  have hxQRres : x % 11 = 1 ∨ x % 11 = 3 ∨ x % 11 = 4 ∨ x % 11 = 5 ∨ x % 11 = 9 :=
    prod_mod_qr x hx0 hxp
  have hMQR : (p * x) % 11 = 1 ∨ (p * x) % 11 = 3 ∨ (p * x) % 11 = 4 ∨
      (p * x) % 11 = 5 ∨ (p * x) % 11 = 9 :=
    qr_closed_mod11 p x hqr hxQRres
  intro d hd hcong
  have hpn1 : 1 < p := Nat.Prime.one_lt hnp
  have hp0 : (0 : ℕ) < p := by omega
  have hx0p : (0 : ℕ) < x := hx0
  have hN0 : 0 < p ^ 2 * x ^ 2 := by positivity
  have hd0 : 0 < d := Nat.pos_of_dvd_of_pos hd hN0
  have hdQR : d % 11 = 1 ∨ d % 11 = 3 ∨ d % 11 = 4 ∨ d % 11 = 5 ∨ d % 11 = 9 := by
    refine prod_mod_qr d hd0 ?_
    intro q hqp hqd
    have hqN : q ∣ p ^ 2 * x ^ 2 := hqd.trans hd
    rcases (Nat.Prime.dvd_mul hqp).mp hqN with hqp2 | hqx2
    · have hqeq : q = p := Nat.prime_eq_prime_of_dvd_pow hqp hnp hqp2
      rw [hqeq]; exact hqr
    · have hqx : q ∣ x := Nat.Prime.dvd_of_dvd_pow hqp hqx2
      exact hxp q hqp hqx
  -- the contradiction: the sum of two QR residues is never 0 (mod 11)
  have hsum : (d + p * x) % 11 ≠ 0 := by
    rcases hdQR with e | e | e | e | e
    · rcases hMQR with k | k | k | k | k
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
    · rcases hMQR with k | k | k | k | k
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
    · rcases hMQR with k | k | k | k | k
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
    · rcases hMQR with k | k | k | k | k
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
    · rcases hMQR with k | k | k | k | k
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
      · rw [Nat.add_mod, e, k]; norm_num
  exact hsum hcong

end ResidualPrimes

