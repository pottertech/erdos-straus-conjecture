#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Prime Hard Case Verification (1,000,001 – 10,000,000)
Optimized v4: Better divisor generation for large x.
"""

import math
import json
import time
import sys
from collections import Counter
import numpy as np

def isqrt(n):
    return int(math.isqrt(n))

def sieve_primes_numpy(limit):
    """Sieve of Eratosthenes using numpy for speed."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def check_B3_fast(n, small_primes):
    """Check if all odd prime factors of B3 = n(n+3)/4 are ≡ 1 mod 3."""
    B3 = n * (n + 3) // 4
    temp = B3
    while temp % 2 == 0:
        temp //= 2
    
    if temp == 1:
        return True
    
    for p in small_primes:
        if p * p > temp:
            break
        if temp % p == 0:
            if p % 3 != 1:
                return False
            while temp % p == 0:
                temp //= p
    
    if temp > 1:
        if temp % 3 != 1:
            return False
    
    return True

# Global small primes list
small_primes_list = None

def factor_x(n, primes):
    """Factor n using trial division with precomputed primes."""
    factors = {}
    temp = n
    for p in primes:
        if p * p > temp:
            break
        if temp % p == 0:
            count = 0
            while temp % p == 0:
                temp //= p
                count += 1
            factors[p] = count
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def gen_divisors_from_factors(factors):
    """Generate all divisors from prime factorization dict, sorted."""
    divs = [1]
    for p, e in factors.items():
        new_divs = []
        pe = 1
        for i in range(e + 1):
            for d in divs:
                new_divs.append(d * pe)
            pe *= p
        divs = new_divs
    divs.sort()
    return divs

def find_umethod_prime_fast(n, search_range=50000):
    """Find u-method solution for prime n.
    Returns (x, y, z, u, is_parametric) or None."""
    base = n // 4 + 1
    
    for k in range(search_range):
        x = base + k
        u = 4 * k + 3
        if u <= 0:
            continue
        
        nx = n * x
        D = nx * nx
        target = (-nx) % u
        
        x2 = x * x
        sqrt_D = isqrt(D)
        
        # First check the 9 guaranteed divisors: {1, x, x^2} × {1, n, n^2}
        x_factors_list = [1, x, x2]
        n_factors_list = [1, n, n*n]
        for nf in n_factors_list:
            for xf in x_factors_list:
                d1 = nf * xf
                if d1 > sqrt_D:
                    continue
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
        
        # If guaranteed divisors didn't work, factor x and generate all divisors of x^2
        # Factor x (much smaller than x^2)
        x_factors = factor_x(x, small_primes_list)
        # Divisors of x^2 = each exponent doubled
        x2_factors = {p: 2 * e for p, e in x_factors.items()}
        divs_x2 = gen_divisors_from_factors(x2_factors)
        
        for nf in [1, n, n*n]:
            for d in divs_x2:
                d1 = nf * d
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

def flush():
    sys.stdout.flush()

