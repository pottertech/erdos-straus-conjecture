#!/usr/bin/env python3
"""
Problem 3: Focused failure analysis for ω=2 hard cases with A/log(n) > 1.
Plus per-A failure probability estimation from a sample.
"""

import math
import json
import time
import sys
from collections import Counter, defaultdict
from sympy import factorint, isprime, divisors, legendre_symbol

def build_spf(limit):
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

def sieve_primes_bytearray(limit):
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
        if n >= 2: is_hard[n] = 1
        n += 12
    n = 1
    while n <= limit:
        if n % 5 == 0 and n >= 2: is_hard[n] = 0
        n += 12
    for p in range(5, limit + 1):
        if not is_prime_arr[p] or p % 3 != 2: continue
        inv12 = pow(12, -1, p) if math.gcd(12, p) == 1 else None
        if inv12 is not None:
            k0 = ((-1) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2: n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p): is_hard[n] = 0
            k0 = ((p - 4) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2: n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p): is_hard[n] = 0
    return [n for n in range(2, limit + 1) if is_hard[n]]

def classify_failure_detailed(n, A):
    """Classify why A fails for n. Returns detailed failure info."""
    if (n + A) % 4 != 0:
        return {'status': 'congruence_fail'}
    
    x = (n + A) // 4
    D = n * (n + A)
    
    D_factors = factorint(D)
    v2_D = D_factors.get(2, 0)
    target = A - 1
    
    # Check QR status of each prime factor mod A (if A is prime)
    qr_info = {}
    if isprime(A):
        for p in D_factors:
            if p == 2:
                qr_info[p] = 'QR' if A % 8 in [1, 7] else 'QNR'
            elif p == A:
                qr_info[p] = 'zero'
            else:
                ls = int(legendre_symbol(p, A))
                qr_info[p] = 'QR' if ls == 1 else 'QNR'
    
    # Check for matching divisors
    has_matching = False
    has_passing = False
    for m in divisors(D):
        if m % A == target:
            has_matching = True
            v2_m = 0
            tm = m
            while tm % 2 == 0:
                v2_m += 1
                tm //= 2
            if v2_m > 0 and v2_D < 2: continue
            if v2_m > 0 and v2_m > v2_D - 2: continue
            num = n * x * (m + 1)
            den = A * m
            if num % den != 0: continue
            y = num // den
            if y > 0:
                z = m * y
                if z > 0 and 4*x*y*z == n*(y*z + x*z + x*y):
                    has_passing = True
                    break
    
    if has_passing:
        return {'status': 'works'}
    
    all_qr = False
    if isprime(A) and qr_info:
        all_qr = all(v == 'QR' for v in qr_info.values() if v != 'zero')
    
    if not has_matching:
        if all_qr:
            return {'status': 'all_qr', 'qr_info': qr_info, 'D_factors': D_factors}
        elif isprime(A):
            return {'status': 'no_divisor_qnr_exists', 'qr_info': qr_info, 'D_factors': D_factors}
        else:
            return {'status': 'no_divisor_composite', 'D_factors': D_factors}
    
    return {'status': 'condition_fail', 'qr_info': qr_info, 'D_factors': D_factors}

