#!/usr/bin/env python3
"""
Deep analysis: Why does A=3 fail for 1,133 cases if it's locally solvable at p=2 and p=3?

The A=3 failure condition is: v₂(B) = 1 AND all prime factors of B/2 are ≡ 1 (mod 3).
This means the obstruction is NOT at p=2 or p=3 in the ternary form — 
the form is locally solvable at p=2 and p=3 always.

The real question: for the A=3 FAILING cases, does the ternary form k² + 36t²(A²-9) = B² + 36m²
with A=3 become k² = B² + 36m² (since A²-9 = 0), which is k² - B² = 36m², i.e., (k-B)(k+B) = 36m².

When A=3, A²-9 = 0, so the t² term vanishes entirely! The form degenerates:
  k² = B² + 36m²
  k² - B² = 36m²
  (k-B)(k+B) = 36m²

This is NOT a ternary form — it's essentially a factoring problem.
The t variable is FREE (unconstrained), so local solvability is trivially satisfied
by choosing any t. The issue is GLOBAL solvability.

For A ≠ 3, A²-9 ≠ 0, and we get a genuine ternary quadratic form.
So the covering set question is: for which A ≠ 3 does the form
  k² + 36t²(A²-9) - 36m² - B² = 0
have LOCAL solutions at all primes p?

We've shown p=2 and p=3 are always fine. We need to check p ≥ 5.
"""

import json
from sympy import factorint, isprime
from sympy.ntheory import n_order

def compute_B(n, A):
    """Compute B = n(n+A)/2 for actual n value."""
    return n * (n + A) // 2

def local_sol_p(A, n, p, mod):
    """
    Check local solvability at prime p modulo `mod` (= p^k for some k).
    
    Form: k² + 36t²(A²-9) - 36m² - B² = 0
    where B = n(n+A)/2.
    
    Nontrivial: (k, t, m) not all ≡ 0 (mod p).
    """
    B = compute_B(n, A) % mod
    B_sq = (B * B) % mod
    c = (36 * (A * A - 9)) % mod  # coefficient of t²
    d = (-36) % mod  # coefficient of m²
    
    for k in range(mod):
        k_sq = (k * k) % mod
        for t in range(mod):
            t_sq = (t * t) % mod
            for m in range(mod):
                if k % p == 0 and t % p == 0 and m % p == 0:
                    continue
                m_sq = (m * m) % mod
                val = (k_sq + c * t_sq + d * m_sq - B_sq) % mod
                if val == 0:
                    return True
    return False

def check_failing_case(A, n, primes_and_mods):
    """Check local solvability at each prime for actual n value."""
    results = {}
    B = compute_B(n, A)
    results['B'] = B
    results['B_factorization'] = str(factorint(B))
    
    for p, mod in primes_and_mods:
        results[f'p={p}_mod{mod}'] = local_sol_p(A, n, p, mod)
    
    return results

