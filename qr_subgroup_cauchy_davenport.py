#!/usr/bin/env python3
"""
Cauchy-Davenport / Kneser argument for the QR subgroup.

GOAL: Prove that when (n/u) = -1 (QNR case) and ω(x) >= k,
the QR subset of divisors of x² covers EVERY element of the QR subgroup
of (Z/uZ)*, for appropriate k depending on u.

KEY FACTS:
- (Z/uZ)* is cyclic of order u-1 for prime u
- QR subgroup has order (u-1)/2
- When (n/u) = -1: x is QNR, so x has >= 1 QNR prime factor
- QR divisors of x² come from:
  (a) QR prime factors of x: {1, p, p²} all QR
  (b) Pairs of QNR factors: p*q is QR (QNR × QNR = QR)
  (c) p² for any p: always QR
  
- The QR divisors form a subset sum in the QR subgroup
- We need this subset sum to cover all of QR subgroup (or at least T_0, T_2)

CAUCHY-DAVENPORT (for Z/pZ):
  If A, B ⊆ Z/pZ, |A+B| >= min(p, |A|+|B|-1)
  
For our case: the QR subgroup is isomorphic to Z/((u-1)/2)Z (cyclic).
If the QR subgroup order (u-1)/2 is PRIME, Cauchy-Davenport applies directly.

For (u-1)/2 composite: need Kneser's theorem or Chowla's theorem.

STRATEGY:
1. Map the QR divisors to Z/((u-1)/2)Z via discrete log in the QR subgroup
2. Each QR prime factor p of x gives a set {0, d, 2d} in Z/((u-1)/2)Z 
   where d = dlog_QR(p) (dlog within the QR subgroup)
3. Each QNR prime factor pair (p,q) gives QR element with dlog = dlog(p)+dlog(q)
4. The bounded sum set is the sumset of these {0, d, 2d} sets
5. Apply Cauchy-Davenport iteratively: |A + {0,d,2d}| >= min(m, |A|+2)
   where m = (u-1)/2 is the QR subgroup order

For k QR "generators" (each contributing {0, d_i, 2d_i}):
  |S_k| >= min(m, 2k+1) by iterated Cauchy-Davenport

For coverage of the QR subgroup: need 2k+1 >= m = (u-1)/2
  → k >= (u-1)/4 + 1/2 → k >= u/4

For u = 127: k >= 32 → ω(x) >= 32 (!) — way too large
For u = 1000: k >= 250 → impractical

BUT: Cauchy-Davenport gives |A+B| >= |A|+|B|-1, which is the WORST case.
In practice, the sumset grows much faster. And we don't need to cover 
ALL of the QR subgroup — just 2 specific targets (T_0 and T_2).

So the question is: does the QR sumset of k generators of size 3 
intersect {T_0, T_2} for k much smaller than u/4?

Let's compute this empirically.
"""

import sympy
from sympy import isprime, primitive_root, discrete_log, factorint, legendre_symbol
import random
import json
from collections import defaultdict

def get_u_values(max_u=127):
    return [u for u in range(3, max_u+1) if isprime(u) and u % 4 == 3]

def qr_subgroup_order(u):
    """Order of QR subgroup of (Z/uZ)* = (u-1)/2."""
    return (u - 1) // 2

def is_qr_subgroup_prime(u):
    """Check if (u-1)/2 is prime (for Cauchy-Davenport)."""
    m = qr_subgroup_order(u)
    return isprime(m)

