#!/usr/bin/env python3
"""
Problem 3: Measure A/log(n) for ALL ω=2 hard cases up to 10,000,000.

For each ω=2 hard case (n has exactly 2 distinct prime factors), find the
minimum parametric A (z=my condition) and compute A/log(n).

Output: Distribution statistics, trend analysis, and JSON data file.

Key questions:
1. What is the exact distribution of A/log(n) for ω=2 hard cases?
2. Is the decreasing trend (1.61 at 100K, 1.63 at 1M, 1.36 at 1M-10M) confirmed?
3. What is the lim sup behavior as n → ∞?
"""

import math
import json
import time
import sys
from collections import Counter, defaultdict

# ---------------------------------------------------------------------------
# Sieve and helpers
# ---------------------------------------------------------------------------

def sieve_primes(limit):
    """Simple sieve. Returns bytearray where is_prime[i] = 1 if i is prime."""
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = 0
    return is_prime

def build_spf(limit):
    """Build smallest-prime-factor array up to limit."""
    spf = [0] * (limit + 1)
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    return spf

def find_hard_cases_sieve(limit):
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

    is_prime = sieve_primes(limit)

    for p in range(5, limit + 1):
        if p > limit:
            break
        if not is_prime[p]:
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

def count_distinct_prime_factors(n, is_prime):
    """Count distinct prime factors of n using trial division."""
    count = 0
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            count += 1
            while temp % d == 0:
                temp //= d
        d += 1
        # Skip even after 2
        if d == 4:
            d = 3
    if temp > 1:
        count += 1
    return count

def get_prime_factors(n):
    """Return set of distinct prime factors of n."""
    factors = set()
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
        if d == 4:
            d = 3
    if temp > 1:
        factors.add(temp)
    return factors

def factorize(n, spf):
    """Factor n using SPF array. Returns dict {prime: exponent}."""
    factors = {}
    temp = int(n)
    while temp > 1:
        if temp < len(spf) and spf[temp] > 0:
            p = int(spf[temp])
        else:
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
# Parametric solver
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
# Main measurement
# ---------------------------------------------------------------------------

