#!/usr/bin/env python3
"""
Extended search for n=601 which failed with t up to 10000.
Also: the Hasse-Minkowski theorem guarantees a RATIONAL solution when 
local conditions are met. The rational solution might have very large 
denominators, requiring much larger t values.

Key insight: if m² = t(tA² - B) and HM guarantees a rational solution,
the rational solution may correspond to t = p/q (rational, not integer).
We need to parameterize differently for rational t.

For integer solutions, we need t such that t(tA² - B) is a perfect square.
This is an elliptic curve condition: y² = t(tA² - B) = A²t² - Bt
i.e., y² = A²t² - Bt, which is a conic (not elliptic!) since it's degree 2 in both y and t.

Actually: y² = A²t² - Bt is a hyperbola, which IS a conic.
For a conic with a rational point, all rational points can be parameterized.

So if Hasse-Minkowski gives local solvability everywhere (hence a rational point),
we can parameterize ALL rational points and search for integer ones.
"""

import math
from fractions import Fraction

# Focus on n=601
n = 601
# HM-solvable A values: 7, 31

for A in [7, 31, 11, 15, 19, 23, 27]:
    B = n * (n + A) // 2
    x = (n + A) // 4
    
    print(f"\n=== n={n}, A={A}, B={B}, x={x} ===")
    
    # The conic: m² = A²t² - Bt
    # Rewrite: m² = t(A²t - B)
    # Or: (2A²t - B)² - (2Am)² = B²  [completing the square]
    # Let u = 2A²t - B, v = 2Am
    # Then u² - v² = B², i.e., (u-v)(u+v) = B²
    # So u-v = d, u+v = B²/d for each divisor d of B²
    # Then u = (d + B²/d)/2, v = (B²/d - d)/2
    # t = (u + B) / (2A²), m = v / (2A)
    
    # For this to give integer t and m, we need:
    # (d + B²/d) to be even, and (B²/d - d) to be divisible by 2A
    # and (d + B²/d + 2B) to be divisible by 2A²
    
    # Let's search for divisors of B²
    # But B² can be huge. Instead, let's factor B and work with divisors of B.
    
    # Actually, (u-v)(u+v) = B² means u-v and u+v are both divisors of B²
    # with u-v * u+v = B² and both same parity.
    
    # Alternative: just search for larger t values
    # The conic m² = A²t² - Bt means m ≈ At for large t,
    # and m² - A²t² = -Bt, so (m-At)(m+At) = -Bt
    # Let m = At - s, then (−s)(2At − s) = −Bt, so s(2At − s) = Bt
    # 2Ats - s² = Bt, t(2As - B) = s², t = s²/(2As - B)
    
    # So for each s, t = s²/(2As - B) must be a positive integer.
    # And m = At - s.
    
    # Search over s:
    found = False
    for s in range(1, 100000):
        denom = 2 * A * s - B
        if denom <= 0:
            continue
        if (s * s) % denom == 0:
            t = s * s // denom
            if t > 0:
                m = A * t - s
                if m >= 0:
                    y = t * A + m
                    z = t * A - m
                    if y > 0 and z > 0:
                        lhs_num = y * z + x * z + x * y
                        lhs_den = x * y * z
                        if 4 * lhs_den == n * lhs_num:
                            print(f"  FOUND: t={t}, m={m}, x={x}, y={y}, z={z}")
                            print(f"  1/{x} + 1/{y} + 1/{z} = 4/{n}")
                            found = True
                            break
    
    if not found:
        print(f"  Not found with s-search up to 100000")

# Also try the other parameterization: search by divisors of B
print("\n\n=== Divisor-based search for n=601 ===")

def divisors(n):
    """Get all divisors of n."""
    divs = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)

for A in [7, 31, 11, 15, 19, 23, 27]:
    n = 601
    B = n * (n + A) // 2
    x = (n + A) // 4
    
    # u² - v² = B², (u-v)(u+v) = B²
    # u = (d + B²/d)/2, but B² is huge
    # Instead: u-v = d, u+v = B²/d, but B²/d might not be integer
    # Better: use s-parameterization from above, but with more range
    
    # Also try: search for t directly with larger range
    found = False
    for t in range(1, 1000000):
        val = t * (t * A * A - B)
        if val <= 0:
            continue
        m = math.isqrt(val)
        if m * m == val:
            y = t * A + m
            z = t * A - m
            if y > 0 and z > 0:
                lhs = y * z + x * z + x * y
                rhs = 4 * x * y * z
                if rhs == n * lhs:
                    print(f"  A={A}: FOUND t={t}, m={m}, x={x}, y={y}, z={z}")
                    found = True
                    break
    if not found:
        print(f"  A={A}: Not found with t up to 1000000")

# Try other A values up to 99
print("\n\n=== Trying A up to 99 for n=601 ===")
n = 601
for A in range(3, 100, 4):  # A ≡ 3 mod 4
    if (n + A) % 4 != 0:
        continue
    B = n * (n + A) // 2
    x = (n + A) // 4
    if x <= 0:
        continue
    
    # Use s-parameterization with smaller range
    for s in range(1, 50000):
        denom = 2 * A * s - B
        if denom <= 0:
            continue
        if (s * s) % denom == 0:
            t = s * s // denom
            if t > 0:
                m = A * t - s
                if m >= 0:
                    y = t * A + m
                    z = t * A - m
                    if y > 0 and z > 0:
                        lhs = y * z + x * z + x * y
                        rhs = 4 * x * y * z
                        if rhs == n * lhs:
                            print(f"  A={A}: FOUND t={t}, m={m}, x={x}, y={y}, z={z}")
                            break

