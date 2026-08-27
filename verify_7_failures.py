#!/usr/bin/env python3
"""
Investigate the 7 failures from the 1B verification run.
These are prime hard cases where no u-method solution was found with u <= 255.
We'll search with much larger u (up to 2000) and characterize each case.
"""

import sympy
from sympy import factorint, isprime, jacobi_symbol
import json
import time

def is_hard_case(n):
    """Check if n is a hard case for Erdős-Straus."""
    if n < 2:
        return False
    if n % 12 != 1:
        return False
    if n % 5 == 0:
        return False
    B3 = n * (n + 3) // 4
    if B3 % 2 == 0:
        B3_odd = B3
        while B3_odd % 2 == 0:
            B3_odd //= 2
    else:
        B3_odd = B3
    # Remove factor 2
    while B3_odd % 2 == 0:
        B3_odd //= 2
    # Check all odd prime factors of B3 are ≡ 1 mod 3
    for p in factorint(B3_odd).keys():
        if p % 3 != 1:
            return False
    return True

def u_method_search(n, u_max=2000):
    """
    Search for u-method solution with u up to u_max.
    u must be ≡ 3 mod 4 (so that x = (n+u)/4 is integer, since n ≡ 1 mod 12 → n ≡ 1 mod 4).
    Returns (min_u, x, y, z, j_target, is_parametric) or None.
    """
    for u in range(3, u_max + 1, 4):  # u ≡ 3 mod 4
        if (n + u) % 4 != 0:
            continue
        x = (n + u) // 4
        if x <= 0:
            continue
        
        # D = n^2 * x^2
        D = n * n * x * x
        
        # Three-target reduction: need d' | x^2 with d' ≡ -x*n^j mod u for j in {0,1,2}
        # Equivalently: need d | D with d ≡ -nx mod u, d <= sqrt(D), u | (d + nx)
        
        # For small u, we can enumerate divisors of D mod u
        # But D is huge. Instead, factor x and enumerate divisors of x^2 mod u.
        
        x_factors = factorint(x)
        
        # Generate all divisors of x^2 mod u
        # x^2 has prime factorization with exponents doubled
        x2_factors = {p: 2*e for p, e in x_factors.items()}
        
        # Generate divisors of x^2 mod u
        divs_x2 = set()
        # Start with 1
        divs_x2.add(1 % u)
        
        for p, max_exp in x2_factors.items():
            p_mod = p % u
            new_divs = set()
            pe = 1  # p^0
            for e in range(max_exp + 1):
                for d in divs_x2:
                    val = (d * pe) % u
                    new_divs.add(val)
                pe = (pe * p_mod) % u
            divs_x2 = new_divs
        
        # Targets: -x * n^j mod u for j in {0, 1, 2}
        x_mod = x % u
        n_mod = n % u
        
        targets = set()
        nj = 1
        for j in range(3):
            t = (-x_mod * nj) % u
            targets.add(t)
            nj = (nj * n_mod) % u
        
        # Check if any divisor of x^2 hits any target
        hit = divs_x2 & targets
        if hit:
            # Found a solution! Determine which target
            for t in hit:
                # Find which j
                nj = 1
                for j in range(3):
                    if (-x_mod * nj) % u == t:
                        break
                    nj = (nj * n_mod) % u
                
                # Reconstruct the actual divisor d' of x^2
                # and then d = n^(2-j) * d' (since a = 2-j)
                a = 2 - j
                # d = n^a * d', d' = t's corresponding divisor
                
                # Find the actual d' (divisor of x^2 that equals t mod u)
                # We need to find which divisor gives this residue
                # For the parametric check: d' | x (j=0 or j=1 with a=2 or a=1)
                # is_parametric if d' | x (not just x^2)
                
                # Check parametric: does x have a divisor hitting j=0 or j=1 target?
                divs_x = set()
                divs_x.add(1 % u)
                for p, max_exp in x_factors.items():
                    p_mod = p % u
                    new_divs = set()
                    pe = 1
                    for e in range(max_exp + 1):
                        for d in divs_x:
                            val = (d * pe) % u
                            new_divs.add(val)
                        pe = (pe * p_mod) % u
                    divs_x = new_divs
                
                param_targets = set()
                nj = 1
                for jj in range(2):  # j=0, j=1
                    t_p = (-x_mod * nj) % u
                    param_targets.add(t_p)
                    nj = (nj * n_mod) % u
                
                is_parametric = bool(divs_x & param_targets)
                
                return (u, x, is_parametric, j, len(divs_x2), len(divs_x))
        
        # Also check via direct divisor enumeration for small cases
        # D = n^2 * x^2, need d | D, d ≡ -nx mod u, d <= sqrt(D) = nx
        nx = n * x
        target_d = (-nx) % u
        # Check if any divisor of D up to nx has this residue
        # This is equivalent to the three-target check above
        
    return None

