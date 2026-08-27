#!/usr/bin/env python3
"""
Theorem 3 Forward Direction — Centered Signed-Exponent Analysis
================================================================

Per Mark Kruelle's insight: stop analyzing -1 ∈ D_A. Work with the centered criterion.

For each prime-A case, compute:
- n, A, N = n*(n+A)/4
- factorization N = ∏ p_i^{e_i}
- h = |H(A)|
- subgroup generator u (primitive root mod A, stepped to H(A))
- dlog vector s_i where p_i ≡ u^{s_i} mod A
- shortest signed representation h/2 = Σ s_i*δ_i mod h with -e_i ≤ δ_i ≤ e_i
- route type classification
- whether n participates, whether m contributes the decisive factor

Route types:
1. order-2: some p_i ≡ -1 mod A, δ_i=1 works immediately
2. two-term centered: ∃ i,j with s_i*δ_i + s_j*δ_j ≡ h/2
3. short signed route: h/2 reached using 3-5 factors with small δ_i
4. full interval coverage: Σ_A(N) = Z/hZ
5. m-route: direct n-route fails, factor of m=(n+A)/4 supplies decisive residue
6. exceptional structured: special parity/restriction cases
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, legendre_symbol
from collections import defaultdict, Counter
from math import lcm
from itertools import product as iterproduct

PRIME_A = [3, 7, 11, 19, 23, 31]

def find_primitive_root(p):
    if p == 2: return 1
    phi = p - 1
    factors = factorint(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    return None

def multiplicative_order(a, n):
    if gcd(a, n) > 1: return None
    val = a % n
    for i in range(1, n):
        if val == 1: return i
        val = (val * a) % n
    return None

def discrete_log_mod(g, target, p):
    val = 1
    for i in range(p - 1):
        if val == target % p: return i
        val = (val * g) % p
    return None

def compute_centered_criterion(n, A):
    """
    Compute the centered signed-exponent criterion for given n, A.
    
    Returns: dict with all computed fields, or None if inapplicable.
    """
    if gcd(n, A) > 1:
        return None
    if not isprime(A):
        return None
    
    m = (n + A) // 4
    N = n * m  # = n*(n+A)/4
    factors_N = factorint(N)
    # Only prime factors coprime to A
    prime_factors = [(p, e) for p, e in factors_N.items() if gcd(p, A) == 1]
    if not prime_factors:
        return None
    
    # Separate n factors from m factors
    factors_n = factorint(n)
    factors_m = factorint(m)
    
    g = find_primitive_root(A)
    if g is None:
        return None
    
    # Compute orders and h
    orders = [multiplicative_order(p, A) for p, _ in prime_factors]
    h = 1
    for o in orders:
        h = lcm(h, o)
    if h <= 1:
        return None  # All QR, forward direction hypothesis not met
    
    if h % 2 != 0:
        return None  # h odd means -1 not in H(A), forward direction hypothesis not met
    
    # Compute dlog values mod h
    step = (A - 1) // h
    s_values = {}
    for p, e in prime_factors:
        dlg = discrete_log_mod(g, p, A)
        if dlg is None:
            return None
        s_values[p] = dlg % h
    
    # The centered set: Σ_A(N) = { Σ s_i*δ_i mod h : -e_i ≤ δ_i ≤ e_i }
    # We need h/2 ∈ Σ_A(N)
    target = h // 2
    
    # Check if any p_i ≡ -1 mod A (order-2 route)
    order_2_primes = []
    for p, e in prime_factors:
        if multiplicative_order(p, A) == 2:
            order_2_primes.append(p)
    
    has_order_2 = len(order_2_primes) > 0
    
    # Compute the full signed sumset
    # For small cases, brute force; for larger, sample
    signed_set = set()
    ranges = [range(-e, e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    
    total_combos = 1
    for _, e in prime_factors:
        total_combos *= (2 * e + 1)
    
    if total_combos <= 5_000_000:
        for combo in iterproduct(*ranges):
            val = sum(d * s for d, s in zip(combo, s_list)) % h
            signed_set.add(val)
    else:
        # Sample: random + structured
        import random
        random.seed(42)
        for _ in range(500000):
            combo = [random.randint(-e, e) for _, e in prime_factors]
            val = sum(d * s for d, s in zip(combo, s_list)) % h
            signed_set.add(val)
        # Also try structured: single-term, two-term
        for i, (p, e) in enumerate(prime_factors):
            for d in range(-e, e + 1):
                val = (d * s_list[i]) % h
                signed_set.add(val)
                for j in range(i + 1, len(prime_factors)):
                    p2, e2 = prime_factors[j]
                    for d2 in range(-e2, e2 + 1):
                        val2 = (d * s_list[i] + d2 * s_list[j]) % h
                        signed_set.add(val2)
    
    target_in_signed = target in signed_set
    full_coverage = len(signed_set) == h
    
    # Find shortest signed representation of h/2
    shortest_repr = None
    shortest_len = float('inf')
    
    # Try single-term
    for i, (p, e) in enumerate(prime_factors):
        for d in range(-e, e + 1):
            if (d * s_list[i]) % h == target:
                if 1 < shortest_len:
                    shortest_len = 1
                    shortest_repr = [(p, d)]
                    break
    
    # Try two-term
    if shortest_len > 2:
        for i in range(len(prime_factors)):
            p1, e1 = prime_factors[i]
            for d1 in range(-e1, e1 + 1):
                for j in range(i + 1, len(prime_factors)):
                    p2, e2 = prime_factors[j]
                    for d2 in range(-e2, e2 + 1):
                        if (d1 * s_list[i] + d2 * s_list[j]) % h == target:
                            if 2 < shortest_len:
                                shortest_len = 2
                                shortest_repr = [(p1, d1), (p2, d2)]
    
    # Try 3-term (limited search)
    if shortest_len > 3 and len(prime_factors) <= 8:
        for i in range(len(prime_factors)):
            p1, e1 = prime_factors[i]
            for d1 in range(-e1, e1 + 1):
                for j in range(i + 1, len(prime_factors)):
                    p2, e2 = prime_factors[j]
                    for d2 in range(-e2, e2 + 1):
                        partial = (d1 * s_list[i] + d2 * s_list[j]) % h
                        remaining = (target - partial) % h
                        for k in range(j + 1, len(prime_factors)):
                            p3, e3 = prime_factors[k]
                            s3 = s_list[k]
                            for d3 in range(-e3, e3 + 1):
                                if (d3 * s3) % h == remaining:
                                    if 3 < shortest_len:
                                        shortest_len = 3
                                        shortest_repr = [(p1, d1), (p2, d2), (p3, d3)]
    
    # Classify route type
    route_type = None
    route_detail = ""
    
    if has_order_2:
        p_order2 = order_2_primes[0]
        # Check if δ=1 works (it should: p^1 ≡ -1 mod A means s_i*1 = h/2)
        route_type = "1_order_2"
        s_p = s_values[p_order2]
        if s_p == target:
            route_detail = f"p={p_order2} ≡ -1 mod {A}, δ=1 → h/2={target}"
            if shortest_repr is None:
                shortest_repr = [(p_order2, 1)]
                shortest_len = 1
        else:
            route_detail = f"p={p_order2} has order 2, s={s_p}, h/2={target}"
    
    if route_type is None and shortest_len == 2:
        route_type = "2_two_term"
        route_detail = f"Two factors: {shortest_repr}"
    
    if route_type is None and shortest_len == 3:
        route_type = "3_short_signed"
        route_detail = f"Three factors: {shortest_repr}"
    
    if route_type is None and full_coverage:
        route_type = "4_full_coverage"
        route_detail = f"Σ_A(N) = Z/{h}Z"
    
    if route_type is None and target_in_signed:
        # Found but needed more terms
        route_type = "3_short_signed"
        route_detail = f"Shortest repr uses {shortest_len} terms: {shortest_repr}"
    
    if route_type is None and not target_in_signed:
        # Check m-route: does a factor of m contribute the decisive residue?
        m_factors_only = [(p, e) for p, e in prime_factors if p in factors_m and p not in factors_n]
        n_factors_only = [(p, e) for p, e in prime_factors if p in factors_n and p not in factors_m]
        
        # Check if target reachable using only m-factors
        if m_factors_only:
            m_signed_set = set()
            m_ranges = [range(-e, e + 1) for _, e in m_factors_only]
            m_s_list = [s_values[p] for p, _ in m_factors_only]
            m_total = 1
            for _, e in m_factors_only:
                m_total *= (2 * e + 1)
            if m_total <= 1_000_000:
                for combo in iterproduct(*m_ranges):
                    val = sum(d * s for d, s in zip(combo, m_s_list)) % h
                    m_signed_set.add(val)
                if target in m_signed_set:
                    route_type = "5_m_route"
                    route_detail = f"m-factor alone reaches h/2"
        
        if route_type is None:
            route_type = "6_exceptional"
            route_detail = f"Target not in signed set. |Σ|={len(signed_set)}/{h}"
    
    # Determine which factors come from n vs m
    n_factor_primes = set(factors_n.keys())
    m_factor_primes = set(factors_m.keys())
    
    # Check if n is QR mod A (direct route indicator)
    n_qr = legendre_symbol(n, A) == 1
    
    # Check if m has a QNR factor mod A
    m_has_qnr = any(legendre_symbol(p, A) == -1 for p, _ in prime_factors if p in m_factor_primes and p not in n_factor_primes)
    
    return {
        'n': n,
        'A': A,
        'N': N,
        'm': m,
        'h': h,
        'target': target,
        'prime_factors': [(p, e) for p, e in prime_factors],
        's_values': {str(p): s_values[p] for p, _ in prime_factors},
        'orders': orders,
        'stab_size': None,  # computed separately if needed
        'n_qr': n_qr,
        'm_has_qnr': m_has_qnr,
        'has_order_2': has_order_2,
        'order_2_primes': order_2_primes,
        'target_in_signed': target_in_signed,
        'full_coverage': full_coverage,
        'signed_set_size': len(signed_set),
        'shortest_repr': [(str(p), d) for p, d in shortest_repr] if shortest_repr else None,
        'shortest_len': shortest_len if shortest_repr else None,
        'route_type': route_type,
        'route_detail': route_detail,
        'n_factors': sorted(n_factor_primes),
        'm_factors': sorted(m_factor_primes),
    }

def main():
    print("=" * 80)
    print("THEOREM 3 FORWARD — CENTERED SIGNED-EXPONENT ANALYSIS")
    print("=" * 80)
    print()
    
    all_results = []
    route_counts = Counter()
    route_examples = defaultdict(list)
    
    # Analyze primes n ≡ 1 mod 12, n ≢ 0 mod 5, up to 100000
    n = 13
    count = 0
    while n <= 100000:
        if not isprime(n) or n % 12 != 1 or n % 5 == 0:
            n = int(nextprime(n))
            continue
        
        for A in PRIME_A:
            if gcd(n, A) > 1:
                continue
            
            result = compute_centered_criterion(n, A)
            if result is None:
                continue
            
            # Only care about cases where forward direction hypothesis is met
            # (h even and > 1, i.e., some QNR factor exists)
            if result['h'] <= 1 or result['h'] % 2 != 0:
                continue
            
            all_results.append(result)
            route_counts[result['route_type']] += 1
            if len(route_examples[result['route_type']]) < 3:
                route_examples[result['route_type']].append(result)
            
            count += 1
        
        n = int(nextprime(n))
    
    print(f"Total cases analyzed: {count}")
    print(f"Primes scanned: {sum(1 for r in all_results if r == all_results[0] or True) // len(PRIME_A)}")
    print()
    
    # Route type summary
    print("=== ROUTE TYPE CLASSIFICATION ===")
    print()
    route_names = {
        '1_order_2': 'Order-2 route (p ≡ -1 mod A)',
        '2_two_term': 'Two-term centered route',
        '3_short_signed': 'Short signed route (3+ terms)',
        '4_full_coverage': 'Full interval coverage (Σ = Z/hZ)',
        '5_m_route': 'm-route (m-factor decisive)',
        '6_exceptional': 'Exceptional/structured',
    }
    
    for rt in sorted(route_counts.keys()):
        name = route_names.get(rt, rt)
        count_rt = route_counts[rt]
        pct = 100 * count_rt / len(all_results)
        print(f"  {rt}: {name}")
        print(f"    Count: {count_rt} ({pct:.1f}%)")
        if route_examples[rt]:
            ex = route_examples[rt][0]
            print(f"    Example: n={ex['n']}, A={ex['A']}, h={ex['h']}, "
                  f"|Σ|={ex['signed_set_size']}/{ex['h']}")
            if ex['shortest_repr']:
                print(f"    Shortest: {ex['shortest_repr']}")
            print(f"    Detail: {ex['route_detail']}")
        print()
    
    # Check: are there ANY failures (target not in signed set)?
    failures = [r for r in all_results if not r['target_in_signed']]
    print(f"=== FAILURE ANALYSIS ===")
    print(f"Cases where h/2 ∉ Σ_A(N): {len(failures)} ({100*len(failures)/len(all_results):.1f}%)")
    
    if failures:
        print()
        print("Failure breakdown by h:")
        h_fail = Counter(r['h'] for r in failures)
        for h, c in sorted(h_fail.items()):
            print(f"  h={h}: {c} failures")
        
        print()
        print("Failure breakdown by A:")
        A_fail = Counter(r['A'] for r in failures)
        for A, c in sorted(A_fail.items()):
            print(f"  A={A}: {c} failures")
        
        print()
        print("Sample failures:")
        for f in failures[:10]:
            print(f"  n={f['n']}, A={f['A']}, h={f['h']}, "
                  f"|Σ|={f['signed_set_size']}/{f['h']}, "
                  f"n_qr={f['n_qr']}, m_has_qnr={f['m_has_qnr']}")
    else:
        print("*** ALL CASES SATISFY h/2 ∈ Σ_A(N) ***")
        print("The centered criterion holds universally in tested range!")
    
    # Analyze h/2 parity in signed set
    print()
    print("=== SIGNED SET SIZE ANALYSIS ===")
    size_ratios = []
    for r in all_results:
        ratio = r['signed_set_size'] / r['h']
        size_ratios.append(ratio)
    
    import statistics
    print(f"  Mean |Σ|/h: {statistics.mean(size_ratios):.3f}")
    print(f"  Median |Σ|/h: {statistics.median(size_ratios):.3f}")
    print(f"  Min |Σ|/h: {min(size_ratios):.3f}")
    print(f"  Max |Σ|/h: {max(size_ratios):.3f}")
    
    full_cov = sum(1 for r in all_results if r['full_coverage'])
    print(f"  Full coverage (Σ = Z/hZ): {full_cov} ({100*full_cov/len(all_results):.1f}%)")
    
    # Save results
    output = {
        'total_cases': len(all_results),
        'route_counts': dict(route_counts),
        'failure_count': len(failures),
        'failures': [
            {
                'n': f['n'], 'A': f['A'], 'h': f['h'],
                'signed_set_size': f['signed_set_size'],
                'n_qr': f['n_qr'], 'm_has_qnr': f['m_has_qnr'],
                'route_type': f['route_type'],
            } for f in failures
        ] if failures else [],
    }
    
    with open('centered_analysis_results.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print()
    print("Results saved to centered_analysis_results.json")
    
    # Key finding
    print()
    print("=" * 80)
    if not failures:
        print("KEY FINDING: The centered signed-exponent criterion h/2 ∈ Σ_A(N)")
        print("holds for ALL tested prime-A cases (n ≤ 100,000).")
        print("This is a strictly stronger result than the old D_A criterion.")
        print("The forward direction may be provable through this framework.")
    else:
        print(f"KEY FINDING: {len(failures)} failures remain in the centered framework.")
        print("These need covering-set analysis (same as before, but fewer cases).")
    print("=" * 80)

if __name__ == "__main__":
    main()