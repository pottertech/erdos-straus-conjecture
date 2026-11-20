#!/usr/bin/env python3
"""u=31 layer, CORRECTED cohort (FIRST_A_STRUCTURE.md reconciliation).

The true u=31 stage over the full residual class <= 10^7:
  entrants  = 217 (records with first-A >= 31)
  successes = 152 (first-A == 31)
  failures  = 65  (first-A >= 35)

Checks (mirroring analysis/u31_classification_verify.py):
  1. exact criterion vs the verified dataset first-A: 0 mismatches;
  2. span criterion (log form, primitive root 3, target 15) vs dataset: 0 mismatches;
  3. QR-purity (all factors 3-power residues mod 31, i.e. even logs) among
     failures vs successes -- this analysis is meaningful here, unlike u=35,
     because the forced factor 2 has even log (log_3(2) = 24);
  4. cube-QNR rescue admissibility: the doc's theorem predicts no failure
     admits a rescue witness;
  5. the span-delicate (non-QR-pure failure) recount, and v2-slice tables.
"""
import json
import sys
from math import gcd
from collections import Counter

from sympy import factorint

sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('favD', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['favD'] = fav
spec.loader.exec_module(fav)

DLOG = {}
v = 1
for k in range(30):
    DLOG[v] = k
    v = v * 3 % 31
INV = {b: a for a, b in DLOG.items()}
KMAP = {15: 0, 9: 1, 21: -1, 3: 2, 27: -2}


def span31_fails(n):
    x = (n + 31) // 4
    f = factorint(n * x)
    logs = {}
    for p, e in f.items():
        d = DLOG[p % 31]
        logs[d] = logs.get(d, 0) + e
    res = {0}
    for l, vv in sorted(logs.items()):
        res = {(r + c * l) % 30 for r in res for c in range(-vv, vv + 1)}
        if len(res) == 30:
            break
    return logs, 15 not in res


def exact31(n):
    x = (n + 31) // 4
    nx = n * x
    if nx % 31 == 0:
        return True
    if gcd(nx, 31) == 1:
        r = fav.centered_check(n, 31)
        return bool(r.success) if r is not None else None
    return nx % 31 == 0


def rescue_admissible(n):
    x = (n + 31) // 4
    a = (x & -x).bit_length() - 1 if x % 2 == 0 else 0
    f = factorint(n * x)
    for s, k in KMAP.items():
        if f.get(INV[s], 0) >= 1 and a >= abs(k):
            return (s, INV[s], k)
    return None


def main():
    fa = {}
    for line in open('results/layer4_certificates.jsonl'):
        r = json.loads(line)
        n = r['n']
        if n % 24 == 1:
            fa[n] = r['A']
    entrants = [n for n, a in fa.items() if a >= 31]
    succ = [n for n in entrants if fa[n] == 31]
    fail = [n for n in entrants if fa[n] >= 35]
    print(f"corrected u=31 cohort: entrants {len(entrants)} | succeed {len(succ)} | fail {len(fail)}")

    m_exact = m_span = 0
    fp = []
    for n in sorted(entrants):
        want_fail = fa[n] >= 35
        ex = exact31(n)
        if bool(ex) != (not want_fail):
            m_exact += 1
        logs, sfail = span31_fails(n)
        if sfail != want_fail:
            m_span += 1
        x = (n + 31) // 4
        v2nx = (factorint(n * x)).get(2, 0)
        qr_pure = all(d % 2 == 0 for d in logs)
        resc = rescue_admissible(n)
        fp.append({'n': n, 'first_A': fa[n], 'fails': want_fail,
                   'qr_pure': qr_pure, 'rescue_witness': str(resc),
                   'v2_x': (x & -x).bit_length() - 1 if x % 2 == 0 else 0,
                   'n_mod_96': n % 96})
    print(f"exact-vs-dataset mismatches: {m_exact}; span-vs-exact mismatches: {m_span}")

    ff = [d for d in fp if d['fails']]
    ss = [d for d in fp if not d['fails']]
    print(f"failures: {len(ff)}")
    print("  QR-pure among failures:", sum(1 for d in ff if d['qr_pure']))
    print("  QR-pure among successes (must be 0):", sum(1 for d in ss if d['qr_pure']))
    print("  failures admitting the cube-QNR rescue (must be 0):",
          sum(1 for d in ff if d['rescue_witness'] != 'None'))
    print("  successes covered by a simple witness form:",
          sum(1 for d in ss if d['rescue_witness'] != 'None'))
    print("  span-delicate failures (non-QR-pure, no rescue):",
          sum(1 for d in ff if (not d['qr_pure']) and d['rescue_witness'] == 'None'))
    print("  failure count by n mod 96 slice:", dict(Counter(d['n_mod_96'] for d in ff)))
    print("  failure first_A histogram:", dict(Counter(d['first_A'] for d in ff)))

    out = {'entrants': entrants, 'successes31': succ, 'failures31': fail,
           'exact_mismatches': m_exact, 'span_mismatches': m_span,
           'fingerprints': sorted(fp, key=lambda d: d['n'])}
    json.dump(out, open('analysis/u31_layer_corrected.json', 'w'), indent=1)
    print("wrote analysis/u31_layer_corrected.json")
    return


if __name__ == '__main__':
    main()
