#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Parametric (z=my) Verification to 10,000,000
Optimized v2: Fast B3 check using sieve-based factorization.

For ALL hard cases (prime + composite), verify that a parametric z=my solution
exists for some A ≡ 3 (mod 4) with A ≤ 107.
"""

import math
import json
import time
import sys
from collections import Counter
import numpy as np

def sieve_primes_numpy(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def smallest_prime_factor(n, sieve, sp_arr):
    """Find smallest odd prime factor of n using sieve lookup."""
    if n <= 1:
        return None
    # Check small primes directly from sieve
    limit = len(sieve)
    sqrt_n = int(math.isqrt(n)) + 1
    # Only check primes up to min(sqrt_n, len(sieve)-1)
    check_limit = min(sqrt_n, limit - 1)
    for p in range(3, check_limit + 1, 2):
        if sieve[p] and n % p == 0:
            return p
    # If n > sieve limit and no factor found, n might be prime or have a large factor
    if n > limit - 1:
        # Check remaining up to sqrt(n)
        for p in range(check_limit + 1 | 1, sqrt_n + 1, 2):
            if n % p == 0:
                return p
    return None  # n is prime (or 1)

def check_B3_sieve(n, sieve, sp_arr):
    """
    Check if all odd prime factors of B3 = n(n+3)/4 are ≡ 1 mod 3.
    Uses sieve for fast small-factor detection.
    """
    B3 = n * (n + 3) // 4
    temp = B3
    # Remove powers of 2
    while temp % 2 == 0:
        temp //= 2
    if temp == 1:
        return True
    
    # Factor temp using sieve
    while temp > 1:
        p = sp_arr[temp] if temp < len(sp_arr) else None
        if p is None:
            # temp is prime — check mod 3
            if temp % 3 != 1:
                return False
            break
        # p is smallest prime factor
        if p % 3 != 1 and p != 2:
            return False
        while temp % p == 0:
            temp //= p
    
    return True

def build_smallest_prime_array(limit):
    """Build array where sp[i] = smallest prime factor of i, for i up to limit."""
    sp = np.zeros(limit + 1, dtype=np.int32)
    for i in range(2, limit + 1):
        if sp[i] == 0:  # i is prime
            sp[i] = i
            if i <= int(math.isqrt(limit)):
                for j in range(i*i, limit + 1, i):
                    if sp[j] == 0:
                        sp[j] = i
    return sp

def factor_n(n, sp_arr, sieve):
    """Factor n using smallest prime factor array."""
    factors = {}
    temp = n
    while temp > 1:
        if temp < len(sp_arr):
            p = sp_arr[temp]
        else:
            # Find smallest factor by trial division
            p = None
            sqrt_t = int(math.isqrt(temp)) + 1
            for candidate in range(2, min(sqrt_t, len(sieve))):
                if sieve[candidate] and temp % candidate == 0:
                    p = candidate
                    break
            if p is None:
                # temp is prime
                p = temp
        if p is None or p == 0:
            p = temp  # temp is prime
        factors[p] = factors.get(p, 0) + 1
        temp //= p
    return factors

def gen_divisors_from_factors(factors):
    """Generate all divisors from prime factorization dict."""
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

def find_parametric_solution(n, max_A=107, sp_arr=None, sieve=None):
    """
    Find a parametric (z=my) solution for hard case n.
    
    For each A ≡ 3 (mod 4), A ≤ max_A:
      x = (n + A) / 4
      D = n * (n + A)
      Need divisor m of D with m ≡ -1 (mod A) and 2-adic constraint.
    
    Returns (A, x, y, z, m) or None.
    """
    for A in range(3, max_A + 1, 4):  # A = 3, 7, 11, 15, 19, ...
        if (n + A) % 4 != 0:
            continue
        x = (n + A) // 4
        D = n * (n + A)
        target = (A - 1) % A  # m ≡ -1 mod A
        
        D_factors = factor_n(D, sp_arr, sieve)
        divisors = gen_divisors_from_factors(D_factors)
        
        v2_D = D_factors.get(2, 0)
        
        for m in divisors:
            if m <= 0:
                continue
            if m % A != target:
                continue
            # 2-adic constraint: m odd or v2(m) <= v2(D) - 2
            v2_m = 0
            temp_m = m
            while temp_m % 2 == 0:
                v2_m += 1
                temp_m //= 2
            
            if v2_m > 0 and v2_D < 2:
                continue
            if v2_m > 0 and v2_m > v2_D - 2:
                continue
            
            # y = nx(m+1) / (A*m) — use Python big ints
            num = int(n) * int(x) * int(m + 1)
            den = int(A) * int(m)
            if num % den != 0:
                continue
            y = num // den
            if y <= 0:
                continue
            
            z = m * y
            if z <= 0:
                continue
            
            # Verify with big ints
            lhs = 4 * x * y * z
            rhs = n * (y * z + x * z + x * y)
            if lhs == rhs:
                return (A, x, y, z, m)
    
    return None

def find_umethod_solution(n, sp_arr=None, sieve=None):
    """
    Find a u-method solution (may be non-parametric).
    Returns (A, x, y, z, u, is_parametric) or None.
    All arithmetic uses Python native ints to avoid overflow.
    """
    n = int(n)  # ensure Python int
    for k in range(50000):
        x = n // 4 + 1 + k
        u = 4 * x - n
        if u <= 0 or u > 200003:
            continue
        
        nx = n * x  # Python big int
        D = nx * nx  # Python big int
        target = (-nx) % u
        sqrt_D = int(math.isqrt(D))
        
        # Check 9 guaranteed divisors first
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
                    return (u, x, y, z, u, is_param)
        
        # Full divisor search on x²
        x_factors = factor_n(x, sp_arr, sieve)
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
                    return (u, x, y, z, u, is_param)
    
    return None

def flush():
    sys.stdout.flush()

def main():
    start_time = time.time()
    
    print("=" * 70, flush=True)
    print("Erdős-Straus Conjecture: Parametric Verification to 10,000,000", flush=True)
    print("Checking ALL hard cases for z=my solutions (A ≤ 107)", flush=True)
    print("=" * 70, flush=True)
    
    sieve_limit = 10000000
    
    # Step 0: Build sieve and smallest prime factor array
    print(f"\n[0/4] Building prime sieve up to {sieve_limit:,}...", flush=True)
    t0 = time.time()
    sieve = sieve_primes_numpy(sieve_limit)
    print(f"  Sieve: {time.time()-t0:.1f}s ({int(sieve.sum()):,} primes)", flush=True)
    
    # Build smallest prime factor array up to 5M (for factoring D = n*(n+A) up to ~1e14)
    # Actually we need sp up to sqrt(D) ≈ 1e7, but that's too much memory for sp array
    # Use a compromise: sp up to 1M, then trial division for larger factors
    sp_limit = 2000000  # 2M should cover most factoring needs
    print(f"  Building smallest-prime-factor array up to {sp_limit:,}...", flush=True)
    t0 = time.time()
    sp_arr = build_smallest_prime_array(sp_limit)
    print(f"  SP array: {time.time()-t0:.1f}s", flush=True)
    
    # Step 1: Find all hard cases using FAST B3 check
    print("\n[1/4] Scanning for hard cases...", flush=True)
    scan_start = time.time()
    hard_cases = []
    count_checked = 0
    
    n = 1
    while n <= sieve_limit:
        if n >= 2 and n % 5 != 0:
            count_checked += 1
            if check_B3_sieve(n, sieve, sp_arr):
                hard_cases.append(n)
        
        if count_checked % 100000 == 0 and count_checked > 0:
            elapsed = time.time() - scan_start
            print(f"  n={n:,} ({count_checked:,} checked, {len(hard_cases)} hard, {elapsed:.1f}s)", flush=True)
        
        n += 12
    
    scan_time = time.time() - scan_start
    print(f"  Found {len(hard_cases)} hard cases in {scan_time:.1f}s", flush=True)
    
    # Step 2: Find parametric solutions
    print(f"\n[2/4] Solving {len(hard_cases)} hard cases (parametric first, u-method fallback)...", flush=True)
    solve_start = time.time()
    
    results = []
    param_A_dist = Counter()
    non_parametric = []
    total_failures = []
    max_param_A = 0
    max_param_A_n = 0
    
    for i, n in enumerate(hard_cases):
        if (i + 1) % 500 == 0:
            elapsed = time.time() - solve_start
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (len(hard_cases) - i - 1) / rate if rate > 0 else 0
            print(f"  {i+1}/{len(hard_cases)} ({elapsed:.1f}s, {rate:.1f}/s, ETA {eta:.0f}s, non_param={len(non_parametric)}, fail={len(total_failures)})", flush=True)
        
        # Try parametric (z=my) with A ≤ 107
        param_result = find_parametric_solution(n, max_A=107, sp_arr=sp_arr, sieve=sieve)
        
        if param_result is not None:
            A, x, y, z, m = param_result
            results.append({'n': n, 'A': A, 'method': 'parametric'})
            param_A_dist[A] += 1
            if A > max_param_A:
                max_param_A = A
                max_param_A_n = n
        else:
            # Parametric failed — try u-method
            u_result = find_umethod_solution(n, sp_arr=sp_arr, sieve=sieve)
            if u_result is not None:
                A, x, y, z, u, is_param = u_result
                if is_param:
                    results.append({'n': n, 'A': A, 'method': 'parametric_via_umethod'})
                    param_A_dist[A] += 1
                    if A > max_param_A:
                        max_param_A = A
                        max_param_A_n = n
                else:
                    non_parametric.append({'n': n, 'A': A, 'u': u, 'x': x, 'y': y, 'z': z})
                    results.append({'n': n, 'A': A, 'method': 'non_parametric'})
            else:
                total_failures.append(n)
                results.append({'n': n, 'A': None, 'method': 'failed'})
    
    solve_time = time.time() - solve_start
    total_time = time.time() - start_time
    
    # Step 3: Report
    param_count = sum(1 for r in results if r['method'].startswith('parametric'))
    
    print(f"\n[3/4] Report generation...", flush=True)
    print(f"  Total time: {total_time:.1f}s", flush=True)
    print(f"  Hard cases: {len(hard_cases)}", flush=True)
    print(f"  Parametric: {param_count} ({100*param_count/len(hard_cases):.4f}%)", flush=True)
    print(f"  Non-parametric: {len(non_parametric)}", flush=True)
    print(f"  Failures: {len(total_failures)}", flush=True)
    print(f"  Max param A: {max_param_A} (n={max_param_A_n})", flush=True)
    
    # Markdown report
    lines = []
    lines.append("# Erdős-Straus Conjecture: Parametric Verification to 10,000,000")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"**Date:** 2026-08-16")
    lines.append(f"**Range:** All hard cases from 2 to 10,000,000")
    lines.append(f"**Method:** Parametric z=my (A ≤ 107), then u-method fallback")
    lines.append(f"**Total computation time:** {total_time:.1f}s")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total hard cases | {len(hard_cases)} |")
    lines.append(f"| Parametric (z=my) solutions | {param_count} ({100*param_count/len(hard_cases):.4f}%) |")
    lines.append(f"| Non-parametric (u-method only) | {len(non_parametric)} |")
    lines.append(f"| Total failures | {len(total_failures)} |")
    lines.append(f"| Max parametric A | {max_param_A} (n={max_param_A_n}) |")
    lines.append("")
    
    lines.append("## Distribution of Min Parametric A")
    lines.append("")
    lines.append("| A | Count | Percentage | Cumulative % |")
    lines.append("|---|-------|------------|--------------|")
    cumulative = 0
    for A in sorted(param_A_dist.keys()):
        count = param_A_dist[A]
        cumulative += count
        pct = 100.0 * count / max(param_count, 1)
        cum_pct = 100.0 * cumulative / max(param_count, 1)
        lines.append(f"| {A} | {count} | {pct:.2f}% | {cum_pct:.2f}% |")
    lines.append("")
    
    lines.append(f"## Non-Parametric Cases")
    lines.append("")
    lines.append(f"**Total:** {len(non_parametric)}")
    lines.append("")
    if non_parametric:
        lines.append("| n | A | u | z mod y |")
        lines.append("|---|---|---|---------|")
        for c in non_parametric[:100]:
            lines.append(f"| {c['n']} | {c['A']} | {c['u']} | {c['z'] % c['y']} |")
        if len(non_parametric) > 100:
            lines.append(f"| ... ({len(non_parametric)-100} more) |")
    lines.append("")
    
    lines.append("## Failures")
    lines.append("")
    if total_failures:
        lines.append(f"**{len(total_failures)} cases with no solution!**")
        lines.append(f"Cases: {', '.join(str(n) for n in total_failures[:50])}")
    else:
        lines.append("**None.** All hard cases solved.")
    lines.append("")
    
    lines.append("## Key Findings")
    lines.append("")
    lines.append(f"1. **{param_count}/{len(hard_cases)} ({100*param_count/len(hard_cases):.4f}%)** have parametric z=my solutions with A ≤ 107.")
    lines.append(f"2. **Max parametric A = {max_param_A}** at n = {max_param_A_n}.")
    lines.append(f"3. **{len(non_parametric)}** non-parametric cases.")
    lines.append(f"4. **{len(total_failures)}** total failures.")
    lines.append("")
    lines.append(f"**Completed:** 2026-08-16 ({total_time:.1f}s)")
    
    report = "\n".join(lines)
    out = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/PARAMETRIC_VERIFICATION_10M.md"
    with open(out, 'w') as f:
        f.write(report)
    print(f"\nReport: {out}", flush=True)
    
    # JSON
    jpath = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/parametric_verification_10m.json"
    jdata = {
        'range': [2, 10000000], 'max_A': 107,
        'total_hard_cases': len(hard_cases),
        'parametric_count': param_count,
        'non_parametric_count': len(non_parametric),
        'failure_count': len(total_failures),
        'max_parametric_A': max_param_A,
        'max_parametric_A_n': max_param_A_n,
        'param_A_distribution': dict(param_A_dist),
        'non_parametric_cases': [{'n': c['n'], 'A': c['A'], 'u': c['u']} for c in non_parametric[:2000]],
        'total_failures': total_failures,
        'total_time': total_time,
    }
    with open(jpath, 'w') as f:
        json.dump(jdata, f, indent=2)
    print(f"JSON: {jpath}", flush=True)
    
    print(f"\n{'='*70}", flush=True)
    print(f"DONE: {param_count} param / {len(non_parametric)} non-param / {len(total_failures)} fail", flush=True)
    print(f"Max param A: {max_param_A} (n={max_param_A_n})", flush=True)
    print(f"Time: {total_time:.1f}s", flush=True)

if __name__ == "__main__":
    main()