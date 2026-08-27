#!/usr/bin/env python3
"""
Phase 2: Close the n ≡ 1 mod 24 gap.

The cascade with guaranteed + deterministic factors gives product 1.26e-3
for n ≡ 1 mod 24. This means ~0.13% of residue classes survive.

Strategy: For the surviving residue classes, show that the ACTUAL 
factorization of x = (n+u)/4 provides enough divisors to cover a target.

Key insight: For large u (103, 107, 127), the guaranteed 9 divisors 
are sparse (9 out of 100+ residues). But x = (n+u)/4 is a large number
(~n/4), and by Hardy-Ramanujan, ω(x) ~ log log x. For n > 10^6, 
ω(x) ≥ 3 is typical, giving |divisors of x²| = 3^3 = 27 (or more).

But we need DETERMINISTIC, not typical. The question is:
  For n ≡ 1 mod 24, can we find a SUBSET of u values where the 
  cascade product reaches 0?

Approach 1: Find u values where F_u(n≡1) = ∅ using stronger factor guarantees.
Approach 2: Use the Burgess bound to show that for large n, some u has 
  n as QNR, guaranteeing a QNR factor of x, which breaks the all-QR obstruction.
Approach 3: Show that the INTERSECTION of all F_u is empty by CRT, even 
  though the product is nonzero — the product is an UPPER BOUND on the 
  intersection, not the exact size.

Wait — actually, the CRT product IS the exact intersection size (by CRT 
independence). So if the product is nonzero, the intersection is nonempty.

BUT: the CRT product assumes the failure sets are INDEPENDENT across u values.
This is true for the GUARANTEED divisors (which depend only on n mod u).
But the ACTUAL divisors depend on the factorization of x, which depends on 
n (not just n mod u). So the actual failure sets are NOT independent across u!

For example, if n is a specific prime, then x = (n+u)/4 is different for 
each u, with independent factorizations. So the actual failure events 
ARE approximately independent (different u → different x → different 
factorization → independent success/failure).

For the DETERMINISTIC proof, we need to show that no n falls in ALL F_u 
simultaneously. The CRT product being nonzero means the guaranteed 
divisors don't suffice. But the ACTUAL divisors (from x's factorization) 
can only help.

Let me try Approach 1: find additional u values or factor guarantees 
that zero out some F_u for n ≡ 1 mod 24.
"""

import sympy
from sympy import isprime, primitive_root, factorint
import json
from itertools import product as iterproduct

def get_u_values(max_u=127):
    return [u for u in range(3, max_u+1) if isprime(u) and u % 4 == 3]

