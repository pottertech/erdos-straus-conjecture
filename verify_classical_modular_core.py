#!/usr/bin/env python3
"""Verify the corrected classical modular identities and six-class CRT core.

This script uses exact integer arithmetic only.  It is intentionally independent
of the u-method verifier.
"""

from fractions import Fraction


def check(n: int, xyz: tuple[int, int, int]) -> bool:
    x, y, z = xyz
    return x > 0 and y > 0 and z > 0 and (
        Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
    )


def mod8_5(n: int):
    assert n % 8 == 5
    return ((n + 3) // 4, n * (n + 3) // 8, n * (n + 3) // 4)


def mod15_7(n: int):
    assert n % 15 == 7
    return (2 * (2 * n + 1) // 15, 4 * n, 4 * n * (2 * n + 1) // 15)


def mod15_13(n: int):
    assert n % 15 == 13
    return (4 * (n + 2) // 15, 4 * n, 2 * n * (n + 2) // 15)


def mod7_3(n: int):
    assert n % 7 == 3
    return ((2 * n + 1) // 7, 2 * n, 2 * n * (2 * n + 1) // 7)


def mod7_5(n: int):
    assert n % 7 == 5
    return (2 * (n + 2) // 7, 2 * n, n * (n + 2) // 7)


def mod7_6(n: int):
    assert n % 7 == 6
    return (2 * (n + 1) // 7, 2 * n, 2 * n * (n + 1) // 7)


def verify_family(modulus: int, residue: int, fn, limit: int = 100_000):
    tested = 0
    for n in range(max(2, residue), limit + 1):
        if n % modulus != residue:
            continue
        xyz = fn(n)
        if not check(n, xyz):
            raise AssertionError((modulus, residue, n, xyz))
        tested += 1
    return tested


def six_core_residues():
    return [
        r for r in range(840)
        if r % 24 == 1 and r % 5 in (1, 4) and r % 7 in (1, 2, 4)
    ]


def main():
    families = [
        (8, 5, mod8_5),
        (15, 7, mod15_7),
        (15, 13, mod15_13),
        (7, 3, mod7_3),
        (7, 5, mod7_5),
        (7, 6, mod7_6),
    ]
    for modulus, residue, fn in families:
        count = verify_family(modulus, residue, fn)
        print(f"verified {count:6d} values for n == {residue} (mod {modulus})")

    core = six_core_residues()
    expected = [1, 121, 169, 289, 361, 529]
    print("six-class CRT core:", core)
    if core != expected:
        raise AssertionError((core, expected))

    print("all exact modular identity and CRT checks passed")


if __name__ == "__main__":
    main()
