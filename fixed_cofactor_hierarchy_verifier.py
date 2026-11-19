"""Reproduce finite exceptional sets for the infinite fixed-cofactor hierarchy.

For a fixed prime s == 3 (mod 8), set
    d = (s+1)/2,
    M = 2(s+1),
    r == s+2 (mod M).
Every exceptional earlier modulus has form c*r with c<s, c==3 (mod 4).
The master equation bounds collisions by k*h < d*c^2, so the possible bad r
form a finite computable set.
"""

from math import gcd, lcm


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


def phi(n):
    x = n
    out = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            out -= out // p
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out -= out // x
    return out


def exceptional_parameters(s):
    assert is_prime(s) and s > 3 and s % 8 == 3
    d = (s + 1) // 2
    M = 2 * (s + 1)
    a = s + 2
    assert gcd(a, M) == 1
    bad = {}

    for c in range(3, s, 4):
        # Equality kh=d*c^2 requires 4d|B, equivalently 8(s+1)|cr+1.
        # Since r==1 mod s+1, this would imply c+1==0 mod s+1, impossible.
        bound = d * c * c
        hits = set()
        witnesses = []
        for k in range(1, bound):
            for h in range(1, (bound - 1) // k + 1):
                den = bound - k * h
                num = k + d * h - 2 * d * c
                if num <= 0 or num % den:
                    continue
                r = num // den
                if r <= s or r % M != a or not is_prime(r):
                    continue
                if (r * h + 1) % (16 * d):
                    continue
                hits.add(r)
                witnesses.append((r, k, h))
        if hits:
            bad[c] = {"primes": sorted(hits), "witnesses": witnesses}
    return bad


def hierarchy_partial_coefficient(limit):
    total = 0.0
    count = 0
    for s in range(11, limit + 1, 8):
        if not is_prime(s):
            continue
        total += 4.0 / (s * phi(2 * (s + 1)))
        count += 1
    return count, total


def regression():
    # Previously clean rows.
    for s in (11, 19, 43, 59, 67):
        bad = exceptional_parameters(s)
        assert not bad, (s, bad)

    # First known nonempty finite exceptional set in the natural d=(s+1)/2 pattern.
    bad83 = exceptional_parameters(83)
    assert 23 in bad83
    assert 1429 in bad83[23]["primes"]

    count, coeff = hierarchy_partial_coefficient(100000)
    assert coeff > 0.0676803
    return {"s83": bad83, "partial_count": count, "partial_coefficient": coeff}


if __name__ == "__main__":
    print(regression())
    print("PASS: fixed-cofactor hierarchy finite-exception regression")
