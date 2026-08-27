#!/usr/bin/env python3
"""
Compute explicit constant C for the Erdős-Straus covering set.

The density-0 sieve bound (Theorem 14) says:
  P(bad) ~ (log X)^{-3/8} → 0

To get an explicit C, we need to find N₀ such that for all n > N₀,
at least one QNR prime q ≤ X = n^{1/(4√e)+ε} divides m₃ or m₇/2.

The sieve gives: P(bad) ≈ exp(-3/4 · H) where H = Σ_{q QNR ≤ X} 1/q

For this to be < 1 (i.e., bad set is empty), we need:
  exp(-3/4 · H) < 1, which is always true if H > 0.

But we need it to be < 1/π(N) (less than one prime in the range).

Actually, the right question is: for which N is the bad set provably empty?

The sieve bound: #bad ≤ N ≤ N · (log X_N)^{-3/8} / log N

For this to be < 1: N · (log X_N)^{-3/8} / log N < 1
→ N / log N < (log X_N)^{3/8}
→ (log X_N)^{3/8} > N / log N

Since X_N = N^{1/(4√e)+ε}, log X_N = (1/(4√e)+ε) log N

So: ((1/(4√e)+ε) log N)^{3/8} > N / log N
→ (log N)^{3/8} · (1/(4√e)+ε)^{3/8} > N / log N
→ (log N)^{11/8} > N · (1/(4√e)+ε)^{-3/8}

This NEVER holds! The left side grows logarithmically, the right side grows linearly.
So the sieve CANNOT prove the bad set is empty for large N.

This means the density-0 result is the BEST we can get from this sieve.
The bad set has density 0 but may be infinite.

The constant bound C = 31 is a COMPUTATIONAL result, not a proven one.
The Burgess bound gives A = O(n^0.092) for all n, which is the best PROVEN result.

However, we can compute an EXPLICIT Burgess bound: for what N does the 
Burgess bound guarantee a QNR prime ≤ X exists?

Burgess: |Σ_{n≤X} χ(n)| ≤ C_r · X^{1-1/r} · q^{(r+1)/(4r²)} · (log q)^{1/(4r)}

For the sum to be < X (meaning not all are QR, so at least one QNR exists):
C_r · X^{-1/r} · q^{(r+1)/(4r²)} · (log q)^{1/(4r)} < 1

→ X > (C_r)^r · q^{(r+1)/(4r)} · (log q)^{1/4}

With q = n (our prime), r = 2:
X > C_2² · n^{3/8} · (log n)^{1/4}

The explicit Burgess constant C_2 from Francis (2021) is approximately 1.5
(more precisely, Francis gives C_2 ≤ 1.552 for r=2).

So: X > (1.552)² · n^{3/8} · (log n)^{1/4}
   X > 2.41 · n^{3/8} · (log n)^{1/4}

And X = n^{1/(4√e)+ε} = n^{0.0919+ε}

We need: n^{0.0919+ε} > 2.41 · n^{3/8} · (log n)^{1/4}
→ n^{0.0919+ε - 0.375} > 2.41 · (log n)^{1/4}
→ n^{-0.283+ε} > 2.41 · (log n)^{1/4}

This requires ε > 0.283, giving X = n^{0.375+} which is not useful 
(the exponent exceeds 3/8 = 0.375).

So the Burgess bound with r=2 doesn't give a useful explicit bound for our application.
We need larger r.

For general r, the threshold is:
X > C_r^r · n^{(r+1)/(4r)} · (log n)^{1/4}

And X = n^{1/(4√e)+ε} = n^{0.0919+ε}

We need: 0.0919+ε ≥ (r+1)/(4r) = 1/4 + 1/(4r)
→ ε ≥ 1/4 + 1/(4r) - 0.0919 = 0.1581 + 1/(4r)

For r → ∞: ε ≥ 0.1581, giving X = n^{0.25+}

But the Burgess exponent (r+1)/(4r) → 1/4 as r → ∞, and we need X = n^{1/(4√e)+ε}
with 1/(4√e) ≈ 0.092. So we need 0.092 + ε ≥ 0.25, i.e., ε ≥ 0.158.

This means the Burgess bound with the 1/(4√e) exponent is NOT achievable
with the standard approach. The 1/(4√e) comes from optimizing r, but the
constant C_r grows with r.

The issue: the Burgess bound gives A = O(n^{1/4+ε}) (not 1/(4√e)+ε) 
when you track constants properly. The 1/(4√e) is the OPTIMAL exponent
but requires r growing with n, which makes C_r grow.

Let me recalculate properly.
"""

