#!/usr/bin/env python3
"""
Exhaustive verification of prime hard cases from 100M to 1B.
Corrected u-method implementation with complete divisor enumeration.
Search u up to 300 (≡ 3 mod 4), with full three-target check.
"""

import sympy
from sympy import factorint, isprime, jacobi_symbol
import json
import time
import sys

def is_hard_case_fast(n, n_mod_12, n_mod_5):
    """Fast hard case check using precomputed residues."""
    if n_mod_12 != 1:
        return False
    if n_mod_5 == 0:
        return False
    # Check B3 = n*(n+3)/4, all odd prime factors ≡ 1 mod 3
    B3 = n * (n + 3) // 4
    # Remove factor 2
    while B3 % 2 == 0:
        B3 //= 2
    # Also remove factor 3 (since 3 ≡ 0 mod 3, not ≡ 1)
    # Wait - the condition is all ODD prime factors of B3 ≡ 1 mod 3
    # 3 is odd and 3 ≡ 0 mod 3, so if 3 | B3, it's NOT a hard case
    # Actually re-read: "all odd prime factors of B3 ≡ 1 mod 3"
    # 3 is an odd prime, 3 mod 3 = 0 ≠ 1, so 3 | B3 means NOT hard case
    if B3 % 3 == 0:
        return False
    for p in factorint(B3).keys():
        if p % 3 != 1:
            return False
    return True

def u_method_solve(n, u_max=300):
    """
    Find minimum u (≡ 3 mod 4) such that the u-method works.
    Uses complete divisor enumeration of x^2 mod u.
    Returns (min_u, is_parametric, j_target) or None.
    """
    n_mod = n  # for mod operations
    
    for u in range(3, u_max + 1, 4):  # u ≡ 3 mod 4
        if (n + u) % 4 != 0:
            continue
        x = (n + u) // 4
        if x <= 0:
            continue
        
        # Factor x
        x_factors = factorint(x)
        
        # Generate all divisors of x^2 mod u
        # x^2 has exponents doubled
        x2_exp = {p: 2*e for p, e in x_factors.items()}
        
        # Generate divisors of x^2 mod u using iterative approach
        divs_x2_mod = {1 % u}
        for p, max_e in x2_exp.items():
            p_mod = p % u
            if p_mod == 0:
                continue  # p | u, skip (divisor is 0 mod u, useless)
            new_divs = set()
            pe = 1
            for e in range(max_e + 1):
                for d in divs_x2_mod:
                    new_divs.add((d * pe) % u)
                pe = (pe * p_mod) % u
            divs_x2_mod = new_divs
        
        # Generate divisors of x mod u (for parametric check)
        divs_x_mod = {1 % u}
        for p, max_e in x_factors.items():
            p_mod = p % u
            if p_mod == 0:
                continue
            new_divs = set()
            pe = 1
            for e in range(max_e + 1):
                for d in divs_x_mod:
                    new_divs.add((d * pe) % u)
                pe = (pe * p_mod) % u
            divs_x_mod = new_divs
        
        # Three targets: -x * n^j mod u for j in {0, 1, 2}
        x_mod = x % u
        n_mod_u = n % u
        
        # Compute targets
        targets = []
        nj = 1
        for j in range(3):
            t = (-x_mod * nj) % u
            targets.append(t)
            nj = (nj * n_mod_u) % u
        
        # Check u-method: any divisor of x^2 hits any target
        hit = False
        j_hit = -1
        for j, t in enumerate(targets):
            if t in divs_x2_mod:
                hit = True
                j_hit = j
                break
        
        if not hit:
            continue
        
        # Check parametric: divisors of x hit targets j=0 or j=1
        is_parametric = (targets[0] in divs_x_mod) or (targets[1] in divs_x_mod)
        
        return (u, is_parametric, j_hit, len(divs_x2_mod), len(divs_x_mod))
    
    return None

