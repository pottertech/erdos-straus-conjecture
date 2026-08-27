#!/usr/bin/env python3
"""Fast 100M-1B verification — pre-computed prime lists, no repeated primerange calls."""
import sympy
from sympy import isprime, primerange
import time, json

SMALL_PRIMES = list(primerange(5, 1000))
SMALL_PRIMES_TRIAL = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
U_VALUES = [u for u in range(3, 256, 4) if isprime(u)]

def is_hard_case(n):
    if n % 12 != 1 or n % 5 == 0: return False
    B3 = n * (n + 3) // 4
    while B3 % 2 == 0: B3 //= 2
    while B3 % 3 == 0: B3 //= 3
    for p in SMALL_PRIMES:
        if B3 == 1: return True
        if B3 % p == 0:
            if p % 3 == 2: return False
            while B3 % p == 0: B3 //= p
    if B3 == 1: return True
    if B3 % 3 == 2: return False
    if B3 > 1:
        try:
            d = sympy.ntheory.factor_.pollard_rho(B3, retries=1)
            if d and (d % 3 == 2 or (B3 // d) % 3 == 2): return False
        except: pass
    return True

def solve_umethod(n):
    for u in U_VALUES:
        x = (n + u) // 4
        if x < 1: continue
        factors = {}
        temp = x
        for p in SMALL_PRIMES_TRIAL:
            if temp == 1: break
            while temp % p == 0:
                factors[p] = factors.get(p, 0) + 1
                temp //= p
        if temp > 1:
            if isprime(temp): factors[temp] = 1
            else:
                try: factors.update(sympy.ntheory.factor_.factorint(temp, limit=5000))
                except: factors[temp] = 1
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
                for val in reachable: new_reach.add((val * pe) % u)
                pe = (pe * (p % u)) % u
            reachable = new_reach
            if any(t in reachable for t in targets): return True, u
        if any(t in reachable for t in targets): return True, u
    return False, None

start = time.time()
print("Fast verification: 100M to 1B (pre-computed primes)")
print("=" * 70)
flush = True

count, max_a, failures, a_dist = 0, 0, [], {}
batch_start = 100000000

while batch_start < 1000000000:
    batch_end = min(batch_start + 10000000, 1000000000)
    batch_count = 0
    for n in primerange(batch_start, batch_end):
        if n % 12 == 1 and n % 5 != 0 and is_hard_case(n):
            ok, u = solve_umethod(n)
            count += 1; batch_count += 1
            if ok: max_a = max(max_a, u); a_dist[u] = a_dist.get(u, 0) + 1
            else: failures.append(n); print(f"  ❌ n={n}", flush=True)
    elapsed = time.time() - start
    print(f"  [{batch_start//1000000}M-{batch_end//1000000}M] hard={count} max_A={max_a} fails={len(failures)} t={elapsed:.0f}s", flush=True)
    batch_start = batch_end

elapsed = time.time() - start
print(f"\n{'='*70}\nRESULTS: 100M-1B\n  Hard: {count}  Fails: {len(failures)}  MaxA: {max_a}  Time: {elapsed/3600:.1f}h")
if failures: print(f"  FAILURES: {failures[:50]}")
for u in sorted(a_dist): print(f"  A={u:3d}: {a_dist[u]:6d} ({a_dist[u]/count*100:.1f}%)")
json.dump({"range":"100M-1B","total":count,"failures":len(failures),"max_a":max_a,
           "failures_list":failures[:100],"a_distribution":a_dist,"runtime":elapsed},
          open('verification_100M_1B.json','w'), indent=2)
print("\nSaved to verification_100M_1B.json")