"""Analyze square-class capture by divisor-modulus ancestors in square-completed Type II.

For depth B, m=4B-1 and
    Q_B = {D mod m : D | B^2}.
This script measures how much of the unit quadratic-residue set modulo m is
contained in Q_B.  These are the square classes that a semiprime mixed direction
u^2 can inherit from depth B whenever m | 4uv-1.

Finite output is exploratory; the definitions and membership tests are exact.
"""

from math import gcd
import argparse, json


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        base = list(ds)
        ds = []
        pe = 1
        for _ in range(e + 1):
            ds.extend(d * pe for d in base)
            pe *= p
    return ds


def unit_square_classes(m):
    return {a * a % m for a in range(1, m) if gcd(a, m) == 1}


def ancestor_set(B):
    m = 4 * B - 1
    return {d % m for d in divisors(B * B) if gcd(d, m) == 1}


def analyze(Bmax):
    rows = []
    for B in range(1, Bmax + 1):
        m = 4 * B - 1
        qr = unit_square_classes(m)
        q = ancestor_set(B)
        captured = q & qr
        rows.append({
            'B': B,
            'modulus': m,
            'modulus_factorization': factor(m),
            'qr_count': len(qr),
            'captured_qr_count': len(captured),
            'capture_ratio': len(captured) / len(qr),
            'captured_qr': sorted(captured),
            'missed_qr': sorted(qr - captured),
        })
    return rows


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--B-max', type=int, default=100)
    ap.add_argument('--min-ratio', type=float, default=0.0)
    ap.add_argument('--json')
    args = ap.parse_args()

    rows = [r for r in analyze(args.B_max) if r['capture_ratio'] >= args.min_ratio]
    rows.sort(key=lambda r: (-r['capture_ratio'], r['B']))
    for r in rows:
        print(r)
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(rows, fh, indent=2)
