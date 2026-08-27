/-
# Erdős-Straus Conjecture: Modular Identities

This file proves parametric identities providing explicit solutions
to the Erdős-Straus equation 4/n = 1/x + 1/y + 1/z for various
residue classes of n.

Cross-multiplied form: 4*x*y*z = n*(x*z + y*z + x*y)
-/

import Mathlib
import ErdosStraus.Basic

open Nat

/-! ## Case 1: n ≡ 0 mod 3 (n = 3k)

For n = 3k, the solution is x = 3k, y = 2k, z = 2k.
Identity: 4/(3k) = 1/(3k) + 1/(2k) + 1/(2k)
Check: 1/(3k) + 2/(2k) = 1/(3k) + 1/k = (1 + 3)/(3k) = 4/(3k) ✓
-/

theorem ErdosStraus.case_mod_3 (k : ℕ) (hk : k > 0) :
    ErdosStraus.eq (3 * k) (3 * k) (2 * k) (2 * k) := by
  refine ⟨mul_pos (by norm_num) hk, mul_pos (by norm_num) hk,
    mul_pos (by norm_num) hk, mul_pos (by norm_num) hk, ?_⟩
  -- 4 * (3k) * (2k) * (2k) = (3k) * ((3k)*(2k) + (2k)*(2k) + (3k)*(2k))
  ring

/-! ## Case 2: n ≡ 2 mod 3 (n = 3k + 2)

For n = 3k + 2, the solution is x = n, y = k+1, z = n*(k+1).
Identity: 4/n = 1/n + 1/(k+1) + 1/(n*(k+1))
Check: 1/n + 1/(k+1) + 1/(n(k+1)) = 1/n + (n+1)/(n(k+1))
     = 1/n + (3k+3)/(n(k+1)) = 1/n + 3/n = 4/n ✓
-/

theorem ErdosStraus.case_mod_3_eq_2 (k : ℕ) :
    ErdosStraus.eq (3 * k + 2) (3 * k + 2) (k + 1) ((3 * k + 2) * (k + 1)) := by
  refine ⟨by omega, by omega, by omega, by omega, ?_⟩
  -- Let n = 3k + 2. Prove: 4 * n * (k+1) * n*(k+1) = n * (n * n*(k+1) + (k+1)*n*(k+1) + n*(k+1))
  -- RHS = n²(k+1)(n + k + 2) = n²(k+1)(4k+4) = 4n²(k+1)² = LHS
  ring

/-! ## General lemma: n even → x = n/2, y = n, z = n

For any even n ≥ 2: 4/n = 1/(n/2) + 1/n + 1/n = 2/n + 1/n + 1/n = 4/n ✓
This covers n ≡ 4 mod 12 and n ≡ 10 mod 12.
-/

theorem ErdosStraus.case_even (n : ℕ) (hn : n ≥ 2) (h2 : 2 ∣ n) :
    ErdosStraus.eq n (n / 2) n n := by
  have hn_pos : n > 0 := by omega
  have hndiv2_pos : n / 2 > 0 := by
    rw [Nat.div_pos_iff (by norm_num)]
    omega
  refine ⟨hn_pos, hndiv2_pos, hn_pos, hn_pos, ?_⟩
  -- (n/2) * 2 = n since 2 | n
  have hndiv2 : (n / 2) * 2 = n := Nat.div_mul_cancel (by norm_num) h2
  -- 4 * (n/2) * n * n = 2 * ((n/2)*2) * n * n = 2 * n * n * n
  -- n * ((n/2)*n + n*n + (n/2)*n) = n * ((n/2)*2*n + n*n) = n * (n² + n²) = 2n³
  calc 4 * (n / 2) * n * n
      = 2 * ((n / 2) * 2) * n * n := by ring
    _ = 2 * n * n * n := by rw [hndiv2]
    _ = n * ((n / 2) * 2 * n + n * n) := by rw [hndiv2]; ring
    _ = n * (n / 2 * n + n * n + n / 2 * n) := by ring

/-! ## Case 3: n ≡ 4 mod 12

n ≡ 4 mod 12 → n is even → apply case_even.
-/

theorem ErdosStraus.case_mod_12_eq_4 (n : ℕ) (hn : n ≡ 4 [MOD 12]) (hge : n ≥ 4) :
    ErdosStraus.eq n (n / 2) n n := by
  apply ErdosStraus.case_even n hge
  -- n ≡ 4 mod 12 → n ≡ 0 mod 2
  have : n ≡ 0 [MOD 2] := by
    have h4_mod_2 : (4 : ℕ) ≡ 0 [MOD 2] := by decide
    exact Nat.Modeq.trans hn h4_mod_2
  exact (Nat.modeq_zero_iff_dvd (n := n)).mp this