def compute_qr_coverage(u, omega_qr, omega_qnr, n_trials=10000):
    """
    For prime u with (n/u) = -1:
    - omega_qr = number of QR prime factors of x
    - omega_qnr = number of QNR prime factors of x (>= 1 by inheritance)
    - Total omega(x) = omega_qr + omega_qnr
    
    QR divisors of x² come from:
    - QR factors: {0, d_i, 2*d_i} in QR dlog space (omega_qr generators)
    - QNR pairs: products of 2 QNR factors → QR elements
      With omega_qnr QNR factors, there are C(omega_qnr, 2) + omega_qnr pairs
      (including p*p = p² which is QR)
      Each pair gives one QR "generator" {0, d_pair, 2*d_pair}? 
      No — each pair gives a SINGLE QR element, not a generator set.
      
    Wait, let me think more carefully.
    
    x has factorization x = p_1^{e_1} * ... * p_k^{e_k}
    x² has factorization x² = p_1^{2*e_1} * ... * p_k^{2*e_k}
    
    Divisors of x² = product of p_i^{a_i} where 0 <= a_i <= 2*e_i.
    
    A divisor d = product p_i^{a_i} is QR iff:
    - The number of QNR primes with ODD exponent in d is even.
    
    So QR divisors are those where an even number of QNR primes have odd exponent.
    
    For a QNR prime p_i with exponent range {0, 1, ..., 2*e_i}:
    - Even exponents (0, 2, ..., 2*e_i) → p_i^{even} is QR → contributes QR factor
    - Odd exponents (1, 3, ..., 2*e_i-1) → p_i^{odd} is QNR → contributes QNR factor
    
    For the divisor to be QR: need even count of QNR primes with odd exponent.
    
    If omega_qnr = 1 (one QNR prime factor q):
    - Even exponent on q: 0, 2, ..., 2*e_q → QR divisors (e_q+1 choices)
    - Odd exponent on q: 1, 3, ..., 2*e_q-1 → QNR divisors (e_q choices)
    - QR divisors: (QR factor choices) × (e_q+1 choices for q's even exponents)
    
    For e_q = 1 (squarefree x): q has exponents {0, 1, 2} in x²
    - QR: q^0 or q^2 (2 choices)
    - QNR: q^1 (1 choice)
    
    So with omega_qr QR factors (each {0, p, p²} = 3 choices) and 1 QNR factor 
    (with 2 QR choices: q^0 or q^2):
    |QR divisors| = 3^{omega_qr} × 2
    
    With omega_qnr = 2 QNR factors q1, q2 (each with 2 QR exponent choices 
    and 1 QNR choice):
    QR divisors: both even (2×2=4) or both odd (1×1=1) = 5 choices for QNR part
    |QR divisors| = 3^{omega_qr} × 5
    
    With omega_qnr QNR factors, each with {even=QR, odd=QNR}:
    QR requires even number of "odd" choices.
    Number of QR combos = sum_{j even} C(omega_qnr, j) × 2^{omega_qnr-j} × 1^j
                        = (3^{omega_qnr} + 1) / 2  [by binomial theorem]
    
    Wait: each QNR factor has:
    - 2 "even" (QR) exponent choices (0 or 2 for e=1)
    - 1 "odd" (QNR) exponent choice (1 for e=1)
    
    Number of QR combos = sum_{j even} C(omega_qnr, j) * 2^{omega_qnr-j} * 1^j
    
    Let a = 2 (even choices), b = 1 (odd choice):
    Sum = (a+b)^{omega_qnr} / 2 + (a-b)^{omega_qnr} / 2
        = (3^{omega_qnr} + 1^{omega_qnr}) / 2
        = (3^{omega_qnr} + 1) / 2
    
    So |QR divisors of x²| = 3^{omega_qr} × (3^{omega_qnr} + 1) / 2
    
    For omega_qr = 0, omega_qnr = 1: |QR| = 1 × 2 = 2
    For omega_qr = 1, omega_qnr = 1: |QR| = 3 × 2 = 6
    For omega_qr = 2, omega_qnr = 1: |QR| = 9 × 2 = 18
    For omega_qr = 3, omega_qnr = 1: |QR| = 27 × 2 = 54
    For omega_qr = 0, omega_qnr = 3: |QR| = 1 × 14 = 14
    For omega_qr = 1, omega_qnr = 2: |QR| = 3 × 5 = 15
    For omega_qr = 2, omega_qnr = 2: |QR| = 9 × 5 = 45
    For omega_qr = 0, omega_qnr = 5: |QR| = 1 × 122 = 122
    For omega_qr = 2, omega_qnr = 3: |QR| = 9 × 14 = 126
    
    And |QR subgroup| = (u-1)/2.
    
    For coverage: need |QR divisors| >= (u-1)/2 (necessary, not sufficient).
    
    |QR divisors| >= (u-1)/2 requires:
    3^{omega_qr} × (3^{omega_qnr}+1)/2 >= (u-1)/2
    
    For omega_qr = 0, omega_qnr = k: (3^k+1)/2 >= (u-1)/2 → 3^k >= u-2
    For u=127: 3^k >= 125 → k >= 5 (omega_qnr >= 5, so omega(x) >= 5)
    For u=1000: 3^k >= 998 → k >= 7 (omega(x) >= 7)
    
    For omega_qr = k, omega_qnr = 1: 3^k × 2 >= (u-1)/2 → 3^k >= (u-1)/4
    For u=127: 3^k >= 31.5 → k >= 4 (omega(x) >= 5)
    For u=1000: 3^k >= 250 → k >= 6 (omega(x) >= 7)
    
    So pigeonhole-wise, omega(x) >= 7 covers u up to ~1000.
    
    But pigeonhole isn't sufficient. Let's check Cauchy-Davenport.
    """
    m = qr_subgroup_order(u)  # QR subgroup order
    
    # The QR divisors form a sumset in Z/mZ
    # Each QR prime factor contributes {0, d_i, 2*d_i} (3 elements)
    # Each QNR prime factor pair contributes... this is more complex.
    
    # For the Cauchy-Davenport argument:
    # If m is prime, then for sets A, B in Z/mZ:
    # |A + B| >= min(m, |A| + |B| - 1)
    
    # Iterated: |S_1 + S_2 + ... + S_k| >= min(m, sum(|S_i|) - k + 1)
    # With each |S_i| = 3: |S| >= min(m, 3k - k + 1) = min(m, 2k+1)
    
    # For coverage: 2k+1 >= m → k >= (m+1)/2 = (u+1)/4
    
    # This is the WORST CASE bound. In practice, coverage is much better.
    
    return {
        'u': u,
        'qr_order': m,
        'qr_order_prime': isprime(m),
        'pigeonhole_omega': None,  # computed below
        'cauchy_davenport_omega': (m + 1) // 2,
    }

