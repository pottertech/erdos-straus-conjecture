import Mathlib
import ErdosStrausConjecture.Basic

namespace ErdosStrausConjecture

-- ============================================
-- THEOREM 4: n ≡ 13 (mod 24) → Parametric A = 3
-- ============================================
-- For prime n ≡ 13 mod 24 (hard case), u = 3 always gives a parametric
-- (z = my) solution.
--
-- Proof:
--   n ≡ 13 mod 24 → n ≡ 5 mod 8 → n + 3 ≡ 0 mod 8 → 8 | (n+3) → 2 | (n+3)/4
--   n ≡ 1 mod 3 → x = (n+3)/4 ≡ 1 mod 3 → -x ≡ 2 mod 3
--   Divisor d' = 2 of x satisfies d' ≡ 2 ≡ -x mod 3
--   By parametric condition (Lemma 2), z = my exists.
--
-- The actual Erdős-Straus solution is constructed explicitly:
--   x = (n+3)/4, u = 3
--   Since 2 | x, write x = 2w. Then nx = n*2w.
--   y = (2 + nx) / 3  (divisible since nx ≡ 1 mod 3)
--   z = nx * (nx/2 + 1) / 3  (divisible since nx/2 + 1 ≡ 0 mod 3)
-- ============================================

-- ----------------------------------------------
-- Lemma: n ≡ 13 mod 24 → n ≡ 5 mod 8
-- ----------------------------------------------
lemma mod_24_13_implies_mod_8_5 (n : ℕ) (h : n % 24 = 13) :
    n % 8 = 5 := by omega

-- ----------------------------------------------
-- Lemma: n ≡ 13 mod 24 → n ≡ 1 mod 3
-- ----------------------------------------------
lemma mod_24_13_implies_mod_3_1 (n : ℕ) (h : n % 24 = 13) :
    n % 3 = 1 := by omega

-- ----------------------------------------------
-- Lemma: n ≡ 5 mod 8 → 8 | (n + 3)
-- ----------------------------------------------
lemma mod_8_5_implies_8_dvd_n_plus_3 (n : ℕ) (h : n % 8 = 5) :
    8 ∣ n + 3 := by omega

-- ----------------------------------------------
-- Lemma: 8 | (n+3) → 2 | ((n+3)/4)
-- ----------------------------------------------
lemma eight_dvd_implies_two_dvd_quotient (n : ℕ) (h : 8 ∣ n + 3) :
    2 ∣ (n + 3) / 4 := by
  obtain ⟨k, hk⟩ := h
  -- n + 3 = 8k, so (n+3)/4 = 8k/4 = 2k
  -- Substitute n+3 = 8k everywhere
  rw [hk]
  -- Goal: 2 ∣ (8 * k) / 4
  -- 8k / 4 = 2k since 8k = 4 * (2k)
  have h4_dvd_8k : 4 ∣ 8 * k := ⟨2 * k, by
    show 8 * k = 4 * (2 * k)
    rw [← Nat.mul_assoc]⟩
  have hdiv : (8 * k) / 4 = 2 * k := by
    -- 8 * k = 4 * (2 * k), and 4 > 0
    -- So (8 * k) / 4 = (4 * (2 * k)) / 4 = 2 * k
    have h8k : 8 * k = 4 * (2 * k) := by
      calc 8 * k = (4 * 2) * k := by rw [show (4 : ℕ) * 2 = 8 from by norm_num]
        _ = 4 * (2 * k) := Nat.mul_assoc 4 2 k
    rw [h8k]
    -- Goal: 4 * (2 * k) / 4 = 2 * k
    -- (a * b) / a = b when a > 0
    exact Nat.mul_div_cancel_left _ (by norm_num : (4 : ℕ) > 0)
  rw [hdiv]
  exact ⟨k, rfl⟩

