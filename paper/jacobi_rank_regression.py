#!/usr/bin/env python3
"""Finite regression for the Jacobi first-occurrence/rank theorem.

This is not part of the proof. It incrementally computes the F_2-span of the
squarefree-kernel parity vectors of m_A=4A-1 and checks that a new vector occurs
iff m_A is prime or m_A=3q with q == 1 (mod 4) prime. It also checks the exact
rank against the corresponding prime-count formula.

Default bound: A <= 100000.
"""

from __future__ import annotations

import argparse
from sympy import factorint, isprime, primerange


def scan(limit: int) -> tuple[int, list[tuple[int, int]]]:
    prime_index: dict[int, int] = {}
    basis: dict[int, int] = {}
    rank = 0
    mismatches: list[tuple[int, int]] = []

    for A in range(1, limit + 1):
        m = 4 * A - 1
        bits = 0
        for p, e in factorint(m).items():
            if e & 1:
                if p not in prime_index:
                    prime_index[p] = len(prime_index)
                bits ^= 1 << prime_index[p]

        x = bits
        is_new = False
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                rank += 1
                is_new = True
                break

        predicted = isprime(m) or (
            m % 3 == 0
            and isprime(m // 3)
            and (m // 3) % 4 == 1
        )
        if is_new != predicted:
            mismatches.append((A, m))

    return rank, mismatches


def formula(limit: int) -> int:
    prime_targets = sum(1 for p in primerange(2, 4 * limit) if p % 4 == 3)
    qmax = (4 * limit - 1) // 3
    composite_targets = sum(1 for q in primerange(2, qmax + 1) if q % 4 == 1)
    return prime_targets + composite_targets


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    args = parser.parse_args()

    rank, mismatches = scan(args.limit)
    expected = formula(args.limit)

    print(f"limit={args.limit}")
    print(f"incremental_rank={rank}")
    print(f"prime_count_formula={expected}")
    print(f"classification_mismatches={len(mismatches)}")

    if mismatches:
        print("first mismatches:", mismatches[:10])
        raise SystemExit(1)
    if rank != expected:
        raise SystemExit("rank does not match exact prime-count formula")

    print("PASS")


if __name__ == "__main__":
    main()
