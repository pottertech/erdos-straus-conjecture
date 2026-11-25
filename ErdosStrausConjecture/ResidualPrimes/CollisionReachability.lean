import Mathlib.Data.Nat.Totient
import Mathlib.Data.ZMod.Basic

/-!
# Residual Prime Structure: opposite-residue reachability (Paper 2, R4/R5)

Machine-checked statements underlying `research/residual_primes/`:

1. **Pigeonhole sufficiency.** For `0 < u` and `Nat.Coprime M u`, if the
   one-sided divisor-residue set of `M` modulo `u` is larger than half of the
   unit group of `ZMod u`, it contains two opposite residues.

2. **Collision form of the centered criterion.** With the centered product
   set defined as the quotient set `D·D⁻¹` (the ninth-review §5.3
   formulation), membership of `-1` is exactly an opposite-residue collision:
   exactly the existence of a pair `d₁ d₂ ∣ M` with `(d₁ + d₂) % u = 0`.

Scope: the factorization-window characterization of the centered product set
(`∏ q^[−e, e]`-products over the prime factorization of `M` equaling `D·D⁻¹`)
is the R4-lane extension and is NOT claimed here. This module is
self-contained Mathlib and uses no project axioms.
-/

namespace ResidualPrimes

variable (u M : ℕ)

/-- The one-sided divisor-residue set `D_u(M) = { d mod u : d ∣ M }`. -/
noncomputable def divResidues : Finset (ZMod u) :=
  (Nat.divisors M).image (fun (d : ℕ) => ((d : ZMod u)))

/-- The image of `D_u(M)` under additive negation. -/
noncomputable def negResidues : Finset (ZMod u) := (divResidues u M).image Neg.neg

/-- `D_u(M)` contains two opposite residues (the collision condition). -/
def hasOppositePair : Prop := (divResidues u M ∩ negResidues u M).Nonempty

/-- The collision-pair condition: two divisors of `M` whose residues add to
zero modulo `u`. -/
def hasCollisionPair : Prop :=
  ∃ d₁ d₂ : ℕ, d₁ ∣ M ∧ d₂ ∣ M ∧ (d₁ + d₂) % u = 0

/-- The centered product set, `D·D⁻¹` formulation: `z` is a quotient of two
divisor residues of `M`. -/
def InCentered (z : ZMod u) : Prop :=
  ∃ d₁ d₂ : ℕ, d₁ ∣ M ∧ d₂ ∣ M ∧ (d₁ : ZMod u) * (d₂ : ZMod u)⁻¹ = z

/-- A divisor of `M` is a unit in `ZMod u` whenever `gcd(M, u) = 1`. -/
theorem isUnit_of_dvd (hM : Nat.Coprime M u) (d : ℕ) (hd : d ∣ M) :
    IsUnit ((d : ZMod u)) :=
  (ZMod.isUnit_iff_coprime d u).mpr (hM.of_dvd_left hd)

/-- Negation preserves units in `ZMod u`. -/
theorem isUnit_neg_of {x : ZMod u} (h : IsUnit x) : IsUnit (-x) :=
  IsUnit.neg h

