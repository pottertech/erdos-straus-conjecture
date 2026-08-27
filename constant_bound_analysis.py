#!/usr/bin/env python3
"""
Open Problems #3 & #4: Constant Bound Conjecture & Covering System Proof
=========================================================================
Problem #3: Prove A ≤ C for some absolute constant C.
Problem #4: Prove a finite covering set works for ALL n.

The 10M verification shows:
- A ≤ 31 covers all n ≤ 100K but NOT all n ≤ 10M (65 cases need A > 31)
- A ≤ 59 covers all n ≤ 10M except n=8,803,369 (needs A=107)
- A ≤ 107 covers all n ≤ 10M

Key questions:
1. How does max_A(n) grow with n? Is it bounded or slowly growing?
2. What's the distribution of minimal A across n ≤ 10M?
3. Are there structural reasons some n need large A?
4. Can we prove a bound using the covering set + Burgess argument?

Strategy:
1. Analyze the 10M data: how does max_A grow?
2. Identify n values requiring large A — what's special about them?
3. Test whether the covering set {3,7,11,19,23,31} fails for predictable reasons
4. Estimate: does max_A(n) grow like log(n), log²(n), or is it bounded?
5. If max_A appears bounded, estimate the bound
6. If growing, characterize the growth rate
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, legendre_symbol, mod_inverse
from collections import defaultdict, Counter
from math import log, log2, lcm

# Extended covering set for 10M analysis
EXTENDED_A = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107]

def find_primitive_root(p):
    if p == 2: return 1
    phi = p - 1
    factors = factorint(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    return None

def discrete_log_mod(g, target, p):
    val = 1
    for i in range(p - 1):
        if val == target % p: return i
        val = (val * g) % p
    return None

def multiplicative_order(a, n):
    if gcd(a, n) > 1: return None
    val = a % n
    for i in range(1, n):
        if val == 1: return i
        val = (val * a) % n
    return None

def check_T_in_D(n, A):
    """Quick check: is T ∈ D_A for this (n, A)?"""
    if gcd(n, A) > 1:
        return None  # skip
    
    m = (n + A) // 4
    nx = n * m
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    if not prime_factors:
        return None
    
    if not isprime(A):
        # Composite A: direct D_A computation
        D_A = set([1])
        for p, e in prime_factors:
            p_mod = p % A
            new_D = set()
            for d in D_A:
                for exp in range(2 * e + 1):
                    new_D.add(pow(p_mod, exp, A) * d % A)
            D_A = new_D
        T = (-n * n * mod_inverse(4, A)) % A
        return T in D_A
    
    # Prime A: use dlog
    g = find_primitive_root(A)
    if g is None: return None
    
    orders = [multiplicative_order(p, A) for p, _ in prime_factors]
    h = 1
    for o in orders: h = lcm(h, o)
    
    if h <= 1:
        T = (-n * n * mod_inverse(4, A)) % A
        return T == 1
    
    s_values = {}
    for p, e in prime_factors:
        dlg = discrete_log_mod(g, p, A)
        step = (A - 1) // h
        if h <= 1:
            s_values[p] = 0; continue
        try:
            s_inv = mod_inverse(step, h)
            s_i = (dlg * s_inv) % h
        except:
            s_i = None
            for s in range(h):
                if (s * step) % h == dlg % h: s_i = s; break
            if s_i is None: return None
        s_values[p] = s_i
    
    from itertools import product as iterproduct
    D_A = set()
    ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    for combo in iterproduct(*ranges):
        D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
    
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    return dlog_T in D_A


def find_minimal_A(n, max_A=107):
    """Find the smallest A ≡ 3 (mod 4) that works for n."""
    A = 3
    while A <= max_A:
        if gcd(n, A) == 1:
            result = check_T_in_D(n, A)
            if result is True:
                return A
        A += 4
    return None  # not found within max_A


def analyze_10M_growth():
    """
    Analyze how max_A grows with n by sampling.
    Full 10M scan takes too long, so we sample strategically.
    """
    print("Analyzing max_A growth across n range...")
    print("=" * 80)
    
    # Sample at different n scales
    scales = [
        (1000, 100, "n ≤ 1K"),
        (10000, 200, "n ≤ 10K"),
        (100000, 500, "n ≤ 100K"),
        (500000, 500, "n ≤ 500K"),
        (1000000, 500, "n ≤ 1M"),
        (2000000, 300, "n ≤ 2M"),
        (5000000, 200, "n ≤ 5M"),
        (10000000, 100, "n ≤ 10M"),
    ]
    
    results = []
    
    for max_n, sample_size, label in scales:
        print(f"\n--- {label} (sample {sample_size} primes) ---")
        
        # Sample primes in the target class
        primes_in_class = []
        n = 13
        step = max(1, max_n // sample_size)
        while n <= max_n:
            if n % 12 == 1 and n % 5 != 0 and isprime(n):
                primes_in_class.append(n)
            n = nextprime(n)
        
        # Subsample if needed
        if len(primes_in_class) > sample_size:
            # Even spacing
            idx = [i * len(primes_in_class) // sample_size for i in range(sample_size)]
            primes_in_class = [primes_in_class[i] for i in idx]
        
        min_A_values = []
        max_A_in_range = 0
        hard_cases = []
        
        for n in primes_in_class:
            min_A = find_minimal_A(n, max_A=107)
            if min_A is not None:
                min_A_values.append((n, min_A))
                if min_A > max_A_in_range:
                    max_A_in_range = min_A
                if min_A > 31:
                    hard_cases.append((n, min_A))
            else:
                hard_cases.append((n, None))
        
        if min_A_values:
            A_dist = Counter(a for _, a in min_A_values)
            avg_A = sum(a for _, a in min_A_values) / len(min_A_values)
            print(f"  Primes sampled: {len(primes_in_class)}")
            print(f"  Min A distribution: {dict(sorted(A_dist.items())[:15])}")
            print(f"  Max A needed: {max_A_in_range}")
            print(f"  Avg A: {avg_A:.1f}")
            print(f"  Cases needing A > 31: {sum(1 for _, a in min_A_values if a > 31)}")
            print(f"  Cases needing A > 59: {sum(1 for _, a in min_A_values if a > 59)}")
            if hard_cases:
                print(f"  Hard cases (A > 31): {hard_cases[:10]}")
            
            results.append({
                'max_n': max_n,
                'sample_size': len(primes_in_class),
                'max_A': max_A_in_range,
                'avg_A': avg_A,
                'dist': dict(A_dist),
                'hard_cases': hard_cases[:20],
            })
    
    return results


def analyze_hard_cases():
    """
    Find n values that need large A and analyze what makes them special.
    Focus on n ≤ 100K first (full scan), then sample larger n.
    """
    print(f"\n{'='*80}")
    print("HARD CASE ANALYSIS: n values needing large A")
    print(f"{'='*80}")
    
    # Full scan n ≤ 100K
    hard_cases = []
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            min_A = find_minimal_A(n, max_A=107)
            if min_A and min_A > 11:  # A > 11 is "harder"
                hard_cases.append((n, min_A))
        n = nextprime(n)
    
    print(f"\nn ≤ 100K: {len(hard_cases)} cases needing A > 11")
    
    # Distribution
    A_dist = Counter(a for _, a in hard_cases)
    print(f"A distribution: {dict(sorted(A_dist.items()))}")
    
    # What fraction of n are QR mod all of {7, 11, 19, 23, 31}?
    qr_all = []
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            if all(legendre_symbol(A, n) == 1 for A in [7, 11, 19, 23, 31] if gcd(A, n) == 1):
                qr_all.append(n)
        n = nextprime(n)
    
    print(f"\nn QR mod all of {{7, 11, 19, 23, 31}}: {len(qr_all)} primes")
    
    # For these, what A works?
    qr_all_min_A = []
    for n in qr_all:
        min_A = find_minimal_A(n, max_A=107)
        if min_A:
            qr_all_min_A.append((n, min_A))
    
    A_dist_qr = Counter(a for _, a in qr_all_min_A)
    print(f"Min A for QR-all cases: {dict(sorted(A_dist_qr.items()))}")
    
    # The key question: is needing large A correlated with n being QR mod many small primes?
    print(f"\nCorrelation: n QR mod many A values → needs larger A")
    
    # For each n ≤ 100K, count how many of {7, 11, 19, 23, 31} have (A/n) = -1
    qr_count_dist = defaultdict(list)  # qr_count -> list of (n, min_A)
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            qr_count = sum(1 for A in [7, 11, 19, 23, 31] if gcd(A, n) == 1 and legendre_symbol(A, n) == 1)
            min_A = find_minimal_A(n, max_A=107)
            if min_A:
                qr_count_dist[qr_count].append((n, min_A))
        n = nextprime(n)
    
    print(f"\n{'QR count':>8} {'Cases':>6} {'Max A':>6} {'Avg A':>6} {'A>31':>5}")
    for qr_cnt in sorted(qr_count_dist.keys()):
        cases = qr_count_dist[qr_cnt]
        max_A = max(a for _, a in cases)
        avg_A = sum(a for _, a in cases) / len(cases)
        over_31 = sum(1 for _, a in cases if a > 31)
        print(f"{qr_cnt:>8} {len(cases):>6} {max_A:>6} {avg_A:>6.1f} {over_31:>5}")
    
    return hard_cases, qr_all


def growth_rate_analysis(results):
    """
    Estimate how max_A grows with n.
    If max_A is bounded, it should plateau.
    If growing, fit the growth rate.
    """
    print(f"\n{'='*80}")
    print("GROWTH RATE ANALYSIS")
    print(f"{'='*80}")
    
    print(f"\n{'max_n':>10} {'Max A':>6} {'Avg A':>6} {'log2(n)':>8} {'A/log²(n)':>10} {'A/log(n)':>10}")
    for r in results:
        max_n = r['max_n']
        max_A = r['max_A']
        avg_A = r['avg_A']
        log2n = log2(max_n) if max_n > 1 else 0
        logn = log(max_n) if max_n > 1 else 0
        a_over_log2 = max_A / (log2n ** 2) if log2n > 0 else 0
        a_over_log = max_A / logn if logn > 0 else 0
        print(f"{max_n:>10} {max_A:>6} {avg_A:>6.1f} {log2n:>8.1f} {a_over_log2:>10.2f} {a_over_log:>10.2f}")
    
    # Is max_A growing or plateauing?
    max_A_values = [r['max_A'] for r in results]
    if len(max_A_values) >= 3:
        early = max_A_values[:len(max_A_values)//2]
        late = max_A_values[len(max_A_values)//2:]
        avg_early = sum(early) / len(early)
        avg_late = sum(late) / len(late)
        print(f"\n  Avg max_A (early half): {avg_early:.1f}")
        print(f"  Avg max_A (late half): {avg_late:.1f}")
        if avg_late > avg_early * 1.5:
            print(f"  → max_A appears to be GROWING")
        elif avg_late > avg_early * 1.1:
            print(f"  → max_A appears to be SLOWLY GROWING")
        else:
            print(f"  → max_A appears to be PLATEAUING (bounded?)")


def covering_set_feasibility(results):
    """
    Estimate: if we use covering set up to A = C, how many n need larger A?
    This tells us what C would need to be.
    """
    print(f"\n{'='*80}")
    print("COVERING SET FEASIBILITY")
    print(f"{'='*80}")
    
    for r in results:
        max_n = r['max_n']
        dist = r['dist']
        total = r['sample_size']
        
        # Cumulative coverage
        cumulative = 0
        for A in sorted(dist.keys()):
            cumulative += dist[A]
            if cumulative >= total * 0.99:
                print(f"  n ≤ {max_n:>8}: 99% coverage at A ≤ {A}, 100% at A ≤ {r['max_A']}")
                break
    
    print(f"\nThe constant bound conjecture requires A ≤ C for ALL n.")
    print(f"If max_A grows like log(n), no constant C suffices.")
    print(f"If max_A is bounded, C exists but may be large.")
    print(f"Current data: max_A = {max(r['max_A'] for r in results)} for n up to {max(r['max_n'] for r in results)}")


def main():
    # Growth analysis
    results = analyze_10M_growth()
    
    # Hard case analysis
    hard_cases, qr_all = analyze_hard_cases()
    
    # Growth rate
    growth_rate_analysis(results)
    
    # Covering set feasibility
    covering_set_feasibility(results)
    
    # Save
    output = {
        'growth_results': [{'max_n': r['max_n'], 'max_A': r['max_A'], 'avg_A': r['avg_A']} for r in results],
        'hard_cases_100k': [(n, a) for n, a in hard_cases[:50]],
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/constant_bound_analysis.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to constant_bound_analysis.json")


if __name__ == '__main__':
    main()