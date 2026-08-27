#!/usr/bin/env python3
"""
Problem 3: Failure mechanism analysis for ω=2 hard cases.

For each ω=2 hard case that needs A > log(n), analyze WHY small A values fail:
1. All-QR obstruction (all prime factors of D = n(n+A) are QR mod A)
2. Bounded subset sum (QNR factors exist but can't reach target exponent)
3. No divisor matching (no divisor of D ≡ -1 mod A at all)

This reveals the mechanism behind the A/log(n) ratio.
"""

import math
import json
import time
import sys
from collections import Counter, defaultdict
from sympy import factorint, isprime, divisors, legendre_symbol, primitive_root, discrete_log

def build_spf(limit):
    """Build smallest-prime-factor array up to limit using linear sieve."""
    spf = [0] * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > limit:
                break
            spf[i * p] = p
    return spf, primes

def compute_omega_sieve(limit, spf):
    omega = [0] * (limit + 1)
    for i in range(2, limit + 1):
        p = spf[i]
        if p == i:
            omega[i] = 1
        else:
            m = i // p
            if m % p == 0:
                omega[i] = omega[m]
            else:
                omega[i] = omega[m] + 1
    return omega

def sieve_primes(limit):
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = 0
    return is_prime

def find_hard_cases_sieve(limit, is_prime_arr):
    is_hard = bytearray(b'\x00') * (limit + 1)
    n = 1
    while n <= limit:
        if n >= 2:
            is_hard[n] = 1
        n += 12
    n = 1
    while n <= limit:
        if n % 5 == 0 and n >= 2:
            is_hard[n] = 0
        n += 12
    for p in range(5, limit + 1):
        if p > limit or not is_prime_arr[p] or p % 3 != 2:
            continue
        inv12 = pow(12, -1, p) if math.gcd(12, p) == 1 else None
        if inv12 is not None:
            k0 = ((-1) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2: n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p):
                is_hard[n] = 0
            k0 = ((p - 4) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2: n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p):
                is_hard[n] = 0
    return [n for n in range(2, limit + 1) if is_hard[n]]

def classify_failure(n, A, spf):
    """
    Classify why A fails for n.
    Returns: 'all_qr', 'no_divisor', 'subset_sum', 'v2_fail', or 'works'
    """
    if (n + A) % 4 != 0:
        return 'congruence_fail'
    
    x = (n + A) // 4
    D = n * (n + A)
    
    D_factors = factorint(D)
    v2_D = D_factors.get(2, 0)
    
    # Check if any divisor of D ≡ -1 mod A
    target = A - 1
    divs = divisors(D)
    
    has_matching = False
    for m in divs:
        if m % A == target:
            has_matching = True
            v2_m = 0
            tm = m
            while tm % 2 == 0:
                v2_m += 1
                tm //= 2
            if v2_m > 0 and v2_D < 2:
                continue
            if v2_m > 0 and v2_m > v2_D - 2:
                continue
            num = n * x * (m + 1)
            den = A * m
            if num % den != 0:
                continue
            y = num // den
            if y > 0:
                z = m * y
                if z > 0 and 4*x*y*z == n*(y*z + x*z + x*y):
                    return 'works'
    
    if not has_matching:
        # No divisor of D ≡ -1 mod A
        # Check if all prime factors are QR mod A (if A is prime)
        if isprime(A):
            all_qr = True
            for p in D_factors:
                if p == 2:
                    continue
                if p == A:
                    continue
                ls = int(legendre_symbol(p, A))
                if ls == -1:
                    all_qr = False
                    break
            if all_qr:
                return 'all_qr'  # All primes QR → -1 unreachable as product
            else:
                return 'subset_sum'  # QNR exists but can't form -1
        else:
            return 'no_divisor_composite'
    
    # Has matching divisors but none satisfy all conditions
    return 'condition_fail'

def analyze_case(n, spf):
    """Analyze all A values up to the first success for n."""
    log_n = math.log(n)
    results = []
    
    for A in range(3, 200, 4):
        if (n + A) % 4 != 0:
            continue
        status = classify_failure(n, A, spf)
        results.append({'A': A, 'status': status, 'ratio': A / log_n})
        if status == 'works':
            break
    
    return results