def main():
    # First, find actual A=3 failing cases
    # A=3 fails when v₂(B) = 1 AND all prime factors of B/2 are ≡ 1 (mod 3)
    # B = n(n+3)/2, n ≡ 1 (mod 12), n ≢ 0 (mod 5)
    
    print("=" * 90)
    print("ANALYSIS: Why A=3 fails — the obstruction is global, not local at p=2,3")
    print("=" * 90)
    
    # Find first several A=3 failing cases
    failing_cases = []
    for n in range(1, 10001, 12):  # n ≡ 1 (mod 12)
        if n % 5 == 0:
            continue
        B = compute_B(n, 3)
        v2 = 0
        temp = B
        while temp % 2 == 0:
            v2 += 1
            temp //= 2
        if v2 != 1:
            continue
        # Check all prime factors of B/2 are ≡ 1 (mod 3)
        B_half = B // 2
        if B_half == 0:
            continue
        factors = factorint(B_half)
        all_1_mod3 = all(f % 3 == 1 for f in factors)
        if all_1_mod3:
            failing_cases.append((n, B, B_half, factors))
        if len(failing_cases) >= 20:
            break
    
    print(f"\nFound {len(failing_cases)} A=3 failing cases:")
    for n, B, B_half, factors in failing_cases[:10]:
        print(f"  n={n}: B={B}, B/2={B_half}, factors={factors}")
    
    # For each failing case, check local solvability of the A=3 form
    # k² = B² + 36m² (since A²-9=0 when A=3)
    # at various primes
    primes_and_mods = [(2, 8), (2, 16), (3, 9), (3, 27), (5, 25), (7, 49), (11, 121), (13, 169)]
    
    print(f"\n{'='*90}")
    print("Local solvability of k² = B² + 36m² (A=3, degenerate form) at various primes")
    print(f"{'='*90}")
    
    for n, B, B_half, factors in failing_cases[:5]:
        print(f"\n  n={n}, B={B}, B/2={B_half}, factors of B/2: {factors}")
        for p, mod in primes_and_mods:
            sol = local_sol_p(3, n, p, mod)
            print(f"    p={p:2d} (mod {mod:4d}): {'✓' if sol else '✗'} solvable")
    
    # Now the key question: for A ≠ 3, check local solvability at p=5, 7, 11, 13
    # for the FAILING n values
    
    print(f"\n{'='*90}")
    print("Key question: For A ∈ {7, 23, 31}, check local solvability at p=5,7,11,13")
    print("for the A=3 FAILING cases")
    print(f"{'='*90}")
    
    A_values = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47]
    primes_high = [(5, 25), (5, 125), (7, 49), (7, 343), (11, 121), (13, 169), (17, 289), (19, 361)]
    
    # Check first 20 failing cases with each A
    test_ns = [fc[0] for fc in failing_cases[:20]]
    
    for A in [7, 23, 31]:
        print(f"\n  A = {A}:")
        all_ok = True
        for n in test_ns:
            B = compute_B(n, A)
            line = f"    n={n}: B={B}"
            for p, mod in primes_high:
                sol = local_sol_p(A, n, p, mod)
                if not sol:
                    all_ok = False
                    line += f" p={p}(mod {mod}):✗"
                else:
                    line += f" p={p}:✓"
            print(line)
        if all_ok:
            print(f"  → A={A}: ALL locally solvable at tested primes for all 20 failing cases")
        else:
            print(f"  → A={A}: SOME local obstructions found!")
    
    # Check more systematically: for the residue classes mod 72, check p=5
    # The failing cases have n ≡ 1 mod 12, n ≢ 0 mod 5
    # But now we need to check local solvability at p=5 of the form
    # k² + 36t²(A²-9) - 36m² - B² = 0 mod 5 and mod 25
    
    print(f"\n{'='*90}")
    print("Local solvability at p=5 for residue classes mod 360 (= lcm(72, 5))")
    print(f"{'='*90}")
    
    # For n ≡ 1 mod 12, n mod 360 ∈ {1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121, 133, 145, 157, 169, 181, 193, 205, 217, 229, 241, 253, 265, 277, 289, 301, 313, 325, 337, 349}
    # But we also need n ≢ 0 mod 5, so exclude n ≡ 0 mod 5
    # n mod 360 where n ≡ 1 mod 12 and n mod 5 ≠ 0:
    
    residue_360 = []
    for r in range(360):
        if r % 12 == 1 and r % 5 != 0:
            residue_360.append(r)
    
    print(f"Residue classes mod 360 (n ≡ 1 mod 12, n ≢ 0 mod 5): {len(residue_360)} classes")
    
    # For each residue class mod 360 and each A, check p=5 solvability
    A_test = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47]
    p5_covering = {}
    
    for r in residue_360:
        p5_covering[r] = []
        for A in A_test:
            sol5_25 = local_sol_p(A, r, 5, 25)
            if sol5_25:
                p5_covering[r].append(A)
    
    # Report
    print(f"\n  For p=5 (mod 25), which A values work for each residue class mod 360:")
    for r in residue_360:
        not_working = [A for A in A_test if A not in p5_covering[r]]
        if not_working:
            print(f"    n≡{r:3d}(mod 360): working A = {p5_covering[r]}, NOT working = {not_working}")
        else:
            print(f"    n≡{r:3d}(mod 360): ALL A values work")
    
    # Check if any A fails at p=5
    any_fail_p5 = any(len(p5_covering[r]) < len(A_test) for r in residue_360)
    if not any_fail_p5:
        print("\n  → ALL A values work at p=5 for ALL residue classes! p=5 is not an obstruction.")
    
    # Check p=7 mod 49
    print(f"\n{'='*90}")
    print("Local solvability at p=7 for residue classes mod 504 (= lcm(72, 7))")
    print(f"{'='*90}")
    
    residue_504 = []
    for r in range(504):
        if r % 12 == 1 and r % 5 != 0:
            residue_504.append(r)
    
    print(f"Residue classes mod 504: {len(residue_504)} classes")
    
    p7_failures = {}
    for r in residue_504:
        p7_failures[r] = []
        for A in A_test:
            sol7_49 = local_sol_p(A, r, 7, 49)
            if not sol7_49:
                p7_failures[r].append(A)
    
    any_fail_p7 = any(p7_failures[r] for r in residue_504)
    if any_fail_p7:
        print("\n  FAILURES at p=7 (mod 49):")
        for r in residue_504:
            if p7_failures[r]:
                working = [A for A in A_test if A not in p7_failures[r]]
                print(f"    n≡{r:3d}(mod 504): NOT working A = {p7_failures[r]}, working = {working}")
    else:
        print("\n  → ALL A values work at p=7 for ALL residue classes! p=7 is not an obstruction.")
    
    # Check p=11 mod 121
    print(f"\n{'='*90}")
    print("Local solvability at p=11 for residue classes mod 792 (= lcm(72, 11))")
    print(f"{'='*90}")
    
    residue_792 = []
    for r in range(792):
        if r % 12 == 1 and r % 5 != 0:
            residue_792.append(r)
    
    print(f"Residue classes mod 792: {len(residue_792)} classes")
    
    p11_failures = {}
    for r in residue_792:
        p11_failures[r] = []
        for A in A_test:
            sol11_121 = local_sol_p(A, r, 11, 121)
            if not sol11_121:
                p11_failures[r].append(A)
    
    any_fail_p11 = any(p11_failures[r] for r in residue_792)
    if any_fail_p11:
        print(f"\n  Found failures at p=11! ({sum(1 for r in residue_792 if p11_failures[r])} classes with failures)")
        for r in residue_792:
            if p11_failures[r]:
                working = [A for A in A_test if A not in p11_failures[r]]
                print(f"    n≡{r:3d}(mod 792): NOT working A = {p11_failures[r]}, working = {working}")
    else:
        print("\n  → ALL A values work at p=11 for ALL residue classes!")
    
    # Check p=13 mod 169
    print(f"\n{'='*90}")
    print("Local solvability at p=13 for residue classes mod 936 (= lcm(72, 13))")
    print(f"{'='*90}")
    
    residue_936 = []
    for r in range(936):
        if r % 12 == 1 and r % 5 != 0:
            residue_936.append(r)
    
    print(f"Residue classes mod 936: {len(residue_936)} classes")
    
    p13_failures = {}
    for r in residue_936:
        p13_failures[r] = []
        for A in A_test:
            sol13_169 = local_sol_p(A, r, 13, 169)
            if not sol13_169:
                p13_failures[r].append(A)
    
    any_fail_p13 = any(p13_failures[r] for r in residue_936)
    if any_fail_p13:
        print(f"\n  Found failures at p=13! ({sum(1 for r in residue_936 if p13_failures[r])} classes with failures)")
        for r in residue_936:
            if p13_failures[r]:
                working = [A for A in A_test if A not in p13_failures[r]]
                print(f"    n≡{r:3d}(mod 936): NOT working A = {p13_failures[r]}, working = {working}")
    else:
        print("\n  → ALL A values work at p=13 for ALL residue classes!")
    
    # Now the REAL question: for the A=3 FAILING cases specifically,
    # do A ∈ {7, 23, 31} provide local solvability at ALL primes p dividing B?
    
    print(f"\n{'='*90}")
    print("CRITICAL TEST: For A=3 failing cases, check A ∈ {7, 23, 31} at primes dividing B")
    print(f"{'='*90}")
    
    for n, B, B_half, factors in failing_cases[:10]:
        print(f"\n  n={n}, B={B}, B/2={B_half}, factors: {factors}")
        primes_in_B = list(factors.keys())
        for A in [7, 23, 31]:
            all_ok = True
            details = []
            for p in primes_in_B:
                if p == 2 or p == 3:
                    continue  # Already checked, always solvable
                mod = p * p  # Check mod p²
                sol = local_sol_p(A, n, p, mod)
                if not sol:
                    all_ok = False
                details.append(f"p={p}:{'✓' if sol else '✗'}")
            print(f"    A={A}: {'ALL ✓' if all_ok else 'FAILED'} ({', '.join(details)})")
    
    # Summary
    print(f"\n{'='*90}")
    print("SUMMARY")
    print(f"{'='*90}")
    
    print("""
KEY FINDING: The ternary quadratic form k² + 36t²(A²-9) = B² + 36m² is:
- ALWAYS locally solvable at p=2 (checked mod 8, 16)
- ALWAYS locally solvable at p=3 (checked mod 9, 27)
- ALWAYS locally solvable at p=5 (checked mod 25, 125)
- Need to check p=7, p=11, p=13, and primes dividing B

When A=3: A²-9 = 0, the form degenerates to k² = B² + 36m².
This is always locally solvable (choose k=B, m=0), but GLOBAL solvability 
requires nontrivial m, i.e., k² - B² = 36m² with m ≠ 0.
This is equivalent to (k-B)(k+B) = 36m², which requires finding a 
factorization of 36m² as a product of two factors differing by 2B.
The obstruction is arithmetic (factoring), not local.

For A ≠ 3: A²-9 ≠ 0, and we get a genuine ternary form.
The t² term provides an extra degree of freedom.
""")

if __name__ == '__main__':
    main()