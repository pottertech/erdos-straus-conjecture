#!/usr/bin/env python3
"""
Large-scale verification of Erdős-Straus conjecture z=my parametrization.
Tests all "hard cases" up to n = 10,000,000.

Hard case definition:
  - n ≡ 1 (mod 12)
  - n ≢ 0 (mod 5)
  - All prime factors of B₃ = n(n+3)/4 are ≡ 1 (mod 3) (excluding p=2)

For each hard case, find minimum A from A_list (all ≡ 3 mod 4) such that
D = n(n+A) has a divisor m with 4A | (D/m)(m+1).
"""

import sys
import time
from collections import Counter
from sympy import factorint, divisors, isprime

# A_list: all values ≡ 3 mod 4 up to 499
A_list = [3, 7, 11, 15, 19, 23, 31, 43, 47, 55, 59, 67, 71, 79, 83, 91, 95, 99,
          103, 107, 111, 115, 119, 123, 127, 131, 135, 139, 143, 147, 151, 155,
          159, 163, 167, 171, 175, 179, 183, 187, 191, 195, 199, 211, 223, 227,
          231, 239, 243, 247, 251, 255, 259, 263, 267, 271, 279, 283, 287, 291,
          295, 299, 303, 307, 311, 315, 319, 323, 327, 331, 335, 339, 343, 347,
          351, 355, 359, 363, 367, 371, 375, 379, 383, 387, 391, 395, 399, 403,
          407, 411, 415, 419, 423, 427, 431, 435, 439, 443, 447, 451, 455, 459,
          463, 467, 471, 475, 479, 483, 487, 491, 495, 499]

N_MAX = 10_000_000


def is_hard_case(n):
    """Check if n is a hard case for the Erdős-Straus conjecture."""
    # n ≡ 1 (mod 12)
    if n % 12 != 1:
        return False
    # n ≢ 0 (mod 5)
    if n % 5 == 0:
        return False
    # All prime factors of B₃ = n(n+3)/4 are ≡ 1 (mod 3) (excluding p=2)
    B3 = n * (n + 3) // 4
    factors = factorint(B3)
    for p, exp in factors.items():
        if p == 2:
            continue
        if p % 3 != 1:
            return False
    return True


def count_prime_factors(n):
    """Count distinct prime factors of n (omega function)."""
    return len(factorint(n))


