#!/usr/bin/env python3
"""Finite centered-residue obstruction analyzer for prime u-layers.

For a prime u ≡ 3 (mod 4), choose a primitive root g.  The centered target -1
has discrete log (u-1)/2.  Given prime factors that are known to divide
M = n(n+u)/4, this script computes the exact centered shifts supplied by those
forced factors and classifies which residue classes of one additional prime
factor can or cannot reach the target.

This is a finite group calculation only.  It does not assume random divisor
behavior and does not claim that a prime factor in a useful class must exist.
"""

from itertools import product
from math import gcd


def factorint(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_prime(n):
    if n < 2:
        return False
    return len(factorint(n)) == 1 and next(iter(factorint(n).values())) == 1


def primitive_root(p):
    if not is_prime(p):
        raise ValueError("u must be prime")
    phi = p - 1
    qs = list(factorint(phi))
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in qs):
            return g
    raise RuntimeError("primitive root not found")


def dlog_table(p, g):
    table = {}
    v = 1
    for k in range(p - 1):
        table[v] = k
        v = (v * g) % p
    return table


def forced_shift_set(u, forced):
    """Return centered dlog shifts from forced=[(prime, exponent), ...]."""
    g = primitive_root(u)
    logs = dlog_table(u, g)
    mod = u - 1
    ranges = []
    weights = []
    for p, e in forced:
        if gcd(p, u) != 1:
            raise ValueError(f"forced factor {p} is not a unit mod {u}")
        weights.append(logs[p % u])
        ranges.append(range(-e, e + 1))
    shifts = {
        sum(c * w for c, w in zip(cs, weights)) % mod
        for cs in product(*ranges)
    }
    return g, logs, shifts


def classify_single_extra(u, forced):
    if not is_prime(u) or u % 4 != 3:
        raise ValueError("u must be a prime congruent to 3 mod 4")
    g, logs, shifts = forced_shift_set(u, forced)
    mod = u - 1
    target = mod // 2

    qr = []
    qnr = []
    closing = []
    blind = []

    for r in range(1, u):
        s = logs[r]
        is_qr = (s % 2 == 0)
        (qr if is_qr else qnr).append(r)
        # One extra prime can be used with centered exponent -1, 0, or +1.
        works = any((target - c * s) % mod in shifts for c in (-1, 0, 1))
        (closing if works else blind).append(r)

    return {
        "u": u,
        "primitive_root": g,
        "target_log": target,
        "forced": forced,
        "forced_logs": [(p, logs[p % u], e) for p, e in forced],
        "forced_shift_logs": sorted(shifts),
        "qr_residues": qr,
        "qnr_residues": qnr,
        "single_extra_closes": closing,
        "single_extra_blind": blind,
        "qnr_single_extra_blind": [r for r in blind if r in qnr],
    }


def show(result):
    print(f"u={result['u']}  primitive root={result['primitive_root']}")
    print(f"target log(-1)={result['target_log']}")
    print(f"forced factors/logs={result['forced_logs']}")
    print(f"forced shift logs={result['forced_shift_logs']}")
    print(f"QNR residues={result['qnr_residues']}")
    print(f"QNR blind to one extra factor={result['qnr_single_extra_blind']}")
    print()


if __name__ == "__main__":
    # Exact layers derived in the corrected analysis.
    # u=7: shift-divisor purity forces 2 | x_7.
    show(classify_single_extra(7, [(2, 1)]))

    # u=11: n ≡ 1 (mod 12) forces 3 | x_11.
    show(classify_single_extra(11, [(3, 1)]))

    # u=23: n ≡ 1 (mod 24) forces 2*3 | x_23.
    show(classify_single_extra(23, [(2, 1), (3, 1)]))
