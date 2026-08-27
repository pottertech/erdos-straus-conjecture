/-
# Erdős-Straus Conjecture: Basic Definitions

The Erdős-Straus conjecture states that for every integer n ≥ 2,
there exist positive integers x, y, z such that 4/n = 1/x + 1/y + 1/z.

Equivalently (cross-multiplying): 4*x*y*z = n*(x*z + y*z + x*y).
-/

import Mathlib

open Nat

/-- The Erdős-Straus equation: 4/n = 1/x + 1/y + 1/z.
    We use the cross-multiplied form: 4*x*y*z = n*(x*z + y*z + x*y),
    together with positivity conditions. -/
def ErdosStraus.eq (n x y z : ℕ) : Prop :=
  n > 0 ∧ x > 0 ∧ y > 0 ∧ z > 0 ∧ 4 * x * y * z = n * (x * z + y * z + x * y)

/-- The A-parameter: A = 4x - n (as integer). -/
def ErdosStraus.A_param (n x : ℕ) : ℤ := 4 * (x : ℤ) - (n : ℤ)

/-- The Erdős-Straus conjecture: for all n ≥ 2, the equation has a solution. -/
def ErdosStraus.conjecture : Prop :=
  ∀ n : ℕ, n ≥ 2 → ∃ x y z : ℕ, x > 0 ∧ y > 0 ∧ z > 0 ∧
    4 * x * y * z = n * (x * z + y * z + x * y)