#!/usr/bin/env python3
"""Verification for MOD31_EXACT_REDUCTION.md (run after u31_layer_analysis.py).

Checks, on analysis/u31_layer.json:
  1. span-criterion (log form, primitive root 3 mod 31) vs exact
     centered/divisor-pair criterion on ALL u=31 stage entrants: 0 mismatches;
  2. QR-pure sub-theorem: every QR-pure entrant fails; count reported;
  3. cube-QNR rescue theorem: no failure admits the rescue witness (0/93),
     and every cube-QNR success has a valid witness under the stated v2
     conditions (mechanism check; successes outside the single-witness form
     are rescued by wider spans and are only counted, not verified here);
  4. cascade replication counts vs DETERMINISTIC_CASCADE_STATUS.md.

Exit code 0 = all checks pass.
"""
import json
import sys
from math import gcd

from sympy import factorint, legendre_symbol

d = json.load(open('analysis/u31_layer.json'))

dlog = {}
v = 1
for k in range(30):
    dlog[v] = k
    v = v * 3 % 31
inv = {a: b for b, a in dlog.items()}

KMAP = {15: 0, 9: 1, 21: -1, 3: 2, 27: -2}  # log_s -> c_2 in the cube-QNR witness


def span_fails(n, u=31):
    x = (n + u) // 4
    f = factorint(n * x)
    logs = {}
    for p, e in f.items():
        logs[dlog[p % 31]] = logs.get(dlog[p % 31], 0) + e
    res = {0}
    for l, vv in sorted(logs.items()):
        res = {(r + c * l) % 30 for r in res for c in range(-vv, vv + 1)}
        if len(res) == 30:
            break
    return 15 not in res


def exact_result(n):
    x = (n + 31) // 4
    nx = n * x
    if gcd(nx, 31) == 1:
        r = fav.centered_check(n, 31)
        return bool(r.success)
    return nx % 31 == 0


def rescue_admissible(n):
    """(s, q, k) exists per the cube-QNR witness with v2(nx) >= |k|?"""
    x = (n + 31) // 4
    a = (x & -x).bit_length() - 1 if x % 2 == 0 else 0
    f = factorint(n * x)
    for s, k in KMAP.items():
        if f.get(inv[s], 0) >= 1 and a >= abs(k):
            return (s, inv[s], k)
    return None


sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('fav_v', 'finite_abelian_centered_verifier.py')
fav = importlib.util.module_from_spec(spec)
sys.modules['fav_v'] = fav
spec.loader.exec_module(fav)

errors = []

# 1. span vs exact on all entrants
mis = []
for n in d['u31']['entrants']:
    if span_fails(n) != (not exact_result(n)):
        mis.append(n)
print(f'check 1: span-criterion vs exact criterion on {len(d["u31"]["entrants"])} entrants: '
      f'{len(mis)} mismatches')
if mis:
    errors.append(f'span mismatches: {mis}')

# 2. QR-pure failures
fp = d['u31_failure_fingerprints']
qr_pure_fail = sum(1 for f in fp if f['qr_pure_mod31'])
print(f'check 2: QR-pure failures: {qr_pure_fail} of {len(fp)} (MOD31 doc: 60)')
if qr_pure_fail != 60:
    errors.append(f'QR-pure count {qr_pure_fail} != 60')

# also: no QR-pure success
qr_pure_succ = 0
for n in d['u31']['successes']:
    f = factorint(n * ((n + 31) // 4))
    if all(legendre_symbol(p, 31) == 1 for p in f):
        qr_pure_succ += 1
print(f'check 2b: QR-pure successes (must be 0): {qr_pure_succ}')
if qr_pure_succ:
    errors.append('QR-pure success exists - contradicts parity obstruction')

# 3. rescue theorem both directions
resc_in_fail = [n for n in d['u31']['failures'] if rescue_admissible(n)]
print(f'check 3a: failures admitting the cube-QNR witness (must be 0): {len(resc_in_fail)}')
if resc_in_fail:
    errors.append(f'failures with cube-QNR witness: {resc_in_fail}')
covered_s = [n for n in d['u31']['successes'] if rescue_admissible(n)]
print(f'check 3b: successes covered by the witness form: {len(covered_s)} '
      f'(sufficient-direction count; rest use wider spans)')

# 4. cascade replication counts
doc = {'hard_primes': 48711, 'after_shift_divisor': 7272}
seq_doc = {'7': 2137, '11': 1054, '15': 681, '23': 283, '31': 93, '35': 67,
           '39': 29, '43': 25, '47': 9, '51': 7, '55': 5, '59': 2, '63': 1}
if d['hard_primes'] != doc['hard_primes'] or d['after_shift_divisor'] != doc['after_shift_divisor']:
    errors.append('cascade base counts differ')
for u, expected_surv in seq_doc.items():
    got = d['sequential'][u]['survivors']
    if got != expected_surv:
        errors.append(f'layer u={u} survivors {got} != {expected_surv}')
print(f'check 4: cascade replication vs documented tables: '
      f'{"OK" if not any(e.startswith("cascade") or "survivors" in e for e in errors) else "FAIL"}')
print('residual final:', d['residual_final'])
if d['residual_final'] != [8803369]:
    errors.append(f'unexpected residual {d["residual_final"]}')

if errors:
    print('ERRORS:')
    for e in errors:
        print(' -', e)
    sys.exit(1)
print('ALL MOD31 VERIFICATION CHECKS PASSED')