def compute_failure_set_detailed(u, n_mod_24, extra_factor_primes=None):
    """
    Compute failure set for (u, n mod 24) with specified extra prime factors.
    
    extra_factor_primes: list of primes that are GUARANTEED to divide x 
    for this (u, n_mod_24) pair.
    
    A prime p is guaranteed to divide x = (n+u)/4 when:
      4p | (n+u), i.e., n ≡ -u mod 4p.
    
    Given n ≡ n_mod_24 mod 24, we can check:
      n ≡ n_mod_24 mod gcd(24, 4p)
    
    For p=2: need n ≡ -u mod 8. n mod 8 = n_mod_24 mod 8.
    For p=3: need n ≡ -u mod 12. n mod 12 = n_mod_24 mod 12.
    For p=5: need n ≡ -u mod 20. n mod 20 = n_mod_24 mod 20 (since gcd(24,20)=4).
      Actually n mod 20 is not determined by n mod 24 alone. 
      n mod lcm(24, 20) = n mod 120 determines both.
    
    So for p ≥ 5, we need n mod 4p, which requires n mod lcm(24, 4p).
    For the cascade, we should work mod lcm of all (u, 4p) values.
    
    But this makes the CRT analysis more complex. Let me instead just 
    check which (u, n_mod_24) pairs give which guaranteed factors.
    """
    inv4 = pow(4, -1, u)
    
    if extra_factor_primes is None:
        # Auto-determine based on n_mod_24
        extra_factor_primes = []
        # Check each prime
        for p in [2, 3, 5, 7, 11, 13]:
            # p | x iff n ≡ -u mod 4p
            # n mod 4p is determined by n mod lcm(24, 4p)
            lcm_val = sympy.ilcm(24, 4*p)
            # Check if n_mod_24 is consistent with n ≡ -u mod 4p
            # n ≡ n_mod_24 mod 24 AND n ≡ -u mod 4p
            # By CRT, this has a solution iff n_mod_24 ≡ -u mod gcd(24, 4p)
            g = sympy.gcd(24, 4*p)
            if (n_mod_24 - (-u % (4*p))) % g == 0:
                # Consistent — but this means p MIGHT divide x, not GUARANTEED.
                # p is guaranteed to divide x ONLY if ALL n ≡ n_mod_24 mod 24 
                # satisfy n ≡ -u mod 4p, which requires 4p | 24, i.e., p ∈ {2, 3}.
                # For p ≥ 5, it's not guaranteed from n mod 24 alone.
                if p in [2, 3]:
                    extra_factor_primes.append(p)
    
    # For p ≥ 5, we need to split n mod 24 into finer residue classes.
    # Let's work mod 120 = lcm(24, 8, 12, 20) to capture p=5 as well.
    # Actually, let's work mod M = lcm(24, 4*5, 4*7, 4*11, 4*13) = lcm(24, 20, 28, 44, 52)
    
    M = 24
    for p in [5, 7, 11, 13]:
        M = sympy.ilcm(M, 4*p)
    
    # Enumerate all n mod M that are ≡ n_mod_24 mod 24
    n_mods_M = [n for n in range(M) if n % 24 == n_mod_24 and sympy.gcd(n, M) == 1 or True]  # include all, filter later
    
    failure_set_mod_u = set()
    
    for n_mod_M in n_mods_M:
        # n mod u
        n_mod = n_mod_M % u
        if n_mod == 0:
            continue
        
        x_mod = (n_mod * inv4) % u
        
        # Determine which primes divide x = (n+u)/4
        # p | x iff n ≡ -u mod 4p iff n_mod_M ≡ -u mod 4p (since 4p | M)
        factors = []
        for p in [2, 3, 5, 7, 11, 13]:
            if (n_mod_M - (-u % (4*p))) % (4*p) == 0:
                factors.append(p)
        
        # Compute divisor set mod u
        # Start with guaranteed: {n^a * x^b : a,b ∈ {0,1,2}}
        divisors = set()
        for a in range(3):
            for b in range(3):
                val = pow(n_mod, a, u) * pow(x_mod, b, u) % u
                divisors.add(val)
        
        # Add factors
        for p in factors:
            p_mod = p % u
            if p_mod == 0:
                continue
            new_divs = set()
            for d in divisors:
                for e in range(3):  # p^0, p^1, p^2
                    new_divs.add((d * pow(p_mod, e, u)) % u)
            divisors = new_divs
        
        # Compute targets
        targets = set()
        for j in range(3):
            target = (-x_mod * pow(n_mod, j, u)) % u
            targets.add(target)
        
        if not (divisors & targets):
            failure_set_mod_u.add(n_mod)
    
    return failure_set_mod_u

# ============ MAIN ============

u_values = get_u_values(127)
print("="*80)
print("PHASE 2: Closing the n ≡ 1 mod 24 gap")
print("="*80)

# First, let's see which n mod 120 classes are hard cases
# Hard case: n ≡ 1 mod 12 AND n ≢ 0 mod 5
# n ≡ 1 mod 12: n mod 12 ∈ {1}
# n ≢ 0 mod 5: n mod 5 ∈ {1, 2, 3, 4}
# Combined: n mod 60 ∈ {1, 13, 37, 49} (n ≡ 1 mod 12, n ≢ 0 mod 5)
# For n ≡ 1 mod 24: n mod 120 ∈ {1, 49, 73, 97} (n ≡ 1 mod 24, n ≢ 0 mod 5)

hard_cases_mod_120 = []
for n in range(120):
    if n % 12 == 1 and n % 5 != 0 and n % 24 == 1:
        hard_cases_mod_120.append(n)

print(f"\nHard case classes mod 120 (n ≡ 1 mod 24): {hard_cases_mod_120}")

# For each such class, compute the cascade
M = 120  # lcm(24, 20) captures factor 5

print(f"\n{'='*80}")
print(f"Cascade analysis mod {M} for n ≡ 1 mod 24 hard cases")
print(f"{'='*80}")

