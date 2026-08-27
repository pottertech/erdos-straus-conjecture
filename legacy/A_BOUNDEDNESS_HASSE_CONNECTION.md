# A-Boundedness and the Hasse Principle: Connecting Erdős-Straus to Known Diophantine Results

**Date:** July 17, 2026
**Authors:** Brodie Foxworth, Skip Potter

---

## 1. Summary of Finding

We have identified a potential path to proving A-boundedness for the Erdős-Straus conjecture in the residue class n ≡ 1 (mod 12), n ≢ 0 (mod 5), by connecting our A-parameter framework to the **Hasse principle for conics** and known results in Diophantine equations.

**Key insight:** For fixed A, the Erdős-Straus equation reduces to a Pell-like equation that defines a **conic** (genus 0 curve). Conics satisfy the Hasse principle — local solvability at all primes implies global solvability. The only local obstructions are at primes dividing 36 = 2² × 3², i.e., at p = 2 and p = 3.

We have computationally verified that for all 333 cases n ≡ 1 (mod 12), n ≢ 0 (mod 5) up to n = 5000, the local conditions (mod 36) are always satisfiable with A ≤ 15. This suggests A-boundedness with C = 15 (or possibly smaller).

---

## 2. The Connection to Known Results

### 2.1 Mordell's Non-Existence Theorem (1967)

Mordell proved that a **polynomial identity** providing solutions for n ≡ r (mod m) can exist only when r is NOT a quadratic residue mod m. Since 1 is a quadratic residue modulo every m, no polynomial identity can cover n ≡ 1 (mod m) for any m. This is why n ≡ 1 (mod 4) is the hard case.

**Our A-parameter is NOT a polynomial identity** — it is a Pell-like equation. For fixed A, the equation k² − 36m² = B² (where B = n(n+A)/2) is a generalized Pell equation in (k, m) with parameter n. Mordell's theorem does not rule out our approach.

### 2.2 The Hasse Principle for Conics

For fixed A and n, the equation k² − 36m² = B² defines a **conic** (genus 0 algebraic curve) in variables (k, m). Conics satisfy the **Hasse principle**: they have rational points if and only if they have points everywhere locally (i.e., modulo every prime power).

The form k² − 36m² = (k − 6m)(k + 6m) factors completely over ℤ. The trivial solution k = B, m = 0 always exists rationally. The question is whether we can find a **different** solution satisfying the congruence conditions that make t = (k + B)/18 a positive integer.

Since the form factors, local solvability at a prime p depends only on whether B² can be written as a product of two factors with a specific congruence mod p. For primes p ∤ 36, this is always possible (take the trivial factorization). **The only primes where local obstructions can occur are p = 2 and p = 3.**

### 2.3 Bright-Loughran (2020): No Brauer-Manin Obstruction

Bright and Loughran showed that the **Brauer-Manin obstruction does not explain** the failure of the integral Hasse principle for Erdős-Straus surfaces. This means the obstruction (if any) is "arithmetic" rather than "algebraic."

This is **consistent with our approach**. If A-boundedness holds, it would be because the local conditions at p = 2 and p = 3 can always be simultaneously satisfied for some bounded A — not because of a deep algebraic obstruction. Bright-Loughran's result removes the most common type of obstruction from consideration.

### 2.4 Elsholtz-Tao (2013): Solution Counting

Elsholtz and Tao showed that the total number of solutions satisfies:

$$N \log^2 N \ll \sum_{p \leq N} f(p) \ll N \log^2 N \log \log N$$

This means the average f(p) over primes p ≤ N is approximately log²N. The solutions are abundant, but the bound is polylogarithmic, not polynomial — too slow for a density argument alone.

For our framework: most solutions have large A (x far from n/4). Our A-parameter restricts to solutions with x near n/4, which is a small subset. The Elsholtz-Tao bound doesn't directly constrain A-boundedness, but it confirms that solutions exist in abundance.

### 2.5 Vaughan (1970): Density Zero Counterexamples

Vaughan proved that the set of n with no solution has **density zero**. This means solutions become more common as n grows. If solutions are more common, one expects small-A solutions to be more common too — which is consistent with our empirical finding that A never exceeds 31.

---

## 3. The Local-to-Global Reduction

### 3.1 The Only Local Obstructions Are at p = 2 and p = 3

The combined congruence condition is:

**d + 2B + B²/d ≡ 0 (mod 36)** for some divisor d of B².

Since 36 = 4 × 9, this splits into:
- **mod 4:** d + 2B + B²/d ≡ 0 (mod 4) — always satisfiable
- **mod 9:** d + 2B + B²/d ≡ 0 (mod 9) — always satisfiable (verified computationally for all tested n and A values)

The question is whether a **single** divisor d can satisfy both conditions simultaneously (i.e., the mod 36 condition).

### 3.2 Computational Verification of the Mod 36 Condition

