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

/-- The CRT decode: the pair `(r mod 3, r mod 5)` of a residue. -/
def crtPair (r : ℕ) : ℕ × ℕ := (r % 3, r % 5)

/-- **The divisor-residue set** `D_u(M) = { d mod u : d ∣ M }`, as the
image of the natural-divisor Finset. -/
def uDset (u M : ℕ) : Finset ℕ := (Nat.divisors M).image (fun d => d % u)

/-- The membership elimination for `uDset`: a realized residue comes from a
divisor (which exists only when `M ≠ 0`). -/
theorem uDset_mem_elim {u M r : ℕ} (h : r ∈ uDset u M) :
    ∃ d, d ∣ M ∧ M ≠ 0 ∧ d % u = r := by
  simp only [uDset, Finset.mem_image] at h
  obtain ⟨d, hdvd, hmod⟩ := h
  have ⟨hdvd, hM0⟩ : d ∣ M ∧ M ≠ 0 := Nat.mem_divisors.mp hdvd
  exact ⟨d, hdvd, hM0, hmod⟩

/-- The membership introduction for `uDset`. -/
theorem uDset_mem_of_dvd {u M d : ℕ} (hd : d ∣ M) (hM : M ≠ 0) :
    d % u ∈ uDset u M :=
  Finset.mem_image.mpr ⟨d, Nat.mem_divisors.mpr ⟨hd, hM⟩, rfl⟩

/-- **The CRT decode is injective on the residues below 15** (the
distinct mod-15 residues carry distinct `(3, 5)`-pairs). -/
theorem crtPair_injOn15 : Set.InjOn crtPair (Finset.range 15) := by
  intro r hr r' hr' h
  simp only [crtPair, Prod.mk.injEq] at h
  have hlt : r < 15 := Finset.mem_range.mp hr
  have hlt' : r' < 15 := Finset.mem_range.mp hr'
  omega

/-- **The composite-layer deficit bound (E-030/E-031 as a theorem).** The
divisor-residue set at `u = 15` never exceeds the product of the layer sets
at 3 and 5: every realized pair is a member of both layer sets, and the CRT
decode is injective on the residues (so the image does not collapse). This
is exactly the nonnegativity of the E-030 census deficit
`|D3| * |D5| - |D15|`. -/
theorem uDset15_card_le (M : ℕ) :
    (uDset 15 M).card ≤ (uDset 3 M).card * (uDset 5 M).card := by
  have hinj : Set.InjOn crtPair (uDset 15 M) := by
    refine crtPair_injOn15.mono ?_
    intro a ha
    obtain ⟨d, hdvd, hM0, hmod⟩ := uDset_mem_elim ha
    exact Finset.mem_coe.mpr (Finset.mem_range.mpr (by omega))
  have hcard : ((uDset 15 M).image crtPair).card = (uDset 15 M).card :=
    Finset.card_image_of_injOn hinj
  have hsub : (uDset 15 M).image crtPair ⊆ uDset 3 M ×ˢ uDset 5 M := by
    intro w hw
    simp only [Finset.mem_image] at hw
    obtain ⟨r, hr, hwr⟩ := hw
    obtain ⟨d, hdvd, hM0, hmod⟩ := uDset_mem_elim hr
    have h3m : r % 3 = d % 3 := by omega
    have h5m : r % 5 = d % 5 := by omega
    refine Finset.mem_product.mpr ⟨?_, ?_⟩
    · rw [← hwr, crtPair, h3m]
      exact uDset_mem_of_dvd hdvd hM0
    · rw [← hwr, crtPair, h5m]
      exact uDset_mem_of_dvd hdvd hM0
  have hle := Finset.card_le_card hsub
  rw [hcard, Finset.card_product] at hle
  exact hle

/-- The CRT decode at the coprime pair `(a, b)`. -/
def crtPair2 (a b : ℕ) (r : ℕ) : ℕ × ℕ := (r % a, r % b)

