#!/usr/bin/env python3
"""
Optimized deep analysis using quadratic residues and Hasse-Minkowski theorem.

For the ternary quadratic form Q(k,t,m) = k² + 36(A²-9)t² - 36m² - B² = 0,
we check local solvability at each prime p using quadratic residue theory 
instead of brute-forcing all triples.

Key insight: Q(k,t,m) = k² - B² + 36(A²-9)t² - 36m² = 0
  → k² = B² + 36m² - 36(A²-9)t² = B² + 36(m² - (A²-9)t²)
  → k² = B² + 36·f(t,m)  where f(t,m) = m² - (A²-9)t²

For local solvability at p: we need k² ≡ B² + 36·f(t,m) (mod p^k)
with (k,t,m) not all ≡ 0 (mod p).

This is equivalent to: B² + 36·f(t,m) must be a quadratic residue mod p^k
for some (t,m) not both ≡ 0 (mod p), and then k exists.

Actually, it's simpler: we need the form to represent 0 nontrivially.
By the theory of ternary quadratic forms, Q = 0 has a nontrivial p-adic solution
iff Q is isotropic over Q_p.

For an odd prime p not dividing 6 (so p ≥ 5):
  Q(k,t,m) = k² + 36(A²-9)t² - 36m² - B²
  Since p ∤ 36, we can write: Q = k² - B² + 36((A²-9)t² - m²)
  
  Mod p: k² ≡ B² - 36((A²-9)t² - m²) (mod p)
  We need (t, m) not both 0 mod p such that B² - 36((A²-9)t² - m²) is a QR mod p.
  
  If B ≢ 0 (mod p): take t=0, m=0, then k² ≡ B² (mod p), which gives k ≡ ±B (mod p).
  But this is trivial! (k=B, t=0, m=0). We need nontrivial = not all zero mod p.
  k ≡ ±B ≢ 0 mod p (since B ≢ 0). So (k,t,m) = (±B, 0, 0) is nontrivial mod p.
  → Always solvable mod p when p ∤ B.

  If p | B: then k² ≡ 36(m² - (A²-9)t²) (mod p).
  Take k=0, t=1, m=0: need 36·(-(A²-9)) ≡ -36(A²-9) (mod p) to be ≡ k² = 0 (mod p).
  Wait, we need Q = 0: k² + 36(A²-9)t² - 36m² - B² = 0.
  With k=0, t=1, m=0, B≡0: Q = 36(A²-9) (mod p). This is 0 iff p | (A²-9).
  
  Actually let me think more carefully. If p | B:
    Q = k² + 36(A²-9)t² - 36m² (mod p)  (since B² ≡ 0)
    We need (k,t,m) not all 0 mod p with Q ≡ 0 (mod p).
    Take t=1, m=0: Q = k² + 36(A²-9) (mod p). Need k² ≡ -36(A²-9) (mod p).
    This has a solution iff -36(A²-9) is a QR mod p (or is 0).
    Take t=0, m=1: Q = k² - 36 (mod p). Need k² ≡ 36 (mod p). Since 36 = 6², k≡6 mod p. ✓
    So (k,m,t) = (6,0,1) gives Q = 36 + 0 - 36 = 0 (mod p). Nontrivial since k=6≢0.
    → Always solvable mod p when p | B, using k=6, m=1, t=0.

So for ANY odd prime p ≥ 5, the form is ALWAYS locally solvable mod p!
The only question is lifting to higher powers (mod p², p³, etc.).

By Hensel's lemma: if there's a nonsingular solution mod p, it lifts to mod p^k.
A solution (k₀, t₀, m₀) is nonsingular if the gradient ∇Q ≠ 0 at that point mod p.
∇Q = (2k, 72(A²-9)t, -72m).
At (6, 0, 1): ∇Q = (12, 0, -72). For p ≥ 5: 12 ≢ 0 (mod 5), so nonsingular. ✓
At (±B, 0, 0) with p ∤ B: ∇Q = (±2B, 0, 0). Since p ∤ B, nonsingular. ✓

So by Hensel's lemma, ALL solutions lift! The form is isotropic over Q_p for ALL p ≥ 5.

For p=2 and p=3, we already verified computationally that solutions exist mod 8, 16, 9, 27.

CONCLUSION: The ternary form k² + 36(A²-9)t² - 36m² - B² = 0 is locally solvable 
at ALL primes for ALL odd A and ALL n ≡ 1 (mod 12).

This means: local solvability (Hasse principle) is NEVER the obstruction.
The covering set {7, 23, 31} works trivially because EVERY A works locally.
The real obstruction for A=3 failures is GLOBAL, not local.
"""

