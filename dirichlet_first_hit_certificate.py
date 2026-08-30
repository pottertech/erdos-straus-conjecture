"""Upgrade an exact finite CRT-cover survivor to a Dirichlet prime progression.

This imports global_first_hit_crt_cover_solver.run().  If that solver returns an
uncovered k-progression, then

    n = a + mA * (r + M*j)

is an arithmetic progression avoiding every square-completed Type-II layer
B <= B_max while remaining inside the target depth-A Type-II progression.

When gcd(n0, step)=1, Dirichlet's theorem gives infinitely many primes in the
progression.  An optional additional congruence n == core_residue (mod 840)
can be imposed when CRT-compatible; the resulting class is again checked to
be reduced.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, lcm

from global_first_hit_crt_cover_solver import run as cover_run


def crt_pair(a: int, m: int, b: int, n: int):
    g = gcd(m, n)
    if (b - a) % g:
        return None
    mm, nn = m // g, n // g
    t = ((b - a) // g) * pow(mm, -1, nn) % nn
    x = (a + m * t) % lcm(m, n)
    return x, lcm(m, n)


def certificate(A: int, D: int, B_max: int, node_budget: int, core_residue=None):
    out = cover_run(A, D, B_max, node_budget)
    if out.get("status") != "uncovered":
        return {
            "cover_result": out,
            "dirichlet_certificate": False,
            "reason": "exact cover solver did not return an uncovered class",
        }

    mA = out["mA"]
    a = out["target_residue"]
    r = out["uncovered_k_progression"]["residue"]
    M = out["uncovered_k_progression"]["modulus"]

    n0 = a + mA * r
    step = mA * M
    reduced = gcd(n0, step) == 1

    cert = {
        "A": A,
        "D": D,
        "B_max": B_max,
        "n_residue": n0 % step,
        "n_modulus": step,
        "gcd": gcd(n0, step),
        "reduced": reduced,
        "consequence_if_reduced": (
            f"infinitely many primes have Type-II square depth > {B_max} "
            f"and <= {A}"
        ),
    }

    if core_residue is not None:
        merged = crt_pair(n0, step, core_residue, 840)
        if merged is None:
            cert["core_intersection"] = {
                "requested_residue_mod_840": core_residue,
                "compatible": False,
            }
        else:
            x, mod = merged
            cert["core_intersection"] = {
                "requested_residue_mod_840": core_residue,
                "compatible": True,
                "residue": x,
                "modulus": mod,
                "gcd": gcd(x, mod),
                "reduced": gcd(x, mod) == 1,
                "dirichlet": gcd(x, mod) == 1,
            }

    return {
        "cover_result": {
            k: v for k, v in out.items()
            if k not in ("uncovered_k_progression", "uncovered_n_progression")
        },
        "dirichlet_certificate": cert,
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, required=True)
    ap.add_argument("--D", type=int, required=True)
    ap.add_argument("--B-max", type=int, required=True)
    ap.add_argument("--node-budget", type=int, default=2_000_000)
    ap.add_argument("--core-residue", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()

    out = certificate(args.A, args.D, args.B_max, args.node_budget, args.core_residue)
    print(json.dumps(out, indent=2))
    if args.json:
        with open(args.json, "w") as fh:
            json.dump(out, fh, indent=2)
