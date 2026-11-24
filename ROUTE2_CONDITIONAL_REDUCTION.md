# A Lean-Verified Conditional Reduction of the Erdős–Straus Conjecture and a Constructive Divisor-Span Framework

**Version:** v1.10 (revised from the v1.9 external review of 2026-11-24; revision notes in `CHANGELOG.md`)  
**Date:** 2026-11-19 (v1) / 2026-11-21 (v1.1) / 2026-11-22 (v1.2) / 2026-11-23 (v1.3, v1.4) / 2026-11-24 (v1.5, v1.6, v1.7, v1.8, v1.9, v1.10)  
**Author:** Brodie Foxworth  
**Repository:** `pottertech/erdos-straus-conjecture`

> **Disclaimer.** This is not a proof of the Erdős–Straus conjecture and does not claim to be one. It proves a *reduction*: that the full conjecture follows, by an argument every step of which is both written out here and machine-verified in Lean 4 with no new axioms — the axiom dependency of the reduction's proof term is audited explicitly in Appendix A — from the single hypothesis **(H24)** — that every prime congruent to 1 modulo 24 has an Erdős–Straus representation. The hypothesis itself remains open; Section 6 states precisely what is and is not known about it.

> **Positioning (second external review).** The reduction to the prime class `≡ 1 (mod 24)` formalizes content the classical literature already contains: Mordell's identity table and its successors narrow the residual primes further, to six residue classes modulo 840 — `1, 121, 169, 289, 361, 529 (mod 840)` (Mordell's *Diophantine Equations*; Salez's seven-equation sieve; cf. Ionascu–Wilson's extension) — every one of them `≡ 1 (mod 24)`. This paper therefore does **not** claim the mod-24 narrowing as new mathematics. Its contributions are (i) the **machine-checked formalization** of the reduction and of the constructive criterion (Appendix A), (ii) the **constructive divisor-span framework**: the layer analyses, the verified certificate layer, and the exact-criterion sweeps of §6.5 (`FIRST_A_STRUCTURE.md`, `sweep_exact/`), and (iii) the **finite-search equivalence** of Theorem 5.2, which turns (H24) into a finite per-prime search statement with the span condition as the test.

---

## Abstract

We prove a conditional reduction for the Erdős–Straus conjecture. The reduction is elementary and complete: given the hypothesis (H24) that every prime `p ≡ 1 (mod 24)` admits positive integers `x, y, z` with `4/p = 1/x + 1/y + 1/z`, the conjecture holds for all `n ≥ 2`. The formal reduction has two components: (i) a scaling lemma showing that a solution for a prime factor lifts to all of its multiples — once (H24) and Theorem 4.2 supply representations for the primes, every composite inherits one — which removes the composite portion of the resistant class from consideration entirely; and (ii) a mod-chain lemma showing that the certified 7-case partition of the conjecture, combined with the known prime case `n ≡ 5 (mod 8)`, leaves exactly the primes `≡ 1 (mod 24)` uncovered. Both components are formalized in Lean 4 with no new axioms — Appendix A audits the actual axiom dependency — and zero `sorry` declarations (`ErdosStrausConjecture.Reduction`); the companion constructive criterion (`CenteredCriterion`), which converts any span witness of the u-method into an explicit solution, is likewise fully formalized. We then analyze the remaining hypothesis (H24): its span-criterion translation, the constraints a covering argument must satisfy (the Mordell non-residue obstruction; the span-reachability obstacle documented for the layers `u = 31` and `u = 35`), the effectiveness available from classical least-quadratic-non-residue bounds (Burgess, Norton) and the GRH bound (Ankeny), and the empirical record — a verified certificate layer of 166,011 primes `≡ 1 (mod 12)` up to 10,000,000 (82,887 of them `≡ 1 (mod 24)`, the class (H24) concerns) in which the largest first-working parameter is `A = 107`. Beyond the certificate layer, this release reports an exact billion-range sweep (3,194,231 hard cases, zero failures, first-working maximum `u = 83`), the mod-840-filtered 22,222-prime research cohort, and an independent Rust-kernel re-verification of the exported proof closure under strict axiom enforcement (15 principal theorems, zero typechecker errors).

---

## 1. Introduction

The Erdős–Straus conjecture states that for every integer `n ≥ 2`, there exist positive integers `x, y, z` such that

$$\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}.$$

Despite work since 1950 (Erdős, Mordell, Vaughan, Elsholtz–Tao, Salez, Bright–Loughran, Mballa), the conjecture remains open. The classical obstruction to identity-based attacks is the Mordell (1969) principle: for a **primitive** residue class `n ≡ r (mod m)` with `gcd(r, m) = 1` (the qualification Elsholtz–Tao state explicitly), a polynomial identity providing solutions for all members of the class can exist only when `r` is a quadratic non-residue modulo `m` — for non-primitive classes the principle does not apply (e.g. `n ≡ 4 (mod 12)`: 4 is a quadratic residue mod 12 (`2² ≡ 4`), yet every member satisfies `4/n = 1/(n/2) + 1/n + 1/n`). Since 1 is a quadratic residue modulo every `m`, the class `n ≡ 1 (mod 12)` — which contains the resistant cases — is closed to finite systems of uniform polynomial identities (the Mordell obstruction, as stated precisely in §6.4); it remains open whether *other* congruence-based approaches (e.g. the covering-system reformulation of Bloom–Elsholtz) can succeed there.

The present paper sharpens *where* the conjecture's remaining content lives. Its starting point is the certified toolkit of the companion manuscript v13: the six modular identities covering every `n ≢ 1 (mod 12)` (together with `n ≡ 1 (mod 12)` with `5 ∣ n`), Theorem 2 covering the prime case `n ≡ 5 (mod 8)`, and a machine-verified case partition. We add:

- **The scaling lemma** (§3): a solution for `n` lifts to a solution for `n·k` for every `k ≥ 1`; consequently every composite inherits a solution from a prime factor provided that factor has one, and only prime residue classes can be intrinsically hard.
- **The mod-chain lemma** (§4): `n ≡ 1 (mod 12)` and `n ≢ 1 (mod 24)` force `n ≡ 5 (mod 8)` — so for primes, the certified Theorem 2 case (§2.3) meets the resistant class in exactly one residue, leaving `n ≡ 1 (mod 24)` as the sole uncovered prime class.
- **The conditional reduction** (§5): hence the full conjecture follows from (H24), the statement that every prime `≡ 1 (mod 24)` has a representation.

Everything in §2–§5 is machine-verified: the partition, the identities, the constructive criterion, the scaling lemma, the mod-chain lemma, the reduction, and **both directions of Theorem 5.2 — composed into a single machine-checked biconditional** (the constructive reverse `u_method_witness` in `CenteredCriterion.lean`; the witness-extraction `witness_extraction` and the composed equivalence `finite_search_equivalence` in `FiniteSearch.lean`, the latter added at v1.4/v1.5 per external review V14-03 — the ten-module CI build set: `DivisorResidue`, `ClassicalIdentities`, `OmegaCases`, `CenteredEquivalence`, `MainTheorem`, `Theorem4`, `NewTheorems`, `CenteredCriterion`, `Reduction`, `FiniteSearch`; 0 `sorry` declarations in the new results; 2 documented axioms in the context modules). Section 6 presents mathematical analysis and computational results: it states what (H24) means, what the classical analytic results do and do not supply toward it, and what the verified computational record shows.

---

## 2. Notation and the certified toolkit

Throughout, `IsErdosStraus n` abbreviates: there exist positive integers `x, y, z` with `4·x·y·z = n·(x·y + x·z + y·z)`, i.e. `4/n = 1/x + 1/y + 1/z`.

The reduction assembles five components, all previously formalized and CI-enforced:

**2.1 The seven-case partition.** Every `n ≥ 2` falls into exactly one of seven residue cases: `n ≡ 0 (mod 3)`; `n ≡ 2 (mod 3)`; `n ≡ 4, 7, 10 (mod 12)`; `n ≡ 1 (mod 12)` with `5 ∣ n`; and `n ≡ 1 (mod 12)` with `5 ∤ n`. The first five are solved by the identities of §2.2, the sixth explicitly, and the seventh splits further. Machine-checked as `residue_classification` (`MainTheorem.lean`).

**2.2 The modular identities.** Each coverable case has an explicit two- or three-term representation; for example, for `n = 3k + 2`,

$$\frac{4}{n} = \frac{1}{n} + \frac{1}{k+1} + \frac{1}{n(k+1)},$$

verified by clearing denominators. All six cases (`mod_3_zero`, `mod_3_two`, `mod_12_four`, `mod_12_seven`, `mod_12_ten`, `mod_12_one_mod_5_zero`) are proven in Lean in `Identities.lean` — the module the case-partition theorems actually import.

**2.3 Theorem 2, with its explicit identity.** Every prime `n ≡ 5 (mod 8)` — indeed
every integer `n ≡ 5 (mod 8)`, primality unnecessary — has `A = 3`:
$$\frac{4}{n} = \frac{1}{\frac{n+3}{4}} + \frac{1}{\frac{n(n+3)}{8}} + \frac{1}{\frac{n(n+3)}{4}}.$$
Clearing denominators — with `A = (n+3)/4`, `B = n(n+3)/8`, `C = n(n+3)/4`: `4·A·B·C − n·(B·C + A·C + A·B) = n²(n+3)³/32 − n·n(n+3)³/32 = 0` — verified directly by `linear_combination` in Lean (`CenteredEquivalence.lean`, `theorem2`); each denominator is a positive integer since `n ≡ 5 (mod 8)` makes `n + 3` divisible by 8.

