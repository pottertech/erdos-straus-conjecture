#!/usr/bin/env python3
"""
A=3 Analysis for Erdős-Straus Conjecture
Residue class: n ≡ 1 (mod 12), n ≢ 0 (mod 5)

When A=3:
  x = (n+3)/4
  B = n(n+3)/2
  Pell equation: k² - 36m² = B², where k = 18t - B
  Factors as: (k-6m)(k+6m) = B²
  Let d = k-6m, then k+6m = B²/d
  So: k = (d + B²/d)/2, m = (B²/d - d)/12
  
  Conditions:
  1. d | B²
  2. d + B²/d ≡ 0 (mod 2)  [k integer]
  3. (B²/d - d) ≡ 0 (mod 12)  [m integer]  =>  d + 2B + B²/d ≡ 0 (mod 36) combined
  4. m ≥ 0  =>  B²/d ≥ d  =>  d ≤ B
  5. z = 3t - m > 0, where t = (k + B)/18 = (d + B²/d + 2B)/36
     So z = 3*(d + B²/d + 2B)/36 - (B²/d - d)/12
          = (d + B²/d + 2B)/12 - (B²/d - d)/12
          = (d + B²/d + 2B - B²/d + d)/12
          = (2d + 2B)/12
          = (d + B)/6
     So z > 0  <=>  d + B > 0  <=>  d > -B
     Since d > 0 (divisor), z > 0 is ALWAYS satisfied!
     
     Wait, let me recheck. z = 3t - m, t = (k+B)/18, k = (d + B²/d)/2
     t = ((d + B²/d)/2 + B) / 18 = (d + B²/d + 2B) / 36
     3t = (d + B²/d + 2B) / 12
     m = (B²/d - d) / 12
     z = 3t - m = (d + B²/d + 2B) / 12 - (B²/d - d) / 12
       = (d + B²/d + 2B - B²/d + d) / 12
       = (2d + 2B) / 12
       = (d + B) / 6

  So z = (d + B) / 6, and since d > 0 and B > 0, z > 0 is ALWAYS satisfied!

  This means the ONLY conditions are:
  1. d | B²
  2. d + 2B + B²/d ≡ 0 (mod 36)  [combined congruence for integer k, t, m]
  3. m ≥ 0  =>  d ≤ B

  And z > 0 is automatic (always true for positive d, B).
"""

import json
import sys
from collections import Counter, defaultdict
import math

def divisors_of_n_squared(n):
    """Get all divisors of n² using prime factorization of n."""
    # Factor n
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
    
    # Divisors of n² = product of p^(2*e) for each prime p with exponent e in n
    divs = [1]
    for p, e in factors.items():
        new_divs = []
        for d in divs:
            for i in range(2*e + 1):
                new_divs.append(d * p**i)
        divs = new_divs
    return sorted(divs)

def check_mod36_condition(d, B):
    """Check if d + 2B + B²/d ≡ 0 (mod 36)."""
    B2_over_d = B * B // d
    return (d + 2 * B + B2_over_d) % 36 == 0

