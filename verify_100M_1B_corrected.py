#!/usr/bin/env python3
"""
Exhaustive verification of prime hard cases.

This verifier uses the exact u-method factorization

    (u y - n x)(u z - n x) = n^2 x^2,

with x = (n + u)/4.  A candidate u succeeds only when an actual divisor
pair d1*d2 = n^2*x^2 satisfies

    d1 == d2 == -n*x (mod u).

This deliberately avoids the previously used three-target shortcut
{-x*n^j : j = 0,1,2}, which is not equivalent in general.
"""

import json
import sys
import time

import sympy
from sympy import factorint


def is_hard_case_fast(n, n_mod_12, n_mod_5):
    """Return True exactly for the repository's prime hard-case criterion."""
    if n_mod_12 != 1:
        return False
    if n_mod_5 == 0:
        return False

    b3 = n * (n + 3) // 4
    while b3 % 2 == 0:
        b3 //= 2

    # 3 is an odd prime and is not 1 mod 3, so its presence excludes hardness.
    if b3 % 3 == 0:
        return False

    return all(p % 3 == 1 for p in factorint(b3).keys())


def divisors_from_factorization(factors):
    """Yield every positive divisor represented by a {prime: exponent} map."""
    items = list(factors.items())

    def rec(i, acc):
        if i == len(items):
            yield acc
            return
        p, e = items[i]
        pe = 1
        for _ in range(e + 1):
            yield from rec(i + 1, acc * pe)
            pe *= p

    yield from rec(0, 1)


def verify_u_witness(n, u, d1, d2):
    """Check the exact algebraic witness, including the unit-fraction identity."""
    if u <= 0 or (n + u) % 4 != 0:
        return False

    x = (n + u) // 4
    D = (n * x) ** 2
    target = (-n * x) % u

    if d1 <= 0 or d2 <= 0 or d1 * d2 != D:
        return False
    if d1 % u != target or d2 % u != target:
        return False

    if (d1 + n * x) % u != 0 or (d2 + n * x) % u != 0:
        return False

    y = (d1 + n * x) // u
    z = (d2 + n * x) // u
    if y <= 0 or z <= 0:
        return False

    # Cross-multiplied exact identity; no floating-point arithmetic.
    return 4 * x * y * z == n * (y * z + x * z + x * y)


def u_method_solve(n, u_max=300):
    """
    Find the least u == 3 (mod 4) <= u_max satisfying the exact u-method.

    For prime n, every divisor of D=n^2*x^2 can be written n^a*e with
    a in {0,1,2} and e|x^2.  We enumerate those actual divisors and test
    both members of the complementary divisor pair directly.

    Returns a witness dictionary, or None.
    """
    for u in range(3, u_max + 1, 4):
        if (n + u) % 4 != 0:
            continue

        x = (n + u) // 4
        if x <= 0:
            continue

        D = (n * x) ** 2
        target = (-n * x) % u
        x_factors = factorint(x)
        x2_factors = {p: 2 * e for p, e in x_factors.items()}
        nx = n * x

        divisor_count = 1
        for e in x2_factors.values():
            divisor_count *= e + 1

        for a in range(3):
            n_power = n ** a
            for e_div in divisors_from_factorization(x2_factors):
                d1 = n_power * e_div
                if d1 % u != target:
                    continue

                d2 = D // d1
                if d2 % u != target:
                    continue

                if not verify_u_witness(n, u, d1, d2):
                    raise AssertionError(
                        f"Internal verifier error for n={n}, u={u}, d1={d1}, d2={d2}"
                    )

                is_parametric = (nx % d1 == 0) or (nx % d2 == 0)
                return {
                    "u": u,
                    "x": x,
                    "d1": d1,
                    "d2": d2,
                    "n_exponent": a,
                    "is_parametric": is_parametric,
                    "x2_divisor_count": divisor_count,
                }

    return None


def verify_range(start, end, u_max=300, batch_log=10000):
    """Verify all prime hard cases in [start, end] with exact witnesses."""
    t0 = time.time()
    results = {
        "range": [start, end],
        "u_max": u_max,
        "criterion": "direct divisor pair: d1*d2=n^2*x^2 and d1=d2=-n*x (mod u)",
        "total_primes": 0,
        "total_hard_cases": 0,
        "solved": 0,
        "failures": [],
        "max_A": 0,
        "max_A_n": 0,
        "A_distribution": {},
        "non_parametric_count": 0,
        "non_parametric_cases": [],
    }

    count = 0
    last_log = time.time()

    for n in sympy.sieve.primerange(start, end + 1):
        results["total_primes"] += 1
        count += 1

        if not is_hard_case_fast(n, n % 12, n % 5):
            continue

        results["total_hard_cases"] += 1
        witness = u_method_solve(n, u_max=u_max)

        if witness is not None:
            u = witness["u"]
            results["solved"] += 1
            results["A_distribution"][u] = results["A_distribution"].get(u, 0) + 1

            if u > results["max_A"]:
                results["max_A"] = u
                results["max_A_n"] = n

            if not witness["is_parametric"]:
                results["non_parametric_count"] += 1
                if len(results["non_parametric_cases"]) < 100:
                    results["non_parametric_cases"].append({
                        "n": n,
                        "u": u,
                        "n_exponent": witness["n_exponent"],
                        "d1": witness["d1"],
                        "d2": witness["d2"],
                    })
        else:
            results["failures"].append(n)
            if len(results["failures"]) <= 50:
                print(f"  FAILURE: n={n:,}", flush=True)

        now = time.time()
        if now - last_log > 30:
            elapsed = now - t0
            rate = results["total_hard_cases"] / elapsed if elapsed > 0 else 0
            print(
                f"  Progress: {count:,} primes, {results['total_hard_cases']:,} hard cases, "
                f"{results['solved']:,} solved, {len(results['failures'])} failures, "
                f"max_A={results['max_A']}, rate={rate:.0f}/s, elapsed={elapsed:.0f}s",
                flush=True,
            )
            last_log = now

    results["runtime_seconds"] = time.time() - t0
    return results


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    else:
        start = 100_000_001
        end = 200_000_000

    u_max = int(sys.argv[3]) if len(sys.argv) >= 4 else 300

    print(f"Verifying prime hard cases from {start:,} to {end:,} with u_max={u_max}")
    print("Criterion: exact complementary divisor pair")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    results = verify_range(start, end, u_max=u_max)

    print(f"\n{'=' * 60}")
    print(f"RESULTS: {start:,} to {end:,}")
    print(f"{'=' * 60}")
    print(f"Total primes: {results['total_primes']:,}")
    print(f"Total hard cases: {results['total_hard_cases']:,}")
    print(f"Solved: {results['solved']:,}")
    print(f"Failures: {len(results['failures'])}")
    if results["failures"]:
        print(f"Failed cases: {results['failures'][:20]}")
    print(f"Max A: {results['max_A']} (at n={results['max_A_n']:,})")
    print(f"Non-parametric: {results['non_parametric_count']:,}")
    print(f"Runtime: {results['runtime_seconds']:.1f}s")

    print("\nA distribution:")
    for u in sorted(results["A_distribution"]):
        cnt = results["A_distribution"][u]
        pct = 100 * cnt / results["solved"] if results["solved"] else 0
        print(f"  A={u:3d}: {cnt:6d} ({pct:5.1f}%)")

    fname = f"verification_{start}_{end}.json"
    with open(fname, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {fname}")
