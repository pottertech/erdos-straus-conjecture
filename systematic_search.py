#!/usr/bin/env python3
"""
Systematic search for Erdős-Straus solutions for n ≡ 1 (mod 12), n ≢ 0 (mod 5).
For each n, search x from ceil(n/4) upward, and for each x find y, z such that
4/n = 1/x + 1/y + 1/z.

Mathematical approach:
  4/n - 1/x = (4x - n)/(nx) = remainder
  We need 1/y + 1/z = remainder = (4x-n)/(nx)
  
  Let r_num = 4x - n, r_den = nx. Then remainder = r_num/r_den.
  We need 1/y + 1/z = r_num/r_den, i.e., (y+z)/(yz) = r_num/r_den.
  
  Cross-multiplying: r_den*(y+z) = r_num*yz
  Let s = y+z, p = yz. Then r_num * p = r_den * s, so p = r_den * s / r_num.
  For p integer, need r_num | r_den * s.
  
  y and z are roots of t² - s*t + p = 0.
  Discriminant: D = s² - 4p = s² - 4*r_den*s/r_num = s(s - 4*r_den/r_num)
  For D to be a perfect square (and real), need s >= 4*r_den/r_num = 4*nx/(4x-n).
  
  Alternative direct approach: for each x, compute remainder = (4x-n)/(nx),
  then for each divisor d of r_num, set 1/y = d/(nx), so y = nx/d,
  then 1/z = (r_num - d)/(nx), so z = nx/(r_num - d).
  Both d and r_num - d must be positive, so 0 < d < r_num.
  And both y = nx/d and z = nx/(r_num-d) must be integers, i.e., d | nx and (r_num-d) | nx.
  
  Actually simpler: 4/n - 1/x = (4x-n)/(nx). 
  We want to write this as 1/y + 1/z where y <= z.
  Set 1/y + 1/z = (4x-n)/(nx).
  
  A standard decomposition: if a/b = 1/y + 1/z, then for each divisor e of a*b with e <= sqrt(a*b),
  we can try y = b*e/a... hmm, let me use a cleaner approach.
  
  Actually the cleanest: 
  remainder = (4x-n)/(nx) = A/B where A = 4x-n, B = nx.
  We want 1/y + 1/z = A/B.
  So B*(y+z) = A*yz => A*yz - B*y - B*z = 0 => (Ay - B)(Az - B) = B²
  So (Ay-B)(Az-B) = B², meaning we need factorizations of B².
  
  For each divisor f1 of B² with f1 <= B (so y <= z), set Ay - B = f1, Az - B = B²/f1.
  Then y = (f1 + B)/A, z = (B²/f1 + B)/A = B(B/f1 + 1)/A.
  Both must be positive integers.
  
  This is the most efficient approach. B = nx can be large, but B² factorization
  via trial division up to sqrt(B²) = B = nx is feasible for moderate n.
  
  For large n, we use a simpler approach: iterate y from ceil(B/A) upward
  and check if z = B*y/(A*y - B) is a positive integer.
"""

import json
import math
import time
from fractions import Fraction
from collections import defaultdict