**2.4 The residual-class lemma.** The 7-case partition refines to: everything is covered except

$$C = \{n ≥ 13 :\; n ≡ 1 \pmod{12},\; 5 \nmid n,\; \neg(n \text{ prime} \wedge n ≡ 5 \pmod 8)\}.$$

This is `erdos_straus_except_residual_open_class` (`MainTheorem.lean`), the unconditional coverage theorem of the program. Inside `C`, the elementary facts resolve the set further into the prime class `n ≡ 1 (mod 24)` and the composites `≡ 1 (mod 12)` with `5 ∤ n`.

**2.5 The constructive criterion.** For odd `u ≡ 3 (mod 4)` with `u = 4x − n > 0` and `x = (n+u)/4` a positive integer: whenever there is a positive divisor `P ∣ (n·x)²` with `P ≡ −n·x (mod u)` and `gcd(u, n·x) = 1`, the construction

$$x = \frac{n+u}{4}, \quad y = \frac{P + n x}{u}, \quad z = \frac{Q + n x}{u}, \quad Q = \frac{(n x)^2}{P}$$

is positive-integer-valued and satisfies `4·x·y·z = n·(x·y + x·z + y·z)` identically. This is `u_method_core` and its constructive wrapper in `CenteredCriterion.lean` (0 `sorry`). In span language: with `M = n·x` and `gcd(M, u) = 1` as required above, the divisor condition on `P` is equivalent to `P·M^{-1} ≡ −1 (mod u)`; a span witness with exponent coefficients in `[−e_j, e_j]` relative to the prime factorization of `M` becomes the divisor `P ∣ M²` (exponents in `[0, 2e_j]`) after multiplication by `M`, and conversely. §6.1 states this precisely.

---

## 3. The scaling lemma

**Lemma 3.1 (scaling).** If `4/n = 1/x + 1/y + 1/z` with `x, y, z > 0` and `k ≥ 1`, then

$$\frac{4}{nk} = \frac{1}{kx} + \frac{1}{ky} + \frac{1}{kz}.$$

*Proof.* The starting identity is `4·x·y·z = n·(x·y + x·z + y·z)`. Multiplying through by `k³`,

$$4(kx)(ky)(kz) = k^3 \cdot 4xyz = k^3 \cdot n(xy + xz + yz) = (nk)\big((kx)(ky) + (kx)(kz) + (ky)(kz)\big),$$

which is the defining identity for `(nk, kx, ky, kz)`, with every denominator positive. ∎

**Lemma 3.2 (prime descent).** Every composite `n ≥ 2` has a prime divisor `p` with `n = p·(n/p)` and `n/p ≥ 1`.

*Proof.* Standard (every `m ≠ 1` has a prime divisor); formalized via `Nat.exists_prime_and_dvd`. ∎

**Corollary 3.3 (composites inherit; the hard core is prime).** If every prime has a representation, then every composite `n ≥ 2` has one: take a prime factor `p ∣ n` (Lemma 3.2), a representation for `p` (hypothesis), and scale by `n/p` via Lemma 3.1.

In Lean this is the composite branch of `full_conjecture_of_h24` (`Reduction.lean`), with `Reduction.scaling` proved by `ring`-normalization after rewriting through the hypothesis.

The consequence is worth stating plainly: **composite residue classes cannot be intrinsically hard.** Whatever resists the conjecture resists only on primes.

---

## 4. The mod-chain: why exactly 1 (mod 24)

**Lemma 4.1 (mod-chain).** If `n ≡ 1 (mod 12)` and `n ≢ 1 (mod 24)`, then `n ≡ 5 (mod 8)`.

*Proof.* Since `12 ∣ 24`, `n ≡ 1 (mod 12)` gives `n mod 24 ∈ {1, 13}` with `0 ≤ n mod 24 < 24`; by hypothesis it is not `1`, so `n ≡ 13 (mod 24)`. Writing `n = 24·⌊n/24⌋ + 13` and rearranging,

$$n = 5 + \left(1 + 3\left\lfloor \tfrac{n}{24}\right\rfloor\right)\cdot 8,$$

gives `n ≡ 5 (mod 8)` directly. ∎

(This lemma is `mod8_of_12` in `Reduction.lean`. The proof carries the explicit rearrangement above rather than trusting `omega` across the three moduli — the tactic does not chain them, and it may fail on goals involving unfolded primality definitions; see Appendix A for the recorded pitfall.)

**Theorem 4.2 (unconditional prime coverage).** Every prime `n ≥ 2` with `n ≢ 1 (mod 24)` has a representation.

*Proof.* Let `n` be prime with `n ≢ 1 (mod 24)`.

- If `n ≢ 1 (mod 12)`: since `n` is prime, `n = 2`, `n = 3`, or `n ≡ 5, 7, 11 (mod 12)`. The residues `5` and `11 (mod 12)` fall under case 2 of the partition (`n ≡ 2 (mod 3)`), as does `n = 2`; the residue `7 (mod 12)` falls under case 3 (`n ≡ 4, 7, 10 (mod 12)`); and `n = 3` falls under case 1 (`n ≡ 0 (mod 3)`). All are covered by the identities of §2.2 — so `n` is covered.
- If `n ≡ 1 (mod 12)`: then by Lemma 4.1 (and `n ≢ 1 (mod 24)`) we get `n ≡ 5 (mod 8)`, and Theorem 2 (§2.3) applies — `n` is prime and `≡ 5 (mod 8)`.

∎ In Lean, this is `prime_non24_isErdosStraus`: the `h_not_open` guard of the residual-class lemma becomes automatic, because the only configuration in which that guard fails for a prime — `n ≡ 1 (mod 12)`, `5 ∤ n`, `n ≥ 13`, not `(prime ∧ n ≡ 5 (mod 8))` — is exactly the `≡ 1 (mod 24)` class, which is excluded here by assumption.

Theorem 4.2 is **unconditional**: no hypothesis is used, and the proof is elementary throughout.

---

## 5. The conditional reduction

**Theorem 5.1 (reduction).** Suppose (H24): *every prime `p ≡ 1 (mod 24)` admits positive integers `x, y, z` with `4/p = 1/x + 1/y + 1/z`.* Then every `n ≥ 2` admits a representation.

*Proof.* Let `n ≥ 2`.

- If `n` is prime: if `n ≡ 1 (mod 24)`, (H24) applies; otherwise Theorem 4.2 applies.
- If `n` is composite: by Corollary 3.3, `n` inherits from any prime factor `p ∣ n`; that prime again falls to (H24) or Theorem 4.2 by the prime branch.

∎ Machine-checked as `full_conjecture_of_h24` (`Reduction.lean`). There is no circularity: the composite branch consults only prime factors, and every prime terminates in either (H24) or a certified identity.

**Remarks.**

1. The reduction also shows the *documented axiom's* class statement (`n ≡ 1 (mod 12), 5 ∤ n, n ≥ 13` assumed wholesale in the Lean development) quantifies over a broader domain than necessary (only its prime `≡ 1 (mod 24)` part is genuinely open), and is not logically stronger once the reduction is established: Theorem 5.1 makes its content logically equivalent to (H24) — an, and the remaining content is machine-checked to follow from (H24).
2. Via §2.5, (H24) for a given prime `p` is *effective in form*: it suffices to exhibit, at any admissible `u`, a divisor `P` satisfying the span condition — the machine-checked wrapper then converts the span witness into an explicit solution. *(Restated per the third external review, V12-02.)* Theorem 5.2 itself already establishes a **finite decision procedure for each residual prime**: enumerate the finite parameter domain `3 ≤ u ≤ 2p, u ≡ 3 (mod 4)`; for each, enumerate the divisors of `M²` and test the span condition; return a solution if one exists, a certified negative result otherwise (given a correct implementation). Termination is therefore unconditional — it does not depend on (H24). What a proof of (H24) would guarantee is that the procedure **always returns a positive result**; a stronger quantitative covering theorem (`F(p) = O(log p)`, `O((log p)²)`, or a universal constant — open research questions, §6.3) could provide substantially smaller search bounds.

**Theorem 5.2 (finite-search equivalence).** Fix an odd prime `p ≡ 1 (mod 4)` (the (H24) class `p ≡ 1 (mod 24)` is the motivating instance; per the third external review, V12-06, the theorem does not use the `mod 24` restriction). Then `p` has an Erdős–Straus representation **if and only if** there exist `u` and a divisor `P` with

$$0 < u \le 2p, \qquad u \equiv 3 \pmod 4, \qquad \gcd(u, M) = 1 \ (M = px,\ x = (p+u)/4), \qquad P \mid M^2, \qquad P \equiv -M \pmod u.$$

*Domain remark (per review §4.4).* The admissible `u` satisfying `0 < u ≤ 2p, u ≡ 3 (mod 4)` are exactly `{3, 7, 11, …, 2p−3}` — `(p−1)/2` of them — and no member is divisible by `p` (the only multiples of `p` in range are `p` itself, `≡ 1 (mod 4)`, and `2p ≡ 2 (mod 4)`).

