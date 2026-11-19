#!/usr/bin/env python3
"""Exact u=31 layer analysis for the corrected deterministic cascade.

Replicates the corrected cascade (shift-divisor reduction, then exact
u=7, 11, 15, 23 layers, extended 31..63) over prime hard cases up to
10^7 using the exact criteria, verifies the documented survivor counts,
and fingerprints every u=31 failure.

Output: analysis/u31_layer.json
"""
import json
import sys
import time
from math import gcd

from sympy import factorint, primerange, legendre_symbol

sys.path.insert(0, '.')
import importlib.util

spec = importlib.util.spec_from_file_location('fav3', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['fav3'] = fav
spec.loader.exec_module(fav)

N_MAX = 10_000_000
U_LAYER = [7, 11, 15, 23, 31, 35, 39, 43, 47, 51, 55, 59, 63]

# primes up to 10^4 for fast trial division
SMALL_PRIMES = list(primerange(2, 10_000))


def fast_factor(m, bound=10_000):
    """Factor m (<= ~1.1e7) via trial division: cofactor is 1 or prime."""
    f = {}
    for p in SMALL_PRIMES:
        if p * p > m:
            break
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors(m):
    ds = {1}
    for p, e in factorint(m).items():
        ds = {d * p**k for d in ds for k in range(e + 1)}
    return sorted(ds)


def direct_works(n, u):
    if (n + u) % 4:
        return None
    x = (n + u) // 4
    nx = n * x
    if nx % u == 0:
        return True
    D = nx * nx
    target = (-nx) % u
    for d1 in divisors(D):
        if d1 * d1 <= D and d1 % u == target:
            return True
    return False


def u_works(n, u):
    if (n + u) % 4:
        return None
    x = (n + u) // 4
    nx = n * x
    if gcd(nx, u) == 1:
        r = fav.centered_check(n, u)
        return bool(r.success) if r is not None else None
    return direct_works(n, u)


def is_hard_prime(n):
    if n % 12 != 1 or n % 5 == 0:
        return False
    b3 = (n + 3) // 4  # = 3k+1; may be even — 2 is not an odd prime factor
    for p in fast_factor(b3):
        if p != 2 and p % 3 != 1:
            return False
    return True


def shift_divisor_ok(n):
    # n+1: every ODD prime factor must be 1 mod 4 (2 is exempt)
    for p in fast_factor(n + 1):
        if p != 2 and p % 4 != 1:
            return False
    # n+4 is odd for n ≡ 1 mod 24: every prime factor must be 1 mod 4
    for p in fast_factor(n + 4):
        if p % 4 != 1:
            return False
    return True


def main():
    out = {'n_max': N_MAX,
           'started': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    hard = after_shift = 0
    first_success = {}   # n -> first working u
    t0 = time.time()
    for n in primerange(2, N_MAX):
        if not is_hard_prime(n):
            continue
        hard += 1
        if not shift_divisor_ok(n):
            continue
        after_shift += 1
        if after_shift % 500 == 0:
            print(f'prog n={n} hard={hard} shift={after_shift} '
                  f't={time.time()-t0:.0f}s', flush=True)
        for u in U_LAYER:
            w = u_works(n, u)
            if w is True:
                first_success[n] = u
                break
            if w is None:
                raise RuntimeError(f'unexpected None at n={n} u={u}')
        if n not in first_success:
            first_success[n] = None
    seq = {}
    prev = after_shift
    for u in U_LAYER:
        cnt = sum(1 for v in first_success.values() if v == u)
        prev -= cnt
        seq[str(u)] = {'succeed': cnt, 'survivors': prev}
    out.update({'hard_primes': hard, 'after_shift_divisor': after_shift,
                'sequential': seq})
    # u=31 stage: enter = survived first 4 layers (first_u is None or >= 31)
    entrants = [n for n, v in first_success.items()
                if v is None or v >= 31]
    # order by entry stage (<= 23-stage survivors)
    failures31, successes31 = [], []
    for n in entrants:
        w = u_works(n, 31)
        (successes31 if w else failures31).append(n)
    out['u31'] = {'entrants': entrants, 'successes': successes31,
                  'failures': failures31}
    # fingerprints at u=31 for the failures
    fps = []
    for n in failures31:
        x = (n + 31) // 4
        M = n * x
        f = factorint(M)
        qr = all(legendre_symbol(p, 31) == 1 for p in f)
        fps.append({'n': n,
                    'v2_x': (x & -x).bit_length() - 1 if x % 2 == 0 else 0,
                    'x': x,
                    'qr_pure_mod31': qr,
                    'M_fact': {str(p): e for p, e in sorted(f.items())}})
    out['u31_failure_fingerprints'] = fps
    # continue the extended sweep for the u=31 failures
    tail = {}
    alive = list(failures31)
    for u in U_LAYER[5:]:
        nxt = []
        for n in alive:
            if u_works(n, u) is not True:
                nxt.append(n)
        tail[str(u)] = len(nxt)
        alive = nxt
    out['extended_after_u31'] = tail
    out['residual_final'] = alive
    json.dump(out, open('analysis/u31_layer.json', 'w'), indent=1)
    print('DONE in', round(time.time() - t0, 1), 's', file=sys.stderr)


if __name__ == '__main__':
    main()
