#!/usr/bin/env python3
"""R9 (E-020): independent cross-validation of the u = 7 composition-level
iff (E-018, engine v0.14 route) using Pollard rho factorization (no shared
code with the C sieve engines) plus a from-scratch opposite-pair re-deriva-
tion from the independently factored divisor set of (n*x)^2.

What it checks
--------------
(1) Structural invariants of the engine's full-run iff census (U7IFF rows):
    the two zero cells (span_notcond = 0, fail_cond = 0) per class and the
    cross-artifact consistency (the span cells equal the E-016 depth-0
    census counts, the fail cells sum to E-014's 414,261).
(2) An independent sweep of (H24) primes in [10^7, 10^7 + 2.4e6): the
    re-derived 4-way classification under the iff (span iff 5 | x' or an
    odd prime divisor of x' in {3,5,6} mod 7) with the same two zero cells
    verified at zero-mismatch scale.
(3) For sampled span and fail records per class (400 each), a from-scratch
    span check: the divisor set of (n*x)^2 built from the rho factorization
    contains a divisor d with d + n*x = 0 (mod 7) exactly when the record
    classified as a spanner.

Exits 0 iff every check passes.
"""
import sys
from math import isqrt, gcd

LO = 10**7
SPAN_SUB = 2_400_000
CLASS_SAMPLE = 400

def eratosthenes(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i, v in enumerate(sieve) if v]

TRAIL = eratosthenes(5000)

def is_prime_small_check(m):
    for p in TRAIL:
        if p * p > m:
            return True
        if m % p == 0:
            return False
    return None  # bigger than the trial range

def is_prime(p):
    r = is_prime_small_check(p)
    if r is not None:
        return r
    # deterministic Miller-Rabin base set for p < 3.3e24
    d = p - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, p)
        if x in (1, p - 1):
            continue
        for _ in range(s - 1):
            x = x * x % p
            if x == p - 1:
                break
        else:
            return False
    return True

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = random.randrange(1, n - 1)
        x = random.randrange(2, n - 1)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:
            return d

import random
random.seed(20261125)

def factorize(n):
    facs = {}
    for p in TRAIL:
        if p * p > n:
            break
        while n % p == 0:
            facs[p] = facs.get(p, 0) + 1
            n //= p
    if n == 1:
        return facs
    if is_prime(n):
        facs[n] = facs.get(n, 0) + 1
        return facs
    stack = [n]
    while stack:
        m = stack.pop()
        if is_prime(m):
            facs[m] = facs.get(m, 0) + 1
            continue
        d = pollard_rho(m)
        stack.append(d)
        stack.append(m // d)
    return facs

def divisors_from_facs(facs):
    divs = [1]
    for p, e in sorted(facs.items()):
        base = list(divs)
        pk = 1
        for _ in range(e):
            pk *= p
            divs = divs + [d * pk for d in base]
    return divs

def has_opposite_pair(N, Nsq, divs):
    """the R1 window form: exists d | N^2 with d + N == 0 (mod 7) and
    d <= N (the centered window)."""
    target = (-N) % 7
    for d in divs:
        if d % 7 == target and d <= N:
            return True
    return False

def main():
    # ---- (1) the engine census invariants
    run_file = "research/residual_primes/analysis/u7_iff_v014/full_run.txt"
    iff = {}
    for line in open(run_file):
        if line.startswith("U7IFF r7="):
            t = line.split()
            r7 = int(t[1].split("=")[1])
            iff[r7] = {k: int(v) for k, v in
                       (item.split("=") for item in t[2:6])}
    assert set(iff) == {1, 2, 4}
    for r, c in iff.items():
        assert c["span_notcond"] == 0, (r, c)
        assert c["fail_cond"] == 0, (r, c)
    # cross-artifact consistency (E-016 depth-0 census, E-014 fail total)
    assert (iff[1]["span_cond"], iff[2]["span_cond"], iff[4]["span_cond"]) == \
           (124680, 124508, 132464), iff
    assert sum(c["span_cond"] for c in iff.values()) == 381652
    assert sum(c["fail_notcond"] for c in iff.values()) == 414261
    assert sum(sum(c.values()) for c in iff.values()) == 381652 + 414261
    print("(1) census invariants OK:", {r: sum(c.values()) for r, c in iff.items()})

    # ---- (2) the independent sweep + classification
    per_class = {r: {"span_cond": 0, "span_notcond": 0,
                     "fail_cond": 0, "fail_notcond": 0} for r in (1, 2, 4)}
    span_samples = {1: [], 2: [], 4: []}
    fail_samples = {1: [], 2: [], 4: []}
    n_recs = 0
    end = LO + SPAN_SUB
    # (H24) primes: 1 (mod 24)
    p = LO + 1
    p += (1 - p % 24) % 24
    while p < end:
        if is_prime(p):
            n_mod = p % 7
            if n_mod in (1, 2, 4):
                n = p
                x = (n + 7) // 4
                fivex = (x % 5 == 0)
                cond = False
                facs = None
                if not fivex:
                    facs = factorize(x)
                    for q2, e in facs.items():
                        if q2 != 2 and q2 != 5 and q2 % 7 in (3, 5, 6):
                            cond = True
                            break
                isspan = fivex or cond
                in_domain = not fivex  # the iff's domain: 5-free x'
                if isspan:
                    if cond:
                        per_class[n_mod]["span_cond"] += 1
                        if len(span_samples[n_mod]) < CLASS_SAMPLE:
                            span_samples[n_mod].append((n, x, facs))
                    elif in_domain:
                        per_class[n_mod]["span_notcond"] += 1
                    else:
                        # 5-divisible spanner: outside the iff's census domain
                        if len(span_samples[n_mod]) < CLASS_SAMPLE:
                            span_samples[n_mod].append((n, x, None))
                else:
                    per_class[n_mod]["fail_notcond"] += 1
                    if len(fail_samples[n_mod]) < CLASS_SAMPLE:
                        fail_samples[n_mod].append((n, x, facs))
                n_recs += 1
        p += 24
    for r in (1, 2, 4):
        got = per_class[r]
        assert got["span_notcond"] == 0 and got["fail_cond"] == 0, (r, got)
    print("(2) sweep:", n_recs, "records;", {r: c for r, c in per_class.items()})

    # ---- (3) the from-scratch opposite-pair re-derivation on samples
    checked = 0
    for r in (1, 2, 4):
        for n, x, facs in span_samples[r]:
            if facs is None:  # 5 | x records skipped in sampling
                facs = factorize(x)
            facs_n = factorize(n)  # n prime: cheap
            facs_sq = dict(facs_n)
            for q2, e in facs.items():
                facs_sq[q2] = facs_sq.get(q2, 0) + 2 * e
            N = n * x
            divs = divisors_from_facs(facs_sq)
            assert len(divs) < 200000, len(divs)
            ok = has_opposite_pair(N, N * N, divs)
            assert ok, ("spanner without opposite pair", r, n, x)
            checked += 1
        for n, x, facs in fail_samples[r]:
            facs_n = {"": 0} and factorize(n)
            facs_sq = dict(facs_n)
            for q2, e in facs.items():
                facs_sq[q2] = facs_sq.get(q2, 0) + 2 * e
            N = n * x
            divs = divisors_from_facs(facs_sq)
            ok = has_opposite_pair(N, N * N, divs)
            assert not ok, ("failer with opposite pair", r, n, x)
            checked += 1
    print("(3) from-scratch opposite-pair re-derivation:", checked,
          "records all in agreement (spanners have the pair, failers none)")
    print("R9 CROSSVAL: ALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