def verify_range(start, end, u_max=300, batch_log=10000):
    """Verify all prime hard cases in [start, end]."""
    t0 = time.time()
    
    # Find all primes in range
    # For large ranges, use sympy primerange
    
    results = {
        'range': [start, end],
        'u_max': u_max,
        'total_primes': 0,
        'total_hard_cases': 0,
        'solved': 0,
        'failures': [],
        'max_A': 0,
        'max_A_n': 0,
        'A_distribution': {},
        'non_parametric_count': 0,
        'non_parametric_cases': [],
    }
    
    count = 0
    last_log = time.time()
    
    for n in sympy.sieve.primerange(start, end + 1):
        results['total_primes'] += 1
        count += 1
        
        n_mod_12 = n % 12
        n_mod_5 = n % 5
        
        if not is_hard_case_fast(n, n_mod_12, n_mod_5):
            continue
        
        results['total_hard_cases'] += 1
        
        # Solve
        result = u_method_solve(n, u_max=u_max)
        
        if result:
            u, is_param, j, n_d2, n_d1 = result
            results['solved'] += 1
            
            # Track A distribution
            results['A_distribution'][u] = results['A_distribution'].get(u, 0) + 1
            
            if u > results['max_A']:
                results['max_A'] = u
                results['max_A_n'] = n
            
            if not is_param:
                results['non_parametric_count'] += 1
                if len(results['non_parametric_cases']) < 100:  # Keep first 100
                    results['non_parametric_cases'].append({
                        'n': n, 'u': u, 'j': j
                    })
        else:
            results['failures'].append(n)
            if len(results['failures']) <= 50:
                print(f"  FAILURE: n={n:,}", flush=True)
        
        # Log progress
        now = time.time()
        if now - last_log > 30:
            elapsed = now - t0
            rate = results['total_hard_cases'] / elapsed if elapsed > 0 else 0
            print(f"  Progress: {count:,} primes, {results['total_hard_cases']:,} hard cases, "
                  f"{results['solved']:,} solved, {len(results['failures'])} failures, "
                  f"max_A={results['max_A']}, rate={rate:.0f}/s, "
                  f"elapsed={elapsed:.0f}s", flush=True)
            last_log = now
    
    t1 = time.time()
    results['runtime_seconds'] = t1 - t0
    
    return results

if __name__ == '__main__':
    # Parse args
    if len(sys.argv) >= 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    else:
        start = 100_000_001
        end = 200_000_000
    
    u_max = 300
    if len(sys.argv) >= 4:
        u_max = int(sys.argv[3])
    
    print(f"Verifying prime hard cases from {start:,} to {end:,} with u_max={u_max}")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = verify_range(start, end, u_max=u_max)
    
    print(f"\n{'='*60}")
    print(f"RESULTS: {start:,} to {end:,}")
    print(f"{'='*60}")
    print(f"Total primes: {results['total_primes']:,}")
    print(f"Total hard cases: {results['total_hard_cases']:,}")
    print(f"Solved: {results['solved']:,}")
    print(f"Failures: {len(results['failures'])}")
    if results['failures']:
        print(f"Failed cases: {results['failures'][:20]}")
    print(f"Max A: {results['max_A']} (at n={results['max_A_n']:,})")
    print(f"Non-parametric: {results['non_parametric_count']:,}")
    print(f"Runtime: {results['runtime_seconds']:.1f}s")
    
    # A distribution
    print(f"\nA distribution:")
    for u in sorted(results['A_distribution'].keys()):
        cnt = results['A_distribution'][u]
        pct = 100 * cnt / results['solved'] if results['solved'] > 0 else 0
        print(f"  A={u:3d}: {cnt:6d} ({pct:5.1f}%)")
    
    # Save results
    fname = f'verification_{start}_{end}.json'
    with open(fname, 'w') as f:
        # Convert non-serializable items
        out = {k: v for k, v in results.items()}
        json.dump(out, f, indent=2)
    print(f"\nResults saved to {fname}")