# Layer 4: Draft Proof Outlines per Route Family


### Order-2 Route (PROVEN)
**Claim:** If some prime p | nx has ord_A(p) = 2 (i.e., p ≡ -1 mod A), then h/2 ∈ Σ_A(N) with δ_p = 1.

**Proof:** p ≡ -1 mod A means dlog(p) = h/2. Taking δ_p = 1 (which satisfies -e_p ≤ 1 ≤ e_p since e_p ≥ 1), we get s_p · 1 = h/2 mod h. ∎

**Status:** Proven in general (Theorem 3.3, Case 2a). Covers 445 + 3687 = 4132 cases.


### Direct n-QNR Route (PROVEN)
**Claim:** If (A/n) = -1 (n is QNR mod A), then A works via the direct route.

**Proof:** Since (A/n) = -1 and n ≡ 1 mod 4, by QR reciprocity (n/A) = (A/n) = -1. So n is QNR mod A, meaning n has even order mod A, contributing a QNR generator to H(A). This gives h even with n as a QNR factor, and the order-2 or Kneser argument applies. ∎

**Status:** Proven (Theorem 5 + Jacobi identity). This is Layer 3 of the rescue chain.


### M-Route (COMPUTATIONAL — needs proof)
**Claim:** If (A/n) = 1 (direct route fails) but some prime p | m_A = (n+A)/4 has (p/A) = -1, then A works.

**Proof:** By Theorem 5, (p/A) = (n/p) when p | m_A. So p is QNR mod A iff n is QNR mod p. The QNR factor p enters nx = n·m_A, giving h even and the order-2 or centered route applies.

**Status:** Computationally verified (100% for n ≤ 100K). General proof open.
**Key obstacle:** The Jacobi identity (n/m_A) = (m_A/A) = 1 when (A/n) = 1 means the Jacobi symbol cannot distinguish 0 QNR factors from 2+ QNR factors. Proof must work at the factorization level.


### Two-Term Centered Route (PARTIALLY PROVEN)
**Claim:** There exist primes p_i, p_j | N and signed exponents δ_i ∈ [-e_i, e_i], δ_j ∈ [-e_j, e_j] with s_i·δ_i + s_j·δ_j ≡ h/2 mod h.

**Status:** Proven when Kneser's theorem applies (trivial stabilizer, Σ(2e_i+1) ≥ m+k-1). The remaining two-term cases need case-by-case verification.

**Proof strategy:** Classify by (s_i, s_j) pairs and show that the AP {s_i·δ_i : -e_i ≤ δ_i ≤ e_i} intersects the shifted AP {h/2 - s_j·δ_j : -e_j ≤ δ_j ≤ e_j}. This is a problem about AP intersection in Z/hZ.


### Full Coverage Route (PROVEN under Kneser)
**Claim:** Σ_A(N) = Z/hZ, so h/2 is trivially reachable.

**Proof:** By Kneser's theorem, if the stabilizer is trivial and Σ|A_i| = Σ(2e_i+1) ≥ h + k - 1, then |Σ| ≥ h, so Σ = Z/hZ. ∎

**Status:** Proven for trivial-stabilizer cases with sufficient exponent sum.

