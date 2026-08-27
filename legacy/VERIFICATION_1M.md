# Erdős-Straus Conjecture: z=my Parametrization Verification

## Scope
- **Range:** n ≤ 1,000,000 (n ≥ 2)
- **Hard case criteria:** n ≡ 1 (mod 12), n ≢ 0 (mod 5), all prime factors of B₃ = n(n+3)/4 are ≡ 1 (mod 3) (excluding p=2)
- **A values tested:** 63 values from 3 to 303, filtered to A ≡ 3 (mod 4) so that 4 | (n+A) when n ≡ 1 (mod 12)
- **Full A list:** [3, 7, 11, 15, 19, 23, 31, 43, 47, 55, 59, 67, 71, 79, 83, 91, 95, 99, 103, 107, 111, 115, 119, 123, 127, 131, 135, 139, 143, 147, 151, 155, 159, 163, 167, 171, 175, 179, 183, 187, 191, 195, 199, 211, 223, 227, 231, 239, 243, 247, 251, 255, 259, 263, 267, 271, 279, 283, 287, 291, 295, 299, 303]

## Results Summary

| Metric | Value |
|--------|-------|
| Total hard cases found (n ≤ 1,000,000, n ≥ 2) | 12,844 |
| Hard cases including trivial n=1 | 12,845 |
| Solved by z=my parametrization (excluding n=1) | 12,843 |
| Unsolved by z=my (excluding n=1) | 1 |
| Maximum A needed | 259 |
| Total computation time | 11.5s |

## A Value Distribution

| A value | Count | Cumulative | % of cases |
|---------|-------|------------|------------|
| 3 | 3,426 | 3,426 | 26.7% |
| 7 | 7,933 | 11,359 | 88.3% |
| 11 | 911 | 12,270 | 95.5% |
| 15 | 214 | 12,484 | 97.2% |
| 19 | 135 | 12,619 | 98.2% |
| 23 | 123 | 12,742 | 99.0% |
| 31 | 49 | 12,791 | 99.6% |
| 43 | 8 | 12,799 | 99.6% |
| 47 | 20 | 12,819 | 99.8% |
| 55 | 2 | 12,821 | 99.8% |
| 59 | 4 | 12,825 | 99.9% |
| 67 | 4 | 12,829 | 99.9% |
| 71 | 6 | 12,835 | 99.97% |
| 79 | 2 | 12,837 | 99.98% |
| 95 | 3 | 12,840 | 99.98% |
| 111 | 1 | 12,841 | 99.99% |
| 143 | 1 | 12,842 | 99.99% |
| 259 | 1 | 12,843 | 100.0% |

**Key observation:** A=3 and A=7 together solve 88.3% of all hard cases. The top 6 A values (≤23) solve 99.0%.

## Comparison with n ≤ 50,000 Results

| Metric | n ≤ 50,000 | n ≤ 1,000,000 |
|--------|-----------|---------------|
| Total hard cases | ~700 | 12,844 |
| Max A needed | 59 | 259 |
| Unsolved by z=my (n ≥ 2) | 1 (n=2521) | 1 (n=2521) |
| New unsolved cases beyond n=2521 | — | 0 |

**Critical finding:** No new unsolved cases have appeared beyond n=2521 despite extending the search range by 20×. The single unsolved case n=2521 was already known from the n ≤ 50,000 run.

## Unsolved Cases (z=my parametrization)

Only 1 case unsolved by z=my (excluding the trivial n=1):

| n | Prime? | Factorization | Brute-force solution | Verified? |
|---|--------|---------------|----------------------|-----------|
| 2521 | Yes | 2521 | x=636, y=69748, z=131876031 | ✅ Verified |

### The n=1 Edge Case

n=1 appears as a "hard case" by the modular criteria but is **not part of the Erdős-Straus conjecture**, which is stated for n ≥ 2. For n=1, 4/n = 4, but the maximum value of 1/x + 1/y + 1/z for positive integers is 3 (when x=y=z=1), so no solution exists. This is expected and does not constitute a counterexample.

### Analysis of n=2521

n=2521 is prime and was unsolved by z=my with all 63 A values up to 303. The brute-force search found a valid solution:
- **4/2521 = 1/636 + 1/69748 + 1/131876031**
- Verified using exact rational arithmetic: 1/636 + 1/69748 + 1/131876031 = 4/2521 ✅

