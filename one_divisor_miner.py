"""Exact one-divisor centered search on the corrected classical core.

For u == 3 (mod 4), x=(n+u)/4 and M=n*x, search for any divisor
s|M with s == -1 (mod u).  Such an s gives the exact decomposition

    X = x
    Y = M*r
    Z = (M/s)*r
    r = (s+1)/u.

For prime n with gcd(n,x)=1, every s|M is d or n*d with d|x, so the
search has two divisor branches inside x:

    d == -1 (mod u),
    n*d == -1 (mod u).
"""

from math import gcd
import argparse, json, time

from short_relation_miner import CORE, isprime32, factor, hard_gate, shift_reduced


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


def one_divisor_witness(n, u_max=299):
    for u in range(3, u_max + 1, 4):
        if (n + u) % 4:
            continue
        x = (n + u) // 4
        ds = divisors_from_factorization(factor(x))

        # Branch X: s=d with d|x.
        for d in ds:
            if d % u == u - 1:
                s = d
                M = n * x
                k = M // s
                r = (s + 1) // u
                return {
                    'n': n, 'u': u, 'x': x, 'branch': 'x',
                    'd': d, 's': s, 'k': k, 'r': r,
                    'y': M * r, 'z': k * r,
                }

        # Branch NX: s=n*d with d|x.
        for d in ds:
            s = n * d
            if s % u == u - 1:
                M = n * x
                k = M // s
                r = (s + 1) // u
                return {
                    'n': n, 'u': u, 'x': x, 'branch': 'n*x',
                    'd': d, 's': s, 'k': k, 'r': r,
                    'y': M * r, 'z': k * r,
                }
    return None


def verify_witness(w):
    n, x, y, z = w['n'], w['x'], w['y'], w['z']
    M = n * x
    return (
        w['s'] * w['k'] == M
        and w['s'] + 1 == w['u'] * w['r']
        and 4 * x == n + w['u']
        and 4 * x * y * z == n * (x * y + x * z + y * z)
    )


def run(lo, hi, u_max=299, save_records=True):
    core = hard = tail = 0
    failures, records = [], []
    branch_counts = {'x': 0, 'n*x': 0}
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

            w = one_divisor_witness(n, u_max)
            if w is None:
                failures.append(n)
                continue
            if not verify_witness(w):
                bad.append(w)
            branch_counts[w['branch']] += 1
            if save_records:
                records.append(w)

    return {
        'range': [lo, hi],
        'u_max': u_max,
        'core_primes': core,
        'after_hard': hard,
        'after_shift': tail,
        'certificate_count': len(records) if save_records else tail - len(failures),
        'failure_count': len(failures),
        'failures': failures,
        'branch_counts': branch_counts,
        'bad_certificate_count': len(bad),
        'bad_certificates': bad,
        'records': records,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lo', type=int, default=2)
    ap.add_argument('--hi', type=int, required=True)
    ap.add_argument('--u-max', type=int, default=299)
    ap.add_argument('--json')
    ap.add_argument('--no-records', action='store_true')
    args = ap.parse_args()

    start = time.time()
    out = run(args.lo, args.hi, args.u_max, not args.no_records)
    out['seconds'] = time.time() - start
    print({k: v for k, v in out.items() if k not in ('records', 'bad_certificates')})
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(out, fh, indent=2)
