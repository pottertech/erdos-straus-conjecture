#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Parametric (z=my) Verification to 10,000,000

For ALL hard cases (not just primes), verify that a parametric z=my solution
exists for some A ≡ 3 (mod 4) with A ≤ 107.

Tracks:
- Max parametric A found
- Cases where z=my fails but u-method succeeds (non-parametric)
- Cases where neither works (true failures)
- Distribution of min A values

This extends the 2M parametric check to 10M to match the u-method range.
"""

import math
import json
import time
import sys
from collections import Counter
import numpy as np

def sieve_primes_numpy(limit):
    """Sieve of Eratosthenes using numpy."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def is_prime(n, sieve):
    if n < len(sieve):
        return sieve[n]
    # Fallback for n > sieve limit (shouldn't happen here)
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Global small primes for trial division
small_primes_list = None

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

def factor_n(n, primes):
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

def omega(n, primes):
    """Count distinct prime factors of n."""
    count = 0
    temp = n
    for p in primes:
        if p * p > temp:
            break
        if temp % p == 0:
            count += 1
            while temp % p == 0:
                temp //= p
    if temp > 1:
        count += 1
    return count

def find_parametric_solution(n, max_A=107, small_primes=None):
    """
    Find a parametric (z=my) solution for hard case n.
    
    For each A ≡ 3 (mod 4), A ≤ max_A:
      x = (n + A) / 4  (must be integer, so n + A ≡ 0 mod 4)
      D = n * (n + A)  (for z=my: D = n(n+A), need divisor m | D with m ≡ -1 mod A)
      
    Actually, the z=my condition is:
      x = (n+A)/4, need A | (4x-n) trivially, then
      y = nx(m+1)/(Am), z = my
      Need m | (nx/A) and m ≡ -1 (mod A)
      
    Equivalent: D = n*(n+A), find divisor d of D with d ≡ -1 (mod A)
    and 2-adic constraint satisfied.
    
    Returns (A, x, y, z, m) or None if no parametric solution found.
    """
    for A in range(3, max_A + 1, 4):  # A ≡ 3 mod 4: 3, 7, 11, 15, 19, ...
        if (n + A) % 4 != 0:
            continue
        x = (n + A) // 4
        
        # For z=my: D = n*(n+A), need divisor m of D with m ≡ -1 (mod A)
        # and the 2-adic constraint: m odd or v2(m) <= v2(D) - 2
        D = n * (n + A)
        
        target = (A - 1) % A  # m ≡ -1 mod A
        
        # Factor D
        D_factors = factor_n(D, small_primes)
        divisors = gen_divisors_from_factors(D_factors)
        
        v2_D = D_factors.get(2, 0)
        
        for m in divisors:
            if m <= 0:
                continue
            if m % A != target:
                continue
            # 2-adic constraint
            v2_m = 0
            temp = m
            while temp % 2 == 0:
                v2_m += 1
                temp //= 2
            
            if v2_m > 0 and v2_D < 2:
                continue  # v2(m) > 0 but v2(D) < 2, constraint fails
            if v2_m > v2_D - 2 and v2_m > 0:
                continue  # v2(m) > v2(D) - 2
            
            # Check y is positive integer
            # y = nx(m+1) / (A*m)
            num = n * x * (m + 1)
            den = A * m
            if num % den != 0:
                continue
            y = num // den
            if y <= 0:
                continue
            
            z = m * y
            if z <= 0:
                continue
            
            # Verify: 4/n = 1/x + 1/y + 1/z
            lhs_num = 4 * x * y * z
            rhs_num = n * (y * z + x * z + x * y)
            if lhs_num == rhs_num:
                return (A, x, y, z, m)
    
    return None

