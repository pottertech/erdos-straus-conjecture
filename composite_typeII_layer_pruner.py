"""Exact structural redundancy analysis for square-completed Type-II layers.

At square depth A, put m_A = 4*A - 1 and

    T_A = { -4*D mod m_A : D | A^2 }.

A residue r in T_A is *divisor-modulus inherited* from a smaller layer B if
m_B | m_A and r mod m_B lies in T_B.  In that case every integer in the
progression n == r (mod m_A) already satisfies the depth-B Type-II congruence,
so r adds no new global progression.

This is an exact pruning criterion.  It is deliberately conservative:
non-dividing earlier moduli can cover subprogressions of r (mod m_A), but not
uniformly by this simple implication, so they are not called inherited here.
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


def is_prime(n):
    if n < 2:
        return False
    f = factor_small(n)
    return len(f) == 1 and next(iter(f.values())) == 1


def divisors_of_square(A):
    ds = [1]
    for p, e in factor_small(A).items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(2 * e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return sorted(ds)


def trap_residues(A):
    m = 4 * A - 1
    by_residue = {}
    for D in divisors_of_square(A):
        by_residue.setdefault((-4 * D) % m, []).append(D)
    return by_residue


def analyze(A_max):
    layers = {A: trap_residues(A) for A in range(1, A_max + 1)}
    records = []

    for A in range(1, A_max + 1):
        m = 4 * A - 1
        traps = set(layers[A])
        inherited = set()
        parents = []

        for B in range(1, A):
            mb = 4 * B - 1
            if m % mb:
                continue
            hits = sorted(r for r in traps if r % mb in layers[B])
            if hits:
                inherited.update(hits)
                parents.append({
                    'B': B,
                    'modulus': mb,
                    'inherited_count': len(hits),
                })

        primitive = sorted(traps - inherited)
        records.append({
            'A': A,
            'modulus': m,
            'modulus_prime': is_prime(m),
            'trap_count': len(traps),
            'inherited_count': len(inherited),
            'primitive_count': len(primitive),
            'fully_redundant': len(primitive) == 0,
            'primitive_residues': primitive,
            'parents': parents,
        })

    composite = [r for r in records if not r['modulus_prime']]
    summary = {
        'A_max': A_max,
        'layer_count': len(records),
        'prime_modulus_layers': sum(r['modulus_prime'] for r in records),
        'composite_modulus_layers': len(composite),
        'fully_redundant_composite_layers': sum(r['fully_redundant'] for r in composite),
        'primitive_composite_layers': sum(not r['fully_redundant'] for r in composite),
    }
    if composite:
        summary['fully_redundant_composite_fraction'] = (
            summary['fully_redundant_composite_layers'] / len(composite)
        )
        summary['mean_primitive_fraction_composite'] = sum(
            r['primitive_count'] / r['trap_count'] for r in composite
        ) / len(composite)

    return {'summary': summary, 'layers': records}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--A-max', type=int, default=2000)
    ap.add_argument('--json')
    ap.add_argument('--show-primitive', action='store_true')
    args = ap.parse_args()

    out = analyze(args.A_max)
    print(json.dumps(out['summary'], indent=2))

    if args.show_primitive:
        for row in out['layers']:
            if not row['modulus_prime'] and row['primitive_count']:
                print(row)

    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(out, fh, indent=2)