def find_solution(n, x_max_mult=3):
    """
    Find x, y, z with 4/n = 1/x + 1/y + 1/z.
    Search x from ceil(n/4) to x_max_mult * n.
    For each x, use the divisor method on B² = (nx)².
    """
    x_min = math.ceil(n / 4)
    x_max = x_max_mult * n
    
    for x in range(x_min, x_max + 1):
        A = 4 * x - n
        B = n * x
        if A <= 0:
            continue
        
        # We need (Ay - B)(Az - B) = B²
        # Let f1 = Ay - B, f2 = Az - B, f1 * f2 = B²
        # y = (f1 + B) / A, z = (f2 + B) / A
        # Need f1 | B² effectively, and (f1 + B) % A == 0, (f2 + B) % A == 0
        # where f2 = B² / f1
        
        # For efficiency, iterate f1 over divisors of B².
        # B² = (nx)². Its divisors can be found by factoring nx.
        # But for large nx, factoring is slow. Use the y-iteration approach instead.
        
        # y-iteration approach: y ranges from ceil(B/A) to floor(2B/A)
        # because 1/y <= A/B so y >= B/A, and 1/y >= A/(2B) so y <= 2B/A (since 1/z >= 1/y... no)
        # Actually y >= ceil(B/A) since 1/y <= A/B (because 1/y <= remainder, as 1/z > 0)
        # And y <= 2*B/A since 1/y >= remainder/2 (because y <= z so 1/y >= 1/z, thus 1/y >= remainder/2)
        
        y_min = math.ceil(B / A)
        # Upper bound: when z >= y, 1/y >= A/(2B), so y <= 2B/A
        # But we also cap y to keep search reasonable
        y_max = min(2 * B // A + 1, B)  # Don't search more than B values
        
        for y in range(y_min, y_max + 1):
            # 1/z = A/B - 1/y = (Ay - B) / (By)
            # z = By / (Ay - B)
            num = A * y - B
            if num <= 0:
                continue
            if (B * y) % num != 0:
                continue
            z = (B * y) // num
            if z < y:
                continue
            # Verify
            if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n):
                return (x, y, z)
    
    return None

