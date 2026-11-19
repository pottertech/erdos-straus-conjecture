"""Analyze the genuinely square-only Type-II directions at A = u*v.

For squarefree semiprime A=u*v, the only square-completion divisors outside
the two Lopez boundary orthants are D=u^2 and D=v^2.  Along an ancestry edge
m_B=4*B-1 | m_A=4*A-1, these two directions are inherited together.

The exact test is

    u^2 mod m_B in Q_B,
    Q_B = {E mod m_B : E | B^2}.

If this holds, v^2 is inherited automatically because A == B (mod m_B)
and v^2 == B^2/u^2 (mod m_B).
"""

import argparse
import json


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


def divisors_from_factor(f):
    ds = [1]
    for p, e in f.items():
        base = list(ds)
        ds = []
        pe = 1
        for _ in range(e + 1):
            ds.extend(d * pe for d in base)
            pe *= p
    return sorted(ds)


def divisors_of_square(n):
    return divisors_from_factor({p: 2 * e for p, e in factor_small(n).items()})


def squarefree_semiprime_factors(n):
    f = factor_small(n)
    if len(f) != 2 or any(e != 1 for e in f.values()):
        return None
    return tuple(sorted(f))


def ancestors(A):
    """Return B<A such that 4B-1 divides 4A-1."""
    m = 4 * A - 1
    out = []
    for d in divisors_from_factor(factor_small(m)):
        if 1 < d < m and d % 4 == 3:
            out.append((d + 1) // 4)
    return sorted(out)


def qset(B):
    m = 4 * B - 1
    return {D % m for D in divisors_of_square(B)}


def analyze_one(A):
    uv = squarefree_semiprime_factors(A)
    if uv is None:
        return None
    u, v = uv
    mA = 4 * A - 1
    inherited = []

    for B in ancestors(A):
        mB = 4 * B - 1
        Q = qset(B)
        hit_u = (u * u) % mB in Q
        hit_v = (v * v) % mB in Q
        if hit_u != hit_v:
            raise AssertionError((A, B, u, v, hit_u, hit_v))
        if hit_u:
            inherited.append(B)

    return {
        'A': A,
        'u': u,
        'v': v,
        'modulus': mA,
        'mixed_residues': sorted({(-4*u*u) % mA, (-4*v*v) % mA}),
        'inheriting_ancestors': inherited,
        'minimum_inheriting_ancestor': inherited[0] if inherited else None,
        'primitive_mixed_pair': not inherited,
    }


def run(A_max):
    rows = []
    for A in range(2, A_max + 1):
        row = analyze_one(A)
        if row is not None:
            rows.append(row)

    inherited = [r for r in rows if not r['primitive_mixed_pair']]
    primitive = [r for r in rows if r['primitive_mixed_pair']]
    min_counts = {}
    for r in inherited:
        b = str(r['minimum_inheriting_ancestor'])
        min_counts[b] = min_counts.get(b, 0) + 1

    return {
        'summary': {
            'A_max': A_max,
            'squarefree_semiprime_count': len(rows),
            'shadowed_mixed_pair_count': len(inherited),
            'primitive_mixed_pair_count': len(primitive),
            'primitive_fraction': len(primitive) / len(rows) if rows else 0.0,
            'minimum_ancestor_counts': dict(
                sorted(min_counts.items(), key=lambda kv: int(kv[0]))
            ),
        },
        'rows': rows,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--A-max', type=int, default=100000)
    ap.add_argument('--json')
    ap.add_argument('--show-primitive', action='store_true')
    args = ap.parse_args()

    out = run(args.A_max)
    print(json.dumps(out['summary'], indent=2))
    if args.show_primitive:
        for row in out['rows']:
            if row['primitive_mixed_pair']:
                print(row)
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(out, fh, indent=2)
