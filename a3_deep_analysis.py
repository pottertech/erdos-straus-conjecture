#!/usr/bin/env python3
"""
Deep analysis of the A=3 failure pattern.

KEY FINDINGS FROM FIRST RUN:
- B ≡ 0 (mod 4) → ALWAYS works (100%)
- B ≡ 2 (mod 4) → works 66% of the time
- All failures are "no divisor d ≤ B of B² satisfies mod 36"
- z = (d+B)/6 is always positive (confirmed)
- 3 ∤ B always (confirmed)
- B mod 36: 8, 20, 32 → 100%; 2, 14, 26 → ~66%

B ≡ 0 (mod 4) corresponds to B mod 36 ∈ {8, 20, 32} (since B mod 9 ∈ {2,5,8})
B ≡ 2 (mod 4) corresponds to B mod 36 ∈ {2, 14, 26}

So the question: among B ≡ 2 (mod 4), what distinguishes working from failing?

The mod 36 condition: d + 2B + B²/d ≡ 0 (mod 36)
Since B ≡ 2 (mod 4), B = 4k+2. B² = 16k² + 16k + 4 = 4(4k² + 4k + 1).
B² ≡ 4 (mod 16). B²/4 = 4k² + 4k + 1 ≡ 1 (mod 2), so B² has exactly 2-adic valuation 2.

For the mod 36 = mod 4 × mod 9 condition:
- mod 4: d + 2B + B²/d ≡ 0 (mod 4)
  B ≡ 2 (mod 4), B² ≡ 0 (mod 4), so B²/d ≡ 0 (mod 4) if 4|d, else B²/d mod 4 depends.
  If d is odd: d + 2·2 + B²/d mod 4. B² = 4·(odd), so B²/d = 4·(odd/d). If d is odd, B²/d = 4·integer, so B²/d ≡ 0 (mod 4).
  So condition mod 4: d + 4 + 0 ≡ 0 (mod 4) → d ≡ 0 (mod 4). But d is odd, contradiction.
  Wait, d | B² and B = 4k+2 = 2(2k+1). So B² = 4(2k+1)². 
  The odd part of B² is (2k+1)². Divisors of B² are of form 2^a · d_odd where 0 ≤ a ≤ 2 and d_odd | (2k+1)².
  
  For d = 2^a · d_odd:
  B²/d = 2^(2-a) · (2k+1)²/d_odd
  
  mod 4 condition: d + 2B + B²/d ≡ 0 (mod 4)
  2B = 2·2(2k+1) = 4(2k+1) ≡ 0 (mod 4)
  So: d + B²/d ≡ 0 (mod 4)
  
  d = 2^a · d_odd, B²/d = 2^(2-a) · ((2k+1)²/d_odd)
  d + B²/d = 2^a · d_odd + 2^(2-a) · ((2k+1)²/d_odd)
  
  a=0: d_odd + 4·((2k+1)²/d_odd) ≡ d_odd + 0 ≡ d_odd (mod 4). Need d_odd ≡ 0 (mod 4), but d_odd is odd. FAIL.
  a=1: 2·d_odd + 2·((2k+1)²/d_odd) = 2(d_odd + (2k+1)²/d_odd). 
       Since (2k+1)²/d_odd is odd (both d_odd and (2k+1)²/d_odd are odd, and their product is odd²=odd), 
       d_odd + (2k+1)²/d_odd = odd + odd = even. So 2·even ≡ 0 (mod 4). WORKS if d_odd + (2k+1)²/d_odd is even, which it always is (odd+odd=even).
       So a=1 ALWAYS satisfies mod 4!
  a=2: 4·d_odd + 1·((2k+1)²/d_odd) = 0 + (2k+1)²/d_odd (mod 4). Need (2k+1)²/d_odd ≡ 0 (mod 4), but it's odd. FAIL.

  So for B ≡ 2 (mod 4): d must have 2-adic valuation exactly 1 (d = 2·d_odd where d_odd | (2k+1)²).
  This automatically satisfies mod 4.

  Now mod 9 condition: d + 2B + B²/d ≡ 0 (mod 9)
  With d = 2·d_odd, B²/d = 2·(2k+1)²/d_odd (since B²=4(2k+1)², B²/d = 4(2k+1)²/(2·d_odd) = 2(2k+1)²/d_odd)
  
  So: 2·d_odd + 2B + 2·(2k+1)²/d_odd ≡ 0 (mod 9)
  Divide by 2 (since gcd(2,9)=1, multiply by 5):
  d_odd + B + (2k+1)²/d_odd ≡ 0 (mod 9)
  
  Let O = 2k+1 (the odd part of B). B = 2O. So:
  d_odd + 2O + O²/d_odd ≡ 0 (mod 9)
  
  This is the same Pell structure on the odd part! We need d_odd | O² with d_odd + 2O + O²/d_odd ≡ 0 (mod 9).
  
  For B ≡ 0 (mod 4): B = 4m. B² = 16m². Divisors have 2-adic valuation 0..4.
  Similar analysis would show the mod 4 condition is more flexible.
"""

