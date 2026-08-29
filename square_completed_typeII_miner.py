"""Factorization-free finite search for square-completed prime Type II.

For prime n == 1 (mod 4), standard Type II is equivalent to

    D | A^2,
    n % (4*A - 1) == (-4*D) % (4*A - 1),
    n does not divide D.

This is the square-divisor completion of Lopez Type A.  The script scans
A in increasing order, enumerates divisors only of the small integer A^2,
and never factors n or a shifted value involving n.

Given a certificate (A,D), it recovers the canonical Dahan coordinates

    alpha = gcd(D, A^2/D),
    u^2    = D/alpha,
    a^2    = (A^2/D)/alpha,

checks the corresponding Theorem-3.9 divisibility, reconstructs the
fixed-shift Type-II decomposition, and verifies the original ESC identity
by exact integer cross multiplication.
"""

from collections import Counter
from math import gcd, isqrt
import argparse, json, time

CORE = (1, 121, 169, 289, 361, 529)


def isprime32(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for base in (2, 3, 5, 7):
        if base >= n:
            continue
        x = pow(base, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factor_small(n):
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors_of_square(n):
    ds = [1]
    for p, e in factor_small(n).items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(2 * e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return ds


def build_layers(A_max):
    layers = []
    for A in range(1, A_max + 1):
        modulus = 4 * A - 1
        residues = {}
        for D in divisors_of_square(A):
            residues.setdefault((-4 * D) % modulus, []).append(D)
        layers.append((A, modulus, residues))
    return layers


def find_witness(n, layers):
    for A, modulus, residues in layers:
        for D in residues.get(n % modulus, ()):  # D | A^2 by construction
            if D % n == 0:
                continue
            return {'n': n, 'A': A, 'D': D, 'modulus': modulus}
    return None


def recover_and_verify(w):
    n, A, D = w['n'], w['A'], w['D']
    modulus = 4 * A - 1
    if A * A % D:
        return None
    if (n + 4 * D) % modulus:
        return None
    if D % n == 0:
        return None

    E = A * A // D
    alpha = gcd(D, E)
    u2 = D // alpha
    a2 = E // alpha
    u = isqrt(u2)
    a = isqrt(a2)
    if u * u != u2 or a * a != a2 or gcd(u, a) != 1:
        return None
    if A != alpha * u * a:
        return None

    s = modulus
    if (a * n + u) % s:
        return None
    v = (a * n + u) // s
    if (u + v) % a:
        return None
    shift = (u + v) // a
    if shift <= 0 or shift % 4 != 3:
        return None

    K_num = n + shift
    if K_num % 4:
        return None
    K = K_num // 4
    if K != alpha * u * v:
        return None

    # Standard Type-II binary decomposition from divisors u,v of K.
    scale = a * n * alpha
    x = K
    y = scale * u
    z = scale * v
    if min(x, y, z) <= 0:
        return None
    if 4 * x * y * z != n * (x * y + x * z + y * z):
        return None

    out = dict(w)
    out.update({
        'alpha': alpha,
        'u': u,
        'a': a,
        's': s,
        'v': v,
        'shift': shift,
        'K': K,
        'x': x,
        'y': y,
        'z': z,
    })
    return out


def run(lo, hi, A_max=624, save_records=False):
    layers = build_layers(A_max)
    total = 0
    failures = []
    bad = []
    records = []
    distribution = Counter()
    frontier = []
    record_A = 0

    for block in range(lo // 840, hi // 840 + 1):
        base = 840 * block
        for residue in CORE:
            n = base + residue
            if n < lo or n > hi or n < 2 or not isprime32(n):
                continue
            total += 1
            w = find_witness(n, layers)
            if w is None:
                failures.append(n)
                continue
            full = recover_and_verify(w)
            if full is None:
                bad.append(w)
                continue
            distribution[full['A']] += 1
            if full['A'] > record_A:
                record_A = full['A']
                frontier.append({
                    'n': n,
                    'A': full['A'],
                    'D': full['D'],
                    'u': full['u'],
                    'a': full['a'],
                    'alpha': full['alpha'],
                    's': full['s'],
                    'shift': full['shift'],
                })
            if save_records:
                records.append(full)

    return {
        'range': [lo, hi],
        'A_max': A_max,
        'six_class_primes': total,
        'certificate_count': total - len(failures) - len(bad),
        'failure_count': len(failures),
        'failures': failures,
        'bad_certificate_count': len(bad),
        'bad_certificates': bad,
        'depth_distribution': dict(sorted(distribution.items())),
        'record_frontier': frontier,
        'records': records,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lo', type=int, default=2)
    ap.add_argument('--hi', type=int, required=True)
    ap.add_argument('--A-max', type=int, default=624)
    ap.add_argument('--json')
    ap.add_argument('--records', action='store_true')
    args = ap.parse_args()

    start = time.time()
    out = run(args.lo, args.hi, args.A_max, args.records)
    out['seconds'] = time.time() - start
    print({k: v for k, v in out.items() if k not in ('records', 'bad_certificates', 'depth_distribution')})
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(out, fh, indent=2)