/-! ## Case 4: n ≡ 10 mod 12

n ≡ 10 mod 12 → n is even → apply case_even.
-/

theorem ErdosStraus.case_mod_12_eq_10 (n : ℕ) (hn : n ≡ 10 [MOD 12]) (hge : n ≥ 10) :
    ErdosStraus.eq n (n / 2) n n := by
  apply ErdosStraus.case_even n hge
  -- n ≡ 10 mod 12 → n ≡ 0 mod 2
  have : n ≡ 0 [MOD 2] := by
    have h10_mod_2 : (10 : ℕ) ≡ 0 [MOD 2] := by decide
    exact Nat.Modeq.trans hn h10_mod_2
  exact (Nat.modeq_zero_iff_dvd (n := n)).mp this

/-! ## Case 5: n ≡ 7 mod 12

For n ≡ 7 mod 12, n is odd and n+1 ≡ 8 mod 12, so 4 | (n+1) and 2 | (n+1).
The identity: 4/n = 4/(n+1) + 4/(n(n+1))
           = 1/((n+1)/4) + 1/(n(n+1)/4)  [two unit fractions]
           = 1/((n+1)/4) + 1/(2·n(n+1)/8) + 1/(2·n(n+1)/8)  [split second fraction]

Actually, let's use a cleaner 3-term decomposition:
4/n = 1/((n+1)/4) + 1/(n(n+1)/2) + 1/(n(n+1)/2)
Check: 4/(n+1) + 2/(n(n+1)/2) = 4/(n+1) + 4/(n(n+1)) = (4n + 4)/(n(n+1)) = 4/n ✓

With n = 7: x = 2, y = z = 28.  4·2·28·28 = 6272 = 7·(56+784+56) = 7·896 = 6272 ✓
-/

