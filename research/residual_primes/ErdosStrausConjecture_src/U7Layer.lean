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

end ResidualPrimes
