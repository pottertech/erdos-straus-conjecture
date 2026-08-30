"""Exact regression for the refuted five-factor ancestry-cover conjecture.

The smallest all-3-mod-4 five-prime modulus avoiding the universal prime
ancestors 3 and 7 is

    m = 11*19*23*31*43 = 6_407_731.

The square class r=3_990_232 survives every proper ancestor d|m with
d == 3 (mod 4).  This script verifies the claim exactly, using integer
arithmetic only.
"""

from math import gcd
from itertools import combinations


PRIMES = (11, 19, 23, 31, 43)
M = 6_407_731
R = 3_990_232


def factor(n):
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


def divisors_from_factorization(f):
    ds = [1]
    for p, e in f.items():
        base = list(ds)
        out = []
        pe = 1
        for _ in range(e + 1):
            out.extend(x * pe for x in base)
            pe *= p
        ds = out
    return sorted(ds)


def divisors(n):
    return divisors_from_factorization(factor(n))


def qset(B):
    d = 4 * B - 1
    return {E % d for E in divisors(B * B)}


def is_nonzero_square_mod_prime(r, p):
    if r % p == 0:
        return False
    return pow(r % p, (p - 1) // 2, p) == 1


def proper_3mod4_ancestors_of_squarefree_five_negative(primes):
    # A product of k primes, each 3 mod 4, is 3 mod 4 exactly when k is odd.
    # Proper nontrivial odd subset sizes are therefore 1 and 3.
    out = []
    for k in (1, 3):
        for subset in combinations(primes, k):
            d = 1
            for p in subset:
                d *= p
            out.append(d)
    return sorted(out)


def main():
    assert M == 11 * 19 * 23 * 31 * 43
    assert M % 4 == 3
    assert gcd(M, R) == 1

    local = {}
    for p in PRIMES:
        assert p % 4 == 3
        assert is_nonzero_square_mod_prime(R, p)
        local[p] = R % p

    ancestors = proper_3mod4_ancestors_of_squarefree_five_negative(PRIMES)
    assert len(ancestors) == 15

    rows = []
    for d in ancestors:
        B = (d + 1) // 4
        residue = R % d
        inherited = residue in qset(B)
        rows.append((d, B, residue, inherited))
        assert not inherited, (d, B, residue)

    print({
        "status": "PASS",
        "m": M,
        "r": R,
        "local_square_residues": local,
        "proper_ancestor_count": len(ancestors),
        "rows": rows,
    })


if __name__ == "__main__":
    main()
