"""Probe global first-hit depth inside a realized primitive Type-II progression.

A divisor-modulus primitive class at depth A gives a genuine Type-II
progression

    n == -4*D (mod 4*A-1),  D | A^2.

That progression can still be solved at a much smaller unrelated depth B
whose modulus 4*B-1 does not divide 4*A-1.  This script samples primes in a
specified progression and computes their minimum square-completed Type-II
depth up to a requested bound.

Finite diagnostic only: sampling does not prove coverage of the entire
progression.
"""

import argparse
from collections import Counter
from math import isqrt


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


def divisors_of_square(n):
    ds = [1]
    for p, e in factor_small(n).items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(2 * e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return ds


def isprime64(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def build_layers(A_max):
    layers = []
    for A in range(1, A_max + 1):
        m = 4 * A - 1
        traps = {(-4 * D) % m for D in divisors_of_square(A)}
        layers.append((A, m, traps))
    return layers


def first_depth(n, layers):
    for A, m, traps in layers:
        if n % m in traps:
            return A
    return None


def sample(A, D, count, depth_bound):
    m = 4 * A - 1
    residue = (-4 * D) % m
    layers = build_layers(depth_bound)
    rows = []
    k = 0
    while len(rows) < count:
        n = residue + k * m
        if n > 1 and isprime64(n):
            rows.append((n, first_depth(n, layers)))
        k += 1
    hist = Counter(depth for _, depth in rows)
    return m, residue, rows, hist


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--A', type=int, required=True)
    ap.add_argument('--D', type=int, required=True)
    ap.add_argument('--count', type=int, default=100)
    ap.add_argument('--depth-bound', type=int, default=1000)
    args = ap.parse_args()

    if (args.A * args.A) % args.D:
        raise SystemExit('D must divide A^2')

    m, residue, rows, hist = sample(args.A, args.D, args.count, args.depth_bound)
    print('modulus', m)
    print('progression residue', residue)
    print('sampled primes', len(rows))
    print('unresolved within bound', hist.get(None, 0))
    print('histogram', dict(sorted((k if k is not None else -1, v) for k, v in hist.items())))
    print('first rows', rows[:20])