*Proof.* (⟸) is the constructive criterion of §2.5. (⟹) suppose `4/p = 1/x + 1/y + 1/z`, all positive. The defining identity `4·x·y·z = p(xy + xz + yz)` is fully symmetric in `x, y, z`, so reorder with `x` the smallest denominator. Then `4/p = 1/x + 1/y + 1/z > 1/x` gives `x > p/4`, and `4/p ≤ 3/x` gives `x ≤ 3p/4`; setting `u = 4x − p` yields `0 < u ≤ 2p`, `u ≡ −p ≡ 3 (mod 4)`. **Coprimality (the step added per review §4.2):** any common divisor `d` of `u` and `p` divides `4x = u + p`; since `p` is an odd prime, `d` is `1` or `p`, and `d = p` would force `p ∣ 4x`, hence `p ∣ x` (as `p ∤ 4`), contradicting `0 < x < p` — so `gcd(u, p) = 1`. The same argument with a common divisor of `u` and `x` (it divides `4x − u = p`, and would be `p` only if `p ∣ x`, again impossible) gives `gcd(u, x) = 1`; hence `gcd(u, M) = gcd(u, px) = 1` as the theorem requires. The witness is explicit: `P := u·y − M` and `Q := u·z − M` satisfy `P·z = p·x·y` and `Q·y = p·x·z` (one-line consequences of the defining identity), hence are positive, and `P·Q·y·z = (P·z)(Q·y) = p²x²y·z`, i.e. `P·Q = M²`. Finally `P = u·y − M ≡ −M (mod u)` additively. ∎

*Scope note (V12-06, continued).* The smallest-denominator argument and the divisor-factorization method are classical; the paper claims no originality for them. The contribution is the machine-checked **composition**: the extraction (`witness_extraction`, module `FiniteSearch.lean` — committed in v1.3, 0 sorries, standard axioms only) with the constructive reverse (`u_method_witness`, `CenteredCriterion.lean`) together make both directions of this equivalence Lean-verified, and fold the per-prime search into the span framework of §6.1. The open problem is then exactly: *for every prime `p ≡ 1 (mod 24)` the finite domain `{3, 7, …, 2p−3}` contains a successful parameter.*

---

## 6. (H24): what is and is not known

This section presents mathematical results, analytical observations, and computational evidence. It is included because (H24) is now, by Theorem 5.1, the precise remaining content of the conjecture.

**6.1 The span-criterion form.** For a prime `p ≡ 1 (mod 24)` and an admissible parameter `u ≡ 3 (mod 4)` with `p ∤ u`, put `M = p·(p+u)/4` (= `p·x`, so `gcd(M, u) = 1`: a common divisor of `x = (p+u)/4` and `u` divides `4x = p + u` and hence also `p`, and `p ∤ u`). By the one-divisor reduction (`CENTERED_PRODUCT_SET_THEOREM.md`; §2.5), the constructive criterion is equivalent to

$$\exists\, P \mid M^2 \;\;\text{with}\;\; P \equiv -M \;(\mathrm{mod}\ u) \qquad\Longleftrightarrow\qquad \exists\, P \mid M^2 \;\;\text{with}\;\; P\cdot M^{-1} \equiv -1 \;(\mathrm{mod}\ u).$$

Writing the prime factorization `M = ∏_{j=1}^{r} q_j^{e_j}`, the right-hand condition is the *span condition*: define the **centered product set** in the unit group `(ℤ/uℤ)×`,

$$\mathcal{S}_u(M) \;=\; \prod_{j=1}^{r}\,\bigl\{\,q_j^{-e_j},\; q_j^{-(e_j-1)},\; \ldots,\; q_j^{e_j-1},\; q_j^{e_j}\,\bigr\},$$

i.e. the set of all products `∏_j q_j^{t_j} (mod u)` with integer coefficients `t_j ∈ [−e_j, e_j]`. The parameter `u` succeeds for `p` iff `−1 ∈ 𝒮_u(M)`. The two divisor formulations match exactly: a divisor `P ∣ M²` has exponents `b_j ∈ [0, 2e_j]`, and putting `t_j = b_j − e_j` gives `P·M^{-1} = ∏_j q_j^{t_j}` — so multiplying the congruence `P ≡ −M (mod u)` by the unit `M^{-1}` (invertible because `gcd(M, u) = 1`) turns it into `P·M^{-1} ≡ −1 (mod u)`; conversely, any span witness `∏_j q_j^{t_j} ≡ −1 (mod u)` yields the divisor `P = ∏_j q_j^{t_j + e_j} ∣ M²` with `P ≡ −M (mod u)`. The permitted coefficient range is therefore exactly `[−e_j, e_j]`, matching the exponent window `[0, 2e_j]` of the divisors of `M²`.

**Cyclicity caveat (this subsection replaces the earlier single-generator formulation).** `(ℤ/uℤ)×` is a finite abelian group and is *not* cyclic in general; a discrete-logarithm phrasing to a single generator `g` is available only when the group happens to be cyclic — e.g. `(ℤ/35ℤ)× ≅ (ℤ/5ℤ)× × (ℤ/7ℤ)× ≅ C₄ × C₆` is noncyclic (it has no element of order 24). When `u` is an odd prime power — in particular every prime `u` (the prime-parameter layers `3, 7, 11, 19, 23, 31, 47, 59, 71, 79, 83, 103, 107, 127` of the repository's layer documents, and the composite prime power `u = 27 = 3³`) — `(ℤ/uℤ)×` is cyclic of order `φ(u)`: for a generator `g`, with `k_j = dlog_g(q_j mod u)` and `−1 = g^{φ(u)/2}`, the condition reads `∑_j k_j·t_j ≡ φ(u)/2 (mod φ(u))` for some `t_j ∈ [−e_j, e_j]` — a bounded modular integer combination (per the fourth review's V13-07 terminology note). In general, decompose `u = ∏_ℓ u_ℓ` into pairwise-coprime prime powers; by CRT, `(ℤ/uℤ)× ≅ ∏_ℓ (ℤ/u_ℓℤ)×`, and the condition is *coupled*: the same coefficients `t_j` must realize `−1` in every component simultaneously (since `−1 (mod u)` maps to `(−1, …, −1)` under the CRT isomorphism). `u = 35` is the worked example: the coupled condition in `(ℤ/5ℤ)× × (ℤ/7ℤ)×` is the correct formulation, and no single-generator version exists. The certificate dataset itself exercises the noncyclic case: 991 of its 166,011 records have a noncyclic first-working parameter `u ∈ {15, 35, 39, 51, 55}` (of 1,082 records whose first-working parameter is composite, the remainder is the cyclic prime power `u = 27`). The layer analyses `MOD31_EXACT_REDUCTION.md` and `MOD35_CRT_SPAN.md` document this condition exactly, with zero mismatch across the certified stages (at `u = 31`: 283 stage entrants, 0 span mismatches; at `u = 35`: the coupled condition in `(ℤ/5)× × (ℤ/7)×`, 93 entrants, 0 mismatches; a 2026-11-19 reconciliation, `FIRST_A_STRUCTURE.md`, recomputed the stage chains with the full admissible layer set — the documented chain omitted `u = 19` and `u = 27`, and the true residual-class stages are 217 entrants, of which 152 succeed, at `u = 31` and 65 entrants, of which 17 succeed, at `u = 35`, terminating identically).

**6.2 What least-non-residue bounds give.** The classical effective inputs are:

- *Burgess (1962) via Norton (1971):* the least prime quadratic non-residue `q` modulo `p` satisfies `q ≪ p^{1/(4√e) + ε}` for every `ε > 0`.
- *Ankeny (1952), under GRH:* the least non-residue is `O((log p)²)`.