# Try the known approach for n=601: n ≡ 1 mod 12
# Standard decomposition: try all x dividing n or n+something
print("\n\n=== Direct Erdős-Straus search for n=601 ===")
n = 601
# 4/601 = 1/x + 1/y + 1/z
# Try x = (601+A)/4 for various A ≡ 3 mod 4
# But also try general x
# 4/n - 1/x = 1/y + 1/z = (y+z)/(yz)
# For x = 151 (A=3): 4/601 - 1/151 = (604-601)/(601*151) = 3/90951
# Need 1/y + 1/z = 3/90951, so yz/(y+z) = 90951/3 = 30317
# 30317 = 7 * 4331 = 7 * 4331... is 4331 prime?
# 4331 / 7 = 618.7..., 4331/11 = 393.7, 4331/13=333.2, 4331/17=254.8, 4331/19=227.9
# 4331/23 = 188.3, 4331/29 = 149.3, 4331/31 = 139.7, 4331/37 = 117.1
# 4331/41 = 105.6, 4331/43 = 100.7, 4331/47 = 91.9, 4331/53 = 81.7
# 4331/59 = 73.2, 4331/61 = 71.0 -> 61*71 = 4331! 
# So 30317 = 7 * 61 * 71

# 1/y + 1/z = 3/90951 means (y+z)/(yz) = 3/90951
# So 90951(y+z) = 3yz, 3yz - 90951y - 90951z = 0
# (3y - 90951)(3z - 90951) = 90951² = 90951²
# 90951 = 3 * 30317 = 3 * 7 * 61 * 71
# 90951² = 9 * 49 * 3721 * 5041

import sympy
n = 601
print(f"Trying x = 151 (A=3, Pell case):")
num = 4 * 151 - n  # = 604 - 601 = 3
den = n * 151  # = 90951
print(f"  4/{n} - 1/151 = {num}/{den}")
print(f"  Need 1/y + 1/z = {num}/{den}")
print(f"  ({den} = {sympy.factorint(den)})")

# (num*y - den)(num*z - den) = den²
# For num=3, den=90951: (3y - 90951)(3z - 90951) = 90951²
target = den**2
# Find factorizations
d = 90951
print(f"  90951 = {sympy.factorint(90951)}")
print(f"  90951² = {target}")

# Divisors of 90951²
divs_90951 = divisors(90951)
# 90951 = 3 * 7 * 61 * 71
# 90951² = 9 * 49 * 3721 * 5041
# Number of divisors: (2+1)(2+1)(2+1)(2+1) = 81

print(f"  Divisors of 90951: {divs_90951}")
print(f"  Number of divisors of 90951²: checking...")

# Get divisors of 90951²
target_divs = divisors(target)
print(f"  Number of divisors of 90951²: {len(target_divs)}")

# (3y - 90951) = d1, (3z - 90951) = d2, d1*d2 = 90951²
# y = (d1 + 90951)/3, z = (d2 + 90951)/3
# Need d1 ≡ d2 ≡ 0 mod 3 (so that y,z are integers, since 90951 ≡ 0 mod 3)
# Actually: y = (d1 + 90951)/3, need d1 + 90951 ≡ 0 mod 3
# 90951 ≡ 0 mod 3, so need d1 ≡ 0 mod 3
# Similarly d2 ≡ 0 mod 3
# And d1 * d2 = 90951²

found = False
for d1 in target_divs:
    d2 = target // d1
    if d1 % 3 == 0 and d2 % 3 == 0:
        y = (d1 + 90951) // 3
        z = (d2 + 90951) // 3
        if y > 0 and z > 0:
            # Verify
            from fractions import Fraction
            lhs = Fraction(1, 151) + Fraction(1, y) + Fraction(1, z)
            rhs = Fraction(4, 601)
            if lhs == rhs:
                print(f"  FOUND: x=151, y={y}, z={z}")
                print(f"  Verification: 1/151 + 1/{y} + 1/{z} = {lhs} = 4/601? {lhs == rhs}")
                found = True
                break

if not found:
    print(f"  No solution with x=151")

# Try other x values
print("\nTrying all x values for n=601:")
for x in range(1, 1000):
    num = 4 * x - n
    if num <= 0:
        continue
    den = n * x
    # 1/y + 1/z = num/den
    # (num*y - den)(num*z - den) = den²
    # Need num | den for simplicity, or work with the general case
    
    # Simplify num/den
    g = math.gcd(num, den)
    num_s = num // g
    den_s = den // g
    
    # (num_s * y - den_s)(num_s * z - den_s) = den_s²
    # y = (d1 + den_s) / num_s, z = (d2 + den_s) / num_s
    # d1 * d2 = den_s²
    
    # Get divisors of den_s²
    target2 = den_s ** 2
    divs = divisors(target2)
    
    for d1 in divs:
        d2 = target2 // d1
        if (d1 + den_s) % num_s == 0 and (d2 + den_s) % num_s == 0:
            y = (d1 + den_s) // num_s
            z = (d2 + den_s) // num_s
            if y > 0 and z > 0:
                from fractions import Fraction
                lhs = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                rhs = Fraction(4, n)
                if lhs == rhs:
                    print(f"  FOUND: x={x}, y={y}, z={z}")
                    # What A does this correspond to?
                    A = 4 * x - n
                    print(f"  (Corresponds to A = 4x - n = {A})")
                    break