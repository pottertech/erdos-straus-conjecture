import Mathlib
import ErdosStrausConjecture.ResidualPrimes.CollisionReachability

/-!
# Residual Prime Structure: the factorization-window form (Paper 2, R4-lane extension)

The centered product set in the span-window form: an element `z` is a
window-span product

`z = ∏ q^{t_q} (mod u), written with t_q = a_q − b_q, 0 ≤ a_q, b_q ≤ e_q,`

for `e_q` the exponents in `M`'s factorization — if and only if `z` is a
quotient `D·D⁻¹` of two divisor residues of `M` (the ninth review's §5.3
formulation, already machine-checked against the collision condition in
`CollisionReachability.lean`).

No coprimality is needed for the formal identity: the two encodings are the
same set. Under the Paper-1 admissibility hypothesis `gcd(M, u) = 1` every
factor `q ∣ M` is a unit of `ZMod u`, so the quotient form is the span.
-/

namespace ResidualPrimes

/-- Casting a Finsupp product distributes over the product (leaf casts). -/
theorem cast_prod_finsupp (u : ℕ) (f : ℕ →₀ ℕ) :
    ((f.prod (fun (x y : ℕ) => ((x ^ y : ℕ) : ZMod u)))) =
      (((f.prod (fun (x y : ℕ) => (x ^ y : ℕ))) : ℕ) : ZMod u) := by
  simp

/-- The factorization-window span of `M` equals the centered quotient set
`D·D⁻¹`. -/
theorem window_iff_inCentered (M u : ℕ) (hM0 : 0 < M) (z : ZMod u) :
    (∃ f g : ℕ →₀ ℕ, f ≤ M.factorization ∧ g ≤ M.factorization ∧
      ((f.prod (fun q e : ℕ => (((q ^ e : ℕ)) : ZMod u)))) *
        (((g.prod (fun q e : ℕ => (((q ^ e : ℕ)) : ZMod u))))⁻¹) = z) ↔
    InCentered u M z := by
  constructor
  · rintro ⟨f, g, hf, hg, hval⟩
    have hA : (((f.prod (· ^ ·)) : ℕ) : ZMod u) =
        f.prod (fun q e : ℕ => (((q ^ e : ℕ)) : ZMod u)) :=
      (cast_prod_finsupp u f).symm
    have hB : (((g.prod (· ^ ·)) : ℕ) : ZMod u) =
        g.prod (fun q e : ℕ => (((q ^ e : ℕ)) : ZMod u)) :=
      (cast_prod_finsupp u g).symm
    refine ⟨f.prod (· ^ ·), g.prod (· ^ ·),
      Nat.prod_pow_dvd_of_le_factorization hf,
      Nat.prod_pow_dvd_of_le_factorization hg, ?_⟩
    rw [hA, hB]
    exact hval
  · rintro ⟨d₁, d₂, hd₁, hd₂, hval⟩
    have hd10 : d₁ ≠ 0 := by
      intro hc
      rw [hc] at hd₁
      obtain ⟨c, hc2⟩ := hd₁
      rw [Nat.zero_mul] at hc2
      exact hM0.ne hc2.symm
    have hd20 : d₂ ≠ 0 := by
      intro hc
      rw [hc] at hd₂
      obtain ⟨c, hc2⟩ := hd₂
      rw [Nat.zero_mul] at hc2
      exact hM0.ne hc2.symm
    have hfb : d₁.factorization ≤ M.factorization :=
      (Nat.factorization_le_iff_dvd hd10 (ne_of_gt hM0)).mpr hd₁
    have hgb : d₂.factorization ≤ M.factorization :=
      (Nat.factorization_le_iff_dvd hd20 (ne_of_gt hM0)).mpr hd₂
    refine ⟨d₁.factorization, d₂.factorization, hfb, hgb, ?_⟩
    have leaf1 : (d₁.factorization.prod
        (fun (q e : ℕ) => (((q ^ e : ℕ)) : ZMod u))) = ((d₁ : ZMod u)) := by
      rw [cast_prod_finsupp u d₁.factorization,
        Nat.prod_factorization_pow_eq_self hd10]
    have leaf2 : (d₂.factorization.prod
        (fun (q e : ℕ) => (((q ^ e : ℕ)) : ZMod u))) = ((d₂ : ZMod u)) := by
      rw [cast_prod_finsupp u d₂.factorization,
        Nat.prod_factorization_pow_eq_self hd20]
    rw [leaf1, leaf2]
    exact hval

end ResidualPrimes
