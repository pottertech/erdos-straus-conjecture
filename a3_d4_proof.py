#!/usr/bin/env python3
"""
Verify why d=4 works for ALL v₂(B) ≥ 2 cases.
Prove: if 4 | B and 3 ∤ B, then d=4 satisfies d + 2B + B²/d ≡ 0 (mod 36).

d = 4, B = 4m (since 4|B), B² = 16m², B²/d = 4m²
d + 2B + B²/d = 4 + 8m + 4m² = 4(1 + 2m + m²) = 4(1+m)²

Need 36 | 4(1+m)², i.e., 9 | (1+m)² (since 36/gcd(36,4) = 9).
9 | (1+m)² iff 3 | (1+m) iff m ≡ 2 (mod 3).

B = 4m, B mod 36 ∈ {8, 20, 32} (the 100% success residues).
B = 4m → m = B/4.
B ≡ 8 (mod 36) → m ≡ 2 (mod 9) → m ≡ 2 (mod 3) ✓
B ≡ 20 (mod 36) → m ≡ 5 (mod 9) → m ≡ 2 (mod 3) ✓  
B ≡ 32 (mod 36) → m ≡ 8 (mod 9) → m ≡ 2 (mod 3) ✓

So m ≡ 2 (mod 3) ALWAYS when B ≡ 0 (mod 4) and B ≡ 1 (mod 3) (which it is since 3∤B and B ≡ 1 mod 3).

Wait, is B ≡ 1 (mod 3)? B = n(n+3)/2, n ≡ 1 (mod 3), n+3 ≡ 1 (mod 3), so n(n+3) ≡ 1 (mod 3).
B = n(n+3)/2. Since 2 ≡ 2 (mod 3), and we need to compute B mod 3.
n(n+3) ≡ 1 (mod 3). B = n(n+3)/2. Since 2⁻¹ ≡ 2 (mod 3), B ≡ 1·2 ≡ 2 (mod 3).
So B ≡ 2 (mod 3). 

B = 4m, 4 ≡ 1 (mod 3), so m ≡ B ≡ 2 (mod 3). So m ≡ 2 (mod 3) ALWAYS!
Therefore 3 | (1+m) always, so 9 | (1+m)² always, so 36 | 4(1+m)² always.

QED: d=4 works for ALL v₂(B) ≥ 2 cases in our residue class.
"""

# Verify
count = 0
for n in range(13, 100001):
    if n % 12 != 1 or n % 5 == 0:
        continue
    B = n * (n + 3) // 2
    if B % 4 != 0:
        continue
    m = B // 4
    assert m % 3 == 2, f"m mod 3 != 2 for n={n}, m={m}"
    # d = 4: check 4(1+m)^2 mod 36 == 0
    assert (4 * (1 + m) ** 2) % 36 == 0, f"d=4 fails for n={n}"
    count += 1

print(f"Verified d=4 works for all {count} cases with v₂(B) ≥ 2")
print(f"B ≡ 2 (mod 3) always, so m = B/4 ≡ 2 (mod 3) always, so 9|(1+m)² always, so 36|4(1+m)² always.")
print()
print("PROOF COMPLETE: d=4 works for ALL v₂(B) ≥ 2 cases because:")
print("  B = n(n+3)/2, n ≡ 1 (mod 3) → n(n+3) ≡ 1 (mod 3)")
print("  B = n(n+3)/2 ≡ 1·2⁻¹ ≡ 1·2 ≡ 2 (mod 3)")
print("  B = 4m → m = B/4 ≡ B·1 ≡ 2 (mod 3) (since 4 ≡ 1 mod 3)")
print("  1+m ≡ 0 (mod 3) → 9|(1+m)² → 36|4(1+m)² → mod 36 satisfied ✓")