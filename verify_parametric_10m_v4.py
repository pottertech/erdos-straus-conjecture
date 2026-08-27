#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Parametric (z=my) Verification to 10,000,000
v4: Fast B3 check using precomputed "bad prime" sieve.

Key optimization: Instead of factoring B3 = n(n+3)/4 for each n,
precompute which n have B3 with all odd prime factors ≡ 1 mod 3.

B3 = n(n+3)/4. The "bad" primes (≡ 2 mod 3) that disqualify n are:
2 (ignored, we strip it), 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, 101, 107, ...

For each bad prime p, n is disqualified if p | B3, i.e., p | n(n+3)/4.
Since p is odd and p ≡ 2 mod 3, p | B3 iff p | n or p | (n+3).

So n is a hard case iff:
1. n ≡ 1 mod 12
2. n ≢ 0 mod 5
3. For all primes p ≡ 2 mod 3 with p > 3: p ∤ n AND p ∤ (n+3)

Wait, that's not quite right. B3 = n(n+3)/4, and we need all ODD prime factors ≡ 1 mod 3.
So we need: for all odd primes p | B3, p ≡ 1 mod 3.
Equivalently: no odd prime p ≡ 2 mod 3 divides B3.
B3 = n(n+3)/4, so p | B3 iff p | n or p | (n+3) (since p is odd, p ∤ 4).

So n is a hard case iff:
1. n ≡ 1 mod 12 (so 3 | (n+2), and 4 | n(n+3) since n ≡ 1 mod 4 and 3 ≡ 3 mod 4, n*3 ≡ 3 mod 4... wait)

Actually let me reconsider. n ≡ 1 mod 12 means:
- n ≡ 1 mod 4, so n+3 ≡ 0 mod 4, so n(n+3)/4 = n * (n+3)/4 is integer
- n ≡ 1 mod 3, so n+3 ≡ 1 mod 3

B3 = n * (n+3)/4. Odd prime factors come from n and (n+3)/4.

For n ≡ 1 mod 12: n ≡ 1 mod 3, so 3 ∤ n. And n+3 ≡ 4 mod 12, so (n+3)/4 ≡ 1 mod 3, so 3 ∤ (n+3)/4.
So 3 never divides B3 for hard case candidates. Good.

Hard case iff: n ≡ 1 mod 12, n ≢ 0 mod 5, and no prime p ≡ 2 mod 3 (p ≥ 5) divides n or (n+3)/4.

Actually p | B3 iff p | n or p | (n+3) (since gcd(n, n+3) | 3, and 3 ∤ B3 here).
So p | B3 iff p | n or p | (n+3), for p ≥ 5.

So we can use a sieve: mark all n ≡ 1 mod 12 where n or n+3 is divisible by any prime p ≡ 2 mod 3, p ≥ 5.
The unmarked ones (also excluding n ≡ 0 mod 5) are hard cases.