-- ----------------------------------------------
-- Lemma: n ≡ 1 mod 3 and x = (n+3)/4 → x ≡ 1 mod 3
-- Key: 4 * x = n + 3, so 4x ≡ n + 3 ≡ 1 + 0 = 1 mod 3.
-- Since 4 ≡ 1 mod 3, x ≡ 1 mod 3.
-- ----------------------------------------------
lemma x_mod_3_eq_1 (n : ℕ) (hn1 : n % 3 = 1) (x : ℕ) (hx : 4 * x = n + 3) :
    x % 3 = 1 := by
  -- 4x = n + 3, so 4x ≡ n + 3 ≡ 1 + 0 = 1 (mod 3)
  -- 4 ≡ 1 (mod 3), so x ≡ 1 (mod 3)
  have h4x_mod3 : (4 * x) % 3 = (n + 3) % 3 := by rw [hx]
  have hn3_mod3 : (n + 3) % 3 = 1 := by omega
  rw [hn3_mod3] at h4x_mod3
  -- h4x_mod3 : (4 * x) % 3 = 1
  -- (4 * x) % 3 = ((4 % 3) * (x % 3)) % 3 = (1 * (x % 3)) % 3 = x % 3
  have h4_mod3 : (4 : ℕ) % 3 = 1 := by norm_num
  have hmul : (4 * x) % 3 = ((4 % 3) * (x % 3)) % 3 := Nat.mul_mod 4 x 3
  rw [h4_mod3] at hmul
  -- hmul : 1 * (x % 3) % 3 = (4 * x) % 3
  -- h4x_mod3 : (4 * x) % 3 = 1
  -- So 1 * (x % 3) % 3 = 1, and since x % 3 < 3, 1 * (x%3) = x%3
  omega

-- ----------------------------------------------
-- MAIN THEOREM: n ≡ 13 mod 24 → Erdős-Straus solution with A = 3
-- ----------------------------------------------
-- This constructs the explicit solution:
--   x = (n+3)/4, y = (2 + n*x) / 3, z = n*x * (n*x/2 + 1) / 3
--
-- Key divisibility facts:
--   1. 8 | (n+3) → x = (n+3)/4 is even → 2 | n*x
--   2. n*x ≡ 1 mod 3 → 3 | (2 + n*x)
--   3. n*x/2 + 1 ≡ 2 + 1 = 0 mod 3 → 3 | (n*x * (n*x/2 + 1))
--
-- The algebraic identity 4xyz = n(xy + xz + yz) follows by ring.
-- ============================================

