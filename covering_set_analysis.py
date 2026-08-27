#!/usr/bin/env python3
"""
Erdős-Straus Conjecture: Covering Set Analysis
=============================================
For n ≡ 1 (mod 12), n ≢ 0 (mod 5), A=3 fails when v₂(B)=1 AND all prime factors of B/2 ≡ 1 (mod 3).

For these failing cases, the equation becomes a ternary quadratic form:
  k² + 36t²(A² - 9) = B² + 36m²
  where B = n(n+A)/2

We need to find A values such that this form is locally solvable at p=2 and p=3
for ALL relevant residue classes of n.

Residue classes: n mod 72 ∈ {1, 13, 25, 37, 49, 61} (n ≡ 1 mod 12)
Then filter for n ≢ 0 (mod 5).

Key insight: Since n ≡ 1 (mod 12), n is odd. We only test odd A, so n+A is even,
making B = n(n+A)/2 an integer. The division by 2 is exact integer division.
"""

import json
from itertools import combinations

def compute_B_mod(A, n, modulus):
    """Compute B = n(n+A)/2 mod modulus, where n is odd and A is odd (so n+A is even)."""
    # n+A is even, so (n+A)//2 is exact. But we need it mod `modulus`.
    # Since n+A is even, we can compute (n+A)//2 mod modulus directly.
    n_plus_A = n + A
    # n_plus_A is even, so integer division is exact
    half = n_plus_A // 2
    B = (n * half) % modulus
    return B

def local_sol_2_mod8(A, n):
    """
    Check local solvability at p=2 (mod 8).
    
    Form: k² + 36t²(A²-9) - 36m² - B² = 0
    where B = n(n+A)/2.
    
    Mod 8: 36 ≡ 4 (mod 8), so:
      k² + 4t²(A²-9) - 4m² - B² ≡ 0 (mod 8)
    
    Nontrivial: (k, t, m) not all ≡ 0 (mod 2).
    """
    B = compute_B_mod(A, n, 8)
    B_sq = (B * B) % 8
    A2m9 = (A * A - 9) % 8
    
    for k in range(8):
        for t in range(8):
            for m in range(8):
                if k % 2 == 0 and t % 2 == 0 and m % 2 == 0:
                    continue
                val = (k*k + 4*t*t*A2m9 - 4*m*m - B_sq) % 8
                if val == 0:
                    return True, B
    
    return False, B

def local_sol_2_mod16(A, n):
    """
    Check local solvability at p=2 (mod 16) for more rigorous check.
    
    Form: k² + 36t²(A²-9) - 36m² - B² = 0
    
    Mod 16: 36 ≡ 4 (mod 16), so:
      k² + 4t²(A²-9) - 4m² - B² ≡ 0 (mod 16)
    
    Nontrivial: (k, t, m) not all ≡ 0 (mod 2).
    """
    B = compute_B_mod(A, n, 16)
    B_sq = (B * B) % 16
    A2m9 = (A * A - 9)  # Keep full value for mod 16 computation
    
    for k in range(16):
        for t in range(16):
            for m in range(16):
                if k % 2 == 0 and t % 2 == 0 and m % 2 == 0:
                    continue
                val = (k*k + 36*t*t*(A2m9) - 36*m*m - B_sq) % 16
                if val == 0:
                    return True, B
    
    return False, B

def local_sol_3_mod9(A, n):
    """
    Check local solvability at p=3 (mod 9).
    
    Form: k² + 36t²(A²-9) - 36m² - B² = 0
    where B = n(n+A)/2.
    
    Mod 9: 36 ≡ 0 (mod 9), so:
      k² - B² ≡ 0 (mod 9)
    
    Nontrivial: (k, t, m) not all ≡ 0 (mod 3).
    """
    B = compute_B_mod(A, n, 9)
    B_sq = (B * B) % 9
    A2m9 = (A * A - 9)
    
    for k in range(9):
        for t in range(9):
            for m in range(9):
                if k % 3 == 0 and t % 3 == 0 and m % 3 == 0:
                    continue
                val = (k*k + 36*t*t*A2m9 - 36*m*m - B_sq) % 9
                if val == 0:
                    return True, B
    
    return False, B

