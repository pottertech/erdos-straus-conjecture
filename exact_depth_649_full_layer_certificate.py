"""Exact certificates for all four realized primitive classes at depth 649."""

from collections import defaultdict
from functools import lru_cache
from math import gcd
import json

A = 649
MA = 4 * A - 1

CASES = {
    11: {"core": 1, "overrides": {71: 2, 113: 1, 2551: 1}},
    59: {"core": 169, "overrides": {7: 3, 29: 1, 31: 1, 107: 1, 271: 1, 337: 1}},
    7139: {"core": 169, "overrides": {17: 3, 19: 1, 29: 1, 37: 1, 229: 1}},
    38291: {"core": 121, "overrides": {13: 1, 29: 3, 37: 1, 41: 1, 71: 1, 317: 1}},
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


def induced_constraints(D):
    target = (-4 * D) % MA
    by_q = defaultdict(set)
    for B in range(1, A):
        mB = 4 * B - 1
        g = gcd(MA, mB)
        q = mB // g
        ma = MA // g
        for E in divisors_of_square(B):
            t = (-4 * E) % mB
            if (target - t) % g:
                continue
            if q == 1:
                raise AssertionError((D, B, E))
            rhs = (t - target) // g
            c = (rhs * pow(ma, -1, q)) % q
            by_q[q].add(c)
    return target, {q: tuple(sorted(cs)) for q, cs in by_q.items()}


def verify_case(D, case):
    assert A * A % D == 0
    target, constraints = induced_constraints(D)
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
        assignment[p] = next(x for x in range(modulus) if unary_ok(p, x))

    for p, x in case["overrides"].items():
        assert unary_ok(p, x)
        assignment[p] = x

    for p, by_q in unary.items():
        for q, bans in by_q.items():
            assert assignment[p] % q not in bans
    for comps, c, q in composite:
        assert not all(assignment[p] % pe == c % pe for p, pe in comps), (D, q, c)

    for p in max_power:
        residue = target % p if MA % p == 0 else (target + MA * (assignment[p] % p)) % p
        assert residue != 0, (D, p)

    core = case["core"]
    g = gcd(MA, 840)
    assert target % g == core % g
    reduced_mod = 840 // g
    lhs = (MA // g) % reduced_mod
    rhs = ((core - target) // g) % reduced_mod
    k_class = (rhs * pow(lhs, -1, reduced_mod)) % reduced_mod
    # Compatibility with the already-fixed odd prime-power coordinates.
    # CRT compatibility is modulo gcd(pe, reduced_mod), not min(pe, reduced_mod).
    for p, pe in ((p, pe) for p, pe in max_power.items() if reduced_mod % p == 0):
        overlap = gcd(pe, reduced_mod)
        assert k_class % overlap == assignment[p] % overlap

    return {
        "D": D,
        "target": target,
        "core": core,
        "constraint_moduli": len(constraints),
        "constraint_classes": sum(len(v) for v in constraints.values()),
        "override_count": len(case["overrides"]),
        "exact_depth": A,
    }


def verify_all():
    return {
        "A": A,
        "mA": MA,
        "cases": [verify_case(D, CASES[D]) for D in sorted(CASES)],
        "conclusion": "all four realized primitive classes support infinitely many primes of exact Type-II square depth 649",
    }


if __name__ == "__main__":
    print(json.dumps(verify_all(), indent=2))