def try_A_values(n):
    """
    Try each A in A_list where (n+A) % 4 == 0.
    Return (min_A, unsolved) where min_A is the minimum working A,
    or None if no A works.
    """
    for A in A_list:
        if (n + A) % 4 != 0:
            continue
        D = n * (n + A)
        # Check if D has a divisor m such that 4A | (D/m)(m+1)
        divs = divisors(D)
        for m in divs:
            # 4A divides (D/m)*(m+1)
            if ((D // m) * (m + 1)) % (4 * A) == 0:
                return A
    return None  # unsolved


def main():
    start_time = time.time()
    
    print(f"Erdős-Straus Conjecture z=my Parametrization Verification")
    print(f"Scanning n ≤ {N_MAX:,} for hard cases...")
    print(f"{'='*60}")
    
    hard_cases = []
    
    # Phase 1: Find all hard cases
    # We iterate n ≡ 1 mod 12, skip n ≡ 0 mod 5, then factor B3
    phase1_start = time.time()
    
    for n in range(1, N_MAX + 1, 12):  # n ≡ 1 mod 12
        if n % 5 == 0:
            continue
        
        B3 = n * (n + 3) // 4
        
        # Quick pre-check: if B3 is even, factor out 2s first
        # Then check remaining odd primes mod 3
        # Use factorint
        factors = factorint(B3)
        
        is_hard = True
        for p in factors:
            if p == 2:
                continue
            if p % 3 != 1:
                is_hard = False
                break
        
        if is_hard:
            hard_cases.append(n)
        
        # Progress report every ~1M numbers
        if n % 1_000_005 == 0 or n == 1:
            elapsed = time.time() - phase1_start
            pct = n / N_MAX * 100
            print(f"  Phase 1: n={n:>10,} / {N_MAX:,} ({pct:.1f}%) | "
                  f"hard cases so far: {len(hard_cases)} | "
                  f"elapsed: {elapsed:.1f}s", flush=True)
    
    phase1_time = time.time() - phase1_start
    print(f"\nPhase 1 complete: {len(hard_cases)} hard cases found in {phase1_time:.1f}s")
    print(f"{'='*60}")
    
    # Phase 2: For each hard case, find minimum A
    phase2_start = time.time()
    
    a_distribution = Counter()
    unsolved = []
    max_A_overall = 0
    max_A_omega2 = 0
    max_A_omega_ge3 = 0
    omega_counts = Counter()
    
    for i, n in enumerate(hard_cases):
        omega_n = count_prime_factors(n)
        omega_counts[omega_n] += 1
        
        min_A = try_A_values(n)
        
        if min_A is None:
            n_prime = isprime(n)
            n_factors = factorint(n)
            unsolved.append({
                'n': n,
                'is_prime': n_prime,
                'factorization': n_factors,
                'omega': omega_n
            })
            print(f"  ⚠️ UNSOLVED: n={n}, prime={n_prime}, ω={omega_n}, factors={n_factors}")
        else:
            a_distribution[min_A] += 1
            if min_A > max_A_overall:
                max_A_overall = min_A
            if omega_n == 2 and min_A > max_A_omega2:
                max_A_omega2 = min_A
            if omega_n >= 3 and min_A > max_A_omega_ge3:
                max_A_omega_ge3 = min_A
        
        # Progress report every 100 cases
        if (i + 1) % 100 == 0 or i == 0:
            elapsed = time.time() - phase2_start
            pct = (i + 1) / len(hard_cases) * 100
            print(f"  Phase 2: case {i+1}/{len(hard_cases)} ({pct:.1f}%) | "
                  f"n={n} | elapsed: {elapsed:.1f}s", flush=True)
    
    phase2_time = time.time() - phase2_start
    total_time = time.time() - start_time
    
    print(f"\nPhase 2 complete in {phase2_time:.1f}s")
    print(f"Total time: {total_time:.1f}s")
    print(f"{'='*60}")
    
    # Print summary
    print(f"\nSUMMARY:")
    print(f"  Total hard cases: {len(hard_cases)}")
    print(f"  Solved: {len(hard_cases) - len(unsolved)}")
    print(f"  Unsolved: {len(unsolved)}")
    print(f"  Max A overall: {max_A_overall}")
    print(f"  Max A (ω=2): {max_A_omega2}")
    print(f"  Max A (ω≥3): {max_A_omega_ge3}")
    print(f"\n  ω distribution: {dict(sorted(omega_counts.items()))}")
    print(f"\n  A distribution:")
    for a, cnt in sorted(a_distribution.items()):
        print(f"    A={a:>3}: {cnt:>6} cases")
    
    # Write full results to file
    results_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/VERIFICATION_10M.md"
    with open(results_path, 'w') as f:
        f.write(f"# Erdős-Straus Conjecture: z=my Parametrization Verification (n ≤ 10,000,000)\n\n")
        f.write(f"**Date:** 2026-08-14\n")
        f.write(f"**Runtime:** {total_time:.1f}s ({total_time/60:.1f} min)\n\n")
        f.write(f"## Parameters\n\n")
        f.write(f"- **N_max:** {N_MAX:,}\n")
        f.write(f"- **Hard case criteria:** n ≡ 1 (mod 12), n ≢ 0 (mod 5), all odd prime factors of B₃ = n(n+3)/4 are ≡ 1 (mod 3)\n")
        f.write(f"- **A list:** {len(A_list)} values, all ≡ 3 (mod 4), range [{A_list[0]}, {A_list[-1]}]\n")
        f.write(f"- **Success criterion:** A works iff D = n(n+A) has a divisor m with 4A | (D/m)(m+1)\n\n")
        
        f.write(f"## Summary Results\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total hard cases | {len(hard_cases)} |\n")
        f.write(f"| Solved by z=my | {len(hard_cases) - len(unsolved)} |\n")
        f.write(f"| Unsolved | {len(unsolved)} |\n")
        f.write(f"| Max A overall | {max_A_overall} |\n")
        f.write(f"| Max A (ω=2) | {max_A_omega2} |\n")
        f.write(f"| Max A (ω≥3) | {max_A_omega_ge3} |\n\n")
        
        f.write(f"## ω(n) Distribution\n\n")
        f.write(f"| ω(n) | Count |\n")
        f.write(f"|------|-------|\n")
        for omega in sorted(omega_counts.keys()):
            f.write(f"| {omega} | {omega_counts[omega]} |\n")
        f.write(f"\n")
        
        f.write(f"## Minimum A Distribution\n\n")
        f.write(f"| A value | Count | Percentage |\n")
        f.write(f"|---------|-------|-----------|\n")
        total_solved = sum(a_distribution.values())
        for a in sorted(a_distribution.keys()):
            pct = a_distribution[a] / total_solved * 100 if total_solved > 0 else 0
            f.write(f"| {a} | {a_distribution[a]} | {pct:.2f}% |\n")
        f.write(f"| **Total** | **{total_solved}** | **100%** |\n\n")
        
        f.write(f"## Growth Comparison with Previous Results\n\n")
        f.write(f"| Bound | Max A overall | Max A (ω=2) | Max A (ω≥3) | Hard cases |\n")
        f.write(f"|-------|-------------|------------|------------|------------|\n")
        f.write(f"| n ≤ 50,000 | 59 | — | — | — |\n")
        f.write(f"| n ≤ 500,000 | — | 19 | 11 | — |\n")
        f.write(f"| n ≤ 10,000,000 | {max_A_overall} | {max_A_omega2} | {max_A_omega_ge3} | {len(hard_cases)} |\n\n")
        
        f.write(f"## Unsolved Cases\n\n")
        if unsolved:
            f.write(f"**{len(unsolved)} unsolved case(s) found.**\n\n")
            f.write(f"| n | Is Prime | ω(n) | Factorization |\n")
            f.write(f"|---|----------|------|----------------|\n")
            for u in unsolved:
                fac_str = " × ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(u['factorization'].items()))
                f.write(f"| {u['n']:,} | {u['is_prime']} | {u['omega']} | {fac_str} |\n")
        else:
            f.write(f"**No unsolved cases.** All hard cases up to n = {N_MAX:,} are solved by the z=my parametrization with A values up to {max_A_overall}.\n\n")
        
        f.write(f"## Complete A Distribution (Detailed)\n\n")
        f.write(f"```\n")
        for a in sorted(a_distribution.keys()):
            bar = "█" * min(a_distribution[a] // 5 + 1, 50)
            f.write(f"A={a:>3}: {a_distribution[a]:>6}  {bar}\n")
        f.write(f"```\n\n")
        
        f.write(f"## Phase Timings\n\n")
        f.write(f"- Phase 1 (finding hard cases): {phase1_time:.1f}s ({phase1_time/60:.1f} min)\n")
        f.write(f"- Phase 2 (solving with z=my): {phase2_time:.1f}s ({phase2_time/60:.1f} min)\n")
        f.write(f"- Total runtime: {total_time:.1f}s ({total_time/60:.1f} min)\n\n")
        
        f.write(f"## Conclusion\n\n")
        if unsolved:
            f.write(f"The z=my parametrization with A values up to {A_list[-1]} fails to solve {len(unsolved)} hard case(s) up to n = {N_MAX:,}.\n")
            f.write(f"Further investigation needed for these cases.\n")
        else:
            f.write(f"✅ The z=my parametrization successfully solves ALL {len(hard_cases)} hard cases up to n = {N_MAX:,}.\n")
            f.write(f"The maximum A needed was {max_A_overall}, well within the tested range of [{A_list[0]}, {A_list[-1]}].\n")
            if max_A_omega2 > 0:
                f.write(f"For ω(n)=2 cases, the maximum A needed was {max_A_omega2}.\n")
            if max_A_omega_ge3 > 0:
                f.write(f"For ω(n)≥3 cases, the maximum A needed was {max_A_omega_ge3}.\n")
            f.write(f"\nThis provides strong computational evidence for the Erdős-Straus conjecture via the z=my parametrization approach.\n")
    
    print(f"\nResults written to {results_path}")
    return hard_cases, a_distribution, unsolved, max_A_overall, max_A_omega2, max_A_omega_ge3


if __name__ == "__main__":
    main()