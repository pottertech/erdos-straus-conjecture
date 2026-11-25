import Mathlib
import ErdosStrausConjecture.CenteredCriterion

/-!
# Residual Prime Structure: the u = 3 layer boundary (Paper 2, R8 piece 3)

The exact class boundary of the first `(mod 4)` layer of the u-method, the
formal counterpart of the E-011 empirical census
(`research/residual_primes/`, engine v0.8, experiment E-011):

The u = 3 span criterion

  `∃ T, T ∣ (n·x)^2 ∧ (T + n·x) ≡ 0 (mod 3)`

is settled on both sides, by two different results that must not be
conflated. The constructive side is `u3_span_of_even_x` below: for even
`x` with `3 ∤ x` (and no hard-case predicate), the criterion holds at
`T = 2`; this is the `n ≡ 5 (mod 8)` class, Paper 1's unconditional
`p ≡ 13 (mod 24)` family. The exclusion side concerns the hard-case
predicate on `x` used here (every prime divisor of `x` is
`≡ 1 (mod 3)`, with no exemption): that predicate can never hold for
even `x`, because `2` would be a prime divisor of `x` and
`2 ≢ 1 (mod 3)`, so under the predicate `x` is odd and the criterion
**fails for every such `x`** (the residual `p ≡ 1 (mod 8)` class, whose
first-working parameter is therefore `≥ 7`). Note the predicate here is
stronger than the sweep engine's, which exempts the factor `2`
(engine v0.8, parity-slip rule); the composed statement
`u3_span_iff_even_of_hard` is correct as an `↔`, but its even side is
vacuous, since the predicate and `2 ∣ x` cannot hold together.

Statements, all self-contained Mathlib + the audited u-method core:

1. `prod_mod_one_of_primes_mod` - the multiplicative residue closure: a
   positive integer whose prime divisors are all `≡ 1 (mod 3)` is itself
   `≡ 1 (mod 3)`.
2. `u3_span_of_even_x` - the constructive direction: for even `x` with
   `3` coprime to `x`, the span criterion holds at `T = 2`.