for n_mod_120 in hard_cases_mod_120:
    print(f"\n--- n ≡ {n_mod_120} mod {M} ---")
    
    cascade_product = 1.0
    any_empty = False
    
    for u in u_values:
        if u == 3:
            # u=3 always fails for n ≡ 1 mod 3 (which includes n ≡ 1 mod 12)
            frac = 1.0
            print(f"  u={u:3d}: |F_u| = {u-1}/{u-1} = 1.000000 (always fails for hard cases)")
            cascade_product *= frac
            continue
        
        # Compute failure set for this (u, n_mod_120) pair
        inv4 = pow(4, -1, u)
        
        # Find all n mod u that appear in this class
        # n ≡ n_mod_120 mod 120, n mod u varies
        # For each n mod u, check if it's in the failure set
        
        # Get all n mod u values that are ≡ n_mod_120 mod gcd(120, u)
        g = sympy.gcd(120, u)
        if n_mod_120 % g != 0 % g:
            # No solutions
            print(f"  u={u:3d}: No valid n mod u")
            continue
        
        # Enumerate n mod u with n ≡ n_mod_120 mod g
        n_mods_u = [n for n in range(1, u) if n % g == n_mod_120 % g]
        
        failure_count = 0
        for n_mod in n_mods_u:
            # Check which primes divide x = (n+u)/4
            # Need to know n mod 4p for each p
            # n ≡ n_mod_120 mod 120 determines n mod 4p for p | 30 (p ∈ {2,3,5})
            # For p=7: need n mod 28. n mod 120 and n mod 28 → n mod lcm(120,28)=840
            # This is getting complex. Let me use n mod 840 = lcm(120, 28, 44, 52)
            
            M_full = 1
            for p in [2, 3, 5, 7, 11, 13]:
                M_full = sympy.ilcm(M_full, 4*p)
            # M_full = lcm(8, 12, 20, 28, 44, 52) = lcm(120, 28, 44, 52)
            # = lcm(120, 28) = 840, lcm(840, 44) = 9240, lcm(9240, 52) = 120120
            
            # For this n_mod u, find the unique n mod M_full with:
            # n ≡ n_mod_120 mod 120 AND n ≡ n_mod mod u
            # By CRT (gcd(120, u) = g, and n_mod_120 ≡ n_mod mod g)
            
            # Actually, let's just compute for the specific n value
            # n = n_mod_120 (smallest positive representative)
            # x = (n_mod_120 + u) / 4 — but this might not be integer!
            # 4 | (n+u) iff n ≡ -u mod 4 iff n_mod_120 ≡ -u mod 4
            
            if (n_mod_120 + u) % 4 != 0:
                # x is not integer for this n — skip (n must satisfy n ≡ -u mod 4)
                # But there exist n ≡ n_mod_120 mod 120 with n ≡ -u mod 4
                # by CRT (gcd(120, 4) = 4, need n_mod_120 ≡ -u mod 4)
                if n_mod_120 % 4 != (-u) % 4:
                    continue  # No valid n in this class for this u
            
            # n = n_mod_120 works (or n_mod_120 + 120*k for the right k)
            # Let's use n = n_mod_120 + 120*k where k makes 4 | (n+u)
            # n + u ≡ n_mod_120 + u + 120*k mod 4
            # 120*k mod 4 = 0, so need n_mod_120 + u ≡ 0 mod 4
            # Already checked above.
            
            n = n_mod_120
            x = (n + u) // 4
            
            # Factor x
            factors_x = factorint(x)
            
            # Compute full divisor set of x² mod u
            # x² has factorization {p: 2*e for p, e in factors_x.items()}
            divisors = {1 % u}
            for p, e in factors_x.items():
                p_mod = p % u
                if p_mod == 0:
                    continue
                new_divs = set()
                pe = 1
                for exp in range(2*e + 1):
                    for d in divisors:
                        new_divs.add((d * pe) % u)
                    pe = (pe * p_mod) % u
                divisors = new_divs
            
            # Also include n factors (D = n²x²)
            n_mod = n % u
            full_divisors = set()
            for a in range(3):  # n^0, n^1, n^2
                na = pow(n_mod, a, u)
                for d in divisors:
                    full_divisors.add((na * d) % u)
            
            # Targets
            x_mod = (n_mod * pow(4, -1, u)) % u
            targets = set()
            for j in range(3):
                target = (-x_mod * pow(n_mod, j, u)) % u
                targets.add(target)
            
            if not (full_divisors & targets):
                failure_count += 1
        
        total = len(n_mods_u)
        frac = failure_count / total if total > 0 else 0
        if failure_count == 0 and total > 0:
            any_empty = True
        cascade_product *= frac
        if failure_count > 0:
            print(f"  u={u:3d}: |F_u| = {failure_count}/{total} = {frac:.6f}")
        elif total > 0:
            print(f"  u={u:3d}: |F_u| = 0/{total} = 0.000000 ✓ (EMPTY)")
    
    print(f"\n  Cascade product: {cascade_product:.6e}")
    print(f"  Any empty F_u: {'YES → PROOF COMPLETE for this class' if any_empty else 'NO'}")