import json
from collections import Counter

def factorize(n):
    factors = {}
    temp = n
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def divisors_of(n):
    """Get all divisors of n."""
    if n <= 0:
        return []
    factors = factorize(n)
    divs = [1]
    for p, e in factors.items():
        new_divs = []
        for d in divs:
            for i in range(e + 1):
                new_divs.append(d * p**i)
        divs = new_divs
    return sorted(divs)

def main():
    # For the failing cases (B ≡ 2 mod 4), we need d = 2·d_odd where d_odd | O²
    # and d_odd + 2O + O²/d_odd ≡ 0 (mod 9)
    # where O = B/2 (the odd part of B)
    
    # The question: for which O does O² have a divisor d_odd with d_odd + 2O + O²/d_odd ≡ 0 (mod 9)?
    # Note: d_odd + O²/d_odd + 2O ≡ 0 (mod 9)
    # This is the SAME condition as the original problem but with O instead of B, and mod 9 instead of mod 36!
    
    # O = B/2 = n(n+3)/4. Since n ≡ 1 (mod 12), n+3 ≡ 4 (mod 12), so (n+3)/4 ≡ 1 (mod 3).
    # O = n · (n+3)/4. n ≡ 1 (mod 3), (n+3)/4 ≡ 1 (mod 3). So O ≡ 1 (mod 3).
    # O² ≡ 1 (mod 3). So O is not divisible by 3.
    
    # For the symmetric case d_odd = O: O + 2O + O = 4O ≡ 0 (mod 9) iff 9 | 4O iff 9 | O (since gcd(4,9)=1).
    # But O ≡ 1 (mod 3), so 3 ∤ O, so 9 ∤ O. Symmetric fails again.
    
    # So we need a non-trivial divisor of O² satisfying the mod 9 condition.
    # This is recursive! The same problem at a smaller scale.
    
    print("="*60)
    print("RECURSIVE STRUCTURE: A=3 reduces to mod-9 Pell on odd part")
    print("="*60)
    print()
    print("For B ≡ 2 (mod 4):")
    print("  B = 2O where O = n(n+3)/4, O ≡ 1 (mod 3)")
    print("  Need d_odd | O² with d_odd + 2O + O²/d_odd ≡ 0 (mod 9)")
    print("  This is the same Pell condition but mod 9 instead of mod 36")
    print("  Symmetric (d_odd = O) needs 9|O, but O ≡ 1 (mod 3), so 3∤O. Fails.")
    print()
    
    # Let's verify: for working cases with B ≡ 2 (mod 4), what is O mod 9?
    # and does the condition reduce correctly?
    
    max_n = 100000
    b2mod4_works = 0
    b2mod4_fails = 0
    o_mod9_works = Counter()
    o_mod9_fails = Counter()
    
    # For each failing case, check if O² has ANY divisor satisfying mod 9
    fail_O_details = []
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        
        B = n * (n + 3) // 2
        
        if B % 4 == 0:
            continue  # Only look at B ≡ 2 (mod 4)
        
        O = B // 2  # odd part
        O2 = O * O
        O_mod9 = O % 9
        
        # Check if O² has divisor d_odd with d_odd + 2O + O²/d_odd ≡ 0 (mod 9) and d_odd ≤ O
        divs_O = divisors_of(O2)
        found = False
        working_d_odd = None
        
        for d_odd in divs_O:
            if d_odd > O:
                break
            if (d_odd + 2 * O + O2 // d_odd) % 9 == 0:
                found = True
                working_d_odd = d_odd
                break
        
        if found:
            b2mod4_works += 1
            o_mod9_works[O_mod9] += 1
        else:
            b2mod4_fails += 1
            o_mod9_fails[O_mod9] += 1
            if len(fail_O_details) < 30:
                # Factor O
                O_factors = factorize(O)
                fail_O_details.append({
                    'n': n,
                    'B': B,
                    'O': O,
                    'O_mod_9': O_mod9,
                    'O_factors': O_factors,
                    'O_num_prime_factors': len(O_factors),
                })
    
    total_b2 = b2mod4_works + b2mod4_fails
    print(f"B ≡ 2 (mod 4) cases: {total_b2}")
    print(f"  Works: {b2mod4_works} ({100*b2mod4_works/total_b2:.1f}%)")
    print(f"  Fails: {b2mod4_fails} ({100*b2mod4_fails/total_b2:.1f}%)")
    
    print(f"\nO mod 9 vs SUCCESS (for B ≡ 2 mod 4 cases):")
    all_mod9 = set(list(o_mod9_works.keys()) + list(o_mod9_fails.keys()))
    for m in sorted(all_mod9):
        w = o_mod9_works.get(m, 0)
        f = o_mod9_fails.get(m, 0)
        t = w + f
        print(f"  O ≡ {m} (mod 9): works={w:5d}, fails={f:5d}, total={t:5d}, success={100*w/t:.1f}%")
    
    print(f"\nFailing cases (B ≡ 2 mod 4) — O factorizations:")
    for d in fail_O_details[:20]:
        print(f"  n={d['n']}, O={d['O']}, O mod 9={d['O_mod_9']}, factors={d['O_factors']}")
    
    # Key question: O ≡ 1 (mod 3). So O mod 9 ∈ {1, 4, 7}.
    # Does the number of prime factors of O matter?
    print(f"\nPrime factor count vs success:")
    factor_count_works = Counter()
    factor_count_fails = Counter()
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue
        
        O = B // 2
        O_factors = factorize(O)
        num_primes = len(O_factors)
        
        # Check if works
        O2 = O * O
        divs_O = divisors_of(O2)
        found = False
        for d_odd in divs_O:
            if d_odd > O:
                break
            if (d_odd + 2 * O + O2 // d_odd) % 9 == 0:
                found = True
                break
        
        if found:
            factor_count_works[num_primes] += 1
        else:
            factor_count_fails[num_primes] += 1
    
    all_counts = set(list(factor_count_works.keys()) + list(factor_count_fails.keys()))
    for c in sorted(all_counts):
        w = factor_count_works.get(c, 0)
        f = factor_count_fails.get(c, 0)
        t = w + f
        print(f"  {c} prime factors: works={w:5d}, fails={f:5d}, total={t:5d}, success={100*w/t:.1f}%")
    
    # Now the deeper question: for B ≡ 0 (mod 4), why does it ALWAYS work?
    # B = 4m. B² = 16m². We need d | 16m² with d + 2B + B²/d ≡ 0 (mod 36).
    # B ≡ 0 (mod 4), so 2B ≡ 0 (mod 8). 
    # mod 4: d + B²/d ≡ 0 (mod 4) (since 2B ≡ 0 mod 4)
    # B² = 16m², so B²/d = 16m²/d.
    # If 4|d: d ≡ 0 (mod 4), B²/d = 16m²/d. If 4|d then 16m²/d may or may not be ≡ 0 mod 4.
    #   d=4: 16m²/4 = 4m² ≡ 0 (mod 4). So d + B²/d ≡ 0 + 0 = 0 (mod 4). WORKS.
    # So d=4 always satisfies mod 4 when B ≡ 0 (mod 4) and 4|B² (which it does since 16|B²).
    
    # mod 9 with d=4: 4 + 2B + B²/4 ≡ 4 + 2B + 4m² (mod 9) where B=4m.
    # = 4 + 8m + 4m² = 4(1 + 2m + m²) = 4(1+m)² (mod 9)
    # Need 9 | 4(1+m)², i.e., 3 | (1+m), i.e., m ≡ 2 (mod 3).
    # But B = 4m, B mod 9 ∈ {8, 20, 32} mod 36 → B mod 9 ∈ {2, 5, 8}
    # B = 4m, so m = B/4. m mod 9 = (B/4) mod 9.
    # B ≡ 8 (mod 36) → B ≡ 8 (mod 9) → m ≡ 8/4 = 2 (mod 9) → m ≡ 2 (mod 3) ✓
    # B ≡ 20 (mod 36) → B ≡ 2 (mod 9) → m ≡ 2·5 = 10 ≡ 1 (mod 9) → m ≡ 1 (mod 3) ✗
    # B ≡ 32 (mod 36) → B ≡ 5 (mod 9) → m ≡ 5·5 = 25 ≡ 7 (mod 9) → m ≡ 1 (mod 3) ✗
    
    # Wait, but B ≡ 20 (mod 36) and B ≡ 32 (mod 36) also have 100% success!
    # So d=4 doesn't always work for the mod 9 part. But other divisors do.
    
    # Let me check: for B ≡ 0 (mod 4), which divisor d gives the solution?
    print(f"\n{'='*60}")
    print("B ≡ 0 (mod 4) ANALYSIS: which divisor works?")
    print(f"{'='*60}")
    
    d_values_b0mod4 = Counter()
    
    for n in range(13, min(max_n + 1, 10001)):  # smaller range for detailed analysis
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 != 0:
            continue
        
        B2 = B * B
        # Get divisors of B²
        B_factors = factorize(B)
        divs = [1]
        for p, e in B_factors.items():
            new_divs = []
            for d in divs:
                for i in range(2*e + 1):
                    new_divs.append(d * p**i)
            divs = new_divs
        divs = sorted(divs)
        
        for d in divs:
            if d > B:
                break
            if (d + 2 * B + B2 // d) % 36 == 0:
                d_values_b0mod4[d] += 1
                break  # first working divisor
    
    print(f"Most common working divisors (B ≡ 0 mod 4, n ≤ 10000):")
    for d, count in d_values_b0mod4.most_common(20):
        print(f"  d={d}: {count} times")
    
    # Check: for B ≡ 0 (mod 4), the 2-adic valuation of B is ≥ 2.
    # B = 2^a · O where a ≥ 2 and O is odd.
    # Key: when a ≥ 2, B² has 2-adic valuation ≥ 4, giving many choices for 2-adic valuation of d.
    # This extra freedom in choosing the 2-part of d is what guarantees success.
    
    print(f"\n{'='*60}")
    print("2-ADIC VALUATION ANALYSIS")
    print(f"{'='*60}")
    
    v2_works = Counter()
    v2_fails = Counter()
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        
        # Compute 2-adic valuation of B
        v2 = 0
        temp = B
        while temp % 2 == 0:
            v2 += 1
            temp //= 2
        
        # Check if A=3 works
        B2 = B * B
        B_factors = factorize(B)
        divs = [1]
        for p, e in B_factors.items():
            new_divs = []
            for d in divs:
                for i in range(2*e + 1):
                    new_divs.append(d * p**i)
            divs = new_divs
        divs = sorted(divs)
        
        found = False
        for d in divs:
            if d > B:
                break
            if (d + 2 * B + B2 // d) % 36 == 0:
                found = True
                break
        
        if found:
            v2_works[v2] += 1
        else:
            v2_fails[v2] += 1
    
    all_v2 = set(list(v2_works.keys()) + list(v2_fails.keys()))
    for v in sorted(all_v2):
        w = v2_works.get(v, 0)
        f = v2_fails.get(v, 0)
        t = w + f
        print(f"  v₂(B) = {v}: works={w:5d}, fails={f:5d}, total={t:5d}, success={100*w/t:.1f}%")
    
    # Now the FINAL question: for B ≡ 2 (mod 4), i.e., v₂(B) = 1,
    # the problem reduces to: does O² have a divisor d_odd with d_odd + 2O + O²/d_odd ≡ 0 (mod 9)?
    # O ≡ 1 (mod 3), so O mod 9 ∈ {1, 4, 7}.
    # This is the EXACT SAME problem as the original Erdős-Straus framework but mod 9!
    
    # For the original problem mod 36 with B not divisible by 3, 
    # we need divisors of B² satisfying a mod-36 condition.
    # When v₂(B) = 1, the mod-4 part forces v₂(d) = 1,
    # reducing to a mod-9 condition on divisors of O².
    # When v₂(B) ≥ 2, there's enough freedom in the 2-adic part to always solve mod 4,
    # and then mod 9 can be solved using the many available divisors.
    
    # Let's check: for v₂(B) ≥ 2, does d = 2^v₂(B) · something always work?
    # Or is it that the large number of divisors with different 2-adic valuations guarantees a mod-36 match?
    
    print(f"\n{'='*60}")
    print("DETAILED: For v₂(B) = 1, what mod-9 residues do divisors of O² give?")
    print(f"{'='*60}")
    
    # For O ≡ 1 (mod 3), O is not divisible by 3.
    # O² mod 9: if O ≡ 1 (mod 9), O² ≡ 1 (mod 9)
    #           if O ≡ 4 (mod 9), O² ≡ 16 ≡ 7 (mod 9)  
    #           if O ≡ 7 (mod 9), O² ≡ 49 ≡ 4 (mod 9)
    
    # Divisors of O²: for any prime p|O with p^e || O, divisors have p^a for 0 ≤ a ≤ 2e.
    # The product d · (O²/d) = O², and d + O²/d + 2O ≡ 0 (mod 9).
    
    # For d_odd = 1: 1 + 2O + O² ≡ (1+O)² (mod 9). Need 9 | (1+O)², i.e., 3 | (1+O).
    # O ≡ 1 (mod 3), so 1+O ≡ 2 (mod 3). NOT divisible by 3. So d=1 never works!
    
    # For d_odd = O: O + 2O + O = 4O. Need 9 | 4O, i.e., 9|O. But 3∤O. Fails.
    
    # So we need non-trivial divisors. The question is whether O² has enough divisors.
    
    # Key insight: if O has many prime factors, O² has many divisors, 
    # giving many residues mod 9, and one is likely to hit 0.
    # If O is a prime or prime power, O² has few divisors, and may not hit 0 mod 9.
    
    # Let's verify: failing cases tend to have O with few prime factors
    print(f"\nFailing cases: O factorization details (first 30):")
    for d in fail_O_details[:30]:
        O = d['O']
        O_factors = d['O_factors']
        num_divs_O2 = 1
        for p, e in O_factors.items():
            num_divs_O2 *= (2*e + 1)
        print(f"  n={d['n']}, O={O}, O mod 9={d['O_mod_9']}, "
              f"ω(O)={len(O_factors)}, τ(O²)={num_divs_O2}, factors={O_factors}")
    
    # Check: are there failing cases where O is prime?
    print(f"\n{'='*60}")
    print("IS O PRIME IN FAILING CASES?")
    print(f"{'='*60}")
    
    def is_prime(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    o_prime_fails = 0
    o_prime_power_fails = 0
    o_composite_fails = 0
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue
        
        O = B // 2
        O2 = O * O
        
        # Check if works
        O_factors = factorize(O)
        divs_O = [1]
        for p, e in O_factors.items():
            new_divs = []
            for d in divs_O:
                for i in range(2*e + 1):
                    new_divs.append(d * p**i)
            divs_O = new_divs
        divs_O = sorted(divs_O)
        
        found = False
        for d_odd in divs_O:
            if d_odd > O:
                break
            if (d_odd + 2 * O + O2 // d_odd) % 9 == 0:
                found = True
                break
        
        if not found:
            if len(O_factors) == 1:
                if list(O_factors.values())[0] == 1:
                    o_prime_fails += 1
                else:
                    o_prime_power_fails += 1
            else:
                o_composite_fails += 1
    
    total_fails = o_prime_fails + o_prime_power_fails + o_composite_fails
    print(f"  O is prime: {o_prime_fails} ({100*o_prime_fails/total_fails:.1f}%)")
    print(f"  O is prime power (p^k, k≥2): {o_prime_power_fails} ({100*o_prime_power_fails/total_fails:.1f}%)")
    print(f"  O is composite (≥2 primes): {o_composite_fails} ({100*o_composite_fails/total_fails:.1f}%)")
    
    # THE PATTERN: when O is prime, O² has only 3 divisors: 1, O, O².
    # d_odd=1: (1+O)² mod 9. O ≡ 1,4,7 (mod 9). 
    #   O≡1: (1+1)²=4, O≡4: (1+4)²=25≡7, O≡7: (1+7)²=64≡1. Never 0 mod 9.
    # d_odd=O: 4O mod 9. O≡1: 4, O≡4: 16≡7, O≡7: 28≡1. Never 0 mod 9.
    # So when O is prime, there are NO solutions! (only 2 divisors ≤ O: 1 and O, neither works)
    
    print(f"\n{'='*60}")
    print("VERIFICATION: O prime → always fails")
    print(f"{'='*60}")
    
    o_prime_total = 0
    o_prime_works = 0
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue
        O = B // 2
        if not is_prime(O):
            continue
        o_prime_total += 1
        
        # Check if A=3 works
        B2 = B * B
        B_factors = factorize(B)
        divs = [1]
        for p, e in B_factors.items():
            new_divs = []
            for d in divs:
                for i in range(2*e + 1):
                    new_divs.append(d * p**i)
            divs = new_divs
        divs = sorted(divs)
        
        for d in divs:
            if d > B:
                break
            if (d + 2 * B + B2 // d) % 36 == 0:
                o_prime_works += 1
                break
    
    print(f"  O prime: {o_prime_works}/{o_prime_total} work ({100*o_prime_works/o_prime_total:.1f}% if total > 0 else 0)" if o_prime_total > 0 else "  O prime: 0 cases")
    
    # When O = p² (prime squared), O² = p⁴, divisors: 1, p, p², p³, p⁴.
    # d_odd ≤ O means d_odd ∈ {1, p, p²}.
    # d_odd=1: (1+p²)² mod 9
    # d_odd=p: p + 2p² + p³ = p(1 + 2p + p²) = p(1+p)² mod 9
    # d_odd=p²: p² + 2p² + p² = 4p² mod 9
    # Need any of these ≡ 0 (mod 9).
    # 4p² ≡ 0 (mod 9) iff 3|p² iff 3|p. But O ≡ 1 (mod 3), so p ≢ 0 (mod 3). Fails.
    # p(1+p)² ≡ 0 (mod 9) iff 3|p or 3|(1+p). p ≢ 0 mod 3. 1+p mod 3: if p≡1, 1+p≡2; if p≡2, 1+p≡0. 
    #   So 3|(1+p) iff p≡2 (mod 3). Then 9|p(1+p)² iff 3|p(1+p)² and the 3-adic valuation is ≥2.
    #   If p≡2 (mod 3): 3|(1+p), v₃(1+p)≥1. v₃(p(1+p)²) = 2·v₃(1+p) ≥ 2. So 9|p(1+p)² iff v₃(1+p)≥1 iff p≡2 (mod 3).
    #   But we also need 9 | p(1+p)², which requires v₃(p(1+p)²) ≥ 2, i.e., v₃((1+p)²) ≥ 2, i.e., v₃(1+p) ≥ 1, i.e., 3|(1+p).
    #   This is p ≡ 2 (mod 3). But O = p² ≡ 1 (mod 3) always (since p ≡ 1 or 2 mod 3, p² ≡ 1 mod 3).
    #   So if p ≡ 2 (mod 3), then d_odd = p works!
    
    print(f"\n{'='*60}")
    print("O = p² case: does p ≡ 2 (mod 3) help?")
    print(f"{'='*60}")
    
    o_primesq_total = 0
    o_primesq_works = 0
    o_primesq_p_mod3 = Counter()
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue
        O = B // 2
        O_factors = factorize(O)
        
        if len(O_factors) == 1 and list(O_factors.values())[0] == 2:
            p = list(O_factors.keys())[0]
            o_primesq_total += 1
            o_primesq_p_mod3[p % 3] += 1
            
            # Check if A=3 works
            B2 = B * B
            divs = [1]
            for pp, e in factorize(B).items():
                new_divs = []
                for d in divs:
                    for i in range(2*e + 1):
                        new_divs.append(d * pp**i)
                divs = new_divs
            divs = sorted(divs)
            
            found = False
            for d in divs:
                if d > B:
                    break
                if (d + 2 * B + B2 // d) % 36 == 0:
                    found = True
                    break
            
            if found:
                o_primesq_works += 1
    
    if o_primesq_total > 0:
        print(f"  O = p²: {o_primesq_works}/{o_primesq_total} work")
        print(f"  p mod 3 distribution: {dict(o_primesq_p_mod3)}")
    
    # SUMMARY OF THE RECURSIVE STRUCTURE
    print(f"\n{'='*60}")
    print("COMPLETE PATTERN SUMMARY")
    print(f"{'='*60}")
    print("""
For n ≡ 1 (mod 12), n ≢ 0 (mod 5), A=3 case:

1. B = n(n+3)/2. Since n ≡ 1 (mod 12):
   - n is odd, n+3 ≡ 4 (mod 12), so B = n·(n+3)/2 is always even
   - 3 ∤ B (since n ≡ 1 mod 3, n+3 ≡ 1 mod 3, so 3 ∤ n(n+3))
   
2. z = (d+B)/6 is ALWAYS positive (confirmed computationally)

3. The mod-36 condition on divisors of B²:
   - When v₂(B) ≥ 2 (B ≡ 0 mod 4): ALWAYS solvable (100%)
     The extra 2-adic freedom provides enough divisor choices
   - When v₂(B) = 1 (B ≡ 2 mod 4): Solvable iff O² = (B/2)² has a 
     divisor d_odd with d_odd + 2O + O²/d_odd ≡ 0 (mod 9)
     
4. For v₂(B) = 1, the problem reduces to a mod-9 Pell condition on O = B/2:
   - O ≡ 1 (mod 3) always
   - When O is prime: only divisors 1 and O of O² satisfy d ≤ O. 
     Neither satisfies mod 9. ALWAYS FAILS.
   - When O has more prime factors: more divisors → higher chance of 
     satisfying mod 9
     
5. Number-theoretic condition: A=3 works iff either
   (a) v₂(B) ≥ 2 (B ≡ 0 mod 4), OR
   (b) v₂(B) = 1 AND O = B/2 is not prime AND O² has a divisor 
       d_odd ≤ O with d_odd + 2O + O²/d_odd ≡ 0 (mod 9)
""")

if __name__ == '__main__':
    main()