#!/usr/bin/env python3
"""
Problem 3: Measure A/log(n) for ALL ω=2 hard cases up to 10,000,000.
v2: Optimized with ω(n) sieve and faster parametric search.

Key optimizations:
- Precompute ω(n) (number of distinct prime factors) via sieve for ALL n ≤ 10M
- Use SPF (smallest prime factor) array for fast factoring
- Only run parametric solver on the ω=2 hard cases (~35K cases)
"""

import math
import json
import time
import sys
from collections import Counter, defaultdict

# ---------------------------------------------------------------------------
# Sieves
# ---------------------------------------------------------------------------

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
    """Compute ω(n) (number of distinct prime factors) for all n up to limit."""
    omega = [0] * (limit + 1)
    for i in range(2, limit + 1):
        p = spf[i]
        if p == i:  # prime
            omega[i] = 1
        else:
            # ω(n) = ω(n/p) + 1 if p doesn't divide n/p, else ω(n/p)
            m = i // p
            if m % p == 0:
                omega[i] = omega[m]
            else:
                omega[i] = omega[m] + 1
    return omega

def find_hard_cases_sieve(limit, is_prime_arr):
    """
    Find all hard cases up to limit using a sieve approach.
    Hard case: n ≡ 1 mod 12, n ≢ 0 mod 5, and no prime p ≡ 2 mod 3 (p ≥ 5)
    divides n or (n+3).
    """
    is_hard = bytearray(b'\x00') * (limit + 1)
    n = 1
    while n <= limit:
        if n >= 2:
            is_hard[n] = 1
        n += 12

    # Remove n ≡ 0 mod 5
    n = 1
    while n <= limit:
        if n % 5 == 0 and n >= 2:
            is_hard[n] = 0
        n += 12

    for p in range(5, limit + 1):
        if p > limit:
            break
        if not is_prime_arr[p]:
            continue
        if p % 3 != 2:
            continue

        inv12 = pow(12, -1, p) if math.gcd(12, p) == 1 else None
        if inv12 is not None:
            # Mark n ≡ 0 mod p
            k0 = ((-1) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2:
                n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p):
                is_hard[n] = 0

            # Mark n ≡ (p-3) mod p (p | (n+3))
            k0 = ((p - 4) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2:
                n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p):
                is_hard[n] = 0

    hard_cases = [n for n in range(2, limit + 1) if is_hard[n]]
    return hard_cases

# ---------------------------------------------------------------------------
# Factoring and divisors
# ---------------------------------------------------------------------------

def factorize(n, spf):
    """Factor n using SPF array. Returns dict {prime: exponent}."""
    factors = {}
    temp = int(n)
    while temp > 1:
        if temp < len(spf) and spf[temp] > 0:
            p = int(spf[temp])
        else:
            # Trial division for factors beyond SPF range
            p = None
            sqrt_t = int(math.isqrt(temp)) + 1
            for c in range(2, min(sqrt_t + 1, len(spf))):
                if spf[c] == c and temp % c == 0:
                    p = c
                    break
            if p is None:
                for c in range(len(spf) | 1, sqrt_t + 1, 2):
                    if temp % c == 0:
                        p = c
                        break
            if p is None:
                p = temp
        factors[p] = factors.get(p, 0) + 1
        temp //= p
    return factors

def gen_divisors(factors):
    """Generate all divisors from factorization."""
    divs = [1]
    for p, e in factors.items():
        new_divs = []
        pe = 1
        for _ in range(e + 1):
            for d in divs:
                new_divs.append(d * pe)
            pe *= p
        divs = new_divs
    divs.sort()
    return divs

# ---------------------------------------------------------------------------
# Parametric solver (optimized)
# ---------------------------------------------------------------------------