def find_solution_optimized(n, x_max_mult=3):
    """
    Optimized version: for each x, use the divisor-pair approach on B² = (nx)².
    (Ay - B)(Az - B) = B²
    f1 * f2 = B², y = (f1 + B)/A, z = (f2 + B)/A
    We iterate f1 over divisors of B (not B²) since B²'s divisors are products
    of divisors of B. Actually, let's just iterate f1 = Ay - B directly.
    
    f1 = Ay - B, so y = (f1 + B)/A. Need f1 > 0 and A | (f1 + B).
    f2 = B²/f1, so z = (f2 + B)/A. Need A | (f2 + B).
    
    f1 ranges from 1 to B (since y <= z means f1 <= f2, and f1*f2 = B², so f1 <= B).
    
    For each f1 from 1 to B:
      - check A | (f1 + B)  =>  f1 ≡ -B (mod A), i.e., f1 ≡ (A - B%A) % A
      - check f1 | B²
      - compute f2 = B² / f1
      - check A | (f2 + B)
    
    This is still O(B) per x which is O(n*x). Too slow for large n.
    
    Better: factorize B = nx, get divisors of B, then divisors of B² are 
    d1*d2 where d1|B and d2|B... no, divisors of B² = {d : d | B²}.
    
    Let's use a different strategy. For each x:
    - A = 4x - n, B = nx
    - f1 must be ≡ -B (mod A) and f1 | B²
    - So f1 = k*A - B%... let me think.
    - f1 ≡ -B (mod A), so f1 = A*t - B for t = 1, 2, 3, ...
    - Then y = t (nice!), and z = (B²/f1 + B)/A = B*(B/f1 + 1)/A
    - f1 = At - B = A*y - B (consistent)
    - Need f1 | B², i.e., (Ay - B) | (nx)²
    - And z = B²/f1 + B)/A = (B²/(Ay-B) + B)/A = B*(B + Ay - B)/(A*(Ay-B)) = B*y/(Ay-B) ... 
      wait that's the same as before.
    
    OK the y-iteration is the simplest. Let me optimize the y-range.
    For the y-iteration: z = By/(Ay-B), need z integer and z >= y.
    Ay - B > 0 => y > B/A.
    z >= y => By/(Ay-B) >= y => B/(Ay-B) >= 1 => B >= Ay - B => A*y <= 2B => y <= 2B/A.
    
    So y ranges from ceil(B/A) + (0 or 1 to ensure Ay-B > 0) to floor(2B/A).
    The range size is about B/A = nx/(4x-n).
    
    For x close to n/4, A = 4x-n is small, range is huge.
    For x = ceil(n/4), A is small (like 1-3), so range ~ nx which is huge.
    
    We need a smarter approach for small A. 
    
    When A is small (say A = 1), remainder = 1/(nx), so we need 1/y + 1/z = 1/(nx).
    This means y = nx+1, z = nx(nx+1) or y = nx+d, z = nx(nx+d)/d for d | nx.
    Actually 1/y + 1/z = 1/B means (y-B)(z-B) = B², so we factor B².
    
    For A = 1: B = nx, need (y - B)(z - B) = B². 
    Factor B = nx, find all divisors of B (which give factorizations of B² via B = d*B/d).
    Divisors of B² that are <= B: for each divisor d of B, the divisors of B² that are 
    products... actually divisors of B² = {d : d | B²}. If B = p1^a1 * p2^a2 * ..., 
    then B² = p1^(2a1) * ..., and divisors of B² = {p1^b1 * ... : 0 <= bi <= 2ai}.
    
    The most practical approach for our range: use the y-iteration but with
    an early exit and a cap on the number of y values to try.
    
    For x close to n/4 where A is small and the range is huge, we can use
    the factorization approach instead.
    
    Let me implement both and switch based on A.
    """
    
    x_min = math.ceil(n / 4)
    x_max = x_max_mult * n
    
    for x in range(x_min, x_max + 1):
        A = 4 * x - n
        B = n * x
        if A <= 0:
            continue
        
        # y ranges from ceil(B/A)+[ensure Ay>B] to floor(2B/A)
        y_lo = max(1, (B + A) // A)  # ceil(B/A), ensures Ay > B when B%A != 0
        if A * y_lo <= B:
            y_lo += 1
        y_hi = 2 * B // A
        y_range = y_hi - y_lo + 1
        
        if y_range <= 0:
            continue
        
        # If range is manageable, do direct iteration
        if y_range <= 500000:
            for y in range(y_lo, y_hi + 1):
                num = A * y - B
                if num <= 0:
                    continue
                if (B * y) % num != 0:
                    continue
                z = (B * y) // num
                if z < y:
                    continue
                if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n):
                    return (x, y, z)
        else:
            # Range too large - use factorization of B²
            # (y - B/A)(z - B/A) = (B/A)² when A divides B... 
            # Actually (Ay - B)(Az - B) = B²
            # f1 = Ay - B, f2 = Az - B, f1*f2 = B²
            # f1 ≡ -B (mod A), f1 > 0, f1 <= B (for y <= z)
            # y = (f1 + B)/A, z = (f2 + B)/A
            
            # Find divisors of B² that are ≡ -B (mod A) and <= B
            # Factorize B
            b = B
            factors = {}
            d = 2
            temp = b
            while d * d <= temp:
                while temp % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    temp //= d
                d += 1
            if temp > 1:
                factors[temp] = factors.get(temp, 0) + 1
            
            # Generate divisors of B²
            # B² has prime exponents 2*each
            primes = list(factors.keys())
            exponents = [2 * factors[p] for p in primes]
            
            # Generate divisors and check condition
            def gen_divisors(idx, current):
                if idx == len(primes):
                    yield current
                    return
                p = primes[idx]
                for e in range(exponents[idx] + 1):
                    yield from gen_divisors(idx + 1, current * (p ** e))
            
            target_mod = A - (B % A)  # f1 ≡ -B (mod A) means f1 ≡ (A - B%A) % A
            if target_mod == A:
                target_mod = 0
            
            best_f1 = None
            for f1 in gen_divisors(0, 1):
                if f1 <= 0 or f1 > B:
                    continue
                if f1 % A != target_mod:
                    continue
                f2 = B * B // f1
                if (f2 + B) % A != 0:
                    continue
                y = (f1 + B) // A
                z = (f2 + B) // A
                if z < y:
                    continue
                if y <= 0 or z <= 0:
                    continue
                # Verify
                if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n):
                    return (x, y, z)
            
    return None

