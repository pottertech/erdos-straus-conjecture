#!/usr/bin/env python3
"""
Extended verification: Prime hard cases from 10M to 100M.
Checks that u-method with A <= 107 solves all prime hard cases.
"""

import sympy
from sympy import isprime, factorint, nextprime
import time
import json

def is_hard_case_prime(n):
    """Check if prime n is a hard case."""
    if n % 12 != 1 or n % 5 == 0:
        return False
    B3 = n * (n + 3) // 4
    factors = factorint(B3)
    for p in factors:
        if p == 2:
            continue
        if p % 3 != 1:
            return False
    return True

def solve_umethod(n, max_u=107):
    """Try u-method with u <= max_u. Return (success, u_used, x_val)."""
    for u in range(3, max_u + 1, 4):
        if not isprime(u):
            continue
        x = (n + u) // 4
        if x < 1:
            continue
        factors = factorint(x)
        
        inv4 = pow(4, -1, u)
        x_mod = (n * inv4) % u
        targets = [(-x_mod) % u, (-x_mod * n) % u, (-x_mod * n * n) % u]
        
        # Build reachable divisor set of x^2 mod u
        reachable = {1}
        for p, e in factors.items():
            if p == u:
                continue
            new_reach = set()
            for val in reachable:
                for a in range(2 * e + 1):
                    new_reach.add((val * pow(p, a, u)) % u)
            reachable = new_reach
        
        if any(t in reachable for t in targets):
            return True, u, x
    
    return False, None, None

# Verify
start = time.time()
print("Extended verification: Prime hard cases 10M to 100M")
print("=" * 60)

hard_cases = []
n = nextprime(10000000)
count = 0
max_a = 0
failures = []
a_distribution = {}

while n < 100000000:
    if is_hard_case_prime(n):
        hard_cases.append(n)
        success, u_used, x_val = solve_umethod(n, max_u=107)
        if success:
            max_a = max(max_a, u_used)
            a_distribution[u_used] = a_distribution.get(u_used, 0) + 1
        else:
            failures.append(n)
        
        count += 1
        if count % 5000 == 0:
            elapsed = time.time() - start
            print(f"  {count} hard cases checked, n={n}, elapsed={elapsed:.0f}s, max_A={max_a}, failures={len(failures)}")
    
    n = nextprime(n)

elapsed = time.time() - start
print()
print("=" * 60)
print(f"RESULTS: 10M to 100M")
print(f"  Total prime hard cases: {count}")
print(f"  Failures (A > 107): {len(failures)}")
print(f"  Max A: {max_a}")
print(f"  Runtime: {elapsed:.0f}s ({elapsed/60:.1f} min)")
print()

if failures:
    print(f"FAILURES: {failures[:20]}")
else:
    print("NO FAILURES - all solved with A <= 107")

print()
print("A distribution:")
for a in sorted(a_distribution.keys()):
    pct = a_distribution[a] / count * 100
    bar = '#' * int(pct)
    print(f"  A={a:3d}: {a_distribution[a]:6d} ({pct:5.1f}%) {bar}")

# Save results
results = {
    "range": "10M to 100M",
    "total_hard_cases": count,
    "failures": len(failures),
    "max_a": max_a,
    "runtime_seconds": elapsed,
    "a_distribution": a_distribution,
    "failure_list": failures[:100],
}
with open("verification_10M_100M.json", "w") as f:
    json.dump(results, f, indent=2)

print()
print("Results saved to verification_10M_100M.json")
