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

/-! ## Parametric witnesses and the one-sided divisor set (sixth review section 4)

With the witness-pair construction `y = (T + n*x)/u` and
`z = ((n*x)^2/T + n*x)/u`, multiplying by `u` gives
`z*u = (n*x)^2/T + n*x = (n*x/T)*(T + n*x)`, so `y` divides `z` exactly
when `T` divides `n*x` — a parametric witness can be detected from a
divisor of `M = n*x` alone, without constructing both denominators.
Consequently a parametric witness exists for `(n, u)` exactly when the
**one-sided product set**
`D_u(n*x) = { d mod u : d divides n*x }` contains `-1` (the sixth
review's boxed criterion), in contrast with the centered product set
`S_u(n*x)` that the paper's criterion uses; the set difference between
`S_u` and `D_u` is exactly the `witness_no_param_at_first_u` population
of section 6.5. Both lemmas apply only the sixth review's elementary
derivations; originality is not claimed.
-/

/-- **Parametric divisibility (sixth review section 4).** Under the
paper's witness conditions (`T` divides `(n*x)^2`, `u` divides
`T + n*x`, `Coprime u (n*x)`), if additionally `T` divides `n*x`, then
`y` divides `z` with quotient `n*x / T`: indeed
`z = y * (n*x / T)`. -/
theorem parametric_divisibility (n x T u : ℕ)
    (hu0 : 0 < u) (hcopr : Nat.Coprime u (n * x))
    (hT2 : T ∣ (n * x) ^ 2) (hTdivM : T ∣ n * x)
    (hcong : u ∣ T + n * x) :
    ((T + n * x) / u) ∣ ((n * x) ^ 2 / T + n * x) / u := by
  have hmul1 : ((n * x) ^ 2 / T) * T = (n * x) ^ 2 :=
    Nat.div_mul_cancel hT2
  -- u divides the z-numerator (the u_method_witness h5/h6 derivation)
  have huz : u ∣ (n * x) ^ 2 / T + n * x := by
    have h5 : u ∣ ((n * x) ^ 2 / T) * (T + n * x) :=
      hcong.mul_left ((n * x) ^ 2 / T)
    have h5b : ((n * x) ^ 2 / T) * (T + n * x)
        = n * x * (n * x + (n * x) ^ 2 / T) := by
      linear_combination hmul1
    have h6 : u ∣ n * x * ((n * x) ^ 2 / T + n * x) := by
      rw [Nat.add_comm ((n * x) ^ 2 / T) (n * x), ← h5b]
      exact h5
    exact Nat.Coprime.dvd_of_dvd_mul_left hcopr h6
  refine ⟨n * x / T, Nat.div_eq_of_eq_mul_left hu0 ?_⟩
  have hT1c : (n * x / T) * T = n * x := Nat.div_mul_cancel hTdivM
  have hsqm : (n * x) * (n * x / T) = (n * x) ^ 2 / T := by
    rw [← Nat.mul_div_assoc (n * x) hTdivM]
    ring
  have hy : (T + n * x) / u * u = T + n * x := Nat.div_mul_cancel hcong
  have hy4 : (T + n * x) * (n * x / T)
      = ((T + n * x) / u * (n * x / T)) * u := by
    have hy3 : (T + n * x) * (n * x / T)
        = ((T + n * x) / u * u) * (n * x / T) := by rw [hy]
    rw [hy3, Nat.mul_assoc, Nat.mul_comm u (n * x / T),
      ← Nat.mul_assoc]

  rw [← hy4, Nat.add_mul, Nat.mul_comm T (n * x / T), hT1c, hsqm,
    Nat.add_comm (n * x) ((n * x) ^ 2 / T)]

/-- **One-sided criterion (sixth review section 4.1).** A parametric
witness exists for `(n, u)` — some `T` meeting the paper's witness
conditions with `T` dividing `n*x` — exactly when `-1` is in the
one-sided set `D_u(n*x)`: some divisor `d` of `n*x` satisfies
`d ≡ −1 (mod u)`. -/
theorem param_exists_iff_onesided (n x u : ℕ)
    (hu0 : 0 < u) (hcopr : Nat.Coprime u (n * x)) :
    (∃ T : ℕ, T ∣ (n * x) ^ 2 ∧ T ∣ n * x ∧ (T + n * x) % u = 0)
      ↔ (∃ d : ℕ, d ∣ n * x ∧ (d + 1) % u = 0) := by
  constructor
  · rintro ⟨T, -, hTm, hcong0⟩
    have hcong : u ∣ T + n * x := Nat.dvd_of_mod_eq_zero hcong0
    have hcoprT : Nat.Coprime T u := by
      have hg1 : Nat.gcd T u ∣ n * x :=
        Nat.dvd_trans (Nat.gcd_dvd_left T u) hTm
      have hg2 : Nat.gcd T u ∣ u := Nat.gcd_dvd_right T u
      have hg3 : Nat.gcd T u ∣ Nat.gcd u (n * x) := Nat.dvd_gcd hg2 hg1
      have hcopr_eq : Nat.gcd u (n * x) = 1 := hcopr
      rw [hcopr_eq] at hg3
      exact Nat.dvd_one.mp hg3
    have hdm : n * x = (n * x / T) * T :=
      (Nat.div_mul_cancel hTm).symm
    have h1 : u ∣ T * (1 + n * x / T) := by
      rw [Nat.mul_add, Nat.mul_one, Nat.mul_comm T (n * x / T), ← hdm]
      exact hcong
    have h2 : (1 + n * x / T) % u = 0 := by
      refine Nat.mod_eq_zero_of_dvd ?_
      exact Nat.Coprime.dvd_of_dvd_mul_left (Nat.Coprime.symm hcoprT) h1
    exact ⟨n * x / T, ⟨T, (Nat.div_mul_cancel hTm).symm⟩,
      by rw [Nat.add_comm (n * x / T) 1]; exact h2⟩
  · rintro ⟨d, hdvd, hd1⟩
    obtain ⟨c, hc⟩ := hdvd
    obtain ⟨w, hw⟩ := Nat.dvd_of_mod_eq_zero hd1
    have hcm2 : c + n * x = c * (d + 1) := by rw [hc]; ring
    exact ⟨c, ⟨d * (n * x), by rw [hc]; ring⟩,
      ⟨d, by rw [hc]; ring⟩,
      by rw [hcm2, hw, Nat.mul_comm c (u * w),
        Nat.mul_assoc u w c, Nat.mul_mod_right u (w * c)]⟩
