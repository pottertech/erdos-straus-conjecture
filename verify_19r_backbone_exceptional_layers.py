"""Verify the bounded exceptional-layer calculation for the 19r backbone."""

from math import isqrt

D = 10
C_VALUES = (3, 7, 11, 15)


def is_prime(n):
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


def candidates(c, require_divisibility=False):
    bound = D * c * c
    out = []
    for k in range(1, bound):
        max_h = (bound - 1) // k
        for h in range(1, max_h + 1):
            den = bound - k * h
            num = k + D * h - 2 * D * c
            if num <= 0 or num % den:
                continue
            r = num // den
            if r <= 1 or r % 40 != 21:
                continue
            if require_divisibility and (r * h + 1) % (16 * D):
                continue
            out.append((r, k, h, is_prime(r), (r * h + 1) % (16 * D)))
    return out


def equality_case_possible(c):
    # Equality kh=d*c^2 requires 4d | B, i.e. 16d | cr+1.
    # Check all four lifts of r == 21 (mod 40) modulo 160.
    return any((c * r + 1) % (16 * D) == 0 for r in (21, 61, 101, 141))


def verify():
    result = {}
    for c in C_VALUES:
        assert not equality_case_possible(c), c
        pre = candidates(c, require_divisibility=False)
        post = candidates(c, require_divisibility=True)
        assert post == [], (c, post)
        result[c] = {"before_160_condition": pre, "after_160_condition": post}

    # The only pre-divisibility candidates occur at c=11 and have r=21 or 61.
    assert {row[0] for row in result[11]["before_160_condition"]} == {21, 61}
    assert all(not row[3] or row[4] != 0 for row in result[11]["before_160_condition"])
    return result


if __name__ == "__main__":
    print(verify())
    print("PASS: no exceptional collision for prime r == 21 (mod 40)")
