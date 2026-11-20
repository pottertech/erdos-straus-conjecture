#!/usr/bin/env python3
"""u=35 layer, CORRECTED cohort (FIRST_A_STRUCTURE.md reconciliation).

The true u=35 stage over the full residual class <= 10^7:
  entrants  = 65 (records with first-A >= 35)
  successes = 17 (first-A == 35)
  failures  = 48 (first-A >= 39)

Checks on the corrected cohort:
  1. exact verdict (u35_works_exact) vs the verified dataset first-A: 0 mismatches;
  2. coupled-CRT span criterion vs exact verdict: 0 mismatches;
  3. failure fingerprints: log-pair tables, v3(x), QR-purity, 7-parity;
  4. candidate separating invariant for the closed form, verified on all 65.
Stdlib + sympy (as in u35_layer_analysis.py).
"""
import json
import sys
from math import gcd
from collections import Counter

from sympy import factorint

sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('favC', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['favC'] = fav
spec.loader.exec_module(fav)

LOG5 = {}
v = 1
for k in range(4):
    LOG5[v] = k
    v = v * 2 % 5
LOG7 = {}
v = 1
for k in range(6):
    LOG7[v] = k
    v = v * 3 % 7
assert LOG5[4] == 2 and LOG7[6] == 3


def span_reach(lm):
    state = {(0, 0)}
    for (a, b), m in lm.items():
        nxt = set()
        for (s5, s7) in state:
            for c in range(-m, m + 1):
                aa = None if a is None else (s5 + c * a) % 4
                bb = None if b is None else (s7 + c * b) % 6
                nxt.add((s5 if aa is None else aa, s7 if bb is None else bb))
        state = nxt
    return (2, 3) in state


def span35_fails(n):
    x = (n + 35) // 4
    f = factorint(n * x)
    lm = {}
    for p, e in f.items():
        r5, r7 = p % 5, p % 7
        lm[(LOG5[r5] if r5 else None, LOG7[r7] if r7 else None)] = \
            lm.get((LOG5[r5] if r5 else None, LOG7[r7] if r7 else None), 0) + e
    return lm, not span_reach(lm)


def exact35(n):
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
    return any(d1 * d1 <= D and d1 % 35 == target for d1 in ds)


def main():
    fa = {}
    for line in open('results/layer4_certificates.jsonl'):
        r = json.loads(line)
        n = r['n']
        if n % 24 == 1:
            fa[n] = r['A']

    entrants = [n for n, a in fa.items() if a >= 35]
    succ = [n for n in entrants if fa[n] == 35]
    fail = [n for n in entrants if fa[n] >= 39]
    print(f"corrected u=35 cohort: entrants {len(entrants)} | succeed {len(succ)} | fail {len(fail)}")

    m_exact = m_span = 0
    fp = []
    for n in sorted(entrants):
        want = fa[n] <= 35
        ex = exact35(n)
        if bool(ex) != want:
            m_exact += 1
        lm, fails = span35_fails(n)
        if fails != (not want):
            m_span += 1
        v3 = factorint((n + 35) // 4).get(3, 0)
        # parity invariants
        qr5 = all(a is None or a % 2 == 0 for (a, b), m in lm.items() for _ in [0])
        qr7 = all((b is None or b % 2 == 0) for (a, b) in lm for _ in [0])
        fp.append({'n': n, 'first_A': fa[n], 'fails': fails,
                   'pairs': sorted([(str(a), str(b), m) for (a, b), m in lm.items()]),
                   'qr_pure_5': qr5, 'qr_pure_7': qr7})
    print(f"exact-vs-dataset mismatches: {m_exact}; span-vs-exact mismatches: {m_span}")

    ff = [d for d in fp if d['fails']]
    print(f"\nfailures: {len(ff)}")
    print("QR-pure-5 among failures:", sum(1 for d in ff if d['qr_pure_5']),
          " QR-pure-7 among failures:", sum(1 for d in ff if d['qr_pure_7']))
    print("QR-pure-5 among successes:", sum(1 for d in fp if not d['fails'] and d['qr_pure_5']),
          " QR-pure-7 among successes:", sum(1 for d in fp if not d['fails'] and d['qr_pure_7']))
    par5 = Counter((d['n'] % 5) for d in fp)
    print("n mod 5 split:", dict(par5))
    # candidate invariant: 7-component reach alone
    def reach7_only(lm):
        s = {0}
        for (a, b), m in lm.items():
            if b is None:
                continue
            s = {(t + c * b) % 6 for t in s for c in range(-m, m + 1)}
        return s
    inv = Counter()
    for d in fp:
        n = d['n']
        x = (n + 35) // 4
        f = factorint(n * x)
        lm = {}
        for p, e in f.items():
            r5, r7 = p % 5, p % 7
            lm[(LOG5[r5] if r5 else None, LOG7[r7] if r7 else None)] = \
                lm.get((LOG5[r5] if r5 else None, LOG7[r7] if r7 else None), 0) + e
        r7 = reach7_only(lm)
        # 7-part target is 3 (odd); even-reachable-only?
        even_only = all(t % 2 == 0 for t in r7)
        inv[(d['fails'], even_only)] += 1
    print("contingency (fails, 7-parity-even-only):", dict(inv))

    out = {'entrants': entrants, 'successes35': succ, 'failures35': fail,
           'exact_mismatches': m_exact, 'span_mismatches': m_span,
           'fingerprints': sorted(fp, key=lambda d: d['n'])}
    json.dump(out, open('analysis/u35_layer_corrected.json', 'w'), indent=1)
    print("wrote analysis/u35_layer_corrected.json")
    return


if __name__ == '__main__':
    main()
