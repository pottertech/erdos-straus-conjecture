"""Verify certified post-Jacobi fixed-cofactor backbone rows.

The verifier checks:
  * d | A for the prescribed prime progression;
  * the fixed s-coordinate is a quadratic residue;
  * the variable r-coordinate has constant quadratic character -1 on sampled
    primes in the progression (the manuscript gives the reciprocity proof);
  * equality cases are incompatible;
  * no bounded exceptional-layer equation has an admissible prime solution.
"""

from math import gcd, lcm

ROWS = [
    # s, d, a, M
    (23, 20, 73, 80),
    (31, 17, 57, 68),
    (43, 22, 45, 88),
    (47, 43, 161, 172),
    (59, 30, 61, 120),
    (67, 34, 69, 136),
]


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


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return -1 if x == p - 1 else x


def exceptional_candidates(s, d, a, M):
    failures = []
    summaries = {}
    for c in range(3, s, 4):
        # Equality kh=d*c^2 would require 4d | B, equivalently 16d | cr+1.
        L = lcm(M, 16 * d)
        equality_lifts = [r for r in range(a, L, M) if (c * r + 1) % (16 * d) == 0]
        if equality_lifts:
            failures.append(("equality", c, equality_lifts))

        bound = d * c * c
        pre = []
        post = []
        for k in range(1, bound):
            for h in range(1, (bound - 1) // k + 1):
                den = bound - k * h
                num = k + d * h - 2 * d * c
                if num <= 0 or num % den:
                    continue
                r = num // den
                if r <= 1 or r % M != a:
                    continue
                row = (r, k, h, is_prime(r), (r * h + 1) % (16 * d))
                pre.append(row)
                if row[3] and row[4] == 0:
                    post.append(row)
        if post:
            failures.append(("collision", c, post))
        summaries[c] = {"equation_candidates": pre, "admissible": post}
    return failures, summaries


def verify_row(s, d, a, M):
    assert M == 4 * d
    assert gcd(a, M) == 1
    assert (s * a + 1) % (4 * d) == 0
    assert legendre(-d, s) == 1

    # Regression check of the constant variable-prime character.
    samples = []
    n = a
    while n < 200000 and len(samples) < 20:
        if is_prime(n) and gcd(n, 2 * d) == 1:
            assert legendre(-d, n) == -1, (s, d, n)
            samples.append(n)
        n += M
    assert samples, (s, d)

    failures, summaries = exceptional_candidates(s, d, a, M)
    assert not failures, (s, failures)
    return {
        "s": s,
        "d": d,
        "progression": (a, M),
        "sample_primes": samples,
        "exceptional_cofactors": list(summaries),
        "candidate_counts": {c: len(v["equation_candidates"]) for c, v in summaries.items()},
    }


def verify_all():
    return [verify_row(*row) for row in ROWS]


if __name__ == "__main__":
    for row in verify_all():
        print(row)
    print("PASS: all certified fixed-cofactor rows have no admissible exceptional collision")