# ============ Analysis 1: QR subgroup structure ============
print("="*80)
print("ANALYSIS 1: QR subgroup structure for each u")
print("="*80)

u_values = get_u_values(127)

print(f"\n{'u':>5} | {'(u-1)/2':>8} | {'prime?':>7} | {'CD omega':>9} | {'Pigeon omega':>13} | {'Notes'}")
print("-"*75)

for u in u_values:
    m = qr_subgroup_order(u)
    cd_omega = (m + 1) // 2
    
    # Pigeonhole: 3^{omega_qr} * (3^{omega_qnr}+1)/2 >= m
    # With omega_qnr = 1 (minimum from QNR inheritance):
    # 3^{omega_qr} * 2 >= m → 3^{omega_qr} >= m/2 → omega_qr >= log3(m/2)
    import math
    pig_omega = math.ceil(math.log(m / 2) / math.log(3)) + 1  # +1 for the QNR factor
    
    prime_str = "PRIME" if isprime(m) else "composite"
    print(f"  {u:3d} | {m:8d} | {prime_str:>7} | {cd_omega:9d} | {pig_omega:13d} |")

# ============ Analysis 2: Empirical coverage — does QR sumset cover targets? ============
print(f"\n{'='*80}")
print("ANALYSIS 2: Empirical QR coverage — does the QR sumset hit the targets?")
print("="*80)