from math import log, sqrt, exp, pi

# Constants
EULER_GAMMA = 0.5772156649
MEISSEL_MERTENS = 0.2614972128

# Burgess bound: for r=2, C_2 from Francis (2021)
# Francis gives: for q prime, χ non-principal, r=2:
# |Σ_{n≤N} χ(n)| ≤ 1.552 · N^{1/2} · q^{3/16} · (log q)^{1/8}
BURGESS_C2 = 1.552

# For general r, the Burgess constant C_r is harder to pin down.
# Iwaniec-Kowalski (2004) give C_r implicitly.
# For our purposes, let's use the known result that the least QNR
# mod a prime p is O(p^{1/(4√e)+ε}) and compute the explicit threshold.

# The key result (Burgess 1957, Theorem 4):
# The least QNR mod p is O(p^{1/(4√e)+ε}) for any ε > 0.
# This means: for any ε > 0, there exists N(ε) such that for p > N(ε),
# the least QNR ≤ p^{1/(4√e)+ε}.

# The explicit version (Norton 1971):
# The least QNR mod p is ≤ p^{1/(4√e)} · (log p)^{...} for large enough p.

# Let's compute what we CAN say explicitly:

print("EXPLICIT CONSTANT COMPUTATION")
print("=" * 80)

# Approach 1: Burgess r=2 with explicit constant
print("\n--- Approach 1: Burgess r=2, explicit constant ---")
print(f"Burgess C_2 = {BURGESS_C2} (Francis 2021)")
print(f"Bound: |Σ χ(n)| ≤ {BURGESS_C2} · N^(1/2) · q^(3/16) · (log q)^(1/8)")
print(f"For QNR to exist: need |Σ| < N, so:")
print(f"  {BURGESS_C2} · N^(-1/2) · q^(3/16) · (log q)^(1/8) < 1")
print(f"  N > {BURGESS_C2}^2 · q^(3/8) · (log q)^(1/4)")
print(f"  N > {BURGESS_C2**2:.2f} · q^(3/8) · (log q)^(1/4)")
print(f"\n  So least QNR ≤ {BURGESS_C2**2:.2f} · n^(3/8) · (log n)^(1/4)")
print(f"  This gives A = O(n^(3/8) · (log n)^(1/4)) — weaker than n^(1/4)")

# Approach 2: Use larger r
print("\n--- Approach 2: Burgess general r ---")
for r in [2, 3, 4, 5, 10, 20, 50]:
    exponent = (r + 1) / (4 * r)
    print(f"  r={r:3d}: exponent = (r+1)/(4r) = {exponent:.4f}, "
          f"1/4 + 1/(4r) = {0.25 + 1/(4*r):.4f}")

print(f"\n  As r → ∞: exponent → 1/4 = 0.25")
print(f"  Burgess optimal: 1/(4√e) ≈ {1/(4*sqrt(exp(1))):.4f}")
print(f"  Gap: 0.25 - {1/(4*sqrt(exp(1))):.4f} = {0.25 - 1/(4*sqrt(exp(1))):.4f}")
print(f"  The 1/(4√e) comes from the optimization, not from r=2")

# The 1/(4√e) result comes from a more careful analysis:
# Burgess (1957) showed that for the LEAST QNR specifically,
# the bound is O(p^{1/(4√e)+ε}) by using the fact that if ALL
# numbers up to X are QR, then the character sum Σ_{n≤X} (n/p) = X,
# which contradicts Burgess when X > p^{1/(4√e)+ε}.

