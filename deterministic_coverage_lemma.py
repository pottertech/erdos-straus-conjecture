#!/usr/bin/env python3
"""
Deterministic Coverage Lemma for the u-method.

GOAL: For each prime u ≡ 3 mod 4, u ≤ 127, determine the minimum k such that
for ALL choices of k discrete logs d_1,...,d_k in Z/(u-1)Z, the bounded subset sum
  S = {a_1*d_1 + ... + a_k*d_k mod (u-1) : a_i ∈ {0,1,2}}
covers at least one of the 3 target dlogs for ANY n mod u.

If such k exists and k ≤ ω(x) is achievable for n in the relevant range,
then the u-method works deterministically.

STRATEGY:
1. For each u, enumerate all possible dlog vectors of length k.
2. For each vector, compute the bounded subset sum S.
3. Check if S covers all possible target sets (for all n mod u coprime to u).
4. If any vector fails (misses targets for some n), k is insufficient.

Key optimization: The target dlogs for a given n are:
  T_a = c + (2-a)*dlog(n) mod (u-1)  for a ∈ {0,1,2}
where c = dlog(-1) + dlog(inv(4)) is fixed for each u.

As n ranges over (Z/uZ)*, dlog(n) ranges over all of Z/(u-1)Z.
So the target set traces out: {c, c + dlog_n, c + 2*dlog_n} for each dlog_n.

For deterministic coverage, we need: for ALL dlog_n ∈ Z/(u-1)Z,
S ∩ {c, c + dlog_n, c + 2*dlog_n} ≠ ∅.

Equivalently: for all t ∈ Z/(u-1)Z, S ∩ {c, c+t, c+2t} ≠ ∅.

The WORST CASE over dlog vectors is the one where S is smallest or most clustered.
We need: NO dlog vector produces an S that misses {c, c+t, c+2t} for some t.

APPROACH: For each u, iterate over k = 1, 2, 3, ...
For each k, check if ALL dlog vectors of length k give S that covers {c, c+t, c+2t}
for all t. Use exhaustive search for small (u-1)^k, sampling for large.

But (u-1)^k can be huge. Instead, use the STRUCTURAL argument:

The bounded subset sum S with k generators of size 3 is a subset of Z/(u-1)Z.
|S| ≤ 3^k. If |S| ≥ u-1, then S = Z/(u-1)Z (pigeonhole doesn't help directly,
but if the sumset is a subgroup, it's everything).

Actually, we should think about this differently. The question is:

For which k does the following hold:
  For all d_1,...,d_k ∈ Z/(u-1)Z, the set {Σ a_i*d_i : a_i ∈ {0,1,2}} 
  intersects every 3-term AP {c, c+t, c+2t} in Z/(u-1)Z?

This is a covering problem. The complement of S must avoid containing any 
3-term AP of the form {c, c+t, c+2t}.

Alternative formulation: The complement S^c must not contain any element x
such that x, x+s, x+2s is a 3-term AP with c ∈ {x, x+s, x+2s} for some shift.
Actually simpler: for each residue r not in S, we need r to not be part of
ANY target triple {c, c+t, c+2t}. But r is in target triple for t = r - c
(and also t = (r-c)/2 if that's integer, and t = 2(r-c)).

So r is missed iff r ∉ S AND the OTHER two elements of the triple are also ∉ S.

Wait, let me re-read. The condition is: for all t, S ∩ {c, c+t, c+2t} ≠ ∅.
So if r ∉ S, we need at least one of the other elements in some triple containing r
to be in S. But r appears in many triples: {c, c+t, c+2t} contains r when:
  - r = c: t arbitrary → need c ∈ S
  - r = c+t: t = r-c → need c ∈ S or c+2(r-c) ∈ S or c-(r-c) = 2c-r ∈ S
  - r = c+2t: t = (r-c)/2 → need c ∈ S or c+(r-c)/2 ∈ S

The simplest necessary condition: c ∈ S. If c ∉ S, then for t = 0, {c,c,c} is missed.

So c = dlog(-1) + dlog(inv(4)) MUST be in S. Then for t ≠ 0, we need
S to intersect {c, c+t, c+2t} — since c ∈ S, this is automatically satisfied!

WAIT. That means the problem is trivially solved if c ∈ S!

Let me check: is c always achievable as a bounded subset sum?

c = dlog(-1) + dlog(inv(4)) = (u-1)/2 - dlog(4) mod (u-1)

The bounded subset sum S = {Σ a_i * d_i : a_i ∈ {0,1,2}} always contains 0 
(all a_i = 0). It also contains each d_i and 2*d_i and sums thereof.

For c ∈ S, we need: c is achievable as Σ a_i * d_i for some a_i ∈ {0,1,2}.

This depends on the d_i (which are dlogs of prime factors of x).

So the question becomes: can the adversary choose dlogs such that c is NOT
a bounded subset sum? If so, the method fails for n with dlog(n) = 0 
(i.e., n ≡ 1 mod u)... but n ≡ 1 mod u might not be a hard case.

Hmm, let me reconsider. The target depends on n, and n is the INPUT, not 
adversarial. The question is whether for a SPECIFIC n, the method works.
So for a specific n, dlog_n is fixed, and the targets are fixed.

The dlogs d_i are determined by the prime factors of x = (n+u)/4, which
is determined by n and u. So EVERYTHING is determined by n.

The question is: for which n does the method fail? And can we bound the
smallest u that works for each n?

So the right framing is:
  For a given n (and hence given x, its factorization, and its dlogs),
  does S cover at least one target?
  
And we want to show: for each n, SOME u ≤ 127 works.

The "adversarial" framing is: can there exist an n where ALL u ≤ 127 fail?
This requires checking all u simultaneously, which is what the cascade does.

So let me take a different approach:

APPROACH: Directly verify the cascade property.

For each prime u ≡ 3 mod 4, u ≤ 127:
  The set of n mod u for which the u-method fails is a specific subset F_u ⊆ (Z/uZ)*.
  |F_u| depends on u and the structure of (Z/uZ)*.

The cascade works iff ∩_u F_u = ∅ (no n is in all failure sets simultaneously).

By CRT (since the u values are coprime primes), the density of ∩_u F_u is
∏_u (|F_u|/(u-1)). If this product is 0, the cascade works.

But CRT gives DENSITY, not emptiness. We need ∩ F_u = ∅ as sets, not just
density 0. However, if the product of densities is < 1/∏(u-1), then by
CRT the intersection is empty (since it would need to contain a fraction
smaller than one residue class).

So: compute |F_u| for each u, and check if ∏(|F_u|/(u-1)) < 1/∏(u-1).

This is the GUARANTEED COVERAGE approach from the existing proof.

Let me compute the EXACT failure sets F_u for each prime u ≤ 127.
"""

