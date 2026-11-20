#!/usr/bin/env python3
"""u=39 layer, CORRECTED cohort from the start (3 * 13 composite, = 3 mod 4).

True u=39 stage over the full residual class <= 10^7 (per FIRST_A_STRUCTURE):
  entrants  = 48 (records with first-A >= 39)
  successes = 22 (first-A == 39)
  failures  = 26 (first-A >= 43)

Structure: n = 24m + 1 gives x = (n+39)/4 = 6m + 10 = 2(3m+5): the forced
factor is 2 (both components: (Z/3)* log of 2 is 1 of C2, (Z/13)* log of 2
is 1 of C12), with 2's log pair (1, 1) -- odd in both components, so like
u=35 the parity argument is structurally dead and purity is never attained.

Checks:
  1. exact criterion vs the verified dataset first-A: 0 mismatches;
  2. coupled span in C2 x C12 (target (1,6), logs g3=2, g13=2) vs exact: 0 mismatches;
  3. subgroup relaxation (exponent caps dropped) count;
  4. fingerprints + saturation (coefficients reduce mod lcm(2,12) = 12).
Stdlib + sympy.
"""
import json
import sys
from math import gcd
from collections import Counter

from sympy import factorint

sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('favE', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['favE'] = fav
spec.loader.exec_module(fav)

LOG3C = {1: 0, 2: 1}          # (Z/3)* = C2, g = 2; −1 = 2 mod 3 -> log 1
LOG13 = {}
v = 1
for k in range(12):
    LOG13[v] = k
    v = v * 2 % 13
assert LOG13[12] == 6, 'target log in C12'


def span_reach(items):
    state = {(0, 0)}
    for (a, b), m in items:
        nxt = set()
        for (s3, s13) in state:
            for c in range(-m, m + 1):
                aa = None if a is None else (s3 + c * a) % 2
                bb = None if b is None else (s13 + c * b) % 12
                nxt.add((s3 if aa is None else aa, s13 if bb is None else bb))
        state = nxt
    return (1, 6) in state


def span39_fails(n):
    x = (n + 39) // 4
    f = factorint(n * x)
    lm = {}
    for p, e in f.items():
        a = LOG3C[p % 3] if p % 3 else None
        b = LOG13[p % 13] if p % 13 else None
        key = (a, b)
        lm[key] = lm.get(key, 0) + e
    return lm, not span_reach([((a, b), m) for (a, b), m in lm.items()])


def u39_works_exact(n):
    x = (n + 39) // 4
    nx = n * x
    if nx % 39 == 0:
        return True
    if gcd(nx, 39) == 1:
        r = fav.centered_check(n, 39)
        return bool(r.success) if r is not None else None
    f = factorint(nx)
    ds = {1}
    for p, e in f.items():
        ds = {d * p**k for d in ds for k in range(e + 1)}
    D = nx * nx
    target = (-nx) % 39
    return any(d1 * d1 <= D and d1 % 39 == target for d1 in ds)


def subgroup_contains(lm):
    S = {(0, 0)}
    gens = [((a % 2) if a is not None else 0, (b % 12) if b is not None else 0)
            for (a, b), m in lm.items()]
    prev = set()
    while prev != S:
        prev = set(S)
        for s in prev:
            for g in gens:
                S.add(((s[0] + g[0]) % 2, (s[1] + g[1]) % 12))
    return (1, 6) in S


def main():
    fa = {}
    for line in open('results/layer4_certificates.jsonl'):
        r = json.loads(line)
        n = r['n']
        if n % 24 == 1:
            fa[n] = r['A']

    entrants = [n for n, a in fa.items() if a >= 39]
    succ = [n for n in entrants if fa[n] == 39]
    fail = [n for n in entrants if fa[n] >= 43]
    print(f"corrected u=39 cohort: entrants {len(entrants)} | succeed {len(succ)} | fail {len(fail)}")

    m_exact = m_span = sub_exact_miss = 0
    fp = []
    for n in sorted(entrants):
        want = fa[n] <= 39
        ex = u39_works_exact(n)
        if bool(ex) != want:
            m_exact += 1
        lm, sfail = span39_fails(n)
        if sfail != (not want):
            m_span += 1
        sg = subgroup_contains(lm)
        if sg != want:
            sub_exact_miss += 1
        f_x = factorint((n + 39) // 4)
        pure13 = all((b is None) or (b % 2 == 0) for (a, b), m in lm.items())
        fp.append({'n': n, 'first_A': fa[n], 'fails': not want,
                   'pairs': sorted([(str(a), str(b), m) for (a, b), m in lm.items()]),
                   'pure_13': pure13,
                   'v2_x': (f_x.get(2, 0)), 'v3_x': (f_x.get(3, 0)),
                   'n_mod_72': n % 72})
    print(f"exact-vs-dataset mismatches: {m_exact}; span-vs-exact mismatches: {m_span}"
          f"; subgroup-vs-exact mismatches: {sub_exact_miss}")

    ff = [d for d in fp if d['fails']]
    print(f"failures: {len(ff)}")
    print("  pure_13 among failures:", sum(1 for d in ff if d['pure_13']),
          " among successes:", sum(1 for d in fp if not d['fails'] and d['pure_13']))
    print("  n mod 72 of failures:", dict(Counter(d['n_mod_72'] for d in ff)))
    print("  failure first_A histogram:", dict(Counter(d['first_A'] for d in ff)))
    pat = Counter(tuple(r['pairs']) for r in fp)
    mixed = [k for k, c in pat.items()
             if len({d['fails'] for d in fp if tuple(d['pairs']) == k}) > 1]
    print("  distinct pair-patterns:", len(pat), " mixed-outcome:", len(mixed))

    out = {'entrants': entrants, 'successes39': succ, 'failures39': fail,
           'exact_mismatches': m_exact, 'span_mismatches': m_span,
           'subgroup_mismatches': sub_exact_miss,
           'fingerprints': sorted(fp, key=lambda d: d['n'])}
    json.dump(out, open('analysis/u39_layer.json', 'w'), indent=1)
    print("wrote analysis/u39_layer.json")
    return


if __name__ == '__main__':
    main()
