"""Exact CRT covering solver for one square-completed Type-II progression.

Fix a target depth A and a realized divisor D|A^2.  The target progression is

    n = a + mA*k,
    mA = 4*A - 1,
    a = -4*D mod mA.

Each earlier depth B and each E|B^2 gives a Type-II trap

    n = -4*E mod mB,  mB = 4*B - 1.

If the two n-progressions are CRT-compatible, that earlier trap removes one
residue class of k modulo

    q = mB / gcd(mA,mB).

This program normalizes all such k-constraints and solves their union exactly.
It does NOT enumerate the full lcm of all q.  Instead it recursively refines a
current CRT class k == r (mod M), discarding constraints that can no longer
intersect that branch.  A return value of covered=True is a finite exact
certificate for the requested horizon B<=B_max.  Otherwise an explicit
uncovered arithmetic progression k == r (mod M) is returned.

This is a finite-horizon covering theorem only; it says nothing about depths
larger than B_max.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from math import gcd, lcm


def factor_small(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
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


def divisors_of_square(n: int) -> list[int]:
    ds = [1]
    for p, e in factor_small(n).items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(2 * e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return sorted(ds)


def validate_target(A: int, D: int) -> None:
    if A < 1 or D < 1 or (A * A) % D:
        raise ValueError("target requires D | A^2")


def induced_k_constraints(A: int, D: int, B_max: int):
    validate_target(A, D)
    mA = 4 * A - 1
    a = (-4 * D) % mA

    by_q: dict[int, set[int]] = {}
    provenance: dict[tuple[int, int], list[tuple[int, int]]] = {}

    for B in range(1, min(B_max, A - 1) + 1):
        mB = 4 * B - 1
        g = gcd(mA, mB)
        q = mB // g
        ma = mA // g

        for E in divisors_of_square(B):
            t = (-4 * E) % mB
            if (a - t) % g:
                continue

            # mA*k == t-a (mod mB).  Divide by g; ma is invertible mod q.
            if q == 1:
                # The entire target progression lies in this earlier trap.
                return {
                    "mA": mA,
                    "a": a,
                    "full_constraint": (B, E),
                    "constraints": {},
                    "provenance": {},
                }

            rhs = (t - a) // g
            c = (rhs * pow(ma, -1, q)) % q
            by_q.setdefault(q, set()).add(c)
            provenance.setdefault((q, c), []).append((B, E))

    return {
        "mA": mA,
        "a": a,
        "full_constraint": None,
        "constraints": {q: tuple(sorted(cs)) for q, cs in sorted(by_q.items())},
        "provenance": provenance,
    }


def compatible_residues(r: int, M: int, q: int, residues: tuple[int, ...]):
    g = gcd(M, q)
    return tuple(c for c in residues if (r - c) % g == 0)


def lifts_of_class(r: int, M: int, q: int):
    """All classes x mod lcm(M,q) reducing to r mod M."""
    g = gcd(M, q)
    L = lcm(M, q)
    count = q // g
    # x = r + M*j.  Distinct modulo L for j=0..count-1.
    return L, (r + M * j for j in range(count))


def exact_cover(constraints: dict[int, tuple[int, ...]], node_budget: int = 2_000_000):
    """Return either an exact finite cover certificate or an uncovered CRT class."""
    items = tuple((q, tuple(cs)) for q, cs in sorted(constraints.items()))
    nodes = 0

    @lru_cache(maxsize=None)
    def search(r: int, M: int, active: tuple[tuple[int, tuple[int, ...]], ...]):
        nonlocal nodes
        nodes += 1
        if nodes > node_budget:
            return ("budget", r, M, ())

        reduced = []
        for q, residues in active:
            cs = compatible_residues(r, M, q, residues)
            if not cs:
                continue
            if M % q == 0:
                if r % q in cs:
                    return ("covered", r, M, ((q, r % q),))
                continue
            reduced.append((q, cs))

        if not reduced:
            return ("uncovered", r, M, ())

        # Choose the refinement giving strong local coverage with modest branching.
        def score(item):
            q, cs = item
            g = gcd(M, q)
            branch = q // g
            # Higher removed fraction first, then lower branch factor.
            return (len(cs) / branch, -branch, len(cs))

        q, cs = max(reduced, key=score)
        L, lifts = lifts_of_class(r, M, q)
        remaining = tuple(item for item in reduced if item[0] != q)
        child_summaries = []

        for x in lifts:
            x %= L
            if x % q in cs:
                child_summaries.append(("covered", x, L, ((q, x % q),)))
                continue
            ans = search(x, L, remaining)
            if ans[0] == "uncovered":
                return ans
            if ans[0] == "budget":
                return ans
            child_summaries.append(ans)

        return ("covered", r, M, tuple(child_summaries))

    result = search(0, 1, items)
    return result, nodes


def run(A: int, D: int, B_max: int, node_budget: int):
    data = induced_k_constraints(A, D, B_max)
    if data["full_constraint"] is not None:
        B, E = data["full_constraint"]
        return {
            "A": A,
            "D": D,
            "B_max": B_max,
            "covered": True,
            "reason": "target progression is contained in one earlier trap",
            "covering_witness": {"B": B, "E": E},
            "nodes": 0,
        }

    result, nodes = exact_cover(data["constraints"], node_budget=node_budget)
    status, r, M, _ = result
    out = {
        "A": A,
        "D": D,
        "mA": data["mA"],
        "target_residue": data["a"],
        "B_max": B_max,
        "constraint_moduli": len(data["constraints"]),
        "constraint_classes": sum(len(v) for v in data["constraints"].values()),
        "nodes": nodes,
        "status": status,
        "covered": status == "covered",
    }
    if status == "uncovered":
        out["uncovered_k_progression"] = {"residue": r, "modulus": M}
        out["uncovered_n_progression"] = {
            "residue_expression": f"{data['a']} + {data['mA']}*({r} + {M}*j)",
        }
    elif status == "budget":
        out["note"] = "node budget exhausted; no mathematical conclusion"
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, required=True)
    ap.add_argument("--D", type=int, required=True)
    ap.add_argument("--B-max", type=int, required=True)
    ap.add_argument("--node-budget", type=int, default=2_000_000)
    ap.add_argument("--json")
    args = ap.parse_args()

    out = run(args.A, args.D, args.B_max, args.node_budget)
    print(json.dumps(out, indent=2))
    if args.json:
        with open(args.json, "w") as fh:
            json.dump(out, fh, indent=2)
