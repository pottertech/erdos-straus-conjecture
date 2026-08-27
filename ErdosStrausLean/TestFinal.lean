import Mathlib
import ErdosStrausLean.Basic
import ErdosStrausLean.StructuralLemmas

open Nat legendreSym

instance : Fact (7 : ℕ).Prime := ⟨by norm_num⟩
instance : Fact (11 : ℕ).Prime := ⟨by norm_num⟩

-- n=109: u=3, x=28, y=1018, z=1553468 (correct from Python)
theorem erdos_straus_109 : ∃ x y z : ℕ, erdos_straus 109 x y z := by
  use 28, 1018, 1553468
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 28 * 1018 * 1553468 = 109 * (28 * 1553468 + 1018 * 1553468 + 28 * 1018)
          ring

-- n=193: u=7, x=50, y=1380, z=1331700 (correct from Python)
theorem erdos_straus_193 : ∃ x y z : ℕ, erdos_straus 193 x y z := by
  use 50, 1380, 1331700
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 50 * 1380 * 1331700 = 193 * (50 * 1331700 + 1380 * 1331700 + 50 * 1380)
          ring

-- n=241: u=7, x=62, y=2139, z=1030998 (corrected from Python)
theorem erdos_straus_241 : ∃ x y z : ℕ, erdos_straus 241 x y z := by
  use 62, 2139, 1030998
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 62 * 2139 * 1030998 = 241 * (62 * 1030998 + 2139 * 1030998 + 62 * 2139)
          ring

-- n=337: u=3, x=85, y=9550, z=54711950 (corrected from Python)
theorem erdos_straus_337 : ∃ x y z : ℕ, erdos_straus 337 x y z := by
  use 85, 9550, 54711950
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 85 * 9550 * 54711950 = 337 * (85 * 54711950 + 9550 * 54711950 + 85 * 9550)
          ring

-- n=1009: u=3, x=253, y=85096, z=1974822872 (the ChatGPT example!)
theorem erdos_straus_1009 : ∃ x y z : ℕ, erdos_straus 1009 x y z := by
  use 253, 85096, 1974822872
  constructor
  · omega
  · constructor
    · omega
    · constructor
      · omega
      · constructor
        · omega
        · show 4 * 253 * 85096 * 1974822872 = 1009 * (253 * 1974822872 + 85096 * 1974822872 + 253 * 85096)
          ring
