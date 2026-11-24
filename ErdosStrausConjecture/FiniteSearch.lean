import Mathlib
import ErdosStrausConjecture.Basic
import ErdosStrausConjecture.CenteredCriterion

/-!
# Finite-search extraction for the Erdős–Straus parameter (Theorem 5.2)

The witness-extraction direction of the paper's finite-search equivalence:
any Erdős–Straus solution for an odd prime `p ≡ 1 (mod 4)`, once its
smallest denominator is named `x`, produces an admissible parameter
`u = 4x − p` (with `0 < u ≤ 2p`, `u ≡ 3 (mod 4)`, `gcd(p·x, u) = 1`) and an
explicit divisor witness `T ∣ (p·x)²` with `T ≡ −p·x (mod u)`, whose
complementary divisor `(p·x)²/T ≡ −p·x (mod u)` is exactly the input that
`CenteredCriterion.u_method_witness` converts back into a solution.
Combined with `u_method_witness`, this establishes the equivalence between
representations and witnesses in the finite domain
`0 < u ≤ 2p, u ≡ 3 (mod 4)` — the `(mod 24)` instance is hypothesis (H24).
-/

namespace ErdosStrausConjecture

/-- **Theorem 5.2 (finite-search equivalence, extraction direction).**
If `4/p = 1/x + 1/y + 1/z` with `p` an odd prime, `p ≡ 1 (mod 4)`, and `x`
the smallest denominator, then `u = 4x − p` satisfies `0 < u ≤ 2p`,
`u ≡ 3 (mod 4)`, is coprime to `p·x`, and `T = 4xy − p(x+y)` is a positive
divisor of `(p·x)²` with `T + p·x ≡ 0 (mod u)` and
`(p·x)²/T + p·x ≡ 0 (mod u)`. -/
theorem witness_extraction
    (p x y z : ℕ)
    (hpr : Nat.Prime p) (hp4 : p % 4 = 1)
    (hx : 0 < x) (hy : 0 < y) (hz : 0 < z)
    (hxy : x ≤ y) (hxz : x ≤ z)
    (heq : 4 * x * y * z = p * (x * y + x * z + y * z)) :
    ∃ u T : ℕ,
      u + p = 4 * x ∧ 0 < u ∧ u ≤ 2 * p ∧ u % 4 = 3 ∧
      Nat.Coprime (p * x) u ∧
      0 < T ∧ T ∣ (p * x) ^ 2 ∧ (T + p * x) % u = 0 ∧
      ((p * x) ^ 2 / T + p * x) % u = 0 := by
  have hp2 : 2 ≤ p := hpr.two_le
  have hp0 : 0 < p := by omega
  -- the defining identity, distributed
  have h4 : 4 * x * y * z = p * x * y + p * x * z + p * y * z := by
    rw [heq]; ring
  have hpxy_pos : 0 < p * x * y := Nat.mul_pos (Nat.mul_pos hp0 hx) hy
  have hpxz_pos : 0 < p * x * z := Nat.mul_pos (Nat.mul_pos hp0 hx) hz
  -- non-truncation bounds for the witness-defining differences
  have hTle : p * x + p * y ≤ 4 * x * y := by
    refine Nat.le_of_mul_le_mul_right ?_ hz
    rw [Nat.add_mul]
    linarith [h4]
  have hQle : p * x + p * z ≤ 4 * x * z := by
    refine Nat.le_of_mul_le_mul_right ?_ hy
    rw [Nat.add_mul]
    linarith [h4]
  -- cross-term domination (x is the smallest denominator)
  have h1a : p * x * y ≤ p * y * z := by
    have hpx : p * x ≤ p * z := Nat.mul_le_mul_left p hxz
    calc p * x * y = (p * x) * y := by ring
      _ ≤ (p * z) * y := Nat.mul_le_mul_right y hpx
      _ = p * y * z := by ring
  have h1b : p * x * z ≤ p * y * z := by
    have hpx : p * x ≤ p * y := Nat.mul_le_mul_left p hxy
    calc p * x * z = (p * x) * z := by ring
      _ ≤ (p * y) * z := Nat.mul_le_mul_right z hpx
      _ = p * y * z := by ring
  have hsum : 4 * x * y * z ≤ 3 * (p * y * z) := by linarith [h4, h1a, h1b]
  have h4x3p : 4 * x ≤ 3 * p := by
    refine Nat.le_of_mul_le_mul_right ?_ (Nat.mul_pos hy hz)
    linarith [hsum]
  have hpxy_big : p ≤ p * x * y := by
    have h1 : p ≤ p * x := Nat.le_mul_of_pos_right p hx
    have h2 : p * x ≤ p * x * y := Nat.le_mul_of_pos_right (p * x) hy
    linarith
  have hb : p * y * z + p ≤ 4 * x * y * z := by linarith [h4, hpxy_big]
  have hplt : p < 4 * x := by
    have h1 : p * (y * z) < (4 * x) * (y * z) := by linarith [hb, hp2]
    exact Nat.lt_of_mul_lt_mul_right h1
  -- witness product identities
  have hTz : (4 * x * y - p * (x + y)) * z = p * x * y := by
    rw [Nat.sub_mul, Nat.mul_add, Nat.add_mul,
      show (4 * x * y) * z = 4 * x * y * z from by ring,
      show (p * x) * z = p * x * z from by ring,
      show (p * y) * z = p * y * z from by ring, h4]
    omega
  have hQy : (4 * x * z - p * (x + z)) * y = p * x * z := by
    rw [Nat.sub_mul, Nat.mul_add, Nat.add_mul,
      show (4 * x * z) * y = 4 * x * y * z from by ring,
      show (p * x) * y = p * x * y from by ring,
      show (p * z) * y = p * y * z from by ring, h4]
    omega
  have hkey : (4 * x * y - p * (x + y)) * (4 * x * z - p * (x + z)) * (y * z)
      = (p * x) ^ 2 * (y * z) := by
    calc (4 * x * y - p * (x + y)) * (4 * x * z - p * (x + z)) * (y * z)
        = (4 * x * y - p * (x + y)) * z * ((4 * x * z - p * (x + z)) * y) := by ring
      _ = p * x * y * (p * x * z) := by rw [hTz, hQy]
      _ = (p * x) ^ 2 * (y * z) := by ring
  have hdiv : (4 * x * y - p * (x + y)) * (4 * x * z - p * (x + z)) = (p * x) ^ 2 :=
    Nat.eq_of_mul_eq_mul_right (Nat.mul_pos hy hz) hkey
  -- positivity of the witnesses
  have hTpos : 0 < 4 * x * y - p * (x + y) := by
    by_contra hc
    rw [Nat.le_zero.mp (Nat.not_lt.mp hc)] at hTz
    omega
  have hQpos : 0 < 4 * x * z - p * (x + z) := by
    by_contra hc
    rw [Nat.le_zero.mp (Nat.not_lt.mp hc)] at hQy
    omega
  -- the mod conditions
  have hTpx : (4 * x * y - p * (x + y)) + p * x = 4 * x * y - p * y := by
    rw [Nat.mul_add]; omega
  have hQpx : (4 * x * z - p * (x + z)) + p * x = 4 * x * z - p * z := by
    rw [Nat.mul_add]; omega
  refine ⟨4 * x - p, 4 * x * y - p * (x + y), ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · omega  -- u + p = 4 * x (V14-03: the exported defining equation), from hplt
  · omega  -- 0 < u, from hplt
  · omega  -- u ≤ 2p, from h4x3p
  · omega  -- u % 4 = 3, from hp4
  · -- Nat.Coprime (p * x) (4 * x - p)
    have hxlt : x < p := by omega
    have hcop_p : Nat.Coprime p (4 * x - p) := by
      rw [Nat.Prime.coprime_iff_not_dvd hpr]
      intro hd
      have hx4 : p ∣ 4 * x := by
        have h1 : p ∣ (4 * x - p) + p := dvd_add hd (dvd_refl p)
        have h2 : (4 * x - p) + p = 4 * x := by omega
        rw [h2] at h1
        exact h1
      rcases (Nat.Prime.dvd_mul hpr).mp hx4 with h4d | hxd
      · have h5 : p ≤ 4 := Nat.le_of_dvd (by omega) h4d
        omega
      · have h5 : p ≤ x := Nat.le_of_dvd hx hxd
        omega
    have hcop_x : Nat.Coprime x (4 * x - p) := by
      have h3 : Nat.gcd x (4 * x - p) ∣ x := Nat.gcd_dvd_left x (4 * x - p)
      have h2 : Nat.gcd x (4 * x - p) ∣ 4 * x - p := Nat.gcd_dvd_right x (4 * x - p)
      have h4g : Nat.gcd x (4 * x - p) ∣ 4 * x := h3.trans ⟨4, by ring⟩
      have hgp : Nat.gcd x (4 * x - p) ∣ 4 * x - (4 * x - p) := Nat.dvd_sub h4g h2
      rw [Nat.sub_sub_self (by omega)] at hgp  -- the gcd now divides p
      have hdgcd : Nat.gcd x (4 * x - p) ∣ Nat.gcd p (4 * x - p) := Nat.dvd_gcd hgp h2
      have h6 : Nat.gcd p (4 * x - p) = 1 := hcop_p
      rw [h6] at hdgcd
      exact Nat.dvd_one.mp hdgcd
    exact Nat.Coprime.mul_left hcop_p hcop_x
  · exact hTpos  -- 0 < T
  · exact ⟨4 * x * z - p * (x + z), hdiv.symm⟩  -- T ∣ (p·x)²
  · -- (T + p·x) % u = 0
    have hdvd1 : (4 * x - p) ∣ 4 * x * y - p * y :=
      ⟨y, by rw [Nat.sub_mul]⟩
    rw [hTpx, Nat.mod_eq_zero_of_dvd hdvd1]
  · -- ((p·x)² / T + p·x) % u = 0
    have hMWdiv : (p * x) ^ 2 / (4 * x * y - p * (x + y))
        = 4 * x * z - p * (x + z) := by
      rw [← hdiv, Nat.mul_div_cancel_left _ hTpos]
    have hdvd2 : (4 * x - p) ∣ 4 * x * z - p * z :=
      ⟨z, by rw [Nat.sub_mul]⟩
    rw [hMWdiv, hQpx, Nat.mod_eq_zero_of_dvd hdvd2]