def main():
    start = time.time()
    limit = 10_000_000
    
    print("=" * 70, flush=True)
    print("Problem 3: Failure Mechanism Analysis for ω=2", flush=True)
    print("=" * 70, flush=True)
    
    # Build sieves
    print(f"\n[1/4] Building sieves...", flush=True)
    spf, primes = build_spf(limit)
    is_prime_arr = bytearray(b'\x00') * (limit + 1)
    for p in primes:
        is_prime_arr[p] = 1
    omega = compute_omega_sieve(limit, spf)
    hard_cases = find_hard_cases_sieve(limit, is_prime_arr)
    omega2_cases = [n for n in hard_cases if omega[n] == 2]
    print(f"  {len(omega2_cases)} ω=2 hard cases", flush=True)
    
    # Analyze failures for all ω=2 cases
    print(f"\n[2/4] Analyzing failure mechanisms...", flush=True)
    t0 = time.time()
    
    # Collect statistics
    failure_types = Counter()
    failure_by_A = defaultdict(Counter)  # A -> {failure_type: count}
    consecutive_failures = []
    
    # For trend analysis
    high_ratio_cases = []  # A/log(n) > 1
    all_first_A = Counter()
    
    for i, n in enumerate(omega2_cases):
        if (i + 1) % 500 == 0:
            el = time.time() - t0
            rate = (i + 1) / el if el > 0 else 0
            eta = (len(omega2_cases) - i - 1) / rate if rate > 0 else 0
            print(f"  {i+1}/{len(omega2_cases)} ({el:.0f}s, {rate:.1f}/s, ETA {eta:.0f}s)", flush=True)
        
        log_n = math.log(n)
        failures_before_success = 0
        
        for A in range(3, 200, 4):
            if (n + A) % 4 != 0:
                continue
            status = classify_failure(n, A, spf)
            if status == 'works':
                all_first_A[A] += 1
                ratio = A / log_n
                if ratio > 1.0:
                    high_ratio_cases.append({
                        'n': n, 'A': A, 'ratio': ratio,
                        'failures': failures_before_success,
                    })
                consecutive_failures.append(failures_before_success)
                break
            else:
                failure_types[status] += 1
                failure_by_A[A][status] += 1
                failures_before_success += 1
    
    analyze_time = time.time() - t0
    
    # Report
    print(f"\n[3/4] Results (analysis time: {analyze_time:.0f}s):", flush=True)
    
    print(f"\n  Failure type distribution:", flush=True)
    total_failures = sum(failure_types.values())
    for ft, count in failure_types.most_common():
        pct = 100 * count / total_failures
        print(f"    {ft:25s}: {count:6d} ({pct:5.2f}%)", flush=True)
    
    print(f"\n  First-success A distribution:", flush=True)
    total_cases = sum(all_first_A.values())
    for A in sorted(all_first_A.keys()):
        count = all_first_A[A]
        pct = 100 * count / total_cases
        cum = sum(all_first_A[a] for a in sorted(all_first_A.keys()) if a <= A)
        cum_pct = 100 * cum / total_cases
        print(f"    A={A:3d}: {count:6d} ({pct:5.2f}%)  cum: {cum_pct:5.2f}%", flush=True)
    
    print(f"\n  Consecutive failures before success:", flush=True)
    cf_counter = Counter(consecutive_failures)
    for nf in sorted(cf_counter.keys()):
        count = cf_counter[nf]
        pct = 100 * count / len(consecutive_failures)
        print(f"    {nf:3d} failures: {count:6d} ({pct:5.2f}%)", flush=True)
    
    print(f"\n  Cases with A/log(n) > 1.0: {len(high_ratio_cases)} ({100*len(high_ratio_cases)/total_cases:.2f}%)", flush=True)
    print(f"  Cases with A/log(n) > 1.5: {sum(1 for c in high_ratio_cases if c['ratio'] > 1.5)}", flush=True)
    print(f"  Cases with A/log(n) > 2.0: {sum(1 for c in high_ratio_cases if c['ratio'] > 2.0)}", flush=True)
    
    # Failure breakdown by A value
    print(f"\n  Failure breakdown by A value (top 10):", flush=True)
    for A in sorted(failure_by_A.keys())[:10]:
        ft_counts = failure_by_A[A]
        total_A = sum(ft_counts.values())
        print(f"    A={A:3d} ({total_A:5d} failures): ", end='', flush=True)
        parts = []
        for ft, c in ft_counts.most_common():
            parts.append(f"{ft}={c}")
        print(', '.join(parts), flush=True)
    
    # Per-u failure probability
    print(f"\n  Per-A failure probability (prime A only):", flush=True)
    for A in sorted(failure_by_A.keys()):
        if not isprime(A):
            continue
        ft_counts = failure_by_A[A]
        total_A = sum(ft_counts.values())
        success_A = all_first_A.get(A, 0)
        total_attempted = total_A + success_A
        if total_attempted > 0:
            fail_prob = total_A / total_attempted
            all_qr_count = ft_counts.get('all_qr', 0)
            ss_count = ft_counts.get('subset_sum', 0)
            print(f"    A={A:3d}: fail_prob={fail_prob:.4f} (all_qr={all_qr_count}, subset_sum={ss_count}, success={success_A})", flush=True)
    
    # Save
    print(f"\n[4/4] Saving...", flush=True)
    jpath = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/problem3_failure_analysis.json"
    with open(jpath, 'w') as f:
        json.dump({
            'failure_types': dict(failure_types),
            'first_A_distribution': dict(all_first_A),
            'consecutive_failures_dist': dict(cf_counter),
            'high_ratio_cases': high_ratio_cases[:200],
            'failure_by_A': {str(k): dict(v) for k, v in failure_by_A.items()},
            'total_cases': total_cases,
            'analyze_time': analyze_time,
        }, f, indent=2)
    print(f"  JSON: {jpath}", flush=True)
    
    total_time = time.time() - start
    print(f"\nDONE in {total_time:.0f}s", flush=True)

if __name__ == "__main__":
    main()