"""Regression checks for the symbolic composite exact-depth theorem.

These tests are not part of the proof. They guard against transcription errors in
A_q=(3q+1)/4, witness selection, target residues, and the universal-safe-residue
construction.
"""

from math import gcd

CASES = [
    # q, witness D
    (13, 2),   # A=10, elementary D=2 family
    (29, 11),  # A=22, odd witness 11 == 2 mod 3
    (73, 5),   # A=55, odd witness 5 == 2 mod 3
    (113, 17), # A=85, odd witness 17 == 2 mod 3
    (193, 29), # A=145, odd witness 29 == 2 mod 3
]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def safe_residue_check(B: int) -> bool:
    m = 4 * B - 1
    return all((4 * E + 1) % m != 0 for E in divisors(B * B))


def check_case(q: int, D: int):
    assert is_prime(q)
    assert q % 4 == 1
    A = (3 * q + 1) // 4
    assert 4 * A - 1 == 3 * q
    assert (A * A) % D == 0
    assert D % 3 == 2
    target = (-4 * D) % (3 * q)
    assert target % 3 == 1

    # q cannot divide any earlier layer modulus.
    for B in range(1, A):
        mB = 4 * B - 1
        assert mB % q != 0
        assert gcd(3 * q, mB) in (1, 3)
        assert safe_residue_check(B)

    return {
        "q": q,
        "A": A,
        "D": D,
        "target_mod_3q": target,
        "checked_earlier_depths": A - 1,
    }


def main():
    rows = [check_case(q, D) for q, D in CASES]
    for row in rows:
        print(row)
    print("PASS: symbolic backbone regression suite")


if __name__ == "__main__":
    main()