These results bound the least quadratic non-residue for a specified modulus. Scope, made explicit per the ninth review's V19-05: the classical bounds establish the **existence** of small non-residues modulo a given number — they neither guarantee that such a non-residue divides `M = p(p+u)/4`, nor that the bounded product set of `M`'s prime factors reaches `−1` modulo `u`. Obtaining a non-residue in a *prescribed residue class* is a strictly stronger demand and would need its own effective input — e.g. a GRH-conditional Ankeny-type bound for the least prime in a prescribed coset of `(`ℤ/uℤ)*`, or uniform Burgess-type character-sum estimates over that coset; no unconditional theorem of that strength is claimed or used here. These results also do **not** address the actual requirement of (H24): the non-residue's discrete logarithm must land in a specific coset determined by the forced factors' span — a *reachability* condition, not an existence condition (cyclic-scope: for a prime parameter `u` such as 31, `(ℤ/uℤ)×` is cyclic and the single-generator phrasing is exact; the noncyclic layers carry the coupled CRT formulation of §6.1). The `u = 31` analysis makes the distinction concrete on the corrected cohort: of the 65 true failures at that layer (first-u ≥ 35), 47 are QR-pure — blocked by the parity obstruction before any reachability question can arise — and 18 further failures are non-QR-pure yet still unreachable (the span-delicate cases, fingerprinted in `analysis/u31_layer_corrected.json`); the cube-class rescue structure, while characterizable, is not a consequence of Burgess-type bounds.

**6.3 What remains open after Theorem 5.2.** Theorem 5.2 changed the shape of the remaining objective. The search domain is no longer something to be bounded — it is **proved** finite: the complete admissible domain is `{3, 7, …, 2p−3}` (`B(p) = 2p−3` is now a theorem, not an objective, and no member needs a coprimality exclusion). Distinguishing three separate objectives (per the third external review, V12-03):

| Objective | Status |
| --- | --- |
| Establish a finite, complete search domain per prime | **Proved** (Theorem 5.2) |
| Establish that the domain always contains a witness | Open; equivalent to (H24) |
| Establish a substantially smaller sufficient bound | Open; stronger quantitative objective |

The quantitative question is now expressed in terms of a precisely defined quantity. Define, for `p ≡ 1 (mod 24)`,
For **every prime `p ≡ 1 (mod 4)`** (restored at v1.9 per the ninth review's V18-02), define

> `F(p) = min{ u ∈ {3, 7, …, 2p−3} : −1 ∈ S_u(p(p+u)/4) }`,
>
> with **`F(p) = ∞` when the set is empty** (the hypothetical counterexample cases the program characterizes).

Both the (H24) equivalence and the v1.8 mod-24 lemma use this same well-defined function on its full domain. Then: the finite-search objective is exactly `F(p) ≤ 2p−3` **for every** such `p` (equivalent to (H24)); the quantitative objectives are `F(p) = O(log p)`, `F(p) = O((log p)²)`, or a universal constant bound — these are **research questions, not established results**, and the verified computational record through `10^9` alone justifies none of them (though the empirical maxima — first-working `u = 83` against `2p = 575,134,562` at `p = 287,567,281`, and `107` against `2p = 17,606,738` at `p = 8,803,369` — suggest the bound gap is enormous and worth attacking). The instructive case in the data, `p = 8,803,369`, was settled by computation (first working `A = 107`) — a parameter that may have antecedents in the literature this repository has not verified: the Ionascu–Wilson framework (Rev. Roumaine Math. Pures Appl. 56 (2011), 21–30) already bounds the first denominator and tabulates exceptional prime classes, so this program claims no novelty for the record itself.

**6.4 The Mordell constraint on identity-hunting.** By the Mordell (1969) principle — the framework being *polynomial identities*: parametric solutions `4/n = 1/x(n) + 1/y(n) + 1/z(n)` with `x(n), y(n), z(n)` polynomials in `n` (rational, in particular integer, coefficients), required to give solutions for **every** integer `n` in an entire residue class `n ≡ r (mod m)` — no such identity exists for a **primitive** class `gcd(r, m) = 1` whose representative is a quadratic residue modulo `m` (i.e. whenever `x² ≡ r (mod m)` is solvable); the primitiveness hypothesis is essential — Elsholtz–Tao state it explicitly, and non-primitive QR classes can admit trivial identities (e.g. `n ≡ 4 (mod 12)`: `4/n = 1/(n/2) + 1/n + 1/n` for all members). The obstruction is uniform: no polynomial identity, and hence no finite system of identities, can cover the `≡ 1`-classes, because `1` is a quadratic residue modulo every modulus. Two scope qualifications are in order: the obstruction is about **finite systems of uniform polynomial identities** — it does not eliminate more general *covering systems* (the survey of Bloom and Elsholtz (2022) reformulates the conjecture as a coverage claim over congruence classes, a potentially infinite covering system that the obstruction does not rule out), nor does it eliminate the span-route or other structural mechanisms. The route to (H24) therefore cannot finish purely by extending the identity table; this repository's route goes through the span/reachability structure of §6.1 — the route its data are built for — while covering-system routes along the Bloom–Elsholtz reformulation remain open alternatives.

**6.5 The empirical record.** Two computational layers support the expectation that (H24) holds with tiny parameters; as of the 2026-11-21 revision their methods and exact scopes are stated below, and the hard-case-sweep artifact class was re-attributed and then resolved by a corrected re-run the same day:

- the certificate layer `results/layer4_certificates.jsonl`: **166,011 records**, each carrying a full divisor-certificate (`n, A, x, y, z, P, Q, T, N`) re-verified field-by-field — divisor relations, congruences, positivity, and the unit-fraction identity — by the CI-gated verifier `analysis/layer4/verify_certificates.py`, with record count, duplicates, exact domain coverage, and max `A` checked by the independent checker `analysis/layer4/check_certificate_dataset.py`. The dataset's domain — the sense of *admissible* in the layer-4 tooling — is exactly: `p` prime, `13 ≤ p ≤ 10,000,000`, `p ≡ 1 (mod 12)`. That domain decomposes into **82,887 primes `≡ 1 (mod 24)`** — the class (H24) is about — and **83,124 primes `≡ 13 (mod 24)`**, which are already covered unconditionally by Theorem 2 (primes `≡ 5 (mod 8)`); the layer is thus a strict superset of (H24)'s domain, and the (H24)-exact figure is the 82,887-record subclass. Within the layer, the largest first-working `A` = **107** (record `8,803,369`, which is prime and `≡ 1 (mod 24)`); every record's parameter `A` is an admissible `u` (odd, `≡ 3 (mod 4)`, with `gcd(n·x, u) = 1`), and each record's witness is verified independently of the search that located it.
- hard-case sweeps toward `10^9` — **resolved by the corrected exact-criterion re-run of 2026-11-21** (`sweep_exact/`). The previously cited artifacts are retired: `verification_100M_1B.json` was produced by the superseded three-target shortcut (pre-2026-08-28), and even the exact-criterion `verification_10M_1B.json` carries a verifier defect — its `factor_x` trials odd primes only (no `2`), corrupting the divisor enumeration for **even `x`**. Which records have even `x` is a two-sided parity interaction (corrected per external review F-02): `x = (n + u)/4` is even precisely when `n ≡ 5 (mod 8)` and `u ≡ 3 (mod 8)`, or when `n ≡ 1 (mod 8)` and `u ≡ 7 (mod 8)` — so the bug struck **both prime classes at alternating parameter parities**, not one class as previously stated. Its recorded **7 "no-solution" cases are disproven by explicit witnesses** (all resolve within `u ≤ 251`, first `u ∈ {3, 31, 71, 151}` — `sweep_exact/seven_case_witnesses.json`; three of them resolve at `u = 3`). The corrected re-run (`sweep_exact/exact_span_sweep.c`, predicates mirrored 1:1 from the committed verifiers, self-tested by an independent brute-force enumeration on 1,326 cases with 0 mismatches plus pinned anchors `n = 1129 → u = 11`, `n = 8,803,369 → u = 107`, and — added after external review F-01 — `n = 32,349,601 → u = 15`) reproduces the committed populations **exactly** — 3,194,231 prime hard cases in `[10^7, 10^9)` (the `verify_10M_to_1B` family) and 2,850,823 in `[10^8, 10^9)` (the sum of the `corrected.py` family's two sub-range artifacts, 345,956 + 2,504,867) — and finds **0 failures at `u ≤ 251` in both**. A second defect found at review (F-01): the re-run's parameter list had enumerated **prime `u` only**, never testing the composite layers 15, 27, 35, 39, 51, 55, 63, 75 — `n = 32,349,601` was wrongly reported at first-u 227 while an exact `u = 15` certificate exists (verified independently at review, and now by the corrected engine's own self-test anchor). With the **full admissible u-set** (every integer `u ≡ 3 (mod 4)` ≤ 251), the sweep reports largest first-working `u = 83` (at `n = 287,567,281`); the recorded distribution is led by `u = 3: 830,200` and `u = 7: 1,949,770` (**87.0%** at `u ≤ 7` — figure also independently confirmed at review; `sweep_exact/verification_10M_1B_exact_rerun.json`, `verification_100M_1B_exact_rerun.json`, `nonparametric_1e7_1e9.jsonl`, `NONPARAMETRIC_TAIL.md`).
- **The sweep population, stated mathematically (per the third external review, V12-04).** So an independent reader can reconstruct the population without the repository's scripts, the hard-case population counted as 3,194,231 is exactly the set
  {prime `p` : `10^7 < p < 10^9` (endpoints excluded, the interval actually iterated is `10000001 ≤ p ≤ 999999999`), `p ≡ 1 (mod 12)`,
   and every odd prime factor of `(p+3)/4` is `≡ 1 (mod 3)` }
  —the "b₃-hard" predicate of the certificate layer, **including** the case in which `x` is a power of two (`b₃ = 2^a`, i.e. all odd prime factors vacuously `≡ 1 (mod 3)`; no previously solved or otherwise-solved case is omitted or special-cased: the predicate is applied uniformly, the earlier cascade layers simply never meet it). The per-`p` search then tests the **complete admissible parameter set** `u = 3, 7, 11, …, 255` (every integer `≡ 3 (mod 4)` up to the engine's ceiling 255 — harmonized across source, metadata, and text at v1.4; the earlier text said 251, the engine and metadata said 255, and the recorded maximum 83 makes the difference immaterial), in that order, and the **first-working parameter** is the least `u` in that set satisfying the exact one-divisor span criterion (§6.1): a divisor `P` of `M²` (`M = p·x` with `x = (p+u)/4`, requiring `u ≡ 3 (mod 4)`) with `P ≡ −M (mod u)` — the complementary congruence `M²/P ≡ −M (mod u)` follows automatically from `gcd(M, u) = 1` and is checked as a safety net. Failure within the ceiling is reported as a miss (there are none in either committed range). This is the full specification of the distribution table below; reproducing it is a straightforward program of the same shape, and the reviews' independent implementations of §5–§6 matched it at every reported statistic.

**Third-party implementation executed (fourth review §3.5).** The review retained its independent C++ implementation and results so the author could reproduce its findings; the source (committed here as `third_party_independent_sweep.cpp` — residue-map divisor enumeration, 128-bit witness arithmetic with assertion validation, `u ≤ 251` ceiling) was re-executed by the author end-to-end in 4.3 s. Its output agreed **entry-for-entry** on all three populations: the certificate layer (166,011 primes in the certificate domain, (H24) subclass 82,887, maximum first-working `u = 107` at `p = 8,803,369`, and the full 16-row parameter distribution — itself matching the committed certificate dataset's own field histogram), the `[10^7, 10^9)` sweep (3,194,231 / 0 failures / max `u = 83`, (H24) 2,364,031, the full 21-row distribution identical to `verification_10M_1B_exact_rerun.json`), and the `[10^8, 10^9)` sweep (2,850,823 / 0 / 83, (H24) 2,110,409, identical to `verification_100M_1B_exact_rerun.json`), including both `u = 83` record primes (`287,567,281`, `651,412,441`), every returned witness re-validated by 128-bit exact arithmetic. The reviewer's `u ≤ 251` ceiling versus the repository engine's `u ≤ 255` is immaterial (the recorded maximum is 83). Three engines — the reviewer's C++, this repository's C engine, and the committed Python/certificate lineage — now agree statistic-for-statistic.

No counterexample to (H24) is known. Two cautionary notes keep the record honest: this repository's own exact-criterion exhaustive verification is the certificate layer to `10^7` together with the corrected `10^9` hard-case sweeps (§6.5), while the literature's reported exhaustive record is the `~10^{18}` range (Mihnea & Bogdan, arXiv:2509.00128, 2025 — *reported*, not independently verified by this repository); and the earlier `10^{21}`-type claims in this repository were withdrawn in `CORRECTED_CLAIM_AUDIT.md` and are **not** relied upon anywhere in this paper. Computation cannot close a universal claim, and nothing in §6.1–6.4 stands in for the missing theorem.

**Fourth-review additions to the sweep record (2026-11-23).** An independent third-party re-implementation (a separate C++ engine using a prime sieve, complete factorization, exhaustive divisor-residue enumeration with composite parameters, and integer witness validation — not the repository's engine) reproduced the full sweep through `10^9` exact-integer: population 3,194,231, 0 failures, maximum first-working `u = 83`, and the complete distribution below **matching the committed artifacts statistic-for-statistic (11 of 11 published comparisons plus the full 21-row distribution)**, in under ten minutes. It also (i) found a **second maximum-record prime**: the first-working parameter `u = 83` is attained by `p = 287,567,281` *and* `p = 651,412,441` — this repository's regenerated sweeps confirm both (the engine's parameter-ceiling is now harmonized across source, metadata, and text at `u ≤ 255`, every integer `≡ 3 (mod 4)`; the recorded maximum 83 is far below either 251 or 255, which is why the earlier 251/255 wording discrepancy was immaterial), (ii) added the two anchors to regression pinning (the engine's self-test now carries `651412441 → 83` alongside the three earlier anchors), and (iii) supplied (H24)-specific population statistics, verified here by the repository's own regeneration: of the 3,194,231 hard cases in `[10^7, 10^9)`, **2,364,031 are primes `≡ 1 (mod 24)`** — the class (H24) is about — and of the 2,850,823 in `[10^8, 10^9)`, **2,110,409 are**. The regenerated artifacts now carry the (H24)/(≡ 13 (mod 24)) split natively (`h24_hard_cases`), and a new middle-range artifact (`verification_10M_100M_exact_rerun.json`: 343,408 hard cases, first-working maximum `u = 63`, non-parametric 34,506) closes the range decomposition exactly: 343,408 + 2,850,823 = 3,194,231 and 34,506 + 283,063 = 317,569 (the non-parametric three-way split: 34,506 in `[10^7, 10^8)`, 283,063 in `[10^8, 10^9)`, and 0 in-sweep below `10^7` — the ≤ `10^7` non-parametric statistics come from the certificate layer, a different population, per §6.5's layer definition).

**Arithmetic safety (fixed per the fourth review's V14-01, fifth review's finding retained).** Two signed-64-bit overflow sites existed in the C engine's divisor search (the product `d1n · xfs[b]` / `d1n · divs[b]` was computed before the admissibility bound check, and for the largest sweep primes the true product `px²` reaches ≈ p³/16 ≈ 6.25 × 10^{25} near `p = 10⁹` (approximately 6.8 million times the signed 64-bit maximum (6.25 × 10^{25} against 9.22 × 10^{18}) at the top of the range; the ≈2.12 × 10^{21} figure previously cited corresponded to the review's smaller anchor-scale example) — undefined behavior in C). Both sites now widen to 128 bits before the bound check, in both engines; and the sanitizer additionally exposed a subtler defect the review's line-grep had missed: the divisor-table construction itself (`divisors_of_square`) accumulated per-prime exponent overshoots (pass `k` of `0..2e` multiplied the *current* list by `p^k`, so combined exponents could exceed `2e`) whose intermediate products also overflowed i64. The construction now accumulates in 128 bits and keeps only divisors ≤ `M` — the admissible-candidate superset is unchanged, since a candidate is `d1n · divs[b]` with `d1n ≥ 1`, so no divisor above `M` can ever be admissible. Both engines were rebuilt under `-fsanitize=undefined -fno-sanitize-recover=undefined` and rerun: the full `[10^7, 10^9)` sweep completes in **67 s with zero sanitizer reports**, and the sanitized regenerated artifacts reproduce every published statistic exactly (populations 3,194,231 / 0 failures / max `u = 83`, complete 21-bucket distribution identical, (H24) splits 2,364,031 / 2,110,409, non-parametric decomposition 34,506 + 283,063 = 317,569). The artifact SHA-256 pins in Appendix A were updated; Appendix A's reproduction command now specifies the sanitized build.

**Witness-dependent classification (per fourth review V14-02).** The non-parametric counts must be read as *witness-selection* statistics, not intrinsic prime properties: 317,569 is **"the number of primes for which the first witness selected by the specified enumeration algorithm is non-parametric."** The distinction is concrete — for `p = 193`, `u = 7`, `x = 50` (p = 193 is b₃-hard, first-working `u = 7`), both a parametric witness (`y = 1,380`, `z = 1,331,700`, `z mod y = 0`) and a non-parametric witness (`y = 1,450`, `z = 27,985`, `z mod y = 435`) provide two representations at the same parameter — so a first-found non-parametric witness does *not* establish that no parametric witness exists at that parameter. The v1.5 engine therefore separates the three classes the review recommends, by scanning all witnesses at the first-working parameter: over `[10^7, 10^9)`, **2,876,662 primes have their first-selected witness parametric; 228,486 have both types available with a non-parametric witness selected first; and 89,083 (2.79%) have no parametric witness at the first-working parameter** (over `[10^8, 10^9)`: 2,567,760 / 204,728 / 78,335; over `[10^7, 10^8)`: 308,902 / 23,758 / 10,748) — the third class is the review's proposed research target and is now a native field (`witness_no_param_at_first_u`) of the committed artifacts.

**Intrinsic witness classification (per sixth review §3.3).** The witness-selection statistics above remain published for reproducibility, but the review's stronger classification depends only on *which witnesses exist* at the first-working parameter, not on the enumeration order. The review's independent engine computed it and this repository's records reproduce it: with denominators ordered `y ≤ z`, over `[10^7, 10^9)` **83,860 primes (2.63%) have only parametric witnesses, 3,021,288 (94.59%) have both types, and 89,083 (2.79%) have only nonparametric witnesses** (over `[10^7, 10^8)`: 10,439 / 322,221 / 10,748; over `[10^8, 10^9)`: 73,421 / 2,699,067 / 78,335). The intrinsic and selection-based tables agree on the research population's size (89,083), which is consistent: a prime whose first-*selected* witness is non-parametric is exactly not one whose first-selected witness is parametric, and the count of primes with no parametric witness available at all is selection-order-free.

**One-sided characterization of the research population (per sixth review §4; formalized at v1.6).** With `M = p·x` and the witness-pair construction `y = (P + M)/u`, `z = (M²/P + M)/u`, the ratio is exactly `z/y = M/P` (multiplying by `u`: `z·u = M²/P + M = (M/P)·(P + M)`), hence

> **`y ∣ z  ⟺  P ∣ M`.**

A parametric witness can therefore be detected from the divisors of `M` alone, without constructing both denominators. Writing `P = M/d`, the required congruences reduce to `d ≡ −1 (mod u)` (cancel the unit `P` modulo `u`; `gcd(M, u) = 1` by admissibility), which gives the review's **one-sided product-set criterion**: a parametric witness exists for `(p, u)` iff **`−1 ∈ 𝒟_u(M)`**, where `𝒟_u(M) = { Π qⱼ^{tⱼ} mod u : 0 ≤ tⱼ ≤ eⱼ }` is the set of divisor residues of `M` — in contrast with the paper's centered product set `𝒮_u(M)`, which spans products of divisor residues and their multiplicative inverses (modulo `u`; equivalently `𝒮_u = 𝒟_u · 𝒟_u^{-1}` in the unit group). The review's proposed research population (sixth review §4.2) is therefore characterized exactly by the set-difference

> **`−1 ∈ 𝒮_u(M)` and `−1 ∉ 𝒟_u(M)`** at the first-working `u` — the 89,083 primes are precisely those where centered reachability succeeds but one-sided reachability does not.

Both statements — and the complete divisibility biconditional — are now machine-verified in `FiniteSearch.lean` (axiom sets `propext, Classical.choice, Quot.sound` for `parametric_divisibility` and the composed iff, `propext, Quot.sound` for the constructive `param_exists_iff_onesided`, per the current 15-result CI audit): `parametric_divisibility` (`T ∣ M ⟹ y ∣ z`, quotient `M/T`), `parametric_divisibility_iff` (the complete biconditional `T ∣ M ⟺ y ∣ z` added at v1.7 per the seventh review's V16-01, with positivity and exact-divisibility hypotheses), and `param_exists_iff_onesided` (parametric-witness existence ⟺ some divisor `d ∣ M` satisfies `(d + 1) mod u = 0`, i.e. `−1 ∈ 𝒟_u(M)`). The review notes the elementary derivations may have antecedents in the literature this repository has not verified; originality is not claimed here either.

**Classical mod-840 filtering executed independently and reproduced (seventh review §4).** The classical reduction restricts the unresolved prime classes to `p ≡ 1, 121, 169, 289, 361, 529 (mod 840)`. The seventh review's independent engine applied the restriction to the full sweep population and this repository archived and re-executed its source byte-for-byte (`sweep_exact/third_party_independent_mod840.cpp`, SHA-256 `3b5fafb47750c10fa8c19c7dc950be01b6a3c8c87043df039c523dace4163d40`; committed output and digest alongside), reproducing every number exactly:

| Population | Total | Only parametric | Both types | Only nonparametric |
| --- | --- | --- | --- | --- |
| Complete sweep `[10^7, 10^9)` | 3,194,231 | 83,860 | 3,021,288 | 89,083 |
| (H24) | 2,364,031 | 83,860 | 2,191,088 | 89,083 |
| Classical mod-840 | 795,913 | 22,743 | 750,948 | **22,222** |

Two structural observations carry forward. First, **all 89,083 nonparametric-only primes are in (H24)** — the mod-24 filter removes none of them; the research cohort was always a (H24) cohort. Second, the classical mod-840 filter removes **66,861 of the 89,083 (75.05%)**, leaving a **22,222-prime research cohort** with the following distribution over the six classical residual classes (total hard cases / only-nonparametric): `1: 129,979 / 5,502`; `121: 129,963 / 5,028`; `169: 129,675 / 1,939`; `289: 130,073 / 1,916`; `361: 138,184 / 5,737`; `529: 138,039 / 2,100` — total 795,913 / 22,222. The class-to-class structure splits cleanly: the **nonparametric-only rate** differs substantially between two groups — `1: 4.23%`, `121: 3.87%`, `361: 4.15%` (a near-4% group) versus `169: 1.50%`, `289: 1.47%`, `529: 1.52%` (a near-1.5% group), while the total populations are nearly flat (129,675 to 138,184; the smallest is 169, not 1). The rate split is a question for further structural analysis; the counts alone do not establish cause.

**Opposite-residue collision reformulation (seventh review §5.3).** With `𝒟 = 𝒟_u(M)` the one-sided divisor set, every centered exponent combination separates into positive and negative parts, giving `𝒮_u(M) = 𝒟·𝒟^{-1}`; hence `−1 ∈ 𝒮_u(M)` iff `∃ a, b ∈ 𝒟 : a·b^{-1} = −1`, i.e. iff the one-sided set contains two opposite residues `𝒟 ∩ (−𝒟) ≠ ∅`. Centered reachability succeeds precisely when the divisor-residue set contains two opposite residues. The pigeonhole principle then supplies a **sufficient** (not necessary) condition — valid for cyclic and noncyclic unit groups alike: `|𝒟_u(M)| > φ(u)/2 ⟹ −1 ∈ 𝒮_u(M)`. This gives the research program a concrete analytical target: prove adequate growth of the divisor-residue set across parameter layers, or establish an opposite-residue collision structurally. The formulation's originality in the literature is not established and is not claimed.

**The `p ≡ 13 (mod 24)` class resolves at `u = 3` (eighth review §5; promoted to a machine-checked lemma).** This is not merely the empirical observation that every only-nonparametric prime lies in (H24) — it follows from the structure. For `p = 24k + 13`, the parameter gives `x = (p + 3)/4 = 6k + 4`, which is **even**, so `M = p·x` is even while `M ≡ 1 (mod 3)` (both factors are `1 mod 3`). The divisor `T = 2 ≡ −1 (mod 3)` therefore satisfies every witness condition — `2 ∣ M²`, `2 ∣ M`, and `(2 + M) mod 3 = 0` — so the one-sided criterion supplies a parametric witness at the smallest admissible parameter:

> **`F(p) = 3` for every prime `p ≡ 13 (mod 24)`.**

Made explicit per the ninth review's V18-03 — the converse side applies to **(H24) primes satisfying the hard-case population predicate** (with it, `x = (p+3)/4` is odd and every prime factor of `M` is `1 mod 3`, so every divisor residue is `1` and `u = 3` fails; without the predicate the claim is false — e.g. `p = 97 ≡ 1 (mod 24)`: `M = 2425 = 5²·97` has the factor `5 ≡ 2 (mod 3)`, and indeed `u = 3` succeeds there: `4/97 = 1/25 + 1/970 + 1/4850`), this **explains the u = 3 population exactly**: `3,194,231 − 2,364,031 = 830,200` is the reported count of primes whose first-working parameter is 3 — the full sweep population minus its (H24) subclass, identically. The implication's witness direction is machine-verified (`h213_parametric_u3` in `FiniteSearch.lean`, in the 15-result CI axiom audit); it also supplies another regression invariant for every future sweep.


**Independent proof-kernel verification (standing since v1.5; the current release's record).** The principal-theorem dependency closure is exported with [lean4export](https://github.com/leanprover/lean4export) pinned at `a3e35a5` (the upstream commit whose toolchain is exactly `v4.30.0`) and re-checked with [nanoda](https://github.com/ammkrn/nanoda_lib) pinned at `0da9f98` (v0.4.32) — a **Rust implementation of the Lean 4 type-checking kernel, independent of Lean's own** — under **strict axiom enforcement** (`unpermitted_axiom_hard_error: true`, `unsafe_permit_all_axioms: false`, permitted axioms = the standard trio only; any unpermitted axiom used by any checked declaration aborts the run). **Most recent proof verification (v1.8), carried forward to v1.9 with unchanged Lean sources: 13,093 declarations checked, zero typechecker errors, exit 0** (export SHA-256 `95a175a22903ad2d0957b0551df50b5d07e63cd6517a0c56fe007bab51ac1767`) (the full release gate `scripts/nanoda_gate.sh` also asserts both tool revisions and clean source trees, rebuilds both executables from their pins, records the binary hashes and the export SHA-256 pre- and post-check, and regenerates every evidence file it hashes; end-to-end PASS). The export's axiom set is independently enumerated from the intern table as **exactly three** fully qualified axioms — `propext`, `Quot.sound`, `Classical.choice` — with no `sorryAx`, no `Lean.trustCompiler`, and neither documented project axiom; all **15** principal theorems resolve as fully qualified `thm` records (exact names, exactly once each). Verification lineage: v1.5 — 11 theorems, 13,076 declarations; v1.6 — 13, 13,083; v1.7 — 14, 13,086; v1.8 — 15, 13,093 (all strict, all exit 0; zero typechecker errors in every prior release as well — per-release details and the complete evidence pack with digests in `SHA256SUMS` live in `verification_nano/NANODA_RUN.md`, with the historical per-release instructions marked as historical there).

**The excluded-class observation (per the fourth review's §6).** The b₃-hard population predicate itself yields a provable one-line structure in the opposite direction. For a prime `p ≡ 1 (mod 12)`, set `x = (p+3)/4`, `M = p·x`. If the predicate *fails*, `x` has an odd prime factor `q` with `q ≡ 2 (mod 3)`; since `q ∣ M`, the centered product set for `u = 3` contains `q`, and `q ≡ −1 (mod 3)` — so **every excluded prime already possesses a valid divisor-span witness at `u = 3`**. Combined with (i) the independently reproduced certificate-layer coverage through `10^7`, (ii) the independently reproduced hard-case sweep through `10^9` (the b₃-hard cases), (iii) the unconditional prime coverage outside (H24) (Theorem 5.1's partition), and (iv) the scaling lemma for composites, this yields independent computational verification of the Erdős–Straus conjecture for **every integer `2 ≤ n ≤ 10^9`**. This is not a computational world record (the literature reports `~10^{18}`), but it is an independent validation of this program's mathematical and computational framework. The b₃-failure side of §6.1's structure is thus a *proved sufficient condition*, not a heuristic; the span-reachability of the b₃-hard cases (the (H24)-residue) remains the single open question.

---

## 7. Conclusion

The Erdős–Straus conjecture is logically equivalent to the single statement (H24) about primes `≡ 1 (mod 24)`. One direction is trivial; the other is Theorem 5.1, whose proof is elementary, complete, and machine-checked with no new axioms. The reduction's practical value: it eliminates the composite portion of the resistant class with no casework (scaling, §3); it shows the certified partition meets the resistant class in exactly one prime residue (§4); Theorem 5.2 bounds the per-prime search domain (`0 < u ≤ 2p`, finite); and it converts any future analytic progress toward (H24) — a covering theorem over the span classes of §6.1, or a GRH-conditional span-reachability result — into solutions, because the criterion-to-solution direction is constructive and formalized (§2.5).

The conjecture is not proved, here or in the literature; (H24) is open, and the remaining open problem it poses is now shaped by Theorem 5.2: the per-prime search domain is **proved** finite (`{3, 7, …, 2p−3}`), so what remains is to prove the *witness-existence* half — that the domain always contains a span-reachable witness, i.e. `F(p) ≤ 2p−3` for every prime `p ≡ 1 (mod 24)` (§6.3) — or the stronger quantitative form of the same statement. This provides an equivalent formulation suitable for structural analysis, because every surrounding combinatorial ingredient is now either certified or reduced away.

---

## Appendix A. Provenance and reproducibility

**Lean formalization.** Lean 4.30.0 with Mathlib v4.30.0 (pinned, CI-enforced). The components of this paper:

| Component | Module | Status |
|---|---|---|
| Scaling lemma (`scaling`) | `Reduction.lean` | proven, 0 `sorry` |
| Mod-chain lemma (`mod8_of_12`) | `Reduction.lean` | proven, 0 `sorry` |
| Unconditional prime coverage (`prime_non24_isErdosStraus`) | `Reduction.lean` | proven, 0 `sorry` |
| Witness-extraction direction of Theorem 5.2 (`witness_extraction`) | `FiniteSearch.lean` | proven, 0 `sorry` |
| Conditional reduction (`full_conjecture_of_h24`) | `Reduction.lean` | proven, 0 `sorry` |
| Constructive criterion (`u_method_core` + wrapper) | `CenteredCriterion.lean` | proven, 0 `sorry` |

Supporting Lean modules: `DivisorResidue`, `ClassicalIdentities`, `OmegaCases`, `CenteredEquivalence`, `MainTheorem`, `Theorem4`, `NewTheorems` — together with `CenteredCriterion`, `Reduction`, and (from v1.3) `FiniteSearch`, the ten-module CI build set. Remaining unfinished goals in the root project: 3, census-enforced (all in `OmegaCases.lean`). Documented axioms: 2 — `erdos_straus_mod_12_1_not_div_5_conjecture` (whose content Theorem 5.1 shows follows from (H24)) and `divisor_residue_criterion_reverse`.

**Source pinning (fourth-review rewrite, V13-04).** The v1.3 pinning note claimed that commits after `f035a9d…` touch only the paper text, data files, and sweep engines. That claim became false with v1.3 itself, which introduced the new module `ErdosStrausConjecture/FiniteSearch.lean`, extended `scripts/print_axioms.lean`, and changed the CI workflow. The pinning is therefore restated as a **full-tree rule**: each paper release is pinned to the complete accepted tree by an immutable release tag — the v1.2-era tag `paper-v1.3` is preserved as provenance but is **known-incomplete** for v1.3 content (fourth review V13-01: it predates the `FiniteSearch.lean` formalization, the updated audit script, and the ten-module CI, so a reviewer following it would miss the v1.3 theorem); the authoritative v1.3 content lives on `main` at commit `83cda3d8134eda8f5ef53135937cb206d8dd6cc0`, the release trees carrying all of this were pinned after their commits by the immutable tags **`paper-v1.4`**, **`paper-v1.5`** (`ee9b8dca5fb92f7abbc99ab6ef7d1db70b154ee7`), **`paper-v1.6`**, **`paper-v1.7`** (`d234c2cec993fec97e5d1645261e029eede2b8c4`). Lean 4.30.0 and Mathlib v4.30.0 are pinned by `lean-toolchain` and the upstream revision in `lakefile.toml`. The audit below is now executed **by CI** (the `print_axioms` gate, V13-03), not by hand. The artifact-provenance table (single release summary, current at v1.10):

| Artifact | Provenance |
| --- | --- |
| Lean modules | The complete accepted tree, pinned by release tag **`paper-v1.10`** (the proof-source lineage: `paper-v1.8` = `a4077e6c3e4fe2d6369cdf57c9b50e722a2798f3`, unchanged through the documentation releases `paper-v1.9`/`paper-v1.10` per V19-03); the full per-release lineage (through `paper-v1.7` = `d234c2cec993fec97e5d1645261e029eede2b8c4`) is recorded in `CHANGELOG.md` |
| Lean axiom audit | `scripts/print_axioms.lean` + gate `scripts/check_axioms_audit.py`; **executed in CI** (`lake env lean scripts/print_axioms.lean | scripts/check_axioms_audit.py`); latest local execution: **15 principal results** (v1.6's `parametric_divisibility` (trio) and `param_exists_iff_onesided` (`propext, Quot.sound`); v1.7's `parametric_divisibility_iff` (trio); v1.8's `h213_parametric_u3` (trio)), all matching the expected axiom sets exactly |
| Certificate dataset | `results/layer4_certificates.jsonl`, SHA-256 `e864053e4e193fb8f781994994a1fc885c5c9e5fd02362f2018dceca3e50634f` (unchanged; re-verified at v1.4; **byte-integrity fully verified at v1.6**: all 166,011 records re-validated field-wise from the committed bytes with exact big-integer arithmetic — zero failures, max `A` = 107 at `n` = 8,803,369, (H24) subclass 82,887) |
| Certificate verifier | `analysis/layer4/verify_certificates.py` at commit `e695c05` (the dataset-regeneration commit) |
| Corrected sweep engine | `sweep_exact/exact_span_sweep.c` (full-u-set version, uncapped non-parametric counter, mod-24 split, four pinning anchors `1129→11`, `8803369→107`, `32349601→15`, `651412441→83` — the fourth anchor added per the fourth review's independent finding) |
| Sweep results | `sweep_exact/verification_10M_1B_exact_rerun.json` SHA-256 `d9f7720bce9627c8fe126aebc5abfdcffa826ddf77dbcce517716555f242e2ea`; `verification_100M_1B_exact_rerun.json` SHA-256 `b2fcbca453b767aac2ba956091f0de08de254e08a6f4b63263fd381cedec9867` — **the 100M–1B artifact was REGENERATED at v1.4** (the previously committed copy predated the F-01 composite-parameter fix: it reported a first-u maximum of 167 with no composite buckets; the regenerated file reports 2,850,823 hard cases, 0 failures, maximum first-working `u = 83`, and the composite buckets — matching the fourth review's independent execution statistic-by-statistic); `verification_10M_100M_exact_rerun.json` SHA-256 `c0ea3d42d3ab569e806ecd51dddc2d6156910a8c4b4020adaa21ed3cdccb0fa0` (middle-range artifact supplying the independent non-parametric decomposition; regenerated sanitized at v1.5 alongside the two primary artifacts, with the same published statistics); `nonparametric_1e7_1e9.jsonl` unchanged SHA-256 `f235af39a985de2e1ba14e9dae3dbaa112f83b20378b462881daf196b37a435d` (**byte-integrity verified at v1.6**: all 317,569 records re-validated from the committed bytes with exact big-integer arithmetic — zero failures, all `is_param` = 0 as labeled, full `u`-bucket decomposition summing exactly to 317,569; digests for both datasets also recorded in `verification_nano/SHA256SUMS`) |
| Manuscript | Git tag **`paper-v1.10`** (repository `pottertech/erdos-straus-conjecture`, branch `main`) |
| Independent mod-840 engine | `sweep_exact/third_party_independent_mod840.cpp` SHA-256 `3b5fafb47750c10fa8c19c7dc950be01b6a3c8c87043df039c523dace4163d40` (the seventh review's source, byte-faithful), archived output `third_party_mod840_output.txt` SHA-256 `6b419d9167e720414d8047ca0e7fc21ce9f401c1abe7c836c7cee89ea37134da`; re-executed by this repository: every statistic reproduced exactly (see §6.5) |

Reproduction (paths self-consistent per V14-05): `lake build ErdosStrausConjecture.FiniteSearch` (or simply `lake build`), then `lake env lean scripts/print_axioms.lean | python3 scripts/check_axioms_audit.py` (CI-enforced); for the sweep, `cc -O2 -std=c17 -fsanitize=undefined -fno-sanitize-recover=undefined sweep_exact/exact_span_sweep.c -o exact_span_sweep && ./exact_span_sweep 10000001 999999999 > rerun.json` (run from the repository root; `--selftest` runs the four pinning anchors plus the 1,326-case brute-force cross-check and must exit 0 under sanitization). The committed sweep artifacts are the byte-pinned outputs above. The review's retained independent implementation is committed at `sweep_exact/third_party_independent_sweep.cpp` (with `sweep_exact/bits/stdc++.h`, a libc++ shim — the reviewer's source itself is byte-faithful), SHA-256 `4ffeea9f144ef4fd16656dad9a016c7eee0e27b296b9a2c776f247427bddc70c`; the independent Rust proof-kernel verification record is `verification_nano/NANODA_RUN.md`.

**Axiom dependency audit (added 2026-11-21).** `#print axioms` on the principal results — run as `lake env lean scripts/print_axioms.lean` (Lean 4.30.0, Mathlib v4.30.0. The committed `verification_nano/lean_build.log` is regenerated by every release-gate run and reports `Build completed successfully (8481 jobs)` with 0 errors; earlier releases' builds report 8,477–8,480 jobs — the count is incidental, the gate's 0-error condition is the invariant):

