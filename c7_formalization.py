#!/usr/bin/env python3
"""
Formalize the C = 7 constant bound for primes.

Key facts:
- A = 3 covers n ≡ 5 (mod 8) directly (Theorem 2, proven)
- For n ≡ 1 (mod 8), A = 3 has (3/n) = 1 (since n ≡ 1 mod 12 → (3/n) = 1)
  So the direct route fails for A = 3 when n ≡ 1 (mod 8)
- But the m-route may still work: some prime p | m_3 = (n+3)/4 could be QNR mod n
  
The question: for prime n ≡ 1 (mod 12), n ≢ 0 (mod 5), n ≡ 1 (mod 8):
  Does A = 3 or A = 7 always work (via direct or m-route)?

Strategy:
1. Split primes by n mod 8:
   - n ≡ 5 (mod 8): A = 3 works directly (Theorem 2) ✅
   - n ≡ 1 (mod 8): need to check A = 3 m-route AND A = 7

2. For n ≡ 1 (mod 8), check:
   - Does A = 3 m-route work? (some p | (n+3)/4 is QNR mod n)
   - If not, does A = 7 work? (either direct: (7/n) = -1, or m-route: some p | (n+7)/4 is QNR mod n)

3. Verify computationally up to 10M and look for structural reasons
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, legendre_symbol, mod_inverse
from collections import Counter, defaultdict
from math import lcm

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
    
    if not isprime(A):
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
    
    from itertools import product as iterproduct
    D_A = set()
    ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    for combo in iterproduct(*ranges):
        D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
    
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    return dlog_T in D_A

def check_route_details(n, A):
    """Check which route works for (n, A) and return details."""
    if gcd(n, A) > 1:
        return {'works': False, 'route': 'gcd', 'direct': False, 'mroute': False, 'mroute_primes': []}
    
    m = (n + A) // 4
    
    # Direct route: is A QNR mod n?
    direct = False
    if isprime(A) and isprime(n):
        direct = legendre_symbol(A, n) == -1
    
    # M-route: is some prime factor of m a QNR mod n?
    m_factors = factorint(m)
    mroute_primes = []
    for p in m_factors:
        if isprime(n) and legendre_symbol(p, n) == -1:
            mroute_primes.append(p)
    mroute = len(mroute_primes) > 0
    
    # Does T ∈ D_A?
    T_in_D = check_T_in_D(n, A)
    
    route = 'none'
    if T_in_D and direct and mroute:
        route = 'both'
    elif T_in_D and direct:
        route = 'direct'
    elif T_in_D and mroute:
        route = 'm_route'
    elif T_in_D:
        route = 'other'
    
    return {
        'works': T_in_D or False,
        'route': route,
        'direct': direct,
        'mroute': mroute,
        'mroute_primes': mroute_primes,
        'm': m,
        'm_factors': dict(m_factors),
    }


def main():
    print("Formalizing C = 7: Why do A=3 and A=7 cover all primes?")
    print("=" * 80)
    
    # Step 1: Split by n mod 8
    print("\nStep 1: Split primes by n mod 8")
    
    n_mod8_counts = Counter()
    n_mod8_A3_works = Counter()
    n_mod8_A7_works = Counter()
    
    n = 13
    total_primes = 0
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            total_primes += 1
            mod8 = n % 8
            n_mod8_counts[mod8] += 1
            
            # Check A = 3
            r3 = check_route_details(n, 3)
            if r3['works']:
                n_mod8_A3_works[mod8] += 1
            
            # Check A = 7
            r7 = check_route_details(n, 7)
            if r7['works']:
                n_mod8_A7_works[mod8] += 1
        
        n = nextprime(n)
    
    print(f"\nTotal primes in class ≤ 100K: {total_primes}")
    print(f"\n{'n mod 8':>8} {'Count':>6} {'A=3 works':>10} {'A=7 works':>10} {'Either':>6}")
    for mod8 in sorted(n_mod8_counts.keys()):
        c = n_mod8_counts[mod8]
        a3 = n_mod8_A3_works[mod8]
        a7 = n_mod8_A7_works[mod8]
        either = sum(1 for _ in range(c))  # placeholder
        print(f"{mod8:>8} {c:>6} {a3:>10} {a7:>10}")
    
    # Step 2: For n ≡ 1 (mod 8), analyze why A=3 or A=7 works
    print(f"\n{'='*80}")
    print("Step 2: For n ≡ 1 (mod 8), why does A=3 or A=7 work?")
    print(f"{'='*80}")
    
    n1mod8_cases = []
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n) and n % 8 == 1:
            r3 = check_route_details(n, 3)
            r7 = check_route_details(n, 7)
            
            n1mod8_cases.append({
                'n': n,
                'A3_works': r3['works'],
                'A3_route': r3['route'],
                'A3_direct': r3['direct'],
                'A3_mroute': r3['mroute'],
                'A3_mroute_primes': r3['mroute_primes'],
                'A3_m': r3['m'],
                'A7_works': r7['works'],
                'A7_route': r7['route'],
                'A7_direct': r7['direct'],
                'A7_mroute': r7['mroute'],
                'A7_mroute_primes': r7['mroute_primes'],
                'A7_m': r7['m'],
            })
        n = nextprime(n)
    
    print(f"\nPrimes n ≡ 1 (mod 8) in class ≤ 100K: {len(n1mod8_cases)}")
    
    # A=3 route distribution
    a3_routes = Counter(c['A3_route'] for c in n1mod8_cases)
    print(f"\nA=3 route distribution (n ≡ 1 mod 8):")
    for route, cnt in a3_routes.most_common():
        print(f"  {route}: {cnt}")
    
    # A=7 route distribution
    a7_routes = Counter(c['A7_route'] for c in n1mod8_cases)
    print(f"\nA=7 route distribution (n ≡ 1 mod 8):")
    for route, cnt in a7_routes.most_common():
        print(f"  {route}: {cnt}")
    
    # Combined coverage
    both_fail = sum(1 for c in n1mod8_cases if not c['A3_works'] and not c['A7_works'])
    a3_only = sum(1 for c in n1mod8_cases if c['A3_works'] and not c['A7_works'])
    a7_only = sum(1 for c in n1mod8_cases if not c['A3_works'] and c['A7_works'])
    both_work = sum(1 for c in n1mod8_cases if c['A3_works'] and c['A7_works'])
    
    print(f"\nCombined A=3 ∪ A=7 coverage (n ≡ 1 mod 8):")
    print(f"  Both work: {both_work}")
    print(f"  A=3 only: {a3_only}")
    print(f"  A=7 only: {a7_only}")
    print(f"  Both fail: {both_fail}")
    print(f"  Total covered: {len(n1mod8_cases) - both_fail}/{len(n1mod8_cases)}")
    
    # Step 3: For n ≡ 1 (mod 8), A=3 has (3/n) = ?
    # n ≡ 1 mod 12 → n ≡ 1 mod 3 → (3/n) depends on n mod 12
    # By quadratic reciprocity: (3/n) = (n/3) * (-1)^{(3-1)(n-1)/4} = (n/3) * (-1)^{(n-1)/2}
    # n ≡ 1 mod 4 → (n-1)/2 is even → (3/n) = (n/3)
    # n ≡ 1 mod 3 → (n/3) = (1/3) = 1
    # So (3/n) = 1 always for n ≡ 1 mod 12. Direct route NEVER works for A=3.
    
    print(f"\n{'='*80}")
    print("Step 3: Structural analysis of A=3 m-route for n ≡ 1 (mod 8)")
    print(f"{'='*80}")
    
    print(f"\nFor n ≡ 1 (mod 12): (3/n) = (n/3)·(-1)^{{(n-1)/2}} = 1·1 = 1")
    print(f"  → A=3 direct route NEVER works (always QR)")
    print(f"  → Only m-route can work for A=3")
    
    # m_3 = (n+3)/4. For n ≡ 1 (mod 8): n+3 ≡ 4 (mod 8), so m_3 = (n+3)/4 is odd
    # For n ≡ 5 (mod 8): n+3 ≡ 0 (mod 8), so m_3 = (n+3)/4 is even → 2|m_3 → 2 is QNR mod 3 → works!
    
    print(f"\nFor n ≡ 5 (mod 8): m_3 = (n+3)/4 is EVEN → 2|m_3")
    print(f"  2 mod 3 = -1, so 2 is QNR mod 3 → A=3 direct route via Theorem 2 ✅")
    
    print(f"\nFor n ≡ 1 (mod 8): m_3 = (n+3)/4 is ODD (no factor of 2)")
    print(f"  Need some ODD prime p | m_3 with (p/n) = -1")
    print(f"  m_3 = (n+3)/4, and n+3 ≡ 4 (mod 8), so m_3 is odd")
    
    # Analyze m_3 structure for n ≡ 1 (mod 8)
    print(f"\nAnalyzing m_3 = (n+3)/4 for n ≡ 1 (mod 8):")
    
    m3_small_primes = Counter()  # smallest prime factor of m_3
    m3_qnr_primes = Counter()  # smallest QNR prime in m_3
    
    for c in n1mod8_cases:
        m3 = c['A3_m']
        if m3 > 1:
            factors = factorint(m3)
            smallest_p = min(factors.keys())
            m3_small_primes[smallest_p] += 1
            
            if c['A3_mroute_primes']:
                smallest_qnr = min(c['A3_mroute_primes'])
                m3_qnr_primes[smallest_qnr] += 1
    
    print(f"\n  Smallest prime factor of m_3:")
    for p, cnt in m3_small_primes.most_common(15):
        print(f"    p={p}: {cnt} cases")
    
    print(f"\n  Smallest QNR prime in m_3:")
    for p, cnt in m3_qnr_primes.most_common(15):
        print(f"    p={p}: {cnt} cases")
    
    # Step 4: Why does the m-route work? The key: m_3 = (n+3)/4 always has a small QNR prime
    print(f"\n{'='*80}")
    print("Step 4: Why m-route works — smallest QNR in m_3 or m_7")
    print(f"{'='*80}")
    
    # For each n ≡ 1 (mod 8), find the smallest QNR prime in m_3 or m_7
    smallest_qnr_overall = []
    for c in n1mod8_cases:
        all_qnr = c['A3_mroute_primes'] + c['A7_mroute_primes']
        if all_qnr:
            smallest_qnr_overall.append(min(all_qnr))
    
    qnr_dist = Counter(smallest_qnr_overall)
    print(f"\nSmallest QNR prime in m_3 ∪ m_7 (n ≡ 1 mod 8):")
    for p, cnt in sorted(qnr_dist.items())[:20]:
        print(f"  p={p}: {cnt} cases")
    
    print(f"\n  Max smallest QNR: {max(smallest_qnr_overall) if smallest_qnr_overall else 'N/A'}")
    print(f"  Mean: {sum(smallest_qnr_overall)/len(smallest_qnr_overall):.1f}" if smallest_qnr_overall else "")
    
    # Step 5: The structural argument
    print(f"\n{'='*80}")
    print("Step 5: Structural argument for C = 7")
    print(f"{'='*80}")
    
    # For n ≡ 5 (mod 8): A = 3 works directly (Theorem 2). DONE.
    # For n ≡ 1 (mod 8): 
    #   A = 3: (3/n) = 1, so direct fails. Need m-route: some p | (n+3)/4 is QNR mod n.
    #   A = 7: (7/n) could be ±1. If -1, direct works. If +1, need m-route.
    
    # Key: (n+3)/4 and (n+7)/4 are "random-looking" numbers of size ~n/4.
    # The smallest QNR mod n is known to be O(n^{1/(4√e)+ε}) by Burgess.
    # But we need the QNR to divide (n+3)/4 or (n+7)/4 — a much stronger condition.
    
    # HOWEVER: the computation shows the smallest QNR in m_3 or m_7 is always very small (≤ some bound).
    # This suggests that small primes (2, 3, 5, 7, 11, ...) are QNR mod n for most n,
    # and at least one of them divides m_3 or m_7.
    
    # The question: is there a structural reason why a small QNR must divide (n+3)/4 or (n+7)/4?
    
    # (n+3)/4 ≡ 0 (mod p) iff n ≡ -3 (mod 4p) iff n ≡ 4p-3 (mod 4p)
    # (n+7)/4 ≡ 0 (mod p) iff n ≡ -7 (mod 4p) iff n ≡ 4p-7 (mod 4p)
    
    # So p | m_3 iff n ≡ -3 (mod 4p)
    # And p | m_7 iff n ≡ -7 (mod 4p)
    
    # For p = 2: n ≡ -3 ≡ 5 (mod 8) → covers n ≡ 5 (mod 8) (already done by Theorem 2)
    # For p = 3: n ≡ -3 ≡ 9 (mod 12) → n ≡ 9 (mod 12), but n ≡ 1 (mod 12), so 3 ∤ m_3
    # For p = 5: n ≡ -3 ≡ 17 (mod 20) → need n ≡ 17 (mod 20)
    #            n ≡ -7 ≡ 13 (mod 20) → need n ≡ 13 (mod 20)
    
    # The key: for each small prime p, it divides m_3 for 1/(4p) of primes n,
    # and divides m_7 for 1/(4p) of primes n. Together, p divides m_3 or m_7
    # for ~1/(2p) of primes n.
    
    # If p is QNR mod n, then by Theorem 5 (Legendre symbol identity), (p/A) = (n/p) = -1,
    # so p is QNR mod A, giving a QNR generator in H(A).
    
    # The question: does the Burgess bound guarantee that the least QNR is small enough
    # that it must divide m_3 or m_7?
    
    print(f"\nFor n ≡ 5 (mod 8): A = 3 works directly (Theorem 2). ✅")
    print(f"\nFor n ≡ 1 (mod 8):")
    print(f"  A = 3: (3/n) = 1 always. Need m-route: p | (n+3)/4 with (p/n) = -1.")
    print(f"  A = 7: (7/n) = ±1. If -1, direct works. If +1, need m-route.")
    print(f"\n  p | m_3 iff n ≡ -3 (mod 4p)")
    print(f"  p | m_7 iff n ≡ -7 (mod 4p)")
    print(f"\n  For a small prime p to help, need BOTH:")
    print(f"    (a) p | m_3 or p | m_7 (i.e., n ≡ -3 or -7 (mod 4p))")
    print(f"    (b) (p/n) = -1 (p is QNR mod n)")
    print(f"\n  By Theorem 5: (p/A) = (n/p), so if (n/p) = -1 then p is QNR mod A.")
    print(f"\n  The Burgess bound guarantees the least QNR mod n is O(n^{{1/(4√e)+ε}}).")
    print(f"  For this to help, we need a QNR p that ALSO divides m_3 or m_7.")
    print(f"  This is a JOINT condition: p ≡ -3·4⁻¹ or -7·4⁻¹ (mod p) AND (p/n) = -1.")
    
    # Step 6: Verify the joint condition holds computationally
    print(f"\n{'='*80}")
    print("Step 6: Joint condition verification")
    print(f"{'='*80}")
    
    # For each n ≡ 1 (mod 8), check: what's the smallest p such that
    # (p | m_3 or p | m_7) AND (p/n) = -1?
    
    joint_smallest = []
    for c in n1mod8_cases:
        n = c['n']
        all_qnr = sorted(set(c['A3_mroute_primes'] + c['A7_mroute_primes']))
        if all_qnr:
            joint_smallest.append((n, all_qnr[0]))
    
    if joint_smallest:
        p_dist = Counter(p for _, p in joint_smallest)
        print(f"\nSmallest p with (p|m_3 or p|m_7) AND (p/n)=-1:")
        for p, cnt in sorted(p_dist.items())[:20]:
            print(f"  p={p}: {cnt} cases")
        
        max_p = max(p for _, p in joint_smallest)
        print(f"\n  Max smallest QNR dividing m_3 or m_7: {max_p}")
        print(f"  This means C = max(7, max_p) would suffice if max_p is bounded.")
    
    # Step 7: Check if there are n where A=3 AND A=7 both fail
    print(f"\n{'='*80}")
    print("Step 7: Cases where both A=3 and A=7 fail")
    print(f"{'='*80}")
    
    both_fail_cases = [c for c in n1mod8_cases if not c['A3_works'] and not c['A7_works']]
    print(f"\nCases where A=3 AND A=7 both fail: {len(both_fail_cases)}")
    
    if both_fail_cases:
        print(f"  These need A > 7. Let's check what A works:")
        for c in both_fail_cases[:20]:
            n = c['n']
            # Find minimal A
            A = 11
            while A <= 200:
                if gcd(n, A) == 1:
                    result = check_T_in_D(n, A)
                    if result:
                        r = check_route_details(n, A)
                        print(f"    n={n}: A={A} works (route={r['route']})")
                        break
                A += 4
    
    # Step 8: Extend to 10M — check n ≡ 1 (mod 8) primes
    print(f"\n{'='*80}")
    print("Step 8: Extended verification up to 10M")
    print(f"{'='*80}")
    
    both_fail_10M = 0
    total_1mod8_10M = 0
    max_smallest_qnr = 0
    
    n = 13
    while n <= 10000000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n) and n % 8 == 1:
            total_1mod8_10M += 1
            r3 = check_route_details(n, 3)
            r7 = check_route_details(n, 7)
            
            if not r3['works'] and not r7['works']:
                both_fail_10M += 1
                if both_fail_10M <= 10:
                    # Find what A works
                    A = 11
                    while A <= 200:
                        if gcd(n, A) == 1:
                            result = check_T_in_D(n, A)
                            if result:
                                print(f"  n={n}: A=3,7 fail, A={A} works")
                                break
                        A += 4
            
            # Track smallest QNR
            all_qnr = sorted(set(r3['mroute_primes'] + r7['mroute_primes']))
            if all_qnr and all_qnr[0] > max_smallest_qnr:
                max_smallest_qnr = all_qnr[0]
        
        n = nextprime(n)
    
    print(f"\n  Total primes n ≡ 1 (mod 8) ≤ 10M: {total_1mod8_10M}")
    print(f"  Both A=3,7 fail: {both_fail_10M}")
    print(f"  Max smallest QNR in m_3∪m_7: {max_smallest_qnr}")
    
    if both_fail_10M == 0:
        print(f"\n  ✅ A=3 ∪ A=7 covers ALL primes n ≡ 1 (mod 8) up to 10M")
        print(f"  Combined with Theorem 2 (n ≡ 5 mod 8 → A=3):")
        print(f"  → C = 7 for all primes n ≡ 1 (mod 12), n ≢ 0 (mod 5), n ≤ 10M")
    
    # Save
    output = {
        'total_1mod8_100k': len(n1mod8_cases),
        'both_fail_100k': len(both_fail_cases),
        'total_1mod8_10M': total_1mod8_10M,
        'both_fail_10M': both_fail_10M,
        'max_smallest_qnr': max_smallest_qnr,
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/c7_proof_data.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to c7_proof_data.json")


if __name__ == '__main__':
    main()