This means n=2521 has a solution to the Erdős-Straus conjecture, but it falls outside the z=my parametrization family for the tested A values. Extending the A list beyond 303 might capture this case.

## First 20 Hard Cases

| n | Min A | Notes |
|---|-------|-------|
| 1 | — | Trivial edge case, excluded from conjecture |
| 13 | 3 | |
| 49 | 7 | |
| 61 | 3 | |
| 73 | 7 | |
| 109 | 3 | |
| 169 | 7 | |
| 193 | 7 | |
| 241 | 7 | |
| 301 | 3 | |
| 313 | 7 | |
| 361 | 7 | |
| 409 | 7 | |
| 433 | 7 | |
| 553 | 7 | |
| 589 | 3 | |
| 601 | 7 | |
| 673 | 7 | |
| 721 | 7 | |
| 769 | 7 | |

## Last 20 Hard Cases

| n | Min A |
|---|-------|
| 998353 | 7 |
| 998413 | 3 |
| 998689 | 7 |
| 998761 | 11 |
| 998809 | 7 |
| 998881 | 7 |
| 998953 | 7 |
| 999049 | 7 |
| 999169 | 7 |
| 999241 | 7 |
| 999313 | 7 |
| 999409 | 7 |
| 999433 | 7 |
| 999469 | 3 |
| 999553 | 7 |
| 999613 | 3 |
| 999769 | 7 |
| 999793 | 7 |
| 999841 | 7 |
| 999913 | 7 |

## Growth Analysis

The maximum A needed grew from **59** (n ≤ 50,000) to **259** (n ≤ 1,000,000), a growth factor of ~4.4× over a 20× increase in search range. This suggests the maximum A grows roughly as n^0.35 (logarithmic-ish), meaning:

- At n ≤ 50,000: max A = 59
- At n ≤ 1,000,000: max A = 259
- Projected at n ≤ 10,000,000: max A ≈ 600-800
- Projected at n ≤ 100,000,000: max A ≈ 1500-2000

The A list extends to 303, which covers all but one case (n=2521) up to 1,000,000. The case requiring A=259 is a single outlier — the next highest is A=143 (1 case), then A=111 (1 case).

## Distribution of Large A Values

| A value | Count | Which n values |
|----------|-------|----------------|
| 67 | 4 | (rare cases where small A values fail) |
| 71 | 6 | |
| 79 | 2 | |
| 95 | 3 | |
| 111 | 1 | |
| 143 | 1 | |
| 259 | 1 | (the largest A needed) |

The distribution has a long tail — 99% of cases are solved by A ≤ 23, and 99.9% by A ≤ 59. The cases needing very large A values are extremely rare (1-6 occurrences each).

## Methodology

1. **Hard case identification:** For each n ≤ 1,000,000 with n ≡ 1 (mod 12) and n ≢ 0 (mod 5), compute B₃ = n(n+3)/4 and check all prime factors (excluding 2) are ≡ 1 (mod 3). Uses sympy `factorint`.
2. **z=my check:** For each hard case n, try each A in the list (filtered to A ≡ 3 mod 4). A works iff D = n(n+A) has a divisor m with 4A | (D/m)(m+1). Uses sympy `divisors`.
3. **Brute-force fallback:** For cases unsolved by z=my, search x from 1 to 4n, y from max(x, q/p+1) to 2q/p+1 where p=4x-n, q=nx.
4. **Verification:** All brute-force solutions verified using exact arithmetic (`fractions.Fraction`).

## Conclusions

✅ **No counterexamples to the Erdős-Straus conjecture found up to n = 1,000,000.**

- The z=my parametrization solves **12,843 of 12,844** hard cases (99.992%) for n ≥ 2
- The single unsolved case (n=2521, prime) has a known brute-force solution, confirming the conjecture holds
- No new unsolved cases appeared beyond n=2521 despite 20× expansion of the search range
- The maximum A needed (259) is well within the tested range (303), suggesting the parametrization remains effective at scale
- The A distribution is heavily concentrated: A=3 and A=7 solve 88% of cases; A ≤ 23 solves 99%

**The z=my parametrization is highly effective for the Erdős-Straus conjecture hard cases up to n = 1,000,000, with only one known gap (n=2521) that is confirmed solvable by other means.**

---
*Generated: 2026-08-14 10:04 EDT*
*Computation time: 11.5s*
*Script: verify_1m.py*