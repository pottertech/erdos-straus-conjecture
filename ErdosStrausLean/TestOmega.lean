import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas

open Nat

-- n=2: 4/2 = 1/1 + 1/2 + 1/2
theorem erdos_straus_2 : ∃ x y z : ℕ, erdos_straus 2 x y z := by
  use 1, 2, 2
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 1 * 2 * 2 = 2 * (1 * 2 + 2 * 2 + 1 * 2)
          ring

-- n=3: 4/3 = 1/1 + 1/4 + 1/12
theorem erdos_straus_3 : ∃ x y z : ℕ, erdos_straus 3 x y z := by
  use 1, 4, 12
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 1 * 4 * 12 = 3 * (1 * 12 + 4 * 12 + 1 * 4)
          ring

-- n=5: 4/5 = 1/2 + 1/4 + 1/20
theorem erdos_straus_5 : ∃ x y z : ℕ, erdos_straus 5 x y z := by
  use 2, 4, 20
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 2 * 4 * 20 = 5 * (2 * 20 + 4 * 20 + 2 * 4)
          ring

-- n=7: 4/7 = 1/2 + 1/15 + 1/210
theorem erdos_straus_7 : ∃ x y z : ℕ, erdos_straus 7 x y z := by
  use 2, 15, 210
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 2 * 15 * 210 = 7 * (2 * 210 + 15 * 210 + 2 * 15)
          ring

-- n=13 (first hard case prime, 13 ≡ 1 mod 12): 4/13 = 1/4 + 1/18 + 1/468
theorem erdos_straus_13 : ∃ x y z : ℕ, erdos_straus 13 x y z := by
  use 4, 18, 468
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 4 * 18 * 468 = 13 * (4 * 468 + 18 * 468 + 4 * 18)
          ring

-- n=17: 4/17 = 1/5 + 1/85 + 1/85
-- Check: 4*5*85*85 = 144500, 17*(5*85+85*85+5*85) = 17*(425+7225+425) = 17*8075 = 137275... no
-- 4/17: x=5 → 4*5/17 = 20/17, need 20yz = 17(5z+yz+5y) → 20yz = 85z+17yz+85y → 3yz = 85z+85y → 3yz-85z-85y = 0
-- (3y-85)(3z-85) = 85² = 7225. 3y-85=1 → y=86/3 not integer. 3y-85=5 → y=90/3=30. 3z-85=1445 → z=1530/3=510
-- Check: 4*5*30*510 = 306000, 17*(5*510+30*510+5*30) = 17*(2550+15300+150) = 17*18000 = 306000 ✅
theorem erdos_straus_17 : ∃ x y z : ℕ, erdos_straus 17 x y z := by
  use 5, 30, 510
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 5 * 30 * 510 = 17 * (5 * 510 + 30 * 510 + 5 * 30)
          ring

-- n=97 (hard case prime, 97 ≡ 1 mod 12, 97 ≡ 1 mod 24):
-- Using u-method with u=3: x=(97+3)/4=25, D=97²*25²=9409*625=5880625
-- This is a harder case. Let me use the parametric solution for n ≡ 1 mod 12 with 5|n.
-- Actually 97 is not divisible by 5, so it's a true hard case.
-- For n=97, A=3: x=25, need (3y-97*25)(3z-97*25) = 97²*25²
-- 97*25 = 2425, 3y-2425 divides 2425² = 5880625
-- Let me just compute: 4/97 = 1/25 + 1/... 
-- 4/97 - 1/25 = (100-97)/(97*25) = 3/2425
-- 1/y + 1/z = 3/2425 → (3y-2425)(3z-2425) = 2425²
-- 2425 = 5² * 97, 2425² = 5⁴ * 97² = 625 * 9409 = 5880625
-- d₁ = 1: y = (2425+1)/3 = 2426/3 not int
-- d₁ = 5: y = 2430/3 = 810, z = (5880625/5 + 2425)/3 = (1176125+2425)/3 = 1178550/3 = 392850
-- Check: 4*25*810*392850 = 4*25*810*392850 = 31831050000
-- 97*(25*392850 + 810*392850 + 25*810) = 97*(9821250 + 318208500 + 20250) = 97*318050000 = 30850850000... hmm let me just use ring
-- Actually: 4*25*810*392850 = 100*810*392850 = 81000*392850 = 31820850000
-- 97*(25*392850+810*392850+25*810) = 97*(9821250+318208500+20250) = 97*318050000 = 30850850000
-- 31820850000 ≠ 30850850000. Off by 970000000. Let me recheck.
-- 1/25 + 1/810 + 1/392850 should equal 4/97
-- 1/25 = 392850/9821250... this is getting complex. Let me just try with ring.
theorem erdos_straus_97 : ∃ x y z : ℕ, erdos_straus 97 x y z := by
  use 25, 810, 392850
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 25 * 810 * 392850 = 97 * (25 * 392850 + 810 * 392850 + 25 * 810)
          ring
