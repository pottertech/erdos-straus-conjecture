"""Optimize rigorous fixed-ancestor density bounds for squarefree semiprime mixed-square inheritance.

For each depth B, m=4B-1 and Q_B={D mod m:D|B^2}.  Conditional on
A=uv == B (mod m), u^2 is uniform among unit square classes in the fixed-modulus
semiprime limit, so a pairwise-coprime ancestor contributes capture probability
eta(B)/phi(m), where eta is the exact unit-square capture ratio.

The script starts with B={1,2,3,6,12}, whose combined survivor density is
208069/558624, then greedily adds pairwise-coprime moduli ranked by exact capture
probability.  All arithmetic is exact Fraction arithmetic.
"""

from fractions import Fraction
from math import gcd
import argparse


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


def phi(n):
    out = n
    for p in factor(n):
        out = out // p * (p - 1)
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


def capture_ratio(B):
    m = 4 * B - 1
    qr = unit_square_classes(m)
    Q = {d % m for d in divisors(B * B) if gcd(d, m) == 1}
    return Fraction(len(Q & qr), len(qr))


def candidates(Bmax, accumulated_modulus):
    rows = []
    for B in range(1, Bmax + 1):
        m = 4 * B - 1
        if gcd(m, accumulated_modulus) != 1:
            continue
        eta = capture_ratio(B)
        risk = eta / phi(m)
        rows.append((risk, B, m, eta))
    rows.sort(reverse=True)
    return rows


def optimize(Bmax=500, additions=20):
    base = [1, 2, 3, 6, 12]
    modulus = 1
    for B in base:
        modulus *= 4 * B - 1

    survivor = Fraction(208069, 558624)
    chosen = []

    # Recompute rankings after every selection because coprimality changes.
    for _ in range(additions):
        rows = candidates(Bmax, modulus)
        if not rows:
            break
        risk, B, m, eta = rows[0]
        chosen.append((B, m, eta, risk))
        modulus *= m
        survivor *= 1 - risk

    return chosen, survivor


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--B-max", type=int, default=500)
    ap.add_argument("--additions", type=int, default=20)
    args = ap.parse_args()

    chosen, survivor = optimize(args.B_max, args.additions)
    print("base ancestors: 1,2,3,6,12")
    for i, (B, m, eta, risk) in enumerate(chosen, 1):
        print(
            f"{i:2d}. B={B:4d} m={m:5d} "
            f"eta={eta} capture={risk}"
        )
    print("survivor exact:", survivor)
    print("survivor float:", float(survivor))
    print("inherited lower bound:", float(1 - survivor))
