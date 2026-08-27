#!/usr/bin/env python3
"""
Theorem 3 Forward Direction (⟸) — Analytic Proof Attempt
=========================================================

Goal: Prove that for prime n ≡ 1 (mod 12), n ≢ 0 (mod 5), and prime A ≡ 3 (mod 4),
if some prime factor p of nx is a QNR mod A, then T ∈ D_A((nx)²).

Equivalently: −1 ∈ H(A) ⟹ T = −1·nm ∈ D_A.

Current state:
- Proven for h=2 (single QNR), order-2 QNR, and Kneser with trivial stabilizer
- Fails in 821/10,917 cases (single-A argument)
- Covering set {3,7,11,19,23,31} rescues all failures (computational)

Strategy: Find analytic arguments to reduce/eliminate computational dependence.

Key questions:
1. Can we prove the covering set property analytically?
2. Can we extend the Kneser argument to cover more cases?
3. Can we prove the parity obstruction never persists across all 6 prime A values?
4. Can the sieve argument (Theorem 14) be made rigorous for the constant bound?
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, mod_inverse, legendre_symbol
from collections import defaultdict, Counter
from math import lcm, log
from itertools import product as iterproduct

PRIME_A = [3, 7, 11, 19, 23, 31]

def find_primitive_root(p):
    if p == 2: return 1
    phi = p - 1
    factors = factorint(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    return None

def multiplicative_order(a, n):
    if gcd(a, n) > 1: return None
    val = a % n
    for i in range(1, n):
        if val == 1: return i
        val = (val * a) % n
    return None

def discrete_log_mod(g, target, p, max_iter=None):
    """Find k such that g^k ≡ target (mod p)."""
    if max_iter is None:
        max_iter = p
    val = 1
    for i in range(max_iter):
        if val == target % p: return i
        val = (val * g) % p
    return None

def compute_H_and_D(n, A):
    """Compute H(A), D_A, and related structures for given n, A."""
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
    for o in orders:
        h = lcm(h, o)
    if h <= 1: return None
    
    # Compute dlog values mod h
    step = (A - 1) // h
    s_values = {}
    for p, e in prime_factors:
        dlg = discrete_log_mod(g, p, A)
        if dlg is None: return None
        s_values[p] = (dlg * 1) % h  # dlog of p in Z/hZ
    
    # Target T = -1 * nm mod A
    # dlog(T) = h/2 + sum(e_i * s_i) mod h
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    dlog_neg1 = h // 2
    
    # Compute D_A: all products of p_i^a_i mod h where 0 <= a_i <= 2*e_i
    # D_A = { sum(a_i * s_i) mod h : 0 <= a_i <= 2*e_i }
    dlog_set = set()
    ranges = [range(0, 2*e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    
    for combo in iterproduct(*ranges):
        val = sum(a * s for a, s in zip(combo, s_list)) % h
        dlog_set.add(val)
    
    # Stabilizer of D_A in Z/hZ
    stab = set()
    for s in range(h):
        if all((d + s) % h in dlog_set for d in dlog_set):
            stab.add(s)
    
    # Check membership
    neg1_in_D = dlog_neg1 in dlog_set
    T_in_D = dlog_T in dlog_set
    neg1_in_H = (h % 2 == 0)  # -1 is always in H when h is even
    
    return {
        'n': n, 'A': A, 'h': h, 'stab_size': len(stab),
        'prime_factors': [(p, e) for p, e in prime_factors],
        's_values': s_values,
        'dlog_nm': dlog_nm,
        'dlog_T': dlog_T,
        'dlog_neg1': dlog_neg1,
        'neg1_in_D': neg1_in_D,
        'T_in_D': T_in_D,
        'D_size': len(dlog_set),
        'h_even': h % 2 == 0,
        'dlog_set': sorted(dlog_set),
    }

def analyze_gap_structure(max_n=10000):
    """Analyze gap structure across all prime A values for primes up to max_n."""
    results = {
        'total_primes': 0,
        'gaps_by_A': {A: 0 for A in PRIME_A},
        'gaps_by_h': defaultdict(list),
        'simultaneous_gaps': [],
        'parity_obstruction': 0,
        'coset_obstruction': 0,
        'rescue_pairs': [],
        'unrescued': [],
    }
    
    n = 13
    while n <= max_n:
        if not isprime(n) or n % 12 != 1 or n % 5 == 0:
            n = int(nextprime(n))
            continue
        
        results['total_primes'] += 1
        
        # Check all prime A values
        gap_A = []
        for A in PRIME_A:
            if gcd(n, A) > 1:
                continue
            info = compute_H_and_D(n, A)
            if info is None:
                continue
            if info['h_even'] and not info['T_in_D']:
                gap_A.append((A, info))
        
        if gap_A:
            results['simultaneous_gaps'].append({
                'n': n,
                'gap_count': len(gap_A),
                'gap_A_values': [a for a, _ in gap_A],
                'h_values': [info['h'] for _, info in gap_A],
                'stab_sizes': [info['stab_size'] for _, info in gap_A],
            })
            
            # Check rescue: which A values succeed?
            success_A = []
            for A in PRIME_A:
                if gcd(n, A) > 1:
                    continue
                info = compute_H_and_D(n, A)
                if info and info['T_in_D']:
                    success_A.append(A)
            
            if not success_A:
                results['unrescued'].append(n)
            else:
                results['rescue_pairs'].append({
                    'n': n,
                    'gap_A': [a for a, _ in gap_A],
                    'success_A': success_A,
                })
        
        n = int(nextprime(n))
    
    return results

def analyze_kneser_extension():
    """
    The Kneser argument works when:
    - h = 2m, m odd > 1
    - Stabilizer is trivial
    - Sum(2*e_i + 1) >= m + k - 1
    
    The 929 proven cases use this. The remaining cases fail because:
    1. Non-trivial stabilizer (but S' = Z/m computationally)
    2. Sum(2*e_i + 1) < m + k - 1 (too few primes / too small exponents)
    
    Can we extend Kneser to cover more cases analytically?
    
    Key insight: Kneser gives |S'| >= sum|A_i| - (k-1)|H|.
    If H is trivial and sum|A_i| >= m, then S' = Z/m.
    
    When sum|A_i| < m, we need a different argument.
    But: the A_i are arithmetic progressions in Z/m with step s_i.
    Their sizes are 2*e_i + 1.
    
    Question: when does a union of APs cover Z/m even though
    the Kneser bound doesn't guarantee it?
    
    This happens because Kneser is a LOWER bound — the actual
    sumset can be larger. The question is whether we can prove
    it's always Z/m under weaker conditions.
    """
    pass  # Analysis only

def analyze_parity_persistence():
    """
    Theorem 10 proves dlog(T) is always odd in trivial-stab gap cases.
    
    Key question: can the parity obstruction persist across ALL 6 prime A values?
    
    For each A, the group order h_A depends on n. Different A values give
    different h values. The parity obstruction requires:
    1. h_A is even (so -1 ∈ H(A))
    2. h_A/2 is odd (so dlog(T) is odd)
    3. The specific odd position h_A/2 + dlog(nm) is a hole in D_A
    
    For the obstruction to persist across ALL 6 primes:
    - All 6 must have even h
    - All 6 must have the target at an odd position that's a hole
    
    Theorem 11 says max |H_gap| = 4. Can we prove this analytically?
    
    The 6 prime A values give group orders:
    A=3: h ∈ {1, 2} (very small)
    A=7: h ∈ {1, 2, 3, 6}
    A=11: h ∈ {1, 2, 5, 10}
    A=19: h ∈ {1, 2, 3, 6, 9, 18}
    A=23: h ∈ {1, 2, 11, 22}
    A=31: h ∈ {1, 2, 3, 5, 6, 10, 15, 30}
    
    For A=3: h is at most 2. When h=2, the single QNR case always works.
    So A=3 NEVER has a gap when h=2.
    
    The only way A=3 can have a gap is when h=1 (all QR), which means
    A=3 doesn't help but also doesn't have a gap — it's just irrelevant.
    
    Wait — actually when h=1, -1 ∉ H(A) (since H(A) = {1}), so the
    forward direction's hypothesis isn't met. No gap, just inapplicable.
    
    So A=3 can never have a gap (it either works at h=2 or is inapplicable).
    
    This means at most 5 of 6 primes can have gaps.
    Can we prove at most 4 (Theorem 11)?
    """
    # The h values available for each A:
    h_options = {
        3:  [1, 2],           # |ord_3(p)| divisors
        7:  [1, 2, 3, 6],     # |ord_7(p)| divisors  
        11: [1, 2, 5, 10],    # |ord_11(p)| divisors
        19: [1, 2, 3, 6, 9, 18],
        23: [1, 2, 11, 22],
        31: [1, 2, 3, 5, 6, 10, 15, 30],
    }
    
    print("=== Parity Persistence Analysis ===")
    print()
    print("A=3: h ∈ {1, 2}. When h=2, always works (single QNR, exp 1).")
    print("     A=3 can NEVER have a gap. Maximum gaps = 5 of 6 primes.")
    print()
    
    # For A=3 to be inapplicable: all prime factors of nx must be QR mod 3.
    # Since n ≡ 1 mod 12, (n/3) = 1. And m = (n+3)/4.
    # If m has a QNR prime factor mod 3, that gives h=2 and A=3 works.
    # If m is all-QR mod 3, h=1 and A=3 is inapplicable.
    # QNR mod 3 means p ≡ 2 mod 3.
    # So A=3 is inapplicable iff all prime factors of m_3 = (n+3)/4 are ≡ 1 mod 3.
    
    print("A=3 inapplicable when: all prime factors of (n+3)/4 are ≡ 1 mod 3")
    print("This requires (n+3)/4 to be a product of primes ≡ 1 mod 3 only.")
    print("By Dirichlet, primes ≡ 1 mod 3 have density 1/2, so this is rare.")
    print()
    
    # Now: can we prove that at most 4 of {7, 11, 19, 23, 31} can simultaneously gap?
    # The h values for gaps must have h/2 odd, so h ≡ 2 mod 4:
    # A=7:  h=6  (h/2=3, odd ✓) or h=2 (h/2=1, but h=2 always works)
    # A=11: h=10 (h/2=5, odd ✓) or h=2 (always works)
    # A=19: h=18 (h/2=9, odd ✓) or h=6 (h/2=3, odd ✓)
    # A=23: h=22 (h/2=11, odd ✓) or h=2 (always works)
    # A=31: h=30 (h/2=15, odd ✓) or h=10 (h/2=5, odd ✓) or h=6 (h/2=3, odd ✓)
    
    print("h values where parity obstruction is possible (h/2 odd, h > 2):")
    parity_h = {
        7:  [6],
        11: [10],
        19: [6, 18],
        23: [22],
        31: [6, 10, 30],
    }
    for A, hs in parity_h.items():
        print(f"  A={A}: h ∈ {hs}")
    
    print()
    print("Total distinct h values for parity obstruction: {6, 10, 18, 22, 30}")
    print("These are 5 distinct group orders.")
    print()
    print("Key question: can a single prime n produce parity gaps at all 5 h values simultaneously?")
    print()
    
    # The h value for each A is determined by the orders of prime factors of nx mod A.
    # Different A values see different quadratic character → different orders → different h.
    # But: if n is QR mod all small primes, then h=1 for all A (all-QR), and no gaps at all.
    # The gaps require specific QNR structure.
    
    # Can we use the pigeonhole principle?
    # 5 distinct h values, 5 prime A values (excluding A=3).
    # Theorem 11 says max 4 simultaneous gaps.
    # Can we prove this from the structure of h values?
    
    # A=7: h=6 requires ord_7(p)=6 or ord_7(p)=3 for some p|nx
    #   h=6 means Z/6 structure. h/2=3 (odd). Parity gap needs D_A to miss position 3+something.
    # A=19: h=6 requires ord_19(p)=6 or 3 for some p|nx
    #   If A=7 has h=6, that means some p|nx has ord_7(p) ∈ {3,6}.
    #   Does this constrain ord_19(p)?
    
    # The orders mod different primes are INDEPENDENT by CRT (for different A).
    # So in principle, all 5 could gap simultaneously.
    # But Theorem 11 says it never happens (computationally, max=4).
    
    # The question is: is there an analytic reason, or is it just computational coincidence?
    
    return parity_h

def analyze_covering_set_analytic():
    """
    Can we prove the covering set property analytically?
    
    The covering set {3, 7, 11, 19, 23, 31} works because:
    1. A=3: Always works when h=2 (proven). Inapplicable when h=1.
    2. A=7: Works when h=2 (proven) or h=6 with Kneser (proven when stab trivial).
    3. A=11: Works when h=2 (proven) or h=10 with Kneser (proven when stab trivial).
    4. A=19: Works when h=2,6 (proven/Kneser). h=18 may fail.
    5. A=23: Works when h=2 (proven) or h=22 with Kneser (proven when stab trivial).
    6. A=31: Works when h=2,10 (proven/Kneser). h=6,30 may fail.
    
    The hard cases are:
    - h=18 at A=19 (382 failures)
    - h=30 at A=31 (266 failures)
    - h=6 at A=7 (91 failures)
    - h=10 at A=11 (51 failures)
    - h=22 at A=23 (21 failures)
    - h=6 at A=31 (contributes to some failures)
    
    But A=3 catches everything when h=2, and h=2 means a single QNR factor.
    
    The key structural fact: if ALL of {7,11,19,23,31} have h > 2 (i.e., no single
    QNR factor for any of them), that means every prime factor of nx is QR mod ALL
    six primes. By QR reciprocity, this constrains n heavily.
    
    Can we prove that if n is QR mod all of {3,7,11,19,23,31}, then n must be
    in a specific residue class, and in that class, some other argument works?
    """
    print("=== Covering Set Analytic Analysis ===")
    print()
    
    # If n ≡ 1 mod 12 and (n/p) = 1 for all p in {3,7,11,19,23,31}:
    # (3/n) = 1 since n ≡ 1 mod 12 (always true)
    # What residue classes does this constrain n to?
    
    # By QR reciprocity for n ≡ 1 mod 4:
    # (p/n) = (n/p) for all p ≡ 1 mod 4
    # (p/n) = (n/p) * (-1)^((p-1)/2 * (n-1)/2) for p ≡ 3 mod 4
    # Since n ≡ 1 mod 4, (n-1)/2 is even, so (-1)^... = 1.
    # So (p/n) = (n/p) for ALL primes p when n ≡ 1 mod 4.
    
    # This means: if n is QR mod all of {3,7,11,19,23,31}, then
    # all of {3,7,11,19,23,31} are QR mod n.
    
    # By the covering set analysis, when (7/n) = -1, A=7 works directly.
    # When (7/n) = 1, we need the m-route.
    
    # If n is QR mod all 6 primes, then the direct route fails for all 6.
    # The m-route requires a QNR prime factor of m_A.
    
    # The sieve argument (Theorem 14) shows this has density 0.
    # But can we prove it FINITE? That's the constant bound conjecture.
    
    print("If n is QR mod all of {3,7,11,19,23,31}:")
    print("  → All 6 primes are QR mod n (by QR reciprocity, n ≡ 1 mod 4)")
    print("  → Direct route fails for all 6")
    print("  → m-route needed: need QNR prime factor of some m_A")
    print()
    print("The sieve argument (Thm 14) shows density-0 of such n.")
    print("But constant bound C=31 is only computationally verified.")
    print()
    print("Alternative: Can we prove that for n QR mod all 6 primes,")
    print("the m-route MUST work for at least one A, using coprimality?")
    
    # The m_A values are:
    # m_3 = (n+3)/4
    # m_7 = (n+7)/4
    # m_11 = (n+11)/4
    # m_19 = (n+19)/4
    # m_23 = (n+23)/4
    # m_31 = (n+31)/4
    
    # Key: gcd(m_3, m_7/2) = 1 (proven, §5.1)
    # Can we extend this to more pairs?
    
    # m_3 = (n+3)/4, m_7 = (n+7)/4
    # gcd(m_3, m_7) = gcd((n+3)/4, (n+7)/4) = gcd((n+3)/4, 1) = 1
    # Wait: (n+7)/4 - (n+3)/4 = 1. So gcd(m_3, m_7) = 1!
    
    # Actually: m_7 = (n+7)/4 and m_7/2 = (n+7)/8 (when n ≡ 1 mod 8)
    # gcd(m_3, m_7/2) = gcd((n+3)/4, (n+7)/8)
    # (n+3)/4 - 2*(n+7)/8 = (n+3)/4 - (n+7)/4 = -4/4 = -1
    # So gcd = 1. ✓
    
    # More generally: gcd(m_A, m_B) for A ≠ B?
    # m_A - m_B = (A - B)/4
    # So gcd(m_A, m_B) | (A-B)/4
    
    # For prime A, B with A ≠ B:
    # gcd(m_A, m_B) divides (A-B)/4
    
    # A=3, B=7: gcd | 1 → gcd = 1
    # A=3, B=11: gcd | 2 → gcd ∈ {1, 2}
    # A=3, B=19: gcd | 4 → gcd ∈ {1, 2, 4}
    # A=7, B=11: gcd | 1 → gcd = 1
    # A=7, B=19: gcd | 3 → gcd ∈ {1, 3}
    # A=11, B=19: gcd | 2 → gcd ∈ {1, 2}
    # etc.
    
    print()
    print("=== Coprimality Structure ===")
    for i, A in enumerate(PRIME_A):
        for B in PRIME_A[i+1:]:
            diff = abs(A - B) // 4
            print(f"  gcd(m_{A}, m_{B}) divides {diff}", end="")
            if diff == 1:
                print(" → ALWAYS coprime ✓")
            else:
                print(f" → may share factor of {diff}")
    
    print()
    print("Key: m_3 and m_7 are ALWAYS coprime (diff=1)")
    print("     m_7 and m_11 are ALWAYS coprime (diff=1)")
    print()
    print("These coprimalities give independent QNR factor chances.")

def main():
    print("=" * 70)
    print("THEOREM 3 FORWARD DIRECTION — ANALYTIC PROOF ANALYSIS")
    print("=" * 70)
    print()
    
    # 1. Parity persistence analysis
    parity_h = analyze_parity_persistence()
    
    # 2. Covering set analytic structure
    analyze_covering_set_analytic()
    
    # 3. Run gap analysis for small primes
    print()
    print("=" * 70)
    print("COMPUTATIONAL VERIFICATION (small primes)")
    print("=" * 70)
    
    results = analyze_gap_structure(max_n=10000)
    print(f"\nPrimes analyzed: {results['total_primes']}")
    print(f"Primes with at least 1 gap: {len(results['simultaneous_gaps'])}")
    print(f"Max simultaneous gaps: {max(g['gap_count'] for g in results['simultaneous_gaps']) if results['simultaneous_gaps'] else 0}")
    print(f"Unrescued primes: {results['unrescued']}")
    
    if results['simultaneous_gaps']:
        gap_counts = Counter(g['gap_count'] for g in results['simultaneous_gaps'])
        print(f"Gap count distribution: {dict(sorted(gap_counts.items()))}")
    
    # 4. Analyze which h values can co-occur
    print()
    print("=== Co-occurrence of parity-obstructed h values ===")
    if results['simultaneous_gaps']:
        h_cooccur = defaultdict(int)
        for g in results['simultaneous_gaps']:
            h_set = frozenset(g['h_values'])
            h_cooccur[h_set] += 1
        for h_set, count in sorted(h_cooccur.items(), key=lambda x: -x[1])[:10]:
            print(f"  h={set(h_set)}: {count} primes")

if __name__ == "__main__":
    main()