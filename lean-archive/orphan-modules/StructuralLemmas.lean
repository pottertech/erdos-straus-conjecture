import Mathlib
import ErdosStrausConjecture.Basic

-- ⚠ STATUS (2026-11-18): this module does NOT compile with the pinned
-- toolchain (Lean/Mathlib v4.30.0): tactic errors at lines 210/218/220
-- (rewrites no longer type-check; authored/tested on Lean 4.33.1), plus
-- 5 unfinished `sorry` goals (lines 233-278). Excluded from the CI build
-- set until revalidated. See README.md (Lean section).

namespace ErdosStrausConjecture

-- ============================================
-- QNR INHERITANCE LEMMA
-- ============================================
-- For prime u ≡ 3 mod 4, if n is QNR mod u then x = (n+u)/4 is also QNR mod u.
--
-- Proof: x ≡ n · 4⁻¹ mod u. Since 4 = 2², 4⁻¹ is QR.
-- QNR × QR = QNR (Legendre symbol: (n/u)·(4⁻¹/u) = (n/u)·1 = (n/u) = -1).
--
-- Key fact: (-1/u) = -1 when u ≡ 3 mod 4 (Euler's criterion).
--
-- Mathlib lemmas used:
--   - ZMod.exists_sq_eq_neg_one_iff : IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3
--     (from Mathlib.NumberTheory.LegendreSymbol.Basic)
--   - ZMod.natCast_eq_zero_iff : (a : ZMod b) = 0 ↔ b ∣ a
--     (from Mathlib.Data.ZMod.Basic)
--   - eq_inv_of_mul_eq_one_right : a * b = 1 → b = a⁻¹
--     (from Mathlib.Algebra.Group.Basic)
--   - Nat.modEq_zero_iff_dvd : a ≡ 0 [MOD n] ↔ n ∣ a
--     (from Mathlib.Data.Nat.ModEq)
-- ============================================

-- ----------------------------------------------
-- Helper: (n + u : ZMod u) = (n : ZMod u)
-- Because n + u ≡ n (mod u) since u ≡ 0 (mod u)
-- ----------------------------------------------
lemma cast_add_self (n u : ℕ) : ((n + u : ℕ) : ZMod u) = (n : ZMod u) := by
  rw [ZMod.natCast_eq_natCast_iff]
  have h : u ≡ 0 [MOD u] := Nat.modEq_zero_iff_dvd.mpr dvd_rfl
  have := h.add_left n
  omega

-- ----------------------------------------------
-- Helper: 4 ≠ 0 in ZMod u when u ≡ 3 mod 4, u prime
-- ----------------------------------------------
lemma four_ne_zero_zmod (u : ℕ) (hu : u.Prime) (hu3 : u % 4 = 3) :
    (4 : ZMod u) ≠ 0 := by
  intro h
  have hu_dvd : u ∣ 4 := (ZMod.natCast_eq_zero_iff 4 u).mp h
  have hle4 : u ≤ 4 := Nat.le_of_dvd (by norm_num) hu_dvd
  have hge3 : u ≥ 3 := by omega
  interval_cases u
  · norm_num at hu_dvd
  · exact absurd hu (by norm_num : ¬ Nat.Prime 4)

-- ----------------------------------------------
-- Helper: (n+u)/4 cast to ZMod u = n * 4⁻¹
-- Key: 4 * ((n+u)/4) = n+u ≡ n (mod u), so 4 * x = n in ZMod u
-- ----------------------------------------------
lemma div_cast_eq_inv (n u : ℕ) (hu : u.Prime) (hu3 : u % 4 = 3)
    (hn_mod4 : n % 4 = 1) :
    (((n + u) / 4 : ℕ) : ZMod u) = (n : ZMod u) * (4 : ZMod u)⁻¹ := by
  haveI : Fact u.Prime := ⟨hu⟩
  have h4_dvd : 4 ∣ n + u := by omega
  have h4_ne_0 := four_ne_zero_zmod u hu hu3
  have h4x : 4 * ((n + u) / 4) = n + u := by
    rw [mul_comm]; exact Nat.div_mul_cancel h4_dvd
  have hmod : (4 : ZMod u) * (((n + u) / 4 : ℕ) : ZMod u) = (n : ZMod u) := by
    have h1 : ((4 * ((n + u) / 4) : ℕ) : ZMod u) = ((n + u : ℕ) : ZMod u) := by
      rw [h4x]
    have h2 : ((4 * ((n + u) / 4) : ℕ) : ZMod u) =
              (4 : ZMod u) * (((n + u) / 4 : ℕ) : ZMod u) :=
      Nat.cast_mul 4 ((n + u) / 4)
    have h3 : ((n + u : ℕ) : ZMod u) = (n : ZMod u) := cast_add_self n u
    rw [h2] at h1; rw [h1, h3]
  calc (((n + u) / 4 : ℕ) : ZMod u)
      = 1 * (((n + u) / 4 : ℕ) : ZMod u) := by ring
    _ = ((4 : ZMod u))⁻¹ * (4 : ZMod u) * (((n + u) / 4 : ℕ) : ZMod u) := by
      rw [inv_mul_cancel₀ h4_ne_0]
    _ = (4 : ZMod u)⁻¹ * ((4 : ZMod u) * (((n + u) / 4 : ℕ) : ZMod u)) := by ring
    _ = (4 : ZMod u)⁻¹ * (n : ZMod u) := by rw [hmod]
    _ = (n : ZMod u) * (4 : ZMod u)⁻¹ := by ring

-- ----------------------------------------------
-- Helper: (a * a)⁻¹ = a⁻¹ * a⁻¹ in a field
-- ----------------------------------------------
lemma inv_sq_eq_sq_inv (p : ℕ) [Fact p.Prime] (a : ZMod p) (ha : a ≠ 0) :
    (a * a)⁻¹ = a⁻¹ * a⁻¹ := by
  symm
  apply eq_inv_of_mul_eq_one_right
  calc (a * a) * (a⁻¹ * a⁻¹)
      = a * (a * (a⁻¹ * a⁻¹)) := by ring
    _ = a * ((a * a⁻¹) * a⁻¹) := by ring
    _ = a * (1 * a⁻¹) := by rw [mul_inv_cancel₀ ha]
    _ = a * a⁻¹ := by rw [one_mul]
    _ = 1 := by rw [mul_inv_cancel₀ ha]

-- ----------------------------------------------
-- Helper: QNR * square = QNR (contrapositive)
-- If n is not a square and s ≠ 0, then n * (s * s) is not a square.
-- Proof: if n * s² = w², then n = (w * s⁻¹)².
-- ----------------------------------------------
lemma qnr_mul_sq (p : ℕ) [Fact p.Prime] (n s : ZMod p) (hs : s ≠ 0)
    (h : ¬ IsSquare n) : ¬ IsSquare (n * (s * s)) := by
  rintro ⟨w, hw⟩
  apply h
  refine ⟨w * s⁻¹, ?_⟩
  have hss_ne : s * s ≠ 0 := mul_ne_zero hs hs
  have hinv_ss : (s * s)⁻¹ = s⁻¹ * s⁻¹ := inv_sq_eq_sq_inv p s hs
  have h1 : (w * s⁻¹) * (w * s⁻¹) = w * w * (s * s)⁻¹ := by rw [hinv_ss]; ring
  rw [h1, ← hw, mul_assoc, mul_inv_cancel₀ hss_ne, mul_one]

-- ----------------------------------------------
-- Lemma: -1 is QNR mod p when p ≡ 3 mod 4
-- ----------------------------------------------
-- Uses ZMod.exists_sq_eq_neg_one_iff from Mathlib.NumberTheory.LegendreSymbol.Basic:
--   IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3
-- The contrapositive gives: p % 4 = 3 → ¬ IsSquare (-1 : ZMod p)

lemma neg_one_qnr_mod_4_3 (p : ℕ) (hp : p.Prime) (hp3 : p % 4 = 3) :
    ¬ IsSquare (-1 : ZMod p) := by
  haveI : Fact p.Prime := ⟨hp⟩
  intro h
  rw [ZMod.exists_sq_eq_neg_one_iff] at h
  omega

-- ----------------------------------------------
-- Lemma: 4 is always QR (it's a perfect square)
-- ----------------------------------------------
lemma four_is_square (p : ℕ) [hp : Fact p.Prime] :
    IsSquare (4 : ZMod p) := by
  exact ⟨2, by norm_num⟩

-- ----------------------------------------------
-- Lemma: 4⁻¹ is QR (inverse of QR is QR)
-- ----------------------------------------------
lemma four_inv_is_square (p : ℕ) [hp : Fact p.Prime] (hp_ne_2 : p ≠ 2) :
    IsSquare ((4 : ZMod p)⁻¹) := by
  -- 4 = 2², so 4⁻¹ = (2⁻¹)², which is a square
  refine ⟨(2 : ZMod p)⁻¹, ?_⟩
  rw [← sq]
  norm_num

-- ----------------------------------------------
-- MAIN LEMMA: QNR Inheritance
-- ----------------------------------------------
-- If n is QNR mod u (prime u ≡ 3 mod 4, n ≡ 1 mod 4),
-- then x = (n+u)/4 is also QNR mod u.
--
-- Proof: x ≡ n · 4⁻¹ mod u. Since 4 = 2², 4⁻¹ = (2⁻¹)² is QR.
-- n is QNR, 4⁻¹ is QR → n · 4⁻¹ is QNR (by qnr_mul_sq).
-- ============================================

lemma qnr_inheritance (n u : ℕ) (hu : u.Prime) (hu3 : u % 4 = 3)
    (hn_mod4 : n % 4 = 1)
    (hn_qnr : ¬ IsSquare (n : ZMod u)) :
    ¬ IsSquare ((((n + u) / 4 : ℕ) : ZMod u)) := by
  haveI : Fact u.Prime := ⟨hu⟩
  -- Step 1: (n+u)/4 = n * 4⁻¹ in ZMod u
  have hdiv : (((n + u) / 4 : ℕ) : ZMod u) = (n : ZMod u) * (4 : ZMod u)⁻¹ :=
    div_cast_eq_inv n u hu hu3 hn_mod4
  rw [hdiv]
  -- Step 2: 4 = 2 * 2, so 4⁻¹ = (2 * 2)⁻¹ = 2⁻¹ * 2⁻¹
  have h4_eq : (4 : ZMod u) = (2 : ZMod u) * (2 : ZMod u) := by norm_num
  rw [h4_eq]
  have h4_inv : ((2 : ZMod u) * (2 : ZMod u))⁻¹ = (2 : ZMod u)⁻¹ * (2 : ZMod u)⁻¹ := by
    apply inv_sq_eq_sq_inv
    intro h
    have : u ∣ 2 := (ZMod.natCast_eq_zero_iff 2 u).mp h
    have hle2 : u ≤ 2 := Nat.le_of_dvd (by norm_num) this
    omega
  rw [h4_inv]
  -- Step 3: 2⁻¹ ≠ 0 (since 2 ≠ 0 mod u, as u ≥ 3)
  have h2_ne_0 : (2 : ZMod u) ≠ 0 := by
    intro h
    have : u ∣ 2 := (ZMod.natCast_eq_zero_iff 2 u).mp h
    have hle2 : u ≤ 2 := Nat.le_of_dvd (by norm_num) this
    omega
  have h2inv_ne_0 : ((2 : ZMod u)⁻¹) ≠ 0 := by
    intro h
    have h1 : (1 : ZMod u) = (2 : ZMod u) * (2 : ZMod u)⁻¹ := by
      rw [mul_inv_cancel₀ h2_ne_0]
    rw [h, mul_zero] at h1
    exact absurd h1 (by norm_num : (1 : ZMod u) ≠ 0)
  -- Step 4: Apply qnr_mul_sq with s = 2⁻¹
  exact qnr_mul_sq u (n : ZMod u) (2 : ZMod u)⁻¹ h2inv_ne_0 hn_qnr

-- ----------------------------------------------
-- Corollary: Target -nx is always QNR mod u
-- ----------------------------------------------
-- For prime u ≡ 3 mod 4, n ≡ 1 mod 4, the target -nx is always QNR mod u.
--
-- Proof: (-1) is QNR for u ≡ 3 mod 4 (Euler's criterion).
--   n QR → x = n·4⁻¹ is QR → -nx = (-1)·n·x = QNR·QR·QR = QNR ✓
--   n QNR → x = n·4⁻¹ is QNR (by inheritance) → -nx = (-1)·n·x = QNR·QNR·QNR
--     = QR·QNR = QNR ✓
-- So in both cases, -nx is QNR. ∎
-- ============================================

lemma target_always_qnr (n u : ℕ) (hu : u.Prime) (hu3 : u % 4 = 3)
    (hn_mod4 : n % 4 = 1) :
    ¬ IsSquare (-(n * ((n + u) / 4 : ℕ) : ZMod u)) := by
  haveI : Fact u.Prime := ⟨hu⟩
  -- x = (n+u)/4, and in ZMod u: x = n * 4⁻¹
  have hdiv : (((n + u) / 4 : ℕ) : ZMod u) = (n : ZMod u) * (4 : ZMod u)⁻¹ :=
    div_cast_eq_inv n u hu hu3 hn_mod4
  -- -1 is QNR mod u (Euler's criterion)
  have h_neg1_qnr : ¬ IsSquare (-1 : ZMod u) := neg_one_qnr_mod_4_3 u hu hu3
  -- Case split: n is QR or QNR mod u
  by_cases hn_qnr : IsSquare (n : ZMod u)
  · -- n is QR: x = n * 4⁻¹ is QR (QR * QR = QR)
    -- -nx = (-1) * n * x = QNR * QR * QR = QNR * QR = QNR
    -- n is QR, 4⁻¹ is QR, so x is QR (product of squares)
    have h4_inv_qr : IsSquare ((4 : ZMod u)⁻¹) := four_inv_is_square u (by
      intro h; have : u = 2 := by
        have hdvd : u ∣ 4 := (ZMod.natCast_eq_zero_iff 4 u).mp (by rw [h] : (4 : ZMod u) = 0)
        have hle4 : u ≤ 4 := Nat.le_of_dvd (by norm_num) hdvd
        omega
      omega)
    -- x = n * 4⁻¹ is QR (product of two squares)
    obtain ⟨a, ha⟩ := hn_qnr
    obtain ⟨b, hb⟩ := h4_inv_qr
    have hx_qr : IsSquare ((n : ZMod u) * (4 : ZMod u)⁻¹) := ⟨a * b, by
      rw [← ha, ← hb]
      ring⟩
    rw [hdiv] at hx_qr
    -- -n * x = (-1) * (n * x), and (-1) is QNR, n*x is QR
    -- QNR * QR = QNR
    obtain ⟨c, hc⟩ := hx_qr
    -- -1 * (c * c) is not a square (by qnr_mul_sq with s such that s*s = -1... no)
    -- Actually, we need: (-1) * (c * c) is not a square
    -- This is qnr_mul_sq applied with n = -1, s = c
    have hc_ne_0 : c ≠ 0 := by
      intro hz
      rw [hz, mul_zero] at hc
      -- (n * 4⁻¹) = 0 means n = 0 or 4⁻¹ = 0
      -- n = 0 would mean u | n, which is possible
      -- 4⁻¹ = 0 would mean 4 = 0, which is false
      sorry -- Edge case: c = 0 means n * 4⁻¹ = 0, need to handle
    -- Apply qnr_mul_sq: (-1) is not a square, c ≠ 0 → (-1) * c² is not a square
    have : ¬ IsSquare ((-1 : ZMod u) * (c * c)) := qnr_mul_sq u (-1 : ZMod u) c hc_ne_0 h_neg1_qnr
    -- But (-1) * c² = -n * x (since c² = n * x and -1 * c² = -c² = -(n*x))
    sorry
  · -- n is QNR: x = n * 4⁻¹ is QNR (by inheritance)
    -- -nx = (-1) * n * x = QNR * QNR * QNR = QR * QNR = QNR
    have hx_qnr : ¬ IsSquare ((((n + u) / 4 : ℕ) : ZMod u)) :=
      qnr_inheritance n u hu hu3 hn_mod4 hn_qnr
    -- -n * x = (-1) * (n * x). We need this is not a square.
    -- (-1) is QNR, n is QNR → (-1)*n is QR (QNR * QNR = QR)
    -- QR * x (QNR) = QNR
    sorry -- Needs: product of QNR * QNR = QR, then QR * QNR = QNR

end ErdosStrausConjecture

-- ============================================
-- THREE-TARGET REDUCTION
-- ============================================
-- The u-method works for (n, u) iff x² has a divisor d' ≡ -x·n^j mod u
-- for some j ∈ {0, 1, 2}.
--
-- Proof: Divisors of D = n²x² are {n^a · d' : a ∈ {0,1,2}, d' | x²}.
-- Target is -nx ≡ -n²·4⁻¹ mod u (since x ≡ n·4⁻¹ mod u).
-- Setting j = 2-a, condition becomes d' ≡ -x·n^j mod u. ∎
-- ============================================

namespace ErdosStrausConjecture

/-- Three-target reduction: the u-method condition reduces to finding
    a divisor of x² congruent to one of three targets mod u. -/
theorem three_target_reduction (n u : ℕ) (hu : u.Prime) (hu3 : u % 4 = 3)
    (hn1 : n % 12 = 1) :
    let x := (n + u) / 4
    (∃ d : ℕ, d ∣ x^2 ∧ ∃ j ∈ ({0,1,2} : Finset ℕ),
        (d : ℤ) ≡ -(x : ℤ) * n^j [ZMOD u]) →
    ∃ y z : ℕ, (4 : ℕ) * x * y * z = n * (x * z + y * z + x * y) := by
  sorry -- Requires substantial machinery (divisor construction from congruence)

/-- Parametric condition: z = my exists iff x has a divisor d' ≡ -x mod u
    OR d' ≡ -nx mod u. -/
theorem parametric_condition (n u : ℕ) (hu : u.Prime) (hu3 : u % 4 = 3) :
    let x := (n + u) / 4
    (∃ d : ℕ, d ∣ x ∧ ((d : ℤ) ≡ -(x : ℤ) [ZMOD u] ∨ (d : ℤ) ≡ -(n * x : ℤ) [ZMOD u])) →
    ∃ y z : ℕ, (4 : ℕ) * x * y * z = n * (x * z + y * z + x * y) := by
  sorry

end ErdosStrausConjecture