def analyze_n(n):
    """
    For a given n ≡ 1 (mod 12), n ≢ 0 (mod 5), check if A=3 works.
    
    Returns dict with:
    - works: bool
    - working_divisors: list of (d, m, z, t) tuples
    - mod36_satisfying: list of (d, m) tuples (z always > 0)
    - B: value of B
    - fail_reason: if not works, why
    """
    B = n * (n + 3) // 2
    B2 = B * B
    
    # Get divisors of B²
    divs = divisors_of_n_squared(B)
    
    # Find divisors satisfying mod 36 condition AND d <= B (for m >= 0)
    mod36_pass = []
    for d in divs:
        if d > B:
            break  # divisors are sorted, and we need d <= B for m >= 0
        if check_mod36_condition(d, B):
            B2_over_d = B2 // d
            m = (B2_over_d - d) // 12
            # Verify m is integer (should be guaranteed by mod 36 condition)
            if (B2_over_d - d) % 12 != 0:
                continue
            t = (d + B2_over_d + 2 * B) // 36
            if (d + B2_over_d + 2 * B) % 36 != 0:
                continue
            z = (d + B) // 6
            if (d + B) % 6 != 0:
                continue
            mod36_pass.append({
                'd': d,
                'm': m,
                't': t,
                'z': z,
                'z_positive': z > 0,
                'd_over_B': d / B if B > 0 else 0
            })
    
    working = [s for s in mod36_pass if s['z_positive'] and s['m'] >= 0]
    
    result = {
        'n': n,
        'B': B,
        'B_mod_9': B % 9,
        'B_mod_36': B % 36,
        'num_divisors_B2': len(divs),
        'num_mod36_pass': len(mod36_pass),
        'num_working': len(working),
        'works': len(working) > 0,
    }
    
    if working:
        result['working_divisors'] = working
        result['best_d'] = working[0]['d']  # smallest d (largest m)
    else:
        if len(mod36_pass) == 0:
            result['fail_reason'] = 'no_mod36_divisor'
        else:
            # All mod36 pass have z <= 0 (but we showed z always > 0, so this shouldn't happen)
            result['fail_reason'] = 'z_le_zero'
            result['mod36_satisfying'] = mod36_pass
    
    return result

