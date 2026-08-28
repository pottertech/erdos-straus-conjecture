#!/usr/bin/env python3
"""Exact deterministic residue-cascade analysis for the corrected u-method.

For prime u == 3 (mod 4), x=(n+u)/4 and D=(nx)^2.  If distinct small
primes p_i are forced to divide x, write x = P*q with P=prod p_i.  The
safe guaranteed divisor basis for x^2 is then

    q^b * prod p_i^c_i,  b,c_i in {0,1,2},

not x^b * prod p_i^c_i (which can exceed the available exponents).
"""

from itertools import product
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

    # If u itself is forced to divide x then the target is 0 mod u and a
    # direct u-divisible divisor witness exists.  Handle that in class_covered.
    P = 1
    for p in extras:
        P = P * p % u
    if gcd(P, u) != 1:
        raise ValueError("u divides the forced factor product")

    qmod = xmod * pow(P, -1, u) % u
    vals = set()
    for a in range(3):
        for b in range(3):
            base = pow(nmod, a, u) * pow(qmod, b, u) % u
            for cs in product(range(3), repeat=len(extras)):
                v = base
                for p, c in zip(extras, cs):
                    v = v * pow(p, c, u) % u
                vals.add(v)
    return xmod, vals


def class_covered(r, modulus, u, primes=SMALL_FACTORS):
    extras = forced_factors(r, modulus, u, primes)
    if u in extras:
        return True, extras
    for nmod in possible_n_mod_u(r, modulus, u):
        xmod, vals = guaranteed_residues(nmod, u, extras)
        if (-nmod * xmod) % u not in vals:
            return False, extras
    return True, extras


def failure_residues(u, extras):
    bad = []
    for nmod in range(1, u):
        xmod, vals = guaranteed_residues(nmod, u, extras)
        if (-nmod * xmod) % u not in vals:
            bad.append(nmod)
    return bad


def qr_residues(u):
    return [a for a in range(1, u) if legendre_symbol(a, u) == 1]


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
    modulus = lcm(120, 4 * 7, 4 * 11, 4 * 13)
    residues = [
        r for r in range(modulus)
        if r % 120 in (1, 49) and gcd(r, 2 * 3 * 5 * 7 * 11 * 13) == 1
    ]
    uncovered = [
        r for r in residues
        if not any(class_covered(r, modulus, u)[0] for u in U_VALUES)
    ]

    print(f"\nResidual refinement modulo {modulus}")
    print(f"  admissible classes: {len(residues)}")
    print(f"  deterministically covered: {len(residues) - len(uncovered)}")
    print(f"  remaining: {len(uncovered)}")

    assert all(legendre_symbol(r, 7) == 1 for r in uncovered)
    print("  all remaining classes are QR mod 7")
    for p in (11, 13):
        qr = sum(1 for r in uncovered if legendre_symbol(r, p) == 1)
        print(f"  mod {p}: QR={qr}, QNR={len(uncovered)-qr}")


def verify_u7_qnr_lemma():
    # n == 1 or 49 mod 120 implies n == 1 mod 8, so for u=7,
    # x=(n+7)/4 is even.  Write x=2q and use q and 2 as independent
    # guaranteed factors of x.
    bad7 = failure_residues(7, [2])
    qr7 = qr_residues(7)
    assert bad7 == qr7
    print("\nVerified exact u=7 QNR reduction:")
    print(f"  failure residues = QR_7 = {bad7}")

    # Diagnostic only: these are not full-QNR lemmas.
    bad11 = failure_residues(11, [3])
    bad23 = failure_residues(23, [2, 3])
    print(f"  u=11 forced-factor failure residues: {bad11}")
    print(f"  u=23 forced-factor failure residues: {bad23}")


if __name__ == "__main__":
    base120_report()
    verify_u7_qnr_lemma()
    residual_120120_report()
