"""Reproduce the explicit finite lower-bound constant from the fixed-cofactor hierarchy.

This script is finite arithmetic only.  It does not prove the hierarchy theorem;
it verifies the numerical coefficient obtained by summing already-proved fixed-s
families through a chosen cutoff.
"""

from math import gcd, isqrt


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def phi(n):
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            result -= result // p
            while x % p == 0:
                x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        result -= result // x
    return result


def certificate(limit=1_000_000):
    total = 0.0
    count = 0
    for s in primes_upto(limit):
        if s > 3 and s % 8 == 3:
            total += 4.0 / (s * phi(2 * (s + 1)))
            count += 1

    extra = 1/7 + 1/184 + 1/248 + 1/987
    base = 8/3
    coefficient = base + total + extra
    return {
        "cutoff": limit,
        "canonical_cofactor_count": count,
        "canonical_partial_sum": total,
        "prime_3q_base": base,
        "explicit_7mod8_extra": extra,
        "certified_liminf_coefficient": coefficient,
    }


if __name__ == "__main__":
    result = certificate()
    for key, value in result.items():
        print(f"{key}: {value}")