import sympy
from sympy import isprime, primitive_root, discrete_log, factorint, n_order, legendre_symbol
import itertools
import json
from collections import defaultdict

def get_u_values(max_u=127):
    """Get primes u ≡ 3 mod 4 up to max_u."""
    return [u for u in range(3, max_u+1) if isprime(u) and u % 4 == 3]

def compute_failure_set(u):
    """
    For prime u ≡ 3 mod 4, compute the exact set of n mod u for which 
    the u-method fails (no divisor of x² hits any of the 3 targets).
    
    The u-method works iff x² has a divisor d' with d' ≡ -x*n^j mod u 
    for j ∈ {0,1,2}, where x = (n+u)/4.
    
    For each n mod u (coprime to u):
      1. Compute x = (n+u)/4 mod u (need 4 | (n+u), but mod u we just compute 
         x ≡ n * inv(4) mod u)
      2. Factor x to get its prime factors (but x depends on the ACTUAL value 
         of n, not just n mod u!)
         
    PROBLEM: x = (n+u)/4 depends on the actual n, not just n mod u.
    The factorization of x depends on n, not n mod u.
    
    So we CAN'T compute F_u purely from n mod u. We need to think differently.
    
    ALTERNATIVE: Instead of computing F_u as a set of residues, compute the 
    guaranteed coverage from the structural divisors {1, x, x²} × {1, n, n²}.
    
    The GUARANTEED divisors of D = n²x² are:
      {1, n, n²} × {1, x, x²} = {n^a * x^b : a,b ∈ {0,1,2}}
    
    These 9 divisors are ALWAYS present (for any n). The residues they hit 
    mod u depend only on n mod u (since x ≡ n*inv(4) mod u).
    
    So the GUARANTEED coverage from these 9 divisors gives a set of ≤ 9 
    residues mod u. If a target is among these 9, the method works 
    (using only guaranteed divisors, no need for other factors of x).
    
    The FULL divisor set (including factors of x beyond {1,x,x²}) can only 
    ADD coverage. So F_u (guaranteed) ⊆ F_u (full), and if the guaranteed 
    cascade already has empty intersection, we're done.
    
    Let's compute F_u using guaranteed divisors only.
    """
    if not isprime(u) or u % 4 != 3:
        return None
    
    inv4 = pow(4, -1, u)
    g = primitive_root(u)
    mod = u - 1  # order of (Z/uZ)*
    
    # For each n mod u (coprime to u):
    # x ≡ n * inv4 mod u
    # Guaranteed divisors of D = n²x²: {n^a * x^b : a,b ∈ {0,1,2}}
    # Their residues mod u: {(n^a * (n*inv4)^b) mod u : a,b ∈ {0,1,2}}
    #                      = {(n^(a+b) * inv4^b) mod u : a,b ∈ {0,1,2}}
    
    # Targets: -x * n^j mod u for j ∈ {0,1,2}
    # = -(n*inv4) * n^j = -n^(j+1) * inv4 mod u
    
    failure_set = set()
    
    for n_mod in range(1, u):
        if n_mod % u == 0:
            continue
        
        x_mod = (n_mod * inv4) % u
        
        # Guaranteed divisor residues mod u
        guaranteed = set()
        for a in range(3):
            for b in range(3):
                # n^a * x^b mod u
                val = pow(n_mod, a, u) * pow(x_mod, b, u) % u
                guaranteed.add(val)
        
        # Target residues mod u
        targets = set()
        for j in range(3):
            # -x * n^j mod u
            target = (-x_mod * pow(n_mod, j, u)) % u
            targets.add(target)
        
        # Check if any target is in guaranteed divisors
        if not (guaranteed & targets):
            failure_set.add(n_mod)
    
    return failure_set

