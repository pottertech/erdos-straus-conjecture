import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.UMethod
import ErdosStrausLean.StructuralLemmas

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩

-- Restate proven lemmas
theorem qr_ne_qnr_mod_p (a b : ℤ) (ha : legendreSym 7 a = 1) (hb : legendreSym 7 b = -1) :
    a % 7 ≠ b % 7 := by
  intro h
  have hmod_a : legendreSym 7 a = legendreSym 7 (a % 7) := legendreSym.mod (p := 7) a
  have hmod_b : legendreSym 7 b = legendreSym 7 (b % 7) := legendreSym.mod (p := 7) b
  rw [hmod_a] at ha; rw [hmod_b] at hb
  rw [h] at ha; rw [hb] at ha; norm_num at ha

-- Key intermediate: if 4*x*y*z = n*(x*z + y*z + x*y) and u = 4x - n,
-- then d₁ = u*y - n*x divides n²x² and d₁ ≡ -n*x mod u
-- This follows from umethod_identity: (uy-nx)(uz-nx) = n²x²
-- So d₁ = uy-nx is a divisor of n²x², and d₁ mod u = (uy-nx) mod u = -nx mod u

-- For the A=7 obstruction, we need the contrapositive:
-- If no divisor of n²x² matches -nx mod 7, then no solution exists.

-- Let me prove this for a specific case: n=29 (≡ 1 mod 7, ≡ 1 mod 12)
-- 29 mod 7 = 1, 29 mod 12 = 5... no, 29 = 2*12+5, so 29 ≡ 5 mod 12.
-- Need n ≡ 1 mod 12 and n ≡ 1 mod 7. n=49? 49=4*12+1 ✓, 49=7*7 → 49 ≡ 0 mod 7. No.
-- n=85? 85=7*12+1 ✓, 85 mod 7 = 85-12*7=85-84=1 ✓. But 85=5*17, 5|85. Not a hard case.
-- n=121? 121=10*12+1 ✓, 121 mod 7 = 121-17*7=121-119=2. Not 1 mod 7.
-- n=169? 169=14*12+1 ✓, 169 mod 7 = 169-24*7=169-168=1 ✓. 5∤169 ✓. 169=13².
-- Let me use n=169 as the test case.

-- For n=169: x=(169+7)/4=44, nx=169*44=7436, D=169²*44²=28561*1936=55286096
-- -nx mod 7: 7436 mod 7 = 7436-1062*7=7436-7434=2, -7436≡-2≡5 mod 7
-- So target is 5, which is QNR mod 7 ✅
-- All prime factors of D=169²*44²: 13 (from 169) and 2, 11 (from 44)
-- 13 mod 7 = 6 (QNR), so 13 is NOT QR mod 7 → the obstruction doesn't apply to 169
-- The obstruction applies when ALL prime factors are QR mod 7 = {1,2,4}

-- For the obstruction to apply, we need n(n+7) to have all prime factors in {1,2,4} mod 7.
-- This is a strong condition. Let me just prove the theorem statement with `sorry`
-- replaced by the argument structure, even if the specific n conditions aren't met.

-- Actually, let me just try to close the sorry with the right proof structure.
-- The theorem says: IF all prime factors of n(n+7) (≠2,7) are QR mod 7, THEN no solution.
-- Proof: By contradiction. Suppose y,z satisfy the ES equation with x=(n+7)/4.
-- By u-method: d₁ = 7y - nx divides D=n²x², and d₁ ≡ -nx mod 7.
-- All prime factors of D divide n*(n+7), so they're all QR mod 7.
-- By all_qr_factors_implies_qr: d₁ is QR mod 7 (as a divisor of D).
-- But -nx is QNR mod 7 (need to prove this from n ≡ 1 mod 12).
-- By qr_ne_qnr_mod_p: d₁ ≢ -nx mod 7. Contradiction with d₁ ≡ -nx mod 7.

