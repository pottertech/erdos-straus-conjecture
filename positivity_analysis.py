#!/usr/bin/env python3
"""
Positivity Analysis for A ≠ 3 in the Erdős-Straus Conjecture

For A = 3, we proved z = (d + B)/6 is always positive (automatic positivity).
For A ≠ 3, the equation is a ternary quadratic form:
  k² + 36t²(A² - 9) = B² + 36m²
where B = n(n+A)/2, k = 18t - B, x = (n+A)/4, y = tA + m, z = tA - m.

This script:
1. Finds all 1,133 cases where A=3 fails (up to n=10000)
2. For each, finds the minimum A that works using fast search
3. Computes z = tA - m and analyzes its structure
4. Looks for a manifestly positive expression for z analogous to (d+B)/6
5. Saves results to positivity_analysis.json
"""

import json
import math
import os
from fractions import Fraction
from collections import Counter, defaultdict

# ============================================================
# Helper functions
# ============================================================

def factorize(n):
    """Return prime factorization as dict."""
    factors = {}
    temp = abs(n)
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def compute_B(n, A):
    """B = n(n+A)/2"""
    return n * (n + A) // 2

def check_a3_works(n):
    """
    Check if A=3 works for this n.
    A=3 works iff v₂(B) ≥ 2 OR (v₂(B) = 1 AND B/2 has a prime factor ≡ 2 mod 3)
    """
    B = compute_B(n, 3)
    
    # v₂(B)
    v2 = 0
    temp = B
    while temp % 2 == 0:
        v2 += 1
        temp //= 2
    
    if v2 >= 2:
        return True, "v₂(B) ≥ 2"
    
    # v₂(B) = 1, check if B/2 has a prime factor ≡ 2 (mod 3)
    O = B // 2
    factors = factorize(O)
    has_2mod3 = any(p % 3 == 2 for p in factors.keys())
    
    if has_2mod3:
        return True, "v₂(B)=1, has prime ≡ 2 (mod 3)"
    else:
        return False, "v₂(B)=1, all primes ≡ 1 (mod 3)"

def find_es_solution_fast(n, A, max_t=50000):
    """
    Find a solution to 4/n = 1/x + 1/y + 1/z using the fast search.
    
    The condition is: m² = t(tA² - B) where B = n(n+A)/2
    We search for t such that t(tA² - B) is a perfect square.
    
    Returns: dict with solution info or {'found': False}
    """
    if (n + A) % 4 != 0:
        return {'found': False, 'reason': '(n+A) not divisible by 4'}
    
    B = compute_B(n, A)
    x = (n + A) // 4
    
    if x <= 0:
        return {'found': False, 'reason': 'x <= 0'}
    
    A2 = A * A
    
    for t in range(1, max_t):
        val = t * (t * A2 - B)
        if val <= 0:
            continue
        
        m = math.isqrt(val)
        if m * m == val:
            y = t * A + m
            z = t * A - m
            if y > 0 and z > 0:
                # Verify with exact arithmetic
                lhs = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                rhs = Fraction(4, n)
                if lhs == rhs:
                    k = 18 * t - B
                    # Compute the "effective" d and q
                    # For A ≠ 3, the factoring (k-6m)(k+6m) doesn't give B²
                    # Instead: (k-6m)(k+6m) = k² - 36m² = B² - 36t²(A²-9)
                    effective_N = B*B - 36*t*t*(A*A - 9)
                    
                    return {
                        'found': True,
                        'x': x, 'y': y, 'z': z,
                        't': t, 'm': m, 'k': k,
                        'B': B, 'A': A,
                        'effective_N': effective_N,
                        'verified': True
                    }
    
    return {'found': False, 'reason': f'no solution found up to t={max_t}'}

def find_min_A_solution(n, max_A=200, max_t=50000):
    """Find the minimum A ≡ 3 (mod 4) that gives a valid ES solution."""
    A = 3
    while A <= max_A:
        result = find_es_solution_fast(n, A, max_t)
        if result['found']:
            return result
        A += 4
    return {'found': False, 'reason': f'no A found up to {max_A}'}