def empirical_qr_coverage(u, omega_qr, omega_qnr, n_trials=5000):
    """
    For prime u with QR subgroup of order m = (u-1)/2:
    - Generate random QR/QNR prime factorization of x
    - Compute QR divisors of x² mod u
    - Check if T_0 and T_2 (the QR targets) are covered
    
    Returns: (coverage_prob_T0, coverage_prob_T2, coverage_prob_any)
    """
    if not isprime(u) or u % 4 != 3:
        return None
    
    m = qr_subgroup_order(u)
    g = primitive_root(u)
    
    # g is a primitive root mod u. QR elements have even dlog.
    # QR subgroup generator: g² (has order m)
    g2 = pow(g, 2, u)
    
    # Targets when (n/u) = -1:
    # T_0 = -x (QR), T_2 = -x*n² (QR), T_1 = -x*n (QNR)
    # In QR dlog space: dlog_QR(T) = dlog(T) / 2 mod m
    # But we need specific n to compute targets.
    
    # For the coverage analysis, we check: does the QR divisor set 
    # cover ALL m QR residues? Or at least the 2 target QR residues?
    
    # Since targets depend on n, we check for random n with (n/u) = -1:
    
    qnr_residues = [n for n in range(2, u) if legendre_symbol(n, u) == -1]
    
    if not qnr_residues:
        return None
    
    t0_covered = 0
    t2_covered = 0
    any_covered = 0
    full_coverage = 0  # QR set = entire QR subgroup
    
    for trial in range(n_trials):
        # Random n that is QNR mod u
        n_mod = random.choice(qnr_residues)
        
        # Random factorization: choose omega_qr QR primes and omega_qnr QNR primes
        qr_primes = [p for p in sympy.primerange(2, 10000) if legendre_symbol(p, u) == 1 and p % u != 0]
        qnr_primes = [p for p in sympy.primerange(2, 10000) if legendre_symbol(p, u) == -1 and p % u != 0]
        
        if len(qr_primes) < omega_qr or len(qnr_primes) < omega_qnr:
            return None
        
        chosen_qr = random.sample(qr_primes, omega_qr)
        chosen_qnr = random.sample(qnr_primes, omega_qnr)
        
        # Build x from these factors (just need the factors, not actual x)
        all_factors = list(chosen_qr) + list(chosen_qnr)
        # Exponents all 1 (squarefree x, worst case)
        x_factors = {p: 1 for p in all_factors}
        
        # Compute QR divisors of x² mod u
        # x² has exponents {p: 2 for p in all_factors}
        # Divisors: product p^{a_p} where a_p ∈ {0, 1, 2}
        # QR divisors: those where even number of QNR primes have odd exponent
        
        qr_divisors = set()
        
        # Enumerate all 3^{omega} divisors
        for exponents in itertools.product(range(3), repeat=len(all_factors)):
            d = 1
            is_qr = True
            qnr_odd_count = 0
            
            for i, (p, e) in enumerate(zip(all_factors, exponents)):
                p_mod = p % u
                d = (d * pow(p_mod, e, u)) % u
                
                # Check if this contributes QNR
                if p in chosen_qnr and e % 2 == 1:
                    qnr_odd_count += 1
            
            if qnr_odd_count % 2 == 0:  # QR divisor
                qr_divisors.add(d)
        
        # Compute targets
        inv4 = pow(4, -1, u)
        x_mod = (n_mod * inv4) % u
        
        T0 = (-x_mod) % u  # -x (QR since n is QNR)
        T2 = (-x_mod * pow(n_mod, 2, u)) % u  # -x*n² (QR)
        
        if T0 in qr_divisors:
            t0_covered += 1
        if T2 in qr_divisors:
            t2_covered += 1
        if T0 in qr_divisors or T2 in qr_divisors:
            any_covered += 1
        
        if len(qr_divisors) >= m:
            full_coverage += 1
    
    return {
        't0_coverage': t0_covered / n_trials,
        't2_coverage': t2_covered / n_trials,
        'any_coverage': any_covered / n_trials,
        'full_qr_coverage_prob': full_coverage / n_trials,
    }

import itertools

# Test for small u values
print(f"\n{'u':>5} | {'ω_QR':>4} | {'ω_QNR':>5} | {'ω_total':>7} | {'P(T₀ hit)':>10} | {'P(T₂ hit)':>10} | {'P(any)':>8} | {'P(full QR)':>10}")
print("-"*80)

random.seed(42)

for u in [7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127]:
    if not isprime(u) or u % 4 != 3:
        continue
    
    m = qr_subgroup_order(u)
    
    # Test with increasing omega until we get 100% coverage
    for omega_qnr in [1, 2, 3]:
        for omega_qr in [0, 1, 2, 3, 4, 5]:
            total = omega_qr + omega_qnr
            
            if 3**total > 50000:  # Skip if too many divisors to enumerate
                continue
            
            result = empirical_qr_coverage(u, omega_qr, omega_qnr, n_trials=1000)
            if result is None:
                continue
            
            print(f"  {u:3d} | {omega_qr:4d} | {omega_qnr:5d} | {total:7d} | "
                  f"{result['t0_coverage']:10.4f} | {result['t2_coverage']:10.4f} | "
                  f"{result['any_coverage']:8.4f} | {result['full_qr_coverage_prob']:10.4f}")
            
            if result['any_coverage'] >= 0.999:
                print(f"       → 100% coverage with ω(x) = {total} (ω_QR={omega_qr}, ω_QNR={omega_qnr}) ✓")
                break
        else:
            continue
        break