3. `isErdosStraus_of_even_x` - the primality-free representation behind the
   u = 3 layer (the sharpened form of Paper 1's `F(p) = 3` family).
4. `u3_span_fails_of_odd_x` - the exclusion direction: under the hard-case
   predicate, no span candidate exists at `u = 3` for odd `x`.
5. `u3_span_iff_even_of_hard` - the composed boundary under the
   hard-case predicate: the criterion holds iff `2 ∣ x`, which the
   predicate itself rules out, so under the predicate the criterion
   never holds. The E-011 run agrees empirically over the full sweep
   `[10^7, 10^9)` (3,194,231 records, zero mismatches: the u = 3
   population is exactly the non-(H24) records,
   830,200 = 3,194,231 - 2,364,031).
-/

namespace ResidualPrimes

/-- The u = 3 span-side criterion: a span candidate `T` dividing `(n·x)^2`
with `T + n·x ≡ 0 (mod 3)`. -/
def u3Span (n x : ℕ) : Prop := ∃ T : ℕ, T ∣ (n * x) ^ 2 ∧ (T + n * x) % 3 = 0

/-- **Multiplicative residue closure.** A positive integer whose prime
divisors are all `≡ 1 (mod 3)` is itself `≡ 1 (mod 3)`. -/
theorem prod_mod_one_of_primes_mod (T : ℕ) (hT0 : 0 < T)
    (hall : ∀ q : ℕ, q.Prime → q ∣ T → q % 3 = 1) : T % 3 = 1 := by
  have key : ∀ t : ℕ, t ≤ T → 0 < t →
      (∀ q : ℕ, q.Prime → q ∣ t → q % 3 = 1) → t % 3 = 1 := by
    intro t
    induction t using Nat.strongRecOn with | ind t ih
    · intro _hle ht0 hall'
      by_cases h1 : t = 1
      · subst h1; norm_num
      · have htgt1 : 1 < t := by omega
        by_cases hpr : Nat.Prime t
        · exact hall' t hpr (dvd_refl t)
        · obtain ⟨q, hqp, hqt⟩ := Nat.exists_prime_and_dvd (by omega)
          have hqne : q ≠ t := by rintro rfl; exact hpr hqp
          have hlq : q ≤ t := Nat.le_of_dvd ht0 hqt
          have hqlt : q < t := Nat.lt_of_le_of_ne hlq hqne
          have htdq : t / q ∣ t := Nat.div_dvd_of_dvd hqt
          have hlt : t / q < t := Nat.div_lt_self ht0 hqp.one_lt
          have hlqT : t / q ≤ T := Nat.le_trans (Nat.le_of_dvd ht0 htdq) _hle
          have htq0 : 0 < t / q := Nat.div_pos hlq (by linarith [hqp.one_lt])
          have hall2 : ∀ r : ℕ, r.Prime → r ∣ t / q → r % 3 = 1 :=
            fun r hr hrd => hall' r hr (hrd.trans htdq)
          have hrec : (t / q) % 3 = 1 := ih (t / q) hlt hlqT htq0 hall2
          have hqmod : q % 3 = 1 := hall' q hqp hqt
          calc t % 3
              = ((t / q) * q) % 3 := by rw [Nat.div_mul_cancel hqt]
            _ = ((t / q) % 3) * (q % 3) % 3 := Nat.mul_mod (t / q) q 3
            _ = 1 := by rw [hrec, hqmod]
  exact key T (Nat.le_refl T) hT0 hall

/-- **The u = 3 span, constructive direction.** For `4·x = n + 3` with
`2 ∣ x` and `3` coprime to `x`, the span criterion holds at `T = 2`. -/
theorem u3_span_of_even_x (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 3) (h2x : 2 ∣ x) (hx3 : ¬(3 ∣ x)) : u3Span n x := by
  have hx2 : x = 2 * (x / 2) := by
    have hd := Nat.div_add_mod x 2
    rw [Nat.mod_eq_zero_of_dvd h2x] at hd
    omega
  have hxM : 2 ∣ n * x := dvd_mul_of_dvd_right h2x n
  have hM1 : (n * x) % 3 = 1 := by
    have hnx : n % 3 = x % 3 := by omega
    have hx3' : x % 3 = 1 ∨ x % 3 = 2 := by
      have hb : x % 3 < 3 := Nat.mod_lt _ (by norm_num)
      omega
    rcases hx3' with h1 | h2
    · rw [Nat.mul_mod, hnx, h1]
    · rw [Nat.mul_mod, hnx, h2]
  refine ⟨2, ?_, ?_⟩
  · rw [Nat.pow_two]; exact dvd_mul_of_dvd_right hxM (n * x)
  · calc (2 + n * x) % 3
        = ((n * x) + 2) % 3 := by rw [add_comm]
      _ = ((n * x) % 3 + 2 % 3) % 3 := Nat.add_mod _ _ _
      _ = (1 + 2) % 3 := by rw [hM1]
      _ = 0 := by norm_num

/-- The sharpened, primality-free representation behind the u = 3 layer:
for `4·x = n + 3`, `2 ∣ x`, `3` coprime to `x`, Paper 1's u-method core
turns the `T = 2` span into an explicit positive solution of the witness
identity. -/
theorem isErdosStraus_of_even_x (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 3) (h2x : 2 ∣ x) (hx3 : ¬(3 ∣ x)) :
    ErdosStrausConjecture.IsErdosStraus n := by
  have hsq : (n * x) ^ 2 = (n * x) * (n * x) := Nat.pow_two _
  have hx2 : x = 2 * (x / 2) := by
    have hd := Nat.div_add_mod x 2
    rw [Nat.mod_eq_zero_of_dvd h2x] at hd
    omega
  have hxM : 2 ∣ n * x := dvd_mul_of_dvd_right h2x n
  have hnx : n % 3 = x % 3 := by omega
  have hx3' : x % 3 = 1 ∨ x % 3 = 2 := by
    have hb : x % 3 < 3 := Nat.mod_lt _ (by norm_num)
    omega
  have hM1 : (n * x) % 3 = 1 := by
    rcases hx3' with h1 | h2
    · rw [Nat.mul_mod, hnx, h1]
    · rw [Nat.mul_mod, hnx, h2]
  have h3M : ¬ (3 ∣ n * x) := by
    intro hd
    rcases (Nat.Prime.dvd_mul Nat.prime_three).mp hd with hn3 | hxm3
    · have hn3' : n % 3 = 0 := Nat.dvd_iff_mod_eq_zero.mp hn3
      omega
    · exact hx3 hxm3
  have hcopr : Nat.Coprime 3 (n * x) :=
    (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3M
  obtain ⟨y, z, hy, hz, hid⟩ :=
    ErdosStrausConjecture.u_method_witness n x 2 3 hn0 hx0 (by norm_num)
      (by omega) hcopr (by rw [hsq]; exact dvd_mul_of_dvd_right hxM _)
      (by norm_num) (by
        have hc : (2 + n * x) % 3 = 0 := by
          calc (2 + n * x) % 3
              = ((n * x) + 2) % 3 := by rw [add_comm]
            _ = ((n * x) % 3 + 2 % 3) % 3 := Nat.add_mod _ _ _
            _ = (1 + 2) % 3 := by rw [hM1]
            _ = 0 := by norm_num
        exact Nat.dvd_iff_mod_eq_zero.mpr hc)
  exact ⟨x, y, z, hx0, hy, hz, hid⟩

/-- **The u = 3 span, exclusion direction.** Under the hard-case predicate
(every prime divisor of `x` is `≡ 1 (mod 3)`) with `x` odd, no span
candidate exists at `u = 3`. -/
theorem u3_span_fails_of_odd_x (n x : ℕ) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 3) (hodd : ¬ (2 ∣ x)) (hnp : n.Prime)
    (hxp : ∀ q : ℕ, q.Prime → q ∣ x → q % 3 = 1) :
    ¬ u3Span n x := by
  have hx1 : x % 3 = 1 := prod_mod_one_of_primes_mod x hx0 hxp
  have hn1 : n % 3 = 1 := by omega
  have hM1 : (n * x) % 3 = 1 := by rw [Nat.mul_mod, hn1, hx1]
  rintro ⟨T, hT, hcong⟩
  have hT0 : 0 < T := by
    by_contra hTz
    have hTe : T = 0 := Nat.le_zero.mp (Nat.not_lt.mp hTz)
    rw [hTe, Nat.zero_add] at hcong
    exact absurd (hM1.symm.trans hcong) Nat.one_ne_zero
  have hallT : ∀ q : ℕ, q.Prime → q ∣ T → q % 3 = 1 := by
    intro q hqp hqT
    have hqM2 : q ∣ (n * x) ^ 2 := hqT.trans hT
    have hqM : q ∣ n * x := hqp.dvd_of_dvd_pow hqM2
    rcases (Nat.Prime.dvd_mul hqp).mp hqM with hqn | hqx
    · have hqeq : q = n :=
        Nat.prime_eq_prime_of_dvd_pow hqp hnp (by rw [pow_one]; exact hqn)
      rw [hqeq]; exact hn1
    · exact hxp q hqp hqx
  have hT1 : T % 3 = 1 := prod_mod_one_of_primes_mod T hT0 hallT
  have hsum : (T + n * x) % 3 = 2 := by
    calc (T + n * x) % 3
        = (T % 3 + (n * x) % 3) % 3 := Nat.add_mod _ _ _
      _ = (1 + 1) % 3 := by rw [hT1, hM1]
      _ = 2 := by norm_num
  rw [hsum] at hcong
  exact absurd hcong (by decide : ¬ ((2 : ℕ) = 0))

/-- **The u = 3 layer boundary (E-011/E-012).** Under the hard-case
predicate the span criterion at `u = 3` holds iff `x` is even, but the
predicate rules out even `x` (a prime divisor `2` would need
`2 ≡ 1 (mod 3)`), so under the predicate the criterion never holds; the
constructive even-`x` result is `u3_span_of_even_x`, which assumes no
hard-case predicate. -/
theorem u3_span_iff_even_of_hard (n x : ℕ) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 3) (hnp : n.Prime)
    (hxp : ∀ q : ℕ, q.Prime → q ∣ x → q % 3 = 1) :
    u3Span n x ↔ 2 ∣ x := by
  have hx3 : ¬ (3 ∣ x) := by
    intro h3
    have h31 := hxp 3 Nat.prime_three h3
    rw [Nat.mod_self] at h31
    exact Nat.zero_ne_one h31
  have hn0 : 0 < n := by omega
  constructor
  · intro hsp
    by_cases h2 : 2 ∣ x
    · exact h2
    · exact absurd hsp (u3_span_fails_of_odd_x n x hx0 hu4 h2 hnp hxp)
  · intro h2
    exact u3_span_of_even_x n x hn0 hx0 hu4 h2 hx3

end ResidualPrimes