def analyze_z_structure(sol):
    """
    Analyze the structure of z = tA - m in terms of fundamental parameters.
    
    For A=3: z = (d+B)/6 where d is a divisor of B²
    For A≠3: we need to find an analogous expression.
    
    Key relationships:
    - k = 18t - B
    - m² = t(tA² - B) = t²A² - tB
    - z = tA - m
    - y = tA + m
    - y*z = t²A² - m² = t²A² - (t²A² - tB) = tB
    - So yz = tB (this is always true!)
    
    For A=3:
    - z = 3t - m, and k² - 36m² = B²
    - (k-6m)(k+6m) = B², let d = k-6m, q = k+6m
    - z = 3t - m = (18t - 6m)/6 = (k + B - 6m)/6
    - But k = (d+q)/2 and 6m = (q-d)/2
    - So z = ((d+q)/2 + B - (q-d)/2)/6 = (d + B)/6
    
    For A≠3:
    - z = tA - m
    - We need to express z in terms of k, B, t, A
    - k = 18t - B, so t = (k + B)/18
    - z = A(k + B)/18 - m = (A(k+B) - 18m)/18
    - This doesn't simplify as nicely.
    
    Alternative: use the "effective factoring"
    - (k-6m)(k+6m) = B² - 36t²(A²-9) = effective_N
    - Let p = k-6m, q = k+6m, so pq = effective_N
    - z = tA - m = A(k+B)/18 - (q-p)/12
    
    Let's try: z = tA - m, and m = (q-p)/12, t = (k+B)/18 = ((p+q)/2 + B)/18 = (p+q+2B)/36
    z = A(p+q+2B)/36 - (q-p)/12
    z = (A(p+q+2B) - 3(q-p))/36
    z = (Ap + Aq + 2AB - 3q + 3p)/36
    z = ((A+3)p + (A-3)q + 2AB)/36
    
    For A=3: z = (6p + 0·q + 6B)/36 = (6(p+B))/36 = (p+B)/6 = (d+B)/6 ✓
    
    For A≠3: z = ((A+3)p + (A-3)q + 2AB)/36
    
    Where p = k-6m, q = k+6m, and pq = B² - 36t²(A²-9)
    """
    A = sol['A']
    B = sol['B']
    t = sol['t']
    m = sol['m']
    k = sol['k']
    z = sol['z']
    x = sol['x']
    
    # Compute p, q
    p = k - 6*m
    q = k + 6*m
    
    # Effective N
    eff_N = p * q  # = B² - 36t²(A²-9)
    
    # z from the formula
    z_formula = ((A+3)*p + (A-3)*q + 2*A*B) // 36
    assert z_formula == z, f"Formula mismatch: {z_formula} != {z} for n={sol.get('n','?')}, A={A}"
    
    # For A=3: z = (p + B)/6 = (d + B)/6
    if A == 3:
        z_a3 = (p + B) // 6
        assert z_a3 == z
        return {
            'z': z,
            'p': p, 'q': q,
            'eff_N': eff_N,
            'z_formula': f'z = (d + B)/6 = ({p} + {B})/6 = {z}',
            'z_expression': '(d + B) / 6',
            'manifestly_positive': True,
            'reason': 'd > 0 and B > 0, so z > 0'
        }
    
    # For A ≠ 3: z = ((A+3)p + (A-3)q + 2AB) / 36
    # Let's break this down further
    
    # Note: p = k - 6m, q = k + 6m
    # Since z > 0 and y > 0, we have tA > m, so p = k - 6m = 18t - B - 6m
    # = 18(tA) - 18(tA-t) - B - 6m... hmm, let me think differently
    
    # Alternative expression: z = tA - m
    # y*z = tB (always true)
    # So z = tB / y = tB / (tA + m)
    
    # Also: z = (y*z) / y = tB / y
    # And: z = tA - m, y = tA + m
    # y - z = 2m, y + z = 2tA
    # yz = t²A² - m² = t²A² - t(tA² - B) = t²A² - t²A² + tB = tB
    
    # So z = tB / (tA + m)
    # This is manifestly positive when t > 0, B > 0, and tA + m > 0 (which is y > 0)!
    
    # But can we express z WITHOUT referencing m?
    # z = tB / y, but y = tA + m, which depends on m.
    
    # Let's try: z = (A(k+B) - 18m) / 18
    # = (Ak + AB - 18m) / 18
    # = (A(18t-B) + AB - 18m) / 18  [using k = 18t - B]
    # = (18At - AB + AB - 18m) / 18
    # = (18At - 18m) / 18
    # = At - m  [circular!]
    
    # Let's try the p, q approach more carefully.
    # p = k - 6m, q = k + 6m
    # z = ((A+3)p + (A-3)q + 2AB) / 36
    
    # For A > 3: A-3 > 0, so all terms (A+3)p, (A-3)q, 2AB are positive IF p > 0.
    # Is p always positive? p = k - 6m = 18t - B - 6m.
    # p > 0 iff 18t > B + 6m iff t > (B + 6m)/18
    
    # For A = 3: p = k - 6m, and pq = B², so p = B²/q.
    # p > 0 always since B > 0.
    
    # For A ≠ 3: pq = B² - 36t²(A²-9)
    # When A > 3: A² - 9 > 0, so pq = B² - 36t²(A²-9) < B²
    # pq could be negative! (if 36t²(A²-9) > B²)
    
    # But we know z > 0 for actual solutions. Let's check.
    
    # Another approach: express z purely in terms of n, A, t, B
    # z = tA - m where m = sqrt(t²A² - tB)
    # z = tA - sqrt(t²A² - tB)
    # = tA - sqrt(t(tA² - B))
    
    # Rationalize: z = tA - sqrt(t²A² - tB)
    # = (tA - sqrt(t²A² - tB)) * (tA + sqrt(t²A² - tB)) / (tA + sqrt(t²A² - tB))
    # = (t²A² - (t²A² - tB)) / (tA + sqrt(t²A² - tB))
    # = tB / (tA + sqrt(t²A² - tB))
    # = tB / y
    
    # So z = tB / y = tB / (tA + m)
    # This is manifestly positive when t > 0, B > 0 (both guaranteed for valid solutions).
    # The only question is whether y = tA + m > 0, which is guaranteed since y > 0 is required.
    
    # But this is somewhat circular - we need y > 0 to conclude z > 0.
    # The question is: can we prove z > 0 from the local conditions alone?
    
    # Key insight: z = tB / y. If we can show y > 0 from local conditions, then z > 0.
    # But y = tA + m, and m = sqrt(t²A² - tB). 
    # y > 0 iff tA > -m, i.e., tA + m > 0.
    # Since t > 0, A > 0, m ≥ 0, we have y = tA + m > 0 AUTOMATICALLY.
    
    # Wait! m = sqrt(t²A² - tB) ≥ 0 by definition (we take the non-negative root).
    # So y = tA + m ≥ tA > 0 (since t ≥ 1, A ≥ 3).
    # And z = tA - m. For z > 0, we need tA > m, i.e., tA > sqrt(t²A² - tB).
    # Squaring: t²A² > t²A² - tB iff tB > 0 iff t > 0 and B > 0. ALWAYS TRUE!
    
    # So z = tA - m > 0 IFF tB > 0 IFF t > 0 and B > 0.
    # Since t ≥ 1 and B = n(n+A)/2 > 0 for n ≥ 1, A ≥ 3, z > 0 ALWAYS!
    
    # But wait - this seems too easy. Let me verify.
    # z > 0 iff tA > m iff t²A² > m² = t²A² - tB iff tB > 0. YES.
    
    # So z > 0 is AUTOMATIC whenever:
    # 1. t > 0 (which is required for the solution to exist)
    # 2. B > 0 (which is true since n > 0, A > 0)
    # 3. m² = t²A² - tB ≥ 0 (which is required for m to be real/integer)
    
    # The key: m² = t(tA² - B) ≥ 0 means tA² ≥ B.
    # Then z = tA - m, and z² = t²A² - 2tAm + m² = t²A² - 2tAm + t²A² - tB
    # Actually, z = tA - m, so z > 0 iff tA > m.
    # tA > m iff (tA)² > m² = t²A² - tB iff 0 > -tB iff tB > 0. QED.
    
    # So z > 0 is AUTOMATIC for ALL A (not just A=3), as long as:
    # - t > 0 (guaranteed by the search)
    # - B > 0 (guaranteed since n > 0, A > 0)
    # - m² = t(tA² - B) ≥ 0 (guaranteed since we only accept solutions where this is a perfect square)
    
    return {
        'z': z,
        'p': p, 'q': q,
        'eff_N': eff_N,
        'z_formula_general': f'z = ((A+3)p + (A-3)q + 2AB) / 36 = {z}',
        'z_formula_rationalized': 'z = tB / y = tB / (tA + m)',
        'z_expression': 'tB / (tA + m)',
        'z_positive_proof': 'z > 0 iff tA > m iff t²A² > m² = t²A² - tB iff tB > 0',
        'manifestly_positive': True,
        'reason': f'z = tB/(tA+m), t>0, B>0, m≥0 ⟹ tA+m>0 ⟹ z>0. Also z²>0 iff tB>0.',
        'p_sign': 'positive' if p > 0 else 'negative',
        'q_sign': 'positive' if q > 0 else 'negative',
        'eff_N_sign': 'positive' if eff_N > 0 else 'negative',
        'eff_N_vs_B2': eff_N - B*B,  # = -36t²(A²-9)
    }