def local_sol_3_mod27(A, n):
    """
    Check local solvability at p=3 (mod 27) for more rigorous check.
    
    Form: k² + 36t²(A²-9) - 36m² - B² = 0
    
    Mod 27: 36 ≡ 9 (mod 27), so:
      k² + 9t²(A²-9) - 9m² - B² ≡ 0 (mod 27)
    
    Nontrivial: (k, t, m) not all ≡ 0 (mod 3).
    """
    B = compute_B_mod(A, n, 27)
    B_sq = (B * B) % 27
    A2m9 = (A * A - 9)
    
    for k in range(27):
        for t in range(27):
            for m in range(27):
                if k % 3 == 0 and t % 3 == 0 and m % 3 == 0:
                    continue
                val = (k*k + 36*t*t*A2m9 - 36*m*m - B_sq) % 27
                if val == 0:
                    return True, B
    
    return False, B

def main():
    # Residue classes: n mod 72 ∈ {1, 13, 25, 37, 49, 61} (n ≡ 1 mod 12)
    residue_classes = [1, 13, 25, 37, 49, 61]
    
    # A values to test: odd values from 3 to 47
    A_values = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47]
    
    results = {}
    
    print("=" * 90)
    print("Erdős-Straus Conjecture: Covering Set Analysis")
    print("For n ≡ 1 (mod 12), n ≢ 0 (mod 5)")
    print("Residue classes mod 72: {1, 13, 25, 37, 49, 61}")
    print("A values tested:", A_values)
    print("=" * 90)
    
    for n_mod in residue_classes:
        print(f"\n--- n ≡ {n_mod} (mod 72) ---")
        results[n_mod] = {}
        
        for A in A_values:
            B_mod8 = compute_B_mod(A, n_mod, 8)
            B_mod9 = compute_B_mod(A, n_mod, 9)
            B_mod16 = compute_B_mod(A, n_mod, 16)
            B_mod27 = compute_B_mod(A, n_mod, 27)
            
            sol2_8, _ = local_sol_2_mod8(A, n_mod)
            sol2_16, _ = local_sol_2_mod16(A, n_mod)
            sol3_9, _ = local_sol_3_mod9(A, n_mod)
            sol3_27, _ = local_sol_3_mod27(A, n_mod)
            
            both_8_9 = sol2_8 and sol3_9
            both_16_9 = sol2_16 and sol3_9
            both_16_27 = sol2_16 and sol3_27
            both_8_27 = sol2_8 and sol3_27
            
            results[n_mod][A] = {
                'B_mod8': B_mod8,
                'B_mod9': B_mod9,
                'B_mod16': B_mod16,
                'B_mod27': B_mod27,
                'sol_p2_mod8': sol2_8,
                'sol_p2_mod16': sol2_16,
                'sol_p3_mod9': sol3_9,
                'sol_p3_mod27': sol3_27,
                'sol_both_8_9': both_8_9,
                'sol_both_16_9': both_16_9,
                'sol_both_16_27': both_16_27,
                'sol_both_8_27': both_8_27,
            }
            
            print(f"  A={A:3d}: B≡{B_mod8}(mod8), B≡{B_mod9}(mod9), B≡{B_mod16}(mod16), B≡{B_mod27}(mod27)")
            print(f"        p2(8):{'✓' if sol2_8 else '✗'} p2(16):{'✓' if sol2_16 else '✗'} p3(9):{'✓' if sol3_9 else '✗'} p3(27):{'✓' if sol3_27 else '✗'}")
            print(f"        BOTH(8,9):{'✓' if both_8_9 else '✗'} BOTH(16,9):{'✓' if both_16_9 else '✗'} BOTH(16,27):{'✓' if both_16_27 else '✗'} BOTH(8,27):{'✓' if both_8_27 else '✗'}")
    
    # ============ COVERING SET ANALYSIS ============
    print("\n" + "=" * 90)
    print("COVERING SET ANALYSIS")
    print("=" * 90)
    
    # Use the most rigorous check: mod 16 for p=2, mod 27 for p=3
    # But also check the standard mod 8/mod 9
    
    for check_name, check_key in [("mod 8 / mod 9", "sol_both_8_9"), 
                                   ("mod 16 / mod 9", "sol_both_16_9"),
                                   ("mod 16 / mod 27", "sol_both_16_27"),
                                   ("mod 8 / mod 27", "sol_both_8_27")]:
        print(f"\n{'='*60}")
        print(f"Check level: {check_name}")
        print(f"{'='*60}")
        
        covering = {}
        for n_mod in residue_classes:
            working_A = [A for A in A_values if results[n_mod][A][check_key]]
            covering[n_mod] = working_A
            print(f"  n ≡ {n_mod:3d} (mod 72): A values that work: {working_A}")
        
        # Check singles
        for A in A_values:
            if all(A in covering[n_mod] for n_mod in residue_classes):
                print(f"\n  *** SINGLE A = {A} covers ALL residue classes! ***")
        
        # Check pairs
        pairs_found = False
        for i, A1 in enumerate(A_values):
            for A2 in A_values[i+1:]:
                covered = all(A1 in covering[n_mod] or A2 in covering[n_mod] 
                            for n_mod in residue_classes)
                if covered:
                    print(f"  Pair A ∈ {{{A1}, {A2}}} covers ALL")
                    pairs_found = True
        if not pairs_found:
            print("  No covering pair found.")
        
        # Check triples
        triples = []
        for i, A1 in enumerate(A_values):
            for j, A2 in enumerate(A_values[i+1:], i+1):
                for A3 in A_values[j+1:]:
                    covered = all(
                        A1 in covering[n_mod] or A2 in covering[n_mod] or A3 in covering[n_mod]
                        for n_mod in residue_classes
                    )
                    if covered:
                        triples.append((A1, A2, A3))
        
        if triples:
            print(f"\n  Found {len(triples)} covering triples:")
            for triple in triples[:30]:
                detail = []
                for n_mod in residue_classes:
                    covers = [str(A) for A in triple if A in covering[n_mod]]
                    detail.append(f"n≡{n_mod}:{'+'.join(covers) if covers else 'NONE'}")
                print(f"    A ∈ {{{', '.join(map(str, triple))}}} → {' | '.join(detail)}")
        else:
            print("  No covering triple found.")
        
        # Check quadruples if no triple works
        if not triples:
            quads = []
            for i, A1 in enumerate(A_values):
                for j, A2 in enumerate(A_values[i+1:], i+1):
                    for k, A3 in enumerate(A_values[j+1:], j+1):
                        for A4 in A_values[k+1:]:
                            covered = all(
                                any(A in covering[n_mod] for A in [A1, A2, A3, A4])
                                for n_mod in residue_classes
                            )
                            if covered:
                                quads.append((A1, A2, A3, A4))
            if quads:
                print(f"\n  Found {len(quads)} covering quadruples:")
                for quad in quads[:20]:
                    detail = []
                    for n_mod in residue_classes:
                        covers = [str(A) for A in quad if A in covering[n_mod]]
                        detail.append(f"n≡{n_mod}:{'+'.join(covers) if covers else 'NONE'}")
                    print(f"    A ∈ {{{', '.join(map(str, quad))}}} → {' | '.join(detail)}")
            else:
                print("  No covering quadruple found.")
    
    # ============ TEST {7, 23, 31} ============
    print("\n" + "=" * 90)
    print("VERIFICATION: A ∈ {7, 23, 31}")
    print("=" * 90)
    
    test_set = [7, 23, 31]
    for check_name, check_key in [("mod 8/mod 9", "sol_both_8_9"), 
                                   ("mod 16/mod 9", "sol_both_16_9"),
                                   ("mod 16/mod 27", "sol_both_16_27")]:
        print(f"\n  Check: {check_name}")
        all_ok = True
        for n_mod in residue_classes:
            covers = [str(A) for A in test_set if results[n_mod][A][check_key]]
            ok = any(A in [7, 23, 31] and results[n_mod][A][check_key] for A in test_set)
            # More precisely:
            ok = any(results[n_mod][A][check_key] for A in test_set)
            if not ok:
                all_ok = False
            print(f"    n ≡ {n_mod:3d} (mod 72): {'✓' if ok else '✗'} covered by {covers}")
        print(f"  → {'COVERS ALL' if all_ok else 'DOES NOT COVER ALL'}")
    
    # ============ MINIMAL COVERING SET ============
    print("\n" + "=" * 90)
    print("MINIMAL COVERING SET (most rigorous: mod 16 / mod 27)")
    print("=" * 90)
    
    check_key = "sol_both_16_27"
    covering = {}
    for n_mod in residue_classes:
        covering[n_mod] = [A for A in A_values if results[n_mod][A][check_key]]
    
    for size in range(1, 5):
        found = False
        for combo in combinations(A_values, size):
            covered = all(
                any(A in covering[n_mod] for A in combo)
                for n_mod in residue_classes
            )
            if covered:
                print(f"\nMinimal covering set (size {size}): A ∈ {{{', '.join(map(str, combo))}}}")
                for n_mod in residue_classes:
                    covers = [str(A) for A in combo if A in covering[n_mod]]
                    print(f"  n ≡ {n_mod:3d} (mod 72): covered by {{{', '.join(covers)}}}")
                found = True
                break
        if found:
            break
    
    # Also for mod 8/mod 9
    print("\nMinimal covering set (mod 8/mod 9):")
    check_key = "sol_both_8_9"
    covering = {}
    for n_mod in residue_classes:
        covering[n_mod] = [A for A in A_values if results[n_mod][A][check_key]]
    
    for size in range(1, 5):
        found = False
        for combo in combinations(A_values, size):
            covered = all(
                any(A in covering[n_mod] for A in combo)
                for n_mod in residue_classes
            )
            if covered:
                print(f"Minimal covering set (size {size}): A ∈ {{{', '.join(map(str, combo))}}}")
                for n_mod in residue_classes:
                    covers = [str(A) for A in combo if A in covering[n_mod]]
                    print(f"  n ≡ {n_mod:3d} (mod 72): covered by {{{', '.join(covers)}}}")
                found = True
                break
        if found:
            break
    
    # Save results
    output = {
        'description': 'Local solvability analysis for Erdős-Straus conjecture covering set',
        'parameters': {
            'residue_classes_mod72': residue_classes,
            'A_values_tested': A_values,
            'n_condition': 'n ≡ 1 (mod 12), n ≢ 0 (mod 5)',
            'form': 'k² + 36t²(A²-9) = B² + 36m², B = n(n+A)/2',
        },
        'results': {str(k): v for k, v in results.items()},
        'test_set_7_23_31': {
            'covers_mod8_mod9': all(any(results[n_mod][A]['sol_both_8_9'] for A in [7,23,31]) for n_mod in residue_classes),
            'covers_mod16_mod9': all(any(results[n_mod][A]['sol_both_16_9'] for A in [7,23,31]) for n_mod in residue_classes),
            'covers_mod16_mod27': all(any(results[n_mod][A]['sol_both_16_27'] for A in [7,23,31]) for n_mod in residue_classes),
        }
    }
    
    output_path = '/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/covering_set_analysis.json'
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to {output_path}")

if __name__ == '__main__':
    main()