def main():
    # Target: n ≡ 1 (mod 12), n ≢ 0 (mod 5), n >= 13, n <= 100000
    target_n = []
    for n in range(13, 100001):
        if n % 12 == 1 and n % 5 != 0:
            target_n.append(n)
    
    print(f"Total target n values: {len(target_n)}")
    print(f"Range: n = {target_n[0]} to n = {target_n[-1]}")
    
    results = {}
    x_values = []
    no_solution = []
    
    start_time = time.time()
    
    for i, n in enumerate(target_n):
        sol = find_solution_optimized(n, x_max_mult=3)
        
        if sol:
            x, y, z = sol
            results[str(n)] = {"x": x, "y": y, "z": z}
            x_values.append((n, x))
        else:
            no_solution.append(n)
            results[str(n)] = {"x": None, "y": None, "z": None, "found": False}
        
        if (i + 1) % 100 == 0:
            elapsed = time.time() - start_time
            print(f"Progress: {i+1}/{len(target_n)} ({100*(i+1)/len(target_n):.1f}%) - "
                  f"Elapsed: {elapsed:.1f}s - Last n: {n} - "
                  f"Solutions found: {len(x_values)} - No solution: {len(no_solution)}")
        
        # Early analysis: print x values for first 50
        if i < 50 and sol:
            m = (n - 1) // 12
            print(f"  n={n}, m={m}, x={x}, 3m+1={3*m+1}, 3m+2={3*m+2}, "
                  f"x-3m-1={x-3*m-1 if x >= 3*m+1 else 'N/A'}, "
                  f"x/n={x/n:.4f}, x-ceil(n/4)={x - math.ceil(n/4)}")
    
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"SEARCH COMPLETE")
    print(f"{'='*60}")
    print(f"Total n tested: {len(target_n)}")
    print(f"Solutions found: {len(x_values)}")
    print(f"No solution found: {len(no_solution)}")
    print(f"Time: {elapsed:.1f}s")
    
    if no_solution:
        print(f"\nn values with no solution (within bounds): {no_solution[:20]}...")
    
    # Analyze x values
    print(f"\n{'='*60}")
    print(f"X VALUE ANALYSIS")
    print(f"{'='*60}")
    
    # Group by n mod 60 (finer residue classes)
    mod60_groups = defaultdict(list)
    for n, x in x_values:
        mod60_groups[n % 60].append((n, x))
    
    for mod_val in sorted(mod60_groups.keys()):
        group = mod60_groups[mod_val]
        x_diffs = []
        x_ratios = []
        x_ceil_diffs = []
        for n, x in group:
            m = (n - 1) // 12
            x_diffs.append(x - (3 * m + 1))
            x_ratios.append(x / n)
            x_ceil_diffs.append(x - math.ceil(n / 4))
        
        print(f"\nn ≡ {mod_val} (mod 60): {len(group)} values")
        print(f"  x - (3m+1): min={min(x_diffs)}, max={max(x_diffs)}, "
              f"mean={sum(x_diffs)/len(x_diffs):.2f}")
        print(f"  x/n ratio: min={min(x_ratios):.4f}, max={max(x_ratios):.4f}, "
              f"mean={sum(x_ratios)/len(x_ratios):.4f}")
        print(f"  x - ceil(n/4): min={min(x_ceil_diffs)}, max={max(x_ceil_diffs)}, "
              f"mean={sum(x_ceil_diffs)/len(x_ceil_diffs):.2f}")
        
        # Show first 5 and last 5
        print(f"  First 5: {[(n, x) for n, x in group[:5]]}")
        if len(group) > 5:
            print(f"  Last 5:  {[(n, x) for n, x in group[-5:]]}")
    
    # Check if x = ceil(n/4) + k for small k
    print(f"\n{'='*60}")
    print(f"X = ceil(n/4) + k analysis")
    print(f"{'='*60}")
    k_counts = defaultdict(int)
    for n, x in x_values:
        k = x - math.ceil(n / 4)
        k_counts[k] += 1
    
    for k in sorted(k_counts.keys())[:20]:
        print(f"  k={k}: {k_counts[k]} values ({100*k_counts[k]/len(x_values):.1f}%)")
    
    # Check relationship x vs n/4
    print(f"\n{'='*60}")
    print(f"X relative to n/4 (exact)")
    print(f"{'='*60}")
    quarter_diffs = []
    for n, x in x_values:
        # x - n/4 (as fraction)
        # 4x - n = A, so x = (n + A)/4, x - n/4 = A/4
        A = 4 * x - n
        quarter_diffs.append(A)
    
    a_counts = defaultdict(int)
    for A in quarter_diffs:
        a_counts[A] += 1
    
    for A in sorted(a_counts.keys())[:30]:
        print(f"  A = 4x-n = {A}: {a_counts[A]} values ({100*a_counts[A]/len(quarter_diffs):.1f}%)")
    
    # Save results
    output = {
        "metadata": {
            "conjecture": "Erdős-Straus",
            "target": "n ≡ 1 (mod 12), n ≢ 0 (mod 5), 13 ≤ n ≤ 100000",
            "total_tested": len(target_n),
            "solutions_found": len(x_values),
            "no_solution_count": len(no_solution),
            "no_solution_list": no_solution,
            "time_seconds": elapsed,
        },
        "solutions": results,
        "x_analysis": {
            "x_minus_ceil_n_over_4_distribution": dict(sorted(k_counts.items())),
            "A_equals_4x_minus_n_distribution": dict(sorted(a_counts.items())),
        },
    }
    
    output_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/search_results.json"
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")
    
    # Final pattern analysis
    print(f"\n{'='*60}")
    print(f"PATTERN ANALYSIS FOR FORMULA")
    print(f"{'='*60}")
    
    # Check if x = ceil(n/4) always works (A=1,2,3 typically)
    a1_count = a_counts.get(1, 0)
    a2_count = a_counts.get(2, 0)
    a3_count = a_counts.get(3, 0)
    a_total = len(x_values)
    print(f"x = ceil(n/4) (A=1 or A=2 or A=3 depending on n%4): "
          f"A=1:{a1_count}, A=2:{a2_count}, A=3:{a3_count}")
    print(f"Percentage with A <= 3: {100*(a1_count+a2_count+a3_count)/a_total:.1f}%")
    print(f"Percentage with A <= 10: {100*sum(v for k,v in a_counts.items() if k<=10)/a_total:.1f}%")
    print(f"Percentage with A <= 100: {100*sum(v for k,v in a_counts.items() if k<=100)/a_total:.1f}%")
    print(f"Max A value: {max(a_counts.keys())}")
    
    # Check x = 3m+1 formula
    print(f"\nChecking x = 3m+1 formula:")
    match_3m1 = 0
    match_3m2 = 0
    match_other = 0
    for n, x in x_values:
        m = (n - 1) // 12
        if x == 3 * m + 1:
            match_3m1 += 1
        elif x == 3 * m + 2:
            match_3m2 += 1
        else:
            match_other += 1
    print(f"  x = 3m+1: {match_3m1} ({100*match_3m1/a_total:.1f}%)")
    print(f"  x = 3m+2: {match_3m2} ({100*match_3m2/a_total:.1f}%)")
    print(f"  Other:    {match_other} ({100*match_other/a_total:.1f}%)")
    
    # What are the "other" cases?
    if match_other > 0:
        print(f"\n  Sample 'other' cases:")
        other_count = 0
        for n, x in x_values:
            m = (n - 1) // 12
            if x != 3 * m + 1 and x != 3 * m + 2:
                A = 4 * x - n
                print(f"    n={n}, m={m}, x={x}, 3m+1={3*m+1}, 3m+2={3*m+2}, "
                      f"x-3m-1={x-3*m-1}, A=4x-n={A}")
                other_count += 1
                if other_count >= 30:
                    break


if __name__ == "__main__":
    main()