theorem theorem4_parametric_a3 (n : ℕ) (hn : n ≥ 13)
    (hn_mod : n % 24 = 13) :
    IsErdosStraus n := by
  -- Set up variables
  set x := (n + 3) / 4
  -- 4 * x = n + 3
  have h4x : 4 * x = n + 3 := by
    have h4 : 4 ∣ n + 3 := by omega
    have hdiv := Nat.div_mul_cancel h4
    -- hdiv : (n+3)/4 * 4 = n+3, i.e., x * 4 = n + 3
    -- Need 4 * x = n + 3, which is mul_comm
    rw [mul_comm] at hdiv
    exact hdiv
  have hx_pos : x > 0 := by omega
  -- n ≡ 1 mod 3
  have hn_mod3 : n % 3 = 1 := mod_24_13_implies_mod_3_1 n hn_mod
  -- x ≡ 1 mod 3
  have hx_mod3 : x % 3 = 1 := x_mod_3_eq_1 n hn_mod3 x h4x
  -- x is even (2 | x)
  have h8_dvd : 8 ∣ n + 3 := mod_8_5_implies_8_dvd_n_plus_3 n
    (mod_24_13_implies_mod_8_5 n hn_mod)
  have h2_dvd_x : 2 ∣ x := eight_dvd_implies_two_dvd_quotient n h8_dvd
  obtain ⟨w, hw⟩ := h2_dvd_x
  have hx_eq : x = 2 * w := by omega
  -- nx = n * x = n * 2w, so nx is even
  set nx := n * x
  have hnx_even : Even nx := by
    have hx_even : Even x := ⟨w, by omega⟩
    exact hx_even.mul_left n
  obtain ⟨w2, hw2⟩ := hnx_even
  have h2w2 : 2 * w2 = nx := by omega
  -- nx ≡ 1 mod 3 (since n ≡ 1, x ≡ 1 → nx ≡ 1)
  have hnx_mod3 : nx % 3 = 1 := by
    have hmul : (n * x) % 3 = ((n % 3) * (x % 3)) % 3 := Nat.mul_mod n x 3
    rw [hmul, hn_mod3, hx_mod3]
  -- 3 | (2 + nx) since nx ≡ 1 → 2 + nx ≡ 0 mod 3
  have h3_dvd_2nx : 3 ∣ 2 + nx := by omega
  -- 3 | (nx * (w2 + 1)) since w2 ≡ 2 mod 3 → w2 + 1 ≡ 0 mod 3
  have hw2_mod3 : w2 % 3 = 2 := by
    -- 2 * w2 = nx, nx ≡ 1 mod 3
    have hmul : (2 * w2) % 3 = ((2 : ℕ) % 3 * (w2 % 3)) % 3 := Nat.mul_mod 2 w2 3
    have h2_mod3 : (2 : ℕ) % 3 = 2 := by norm_num
    -- 2 * w2 % 3 = nx % 3 = 1
    have : (2 * w2) % 3 = 1 := by omega
    omega
  have h3_dvd_nx_w2p1 : 3 ∣ nx * (w2 + 1) := by
    -- w2 + 1 ≡ 2 + 1 = 0 mod 3 → 3 | (w2 + 1)
    have h3_dvd_w2p1 : 3 ∣ w2 + 1 := by omega
    -- 3 | (w2 + 1) → 3 | (nx * (w2 + 1))
    obtain ⟨k, hk⟩ := h3_dvd_w2p1
    refine ⟨nx * k, ?_⟩
    rw [hk]; ring
  -- Construct y and z
  set y := (2 + nx) / 3
  set z := (nx * (w2 + 1)) / 3
  -- Divisibility gives us the key equations
  have h3y : 3 * y = 2 + nx := by
    have := Nat.div_mul_cancel h3_dvd_2nx
    -- this : y * 3 = 2 + nx (after set)
    rw [mul_comm] at this
    exact this
  have h3z : 3 * z = nx * (w2 + 1) := by
    have := Nat.div_mul_cancel h3_dvd_nx_w2p1
    -- this : z * 3 = nx * (w2 + 1) (after set)
    rw [mul_comm] at this
    exact this
  -- Positivity
  have hy_pos : y > 0 := by
    have : 3 ≤ 2 + nx := by omega
    exact Nat.div_pos this (by norm_num)
  have hz_pos : z > 0 := by
    have hx_ge2 : x ≥ 2 := by omega
    have hnx_ge : nx ≥ 26 := by
      calc nx = n * x := rfl
        _ ≥ 13 * 2 := by gcongr
        _ = 26 := by norm_num
    have hw2_ge : w2 ≥ 13 := by omega
    have hw2p1_ge : w2 + 1 ≥ 14 := by omega
    have : 3 ≤ nx * (w2 + 1) := by
      calc nx * (w2 + 1) ≥ 26 * 14 := by gcongr
        _ = 364 := by norm_num
        _ ≥ 3 := by norm_num
    exact Nat.div_pos this (by norm_num)
  -- The key relation: 2*w2 + 3*x = 4*x²
  -- From 2*w2 = nx = n*x and 4*x = n + 3:
  -- 2*w2 + 3*x = n*x + 3*x = (n+3)*x = 4x*x
  have hrel : 2 * w2 + 3 * x = 4 * x * x := by
    calc 2 * w2 + 3 * x
        = nx + 3 * x := by omega
      _ = n * x + 3 * x := by rfl
      _ = (n + 3) * x := by ring
      _ = (4 * x) * x := by rw [← h4x]
      _ = 4 * x * x := by ring
  -- Main identity: 4*x*y*z = n*(x*y + x*z + y*z)
  -- Strategy: multiply both sides by 9, substitute 3y and 3z, use ring
  have hmain : 4 * x * y * z = n * (x * y + x * z + y * z) := by
    -- Substitute 3*y = 2+nx, 3*z = nx*(w2+1), 2*w2 = nx into the identity
    -- We work with the expanded form directly
    -- The key polynomial identity (with correction term):
    -- 4x*(2+2w2)*(2w2*(w2+1)) + 6*(w2+1)²*(2w2+3x) =
    -- n*(3x*(2+2w2) + 3x*(2w2*(w2+1)) + (2+2w2)*(2w2*(w2+1))) + 6*(w2+1)²*(4x²)
    have hcorr :
        4 * x * (2 + 2 * w2) * (2 * w2 * (w2 + 1)) +
        6 * (w2 + 1) * (w2 + 1) * (2 * w2 + 3 * x) =
        n * (3 * x * (2 + 2 * w2) + 3 * x * (2 * w2 * (w2 + 1)) +
             (2 + 2 * w2) * (2 * w2 * (w2 + 1))) +
        6 * (w2 + 1) * (w2 + 1) * (4 * x * x) := by
      -- Use linear_combination in ℤ
      have h4x_int : (4 * x : ℤ) = n + 3 := by exact_mod_cast h4x
      have h2w2_int : (2 * w2 : ℤ) = n * x := by exact_mod_cast h2w2
      have h_int :
          ((4 * x * (2 + 2 * w2) * (2 * w2 * (w2 + 1) : ℕ) +
            6 * (w2 + 1) * (w2 + 1) * (2 * w2 + 3 * x : ℕ) : ℤ)) =
          ((n * (3 * x * (2 + 2 * w2) + 3 * x * (2 * w2 * (w2 + 1)) +
             (2 + 2 * w2) * (2 * w2 * (w2 + 1)) : ℕ) +
            6 * (w2 + 1) * (w2 + 1) * (4 * x * x : ℕ) : ℤ)) := by
        push_cast
        linear_combination -2 * (w2 + 1)^2 * ((3*x - 2*w2) * h4x_int + (-6) * h2w2_int)
      exact Int.ofNat_inj.mp h_int
    -- Use hrel to replace 2*w2 + 3*x with 4*x*x in the correction
    rw [hrel] at hcorr
    -- Connect (2 + 2*w2) = 3*y and (2*w2*(w2+1)) = 3*z
    have h3y_eq : 2 + 2 * w2 = 3 * y := by omega
    have h3z_eq : 2 * w2 * (w2 + 1) = 3 * z := by
      calc 2 * w2 * (w2 + 1)
          = (2 * w2) * (w2 + 1) := by ring
        _ = nx * (w2 + 1) := by rw [h2w2]
        _ = 3 * z := h3z.symm
    -- Rewrite hcorr using these equalities
    rw [h3y_eq, h3z_eq] at hcorr
    -- Cancel 6*(w2+1)^2*(4*x*x) from both sides
    have h9_identity : 4 * x * (3 * y) * (3 * z) =
        n * (3 * x * (3 * y) + 3 * x * (3 * z) + (3 * y) * (3 * z)) :=
      add_right_cancel hcorr
    -- Extract from the ×9 identity
    have e1 : 4 * x * (3 * y) * (3 * z) = 9 * (4 * x * y * z) := by ring
    have e2 : n * (3 * x * (3 * y) + 3 * x * (3 * z) + (3 * y) * (3 * z)) =
        9 * (n * (x * y + x * z + y * z)) := by ring
    -- Combined: 9*(4xyz) = 9*(n*(xy+xz+yz))
    have h9 : 9 * (4 * x * y * z) = 9 * (n * (x * y + x * z + y * z)) := by
      rw [← e1, ← e2]; exact h9_identity
    -- Cancel the 9
    exact Nat.mul_left_cancel (by norm_num : (9 : ℕ) > 0) h9
  exact ⟨x, y, z, hx_pos, hy_pos, hz_pos, hmain⟩

-- ============================================
-- COROLLARY: n ≡ 13 mod 24 (any n ≥ 13, not just prime)
-- ============================================
-- Note: The proof only uses n ≡ 13 mod 24, not primality.
-- So this works for ALL n ≡ 13 mod 24, not just primes.

theorem erdos_straus_mod_24_13 (n : ℕ) (hn : n ≥ 13) (hmod : n % 24 = 13) :
    IsErdosStraus n := theorem4_parametric_a3 n hn hmod

end ErdosStrausConjecture