"""Exact certificates for all four realized primitive classes at depth 22339.

For each D in {89, 251, 22361, 67079}, reconstruct every earlier
square-completed Type-II trap B < 22339, convert intersections to forbidden
k-congruences, build the deterministic least-unary-safe prime-power baseline,
apply the compact D-specific overrides below, and verify:

  * every unary exclusion is avoided;
  * every composite forbidden tuple is avoided;
  * the resulting denominator progression is reduced;
  * a compatible classical residue class modulo 840 exists.

CRT + Dirichlet then gives infinitely many primes of exact Type-II square depth
22339 from each of the four target divisor classes.
"""

from collections import defaultdict
from functools import lru_cache
from math import gcd
import json

A = 22339
MA = 4 * A - 1

CASES = {
    89: {
        "core": 169,
        "overrides": {61: 2, 71: 1, 173: 1, 211: 1, 233: 1, 331: 1, 337: 1,
                      457: 1, 607: 2, 653: 1, 881: 1, 911: 1, 1361: 2, 1459: 1, 2887: 1},
    },
    251: {
        "core": 361,
        "overrides": {7: 3, 53: 2, 59: 1, 71: 1, 83: 1, 113: 1, 127: 1, 131: 1,
                      137: 1, 163: 1, 479: 2, 821: 1, 829: 1, 1051: 1, 1091: 1,
                      1511: 1, 1567: 1, 1667: 1, 1979: 1, 2903: 1, 6803: 1},
    },
    22361: {
        "core": 121,
        "overrides": {19: 3, 31: 2, 47: 1, 53: 1, 131: 1, 149: 3, 227: 1, 359: 1,
                      409: 2, 419: 1, 677: 1, 811: 1, 977: 2, 2029: 1, 2671: 1, 2843: 1},
    },
    67079: {
        "core": 169,
        "overrides": {19: 4, 41: 2, 47: 3, 107: 2, 293: 1, 331: 1, 853: 1,
                      5227: 1, 5569: 1},
    },
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
                raise AssertionError(("contained in earlier trap", D, B, E))
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
        for x in range(modulus):
            if unary_ok(p, x):
                assignment[p] = x
                break
        else:
            raise AssertionError(("unary coordinate fully covered", D, p))

    for p, x in case["overrides"].items():
        assert p in max_power
        assert unary_ok(p, x)
        assignment[p] = x

    for p, by_q in unary.items():
        for q, bans in by_q.items():
            assert assignment[p] % q not in bans, (D, "unary", p, q)

    for comps, c, q in composite:
        assert not all(assignment[p] % pe == c % pe for p, pe in comps), (D, "composite", q, c)

    bad = []
    for p in sorted(max_power):
        if MA % p == 0:
            residue = target % p
        else:
            residue = (target + MA * (assignment[p] % p)) % p
        if residue == 0:
            bad.append(p)
    assert not bad, (D, "non-reduced", bad)

    core = case["core"]
    assert target % 105 == core % 105
    # Solve (MA/105) k == (core-target)/105 (mod 8).
    lhs = (MA // 105) % 8
    rhs = ((core - target) // 105) % 8
    k8 = (rhs * pow(lhs, -1, 8)) % 8
    assert (target + MA * k8 - core) % 840 == 0

    return {
        "D": D,
        "target_residue_mod_89355": target,
        "classical_core_mod_840": core,
        "k_mod_8_for_core": k8,
        "constraint_moduli": len(constraints),
        "constraint_classes": sum(len(v) for v in constraints.values()),
        "prime_power_coordinates": len(max_power),
        "composite_forbidden_tuples": len(composite),
        "override_count": len(case["overrides"]),
        "reduced": True,
        "exact_depth": A,
    }


def verify_all():
    out = [verify_case(D, CASES[D]) for D in sorted(CASES)]
    return {
        "A": A,
        "mA": MA,
        "cases": out,
        "conclusion": "all four realized primitive classes support infinitely many primes of exact Type-II square depth 22339",
    }


if __name__ == "__main__":
    print(json.dumps(verify_all(), indent=2))
