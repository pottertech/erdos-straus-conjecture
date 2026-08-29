"""Exact finite verification that n=2521 has no unit-partner certificate.

This does NOT say 2521 is an Erdős--Straus counterexample.  It is solved by
the full binary criterion at u=31 with the non-unit pair (2,29).

The script verifies two facts:

1. Untwisted branch: only j <= 210 can possibly work, where
       u = 4*j - 1, K = 630 + j.
   Every divisor of K is checked for d == -1 (mod u).

2. Twisted branch: every solution has a <= floor(n/2).  For each
   a=1,...,1260, the factorization identity
       (4*a*d-n)(4*a*r-n) = n^2 + 4*a
   implies u=4*a*d-n divides n^2+4*a and u == -n (mod 4*a).
   All such divisors are enumerated and reconstructed.
"""

from math import isqrt

N = 2521
M = (N - 1) // 4  # 630


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


def divisors_from_factorization(fm):
    ds = [1]
    for p, e in fm.items():
        base = list(ds)
        pe = 1
        new = list(base)
        for _ in range(e):
            pe *= p
            new.extend(d * pe for d in base)
        ds = new
    return sorted(ds)


def untwisted_solutions():
    # u-1 <= K is necessary:
    # 4j-2 <= 630+j  =>  3j <= 632  =>  j <= 210.
    sols = []
    for j in range(1, 211):
        u = 4 * j - 1
        K = M + j
        for d in divisors_from_factorization(factor(K)):
            if d % u == u - 1:
                sols.append((j, u, K, d))
    return sols


def twisted_solutions():
    sols = []
    for a in range(1, N // 2 + 1):
        value = N * N + 4 * a
        for u in divisors_from_factorization(factor(value)):
            if u % 4 != 3:
                continue
            if (u + N) % (4 * a) != 0:
                continue
            d = (u + N) // (4 * a)
            if d <= 0:
                continue
            if (N * d + 1) % u != 0:
                continue
            r = (N * d + 1) // u
            # Exact reconstruction checks.
            assert u == 4 * a * d - N
            assert (4 * a * d - N) * (4 * a * r - N) == N * N + 4 * a
            sols.append((a, d, r, u))
    return sols


if __name__ == "__main__":
    untwisted = untwisted_solutions()
    twisted = twisted_solutions()

    print("n =", N)
    print("untwisted solutions:", untwisted)
    print("twisted solutions:", twisted)

    assert untwisted == []
    assert twisted == []

    # Separate explicit full-binary certificate showing 2521 is solved.
    u = 31
    K = (N + u) // 4
    assert K == 638
    assert K % 2 == 0 and K % 29 == 0
    assert (2 + 29) % u == 0
    print("full binary certificate: u=31, K=638, pair=(2,29)")
    print("PASS: 2521 is a permanent unit-partner exception, not an ESC exception")
