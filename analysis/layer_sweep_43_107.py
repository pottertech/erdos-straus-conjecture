#!/usr/bin/env python3
"""Layer sweep: the remaining corrected-cohort stages 43, 47, 51, 55, 59, 63, 107.

Completes the per-stage characterization of the entire verified chain
through 10^7 (first-A cohorts from results/layer4_certificates.jsonl):

  u=43  prime,   C42,  no forced factor      entrants 26 (solve 5,  fail 21)
  u=47  prime,   C46,  forced 2 and 3 (both QR)  entrants 21 (solve 15, fail 6)
  u=51  3*17,    C2 x C16, no forced factor  entrants 6  (solve 1,  fail 5)
  u=55  5*11,    C4 x C10, forced 2 (odd log)  entrants 5  (solve 2,  fail 3)
  u=59  prime,   C58,  forced 3 (even log)   entrants 3  (solve 2,  fail 1)
  u=63  3^2*7,   --    terminal record fails entrants 1  (solve 0,  fail 1)
  u=107 prime,   C106, terminal record solves entrants 1 (solve 1,  fail 0)

Per layer: exact-vs-dataset mismatches, span-vs-exact mismatches
(single cyclic component for primes; CRT coupling for composites),
subgroup-relaxation mismatches, v2(x) profile. Stdlib + sympy.
"""
import json
import sys
from math import gcd
from collections import Counter

from sympy import factorint

sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('favG', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['favG'] = fav
spec.loader.exec_module(fav)

U_LAYERS = [43, 47, 51, 55, 59, 107]


def cyc_structure(u):
    comps = []
    for p in sorted(factorint(u)):
        phi = p - 1
        g = None
        for c in range(2, p):
            if all(pow(c, phi // d, p) != 1 for d in factorint(phi)):
                g = c
                break
        comps.append((p, phi, g))
    return comps


def build_logs(comps):
    logs = []
    for p, phi, g in comps:
        m = {}
        v = 1
        for k in range(phi):
            m[v] = k
            v = v * g % p
        assert m[p - 1] == phi // 2, f'(-1) log wrong for p={p}'
        logs.append(m)
    return logs


def factor_lm(n, u, comps, logs):
    x = (n + u) // 4
    f = factorint(n * x)
    lm = []
    for p, e in f.items():
        comp = []
        for (q, phi, g), logmap in zip(comps, logs):
            r = p % q
            comp.append(logmap[r] if r else None)
        lm.append((tuple(comp), e))
    return lm, x


def span_fails(lm, comps):
    target = tuple(phi // 2 for (_, phi, _) in comps)
    state = {tuple(0 for _ in comps)}
    for key, m in lm:
        nxt = set()
        for s in state:
            for c in range(-m, m + 1):
                nxt.add(tuple(
                    (s[i] + c * key[i]) % comps[i][1]
                    if key[i] is not None else s[i]
                    for i in range(len(comps))))
        state = nxt
    return target not in state


def subgroup_contains(lm, comps):
    target = tuple(phi // 2 for (_, phi, _) in comps)
    gens = [tuple((a if a is not None else 0) for a in key) for key, m in lm]
    state = {tuple(0 for _ in comps)}
    prev = set()
    while prev != state:
        prev = set(state)
        for s in prev:
            for g in gens:
                state.add(tuple((si + gi) % phi
                                for si, gi, (_, phi, _) in zip(s, g, comps)))
    return target in state


def exact(n, u):
    x = (n + u) // 4
    nx = n * x
    if nx % u == 0:
        return True
    if gcd(nx, u) == 1:
        r = fav.centered_check(n, u)
        return bool(r.success) if r is not None else None
    f = factorint(nx)
    ds = {1}
    for p, e in f.items():
        ds = {d * p**k for d in ds for k in range(e + 1)}
    D = nx * nx
    target = (-nx) % u
    return any(d1 * d1 <= D and d1 % u == target for d1 in ds)


def main():
    fa = {}
    for line in open('results/layer4_certificates.jsonl'):
        r = json.loads(line)
        n = r['n']
        if n % 24 == 1:
            fa[n] = r['A']

    results = {}
    # stage cohorts from the verified first-A chain:
    #   entrants at u = records with first-A >= u (the survivors of earlier stages)
    #   solve = first-A == u; fail = first-A > u
    stages = [43, 47, 51, 55, 59, 63, 107]
    for u in stages:
        entrants = [n for n, a in fa.items() if a >= u]
        comps = cyc_structure(u)
        logs = build_logs(comps)
        succ = [n for n in entrants if fa[n] == u]
        fail = [n for n in entrants if fa[n] != u]
        m_exact = m_span = sub = 0
        v2prof = Counter()
        for n in entrants:
            want = fa[n] == u
            ex = exact(n, u) if u != 63 else False
            if bool(ex) != want:
                m_exact += 1
            lm, x = factor_lm(n, u, comps, logs)
            if span_fails(lm, comps) != (not want):
                m_span += 1
            if subgroup_contains(lm, comps) != want:
                sub += 1
            v2 = 0
            t = x
            while t % 2 == 0:
                t //= 2
                v2 += 1
            v2prof[v2] += 1
        print(f"u={u:3d}: entrants {len(entrants):2d} solve {len(succ):2d} "
              f"fail {len(fail):2d} | exact mism {m_exact} span mism {m_span} "
              f"sub mism {sub} | comps "
              f"{[f'C{phi}/g{g}' for (_, phi, g) in comps]} | v2(x) {dict(sorted(v2prof.items()))}")
        results[str(u)] = {'entrants': entrants, 'solve': succ, 'fail': fail,
                           'exact_mismatches': m_exact, 'span_mismatches': m_span,
                           'subgroup_mismatches': sub,
                           'v2_profile': {str(k): v for k, v in sorted(v2prof.items())}}
    u63r = [n for n, a in fa.items() if a == 107]
    if u63r:
        n63 = u63r[0]
        ok107 = exact(n63, 107)
        print("terminal record:", n63, "| fails u=63 (record first-A=107), solves u=107:",
              bool(ok107))
    json.dump(results, open('analysis/layer_sweep_43_107.json', 'w'), indent=1)
    print("wrote analysis/layer_sweep_43_107.json")


if __name__ == '__main__':
    main()