-- The tricky part: proving -nx is QNR mod 7 from the given conditions.
-- n ≡ 1 mod 12 → n ≡ 1 mod 4 (so (n+7) ≡ 0 mod 4, x is integer)
-- n ≡ 1 mod 12 → n ≡ 1 mod 3
-- But we need n mod 7. The obstruction hypothesis says all prime factors of n(n+7)
-- are QR mod 7 = {1,2,4}. If n ≡ 1 mod 7, then n+7 ≡ 1 mod 7, x ≡ 2 mod 7,
-- nx ≡ 2 mod 7, -nx ≡ 5 mod 7 (QNR ✅).
-- But the hypothesis doesn't directly tell us n ≡ 1 mod 7.
-- Actually, if n itself has all prime factors QR mod 7, then n is QR mod 7.
-- And n+7 has all prime factors QR mod 7, so n+7 is QR mod 7.
-- But QR values mod 7 are {1,2,4}. So n mod 7 ∈ {1,2,4} and (n+7) mod 7 = n mod 7 ∈ {1,2,4}.
-- x = (n+7)/4. 4⁻¹ mod 7 = 2. So x mod 7 = 2*(n mod 7).
-- If n ≡ 1: x ≡ 2, nx ≡ 2, -nx ≡ 5 (QNR ✅)
-- If n ≡ 2: x ≡ 4, nx ≡ 8 ≡ 1, -nx ≡ 6 (QNR ✅)
-- If n ≡ 4: x ≡ 1, nx ≡ 4, -nx ≡ 3 (QNR ✅)
-- In ALL cases where n is QR mod 7 (and n+7 ≡ n mod 7), -nx is QNR mod 7! ✅

-- This is the key insight: for ANY QR value of n mod 7, -nx is always QNR mod 7.
-- This follows from: -1 is QNR mod 7 (since 7 ≡ 3 mod 4), and x is QR (since x = (n+7)/4
-- and 4 is QR, so x ≡ (n+7)*4⁻¹ ≡ n*2 mod 7, and QR*QR = QR).
-- So -nx = (-1)*n*x = QNR*QR*QR = QNR. ✅

-- This is exactly what neg_four_n_qnr proves (for general u ≡ 3 mod 4)!
-- neg_four_n_qnr : if n is QR mod u and u ≡ 3 mod 4, then -4n is QNR mod u
-- But we need -nx, not -4n. However, x = (n+7)/4, so nx = n*(n+7)/4.
-- -nx = -n*(n+7)/4. Since 4 is QR, -nx/(-1) = nx is QR (n is QR, x is QR).
-- So -nx = (-1)*nx, and -1 is QNR (7 ≡ 3 mod 4), so -nx = QNR*QR = QNR. ✅

-- This is exactly neg_n_qnr! With u=7, n_qr = nx (which is QR), we get -nx is QNR.
-- But we need to prove nx is QR first: nx = n*x, both QR → product is QR.

-- OK this is getting complex. Let me just try to prove the full theorem and see
-- what Lean can verify.

-- For now, let me just prove a simpler version: the obstruction for a specific n
-- where we can verify everything by computation.

-- n=121: 121 ≡ 1 mod 12 ✓, 121 mod 7 = 2 (QR ✓), 121 = 11², 11 mod 7 = 4 (QR ✓)
-- 128 = 121+7 = 128, 128 = 2⁷, 2 mod 7 = 2 (QR ✓)
-- So all prime factors of 121*128 = 15488 are QR mod 7 ✓
-- x = 128/4 = 32, nx = 121*32 = 3872, D = 121²*32² = 14641*1024 = 14992384
-- -nx mod 7: 3872 mod 7 = 3872-553*7=3872-3871=1, -3872 ≡ -1 ≡ 6 mod 7 (QNR ✓)
-- So the obstruction should apply!

-- To prove no solution exists, we'd need to check that no divisor of 14992384
-- is ≡ 6 mod 7. But 14992384 = 2⁷ * 11², and divisors are 2^a * 11^b for a≤7, b≤2.
-- 2 mod 7 = 2, 11 mod 7 = 4. So divisors mod 7 = 2^a * 4^b mod 7.
-- 2^a mod 7: 1,2,4,1,2,4,1,2 (period 3)
-- 4^b mod 7: 1,4,2 (period 3)
-- Products: {1,2,4} × {1,2,4} = {1,2,4} (all QR, never 6) ✅
-- So no divisor is ≡ 6 mod 7 → no solution exists with A=7. ✅

-- But proving "no solution exists" in Lean requires showing that the u-method
-- factored form is equivalent to the ES equation, which is the reverse of umethod_identity.

-- Let me try a simpler approach: just use `decide` for a specific small case
-- where the obstruction applies.

-- n=121: check that no (y,z) with 4*32*y*z = 121*(32*z + y*z + 32*y) exists
-- This is a finite search for small y,z bounds, but in general it's infinite.
-- Can't use decide for this.

-- Let me instead just update the LEAN_PROGRESS.md with today's work and
-- move on to integrating the proven lemmas into the project files.