def find_parametric_A(n, max_A=200, spf=None):
    """Find minimum parametric z=my A for n. Returns A or None."""
    n = int(n)
    for A in range(3, max_A + 1, 4):
        if (n + A) % 4 != 0:
            continue
        x = (n + A) // 4
        D = n * (n + A)
        target = A - 1  # m ≡ -1 mod A

        D_factors = factorize(D, spf)
        divisors = gen_divisors(D_factors)
        v2_D = D_factors.get(2, 0)

        for m in divisors:
            if m % A != target:
                continue
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
                if z > 0 and 4 * x * y * z == n * (y * z + x * z + x * y):
                    return A
    return None

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    start = time.time()

    print("=" * 70, flush=True)
    print("Problem 3: ω=2 A/log(n) Measurement to 10M (v2 optimized)", flush=True)
    print("=" * 70, flush=True)

    limit = 10_000_000

    # Build SPF and prime sieve
    print(f"\n[1/6] Building SPF up to {limit:,}...", flush=True)
    t0 = time.time()
    spf, primes = build_spf(limit)
    spf_time = time.time() - t0
    print(f"  SPF: {spf_time:.1f}s, {len(primes)} primes", flush=True)

    # Build is_prime bytearray for hard case sieve
    is_prime_arr = bytearray(b'\x00') * (limit + 1)
    for p in primes:
        is_prime_arr[p] = 1

    # Compute ω(n) for all n
    print(f"\n[2/6] Computing ω(n) sieve...", flush=True)
    t0 = time.time()
    omega = compute_omega_sieve(limit, spf)
    omega_time = time.time() - t0
    print(f"  ω sieve: {omega_time:.1f}s", flush=True)

    # Find hard cases
    print(f"\n[3/6] Sieving for hard cases up to {limit:,}...", flush=True)
    t0 = time.time()
    hard_cases = find_hard_cases_sieve(limit, is_prime_arr)
    hard_time = time.time() - t0
    print(f"  Found {len(hard_cases)} hard cases in {hard_time:.1f}s", flush=True)

    # Filter to ω=2
    omega2_cases = [n for n in hard_cases if omega[n] == 2]
    print(f"  ω=2 cases: {len(omega2_cases)}", flush=True)

    # Compute parametric A for each ω=2 case
    print(f"\n[4/6] Computing parametric A for {len(omega2_cases)} ω=2 cases...", flush=True)
    t0 = time.time()

    results = []
    A_distribution = Counter()
    ratio_hist = Counter()  # 0.1-width buckets

    range_stats = {
        'le_100K': {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
        '100K_1M': {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
        '1M_10M':  {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
        'total':   {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
    }

    for i, n in enumerate(omega2_cases):
        if (i + 1) % 500 == 0:
            el = time.time() - t0
            rate = (i + 1) / el if el > 0 else 0
            eta = (len(omega2_cases) - i - 1) / rate if rate > 0 else 0
            print(f"  {i+1}/{len(omega2_cases)} ({el:.0f}s, {rate:.1f}/s, ETA {eta:.0f}s)", flush=True)

        A = find_parametric_A(n, max_A=200, spf=spf)
        if A is None:
            print(f"  WARNING: No parametric solution for n={n} (ω=2) with A≤200", flush=True)
            continue

        log_n = math.log(n)
        ratio = A / log_n

        results.append({'n': n, 'A': A, 'log_n': log_n, 'ratio': ratio})
        A_distribution[A] += 1
        bucket = round(ratio, 1)
        ratio_hist[bucket] += 1

        if n <= 100_000:
            r = 'le_100K'
        elif n <= 1_000_000:
            r = '100K_1M'
        else:
            r = '1M_10M'

        for key in [r, 'total']:
            s = range_stats[key]
            s['count'] += 1
            s['max_A'] = max(s['max_A'], A)
            if ratio > s['max_ratio']:
                s['max_ratio'] = ratio
                s['max_ratio_n'] = n
            s['sum_ratio'] += ratio

    compute_time = time.time() - t0

    # Statistics
    print(f"\n[5/6] Computing statistics...", flush=True)

    total_count = len(results)
    all_ratios = [r['ratio'] for r in results]
    all_ratios.sort()

    def percentile(sorted_list, p):
        if not sorted_list:
            return 0
        idx = min(int(len(sorted_list) * p), len(sorted_list) - 1)
        return sorted_list[idx]

    stats = {
        'total_omega2_cases': total_count,
        'max_A': max(r['A'] for r in results) if results else 0,
        'max_A_n': max(results, key=lambda r: r['A'])['n'] if results else 0,
        'max_ratio': max(r['ratio'] for r in results) if results else 0,
        'max_ratio_n': max(results, key=lambda r: r['ratio'])['n'] if results else 0,
        'mean_ratio': sum(all_ratios) / len(all_ratios) if all_ratios else 0,
        'median_ratio': percentile(all_ratios, 0.5),
        'p95_ratio': percentile(all_ratios, 0.95),
        'p99_ratio': percentile(all_ratios, 0.99),
        'p999_ratio': percentile(all_ratios, 0.999),
    }

    # Range breakdown
    print(f"\n  Range breakdown:", flush=True)
    for key, label in [('le_100K', '≤ 100K'), ('100K_1M', '100K–1M'), ('1M_10M', '1M–10M'), ('total', 'Total ≤ 10M')]:
        s = range_stats[key]
        mean = s['sum_ratio'] / s['count'] if s['count'] > 0 else 0
        print(f"    {label}: {s['count']:6d} cases, max A={s['max_A']:3d}, max A/log(n)={s['max_ratio']:.4f} (n={s['max_ratio_n']}), mean={mean:.4f}", flush=True)

    print(f"\n  Overall statistics:", flush=True)
    print(f"    Total ω=2 cases: {total_count}", flush=True)
    print(f"    Max A: {stats['max_A']} (n={stats['max_A_n']})", flush=True)
    print(f"    Max A/log(n): {stats['max_ratio']:.6f} (n={stats['max_ratio_n']})", flush=True)
    print(f"    Mean A/log(n): {stats['mean_ratio']:.6f}", flush=True)
    print(f"    Median: {stats['median_ratio']:.6f}", flush=True)
    print(f"    p95: {stats['p95_ratio']:.6f}", flush=True)
    print(f"    p99: {stats['p99_ratio']:.6f}", flush=True)
    print(f"    p99.9: {stats['p999_ratio']:.6f}", flush=True)

    print(f"\n  Distribution of A/log(n) (0.1-width buckets):", flush=True)
    for bucket in sorted(ratio_hist.keys()):
        count = ratio_hist[bucket]
        pct = 100 * count / total_count
        bar = '#' * int(pct)
        print(f"    [{bucket:.1f}, {bucket+0.1:.1f}): {count:6d} ({pct:5.2f}%) {bar}", flush=True)

    print(f"\n  A value distribution:", flush=True)
    for A in sorted(A_distribution.keys()):
        count = A_distribution[A]
        pct = 100 * count / total_count
        print(f"    A={A:3d}: {count:6d} ({pct:5.2f}%)", flush=True)

    # Trend analysis by log(n) bins
    print(f"\n  Trend analysis (max A/log(n) by log(n) bin):", flush=True)
    log_bins = {}
    for r in results:
        lb = int(r['log_n'])
        if lb not in log_bins:
            log_bins[lb] = {'max_ratio': 0, 'max_A': 0, 'n': 0, 'count': 0, 'sum_ratio': 0}
        log_bins[lb]['count'] += 1
        log_bins[lb]['sum_ratio'] += r['ratio']
        if r['ratio'] > log_bins[lb]['max_ratio']:
            log_bins[lb]['max_ratio'] = r['ratio']
            log_bins[lb]['max_A'] = r['A']
            log_bins[lb]['n'] = r['n']

    print(f"    {'log(n)':>8s} | {'n range':>22s} | {'cases':>6s} | {'max A':>6s} | {'max ratio':>10s} | {'mean ratio':>10s} | {'at n':>10s}", flush=True)
    print(f"    {'-'*8} | {'-'*22} | {'-'*6} | {'-'*6} | {'-'*10} | {'-'*10} | {'-'*10}", flush=True)
    for lb in sorted(log_bins.keys()):
        s = log_bins[lb]
        n_lo = int(math.exp(lb))
        n_hi = int(math.exp(lb + 1))
        mean_r = s['sum_ratio'] / s['count']
        print(f"    [{lb:>2d},{lb+1:>2d})  | [{n_lo:>10d},{n_hi:>10d}) | {s['count']:>6d} | {s['max_A']:>6d} | {s['max_ratio']:>10.4f} | {mean_r:>10.4f} | {s['n']:>10d}", flush=True)

    # Top 30 worst cases
    print(f"\n  Top 30 worst cases by A/log(n):", flush=True)
    worst = sorted(results, key=lambda r: -r['ratio'])[:30]
    print(f"    {'n':>10s} | {'A':>4s} | {'log(n)':>8s} | {'A/log(n)':>10s}", flush=True)
    print(f"    {'-'*10} | {'-'*4} | {'-'*8} | {'-'*10}", flush=True)
    for r in worst:
        print(f"    {r['n']:>10d} | {r['A']:>4d} | {r['log_n']:>8.4f} | {r['ratio']:>10.6f}", flush=True)

    # Save JSON
    print(f"\n[6/6] Saving data...", flush=True)
    jpath = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/problem3_omega2_measurement.json"
    with open(jpath, 'w') as f:
        json.dump({
            'limit': limit,
            'total_hard_cases': len(hard_cases),
            'total_omega2_cases': total_count,
            'stats': stats,
            'range_stats': {k: v for k, v in range_stats.items()},
            'A_distribution': dict(A_distribution),
            'ratio_histogram': dict(ratio_hist),
            'log_bin_trend': {str(k): v for k, v in log_bins.items()},
            'worst_cases': [{'n': r['n'], 'A': r['A'], 'ratio': r['ratio']} for r in worst],
            'all_results': [{'n': r['n'], 'A': r['A'], 'ratio': r['ratio']} for r in results],
            'compute_time': compute_time,
            'total_time': time.time() - start,
        }, f, indent=2)
    print(f"  JSON: {jpath}", flush=True)

    total_time = time.time() - start
    print(f"\nDONE in {total_time:.0f}s", flush=True)

if __name__ == "__main__":
    main()