def compute_extended_failure_set(u, extra_primes=None):
    """
    Compute failure set with guaranteed divisors PLUS extra prime factors.
    
    extra_primes: list of primes that x might have (e.g., [2, 3, 5] from 
                  deterministic factor guarantees).
    For each n mod u, we add divisors from these extra primes.
    
    When 2|x: x has factor 2, so x² has factor 4, giving extra divisors {1,2,4}
    When 3|x: x has factor 3, so x² has factor 9, giving extra divisors {1,3,9}
    etc.
    
    But whether 2|x depends on n (x = (n+u)/4). 
    2|x iff n+u ≡ 0 mod 8 iff n ≡ -u mod 8.
    3|x iff n+u ≡ 0 mod 12 iff n ≡ -u mod 12.
    
    So for each n mod u, we know which small primes divide x based on n mod (lcm(u, 8, 12, ...)).
    But we're working mod u only, so we need to consider n mod u and use CRT.
    
    Actually, for the cascade argument, we need:
    - For each u, compute F_u ⊆ {n mod u : u-method fails}
    - F_u should include ALL factors of x, not just guaranteed ones
    
    But we can compute F_u for the GUARANTEED + DETERMINISTIC factors:
    For n mod u, the deterministic factors are those p where p | (n+u)/4,
    which depends on n mod (4p). By CRT, n mod u and n mod 4p are independent
    (when gcd(u, 4p) = 1, which is true for p < u).
    
    So the failure set considering deterministic factor p is:
    F_u(p) = {n mod u : for BOTH n mod 4p = -u mod 4p (p|x) and 
               n mod 4p ≠ -u mod 4p (p∤x), the u-method fails}
    
    When p|x: extra divisors from p² | x² give more coverage
    When p∤x: only guaranteed divisors
    
    The failure set with factor p is:
    F_u^p = F_u(guaranteed only) ∩ F_u(with p factor)
    
    Wait no. For a specific n, EITHER p|x OR p∤x. So:
    - If p|x: the failure set for such n is F_u(with p) 
    - If p∤x: the failure set for such n is F_u(guaranteed)
    
    The total failure set is:
    F_u = (F_u(guaranteed) ∩ {n : p∤x for all deterministic p}) 
        ∪ (F_u(with p) ∩ {n : p|x, other deterministic q∤x})
        ∪ ...
    
    This gets complicated. Let me just compute the guaranteed failure set first
    and see if the cascade product is already small enough.
    """
    pass