# ============ Analysis 3: Deterministic check for small u ============
print(f"\n{'='*80}")
print("ANALYSIS 3: Deterministic check — ALL factorizations")
print("="*80)

def deterministic_qr_coverage(u, omega_qr, omega_qnr):
    """
    For prime u, check if for ALL possible QR/QNR prime factorizations 
    of x with omega_qr QR factors and omega_qnr QNR factors, the QR 
    divisors of x² cover ALL QR residues mod u (i.e., the QR sumset 
    = entire QR subgroup).
    
    This is the DETERMINISTIC version: no random sampling.
    
    For small u, we can enumerate all possible dlog vectors.
    """
    if not isprime(u) or u % 4 != 3:
        return None
    
    m = qr_subgroup_order(u)
    g = primitive_root(u)
    
    # QR subgroup: {g^{2k} mod u : k = 0, ..., m-1}
    # Dlog in QR subgroup: element g^{2k} has QR-dlog k
    
    # Each QR prime factor p has QR-dlog = dlog_g(p) / 2 mod m
    # Each QNR prime factor q has dlog_g(q) odd, so can't be directly mapped to QR dlog
    
    # For QR divisors:
    # - QR factors with exponent {0, 1, 2}: dlog_g = {0, 2*d_qr, 4*d_qr} = {0, d_qr, 2*d_qr} in QR dlog
    # - QNR factors: must come in pairs (even count with odd exponent)
    #   Each QNR factor q with exponent e:
    #     e even (0, 2): QR element, dlog = e * dlog_g(q) / 2 mod m
    #     e odd (1): QNR element (not in QR subgroup)
    
    # For a QNR factor with dlog_g(q) = 2*j + 1 (odd):
    #   e=0: contributes 0 to QR dlog
    #   e=2: contributes 2*(2j+1)/2 = 2j+1 to QR dlog... 
    #   Wait, this isn't right. Let me think again.
    
    # dlog_g(p^e) = e * dlog_g(p) mod (u-1)
    # For QR: need dlog_g(p^e) even
    # For QR factor p: dlog_g(p) = 2k → e*2k is always even → always QR
    # For QNR factor q: dlog_g(q) = 2j+1 → e*(2j+1) is even iff e is even
    
    # QR dlog (in Z/mZ): dlog_g(d) / 2 mod m
    
    # QR factor p with dlog_g(p) = 2k:
    #   e=0: dlog_g = 0 → QR dlog = 0
    #   e=1: dlog_g = 2k → QR dlog = k
    #   e=2: dlog_g = 4k → QR dlog = 2k
    # So QR factor contributes {0, k, 2k} in QR dlog space (Z/mZ)
    
    # QNR factor q with dlog_g(q) = 2j+1:
    #   e=0: dlog_g = 0 → QR dlog = 0 (but e=0 means not included)
    #   e=1: dlog_g = 2j+1 → QNR (not in QR)
    #   e=2: dlog_g = 2(2j+1) = 4j+2 → QR dlog = 2j+1 mod m
    # So QNR factor with e=2 contributes {0, 2j+1} in QR dlog (for e ∈ {0, 2})
    
    # For QR divisors: QNR factors must have even total odd exponent count.
    # With 1 QNR factor: e ∈ {0, 2} (even) → 2 choices: {0, 2j+1}
    # With 2 QNR factors: (e1,e2) ∈ {(0,0), (0,2), (2,0), (2,2)} (all even)
    #   OR (e1,e2) ∈ {(1,1)} (both odd → even count → QR)
    #   e1=1,e2=1: dlog = (2j1+1) + (2j2+1) = 2(j1+j2+1) → QR dlog = j1+j2+1 mod m
    # So with 2 QNR factors, QR contributions: {0, 2j1+1, 2j2+1, j1+j2+1} 
    #   Wait, that's not right either. Let me be more careful.
    
    # With 2 QNR factors q1, q2 (dlogs 2j1+1, 2j2+1):
    # QR divisors from QNR part (even number of odd exponents):
    # (e1,e2) = (0,0): dlog = 0 → QR dlog = 0
    # (e1,e2) = (0,2): dlog = 2(2j2+1) → QR dlog = 2j2+1
    # (e1,e2) = (2,0): dlog = 2(2j1+1) → QR dlog = 2j1+1
    # (e1,e2) = (2,2): dlog = 2(2j1+1) + 2(2j2+1) → QR dlog = 2j1+2j2+2 mod m
    # (e1,e2) = (1,1): dlog = (2j1+1) + (2j2+1) = 2(j1+j2+1) → QR dlog = j1+j2+1 mod m
    
    # So QNR part contributes: {0, 2j1+1, 2j2+1, 2j1+2j2+2, j1+j2+1} mod m
    # That's up to 5 QR values from 2 QNR factors.
    
    # This is getting complex. Let me just compute empirically whether 
    # the QR sumset covers everything, for small cases.
    
    # Enumerate all possible dlog vectors for QR and QNR primes
    # QR dlog: k ∈ Z/mZ (m choices)
    # QNR dlog: 2j+1, j ∈ Z/mZ (m choices, same set)
    
    # For omega_qr QR factors: dlog vector (k_1, ..., k_{omega_qr}) in (Z/mZ)^{omega_qr}
    # For omega_qnr QNR factors: dlog vector (j_1, ..., j_{omega_qnr}) in (Z/mZ)^{omega_qnr}
    
    # QR sumset = {sum of QR contributions} mod m
    
    # For omega_qr = a, omega_qnr = b:
    # Total combinations: m^{a+b} — too many for large m
    
    # For small m (m <= 30 or so), we can enumerate.
    
    if m > 30:
        return None  # Too large for exhaustive
    
    # Enumerate all possible dlog vectors
    # QR factor i: contributes {0, k_i, 2*k_i} to QR dlog
    # QNR factor j: contributes (from even exponents) {0, 2*j_j+1 mod m}
    #   and from odd-odd pairs: {j_j1 + j_j2 + 1} for each pair
    
    # Actually, let me just compute the QR divisor set for each dlog vector
    # and check if it covers all of Z/mZ.
    
    all_covered = True
    
    for k_vec in itertools.product(range(m), repeat=omega_qr):
        for j_vec in itertools.product(range(m), repeat=omega_qnr):
            # Compute QR divisor dlogs
            qr_dlogs = set()
            
            # QR factor contributions: {0, k_i, 2*k_i}
            qr_sets = [{0, k % m, (2*k) % m} for k in k_vec]
            
            # QNR factor contributions (even exponents only): {0, (2j+1) % m}
            qnr_even_sets = [{0, (2*j + 1) % m} for j in j_vec]
            
            # QNR odd-odd pair contributions
            # For each pair (j_a, j_b): {j_a + j_b + 1}
            # This adds extra elements when both have odd exponent
            qnr_pair_elements = set()
            for a in range(omega_qnr):
                for b in range(a+1, omega_qnr):
                    qnr_pair_elements.add((j_vec[a] + j_vec[b] + 1) % m)
            
            # Total QR dlog set = sumset of all QR sets + QNR even sets + pair elements
            # Start with {0}
            current = {0}
            for s in qr_sets:
                current = {(c + x) % m for c in current for x in s}
            for s in qnr_even_sets:
                current = {(c + x) % m for c in current for x in s}
            # Add pair contributions (each pair element is one specific QR dlog)
            # The pair elements represent (e1=1, e2=1) for that pair
            # with all other QNR factors at e=0
            # So they multiply with QR factor contributions
            if qnr_pair_elements:
                # For each base in current (with all QNR at e=0), 
                # add base + pair_element for each pair
                # But we also need to consider: what if 3 QNR factors all have e=1?
                # Then we have C(3,2) pairs but also the triple (e1=e2=e3=1)
                # which has 3 odd → NOT QR. So only even-count subsets.
                
                # For omega_qnr QNR factors, QR subsets (even number of odd exponents):
                # - All even: product of {0, 2j+1} for each → already in current
                # - 2 odd, rest even: pair_elements × rest_even
                # - 4 odd, rest even: etc.
                
                # This gets combinatorially complex. For small omega_qnr, enumerate directly.
                
                # Enumerate all parity vectors for QNR factors
                qnr_qr_dlogs = set()
                for parity in itertools.product([0, 1], repeat=omega_qnr):
                    if sum(parity) % 2 != 0:
                        continue  # Odd number of QNR with odd exponent → not QR
                    
                    # Compute dlog contribution from QNR factors
                    qnr_dlog = 0
                    for idx, p in enumerate(parity):
                        if p == 0:  # Even exponent (0 or 2)
                            # Choose exponent 0 (contributes 0) or 2 (contributes 2j+1)
                            # We need to enumerate both... this doubles the cases
                            pass
                        else:  # Odd exponent (1)
                            qnr_dlog = (qnr_dlog + j_vec[idx]) % m
                    
                    # For even-exponent factors, they contribute {0, 2j+1}
                    # For odd-exponent factors (paired), they contribute {j} 
                    # (since dlog = (2j+1), QR dlog = j when paired)
                    
                    # Actually this is getting too complex for the general case.
                    # Let me just compute directly for omega_qnr <= 3.
                    pass
                
                # For omega_qnr = 1: QR QNR contribution = {0, 2j+1} (e=0 or e=2)
                if omega_qnr == 1:
                    j = j_vec[0]
                    qnr_qr_set = {0, (2*j + 1) % m}
                    current = {(c + x) % m for c in current for x in qnr_qr_set}
                
                elif omega_qnr == 2:
                    j1, j2 = j_vec
                    # QR combos: (e1,e2) ∈ {(0,0), (0,2), (2,0), (2,2), (1,1)}
                    # dlogs: 0, 2j2+1, 2j1+1, 2j1+2j2+2, j1+j2+1
                    qnr_qr_set = {
                        0,
                        (2*j2 + 1) % m,
                        (2*j1 + 1) % m,
                        (2*j1 + 2*j2 + 2) % m,
                        (j1 + j2 + 1) % m,
                    }
                    current = {(c + x) % m for c in current for x in qnr_qr_set}
                
                elif omega_qnr == 3:
                    j1, j2, j3 = j_vec
                    # QR combos: even number of odd exponents
                    # 0 odd: (e1,e2,e3) all even → {0, 2j1+1} × {0, 2j2+1} × {0, 2j3+1}
                    # 2 odd: 3 pairs × even exponent for the third
                    # (1,1,0): j1+j2+1, times {0, 2j3+1}
                    # (1,0,1): j1+j3+1, times {0, 2j2+1}  
                    # (0,1,1): j2+j3+1, times {0, 2j1+1}
                    qnr_qr_set = set()
                    # 0 odd
                    for e1 in [0, (2*j1+1) % m]:
                        for e2 in [0, (2*j2+1) % m]:
                            for e3 in [0, (2*j3+1) % m]:
                                qnr_qr_set.add((e1 + e2 + e3) % m)
                    # 2 odd (pair 1,2)
                    for e3 in [0, (2*j3+1) % m]:
                        qnr_qr_set.add((j1 + j2 + 1 + e3) % m)
                    # 2 odd (pair 1,3)
                    for e2 in [0, (2*j2+1) % m]:
                        qnr_qr_set.add((j1 + j3 + 1 + e2) % m)
                    # 2 odd (pair 2,3)
                    for e1 in [0, (2*j1+1) % m]:
                        qnr_qr_set.add((j2 + j3 + 1 + e1) % m)
                    
                    current = {(c + x) % m for c in current for x in qnr_qr_set}
            
            # Check if current covers all of Z/mZ
            if len(current) < m:
                all_covered = False
                return False  # Found a failing dlog vector
    
    return all_covered

