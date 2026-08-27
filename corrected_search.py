#!/usr/bin/env python3
"""
Fix: The integer solutions found satisfy k² + 36(A²-9)t² - 36m² = B²
but the mapping to (x,y,z) must be verified against 4/n = 1/x + 1/y + 1/z.

The decomposition is:
  4/n = 1/x + 1/y + 1/z
where:
  x = (n+A)/4
  y = tA + m
  z = tA - m
  k = 18t - B
  B = n(n+A)/2

Let's verify the algebra: does k² + 36(A²-9)t² - 36m² = B² 
actually imply 4/n = 1/x + 1/y + 1/z?

The derivation should be:
  1/y + 1/z = (y+z)/(yz) = (2tA)/(t²A² - m²)
  1/x + 1/y + 1/z = (n+A)/4... wait, x = (n+A)/4, so 1/x = 4/(n+A)
  1/y + 1/z = 2tA / (t²A² - m²)
  
  4/n = 4/(n+A) + 2tA/(t²A² - m²)
  
  4/n - 4/(n+A) = 2tA/(t²A² - m²)
  4A / (n(n+A)) = 2tA / (t²A² - m²)
  2 / (n(n+A)) = t / (t²A² - m²)
  2(t²A² - m²) = tn(n+A)
  2t²A² - 2m² = tn(n+A) = 2tB  (since B = n(n+A)/2, so tn(n+A) = 2tB)
  2t²A² - 2m² = 2tB
  t²A² - m² = tB
  m² = t²A² - tB = t(tA² - B) = t(tA² - n(n+A)/2)

So the condition is: m² = t(tA² - B)

And the quadratic form condition is:
  k² + 36(A²-9)t² - 36m² = B²
  (18t - B)² + 36(A²-9)t² - 36m² = B²
  324t² - 36tB + B² + 36(A²-9)t² - 36m² = B²
  324t² - 36tB + 36(A²-9)t² - 36m² = 0
  324t² + 36(A²-9)t² - 36tB - 36m² = 0
  36t²(9 + A² - 9) - 36tB - 36m² = 0
  36t²A² - 36tB - 36m² = 0
  t²A² - tB - m² = 0
  m² = t²A² - tB = t(tA² - B)

So the quadratic form condition IS equivalent to m² = t(tA² - B),
which IS the Erdős-Straus condition!

The issue is in the search: it finds (k,t,m) satisfying the quadratic form
but may use wrong parity conditions or wrong B. Let me write a clean search
that verifies the ACTUAL Erdős-Straus equation.
"""

import json
from fractions import Fraction

A3_FAIL_N = [49, 73, 169, 193, 241, 313, 361, 409, 433, 601, 673]
A_VALUES = [7, 11, 15, 19, 23, 27, 31]

def compute_B(n, A):
    return n * (n + A) // 2

def find_es_solution(n, A, max_t=5000):
    """
    Find a solution to 4/n = 1/x + 1/y + 1/z where x = (n+A)/4, 
    y = tA + m, z = tA - m.
    
    The condition is: m² = t(tA² - B) where B = n(n+A)/2
    
    So we need t(tA² - B) to be a perfect square.
    """
    B = compute_B(n, A)
    x = (n + A) // 4
    
    # Check x is a positive integer
    if (n + A) % 4 != 0:
        return {'found': False, 'reason': 'x = (n+A)/4 not integer'}
    
    if x <= 0:
        return {'found': False, 'reason': 'x <= 0'}
    
    for t in range(1, max_t):
        val = t * (t * A * A - B)
        if val <= 0:
            continue
        
        # Check if val is a perfect square
        import math
        m = math.isqrt(val)
        if m * m == val:
            y = t * A + m
            z = t * A - m
            if y > 0 and z > 0:
                # Verify!
                lhs = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                rhs = Fraction(4, n)
                if lhs == rhs:
                    k = 18 * t - B
                    return {
                        'found': True,
                        'x': x, 'y': y, 'z': z,
                        't': t, 'm': m, 'k': k,
                        'verified': True,
                        'lhs': str(lhs),
                        'rhs': str(rhs)
                    }
                else:
                    return {
                        'found': False,
                        'reason': f'quadratic form satisfied but ES fails: 1/{x}+1/{y}+1/{z}={lhs}≠{rhs}'
                    }
    
    return {'found': False, 'reason': f'no t found up to {max_t}'}

print("=" * 80)
print("CORRECTED ERDŐS-STRAUS SOLUTION SEARCH")
print("=" * 80)
print()
print("Condition: m² = t(tA² - B) where B = n(n+A)/2")
print("Then x = (n+A)/4, y = tA + m, z = tA - m")
print()

all_results = {}
all_verified = True

for n in A3_FAIL_N:
    all_results[str(n)] = {}
    print(f"--- n = {n} ---")
    
    for A in A_VALUES:
        result = find_es_solution(n, A, max_t=10000)
        all_results[str(n)][str(A)] = result
        
        if result['found']:
            print(f"  A={A:2d}: ✓ x={result['x']}, y={result['y']}, z={result['z']} "
                  f"(t={result['t']}, m={result['m']}) — VERIFIED")
        else:
            print(f"  A={A:2d}: ✗ {result['reason']}")
            if 'quadratic form satisfied' in result.get('reason', ''):
                all_verified = False
    
    print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)

