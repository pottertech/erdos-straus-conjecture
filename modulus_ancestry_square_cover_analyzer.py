"""Exact modulus-level analyzer for square-completed Type-II ancestry.

For any odd m == 3 (mod 4), define A=(m+1)/4.  A proper ancestor divisor is a
divisor d of m with 1<d<m and d == 3 (mod 4), corresponding to depth
B=(d+1)/4.

For such B let
    Q_B = {E mod d : E | B^2}.
A unit square class r modulo m is inherited if for some proper ancestor d,
its reduction r mod d lies in Q_B.

The script tests whether the proper-ancestor system covers every unit square
class modulo m.  This is independent of any denominator-prime search and is
therefore a pure structural test of the square-completed depth geometry.
"""

import argparse
from functools import lru_cache
from math import gcd


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


@lru_cache(maxsize=None)
def qset(B):
    d = 4 * B - 1
    return frozenset(E % d for E in divisors(B * B))


def proper_ancestors(m):
    return [d for d in divisors(m) if 1 < d < m and d % 4 == 3]


def unit_square_classes(m):
    return sorted({(x * x) % m for x in range(1, m) if gcd(x, m) == 1})


def survivor_classes(m, stop_after=None):
    if m % 4 != 3:
        raise ValueError('m must be 3 mod 4')
    ads = proper_ancestors(m)
    survivors = []
    for r in unit_square_classes(m):
        inherited = False
        for d in ads:
            B = (d + 1) // 4
            if r % d in qset(B):
                inherited = True
                break
        if not inherited:
            survivors.append(r)
            if stop_after and len(survivors) >= stop_after:
                break
    return survivors


def audit(limit, min_omega=5):
    tested = 0
    counterexamples = []
    for m in range(3, limit + 1, 4):
        omega = len(factor(m))
        if omega < min_omega:
            continue
        tested += 1
        s = survivor_classes(m, stop_after=1)
        if s:
            counterexamples.append({
                'm': m,
                'factorization': factor(m),
                'first_survivor_square_class': s[0],
            })
    return {
        'limit': limit,
        'min_omega': min_omega,
        'tested_moduli': tested,
        'counterexample_count': len(counterexamples),
        'counterexamples': counterexamples,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--m', type=int)
    ap.add_argument('--limit', type=int)
    ap.add_argument('--min-omega', type=int, default=5)
    args = ap.parse_args()

    if args.m is not None:
        m = args.m
        print({
            'm': m,
            'factorization': factor(m),
            'omega': len(factor(m)),
            'proper_ancestors': proper_ancestors(m),
            'survivors': survivor_classes(m),
        })
    elif args.limit is not None:
        print(audit(args.limit, args.min_omega))
    else:
        ap.error('provide --m or --limit')
