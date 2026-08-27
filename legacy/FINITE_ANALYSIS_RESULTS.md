# 12-Case Finite Analysis: Results and Limitations

**Date:** July 17, 2026
**Authors:** Brodie Foxworth, Skip Potter

---

## 1. The Plan

The goal was to prove A-boundedness by showing that for each n ≡ 1 (mod 12), n ≢ 0 (mod 5), there exists a bounded A ≡ 3 (mod 4) satisfying the local conditions mod 36, and then invoking the Hasse principle for conics to get global solutions.

The analysis reduces to 3 residue classes (n mod 36 ∈ {1, 13, 25}) × finitely many A values.

---

## 2. What We Proved

### Theorem: The mod 36 condition is always satisfiable

For every n ≡ 1 (mod 12) with n ≢ 0 (mod 5), there exists A ≡ 3 (mod 4) with A ≤ 35 such that the mod 36 condition (d + 2B + B²/d ≡ 0 mod 36 for some divisor d of B²) is satisfiable.

**Proof:** For each residue class, choose A = 36 − (n mod 36):

| n mod 36 | A | A mod 4 | n + A mod 36 |
|-----------|------|---------|--------------|
| 1 | 35 | 3 ✓ | 0 |
| 13 | 23 | 3 ✓ | 0 |
| 25 | 11 | 3 ✓ | 0 |

In each case, n + A ≡ 0 (mod 36), so (n+A)/2 ≡ 0 (mod 18). Therefore B = n(n+A)/2 ≡ 0 (mod 18), giving 9 | B. Taking d = B: d + 2B + B²/d = 4B, and since 18 | B, we have 72 | 4B, hence 36 | 4B. **QED.**

---

## 3. What We Could NOT Prove

### The mod 36 condition is NECESSARY but NOT SUFFICIENT

The mod 36 condition guarantees local solvability of the Pell-like equation k² − 36m² = B² at p = 2 and p = 3. By the Hasse principle for conics, this implies a **rational** solution (k, m) exists.

However, we need more than a rational solution — we need:
1. **Integer** solutions (k, m) with specific congruence conditions (k + B ≡ 0 mod 18)
2. **Positive** integers y = tA + m and z = tA − m > 0

The gap between "rational solution exists" and "positive integer solution with z > 0" is the **integral Hasse principle** gap. The mod 36 condition ensures the congruence part, but does not guarantee that the resulting t and m give z > 0.

### Empirical Evidence: A is NOT Bounded by 15

Using the fast search algorithm (checking F = t²A² − 2nxt directly), we found:

| n | n mod 36 | Min A (actual solution) | Min A (mod 36 only) |
|------|----------|------------------------|--------------------|
| 169 | 25 | 7 | 11 (mod 36 ok, but no valid solution) |
| 241 | 25 | 11 | 11 (mod 36 ok, but A=11 gives asymmetric solution) |
| 601 | 25 | **87** | 11 (mod 36 ok, but no valid solution until A=87) |
| 673 | 25 | **47** | 11 (mod 36 ok, but no valid solution until A=47) |
| 193 | 13 | 15 | 23 (mod 36 ok, but no valid solution until A=15) |
| 433 | 1 | 15 | 35 (mod 36 ok, but no valid solution until A=15) |

**Key finding:** The mod 36 condition is satisfied with small A (≤ 35), but actual Erdős-Straus solutions sometimes require much larger A (up to 87 for n = 601).

---

## 4. Why the Proof Attempt Failed

### The Integral Hasse Principle Gap

The Hasse principle for conics guarantees **rational** points when local conditions are met. But the Erdős-Straus conjecture requires **positive integer** points. The conversion from rational to integer points requires:

1. **Integrality:** The rational solution (k, m) must satisfy k + B ≡ 0 (mod 18), making t = (k+B)/18 an integer. This is a congruence condition that IS captured by mod 36.

2. **Positivity:** The integer solution must give z = tA − m > 0. This is an **inequality** condition that is NOT captured by any local/modular condition.

The positivity condition is a **global** constraint — it depends on the actual size of t and m, not just their residues. No finite modular analysis can capture it.

### Connection to Bright-Loughran

Bright-Loughran (2020) showed that the Brauer-Manin obstruction does not explain the failure of the integral Hasse principle for Erdős-Straus surfaces. Our finding is consistent: the failure is not due to an algebraic obstruction (Brauer group) but due to the **positivity constraint** — a real-analytic condition that no algebraic tool can directly address.

---

## 5. Honest Assessment

### What we accomplished:
1. **Complete computational verification** for all 6,666 cases up to n = 100,000 — 100% success rate.
2. **A-parameter framework** — clean characterization of solutions via A = 4x − n.
3. **Proved the mod 36 condition** is always satisfiable with A ≤ 35 — this is a genuine theorem, just not strong enough.
4. **Identified the exact gap** — the integral Hasse principle gap between rational solvability (guaranteed) and positive integer solvability (not guaranteed by local conditions alone).

### What we could not accomplish:
1. **Prove A is bounded** — the mod 36 condition doesn't bound A tightly enough. A can be as large as 87 even for n ≈ 600.
2. **Close the integral Hasse principle gap** — this would require showing that when local conditions are satisfied, a positive integer solution always exists. This is essentially equivalent to the Erdős-Straus conjecture itself.

### The fundamental difficulty:
The Erdős-Straus conjecture, in our framework, reduces to: "for each n, some A gives a Pell-like equation with a positive integer solution." The local conditions (mod 36) are always satisfiable, but the **global** positivity constraint is the real obstruction. This is exactly the kind of problem that the Hasse principle (even working perfectly for conics) cannot resolve — it's an integral problem, not a rational one.

---

## 6. What This Means for the Conjecture

Our work suggests that the Erdős-Straus conjecture, for the residue class n ≡ 1 (mod 12), n ≢ 0 (mod 5), is **likely true** (0 counterexamples in 6,666 cases up to 100,000), but the proof requires tools beyond:

- Modular identities (blocked by Mordell's theorem)
- Local conditions / Hasse principle (satisfied but insufficient)
- Brauer-Manin obstruction (shown not to apply by Bright-Loughran)

The missing ingredient is likely an **analytic** argument — showing that the density or distribution of solutions guarantees at least one with positive z. This connects to the Elsholtz-Tao counting result, but their polylogarithmic bound is too weak for a direct density argument.

---

*This is an honest report of a partial proof attempt. The mod 36 theorem is a real result; the failure to close the integral Hasse gap is an honest limitation of the approach.*