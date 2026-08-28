#!/usr/bin/env python3
"""Verify the exact u=7 characterization on prime hard cases.

For n == 1 or 49 (mod 120), x=(n+7)/4 is even.  The theorem predicts:

  exact u=7 succeeds
    iff
  n is QNR mod 7 OR x has an odd QNR prime factor mod 7.

Equivalently, u=7 fails iff n and every odd prime factor of x are QR mod 7.
"""

import sys
from sympy import factorint, legendre_symbol, primerange


def is_hard_case(n):
    if n % 12 != 1 or n % 5 == 0:
        return False
    b3 = n * (n + 3) // 4
    while b3 % 2 == 0:
        b3 //= 2
    if b3 % 3 == 0:
        return False
    return all(p % 3 == 1 for p in factorint(b3))


def divisors_from_factorization(factors):
    ds = [1]
    for p, e in factors.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds


def exact_u7_success(n):
    u = 7
    x = (n + u) // 4
    D = (n * x) ** 2
    target = (-n * x) % u
    x2 = {p: 2 * e for p, e in factorint(x).items()}
    for a in range(3):
        for e_div in divisors_from_factorization(x2):
            d1 = n**a * e_div
            if d1 % u != target:
                continue
            d2 = D // d1
            if d2 % u == target:
                return True
    return False


def predicted_u7_success(n):
    if legendre_symbol(n, 7) == -1:
        return True
    x = (n + 7) // 4
    for p in factorint(x):
        if p in (2, 7):
            continue
        if legendre_symbol(p, 7) == -1:
            return True
    return False


def main(limit):
    checked = successes = failures = 0
    mismatches = []
    for n in primerange(2, limit + 1):
        if n % 120 not in (1, 49) or not is_hard_case(n):
            continue
        checked += 1
        exact = exact_u7_success(n)
        predicted = predicted_u7_success(n)
        if exact:
            successes += 1
        else:
            failures += 1
        if exact != predicted:
            mismatches.append(n)
            if len(mismatches) >= 20:
                break

    print(f"limit={limit:,}")
    print(f"checked={checked:,}")
    print(f"u7_successes={successes:,}")
    print(f"u7_failures={failures:,}")
    print(f"mismatches={len(mismatches)}")
    if mismatches:
        print("first mismatches:", mismatches)
        raise SystemExit(1)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000)