# The argument: if all integers 1..X are QR mod p, then
# Σ_{n=1}^{X} (n/p) = X (since each (n/p) = 1)
# But Burgess: |Σ_{n=1}^{X} (n/p)| ≤ C_r · X^{1-1/r} · p^{(r+1)/(4r²)}
# So: X ≤ C_r · X^{1-1/r} · p^{(r+1)/(4r²)}
# → X^{1/r} ≤ C_r · p^{(r+1)/(4r²)}
# → X ≤ C_r^r · p^{(r+1)/(4r)}

# Optimizing: minimize (r+1)/(4r) = 1/4 + 1/(4r) over r
# But C_r grows with r. The optimal balance gives 1/(4√e).

# The 1/(4√e) comes from the SPECIFIC growth rate of C_r.
# Burgess (1957) shows C_r = O(r^{1/2r}) (up to constants),
# so the total bound is:
# X ≤ C · r^{1/2} · p^{1/4 + 1/(4r)}
# Minimizing over r: d/dr [1/2 · log r + 1/(4r) · log p] = 0
# → 1/(2r) - 1/(4r²) · log p = 0
# → r = log p / 2
# → exponent = 1/4 + 1/(4 · log(p)/2) = 1/4 + 1/(2 log p)
# As p → ∞: exponent → 1/4

# But the CONSTANT grows as r^{1/2} = (log p / 2)^{1/2}
# So: X ≤ C · (log p)^{1/2} · p^{1/4 + 1/(2 log p)}
# = C · (log p)^{1/2} · p^{1/4} · p^{1/(2 log p)}
# = C · (log p)^{1/2} · p^{1/4} · e^{1/2}  (since p^{1/log p} = e)
# = C · √e · (log p)^{1/2} · p^{1/4}

# Hmm, this gives X = O(p^{1/4} · (log p)^{1/2}), not O(p^{1/(4√e)}).

# The 1/(4√e) comes from a DIFFERENT optimization.
# Let me look at this more carefully.

# Actually, the 1/(4√e) result (Burgess 1957, Theorem 4) uses a 
# DIFFERENT approach than just applying the character sum bound.
# It uses the fact that if n is the least QNR, then ALL primes ≤ n 
# are QR (otherwise a smaller QNR exists). This means the PRODUCT
# of all primes ≤ n is QR, and by properties of the Legendre symbol,
# this constrains n.

# The actual result: Burgess proves that for any ε > 0 and 
# sufficiently large prime p, the least QNR mod p is at most 
# p^{1/(4√e) + ε}.

# The proof uses the Pólya-Vinogradov completion combined with
# the Burgess character sum bound, and the optimization over r
# gives 1/(4√e) from the interplay between:
# - The character sum bound: |Σ| ≤ C_r · N^{1-1/r} · p^{(r+1)/(4r²)}
# - The constraint that if N is the least QNR, Σ_{n≤N} (n/p) = N - 1 
#   (since all n < N are QR, so (n/p) = 1, and N itself is QNR with (N/p) = -1)
# - So N - 1 ≤ C_r · N^{1-1/r} · p^{(r+1)/(4r²)}
# - N^{1/r} ≤ C_r · p^{(r+1)/(4r²)} (approximately)
# - N ≤ C_r^r · p^{(r+1)/(4r)}

# The 1/(4√e) arises from the optimal choice of r as a function of p.
# With C_r ~ r^{1/(2r)} (from Burgess), the bound becomes:
# N ≤ C · r^{1/2} · p^{(r+1)/(4r)}
# Taking log: log N ≤ log C + (1/2) log r + ((r+1)/(4r)) log p
# Minimizing over r: d/dr [(1/2) log r + (r+1)/(4r) · log p] = 0
# → 1/(2r) + [-1/(4r²)] · log p = 0
# → r = log p / 2

# At r = log(p)/2:
# exponent = (r+1)/(4r) = 1/4 + 1/(4r) = 1/4 + 1/(2 log p)
# C_r^r = (r^{1/(2r)})^r = r^{1/2} = (log p / 2)^{1/2}

