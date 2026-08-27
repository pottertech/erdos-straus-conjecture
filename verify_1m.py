#!/usr/bin/env python3
"""
Erdős-Straus Conjecture - z=my Parametrization Verification up to n = 1,000,000
"""
import sys
import time
from fractions import Fraction
from collections import Counter
from sympy import factorint, divisors

# A values from the list, filtered to A ≡ 3 mod 4 (so that 4 | (n+A) when n ≡ 1 mod 12)
# Original list:
ALL_A = [3, 7, 11, 15, 19, 23, 31, 43, 47, 55, 59, 67, 71, 79, 83, 91, 95, 99,
         103, 107, 111, 115, 119, 123, 127, 131, 135, 139, 143, 147, 151, 155, 159,
         163, 167, 171, 175, 179, 183, 187, 191, 195, 199, 211, 223, 227, 231, 239,
         243, 247, 251, 255, 259, 263, 267, 271, 279, 283, 287, 291, 295, 299, 303]

# Filter: A ≡ 3 mod 4 (since n ≡ 1 mod 12 => n ≡ 1 mod 4, so A ≡ 3 mod 4 => n+A ≡ 0 mod 4)
A_LIST = [a for a in ALL_A if a % 4 == 3]
print(f"A values to try (A ≡ 3 mod 4): {A_LIST}")
print(f"Count: {len(A_LIST)}")

def is_prime_sympy(n):
    """Check if n is prime using sympy."""
    from sympy import isprime
    return isprime(n)

def is_hard_case(n):
    """Check if n is a 'hard case':
       - n ≡ 1 (mod 12)
       - n ≢ 0 (mod 5)
       - All prime factors of B3 = n(n+3)/4 are ≡ 1 (mod 3) (excluding p=2)
    """
    if n % 12 != 1:
        return False
    if n % 5 == 0:
        return False
    B3 = n * (n + 3) // 4
    # B3 must be integer
    if n * (n + 3) % 4 != 0:
        return False
    factors = factorint(B3)
    for p, e in factors.items():
        if p == 2:
            continue
        if p % 3 != 1:
            return False
    return True

def z_my_check(n, A):
    """Check if z=my parametrization works for given n, A.
    A works iff D = n(n+A) has a divisor m with 4A | (D/m)(m+1).
    """
    D = n * (n + A)
    divs = divisors(D)
    fourA = 4 * A
    for m in divs:
        quotient = D // m
        product = quotient * (m + 1)
        if product % fourA == 0:
            return True
    return False

def find_min_A(n):
    """Find minimum A from A_LIST that works for z=my parametrization."""
    for A in A_LIST:
        if z_my_check(n, A):
            return A
    return None

def brute_force_search(n):
    """Brute-force search for ANY solution to 4/n = 1/x + 1/y + 1/z.
    Search x from 1 to 4n, then y from x to 2*q//p+1 where p=4x-n, q=n*x.
    Returns (x, y, z) or None.
    """
    for x in range(1, 4 * n + 1):
        p = 4 * x - n
        if p <= 0:
            continue
        q = n * x
        # 1/y + 1/z = p/q => y >= x (WLOG), z = q*y / (p*y - q)
        # Need p*y - q > 0 => y > q/p
        y_start = max(x, q // p + 1)
        y_end = 2 * q // p + 1
        for y in range(y_start, y_end + 1):
            num = q * y
            den = p * y - q
            if den <= 0:
                continue
            if num % den == 0:
                z = num // den
                if z >= y:  # maintain ordering x <= y <= z
                    return (x, y, z)
    return None

def verify_solution(n, x, y, z):
    """Verify 4/n = 1/x + 1/y + 1/z"""
    return Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)

# ============================================================
# MAIN
# ============================================================

print("=" * 70)
print("Erdős-Straus Conjecture - z=my Parametrization Verification")
print("Range: n ≤ 1,000,000")
print("=" * 70)

start_time = time.time()

# Step 1: Find all hard cases
print("\n[Step 1] Finding all hard cases n ≤ 1,000,000...")
hard_cases = []
t0 = time.time()
for n in range(1, 1_000_001):
    if n % 12 != 1:
        continue
    if n % 5 == 0:
        continue
    B3 = n * (n + 3) // 4
    if n * (n + 3) % 4 != 0:
        continue
    factors = factorint(B3)
    is_hard = True
    for p, e in factors.items():
        if p == 2:
            continue
        if p % 3 != 1:
            is_hard = False
            break
    if is_hard:
        hard_cases.append(n)
    if n % 100000 == 0:
        elapsed = time.time() - t0
        print(f"  ... scanned up to n={n}, found {len(hard_cases)} hard cases so far, {elapsed:.1f}s elapsed")

elapsed_step1 = time.time() - t0
print(f"Found {len(hard_cases)} hard cases in {elapsed_step1:.1f}s")
print(f"First 20 hard cases: {hard_cases[:20]}")
print(f"Last 20 hard cases: {hard_cases[-20:]}")