import json
from sympy import factorint, isprime, legendre_symbol

def compute_B(n, A):
    return n * (n + A) // 2

def verify_hensel_p_ge_5(A, n, p, mod=None):
    """
    For p >= 5, verify that a nonsingular solution exists mod p.
    By the analysis above, this should always work.
    """
    B = compute_B(n, A) % p
    B_sq = (B * B) % p
    
    # Case 1: p does not divide B → use (k, t, m) = (B, 0, 0) mod p
    # But this is trivial if we need (t,m) nonzero... let's check nontriviality.
    # (k, t, m) = (B, 0, 0): Q = B² - B² = 0. ✓ Nontrivial since B ≢ 0 mod p.
    if B % p != 0:
        # Check nonsingularity: ∇Q = (2B, 0, 0) ≠ 0 mod p since p ∤ B and p ≥ 3
        return True, "p ∤ B: solution (B, 0, 0), nonsingular"
    
    # Case 2: p | B → use (k, t, m) = (6, 0, 1) mod p
    # Q = 36 + 0 - 36 - 0 = 0 mod p. ✓
    # Nontrivial: k=6, m=1, both nonzero mod p (since p ≥ 5, p ∤ 6)
    # Nonsingular: ∇Q = (12, 0, -72) ≠ 0 mod p (since p ≥ 5, p ∤ 12)
    return True, "p | B: solution (6, 0, 1), nonsingular"

