"""Exact regression checks for proper-ancestor survivor counterexamples.

This script verifies two facts used by the current ancestry notes:

1. mixed-signature survivor
       m = 352495 = 5*11*13*17*29
       r = 224316

2. all-3-mod-4 survivor
       m = 6407731 = 11*19*23*31*43
       r = 3990232

For each case it checks that r is a unit square modulo every prime factor and
that r avoids Q_B for every proper divisor d|m with d == 3 (mod 4), where
B=(d+1)/4 and Q_B={E mod d : E|B^2}.

No claim about Erdős--Straus counterexamples is made; these are counterexamples
only to a proposed proper-ancestor coverage lemma.
"""

from itertools import combinations
from math import gcd, prod


def factor_small(n):
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors_from_factorization(fac):
    ds = [1]
    for p, e in fac.items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return sorted(ds)


def divisors(n):
    return divisors_from_factorization(factor_small(n))


def qset(d):
    assert d % 4 == 3
    B = (d + 1) // 4
    return {E % d for E in divisors(B * B)}


def is_nonzero_square_mod_prime(r, p):
    if r % p == 0:
        return False
    return pow(r % p, (p - 1) // 2, p) == 1


def verify_case(m, r, primes):
    assert prod(primes) == m
    assert len(set(primes)) == len(primes)
    assert m % 4 == 3
    assert gcd(m, r) == 1

    for p in primes:
        assert is_nonzero_square_mod_prime(r, p), (m, r, p, r % p)

    proper_ancestors = [
        d for d in divisors(m)
        if 1 < d < m and d % 4 == 3
    ]

    rows = []
    for d in proper_ancestors:
        B = (d + 1) // 4
        residue = r % d
        hit = residue in qset(d)
        assert not hit, (m, r, d, B, residue)
        rows.append((d, B, residue))

    return rows


def main():
    cases = [
        (352495, 224316, (5, 11, 13, 17, 29)),
        (6407731, 3990232, (11, 19, 23, 31, 43)),
    ]

    for m, r, primes in cases:
        rows = verify_case(m, r, primes)
        print({
            'm': m,
            'r': r,
            'prime_factors': primes,
            'proper_3mod4_ancestors': len(rows),
            'verified_survivor': True,
        })


if __name__ == '__main__':
    main()
