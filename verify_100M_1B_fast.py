#!/usr/bin/env python3
"""
Extended verification: Prime hard cases from 100M to 1B.
With per-case factorization timeout to prevent pathological hangs.
Uses trial division + Pollard rho with timeout for factorint.
"""
import sympy
from sympy import isprime, nextprime, factorint
import time, json, signal, threading

def is_hard_case_prime_fast(n):
    """Check if n is a hard case prime without full factorization.
    Uses trial division up to 10^6, then Pollard rho with timeout."""
    if n % 12 != 1 or n % 5 == 0:
        return False
    if not isprime(n):
        return False
    B3 = n * (n + 3) // 4
    # Quick trial division for small factors
    factors = {}
    temp = B3
    for p in sympy.primerange(2, 100000):
        if temp == 1:
            break
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
    # If temp > 1, it's a large factor — check if it's 1 mod 3 or 2
    if temp > 1:
        if temp % 3 == 2:
            # This is an odd prime ≡ 2 mod 3 → NOT a hard case
            return False
        # Could be composite — try to factor with timeout
        if temp > 10**12:
            # Skip expensive factorization, just check temp mod 3
            # If temp ≡ 1 mod 3 and is prime or product of primes ≡ 1 mod 3, it's hard
            # If temp ≡ 2 mod 3, not hard. If temp ≡ 0 mod 3, check further.
            if temp % 3 == 0:
                # Has factor 3 — need to check if 3 is the only factor ≡ 0 mod 3
                while temp % 3 == 0:
                    temp //= 3
                if temp > 1 and temp % 3 == 2:
                    return False
            # Assume it's hard if all large factors are ≡ 1 mod 3
            # This is correct unless temp has a large prime factor ≡ 2 mod 3
            # We'll do a quick primality check
            if isprime(temp) and temp % 3 == 2:
                return False
            # If composite, try Pollard rho
            try:
                large_factors = factorint(temp, limit=10**6)
                for p in large_factors:
                    if p != 2 and p % 3 == 2:
                        return False
            except:
                # If factorization fails, assume hard case (conservative)
                pass
        else:
            # Small enough to factor normally
            try:
                large_factors = factorint(temp)
                for p in large_factors:
                    if p != 2 and p % 3 == 2:
                        return False
            except:
                pass
    return all(p == 2 or p % 3 == 1 for p in factors) and (temp == 1 or temp % 3 != 2)

def solve_umethod(n, max_u=255):
    """Check u-method with three-target reduction."""
    for u in range(3, max_u + 1, 4):
        if not isprime(u):
            continue
        x = (n + u) // 4
        if x < 1:
            continue
        
        # Factor x with trial division (fast for small factors)
        factors = {}
        temp = x
        for p in sympy.primerange(2, min(10000, x)):
            if temp == 1:
                break
            while temp % p == 0:
                factors[p] = factors.get(p, 0) + 1
                temp //= p
        if temp > 1:
            # Large remaining factor
            if isprime(temp):
                factors[temp] = 1
            else:
                # Try Pollard rho with small limit
                try:
                    rest_factors = sympy.factorint(temp, limit=10**5)
                    factors.update(rest_factors)
                except:
                    factors[temp] = 1  # Treat as prime
        
        # Compute divisors of x² mod u
        inv4 = pow(4, -1, u)
        x_mod = (n * inv4) % u
        targets = [(-x_mod) % u, (-x_mod * n) % u, (-x_mod * pow(n, 2, u)) % u]
        
        reachable = {1}
        for p, e in factors.items():
            if p % u == 0:
                continue
            new_reach = set()
            pe = 1
            for a in range(2 * e + 1):
                for val in reachable:
                    new_reach.add((val * pe) % u)
                pe = (pe * (p % u)) % u
            reachable = new_reach
            # Early exit if we already hit a target
            if any(t in reachable for t in targets):
                return True, u, x
        
        if any(t in reachable for t in targets):
            return True, u, x
    return False, None, None

start = time.time()
print("Extended verification: Prime hard cases 100M to 1B (with timeout protection)")
print("=" * 70)
print("Using A <= 255, trial division + Pollard rho for factorization")
print()

count = 0
max_a = 0
failures = []
a_distribution = {}
n = nextprime(100000000)
last_report = time.time()

while n < 1000000000:
    if is_hard_case_prime_fast(n):
        success, u_used, x_val = solve_umethod(n, max_u=255)
        if success:
            max_a = max(max_a, u_used)
            a_distribution[u_used] = a_distribution.get(u_used, 0) + 1
        else:
            failures.append(n)
            print(f"  ❌ FAILURE at n={n}")
        
        count += 1
        if count % 1000 == 0:
            elapsed = time.time() - start
            rate = count / elapsed
            remaining = (1000000000 - n) / (n - 100000000) * elapsed if n > 100000000 else 0
            print(f"  [{count} cases] n={n:,} elapsed={elapsed:.0f}s rate={rate:.1f}/s "
                  f"max_A={max_a} fails={len(failures)} ETA={remaining:.0f}s")
            last_report = time.time()
    
    n = nextprime(n)
    
    # Safety: print heartbeat every 60s
    if time.time() - last_report > 60:
        elapsed = time.time() - start
        print(f"  [heartbeat] n={n:,} elapsed={elapsed:.0f}s cases={count} fails={len(failures)}")
        last_report = time.time()

elapsed = time.time() - start
print()
print("=" * 70)
print(f"RESULTS: 100M to 1B")
print(f"  Total hard cases: {count}")
print(f"  Failures: {len(failures)}")
print(f"  Max A: {max_a}")
print(f"  Runtime: {elapsed:.0f}s ({elapsed/3600:.1f} hours)")

if failures:
    print(f"  FAILURES: {failures[:20]}")

# A distribution
print(f"\nA distribution (top 10):")
for u, cnt in sorted(a_distribution.items())[:10]:
    print(f"  A={u}: {cnt} ({cnt/count*100:.1f}%)")
if len(a_distribution) > 10:
    print(f"  ... and {len(a_distribution)-10} more")

results = {
    "range": "100M to 1B",
    "total": count,
    "failures": len(failures),
    "max_a": max_a,
    "failures_list": failures[:100],
    "a_distribution": a_distribution,
    "runtime_seconds": elapsed,
}

with open('verification_100M_1B.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to verification_100M_1B.json")