/-- **The composite-layer deficit bound, general (E-047).** For nonzero
coprime moduli `a, b`: `(uDset (a * b) M).card <= (uDset a M).card *
(uDset b M).card` - the CRT decode `(r % a, r % b)` is injective on the
realized residues (the coprime modular equations compose one-way via
`Nat.modEq_and_modEq_iff_modEq_mul`, and the bounded range closes it),
and every realized pair routes through both layer sets
(`Nat.mod_mod_of_dvd`). This subsumes the u = 15 bound and gives the
u = 35 bound (5 x 7) as a corollary. -/
theorem uDset_coprime_card_le (a b M : ℕ) (ha0 : a ≠ 0) (hb0 : b ≠ 0)
    (hab : Nat.Coprime a b) :
    (uDset (a * b) M).card ≤ (uDset a M).card * (uDset b M).card := by
  have hab0 : a * b ≠ 0 := by
    intro h
    rcases mul_eq_zero.mp h with h' | h'
    · exact ha0 h'
    · exact hb0 h'
  -- the decode is injective on Dset (a * b)
  have hinj : Set.InjOn (crtPair2 a b) (uDset (a * b) M) := by
    intro r hr r' hr' h
    simp only [crtPair2, Prod.mk.injEq] at h
    obtain ⟨d, hdvd, hM0, hmod⟩ := uDset_mem_elim hr
    obtain ⟨d', hdvd', hM0', hmod'⟩ := uDset_mem_elim hr'
    -- the pairs equal: (r % a, r % b) = (r' % a, r' % b)
    have ha : r % a = r' % a := h.1
    have hb : r % b = r' % b := h.2
    -- route the residues back through the divisors
    have hda : (d % (a * b)) % a = d % a :=
      Nat.mod_mod_of_dvd d (Nat.dvd_mul_right a b)
    have hdb : (d % (a * b)) % b = d % b :=
      Nat.mod_mod_of_dvd d (Nat.dvd_mul_left b a)
    have hda' : (d' % (a * b)) % a = d' % a :=
      Nat.mod_mod_of_dvd d' (Nat.dvd_mul_right a b)
    have hdb' : (d' % (a * b)) % b = d' % b :=
      Nat.mod_mod_of_dvd d' (Nat.dvd_mul_left b a)
    have ha2 : r % a = d % a := by rw [← hmod]; exact hda
    have hb2 : r % b = d % b := by rw [← hmod]; exact hdb
    have ha2' : r' % a = d' % a := by rw [← hmod']; exact hda'
    have hb2' : r' % b = d' % b := by rw [← hmod']; exact hdb'
    -- the two modular equations on d, d'
    have q1 : d ≡ d' [MOD a] := by
      simp only [Nat.ModEq]
      rw [← ha2, ← ha2']
      exact ha
    have q2 : d ≡ d' [MOD b] := by
      simp only [Nat.ModEq]
      rw [← hb2, ← hb2']
      exact hb
    -- the coprime composition
    have hcomp2 : d ≡ d' [MOD a * b] :=
      (Nat.modEq_and_modEq_iff_modEq_mul hab).mp (And.intro q1 q2)
    simp only [Nat.ModEq] at hcomp2
    -- r = d % (a*b) and r' = d' % (a*b), so the composition closes
    exact by rw [← hmod, ← hmod']; exact hcomp2
  have hcard : ((uDset (a * b) M).image (crtPair2 a b)).card =
      (uDset (a * b) M).card := Finset.card_image_of_injOn hinj
  -- the image lands in the product of the two layer sets
  have hsub : (uDset (a * b) M).image (crtPair2 a b) ⊆
      uDset a M ×ˢ uDset b M := by
    intro w hw
    simp only [Finset.mem_image] at hw
    obtain ⟨r, hr, hwr⟩ := hw
    obtain ⟨d, hdvd, hM0, hmod⟩ := uDset_mem_elim hr
    have hda : (d % (a * b)) % a = d % a :=
      Nat.mod_mod_of_dvd d (Nat.dvd_mul_right a b)
    have hdb : (d % (a * b)) % b = d % b :=
      Nat.mod_mod_of_dvd d (Nat.dvd_mul_left b a)
    refine Finset.mem_product.mpr ⟨?_, ?_⟩
    · rw [← hwr, ← hmod]
      simp only [crtPair2]
      rw [hda]
      exact uDset_mem_of_dvd hdvd hM0
    · rw [← hwr, ← hmod]
      simp only [crtPair2]
      rw [hdb]
      exact uDset_mem_of_dvd hdvd hM0
  have hle := Finset.card_le_card hsub
  rw [hcard, Finset.card_product] at hle
  exact hle

/-- **The u = 35 deficit bound** (the E-047 corollary at 5 x 7). -/
theorem uDset35_card_le (M : ℕ) :
    (uDset 35 M).card ≤ (uDset 5 M).card * (uDset 7 M).card :=
  uDset_coprime_card_le 5 7 M (by decide) (by decide) (by decide)

/-- **The CRT-pair membership (the mem-level forward fact).** Every divisor-
realized residue at the composite modulus has its `crtPair2` pair in both
layer sets (the mem-level form of the E-047 image-bound route). -/
theorem uDset_mem_crt_pair {a b M r : ℕ} {d : ℕ} (hd : d ∣ M) (hM : M ≠ 0)
    (hr : d % (a * b) = r) :
    r % a ∈ uDset a M ∧ r % b ∈ uDset b M := by
  have hda : (d % (a * b)) % a = d % a :=
    Nat.mod_mod_of_dvd d (Nat.dvd_mul_right a b)
  have hdb : (d % (a * b)) % b = d % b :=
    Nat.mod_mod_of_dvd d (Nat.dvd_mul_left b a)
  refine ⟨?_, ?_⟩
  · rw [← hr, hda]
    exact uDset_mem_of_dvd hd hM
  · rw [← hr, hdb]
    exact uDset_mem_of_dvd hd hM

/-- **The CRT decode is injective on the bounded residues, generally.**
Two residues below `a * b` carrying the same `(mod a, mod b)`-pair are
equal — for coprime `a, b` (the general form of
`crtPair_injOn15`, the exact site of the CRT deficit formalization: the
pair map is a bijection onto the bounded pairs; which pairs lie in the
layer-set image is the divisor-realization question). -/
theorem crtPair2_injOn_lt {a b : ℕ} (hab : Nat.Coprime a b) :
    Set.InjOn (crtPair2 a b) (Finset.range (a * b)) := by
  intro d hd d' hd' h
  have hltd : d < a * b := Finset.mem_range.mp hd
  have hltd' : d' < a * b := Finset.mem_range.mp hd'
  simp only [crtPair2, Prod.mk.injEq] at h
  have ha : d % a = d' % a := h.1
  have hb : d % b = d' % b := h.2
  have q1 : d ≡ d' [MOD a] := by
    simp only [Nat.ModEq]
    exact ha
  have q2 : d ≡ d' [MOD b] := by
    simp only [Nat.ModEq]
    exact hb
  have hcomp : d ≡ d' [MOD a * b] :=
    (Nat.modEq_and_modEq_iff_modEq_mul hab).mp (And.intro q1 q2)
  simp only [Nat.ModEq] at hcomp
  have hm : d % (a * b) = d := Nat.mod_eq_of_lt hltd
  have hm' : d' % (a * b) = d' := Nat.mod_eq_of_lt hltd'
  rw [hm, hm'] at hcomp
  exact hcomp

/-- The coprime divisor split: every divisor of `m₁ * m₂` factors through
coprime-factor divisors (the surjection underpinning the fold). -/
theorem divisors_split_mem {m₁ m₂ d : ℕ} (hcop : Nat.Coprime m₁ m₂)
    (hd : d ∣ m₁ * m₂) :
    ∃ d₁ d₂, d₁ ∣ m₁ ∧ d₂ ∣ m₂ ∧ d = d₁ * d₂ := by
  refine ⟨d.gcd m₁, d.gcd m₂, ?_, ?_, ?_⟩
  · exact Nat.gcd_dvd_right d m₁
  · exact Nat.gcd_dvd_right d m₂
  · exact ((Nat.gcd_mul_gcd_eq_iff_dvd_mul_of_coprime hcop).mpr hd).symm

/-- **The fold skeleton.** The divisor-residue set at the product of coprime
factors is generated exactly by the divisor-pair product: `uDset u (m₁ * m₂)`
is the image of the divisor-product under `(d₁, d₂) ↦ (d₁ * d₂) % u`. This is
the fold form (the E-031 algebra's first structural layer). -/
theorem uDset_fold_image (u m₁ m₂ : ℕ) (hcop : Nat.Coprime m₁ m₂) :
    uDset u (m₁ * m₂) =
    ((Nat.divisors m₁ ×ˢ Nat.divisors m₂).image (fun q => (q.1 * q.2) % u)) := by
  apply Finset.ext
  intro r
  constructor
  · -- ⊆: a divisor of the product splits and its residue is generated
    intro hr
    obtain ⟨d, hdvd, hM0, hmod⟩ := uDset_mem_elim hr
    obtain ⟨d₁, d₂, hd₁, hd₂, hdd⟩ := divisors_split_mem hcop hdvd
    have ha0 : m₁ ≠ 0 := fun h => hM0 (by rw [h]; exact zero_mul m₂)
    have hb0 : m₂ ≠ 0 := fun h => hM0 (by rw [h]; exact mul_zero m₁)
    have hpair : (d₁, d₂) ∈ Nat.divisors m₁ ×ˢ Nat.divisors m₂ :=
      Finset.mem_product.mpr ⟨Nat.mem_divisors.mpr ⟨hd₁, ha0⟩,
        Nat.mem_divisors.mpr ⟨hd₂, hb0⟩⟩
    refine Finset.mem_image.mpr ⟨(d₁, d₂), hpair, ?_⟩
    rw [← hmod, hdd]
  · -- ⊇: every divisor pair's product is a divisor of the product
    intro hr
    obtain ⟨q, hq, hqr⟩ := Finset.mem_image.mp hr
    obtain ⟨hd₁, hd₂⟩ := Finset.mem_product.mp hq
    obtain ⟨hd₁', hM1⟩ := Nat.mem_divisors.mp hd₁
    obtain ⟨hd₂', hM2⟩ := Nat.mem_divisors.mp hd₂
    have hdvd : q.1 * q.2 ∣ m₁ * m₂ := Nat.mul_dvd_mul hd₁' hd₂'
    rw [← hqr]
    exact uDset_mem_of_dvd hdvd (mul_ne_zero hM1 hM2)

/-- **The fold's CRT-pair form (the E-031 algebra).** The realized
`(3, 5)`-pairs at the composite layer are exactly the image of the
divisor-product under the paired residue map — the exact statement of the
census algebra `U15ALG mismatch = 0` (the pair windows ARE the fold, no
residue is generated outside it). -/
theorem crtPair_fold_image15 (m₁ m₂ : ℕ) (hcop : Nat.Coprime m₁ m₂) :
    ((uDset 15 (m₁ * m₂)).image crtPair) =
    ((Nat.divisors m₁ ×ˢ Nat.divisors m₂).image
      (fun q => ((q.1 * q.2) % 3, (q.1 * q.2) % 5))) := by
  -- the fold skeleton rewrites the left image's underlying set
  rw [uDset_fold_image 15 m₁ m₂ hcop]
  -- compose the two images into one map
  rw [Finset.image_image]
  refine Finset.image_congr ?_
  intro q _
  have h3 : ((q.1 * q.2) % 15) % 3 = (q.1 * q.2) % 3 :=
    Nat.mod_mod_of_dvd _ (by decide : 3 ∣ 15)
  have h5 : ((q.1 * q.2) % 15) % 5 = (q.1 * q.2) % 5 :=
    Nat.mod_mod_of_dvd _ (by decide : 5 ∣ 15)
  simp only [Function.comp_apply, crtPair]
  rw [h3, h5]

/-- **The fold's deficit corollary.** The composite layer's residues never
exceed the FULL divisor-product count
`∏ (e_q + 1)`): the CRT decode is injective on the bounded residues, and the
fold's pair form realizes the decode image exactly as the divisor-product's
pair image, whose card is bounded by the product's own count. -/
theorem uDset15_card_le_fold (m₁ m₂ : ℕ) (hcop : Nat.Coprime m₁ m₂) :
    (uDset 15 (m₁ * m₂)).card ≤
      (Nat.divisors m₁).card * (Nat.divisors m₂).card := by
  have hlt : ∀ r ∈ uDset 15 (m₁ * m₂), r < 15 := by
    intro r hr
    obtain ⟨d, _, _, hmod⟩ := uDset_mem_elim hr
    exact hmod ▸ Nat.mod_lt d (by omega)
  have hinj : Set.InjOn crtPair (uDset 15 (m₁ * m₂)) :=
    crtPair_injOn15.mono (fun r hr => Finset.mem_coe.mpr (Finset.mem_range.mpr (hlt r hr)))
  have hcard : ((uDset 15 (m₁ * m₂)).image crtPair).card =
      (uDset 15 (m₁ * m₂)).card := Finset.card_image_of_injOn hinj
  have hpair := crtPair_fold_image15 m₁ m₂ hcop
  have h3 : ((Nat.divisors m₁ ×ˢ Nat.divisors m₂).image
        (fun q => ((q.1 * q.2) % 3, (q.1 * q.2) % 5))).card ≤
      (Nat.divisors m₁ ×ˢ Nat.divisors m₂).card := Finset.card_image_le
  rw [Finset.card_product] at h3

  calc (uDset 15 (m₁ * m₂)).card
      = ((uDset 15 (m₁ * m₂)).image crtPair).card := hcard.symm
    _ = ((Nat.divisors m₁ ×ˢ Nat.divisors m₂).image
          (fun q => ((q.1 * q.2) % 3, (q.1 * q.2) % 5))).card :=
        congrArg Finset.card hpair
    _ ≤ (Nat.divisors m₁).card * (Nat.divisors m₂).card := h3

/-- **The fold's CRT-pair form, general (any composite layer).** For a
composite modulus `u₁ * u₂` of nonzero coprime factors, the realized
`(u₁, u₂)`-pairs of the divisor-residue set at the fold of coprime factors
are exactly the image of the divisor-product under the paired residue map —
the general form of `crtPair_fold_image15` (the census algebra's exactness
at every admissible layer). -/
theorem crtPair2_fold_image (u₁ u₂ m₁ m₂ : ℕ) (hcop : Nat.Coprime m₁ m₂) :
    ((uDset (u₁ * u₂) (m₁ * m₂)).image (crtPair2 u₁ u₂)) =
    ((Nat.divisors m₁ ×ˢ Nat.divisors m₂).image
      (fun q => ((q.1 * q.2) % u₁, (q.1 * q.2) % u₂))) := by
  rw [uDset_fold_image (u₁ * u₂) m₁ m₂ hcop]
  rw [Finset.image_image]
  refine Finset.image_congr ?_
  intro q _
  have h1 : ((q.1 * q.2) % (u₁ * u₂)) % u₁ = (q.1 * q.2) % u₁ :=
    Nat.mod_mod_of_dvd _ (Nat.dvd_mul_right u₁ u₂)
  have h2 : ((q.1 * q.2) % (u₁ * u₂)) % u₂ = (q.1 * q.2) % u₂ :=
    Nat.mod_mod_of_dvd _ (Nat.dvd_mul_left u₂ u₁)
  simp only [Function.comp_apply, crtPair2]
  rw [h1, h2]

/-- **The strengthened general fold deficit corollary.** The divisor-residue
set at **any** layer `u` never exceeds the folded factorization's
divisor-product count, with **no hypothesis on the u side**: the residue
map is an image of the divisor set, so its card is bounded by the divisor
count outright via `Finset.card_image_le`, and the exact equality
`Nat.Coprime.card_divisors_mul` splits that count over the coprime
factors. This is the Emily-brute-force strengthening's first step: the
remaining candidate drop is the `m`-coprimality (the divisor-count
inequality `τ(m₁ * m₂) ≤ τ(m₁) · τ(m₂)` for all factors), recorded
as the remaining staged strengthening. -/
theorem uDset_card_le_fold' (u m₁ m₂ : ℕ) (hcop : Nat.Coprime m₁ m₂) :
    (uDset u (m₁ * m₂)).card ≤
      (Nat.divisors m₁).card * (Nat.divisors m₂).card := by
  have h2 : (Nat.divisors (m₁ * m₂)).card =
      (Nat.divisors m₁).card * (Nat.divisors m₂).card :=
    hcop.card_divisors_mul
  calc (uDset u (m₁ * m₂)).card
      ≤ (Nat.divisors (m₁ * m₂)).card := Finset.card_image_le
    _ ≤ (Nat.divisors m₁).card * (Nat.divisors m₂).card := by rw [h2]

/-- **The mod-15 2-power-orbit closure (the fail-shape window-cell fact).**
A positive integer all of whose prime divisors lie in the mod-15
2-power orbit `{1, 2, 4, 8}` (the cyclic `⟨2⟩ ⊂ (ZMod 15)×`) is itself in
that orbit: the divisor-status induction, with the 4 × 4 product cases
closing (the orbit is closed under multiplication mod 15). This is the
exact cell set of the E-029 fail-shape census (`D`-sets inside
`{1, 2, 4, 8}`). -/
theorem prod_in_clo4_mod15 (T : ℕ) (hT0 : 0 < T)
    (hall : ∀ q : ℕ, q.Prime → q ∣ T →
      (q % 15 = 1 ∨ q % 15 = 2 ∨ q % 15 = 4 ∨ q % 15 = 8)) :
    T % 15 = 1 ∨ T % 15 = 2 ∨ T % 15 = 4 ∨ T % 15 = 8 := by
  have key : ∀ t : ℕ, t ≤ T → 0 < t →
      (∀ q : ℕ, q.Prime → q ∣ t →
        (q % 15 = 1 ∨ q % 15 = 2 ∨ q % 15 = 4 ∨ q % 15 = 8)) →
      t % 15 = 1 ∨ t % 15 = 2 ∨ t % 15 = 4 ∨ t % 15 = 8 := by
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
              (r % 15 = 1 ∨ r % 15 = 2 ∨ r % 15 = 4 ∨ r % 15 = 8) :=
            fun r hr hrd => hall' r hr (hrd.trans htdq)
          have hrec := ih (t / q) hlt hlqT htq0 hall2
          have hqres := hall' q hqp hqt
          have hdiv : t = (t / q) * q := (Nat.div_mul_cancel hqt).symm
          rw [hdiv]
          rcases hrec with e | e | e | e
          · rcases hqres with k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
          · rcases hqres with k | k | k | k
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
            · rw [Nat.mul_mod, e, k]; norm_num
  exact key T (Nat.le_refl T) hT0 hall

/-- The τ-inequality pointwise step per prime:
`(a + b + 1) ≤ (a + 1) * (b + 1)` for naturals (the additive exponent
split is dominated by the multiplicative count product at every prime). -/
theorem count_add_le_count_mul (a b : ℕ) : a + b + 1 ≤ (a + 1) * (b + 1) := by
  have hx : (a + 1) * (b + 1) = a * b + a + b + 1 := by ring
  omega

end ResidualPrimes