| Result | `#print axioms` |
|---|---|
| `Reduction.scaling` | `propext` |
| `Reduction.mod8_of_12` | `propext`, `Classical.choice`, `Quot.sound` |
| `Reduction.prime_non24_isErdosStraus` | `propext`, `Classical.choice`, `Quot.sound` |
| `Reduction.full_conjecture_of_h24` | `propext`, `Classical.choice`, `Quot.sound` |
| `CenteredCriterion.u_method_core` | `propext`, `Classical.choice`, `Quot.sound` |
| `CenteredCriterion.u_method_witness` (the constructive wrapper) | `propext`, `Classical.choice`, `Quot.sound` |
| `MainTheorem.erdos_straus_except_residual_open_class` | `propext`, `Classical.choice`, `Quot.sound` |
| `MainTheorem.residue_classification` | `propext`, `Classical.choice`, `Quot.sound` |
| `CenteredEquivalence.theorem2` | `propext`, `Classical.choice`, `Quot.sound` |
| `FiniteSearch.witness_extraction` (added v1.3; row added v1.4 per review V13-02, confirmed by actual Lean execution and CI-gated) | `propext`, `Classical.choice`, `Quot.sound` |
| `FiniteSearch.finite_search_equivalence` (the composed Theorem 5.2 biconditional; added v1.5 per review V14-03, in the CI gate) | `propext`, `Classical.choice`, `Quot.sound` |
| `FiniteSearch.parametric_divisibility` (sixth review §4 forward: `T ∣ M ⟹ y ∣ z`) | `propext`, `Classical.choice`, `Quot.sound` |
| `FiniteSearch.parametric_divisibility_iff` (seventh review V16-01: the complete biconditional `T ∣ M ⟺ y ∣ z`) | `propext`, `Classical.choice`, `Quot.sound` |
| `FiniteSearch.h213_parametric_u3` (eighth review §5: `p ≡ 13 (mod 24) ⇒` parametric witness at `u = 3`, hence `F(p) = 3`) | `propext`, `Classical.choice`, `Quot.sound` |
| `FiniteSearch.param_exists_iff_onesided` (sixth review §4.1: parametric witness ⟺ `−1 ∈ 𝒟_u(M)`; constructive — no `Classical.choice`) | `propext`, `Quot.sound` |
| *Independent kernel check (Nanoda, strict mode)* | *the full exported principal-theorem closure re-checked by the independent Rust kernel under **strict axiom enforcement** (`unpermitted_axiom_hard_error: true`): **v1.8 — 13,093 declarations, zero errors, exit 0, 15 principal theorems** (export `95a175a2…6767`); the release gate now also records the tool-provenance manifest (`verification_nano/verification_provenance.json`: source commits, binary hashes, versions, UTC timestamp, the **proof-verification source revision** (the tree the verification ran against — v1.8's `a4077e6c…`, with the principal Lean sources byte-identical through the v1.9/v1.10 documentation releases per the tenth review's V19-03), the **publication release tag**, and export digests before/after) and asserts the export hash is unchanged across the check — lineage v1.5/v1.6/v1.7: 13,076 / 13,083 / 13,086 declarations (all strict, all exit 0) — `scripts/nanoda_gate.sh` end-to-end PASS; `verification_nano/NANODA_RUN.md` + evidence pack, `SHA256SUMS`, and provenance manifest committed* |