# ============ MAIN ANALYSIS ============

print("="*80)
print("DETERMINISTIC COVERAGE LEMMA — CASCADE ANALYSIS")
print("="*80)

u_values = get_u_values(127)
print(f"\nPrime u ≡ 3 mod 4 values up to 127: {u_values}")
print(f"Count: {len(u_values)}")

# Step 1: Compute guaranteed failure sets
print(f"\n{'='*80}")
print("STEP 1: Guaranteed divisor coverage (9 divisors: n^a * x^b, a,b ∈ {0,1,2})")
print("="*80)

failure_sets = {}
cascade_product = 1.0
cascade_product_exact = 1  # numerator
cascade_denom = 1  # denominator

for u in u_values:
    F_u = compute_failure_set(u)
    failure_sets[u] = F_u
    frac = len(F_u) / (u - 1)
    cascade_product *= frac
    cascade_product_exact *= len(F_u)
    cascade_denom *= (u - 1)
    
    print(f"  u = {u:3d}: |F_u| = {len(F_u):3d} / {u-1:3d} = {frac:.4f}  "
          f"F_u = {sorted(F_u) if len(F_u) < 20 else '(too many)'}")

print(f"\n{'='*80}")
print("CASCADE PRODUCT (guaranteed divisors only)")
print("="*80)
print(f"  ∏ |F_u|/(u-1) = {cascade_product:.6e}")
print(f"  Exact: {cascade_product_exact} / {cascade_denom}")
print(f"  1/∏(u-1) = {1/cascade_denom:.6e}")
print(f"  Cascade {'WORKS' if cascade_product < 1/cascade_denom else 'NEEDS MORE'} (guaranteed only)")

# Step 2: Check if guaranteed cascade already gives empty intersection
# The intersection is empty iff the product of densities < 1/∏(u-1)
# This is because CRT gives exactly ∏(u-1) residue classes, and each 
# failure set removes |F_u| of them per u.

print(f"\n{'='*80}")
print("STEP 2: CRT intersection analysis")
print("="*80)

# By CRT, the number of residue classes mod ∏(u-1) that are in ALL F_u is:
# ∏ |F_u| / (nothing, since CRT gives independence)
# Actually, CRT says: the map n → (n mod u_1, ..., n mod u_k) is a bijection
# from Z/(∏u_i)Z to ∏ Z/u_iZ. But we're working with (Z/uZ)*, not Z/uZ.
# The map n → (n mod u_1, ..., n mod u_k) restricted to (Z/∏u_iZ)* 
# is a bijection to ∏ (Z/u_iZ)*.

# So the number of n mod ∏u_i that are in ALL F_u is exactly ∏|F_u|.
# (By CRT independence — each u gives an independent constraint.)

# The intersection is empty iff ∏|F_u| = 0, i.e., at least one F_u = ∅.

print(f"\n  ∏|F_u| = {cascade_product_exact}")
if cascade_product_exact == 0:
    print(f"  → At least one F_u is empty → CASCADE IS EMPTY → DETERMINISTIC PROOF COMPLETE!")