/-- **Parametric divisibility, complete biconditional (seventh review V16-01).**
Under the paper's witness conditions with positivity, `T ∣ n*x` holds
exactly when `y ∣ z` (with `y = (T + n*x)/u` and
`z = ((n*x)^2/T + n*x)/u`). Forward: `parametric_divisibility`.
Reverse: from `z*u*T = (n*x)*(y*u)` (multiply the witness identity by
`u*T`, then substitute `z*u = (n*x)^2/T + n*x` and `y*u = T + n*x`) cancel
`u > 0`, then substitute the assumed `y ∣ z` witness and cancel `y > 0`. -/
theorem parametric_divisibility_iff (n x T u : ℕ)
    (hu0 : 0 < u) (hnx : 0 < n * x) (hTpos : 0 < T)
    (hcopr : Nat.Coprime u (n * x))
    (hT2 : T ∣ (n * x) ^ 2)
    (hcong : u ∣ T + n * x) :
    T ∣ n * x ↔
      ((T + n * x) / u) ∣ ((n * x) ^ 2 / T + n * x) / u := by
  constructor
  · intro hTdivM
    exact parametric_divisibility n x T u hu0 hcopr hT2 hTdivM hcong
  · rintro ⟨k, hk⟩
    have hmul1 : ((n * x) ^ 2 / T) * T = (n * x) ^ 2 :=
      Nat.div_mul_cancel hT2
    have huz : u ∣ (n * x) ^ 2 / T + n * x := by
      have h5 : u ∣ ((n * x) ^ 2 / T) * (T + n * x) :=
        hcong.mul_left ((n * x) ^ 2 / T)
      have h5b : ((n * x) ^ 2 / T) * (T + n * x)
          = n * x * (n * x + (n * x) ^ 2 / T) := by
        linear_combination hmul1
      have h6 : u ∣ n * x * ((n * x) ^ 2 / T + n * x) := by
        rw [Nat.add_comm ((n * x) ^ 2 / T) (n * x), ← h5b]
        exact h5
      exact Nat.Coprime.dvd_of_dvd_mul_left hcopr h6
    have hz : ((n * x) ^ 2 / T + n * x) / u * u =
        ((n * x) ^ 2 / T + n * x) := Nat.div_mul_cancel huz
    have hsum : 0 < T + n * x := Nat.add_pos_left hTpos (n * x)
    have hy0 : 0 < (T + n * x) / u :=
      Nat.div_pos (Nat.le_of_dvd hsum hcong) hu0
    have hy : (T + n * x) / u * u = T + n * x :=
      Nat.div_mul_cancel hcong
    have hfinal : ((T + n * x) / u * (n * x)) * u = (n * x) * (T + n * x) := by
      calc ((T + n * x) / u * (n * x)) * u
          = ((T + n * x) / u) * ((n * x) * u) :=
            Nat.mul_assoc ((T + n * x) / u) (n * x) u
        _ = ((T + n * x) / u) * (u * (n * x)) := by
            rw [Nat.mul_comm (n * x) u]
        _ = (((T + n * x) / u) * u) * (n * x) := by
            rw [← Nat.mul_assoc ((T + n * x) / u) u (n * x)]
        _ = (T + n * x) * (n * x) := by rw [hy]
        _ = (n * x) * (T + n * x) := Nat.mul_comm (T + n * x) (n * x)
    have hcross : ((n * x) ^ 2 / T + n * x) / u * T * u =
        ((T + n * x) / u * (n * x)) * u := by
      calc ((n * x) ^ 2 / T + n * x) / u * T * u
          = ((n * x) ^ 2 / T + n * x) / u * (T * u) :=
            Nat.mul_assoc (((n * x) ^ 2 / T + n * x) / u) T u
        _ = ((n * x) ^ 2 / T + n * x) / u * (u * T) := by
            rw [Nat.mul_comm T u]
        _ = (((n * x) ^ 2 / T + n * x) / u * u) * T :=
            (Nat.mul_assoc (((n * x) ^ 2 / T + n * x) / u) u T).symm
        _ = ((n * x) ^ 2 / T + n * x) * T := by rw [hz]
        _ = ((n * x) ^ 2 / T) * T + (n * x) * T := Nat.add_mul _ _ _
        _ = (n * x) ^ 2 + (n * x) * T := by rw [hmul1]
        _ = (n * x) * (T + n * x) := by
            rw [Nat.mul_add (n * x) T (n * x)]
            ring
        _ = ((T + n * x) / u * (n * x)) * u := hfinal.symm
    have hkey : ((n * x) ^ 2 / T + n * x) / u * T
        = ((T + n * x) / u) * (n * x) := Nat.mul_right_cancel hu0 hcross
    have h9 : k * T = n * x := by
      rw [hk] at hkey
      rw [Nat.mul_assoc ((T + n * x) / u) k T] at hkey
      exact Nat.eq_of_mul_eq_mul_left hy0 hkey
    exact ⟨k, by rw [← h9, Nat.mul_comm k T]⟩
