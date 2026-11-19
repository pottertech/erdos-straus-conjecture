import Mathlib
import ErdosStrausConjecture.Basic

/-!
# The constructive core of the u-method

Machine-checks the central algebraic step behind every exact u-method layer
(`MOD31_EXACT_REDUCTION.md` and friends):

If `u = 4x − n > 0` and a positive integer `T` divides `(n·x)²` with
`u ∣ (T + n·x)` — i.e. `T ≡ −n·x (mod u)` — and `gcd(u, n·x) = 1`, then with

    y = (T + n·x) / u,      z = ((n·x)² / T + n·x) / u

we get `0 < y`, `0 < z` and `4·x·y·z = n·(x·y + x·z + y·z)` — a witness for
`IsErdosStraus n`.

Combined with any layer argument that *produces* such a `T` (the centered
product-set / span conditions), this turns layer characterizations into
concrete solutions. Only the constructive direction is formalized here; the
span-side characterizations remain the subject of the layer documents, with
their data verified by `analysis/u31_classification_verify.py`.
-/

namespace ErdosStrausConjecture

/-- **Core identity.** If `u·y = d₁ + n·x`, `u·z = d₂ + n·x`, `u = 4x − n`
with `u ≠ 0`, and `d₁·d₂ = (n·x)²`, then `4·x·y·z = n·(x·y + x·z + y·z)`. -/
theorem u_method_core (n x u d1 d2 y z : ℤ)
    (hu : u = 4 * x - n) (hy : u * y = d1 + n * x) (hz : u * z = d2 + n * x)
    (hdd : d1 * d2 = (n * x) ^ 2) (hu0 : u ≠ 0) :
    4 * x * y * z = n * (x * y + x * z + y * z) := by
  have hd1 : d1 = u * y - n * x := by linarith [hy]
  have hd2 : d2 = u * z - n * x := by linarith [hz]
  -- substitute into hdd: (u·y − n·x)(u·z − n·x) = (n·x)²
  have hexpand : (u * y - n * x) * (u * z - n * x) = (n * x) ^ 2 := by
    rw [hd1, hd2] at hdd; exact hdd
  -- expanding gives u²·y·z = u·n·x·(y + z)
  have hstep : u ^ 2 * y * z = u * (n * x) * (y + z) := by
    linear_combination hexpand
  -- cancel u ≠ 0
  have key : u * (y * z) = n * x * (y + z) := by
    have h2 : u * (u * (y * z)) = u * (n * x * (y + z)) := by
      linear_combination hstep
    exact mul_left_cancel₀ hu0 h2
  have h4x : 4 * x = u + n := by linarith [hu]
  calc 4 * x * y * z
      = (u + n) * (y * z) := by linear_combination (y * z) * h4x
    _ = u * (y * z) + n * (y * z) := by ring
    _ = n * x * (y + z) + n * (y * z) := by rw [key]
    _ = n * (x * y + x * z + y * z) := by ring

/-- **u-method witness.** For `n, x > 0` with `u = 4x − n > 0`,
`gcd(u, n·x) = 1`, and a positive divisor `T` of `(n·x)²` satisfying
`u ∣ (T + n·x)` (i.e. `T ≡ −n·x mod u`), the u-method yields explicit
positive `y, z` with `4·x·y·z = n·(x·y + x·z + y·z)`. -/
theorem u_method_witness (n x T u : ℕ) (hn : 0 < n) (hx : 0 < x)
    (hu0 : 0 < u) (hudef : u = 4 * x - n)
    (hcopr : Nat.Coprime u (n * x))
    (hT : T ∣ (n * x) ^ 2) (hTpos : 0 < T)
    (hcong : u ∣ (T + n * x)) :
    ∃ y z : ℕ, 0 < y ∧ 0 < z ∧ 4 * x * y * z = n * (x * y + x * z + y * z) := by
  have hM2pos : 0 < (n * x) ^ 2 := by positivity
  have hd2le : T ≤ (n * x) ^ 2 := Nat.le_of_dvd hM2pos hT
  have hd2pos : 0 < (n * x) ^ 2 / T := Nat.div_pos hd2le hTpos
  have hmul : ((n * x) ^ 2 / T) * T = (n * x) ^ 2 := Nat.div_mul_cancel hT
  -- u divides d₂·(T + n·x) = (n·x)² + d₂·(n·x) = (n·x)·(n·x + d₂)
  have h5 : u ∣ (n * x) * ((n * x) + (n * x) ^ 2 / T) := by
    have h1 : u ∣ ((n * x) ^ 2 / T) * (T + n * x) :=
      dvd_mul_of_dvd_right hcong _
    have heq : ((n * x) ^ 2 / T) * (T + n * x)
        = (n * x) * ((n * x) + (n * x) ^ 2 / T) := by
      rw [mul_add, hmul, mul_assoc]; ring
    rw [← heq]; exact h1
  -- coprime cancellation: u ∣ (n·x + d₂)
  have h6 : u ∣ ((n * x) + ((n * x) ^ 2 / T)) :=
    hcopr.dvd_of_dvd_mul_left h5
  -- divisibilities for the witnesses
  have hdiv1 : u ∣ (T + n * x) := hcong
  have hdiv2 : u ∣ ((n * x) ^ 2 / T + n * x) := by
    rw [Nat.add_comm]; exact h6
  refine ⟨(T + n * x) / u, ((n * x) ^ 2 / T + n * x) / u, ?_, ?_, ?_⟩
  · have hle : u ≤ T + n * x := Nat.le_of_dvd (by positivity) hdiv1
    exact Nat.div_pos hle hu0
  · have hle : u ≤ (n * x) ^ 2 / T + n * x := Nat.le_of_dvd (by positivity) hdiv2
    exact Nat.div_pos hle hu0
  · have hy : (T + n * x) / u * u = T + n * x := Nat.div_mul_cancel hdiv1
    have hz : ((n * x) ^ 2 / T + n * x) / u * u = (n * x) ^ 2 / T + n * x :=
      Nat.div_mul_cancel hdiv2
      -- the ℤ-level core with the explicit witnesses
    have hcore := u_method_core (n : ℤ) (x : ℤ) (u : ℤ) (T : ℤ)
      (((n * x) ^ 2 / T : ℕ) : ℤ) (((T + n * x) / u : ℕ) : ℤ)
      (((n * x) ^ 2 / T + n * x) / u : ℕ)
      (by omega)
      (by
        have hz1 : ((u : ℕ) : ℤ) ∣ ((T + n * x : ℕ) : ℤ) :=
          Int.natCast_dvd_natCast.mpr hdiv1
        rw [mul_comm]; exact Int.ediv_mul_cancel hz1)
      (by
        have hz2 : ((u : ℕ) : ℤ) ∣ (((n * x) ^ 2 / T + n * x : ℕ) : ℤ) :=
          Int.natCast_dvd_natCast.mpr hdiv2
        rw [mul_comm]; exact Int.ediv_mul_cancel hz2)
      (by
        have hz3 : ((T : ℕ) : ℤ) ∣ (((n * x) ^ 2 : ℕ) : ℤ) :=
          Int.natCast_dvd_natCast.mpr hT
        rw [mul_comm]; exact Int.ediv_mul_cancel hz3)
      (by omega)
    exact_mod_cast hcore

end ErdosStrausConjecture