This is MUCH faster — O(N log log N) sieve instead of factoring each B3.
"""

import math
import json
import time
import sys
from collections import Counter

def sieve_primes(limit):
    """Simple sieve. Returns bytearray where is_prime[i] = 1 if i is prime."""
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = 0
    return is_prime

def build_spf(limit):
    """Build smallest-prime-factor array up to limit."""
    spf = [0] * (limit + 1)
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    return spf

def find_hard_cases_sieve(limit):
    """
    Find all hard cases up to limit using a sieve approach.
    
    Hard case: n ≡ 1 mod 12, n ≢ 0 mod 5, and no prime p ≡ 2 mod 3 (p ≥ 5)
    divides n or (n+3).
    
    We sieve out n where n or n+3 has a prime factor p ≡ 2 mod 3, p ≥ 5.
    """
    # Start with all n ≡ 1 mod 12 as candidates
    # is_hard[i] = 1 if i is still a candidate
    is_hard = bytearray(b'\x00') * (limit + 1)
    n = 1
    while n <= limit:
        if n >= 2:
            is_hard[n] = 1
        n += 12
    
    # Sieve out n ≡ 0 mod 5
    n = 1
    while n <= limit:
        if n % 5 == 0 and n >= 2:
            is_hard[n] = 0
        n += 12
    
    # Sieve out n where n or n+3 is divisible by a "bad" prime (p ≡ 2 mod 3, p ≥ 5)
    # Bad primes: 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, 101, 107, ...
    # Note: 5 is already handled by the n ≢ 0 mod 5 condition for n itself,
    # but 5 | (n+3) also disqualifies. And other bad primes p ≥ 7 matter too.
    
    # Actually wait — we need to be more careful.
    # n ≡ 1 mod 12, so n ≡ 1 mod 3, so 3 ∤ n. Good.
    # n+3 ≡ 4 mod 12. (n+3)/4 might have bad primes.
    # But p | B3 iff p | n or p | (n+3) (for odd p, since B3 = n(n+3)/4 and p ∤ 4).
    
    # So: for each bad prime p ≡ 2 mod 3, p ≥ 5:
    #   Remove n where p | n (i.e., n ≡ 0 mod p)
    #   Remove n where p | (n+3) (i.e., n ≡ -3 mod p ≡ (p-3) mod p)
    # But only for n ≡ 1 mod 12.
    
    # For p = 5: n ≡ 0 mod 5 already removed. Also remove n ≡ 2 mod 5 (since -3 ≡ 2 mod 5).
    #   n ≡ 1 mod 12 and n ≡ 2 mod 5: these are specific residues mod 60.
    
    # General approach: for each bad prime p, mark n ≡ 0 mod p and n ≡ (p-3) mod p
    # among the n ≡ 1 mod 12 candidates.
    
    sqrt_limit = int(math.isqrt(limit)) + 1
    is_prime = sieve_primes(min(limit, 10_000_000))
    
    for p in range(5, limit + 1):
        if p > limit:
            break
        if not is_prime[p]:
            continue
        if p % 3 != 2:  # only bad primes (≡ 2 mod 3)
            continue
        
        # Mark n ≡ 0 mod p (among n ≡ 1 mod 12)
        # n ≡ 1 mod 12 and n ≡ 0 mod p → n ≡ CRT(1 mod 12, 0 mod p)
        # Find first such n ≥ 2
        # n = 1 + 12k, need (1 + 12k) % p == 0 → k ≡ (-1) * inv(12) mod p
        inv12 = pow(12, -1, p) if math.gcd(12, p) == 1 else None
        if inv12 is not None:
            k0 = ((-1) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2:
                n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p):
                is_hard[n] = 0
        
        # Mark n ≡ (p-3) mod p (i.e., p | (n+3))
        # n = 1 + 12k, need (1 + 12k) % p == (p-3) → 12k ≡ (p-4) mod p
        if inv12 is not None:
            k0 = ((p - 4) * inv12) % p
            n0 = 1 + 12 * k0
            if n0 < 2:
                n0 += 12 * p
            for n in range(n0, limit + 1, 12 * p):
                is_hard[n] = 0
    
    # Collect hard cases
    hard_cases = [n for n in range(2, limit + 1) if is_hard[n]]
    return hard_cases

def factorize(n, spf):
    """Factor n using SPF array. Returns dict {prime: exponent}."""
    factors = {}
    temp = int(n)
    while temp > 1:
        if temp < len(spf) and spf[temp] > 0:
            p = int(spf[temp])
        else:
            # Trial division for large factors
            p = None
            sqrt_t = int(math.isqrt(temp)) + 1
            for c in range(2, min(sqrt_t + 1, len(spf))):
                if spf[c] == c and temp % c == 0:
                    p = c
                    break
            if p is None:
                for c in range(len(spf) | 1, sqrt_t + 1, 2):
                    if temp % c == 0:
                        p = c
                        break
            if p is None:
                p = temp
        factors[p] = factors.get(p, 0) + 1
        temp //= p
    return factors

def gen_divisors(factors):
    """Generate all divisors from factorization."""
    divs = [1]
    for p, e in factors.items():
        new_divs = []
        pe = 1
        for _ in range(e + 1):
            for d in divs:
                new_divs.append(d * pe)
            pe *= p
        divs = new_divs
    divs.sort()
    return divs

def find_parametric(n, max_A=107, spf=None):
    """Find parametric z=my solution. Returns (A, x, y, z, m) or None."""
    n = int(n)
    for A in range(3, max_A + 1, 4):
        if (n + A) % 4 != 0:
            continue
        x = (n + A) // 4
        D = n * (n + A)
        target = A - 1  # m ≡ -1 mod A

        D_factors = factorize(D, spf)
        divisors = gen_divisors(D_factors)
        v2_D = D_factors.get(2, 0)

        for m in divisors:
            if m % A != target:
                continue
            v2_m = 0
            tm = m
            while tm % 2 == 0:
                v2_m += 1
                tm //= 2
            if v2_m > 0 and v2_D < 2:
                continue
            if v2_m > 0 and v2_m > v2_D - 2:
                continue

            num = n * x * (m + 1)
            den = A * m
            if num % den != 0:
                continue
            y = num // den
            if y <= 0:
                continue
            z = m * y
            if z <= 0:
                continue

            if 4 * x * y * z == n * (y * z + x * z + x * y):
                return (A, x, y, z, m)
    return None

def find_umethod(n, spf=None):
    """Find u-method solution. Returns (A, x, y, z, u, is_param) or None."""
    n = int(n)
    for k in range(50000):
        x = n // 4 + 1 + k
        u = 4 * x - n
        if u <= 0 or u > 200003:
            continue

        nx = n * x
        D = nx * nx
        target = (-nx) % u
        sqrt_D = int(math.isqrt(D))

        # Check 9 guaranteed divisors
        for nf in [1, n, n * n]:
            for xf in [1, x, x * x]:
                d1 = nf * xf
                if d1 > sqrt_D:
                    continue
                if d1 % u != target:
                    continue
                d2 = D // d1
                if (d2 + nx) % u != 0:
                    continue
                y = (d1 + nx) // u
                z = (d2 + nx) // u
                if y > 0 and z > 0:
                    return (u, x, y, z, u, z % y == 0)

        # Full divisor search on x²
        x_factors = factorize(x, spf)
        x2_factors = {p: 2 * e for p, e in x_factors.items()}
        divs_x2 = gen_divisors(x2_factors)

        for nf in [1, n, n * n]:
            for d in divs_x2:
                d1 = nf * d
                if d1 > sqrt_D:
                    break
                if d1 % u != target:
                    continue
                d2 = D // d1
                if (d2 + nx) % u != 0:
                    continue
                y = (d1 + nx) // u
                z = (d2 + nx) // u
                if y > 0 and z > 0:
                    return (u, x, y, z, u, z % y == 0)
    return None

def main():
    start = time.time()

    print("=" * 70, flush=True)
    print("Erdős-Straus: Parametric Verification to 10M (v4, sieve-based)", flush=True)
    print("=" * 70, flush=True)

    limit = 10_000_000

    # Build SPF for factoring
    print(f"\n[0/4] Building SPF up to 2M...", flush=True)
    t0 = time.time()
    spf = build_spf(2_000_000)
    print(f"  SPF: {time.time()-t0:.1f}s", flush=True)

    # Find hard cases using sieve
    print(f"\n[1/4] Sieving for hard cases up to {limit:,}...", flush=True)
    t0 = time.time()
    hard_cases = find_hard_cases_sieve(limit)
    scan_time = time.time() - t0
    print(f"  Found {len(hard_cases)} hard cases in {scan_time:.1f}s", flush=True)

    # Solve
    print(f"\n[2/4] Solving {len(hard_cases)} cases (parametric A≤107, u-method fallback)...", flush=True)
    t0 = time.time()

    results = []
    param_A_dist = Counter()
    non_param = []
    failures = []
    max_A = 0
    max_A_n = 0

    for i, n in enumerate(hard_cases):
        if (i + 1) % 1000 == 0:
            el = time.time() - t0
            rate = (i + 1) / el if el > 0 else 0
            eta = (len(hard_cases) - i - 1) / rate if rate > 0 else 0
            print(f"  {i+1}/{len(hard_cases)} ({el:.0f}s, {rate:.0f}/s, ETA {eta:.0f}s, np={len(non_param)}, fail={len(failures)})", flush=True)

        pr = find_parametric(n, max_A=107, spf=spf)
        if pr:
            A, x, y, z, m = pr
            results.append({'n': n, 'A': A, 'method': 'parametric'})
            param_A_dist[A] += 1
            if A > max_A:
                max_A = A
                max_A_n = n
        else:
            ur = find_umethod(n, spf=spf)
            if ur:
                A, x, y, z, u, is_p = ur
                if is_p:
                    results.append({'n': n, 'A': A, 'method': 'param_um'})
                    param_A_dist[A] += 1
                    if A > max_A:
                        max_A = A
                        max_A_n = n
                else:
                    non_param.append({'n': n, 'A': A, 'u': u})
                    results.append({'n': n, 'A': A, 'method': 'non_param'})
            else:
                failures.append(n)
                results.append({'n': n, 'A': None, 'method': 'fail'})

    solve_time = time.time() - t0
    total_time = time.time() - start
    param_count = sum(1 for r in results if r['method'].startswith('param'))

    # Report
    print(f"\n[3/4] Results:", flush=True)
    print(f"  Hard cases: {len(hard_cases)}", flush=True)
    print(f"  Parametric: {param_count} ({100*param_count/len(hard_cases):.4f}%)", flush=True)
    print(f"  Non-param: {len(non_param)}", flush=True)
    print(f"  Failures: {len(failures)}", flush=True)
    print(f"  Max param A: {max_A} (n={max_A_n})", flush=True)
    print(f"  Time: {total_time:.0f}s", flush=True)

    # Markdown report
    lines = [
        "# Erdős-Straus Conjecture: Parametric Verification to 10,000,000",
        "",
        "## Overview",
        "",
        f"**Date:** 2026-08-16",
        f"**Range:** All hard cases, 2 to 10,000,000",
        f"**Method:** Parametric z=my (A ≤ 107), u-method fallback",
        f"**B3 check:** Sieve-based (bad primes p ≡ 2 mod 3)",
        f"**Time:** {total_time:.0f}s",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total hard cases | {len(hard_cases)} |",
        f"| Parametric solutions | {param_count} ({100*param_count/len(hard_cases):.4f}%) |",
        f"| Non-parametric | {len(non_param)} |",
        f"| Failures | {len(failures)} |",
        f"| Max parametric A | {max_A} (n={max_A_n}) |",
        "",
        "## A Distribution",
        "",
        "| A | Count | % | Cum % |",
        "|---|-------|---|-------|",
    ]
    cum = 0
    for A in sorted(param_A_dist.keys()):
        c = param_A_dist[A]
        cum += c
        lines.append(f"| {A} | {c} | {100*c/max(param_count,1):.2f}% | {100*cum/max(param_count,1):.2f}% |")
    lines.append("")

    if non_param:
        lines.append("## Non-Parametric Cases")
        lines.append("")
        lines.append(f"**Total:** {len(non_param)}")
        lines.append("")
        lines.append("| n | A | u |")
        lines.append("|---|---|---|")
        for c in non_param[:100]:
            lines.append(f"| {c['n']} | {c['A']} | {c['u']} |")
        if len(non_param) > 100:
            lines.append(f"| ... ({len(non_param)-100} more) |")
        lines.append("")

    lines.append("## Failures")
    lines.append("")
    if failures:
        lines.append(f"**{len(failures)} cases!**")
        lines.append(f"Cases: {', '.join(str(n) for n in failures[:50])}")
    else:
        lines.append("**None.** All hard cases solved.")
    lines.append("")

    lines.append("## Key Findings")
    lines.append("")
    lines.append(f"1. {param_count}/{len(hard_cases)} ({100*param_count/len(hard_cases):.4f}%) parametric with A ≤ 107.")
    lines.append(f"2. Max parametric A = {max_A} at n = {max_A_n}.")
    lines.append(f"3. {len(non_param)} non-parametric, {len(failures)} failures.")
    lines.append("")

    out = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/PARAMETRIC_VERIFICATION_10M.md"
    with open(out, 'w') as f:
        f.write("\n".join(lines))
    print(f"\nReport: {out}", flush=True)

    jpath = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/parametric_verification_10m.json"
    with open(jpath, 'w') as f:
        json.dump({
            'range': [2, limit], 'max_A_searched': 107,
            'total_hard_cases': len(hard_cases),
            'parametric_count': param_count,
            'non_parametric_count': len(non_param),
            'failure_count': len(failures),
            'max_parametric_A': max_A, 'max_parametric_A_n': max_A_n,
            'param_A_distribution': dict(param_A_dist),
            'non_parametric_cases': non_param[:2000],
            'total_failures': failures,
            'total_time': total_time,
        }, f, indent=2)
    print(f"JSON: {jpath}", flush=True)
    print(f"\nDONE in {total_time:.0f}s", flush=True)

if __name__ == "__main__":
    main()