theorem ErdosStraus.case_mod_12_eq_7 (n : ℕ) (hn : n ≡ 7 [MOD 12]) (hge : n ≥ 7) :
    ErdosStraus.eq n ((n + 1) / 4) (n * (n + 1) / 2) (n * (n + 1) / 2) := by
  -- n ≡ 7 mod 12 → n+1 ≡ 8 mod 12 → 4 | (n+1) and 2 | (n+1)
  have hnp1_mod8 : n + 1 ≡ 8 [MOD 12] := by
    have : n + 1 ≡ 7 + 1 [MOD 12] := Nat.Modeq.add hn (by decide)
    exact this
  have h4_dvd_np1 : 4 ∣ n + 1 := by
    have h_np1_mod4 : n + 1 ≡ 0 [MOD 4] := by
      have h8_mod4 : (8 : ℕ) ≡ 0 [MOD 4] := by decide
      exact Nat.Modeq.trans hnp1_mod8 h8_mod4
    exact (Nat.modeq_zero_iff_dvd (n := n + 1)).mp h_np1_mod4
  have h2_dvd_np1 : 2 ∣ n + 1 := by
    have h_np1_mod2 : n + 1 ≡ 0 [MOD 2] := by
      have h8_mod2 : (8 : ℕ) ≡ 0 [MOD 2] := by decide
      exact Nat.Modeq.trans hnp1_mod8 h8_mod2
    exact (Nat.modeq_zero_iff_dvd (n := n + 1)).mp h_np1_mod2
  have h2_dvd_nnp1 : 2 ∣ n * (n + 1) := Dvd.dvd.mul_left (n + 1) h2_dvd_np1
  -- Key divisibility identities
  have h_np1_div4 : (n + 1) / 4 * 4 = n + 1 := Nat.div_mul_cancel (by norm_num) h4_dvd_np1
  have h_nnp1_div2 : n * (n + 1) / 2 * 2 = n * (n + 1) := Nat.div_mul_cancel (by norm_num) h2_dvd_nnp1
  -- Positivity
  have hn_pos : n > 0 := by omega
  have hxp_pos : (n + 1) / 4 > 0 := by
    rw [Nat.div_pos_iff (by norm_num)]
    constructor
    · exact hge
    · omega
  have hnp1_pos : n + 1 > 0 := by omega
  have hnnp1_pos : n * (n + 1) > 0 := mul_pos hn_pos hnp1_pos
  have hyz_pos : n * (n + 1) / 2 > 0 := by
    rw [Nat.div_pos_iff (by norm_num)]
    exact ⟨h2_dvd_nnp1, by omega⟩
  refine ⟨hn_pos, hxp_pos, hyz_pos, hyz_pos, ?_⟩
  -- Prove: 4 * ((n+1)/4) * (n(n+1)/2) * (n(n+1)/2) = n * (((n+1)/4) * (n(n+1)/2) + (n(n+1)/2) * (n(n+1)/2) + ((n+1)/4) * (n(n+1)/2))
  -- Let a = (n+1)/4, b = n(n+1)/2. Then:
  -- LHS = 4ab²
  -- RHS = n(a²b + b² + ab²) = n·b·(a² + b + ab) = n·b·(a² + b(1+a))
  -- With a = (n+1)/4, b = n(n+1)/2 = 2n·a:
  -- b = 2n·a (since n(n+1)/2 = n·(n+1)/2 = n·2a when (n+1)/4 = a, so (n+1) = 4a, b = n·4a/2 = 2na)
  -- LHS = 4a·(2na)² = 4a·4n²a² = 16n²a³
  -- RHS = n·(a·2na + (2na)² + a·2na) = n·(2n²a² + 4n²a² + 2n²a²) = n·8n²a² = 8n³a²
  -- 16n²a³ = 8n³a² → 2a = n → n+1 = 2n → 1 = n. That's wrong!
  -- Let me recheck. b = n(n+1)/2, a = (n+1)/4. b/a = n(n+1)/2 / ((n+1)/4) = 4n/2 = 2n.
  -- So b = 2na. ✓
  -- LHS = 4·a·(2na)² = 4a·4n²a² = 16n²a³
  -- RHS = n·(a·2na + (2na)² + a·2na) = n·(2n²a² + 4n²a² + 2n²a²) = n·8n²a² = 8n³a²
  -- 16n²a³ vs 8n³a² → 2a vs n → 2(n+1)/4 vs n → (n+1)/2 vs n. Only equal when n=1. WRONG!
  -- So my identity is wrong. Let me recheck.
  -- 4/n = 4/(n+1) + 4/(n(n+1))  [this is correct: (4n+4)/(n(n+1)) = 4(n+1)/(n(n+1)) = 4/n]
  -- 4/(n+1) = 1/((n+1)/4) = 1/a  [correct, since a = (n+1)/4]
  -- 4/(n(n+1)) = 1/(n(n+1)/4) = 1/(n·a)  [since (n+1)/4 = a, n(n+1)/4 = na]
  -- So 4/n = 1/a + 1/(na). That's only 2 unit fractions!
  -- To get 3, split 1/(na) = 1/(2na) + 1/(2na):
  -- 4/n = 1/a + 1/(2na) + 1/(2na)
  -- Cross-multiply: 4·a·(2na)·(2na) = n·(a·2na + 2na·2na + a·2na)
  -- LHS = 4a·4n²a² = 16n²a³
  -- RHS = n·(2n²a² + 4n²a² + 2n²a²) = n·8n²a² = 8n³a²
  -- 16n²a³ = 8n³a² → 2a = n → (n+1)/2 = n → n = 1. STILL WRONG!
  -- The issue: 1/(na) = 1/(2na) + 1/(2na) gives 2/(2na) = 1/(na). ✓
  -- But 4/n = 1/a + 1/(na) = (n + 1)/(na) = (n+1)/(n·(n+1)/4) = 4/n. ✓
  -- So 4/n = 1/a + 1/(na) = 1/a + 2/(2na) = 1/a + 1/(2na) + 1/(2na). ✓
  -- The cross-multiplied form should be:
  -- 4·a·(2na)·(2na) = n·(a·(2na) + (2na)·(2na) + a·(2na))
  -- But that's 4/(1/a + 1/(2na) + 1/(2na)) which should equal n.
  -- 1/a + 1/(2na) + 1/(2na) = 1/a + 1/(na) = (n+1)/(na) = (n+1)/(n·(n+1)/4) = 4/n. ✓
  -- So the cross-multiplied form is: 4·x·y·z = n·(xz + yz + xy)
  -- where x = a, y = 2na, z = 2na.
  -- 4·a·(2na)·(2na) = 4a·4n²a² = 16n²a³
  -- n·(a·2na + 2na·2na + a·2na) = n·(2n²a² + 4n²a² + 2n²a²) = n·8n²a² = 8n³a²
  -- 16n²a³ = 8n³a² → 2a = n → WRONG for n > 1.
  -- Wait, something is wrong with my cross-multiplication.
  -- 4/n = 1/x + 1/y + 1/z
  -- → 4/n = (yz + xz + xy)/(xyz)
  -- → 4xyz = n(xz + yz + xy). That's correct.
  -- With x = a, y = 2na, z = 2na:
  -- xz + yz + xy = a·2na + 2na·2na + a·2na = 2n²a² + 4n²a² + 2n²a² = 8n²a²
  -- 4xyz = 4·a·2na·2na = 16n²a³
  -- n(xz + yz + xy) = n·8n²a² = 8n³a²
  -- 16n²a³ = 8n³a² → 2a = n → (n+1)/2 = n → n = 1. WRONG!
  -- So my decomposition is wrong. Let me recheck.
  -- 4/n = 1/a + 1/(2na) + 1/(2na) where a = (n+1)/4.
  -- Check: 1/a + 1/(2na) + 1/(2na) = 1/a + 1/(na) = (n + 1)/(na) = (n+1)/(n(n+1)/4) = 4/n. ✓
  -- So the arithmetic is correct. The issue must be in the cross-multiplication.
  -- 4/n = 1/a + 1/(2na) + 1/(2na)
  -- → 4 = n·(1/a + 1/(2na) + 1/(2na))·(a·2na·2na)/(a·2na·2na)
  -- Hmm, let me just directly compute:
  -- 4xyz = 4·a·(2na)·(2na) = 16n²a³
  -- n(xz + yz + xy) = n·(2na² + 4n²a² + 2na²) = n·(4na² + 4n²a²) = n·4na²(1 + n) = 4n²a²(n+1)
  -- Wait, let me recompute xz + yz + xy:
  -- x = a, y = 2na, z = 2na
  -- xz = a · 2na = 2na²
  -- yz = 2na · 2na = 4n²a²
  -- xy = a · 2na = 2na²
  -- xz + yz + xy = 2na² + 4n²a² + 2na² = 4na² + 4n²a² = 4na²(n + 1)
  -- n(xz + yz + xy) = n · 4na²(n+1) = 4n²a²(n+1)
  -- 4xyz = 16n²a³
  -- So we need: 16n²a³ = 4n²a²(n+1), i.e., 4a = n+1, i.e., a = (n+1)/4. ✓!
  -- So the identity IS correct. I made an arithmetic error before. Let me redo:
  -- 4xyz = 4·a·(2na)·(2na) = 4a·4n²a² = 16n²a³
  -- n(xz + yz + xy) = n·(2na² + 4n²a² + 2na²) = n·(4na² + 4n²a²) = n·4na²(1+n) = 4n²a²(n+1)
  -- 16n²a³ = 4n²a²(n+1) → 4a = n+1 → a = (n+1)/4. ✓!
  -- Great! So the identity is correct. The issue was my arithmetic. Now I need y = 2na.
  -- But 2na = 2n·(n+1)/4 = n(n+1)/2. So y = z = n(n+1)/2. ✓
  -- And x = (n+1)/4. ✓
  -- So the cross-multiplied equation becomes:
  -- 4 · ((n+1)/4) · (n(n+1)/2) · (n(n+1)/2) = n · (((n+1)/4)·(n(n+1)/2) + (n(n+1)/2)·(n(n+1)/2) + ((n+1)/4)·(n(n+1)/2))
  -- Let a = (n+1)/4, b = n(n+1)/2. We need: 4ab² = n(a²b + b² + ab²) wait no:
  -- xz + yz + xy = a·b + b·b + a·b = 2ab + b²
  -- n(xz + yz + xy) = n(2ab + b²) = n·b·(2a + b)
  -- 4xyz = 4·a·b·b = 4ab²
  -- So we need: 4ab² = n·b·(2a + b), i.e., 4ab = n(2a + b).
  -- 4a = n+1, b = n(n+1)/2 = 2na (since 4a = n+1, so n(n+1)/2 = n·4a/2 = 2na).
  -- 4ab = 4a·2na = 8na²
  -- n(2a + b) = n(2a + 2na) = n·2a(1 + n) = 2na(n+1) = 2na·4a = 8na². ✓!
  -- Great, so the proof needs: 4·a·b² = n·b·(2a + b) where a = (n+1)/4, b = n(n+1)/2.
  -- In Lean, we need to use the divisibility facts to rewrite (n+1)/4 * 4 = n+1 and
  -- n*(n+1)/2 * 2 = n*(n+1), then use ring.
  -- Let me structure the proof:
  sorry