# Check for small u
print(f"\n{'u':>5} | {'m':>5} | {'ω_QR':>4} | {'ω_QNR':>5} | {'ω_total':>7} | {'Deterministic?':>14}")
print("-"*60)

for u in [7, 11, 19, 23, 31]:
    if not isprime(u) or u % 4 != 3:
        continue
    m = qr_subgroup_order(u)
    
    if m > 15:  # Too large for exhaustive
        print(f"  {u:3d} | {m:5d} | {'—':>4} | {'—':>5} | {'—':>7} | (m too large)")
        continue
    
    for omega_qnr in [1, 2]:
        for omega_qr in range(0, 6):
            total = omega_qr + omega_qnr
            if m**(total) > 100000:
                continue
            
            result = deterministic_qr_coverage(u, omega_qr, omega_qnr)
            if result is None:
                continue
            
            status = "✅ YES" if result else "❌ NO"
            print(f"  {u:3d} | {m:5d} | {omega_qr:4d} | {omega_qnr:5d} | {total:7d} | {status:>14}")
            
            if result:
                print(f"       → Deterministic coverage with ω(x) = {total} (ω_QR={omega_qr}, ω_QNR={omega_qnr})")
                break
        else:
            continue
        break

# ============ Analysis 4: Sumset growth rate ============
print(f"\n{'='*80}")
print("ANALYSIS 4: Sumset growth — how fast does QR sumset expand?")
print("="*80)