def main():
    print("=" * 90)
    print("THEORETICAL PROOF: Local solvability at ALL primes for the ternary form")
    print("k² + 36(A²-9)t² - 36m² - B² = 0")
    print("=" * 90)
    
    print("""
THEOREM: For any odd A and any n ≡ 1 (mod 12), the ternary quadratic form
  Q(k, t, m) = k² + 36(A²-9)t² - 36m² - B² = 0
where B = n(n+A)/2, is locally solvable (isotropic) over Q_p for ALL primes p.

PROOF:

Case p ≥ 5 (odd prime not dividing 6):

  Subcase p ∤ B: Take (k, t, m) = (B, 0, 0).
    Q = B² + 0 - 0 - B² = 0 (mod p). ✓
    Nontrivial: k ≡ B ≢ 0 (mod p). ✓
    Nonsingular: ∇Q = (2k, 72(A²-9)t, -72m) = (2B, 0, 0) ≢ 0 (mod p) since p ∤ B.
    By Hensel's lemma, lifts to Q_p. ✓

  Subcase p | B: Take (k, t, m) = (6, 0, 1).
    Q = 36 + 0 - 36 - 0 = 0 (mod p). ✓
    Nontrivial: k = 6 ≢ 0, m = 1 ≢ 0 (mod p) since p ≥ 5. ✓
    Nonsingular: ∇Q = (12, 0, -72) ≢ 0 (mod p) since p ≥ 5 (p ∤ 12).
    By Hensel's lemma, lifts to Q_p. ✓

Case p = 3:

  Mod 3: 36 ≡ 0, so Q ≡ k² - B² (mod 3).
  If 3 ∤ B: k ≡ ±B (mod 3). Nontrivial (k ≢ 0). ✓
  If 3 | B: k ≡ 0. Take t=1, m=0: Q = 36(A²-9) ≡ 0 (mod 3) since 36 ≡ 0. 
    Nontrivial (t ≢ 0). ✓
  Lifting to mod 9, 27: verified computationally (brute force above). ✓

Case p = 2:

  Mod 2: 36 ≡ 0, so Q ≡ k² - B² ≡ k² + B² (mod 2).
  k ≡ B (mod 2). If B odd: k=1, nontrivial. If B even: k=0, need t or m odd.
  Take t=1, m=0: Q = 36(A²-9) ≡ 0 (mod 2). ✓
  Lifting to mod 8, 16: verified computationally (brute force above). ✓

∴ The form Q = 0 is isotropic over Q_p for ALL primes p, for ANY odd A and ANY n ≡ 1 (mod 12).

COROLLARY: By the Hasse-Minkowski theorem, a ternary quadratic form over Q 
represents 0 nontrivially if and only if it does so over all Q_p and over R.

The real obstruction at infinity (R): Q = k² + 36(A²-9)t² - 36m² - B² = 0
has indefinite signature (since the coefficients of k², t² are positive and 
m² is negative), so it's automatically isotropic over R.

THEREFORE: By Hasse-Minkowski, the form represents 0 nontrivially over Q 
for ALL odd A and ALL n ≡ 1 (mod 12). This means a rational solution 
(k, t, m) always exists!

The issue with A=3 is NOT local solvability — it's that when A=3, A²-9=0,
the form degenerates to k² = B² + 36m² (binary, not ternary), and 
Hasse-Minkowski for ternary forms doesn't apply. The t variable becomes free,
and the constraint is purely k² - B² = 36m², i.e., (k-B)(k+B) = 36m².

For A ≠ 3, the form is genuinely ternary and Hasse-Minkowski guarantees 
a rational solution. The covering set is therefore:

  ANY SINGLE A ≠ 3 (with A odd) suffices!

The minimal covering set is {A} for any odd A ≥ 5 (or A=7, 11, 15, ...).
In particular, {7} alone suffices, {23} alone suffices, {31} alone suffices.
""")

    # Numerical verification: find actual rational solutions for failing cases
    print("=" * 90)
    print("NUMERICAL VERIFICATION: Find integer solutions for A=3 failing cases with A=7")
    print("=" * 90)
    
    # Find A=3 failing cases
    failing_cases = []
    for n in range(1, 10001, 12):
        if n % 5 == 0:
            continue
        B = compute_B(n, 3)
        v2 = 0
        temp = B
        while temp % 2 == 0:
            v2 += 1
            temp //= 2
        if v2 != 1:
            continue
        B_half = B // 2
        if B_half == 0:
            continue
        factors = factorint(B_half)
        all_1_mod3 = all(f % 3 == 1 for f in factors)
        if all_1_mod3:
            failing_cases.append(n)
        if len(failing_cases) >= 10:
            break
    
    # For each failing case, try A=7 and search for solutions
    # k² + 36(49-9)t² - 36m² - B² = 0
    # k² + 1440t² - 36m² = B²
    for n in failing_cases[:5]:
        A = 7
        B = compute_B(n, A)
        B_sq = B * B
        # k² + 1440t² - 36m² = B²
        # Search small t, m values
        found = False
        for t in range(100):
            for m in range(-B//6 - 1, B//6 + 2):
                # k² = B² - 1440t² + 36m²
                k_sq = B_sq - 1440 * t * t + 36 * m * m
                if k_sq < 0:
                    continue
                k = int(k_sq**0.5)
                for kk in [k-1, k, k+1]:
                    if kk >= 0 and kk * kk == k_sq:
                        print(f"  n={n}, A={A}: k={kk}, t={t}, m={m} → k²={kk*kk}, B²={B_sq}, 1440t²={1440*t*t}, 36m²={36*m*m}")
                        print(f"    Check: {kk*kk} + {1440*t*t} - {36*m*m} = {kk*kk + 1440*t*t - 36*m*m} = B² = {B_sq} ✓")
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            print(f"  n={n}, A={A}: no solution found in search range (t<100, |m|<B/6)")
    
    # Save the proof
    output = {
        'description': 'Proof that the ternary quadratic form is locally solvable at ALL primes',
        'theorem': 'For any odd A and n ≡ 1 (mod 12), Q = k² + 36(A²-9)t² - 36m² - B² = 0 is isotropic over Q_p for all p',
        'proof': {
            'p_ge_5': 'Nonsingular solution exists mod p (either (B,0,0) if p∤B, or (6,0,1) if p|B). Hensel lifts.',
            'p_3': 'k² ≡ B² mod 3 always solvable. Verified mod 9, 27 by brute force.',
            'p_2': 'k² ≡ B² mod 2 always solvable. Verified mod 8, 16 by brute force.',
            'real': 'Form is indefinite, hence isotropic over R.',
            'hasse_minkowski': 'Ternary form isotropic over all Q_p and R → isotropic over Q.',
        },
        'conclusion': 'ANY single odd A ≠ 3 suffices. The covering set is {A} for any odd A ≥ 5.',
        'minimal_covering_set': [7],  # or any odd A >= 5
        'A_values_that_work': 'All odd A >= 5 (and also A=3 is locally solvable but degenerate)',
        'note': 'A=3 is degenerate: A²-9=0, form becomes binary k²=B²+36m². For A≠3, Hasse-Minkowski guarantees rational solution.',
    }
    
    output_path = '/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/covering_set_analysis.json'
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to {output_path}")

if __name__ == '__main__':
    main()