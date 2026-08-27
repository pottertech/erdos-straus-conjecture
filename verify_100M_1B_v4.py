#!/usr/bin/env python3
"""
Ultra-fast 100M-1B verification using sympy primerange + fast hard-case check.
Key optimization: use sympy.primerange for bulk prime generation instead of nextprime().
"""
import sympy
from sympy import isprime, primerange, factorint
import time, json

def is_hard_case(n):
    """Fast hard case check: n ≡ 1 mod 12, n ≢ 0 mod 5, all odd prime factors of B₃ ≡ 1 mod 3."""
    if n % 12 != 1 or n % 5 == 0:
        return False
    B3 = n * (n + 3) // 4
    # Strip 2s
    while B3 % 2 == 0:
        B3 //= 2
    # Strip 3s  
    while B3 % 3 == 0:
        B3 //= 3
    # Quick trial division for primes 5..1000
    for p in primerange(5, 1000):
        if B3 == 1:
            return True
        if B3 % p == 0:
            if p % 3 == 2:
                return False
            while B3 % p == 0:
                B3 //= p
    if B3 == 1:
        return True
    # B3 has a large factor — check mod 3
    if B3 % 3 == 2:
        return False
    # Could be composite with factors all ≡ 1 mod 3
    # Try Pollard rho
    if B3 > 1:
        try:
            d = sympy.ntheory.factor_.pollard_rho(B3, retries=1)
            if d:
                if d % 3 == 2:
                    return False
                if (B3 // d) % 3 == 2:
                    return False
        except:
            pass
    return True

def solve_umethod(n, max_u=255):
    """u-method with early exit."""
    for u in range(3, max_u + 1, 4):
        if not isprime(u):
            continue
        x = (n + u) // 4
        if x < 1:
            continue
        # Factor x — trial division up to 1000, then Pollard rho
        factors = {}
        temp = x
        for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
            if temp == 1: break
            while temp % p == 0:
                factors[p] = factors.get(p, 0) + 1
                temp //= p
        if temp > 1:
            if isprime(temp):
                factors[temp] = 1
            else:
                try:
                    rest = sympy.ntheory.factor_.factorint(temp, limit=5000)
                    factors.update(rest)
                except:
                    factors[temp] = 1
        
        inv4 = pow(4, -1, u)
        x_mod = (n * inv4) % u
        n_mod = n % u
        targets = [(-x_mod) % u, (-x_mod * n_mod) % u, (-x_mod * n_mod * n_mod) % u]
        
        reachable = {1}
        for p, e in factors.items():
            if p % u == 0: continue
            new_reach = set()
            pe = 1
            for a in range(2*e + 1):
                for val in reachable:
                    new_reach.add((val * pe) % u)
                pe = (pe * (p % u)) % u
            reachable = new_reach
            if any(t in reachable for t in targets):
                return True, u
        if any(t in reachable for t in targets):
            return True, u
    return False, None

start = time.time()
print("Ultra-fast verification: 100M to 1B")
print("=" * 70)

count = 0
max_a = 0
failures = []
a_dist = {}
last_report = time.time()
batch_start = 100000000

# Process in 10M batches for progress reporting
while batch_start < 1000000000:
    batch_end = min(batch_start + 10000000, 1000000000)
    batch_count = 0
    
    for n in primerange(batch_start, batch_end):
        if n % 12 == 1 and n % 5 != 0:
            if is_hard_case(n):
                success, u_used = solve_umethod(n, max_u=255)
                count += 1
                batch_count += 1
                if success:
                    max_a = max(max_a, u_used)
                    a_dist[u_used] = a_dist.get(u_used, 0) + 1
                else:
                    failures.append(n)
                    print(f"  ❌ n={n}")
    
    elapsed = time.time() - start
    print(f"  [{batch_start//1000000}M-{batch_end//1000000}M] "
          f"hard={count} max_A={max_a} fails={len(failures)} "
          f"elapsed={elapsed:.0f}s")
    batch_start = batch_end

elapsed = time.time() - start
print(f"\n{'='*70}")
print(f"RESULTS: 100M to 1B")
print(f"  Hard cases: {count}")
print(f"  Failures: {len(failures)}")
print(f"  Max A: {max_a}")
print(f"  Runtime: {elapsed:.0f}s ({elapsed/3600:.1f}h)")
if failures:
    print(f"  FAILURES: {failures[:50]}")

print(f"\nA distribution:")
for u in sorted(a_dist.keys()):
    print(f"  A={u:3d}: {a_dist[u]:6d} ({a_dist[u]/count*100:.1f}%)")

with open('verification_100M_1B.json', 'w') as f:
    json.dump({"range":"100M-1B","total":count,"failures":len(failures),
               "max_a":max_a,"failures_list":failures[:100],
               "a_distribution":a_dist,"runtime":elapsed}, f, indent=2)
print(f"\nSaved to verification_100M_1B.json")