def sumset_growth(u, omega_qr, omega_qnr):
    """
    For prime u, compute the MINIMUM QR sumset size over all possible 
    dlog vectors. This shows how fast the sumset grows.
    
    Uses sampling for larger m.
    """
    if not isprime(u) or u % 4 != 3:
        return None
    
    m = qr_subgroup_order(u)
    g = primitive_root(u)
    
    if m > 100:
        # Sampling
        min_size = m + 1
        for _ in range(10000):
            k_vec = [random.randint(0, m-1) for _ in range(omega_qr)]
            j_vec = [random.randint(0, m-1) for _ in range(omega_qnr)]
            
            # Compute QR sumset
            current = {0}
            for k in k_vec:
                current = {(c + x) % m for c in current for x in [0, k, (2*k) % m]}
            
            # QNR contribution (simplified for omega_qnr = 1)
            if omega_qnr >= 1:
                j = j_vec[0]
                qnr_set = {0, (2*j + 1) % m}
                current = {(c + x) % m for c in current for x in qnr_set}
            
            if omega_qnr >= 2:
                j2 = j_vec[1]
                qnr_set2 = {0, (2*j2 + 1) % m}
                current = {(c + x) % m for c in current for x in qnr_set2}
            
            min_size = min(min_size, len(current))
        
        return min_size
    else:
        # Exhaustive
        min_size = m + 1
        for k_vec in itertools.product(range(m), repeat=omega_qr):
            current = {0}
            for k in k_vec:
                current = {(c + x) % m for c in current for x in [0, k, (2*k) % m]}
            
            if omega_qnr >= 1:
                for j in range(m):
                    qnr_set = {0, (2*j + 1) % m}
                    expanded = {(c + x) % m for c in current for x in qnr_set}
                    min_size = min(min_size, len(expanded))
            else:
                min_size = min(min_size, len(current))
        
        return min_size

print(f"\n{'u':>5} | {'m':>5} | {'ω_QR':>4} | {'ω_QNR':>5} | {'Min QR sumset':>14} | {'Coverage':>10}")
print("-"*65)

for u in [7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127]:
    if not isprime(u) or u % 4 != 3:
        continue
    m = qr_subgroup_order(u)
    
    for omega_qr in range(0, 8):
        for omega_qnr in [1]:  # Minimum from QNR inheritance
            total = omega_qr + omega_qnr
            
            min_size = sumset_growth(u, omega_qr, omega_qnr)
            if min_size is None:
                continue
            
            coverage = min_size / m
            status = "FULL ✓" if min_size >= m else f"{coverage:.2%}"
            
            print(f"  {u:3d} | {m:5d} | {omega_qr:4d} | {omega_qnr:5d} | {min_size:14d} | {status:>10}")
            
            if min_size >= m:
                print(f"       → Full QR coverage with ω(x) = {total} ✓")
                break
        else:
            continue
        break

# ============ Summary ============
print(f"\n{'='*80}")
print("SUMMARY: Cauchy-Davenport / QR Subgroup Coverage")
print("="*80)