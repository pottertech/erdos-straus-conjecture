#!/usr/bin/env python3
"""
Fast 100M-1B verification using modular pre-filtering.
Only ~1/12 of primes are ≡ 1 mod 12, and only ~1/15 of those are hard cases.
Skip the expensive factorization for the vast majority.
"""
import sympy
from sympy import isprime, nextprime
import time, json

def has_prime_factor_2mod3(n, limit=50000):
    """Check if n has a prime factor ≡ 2 mod 3, using trial division up to limit.
    Returns True if such a factor is found (NOT a hard case).
    Returns False if no small factor ≡ 2 mod 3 found (might be hard case)."""
    temp = n
    # Strip factor 2
    while temp % 2 == 0:
        temp //= 2
    # Strip factor 3
    while temp % 3 == 0:
        temp //= 3
    # Check odd primes 5, 7, 11, ...
    p = 5
    while p <= limit and temp > 1:
        if temp % p == 0:
            if p % 3 == 2:
                return True
            while temp % p == 0:
                temp //= p
        p += 2
        if p % 3 == 2:
            # p itself is ≡ 2 mod 3, but we check if it divides temp
            pass
    # If temp > 1, it's a large factor
    if temp > 1:
        if temp > limit * limit:
            # Could be composite — try one round of Pollard rho
            try:
                d = sympy.ntheory.factor_.pollard_rho(temp, retries=3)
                if d and d % 3 == 2:
                    return True
                if d:
                    other = temp // d
                    if other % 3 == 2:
                        return True
                    # Both factors ≡ 1 mod 3 → not found
                    return False
            except:
                pass
        # Small enough or Pollard failed — check directly
        if temp % 3 == 2:
            return True
        if not isprime(temp):
            # Composite — try trial division a bit more
            for p in range(limit, min(limit*10, temp)):
                if temp % p == 0:
                    if p % 3 == 2:
                        return True
                    temp2 = temp // p
                    if temp2 % 3 == 2:
                        return True
                    break
    return False

def solve_umethod_fast(n, max_u=255):
    """Check u-method with fast divisor computation."""
    for u in range(3, max_u + 1, 4):
        if not isprime(u):
            continue
        x = (n + u) // 4
        if x < 1:
            continue
        
        # Factor x using trial division (x ~ n/4 ~ 25M-250M)
        factors = {}
        temp = x
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            if temp == 1:
                break
            while temp % p == 0:
                factors[p] = factors.get(p, 0) + 1
                temp //= p
        
        # For remaining, use sympy factorint with small limit
        if temp > 1:
            if isprime(temp):
                factors[temp] = 1
            else:
                try:
                    rest = sympy.factorint(temp, limit=10000)
                    factors.update(rest)
                except:
                    factors[temp] = 1
        
        # Compute divisors of x² mod u (early exit)
        inv4 = pow(4, -1, u)
        x_mod = (n * inv4) % u
        n_mod = n % u
        n2_mod = (n_mod * n_mod) % u
        targets = [(-x_mod) % u, (-x_mod * n_mod) % u, (-x_mod * n2_mod) % u]
        
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
            # Early exit
            if any(t in reachable for t in targets):
                return True, u
        
        if any(t in reachable for t in targets):
            return True, u
    return False, None

start = time.time()
print("Fast verification: Prime hard cases 100M to 1B")
print("=" * 70)

count = 0
max_a = 0
failures = []
a_dist = {}
n = nextprime(100000000)
last_report = time.time()
total_primes = 0

while n < 1000000000:
    total_primes += 1
    
    # Fast pre-filter: n ≡ 1 mod 12 and n ≢ 0 mod 5
    if n % 12 == 1 and n % 5 != 0:
        # Check B₃ condition: all odd prime factors ≡ 1 mod 3
        B3 = n * (n + 3) // 4
        if not has_prime_factor_2mod3(B3, limit=50000):
            # Likely hard case — verify and solve
            success, u_used = solve_umethod_fast(n, max_u=255)
            count += 1
            if success:
                max_a = max(max_a, u_used)
                a_dist[u_used] = a_dist.get(u_used, 0) + 1
            else:
                failures.append(n)
                print(f"  ❌ FAILURE at n={n}")
    
    n = nextprime(n)
    
    # Heartbeat every 30s
    now = time.time()
    if now - last_report > 30:
        elapsed = now - start
        rate = total_primes / elapsed
        print(f"  [hb] n={n:,} primes={total_primes:,} hard={count} "
              f"max_A={max_a} fails={len(failures)} "
              f"rate={rate:.0f}p/s elapsed={elapsed:.0f}s")
        last_report = now

elapsed = time.time() - start
print()
print("=" * 70)
print(f"RESULTS: 100M to 1B")
print(f"  Total primes checked: {total_primes:,}")
print(f"  Hard cases found: {count:,}")
print(f"  Failures: {len(failures)}")
print(f"  Max A: {max_a}")
print(f"  Runtime: {elapsed:.0f}s ({elapsed/3600:.1f}h)")

if failures:
    print(f"  FAILURES: {failures[:50]}")

print(f"\nA distribution:")
for u in sorted(a_dist.keys()):
    print(f"  A={u:3d}: {a_dist[u]:6d} ({a_dist[u]/count*100:.1f}%)")

results = {
    "range": "100M to 1B",
    "total_primes": total_primes,
    "total_hard": count,
    "failures": len(failures),
    "max_a": max_a,
    "failures_list": failures[:100],
    "a_distribution": a_dist,
    "runtime_seconds": elapsed,
}

with open('verification_100M_1B.json', 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to verification_100M_1B.json")