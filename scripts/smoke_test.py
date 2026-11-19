#!/usr/bin/env python3
"""CI smoke test for the Erdős-Straus repository.

Stdlib only (no third-party packages). Asserts, using the exact u-method
criteria this repository maintains:

1. The direct divisor-pair criterion (d1 | n²x², d1 ≤ √D, d1 ≡ −nx mod u)
   and the centered product-set verifier `finite_abelian_centered_verifier.py`
   agree on every applicable (n, u) pair in a fixed sweep.
2. The documented counterexample regression: n = 1129 (hard case, ≡ 49 mod
   120) FAILS at u = 7 and first succeeds at u = 11 — the concrete fact that
   forced the 2026-08-28 claim audit (CORRECTED_CLAIM_AUDIT.md §2).
3. The first-success distribution over PRIME hard cases n ≤ 1200 for u ≤ 11
   is {3: 6, 7: 10, 11: 1}, matching the corrected_centered_criterion.py sweep
   (17 hard cases, 51 cross-checked pairs, 0 mismatches). The single u=11
   case is exactly n = 1129.

Exit code 0 = pass, 1 = fail (with diagnostics).
"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def factorize(m: int) -> dict:
    """Trial-division factorization (test values are small)."""
    out = {}
    p = 2
    while p * p <= m:
        while m % p == 0:
            out[p] = out.get(p, 0) + 1
            m //= p
        p += 1 if p == 2 else 2
    if m > 1:
        out[m] = out.get(m, 0) + 1
    return out


def divisors(m: int) -> list:
    f = factorize(m)
    ds = {1}
    for p, e in f.items():
        ds = {d * p**k for d in ds for k in range(e + 1)}
    return sorted(ds)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_hard_case(n: int) -> bool:
    """Prime hard-case definition used by corrected_centered_criterion.py:
    n prime, n ≡ 1 mod 12, 5 ∤ n, and every odd prime factor of n(n+3)/4
    is ≡ 1 mod 3."""
    if not is_prime(n):
        return False
    if n % 12 != 1 or n % 5 == 0:
        return False
    b3 = n * (n + 3) // 4
    while b3 % 2 == 0:
        b3 //= 2
    for p in factorize(b3):
        if p % 3 != 1:
            return False
    return True


def u_method_works_divisor_pair(n: int, u: int):
    """Exact direct criterion. Returns True/False, or None when the pair is
    not applicable (x not integral / non-invertible)."""
    if (n + u) % 4:
        return None
    x = (n + u) // 4
    if x < 1:
        return None
    nx = n * x
    if nx % u == 0:
        return None
    D = nx * nx
    target = (-nx) % u
    for d1 in divisors(D):
        if d1 * d1 <= D and d1 % u == target:
            if (d1 + nx) % u == 0 and (D // d1 + nx) % u == 0:
                return True
    return False


def load_module(modname: str, fname: str):
    spec = importlib.util.spec_from_file_location(modname, ROOT / fname)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {fname}: spec unavailable")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod  # required for dataclass processing
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    failures = []

    fav = load_module("fav_smoke", "finite_abelian_centered_verifier.py")

    # 0. verifier self-test
    try:
        fav.self_test()
        print("OK   finite_abelian_centered_verifier.self_test")
    except Exception as e:  # noqa: BLE001
        failures.append(f"self_test raised: {e}")

    # 1. n = 1129 regression (the audit's counterexample)
    gt7 = u_method_works_divisor_pair(1129, 7)
    if gt7 is not False:
        failures.append(f"1129: expected divisor-pair FAIL at u=7, got {gt7}")
    ok = False
    first = None
    for u in (3, 7, 11, 13, 15):
        r = u_method_works_divisor_pair(1129, u)
        if r:
            first = u
            ok = True
            break
    if not ok or first != 11:
        failures.append(f"1129: expected first success at u=11, got {first}")
    else:
        print("OK   n=1129: u=7 fails, first success u=11 (audit counterexample)")

    # 2. sweep + cross-criterion agreement (PRIME hard cases, as in the repo)
    dist = {}
    compared = 0
    mismatch = 0
    u11_cases = []
    for n in range(2, 1201):
        if not is_hard_case(n):
            continue
        for u in (3, 7, 11):
            dp = u_method_works_divisor_pair(n, u)
            cc = fav.centered_check(n, u)
            if cc is None or dp is None:
                continue
            compared += 1
            if bool(dp) != bool(cc.success):
                mismatch += 1
                failures.append(f"criterion mismatch at n={n}, u={u}: dp={dp}, centered={cc.success}")
        for u in (3, 7, 11, 13, 15):
            r = u_method_works_divisor_pair(n, u)
            if r:
                dist[u] = dist.get(u, 0) + 1
                if u == 11:
                    u11_cases.append(n)
                break
        else:
            dist["none"] = dist.get("none", 0) + 1

    expected_dist = {3: 6, 7: 10, 11: 1}
    if compared != 51:
        failures.append(f"expected 51 comparable pairs in sweep, got {compared}")
    if dist != expected_dist:
        failures.append(f"first-u distribution {dist} != documented {expected_dist}")
    if u11_cases != [1129]:
        failures.append(f"u=11 first-success cases {u11_cases} != [1129]")
    if mismatch == 0 and compared == 51 and dist == expected_dist and u11_cases == [1129]:
        print(f"OK   sweep of prime hard cases n≤1200, u≤11: {compared} cross-checked pairs, 0 mismatches")

    print(f"first-u distribution: {dist}")
    if failures:
        print("FAILURES:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SMOKE TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