# ============================================================
# Main analysis
# ============================================================

def main():
    print("=" * 80)
    print("POSITIVITY ANALYSIS FOR A ≠ 3 IN ERDŐS-STRAUS CONJECTURE")
    print("n ≡ 1 (mod 12), n ≢ 0 (mod 5)")
    print("=" * 80)
    
    # Step 1: Find all cases where A=3 fails, up to n=10000
    print("\n1. Finding all cases where A=3 fails (n ≤ 10000)...")
    
    a3_fail_cases = []
    for n in range(13, 10001):
        if n % 12 != 1 or n % 5 == 0:
            continue
        works, reason = check_a3_works(n)
        if not works:
            a3_fail_cases.append(n)
    
    print(f"   Found {len(a3_fail_cases)} cases where A=3 fails")
    
    # Step 2: For each case, find the minimum A that works
    print(f"\n2. Finding minimum A solutions for {len(a3_fail_cases)} cases...")
    
    all_solutions = []
    detailed_results = {}
    
    for idx, n in enumerate(a3_fail_cases):
        if idx % 100 == 0:
            print(f"   Processing case {idx+1}/{len(a3_fail_cases)}: n={n}")
        
        sol = find_min_A_solution(n, max_A=500, max_t=100000)
        
        if sol['found']:
            sol['n'] = n
            analysis = analyze_z_structure(sol)
            
            # Compute additional quantities
            A = sol['A']
            B = sol['B']
            t = sol['t']
            m = sol['m']
            k = sol['k']
            z = sol['z']
            y = sol['y']
            x = sol['x']
            
            # Verify z > 0
            assert z > 0, f"z not positive for n={n}!"
            
            # Check the positivity proof: z > 0 iff tB > 0
            tB = t * B
            z_positive_iff = tB > 0
            
            # Relationship between z and other variables
            z_over_tB = Fraction(z, 1) / Fraction(tB, 1)  # = 1/y
            z_over_B = Fraction(z, B)
            z_over_n = Fraction(z, n)
            z_over_A = Fraction(z, A)
            
            # Check if z is a simple fraction of B
            # z = tB/y, so z/B = t/y
            z_ratio_t_y = Fraction(t, y)
            
            # Also check: is y - z = 2m, y + z = 2tA
            assert y - z == 2 * m
            assert y + z == 2 * t * A
            
            # Check effective N
            eff_N = sol['effective_N']
            
            result = {
                'n': n,
                'A': A,
                'B': B,
                'x': x, 'y': y, 'z': z,
                't': t, 'm': m, 'k': k,
                'p': k - 6*m,
                'q': k + 6*m,
                'eff_N': eff_N,
                'eff_N_positive': eff_N > 0,
                'eff_N_negative': eff_N < 0,
                'eff_N_zero': eff_N == 0,
                'z_positive': True,
                'z_positive_iff_tB_positive': z_positive_iff,
                'z_expression': 'tB / (tA + m)',
                'z_proof': 'z > 0 ⟺ tA > m ⟺ t²A² > m² = t²A² - tB ⟺ tB > 0',
                'z_formula_via_pq': f'z = ((A+3)p + (A-3)q + 2AB) / 36',
                'z_over_B': str(z_over_B),
                'z_over_n': str(z_over_n),
                'z_over_A': str(z_over_A),
                'z_equals_tB_over_y': True,
                'yz_equals_tB': y * z == t * B,
                'analysis': analysis
            }
            
            all_solutions.append(result)
            detailed_results[str(n)] = result
        else:
            print(f"   WARNING: No solution found for n={n}!")
            detailed_results[str(n)] = {'found': False, 'reason': sol.get('reason', 'unknown')}
    
    print(f"\n   Solutions found for {len(all_solutions)}/{len(a3_fail_cases)} cases")
    
    # Step 3: Analyze patterns
    print("\n3. Analyzing patterns in z...")
    
    # Distribution of A values
    A_distribution = Counter(sol['A'] for sol in all_solutions)
    print(f"\n   A value distribution:")
    for A, count in sorted(A_distribution.items()):
        print(f"     A={A:3d}: {count:4d} cases ({100*count/len(all_solutions):.1f}%)")
    
    # Is z always positive?
    all_z_positive = all(sol['z'] > 0 for sol in all_solutions)
    print(f"\n   z always positive: {all_z_positive}")
    
    # Is effective_N always positive, negative, or varies?
    eff_N_positive = sum(1 for sol in all_solutions if sol['eff_N_positive'])
    eff_N_negative = sum(1 for sol in all_solutions if sol['eff_N_negative'])
    eff_N_zero = sum(1 for sol in all_solutions if sol['eff_N_zero'])
    print(f"\n   Effective N = B² - 36t²(A²-9) = (k-6m)(k+6m):")
    print(f"     Positive: {eff_N_positive} ({100*eff_N_positive/len(all_solutions):.1f}%)")
    print(f"     Negative: {eff_N_negative} ({100*eff_N_negative/len(all_solutions):.1f}%)")
    print(f"     Zero: {eff_N_zero} ({100*eff_N_zero/len(all_solutions):.1f}%)")
    
    # What's the sign of p = k - 6m?
    p_positive = sum(1 for sol in all_solutions if sol['p'] > 0)
    p_negative = sum(1 for sol in all_solutions if sol['p'] < 0)
    p_zero = sum(1 for sol in all_solutions if sol['p'] == 0)
    print(f"\n   Sign of p = k - 6m:")
    print(f"     Positive: {p_positive} ({100*p_positive/len(all_solutions):.1f}%)")
    print(f"     Negative: {p_negative} ({100*p_negative/len(all_solutions):.1f}%)")
    print(f"     Zero: {p_zero} ({100*p_zero/len(all_solutions):.1f}%)")
    
    # Key relationship: z = tB / y
    all_yz_tB = all(sol['yz_equals_tB'] for sol in all_solutions)
    print(f"\n   yz = tB always holds: {all_yz_tB}")
    
    # z positivity proof
    print(f"\n4. Positivity proof for A ≠ 3:")
    print(f"   z = tA - m")
    print(f"   m = sqrt(t²A² - tB)  [m² = t(tA² - B)]")
    print(f"   z > 0  ⟺  tA > m  ⟺  (tA)² > m²  ⟺  t²A² > t²A² - tB  ⟺  tB > 0")
    print(f"   Since t ≥ 1 and B = n(n+A)/2 > 0 for n ≥ 1, A ≥ 3: tB > 0 ALWAYS.")
    print(f"   Therefore z > 0 is AUTOMATIC for ALL A (not just A=3).")
    print(f"   The condition m² = t(tA² - B) ≥ 0 (i.e., tA² ≥ B) ensures m is real.")
    print(f"   When m exists as an integer, z > 0 follows automatically.")
    
    # Step 5: Check if the z formula via p,q simplifies
    print(f"\n5. z formula via p, q for A ≠ 3:")
    print(f"   z = ((A+3)p + (A-3)q + 2AB) / 36")
    print(f"   where p = k-6m, q = k+6m, pq = B² - 36t²(A²-9)")
    print(f"")
    print(f"   For A=3: z = (6p + 0·q + 6B)/36 = (p+B)/6  [simple!]")
    print(f"   For A≠3: z = ((A+3)p + (A-3)q + 2AB)/36  [more complex]")
    print(f"")
    print(f"   BUT: z = tB/(tA+m) is the UNIVERSAL formula, valid for ALL A.")
    print(f"   This is manifestly positive when t>0, B>0, tA+m>0.")
    print(f"   Since t≥1, A≥3, m≥0: tA+m ≥ 3 > 0. So z > 0 ALWAYS.")
    
    # Step 6: Can positivity be proven from local conditions alone?
    print(f"\n6. Can positivity be proven from local conditions alone?")
    print(f"")
    print(f"   For A=3: z = (d+B)/6, positivity is from d>0, B>0 (local: d | B² > 0)")
    print(f"   For A≠3: z = tB/(tA+m), positivity requires t>0, B>0, tA+m>0")
    print(f"   - t > 0: This is a GLOBAL condition (t = (k+B)/18 must be positive)")
    print(f"   - B > 0: This is automatic (B = n(n+A)/2 > 0)")
    print(f"   - tA+m > 0: Automatic since t≥1, A≥3, m≥0")
    print(f"   - m² = t(tA²-B) ≥ 0: This is a GLOBAL condition (tA² ≥ B)")
    print(f"")
    print(f"   The key insight: positivity of z is equivalent to tB > 0,")
    print(f"   which is automatic whenever a valid solution exists.")
    print(f"   The EXISTENCE of a solution (with m² = t(tA²-B) ≥ 0, t > 0)")
    print(f"   is the hard part - positivity is automatic once it exists.")
    print(f"")
    print(f"   Comparison with A=3:")
    print(f"   - A=3: z = (d+B)/6. Positivity from d>0 (divisor of B²). LOCAL.")
    print(f"   - A≠3: z = tB/y. Positivity from t>0, B>0, y>0. GLOBAL (t>0 is global).")
    print(f"   BUT: For A=3, t>0 is also needed (t=(d+B²/d+2B)/36), and this is")
    print(f"   guaranteed by the mod 36 condition. For A≠3, t>0 is guaranteed")
    print(f"   by the search algorithm finding t≥1.")
    
    # Collect z/B ratios
    z_over_B_ratios = [Fraction(sol['z'], sol['B']) for sol in all_solutions]
    z_over_n_ratios = [Fraction(sol['z'], sol['n']) for sol in all_solutions]
    
    # Check if z/B has a pattern
    zB_unique = Counter(str(r) for r in z_over_B_ratios)
    zn_unique = Counter(str(r) for r in z_over_n_ratios)
    
    print(f"\n7. z/B ratio distribution (top 20):")
    for ratio, count in zB_unique.most_common(20):
        print(f"   z/B = {ratio:20s}: {count:4d} cases")
    
    print(f"\n   z/n ratio distribution (top 20):")
    for ratio, count in zn_unique.most_common(20):
        print(f"   z/n = {ratio:20s}: {count:4d} cases")
    
    # Check if z is a simple fraction of B for any A
    print(f"\n8. Relationship between z and B for each A value:")
    for A_val in sorted(set(sol['A'] for sol in all_solutions)):
        sols_A = [sol for sol in all_solutions if sol['A'] == A_val]
        zB_ratios = [Fraction(s['z'], s['B']) for s in sols_A]
        unique_r = set(zB_ratios)
        print(f"   A={A_val:3d}: {len(sols_A):4d} solutions, {len(unique_r):4d} unique z/B ratios")
        if len(unique_r) <= 10:
            for r in sorted(unique_r):
                count = sum(1 for zr in zB_ratios if zr == r)
                print(f"           z/B = {r}: {count} cases")
    
    # Final summary
    print(f"\n{'='*80}")
    print("FINAL SUMMARY")
    print(f"{'='*80}")
    
    summary = {
        'total_a3_fail_cases': len(a3_fail_cases),
        'solutions_found': len(all_solutions),
        'all_z_positive': all_z_positive,
        
        'key_finding': {
            'z_expression_universal': 'z = tB / (tA + m)',
            'z_expression_via_pq': 'z = ((A+3)p + (A-3)q + 2AB) / 36',
            'z_expression_a3_special': 'z = (d + B) / 6  [when A=3, p=d, q=B²/d]',
            
            'positivity_proof': {
                'statement': 'z > 0 for ALL A (including A ≠ 3) whenever a valid solution exists',
                'proof': [
                    'z = tA - m where m = sqrt(t²A² - tB) ≥ 0',
                    'z > 0 ⟺ tA > m ⟺ (tA)² > m² = t²A² - tB ⟺ tB > 0',
                    'Since t ≥ 1 (search constraint) and B = n(n+A)/2 > 0 (n ≥ 1, A ≥ 3)',
                    'Therefore tB > 0, hence z > 0. QED.'
                ],
                'is_automatic': True,
                'requires_local_conditions': False,
                'requires_global_conditions': True,
                'global_conditions_needed': [
                    't > 0 (global: t = (k+B)/18 must be positive integer)',
                    'm² = t(tA² - B) ≥ 0 (global: tA² ≥ B)',
                    'm is a non-negative integer (global: perfect square check)'
                ],
                'comparison_with_a3': {
                    'a3_z_formula': 'z = (d + B) / 6',
                    'a3_positivity': 'd > 0 (divisor of B²) and B > 0 → z > 0. LOCAL.',
                    'a_ne_3_z_formula': 'z = tB / (tA + m)',
                    'a_ne_3_positivity': 't > 0 and B > 0 and tA+m > 0 → z > 0. GLOBAL (requires t > 0).',
                    'key_difference': 'For A=3, positivity is from divisor properties (local). For A≠3, positivity is from tB>0 (global but automatic once solution exists).',
                    'unified_view': 'z = tB/y is universal. For A=3, y=tA+m=3t+m, and t=B/9+... giving z=(d+B)/6. The positivity always reduces to tB>0.'
                }
            },
            
            'can_positivity_be_proven_from_local_conditions_alone': {
                'answer': False,
                'explanation': 'For A≠3, z > 0 requires t > 0, which is a global condition (t = (k+B)/18 must be a positive integer). Local conditions (mod p) guarantee rational solvability but not positivity of t. However, positivity is automatic once any valid integer solution exists, because z > 0 ⟺ tB > 0, and t ≥ 1, B > 0 are guaranteed by the solution itself.',
                'nuance': 'The positivity of z is NOT the obstruction. The real obstruction is the EXISTENCE of an integer solution (t, m) with m² = t(tA²-B). Once such a solution exists, z > 0 is automatic. This is the same situation as A=3: the hard part is finding a valid divisor d; once found, z = (d+B)/6 > 0 is trivial.',
                'implication': 'The integral Hasse principle gap is about EXISTENCE of integer solutions, not about POSITIVITY. Positivity is a red herring - it is always automatic once a solution exists.'
            }
        },
        
        'A_distribution': dict(A_distribution),
        'eff_N_signs': {
            'positive': eff_N_positive,
            'negative': eff_N_negative,
            'zero': eff_N_zero
        },
        'p_signs': {
            'positive': p_positive,
            'negative': p_negative,
            'zero': p_zero
        },
        'all_yz_equals_tB': all_yz_tB,
    }
    
    # Save detailed results
    output = {
        'metadata': {
            'description': 'Positivity analysis for z = tA - m in Erdős-Straus conjecture for A ≠ 3',
            'residue_class': 'n ≡ 1 (mod 12), n ≢ 0 (mod 5)',
            'date': '2026-07-17',
            'max_n': 10000,
        },
        'summary': summary,
        'detailed_results': detailed_results,
        'a3_fail_cases': a3_fail_cases,
    }
    
    output_path = os.path.expanduser('~/.openclaw/workspace/ErdosStrausConjecture/positivity_analysis.json')
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\nResults saved to {output_path}")
    
    # Print the final theorem
    print(f"\n{'='*80}")
    print("THEOREM (Positivity of z for all A)")
    print(f"{'='*80}")
    print(f"""
For the Erdős-Straus decomposition with parameter A:
  x = (n+A)/4, y = tA + m, z = tA - m
where m² = t(tA² - B), B = n(n+A)/2:

z > 0 is AUTOMATIC for ALL A ≥ 3 (including A ≠ 3).

Proof:
  z = tA - m, where m = sqrt(t²A² - tB) ≥ 0.
  z > 0  ⟺  tA > m  ⟺  (tA)² > m²  ⟺  t²A² > t²A² - tB  ⟺  tB > 0.
  Since t ≥ 1 (positive integer by construction) and B = n(n+A)/2 > 0
  (for n ≥ 1, A ≥ 3), we have tB > 0, hence z > 0.  □

Equivalently: z = tB / y, which is manifestly positive since t, B, y > 0.

For A = 3: z = (d + B)/6, positivity from d > 0 (divisor of B²). [LOCAL]
For A ≠ 3: z = tB / y, positivity from t > 0 and B > 0. [GLOBAL but automatic]

The positivity of z is NOT the obstruction. The real challenge is the 
EXISTENCE of an integer solution (t, m) with m² = t(tA² - B). Once such 
a solution exists, z > 0 follows automatically — no separate positivity 
argument is needed, for any A.

The integral Hasse principle gap is about EXISTENCE, not POSITIVITY.
""")

if __name__ == '__main__':
    main()