Every principal result depends only on `propext`, `Classical.choice`, and `Quot.sound` — the logical baseline present in essentially all Mathlib-based proofs — and on **none of the two documented project axioms** and **no `sorryAx`**: the axiom declarations of `Mod12Case1.lean` and `DivisorResidue.lean`, and the three census-enforced `sorry` goals of `OmegaCases.lean`, are outside the transitive dependency closure of everything used in §2–§5 (none of those modules is imported by the reduction chain). This makes the disclaimer's "no new axioms" a checked statement: a successful build and a zero-`sorry` census alone do not establish it, because they do not inspect proof-term dependencies; the command above does.

**Engineering note** (recorded because it shaped a proof, and it may recur): `omega` does not chain distinct moduli (the `12 → 24 → 8` step of Lemma 4.1), and when the context contains an unfolded `Nat.Prime` atom it can fail while reporting a counterexample in terms of `minFac`'s internal trial divisions. Both Lemma 4.1 and the composite descent therefore use explicit `Nat.div_add_mod`/`Nat.div_mul_cancel` steps, and arithmetic facts touching primality are established before the branch that introduces the primality atom.

**Verification gates** (all pass; CI runs on every push): `audit_all.sh` — Lean build; certificate verification of the committed dataset (166,011 records at 100%); dataset integrity (exact domain coverage, duplicate check); sorry census; axiom whitelist. `smoke_test.py` — the exact-criterion sweep (51 cross-checked pairs, 0 mismatches; first-success distribution `{3: 6, 7: 10, 11: 1}`, with `n = 1129` the unique `u = 11` case below 1200, pinned as the regression anchor).

