"""Exact finite certificate for a global first-hit square depth of 22339.

Target layer:
    A = 22339
    D = 67079 | A^2
    mA = 4*A - 1 = 89355
    n == -4*D == 89104 (mod 89355)

For every earlier depth 1 <= B < A and every E | B^2, an intersecting
Type-II trap induces one forbidden congruence k == c (mod q), where

    n = 89104 + 89355*k,
    q = (4*B-1) / gcd(89355, 4*B-1).

This script reconstructs all such forbidden congruences, decomposes them into
prime-power coordinates, and verifies a compact satisfying assignment.

Certificate representation:
  * for each prime-power coordinate, start from the least nonnegative residue
    satisfying all unary (prime-power modulus) exclusions;
  * apply the nine overrides listed in OVERRIDES;
  * verify every composite forbidden tuple is avoided;
  * verify that n is nonzero modulo every prime dividing the CRT period.

By the Chinese remainder theorem the coordinate assignment determines a
nonempty arithmetic progression of k.  The local nondivisibility checks prove
that the corresponding n progression is reduced.  Dirichlet therefore gives
infinitely many primes in it.  All earlier square-completed Type-II depths fail
on that progression, while (A,D) gives a depth-22339 Type-II certificate.

The theorem is computationally assisted only in the finite generation and
checking of the explicit congruence system.  No primality sampling is used.
"""

from collections import defaultdict
from functools import lru_cache
from math import gcd

A = 22339
D = 67079
MA = 4 * A - 1
TARGET = (-4 * D) % MA

# Relative to the deterministic least-unary-safe baseline.
OVERRIDES = {
    19: 4,
    41: 2,
    47: 3,
    107: 2,
    293: 1,
    331: 1,
    853: 1,
    5227: 1,
    5569: 1,
}


def factor_small(n):
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


@lru_cache(maxsize=None)
def divisors_of_square(n):
    ds = [1]
    for p, e in factor_small(n).items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(2 * e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return tuple(ds)


def induced_constraints():
    by_q = defaultdict(set)
    for B in range(1, A):
        mB = 4 * B - 1
        g = gcd(MA, mB)
        q = mB // g
        ma = MA // g
        for E in divisors_of_square(B):
            t = (-4 * E) % mB
            if (TARGET - t) % g:
                continue
            if q == 1:
                raise AssertionError(("target contained in earlier trap", B, E))
            rhs = (t - TARGET) // g
            c = (rhs * pow(ma, -1, q)) % q
            by_q[q].add(c)
    return {q: tuple(sorted(cs)) for q, cs in by_q.items()}


def prime_power_components(q):
    return tuple((p, p ** e) for p, e in factor_small(q).items())


def build_certificate(constraints):
    max_power = {}
    unary = defaultdict(lambda: defaultdict(set))
    composite = []

    for q, cs in constraints.items():
        fac = factor_small(q)
        comps = tuple((p, p ** e) for p, e in fac.items())
        for p, pe in comps:
            max_power[p] = max(max_power.get(p, 1), pe)
        if len(fac) == 1:
            p = next(iter(fac))
            unary[p][q].update(cs)
        else:
            for c in cs:
                composite.append((comps, c, q))

    def unary_ok(p, x):
        return all(x % q not in bans for q, bans in unary[p].items())

    assignment = {}
    for p, modulus in sorted(max_power.items()):
        if p not in unary:
            assignment[p] = 0
            continue
        for x in range(modulus):
            if unary_ok(p, x):
                assignment[p] = x
                break
        else:
            raise AssertionError(("unary coordinate fully covered", p, modulus))

    for p, x in OVERRIDES.items():
        if p not in max_power:
            raise AssertionError(("override prime absent", p))
        if not unary_ok(p, x):
            raise AssertionError(("override violates unary constraints", p, x))
        assignment[p] = x

    return max_power, unary, composite, assignment


def verify():
    assert A * A % D == 0
    assert MA == 89355
    assert TARGET == 89104
    assert gcd(TARGET, MA) == 1

    constraints = induced_constraints()
    max_power, unary, composite, assignment = build_certificate(constraints)

    # Verify every unary exclusion exactly.
    unary_classes = 0
    for p, by_q in unary.items():
        x = assignment[p]
        for q, bans in by_q.items():
            unary_classes += len(bans)
            assert x % q not in bans, ("unary violation", p, q, x % q)

    # Verify every composite forbidden tuple exactly.
    composite_classes = 0
    for comps, c, q in composite:
        composite_classes += 1
        violated = all(assignment[p] % pe == c % pe for p, pe in comps)
        assert not violated, ("composite violation", q, c)

    # Reduced progression check.  Let M be the product of the pairwise-coprime
    # maximal prime powers.  We need gcd(TARGET + MA*k0, MA*M)=1.  It suffices
    # to check modulo each prime divisor locally; CRT existence supplies k0.
    bad_primes = []
    for p in sorted(max_power):
        if MA % p == 0:
            residue = TARGET % p
        else:
            residue = (TARGET + MA * (assignment[p] % p)) % p
        if residue == 0:
            bad_primes.append(p)
    assert not bad_primes, ("non-reduced n progression", bad_primes)

    # Optional classical-core intersection.  TARGET == 64 (mod 105) and
    # 169 == 64 (mod 105), so n == 169 (mod 840) is compatible.  Since the
    # k-period is odd, imposing k == 3 (mod 8) is an independent CRT condition.
    assert TARGET % 105 == 169 % 105
    assert (MA // 105) % 8 == 3
    assert ((169 - TARGET) // 105) % 8 == 1
    assert (3 * 3) % 8 == 1  # k == 3 mod 8 solves the reduced equation.

    return {
        "A": A,
        "D": D,
        "mA": MA,
        "target_residue": TARGET,
        "earlier_depths_checked": A - 1,
        "constraint_moduli": len(constraints),
        "constraint_classes": sum(len(v) for v in constraints.values()),
        "prime_power_coordinates": len(max_power),
        "unary_forbidden_classes": unary_classes,
        "composite_forbidden_classes": composite_classes,
        "overrides": dict(sorted(OVERRIDES.items())),
        "reduced_progression": True,
        "classical_core_intersection": "n == 169 (mod 840)",
        "conclusion": "infinitely many primes have exact Type-II square depth 22339",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(verify(), indent=2))
