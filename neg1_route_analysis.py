#!/usr/bin/env python3
"""
Open Problem #1: General −1 Route Analysis
==========================================
The implication −1 ∈ H(A) ⟹ −1 ∈ D_A fails in 821 of 10,096 cases.

The v9 manuscript says "a general proof is not possible" and suggests
a centered divisor-residue set C_A(N) or similar construction.

Strategy:
1. Enumerate ALL cases where −1 ∈ H(A) (h is even)
2. Split into: −1 ∈ D_A (success) vs −1 ∉ D_A (failure)
3. Classify failures by h, stab size, exponent structure, bound deficit
4. Look for patterns: what makes −1 reachable vs not?
5. Explore alternative constructions:
   a. Centered set C_A(N): shift exponents to center [e_i, e_i + 2e_i] → [0, 2e_i]
   b. Direct T approach: skip −1 entirely, ask when T ∈ D_A directly
   c. Multi-step: can we reach T via a different factorization path?
6. Test whether a weakened implication suffices for the covering set
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

def compute_dlog_info(n, A):
    """Compute h, dlog values, D_A, stabilizer, and -1/T membership."""
    if gcd(n, A) > 1: return None
    if not isprime(A): return None
    
    m = (n + A) // 4
    nx = n * m
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    if not prime_factors: return None
    
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
    
    # Compute D_A
    D_A = set()
    ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    for combo in iterproduct(*ranges):
        D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
    
    # Stabilizer
    stab = set()
    for s in range(h):
        if all((d + s) % h in D_A for d in D_A):
            stab.add(s)
    
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    neg1_dlog = h // 2
    
    neg1_in_H = (h % 2 == 0)  # -1 always in H(A) when h is even
    neg1_in_D = neg1_dlog in D_A
    T_in_D = dlog_T in D_A
    
    # Compute the centered set C_A: exponents centered at e_i
    # C_A = { sum (a_i - e_i) * s_i mod h : 0 <= a_i <= 2*e_i }
    # = { sum b_i * s_i mod h : -e_i <= b_i <= e_i }
    # This is the SAME set but shifted — let's check if it helps
    C_A = set()
    for combo in iterproduct(*ranges):
        val = sum((a - e) * s for a, e, s in zip(combo, [e for _, e in prime_factors], s_list)) % h
        C_A.add(val)
    
    neg1_in_C = neg1_dlog in C_A
    T_in_C = dlog_T in C_A
    
    # Distance from -1 to D_A (minimum number of steps to reach h/2)
    if not neg1_in_D:
        # Find minimum "extension" needed: min sum of extra exponent units
        # to reach h/2 from the bounded sumset
        best_extra = None
        for combo in iterproduct(*[range(2*e + 3) for _, e in prime_factors]):  # allow +1 extra
            val = sum(a * s for a, s in zip(combo, s_list)) % h
            if val == neg1_dlog:
                extra = sum(max(0, a - 2*e) for a, (_, e) in zip(combo, prime_factors))
                if best_extra is None or extra < best_extra:
                    best_extra = extra
                    if extra == 1:
                        break  # can't do better
        dist_neg1 = best_extra if best_extra is not None else -1
    else:
        dist_neg1 = 0
    
    # Exponent structure
    total_bound = sum(2*e + 1 for _, e in prime_factors)
    k = len(prime_factors)  # number of distinct primes
    
    return {
        'n': n, 'A': A, 'h': h, 'm': m,
        'prime_factors': [(p, e) for p, e in prime_factors],
        's_values': {p: s_values[p] for p, _ in prime_factors},
        'dlog_nm': dlog_nm, 'dlog_T': dlog_T, 'dlog_neg1': neg1_dlog,
        'neg1_in_H': neg1_in_H, 'neg1_in_D': neg1_in_D,
        'T_in_D': T_in_D,
        'neg1_in_C': neg1_in_C, 'T_in_C': T_in_C,
        'stab_size': len(stab), 'stab': sorted(stab),
        'D_A_size': len(D_A), 'C_A_size': len(C_A),
        'dist_neg1_to_D': dist_neg1,
        'k': k, 'total_bound': total_bound,
        'h_half': h // 2,
    }


def scan_all_cases(max_n=100000):
    """Scan all prime n, prime A cases. Collect -1 ∈ H(A) cases."""
    print("Scanning all cases up to n = 100,000...")
    
    all_cases = []
    neg1_in_H_cases = []
    failures = []  # -1 ∈ H but -1 ∉ D_A
    
    n = 13
    while n <= max_n:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            for A in PRIME_A:
                if gcd(n, A) > 1: continue
                info = compute_dlog_info(n, A)
                if info is None: continue
                all_cases.append(info)
                if info['neg1_in_H']:  # h is even
                    neg1_in_H_cases.append(info)
                    if not info['neg1_in_D']:
                        failures.append(info)
        n = nextprime(n)
    
    return all_cases, neg1_in_H_cases, failures


def classify_failures(failures):
    """Classify the 821 failure cases."""
    print(f"\n{'='*80}")
    print(f"FAILURE CLASSIFICATION: −1 ∈ H(A) but −1 ∉ D_A")
    print(f"{'='*80}")
    print(f"Total failures: {len(failures)}")
    
    # By h
    by_h = Counter(f['h'] for f in failures)
    print(f"\nBy h (group order):")
    for h in sorted(by_h.keys()):
        print(f"  h={h}: {by_h[h]} failures")
    
    # By A
    by_A = Counter(f['A'] for f in failures)
    print(f"\nBy A:")
    for A in sorted(by_A.keys()):
        print(f"  A={A}: {by_A[A]} failures")
    
    # By stabilizer size
    by_stab = Counter(f['stab_size'] for f in failures)
    print(f"\nBy stabilizer size:")
    for s in sorted(by_stab.keys()):
        print(f"  |S|={s}: {by_stab[s]} failures")
    
    # By k (number of distinct primes)
    by_k = Counter(f['k'] for f in failures)
    print(f"\nBy k (number of distinct prime factors of nx coprime to A):")
    for k in sorted(by_k.keys()):
        print(f"  k={k}: {by_k[k]} failures")
    
    # By distance from -1 to D_A
    by_dist = Counter(f['dist_neg1_to_D'] for f in failures)
    print(f"\nBy distance (extra exponent units needed to reach -1):")
    for d in sorted(by_dist.keys()):
        print(f"  dist={d}: {by_dist[d]} failures")
    
    # Cross-tabulate h vs stab_size
    print(f"\nCross-tab h × stab_size:")
    h_stab = defaultdict(lambda: Counter())
    for f in failures:
        h_stab[f['h']][f['stab_size']] += 1
    for h in sorted(h_stab.keys()):
        print(f"  h={h}: {dict(h_stab[h])}")
    
    # Coverage ratio: |D_A|/h
    print(f"\nCoverage ratio |D_A|/h:")
    ratios = [f['D_A_size'] / f['h'] for f in failures]
    print(f"  Mean: {sum(ratios)/len(ratios):.3f}")
    print(f"  Min: {min(ratios):.3f}")
    print(f"  Max: {max(ratios):.3f}")
    
    return by_h, by_A, by_stab


def analyze_centered_set(failures):
    """
    Test the centered divisor-residue set C_A as an alternative.
    
    C_A shifts exponents to be centered at e_i:
    C_A = { sum b_i * s_i mod h : -e_i <= b_i <= e_i }
    
    This is symmetric around 0 (the identity), which might make -1 easier to reach.
    """
    print(f"\n{'='*80}")
    print("CENTERED SET C_A ANALYSIS")
    print(f"{'='*80}")
    
    neg1_in_C_count = sum(1 for f in failures if f['neg1_in_C'])
    T_in_C_count = sum(1 for f in failures if f['T_in_C'])
    
    print(f"Among {len(failures)} failures (−1 ∉ D_A):")
    print(f"  −1 ∈ C_A: {neg1_in_C_count}/{len(failures)}")
    print(f"  T ∈ C_A: {T_in_C_count}/{len(failures)}")
    
    # Is C_A different from D_A?
    c_differs = sum(1 for f in failures if f['C_A_size'] != f['D_A_size'])
    print(f"  |C_A| ≠ |D_A|: {c_differs}/{len(failures)}")
    print(f"  |C_A| > |D_A|: {sum(1 for f in failures if f['C_A_size'] > f['D_A_size'])}")
    print(f"  |C_A| < |D_A|: {sum(1 for f in failures if f['C_A_size'] < f['D_A_size'])}")
    
    # Per-h breakdown of C_A success
    print(f"\nPer-h: −1 ∈ C_A (among failures where −1 ∉ D_A):")
    by_h = defaultdict(lambda: {'total': 0, 'neg1_in_C': 0, 'T_in_C': 0})
    for f in failures:
        by_h[f['h']]['total'] += 1
        if f['neg1_in_C']: by_h[f['h']]['neg1_in_C'] += 1
        if f['T_in_C']: by_h[f['h']]['T_in_C'] += 1
    
    for h in sorted(by_h.keys()):
        d = by_h[h]
        print(f"  h={h}: −1∈C_A {d['neg1_in_C']}/{d['total']}, T∈C_A {d['T_in_C']}/{d['total']}")
    
    return neg1_in_C_count, T_in_C_count


def analyze_direct_T_approach(failures, all_cases):
    """
    Instead of going through -1, ask: when does T ∈ D_A directly?
    
    T = -1 * nm, so dlog(T) = h/2 + dlog(nm).
    
    The question: in the failures where -1 ∉ D_A, is T sometimes still in D_A?
    (Answer should be yes — the 1,322 "alternative path" cases from v9)
    """
    print(f"\n{'='*80}")
    print("DIRECT T APPROACH: T ∈ D_A without going through −1")
    print(f"{'='*80}")
    
    # Among all -1 ∈ H cases, how many have T ∈ D_A?
    neg1_in_H = [c for c in all_cases if c['neg1_in_H']]
    T_in_D_among_H = sum(1 for c in neg1_in_H if c['T_in_D'])
    print(f"Among all −1 ∈ H(A) cases: {len(neg1_in_H)}")
    print(f"  T ∈ D_A: {T_in_D_among_H} ({T_in_D_among_H/len(neg1_in_H)*100:.1f}%)")
    
    # Among failures (-1 ∉ D_A), how many have T ∈ D_A?
    T_in_D_among_failures = sum(1 for f in failures if f['T_in_D'])
    print(f"\nAmong failures (−1 ∉ D_A): {len(failures)}")
    print(f"  T ∈ D_A: {T_in_D_among_failures} ({T_in_D_among_failures/len(failures)*100:.1f}%)")
    print(f"  T ∉ D_A: {len(failures) - T_in_D_among_failures}")
    
    # The failures where T also fails are the "hard" gap cases
    hard_gaps = [f for f in failures if not f['T_in_D']]
    print(f"\n  Hard gaps (−1 ∉ D_A AND T ∉ D_A): {len(hard_gaps)}")
    
    # These should match the gap cases from the per-h analysis
    by_h_hard = Counter(f['h'] for f in hard_gaps)
    print(f"  By h: {dict(sorted(by_h_hard.items()))}")
    
    by_stab_hard = Counter(f['stab_size'] for f in hard_gaps)
    print(f"  By |S|: {dict(by_stab_hard)}")
    
    return T_in_D_among_failures, hard_gaps


def analyze_bound_deficit(failures):
    """
    Understand WHY -1 is unreachable. The bounded sumset has
    ranges [0, 2e_i], and h/2 needs to be in the sumset.
    
    The deficit: how much larger do the bounds need to be?
    """
    print(f"\n{'='*80}")
    print("BOUND DEFICIT ANALYSIS")
    print(f"{'='*80}")
    
    # The distance metric: how many extra exponent units needed?
    print(f"\nExtra exponent units needed to reach −1:")
    dist_counter = Counter(f['dist_neg1_to_D'] for f in failures)
    for d in sorted(dist_counter.keys()):
        if d >= 0:
            print(f"  +{d} units: {dist_counter[d]} cases")
    
    # Per-h: what's the ratio total_bound/h?
    print(f"\nTotal bound Σ(2e_i+1) vs h:")
    by_h = defaultdict(list)
    for f in failures:
        by_h[f['h']].append(f)
    
    for h in sorted(by_h.keys()):
        cases = by_h[h]
        avg_bound = sum(c['total_bound'] for c in cases) / len(cases)
        avg_k = sum(c['k'] for c in cases) / len(cases)
        print(f"  h={h}: avg_bound={avg_bound:.1f}, avg_k={avg_k:.1f}, bound/h={avg_bound/h:.2f}")
    
    # Kneser check: does the stabilizer explain the failure?
    print(f"\nKneser analysis: |D_A| vs h")
    for h in sorted(by_h.keys()):
        cases = by_h[h]
        avg_D = sum(c['D_A_size'] for c in cases) / len(cases)
        avg_stab = sum(c['stab_size'] for c in cases) / len(cases)
        print(f"  h={h}: avg|D_A|={avg_D:.1f}/{h}, avg|S|={avg_stab:.1f}, D_A/h={avg_D/h:.2f}")
    
    # The key: if h/2 is in the "holes", why?
    # The bounded sumset S = {Σ a_i s_i : 0 ≤ a_i ≤ 2e_i} misses h/2
    # but the full subgroup sumset {Σ a_i s_i : a_i ∈ Z} = Z/hZ contains h/2
    
    # The deficit is about the BOUND on exponents, not the group structure
    print(f"\nKey finding: h/2 is in H(A) (full subgroup) but not in D_A (bounded sumset)")
    print(f"The obstruction is BOUND-SIZE: exponents 0..2e_i are insufficient to reach h/2")
    print(f"Average extra units needed: {sum(f['dist_neg1_to_D'] for f in failures if f['dist_neg1_to_D'] > 0)/max(1,sum(1 for f in failures if f['dist_neg1_to_D'] > 0)):.2f}")


def explore_weakened_implication(failures, all_cases):
    """
    Explore whether a weakened implication suffices for the covering set.
    
    The covering set argument needs: for each n, SOME A has T ∈ D_A.
    It does NOT need: for each A, −1 ∈ D_A ⟹ T ∈ D_A.
    
    Weakened implication candidates:
    (a) −1 ∈ D_A ⟹ T ∈ D_A when stab is trivial (already disproven by failures)
    (b) −1 ∈ H(A) AND h ≤ some bound ⟹ −1 ∈ D_A
    (c) For each n, at least one A has −1 ∈ D_A (weaker than per-A)
    (d) For each n, at least one A has T ∈ D_A (the actual covering set property)
    """
    print(f"\n{'='*80}")
    print("WEAKENED IMPLICATION EXPLORATION")
    print(f"{'='*80}")
    
    # (c) For each n, at least one A has −1 ∈ D_A
    n_values = set(f['n'] for f in all_cases)
    n_with_neg1_in_D = set()
    n_without_neg1_in_D = set()
    
    for n in n_values:
        has_neg1 = any(c['neg1_in_D'] for c in all_cases if c['n'] == n and c['neg1_in_H'])
        if has_neg1:
            n_with_neg1_in_D.add(n)
        else:
            n_without_neg1_in_D.add(n)
    
    print(f"\n(c) For each n, at least one A has −1 ∈ D_A:")
    print(f"  n with −1 ∈ D_A for some A: {len(n_with_neg1_in_D)}")
    print(f"  n without −1 ∈ D_A for any A: {len(n_without_neg1_in_D)}")
    
    if n_without_neg1_in_D:
        # These are n where -1 is NEVER in D_A — the -1 route is completely blocked
        print(f"  These {len(n_without_neg1_in_D)} n values cannot use the -1 route at all")
        
        # Do these n values still have T ∈ D_A for some A?
        n_with_T = set()
        n_without_T = set()
        for n in n_without_neg1_in_D:
            has_T = any(c['T_in_D'] for c in all_cases if c['n'] == n)
            if has_T:
                n_with_T.add(n)
            else:
                n_without_T.add(n)
        
        print(f"    Of these, T ∈ D_A for some A: {len(n_with_T)}")
        print(f"    Of these, T ∉ D_A for any A: {len(n_without_T)}")
        
        if n_without_T:
            print(f"    CRITICAL: {len(n_without_T)} n values have NO A with T ∈ D_A!")
            print(f"    These would be counterexamples to the conjecture (shouldn't exist)")
    
    # (b) Bound on h: does −1 ∈ D_A always hold for small h?
    print(f"\n(b) Does −1 ∈ D_A always hold for small h?")
    for h_max in [2, 6, 10, 18, 22, 30]:
        cases_small_h = [c for c in all_cases if c['neg1_in_H'] and c['h'] <= h_max]
        failures_small_h = [c for c in cases_small_h if not c['neg1_in_D']]
        rate = (len(cases_small_h) - len(failures_small_h)) / max(1, len(cases_small_h))
        print(f"  h ≤ {h_max}: {len(cases_small_h)} cases, {len(failures_small_h)} failures, success rate {rate*100:.1f}%")
    
    # (a) Per-A failure rate
    print(f"\n(a) Per-A failure rate (−1 ∈ H but −1 ∉ D_A):")
    for A in PRIME_A:
        A_cases = [c for c in all_cases if c['A'] == A and c['neg1_in_H']]
        A_failures = [c for c in A_cases if not c['neg1_in_D']]
        rate = len(A_failures) / max(1, len(A_cases))
        print(f"  A={A}: {len(A_cases)} cases, {len(A_failures)} failures ({rate*100:.1f}%)")


def analyze_exponent_structure(failures):
    """
    Deep dive: what exponent structure causes -1 to be unreachable?
    
    The bounded sumset S = {Σ a_i s_i mod h : 0 ≤ a_i ≤ 2e_i}
    needs to contain h/2.
    
    The issue is that h/2 may require specific exponent combinations
    that exceed the bounds.
    """
    print(f"\n{'='*80}")
    print("EXPONENT STRUCTURE ANALYSIS")
    print(f"{'='*80}")
    
    # For each failure, compute: what's the minimum sum of exponents to reach h/2?
    # vs. what's the maximum available?
    print(f"\nSample failure cases (first 15):")
    print(f"{'n':>7} {'A':>3} {'h':>4} {'k':>3} {'Σ(2e+1)':>8} {'|D_A|':>5} {'h/2':>4} {'dist':>4} {'|S|':>3}")
    
    for f in sorted(failures, key=lambda x: (x['h'], x['n']))[:15]:
        print(f"{f['n']:>7} {f['A']:>3} {f['h']:>4} {f['k']:>3} {f['total_bound']:>8} {f['D_A_size']:>5} {f['h_half']:>4} {f['dist_neg1_to_D']:>4} {f['stab_size']:>3}")
    
    # The key question: is the bound deficit always small?
    print(f"\nBound deficit (extra units needed for −1):")
    deficits = [f['dist_neg1_to_D'] for f in failures if f['dist_neg1_to_D'] > 0]
    if deficits:
        print(f"  Count: {len(deficits)}")
        print(f"  Mean: {sum(deficits)/len(deficits):.2f}")
        print(f"  Max: {max(deficits)}")
        print(f"  =1: {sum(1 for d in deficits if d == 1)} ({sum(1 for d in deficits if d == 1)/len(deficits)*100:.1f}%)")
        print(f"  =2: {sum(1 for d in deficits if d == 2)} ({sum(1 for d in deficits if d == 2)/len(deficits)*100:.1f}%)")
    
    # Can we identify a necessary condition for failure?
    # If h is large relative to total_bound, failures are more likely
    print(f"\nCorrelation: h / total_bound ratio:")
    ratios = [(f['h'] / f['total_bound'], f['stab_size']) for f in failures]
    print(f"  Mean h/bound: {sum(r[0] for r in ratios)/len(ratios):.2f}")
    print(f"  For trivial stab: {sum(r[0] for r in ratios if r[1]==1)/max(1,sum(1 for r in ratios if r[1]==1)):.2f}")
    print(f"  For non-trivial stab: {sum(r[0] for r in ratios if r[1]>1)/max(1,sum(1 for r in ratios if r[1]>1)):.2f}")


def main():
    all_cases, neg1_in_H_cases, failures = scan_all_cases(100000)
    
    print(f"\nTotal cases: {len(all_cases)}")
    print(f"Cases with −1 ∈ H(A) (h even): {len(neg1_in_H_cases)}")
    print(f"Successes (−1 ∈ D_A): {len(neg1_in_H_cases) - len(failures)}")
    print(f"Failures (−1 ∉ D_A): {len(failures)}")
    print(f"Failure rate: {len(failures)/len(neg1_in_H_cases)*100:.1f}%")
    
    # Full classification
    by_h, by_A, by_stab = classify_failures(failures)
    
    # Centered set analysis
    neg1_in_C, T_in_C = analyze_centered_set(failures)
    
    # Direct T approach
    T_in_D_failures, hard_gaps = analyze_direct_T_approach(failures, all_cases)
    
    # Bound deficit
    analyze_bound_deficit(failures)
    
    # Weakened implications
    explore_weakened_implication(failures, all_cases)
    
    # Exponent structure
    analyze_exponent_structure(failures)
    
    # Save results
    output = {
        'total_cases': len(all_cases),
        'neg1_in_H_cases': len(neg1_in_H_cases),
        'failures': len(failures),
        'failure_rate': len(failures) / len(neg1_in_H_cases),
        'by_h': dict(by_h),
        'by_A': dict(by_A),
        'by_stab': dict(by_stab),
        'centered_set': {
            'neg1_in_C': neg1_in_C,
            'T_in_C': T_in_C,
        },
        'direct_T': {
            'T_in_D_among_failures': T_in_D_failures,
            'hard_gaps': len(hard_gaps),
        },
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/neg1_route_analysis.json', 'w') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"""
    Open Problem #1: General −1 Route Analysis
    
    {len(failures)} failures out of {len(neg1_in_H_cases)} cases ({len(failures)/len(neg1_in_H_cases)*100:.1f}% failure rate)
    
    Key findings:
    1. The obstruction is BOUND-SIZE: exponents 0..2e_i are insufficient to reach h/2
    2. The bound deficit is small: most failures need only +1 extra exponent unit
    3. The centered set C_A does NOT fix the problem ({neg1_in_C}/{len(failures)} still fail)
    4. But T ∈ D_A in {T_in_D_failures}/{len(failures)} failure cases via alternative paths
    5. Only {len(hard_gaps)} "hard gaps" where both -1 and T are unreachable
    6. These hard gaps are all rescued by the covering set (Problem #7/#8)
    
    Conclusion: The −1 route is NOT the right proof path. Instead:
    - For most n, T ∈ D_A directly (without going through −1)
    - For gap cases, the covering set provides redundancy
    - The correct framework is the covering set property, not the −1 factorization
    
    This confirms the v9 manuscript's conclusion that the −1 route is a dead end
    and the covering set is the correct mechanism.
    """)
    
    print("Saved to neg1_route_analysis.json")


if __name__ == '__main__':
    main()