# Step 2: For each hard case, find minimum A
print(f"\n[Step 2] Finding minimum A for each of {len(hard_cases)} hard cases...")
t0 = time.time()
results = {}  # n -> min_A or None
A_distribution = Counter()
unsolved_zmy = []

for i, n in enumerate(hard_cases):
    min_A = find_min_A(n)
    results[n] = min_A
    if min_A is not None:
        A_distribution[min_A] += 1
    else:
        unsolved_zmy.append(n)
    if (i + 1) % 100 == 0 or (i + 1) == len(hard_cases):
        elapsed = time.time() - t0
        print(f"  ... processed {i+1}/{len(hard_cases)} hard cases, {elapsed:.1f}s elapsed, {len(unsolved_zmy)} unsolved by z=my")

elapsed_step2 = time.time() - t0
print(f"Step 2 complete in {elapsed_step2:.1f}s")

# Step 3: Summary statistics
max_A = max((a for a in results.values() if a is not None), default=None)
print(f"\n[Step 3] Summary:")
print(f"  Total hard cases: {len(hard_cases)}")
print(f"  Solved by z=my: {len(hard_cases) - len(unsolved_zmy)}")
print(f"  Unsolved by z=my: {len(unsolved_zmy)}")
print(f"  Maximum A needed: {max_A}")
print(f"\n  A distribution:")
for a in sorted(A_distribution.keys()):
    print(f"    A={a:4d}: {A_distribution[a]:5d} cases")

if unsolved_zmy:
    print(f"\n  Unsolved cases by z=my ({len(unsolved_zmy)} total):")
    for n in unsolved_zmy[:50]:
        is_prime = is_prime_sympy(n)
        factors = factorint(n) if not is_prime else {n: 1}
        print(f"    n={n}, prime={is_prime}, factors={factors}")

# Step 4: Brute-force search for unsolved cases
brute_results = {}
if unsolved_zmy:
    print(f"\n[Step 4] Brute-force search for {len(unsolved_zmy)} unsolved cases...")
    t0 = time.time()
    for n in unsolved_zmy:
        sol = brute_force_search(n)
        brute_results[n] = sol
        if sol:
            x, y, z = sol
            assert verify_solution(n, x, y, z), f"Verification failed for n={n}"
            print(f"  n={n}: FOUND solution x={x}, y={y}, z={z} (verified)")
        else:
            print(f"  n={n}: NO solution found by brute force (potential counterexample!)")
    elapsed_step4 = time.time() - t0
    print(f"Step 4 complete in {elapsed_step4:.1f}s")

total_time = time.time() - start_time
print(f"\n{'=' * 70}")
print(f"TOTAL TIME: {total_time:.1f}s")
print(f"{'=' * 70}")

# Step 5: Write results to file
print("\n[Step 5] Writing results to VERIFICATION_1M.md...")

lines = []
lines.append("# Erdős-Straus Conjecture: z=my Parametrization Verification")
lines.append("")
lines.append("## Scope")
lines.append(f"- **Range:** n ≤ 1,000,000")
lines.append(f"- **Hard case criteria:** n ≡ 1 (mod 12), n ≢ 0 (mod 5), all prime factors of B₃ = n(n+3)/4 are ≡ 1 (mod 3) (excluding p=2)")
lines.append(f"- **A values tested:** {A_LIST}")
lines.append(f"- **A count:** {len(A_LIST)}")
lines.append("")
lines.append("## Results Summary")
lines.append("")
lines.append(f"| Metric | Value |")
lines.append(f"|--------|-------|")
lines.append(f"| Total hard cases found | {len(hard_cases)} |")
lines.append(f"| Solved by z=my parametrization | {len(hard_cases) - len(unsolved_zmy)} |")
lines.append(f"| Unsolved by z=my | {len(unsolved_zmy)} |")
lines.append(f"| Maximum A needed | {max_A} |")
lines.append(f"| Total computation time | {total_time:.1f}s |")
lines.append("")
lines.append("## A Value Distribution")
lines.append("")
lines.append("| A value | Count | Cumulative |")
lines.append("|---------|-------|------------|")
cumulative = 0
for a in sorted(A_distribution.keys()):
    cumulative += A_distribution[a]
    lines.append(f"| {a} | {A_distribution[a]} | {cumulative} |")