def main():
    start = time.time()
    limit = 10_000_000
    
    print("=" * 70, flush=True)
    print("Problem 3: Focused Failure Analysis", flush=True)
    print("=" * 70, flush=True)
    
    # Load measurement results
    with open("/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/problem3_omega2_measurement.json") as f:
        data = json.load(f)
    
    all_results = data['all_results']
    high_ratio = [r for r in all_results if r['ratio'] > 1.0]
    print(f"\nLoaded {len(all_results)} ω=2 cases, {len(high_ratio)} with A/log(n) > 1.0", flush=True)
    
    # Build sieves for hard case finding (needed for per-A probability)
    print(f"\n[1/3] Building sieves...", flush=True)
    spf, primes = build_spf(limit)
    is_prime_arr = sieve_primes_bytearray(limit)
    omega = compute_omega_sieve(limit, spf)
    hard_cases = find_hard_cases_sieve(limit, is_prime_arr)
    omega2_cases = [n for n in hard_cases if omega[n] == 2]
    print(f"  {len(omega2_cases)} ω=2 hard cases", flush=True)
    
    # Analyze high-ratio cases in detail
    print(f"\n[2/3] Detailed analysis of {len(high_ratio)} high-ratio cases...", flush=True)
    t0 = time.time()
    
    # Map n -> result for quick lookup
    n_to_result = {r['n']: r for r in all_results}
    
    detailed = []
    for i, r in enumerate(high_ratio):
        if (i + 1) % 50 == 0:
            print(f"  {i+1}/{len(high_ratio)} ({time.time()-t0:.0f}s)", flush=True)
        
        n = r['n']
        A_final = r['A']
        log_n = math.log(n)
        
        # Analyze each failed A
        failure_chain = []
        for A in range(3, A_final, 4):
            if (n + A) % 4 != 0: continue
            info = classify_failure_detailed(n, A)
            if info['status'] != 'works':
                failure_chain.append({
                    'A': A,
                    'status': info['status'],
                    'qr_info': info.get('qr_info', {}),
                    'D_factors': {str(k): v for k, v in info.get('D_factors', {}).items()},
                })
        
        detailed.append({
            'n': n,
            'A_final': A_final,
            'ratio': r['ratio'],
            'failures': len(failure_chain),
            'failure_chain': failure_chain,
        })
    
    print(f"  Analysis time: {time.time()-t0:.0f}s", flush=True)
    
    # Aggregate failure statistics from high-ratio cases
    failure_types = Counter()
    for case in detailed:
        for f in case['failure_chain']:
            failure_types[f['status']] += 1
    
    print(f"\n  Failure types in high-ratio cases (A/log(n) > 1):", flush=True)
    total_f = sum(failure_types.values())
    for ft, count in failure_types.most_common():
        print(f"    {ft:30s}: {count:5d} ({100*count/total_f:.1f}%)", flush=True)
    
    # Per-A failure probability from ALL ω=2 cases (sample if too many)
    print(f"\n[3/3] Per-A failure probability (all ω=2 cases)...", flush=True)
    t0 = time.time()
    
    # For each prime A ≡ 3 mod 4 up to 50, count failures vs successes
    prime_A_values = [A for A in range(3, 50, 4) if isprime(A)]
    per_A_stats = {}
    
    for A in prime_A_values:
        stats = {'total': 0, 'works': 0, 'all_qr': 0, 'no_divisor_qnr': 0, 
                 'condition_fail': 0, 'no_divisor_composite': 0, 'congruence_fail': 0}
        
        for n in omega2_cases:
            if (n + A) % 4 != 0:
                stats['congruence_fail'] += 1
                stats['total'] += 1
                continue
            
            stats['total'] += 1
            info = classify_failure_detailed(n, A)
            status = info['status']
            if status == 'works':
                stats['works'] += 1
            elif status == 'all_qr':
                stats['all_qr'] += 1
            elif status == 'no_divisor_qnr_exists':
                stats['no_divisor_qnr'] += 1
            elif status == 'condition_fail':
                stats['condition_fail'] += 1
            elif status == 'no_divisor_composite':
                stats['no_divisor_composite'] += 1
        
        per_A_stats[A] = stats
        fail_prob = 1 - stats['works'] / max(stats['total'] - stats['congruence_fail'], 1)
        all_qr_frac = stats['all_qr'] / max(stats['total'] - stats['congruence_fail'], 1)
        print(f"  A={A:3d}: {stats['total']:6d} attempted, {stats['works']:5d} works ({100*stats['works']/max(stats['total'],1):.1f}%), "
              f"fail_prob={fail_prob:.4f}, all_qr={100*all_qr_frac:.1f}%, no_div_qnr={stats['no_divisor_qnr']}", flush=True)
    
    # Save
    print(f"\nSaving...", flush=True)
    jpath = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/problem3_failure_analysis.json"
    with open(jpath, 'w') as f:
        json.dump({
            'high_ratio_case_count': len(high_ratio),
            'failure_types_high_ratio': dict(failure_types),
            'per_A_stats': {str(k): v for k, v in per_A_stats.items()},
            'detailed_cases': detailed[:100],  # top 100
            'analyze_time': time.time() - t0,
        }, f, indent=2)
    print(f"  JSON: {jpath}", flush=True)
    
    total_time = time.time() - start
    print(f"\nDONE in {total_time:.0f}s", flush=True)

if __name__ == "__main__":
    main()