else:
    print(f"  → No F_u is empty → Need to reduce failure sets using extra divisors")
    
    # Step 3: For each u with non-empty F_u, compute the reduction from 
    # deterministic factor guarantees (2|x, 3|x, 5|x)
    print(f"\n{'='*80}")
    print("STEP 3: Reducing failure sets with deterministic factor guarantees")
    print("="*80)
    
    # For each u, and each n in F_u, check if deterministic factors help
    # 2|x iff n ≡ -u mod 8
    # 3|x iff n ≡ -u mod 12
    # 5|x iff n ≡ -u mod 20
    # 7|x iff n ≡ -u mod 28
    
    # When 2|x: x = 2*m, x² = 4*m², divisors of x² include {1, 2, 4} * divisors of m²
    # The extra residues mod u from {1, 2, 4} are:
    #   {d * 1, d * 2, d * 4 mod u : d ∈ existing divisors}
    # This triples the divisor set (roughly)
    
    def compute_failure_with_factors(u, factor_primes=[2, 3, 5, 7]):
        """
        Compute failure set considering deterministic factor guarantees.
        
        For each n mod u in F_u, check if n has deterministic factors
        (based on n mod 4p for each p), and if so, add those factors' 
        divisors to the coverage.
        
        Key insight: for a SPECIFIC n, we know which primes divide x = (n+u)/4
        based on n mod 4p. Since we're working mod u, and gcd(u, 4p) = 1 for p < u,
        n mod u and n mod 4p are INDEPENDENT by CRT.
        
        So for the cascade, we should compute:
        F_u = F_u(guaranteed) for ALL n mod u, regardless of extra factors.
        
        But wait — extra factors can only REDUCE the failure set. So:
        F_u(actual) ⊆ F_u(guaranteed).
        
        The question is: for a specific n, does it have extra factors that 
        push it out of F_u?
        
        For the CRT cascade, we need to work with the ACTUAL failure set,
        which depends on n mod u AND n mod 4p for each p.
        
        By CRT, n mod u and n mod 4p are independent. So:
        P(n in F_u) = P(n in F_u | 2|x) * P(2|x) + P(n in F_u | 2∤x) * P(2∤x)
        
        If 2|x always (for specific u), then P(n in F_u) = P(n in F_u | 2|x).
        
        This gets complex. Let me take a simpler approach:
        
        For each u, compute the MINIMUM failure set over all possible 
        factor combinations. This gives the worst case.
        """
        inv4 = pow(4, -1, u)
        
        # For each n mod u, compute the divisor coverage with all possible 
        # small prime factors and check if ANY factor combination removes n from F_u
        
        # The possible small prime factors of x are those p where 
        # p | (n+u)/4, i.e., n ≡ -u mod 4p.
        # But n mod u and n mod 4p are independent (CRT).
        # So for the purpose of F_u (which is a set of n mod u), we need to 
        # consider ALL possible factorizations of x.
        
        # The MINIMUM coverage (worst case for us) is when x has NO small 
        # prime factors — just the guaranteed {1, x, x²}.
        # The MAXIMUM coverage is when x has ALL possible small prime factors.
        
        # For the cascade to work, we need the MINIMUM coverage to suffice.
        # If the minimum doesn't suffice, we need to show that x MUST have 
        # certain factors (deterministic guarantees).
        
        # Deterministic guarantees from Lemma 4:
        # For n ≡ 1 mod 24: u=23,47,71 → 2|x, 3|x
        # For n ≡ 13 mod 24: u=11,59,83 → 2|x, 3|x; u=107 → 2|x, 3|x, 5|x
        
        # These guarantees depend on n mod 24, which is INDEPENDENT of n mod u
        # (when gcd(u, 24) = 1, true for u > 3).
        
        # So the REAL cascade should be over (n mod u, n mod 24) pairs.
        # By CRT (gcd(u, 24) = 1 for u > 3), these are independent.
        
        # Let me compute F_u(n_mod_24) for each (u, n_mod_24) pair.
        
        results = {}
        
        for n_mod_24 in [1, 13, 5, 17, 25, 29, 37, 41, 49, 53, 61, 65, 73, 77, 85, 89, 97, 101, 109, 113]:
            # Actually, hard cases require n ≡ 1 mod 12, so n mod 24 ∈ {1, 13}
            if n_mod_24 not in [1, 13]:
                continue
            
            failure = set()
            
            for n_mod in range(1, u):
                if n_mod % u == 0:
                    continue
                
                x_mod = (n_mod * inv4) % u
                
                # Guaranteed divisors
                guaranteed = set()
                for a in range(3):
                    for b in range(3):
                        val = pow(n_mod, a, u) * pow(x_mod, b, u) % u
                        guaranteed.add(val)
                
                # Add deterministic factors based on n mod 24
                # For n ≡ 1 mod 24, u = 23: 2|x, 3|x
                # For n ≡ 13 mod 24, u = 11: 2|x, 3|x
                # etc.
                # Check if this (u, n_mod_24) pair has deterministic factors
                
                # 2|x iff n+u ≡ 0 mod 8 iff n ≡ -u mod 8
                # n ≡ n_mod_24 mod 24, so n mod 8 = n_mod_24 mod 8
                has_factor_2 = (n_mod_24 % 8) == ((-u) % 8)
                
                # 3|x iff n+u ≡ 0 mod 12 iff n ≡ -u mod 12
                has_factor_3 = (n_mod_24 % 12) == ((-u) % 12)
                
                # 5|x iff n+u ≡ 0 mod 20 iff n ≡ -u mod 20
                has_factor_5 = (n_mod_24 % 20) == ((-u) % 20)
                
                # 7|x iff n+u ≡ 0 mod 28 iff n ≡ -u mod 28
                has_factor_7 = (n_mod_24 % 28) == ((-u) % 28)
                
                extra_factors = []
                if has_factor_2:
                    extra_factors.append(2)
                if has_factor_3:
                    extra_factors.append(3)
                if has_factor_5:
                    extra_factors.append(5)
                if has_factor_7:
                    extra_factors.append(7)
                
                # Add divisors from extra factors
                # If p|x, then p²|x², giving divisors {1, p, p²} extra
                # These multiply with existing divisors
                full_divisors = set(guaranteed)
                for p in extra_factors:
                    p_mod = p % u
                    if p_mod == 0:
                        continue
                    p2_mod = (p_mod * p_mod) % u
                    extra = {p_mod, p2_mod}
                    # Also multiply with existing
                    new_divs = set(full_divisors)
                    for d in full_divisors:
                        for e in [p_mod, p2_mod]:
                            new_divs.add((d * e) % u)
                    full_divisors = new_divs
                
                # Targets
                targets = set()
                for j in range(3):
                    target = (-x_mod * pow(n_mod, j, u)) % u
                    targets.add(target)
                
                if not (full_divisors & targets):
                    failure.add(n_mod)
            
            results[n_mod_24] = failure
        
        return results

    # Compute failure sets with deterministic factors
    refined_failures = {}
    for u in u_values:
        if u <= 3:
            continue  # u=3 is special (always fails for hard cases)
        refined_failures[u] = compute_failure_with_factors(u)
    
    print(f"\n  Refined failure sets (with deterministic factors):")
    print(f"  {'u':>5} | {'n≡1 mod 24':>12} | {'n≡13 mod 24':>13} | {'Total':>6}")
    print(f"  {'-'*50}")
    
    for u in sorted(refailed_failures.keys()) if 'refailed_failures' in dir() else sorted(refined_failures.keys()):
        f1 = len(refined_failures[u].get(1, set()))
        f13 = len(refined_failures[u].get(13, set()))
        total = f1 + f13
        print(f"  {u:5d} | {f1:12d} | {f13:13d} | {total:6d}")
    
    # Compute refined cascade product
    # For n ≡ 1 mod 24: use F_u(n≡1) for each u
    # For n ≡ 13 mod 24: use F_u(n≡13) for each u
    
    for case_name, n_mod_24 in [("n ≡ 1 mod 24", 1), ("n ≡ 13 mod 24", 13)]:
        product = 1.0
        all_empty = True
        for u in sorted(refined_failures.keys()):
            F = refined_failures[u].get(n_mod_24, set())
            if F:
                all_empty = False
            product *= len(F) / (u - 1)
        
        print(f"\n  Cascade for {case_name}:")
        print(f"    ∏ |F_u|/(u-1) = {product:.6e}")
        print(f"    Any empty F_u: {'YES → PROOF COMPLETE' if all_empty else 'NO'}")

