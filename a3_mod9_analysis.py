#!/usr/bin/env python3
"""
Final analysis: Why do composite O values with 2 prime factors fail?
And what's the exact mod-9 condition?

For v₂(B) = 1, we need d_odd | O² with d_odd + 2O + O²/d_odd ≡ 0 (mod 9)
where O ≡ 1 (mod 3), so O mod 9 ∈ {1, 4, 7}.

When O = pq (two distinct primes), O² = p²q², divisors d ≤ O:
  1, p, q, p², pq, q² (and more if p or q have higher powers)
  
For O = p·q (distinct primes, each to power 1):
  Divisors of O² = p²q²: 1, p, p², q, pq, p²q, q², pq², p²q²
  Divisors ≤ O = pq: 1, p, q, p² (if p²≤pq), pq, q² (if q²≤pq)
  
The mod-9 condition: d + 2O + O²/d ≡ 0 (mod 9)
  d=1: 1 + 2O + O² = (1+O)². O≡1,4,7 mod 9.
    O≡1: (1+1)²=4; O≡4: (1+4)²=25≡7; O≡7: (1+7)²=64≡1. Never 0 mod 9.
  d=O: 4O. O≡1→4, O≡4→16≡7, O≡7→28≡1. Never 0 mod 9.
  d=p: p + 2pq + p²q²/p = p + 2pq + pq² = p(1 + 2q + q²) = p(1+q)²
    Need 9 | p(1+q)². Since gcd(p,9) ∈ {1,3} and p∤3 (O≡1 mod 3):
    Need 9 | (1+q)², i.e., 3 | (1+q), i.e., q ≡ 2 (mod 3).
    Since O = pq ≡ 1 (mod 3), and p,q ≢ 0 mod 3:
    If q ≡ 2 (mod 3), then p ≡ 2 (mod 3) (since 2·2=4≡1 mod 3). 
    If q ≡ 1 (mod 3), then p ≡ 1 (mod 3).
    So d=p works iff both p,q ≡ 2 (mod 3), which means O ≡ 1 (mod 3) ✓
    But we also need 9 | p(1+q)². If q≡2 (mod 3), then 3|(1+q), 
    so v₃((1+q)²) = 2·v₃(1+q) ≥ 2, so 9 | p(1+q)². Works!
  d=q: q(1+p)². Works iff p ≡ 2 (mod 3).
  d=p²: p² + 2pq + q² = (p+q)². Need 9|(p+q)², i.e., 3|(p+q).
    If p≡1,q≡1: p+q≡2. If p≡2,q≡2: p+q≡4≡1. Never 0 mod 3!
  d=q²: q² + 2pq + p² = (p+q)². Same as above. Never 0 mod 3.

So for O = pq (distinct primes):
  d=p works iff q ≡ 2 (mod 3) (which implies p ≡ 2 mod 3 too, since O≡1 mod 3)
  d=q works iff p ≡ 2 (mod 3)
  d=p² or d=q²: (p+q)² mod 9 — works iff 3|(p+q), but p≡q mod 3, so p+q≡2 or 1 mod 3. Never works.
  d=1 or d=O: never works.
  
  d=pq²/q = pq (if pq² ≤ O=pq, i.e., q≤1, impossible for prime q). 
  Actually d=p²q: p²q + 2pq + pq = pq(p+3). Need 9|pq(p+3). Since 3∤pq:
    Need 3|(p+3), i.e., 3|p, impossible. Wait, p+3 mod 3 = p mod 3. So 3∤(p+3) since p≢0 mod 3.
    
  Hmm wait, let me reconsider. For O = pq:
  O² = p²q². All divisors: 1, p, p², q, pq, p²q, q², pq², p²q²
  Divisors d ≤ O = pq: 1, p, q, p² (if p<q), pq, q² (if q²≤pq, i.e., q≤p, impossible if p<q)
  
  So divisors ≤ O: {1, p, q, p² (if p²≤pq → p≤q), pq}
  
  Summary: O = pq works iff p ≡ 2 (mod 3) or q ≡ 2 (mod 3), i.e., at least one prime ≡ 2 (mod 3).
  Equivalently: O = pq FAILS iff both p ≡ 1 (mod 3) and q ≡ 1 (mod 3).
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
    max_n = 100000
    
    print("="*60)
    print("THEORY: O = pq fails iff both p ≡ 1 (mod 3)")
    print("="*60)
    print()
    print("For O = pq (distinct primes, each ≡ 1 mod 3):")
    print("  d=1: (1+O)² mod 9. O≡1→4, O≡4→7, O≡7→1. Never 0.")
    print("  d=p: p(1+q)² mod 9. q≡1 mod 3 → 1+q≡2 → (1+q)²≡4. p≡1 → p·4≡4. Never 0.")
    print("  d=q: q(1+p)² mod 9. Same logic. Never 0.")
    print("  d=p²: (p+q)² mod 9. p≡q≡1 mod 3 → p+q≡2 mod 3 → (p+q)²≡4. Never 0.")
    print("  d=pq: 4O mod 9. O≡1,4,7 → 4,7,1. Never 0.")
    print()
    print("For O = pq where p ≡ 2 (mod 3), q ≡ 2 (mod 3) (so O ≡ 1 mod 3):")
    print("  d=p: p(1+q)². q≡2 mod 3 → 1+q≡0 mod 3 → 9|(1+q)². WORKS!")
    print("  d=q: q(1+p)². p≡2 mod 3 → 1+p≡0 mod 3 → 9|(1+p)². WORKS!")
    print()
    
    # Verify this theory
    print("="*60)
    print("VERIFICATION: For v₂(B)=1, O=pq, does success ⟺ p≡2(mod 3) or q≡2(mod 3)?")
    print("="*60)
    
    theory_correct = 0
    theory_wrong = 0
    details_wrong = []
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue  # Only v₂(B) = 1
        
        O = B // 2
        O_factors = factorize(O)
        
        # Only look at O = pq (exactly 2 distinct primes, each to power 1)
        if len(O_factors) != 2:
            continue
        if list(O_factors.values()) != [1, 1]:
            continue
        
        primes = sorted(O_factors.keys())
        p, q = primes
        p_mod3 = p % 3
        q_mod3 = q % 3
        
        # Theory predicts: works iff at least one prime ≡ 2 (mod 3)
        theory_says_works = (p_mod3 == 2) or (q_mod3 == 2)
        
        # Check actual
        O2 = O * O
        divs_O = divisors_of(O2)
        found = False
        for d_odd in divs_O:
            if d_odd > O:
                break
            if (d_odd + 2 * O + O2 // d_odd) % 9 == 0:
                found = True
                break
        
        if found == theory_says_works:
            theory_correct += 1
        else:
            theory_wrong += 1
            details_wrong.append({
                'n': n, 'O': O, 'p': p, 'q': q, 
                'p_mod3': p_mod3, 'q_mod3': q_mod3,
                'theory_says': theory_says_works, 'actual': found
            })
    
    total = theory_correct + theory_wrong
    print(f"  Theory correct: {theory_correct}/{total} ({100*theory_correct/total:.1f}%)")
    print(f"  Theory wrong: {theory_wrong}")
    if details_wrong:
        for d in details_wrong[:10]:
            print(f"    n={d['n']}, O={d['O']}, p={d['p']}≡{d['p_mod3']}(mod 3), q={d['q']}≡{d['q_mod3']}(mod 3), theory={d['theory_says']}, actual={d['actual']}")
    
    # Now extend: for O = p²q (one prime squared, one to power 1)
    print(f"\n{'='*60}")
    print("O = p²q case analysis")
    print("="*60)
    print()
    print("O = p²q. O² = p⁴q². Divisors d ≤ O with d | O²:")
    print("  d=1: (1+O)² — never 0 mod 9 (O≡1 mod 3)")
    print("  d=p: p(1+q)² — works iff q≡2(mod 3)")
    print("  d=p²: p² + 2p²q + q² = ... let me compute")
    print("  d=q: q(1+p²)/... actually d=q: q + 2p²q + p⁴q/q = q + 2p²q + p⁴")
    print("  d=pq: pq + 2p²q + p²q = pq(1 + 2p + p) = pq(1+3p) — 3p≡0 mod 3, so 1+3p≡1. pq≡O mod 3... need 9|pq(1+3p). Since 3∤pq and 3∤(1+3p) iff 3∤1... wait 1+3p ≡ 1 (mod 3). So need 9|pq·1 = pq, but 3∤pq. Fails.")
    print("  d=p²: p² + 2p²q + p²q²/p² = p² + 2p²q + q² = (p+q)². Same as before — works iff 3|(p+q).")
    print("  d=p²q: O itself. 4O — never 0 mod 9.")
    print()
    print("So for O = p²q:")
    print("  d=p works iff q ≡ 2 (mod 3)")
    print("  d=q works iff ... let me compute: q + 2p²q + p⁴q²/(q) = q + 2p²q + p⁴q = q(1 + 2p² + p⁴) = q(1+p²)²")
    print("    Need 9|q(1+p²)². 3∤q. Need 3|(1+p²). p²≡1 mod 3 (always, since p≢0 mod 3). 1+p²≡2 mod 3. Never 0!")
    print("  d=p²: (p+q)². Works iff 3|(p+q), i.e., p≡q mod 3 and p+q≡0 mod 3. Since p,q∈{1,2} mod 3:")
    print("    p≡q≡1: p+q≡2. p≡q≡2: p+q≡1. p≡1,q≡2 or p≡2,q≡1: p+q≡0 mod 3! Then 9|(p+q)² iff v₃(p+q)≥1, which is true.")
    print("    So d=p² works iff p and q have DIFFERENT residues mod 3! (one ≡1, other ≡2)")
    
    # Verify for O = p²q
    print()
    print("Verification for O = p²q:")
    p2q_theory_correct = 0
    p2q_theory_wrong = 0
    p2q_details = []
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue
        
        O = B // 2
        O_factors = factorize(O)
        
        # O = p²q (one prime to power 2, one to power 1)
        if len(O_factors) != 2:
            continue
        exponents = sorted(O_factors.values())
        if exponents != [1, 2]:
            continue
        
        primes = list(O_factors.keys())
        # p is the one with exponent 2
        if O_factors[primes[0]] == 2:
            p, q = primes[0], primes[1]
        else:
            p, q = primes[1], primes[0]
        
        p_mod3 = p % 3
        q_mod3 = q % 3
        
        # Theory: works iff q≡2(mod 3) [via d=p] OR (p mod 3 ≠ q mod 3) [via d=p²]
        # i.e., works iff q≡2(mod 3) OR p≡1,q≡2 OR p≡2,q≡1
        # = q≡2(mod 3) OR (p mod 3 ≠ q mod 3)
        # = q≡2(mod 3) OR p mod 3 ≠ q mod 3
        
        # If p≡1,q≡1: q≠2, same mod 3 → theory says FAILS
        # If p≡2,q≡2: q≡2 → theory says WORKS (d=p)
        # If p≡1,q≡2: q≡2 → theory says WORKS
        # If p≡2,q≡1: q≠2 but different mod 3 → theory says WORKS (d=p²)
        # So theory says fails ONLY when p≡1(mod 3) and q≡1(mod 3)
        theory_says_works = not (p_mod3 == 1 and q_mod3 == 1)
        
        # Check actual
        O2 = O * O
        divs_O = divisors_of(O2)
        found = False
        for d_odd in divs_O:
            if d_odd > O:
                break
            if (d_odd + 2 * O + O2 // d_odd) % 9 == 0:
                found = True
                break
        
        if found == theory_says_works:
            p2q_theory_correct += 1
        else:
            p2q_theory_wrong += 1
            p2q_details.append({
                'n': n, 'O': O, 'p': p, 'q': q, 
                'p_mod3': p_mod3, 'q_mod3': q_mod3,
                'theory_says': theory_says_works, 'actual': found
            })
    
    total_p2q = p2q_theory_correct + p2q_theory_wrong
    if total_p2q > 0:
        print(f"  Theory correct: {p2q_theory_correct}/{total_p2q} ({100*p2q_theory_correct/total_p2q:.1f}%)")
        print(f"  Theory wrong: {p2q_theory_wrong}")
    if p2q_details:
        for d in p2q_details[:10]:
            print(f"    n={d['n']}, O={d['O']}, p={d['p']}≡{d['p_mod3']}, q={d['q']}≡{d['q_mod3']}, theory={d['theory_says']}, actual={d['actual']}")
    
    # GENERAL THEORY: For ANY O (not just 2-prime), when does A=3 fail?
    # Hypothesis: A=3 fails (for v₂(B)=1) iff ALL prime factors of O are ≡ 1 (mod 3)
    
    print(f"\n{'='*60}")
    print("GENERAL HYPOTHESIS: A=3 fails (v₂(B)=1) iff all primes of O are ≡ 1 (mod 3)")
    print("="*60)
    
    hyp_correct = 0
    hyp_wrong = 0
    hyp_wrong_details = []
    
    all_primes_1mod3_works = 0
    all_primes_1mod3_fails = 0
    some_prime_2mod3_works = 0
    some_prime_2mod3_fails = 0
    
    for n in range(13, max_n + 1):
        if n % 12 != 1 or n % 5 == 0:
            continue
        B = n * (n + 3) // 2
        if B % 4 == 0:
            continue
        
        O = B // 2
        O_factors = factorize(O)
        
        # Check if all prime factors ≡ 1 (mod 3)
        all_1mod3 = all(p % 3 == 1 for p in O_factors.keys())
        
        # Check if A=3 works
        O2 = O * O
        divs_O = divisors_of(O2)
        found = False
        for d_odd in divs_O:
            if d_odd > O:
                break
            if (d_odd + 2 * O + O2 // d_odd) % 9 == 0:
                found = True
                break
        
        if all_1mod3:
            if found:
                all_primes_1mod3_works += 1
            else:
                all_primes_1mod3_fails += 1
        else:
            if found:
                some_prime_2mod3_works += 1
            else:
                some_prime_2mod3_fails += 1
        
        # Theory: fails iff all primes ≡ 1 mod 3
        theory_says_works = not all_1mod3
        
        if found == theory_says_works:
            hyp_correct += 1
        else:
            hyp_wrong += 1
            if len(hyp_wrong_details) < 20:
                hyp_wrong_details.append({
                    'n': n, 'O': O, 'O_factors': O_factors,
                    'all_1mod3': all_1mod3, 'found': found
                })
    
    total_hyp = hyp_correct + hyp_wrong
    print(f"  Theory correct: {hyp_correct}/{total_hyp} ({100*hyp_correct/total_hyp:.2f}%)")
    print(f"  Theory wrong: {hyp_wrong}")
    print(f"  All primes ≡1(mod 3): works={all_primes_1mod3_works}, fails={all_primes_1mod3_fails}")
    print(f"  Some prime ≡2(mod 3): works={some_prime_2mod3_works}, fails={some_prime_2mod3_fails}")
    
    if hyp_wrong_details:
        print(f"\n  WRONG cases:")
        for d in hyp_wrong_details:
            print(f"    n={d['n']}, O={d['O']}, factors={d['O_factors']}, all≡1(mod3)={d['all_1mod3']}, found={d['found']}")
    
    # If hypothesis is wrong, let's check if it's about higher prime powers
    if hyp_wrong > 0:
        print(f"\n  Analyzing wrong cases...")
        for d in hyp_wrong_details:
            O = d['O']
            factors = d['O_factors']
            # Check each divisor
            O2 = O * O
            divs = divisors_of(O2)
            mod9_vals = set()
            for dd in divs:
                if dd > O:
                    break
                mod9_vals.add((dd + 2*O + O2//dd) % 9)
            print(f"    O={O}, factors={factors}, mod9 residues={sorted(mod9_vals)}")
    
    # PROOF OF THE HYPOTHESIS (if correct):
    # If all primes of O are ≡ 1 (mod 3), then every divisor d of O² satisfies d ≡ 1 (mod 3).
    # So d + 2O + O²/d ≡ 1 + 2·1 + 1 = 4 ≡ 1 (mod 3). Hence NOT ≡ 0 (mod 9).
    # Conversely, if some prime p|O has p ≡ 2 (mod 3), then d = p^{v_p(O)} gives...
    # Actually, the key is: d = p (or p^k) can make d ≡ 2 (mod 3) or ≡ 1 (mod 3) depending on k.
    
    print(f"\n{'='*60}")
    print("PROOF OF HYPOTHESIS")
    print("="*60)
    print("""