/-- **Theorem 5.2 composed (the complete biconditional; V14-03).** For an odd
prime `p ≡ 1 (mod 4)`, `p` has an Erdös–Straus representation exactly when
the span witness of the finite-search equivalence exists at the paper's
parameter `u = 4x − p`. This theorem composes the extraction direction
(`witness_extraction`, above) with the constructive reverse
(`u_method_witness`, `CenteredCriterion.lean`), so the manuscript's
Theorem 5.2 is itself a single machine-checked equivalence rather than two
separate ingredients. -/
theorem finite_search_equivalence (p : ℕ) (hpr : Nat.Prime p) (hp4 : p % 4 = 1) :
    (∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧
        4 * x * y * z = p * (x * y + x * z + y * z)) ↔
      (∃ x u T : ℕ, 0 < x ∧ u + p = 4 * x ∧ 0 < u ∧ u ≤ 2 * p ∧ u % 4 = 3 ∧
        Nat.Coprime (p * x) u ∧ 0 < T ∧ T ∣ (p * x) ^ 2 ∧
        (T + p * x) % u = 0 ∧ ((p * x) ^ 2 / T + p * x) % u = 0) := by
  constructor
  · rintro ⟨x, y, z, hx1, hy1, hz1, heq⟩
    rcases Nat.le_total x y with hxy | hyx
    · rcases Nat.le_total x z with hxz | hzx
      · -- x is the smallest denominator
        obtain ⟨u, T, hw⟩ :=
          witness_extraction p x y z hpr hp4 hx1 hy1 hz1 hxy hxz heq
        exact ⟨x, u, T, hx1, hw⟩
      · -- z < x ≤ y: z carries the smallest denominator
        have hzy : z ≤ y := by omega
        obtain ⟨u, T, hw⟩ :=
          witness_extraction p z x y hpr hp4 hz1 hx1 hy1 hzx hzy
            (by linear_combination heq)
        exact ⟨z, u, T, hz1, hw⟩
    · -- y < x
      rcases Nat.le_total y z with hyz | hzy
      · -- y smallest
        obtain ⟨u, T, hw⟩ :=
          witness_extraction p y x z hpr hp4 hy1 hx1 hz1 hyx hyz
            (by linear_combination heq)
        exact ⟨y, u, T, hy1, hw⟩
      · -- z smallest (z < y < x)
        have hzx : z ≤ x := by omega
        obtain ⟨u, T, hw⟩ :=
          witness_extraction p z y x hpr hp4 hz1 hy1 hx1 hzy hzx
            (by linear_combination heq)
        exact ⟨z, u, T, hz1, hw⟩
  · rintro ⟨x, u, T, hx1, hu4x, hu0, hu2p, hu3, hcopr, hT0, hTdvd, hTmod, hTmod2⟩
    have hp0 : 0 < p := hpr.pos
    have hudef : u = 4 * x - p := by omega
    have hcopr' : Nat.Coprime u (p * x) := Nat.coprime_comm.mp hcopr
    have hcong : u ∣ T + p * x := Nat.dvd_of_mod_eq_zero hTmod
    obtain ⟨y', z', hy2, hz2, hbody⟩ :=
      u_method_witness p x T u hp0 hx1 hu0 hudef hcopr' hTdvd hT0 hcong
    exact ⟨x, y', z', hx1, hy2, hz2, hbody⟩