# Step 4: If cascade still doesn't work with guaranteed + deterministic factors,
# compute the EXACT failure sets for each u by considering ALL possible 
# factorizations of x (up to some bound)
print(f"\n{'='*80}")
print("STEP 4: Exact failure sets via full divisor enumeration")
print("="*80)

def compute_exact_failure_set(u, max_x=10000):
    """
    For prime u, compute the EXACT failure set by considering all possible
    prime factorizations of x up to max_x.
    
    For each n mod u, the question is: does there EXIST an x = (n+u)/4 
    (for some n ≡ n_mod mod u) such that the u-method fails?
    
    Since x depends on the actual n (not just n mod u), we need to check
    multiple n values for each residue class.
    
    For n ≡ r mod u, n = r + k*u for k = 0, 1, 2, ...
    x = (n+u)/4 = (r + k*u + u)/4 = (r + u)/4 + k*u/4
    
    For k = 0: x = (r+u)/4 (might not be integer if r+u not div by 4)
    For k = 1: x = (r+2u)/4
    etc.
    
    Actually, x = (n+u)/4 requires 4 | (n+u). So n ≡ -u mod 4.
    Combined with n ≡ r mod u, by CRT: n ≡ r mod u AND n ≡ -u mod 4.
    Since gcd(u, 4) = 1 for u > 2, there's a unique n mod 4u.
    
    So for each r mod u, there's a unique n mod 4u, and x = (n+u)/4 is determined.
    
    The factorization of x varies as n = n_0 + 4u*k for k = 0, 1, 2, ...
    x = (n_0 + 4u*k + u)/4 = x_0 + u*k where x_0 = (n_0 + u)/4.
    
    So x ranges over x_0, x_0 + u, x_0 + 2u, ...
    
    The factorization changes with each k, so the u-method might work for 
    some k and fail for others.
    
    For the CASCADE argument, we need: for EACH n, SOME u works.
    So for each n (i.e., each k for each residue class), the cascade 
    over u values must succeed.
    
    The guaranteed failure set F_u is the set of n mod u where the u-method 
    fails for ALL possible factorizations of x (i.e., all k).
    
    F_u = {r mod u : for ALL k ≥ 0, u-method fails for x = x_0 + u*k}
    
    This is the INTERSECTION over k of the per-k failure sets.
    
    For the cascade, ∩_u F_u = ∅ means: for each n, at least one u works 
    for the SPECIFIC factorization at that n.
    
    But F_u (intersection over k) is too restrictive — it requires ALL 
    factorizations to fail. We need: for each n, SOME u works, which means
    for the SPECIFIC k determined by n, SOME u works.
    
    The right approach: compute the failure set for a SPECIFIC k (i.e., 
    specific n), and show the cascade works for each k.
    
    But this requires knowing the factorization for each n, which is the 
    computational verification we've already done.
    
    For the DETERMINISTIC proof, we need to show that for ANY factorization
    of x, the cascade works. This means: for each r mod u and each possible 
    factorization of x, at least one u in the cascade covers it.
    
    The guaranteed + deterministic factor approach above is the right one —
    it gives a LOWER BOUND on the divisor coverage, and if the cascade 
    product is small enough, we're done.
    
    Let me compute it properly.
    """
    pass

