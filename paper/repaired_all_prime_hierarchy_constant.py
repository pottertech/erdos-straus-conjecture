"""Finite certificate for the repaired every-prime fixed-cofactor hierarchy.

Computes the positive partial sum of the canonical fixed-cofactor contribution
through a user supplied prime bound.  The s == 1 (mod 8) row uses the repaired
2-adic witness

    d = 2^(v2(s-1)-3) * (s-1)

and hence parameter modulus 4d.

The output is a rigorous finite-subfamily contribution once combined with the
symbolic fixed-cofactor theorem and canonical no-reuse lemma.
"""

from math import isqrt
import argparse


def sieve(n):
    p = bytearray(b"\x01") * (n + 1)
    p[:2] = b"\x00\x00"
    for q in range(2, isqrt(n) + 1):
        if p[q]:
            p[q*q:n+1:q] = b"\x00" * (((n - q*q)//q) + 1)
    return [i for i in range(2, n + 1) if p[i]]


def phi(n, primes):
    result = n
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            result -= result // p
            while x % p == 0:
                x //= p
        if x == 1:
            break
    if x > 1:
        result -= result // x
    return result


def v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def contribution(s, factor_primes):
    cls = s % 8
    if cls == 1:
        e = v2(s - 1)
        d = (1 << (e - 3)) * (s - 1)
        modulus = 4 * d
    elif cls == 3:
        modulus = 2 * (s + 1)
    elif cls == 5:
        modulus = 4 * (s - 1)
    elif cls == 7:
        modulus = 2 * (s - 1)
    else:
        raise AssertionError(s)
    return 4.0 / (s * phi(modulus, factor_primes))


def run(limit):
    primes = sieve(limit)
    factor_primes = sieve(isqrt(8 * limit * limit) + 100)
    by_class = {1: 0.0, 3: 0.0, 5: 0.0, 7: 0.0}
    counts = {1: 0, 3: 0, 5: 0, 7: 0}
    for s in primes:
        if s < 5:
            continue
        by_class[s % 8] += contribution(s, factor_primes)
        counts[s % 8] += 1
    total = sum(by_class.values())
    return {
        "limit": limit,
        "counts": counts,
        "partial_sums": by_class,
        "hierarchy_partial_sum": total,
        "base_plus_hierarchy": 8.0/3.0 + total,
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1_000_000)
    args = ap.parse_args()
    print(run(args.limit))
