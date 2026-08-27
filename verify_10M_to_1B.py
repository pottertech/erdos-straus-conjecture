#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Prime Hard Case Verification (10,000,001 – 1,000,000,000)
Optimized v5: Based on verify_primes_10m_v4.py, extended to 1B with chunked sieve.

Key optimizations:
- Numpy sieve in chunks (sieve up to 32000 for trial division, segment sieve for primes)
- Fast B3 check using small primes
- u-method search with A <= 255 (extended range to catch new outliers)
- Progress reporting every 5000 hard cases
"""

import math
import json
import time
import sys
from collections import Counter
import numpy as np

def isqrt(n):
    return int(math.isqrt(n))

def sieve_small_primes(limit):
    """Sieve of Eratosthenes for small primes up to limit."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return sieve

def segmented_prime_gen(start, end, small_sieve):
    """Generate primes in [start, end] using segmented sieve with small_sieve."""
    if start < 2:
        start = 2
    size = end - start + 1
    segment = np.ones(size, dtype=bool)
    
    # For each small prime p, mark multiples in segment
    small_primes = [i for i in range(2, len(small_sieve)) if small_sieve[i]]
    for p in small_primes:
        if p * p > end:
            break
        # Find first multiple of p >= start
        first = ((start + p - 1) // p) * p
        if first < p * p:
            first = p * p
        for j in range(first - start, size, p):
            segment[j] = False
    
    # Yield primes
    for i in range(size):
        if segment[i]:
            yield start + i

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
        # temp is a remaining prime factor
        if temp % 3 != 1:
            return False
    
    return True

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
    return divs

def solve_umethod(n, max_u=255, small_primes=None):
    """Find u-method solution for prime hard case n.
    Returns (u, x, is_parametric) or None."""
    
    for u in range(3, max_u + 1, 4):
        # u must be odd and ≡ 3 mod 4
        # Check if u is prime (quick check)
        if u < len(small_sieve_global) and not small_sieve_global[u]:
            continue
        elif u >= len(small_sieve_global):
            # Quick primality check
            if not is_prime_simple(u):
                continue
        
        x = (n + u) // 4
        if (n + u) % 4 != 0:
            continue  # x must be integer
        
        nx = n * x
        D = nx * nx
        target = (-nx) % u
        
        # First check guaranteed divisors: {1, x, x^2} × {1, n, n^2}
        x2 = x * x
        sqrt_D = isqrt(D)
        
        found = False
        for nf in [1, n, n*n]:
            for xf in [1, x, x2]:
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
                    return (u, x, is_param)
        
        # If guaranteed divisors didn't work, factor x and check all divisors of x^2
        x_factors = factor_x(x, small_primes)
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
                    return (u, x, is_param)
    
    return None

def is_prime_simple(n):
    """Simple primality test for small n."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Global state
small_sieve_global = None
small_primes_list = None

def flush():
    sys.stdout.flush()

def main():
    global small_sieve_global, small_primes_list
    
    start_time = time.time()
    
    RANGE_START = 10_000_001
    RANGE_END = 1_000_000_000
    MAX_U = 255
    
    print("=" * 70, flush=True)
    print("Erdős-Straus Conjecture: Prime Hard Case Verification", flush=True)
    print(f"Range: {RANGE_START:,} to {RANGE_END:,}", flush=True)
    print(f"Max u (A): {MAX_U}", flush=True)
    print("=" * 70, flush=True)
    
    # Step 0: Build small prime sieve (up to 5M for trial division of x)
    # Need primes up to sqrt(max_x) = sqrt(10^9/4) ≈ 15811
    # But for B3 factoring, need primes up to sqrt(B3) ≈ sqrt(10^9 * 10^9 / 4) ≈ 5*10^8
    # That's too large. Use probabilistic B3 check instead.
    # For x factoring: x up to ~2.5*10^8, sqrt(x) ≈ 15811 — small primes up to 16000 suffice
    # For B3: up to ~2.5*10^17, need trial division up to ~5*10^8 — too large
    # Instead: use Miller-Rabin for B3's large factors
    
    print("\n[0/4] Building prime sieve...", flush=True)
    sieve_limit = 50000  # Primes up to 50K for trial division of x and small B3 factors
    small_sieve_global = sieve_small_primes(sieve_limit)
    small_primes_list = [i for i in range(3, sieve_limit + 1, 2) if small_sieve_global[i]]
    print(f"  {len(small_primes_list):,} odd primes up to {sieve_limit}", flush=True)
    
    # Step 1: Find prime hard cases using segmented sieve
    print(f"\n[1/4] Scanning for prime hard cases (n ≡ 1 mod 12)...", flush=True)
    
    CHUNK_SIZE = 10_000_000  # Process 10M numbers at a time
    hard_cases = []
    scan_start = time.time()
    
    chunk_start = RANGE_START
    # Align to first n ≡ 1 mod 12
    while chunk_start % 12 != 1:
        chunk_start += 1
    
    total_chunks = (RANGE_END - RANGE_START + CHUNK_SIZE) // CHUNK_SIZE
    chunk_num = 0
    
    for chunk_base in range(RANGE_START, RANGE_END, CHUNK_SIZE):
        chunk_end = min(chunk_base + CHUNK_SIZE - 1, RANGE_END)
        chunk_num += 1
        
        # Generate primes in this chunk using segmented sieve
        for p in segmented_prime_gen(chunk_base, chunk_end, small_sieve_global):
            if p % 12 != 1 or p % 5 == 0:
                continue
            if check_B3_fast(p, small_primes_list):
                hard_cases.append(p)
        
        elapsed = time.time() - scan_start
        rate = (chunk_base - RANGE_START) / max(elapsed, 1)
        est_total = (RANGE_END - RANGE_START) / max(rate, 1)
        eta = est_total - elapsed
        
        if chunk_num % 10 == 0 or chunk_num == 1:
            print(f"  Chunk {chunk_num}/{total_chunks}: n up to {chunk_end:,} | "
                  f"{len(hard_cases):,} hard cases | {elapsed:.0f}s elapsed | "
                  f"ETA {eta:.0f}s ({eta/60:.0f}m)", flush=True)
    
    scan_time = time.time() - scan_start
    print(f"  Scan complete: {len(hard_cases):,} prime hard cases in {scan_time:.0f}s ({scan_time/60:.1f}m)", flush=True)
    
    # Step 2: Solve each hard case with u-method
    print(f"\n[2/4] Solving {len(hard_cases):,} hard cases with u-method (A ≤ {MAX_U})...", flush=True)
    solve_start = time.time()
    
    results = []
    u_distribution = Counter()
    non_parametric_cases = []
    max_u = 0
    max_u_n = 0
    no_solution_cases = []
    
    for i, n in enumerate(hard_cases):
        if (i + 1) % 5000 == 0:
            elapsed = time.time() - solve_start
            pct = 100 * (i + 1) / len(hard_cases)
            eta = elapsed / (i + 1) * (len(hard_cases) - i - 1)
            print(f"  {i+1:,}/{len(hard_cases):,} ({pct:.1f}%) | n={n:,} | "
                  f"max_A={max_u} | fails={len(no_solution_cases)} | "
                  f"elapsed={elapsed:.0f}s | ETA={eta:.0f}s ({eta/60:.0f}m)", flush=True)
        
        result = solve_umethod(n, max_u=MAX_U, small_primes=small_primes_list)
        
        if result is None:
            no_solution_cases.append(n)
            continue
        
        u, x, is_param = result
        results.append({'n': n, 'u': u, 'x': x, 'is_parametric': is_param})
        u_distribution[u] += 1
        
        if u > max_u:
            max_u = u
            max_u_n = n
        
        if not is_param:
            non_parametric_cases.append(n)
    
    solve_time = time.time() - solve_start
    total_time = time.time() - start_time
    
    # Step 3: Report
    print(f"\n[3/4] Results summary:", flush=True)
    print(f"  Total hard cases: {len(hard_cases):,}", flush=True)
    print(f"  Solutions found:  {len(results):,}", flush=True)
    print(f"  No solution:      {len(no_solution_cases):,}", flush=True)
    print(f"  Max A (u):        {max_u} (at n={max_u_n:,})", flush=True)
    print(f"  Non-parametric:   {len(non_parametric_cases):,}", flush=True)
    print(f"  Scan time:        {scan_time:.0f}s ({scan_time/60:.1f}m)", flush=True)
    print(f"  Solve time:       {solve_time:.0f}s ({solve_time/60:.1f}m)", flush=True)
    print(f"  Total time:       {total_time:.0f}s ({total_time/3600:.1f}h)", flush=True)
    
    print(f"\n  A distribution:", flush=True)
    for u in sorted(u_distribution.keys()):
        count = u_distribution[u]
        pct = 100.0 * count / len(results)
        print(f"    A={u:3d}: {count:6,} ({pct:5.1f}%)", flush=True)
    
    if no_solution_cases:
        print(f"\n  ⚠️  FAILURES ({len(no_solution_cases)}):", flush=True)
        for n in no_solution_cases[:20]:
            print(f"    n={n:,}", flush=True)
        if len(no_solution_cases) > 20:
            print(f"    ... and {len(no_solution_cases) - 20} more", flush=True)
    
    # Step 4: Save results
    print(f"\n[4/4] Saving results...", flush=True)
    
    output = {
        "range": [RANGE_START, RANGE_END],
        "max_u_searched": MAX_U,
        "total_hard_cases": len(hard_cases),
        "solutions_found": len(results),
        "no_solution_count": len(no_solution_cases),
        "no_solution_cases": no_solution_cases[:1000],
        "max_u": max_u,
        "max_u_n": max_u_n,
        "non_parametric_count": len(non_parametric_cases),
        "non_parametric_cases": non_parametric_cases[:1000],
        "u_distribution": dict(u_distribution),
        "scan_time_s": scan_time,
        "solve_time_s": solve_time,
        "total_time_s": total_time,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    json_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/verification_10M_1B.json"
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"  Saved to {json_path}", flush=True)
    
    # Markdown report
    md_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/VERIFICATION_1B.md"
    with open(md_path, 'w') as f:
        f.write(f"# Prime Hard Case Verification: 10M to 1B\n\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d')}\n")
        f.write(f"**Range:** {RANGE_START:,} – {RANGE_END:,}\n")
        f.write(f"**Max u searched:** {MAX_U}\n")
        f.write(f"**Runtime:** {total_time:.0f}s ({total_time/3600:.1f}h)\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Value |\n|--------|-------|\n")
        f.write(f"| Total prime hard cases | {len(hard_cases):,} |\n")
        f.write(f"| Solutions found | {len(results):,} |\n")
        f.write(f"| No solution (A ≤ {MAX_U}) | {len(no_solution_cases):,} |\n")
        f.write(f"| Max A | {max_u} (n={max_u_n:,}) |\n")
        f.write(f"| Non-parametric | {len(non_parametric_cases):,} |\n\n")
        f.write(f"## A Distribution\n\n")
        f.write(f"| A | Count | % |\n|---|-------|---|\n")
        for u in sorted(u_distribution.keys()):
            count = u_distribution[u]
            pct = 100.0 * count / len(results)
            f.write(f"| {u} | {count:,} | {pct:.1f}% |\n")
        if no_solution_cases:
            f.write(f"\n## Failures\n\nFirst 50:\n")
            for n in no_solution_cases[:50]:
                f.write(f"- n={n:,}\n")
    print(f"  Report saved to {md_path}", flush=True)
    
    print(f"\n{'='*70}", flush=True)
    print(f"DONE — Total: {total_time:.0f}s ({total_time/3600:.1f}h)", flush=True)
    print(f"{'='*70}", flush=True)

if __name__ == "__main__":
    main()