def characterize_case(n):
    """Full characterization of a prime hard case."""
    print(f"\n{'='*70}")
    print(f"n = {n:,} (prime={isprime(n)})")
    print(f"n mod 24 = {n % 24}")
    print(f"n mod 120 = {n % 120}")
    
    # Factor n+u for various u
    print(f"\nFactorizations of x = (n+u)/4:")
    for u in [3, 7, 11, 23, 47, 59, 79, 83, 103, 107, 127, 151, 179, 199, 251]:
        if (n + u) % 4 != 0:
            continue
        x = (n + u) // 4
        factors = factorint(x)
        omega_x = len(factors)
        jacobi_n_u = jacobi_symbol(n, u) if isprime(u) else None
        print(f"  u={u:3d}: x={x}, ω(x)={omega_x}, factors={factors}, (n/u)={jacobi_n_u}")
    
    # Search for solution
    print(f"\nSearching u up to 2000...")
    t0 = time.time()
    result = u_method_search(n, u_max=2000)
    t1 = time.time()
    
    if result:
        u, x, is_param, j, n_divs_x2, n_divs_x = result
        print(f"  FOUND: u={u}, x={x}, parametric={is_param}, j-target={j}")
        print(f"  |divs(x²)| mod u = {n_divs_x2}, |divs(x)| mod u = {n_divs_x}")
        print(f"  Time: {t1-t0:.1f}s")
        
        # Compute actual y, z
        D = n * n * x * x
        nx = n * x
        # Find the actual divisor
        # d₁ ≡ -nx mod u, d₁ | D, d₁ <= sqrt(D)
        target = (-nx) % u
        # Enumerate divisors of D up to nx
        # D = n^2 * x^2, divisors are products of divisors of n and x
        # n is prime, so divisors of n^2 = {1, n, n^2}
        # divisors of x^2: all products of p^(0..2e) for p^e || x
        
        x_factors = factorint(x)
        divs_x2_list = [1]
        for p, e in x_factors.items():
            new_list = []
            for d in divs_x2_list:
                pe = 1
                for exp in range(2*e + 1):
                    new_list.append(d * pe)
                    pe *= p
            divs_x2_list = new_list
        
        # Full divisors of D = n^2 * x^2
        found = False
        for a in range(3):  # n^a
            na = n ** a
            for d_prime in divs_x2_list:
                d1 = na * d_prime
                if d1 > nx:
                    continue
                if d1 % u == target:
                    d2 = D // d1
                    if (d1 + nx) % u == 0 and (d2 + nx) % u == 0:
                        y = (d1 + nx) // u
                        z = (d2 + nx) // u
                        zy_ratio = z / y if y != 0 else None
                        print(f"  Solution: x={x}, y={y}, z={z}")
                        print(f"  z/y = {zy_ratio} (integer={'Yes' if z % y == 0 else 'No'})")
                        print(f"  d₁ = {d1}, d₂ = {d2}")
                        found = True
                        break
            if found:
                break
        
        return {'n': n, 'min_u': u, 'parametric': is_param, 'j_target': j, 'time': t1-t0}
    else:
        print(f"  NO SOLUTION found with u ≤ 2000")
        print(f"  Time: {t1-t0:.1f}s")
        return {'n': n, 'min_u': None, 'parametric': None, 'j_target': None, 'time': t1-t0}

# The 7 failures from the 1B run
failures = [
    71310241,
    318545761,
    340912609,
    360055609,
    524792461,
    550027501,
    923573401,
]

print("Investigating 7 failures from 1B verification run")
print("="*70)

results = []
for n in failures:
    # Verify hard case
    hc = is_hard_case(n)
    print(f"\nn={n:,}: prime={isprime(n)}, hard_case={hc}")
    if hc:
        r = characterize_case(n)
        results.append(r)
    else:
        print("  NOT a hard case — skipping")

print(f"\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")
for r in results:
    print(f"  n={r['n']:,}: min_u={r['min_u']}, parametric={r['parametric']}, j={r['j_target']}, time={r['time']:.1f}s")

# Save results
with open('failure_analysis_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("\nResults saved to failure_analysis_results.json")