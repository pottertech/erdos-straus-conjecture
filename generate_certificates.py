#!/usr/bin/env python3
"""
Layer 4 Certificate Generation  (fixed 2026-11-19, issue #7)
=============================================================
For every admissible prime n <= 10M (n ≡ 1 mod 12, 5 ∤ n), generate an
auditable certificate:

- first working A (searched over the exact centered criterion for each A)
- witness divisor P of N² with P ≡ T (mod A), T = (-N) mod A, N = n·x
- complementary divisor Q = N² / P (also ≡ T mod A)
- x = (n + A) / 4, y = (P + N) / A, z = (Q + N) / A
- verified: 4·x·y·z = n·(x·y + x·z + y·z)

Output: results/layer4_certificates.jsonl (streaming, one JSON per line)

Fixes relative to the 2026-08 version (issue #7):
1. y, z are constructed from the witness divisor (closed form), instead of
   a brute-force y-scan capped at 10^6 — which failed for every case whose
   smallest witness y exceeded the cap (e.g. n = 15649, first working A = 7).
2. The witness divisor is found by an exact DP over the residues mod A of
   the prime powers of N (complete; no mod-reduced pseudo-divisors, no
   incomplete sampling past 100k divisors).
3. Records carry the Q field required by analysis/layer4/verify_certificates.py.
4. Main loop covers the full documented range 13 ≤ n ≤ 10,000,000 (the old
   main was left in a 100k debug bound).
"""
import json
import os
import time
from math import gcd

from sympy import isprime, factorint, nextprime

EXTENDED_A = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59,
              63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107]
MAX_N = 10_000_000


def find_divisor_witness(factors_N, A, T):
    """Exact DP: find a divisor P of N² with P ≡ T (mod A).

    factors_N must contain only primes coprime to A (guaranteed by the
    caller's gcd(N, A) = 1 check). States are residues mod A (<= A states),
    each carrying a back-pointer for reconstruction; multipliers are prime
    powers p^a, 1 <= a <= 2e, so the product P divides N².
    """
    T %= A
    states = {1 % A: (None, 1)}   # residue -> (prev_residue, actual multiplier)
    for p, e in factors_N.items():
        vals = []                 # actual prime powers p^a, a = 1..2e
        val = 1
        for _ in range(2 * e):
            val *= p
            vals.append(val)
        new_states = dict(states)
        for r, back in states.items():
            for v in vals:
                nr = (r * v) % A
                if nr not in new_states:
                    new_states[nr] = (r, v)
        states = new_states
    if T not in states:
        return None
    mults = []
    r = T
    while states[r][0] is not None:
        prev, v = states[r]
        mults.append(v)
        r = prev
    P = 1
    for m in mults:
        P *= m
    return P


def find_witness(n, A):
    """Exact centered-criterion certificate for (n, A), or None.

    Succeeds iff gcd(N, A) = 1 and T = (-N) mod A belongs to the centered
    product set of N (built over the prime powers 1..2e of N), in which case
    P, Q, y, z are constructed explicitly and exactly verified.
    """
    if (n + A) % 4:
        return None
    x = m = (n + A) // 4
    N = n * m
    if gcd(N, A) != 1:
        return None
    T = (-N) % A

    factors_N = factorint(N)
    P = find_divisor_witness(factors_N, A, T)
    if P is None:
        return None

    Q = (N * N) // P
    y = (P + N) // A
    z = (Q + N) // A
    # exact verification (defense in depth — mirrors verify_certificates.py)
    if P * Q != N * N:
        return None
    if P % A != T:
        return None
    if Q % A != T:
        return None
    if (P + N) % A != 0 or (Q + N) % A != 0:
        return None
    if 4 * x * y * z != n * (x * y + x * z + y * z):
        return None
    if x <= 0 or y <= 0 or z <= 0:
        return None
    return {'A': A, 'P': P, 'Q': Q, 'x': x, 'y': y, 'z': z, 'T': T, 'N': N}


def A3_parametric_fast(n):
    """Theorem 2 fast path: for n ≡ 5 (mod 8), A = 3 always works, with
    witness divisor P = 2 (x = (n+3)/4 is even), no factorization needed."""
    if n % 8 != 5:
        return None
    x = (n + 3) // 4
    if x % 2 != 0:
        return None
    N = n * x
    P = 2
    Q = (N * N) // P
    y = (P + N) // 3
    z = (Q + N) // 3
    if P * Q != N * N or P % 3 != 2 or Q % 3 != 2:
        return None
    if (P + N) % 3 != 0 or (Q + N) % 3 != 0:
        return None
    if 4 * x * y * z != n * (x * y + x * z + y * z):
        return None
    return {'A': 3, 'P': P, 'Q': Q, 'x': x, 'y': y, 'z': z, 'T': 2, 'N': N}


def main():
    start_time = time.time()

    print("=" * 70)
    print("LAYER 4 CERTIFICATE GENERATION (fixed, issue #7)")
    print("=" * 70)

    output_path = 'results/layer4_certificates.jsonl'
    os.makedirs('results', exist_ok=True)

    count = 0
    certified = 0
    failed = 0
    last_progress = time.time()

    with open(output_path, 'w') as out:
        n = 13
        while n <= MAX_N:
            if not isprime(n) or n % 12 != 1 or n % 5 == 0:
                n = int(nextprime(n))
                continue

            count += 1

            # find first working A
            cert = None
            fast = A3_parametric_fast(n)
            if fast is not None:
                cert = fast
                cert['n'] = n
                cert['verified'] = True
            else:
                for A in EXTENDED_A:
                    if gcd(n, A) > 1:
                        continue
                    result = find_witness(n, A)
                    if result is None:
                        continue
                    x, y, z = result['x'], result['y'], result['z']
                    P, Q, T, N = result['P'], result['Q'], result['T'], result['N']

                    # independent verification (mirrors verify_certificates.py)
                    if N * N % P != 0:
                        continue
                    if Q != N * N // P:
                        continue
                    if P % A != T % A:
                        continue
                    if Q % A != T % A:
                        continue
                    if (P + N) % A != 0 or (Q + N) % A != 0:
                        continue
                    if 4 * x * y * z != n * (x * y + x * z + y * z):
                        continue
                    if x <= 0 or y <= 0 or z <= 0:
                        continue

                    cert = result
                    cert['n'] = n
                    cert['verified'] = True
                    break

            if cert:
                out.write(json.dumps(cert) + '\n')
                certified += 1
            else:
                failed += 1
                if failed <= 10:
                    print(f"  FAILED: n={n}")

            n = int(nextprime(n))

            now = time.time()
            if now - last_progress > 30:
                elapsed = now - start_time
                print(f"  Progress: {count} primes, n={n}, elapsed={elapsed:.0f}s, "
                      f"certified={certified}, failed={failed}", flush=True)
                last_progress = now

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print(f"COMPLETE: {count} primes in {elapsed:.0f}s")
    print(f"  Certified: {certified}")
    print(f"  Failed: {failed}")
    print(f"  Output: {output_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