For all 333 integers n ≡ 1 (mod 12), n ≢ 0 (mod 5) in 13 ≤ n ≤ 5000:

| Min A | Count | Percentage |
|-------|-------|-----------|
| 3 | 258 | 77.5% |
| 7 | 56 | 16.8% |
| 11 | 16 | 4.8% |
| 15 | 3 | 0.9% |

**Key finding:** A ≤ 15 suffices for the mod 36 condition in 100% of cases up to n = 5000. No case required A > 15.

### 3.3 The Path to a Proof

If we could prove that:

> **For every n ≡ 1 (mod 12) with n ≢ 0 (mod 5), there exists A ∈ {3, 7, 11, 15} such that the mod 36 condition is satisfiable,**

then by the Hasse principle for conics, a global rational solution exists for each such (n, A). The remaining step would be to show that the rational solution yields positive integers (x, y, z) — which requires checking the positivity conditions.

Since there are only finitely many residue classes of n modulo 36 (specifically, n mod 36 ∈ {1, 13, 25} for n ≡ 1 mod 12), and for each residue class we need to check finitely many A values (A ∈ {3, 7, 11, 15}), the proof reduces to a **finite case analysis** of residue classes.

### 3.4 Why This Avoids Mordell's Obstruction

Mordell's theorem says no polynomial identity can cover n ≡ 1 (mod m) because 1 is a quadratic residue. But our approach doesn't use polynomial identities — it uses the existence of divisors satisfying congruence conditions. The divisor existence question is a question about the **multiplicative structure** of B = n(n+A)/2, not about polynomial expressions in n.

For each fixed A and each residue class of n mod 36, the condition becomes a statement about which residue classes mod 36 have divisors of B² with the right congruence. This is a finite check — and our computation shows it always succeeds with A ≤ 15.

---

## 4. What Remains to Prove

### Step 1: Prove the mod 36 condition is always satisfiable with A ≤ 15

This requires showing, for each of the three residue classes n mod 36 ∈ {1, 13, 25}, that at least one of A ∈ {3, 7, 11, 15} yields a divisor d of B² = (n(n+A)/2)² satisfying d + 2B + B²/d ≡ 0 (mod 36).

Since B mod 36 depends only on n mod 36 and A, this is a **finite computation** over 3 × 4 = 12 cases.

### Step 2: Show that mod 36 satisfiability implies actual integer solutions

The mod 36 condition guarantees local solvability at p = 2 and p = 3. Combined with automatic solvability at all other primes, the Hasse principle gives a rational solution. We need to show this rational solution can be converted to an integer solution with positive x, y, z.

This is the step where the **integral** Hasse principle comes in — and where Bright-Loughran's result (no Brauer-Manin obstruction) is relevant. The absence of a Brauer-Manin obstruction suggests that integral points should exist when local conditions are satisfied, though this is not automatically guaranteed.

### Step 3: Verify the finite case analysis rigorously

The 12 cases (3 residue classes × 4 A values) can be checked by direct computation. For each case, we need to exhibit a specific divisor d (as a function of B mod 36) that satisfies the congruence.

---

## 5. Comparison with Previous Approaches

| Approach | Type | Covers n ≡ 1 (mod 4)? | Mechanism |
|----------|------|----------------------|-----------|
| Mordell (1967) | Polynomial identities | No (1 is QR) | Closed-form formulas |
| Vaughan (1970) | Density | Density 1 | Analytic number theory |
| Elsholtz-Tao (2013) | Counting | Average bound | Bombieri-Vinogradov, sieve methods |
| Mballa (2026) | Symmetric solutions | Density 1 | Divisor b ≡ 3 (mod 4) |
| Bright-Loughran (2020) | Obstruction theory | N/A | Brauer-Manin (shows no obstruction) |
| **Our approach** | **Pell-like + Hasse** | **Potentially all** | **Local conditions mod 36 + Hasse principle** |

Our approach is qualitatively different from all previous ones because it:
1. Uses the Hasse principle for conics (a local-to-global principle)
2. Reduces to a finite case analysis (mod 36)
3. Is not blocked by Mordell's theorem (uses Pell equations, not polynomial identities)
4. Is consistent with Bright-Loughran (no Brauer-Manin obstruction)

---

## 6. Next Steps

1. **Complete the finite case analysis** — check all 12 cases (3 residue classes × 4 A values) and exhibit explicit divisors satisfying mod 36.
2. **Verify the integral Hasse principle** — confirm that local solvability implies integral (not just rational) solutions.
3. **Extend computation** — verify A ≤ 15 for n up to 10⁶ or higher.
4. **Write formal proof** — if the finite case analysis succeeds, write a rigorous proof.

---

*Tools: Python 3.13, SymPy 1.14.0, PARI/GP. References: Mordell (1967), Vaughan (1970), Elsholtz-Tao (2013), Bright-Loughran (2020), Mballa (2026).*