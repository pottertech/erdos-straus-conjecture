#!/usr/bin/env python3
"""
Verify Erdős-Straus conjecture z=my parametrization for prime hard cases.
Search range: primes from 10,001 to 1,000,000.
"""

import math
import sys
import time
from collections import Counter
from sympy import isprime, factorint, divisors

def is_hard_case(n):
    """Check if prime n satisfies hard case conditions:
    - n ≡ 1 mod 12
    - n ≢ 0 mod 5
    - n is prime
    - All odd prime factors of B3 = n(n+3)/4 are ≡ 1 mod 3
    """
    if n % 12 != 1:
        return False
    if n % 5 == 0:
        return False
    if not isprime(n):
        return False
    
    B3 = n * (n + 3) // 4
    # Factor B3 and check all odd prime factors
    factors = factorint(B3)
    for p, e in factors.items():
        if p == 2:
            continue
        if p % 3 != 1:
            return False
    return True

def isqrt(n):
    return int(math.isqrt(n))

def find_umethod_prime(n, search_range=50000):
    """Find u-method solution for prime n.
    Returns (x, y, z, u, is_parametric) or None.
    
    x ranges from n//4+1 to n//4+search_range
    u = 4x - n, so u starts from small positive values
    """
    x_start = n // 4 + 1
    x_end = min(x_start + search_range, n // 4 + 1 + search_range)
    
    for x in range(x_start, x_end):
        u = 4 * x - n
        if u <= 0:
            continue
        
        nx = n * x
        D = nx * nx  # n^2 * x^2
        target = (-nx) % u
        
        # Get divisors of x^2, multiply by n^0, n^1, n^2
        x2 = x * x
        divs_x2 = divisors(x2)
        sqrt_D = isqrt(D)
        
        for a in range(3):  # n^0, n^1, n^2
            n_factor = n ** a
            for d in divs_x2:
                d1 = n_factor * d
                if d1 > sqrt_D:
                    break
                if d1 % u != target:
                    continue
                d2 = D // d1
                if (d2 + nx) % u != 0:
                    continue
                y = (d1 + nx) // u
                z = (d2 + nx) // u
                if y > 0 and z > 0:
                    is_param = (z % y == 0)
                    return (x, y, z, u, is_param)
    return None

def main():
    print("Scanning for prime hard cases from 10,001 to 1,000,000...")
    print("Conditions: n ≡ 1 mod 12, n ≢ 0 mod 5, n prime, all odd prime factors of B3 ≡ 1 mod 3")
    print()
    
    start_time = time.time()
    
    # Phase 1: Find all hard case primes
    hard_cases = []
    for n in range(10001, 1000001):
        if n % 12 != 1:
            continue
        if n % 5 == 0:
            continue
        if not isprime(n):
            continue
        # Check B3 condition
        B3 = n * (n + 3) // 4
        factors = factorint(B3)
        all_good = True
        for p, e in factors.items():
            if p == 2:
                continue
            if p % 3 != 1:
                all_good = False
                break
        if all_good:
            hard_cases.append(n)
    
    elapsed_find = time.time() - start_time
    print(f"Found {len(hard_cases)} prime hard cases in {elapsed_find:.1f}s")
    print(f"First few: {hard_cases[:10]}")
    print(f"Last few: {hard_cases[-10:]}")
    print()
    
    # Phase 2: Apply u-method to each
    results = []
    u_distribution = Counter()
    non_parametric = []
    max_u = 0
    max_u_n = 0
    no_solution_499 = []
    
    total = len(hard_cases)
    for i, n in enumerate(hard_cases):
        if i % 10 == 0:
            print(f"  Processing {i+1}/{total}: n={n}...", flush=True)
        
        result = find_umethod_prime(n, search_range=50000)
        
        if result is None:
            # Try extended search
            result = find_umethod_prime(n, search_range=100000)
        
        if result is None:
            print(f"  WARNING: No solution found for n={n} even with extended search!")
            no_solution_499.append(n)
            results.append((n, None, None, None, None, None))
        else:
            x, y, z, u, is_param = result
            results.append((n, u, is_param, x, y, z))
            u_distribution[u] += 1
            
            if u > max_u:
                max_u = u
                max_u_n = n
            
            if not is_param:
                non_parametric.append((n, u, x, y, z))
            
            # Check if u > 499
            if u > 499:
                no_solution_499.append(n)
    
    elapsed_total = time.time() - start_time
    print()
    print(f"Total time: {elapsed_total:.1f}s")
    print(f"Total prime hard cases: {total}")
    print(f"Max u found: {max_u} at n={max_u_n}")
    print(f"Non-parametric cases: {len(non_parametric)}")
    print(f"Cases with u > 499: {len(no_solution_499)}")
    print()
    
    # Write results to file
    with open("/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/PRIME_VERIFICATION_1M.md", "w") as f:
        f.write("# Erdős-Straus Conjecture: Prime Hard Case Verification (10,001 – 1,000,000)\n\n")
        f.write("## Overview\n\n")
        f.write(f"**Date:** 2026-08-14\n")
        f.write(f"**Range:** Primes from 10,001 to 1,000,000\n")
        f.write(f"**Method:** General u-method (divisor-based search)\n")
        f.write(f"**Search range:** x from n//4+1, up to 100,000 values of x\n")
        f.write(f"**Total computation time:** {elapsed_total:.1f}s\n\n")
        
        f.write("## Hard Case Conditions\n\n")
        f.write("- n ≡ 1 mod 12\n")
        f.write("- n ≢ 0 mod 5\n")
        f.write("- n is prime\n")
        f.write("- All odd prime factors of B₃ = n(n+3)/4 are ≡ 1 mod 3\n\n")
        
        f.write("## Summary Statistics\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total prime hard cases found | {total} |\n")
        f.write(f"| Solutions found via u-method | {total - len([r for r in results if r[1] is None])} |\n")
        f.write(f"| Cases with no solution (extended search) | {len([r for r in results if r[1] is None])} |\n")
        f.write(f"| Max u found | {max_u} |\n")
        f.write(f"| Max u at n = | {max_u_n} |\n")
        f.write(f"| Non-parametric cases (z/y not integer) | {len(non_parametric)} |\n")
        f.write(f"| Cases with u > 499 | {len(no_solution_499)} |\n\n")
        
        f.write("## Distribution of min u Values\n\n")
        f.write("| u value | Count | Percentage |\n")
        f.write("|---------|-------|------------|\n")
        for u in sorted(u_distribution.keys()):
            count = u_distribution[u]
            pct = 100.0 * count / total
            f.write(f"| {u} | {count} | {pct:.1f}% |\n")
        f.write(f"| **Total** | **{sum(u_distribution.values())} | 100.0%** |\n\n")
        
        f.write("## Max u Details\n\n")
        f.write(f"- **n** = {max_u_n}\n")
        f.write(f"- **u** = {max_u}\n")
        # Find the full details
        for r in results:
            if r[0] == max_u_n and r[1] is not None:
                n, u, is_param, x, y, z = r
                f.write(f"- **x** = {x}\n")
                f.write(f"- **y** = {y}\n")
                f.write(f"- **z** = {z}\n")
                f.write(f"- **is_parametric** = {is_param}\n")
                # Verify: 4/(n) = 1/x + 1/y + 1/z
                lhs = 4 * y * z
                rhs = n * y * z + n * x * z + n * x * y
                f.write(f"- **Verification:** 4·y·z = {lhs}, n·(y·z + x·z + x·y) = {rhs}, match = {lhs == rhs}\n")
                break
        f.write("\n")
        
        f.write("## Non-Parametric Cases (z/y is not integer)\n\n")
        if non_parametric:
            f.write("| n | u | x | y | z | z mod y |\n")
            f.write("|---|---|---|---|---|---------|\n")
            for n, u, x, y, z in non_parametric:
                f.write(f"| {n} | {u} | {x} | {y} | {z} | {z % y} |\n")
            f.write("\n")
        else:
            f.write("None — all cases are parametric (z/y is integer).\n\n")
        
        f.write("## Cases with u > 499\n\n")
        if no_solution_499:
            f.write(f"Found {len(no_solution_499)} cases where no solution with u ≤ 499 exists:\n\n")
            for n in no_solution_499:
                # Find the actual u
                for r in results:
                    if r[0] == n:
                        if r[1] is not None:
                            f.write(f"- n={n}, u={r[1]}\n")
                        else:
                            f.write(f"- n={n}, NO SOLUTION FOUND\n")
                        break
            f.write("\n")
        else:
            f.write("None — all cases have a solution with u ≤ 499.\n\n")
        
        f.write("## All Results (sorted by n)\n\n")
        f.write("| n | u | is_parametric | x | y | z |\n")
        f.write("|---|---|---------------|---|---|---|\n")
        for r in results:
            if r[1] is not None:
                n, u, is_param, x, y, z = r
                f.write(f"| {n} | {u} | {is_param} | {x} | {y} | {z} |\n")
            else:
                f.write(f"| {r[0]} | — | — | — | — | — |\n")
    
    print("Results written to PRIME_VERIFICATION_1M.md")

if __name__ == "__main__":
    main()