If ALL prime factors of O are ≡ 1 (mod 3):
  Every divisor d of O² satisfies d ≡ 1 (mod 3).
  Also O ≡ 1 (mod 3), so O²/d ≡ 1 (mod 3).
  d + 2O + O²/d ≡ 1 + 2 + 1 = 4 ≡ 1 (mod 3).
  So the sum is NOT divisible by 3, hence NOT by 9.
  → A=3 FAILS. ✓

If SOME prime p|O has p ≡ 2 (mod 3):
  Let p have exponent e in O, so p^{2e} | O².
  Consider d = p^a for odd a (1 ≤ a ≤ 2e, a odd):
    d ≡ p^a ≡ 2^a ≡ 2 (mod 3) (since 2^odd ≡ 2 mod 3)
    O²/d = (O²/p^a), and since O has p^e, O²/p^a = p^{2e-a} · (O/p^e)²
    Since 2e-a is odd (even-odd=odd), O²/d ≡ 2 · 1 ≡ 2 (mod 3) if 2e-a is odd
    Actually: O²/d ≡ (O/p^e)² · p^{2e-a}. (O/p^e) ≡ 1 mod 3 (all its primes ≡1). 
    p^{2e-a} ≡ 2^{2e-a} (mod 3). 2e-a is odd, so ≡ 2 (mod 3).
    So O²/d ≡ 2 (mod 3).
    d + 2O + O²/d ≡ 2 + 2 + 2 = 6 ≡ 0 (mod 3). ✓
    
    But we need ≡ 0 (mod 9), not just mod 3!
    
  The condition mod 9 is more subtle. Let's check:
  d + 2O + O²/d mod 9, with d = p (a=1):
    p + 2O + O²/p
    = p + 2p^e · Q + p^{2e-1} · Q²  where Q = O/p^e, Q ≡ 1 mod 3
    ≡ p + 2p^e · Q + p^{2e-1} · Q² (mod 9)
    
  This is more complex. The mod 3 analysis shows divisibility by 3 is guaranteed,
  but mod 9 requires more.
""")

if __name__ == '__main__':
    main()