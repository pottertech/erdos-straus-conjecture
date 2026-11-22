#!/usr/bin/env python3
"""
Follow-up to the 2026-11-21 re-attribution (ROUTE2 §6.5): the 7 hard cases that
`verification_10M_1B.json` records with no u-method solution within prime
u <= 251 (exact criterion). Question: do they resolve at larger prime u?

Method: exact one-divisor criterion (CENTERED_PRODUCT_SET_THEOREM.md):
exists d | (n*x)^2 with d == -n*x (mod u), gcd(M, u) = 1, x = (n+u)/4 —
implemented via the centered span set S_u(M) = prod_j {q_j^t : -e_j <= t <= e_j}
(mod u) over the full prime factorization of M = n*x (sympy).

Output: sweep_exact/no_solution_at_large_u.json
"""
import json
from sympy import factorint, isprime

CASES = [71310241, 318545761, 340912609, 360055609, 524792461, 550027501, 923573401]
UMAX = 3001  # prime u == 3 (mod 4), u <= 3001


def is_hard(n):
    if n % 12 != 1 or n % 5 == 0:
        return False
    B3 = n * (n + 3) // 4
    while B3 % 2 == 0:
        B3 //= 2
    if B3 % 3 == 0:
        return False
    return all(p % 3 == 1 for p in factorint(B3))


def span_hit(mf, u):
    """True iff -1 in S_u(mf); None iff u | M (u-method inapplicable)."""
    if u in mf:
        return None
    reachable = {1}
    for p, e in mf.items():
        q = p % u
        qinv = pow(q, u - 2, u)
        window = [pow(q, t, u) for t in range(e + 1)]
        window += [pow(qinv, t, u) for t in range(1, e + 1)]
        reachable = {(a * w) % u for a in reachable for w in window}
        if (u - 1) in reachable:
            return True
    return (u - 1) in reachable


def first_u(n, primes, umax):
    mf_n = dict(factorint(n))
    for u in primes:
        if u > umax:
            break
        if (n + u) % 4:
            continue
        x = (n + u) // 4
        mf = dict(mf_n)
        for p, e in factorint(x).items():
            mf[p] = mf.get(p, 0) + e
        if span_hit(mf, u):
            return u
    return None


def main():
    primes = [u for u in range(3, UMAX + 1, 4) if isprime(u)]
    cases = []
    for n in CASES:
        hard = is_hard(n)
        u = first_u(n, primes, UMAX)
        cases.append({"n": n, "hard": bool(hard), "first_u": u,
                      "resolves_above_251": bool(u is not None and u > 251)})
        print(f"n={n}: hard={hard} first_u(exact, prime u<={UMAX})={u}", flush=True)
    resolved = [c["n"] for c in cases if c["first_u"] is not None]
    print(f"\nresolved (first exact-criterion u found, prime u<={UMAX}): {resolved if resolved else 'NONE'}")
    with open("sweep_exact/no_solution_at_large_u.json", "w") as f:
        json.dump({"u_max": UMAX, "criterion": "exact one-divisor (centered span)",
                   "u_values": "prime, u = 3 (mod 4)", "cases": cases}, f, indent=2)


if __name__ == "__main__":
    main()