def find_umethod_solution(n, max_A=107, small_primes=None):
    """
    Find a u-method solution (may be non-parametric) for hard case n.
    Uses the general u-method with D = n²x².
    
    Returns (A, x, y, z, u, is_parametric) or None.
    """
    for k in range(50000):
        x = n // 4 + 1 + k
        u = 4 * x - n
        if u <= 0 or u > 200003:
            continue
        
        nx = n * x
        D = nx * nx
        target = (-nx) % u
        
        # Check the 9 guaranteed divisors first
        sqrt_D = int(math.isqrt(D))
        
        for nf in [1, n, n*n]:
            for xf in [1, x, x*x]:
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
                    A = u  # u = 4x - n, and A ≡ u mod 4 (since n ≡ 1 mod 12, u ≡ 3 mod 4)
                    return (A, x, y, z, u, is_param)
        
        # Full divisor search on x²
        x_factors = factor_n(x, small_primes)
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
                    A = u
                    return (A, x, y, z, u, is_param)
    
    return None

def flush():
    sys.stdout.flush()

def main():
    global small_primes_list
    
    start_time = time.time()
    
    print("=" * 70, flush=True)
    print("Erdős-Straus Conjecture: Parametric Verification to 10,000,000", flush=True)
    print("Checking ALL hard cases (prime + composite) for z=my solutions", flush=True)
    print("Max A = 107", flush=True)
    print("=" * 70, flush=True)
    
    # Build prime sieve
    sieve_limit = 10000000
    print(f"\n[0/4] Building prime sieve up to {sieve_limit:,}...", flush=True)
    sieve_start = time.time()
    prime_sieve = sieve_primes_numpy(sieve_limit)
    sieve_time = time.time() - sieve_start
    prime_count = int(prime_sieve.sum())
    print(f"  Sieve built in {sieve_time:.1f}s ({prime_count:,} primes)", flush=True)
    
    # Small primes for trial division (up to sqrt(10M * (10M+107)) ≈ sqrt(1e14) ≈ 1e7)
    print("  Extracting small primes for trial division...", flush=True)
    sp_start = time.time()
    small_primes_list = [i for i in range(2, min(5000001, sieve_limit)) if prime_sieve[i]]
    sp_time = time.time() - sp_start
    print(f"  {len(small_primes_list):,} primes up to 5M extracted in {sp_time:.1f}s", flush=True)
    
    # Step 1: Find ALL hard cases (prime + composite) from 2 to 10M
    print("\n[1/4] Scanning for ALL hard cases (n ≡ 1 mod 12, n ≢ 0 mod 5, B3 condition)...", flush=True)
    hard_cases = []
    scan_start = time.time()
    
    n = 1  # n ≡ 1 mod 12 starts at 1, but n ≥ 2
    count_checked = 0
    while n <= 10000000:
        if n >= 2 and n % 5 != 0:
            count_checked += 1
            if check_B3_fast(n, small_primes_list):
                hard_cases.append(n)
        
        if count_checked % 500000 == 0:
            elapsed = time.time() - scan_start
            print(f"  Scanned to n={n:,} ({count_checked:,} candidates, {len(hard_cases)} hard cases, {elapsed:.1f}s)", flush=True)
        
        n += 12
    
    scan_time = time.time() - scan_start
    print(f"  Scan complete: {len(hard_cases)} total hard cases in {scan_time:.1f}s", flush=True)
    
    # Step 2: For each hard case, find parametric solution
    print(f"\n[2/4] Finding parametric (z=my) solutions for {len(hard_cases)} hard cases...", flush=True)
    solve_start = time.time()
    
    results = []
    param_A_dist = Counter()
    non_parametric = []  # Cases where z=my fails but u-method works
    total_failures = []  # Cases where neither works
    max_param_A = 0
    max_param_A_n = 0
    
    # Also track by omega
    omega_dist = Counter()
    omega_fail = Counter()
    
    for i, n in enumerate(hard_cases):
        if (i + 1) % 1000 == 0:
            elapsed = time.time() - solve_start
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (len(hard_cases) - i - 1) / rate if rate > 0 else 0
            print(f"  Solved {i+1}/{len(hard_cases)} ({elapsed:.1f}s, {rate:.1f}/s, ETA {eta:.0f}s, non_param={len(non_parametric)}, fail={len(total_failures)})", flush=True)
        
        # Try parametric first (z=my)
        param_result = find_parametric_solution(n, max_A=107, small_primes=small_primes_list)
        
        if param_result is not None:
            A, x, y, z, m = param_result
            results.append({
                'n': n,
                'A': A,
                'x': x,
                'y': y,
                'z': z,
                'm': m,
                'method': 'parametric'
            })
            param_A_dist[A] += 1
            if A > max_param_A:
                max_param_A = A
                max_param_A_n = n
        else:
            # Parametric failed — try u-method
            u_result = find_umethod_solution(n, max_A=107, small_primes=small_primes_list)
            if u_result is not None:
                A, x, y, z, u, is_param = u_result
                # This shouldn't be parametric since we already checked, but just in case
                if is_param:
                    results.append({
                        'n': n,
                        'A': A,
                        'x': x,
                        'y': y,
                        'z': z,
                        'm': z // y,
                        'method': 'parametric_via_umethod'
                    })
                    param_A_dist[A] += 1
                    if A > max_param_A:
                        max_param_A = A
                        max_param_A_n = n
                else:
                    non_parametric.append({
                        'n': n,
                        'A': A,
                        'x': x,
                        'y': y,
                        'z': z,
                        'u': u
                    })
                    results.append({
                        'n': n,
                        'A': A,
                        'x': x,
                        'y': y,
                        'z': z,
                        'method': 'non_parametric'
                    })
            else:
                total_failures.append(n)
                results.append({
                    'n': n,
                    'A': None,
                    'method': 'failed'
                })
    
    solve_time = time.time() - solve_start
    total_time = time.time() - start_time
    
    # Step 3: Generate report
    print(f"\n[3/4] Generating report...", flush=True)
    print(f"  Total time: {total_time:.1f}s", flush=True)
    print(f"  Total hard cases: {len(hard_cases)}", flush=True)
    print(f"  Parametric solutions: {sum(1 for r in results if r['method'].startswith('parametric'))}", flush=True)
    print(f"  Non-parametric (u-method only): {len(non_parametric)}", flush=True)
    print(f"  Total failures: {len(total_failures)}", flush=True)
    print(f"  Max parametric A: {max_param_A} (n={max_param_A_n})", flush=True)
    
    # Write markdown report
    report_lines = []
    report_lines.append("# Erdős-Straus Conjecture: Parametric Verification to 10,000,000")
    report_lines.append("")
    report_lines.append("## Overview")
    report_lines.append("")
    report_lines.append(f"**Date:** 2026-08-16")
    report_lines.append(f"**Range:** All hard cases from 2 to 10,000,000")
    report_lines.append(f"**Method:** Parametric z=my (A ≤ 107), then u-method fallback")
    report_lines.append(f"**Total computation time:** {total_time:.1f}s")
    report_lines.append("")
    report_lines.append("## Summary")
    report_lines.append("")
    report_lines.append(f"| Metric | Value |")
    report_lines.append(f"|--------|-------|")
    report_lines.append(f"| Total hard cases | {len(hard_cases)} |")
    param_count = sum(1 for r in results if r['method'].startswith('parametric'))
    report_lines.append(f"| Parametric (z=my) solutions | {param_count} ({100*param_count/len(hard_cases):.3f}%) |")
    report_lines.append(f"| Non-parametric (u-method only) | {len(non_parametric)} |")
    report_lines.append(f"| Total failures (neither works) | {len(total_failures)} |")
    report_lines.append(f"| Max parametric A | {max_param_A} (n={max_param_A_n}) |")
    report_lines.append(f"| Parametric coverage | {100*param_count/len(hard_cases):.4f}% |")
    report_lines.append("")
    
    # Distribution of parametric A values
    report_lines.append("## Distribution of Min Parametric A")
    report_lines.append("")
    report_lines.append("| A | Count | Percentage | Cumulative % |")
    report_lines.append("|---|-------|------------|--------------|")
    cumulative = 0
    for A in sorted(param_A_dist.keys()):
        count = param_A_dist[A]
        cumulative += count
        pct = 100.0 * count / param_count if param_count > 0 else 0
        cum_pct = 100.0 * cumulative / param_count if param_count > 0 else 0
        report_lines.append(f"| {A} | {count} | {pct:.2f}% | {cum_pct:.2f}% |")
    report_lines.append("")
    
    # Non-parametric cases
    report_lines.append(f"## Non-Parametric Cases (z=my fails, u-method succeeds)")
    report_lines.append("")
    report_lines.append(f"**Total:** {len(non_parametric)}")
    report_lines.append("")
    if non_parametric:
        report_lines.append("| n | A | u | x | z mod y |")
        report_lines.append("|---|---|---|---|---------|")
        for case in non_parametric[:100]:
            zmod = case['z'] % case['y']
            report_lines.append(f"| {case['n']} | {case['A']} | {case['u']} | {case['x']} | {zmod} |")
        if len(non_parametric) > 100:
            report_lines.append(f"| ... ({len(non_parametric) - 100} more) |")
    report_lines.append("")
    
    # Total failures
    report_lines.append("## Total Failures (neither parametric nor u-method)")
    report_lines.append("")
    if total_failures:
        report_lines.append(f"**{len(total_failures)} cases with no solution found!**")
        report_lines.append("")
        report_lines.append(f"Cases: {', '.join(str(n) for n in total_failures[:50])}")
    else:
        report_lines.append("**None.** All hard cases have a solution (parametric or u-method).")
    report_lines.append("")
    
    # Key findings
    report_lines.append("## Key Findings")
    report_lines.append("")
    report_lines.append(f"1. **{param_count}/{len(hard_cases)} hard cases ({100*param_count/len(hard_cases):.4f}%) have parametric z=my solutions** with A ≤ 107.")
    report_lines.append(f"2. **Max parametric A = {max_param_A}** at n = {max_param_A_n}.")
    report_lines.append(f"3. **{len(non_parametric)} cases** require non-parametric u-method solutions.")
    report_lines.append(f"4. **{len(total_failures)} total failures** (neither method works within A ≤ 107).")
    if max_param_A <= 19:
        report_lines.append(f"5. **Parametric A ≤ {max_param_A}** — consistent with the ω=2 bound of A ≤ 1.63·log(n).")
    else:
        report_lines.append(f"5. **Parametric A ≤ {max_param_A}** — note: exceeds previous max of 19, needs analysis.")
    report_lines.append("")
    report_lines.append(f"**Completed:** 2026-08-16 (computation time: {total_time:.1f}s)")
    
    report_text = "\n".join(report_lines)
    output_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/PARAMETRIC_VERIFICATION_10M.md"
    with open(output_path, 'w') as f:
        f.write(report_text)
    print(f"\nReport: {output_path}", flush=True)
    
    # Save JSON
    json_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/parametric_verification_10m.json"
    json_data = {
        'range': [2, 10000000],
        'max_A': 107,
        'total_hard_cases': len(hard_cases),
        'parametric_count': param_count,
        'non_parametric_count': len(non_parametric),
        'failure_count': len(total_failures),
        'max_parametric_A': max_param_A,
        'max_parametric_A_n': max_param_A_n,
        'param_A_distribution': dict(param_A_dist),
        'non_parametric_cases': non_parametric[:1000],
        'total_failures': total_failures,
        'total_time': total_time,
    }
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=2)
    print(f"JSON: {json_path}", flush=True)
    
    print(f"\n{'='*70}", flush=True)
    print(f"FINAL SUMMARY", flush=True)
    print(f"{'='*70}", flush=True)
    print(f"Hard cases: {len(hard_cases)}", flush=True)
    print(f"Parametric: {param_count} ({100*param_count/len(hard_cases):.4f}%)", flush=True)
    print(f"Non-parametric: {len(non_parametric)}", flush=True)
    print(f"Failures: {len(total_failures)}", flush=True)
    print(f"Max param A: {max_param_A} (n={max_param_A_n})", flush=True)
    print(f"Time: {total_time:.1f}s", flush=True)

if __name__ == "__main__":
    main()