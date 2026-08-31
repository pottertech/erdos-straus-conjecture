"""Verify the repaired k=0 no-reuse condition for canonical fixed cofactors.

For each prime 5 <= s <= limit, construct the canonical candidate (d, alpha)
by s mod 8.  For the s == 1 mod 8 class we use the repaired 2-adic
choice

    e = v_2(s-1),  d = 2^(e-3) * (s-1),
    alpha == -s^{-1} mod 4d.

For every exceptional cofactor c<s in the correct mod-4 class that divides
4d+1, test whether d divides B_c^2, where

    B_c = (c*alpha+1)/4.

A simultaneous hit is exactly the k=0 reuse obstruction for the global
square-safe choice n == 1 on all non-target coordinates.

The script is a finite certificate only; it does not prove the universal
no-reuse statement for arbitrarily large fixed cofactors.
"""

from math import gcd
import argparse


def sieve_primes(n):
    isprime = bytearray(b"\x01") * (n + 1)
    isprime[:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if isprime[p]:
            isprime[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
        p += 1
    return [i for i in range(2, n + 1) if isprime[i]]


def factor(n, primes):
    out = {}
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out[p] = e
        if x == 1:
            break
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def divisors_from_factor(fac):
    ds = [1]
    for p, e in fac.items():
        old = list(ds)
        ds = []
        pe = 1
        for _ in range(e + 1):
            ds.extend(x * pe for x in old)
            pe *= p
    return ds


def v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def canonical_data(s):
    cls = s % 8
    if cls == 3:
        d = (s + 1) // 2
        modulus = 2 * (s + 1)
        alpha = s + 2
        rmod4 = 1
    elif cls == 7:
        d = (s - 1) // 2
        modulus = 2 * (s - 1)
        alpha = s - 2
        rmod4 = 1
    elif cls == 5:
        d = s - 1
        modulus = 4 * (s - 1)
        alpha = s - 2
        rmod4 = 3
    elif cls == 1:
        e = v2(s - 1)
        # Minimal 2-adic reinforcement that blocks the c=1 divisor reuse:
        # v_2(d) = 2e-3 while v_2(B_1^2) = 2e-4.
        d = (1 << (e - 3)) * (s - 1)
        modulus = 4 * d
        alpha = (-pow(s, -1, modulus)) % modulus
        rmod4 = 3
    else:
        raise AssertionError(s)

    assert gcd(alpha, modulus) == 1
    assert (s * alpha + 1) % (4 * d) == 0
    return d, modulus, alpha, rmod4


def verify(limit):
    primes = sieve_primes(limit)
    factor_primes = sieve_primes(int((8 * limit) ** 0.5) + 100)
    checked = 0
    failures = []
    by_class = {1: 0, 3: 0, 5: 0, 7: 0}

    for s in primes:
        if s < 5:
            continue
        d, modulus, alpha, rmod4 = canonical_data(s)
        by_class[s % 8] += 1
        cmod4 = 3 if rmod4 == 1 else 1

        # Only c | 4d+1 can make the k=0 target residue equal the chosen
        # square-safe residue 1 modulo c.
        fac = factor(4 * d + 1, factor_primes)
        for c in divisors_from_factor(fac):
            if not (0 < c < s and c % 4 == cmod4):
                continue
            assert (c * alpha + 1) % 4 == 0
            B = (c * alpha + 1) // 4
            if (B * B) % d == 0:
                failures.append({
                    "s": s,
                    "class_mod8": s % 8,
                    "d": d,
                    "alpha": alpha,
                    "parameter_modulus": modulus,
                    "c": c,
                    "B": B,
                })
                return {
                    "limit": limit,
                    "checked_prime_cofactors": checked + 1,
                    "class_counts": by_class,
                    "failures": failures,
                }
        checked += 1

    return {
        "limit": limit,
        "checked_prime_cofactors": checked,
        "class_counts": by_class,
        "failures": failures,
        "conclusion": "no k=0 no-reuse failures in the finite certified range",
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1_000_000)
    args = ap.parse_args()
    print(verify(args.limit))