# So N ≤ C · (log p)^{1/2} · p^{1/4 + 1/(2 log p)}
# = C · (log p)^{1/2} · p^{1/4} · p^{1/(2 log p)}
# = C · (log p)^{1/2} · p^{1/4} · e^{1/2}  (since p^{1/log p} = e)
# = C · √e · (log p)^{1/2} · p^{1/4}

# This gives N = O(p^{1/4} · (log p)^{1/2}), not O(p^{1/(4√e)}).

# The 1/(4√e) comes from a REFINED analysis using the completion 
# technique more carefully. See Burgess (1957) for the full argument.

# For our purposes, the practical bound is:
# Least QNR ≤ C · p^{1/4 + ε} for any ε > 0 and large enough p
# where C depends on ε.

# Let's compute what the EXPLICIT bound gives for practical n:

print("\n--- Practical explicit bounds ---")
print(f"\nUsing Burgess r=2 with C_2 = {BURGESS_C2}:")
print(f"  Least QNR ≤ {BURGESS_C2**2:.2f} · n^(3/8) · (log n)^(1/4)")

for n in [1000, 10000, 100000, 1000000, 10000000, 100000000]:
    bound = BURGESS_C2**2 * n**(3/8) * (log(n))**(1/4)
    actual_X = n**(1/(4*sqrt(exp(1))))
    print(f"  n={n:>10}: r=2 bound = {bound:.0f}, n^(1/(4√e)) = {actual_X:.1f}")

print(f"\nUsing r=3 (C_3 ≈ 2.0, approximate):")
C3 = 2.0
for n in [1000, 10000, 100000, 1000000, 10000000]:
    bound = C3**3 * n**(4/12) * (log(n))**(1/4)
    print(f"  n={n:>10}: r=3 bound = {bound:.0f}")

print(f"\n--- What can we actually prove? ---")
print(f"""
The Burgess bound with r=2 and explicit constant C_2 = {BURGESS_C2} (Francis 2021) gives:

  Least QNR mod n ≤ {BURGESS_C2**2:.2f} · n^(3/8) · (log n)^(1/4)

This means A = O(n^(3/8) · (log n)^(1/4)), which is WEAKER than the 
asymptotic O(n^(1/(4√e)+ε)) but is EXPLICIT.

For the Erdős-Straus conjecture, this gives:
  A ≤ {BURGESS_C2**2:.2f} · n^(3/8) · (log n)^(1/4)
  
This is an unconditional, explicit bound.

The 1/(4√e) ≈ 0.092 exponent requires larger r with growing constants.
The asymptotic result (for any ε > 0, exists N(ε)) is proven by Burgess
but the explicit N(ε) is not easily computable from the literature.

SUMMARY:
- Explicit unconditional: A ≤ {BURGESS_C2**2:.2f} · n^(3/8) · (log n)^(1/4) (r=2)
- Asymptotic: A = O(n^(1/(4√e)+ε)) for any ε > 0 (Burgess 1957)
- Computational: A ≤ 31 for all primes ≤ 10M (Theorem 13)
- Density-0: bad set has density 0 (Theorem 14, sieve)
- GRH: A = O((log n)²) (Ankeny 1952)
""")

# Compute the sieve threshold more carefully
print("--- Sieve threshold computation ---")
print(f"\nThe sieve gives P(bad) ~ (log X)^(-3/8)")
print(f"For P(bad) < 1/N (less than one bad prime up to N):")
print(f"  (log X)^(-3/8) < 1/N")
print(f"  N < (log X)^(3/8)")
print(f"  But X = n^(1/(4√e)+ε), so log X ~ 0.092 · log N")
print(f"  N < (0.092 · log N)^(3/8)")
print(f"  This requires N to be SMALL — the sieve can't prove emptiness for large N")
print(f"\n  The density-0 result IS the best we can get from this sieve.")
print(f"  The constant bound C = 31 remains a computational result.")
print(f"  The Burgess bound A = O(n^0.375 · (log n)^0.25) is the best EXPLICIT bound.")