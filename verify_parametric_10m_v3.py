#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Parametric (z=my) Verification to 10,000,000
v3: All arithmetic in Python native ints. No numpy for arithmetic.

For ALL hard cases (prime + composite), verify that a parametric z=my solution
exists for some A ≡ 3 (mod 4) with A ≤ 107.
"""

import math
import json
import time
import sys
from collections import Counter

def sieve_primes(limit):
    """Simple sieve returning a set of primes up to limit."""
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = 0
    return is_prime  # bytearray, indexable, returns int (0 or 1)

def build_spf(limit):
    """Build smallest-prime-factor array up to limit. Returns list of Python ints."""
    spf = [0] * (limit + 1)
    for i in range(2, limit + 1):
        if spf[i] == 0:  # i is prime
            spf[i] = i
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    return spf

def factorize(n, spf):
    """Factor n using SPF array. Returns dict {prime: exponent} with Python int keys/values."""
    factors = {}
    temp = int(n)
    while temp > 1:
        if temp < len(spf) and spf[temp] > 0:
            p = int(spf[temp])
        else:
            # temp is larger than SPF array — trial division
            p = None
            sqrt_t = int(math.isqrt(temp)) + 1
            for candidate in range(2, min(sqrt_t + 1, len(spf))):
                if spf[candidate] == candidate and temp % candidate == 0:  # candidate is prime
                    p = candidate
                    break
            if p is None:
                # Continue trial division beyond SPF array
                start = len(spf)
                if start % 2 == 0:
                    start += 1
                for candidate in range(start, sqrt_t + 1, 2):
                    if temp % candidate == 0:
                        p = candidate
                        break
            if p is None:
                p = temp  # temp is prime
        factors[p] = factors.get(p, 0) + 1
        temp //= p
    return factors

def gen_divisors(factors):
    """Generate all divisors from factorization. Returns sorted list of Python ints."""
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

def check_B3(n, spf):
    """Check if all odd prime factors of B3 = n(n+3)/4 are ≡ 1 mod 3."""
    B3 = n * (n + 3) // 4
    temp = B3
    while temp % 2 == 0:
        temp //= 2
    if temp == 1:
        return True
    while temp > 1:
        if temp < len(spf) and spf[temp] > 0:
            p = spf[temp]
        else:
            p = None
            sqrt_t = int(math.isqrt(temp)) + 1
            for c in range(3, min(sqrt_t + 1, len(spf)), 2):
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
        if p != 2 and p % 3 != 1:
            return False
        while temp % p == 0:
            temp //= p
    return True

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

            # Verify
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
    print("Erdős-Straus: Parametric Verification to 10M (v3, pure Python ints)", flush=True)
    print("=" * 70, flush=True)

    # Build sieve and SPF
    limit = 10_000_000
    print(f"\n[0/4] Building sieve + SPF up to {limit:,}...", flush=True)
    t0 = time.time()
    is_prime = sieve_primes(limit)
    prime_count = sum(is_prime)
    spf = build_spf(2_000_000)  # SPF up to 2M for factoring
    print(f"  Done in {time.time()-t0:.1f}s ({prime_count:,} primes, SPF to 2M)", flush=True)

    # Find hard cases
    print("\n[1/4] Scanning for hard cases...", flush=True)
    t0 = time.time()
    hard_cases = []
    checked = 0
    n = 1
    while n <= limit:
        if n >= 2 and n % 5 != 0:
            checked += 1
            if check_B3(n, spf):
                hard_cases.append(n)
        if checked % 100_000 == 0 and checked > 0:
            print(f"  n={n:,} ({checked:,} checked, {len(hard_cases)} hard, {time.time()-t0:.1f}s)", flush=True)
        n += 12
    print(f"  Found {len(hard_cases)} hard cases in {time.time()-t0:.1f}s", flush=True)

    # Solve
    print(f"\n[2/4] Solving {len(hard_cases)} cases...", flush=True)
    t0 = time.time()
    
    results = []
    param_A_dist = Counter()
    non_param = []
    failures = []
    max_A = 0
    max_A_n = 0

    for i, n in enumerate(hard_cases):
        if (i + 1) % 500 == 0:
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
    print(f"  Total: {len(hard_cases)} hard cases", flush=True)
    print(f"  Parametric: {param_count} ({100*param_count/len(hard_cases):.4f}%)", flush=True)
    print(f"  Non-parametric: {len(non_param)}", flush=True)
    print(f"  Failures: {len(failures)}", flush=True)
    print(f"  Max param A: {max_A} (n={max_A_n})", flush=True)
    print(f"  Time: {total_time:.0f}s", flush=True)

    # Markdown
    lines = [
        "# Erdős-Straus Conjecture: Parametric Verification to 10,000,000",
        "",
        "## Overview",
        "",
        f"**Date:** 2026-08-16",
        f"**Range:** All hard cases, 2 to 10,000,000",
        f"**Method:** Parametric z=my (A ≤ 107), u-method fallback",
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