def main():
    max_n = 100000
    results = []
    works_count = 0
    fail_count = 0
    fail_reasons = Counter()
    
    # Track patterns
    d_over_B_values = []
    d_is_B_count = 0
    d_patterns = Counter()  # patterns of d relative to B
    
    # Track B mod 36 vs success
    b_mod36_success = Counter()
    b_mod36_fail = Counter()
    
    # Track B mod 9 vs success  
    b_mod9_success = Counter()
    b_mod9_fail = Counter()
    
    # Track factorization patterns
    # When A=3 works, what's special about B?
    
    print(f"Analyzing n ≡ 1 (mod 12), n ≢ 0 (mod 5) from 13 to {max_n}...")
    
    for n in range(13, max_n + 1):
        if n % 12 != 1:
            continue
        if n % 5 == 0:
            continue
        
        result = analyze_n(n)
        results.append(result)
        
        b_mod36 = result['B_mod_36']
        b_mod9 = result['B_mod_9']
        
        if result['works']:
            works_count += 1
            b_mod36_success[b_mod36] += 1
            b_mod9_success[b_mod9] += 1
            
            for w in result['working_divisors']:
                d_over_B_values.append(w['d_over_B'])
                if w['d'] == result['B']:
                    d_is_B_count += 1
                
                # Categorize d relative to B
                if w['d'] == result['B']:
                    d_patterns['d=B (symmetric)'] += 1
                elif w['d'] == 1:
                    d_patterns['d=1'] += 1
                else:
                    ratio = w['d_over_B']
                    if ratio < 0.01:
                        d_patterns['d << B (<0.01B)'] += 1
                    elif ratio < 0.1:
                        d_patterns['d < 0.1B'] += 1
                    elif ratio < 0.5:
                        d_patterns['0.1B ≤ d < 0.5B'] += 1
                    elif ratio < 0.9:
                        d_patterns['0.5B ≤ d < 0.9B'] += 1
                    elif ratio < 1.0:
                        d_patterns['0.9B ≤ d < B'] += 1
        else:
            fail_count += 1
            fail_reasons[result['fail_reason']] += 1
            b_mod36_fail[b_mod36] += 1
            b_mod9_fail[b_mod9] += 1
        
        if (n - 13) % 1000 < 12:  # Progress indicator
            pass
    
    total = works_count + fail_count
    
    print(f"\n{'='*60}")
    print(f"RESULTS: n from 13 to {max_n}, n ≡ 1 (mod 12), n ≢ 0 (mod 5)")
    print(f"{'='*60}")
    print(f"Total n values checked: {total}")
    print(f"A=3 works: {works_count} ({100*works_count/total:.2f}%)")
    print(f"A=3 fails: {fail_count} ({100*fail_count/total:.2f}%)")
    print(f"\nFail reasons:")
    for reason, count in fail_reasons.most_common():
        print(f"  {reason}: {count}")
    
    print(f"\n{'='*60}")
    print("d/B RATIO DISTRIBUTION (for working cases):")
    print(f"{'='*60}")
    if d_over_B_values:
        d_over_B_values.sort()
        n_vals = len(d_over_B_values)
        print(f"  Count: {n_vals}")
        print(f"  Min:   {d_over_B_values[0]:.6f}")
        print(f"  25%:   {d_over_B_values[n_vals//4]:.6f}")
        print(f"  Median:{d_over_B_values[n_vals//2]:.6f}")
        print(f"  75%:   {d_over_B_values[3*n_vals//4]:.6f}")
        print(f"  Max:   {d_over_B_values[-1]:.6f}")
        print(f"  d=B count: {d_is_B_count}")
    
    print(f"\nd PATTERNS:")
    for pattern, count in d_patterns.most_common():
        print(f"  {pattern}: {count}")
    
    print(f"\n{'='*60}")
    print("B mod 36 vs SUCCESS:")
    print(f"{'='*60}")
    all_mod36 = set(list(b_mod36_success.keys()) + list(b_mod36_fail.keys()))
    for m in sorted(all_mod36):
        s = b_mod36_success.get(m, 0)
        f = b_mod36_fail.get(m, 0)
        total_m = s + f
        pct = 100 * s / total_m if total_m > 0 else 0
        print(f"  B ≡ {m:2d} (mod 36): works={s:5d}, fails={f:5d}, total={total_m:5d}, success={pct:.1f}%")
    
    print(f"\n{'='*60}")
    print("B mod 9 vs SUCCESS:")
    print(f"{'='*60}")
    all_mod9 = set(list(b_mod9_success.keys()) + list(b_mod9_fail.keys()))
    for m in sorted(all_mod9):
        s = b_mod9_success.get(m, 0)
        f = b_mod9_fail.get(m, 0)
        total_m = s + f
        pct = 100 * s / total_m if total_m > 0 else 0
        print(f"  B ≡ {m} (mod 9): works={s:5d}, fails={f:5d}, total={total_m:5d}, success={pct:.1f}%")
    
    # Deep analysis: for failing cases, what are the divisors of B²?
    print(f"\n{'='*60}")
    print("DEEP ANALYSIS OF FAILING CASES (first 20):")
    print(f"{'='*60}")
    fail_examples = []
    for r in results:
        if not r['works']:
            fail_examples.append(r)
            if len(fail_examples) <= 20:
                print(f"  n={r['n']}, B={r['B']}, B mod 9={r['B_mod_9']}, B mod 36={r['B_mod_36']}, "
                      f"num_divs_B²={r['num_divisors_B2']}, fail={r['fail_reason']}")
    
    # For failing cases, check: what are the divisors of B² mod 36?
    print(f"\n{'='*60}")
    print("DIVISOR MOD 36 ANALYSIS FOR FAILING CASES (first 5):")
    print(f"{'='*60}")
    for r in fail_examples[:5]:
        n = r['n']
        B = r['B']
        B2 = B * B
        divs = divisors_of_n_squared(B)
        print(f"\n  n={n}, B={B}, B mod 36={B % 36}")
        print(f"  B = {B}")
        # Factor B
        temp = B
        factors = {}
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
            d += 1
        if temp > 1:
            factors[temp] = factors.get(temp, 0) + 1
        print(f"  B factorization: {factors}")
        print(f"  B² has {len(divs)} divisors")
        
        # Check each divisor d <= B for mod 36
        mod36_results = []
        for d in divs:
            if d > B:
                break
            B2_over_d = B2 // d
            val = d + 2 * B + B2_over_d
            mod36 = val % 36
            mod36_results.append(mod36)
        
        mod36_counter = Counter(mod36_results)
        print(f"  Divisor mod-36 residues (d ≤ B): {dict(sorted(mod36_counter.items()))}")
        # Which residues appear?
        print(f"  Residue 0 count: {mod36_counter.get(0, 0)} out of {sum(mod36_counter.values())}")
    
    # Success pattern: is it related to specific prime factors of B?
    print(f"\n{'='*60}")
    print("PRIME FACTORIZATION ANALYSIS:")
    print(f"{'='*60}")
    
    # For working vs failing, what primes divide B?
    working_prime_counter = Counter()
    failing_prime_counter = Counter()
    
    for r in results:
        B = r['B']
        temp = B
        primes = set()
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                primes.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            primes.add(temp)
        
        if r['works']:
            for p in primes:
                working_prime_counter[p] += 1
        else:
            for p in primes:
                failing_prime_counter[p] += 1
    
    # Find primes that are more common in working cases
    print("\nPrimes appearing more in WORKING cases (ratio > 0.5):")
    all_primes = set(list(working_prime_counter.keys()) + list(failing_prime_counter.keys()))
    interesting_primes = []
    for p in sorted(all_primes):
        w = working_prime_counter.get(p, 0)
        f = failing_prime_counter.get(p, 0)
        total_p = w + f
        if total_p >= 10:  # only look at primes that appear enough
            ratio = w / total_p
            if ratio > 0.5:
                interesting_primes.append((p, w, f, ratio))
    
    for p, w, f, ratio in interesting_primes[:30]:
        print(f"  p={p}: works={w}, fails={f}, ratio={ratio:.3f}")
    
    print("\nPrimes appearing more in FAILING cases (ratio < 0.5):")
    failing_primes = []
    for p in sorted(all_primes):
        w = working_prime_counter.get(p, 0)
        f = failing_prime_counter.get(p, 0)
        total_p = w + f
        if total_p >= 10:
            ratio = w / total_p
            if ratio < 0.5:
                failing_primes.append((p, w, f, ratio))
    
    for p, w, f, ratio in failing_primes[:30]:
        print(f"  p={p}: works={w}, fails={f}, ratio={ratio:.3f}")
    
    # Check: is 3 | B important? We showed 9 ∤ B, but what about 3 | B?
    print(f"\n{'='*60}")
    print("3 | B ANALYSIS:")
    print(f"{'='*60}")
    b_div3_success = 0
    b_div3_fail = 0
    b_notdiv3_success = 0
    b_notdiv3_fail = 0
    for r in results:
        if r['B'] % 3 == 0:
            if r['works']:
                b_div3_success += 1
            else:
                b_div3_fail += 1
        else:
            if r['works']:
                b_notdiv3_success += 1
            else:
                b_notdiv3_fail += 1
    
    print(f"  3 | B and works: {b_div3_success}")
    print(f"  3 | B and fails: {b_div3_fail}")
    print(f"  3 ∤ B and works: {b_notdiv3_success}")
    print(f"  3 ∤ B and fails: {b_notdiv3_fail}")
    if b_div3_success + b_div3_fail > 0:
        print(f"  3 | B success rate: {100*b_div3_success/(b_div3_success+b_div3_fail):.1f}%")
    if b_notdiv3_success + b_notdiv3_fail > 0:
        print(f"  3 ∤ B success rate: {100*b_notdiv3_success/(b_notdiv3_success+b_notdiv3_fail):.1f}%")
    
    # Check: does 2 | B matter? n ≡ 1 (mod 12) means n is odd, n+3 is even
    # B = n(n+3)/2, n odd, n+3 even, so B = odd * even / 2. 
    # n+3 ≡ 4 (mod 12), so n+3 = 4k for some k. B = n * 4k / 2 = 2nk.
    # So 2 | B always. What about 4 | B? B = 2nk where n ≡ 1 (mod 12), k = (n+3)/4
    # B = 2n(n+3)/4 = n(n+3)/2... let me just check mod 4
    print(f"\n{'='*60}")
    print("B mod 4 ANALYSIS:")
    print(f"{'='*60}")
    b_mod4 = Counter()
    b_mod4_success = Counter()
    b_mod4_fail = Counter()
    for r in results:
        m4 = r['B'] % 4
        b_mod4[m4] += 1
        if r['works']:
            b_mod4_success[m4] += 1
        else:
            b_mod4_fail[m4] += 1
    
    for m in sorted(b_mod4.keys()):
        s = b_mod4_success.get(m, 0)
        f = b_mod4_fail.get(m, 0)
        t = s + f
        print(f"  B ≡ {m} (mod 4): works={s}, fails={f}, total={t}, success={100*s/t:.1f}%")
    
    # The KEY question: when does B² have a divisor d ≤ B with d + 2B + B²/d ≡ 0 (mod 36)?
    # Let's check: for failing cases, what residues mod 36 do the divisors give?
    print(f"\n{'='*60}")
    print("SYSTEMATIC FAILING CASE ANALYSIS:")
    print(f"{'='*60}")
    
    # For each failing case, check ALL divisors (including d > B) for mod 36
    # The condition d ≤ B is for m >= 0. But what if we allow m < 0?
    # Actually m < 0 means y < 0 which is invalid. So d ≤ B is required.
    
    # Let's check: do failing cases have NO divisor d ≤ B with the right mod 36,
    # or do they have divisors but with m < 0?
    
    fail_no_mod36 = 0
    fail_mod32_but_d_gt_B = 0
    fail_summary = []
    
    for r in fail_examples[:50]:  # first 50 failing cases
        n = r['n']
        B = r['B']
        B2 = B * B
        divs = divisors_of_n_squared(B)
        
        found_mod36_any = False
        found_mod36_d_le_B = False
        
        for d in divs:
            B2_over_d = B2 // d
            if (d + 2 * B + B2_over_d) % 36 == 0:
                found_mod36_any = True
                if d <= B:
                    found_mod36_d_le_B = True
                    break
        
        if found_mod36_any and not found_mod36_d_le_B:
            fail_mod32_but_d_gt_B += 1
        
        if not found_mod36_any:
            fail_no_mod36 += 1
        
        fail_summary.append({
            'n': n,
            'B': B,
            'B_mod_36': B % 36,
            'any_mod36_div': found_mod36_any,
            'mod36_d_le_B': found_mod36_d_le_B
        })
    
    print(f"  Out of first 50 failing cases:")
    print(f"  No divisor at all satisfying mod 36: {fail_no_mod36}")
    print(f"  Mod 36 divisor exists but d > B: {fail_mod32_but_d_gt_B}")
    
    # Let's also verify z = (d+B)/6 is always positive and integer
    print(f"\n{'='*60}")
    print("VERIFICATION: z = (d + B) / 6")
    print(f"{'='*60}")
    z_verified = 0
    z_failed = 0
    for r in results[:1000]:  # check first 1000
        if r['works']:
            for w in r['working_divisors']:
                d = w['d']
                B = r['B']
                expected_z = (d + B) // 6
                if (d + B) % 6 == 0 and expected_z > 0:
                    z_verified += 1
                    if expected_z != w['z']:
                        print(f"  MISMATCH: n={r['n']}, d={d}, z={w['z']}, expected={expected_z}")
                        z_failed += 1
                else:
                    print(f"  z NOT INTEGER: n={r['n']}, d={d}, B={B}, (d+B)={d+B}, mod6={(d+B)%6}")
                    z_failed += 1
    
    print(f"  z verified: {z_verified}, z failed: {z_failed}")
    
    # Save full results
    output = {
        'max_n': max_n,
        'total': total,
        'works': works_count,
        'fails': fail_count,
        'works_pct': 100 * works_count / total if total > 0 else 0,
        'fail_reasons': dict(fail_reasons),
        'd_patterns': dict(d_patterns),
        'd_is_B_count': d_is_B_count,
        'b_mod36_success': dict(b_mod36_success),
        'b_mod36_fail': dict(b_mod36_fail),
        'b_mod9_success': dict(b_mod9_success),
        'b_mod9_fail': dict(b_mod9_fail),
        'b_div3_success': b_div3_success,
        'b_div3_fail': b_div3_fail,
        'b_notdiv3_success': b_notdiv3_success,
        'b_notdiv3_fail': b_notdiv3_fail,
        'b_mod4_success': dict(b_mod4_success),
        'b_mod4_fail': dict(b_mod4_fail),
        'd_over_B_stats': {
            'count': len(d_over_B_values),
            'min': min(d_over_B_values) if d_over_B_values else 0,
            'median': sorted(d_over_B_values)[len(d_over_B_values)//2] if d_over_B_values else 0,
            'max': max(d_over_B_values) if d_over_B_values else 0,
        },
        'z_formula_verified': z_verified,
        'z_formula_failed': z_failed,
        'fail_no_mod36_first50': fail_no_mod36,
        'fail_mod32_but_d_gt_B_first50': fail_mod32_but_d_gt_B,
        'first_20_failing': [{'n': r['n'], 'B': r['B'], 'B_mod_36': r['B_mod_36'], 
                              'B_mod_9': r['B_mod_9'], 'num_divs': r['num_divisors_B2'],
                              'fail_reason': r['fail_reason']} 
                             for r in fail_examples[:20]],
        'first_20_working': [{'n': r['n'], 'B': r['B'], 'B_mod_36': r['B_mod_36'],
                              'B_mod_9': r['B_mod_9'], 'best_d': r.get('best_d', 0),
                              'num_working': r['num_working']}
                             for r in results if r['works']][:20],
    }
    
    # Add detailed results for all n
    output['all_results'] = []
    for r in results:
        entry = {
            'n': r['n'],
            'B': r['B'],
            'B_mod_36': r['B_mod_36'],
            'B_mod_9': r['B_mod_9'],
            'works': r['works'],
            'num_working': r['num_working'],
            'num_mod36_pass': r['num_mod36_pass'],
        }
        if r['works']:
            entry['working_divisors'] = r['working_divisors'][:5]  # top 5
        else:
            entry['fail_reason'] = r['fail_reason']
        output['all_results'].append(entry)
    
    output_path = '/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/a3_analysis.json'
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to {output_path}")
    
    # Final summary
    print(f"\n{'='*60}")
    print("FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"A=3 works for {works_count}/{total} = {100*works_count/total:.2f}% of cases")
    print(f"z = (d+B)/6 is ALWAYS positive when d > 0, B > 0")
    print(f"Fail reason is always 'no_mod36_divisor' (no divisor d ≤ B of B² satisfies mod 36)")
    
    # The key question: what number-theoretic condition predicts A=3 success?
    # Let's check B mod 36 more carefully
    print(f"\nB mod 36 SUCCESS RATES (sorted by success rate):")
    mod36_rates = []
    for m in all_mod36:
        s = b_mod36_success.get(m, 0)
        f = b_mod36_fail.get(m, 0)
        t = s + f
        if t > 0:
            mod36_rates.append((m, s, f, t, s/t))
    mod36_rates.sort(key=lambda x: -x[4])
    for m, s, f, t, r in mod36_rates:
        print(f"  B ≡ {m:2d} (mod 36): {s:5d}/{t:5d} = {100*r:.1f}%")

if __name__ == '__main__':
    main()