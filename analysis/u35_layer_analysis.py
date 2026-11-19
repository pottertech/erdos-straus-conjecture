#!/usr/bin/env python3
"""u=35 layer analysis for the corrected deterministic cascade (OSR stack).

Stage entrants: the 93 survivors of the u=31 stage (analysis/u31_layer.json).
u=35 = 5 * 7 (composite, ≡ 3 mod 4). For n ≡ 1 (mod 24): x = (n+35)/4 = 6m+9
= 3(2m+3), so 3 is a forced factor of x (v3(x) >= 1).

Uses the pack's (Z/35)* structure: (Z/5)* x (Z/7)*, target (-1, -1), reached
by the same signed-exponent span as the exact criterion. Cross-checks the
CRT-span formulation against the exact criteria on all entrants.
"""
import json
import sys
from math import gcd

from sympy import factorint

sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('fav7', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['fav7'] = fav
spec.loader.exec_module(fav)

# Structure of (Z/5)*: cyclic order 4, g=2; target -1 = 2^2 mod 5.
LOG5 = {}
v = 1
for k in range(4):
    LOG5[v] = k
    v = v * 2 % 5
# (Z/7)*: cyclic order 6, g=3; target -1 = 3^3 mod 7.
LOG7 = {}
v = 1
for k in range(6):
    LOG7[v] = k
    v = v * 3 % 7

assert LOG5[4 % 5] == 2 and LOG7[6 % 7] == 3, 'primitive root/target sanity'


def crt_pair_class(p):
    """For prime p: (r5 = dlog5(p mod 5 or None-for-nonunit), r7 = ...)."""
    r5 = p % 5
    r7 = p % 7
    return (LOG5.get(r5), LOG7.get(r7))


def span35_reaches_neg1(logs_mult):
    """Exact span check in (Z/5) x (Z/7): exists signed coeffs c_p with
    |c_p| <= m_p such that sum c_p * (a_p, b_p) == (-1, -1) componentwise,
    where a_p in Z/4 (5-part), b_p in Z/6 (7-part). None-log handled by
    caller (unit factors contribute nothing)."""
    items = [(a, b, m) for (a, b), m in logs_mult.items() if a is not None or b is not None]
    reach5 = {0}
    reach7 = {0}
    # Coupled DFS: expand combined residues.
    state = {(0, 0)}
    for a, b, m in items:
        nxt = set()
        for (s5, s7) in state:
            for c in range(-m, m + 1):
                aa = None if a is None else (s5 + c * a) % 4
                bb = None if b is None else (s7 + c * b) % 6
                nx5 = s5 if aa is None else aa
                nx7 = s7 if bb is None else bb
                nxt.add((nx5, nx7))
        state = nxt
    return (2, 3) in state  # (-1 mod 5) = 4 -> log 2; (-1 mod 7) = 6 -> log 3


def u35_works_exact(n):
    x = (n + 35) // 4
    nx = n * x
    if nx % 35 == 0:
        return True
    if gcd(nx, 35) == 1:
        r = fav.centered_check(n, 35)
        return bool(r.success) if r is not None else None
    f = factorint(nx)
    ds = {1}
    for p, e in f.items():
        ds = {d * p**k for d in ds for k in range(e + 1)}
    D = nx * nx
    target = (-nx) % 35
    for d1 in ds:
        if d1 * d1 <= D and d1 % 35 == target:
            return True
    return False


def span35_check(n):
    """Span formulation: logs of prime factors of nx in CRT components."""
    x = (n + 35) // 4
    f = factorint(n * x)
    lm = {}
    for p, e in f.items():
        r5, r7 = p % 5, p % 7
        key = (LOG5[r5] if r5 else None, LOG7[r7] if r7 else None)
        lm[key] = lm.get(key, 0) + e
    return not span35_reaches_neg1(lm)


def main():
    d31 = json.load(open('analysis/u31_layer.json'))
    entrants = d31['u31']['failures']  # 93 survivors of u=31
    succ35, fail35 = [], []
    for n in entrants:
        w = u35_works_exact(n)
        (succ35 if w else fail35).append(n)
    # span cross-check both directions
    mis = [n for n in entrants if span35_check(n) != ((n in fail35))]
    fp = []
    for n in entrants:
        x = (n + 35) // 4
        f = factorint(n * x)
        lm = {}
        for p, e in f.items():
            r5, r7 = p % 5, p % 7
            key = (LOG5[r5] if r5 else None, LOG7[r7] if r7 else None)
            lm[key] = lm.get(key, 0) + e
        v3 = f.get(3, 0)
        fp.append({'n': n, 'v3_x': (factorint(x)).get(3, 0), 'x': x,
                   'logs': {f'{a},{b}': m for (a, b), m in sorted(
                       lm.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1])))},
                   'fails35': n in fail35})
    out = {'entrants': entrants, 'successes35': succ35, 'failures35': fail35,
           'span_mismatches': mis,
           'failures_nonspan': [n for n in entrants
                                if (n in succ35) != (not span35_check(n))],
           'fingerprints': fp}
    json.dump(out, open('analysis/u35_layer.json', 'w'), indent=1)
    print(f'u=35 stage: entrants {len(entrants)} | succeed {len(succ35)} | '
          f'fail {len(fail35)} | span mismatches {len(mis)}')
    print('survivors after u=35:', len(fail35), '(doc: 67)')
    qr5 = lambda f: all(l[0] is None or l[0] % 2 == 0 for l, m in
                        ([(eval(k), m) for k, m in f['logs'].items()]))
    print('non-QR-pure-at-35 failures:',
          sum(1 for f in fp if f['fails35'] and not qr5(f)))


if __name__ == '__main__':
    main()