def main():
    start = time.time()

    print("=" * 70, flush=True)
    print("Problem 3: ω=2 A/log(n) Measurement to 10M", flush=True)
    print("=" * 70, flush=True)

    limit = 10_000_000

    # Build SPF
    print(f"\n[1/5] Building SPF up to 2M...", flush=True)
    t0 = time.time()
    spf = build_spf(2_000_000)
    print(f"  SPF: {time.time()-t0:.1f}s", flush=True)

    # Find hard cases
    print(f"\n[2/5] Sieving for hard cases up to {limit:,}...", flush=True)
    t0 = time.time()
    hard_cases = find_hard_cases_sieve(limit)
    print(f"  Found {len(hard_cases)} hard cases in {time.time()-t0:.1f}s", flush=True)

    # Filter to ω=2 cases and compute A/log(n)
    print(f"\n[3/5] Filtering ω=2 and computing parametric A...", flush=True)
    t0 = time.time()

    omega2_results = []
    all_ratio_buckets = Counter()  # bucketed A/log(n) to 0.1 width
    range_stats = {
        'le_100K': {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
        'le_1M':   {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
        '1M_10M':  {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
        'total':   {'count': 0, 'max_A': 0, 'max_ratio': 0, 'max_ratio_n': 0, 'sum_ratio': 0},
    }

    # Distribution buckets
    ratio_hist = Counter()  # 0.1-width buckets
    A_distribution = Counter()

    for i, n in enumerate(hard_cases):
        if (i + 1) % 2000 == 0:
            el = time.time() - t0
            rate = (i + 1) / el if el > 0 else 0
            eta = (len(hard_cases) - i - 1) / rate if rate > 0 else 0
            print(f"  {i+1}/{len(hard_cases)} ({el:.0f}s, {rate:.0f}/s, ETA {eta:.0f}s, ω2={len(omega2_results)})", flush=True)

        # Count distinct prime factors
        pf = get_prime_factors(n)
        omega = len(pf)
        if omega != 2:
            continue

        # Find parametric A
        A = find_parametric_A(n, max_A=200, spf=spf)
        if A is None:
            print(f"  WARNING: No parametric solution for n={n} (ω=2) with A≤200", flush=True)
            continue

        log_n = math.log(n)
        ratio = A / log_n

        omega2_results.append({
            'n': n,
            'A': A,
            'omega': omega,
            'prime_factors': sorted(pf),
            'log_n': log_n,
            'ratio': ratio,
        })

        A_distribution[A] += 1
        bucket = round(ratio, 1)
        ratio_hist[bucket] += 1

        # Range stats
        if n <= 100_000:
            r = 'le_100K'
        elif n <= 1_000_000:
            r = 'le_1M'
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

    # Compute statistics
    print(f"\n[4/5] Computing statistics...", flush=True)

    total_count = len(omega2_results)
    all_ratios = [r['ratio'] for r in omega2_results]
    all_ratios.sort()

    def percentile(sorted_list, p):
        if not sorted_list:
            return 0
        idx = int(len(sorted_list) * p)
        if idx >= len(sorted_list):
            idx = len(sorted_list) - 1
        return sorted_list[idx]

    stats = {
        'total_omega2_cases': total_count,
        'max_A': max(r['A'] for r in omega2_results) if omega2_results else 0,
        'max_A_n': max(omega2_results, key=lambda r: r['A'])['n'] if omega2_results else 0,
        'max_ratio': max(r['ratio'] for r in omega2_results) if omega2_results else 0,
        'max_ratio_n': max(omega2_results, key=lambda r: r['ratio'])['n'] if omega2_results else 0,
        'mean_ratio': sum(all_ratios) / len(all_ratios) if all_ratios else 0,
        'median_ratio': percentile(all_ratios, 0.5),
        'p95_ratio': percentile(all_ratios, 0.95),
        'p99_ratio': percentile(all_ratios, 0.99),
        'p999_ratio': percentile(all_ratios, 0.999),
    }

    # Range breakdown
    for key, label in [('le_100K', '≤ 100K'), ('le_1M', '≤ 1M'), ('1M_10M', '1M–10M'), ('total', 'Total ≤ 10M')]:
        s = range_stats[key]
        mean = s['sum_ratio'] / s['count'] if s['count'] > 0 else 0
        print(f"  {label}: {s['count']} cases, max A={s['max_A']}, max A/log(n)={s['max_ratio']:.4f} (n={s['max_ratio_n']}), mean={mean:.4f}", flush=True)

    print(f"\n  Overall:", flush=True)
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

    # Trend analysis: max ratio in logarithmic n-bins
    print(f"\n  Trend analysis (max A/log(n) by n-range):", flush=True)
    log_bins = {}
    for r in omega2_results:
        log_bin = int(r['log_n'])  # floor(log(n))
        if log_bin not in log_bins:
            log_bins[log_bin] = {'max_ratio': 0, 'max_A': 0, 'n': 0, 'count': 0}
        log_bins[log_bin]['count'] += 1
        if r['ratio'] > log_bins[log_bin]['max_ratio']:
            log_bins[log_bin]['max_ratio'] = r['ratio']
            log_bins[log_bin]['max_A'] = r['A']
            log_bins[log_bin]['n'] = r['n']

    print(f"    {'log(n) range':>15s} | {'n range':>20s} | {'cases':>6s} | {'max A':>6s} | {'max A/log(n)':>13s} | {'at n':>10s}", flush=True)
    print(f"    {'-'*15} | {'-'*20} | {'-'*6} | {'-'*6} | {'-'*13} | {'-'*10}", flush=True)
    for lb in sorted(log_bins.keys()):
        s = log_bins[lb]
        n_lo = int(math.exp(lb))
        n_hi = int(math.exp(lb + 1))
        print(f"    [{lb:>2d}, {lb+1:>2d})       | [{n_lo:>10d}, {n_hi:>10d}) | {s['count']:>6d} | {s['max_A']:>6d} | {s['max_ratio']:>13.4f} | {s['n']:>10d}", flush=True)

    # Top 20 worst cases by A/log(n)
    print(f"\n  Top 20 worst cases by A/log(n):", flush=True)
    worst = sorted(omega2_results, key=lambda r: -r['ratio'])[:20]
    print(f"    {'n':>10s} | {'A':>4s} | {'log(n)':>8s} | {'A/log(n)':>10s} | prime factors", flush=True)
    print(f"    {'-'*10} | {'-'*4} | {'-'*8} | {'-'*10} | {'-'*30}", flush=True)
    for r in worst:
        pf_str = ' × '.join(str(p) for p in r['prime_factors'])
        print(f"    {r['n']:>10d} | {r['A']:>4d} | {r['log_n']:>8.4f} | {r['ratio']:>10.6f} | {pf_str}", flush=True)

    # Save JSON
    print(f"\n[5/5] Saving data...", flush=True)
    jpath = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/problem3_omega2_measurement.json"
    with open(jpath, 'w') as f:
        json.dump({
            'limit': limit,
            'total_omega2_cases': total_count,
            'stats': stats,
            'range_stats': {k: v for k, v in range_stats.items()},
            'A_distribution': dict(A_distribution),
            'ratio_histogram': dict(ratio_hist),
            'log_bin_trend': {str(k): v for k, v in log_bins.items()},
            'worst_cases': [{'n': r['n'], 'A': r['A'], 'ratio': r['ratio'], 'prime_factors': r['prime_factors']} for r in worst],
            'all_results': [{'n': r['n'], 'A': r['A'], 'ratio': r['ratio']} for r in omega2_results],
            'compute_time': compute_time,
        }, f, indent=2)
    print(f"  JSON: {jpath}", flush=True)

    total_time = time.time() - start
    print(f"\nDONE in {total_time:.0f}s", flush=True)

if __name__ == "__main__":
    main()