/-- Any finset of units in `ZMod u` has at most `φ(u)` members. -/
theorem card_le_totient_of_all_isUnit (hu : 0 < u) (s : Finset (ZMod u))
    (hall : ∀ x ∈ s, IsUnit x) : s.card ≤ Nat.totient u := by
  classical
  haveI : NeZero u := NeZero.of_gt hu
  set g : {x : ZMod u // x ∈ s} → (ZMod u)ˣ := fun y => (hall y.val y.property).unit with hg
  have hinj : Function.Injective g := by
    intro a b h
    apply Subtype.ext
    calc a.val = ((g a : (ZMod u)ˣ) : ZMod u) := rfl
      _ = ((g b : (ZMod u)ˣ) : ZMod u) := by rw [h]
      _ = b.val := rfl
  have hcard : Fintype.card {x : ZMod u // x ∈ s} = s.card := Fintype.card_coe s
  rw [← hcard]
  exact le_trans (Fintype.card_le_of_injective g hinj)
    (le_of_eq (ZMod.card_units_eq_totient u))

/-- `D ∪ (−D)` is a set of units (every member is a unit). -/
theorem isUnit_mem_union (hM : Nat.Coprime M u) (x : ZMod u)
    (hx : x ∈ divResidues u M ∪ negResidues u M) : IsUnit x := by
  rcases Finset.mem_union.mp hx with h | h
  · obtain ⟨d, hd, hdcast⟩ := Finset.mem_image.mp h
    rw [← hdcast]
    exact isUnit_of_dvd u M hM d (Nat.mem_divisors.mp hd).1
  · obtain ⟨y, hy, hycast⟩ := Finset.mem_image.mp h
    obtain ⟨d, hd, hdcast⟩ := Finset.mem_image.mp hy
    rw [← hycast, ← hdcast]
    exact isUnit_neg_of u (isUnit_of_dvd u M hM d (Nat.mem_divisors.mp hd).1)

/-- Additive negation preserves cardinality of the residue set. -/
theorem card_negResidues_eq :
    (negResidues u M).card = (divResidues u M).card := by
  have hinj : Set.InjOn (fun x : ZMod u => -x) (divResidues u M) := by
    intro a ha b hb h
    simpa using h
  simp only [negResidues, Finset.card_image_of_injOn hinj]

/-- **Pigeonhole sufficiency (Paper 2, R5).** If `D_u(M)` is larger than half
of the unit group, it contains two opposite residues. -/
theorem pigeonhole_reachability (hu : 0 < u) (hM : Nat.Coprime M u)
    (hcard : 2 * (divResidues u M).card > Nat.totient u) :
    hasOppositePair u M := by
  by_contra hno
  have hempty : (divResidues u M ∩ negResidues u M) = ∅ := by
    by_contra hc
    exact hno (Finset.nonempty_iff_ne_empty.mpr hc)
  have hdisj : Disjoint (divResidues u M) (negResidues u M) :=
    Finset.disjoint_iff_inter_eq_empty.mpr hempty
  have hbound : (divResidues u M ∪ negResidues u M).card ≤ Nat.totient u :=
    card_le_totient_of_all_isUnit u hu _ (fun x hx => isUnit_mem_union u M hM x hx)
  have hsum : (divResidues u M ∪ negResidues u M).card =
      (divResidues u M).card + (negResidues u M).card :=
    Finset.card_union_of_disjoint hdisj
  rw [hsum, card_negResidues_eq u M] at hbound
  omega

/-- The collision-pair condition and the opposite-residue condition are
equivalent: a pair of divisors with `(d₁ + d₂) % u = 0` is exactly an
opposite-residue collision in `D_u(M)`. -/
theorem hasOppositePair_iff_collisionPair (hM0 : 0 < M) :
    hasOppositePair u M ↔ hasCollisionPair u M := by
  constructor
  · rintro ⟨x, hx⟩
    have hxpair : x ∈ divResidues u M ∧ x ∈ negResidues u M := Finset.mem_inter.mp hx
    obtain ⟨d₁, hd₁, hd₁cast⟩ := Finset.mem_image.mp hxpair.left
    obtain ⟨y, hy, hycast⟩ := Finset.mem_image.mp hxpair.right
    obtain ⟨d₂, hd₂, hd₂cast⟩ := Finset.mem_image.mp hy
    have hd₁dvd : d₁ ∣ M := (Nat.mem_divisors.mp hd₁).1
    have hd₂dvd : d₂ ∣ M := (Nat.mem_divisors.mp hd₂).1
    refine ⟨d₁, d₂, hd₁dvd, hd₂dvd, ?_⟩
    have hcast : ((d₁ + d₂ : ℕ) : ZMod u) = 0 := by
      rw [Nat.cast_add d₁ d₂, hd₁cast, ← hycast, hd₂cast, neg_add_cancel]
    exact Nat.dvd_iff_mod_eq_zero.mp
      ((ZMod.natCast_eq_zero_iff (d₁ + d₂) u).mp hcast)
  · rintro ⟨d₁, d₂, hd₁, hd₂, hpair⟩
    have hcast : ((d₁ + d₂ : ℕ) : ZMod u) = 0 :=
      (ZMod.natCast_eq_zero_iff (d₁ + d₂) u).mpr
        (Nat.dvd_iff_mod_eq_zero.mpr hpair)
    have hdeq : (d₁ : ZMod u) = -(d₂ : ZMod u) := by
      have hsum : (d₁ : ZMod u) + (d₂ : ZMod u) = 0 :=
        ((Nat.cast_add d₁ d₂).symm).trans hcast
      calc (d₁ : ZMod u)
          = (d₁ : ZMod u) + (d₂ : ZMod u) + -(d₂ : ZMod u) := by ring
        _ = -(d₂ : ZMod u) := by rw [hsum]; ring
    have hmpr1 : d₁ ∈ Nat.divisors M := Nat.mem_divisors.mpr ⟨hd₁, ne_of_gt hM0⟩
    have hmpr2 : d₂ ∈ Nat.divisors M := Nat.mem_divisors.mpr ⟨hd₂, ne_of_gt hM0⟩
    exact ⟨(d₁ : ZMod u), Finset.mem_inter.mpr
      ⟨Finset.mem_image.mpr ⟨d₁, hmpr1, rfl⟩,
        Finset.mem_image.mpr ⟨(d₂ : ZMod u),
          Finset.mem_image.mpr ⟨d₂, hmpr2, rfl⟩, hdeq.symm⟩⟩⟩

/-- With `gcd(M, u) = 1`, membership of `-1` in the centered product set
`D·D⁻¹` is exactly the collision-pair condition. -/
theorem mem_centered_neg_one_iff_collisionPair (hM : Nat.Coprime M u) :
    InCentered u M (-1) ↔ hasCollisionPair u M := by
  constructor
  · rintro ⟨d₁, d₂, hd₁, hd₂, hprod⟩
    have hun₂ : IsUnit ((d₂ : ZMod u)) := isUnit_of_dvd u M hM d₂ hd₂
    have hinv : (d₂ : ZMod u)⁻¹ * (d₂ : ZMod u) = 1 := ZMod.inv_mul_of_unit _ hun₂
    refine ⟨d₁, d₂, hd₁, hd₂, ?_⟩
    have hdeq : (d₁ : ZMod u) = -(d₂ : ZMod u) := by
      calc (d₁ : ZMod u)
          = (d₁ : ZMod u) * ((d₂ : ZMod u)⁻¹ * (d₂ : ZMod u)) := by rw [hinv, mul_one]
        _ = ((d₁ : ZMod u) * (d₂ : ZMod u)⁻¹) * (d₂ : ZMod u) := by ring
        _ = (-(1 : ZMod u)) * (d₂ : ZMod u) := by rw [hprod]
        _ = -(d₂ : ZMod u) := by ring
    have hcast : ((d₁ + d₂ : ℕ) : ZMod u) = 0 := by
      rw [Nat.cast_add d₁ d₂, hdeq, neg_add_cancel]
    exact Nat.dvd_iff_mod_eq_zero.mp
      ((ZMod.natCast_eq_zero_iff (d₁ + d₂) u).mp hcast)
  · rintro ⟨d₁, d₂, hd₁, hd₂, hpair⟩
    have hun₂ : IsUnit ((d₂ : ZMod u)) := isUnit_of_dvd u M hM d₂ hd₂
    have hcast : ((d₁ + d₂ : ℕ) : ZMod u) = 0 :=
      (ZMod.natCast_eq_zero_iff (d₁ + d₂) u).mpr
        (Nat.dvd_iff_mod_eq_zero.mpr hpair)
    have hdeq : (d₁ : ZMod u) = -(d₂ : ZMod u) := by
      have hsum : (d₁ : ZMod u) + (d₂ : ZMod u) = 0 :=
        ((Nat.cast_add d₁ d₂).symm).trans hcast
      calc (d₁ : ZMod u)
          = (d₁ : ZMod u) + (d₂ : ZMod u) + -(d₂ : ZMod u) := by ring
        _ = -(d₂ : ZMod u) := by rw [hsum]; ring
    exact ⟨d₁, d₂, hd₁, hd₂, by
      calc (d₁ : ZMod u) * (d₂ : ZMod u)⁻¹
          = -(d₂ : ZMod u) * (d₂ : ZMod u)⁻¹ := by rw [hdeq]
        _ = -((d₂ : ZMod u) * (d₂ : ZMod u)⁻¹) := by ring
        _ = -(1 : ZMod u) := by rw [ZMod.mul_inv_of_unit _ hun₂]
        _ = (-1 : ZMod u) := by ring⟩

/-- The review's boxed criterion `D ∩ (−D) ≠ ∅` is exactly membership of
`-1` in the centered product set `D·D⁻¹`. -/
theorem hasOppositePair_iff_centered_neg_one (hu : 0 < u)
    (hM0 : 0 < M) (hM : Nat.Coprime M u) :
    hasOppositePair u M ↔ InCentered u M (-1) :=
  ⟨fun h => (mem_centered_neg_one_iff_collisionPair u M hM).mpr
      ((hasOppositePair_iff_collisionPair u M hM0).mp h),
   fun h => (hasOppositePair_iff_collisionPair u M hM0).mpr
      ((mem_centered_neg_one_iff_collisionPair u M hM).mp h)⟩

end ResidualPrimes