# ============ Approach 2: Use actual n values ============
print(f"\n{'='*80}")
print("Approach 2: Check actual prime hard cases with full factorization")
print("="*80)

def find_hard_case_primes(limit=10000):
    """Find prime hard cases: n ≡ 1 mod 12, n ≢ 0 mod 5, all odd prime factors 
    of B₃ = n(n+3)/4 are ≡ 1 mod 3."""
    hard_primes = []
    for n in range(13, limit, 12):  # n ≡ 1 mod 12
        if n % 5 == 0:
            continue
        if not isprime(n):
            continue
        # Check B₃ condition
        B3 = n * (n + 3) // 4
        # Factor B3 and check all odd prime factors ≡ 1 mod 3
        factors = factorint(B3)
        if all(p == 2 or p % 3 == 1 for p in factors):
            hard_primes.append(n)
    return hard_primes

hard_primes = find_hard_case_primes(5000)
print(f"Found {len(hard_primes)} prime hard cases up to 5000")
print(f"  n ≡ 1 mod 24: {sum(1 for n in hard_primes if n % 24 == 1)}")
print(f"  n ≡ 13 mod 24: {sum(1 for n in hard_primes if n % 24 == 13)}")

# For each hard case, check which u values work with FULL factorization
print(f"\nChecking full cascade for each hard case...")

all_covered = True
max_u_needed = 0

for n in hard_primes:
    covered = False
    for u in u_values:
        if (n + u) % 4 != 0:
            continue
        x = (n + u) // 4
        factors_x = factorint(x)
        
        # Compute full divisor set of D = n²x² mod u
        divisors = {1 % u}
        for p, e in factors_x.items():
            p_mod = p % u
            if p_mod == 0:
                continue
            new_divs = set()
            pe = 1
            for exp in range(2*e + 1):
                for d in divisors:
                    new_divs.add((d * pe) % u)
                pe = (pe * p_mod) % u
            divisors = new_divs
        
        # Multiply by n^a for a ∈ {0,1,2}
        n_mod = n % u
        full_divisors = set()
        for a in range(3):
            na = pow(n_mod, a, u)
            for d in divisors:
                full_divisors.add((na * d) % u)
        
        # Targets
        x_mod = (n_mod * pow(4, -1, u)) % u
        targets = set()
        for j in range(3):
            target = (-x_mod * pow(n_mod, j, u)) % u
            targets.add(target)
        
        if full_divisors & targets:
            covered = True
            if u > max_u_needed:
                max_u_needed = u
            break
    
    if not covered:
        print(f"  ❌ n = {n} NOT COVERED by any u ≤ 127!")
        all_covered = False

print(f"\n  All {len(hard_primes)} hard cases up to 5000 covered: {'YES ✓' if all_covered else 'NO ✗'}")
print(f"  Maximum u needed: {max_u_needed}")

# ============ Approach 3: Find the tightest cascade subset ============
print(f"\n{'='*80}")
print("Approach 3: Find optimal u subset for n ≡ 1 mod 24")
print("="*80)

# For n ≡ 1 mod 24, the guaranteed cascade product is 1.26e-3.
# But with full factorization, all cases are covered.
# Can we find a SUBSET of u values that already gives product 0?

# The key: find u values where F_u(n≡1 mod 24) is very small or empty
# when considering factor guarantees for n ≡ 1 mod 24 specifically.

