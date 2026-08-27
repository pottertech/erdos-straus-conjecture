#!/usr/bin/env python3
"""
Open Problem #6: M-Route Sufficiency
=====================================
Prove that when the direct route fails (A is QR mod n for all A in covering set),
the m-route always succeeds for some A.

Direct route: A works because (A/n) = -1 (A is QNR mod n)
M-route: A works because some prime p | m_A = (n+A)/4 has (n/p) = -1 (p is QNR mod n)
         By Theorem 5, (p/A) = (n/p), so p is QNR mod A, giving a QNR generator in H(A).

Question: When n is QR mod ALL covering set primes {7, 11, 19, 23, 31}
(the direct route fails for all), does the m-route always succeed for at least one A?

Strategy:
1. Find all n ≤ 100,000 where n is QR mod all of {7, 11, 19, 23, 31}
2. For each such n, check if the m-route works for each A
3. Verify that at least one A always has a QNR prime factor in m_A
4. Analyze the structure: which primes appear as QNR factors of m_A?
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, mod_inverse, legendre_symbol
from collections import defaultdict, Counter
from math import lcm

COVERING_A = [3, 7, 11, 15, 19, 23, 27, 31]
PRIME_A = [3, 7, 11, 19, 23, 31]

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

def check_route(n, A):
    """
    Check if A works for n, and by which route.
    Returns: (works, route_type, details)
    route_type: 'direct' (A is QNR mod n), 'm_route' (some p|m_A is QNR mod n), 'both', 'none'
    """
    if gcd(n, A) > 1:
        return (False, 'gcd', {})
    
    m = (n + A) // 4
    nx = n * m
    
    # Direct route: is A QNR mod n?
    if isprime(A) and isprime(n):
        direct = legendre_symbol(A, n) == -1
    else:
        direct = False
    
    # M-route: is some prime factor of m a QNR mod n?
    m_factors = factorint(m)
    mroute_primes = []
    for p in m_factors:
        if isprime(n) and legendre_symbol(p, n) == -1:
            mroute_primes.append(p)
    
    mroute = len(mroute_primes) > 0
    
    # Does T ∈ D_A?
    # Compute D_A properly
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    if not prime_factors:
        return (False, 'no_factors', {})
    
    if not isprime(A):
        # Composite A - check directly
        D_A = set([1])
        for p, e in prime_factors:
            p_mod = p % A
            new_D = set()
            for d in D_A:
                for exp in range(2 * e + 1):
                    new_D.add(pow(p_mod, exp, A) * d % A)
            D_A = new_D
        T = (-n * n * mod_inverse(4, A)) % A
        T_in_D = T in D_A
    else:
        # Prime A - use dlog
        g = find_primitive_root(A)
        if g is None:
            return (False, 'no_prim_root', {})
        
        orders = [multiplicative_order(p, A) for p, _ in prime_factors]
        h = 1
        for o in orders: h = lcm(h, o)
        if h <= 1:
            T = (-n * n * mod_inverse(4, A)) % A
            D_A = set([1])
            T_in_D = (T == 1)
        else:
            s_values = {}
            for p, e in prime_factors:
                dlg = discrete_log_mod(g, p, A)
                step = (A - 1) // h
                try:
                    s_inv = mod_inverse(step, h)
                    s_i = (dlg * s_inv) % h
                except:
                    s_i = None
                    for s in range(h):
                        if (s * step) % h == dlg % h: s_i = s; break
                s_values[p] = s_i
            
            from itertools import product as iterproduct
            D_A = set()
            ranges = [range(2 * e + 1) for _, e in prime_factors]
            s_list = [s_values[p] for p, _ in prime_factors]
            for combo in iterproduct(*ranges):
                D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
            
            dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
            dlog_T = (h // 2 + dlog_nm) % h
            T_in_D = dlog_T in D_A
    
    if T_in_D and direct and mroute:
        route = 'both'
    elif T_in_D and direct:
        route = 'direct'
    elif T_in_D and mroute:
        route = 'm_route'
    elif T_in_D:
        route = 'other'  # T in D_A but neither direct nor m-route (alternative path)
    else:
        route = 'none'
    
    return (T_in_D, route, {
        'm': m,
        'm_factors': dict(m_factors),
        'mroute_primes': mroute_primes,
        'direct': direct,
        'mroute': mroute,
    })


def main():
    print("Open Problem #6: M-Route Sufficiency Analysis")
    print("=" * 80)
    
    # Step 1: Find all primes n ≤ 100,000 where n is QR mod all of {7, 11, 19, 23, 31}
    print("\nStep 1: Finding n where direct route fails for all prime A...")
    
    direct_fail_cases = []
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            # Check if n is QR mod all covering primes (except A=3, which always has (3/n)=1 for n≡1 mod 12)
            all_qr = all(legendre_symbol(A, n) == 1 for A in [7, 11, 19, 23, 31] if gcd(A, n) == 1)
            if all_qr:
                direct_fail_cases.append(n)
        n = nextprime(n)
    
    print(f"  Found {len(direct_fail_cases)} primes where n is QR mod all of {{7, 11, 19, 23, 31}}")
    
    if not direct_fail_cases:
        print("  No cases where direct route fails for all A simultaneously!")
        print("  This means the direct route alone is sufficient for n ≤ 100,000.")
        print("  M-route is not needed as a fallback for this range.")
        return
    
    # Step 2: For each such n, check if m-route works
    print(f"\nStep 2: Checking m-route for {len(direct_fail_cases)} cases...")
    
    results = []
    mroute_success = 0
    mroute_fail = 0
    
    for n in direct_fail_cases:
        n_results = {}
        any_success = False
        
        for A in COVERING_A:
            if gcd(n, A) > 1:
                continue
            works, route, details = check_route(n, A)
            n_results[A] = (works, route, details)
            if works:
                any_success = True
        
        # Check specifically: does m-route work for at least one A?
        mroute_works = any(
            n_results[A][1] in ('m_route', 'both')
            for A in COVERING_A if A in n_results
        )
        
        # Also check: does ANY A work?
        any_works = any(n_results[A][0] for A in n_results)
        
        if mroute_works:
            mroute_success += 1
        elif any_works:
            mroute_fail += 1
            # A works but NOT via m-route — this means 'other' route
            print(f"  n={n}: A works via 'other' route (not direct, not m-route)")
            for A in n_results:
                if n_results[A][0]:
                    print(f"    A={A}: route={n_results[A][1]}, mroute_primes={n_results[A][2].get('mroute_primes', [])}")
        else:
            mroute_fail += 1
            print(f"  n={n}: NO A works! (gap case)")
        
        results.append({
            'n': n,
            'any_works': any_works,
            'mroute_works': mroute_works,
            'details': {A: {'works': w, 'route': r, 'mroute_primes': d.get('mroute_primes', [])}
                       for A, (w, r, d) in n_results.items()}
        })
    
    print(f"\n{'='*60}")
    print("M-ROUTE SUFFICIENCY RESULTS")
    print(f"{'='*60}")
    print(f"Cases where direct route fails for all A: {len(direct_fail_cases)}")
    print(f"  M-route succeeds for at least one A: {mroute_success}")
    print(f"  M-route fails but other route works: {mroute_fail}")
    print(f"  No A works: {len(direct_fail_cases) - mroute_success - mroute_fail}")
    
    # Step 3: Analyze which A values provide m-route success
    print(f"\n{'='*60}")
    print("M-ROUTE SUCCESS BY A")
    print(f"{'='*60}")
    
    mroute_by_A = Counter()
    for r in results:
        for A in r['details']:
            if r['details'][A]['route'] in ('m_route', 'both'):
                mroute_by_A[A] += 1
    
    for A in sorted(mroute_by_A.keys()):
        print(f"  A={A}: {mroute_by_A[A]} m-route successes")
    
    # Step 4: Analyze which QNR primes appear in m_A
    print(f"\n{'='*60}")
    print("QNR PRIMES IN m_A")
    print(f"{'='*60}")
    
    qnr_primes = Counter()
    for r in results:
        for A in r['details']:
            for p in r['details'][A].get('mroute_primes', []):
                qnr_primes[p] += 1
    
    print(f"  Top QNR primes appearing in m_A:")
    for p, cnt in qnr_primes.most_common(20):
        print(f"    p={p}: appears in {cnt} m_A values")
    
    # Step 5: Check if direct route alone is sufficient
    print(f"\n{'='*60}")
    print("DIRECT ROUTE SUFFICIENCY CHECK")
    print(f"{'='*60}")
    
    # For ALL n ≤ 100,000 (not just direct-fail cases), check if direct route alone suffices
    direct_only_fail = 0
    total_primes = 0
    
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            total_primes += 1
            # Check if any A has direct route success
            direct_any = False
            for A in PRIME_A:
                if gcd(n, A) > 1: continue
                if isprime(A) and legendre_symbol(A, n) == -1:
                    direct_any = True
                    break
            if not direct_any:
                direct_only_fail += 1
        n = nextprime(n)
    
    print(f"  Total primes in target class: {total_primes}")
    print(f"  Primes where direct route fails for ALL A in {{3,7,11,19,23,31}}: {direct_only_fail}")
    print(f"  Direct route success rate: {(total_primes - direct_only_fail)/total_primes*100:.1f}%")
    
    # Save results
    output = {
        'total_direct_fail_cases': len(direct_fail_cases),
        'mroute_success': mroute_success,
        'mroute_fail': mroute_fail,
        'direct_only_fail': direct_only_fail,
        'total_primes': total_primes,
        'mroute_by_A': dict(mroute_by_A),
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/mroute_analysis.json', 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved to mroute_analysis.json")


if __name__ == '__main__':
    main()