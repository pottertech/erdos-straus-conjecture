"""Exact ancestry pruning on the *realized* square-completed Type-II divisor lattice.

For depth A, let m = 4*A - 1 and

    R_A = { D mod m : D | A^2 }.

A realized class r in R_A is divisor-modulus inherited if there exists a
proper divisor modulus e | m, e == 3 (mod 4), with B=(e+1)/4 and

    r mod e in { E mod e : E | B^2 }.

This script enumerates the realized primitive remainder

    P_A^real = R_A \ inherited classes.

Unlike ambient quadratic-residue survivor searches, every class considered
here is represented by an actual divisor D | A^2 and therefore corresponds
to a genuine square-completed Type-II trap progression

    n == -4*D (mod 4*A-1).

The computation is finite structural evidence only; it does not prove global
first-hit status against earlier moduli that do not divide 4*A-1.
"""

import argparse
import json
from collections import Counter
from math import prod


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


def divisors_from_factorization(factors):
    ds = [1]
    for p, e in factors.items():
        base = list(ds)
        new = []
        pe = 1
        for _ in range(e + 1):
            new.extend(d * pe for d in base)
            pe *= p
        ds = new
    return sorted(new)


def divisors_of_square(n):
    f = factor_small(n)
    return divisors_from_factorization({p: 2 * e for p, e in f.items()})


def omega(n):
    return len(factor_small(n))


def realized_layer(A):
    m = 4 * A - 1
    ds = divisors_of_square(A)
    representatives = {}
    for D in ds:
        representatives.setdefault(D % m, []).append(D)
    return m, representatives


def ancestor_sets(m):
    fm = factor_small(m)
    out = []
    for e in divisors_from_factorization(fm):
        if e <= 1 or e >= m or e % 4 != 3:
            continue
        B = (e + 1) // 4
        q = {D % e for D in divisors_of_square(B)}
        out.append((e, B, q))
    return out


def analyze_depth(A):
    m, reps = realized_layer(A)
    ancestors = ancestor_sets(m)
    primitive = {}
    inherited = {}

    for r, Ds in reps.items():
        witnesses = []
        for e, B, q in ancestors:
            if r % e in q:
                witnesses.append({'modulus': e, 'depth': B})
        if witnesses:
            inherited[r] = {'representatives': Ds, 'ancestors': witnesses}
        else:
            primitive[r] = {'representatives': Ds}

    return {
        'A': A,
        'modulus': m,
        'A_factorization': factor_small(A),
        'modulus_factorization': factor_small(m),
        'omega_modulus': omega(m),
        'realized_class_count': len(reps),
        'primitive_class_count': len(primitive),
        'primitive_classes': primitive,
        'inherited_class_count': len(inherited),
    }


def run(A_max, save_examples=50):
    distribution = Counter()
    primitive_layers = 0
    examples = []
    max_omega = 0

    for A in range(1, A_max + 1):
        row = analyze_depth(A)
        if row['primitive_class_count'] == 0:
            continue
        primitive_layers += 1
        w = row['omega_modulus']
        distribution[w] += 1
        max_omega = max(max_omega, w)
        if len(examples) < save_examples or w >= 5:
            examples.append(row)

    return {
        'status': 'exact finite ancestry computation on realized classes D|A^2; not a global first-hit theorem',
        'A_max': A_max,
        'primitive_layer_count': primitive_layers,
        'primitive_layer_count_by_omega_4A_minus_1': dict(sorted(distribution.items())),
        'maximum_observed_omega': max_omega,
        'examples': examples,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--A-max', type=int, required=True)
    ap.add_argument('--json')
    ap.add_argument('--examples', type=int, default=50)
    args = ap.parse_args()

    result = run(args.A_max, args.examples)
    print({k: v for k, v in result.items() if k != 'examples'})
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(result, fh, indent=2)
