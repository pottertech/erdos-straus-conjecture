#!/usr/bin/env python3
"""
Extended verification: Prime hard cases from 100M to 1B.
Checks u-method with A <= 255 (extended range to catch new outliers).
"""
import sympy
from sympy import isprime, factorint, nextprime
import time, json

def is_hard_case_prime(n):
    if n % 12 != 1 or n % 5 == 0:
        return False
    B3 = n * (n + 3) // 4
    factors = factorint(B3)
    return all(p == 2 or p % 3 == 1 for p in factors)

def solve_umethod(n, max_u=255):
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
        reachable = {1}
        for p, e in factors.items():
            if p == u: continue
            new_reach = set()
            for val in reachable:
                for a in range(2 * e + 1):
                    new_reach.add((val * pow(p, a, u)) % u)
            reachable = new_reach
        if any(t in reachable for t in targets):
            return True, u, x
    return False, None, None

start = time.time()
print("Extended verification: Prime hard cases 100M to 1B")
print("=" * 60)
print("Using A <= 255 to catch any new outliers beyond A=127")
print()

count = 0
max_a = 0
failures = []
a_distribution = {}
n = nextprime(100000000)

while n < 1000000000:
    if is_hard_case_prime(n):
        success, u_used, x_val = solve_umethod(n, max_u=255)
        if success:
            max_a = max(max_a, u_used)
            a_distribution[u_used] = a_distribution.get(u_used, 0) + 1
        else:
            failures.append(n)
        
        count += 1
        if count % 10000 == 0:
            elapsed = time.time() - start
            print(f"  {count} cases, n={n}, {elapsed:.0f}s, max_A={max_a}, fails={len(failures)}")
    
    n = nextprime(n)

elapsed = time.time() - start
print()
print("=" * 60)
print(f"RESULTS: 100M to 1B")
print(f"  Total: {count}, Failures: {len(failures)}, Max A: {max_a}")
print(f"  Runtime: {elapsed:.0f}s ({elapsed/3600:.1f} hours)")

if failures:
    print(f"  FAILURES: {failures[:20]}")

results = {
    "range": "100M to 1B",
    "total": count, "failures": len(failures), "max_a": max_a,
    "runtime": elapsed, "a_distribution": a_distribution, "failure_list": failures[:100]
}
with open("verification_100M_1B.json", "w") as f:
    json.dump(results, f, indent=2)
print("Saved to verification_100M_1B.json")
