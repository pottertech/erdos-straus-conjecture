"""Verify the twelve finite local checks in the three-ancestor proof at A=649."""

from math import gcd

A = 649
MA = 4 * A - 1
DS = (11, 59, 7139, 38291)
EXCEPTIONAL = ((130, 3), (303, 7), (476, 11))


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


def crt_two(a, m, b, n):
    assert gcd(m, n) == 1
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


def verify():
    assert MA == 2595
    assert factor(MA) == {3: 1, 5: 1, 173: 1}
    rows = []

    for D in DS:
        assert (A * A) % D == 0
        target = (-4 * D) % MA
        assert target % 3 == 1
        assert target % 5 in (1, 4)
        t173 = target % 173
        assert pow(t173, 86, 173) == 172  # Legendre symbol -1

        for B, cofactor in EXCEPTIONAL:
            m = 4 * B - 1
            assert m == 173 * cofactor
            chosen = crt_two(t173, 173, 1, cofactor)
            assert chosen % 173 == t173
            assert chosen % cofactor == 1

            trap_divisors = divisors_of_square(B)
            trap_residues = {(-4 * E) % m for E in trap_divisors}
            assert chosen not in trap_residues

            eclass = (-chosen * pow(4, -1, m)) % m
            assert not any((E - eclass) % m == 0 for E in trap_divisors)

            rows.append((B, D, chosen, eclass, len(trap_divisors)))

    expected_eclasses = {
        130: {11: 11, 59: 59, 7139: 392, 38291: 404},
        303: {11: 530, 59: 1097, 7139: 565, 38291: 404},
        476: {11: 184, 59: 1097, 7139: 1603, 38291: 404},
    }
    for B, D, _, eclass, _ in rows:
        assert eclass == expected_eclasses[B][D]

    return rows


if __name__ == "__main__":
    rows = verify()
    for row in rows:
        print("B=%d D=%d chosen=%d Eclass=%d divisors_checked=%d" % row)
    print("PASS: all twelve exceptional local checks are safe")
