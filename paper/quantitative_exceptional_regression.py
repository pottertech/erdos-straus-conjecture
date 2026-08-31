#!/usr/bin/env python3
"""Finite sanity check for QUANTITATIVE_EXCEPTIONAL_SET.md.

This script does NOT prove the asymptotic theorem. It enumerates prime parameters q,
counts those for which A=(3q+1)/4 has no prime factor 2 mod 3, and reports

    E(Y) * (log Y)^(3/2) / Y.

The theorem predicts this normalized quantity is bounded. A stable finite value is a
useful regression check for local-density/congruence transcription errors.
"""

from math import isqrt, log


def primes_upto(n: int):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def has_factor_2_mod_3(n: int, primes) -> bool:
    t = n
    for p in primes:
        if p * p > t:
            break
        if t % p == 0:
            if p % 3 == 2:
                return True
            while t % p == 0:
                t //= p
        if t == 1:
            return False
    return t > 1 and t % 3 == 2


def count(Y: int, primes):
    base = 0
    exceptional = 0
    for q in primes:
        if q > Y:
            break
        if q % 4 != 1:
            continue
        base += 1
        A = (3 * q + 1) // 4
        if not has_factor_2_mod_3(A, primes):
            exceptional += 1
    normalized = exceptional * (log(Y) ** 1.5) / Y
    relative = exceptional / base
    return base, exceptional, relative, normalized


def main():
    bounds = (10_000, 100_000, 1_000_000)
    primes = primes_upto(max(bounds))
    print("Y, prime_q_1mod4, exceptional, relative, E(Y)*(log Y)^(3/2)/Y")
    for Y in bounds:
        b, e, r, s = count(Y, primes)
        print(f"{Y}, {b}, {e}, {r:.12f}, {s:.12f}")


if __name__ == "__main__":
    main()
