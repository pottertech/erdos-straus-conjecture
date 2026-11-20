#!/usr/bin/env python3
"""Reconciliation: the forced-structure subclass vs the documented layer counts.

Hypothesis under test: the stage-entrant counts documented in
MOD31_EXACT_REDUCTION.md (283) and MOD35_CRT_SPAN.md (93 = 26 + 67), and the
corrected-cascade narrowing (48,711 primes below 10^7), are measured inside the
FORCED-STRUCTURE subclass

    F = {n prime, n = 1 (mod 24), every prime factor of odd(n+1) and of (n+4)
         is = 1 (mod 4)},

not the full residual class. This script builds the smallest-prime-factor sieve
up to 10,000,004, applies the subclass test to every admissible prime, and
recomputes the first-A aggregates inside F.

Stdlib only.
"""
import json
from collections import Counter

PATH = "results/layer4_certificates.jsonl"
LIMIT = 10_000_004  # covers n+4 for n <= 10,000,000


def build_spf(limit):
    spf = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if spf[i] == i:  # prime
            for m in range(i * i, limit + 1, i):
                if spf[m] == m:
                    spf[m] = i
        i += 1
    return spf


def only_1_mod_4(spf, m):
    """True iff every prime factor of m (or of the odd part when half_flag
    says skip 2s) is = 1 (mod 4)."""
    while m > 1:
        p = spf[m]
        if p % 4 != 1:
            return False
        while m % p == 0:
            m //= p
    return True


def odd_part(m):
    while m % 2 == 0:
        m //= 2
    return m


def main():
    print("building SPF sieve to", LIMIT, "...")
    spf = build_spf(LIMIT)
    print("sieve done")
    total = forced = 0
    a_forced = Counter()
    slice_forced = {}
    max_forced = 0
    max_records = []
    with open(PATH) as f:
        for line in f:
            r = json.loads(line)
            n, a = r["n"], r["A"]
            if n % 24 != 1:
                continue  # admissible primes = 1 (mod 12): split by mod 24
            total += 1
            if not only_1_mod_4(spf, odd_part(n + 1)) or not only_1_mod_4(spf, n + 4):
                continue
            forced += 1
            a_forced[a] += 1
            if a > max_forced:
                max_forced = a
                max_records = [n]
            elif a == max_forced:
                max_records.append(n)
            s = n % 96
            d = slice_forced.setdefault(s, Counter())
            d[a] += 1

    print(f"residual class (n prime = 1 mod 24): {total}")
    print(f"forced subclass F: {forced}")
    print(f"max A in F: {max_forced} at n = {max_records}")
    print("\nfirst-A distribution inside F:")
    for a in sorted(a_forced):
        print(f"  A={a:3d}: {a_forced[a]}")
    ge = lambda cut: sum(v for k, v in a_forced.items() if k >= cut)
    print("\nlayer aggregates inside F (docs: u31 entrants 283; u35: 93 = 26 + 67):")
    print(f"  count(A>=23): {ge(23)}")
    print(f"  count(A>=31): {ge(31)}")
    print(f"  count(A=31):  {a_forced.get(31, 0)}")
    print(f"  count(A>=35): {ge(35)}")
    print(f"  count(A=35):  {a_forced.get(35, 0)}")
    print(f"  count(A>=39): {ge(39)}")
    print("\nper-slice (n mod 96) inside F:")
    for s in sorted(slice_forced):
        d = slice_forced[s]
        print(f"  n%96={s:2d}: count={sum(d.values()):6d} maxA={max(d):3d} As={sorted(d)}")


if __name__ == "__main__":
    main()
