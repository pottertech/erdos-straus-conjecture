#!/usr/bin/env python3
"""Exact deterministic residue-cascade analysis for the corrected u-method.

For prime u == 3 (mod 4), x=(n+u)/4 and D=(nx)^2.  We only use divisors
that are guaranteed from n, x, and small primes p whose divisibility p|x is
forced by the residue class under study.  A residue class is certified for u
when every admissible n mod u has a guaranteed divisor d with

    d == -n*x (mod u).

For units modulo u, the complementary divisor then has the same residue
because D == (-n*x)^2 (mod u).
"""

from math import gcd, lcm
from sympy import primerange, legendre_symbol

U_VALUES = [p for p in primerange(3, 128) if p % 4 == 3]
BASE_CLASSES = [1, 13, 37, 49, 61, 73, 97, 109]
SMALL_FACTORS = [2, 3, 5, 7, 11, 13]


def possible_n_mod_u(r, modulus, u):
    if modulus % u == 0:
        a = r % u
        return [] if a == 0 else [a]
    return list(range(1, u))


def forced_factors(r, modulus, u, primes=SMALL_FACTORS):
    return [p for p in primes if modulus % (4 * p) == 0 and (r + u) % (4 * p) == 0]


def guaranteed_residues(nmod, u, extras):
    inv4 = pow(4, -1, u)
    xmod = nmod * inv4 % u
    vals = {
        pow(nmod, a, u) * pow(xmod, b, u) % u
        for a in range(3)
        for b in range(3)
    }
    for p in extras:
        vals = {v * pow(p, c, u) % u for v in vals for c in range(3)}
    return xmod, vals


def class_covered(r, modulus, u, primes=SMALL_FACTORS):
    extras = forced_factors(r, modulus, u, primes)
    for nmod in possible_n_mod_u(r, modulus, u):
        xmod, vals = guaranteed_residues(nmod, u, extras)
        target = (-nmod * xmod) % u
        if target not in vals:
            return False, extras
    return True, extras


def base120_report():
    print("Exact guaranteed coverage modulo 120")
    for r in BASE_CLASSES:
        hits = []
        for u in U_VALUES:
            ok, extras = class_covered(r, 120, u, [2, 3, 5])
            if ok:
                hits.append((u, extras))
        print(f"  n == {r:3d} (mod 120): {hits or 'NO universal hit'}")


def residual_120120_report():
    modulus = lcm(120, 4 * 7, 4 * 11, 4 * 13)  # 120120
    residues = [
        r for r in range(modulus)
        if r % 120 in (1, 49) and gcd(r, 2 * 3 * 5 * 7 * 11 * 13) == 1
    ]
    uncovered = []
    for r in residues:
        if not any(class_covered(r, modulus, u)[0] for u in U_VALUES):
            uncovered.append(r)

    print(f"\nResidual refinement modulo {modulus}")
    print(f"  admissible classes: {len(residues)}")
    print(f"  deterministically covered: {len(residues) - len(uncovered)}")
    print(f"  remaining: {len(uncovered)}")

    assert all(legendre_symbol(r, 7) == 1 for r in uncovered)
    assert all(legendre_symbol(r, 11) == 1 for r in uncovered)
    q13 = sum(1 for r in uncovered if legendre_symbol(r, 13) == 1)
    n13 = len(uncovered) - q13
    print("  all remaining classes are QR mod 7 and QR mod 11")
    print(f"  mod 13: QR={q13}, QNR={n13}")


def verify_qnr_lemmas():
    # Residual base classes n == 1 or 49 mod 120 have n == 1 mod 8.
    # For u=7, x=(n+7)/4 is even, so factor 2 is guaranteed.
    bad7 = []
    for nmod in range(1, 7):
        xmod, vals = guaranteed_residues(nmod, 7, [2])
        if (-nmod * xmod) % 7 not in vals:
            bad7.append(nmod)
    qr7 = [a for a in range(1, 7) if legendre_symbol(a, 7) == 1]
    assert bad7 == qr7

    # For u=11 and n == 1 mod 12, 3 | (n+11)/4, so factor 3 is guaranteed.
    bad11 = []
    for nmod in range(1, 11):
        xmod, vals = guaranteed_residues(nmod, 11, [3])
        if (-nmod * xmod) % 11 not in vals:
            bad11.append(nmod)
    qr11 = [a for a in range(1, 11) if legendre_symbol(a, 11) == 1]
    assert bad11 == qr11

    print("\nVerified deterministic QNR reductions:")
    print(f"  u=7 failure residues  = QR_7  = {bad7}")
    print(f"  u=11 failure residues = QR_11 = {bad11}")


if __name__ == "__main__":
    base120_report()
    verify_qnr_lemmas()
    residual_120120_report()