def main():
    global small_primes_list
    
    start_time = time.time()
    
    print("=" * 70, flush=True)
    print("Erdős-Straus Conjecture: Prime Hard Case Verification", flush=True)
    print("Range: 1,000,001 to 10,000,000", flush=True)
    print("=" * 70, flush=True)
    
    # Step 0: Build prime sieve
    print("\n[0/3] Building prime sieve up to 10,000,000...", flush=True)
    sieve_start = time.time()
    prime_sieve = sieve_primes_numpy(10000000)
    sieve_time = time.time() - sieve_start
    prime_count = int(prime_sieve.sum())
    print(f"  Sieve built in {sieve_time:.1f}s ({prime_count:,} primes up to 10M)", flush=True)
    
    # For factoring x (up to ~2.5M) and B3 (up to ~2.5e13, need primes up to sqrt(2.5e13) ≈ 5e6)
    print("  Extracting small primes for trial division...", flush=True)
    sp_start = time.time()
    small_primes_list = [i for i in range(3, 5000001, 2) if prime_sieve[i]]
    sp_time = time.time() - sp_start
    print(f"  {len(small_primes_list):,} odd primes up to 5M extracted in {sp_time:.1f}s", flush=True)
    
    # Step 1: Find all prime hard cases
    print("\n[1/3] Scanning for prime hard cases...", flush=True)
    hard_cases = []
    scan_start = time.time()
    
    first_candidate = 1000009  # 12*83334 + 1
    n = first_candidate
    count_checked = 0
    while n <= 10000000:
        count_checked += 1
        if n % 5 != 0:
            if prime_sieve[n]:
                if check_B3_fast(n, small_primes_list):
                    hard_cases.append(n)
        
        if count_checked % 100000 == 0:
            elapsed = time.time() - scan_start
            print(f"  Scanned to n={n:,} ({count_checked:,} candidates, {len(hard_cases)} hard cases, {elapsed:.1f}s)", flush=True)
        
        n += 12
    
    scan_time = time.time() - scan_start
    print(f"  Scan complete: {len(hard_cases)} prime hard cases found in {scan_time:.1f}s", flush=True)
    print(f"  Total candidates checked (n ≡ 1 mod 12): {count_checked:,}", flush=True)
    
    # Step 2: Find u-method solutions
    print(f"\n[2/3] Finding u-method solutions for {len(hard_cases)} hard cases...", flush=True)
    solve_start = time.time()
    
    results = []
    u_distribution = Counter()
    non_parametric_cases = []
    max_u = 0
    max_u_n = 0
    max_u_details = None
    no_solution_cases = []
    u_over_499 = []
    
    for i, n in enumerate(hard_cases):
        if (i + 1) % 500 == 0:
            elapsed = time.time() - solve_start
            print(f"  Solved {i+1}/{len(hard_cases)} cases ({elapsed:.1f}s, no_sol={len(no_solution_cases)})", flush=True)
        
        result = find_umethod_prime_fast(n, search_range=50000)
        
        if result is None:
            no_solution_cases.append(n)
            continue
        
        x, y, z, u, is_param = result
        results.append({
            'n': n,
            'x': x,
            'y': y,
            'z': z,
            'u': u,
            'is_parametric': is_param
        })
        
        u_distribution[u] += 1
        
        if u > max_u:
            max_u = u
            max_u_n = n
            max_u_details = (x, y, z, u, is_param)
        
        if not is_param:
            non_parametric_cases.append((n, u, x, y, z, z % y))
        
        if u > 499:
            u_over_499.append((n, u))
    
    solve_time = time.time() - solve_start
    total_time = time.time() - start_time
    
    print(f"\n[3/3] Generating report...", flush=True)
    print(f"  Total time: {total_time:.1f}s", flush=True)
    print(f"  Solutions found: {len(results)}", flush=True)
    print(f"  No solution: {len(no_solution_cases)}", flush=True)
    print(f"  Max u: {max_u} (n={max_u_n})", flush=True)
    print(f"  Non-parametric: {len(non_parametric_cases)}", flush=True)
    print(f"  u > 499: {len(u_over_499)}", flush=True)
    
    # Generate markdown report
    report_lines = []
    report_lines.append("# Erdős-Straus Conjecture: Prime Hard Case Verification (1,000,001 – 10,000,000)")
    report_lines.append("")
    report_lines.append("## Overview")
    report_lines.append("")
    report_lines.append(f"**Date:** 2026-08-14")
    report_lines.append(f"**Range:** Primes from 1,000,001 to 10,000,000")
    report_lines.append(f"**Method:** General u-method (divisor-based search)")
    report_lines.append(f"**Search range:** x from n//4+1, up to 50,000 values of x (u up to 200,003)")
    report_lines.append(f"**Total computation time:** {total_time:.1f}s")
    report_lines.append("")
    report_lines.append("## Hard Case Conditions")
    report_lines.append("")
    report_lines.append("- n ≡ 1 mod 12")
    report_lines.append("- n ≢ 0 mod 5")
    report_lines.append("- n is prime")
    report_lines.append("- All odd prime factors of B₃ = n(n+3)/4 are ≡ 1 mod 3")
    report_lines.append("")
    report_lines.append("## Summary Statistics")
    report_lines.append("")
    report_lines.append("| Metric | Value |")
    report_lines.append("|--------|-------|")
    report_lines.append(f"| Total prime hard cases found | {len(hard_cases)} |")
    report_lines.append(f"| Solutions found via u-method | {len(results)} |")
    report_lines.append(f"| Cases with no solution (search range 50,000) | {len(no_solution_cases)} |")
    report_lines.append(f"| Max u found | {max_u} |")
    report_lines.append(f"| Max u at n = | {max_u_n} |")
    report_lines.append(f"| Non-parametric cases (z/y not integer) | {len(non_parametric_cases)} |")
    report_lines.append(f"| Cases with u > 499 | {len(u_over_499)} |")
    report_lines.append("")
    
    if no_solution_cases:
        report_lines.append(f"### No-Solution Cases ({len(no_solution_cases)} total)")
        report_lines.append("")
        report_lines.append("These cases were not solved within the 50,000 x-value search range.")
        report_lines.append("")
        report_lines.append("| n |")
        report_lines.append("|---|")
        if len(no_solution_cases) <= 100:
            for n in no_solution_cases:
                report_lines.append(f"| {n} |")
        else:
            for n in no_solution_cases[:50]:
                report_lines.append(f"| {n} |")
            report_lines.append(f"| ... ({len(no_solution_cases) - 60} more) |")
            for n in no_solution_cases[-10:]:
                report_lines.append(f"| {n} |")
        report_lines.append("")
    
    report_lines.append("## Distribution of min u Values")
    report_lines.append("")
    report_lines.append("| u value | Count | Percentage |")
    report_lines.append("|---------|-------|------------|")
    
    total_cases = len(results)
    for u in sorted(u_distribution.keys()):
        count = u_distribution[u]
        pct = 100.0 * count / total_cases
        report_lines.append(f"| {u} | {count} | {pct:.1f}% |")
    report_lines.append(f"| **Total** | **{total_cases} | 100.0%** |")
    report_lines.append("")
    
    # Max u details
    report_lines.append("## Max u Details")
    report_lines.append("")
    if max_u_details:
        x, y, z, u, is_param = max_u_details
        report_lines.append(f"- **n** = {max_u_n}")
        report_lines.append(f"- **u** = {u}")
        report_lines.append(f"- **x** = {x}")
        report_lines.append(f"- **y** = {y}")
        report_lines.append(f"- **z** = {z}")
        report_lines.append(f"- **is_parametric** = {is_param}")
        lhs = 4 * x * y * z
        rhs = max_u_n * (y * z + x * z + x * y)
        report_lines.append(f"- **Verification:** 4·x·y·z = {lhs}, n·(y·z + x·z + x·y) = {rhs}, match = **{lhs == rhs}**")
    report_lines.append("")
    
    # Non-parametric cases
    report_lines.append("## Non-Parametric Cases (z/y is not integer)")
    report_lines.append("")
    report_lines.append(f"**Total non-parametric cases:** {len(non_parametric_cases)}")
    report_lines.append("")
    report_lines.append("| n | u | x | y | z | z mod y |")
    report_lines.append("|---|---|---|---|---|---------|")
    
    if len(non_parametric_cases) <= 60:
        for n_val, u_val, x_val, y_val, z_val, zmod in non_parametric_cases:
            report_lines.append(f"| {n_val} | {u_val} | {x_val} | {y_val} | {z_val} | {zmod} |")
    else:
        for n_val, u_val, x_val, y_val, z_val, zmod in non_parametric_cases[:50]:
            report_lines.append(f"| {n_val} | {u_val} | {x_val} | {y_val} | {z_val} | {zmod} |")
        report_lines.append(f"| ... | ... | ... | ... | ... | ... |")
        for n_val, u_val, x_val, y_val, z_val, zmod in non_parametric_cases[-10:]:
            report_lines.append(f"| {n_val} | {u_val} | {x_val} | {y_val} | {z_val} | {zmod} |")
    report_lines.append("")
    
    # Cases with u > 499
    report_lines.append("## Cases with u > 499")
    report_lines.append("")
    if u_over_499:
        report_lines.append("| n | u |")
        report_lines.append("|---|---|")
        for n_val, u_val in u_over_499:
            report_lines.append(f"| {n_val} | {u_val} |")
    else:
        report_lines.append("**None.** All prime hard cases in this range have u ≤ 499.")
    report_lines.append("")
    
    # No solution cases section
    report_lines.append("## Cases with No Solution")
    report_lines.append("")
    if no_solution_cases:
        report_lines.append(f"**WARNING:** {len(no_solution_cases)} cases had no solution found within 50,000 x-values!")
        report_lines.append("")
        report_lines.append(f"First 50 unsolved cases: {', '.join(str(n) for n in no_solution_cases[:50])}")
        report_lines.append("")
        report_lines.append(f"Last 10 unsolved cases: {', '.join(str(n) for n in no_solution_cases[-10:])}")
        report_lines.append("")
        report_lines.append("These may require a larger search range or a different method.")
    else:
        report_lines.append("**None.** All prime hard cases were solved within the search range.")
    report_lines.append("")
    
    # Comparison with 1M results
    report_lines.append("## Comparison with 1M Results")
    report_lines.append("")
    report_lines.append("| Metric | 1M Results (10,001–1,000,000) | 10M Results (1,000,001–10,000,000) |")
    report_lines.append("|--------|-------------------------------|--------------------------------------|")
    report_lines.append(f"| Total prime hard cases | 6,125 | {len(hard_cases)} |")
    report_lines.append(f"| Solutions found | 6,125 | {len(results)} |")
    report_lines.append(f"| No solution cases | 0 | {len(no_solution_cases)} |")
    report_lines.append(f"| Max u | 59 (n=118,801) | {max_u} (n={max_u_n}) |")
    report_lines.append(f"| Non-parametric cases | 763 | {len(non_parametric_cases)} |")
    report_lines.append(f"| Cases with u > 499 | 0 | {len(u_over_499)} |")
    report_lines.append("")
    
    # Key findings
    report_lines.append("## Key Findings")
    report_lines.append("")
    report_lines.append(f"1. **{len(hard_cases)} prime hard cases** found in the range 1,000,001–10,000,000.")
    if no_solution_cases:
        report_lines.append(f"2. **{len(no_solution_cases)} cases unsolved** within the 50,000 x-value search range (u up to 200,003).")
    else:
        report_lines.append(f"2. **All {len(hard_cases)} cases solved** by the u-method within the 50,000 x-value search range.")
    report_lines.append(f"3. **Maximum u = {max_u}** found at n = {max_u_n}.")
    if u_over_499:
        report_lines.append(f"4. **YES, {len(u_over_499)} cases have u > 499.**")
    else:
        report_lines.append(f"4. **NO case has u > 499** — all prime hard cases have u ≤ 499.")
    report_lines.append(f"5. **{len(non_parametric_cases)} non-parametric cases** found where z/y is not an integer.")
    report_lines.append("")
    report_lines.append("## Verification Timestamp")
    report_lines.append("")
    report_lines.append(f"**Completed:** 2026-08-14 (computation time: {total_time:.1f}s)")
    report_lines.append(f"**Search range:** 50,000 x-values per case (u up to 200,003)")
    report_lines.append(f"**Python:** {sys.version.split()[0]}")
    
    report_text = "\n".join(report_lines)
    
    output_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/PRIME_VERIFICATION_10M.md"
    with open(output_path, 'w') as f:
        f.write(report_text)
    
    print(f"\nReport written to: {output_path}", flush=True)
    print(f"\n{'=' * 70}", flush=True)
    print(f"SUMMARY", flush=True)
    print(f"{'=' * 70}", flush=True)
    print(f"Total prime hard cases: {len(hard_cases)}", flush=True)
    print(f"Solutions found: {len(results)}", flush=True)
    print(f"No solution: {len(no_solution_cases)}", flush=True)
    print(f"Max u: {max_u} (n={max_u_n})", flush=True)
    print(f"Non-parametric cases: {len(non_parametric_cases)}", flush=True)
    print(f"Cases with u > 499: {len(u_over_499)}", flush=True)
    print(f"Total time: {total_time:.1f}s", flush=True)
    
    # Save raw data as JSON
    json_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/prime_verification_10m.json"
    json_data = {
        'range': [1000001, 10000000],
        'total_cases': len(hard_cases),
        'solutions_found': len(results),
        'no_solution_cases': no_solution_cases,
        'max_u': max_u,
        'max_u_n': max_u_n,
        'non_parametric_count': len(non_parametric_cases),
        'u_over_499_count': len(u_over_499),
        'u_distribution': dict(u_distribution),
        'total_time': total_time,
        'results': results[:1000],
        'all_hard_cases': hard_cases,
    }
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=2)
    print(f"Raw data written to: {json_path}", flush=True)

if __name__ == "__main__":
    main()