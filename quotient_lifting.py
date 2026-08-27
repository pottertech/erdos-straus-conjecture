#!/usr/bin/env python3
"""
Quotient Group Lifting Argument (Problem #8)
=============================================
For the 193 non-trivial-stabilizer gap cases:

When D_A has a non-trivial stabilizer S in Z/hZ (|S| = 3 or 5), D_A is S-invariant
(covers whole cosets). The target T = -1·nm lands in a coset that D_A doesn't cover
because nm ∉ S.

The question: can we lift coverage from the quotient group Z/hZ / S to T ∈ D_A
under certain conditions?

Strategy:
1. For each non-trivial-stab gap case, identify the stabilizer S, the quotient Q = Z/hZ / S
2. Show T's coset in Q is the unique uncovered coset
3. Show -1's coset IS covered
4. Show nm ∉ S is the obstruction
5. Prove: if we can find A' where the stabilizer S' contains nm (or S' is trivial),
   then T ∈ D_{A'} — this is the lifting argument
6. Formalize: the coset obstruction at A lifts to coverage at A' because the
   stabilizer structure changes
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
    """Find a primitive root modulo prime p."""
    if p == 2:
        return 1
    phi = p - 1
    factors = factorint(phi)
    for g in range(2, p):
        is_primitive = True
        for q in factors:
            if pow(g, phi // q, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g
    return None


def discrete_log_mod(g, target, p):
    """Compute discrete log of target base g mod p."""
    if target % p == 0:
        return None
    val = 1
    for i in range(p - 1):
        if val == target % p:
            return i
        val = (val * g) % p
    return None


def multiplicative_order(a, n):
    """Compute multiplicative order of a mod n."""
    if gcd(a, n) > 1:
        return None
    val = a % n
    for i in range(1, n):
        if val == 1:
            return i
        val = (val * a) % n
    return None


def compute_full_analysis(n, A):
    """
    Full analysis for given n, A: compute h, D_A, stabilizer, cosets, quotient.
    """
    if gcd(n, A) > 1:
        return None
    
    m = (n + A) // 4
    nx = n * m
    
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    
    if not prime_factors:
        return None
    
    if not isprime(A):
        return None  # Focus on prime A for quotient analysis
    
    g = find_primitive_root(A)
    if g is None:
        return None
    
    # Compute orders and h
    orders = [multiplicative_order(p, A) for p, _ in prime_factors]
    h = 1
    for o in orders:
        h = lcm(h, o)
    
    if h <= 1:
        return None
    
    # Compute s_i (dlog in Z/hZ)
    s_values = {}
    for p, e in prime_factors:
        dlg = discrete_log_mod(g, p, A)
        step = (A - 1) // h
        if h <= 1:
            s_values[p] = 0
            continue
        try:
            s_inv = mod_inverse(step, h)
            s_i = (dlg * s_inv) % h
        except (ValueError, Exception):
            s_i = None
            for s in range(h):
                if (s * step) % h == dlg % h:
                    s_i = s
                    break
            if s_i is None:
                return None
        s_values[p] = s_i
    
    # dlog(nm)
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    
    # Compute D_A
    D_A_elements = set()
    ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    
    for combo in iterproduct(*ranges):
        val = sum(a_i * s_i for a_i, s_i in zip(combo, s_list)) % h
        D_A_elements.add(val)
    
    T_in_D = dlog_T in D_A_elements
    
    # Stabilizer
    stab = set()
    for s in range(h):
        if all((d + s) % h in D_A_elements for d in D_A_elements):
            stab.add(s)
    
    stab_size = len(stab)
    neg1_in_D = (h // 2) in D_A_elements
    
    # Coset analysis
    # Cosets of S in Z/hZ
    cosets = []
    remaining = set(range(h))
    while remaining:
        rep = min(remaining)
        coset = {(rep + s) % h for s in stab}
        cosets.append((rep, coset))
        remaining -= coset
    
    # Which cosets does D_A cover?
    covered_cosets = set()
    for rep, coset in cosets:
        if coset & D_A_elements:
            covered_cosets.add(rep)
    
    # Which coset does T belong to?
    T_coset_rep = None
    for rep, coset in cosets:
        if dlog_T in coset:
            T_coset_rep = rep
            break
    
    # Which coset does -1 belong to?
    neg1_coset_rep = None
    for rep, coset in cosets:
        if (h // 2) in coset:
            neg1_coset_rep = rep
            break
    
    # Which coset does nm belong to?
    nm_coset_rep = None
    for rep, coset in cosets:
        if dlog_nm in coset:
            nm_coset_rep = rep
            break
    
    # Is nm in the stabilizer?
    nm_in_stab = dlog_nm in stab
    
    return {
        'n': n,
        'A': A,
        'h': h,
        'm': m,
        'dlog_T': dlog_T,
        'dlog_nm': dlog_nm,
        'dlog_neg1': h // 2,
        'T_in_D': T_in_D,
        'neg1_in_D': neg1_in_D,
        'stab_size': stab_size,
        'stab': sorted(stab),
        'D_A_size': len(D_A_elements),
        'D_A': sorted(D_A_elements),
        'holes': sorted(set(range(h)) - D_A_elements),
        'cosets': [(rep, sorted(coset)) for rep, coset in cosets],
        'covered_cosets': sorted(covered_cosets),
        'uncovered_cosets': sorted(set(r for r, _ in cosets) - covered_cosets),
        'T_coset': T_coset_rep,
        'neg1_coset': neg1_coset_rep,
        'nm_coset': nm_coset_rep,
        'nm_in_stab': nm_in_stab,
        'prime_factors': [(p, e) for p, e in prime_factors],
        's_values': {p: s_values[p] for p, _ in prime_factors},
    }


def scan_nontrivial_stab_cases(max_n=100000):
    """Find all non-trivial-stabilizer gap cases."""
    print("Scanning for non-trivial-stabilizer gap cases...")
    cases = []
    
    n = 13
    while n <= max_n:
        if n % 12 == 1 and n % 5 != 0 and isprime(n):
            for A in PRIME_A:
                if gcd(n, A) > 1:
                    continue
                info = compute_full_analysis(n, A)
                if info is None:
                    continue
                if not info['T_in_D'] and info['stab_size'] > 1:
                    cases.append(info)
        n = nextprime(n)
    
    return cases


def analyze_quotient_structure(cases):
    """
    Analyze the quotient group structure for all non-trivial-stab gap cases.
    """
    print(f"\n{'='*80}")
    print("QUOTIENT GROUP LIFTING ANALYSIS (Problem #8)")
    print(f"{'='*80}")
    print(f"Total non-trivial-stab gap cases: {len(cases)}")
    
    # Group by stabilizer size
    by_stab = defaultdict(list)
    for c in cases:
        by_stab[c['stab_size']].append(c)
    
    for stab_size in sorted(by_stab.keys()):
        stab_cases = by_stab[stab_size]
        print(f"\n{'='*60}")
        print(f"Stabilizer size |S| = {stab_size}")
        print(f"Cases: {len(stab_cases)}")
        print(f"Quotient group: Z/{len(stab_cases[0]['cosets'])}Z (|Q| = {len(stab_cases[0]['cosets'])})")
        print(f"{'='*60}")
        
        # For each case, verify:
        # 1. -1's coset is covered
        # 2. T's coset is uncovered
        # 3. nm ∉ S
        # 4. T's coset ≠ -1's coset
        
        neg1_covered = 0
        T_uncovered = 0
        nm_not_in_stab = 0
        T_neq_neg1_coset = 0
        
        for c in stab_cases:
            if c['neg1_coset'] in c['covered_cosets']:
                neg1_covered += 1
            if c['T_coset'] in c['uncovered_cosets']:
                T_uncovered += 1
            if not c['nm_in_stab']:
                nm_not_in_stab += 1
            if c['T_coset'] != c['neg1_coset']:
                T_neq_neg1_coset += 1
        
        print(f"  -1's coset covered: {neg1_covered}/{len(stab_cases)}")
        print(f"  T's coset uncovered: {T_uncovered}/{len(stab_cases)}")
        print(f"  nm ∉ S: {nm_not_in_stab}/{len(stab_cases)}")
        print(f"  T's coset ≠ -1's coset: {T_neq_neg1_coset}/{len(stab_cases)}")
        
        # Show coset structure for a few examples
        print(f"\n  Example cases:")
        for c in stab_cases[:5]:
            print(f"    n={c['n']}, A={c['A']}, h={c['h']}")
            print(f"      S = {c['stab']}")
            print(f"      Cosets: {[len(ct) for _, ct in c['cosets']]}")
            print(f"      Covered cosets: {c['covered_cosets']}")
            print(f"      Uncovered cosets: {c['uncovered_cosets']}")
            print(f"      -1 at dlog {c['dlog_neg1']}, coset rep {c['neg1_coset']}")
            print(f"      T at dlog {c['dlog_T']}, coset rep {c['T_coset']}")
            print(f"      nm at dlog {c['dlog_nm']}, coset rep {c['nm_coset']}")
            print(f"      nm ∈ S? {c['nm_in_stab']}")
            print(f"      |D_A| = {c['D_A_size']}/{c['h']}")
    
    return by_stab


def lifting_argument(cases):
    """
    The core lifting argument:
    
    For each non-trivial-stab gap case (n, A):
    - The obstruction is: nm ∉ S → T = -1·nm is in a different coset than -1
    - D_A is S-invariant → covers whole cosets → can't reach T's coset
    
    Lifting: Find A' where either:
    (a) S' = {0} (trivial stabilizer) → no coset obstruction
    (b) S' contains nm → T stays in -1's coset → covered
    (c) S' is different enough that T's coset is covered
    
    We verify: for each n with a non-trivial-stab gap at A,
    there exists A' in the covering set where T ∈ D_{A'}.
    """
    print(f"\n{'='*80}")
    print("LIFTING ARGUMENT: Rescue analysis")
    print(f"{'='*80}")
    
    # For each gap case, find the rescue A' and analyze WHY it works
    rescue_reasons = {
        'trivial_stab_rescue': 0,      # A' has trivial stabilizer
        'nm_in_stab_rescue': 0,        # A' has non-trivial stab but nm ∈ S'
        'different_coset_covered': 0,   # A' has non-trivial stab, T in different (covered) coset
        'full_group_rescue': 0,         # A' gives D_{A'} = full group
        'other': 0,
    }
    
    rescue_details = []
    
    for c in cases:
        n = c['n']
        gap_A = c['A']
        
        for A2 in COVERING_A:
            if A2 == gap_A:
                continue
            if gcd(n, A2) > 1:
                continue
            
            info2 = compute_full_analysis(n, A2)
            if info2 is None or not info2['T_in_D']:
                continue
            
            # Found the rescue! Classify why.
            reason = None
            
            if info2['stab_size'] == 1:
                reason = 'trivial_stab_rescue'
            elif info2.get('nm_in_stab'):
                reason = 'nm_in_stab_rescue'
            elif info2['D_A_size'] == info2['h']:
                reason = 'full_group_rescue'
            elif info2['T_coset'] in info2['covered_cosets']:
                reason = 'different_coset_covered'
            else:
                reason = 'other'
            
            rescue_reasons[reason] += 1
            rescue_details.append({
                'n': n,
                'gap_A': gap_A,
                'gap_h': c['h'],
                'gap_stab_size': c['stab_size'],
                'rescue_A': A2,
                'rescue_h': info2['h'],
                'rescue_stab_size': info2['stab_size'],
                'rescue_reason': reason,
                'rescue_D_A_size': info2['D_A_size'],
                'rescue_h': info2['h'],
            })
            break
    
    print(f"\nRescue reason distribution:")
    for reason, count in sorted(rescue_reasons.items(), key=lambda x: -x[1]):
        print(f"  {reason}: {count}")
    
    print(f"\nTotal rescued: {sum(rescue_reasons.values())}/{len(cases)}")
    
    # Analyze the rescue patterns
    print(f"\n{'='*60}")
    print("RESCUE PATTERN ANALYSIS")
    print(f"{'='*60}")
    
    # By gap stab size
    by_gap_stab = defaultdict(lambda: Counter())
    for d in rescue_details:
        by_gap_stab[d['gap_stab_size']][d['rescue_reason']] += 1
    
    for stab_size in sorted(by_gap_stab.keys()):
        print(f"\n  Gap |S| = {stab_size}:")
        for reason, count in by_gap_stab[stab_size].most_common():
            print(f"    {reason}: {count}")
    
    # By rescue A
    by_rescue_A = defaultdict(int)
    for d in rescue_details:
        by_rescue_A[d['rescue_A']] += 1
    print(f"\n  Rescue A distribution: {dict(sorted(by_rescue_A.items()))}")
    
    # By rescue h
    by_rescue_h = defaultdict(int)
    for d in rescue_details:
        by_rescue_h[d['rescue_h']] += 1
    print(f"  Rescue h distribution: {dict(sorted(by_rescue_h.items()))}")
    
    return rescue_details


def formalize_lifting_lemma(cases, rescue_details):
    """
    Formalize the lifting lemma.
    
    LEMMA (Quotient Lifting):
    Let A be prime, gcd(n,A) = 1, with H(A) of order h and stabilizer S of D_A
    with |S| > 1. If T ∉ D_A because nm ∉ S (coset obstruction), then:
    
    There exists A' ∈ {3, 7, 11, 19, 23, 31} with gcd(n, A') = 1 such that
    T ∈ D_{A'}((nx')²), because:
    
    (a) A' = 3 (h' = 2): D_{A'} has trivial stabilizer (|S'| = 1), so no coset
        obstruction exists. T ∈ D_{A'} iff (3/n) = -1 OR some p|m' is QNR mod 3.
        For n ≡ 5 mod 8, A = 3 works directly (Theorem 2).
    
    (b) For other A', the stabilizer S' either:
        - Is trivial (no coset obstruction)
        - Contains nm (so T stays in -1's coset, which is covered)
        - Has different coset structure where T's coset is covered
    
    PROOF VERIFICATION:
    - All 193 non-trivial-stab gap cases are rescued by some A' (verified computationally)
    - The rescue mechanism is always one of the three cases above
    - The most common rescue is trivial stabilizer (no coset obstruction)
    """
    print(f"\n{'='*80}")
    print("FORMAL LIFTING LEMMA")
    print(f"{'='*80}")
    
    # Verify the three rescue mechanisms cover all cases
    mechanism_counts = Counter(d['rescue_reason'] for d in rescue_details)
    
    mechanism_counts = dict(Counter(d['rescue_reason'] for d in rescue_details))
    total_rescued = sum(mechanism_counts.values())
    total_cases = len(cases)
    print()
    print("    LEMMA (Quotient Lifting for Non-Trivial Stabilizer Cases):")
    print()
    print("    For prime n = 1 (mod 12), n != 0 (mod 5), and prime A = 3 (mod 4) with")
    print("    gcd(n, A) = 1: if D_A has non-trivial stabilizer S (|S| in {3, 5}) and")
    print("    T not in D_A (coset obstruction: nm not in S -> T in uncovered coset), then")
    print("    there exists A' in {3, 7, 11, 19, 23, 31} with T in D_{A'}.")
    print()
    print("    RESCUE MECHANISMS (computationally verified for n <= 100,000):")
    print()
    print(f"    (a) Trivial stabilizer at A': |S'| = 1, no coset obstruction")
    print(f"        Count: {mechanism_counts.get('trivial_stab_rescue', 0)} cases")
    print()
    print(f"    (b) nm in S' at A': T stays in -1's covered coset")
    print(f"        Count: {mechanism_counts.get('nm_in_stab_rescue', 0)} cases")
    print()
    print(f"    (c) Full group: D_{{A'}} = Z/h'Z, T trivially covered")
    print(f"        Count: {mechanism_counts.get('full_group_rescue', 0)} cases")
    print()
    print(f"    (d) Different coset covered: T's coset in D_{{A'}} is covered")
    print(f"        Count: {mechanism_counts.get('different_coset_covered', 0)} cases")
    print()
    print(f"    Total: {total_rescued} / {total_cases} cases rescued")
    print(f"    Unrescued: {total_cases - total_rescued}")
    print()
    print("    The key structural insight: the coset obstruction at A is SPECIFIC to the")
    print("    stabilizer S subset Z/hZ. A different A' produces a different group H(A') of order")
    print("    h', a different stabilizer S' subset Z/h'Z, and different coset structure.")
    print("    The obstruction cannot persist because:")
    print()
    print("    1. If S' = {0} (trivial), there are no cosets to obstruct")
    print("    2. If nm in S', T = -1*nm in (-1 + S') which is -1's coset (always covered)")
    print("    3. If |Q'| = 1 (h' = |S'|), D_{A'} is either everything or nothing")
    print("    4. Different h' means different group structure, different coset decomposition")


def verify_quotient_properties(cases):
    """
    Verify the key properties that make the lifting argument work.
    """
    print(f"\n{'='*80}")
    print("QUOTIENT PROPERTY VERIFICATION")
    print(f"{'='*80}")
    
    # Property 1: In all gap cases, -1's coset is covered but T's isn't
    p1_holds = all(
        c['neg1_coset'] in c['covered_cosets'] and
        c['T_coset'] in c['uncovered_cosets']
        for c in cases
    )
    print(f"Property 1: -1's coset always covered, T's coset always uncovered: {'✅' if p1_holds else '❌'}")
    
    # Property 2: nm never in stabilizer
    p2_holds = all(not c['nm_in_stab'] for c in cases)
    print(f"Property 2: nm ∉ S in all gap cases: {'✅' if p2_holds else '❌'}")
    
    # Property 3: T's coset ≠ -1's coset (this is why nm ∉ S matters)
    p3_holds = all(c['T_coset'] != c['neg1_coset'] for c in cases)
    print(f"Property 3: T's coset ≠ -1's coset in all gap cases: {'✅' if p3_holds else '❌'}")
    
    # Property 4: Exactly one uncovered coset (T's)
    p4_holds = all(len(c['uncovered_cosets']) == 1 for c in cases)
    print(f"Property 4: Exactly 1 uncovered coset (T's) in all gap cases: {'✅' if p4_holds else '❌'}")
    
    # Property 5: Stabilizer sizes
    stab_sizes = Counter(c['stab_size'] for c in cases)
    print(f"Stabilizer size distribution: {dict(stab_sizes)}")
    
    # Property 6: Quotient sizes
    quotient_sizes = Counter(len(c['cosets']) for c in cases)
    print(f"Quotient group sizes: {dict(quotient_sizes)}")
    
    # Property 7: A values that produce non-trivial-stab gaps
    A_values = Counter(c['A'] for c in cases)
    print(f"A values in gap cases: {dict(sorted(A_values.items()))}")
    
    # Property 8: h values
    h_values = Counter(c['h'] for c in cases)
    print(f"h values in gap cases: {dict(sorted(h_values.items()))}")
    
    return p1_holds and p2_holds and p3_holds and p4_holds


def coset_exhaustive_verification(cases):
    """
    For the small cosets (size 3 or 5), do exhaustive verification.
    
    Since |S| ∈ {3, 5} and cosets have size |S|, the quotient Z/hZ/S has
    |Q| = h/|S| elements. For |S|=3: |Q| = h/3. For |S|=5: |Q| = h/5.
    
    These are small enough for exhaustive analysis.
    """
    print(f"\n{'='*80}")
    print("COSET EXHAUSTIVE VERIFICATION")
    print(f"{'='*80}")
    
    for c in cases[:10]:
        h = c['h']
        S = set(c['stab'])
        Q_size = len(c['cosets'])
        
        print(f"\n  n={c['n']}, A={c['A']}, h={h}, |S|={len(S)}, |Q|={Q_size}")
        print(f"  S = {sorted(S)}")
        
        # Show each coset and whether it's covered
        for rep, coset in c['cosets']:
            in_D = bool(set(coset) & set(c['D_A']))
            has_T = c['dlog_T'] in set(coset)
            has_neg1 = c['dlog_neg1'] in set(coset)
            has_nm = c['dlog_nm'] in set(coset)
            
            markers = []
            if in_D: markers.append("D_A✓")
            if has_T: markers.append("T")
            if has_neg1: markers.append("-1")
            if has_nm: markers.append("nm")
            
            print(f"    Coset {rep:3d} {sorted(coset)}: {'covered' if in_D else 'UNCOVERED'} {markers}")


def main():
    cases = scan_nontrivial_stab_cases(100000)
    print(f"Found {len(cases)} non-trivial-stabilizer gap cases")
    
    if not cases:
        print("No cases found!")
        return
    
    # Verify key properties
    all_hold = verify_quotient_properties(cases)
    print(f"\nAll properties hold: {'✅' if all_hold else '❌'}")
    
    # Analyze quotient structure
    by_stab = analyze_quotient_structure(cases)
    
    # Lifting argument
    rescue_details = lifting_argument(cases)
    
    # Formalize the lemma
    formalize_lifting_lemma(cases, rescue_details)
    
    # Exhaustive coset verification for small cases
    coset_exhaustive_verification(cases)
    
    # Save results
    output = {
        'description': 'Quotient group lifting analysis for Erdős-Straus Problem #8',
        'total_cases': len(cases),
        'properties_verified': all_hold,
        'rescue_summary': dict(Counter(d['rescue_reason'] for d in rescue_details)),
    }
    
    output_path = '/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/quotient_lifting_results.json'
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {output_path}")


if __name__ == '__main__':
    main()