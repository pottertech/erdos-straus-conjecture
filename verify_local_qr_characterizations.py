#!/usr/bin/env python3
"""Audit the exact u=7, u=11, and u=23 QR characterizations.

Default limit is 1,000,000. Pass a larger integer to extend the audit.
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


def exact_u_success(n, u):
    x = (n + u) // 4
    D = (n * x) ** 2
    target = (-n * x) % u
    x2 = {p: 2 * e for p, e in factorint(x).items()}
    for a in range(3):
        for e_div in divisors_from_factorization(x2):
            d1 = n**a * e_div
            if d1 % u != target:
                continue
            if (D // d1) % u == target:
                return True
    return False


def all_support_qr(n, x, u):
    if legendre_symbol(n, u) != 1:
        return False
    return all(p == u or legendre_symbol(p, u) == 1 for p in factorint(x))


def predicted_u7(n):
    x = (n + 7) // 4
    return not all_support_qr(n, x, 7)


def predicted_u11(n):
    x = (n + 11) // 4
    assert x % 9 == 0
    return not all_support_qr(n, x, 11)


def predicted_u23(n):
    x = (n + 23) // 4
    assert x % 6 == 0 and (x % 4 == 0 or x % 9 == 0)
    return not all_support_qr(n, x, 23)


def main(limit):
    stats = {
        7: [0, 0, 0],   # checked, failures, mismatches
        11: [0, 0, 0],
        23: [0, 0, 0],
    }

    for n in primerange(2, limit + 1):
        if n % 120 not in (1, 49) or not is_hard_case(n):
            continue

        # u=7: all residual-base cases.
        exact = exact_u_success(n, 7)
        pred = predicted_u7(n)
        stats[7][0] += 1
        stats[7][1] += int(not exact)
        stats[7][2] += int(exact != pred)

        # u=11: v3(x_11) >= 2.
        if n % 36 == 25:
            exact = exact_u_success(n, 11)
            pred = predicted_u11(n)
            stats[11][0] += 1
            stats[11][1] += int(not exact)
            stats[11][2] += int(exact != pred)

        # u=23: v2(x_23) >= 2 or v3(x_23) >= 2.
        if n % 16 == 9 or n % 36 == 13:
            exact = exact_u_success(n, 23)
            pred = predicted_u23(n)
            stats[23][0] += 1
            stats[23][1] += int(not exact)
            stats[23][2] += int(exact != pred)

    print(f"limit={limit:,}")
    for u in (7, 11, 23):
        checked, failures, mismatches = stats[u]
        print(f"u={u}: checked={checked:,}, failures={failures:,}, mismatches={mismatches}")
        if mismatches:
            raise SystemExit(1)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000)