# Let me just compute and print the results
print("\nComputing refined failure sets with deterministic factors...")

refined = {}
for u in u_values:
    if u == 3:
        # u=3 always fails for hard cases (n ≡ 1 mod 3, all divisors ≡ 1 mod 3)
        refined[3] = {1: set(range(1, 3)), 13: set(range(1, 3))}  # all of (Z/3Z)*
        continue
    refined[u] = compute_failure_with_factors(u)

print(f"\n  {'u':>5} | {'F_u (n≡1)':>10} | {'F_u (n≡13)':>11} | {'|F1|/(u-1)':>10} | {'|F13|/(u-1)':>11}")
print(f"  {'-'*65}")

for case_name, n_mod_24 in [("n ≡ 1 mod 24", 1), ("n ≡ 13 mod 24", 13)]:
    product = 1.0
    for u in u_values:
        F = refined[u].get(n_mod_24, set())
        frac = len(F) / (u - 1) if u > 1 else 0
        product *= frac
        print(f"  {u:5d} | {len(F):10d} | {len(refined[u].get(13 if n_mod_24 == 1 else 1, set())):11d} | {frac:10.6f} | {len(refined[u].get(13 if n_mod_24 == 1 else 1, set()))/(u-1):11.6f}")
    print(f"\n  Cascade product for {case_name}: {product:.6e}")
    
    # Check against 1/∏(u-1)
    denom = 1
    for u in u_values:
        denom *= (u - 1)
    
    print(f"  1/∏(u-1) = {1/denom:.6e}")
    print(f"  Ratio: {product * denom:.6f}")
    print(f"  → {'EMPTY INTERSECTION (PROOF COMPLETE)' if product == 0 else 'NEEDS REFINEMENT'}")
    print()

# Save results
results = {
    'u_values': u_values,
    'guaranteed_failures': {str(u): sorted(list(f)) for u, f in failure_sets.items()},
    'refined_failures': {
        str(u): {
            str(nm): sorted(list(f)) 
            for nm, f in refined[u].items()
        }
        for u in refined
    }
}

with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/cascade_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\nResults saved to cascade_results.json")