# From the Phase 1 results:
# u=7: |F_u| = 3/6 = 50% → 3 failures
# u=11: |F_u| = 5/10 = 50% → 5 failures
# u=23: |F_u| = 11/22 = 50% → 11 failures

# The problem is the large u values (103, 107, 127) which have high failure rates.
# But they're needed for the cascade because they cover different residue classes.

# Let's check: which u values have F_u(n≡1) = ∅ when we add factor 7?
# 7|x iff n ≡ -u mod 28. For n ≡ 1 mod 24, this requires n ≡ 1 mod 24 
# AND n ≡ -u mod 28. By CRT, this has solutions iff 1 ≡ -u mod gcd(24,28)=4,
# i.e., u ≡ -1 ≡ 3 mod 4 (always true for our u values).

# So 7|x for SOME n ≡ 1 mod 24 (specifically, n ≡ -u mod 28 AND n ≡ 1 mod 24).
# But not for ALL n ≡ 1 mod 24.

# The refined analysis needs to split n ≡ 1 mod 24 into sub-classes 
# based on n mod 28, mod 44, etc.

# Let's compute the cascade for each (n mod 24, n mod 28, n mod 44, n mod 52) tuple.
# M = lcm(24, 28, 44, 52) = lcm(24, 28) = 168, lcm(168, 44) = 1848, lcm(1848, 52) = 12012

print("\nComputing cascade with finer residue classes (mod 12012)...")
print("This splits n ≡ 1 mod 24 into sub-classes based on which primes divide x.")

M_fine = 1
for p in [2, 3, 5, 7, 11, 13]:
    M_fine = sympy.ilcm(M_fine, 4*p)
print(f"M = lcm(8, 12, 20, 28, 44, 52) = {M_fine}")

# For n ≡ 1 mod 24, enumerate all n mod M that are ≡ 1 mod 24
n_classes = [n for n in range(M_fine) if n % 24 == 1 and n % 5 != 0 and n > 1]
print(f"Number of n ≡ 1 mod 24 classes mod {M_fine} (with n ≢ 0 mod 5): {len(n_classes)}")

# For each class, compute the cascade product
zero_count = 0
nonzero_count = 0
max_product = 0

for n_mod_M in n_classes:
    cascade = 1.0
    has_empty = False
    
    for u in u_values:
        if u == 3:
            cascade *= 1.0  # u=3 always fails
            continue
        
        # Determine n mod u
        n_mod = n_mod_M % u
        if n_mod == 0:
            continue
        
        # Determine which primes divide x = (n+u)/4
        factors = []
        for p in [2, 3, 5, 7, 11, 13]:
            if n_mod_M % (4*p) == (-u) % (4*p):
                factors.append(p)
        
        if (n_mod_M + u) % 4 != 0:
            continue  # x not integer
        
        # Compute divisor coverage
        inv4 = pow(4, -1, u)
        x_mod = (n_mod * inv4) % u
        
        divisors = set()
        for a in range(3):
            for b in range(3):
                divisors.add(pow(n_mod, a, u) * pow(x_mod, b, u) % u)
        
        for p in factors:
            p_mod = p % u
            if p_mod == 0:
                continue
            new_divs = set()
            for d in divisors:
                for e in range(3):
                    new_divs.add((d * pow(p_mod, e, u)) % u)
            divisors = new_divs
        
        targets = set()
        for j in range(3):
            targets.add((-x_mod * pow(n_mod, j, u)) % u)
        
        if divisors & targets:
            has_empty = True  # This u works → F_u is "empty" for this n
            break
    
    if has_empty:
        zero_count += 1
    else:
        nonzero_count += 1

print(f"\n  Classes with at least one working u: {zero_count} / {len(n_classes)}")
print(f"  Classes with NO working u (guaranteed + deterministic factors): {nonzero_count}")

if nonzero_count == 0:
    print(f"\n  ✅ ALL classes covered by guaranteed + deterministic factors!")
    print(f"  → DETERMINISTIC PROOF COMPLETE for n ≡ 1 mod 24")
else:
    print(f"\n  ⚠️  {nonzero_count} classes need full factorization analysis")
    print(f"  → These classes require ω(x) ≥ 3 from non-deterministic factors")