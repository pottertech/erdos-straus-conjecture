#!/usr/bin/env python3
"""
Deep dive into the non-trivial-stab cases where v9 properties don't hold.
Classify the cases where -1's coset is NOT covered or nm IS in S.
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, mod_inverse
from collections import defaultdict, Counter
from itertools import product as iterproduct
from math import lcm

COVERING_A = [3, 7, 11, 15, 19, 23, 27, 31]
PRIME_A = [3, 7, 11, 19, 23, 31]

def find_primitive_root(p):
    if p == 2: return 1
    phi = p - 1
    factors = factorint(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    return None

def discrete_log_mod(g, target, p):
    val = 1
    for i in range(p - 1):
        if val == target % p: return i
        val = (val * g) % p
    return None

def multiplicative_order(a, n):
    if gcd(a, n) > 1: return None
    val = a % n
    for i in range(1, n):
        if val == 1: return i
        val = (val * a) % n
    return None

def compute_full_analysis(n, A):
    if gcd(n, A) > 1: return None
    m = (n + A) // 4
    nx = n * m
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    if not prime_factors: return None
    if not isprime(A): return None
    
    g = find_primitive_root(A)
    if g is None: return None
    
    orders = [multiplicative_order(p, A) for p, _ in prime_factors]
    h = 1
    for o in orders: h = lcm(h, o)
    if h <= 1: return None
    
    s_values = {}
    for p, e in prime_factors:
        dlg = discrete_log_mod(g, p, A)
        step = (A - 1) // h
        if h <= 1:
            s_values[p] = 0; continue
        try:
            s_inv = mod_inverse(step, h)
            s_i = (dlg * s_inv) % h
        except:
            s_i = None
            for s in range(h):
                if (s * step) % h == dlg % h: s_i = s; break
            if s_i is None: return None
        s_values[p] = s_i
    
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    
    D_A = set()
    ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    for combo in iterproduct(*ranges):
        D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
    
    T_in_D = dlog_T in D_A
    stab = set()
    for s in range(h):
        if all((d + s) % h in D_A for d in D_A): stab.add(s)
    
    # Cosets
    cosets = []
    remaining = set(range(h))
    while remaining:
        rep = min(remaining)
        coset = {(rep + s) % h for s in stab}
        cosets.append((rep, coset))
        remaining -= coset
    
    covered_cosets = {rep for rep, coset in cosets if coset & D_A}
    T_coset = next(rep for rep, coset in cosets if dlog_T in coset)
    neg1_coset = next(rep for rep, coset in cosets if (h//2) in coset)
    nm_coset = next(rep for rep, coset in cosets if dlog_nm in coset)
    
    return {
        'n': n, 'A': A, 'h': h, 'm': m,
        'dlog_T': dlog_T, 'dlog_nm': dlog_nm, 'dlog_neg1': h//2,
        'T_in_D': T_in_D,
        'neg1_in_D': (h//2) in D_A,
        'stab_size': len(stab), 'stab': sorted(stab),
        'D_A_size': len(D_A), 'D_A': sorted(D_A),
        'holes': sorted(set(range(h)) - D_A),
        'cosets': [(rep, sorted(coset)) for rep, coset in cosets],
        'covered_cosets': sorted(covered_cosets),
        'uncovered_cosets': sorted(set(r for r,_ in cosets) - covered_cosets),
        'T_coset': T_coset, 'neg1_coset': neg1_coset, 'nm_coset': nm_coset,
        'nm_in_stab': dlog_nm in stab,
        'prime_factors': [(p, e) for p, e in prime_factors],
        's_values': {p: s_values[p] for p, _ in prime_factors},
    }

def main():
    print("Scanning all non-trivial-stab gap cases...")
    cases = []
    n = 13
    while n <= 100000:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            for A in PRIME_A:
                if gcd(n, A) > 1: continue
                info = compute_full_analysis(n, A)
                if info and not info['T_in_D'] and info['stab_size'] > 1:
                    cases.append(info)
        n = nextprime(n)
    
    print(f"Total: {len(cases)}")
    
    # Classify into structural types
    type_A = []  # "Clean" v9 case: -1 covered, T uncovered, nm not in S, T != -1 coset, 1 uncovered coset
    type_B = []  # nm in S but T still not in D_A (surprising!)
    type_C = []  # -1 not in covered coset
    type_D = []  # Multiple uncovered cosets
    type_E = []  # T in same coset as -1
    
    for c in cases:
        clean = (
            c['neg1_coset'] in c['covered_cosets'] and
            c['T_coset'] in c['uncovered_cosets'] and
            not c['nm_in_stab'] and
            c['T_coset'] != c['neg1_coset'] and
            len(c['uncovered_cosets']) == 1
        )
        if clean:
            type_A.append(c)
        elif c['nm_in_stab']:
            type_B.append(c)
        elif c['neg1_coset'] not in c['covered_cosets']:
            type_C.append(c)
        elif len(c['uncovered_cosets']) > 1:
            type_D.append(c)
        elif c['T_coset'] == c['neg1_coset']:
            type_E.append(c)
        else:
            type_E.append(c)  # catch-all
    
    print(f"\n{'='*60}")
    print("STRUCTURAL CLASSIFICATION")
    print(f"{'='*60}")
    print(f"Type A (clean v9 case): {len(type_A)}")
    print(f"Type B (nm in S, but T still missing): {len(type_B)}")
    print(f"Type C (-1 coset not covered): {len(type_C)}")
    print(f"Type D (multiple uncovered cosets): {len(type_D)}")
    print(f"Type E (T = -1 coset or other): {len(type_E)}")
    
    # Deep dive into Type B: nm IS in stabilizer but T still not in D_A
    # This is the most surprising case
    print(f"\n{'='*60}")
    print(f"TYPE B: nm in S but T not in D_A ({len(type_B)} cases)")
    print(f"{'='*60}")
    
    if type_B:
        # When nm in S, T = -1*nm should be in -1's coset (since nm in S means nm+0 in S coset)
        # Wait: nm in S means dlog(nm) is in the stabilizer set
        # T = -1 + nm (additively in dlog) = h/2 + dlog_nm
        # If dlog_nm in S, then h/2 + dlog_nm is in (h/2 + S) which is -1's coset
        # So T should be in -1's coset. But -1's coset may or may not be covered!
        
        for c in type_B[:10]:
            print(f"\n  n={c['n']}, A={c['A']}, h={c['h']}")
            print(f"    S = {c['stab']}")
            print(f"    dlog(nm) = {c['dlog_nm']}, nm in S? {c['nm_in_stab']}")
            print(f"    dlog(-1) = {c['dlog_neg1']}, -1 in D_A? {c['neg1_in_D']}")
            print(f"    dlog(T) = {c['dlog_T']}")
            print(f"    T coset = {c['T_coset']}, -1 coset = {c['neg1_coset']}")
            print(f"    -1 coset covered? {c['neg1_coset'] in c['covered_cosets']}")
            print(f"    |D_A| = {c['D_A_size']}/{c['h']}")
            print(f"    Covered cosets: {c['covered_cosets']}")
            print(f"    Uncovered cosets: {c['uncovered_cosets']}")
            
            # Key question: is -1 actually in D_A?
            print(f"    -1 in D_A (dlog h/2 in D_A)? {c['neg1_in_D']}")
    
    # Type B analysis: if nm in S and -1 in D_A, then T = -1+nm should be in D_A
    # because D_A is S-invariant and -1 in D_A means -1's whole coset is in D_A
    # and nm in S means T = -1+nm is in -1's coset
    # So if T is NOT in D_A, it must be that -1 is NOT in D_A!
    
    type_b_neg1_not_in_D = sum(1 for c in type_B if not c['neg1_in_D'])
    type_b_neg1_in_D_but_coset_uncovered = sum(1 for c in type_B if c['neg1_in_D'] and c['neg1_coset'] not in c['covered_cosets'])
    print(f"\n  Type B breakdown:")
    print(f"    -1 NOT in D_A: {type_b_neg1_not_in_D}")
    print(f"    -1 in D_A but coset uncovered: {type_b_neg1_in_D_but_coset_uncovered}")
    
    # If -1 not in D_A, that's a DIFFERENT obstruction - it's not the coset obstruction
    # at all, it's that -1 itself is not achievable in D_A
    print(f"\n{'='*60}")
    print("REVISED CLASSIFICATION")
    print(f"{'='*60}")
    
    # The real question: is -1 in D_A in the gap cases?
    neg1_in_D_count = sum(1 for c in cases if c['neg1_in_D'])
    neg1_not_in_D_count = sum(1 for c in cases if not c['neg1_in_D'])
    print(f"\n-1 in D_A: {neg1_in_D_count}/{len(cases)}")
    print(f"-1 NOT in D_A: {neg1_not_in_D_count}/{len(cases)}")
    
    # The cases where -1 is NOT in D_A are fundamentally different:
    # the obstruction is that -1 is not reachable, not that the coset blocks T
    if neg1_not_in_D_count > 0:
        print(f"\nCases where -1 NOT in D_A (different obstruction type):")
        neg1_gap = [c for c in cases if not c['neg1_in_D']]
        h_dist = Counter(c['h'] for c in neg1_gap)
        A_dist = Counter(c['A'] for c in neg1_gap)
        stab_dist = Counter(c['stab_size'] for c in neg1_gap)
        print(f"  h distribution: {dict(sorted(h_dist.items()))}")
        print(f"  A distribution: {dict(sorted(A_dist.items()))}")
        print(f"  Stab size: {dict(stab_dist)}")
        
        # For these, the issue is -1 not in D_A, which means h/2 is not in the bounded sumset
        # This is the SAME as the trivial-stab parity obstruction!
        print(f"\n  These are cases where -1 = g^(h/2) is not in D_A.")
        print(f"  The obstruction is parity-based (same as trivial-stab), not coset-based.")
    
    # Cases where -1 IS in D_A but T is not
    print(f"\n{'='*60}")
    print(f"CASES WHERE -1 IN D_A BUT T NOT IN D_A: {neg1_in_D_count}")
    print(f"{'='*60}")
    
    neg1_yes = [c for c in cases if c['neg1_in_D']]
    
    # In these cases, -1 is in D_A. If D_A is S-invariant, -1's coset is covered.
    # T = -1 + nm. If nm not in S, T is in a different coset → uncovered.
    # If nm in S, T is in -1's coset → should be covered.
    
    nm_not_in_S = [c for c in neg1_yes if not c['nm_in_stab']]
    nm_in_S = [c for c in neg1_yes if c['nm_in_stab']]
    
    print(f"  nm not in S: {len(nm_not_in_S)} (classic coset obstruction)")
    print(f"  nm in S: {len(nm_in_S)} (should work but doesn't? investigate)")
    
    if nm_in_S:
        print(f"\n  Anomalous: -1 in D_A, nm in S, but T not in D_A:")
        for c in nm_in_S[:5]:
            print(f"    n={c['n']}, A={c['A']}, h={c['h']}")
            print(f"      dlog(-1)={c['dlog_neg1']}, dlog(nm)={c['dlog_nm']}, dlog(T)={c['dlog_T']}")
            print(f"      S={c['stab']}, nm in S? {c['nm_in_stab']}")
            print(f"      -1 in D_A? {c['neg1_in_D']}, T in D_A? {c['T_in_D']}")
            # Check: is T in -1's coset?
            print(f"      T coset={c['T_coset']}, -1 coset={c['neg1_coset']}, same? {c['T_coset']==c['neg1_coset']}")
    
    # The clean coset obstruction cases
    print(f"\n{'='*60}")
    print(f"CLEAN COSET OBSTRUCTION (-1 in D_A, nm not in S, T in uncovered coset)")
    print(f"{'='*60}")
    
    clean_coset = [c for c in neg1_yes if not c['nm_in_stab']]
    print(f"Count: {len(clean_coset)}")
    
    # Verify T coset is uncovered
    t_uncovered = sum(1 for c in clean_coset if c['T_coset'] in c['uncovered_cosets'])
    print(f"T in uncovered coset: {t_uncovered}/{len(clean_coset)}")
    
    # Verify T coset != -1 coset
    t_neq_neg1 = sum(1 for c in clean_coset if c['T_coset'] != c['neg1_coset'])
    print(f"T coset != -1 coset: {t_neq_neg1}/{len(clean_coset)}")
    
    # How many uncovered cosets?
    unc_dist = Counter(len(c['uncovered_cosets']) for c in clean_coset)
    print(f"Uncovered cosets distribution: {dict(unc_dist)}")
    
    # Stab sizes
    stab_dist = Counter(c['stab_size'] for c in clean_coset)
    print(f"Stab size: {dict(stab_dist)}")
    
    # A values
    A_dist = Counter(c['A'] for c in clean_coset)
    print(f"A values: {dict(sorted(A_dist.items()))}")
    
    # h values
    h_dist = Counter(c['h'] for c in clean_coset)
    print(f"h values: {dict(sorted(h_dist.items()))}")
    
    # Rescue for clean coset cases
    print(f"\n  Rescue analysis for clean coset cases:")
    rescue_A = Counter()
    rescue_h = Counter()
    for c in clean_coset:
        n = c['n']
        for A2 in COVERING_A:
            if A2 == c['A'] or gcd(n, A2) > 1: continue
            info2 = compute_full_analysis(n, A2)
            if info2 and info2['T_in_D']:
                rescue_A[A2] += 1
                rescue_h[info2['h']] += 1
                break
    
    print(f"  Rescue A: {dict(sorted(rescue_A.items()))}")
    print(f"  Rescue h: {dict(sorted(rescue_h.items()))}")
    
    # Save full case data
    output = {
        'total_nontrivial_gap': len(cases),
        'neg1_in_D': neg1_in_D_count,
        'neg1_not_in_D': neg1_not_in_D_count,
        'clean_coset_obstruction': len(clean_coset),
        'nm_in_S_anomalous': len(nm_in_S),
        'type_B_count': len(type_B),
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/quotient_revised_analysis.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to quotient_revised_analysis.json")

if __name__ == '__main__':
    main()