#!/usr/bin/env python3
"""
Focused scan for hard cases (large minimal A) across n ≤ 10M.
The previous sampling missed rare hard cases. This script does a targeted search.

Strategy: The hard cases are n that are QR mod ALL of {7, 11, 19, 23, 31}.
For those n, the direct route fails and we need the m-route or larger A.

From v9 data: 59 such primes exist ≤ 100K, all rescued by m-route with A ≤ 31.
But at 10M scale, 65 cases need A > 31.

So: scan all n that are QR mod all of {7, 11, 19, 23, 31} up to 10M,
find their minimal A, and track the growth.
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, legendre_symbol, mod_inverse
from collections import Counter
from math import lcm
from itertools import product as iterproduct

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
    if gcd(n, A) > 1: return None
    m = (n + A) // 4
    nx = n * m
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    if not prime_factors: return None
    
    if not sympy.isprime(A):
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
        if h <= 1: s_values[p] = 0; continue
        try:
            s_inv = mod_inverse(step, h)
            s_i = (dlg * s_inv) % h
        except:
            s_i = None
            for s in range(h):
                if (s * step) % h == dlg % h: s_i = s; break
            if s_i is None: return None
        s_values[p] = s_i
    
    D_A = set()
    ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    for combo in iterproduct(*ranges):
        D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
    
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    return dlog_T in D_A

def find_minimal_A(n, max_A=200):
    A = 3
    while A <= max_A:
        if gcd(n, A) == 1:
            result = check_T_in_D(n, A)
            if result is True:
                return A
        A += 4
    return None

def main():
    print("Focused scan: n QR mod all of {7, 11, 19, 23, 31} up to 10M")
    print("=" * 80)
    
    # First pass: find all n that are QR mod all of {7, 11, 19, 23, 31}
    # These are the only candidates for needing large A
    qr_all_primes = []
    n = 13
    count = 0
    while n <= 10000000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            count += 1
            if all(legendre_symbol(A, n) == 1 for A in [7, 11, 19, 23, 31] if gcd(A, n) == 1):
                qr_all_primes.append(n)
        n = nextprime(n)
    
    print(f"Total primes in class ≤ 10M: {count}")
    print(f"Primes QR mod all of {{7, 11, 19, 23, 31}}: {len(qr_all_primes)}")
    print(f"  ({len(qr_all_primes)/count*100:.2f}% of primes in class)")
    
    # For each, find minimal A
    results = []
    max_A_found = 0
    hard_cases = []
    
    for i, n in enumerate(qr_all_primes):
        min_A = find_minimal_A(n, max_A=200)
        if min_A:
            results.append((n, min_A))
            if min_A > max_A_found:
                max_A_found = min_A
            if min_A > 31:
                hard_cases.append((n, min_A))
        else:
            hard_cases.append((n, None))
            results.append((n, None))
        
        if (i + 1) % 100 == 0:
            print(f"  Processed {i+1}/{len(qr_all_primes)}, max A so far: {max_A_found}")
    
    print(f"\n{'='*80}")
    print("RESULTS")
    print(f"{'='*80}")
    
    # Distribution of minimal A
    valid_results = [(n, a) for n, a in results if a is not None]
    A_dist = Counter(a for _, a in valid_results)
    print(f"\nMinimal A distribution (n QR mod all covering set):")
    for A in sorted(A_dist.keys()):
        print(f"  A={A}: {A_dist[A]} cases")
    
    print(f"\nMax A needed: {max_A_found}")
    print(f"Cases needing A > 31: {sum(1 for _, a in valid_results if a > 31)}")
    print(f"Cases needing A > 59: {sum(1 for _, a in valid_results if a > 59)}")
    print(f"Cases needing A > 107: {sum(1 for _, a in valid_results if a > 107)}")
    print(f"Cases with no A ≤ 200: {sum(1 for _, a in results if a is None)}")
    
    if hard_cases:
        print(f"\nHard cases (A > 31):")
        for n, a in sorted(hard_cases, key=lambda x: (x[1] or 999, x[0])):
            print(f"  n={n}: A={a}")
    
    # Growth analysis: max A vs n
    print(f"\n{'='*80}")
    print("GROWTH: Max A in intervals")
    print(f"{'='*80}")
    
    intervals = [(1000, "≤1K"), (10000, "≤10K"), (100000, "≤100K"),
                (500000, "≤500K"), (1000000, "≤1M"), (2000000, "≤2M"),
                (5000000, "≤5M"), (10000000, "≤10M")]
    
    print(f"{'Range':>8} {'Cases':>6} {'Max A':>6} {'Avg A':>6} {'A>31':>5} {'A>59':>5}")
    for max_n, label in intervals:
        interval_results = [(n, a) for n, a in valid_results if n <= max_n]
        if interval_results:
            max_A = max(a for _, a in interval_results)
            avg_A = sum(a for _, a in interval_results) / len(interval_results)
            over_31 = sum(1 for _, a in interval_results if a > 31)
            over_59 = sum(1 for _, a in interval_results if a > 59)
            print(f"{label:>8} {len(interval_results):>6} {max_A:>6} {avg_A:>6.1f} {over_31:>5} {over_59:>5}")
    
    # The key question: is max_A growing?
    print(f"\nIf max_A plateaus, the constant bound conjecture holds.")
    print(f"If max_A grows without bound, we need the analytic (Burgess) route.")
    
    # Save
    output = {
        'total_qr_all_primes': len(qr_all_primes),
        'max_A_found': max_A_found,
        'A_distribution': dict(A_dist),
        'hard_cases': [(n, a) for n, a in hard_cases if a is not None],
        'no_solution': [(n, a) for n, a in hard_cases if a is None],
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/hard_cases_10M.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to hard_cases_10M.json")

if __name__ == '__main__':
    main()