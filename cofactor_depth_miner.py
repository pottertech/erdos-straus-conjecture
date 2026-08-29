"""Minimum complementary-cofactor depth for the shift-divisor / Type-A family.

For a residual prime n, the untwisted unit-partner / Type-A family is
exactly

    q | n + 4*a,
    q == -1 (mod 4*a).

This script searches increasing a and returns the first such divisor q.
The complementary factor

    c = (n + 4*a) / q

is the corresponding Erdős--Straus shift.  The fixed-shift Type-A divisor
inside K=(n+c)/4 is

    d = (n+c)/(4*a),

and r=(q+1)/(4*a) satisfies d+1=c*r.

The script uses the range-safe factorization helpers from short_relation_miner.
"""

from collections import Counter
import argparse, json, time

from short_relation_miner import (
    CORE,
    isprime32,
    factor,
    hard_gate,
    shift_reduced,
    assert_factor_range,
)


def divisors_from_factorization(fm):
    ds = [1]
    for p, e in fm.items():
        base = list(ds)
        pe = 1
        new = list(base)
        for _ in range(e):
            pe *= p
            new.extend(d * pe for d in base)
        ds = new
    return ds


def cofactor_layer_witness(n, a):
    """Return an exact Type-A/shift-divisor witness at fixed cofactor a."""
    m = 4 * a
    value = n + m
    assert_factor_range(value)
    for q in divisors_from_factorization(factor(value)):
        if q % m != m - 1:
            continue
        c = value // q
        if c <= 0 or c % 4 != 3:
            continue
        if (n + c) % m:
            continue
        d = (n + c) // m
        r = (q + 1) // m
        if d <= 0 or r <= 0:
            continue
        if d + 1 != c * r:
            continue
        K = (n + c) // 4
        if K != a * d:
            continue
        return {
            'n': n,
            'a': a,
            'q': q,
            'shift': c,
            'K': K,
            'd': d,
            'r': r,
        }
    return None


def minimum_cofactor_witness(n, a_max):
    for a in range(1, a_max + 1):
        w = cofactor_layer_witness(n, a)
        if w is not None:
            return w
    return None


def verify_witness(w):
    n, a, q, c, K, d, r = (
        w['n'], w['a'], w['q'], w['shift'], w['K'], w['d'], w['r']
    )
    if q * c != n + 4 * a:
        return False
    if q % (4 * a) != 4 * a - 1:
        return False
    if 4 * K != n + c:
        return False
    if K != a * d:
        return False
    if d + 1 != c * r:
        return False

    # Explicit Type-A / unit-partner decomposition.
    M = n * K
    s = d
    k = M // s
    rr = (s + 1) // c
    if s * k != M or s + 1 != c * rr:
        return False
    y = M * rr
    z = k * rr
    return 4 * K * y * z == n * (K * y + K * z + y * z)


def run(lo, hi, a_max=143, save_records=False):
    assert_factor_range(hi + 4 * a_max)

    core = hard = tail = 0
    failures = []
    records = []
    distribution = Counter()
    bad = []

    for block in range(lo // 840, hi // 840 + 1):
        base = 840 * block
        for residue in CORE:
            n = base + residue
            if n < lo or n > hi or n < 2 or not isprime32(n):
                continue
            core += 1
            if not hard_gate(n):
                continue
            hard += 1
            if not shift_reduced(n):
                continue
            tail += 1

            w = minimum_cofactor_witness(n, a_max)
            if w is None:
                failures.append(n)
                continue
            distribution[w['a']] += 1
            if not verify_witness(w):
                bad.append(w)
            if save_records:
                records.append(w)

    return {
        'range': [lo, hi],
        'a_max': a_max,
        'core_primes': core,
        'after_hard': hard,
        'after_shift': tail,
        'certificate_count': tail - len(failures),
        'failure_count': len(failures),
        'failures': failures,
        'depth_distribution': dict(sorted(distribution.items())),
        'bad_certificate_count': len(bad),
        'bad_certificates': bad,
        'records': records,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lo', type=int, default=2)
    ap.add_argument('--hi', type=int, required=True)
    ap.add_argument('--a-max', type=int, default=143)
    ap.add_argument('--json')
    ap.add_argument('--records', action='store_true')
    args = ap.parse_args()

    start = time.time()
    out = run(args.lo, args.hi, args.a_max, args.records)
    out['seconds'] = time.time() - start
    print({k: v for k, v in out.items() if k not in ('records', 'bad_certificates')})
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(out, fh, indent=2)