# Count solutions
solution_count = 0
total = 0
n_with_solution = []
n_without = []

for n in A3_FAIL_N:
    has_any = False
    for A in A_VALUES:
        total += 1
        if all_results[str(n)][str(A)]['found']:
            solution_count += 1
            has_any = True
    if has_any:
        n_with_solution.append(n)
    else:
        n_without.append(n)

print(f"Total (n,A) pairs: {total}")
print(f"Solutions found: {solution_count}")
print(f"n values with at least one A solution: {n_with_solution}")
print(f"n values with NO A solution: {n_without}")
print()

# Which A values work for which n?
print("Working A values per n:")
for n in A3_FAIL_N:
    working = [A for A in A_VALUES if all_results[str(n)][str(A)]['found']]
    hm_A = []
    # Reload from the original data
    for A in A_VALUES:
        with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/ternary_analysis.json') as f:
            orig_data = json.load(f)
        if orig_data['local_solvability'][str(n)][str(A)]['hasse_minkowski_global']:
            hm_A.append(A)
    print(f"  n={n:4d}: Working A={working}, HM-solvable A={hm_A}")

print()

# Pattern in A=15 (which always fails at p=3)
print("A=15 always fails at p=3. Let's see why:")
for n in A3_FAIL_N:
    B = compute_B(n, 15)
    # The condition m² = t(225t - B)
    # For p=3: need t(225t - B) to be a square in Q_3
    # 225 = 9*25, so 225t ≡ 0 mod 9
    # t(225t - B) ≡ t(-B) ≡ -tB mod 3
    # For this to be a square mod 3: -tB must be QR mod 3 (i.e., 0 or 1 mod 3)
    # QR mod 3: {0, 1}
    # -tB mod 3: need (-t*B) mod 3 ∈ {0, 1}
    # Since B = n(n+15)/2, and n ≡ 1 mod 3:
    # B = n(n+15)/2, n+15 ≡ n mod 3 ≡ 1 mod 3
    # So B ≡ 1*1/2 ≡ 1*2 ≡ 2 mod 3 (since 1/2 ≡ 2 mod 3)
    # Wait: 1/2 mod 3 = 2 (since 2*2=4≡1 mod 3)
    # So B ≡ 1 * 1 * 2 = 2 mod 3
    # -tB ≡ -t * 2 ≡ -2t ≡ t mod 3 (since -2 ≡ 1 mod 3)
    # So we need t mod 3 ∈ {0, 1}
    # t=0 mod 3: trivially square (0)
    # t=1 mod 3: t ≡ 1, so t(225t-B) ≡ 1*(0-2) ≡ -2 ≡ 1 mod 3 ✓
    # t=2 mod 3: t(225t-B) ≡ 2*(0-2) ≡ -4 ≡ 2 mod 3 ✗ (2 is not QR mod 3)
    
    # But wait, we also need t mod 3 ≠ 0 for nontriviality in some cases
    # Actually the local obstruction is more subtle. Let me check:
    B_mod3 = B % 3
    print(f"  n={n}: B={B}, B mod 3 = {B_mod3}, "
          f"t(225t-B) mod 3 for t=0,1,2: {(0)%3}, {(1*(225-B))%3}, {(2*(450-B))%3}")

print()
print("A=15: For all n ≡ 1 mod 3, B ≡ 2 mod 3, and t=2 mod 3 gives non-square.")
print("But t=0 mod 3 gives trivial, t=1 mod 3 gives square. So p=3 shouldn't fail?")
print("The issue must be at the Hensel lifting level (mod 9, mod 27).")
print()

# Check mod 9 for A=15
for n in A3_FAIL_N[:3]:
    B = compute_B(n, 15)
    print(f"  n={n}: B={B}, B mod 9 = {B%9}")
    for t_mod9 in range(9):
        val = (t_mod9 * (225 * t_mod9 - B)) % 9
        # Is val a square mod 9?
        squares_mod9 = {0, 1, 4, 7}
        is_sq = val in squares_mod9
        print(f"    t≡{t_mod9} mod 9: t(225t-B) ≡ {val} mod 9, square: {is_sq}")

# Save corrected results
output = {
    'description': 'Corrected Erdős-Straus solution search with proper verification',
    'method': 'Direct search for m² = t(tA² - B) with 4/n = 1/x + 1/y + 1/z verification',
    'results': all_results,
    'summary': {
        'total_pairs': total,
        'solutions_found': solution_count,
        'n_with_solution': n_with_solution,
        'n_without_solution': n_without,
        'all_verified': all_verified,
    }
}

with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/corrected_analysis.json', 'w') as f:
    json.dump(output, f, indent=2)

print()
print("Corrected results saved to corrected_analysis.json")