lines.append("")
lines.append("## Comparison with n ≤ 50,000 Results")
lines.append("")
lines.append(f"| Metric | n ≤ 50,000 | n ≤ 1,000,000 |")
lines.append(f"|--------|-----------|---------------|")
lines.append(f"| Max A needed | 59 | {max_A} |")
lines.append(f"| Unsolved by z=my | 0 (if any) | {len(unsolved_zmy)} |")
lines.append("")
lines.append("## Unsolved Cases (z=my parametrization)")
lines.append("")
if unsolved_zmy:
    lines.append(f"Total unsolved: {len(unsolved_zmy)}")
    lines.append("")
    lines.append("| n | Prime? | Factorization | Brute-force solution |")
    lines.append("|---|--------|---------------|----------------------|")
    for n in unsolved_zmy:
        is_p = is_prime_sympy(n)
        facts = factorint(n)
        fact_str = " × ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(facts.items()))
        brute_sol = brute_results.get(n)
        if brute_sol:
            x, y, z = brute_sol
            sol_str = f"x={x}, y={y}, z={z}"
        else:
            sol_str = "NONE FOUND"
        lines.append(f"| {n} | {'Yes' if is_p else 'No'} | {fact_str} | {sol_str} |")
    lines.append("")
    lines.append("### Analysis of Unsolved Cases")
    lines.append("")
    truly_unsolved = [n for n in unsolved_zmy if brute_results.get(n) is None]
    brute_solved = [n for n in unsolved_zmy if brute_results.get(n) is not None]
    lines.append(f"- Cases unsolved by z=my but solved by brute force: {len(brute_solved)}")
    lines.append(f"- Cases unsolved by both z=my and brute force: {len(truly_unsolved)}")
    if truly_unsolved:
        lines.append(f"- **POTENTIAL COUNTEREXAMPLES:** {truly_unsolved}")
    else:
        lines.append(f"- No counterexamples found — all cases have at least one solution")
else:
    lines.append("No unsolved cases — all hard cases up to n=1,000,000 are solved by the z=my parametrization.")
lines.append("")
lines.append("## First 20 Hard Cases")
lines.append("")
lines.append("| n | Min A |")
lines.append("|---|-------|")
for n in hard_cases[:20]:
    a = results[n]
    lines.append(f"| {n} | {a if a else 'unsolved'} |")
lines.append("")
lines.append("## Last 20 Hard Cases")
lines.append("")
lines.append("| n | Min A |")
lines.append("|---|-------|")
for n in hard_cases[-20:]:
    a = results[n]
    lines.append(f"| {n} | {a if a else 'unsolved'} |")
lines.append("")
lines.append("## Growth Analysis")
lines.append("")
lines.append(f"The maximum A needed grew from **59** (n ≤ 50,000) to **{max_A}** (n ≤ 1,000,000).")
if max_A and max_A > 59:
    lines.append(f"This represents a growth factor of {max_A/59:.2f}× over a 20× increase in search range.")
lines.append("")
lines.append("## Methodology")
lines.append("")
lines.append("1. **Hard case identification:** For each n ≤ 1,000,000 with n ≡ 1 (mod 12) and n ≢ 0 (mod 5), compute B₃ = n(n+3)/4 and check all prime factors (excluding 2) are ≡ 1 (mod 3).")
lines.append("2. **z=my check:** For each hard case n, try each A in the list (filtered to A ≡ 3 mod 4). A works iff D = n(n+A) has a divisor m with 4A | (D/m)(m+1).")
lines.append("3. **Brute-force fallback:** For cases unsolved by z=my, search x from 1 to 4n, y from max(x, q/p+1) to 2q/p+1 where p=4x-n, q=nx.")
lines.append("4. **Verification:** All brute-force solutions verified using exact arithmetic (fractions.Fraction).")
lines.append("")
lines.append("## Conclusions")
lines.append("")
if not unsolved_zmy:
    lines.append("✅ **All hard cases up to n = 1,000,000 are solved by the z=my parametrization.**")
    lines.append(f"The maximum A needed was {max_A}, well within the tested range of {max(A_LIST)}.")
    lines.append("No counterexamples to the Erdős-Straus conjecture were found.")
elif truly_unsolved:
    lines.append("⚠️ **Potential counterexamples found!** The following cases have no solution from either z=my or brute force:")
    for n in truly_unsolved:
        lines.append(f"- n = {n}")
    lines.append("")
    lines.append("These require further investigation with extended brute-force search.")
else:
    lines.append("✅ **All hard cases have solutions**, though some require brute force beyond the z=my parametrization.")
    lines.append(f"The z=my parametrization solved {len(hard_cases) - len(unsolved_zmy)} of {len(hard_cases)} hard cases.")
    lines.append(f"The remaining {len(unsolved_zmy)} cases were solved by brute-force search.")
    lines.append("No counterexamples to the Erdős-Straus conjecture were found.")
lines.append("")
lines.append("---")
lines.append(f"*Generated: {time.strftime('%Y-%m-%d %H:%M:%S EDT')}*")
lines.append(f"*Computation time: {total_time:.1f}s*")

output = "\n".join(lines)
output_path = "/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/VERIFICATION_1M.md"
with open(output_path, "w") as f:
    f.write(output)

print(f"Results written to {output_path}")
print(f"\nFinal summary:")
print(f"  Total hard cases: {len(hard_cases)}")
print(f"  Solved by z=my: {len(hard_cases) - len(unsolved_zmy)}")
print(f"  Unsolved by z=my: {len(unsolved_zmy)}")
print(f"  Max A needed: {max_A}")
if unsolved_zmy:
    truly = [n for n in unsolved_zmy if brute_results.get(n) is None]
    print(f"  Brute-force solved: {len(unsolved_zmy) - len(truly)}")
    print(f"  Truly unsolved: {len(truly)}")
    if truly:
        print(f"  COUNTEREXAMPLES: {truly}")
print("DONE")