**Reproduce:**

```bash
lake build ErdosStrausConjecture.Reduction          # the reduction, machine-checked
lake build ErdosStrausConjecture.CenteredCriterion
lake env lean scripts/print_axioms.lean             # axiom audit of the principal results
python3 analysis/layer4/verify_certificates.py       # 166,011-record re-verification
python3 scripts/smoke_test.py                        # n = 1129 regression
bash scripts/audit_all.sh                            # all gates
```

**Revision history.** v1.1–v1.10 revision notes, review-response records, and per-finding implementations live in `CHANGELOG.md` (extracted from this manuscript at v1.7 per the seventh review's editorial recommendation, and maintained thereafter). The version header records the current revision and date.

**Relation to the manuscript lineage.** The v11–v13 lineage (`docs/manuscript_v13.md`) carries the divisor-residue criterion and the structured-reduction frame; its current text was verified free of withdrawn claims during the 2026-11-19 honest-status audit, whose record is `CORRECTED_CLAIM_AUDIT.md` (that document lists and withdraws the superseded claims of the earlier papers — the `10^{21}` verification figure and the deterministic-coverage claims for `n ≡ 13 (mod 24)` and `n ≡ 49 (mod 120)`; none of them is used here). The present paper is the conditional-analysis layer on top of that base and is intended to be read alongside the v13 draft.

---

## References

1. N. C. Ankeny, *The least quadratic non residue*, Ann. of Math. (2) **55** (1952), 65–72.
2. D. A. Burgess, *On character sums and primitive roots*, Proc. London Math. Soc. (3) **12** (1962), 179–192.
3. M. J. Bright and D. Loughran, *Brauer–Manin obstruction for Erdős–Straus surfaces*, Bull. London Math. Soc. **52** (2020), no. 4, 746–761.
4. C. Elsholtz and T. Tao, *Counting the number of solutions to the Erdős–Straus equation on unit fractions*, J. Aust. Math. Soc. **94** (2013), 50–105.
5. R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Problem Books in Mathematics, Springer, New York, 2004.
6. K. K. Norton, *Numbers with small prime factors, and the least kth power non-residue*, Memoirs of the American Mathematical Society **106**, American Mathematical Society, Providence, RI, 1971.
7. L. J. Mordell, *Diophantine Equations*, Pure and Applied Mathematics **30**, Academic Press, London–New York, 1969.
8. S. E. Salez, *The Erdős-Straus conjecture: New modular equations and checking up to N = 10^{17}*, arXiv:1406.6307 (2014).
9. R. C. Vaughan, *On a problem of Erdős, Straus and Schinzel*, Mathematika **17** (1970), 193–198.
10. P. U. Mballa, *A unified parametric approach to the Erdős–Straus conjecture with explicit solutions for a set of integers of natural density one*, arXiv:2602.20036 (2026).
11. Spiridon Mihnea and Dumitru C. Bogdan, *Further verification and empirical evidence for the Erdős–Straus conjecture*, arXiv:2509.00128 (2025). (Computational verification reported through $10^{18}$; author order corrected per review V12-08 to match the arXiv metadata.)
12. E. J. Ionascu and A. Wilson, *On the Erdős–Straus conjecture*, Rev. Roumaine Math. Pures Appl. **56** (2011), no. 1, 21–30. (First-denominator bounds and exceptional-class tables; framework prior to this program's record discussions.)
13. T. Bloom and C. Elsholtz, *Egyptian fractions*, Nieuw Arch. Wisk. (5) **23** (2022), 237–244. (Survey; covering-system reformulation context.)

Repository-internal documents cited in place: `STATUS.md` (standing determination), `CORRECTED_CLAIM_AUDIT.md` (withdrawals), `CENTERED_PRODUCT_SET_THEOREM.md` (exact centered criterion), `DETERMINISTIC_CASCADE_STATUS.md`, `MOD31_EXACT_REDUCTION.md`, `MOD35_CRT_SPAN.md`, `FIRST_A_STRUCTURE.md`, `README.md`, `ROADMAP.md`, `LEAN_PROGRESS.md`, and the verifier/dataset files cited in Appendix A.

All bibliographic details in the numbered list were verified against publisher/library records or the arXiv metadata during the 2026-11-21 revision (replacing the informal works-consulted of v1, which per the repository's claim-discipline had deliberately deferred unverified journal details). Three further references (items 11–13) were added in the 2026-11-22 revision and re-verified against arXiv/library metadata on 2026-11-23, when the author order of item 11 was also corrected (V12-08).

---

*Author's note.* This paper is a working-research artifact of the `erdos-straus-conjecture` repository program, prepared as the companion handout to the v13 reviewer draft. Corrections are welcome and expected — that is the point of outside review.

---
