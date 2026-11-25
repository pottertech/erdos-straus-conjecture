import Mathlib
import ErdosStrausConjecture.CenteredCriterion
import ErdosStrausConjecture.ResidualPrimes.CollisionReachability

/-!
# Residual Prime Structure: the u = 7 layer (Paper 2, R8 piece 4)

The u = 7-layer counterpart of `U3Boundary`, the formal counterpart of the
E-013 empirical census (`research/residual_primes/`, engine v0.9). Within
the (H24) sweep class (â¡ 1 (mod 24)), the u = 7 layer census splits the
records by the prime's residue mod 7: at `p ≡ 3, 5, 6 (mod 7)` the
u = 7 pigeon/s span conditions hold for EVERY record (probe and full-run
0-mismatch), and the failure classes are exactly `p ≡ 1, 2, 4 (mod 7)`.

Formalized here (self-contained Mathlib + the audited u-method core and
collision-reachability module):

1. `u7_span_of_mod7_three` - for `4·x = n + 7`, `n ≡ 3 (mod 7)`,
   the u = 7 span criterion holds at `T = n` (constructive).
2. `u7_span_of_mod7_six` - the same at `n ≡ 6 (mod 7)` with `T = x`.
3. `u7_pigeon_of_mod7_three`, `u7_pigeon_of_mod7_five`,
   `u7_pigeon_of_mod7_six` - for `n ≡ 3, 5, 6 (mod 7)` the residual
   classes are PIGEON-conclusive at `u = 7`: the divisor-residue set of
   `n·x` contains four distinct residues (`{1, n, x, n·x}` at
   `3/6`; `{1, n, x, 2}` at `5`, using `2 ∣ x`, which holds for the
   sweep's `n ≡ 1 (mod 8)` family), so
   `2|D| > φ(7)`, and the audited `pigeonhole_reachability` turns the
   cardinality bound into the collision certificate.
-/

namespace ResidualPrimes

/-- The u = 7 span-side criterion: a span candidate `T` dividing `(n·x)^2`
with `T + n·x ≡ 0 (mod 7)`. -/
def u7Span (n x : ℕ) : Prop := ∃ T : ℕ, T ∣ (n * x) ^ 2 ∧ (T + n * x) % 7 = 0

/-- Membership bridge: a divisor `d` of `M` (with `M > 0`) contributes its
cast as a member of the divisor-residue finset. -/
theorem mem_divResidues (u M d : ℕ) (hd : d ∣ M) (hM0 : 0 < M) :
    ((d : ℕ) : ZMod u) ∈ divResidues u M :=
  Finset.mem_image.mpr ⟨d, Nat.mem_divisors.mpr ⟨hd, ne_of_gt hM0⟩, rfl⟩

/-- Distinctness bridge: unequal residues cast to unequal `ZMod` elements. -/
theorem cast_ne_of_mod_ne (a b k : ℕ) (h : a % k ≠ b % k) :
    ((a : ℕ) : ZMod k) ≠ ((b : ℕ) : ZMod k) := by
  intro hc
  exact h ((ZMod.natCast_eq_natCast_iff a b k).mp hc)

/-- **u = 7 span at residue 3 (constructive).** For `4·x = n + 7` with
`n ≡ 3 (mod 7)`, the span criterion holds at `T = n`. -/
theorem u7_span_of_mod7_three (n x : ℕ) (hu4 : 4 * x = n + 7) (hn3 : n % 7 = 3) :
    u7Span n x := by
  refine ⟨n, ⟨n * (x * x), by ring⟩, ?_⟩
  have hex : (4 * x) % 7 = 3 := by rw [hu4, Nat.add_mod_right, hn3]
  have hx7 : x % 7 = 6 := by omega
  rw [Nat.add_mod, Nat.mul_mod, hn3, hx7]

/-- **u = 7 span at residue 6 (constructive).** For `4·x = n + 7` with
`n ≡ 6 (mod 7)`, the span criterion holds at `T = x`. -/
theorem u7_span_of_mod7_six (n x : ℕ) (hu4 : 4 * x = n + 7) (hn6 : n % 7 = 6) :
    u7Span n x := by
  refine ⟨x, ⟨n * (n * x), by ring⟩, ?_⟩
  have hex : (4 * x) % 7 = 6 := by rw [hu4, Nat.add_mod_right, hn6]
  have hx7 : x % 7 = 5 := by omega
  rw [Nat.add_mod, Nat.mul_mod, hn6, hx7]

/-- **The (H24) u = 7 layer is pigeon-conclusive at residue 3.** For
`4·x = n + 7`, `n ≡ 3 (mod 7)`: the residues of the four divisors
`1, n, x, n·x` are `{1, 3, 6, 4}` (pairwise distinct), so
`2|D| > φ(7)`, and the audited pigeonhole theorem yields the collision. -/
theorem u7_pigeon_of_mod7_three (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hn3 : n % 7 = 3) : hasOppositePair 7 (n * x) := by
  have hex : (4 * x) % 7 = 3 := by rw [hu4, Nat.add_mod_right, hn3]
  have hx7 : x % 7 = 6 := by omega
  have hM0 : 0 < n * x := Nat.mul_pos hn0 hx0
  have hcopr : Nat.Coprime 7 (n * x) := by
    apply (Nat.Prime.coprime_iff_not_dvd Nat.prime_seven).mpr
    intro hd
    rcases (Nat.Prime.dvd_mul Nat.prime_seven).mp hd with hn7 | hx7d
    · have h0 : n % 7 = 0 := Nat.dvd_iff_mod_eq_zero.mp hn7
      omega
    · have h0 : x % 7 = 0 := Nat.dvd_iff_mod_eq_zero.mp hx7d
      omega
  have hcard : 4 ≤ (divResidues 7 (n * x)).card := by
    have hm1 : ((1 : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ 1 (Nat.one_dvd (n * x)) hM0
    have hmn : ((n : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ n ⟨x, by ring⟩ hM0
    have hmx : ((x : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ x ⟨n, by ring⟩ hM0
    have hmp : ((n * x : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ (n * x) (dvd_refl (n * x)) hM0
    have hd1 : ((1 : ℕ) : ZMod 7) ≠ ((n : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne 1 n 7 (by omega)
    have hd2 : ((1 : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne 1 x 7 (by omega)
    have hd3 : ((1 : ℕ) : ZMod 7) ≠ ((n * x : ℕ) : ZMod 7) := by
      have hnx : (n * x) % 7 = 4 := by rw [Nat.mul_mod, hn3, hx7]
      exact cast_ne_of_mod_ne 1 (n * x) 7 (by omega)
    have hd4 : ((n : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne n x 7 (by omega)
    have hd5 : ((n : ℕ) : ZMod 7) ≠ ((n * x : ℕ) : ZMod 7) := by
      have hnx : (n * x) % 7 = 4 := by rw [Nat.mul_mod, hn3, hx7]
      exact cast_ne_of_mod_ne n (n * x) 7 (by omega)
    have hd6 : ((x : ℕ) : ZMod 7) ≠ ((n * x : ℕ) : ZMod 7) := by
      have hnx : (n * x) % 7 = 4 := by rw [Nat.mul_mod, hn3, hx7]
      exact cast_ne_of_mod_ne x (n * x) 7 (by omega)
    have h42 : ((n : ℕ) : ZMod 7) ∉ (insert ((x : ℕ) : ZMod 7) {((n * x : ℕ) : ZMod 7)} : Finset (ZMod 7)) := by
      intro hc
      rcases Finset.mem_insert.mp hc with heq | hc2
      · exact hd4 heq
      · exact hd5 (Finset.mem_singleton.mp hc2)
    have h43 : ((1 : ℕ) : ZMod 7) ∉ (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) {((n * x : ℕ) : ZMod 7)}) : Finset (ZMod 7)) := by
      intro hc
      rcases Finset.mem_insert.mp hc with heq | hc2
      · exact hd1 heq
      rcases Finset.mem_insert.mp hc2 with heq2 | hc3
      · exact hd2 heq2
      · exact hd3 (Finset.mem_singleton.mp hc3)
    have h46 : ((x : ℕ) : ZMod 7) ∉ ({((n * x : ℕ) : ZMod 7)} : Finset (ZMod 7)) :=
      fun hc => hd6 (Finset.mem_singleton.mp hc)
    have h4 : (insert ((1 : ℕ) : ZMod 7) (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) ({((n * x : ℕ) : ZMod 7)} : Finset (ZMod 7))))).card = 4 := by
      rw [Finset.card_insert_of_notMem h43, Finset.card_insert_of_notMem h42,
          Finset.card_insert_of_notMem h46, Finset.card_singleton]
    have hsub : (insert ((1 : ℕ) : ZMod 7) (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) {((n * x : ℕ) : ZMod 7)}))) ⊆
        divResidues 7 (n * x) := by
      intro y hy
      rcases Finset.mem_insert.mp hy with h1 | hy
      · rw [h1]; exact hm1
      rcases Finset.mem_insert.mp hy with h2 | hy
      · rw [h2]; exact hmn
      rcases Finset.mem_insert.mp hy with hx3 | hx4
      · rw [hx3]; exact hmx
      rw [Finset.mem_singleton.mp hx4]; exact hmp
    exact h4.symm.le.trans (Finset.card_le_card hsub)
  have htot : Nat.totient 7 = 6 := by rw [Nat.totient_prime Nat.prime_seven]
  exact pigeonhole_reachability 7 (n * x) (by norm_num) (Nat.Coprime.symm hcopr) (by rw [htot]; omega)

/-- **The (H24) u = 7 layer is pigeon-conclusive at residue 5.** For
`4·x = n + 7`, `n ≡ 5 (mod 7)`, `2 ∣ x`: the residues of
`1, n, x, 2` are `{1, 5, 3, 2}` (pairwise distinct); same pigeon route. -/
theorem u7_pigeon_of_mod7_five (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hn5 : n % 7 = 5) (hx2 : 2 ∣ x) :
    hasOppositePair 7 (n * x) := by
  have hex : (4 * x) % 7 = 5 := by rw [hu4, Nat.add_mod_right, hn5]
  have hx7 : x % 7 = 3 := by omega
  have hM0 : 0 < n * x := Nat.mul_pos hn0 hx0
  have hcopr : Nat.Coprime 7 (n * x) := by
    apply (Nat.Prime.coprime_iff_not_dvd Nat.prime_seven).mpr
    intro hd
    rcases (Nat.Prime.dvd_mul Nat.prime_seven).mp hd with hn7 | hx7d
    · have h0 : n % 7 = 0 := Nat.dvd_iff_mod_eq_zero.mp hn7
      omega
    · have h0 : x % 7 = 0 := Nat.dvd_iff_mod_eq_zero.mp hx7d
      omega
  have hcard : 4 ≤ (divResidues 7 (n * x)).card := by
    have hm1 : ((1 : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ 1 (Nat.one_dvd (n * x)) hM0
    have hmn : ((n : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ n ⟨x, by ring⟩ hM0
    have hmx : ((x : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ x ⟨n, by ring⟩ hM0
    have hm2 : ((2 : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ 2 (hx2.trans ⟨n, by ring⟩) hM0
    have hd1 : ((1 : ℕ) : ZMod 7) ≠ ((n : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne 1 n 7 (by omega)
    have hd2 : ((1 : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne 1 x 7 (by omega)
    have hd4 : ((n : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne n x 7 (by omega)
    have hd5 : ((n : ℕ) : ZMod 7) ≠ ((2 : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne n 2 7 (by omega)
    have hd6 : ((x : ℕ) : ZMod 7) ≠ ((2 : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne x 2 7 (by omega)
    have h2ne : ((1 : ℕ) : ZMod 7) ≠ ((2 : ℕ) : ZMod 7) := by decide
    have h42 : ((1 : ℕ) : ZMod 7) ∉ (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) {((2 : ℕ) : ZMod 7)}) : Finset (ZMod 7)) := by
      intro hc
      rcases Finset.mem_insert.mp hc with heq | hc2
      · exact hd1 heq
      rcases Finset.mem_insert.mp hc2 with heq2 | hc3
      · exact hd2 heq2
      · exact h2ne (Finset.mem_singleton.mp hc3)
    have h43 : ((n : ℕ) : ZMod 7) ∉ (insert ((x : ℕ) : ZMod 7) {((2 : ℕ) : ZMod 7)} : Finset (ZMod 7)) := by
      intro hc
      rcases Finset.mem_insert.mp hc with heq | hc2
      · exact hd4 heq
      · exact hd5 (Finset.mem_singleton.mp hc2)
    have h44 : ((x : ℕ) : ZMod 7) ∉ ({((2 : ℕ) : ZMod 7)} : Finset (ZMod 7)) := fun hc => hd6 (Finset.mem_singleton.mp hc)
    have h4 : (insert ((1 : ℕ) : ZMod 7) (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) ({((2 : ℕ) : ZMod 7)} : Finset (ZMod 7))))).card = 4 := by
      rw [Finset.card_insert_of_notMem h42, Finset.card_insert_of_notMem h43,
          Finset.card_insert_of_notMem h44, Finset.card_singleton]
    have hsub : (insert ((1 : ℕ) : ZMod 7) (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) {((2 : ℕ) : ZMod 7)}))) ⊆
        divResidues 7 (n * x) := by
      intro y hy
      rcases Finset.mem_insert.mp hy with h1 | hy
      · rw [h1]; exact hm1
      rcases Finset.mem_insert.mp hy with h2 | hy
      · rw [h2]; exact hmn
      rcases Finset.mem_insert.mp hy with hx3 | hx4
      · rw [hx3]; exact hmx
      rw [Finset.mem_singleton.mp hx4]; exact hm2
    exact h4.symm.le.trans (Finset.card_le_card hsub)
  have htot : Nat.totient 7 = 6 := by rw [Nat.totient_prime Nat.prime_seven]
  exact pigeonhole_reachability 7 (n * x) (by norm_num) (Nat.Coprime.symm hcopr) (by rw [htot]; omega)

/-- **The (H24) u = 7 layer is pigeon-conclusive at residue 6.** For
`4·x = n + 7`, `n ≡ 6 (mod 7)`: the residues of `1, n, x, n·x`
are `{1, 6, 5, 2}` (pairwise distinct); same pigeon route. -/
theorem u7_pigeon_of_mod7_six (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hn6 : n % 7 = 6) : hasOppositePair 7 (n * x) := by
  have hex : (4 * x) % 7 = 6 := by rw [hu4, Nat.add_mod_right, hn6]
  have hx7 : x % 7 = 5 := by omega
  have hM0 : 0 < n * x := Nat.mul_pos hn0 hx0
  have hcopr : Nat.Coprime 7 (n * x) := by
    apply (Nat.Prime.coprime_iff_not_dvd Nat.prime_seven).mpr
    intro hd
    rcases (Nat.Prime.dvd_mul Nat.prime_seven).mp hd with hn7 | hx7d
    · have h0 : n % 7 = 0 := Nat.dvd_iff_mod_eq_zero.mp hn7
      omega
    · have h0 : x % 7 = 0 := Nat.dvd_iff_mod_eq_zero.mp hx7d
      omega
  have hcard : 4 ≤ (divResidues 7 (n * x)).card := by
    have hm1 : ((1 : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ 1 (Nat.one_dvd (n * x)) hM0
    have hmn : ((n : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ n ⟨x, by ring⟩ hM0
    have hmx : ((x : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ x ⟨n, by ring⟩ hM0
    have hmp : ((n * x : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ (n * x) (dvd_refl (n * x)) hM0
    have hd1 : ((1 : ℕ) : ZMod 7) ≠ ((n : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne 1 n 7 (by omega)
    have hd2 : ((1 : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne 1 x 7 (by omega)
    have hd3 : ((1 : ℕ) : ZMod 7) ≠ ((n * x : ℕ) : ZMod 7) := by
      have hnx : (n * x) % 7 = 2 := by rw [Nat.mul_mod, hn6, hx7]
      exact cast_ne_of_mod_ne 1 (n * x) 7 (by omega)
    have hd4 : ((n : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
      cast_ne_of_mod_ne n x 7 (by omega)
    have hd5 : ((n : ℕ) : ZMod 7) ≠ ((n * x : ℕ) : ZMod 7) := by
      have hnx : (n * x) % 7 = 2 := by rw [Nat.mul_mod, hn6, hx7]
      exact cast_ne_of_mod_ne n (n * x) 7 (by omega)
    have hd6 : ((x : ℕ) : ZMod 7) ≠ ((n * x : ℕ) : ZMod 7) := by
      have hnx : (n * x) % 7 = 2 := by rw [Nat.mul_mod, hn6, hx7]
      exact cast_ne_of_mod_ne x (n * x) 7 (by omega)
    have h42 : ((n : ℕ) : ZMod 7) ∉ (insert ((x : ℕ) : ZMod 7) {((n * x : ℕ) : ZMod 7)} : Finset (ZMod 7)) := by
      intro hc
      rcases Finset.mem_insert.mp hc with heq | hc2
      · exact hd4 heq
      · exact hd5 (Finset.mem_singleton.mp hc2)
    have h43 : ((1 : ℕ) : ZMod 7) ∉ (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) {((n * x : ℕ) : ZMod 7)}) : Finset (ZMod 7)) := by
      intro hc
      rcases Finset.mem_insert.mp hc with heq | hc2
      · exact hd1 heq
      rcases Finset.mem_insert.mp hc2 with heq2 | hc3
      · exact hd2 heq2
      · exact hd3 (Finset.mem_singleton.mp hc3)
    have h46 : ((x : ℕ) : ZMod 7) ∉ ({((n * x : ℕ) : ZMod 7)} : Finset (ZMod 7)) :=
      fun hc => hd6 (Finset.mem_singleton.mp hc)
    have h4 : (insert ((1 : ℕ) : ZMod 7) (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) ({((n * x : ℕ) : ZMod 7)} : Finset (ZMod 7))))).card = 4 := by
      rw [Finset.card_insert_of_notMem h43, Finset.card_insert_of_notMem h42,
          Finset.card_insert_of_notMem h46, Finset.card_singleton]
    have hsub : (insert ((1 : ℕ) : ZMod 7) (insert ((n : ℕ) : ZMod 7)
        (insert ((x : ℕ) : ZMod 7) {((n * x : ℕ) : ZMod 7)}))) ⊆
        divResidues 7 (n * x) := by
      intro y hy
      rcases Finset.mem_insert.mp hy with h1 | hy
      · rw [h1]; exact hm1
      rcases Finset.mem_insert.mp hy with h2 | hy
      · rw [h2]; exact hmn
      rcases Finset.mem_insert.mp hy with hx3 | hx4
      · rw [hx3]; exact hmx
      rw [Finset.mem_singleton.mp hx4]; exact hmp
    exact h4.symm.le.trans (Finset.card_le_card hsub)
  have htot : Nat.totient 7 = 6 := by rw [Nat.totient_prime Nat.prime_seven]
  exact pigeonhole_reachability 7 (n * x) (by norm_num) (Nat.Coprime.symm hcopr) (by rw [htot]; omega)

/-- **The u = 7 span at residue 1 or 6 (the 5-window, depth ≥ 1).**
For `4·x = n + 7`, `n ≡ ±1 (mod 7)` and `125 ∣ x` (so
`5 ∣ x` at depth ≥ 3, hence `5 ∣ n·x`), the span
criterion holds at `T = 5`: for both classes `n·x ≡ 2 (mod 7)`,
so `T + n·x ≡ 5 + 2 ≡ 0`. -/
theorem u7_span_of_fivex_pm1 (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hn : n % 7 = 1 ∨ n % 7 = 6) (hv5 : 125 ∣ x) :
    u7Span n x := by
  have h5M : 5 ∣ n * x := Nat.dvd_trans (show (5 : ℕ) ∣ 125 from ⟨25, by ring⟩)
      (dvd_mul_of_dvd_right hv5 n)
  refine ⟨5, by rw [Nat.pow_two]; exact dvd_mul_of_dvd_right h5M (n * x), ?_⟩
  rcases hn with h1 | h6
  · have hx7 : x % 7 = 2 := by
      have hex : (4 * x) % 7 = 1 := by rw [hu4, Nat.add_mod_right, h1]
      omega
    rw [Nat.add_mod, Nat.mul_mod, h1, hx7]
  · have hx7 : x % 7 = 5 := by
      have hex : (4 * x) % 7 = 6 := by rw [hu4, Nat.add_mod_right, h6]
      omega
    rw [Nat.add_mod, Nat.mul_mod, h6, hx7]

/-- **The u = 7 span at residue 2 or 5 (the 5-window,·depth ≥ 3).**
For `4·x = n + 7`, `n ≡ ±2 (mod 7)` and `125 ∣ x`, the
span criterion holds at `T = 125 ≡ 6 (mod 7)`: for both classes
`n·x ≡ 1 (mod 7)`, so `T + n·x ≡ 6 + 1 ≡ 0`. -/
theorem u7_span_of_fivex_pm2 (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hn : n % 7 = 2 ∨ n % 7 = 5) (hv5 : 125 ∣ x) :
    u7Span n x := by
  have h125M : 125 ∣ n * x := dvd_mul_of_dvd_right hv5 n
  refine ⟨125, by rw [Nat.pow_two]; exact dvd_mul_of_dvd_right h125M (n * x), ?_⟩
  rcases hn with h2 | h5
  · have hx7 : x % 7 = 4 := by
      have hex : (4 * x) % 7 = 2 := by rw [hu4, Nat.add_mod_right, h2]
      omega
    rw [Nat.add_mod, Nat.mul_mod, h2, hx7]
  · have hx7 : x % 7 = 3 := by
      have hex : (4 * x) % 7 = 5 := by rw [hu4, Nat.add_mod_right, h5]
      omega
    rw [Nat.add_mod, Nat.mul_mod, h5, hx7]

/-- **The u = 7 span at residue 3 or 4 (the 5-window, depth ≥ 5).**
For `4·x = n + 7`, `n ≡ ±3 (mod 7)` and `3125 ∣ x`, the
span criterion holds at `T = 3125 ≡ 3 (mod 7)`: for both classes
`n·x ≡ 4 (mod 7)`, so `T + n·x ≡ 3 + 4 ≡ 0`. -/
theorem u7_span_of_fivex_pm3 (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hn : n % 7 = 3 ∨ n % 7 = 4) (hv5 : 3125 ∣ x) :
    u7Span n x := by
  have h3125M : 3125 ∣ n * x := dvd_mul_of_dvd_right hv5 n
  refine ⟨3125, by rw [Nat.pow_two]; exact dvd_mul_of_dvd_right h3125M (n * x), ?_⟩
  rcases hn with h3 | h4
  · have hx7 : x % 7 = 6 := by
      have hex : (4 * x) % 7 = 3 := by rw [hu4, Nat.add_mod_right, h3]
      omega
    rw [Nat.add_mod, Nat.mul_mod, h3, hx7]
  · have hx7 : x % 7 = 1 := by
      have hex : (4 * x) % 7 = 4 := by rw [hu4, Nat.add_mod_right, h4]
      omega
    rw [Nat.add_mod, Nat.mul_mod, h4, hx7]

/-- **The 2-orbit closure.** A positive integer whose prime divisors are
`1`, `2`, or `4 (mod 7)` is itself `1`, `2`, or `4 (mod 7)` - the residue
set `{1, 2, 4}` is multiplicatively closed in `(Z/7)*`. -/
theorem prod_in_orbit_clo_two (T : ℕ) (hT0 : 0 < T)
    (hall : ∀ q : ℕ, q.Prime → q ∣ T →
      q % 7 = 1 ∨ q % 7 = 2 ∨ q % 7 = 4) :
    T % 7 = 1 ∨ T % 7 = 2 ∨ T % 7 = 4 := by
  have key : ∀ t : ℕ, t ≤ T → 0 < t →
      (∀ q : ℕ, q.Prime → q ∣ t →
        q % 7 = 1 ∨ q % 7 = 2 ∨ q % 7 = 4) →
      t % 7 = 1 ∨ t % 7 = 2 ∨ t % 7 = 4 := by
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
          have hqlt : q < t := Nat.lt_of_le_of_ne hlq hqne
          have htdq : t / q ∣ t := Nat.div_dvd_of_dvd hqt
          have hlt : t / q < t := Nat.div_lt_self ht0 hqp.one_lt
          have hlqT : t / q ≤ T := Nat.le_trans (Nat.le_of_dvd ht0 htdq) _hle
          have htq0 : 0 < t / q := Nat.div_pos hlq (by linarith [hqp.one_lt])
          have hall2 : ∀ r : ℕ, r.Prime → r ∣ t / q →
              r % 7 = 1 ∨ r % 7 = 2 ∨ r % 7 = 4 :=
            fun r hr hrd => hall' r hr (hrd.trans htdq)
          have hrec := ih (t / q) hlt hlqT htq0 hall2
          have hqres : q % 7 = 1 ∨ q % 7 = 2 ∨ q % 7 = 4 := hall' q hqp hqt
          have hdiv : t = (t / q) * q := (Nat.div_mul_cancel hqt).symm
          rw [hdiv]
          rcases hrec with hr | hr | hr
          · rcases hqres with k | k | k
            · rw [Nat.mul_mod, hr, k]; norm_num
            · rw [Nat.mul_mod, hr, k]; norm_num
            · rw [Nat.mul_mod, hr, k]; norm_num
          · rcases hqres with k | k | k
            · rw [Nat.mul_mod, hr, k]; norm_num
            · rw [Nat.mul_mod, hr, k]; norm_num
            · rw [Nat.mul_mod, hr, k]; norm_num
          · rcases hqres with k | k | k
            · rw [Nat.mul_mod, hr, k]; norm_num
            · rw [Nat.mul_mod, hr, k]; norm_num
            · rw [Nat.mul_mod, hr, k]; norm_num
  exact key T (Nat.le_refl T) hT0 hall

/-- **The u = 7 span fails when every odd prime divisor of `x` sits in the
2-orbit closure** (E-018's composition-level ⟺, the fail direction).
For `4·x = n + 7`, `n` prime with `n ≡ 1, 2, 4 (mod 7)`, and
every prime divisor of `x` congruent to `1`, `2`, or `4 (mod 7)`, every
divisor of `(n·x)^2` is `1`, `2`, or `4 (mod 7)`, while
`-n·x ≡ 5, 6, 3 (mod 7)` respectively - never reachable, so no
span candidate exists. -/
theorem u7_span_fails_of_orbit_primes (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hnp : n.Prime)
    (hn : n % 7 = 1 ∨ n % 7 = 2 ∨ n % 7 = 4)
    (hxp : ∀ q : ℕ, q.Prime → q ∣ x →
      q % 7 = 1 ∨ q % 7 = 2 ∨ q % 7 = 4) :
    ¬ u7Span n x := by
  have hMres : (n * x) % 7 = 1 ∨ (n * x) % 7 = 2 ∨ (n * x) % 7 = 4 := by
    rcases hn with e1 | e2 | e4
    · have hx7 : x % 7 = 2 := by
        have hex : (4 * x) % 7 = 1 := by rw [hu4, Nat.add_mod_right, e1]
        omega
      rw [Nat.mul_mod, e1, hx7]; norm_num
    · have hx7 : x % 7 = 4 := by
        have hex : (4 * x) % 7 = 2 := by rw [hu4, Nat.add_mod_right, e2]
        omega
      rw [Nat.mul_mod, e2, hx7]; norm_num
    · have hx7 : x % 7 = 1 := by
        have hex : (4 * x) % 7 = 4 := by rw [hu4, Nat.add_mod_right, e4]
        omega
      rw [Nat.mul_mod, e4, hx7]; norm_num
  rintro ⟨T, hT, hcong⟩
  have hT0 : 0 < T := by
    by_contra hTz
    have hTe : T = 0 := Nat.le_zero.mp (Nat.not_lt.mp hTz)
    rw [hTe, Nat.zero_add] at hcong
    omega
  have hallT : ∀ q : ℕ, q.Prime → q ∣ T →
      q % 7 = 1 ∨ q % 7 = 2 ∨ q % 7 = 4 := by
    intro q hqp hqT
    have hqM2 : q ∣ (n * x) ^ 2 := hqT.trans hT
    have hqM : q ∣ n * x := hqp.dvd_of_dvd_pow hqM2
    rcases (Nat.Prime.dvd_mul hqp).mp hqM with hqn | hqx
    · have hqeq : q = n :=
        Nat.prime_eq_prime_of_dvd_pow hqp hnp (by rw [pow_one]; exact hqn)
      rw [hqeq]
      exact hn
    · exact hxp q hqp hqx
  have hTres : T % 7 = 1 ∨ T % 7 = 2 ∨ T % 7 = 4 :=
    prod_in_orbit_clo_two T hT0 hallT
  rcases hTres with t1 | t2 | t4 <;> rcases hMres with m1 | m2 | m4 <;> omega

/-- **The u = 7 span when `x` carries an outside-closure odd prime**
(E-018's composition-level ⟺, the span direction). For `4·x =
n + 7` with `2 ∣ x` and an odd prime `q ∣ x` in residue
`3`, `5`, or `6 (mod 7)`, the divisor-residues
`{1, x, q, 2·q}` are four distinct elements of `D_7(n·x)`
(the residues `{1, 2n, q, 2q}` with `2q ∉ {1, 2n}` for
`q ∉ {1, 2, 4}`), so `2|D| > φ(7)` and the audited pigeonhole
theorem yields the collision. -/
theorem u7_pigeon_of_orbit_breaker (n x : ℕ) (hn0 : 0 < n) (hx0 : 0 < x)
    (hu4 : 4 * x = n + 7) (hcopr : Nat.Coprime (n * x) 7) (hx2 : 2 ∣ x)
    (hn : n % 7 = 1 ∨ n % 7 = 2 ∨ n % 7 = 4)
    (hq : ∃ q : ℕ, q.Prime ∧ q ∣ x ∧
      (q % 7 = 3 ∨ q % 7 = 5 ∨ q % 7 = 6)) :
    hasOppositePair 7 (n * x) := by
  obtain ⟨q, hqp, hqx, hqr⟩ := hq
  have hM0 : 0 < n * x := Nat.mul_pos hn0 hx0
  have h2q : 2 * q ∣ x := by
    have hq2 : q ≠ 2 := by
      intro heq
      rw [heq] at hqr
      omega
    have hd2q : ¬(2 ∣ q) := by
      intro hd
      rcases Nat.Prime.eq_one_or_self_of_dvd hqp 2 hd with h21 | h2q <;> omega
    have hc2q : Nat.Coprime 2 q :=
      (Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr hd2q
    exact Nat.Coprime.mul_dvd_of_dvd_of_dvd hc2q hx2 hqx
  have h2qx : 2 * q ∣ n * x := dvd_mul_of_dvd_right h2q n
  have hqxM : q ∣ n * x := dvd_mul_of_dvd_right hqx n
  -- E-018's span direction: the four divisor-residues {n, x, q, 2*q}
  -- (all residue pairs distinct for q ∉ {1, 2, 4} (mod 7)) close the
  -- pigeon: 2·4 > φ(7) = 6.
  have hcard : 4 ≤ (divResidues 7 (n * x)).card := by
    have hmn : ((n : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ n ⟨x, by ring⟩ hM0
    have hmx : ((x : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ x ⟨n, by ring⟩ hM0
    have hmq : ((q : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ q hqxM hM0
    have hm2 : ((2 * q : ℕ) : ZMod 7) ∈ divResidues 7 (n * x) :=
      mem_divResidues 7 _ (2 * q) h2qx hM0
    rcases hn with e | e | e
    · have hx7 : x % 7 = 2 := by
        have hex : (4 * x) % 7 = 1 := by rw [hu4, Nat.add_mod_right, e]
        omega
      have dn1 : ((n : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n x 7 (by omega)
      have dq1 : ((n : ℕ) : ZMod 7) ≠ ((q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n q 7 (by omega)
      have dq2 : ((n : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n (2 * q) 7 (by omega)
      have dx1 : ((x : ℕ) : ZMod 7) ≠ ((q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne x q 7 (by omega)
      have dx2 : ((x : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne x (2 * q) 7 (by omega)
      have d21 : ((q : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne q (2 * q) 7 (by omega)
      have hdn : ((n : ℕ) : ZMod 7) ∉ (insert ((x : ℕ) : ZMod 7)
          (insert ((q : ℕ) : ZMod 7) ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7)))) := by
        intro hc
        rcases Finset.mem_insert.mp hc with heq | hc2
        · exact dn1 heq
        rcases Finset.mem_insert.mp hc2 with heq2 | hc3
        · exact dq1 heq2
        · exact dq2 (Finset.mem_singleton.mp hc3)
      have hdx : ((x : ℕ) : ZMod 7) ∉ (insert ((q : ℕ) : ZMod 7)
          ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7))) := by
        intro hc
        rcases Finset.mem_insert.mp hc with heq | hc2
        · exact dx1 heq
        · exact dx2 (Finset.mem_singleton.mp hc2)
      have hdq : ((q : ℕ) : ZMod 7) ∉ ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7)) := fun hc =>
        d21 (Finset.mem_singleton.mp hc)
      have h4 : (insert ((n : ℕ) : ZMod 7)
          (insert ((x : ℕ) : ZMod 7)
            (insert ((q : ℕ) : ZMod 7) ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7))))).card = 4 := by
        rw [Finset.card_insert_of_notMem hdn, Finset.card_insert_of_notMem hdx,
            Finset.card_insert_of_notMem hdq, Finset.card_singleton]
      have hsub : (insert ((n : ℕ) : ZMod 7)
          (insert ((x : ℕ) : ZMod 7)
            (insert ((q : ℕ) : ZMod 7) {((2 * q : ℕ) : ZMod 7)}))) ⊆
          divResidues 7 (n * x) := by
        intro y hy
        rcases Finset.mem_insert.mp hy with h1 | hy
        · rw [h1]; exact hmn
        rcases Finset.mem_insert.mp hy with h2 | hy
        · rw [h2]; exact hmx
        rcases Finset.mem_insert.mp hy with h3 | h4m
        · rw [h3]; exact hmq
        rw [Finset.mem_singleton.mp h4m]; exact hm2
      exact h4.symm.le.trans (Finset.card_le_card hsub)
    · have hx7 : x % 7 = 4 := by
        have hex : (4 * x) % 7 = 2 := by rw [hu4, Nat.add_mod_right, e]
        omega
      have dn1 : ((n : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n x 7 (by omega)
      have dq1 : ((n : ℕ) : ZMod 7) ≠ ((q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n q 7 (by omega)
      have dq2 : ((n : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n (2 * q) 7 (by omega)
      have dx1 : ((x : ℕ) : ZMod 7) ≠ ((q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne x q 7 (by omega)
      have dx2 : ((x : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne x (2 * q) 7 (by omega)
      have d21 : ((q : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne q (2 * q) 7 (by omega)
      have hdn : ((n : ℕ) : ZMod 7) ∉ (insert ((x : ℕ) : ZMod 7)
          (insert ((q : ℕ) : ZMod 7) ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7)))) := by
        intro hc
        rcases Finset.mem_insert.mp hc with heq | hc2
        · exact dn1 heq
        rcases Finset.mem_insert.mp hc2 with heq2 | hc3
        · exact dq1 heq2
        · exact dq2 (Finset.mem_singleton.mp hc3)
      have hdx : ((x : ℕ) : ZMod 7) ∉ (insert ((q : ℕ) : ZMod 7)
          ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7))) := by
        intro hc
        rcases Finset.mem_insert.mp hc with heq | hc2
        · exact dx1 heq
        · exact dx2 (Finset.mem_singleton.mp hc2)
      have hdq : ((q : ℕ) : ZMod 7) ∉ ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7)) := fun hc =>
        d21 (Finset.mem_singleton.mp hc)
      have h4 : (insert ((n : ℕ) : ZMod 7)
          (insert ((x : ℕ) : ZMod 7)
            (insert ((q : ℕ) : ZMod 7) ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7))))).card = 4 := by
        rw [Finset.card_insert_of_notMem hdn, Finset.card_insert_of_notMem hdx,
            Finset.card_insert_of_notMem hdq, Finset.card_singleton]
      have hsub : (insert ((n : ℕ) : ZMod 7)
          (insert ((x : ℕ) : ZMod 7)
            (insert ((q : ℕ) : ZMod 7) {((2 * q : ℕ) : ZMod 7)}))) ⊆
          divResidues 7 (n * x) := by
        intro y hy
        rcases Finset.mem_insert.mp hy with h1 | hy
        · rw [h1]; exact hmn
        rcases Finset.mem_insert.mp hy with h2 | hy
        · rw [h2]; exact hmx
        rcases Finset.mem_insert.mp hy with h3 | h4m
        · rw [h3]; exact hmq
        rw [Finset.mem_singleton.mp h4m]; exact hm2
      exact h4.symm.le.trans (Finset.card_le_card hsub)
    · have hx7 : x % 7 = 1 := by
        have hex : (4 * x) % 7 = 4 := by rw [hu4, Nat.add_mod_right, e]
        omega
      have dn1 : ((n : ℕ) : ZMod 7) ≠ ((x : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n x 7 (by omega)
      have dq1 : ((n : ℕ) : ZMod 7) ≠ ((q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n q 7 (by omega)
      have dq2 : ((n : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne n (2 * q) 7 (by omega)
      have dx1 : ((x : ℕ) : ZMod 7) ≠ ((q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne x q 7 (by omega)
      have dx2 : ((x : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne x (2 * q) 7 (by omega)
      have d21 : ((q : ℕ) : ZMod 7) ≠ ((2 * q : ℕ) : ZMod 7) :=
        cast_ne_of_mod_ne q (2 * q) 7 (by omega)
      have hdn : ((n : ℕ) : ZMod 7) ∉ (insert ((x : ℕ) : ZMod 7)
          (insert ((q : ℕ) : ZMod 7) ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7)))) := by
        intro hc
        rcases Finset.mem_insert.mp hc with heq | hc2
        · exact dn1 heq
        rcases Finset.mem_insert.mp hc2 with heq2 | hc3
        · exact dq1 heq2
        · exact dq2 (Finset.mem_singleton.mp hc3)
      have hdx : ((x : ℕ) : ZMod 7) ∉ (insert ((q : ℕ) : ZMod 7)
          ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7))) := by
        intro hc
        rcases Finset.mem_insert.mp hc with heq | hc2
        · exact dx1 heq
        · exact dx2 (Finset.mem_singleton.mp hc2)
      have hdq : ((q : ℕ) : ZMod 7) ∉ ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7)) := fun hc =>
        d21 (Finset.mem_singleton.mp hc)
      have h4 : (insert ((n : ℕ) : ZMod 7)
          (insert ((x : ℕ) : ZMod 7)
            (insert ((q : ℕ) : ZMod 7) ({((2 * q : ℕ) : ZMod 7)} : Finset (ZMod 7))))).card = 4 := by
        rw [Finset.card_insert_of_notMem hdn, Finset.card_insert_of_notMem hdx,
            Finset.card_insert_of_notMem hdq, Finset.card_singleton]
      have hsub : (insert ((n : ℕ) : ZMod 7)
          (insert ((x : ℕ) : ZMod 7)
            (insert ((q : ℕ) : ZMod 7) {((2 * q : ℕ) : ZMod 7)}))) ⊆
          divResidues 7 (n * x) := by
        intro y hy
        rcases Finset.mem_insert.mp hy with h1 | hy
        · rw [h1]; exact hmn
        rcases Finset.mem_insert.mp hy with h2 | hy
        · rw [h2]; exact hmx
        rcases Finset.mem_insert.mp hy with h3 | h4m
        · rw [h3]; exact hmq
        rw [Finset.mem_singleton.mp h4m]; exact hm2
      exact h4.symm.le.trans (Finset.card_le_card hsub)
  exact pigeonhole_reachability 7 (n * x) (by norm_num) hcopr
    (by rw [Nat.totient_prime Nat.prime_seven]; omega)

end ResidualPrimes

