"""Verify the single-bad-coordinate reduction at A=22339.

Only earlier moduli divisible by 37 are checked explicitly.  Every other earlier
modulus receives a unit-square residue and is excluded by the universal Jacobi
obstruction.
"""

from math import gcd

A = 22339
MA = 4 * A - 1
DS = (89, 251, 1988171, 5607089)
GOOD_TARGET_PRIMES = (3, 5, 7, 23)
BAD_PRIME = 37


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors_of_square(n):
    ds = [1]
    for p, e in factor(n).items():
        base = list(ds)
        ds = []
        pe = 1
        for _ in range(2 * e + 1):
            ds.extend(d * pe for d in base)
            pe *= p
    return ds


def crt(congruences):
    x, M = 0, 1
    for a, m in congruences:
        g = gcd(M, m)
        assert (a - x) % g == 0
        M1, m1 = M // g, m // g
        k = ((a - x) // g * pow(M1, -1, m1)) % m1
        x = (x + M * k) % (M * m1)
        M *= m1
    return x, M


def literal_square_lift(a, p):
    """Return x^2 as an integer, with x^2 == a (mod p).

    The literal square remains a square modulo every higher power p^e.
    """
    for x in range(1, p):
        if x * x % p == a % p:
            return x * x
    raise AssertionError((a, p))


def chosen_residue_for_modulus(D, m):
    target = (-4 * D) % MA
    fac = factor(m)
    congruences = []

    for p, e in fac.items():
        pe = p ** e
        if p == BAD_PRIME:
            # Any unit lift of the target nonresidue coordinate is allowed.
            # The literal representative is used at all powers of 37.
            congruences.append((target % BAD_PRIME, pe))
        elif p in GOOD_TARGET_PRIMES:
            congruences.append((literal_square_lift(target % p, p), pe))
        elif p == 67 and D in (251, 1988171):
            congruences.append((4, pe))
        else:
            congruences.append((1, pe))

    return crt(congruences)[0]


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def verify():
    assert MA == 89355
    assert factor(MA) == {3: 1, 5: 1, 7: 1, 23: 1, 37: 1}

    exceptional = []
    for B in range(1, A):
        if (4 * B - 1) % BAD_PRIME == 0:
            exceptional.append(B)
    assert len(exceptional) == 603

    checked = 0
    for D in DS:
        assert A * A % D == 0
        target = (-4 * D) % MA

        for p in GOOD_TARGET_PRIMES:
            assert legendre(target, p) == 1
        assert legendre(target, BAD_PRIME) == -1

        for B in exceptional:
            m = 4 * B - 1
            chosen = chosen_residue_for_modulus(D, m)

            # It must agree with the target on every shared target prime.
            g = gcd(MA, m)
            assert chosen % g == target % g

            traps = {(-4 * E) % m for E in divisors_of_square(B)}
            assert chosen not in traps, (D, B, m, chosen)
            assert gcd(chosen, m) == 1
            checked += 1

    return exceptional, checked


if __name__ == "__main__":
    exceptional, checked = verify()
    print("exceptional 37-bearing layers:", len(exceptional))
    print("local branch checks:", checked)
    print("first exceptional depths:", exceptional[:10])
    print("last exceptional depths:", exceptional[-10:])
    print("PASS: all single-bad-coordinate local checks are safe")
