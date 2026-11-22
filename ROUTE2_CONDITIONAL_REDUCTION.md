# The Erdős–Straus Conjecture Reduces to the Class of Primes Congruent to 1 modulo 24: An Explicit, Machine-Checked Conditional Reduction

**Version:** v1.1 (reviewer-facing draft; revised from the v1 mathematical review of 2026-11-21)  
**Date:** 2026-11-19 (v1) / 2026-11-21 (this revision)  
**Author:** Brodie Foxworth  
**Repository:** `pottertech/erdos-straus-conjecture`

> **Disclaimer.** This is not a proof of the Erdős–Straus conjecture and does not claim to be one. It proves a *reduction*: that the full conjecture follows, by an argument every step of which is both written out here and machine-verified in Lean 4 with no new axioms — the axiom dependency of the reduction's proof term is audited explicitly in Appendix A — from the single hypothesis **(H24)** — that every prime congruent to 1 modulo 24 has an Erdős–Straus representation. The hypothesis itself remains open; Section 6 states precisely what is and is not known about it.

---

## Abstract

We prove a conditional reduction for the Erdős–Straus conjecture. The reduction is elementary and complete: given the hypothesis (H24) that every prime `p ≡ 1 (mod 24)` admits positive integers `x, y, z` with `4/p = 1/x + 1/y + 1/z`, the conjecture holds for all `n ≥ 2`. The proof has two components of the formal reduction: (i) a scaling lemma showing that a solution for a prime factor lifts to all of its multiples — once (H24) and Theorem 4.2 supply representations for the primes, every composite inherits one — which removes the composite half of the resistant class from consideration entirely; and (ii) a mod-chain lemma showing that the certified 7-case partition of the conjecture, combined with the known prime case `n ≡ 5 (mod 8)`, leaves exactly the primes `≡ 1 (mod 24)` uncovered. Both components are formalized in Lean 4 with no new axioms — Appendix A audits the actual axiom dependency — and zero `sorry` declarations (`ErdosStrausConjecture.Reduction`); the companion constructive criterion (`CenteredCriterion`), which converts any span witness of the u-method into an explicit solution, is likewise fully formalized. We then analyze the remaining hypothesis (H24): its span-criterion translation, the constraints a covering argument must satisfy (the Mordell non-residue obstruction; the span-reachability obstacle documented for the layers `u = 31` and `u = 35`), the effectiveness available from classical least-quadratic-non-residue bounds (Burgess, Norton) and the GRH bound (Ankeny), and the empirical record — a verified certificate layer of 166,011 primes `≡ 1 (mod 12)` up to 10,000,000 (82,887 of them `≡ 1 (mod 24)`, the class (H24) concerns) in which the largest first-working parameter is `A = 107`.

---

## 1. Introduction

The Erdős–Straus conjecture states that for every integer `n ≥ 2`, there exist positive integers `x, y, z` such that

$$\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}.$$

Despite work since 1950 (Erdős, Mordell, Vaughan, Elsholtz–Tao, Salez, Bright–Loughran, Mballa), the conjecture remains open. The classical obstruction to identity-based attacks is the Mordell (1969) principle: a polynomial identity providing solutions for all `n ≡ r (mod m)` can exist only when `r` is a quadratic non-residue modulo `m`. Since 1 is a quadratic residue modulo every `m`, the class `n ≡ 1 (mod 12)` — which contains the resistant cases — cannot be finished by identity-hunting no matter how many moduli are classified.

The present paper sharpens *where* the conjecture's remaining content lives. Its starting point is the certified toolkit of the companion manuscript v13: the six modular identities covering every `n ≢ 1 (mod 12)` (together with `n ≡ 1 (mod 12)` with `5 ∣ n`), Theorem 2 covering the prime case `n ≡ 5 (mod 8)`, and a machine-verified case partition. We add:

- **The scaling lemma** (§3): a solution for `n` lifts to a solution for `n·k` for every `k ≥ 1`; consequently every composite inherits a solution from a prime factor provided that factor has one, and only prime residue classes can be intrinsically hard.
- **The mod-chain lemma** (§4): `n ≡ 1 (mod 12)` and `n ≢ 1 (mod 24)` force `n ≡ 5 (mod 8)` — so for primes, the certified Theorem 2 case (§2.3) meets the resistant class in exactly one residue, leaving `n ≡ 1 (mod 24)` as the sole uncovered prime class.
- **The conditional reduction** (§5): hence the full conjecture follows from (H24), the statement that every prime `≡ 1 (mod 24)` has a representation.

Everything in §2–§5 is machine-verified: the partition, the identities, the constructive criterion, the scaling lemma, the mod-chain lemma, and the reduction itself (the nine-module CI build set — `DivisorResidue`, `ClassicalIdentities`, `OmegaCases`, `CenteredEquivalence`, `MainTheorem`, `Theorem4`, `NewTheorems`, `CenteredCriterion`, `Reduction`; 0 `sorry` declarations in the new results; 2 documented axioms in the context modules). Section 6 is honest analysis, not theorem: it states what (H24) means, what the classical analytic results do and do not supply toward it, and what the verified computational record shows.

---

## 2. Notation and the certified toolkit

Throughout, `IsErdosStraus n` abbreviates: there exist positive integers `x, y, z` with `4·x·y·z = n·(x·y + x·z + y·z)`, i.e. `4/n = 1/x + 1/y + 1/z`.

The reduction assembles five components, all previously formalized and CI-enforced:

**2.1 The seven-case partition.** Every `n ≥ 2` falls into exactly one of seven residue cases: `n ≡ 0 (mod 3)`; `n ≡ 2 (mod 3)`; `n ≡ 4, 7, 10 (mod 12)`; `n ≡ 1 (mod 12)` with `5 ∣ n`; and `n ≡ 1 (mod 12)` with `5 ∤ n`. The first five are solved by the identities of §2.2, the sixth explicitly, and the seventh splits further. Machine-checked as `residue_classification` (`MainTheorem.lean`).

**2.2 The modular identities.** Each coverable case has an explicit two- or three-term representation; for example, for `n = 3k + 2`,

$$\frac{4}{n} = \frac{1}{n} + \frac{1}{k+1} + \frac{1}{n(k+1)},$$

verified by clearing denominators. All six cases (`mod_3_zero`, `mod_3_two`, `mod_12_four`, `mod_12_seven`, `mod_12_ten`, `mod_12_one_mod_5_zero`) are proven in Lean in `Identities.lean` — the module the case-partition theorems actually import.

**2.3 Theorem 2.** Every prime `n ≡ 5 (mod 8)` is covered by the parameter `A = 3` (`CenteredEquivalence.lean`, `theorem2`).

**2.4 The residual-class lemma.** The 7-case partition refines to: everything is covered except

$$C = \{n ≥ 13 :\; n ≡ 1 \pmod{12},\; 5 \nmid n,\; \neg(n \text{ prime} \wedge n ≡ 5 \pmod 8)\}.$$

This is `erdos_straus_except_residual_open_class` (`MainTheorem.lean`), the strongest existing honest coverage theorem of the program. Inside `C`, the elementary facts resolve the set further into the prime class `n ≡ 1 (mod 24)` and the composites `≡ 1 (mod 12)` with `5 ∤ n`.

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

1. The reduction also shows the *documented axiom's* class statement (`n ≡ 1 (mod 12), 5 ∤ n, n ≥ 13` assumed wholesale in the Lean development) is formally stronger than necessary: only its prime `≡ 1 (mod 24)` part is genuinely open, and the remaining content is machine-checked to follow from (H24).
2. Via §2.5, (H24) for a given prime `p` is *effective in form*: it suffices to exhibit, at any admissible `u`, a divisor `P` satisfying the span condition — the machine-checked wrapper then converts the span witness into an explicit solution. A future *proof* of (H24) by analytic means yields an effective solving procedure with explicit bounds only if it is effective as a covering argument — e.g. a theorem giving, for every admissible prime `p`, an admissible `u ≤ B(p)` together with a verifiable span witness. A nonconstructive existence argument (a pure density or counting proof) establishes (H24) without supplying any procedure; on its own it would not.

---

## 6. (H24): what is and is not known

This section is analysis, not theorem. It is included because (H24) is now, by Theorem 5.1, the precise remaining content of the conjecture.

**6.1 The span-criterion form.** For a prime `p ≡ 1 (mod 24)` and an admissible parameter `u ≡ 3 (mod 4)` with `p ∤ u`, put `M = p·(p+u)/4` (= `p·x`, so `gcd(M, u) = 1`: a common divisor of `x = (p+u)/4` and `u` divides `4x = p + u` and hence also `p`, and `p ∤ u`). By the one-divisor reduction (`CENTERED_PRODUCT_SET_THEOREM.md`; §2.5), the constructive criterion is equivalent to

$$\exists\, P \mid M^2 \;\;\text{with}\;\; P \equiv -M \;(\mathrm{mod}\ u) \qquad\Longleftrightarrow\qquad \exists\, P \mid M^2 \;\;\text{with}\;\; P\cdot M^{-1} \equiv -1 \;(\mathrm{mod}\ u).$$

Writing the prime factorization `M = ∏_{j=1}^{r} q_j^{e_j}`, the right-hand condition is the *span condition*: define the **centered product set** in the unit group `(ℤ/uℤ)×`,

$$\mathcal{S}_u(M) \;=\; \prod_{j=1}^{r}\,\bigl\{\,q_j^{-e_j},\; q_j^{-(e_j-1)},\; \ldots,\; q_j^{e_j-1},\; q_j^{e_j}\,\bigr\},$$

i.e. the set of all products `∏_j q_j^{t_j} (mod u)` with integer coefficients `t_j ∈ [−e_j, e_j]`. Then `u` succeeds for `(p, u)` iff `−1 ∈ 𝒮_u(M)`. The two divisor formulations match exactly: a divisor `P ∣ M²` has exponents `b_j ∈ [0, 2e_j]`, and putting `t_j = b_j − e_j` gives `P·M^{-1} = ∏_j q_j^{t_j}` — so multiplying the congruence `P ≡ −M (mod u)` by the unit `M^{-1}` (invertible because `gcd(M, u) = 1`) turns it into `P·M^{-1} ≡ −1 (mod u)`; conversely, any span witness `∏_j q_j^{t_j} ≡ −1 (mod u)` yields the divisor `P = ∏_j q_j^{t_j + e_j} ∣ M²` with `P ≡ −M (mod u)`. The permitted coefficient range is therefore exactly `[−e_j, e_j]`, matching the exponent window `[0, 2e_j]` of the divisors of `M²`.

**Cyclicity caveat (this subsection replaces the earlier single-generator formulation).** `(ℤ/uℤ)×` is a finite abelian group and is *not* cyclic in general; a discrete-logarithm phrasing to a single generator `g` is available only when the group happens to be cyclic — e.g. `(ℤ/35ℤ)× ≅ (ℤ/5ℤ)× × (ℤ/7ℤ)× ≅ C₄ × C₆` is noncyclic (it has no element of order 24). When `u` is an odd prime power — in particular every prime `u` (the prime-parameter layers `3, 7, 11, 19, 23, 31, 47, 59, 71, 79, 83, 103, 107, 127` of the repository's layer documents, and the composite prime power `u = 27 = 3³`) — `(ℤ/uℤ)×` is cyclic of order `φ(u)`: for a generator `g`, with `k_j = dlog_g(q_j mod u)` and `−1 = g^{φ(u)/2}`, the condition reads `∑_j k_j·t_j ≡ φ(u)/2 (mod φ(u))` for some `t_j ∈ [−e_j, e_j]` — a weighted subset-sum condition. In general, decompose `u = ∏_ℓ u_ℓ` into pairwise-coprime prime powers; by CRT, `(ℤ/uℤ)× ≅ ∏_ℓ (ℤ/u_ℓℤ)×`, and the condition is *coupled*: the same coefficients `t_j` must realize `−1` in every component simultaneously (since `−1 (mod u)` maps to `(−1, …, −1)` under the CRT isomorphism). `u = 35` is the worked example: the coupled condition in `(ℤ/5ℤ)× × (ℤ/7ℤ)×` is the correct formulation, and no single-generator version exists. The certificate dataset itself exercises the noncyclic case: 991 of its 166,011 records have a noncyclic first-working parameter `u ∈ {15, 35, 39, 51, 55}` (of 1,082 records whose first-working parameter is composite, the remainder is the cyclic prime power `u = 27`). The layer analyses `MOD31_EXACT_REDUCTION.md` and `MOD35_CRT_SPAN.md` document this condition exactly, with zero mismatch across the certified stages (at `u = 31`: 283 stage entrants, 0 span mismatches; at `u = 35`: the coupled condition in `(ℤ/5)× × (ℤ/7)×`, 93 entrants, 0 mismatches; a 2026-11-19 reconciliation, `FIRST_A_STRUCTURE.md`, recomputed the stage chains with the full admissible layer set — the documented chain omitted `u = 19` and `u = 27`, and the true residual-class stages are 217 solvable-152 at `u = 31` and 65 solvable-17 at `u = 35`, terminating identically).

**6.2 What least-non-residue bounds give.** The classical effective inputs are:

- *Burgess (1962) via Norton (1971):* the least prime quadratic non-residue `q` modulo `p` satisfies `q ≪ p^{1/(4√e) + ε}` for every `ε > 0`.
- *Ankeny (1952), under GRH:* the least non-residue is `O((log p)²)`.

These guarantee that a *non-residue* arrives fast. Obtaining a non-residue in a *prescribed residue class* is a strictly stronger demand and would need its own effective input — e.g. a GRH-conditional Ankeny-type bound for the least prime in a prescribed coset of `(ℤ/uℤ)×`, or uniform Burgess-type character-sum estimates over that coset; no unconditional theorem of that strength is claimed or used here. These results also do **not** address the actual requirement of (H24): the non-residue's discrete logarithm must land in a specific coset determined by the forced factors' span — a *reachability* condition, not an existence condition. The `u = 31` analysis makes the distinction concrete: 33 of the 93 failures to that layer's target are span-delicate for reasons unrelated to non-residue existence, and the cube-class rescue structure, while characterizable, is not a consequence of Burgess-type bounds.

**6.3 The covering-theorem gap.** No theorem of the shape "for every prime `p ≡ 1 (mod 24)` some admissible `u` succeeds with `u ≤ B(p)`" is known. The verified cascade handles layer after layer of moduli, but there is no termination argument over the full residual class. The instructive case in the data, `p = 8,803,369`, was settled by computation (first working `A = 107`), not by a covering argument.

**6.4 The Mordell constraint on identity-hunting.** By the Mordell (1969) principle — the framework being *polynomial identities*: parametric solutions `4/n = 1/x(n) + 1/y(n) + 1/z(n)` with `x(n), y(n), z(n)` polynomials in `n` (rational, in particular integer, coefficients), required to give solutions for **every** integer `n` in an entire residue class `n ≡ r (mod m)` — no such identity exists for a class whose representative is a quadratic residue modulo `m` (i.e. whenever the congruence `x² ≡ r (mod m)` is solvable). The obstruction is uniform: no polynomial identity, and hence no finite system of identities, can cover the `≡ 1`-classes, because `1` is a quadratic residue modulo every modulus. The route to (H24) therefore cannot finish purely by extending the identity table; it must reach the span/reachability structure of §6.1, or supply a genuinely different mechanism.

**6.5 The empirical record.** Two computational layers support the expectation that (H24) holds with tiny parameters; as of the 2026-11-21 revision their methods and exact scopes are stated below, and the hard-case-sweep artifact class was re-attributed and then resolved by a corrected re-run the same day:

- the certificate layer `results/layer4_certificates.jsonl`: **166,011 records**, each carrying a full divisor-certificate (`n, A, x, y, z, P, Q, T, N`) re-verified field-by-field — divisor relations, congruences, positivity, and the unit-fraction identity — by the CI-gated verifier `analysis/layer4/verify_certificates.py`, with record count, duplicates, exact domain coverage, and max `A` checked by the independent checker `analysis/layer4/check_certificate_dataset.py`. The dataset's domain — the sense of *admissible* in the layer-4 tooling — is exactly: `p` prime, `13 ≤ p ≤ 10,000,000`, `p ≡ 1 (mod 12)`. That domain decomposes into **82,887 primes `≡ 1 (mod 24)`** — the class (H24) is about — and **83,124 primes `≡ 13 (mod 24)`**, which are already covered unconditionally by Theorem 2 (primes `≡ 5 (mod 8)`); the layer is thus a strict superset of (H24)'s domain, and the (H24)-exact figure is the 82,887-record subclass. Within the layer, the largest first-working `A` = **107** (record `8,803,369`, which is prime and `≡ 1 (mod 24)`); every record's parameter `A` is an admissible `u` (odd, `≡ 3 (mod 4)`, with `gcd(n·x, u) = 1`), and each record's witness is verified independently of the search that located it.
- hard-case sweeps toward `10^9` — **resolved by the corrected exact-criterion re-run of 2026-11-21** (`sweep_exact/`). The previously cited artifacts are retired: `verification_100M_1B.json` was produced by the superseded three-target shortcut (pre-2026-08-28), and even the exact-criterion `verification_10M_1B.json` carries a verifier defect — its `factor_x` trials odd primes only (no `2`), corrupting the divisor enumeration precisely for even `x`; since `n ≡ 13 (mod 24)` forces `x` even at every admissible `u`, that bug strikes exactly the `13 (mod 24)` half of the population, and its recorded **7 "no-solution" cases are disproven by explicit witnesses** (all resolve within `u ≤ 251`, first `u ∈ {3, 31, 71, 151}` — `sweep_exact/seven_case_witnesses.json`; three of them resolve at `u = 3`). The corrected re-run (`sweep_exact/exact_span_sweep.c`, predicates mirrored 1:1 from the committed verifiers, self-tested by an independent brute-force enumeration on 1,326 cases with 0 mismatches plus the pinned `n = 1129 → u = 11` anchor) reproduces the committed populations **exactly** — 3,194,231 prime hard cases in `[10^7, 10^9)` (the `verify_10M_to_1B` family) and 2,850,823 in `[10^8, 10^9)` (the sum of the `corrected.py` family's two sub-range artifacts, 345,956 + 2,504,867) — and finds **0 failures at `u ≤ 251` in both**, with largest first-working `u = 227` (at `n = 32,349,601`), `u = 167` on the `[10^8, 10^9)` slice, and — with the capture cap removed (`sweep_dump_nonparametric.c`, `nonparametric_1e7_1e9.jsonl`) — **327,504 non-parametric first-hits (10.25% of the cohort; 15.5% of the ≤10^7 hard cohort; the identity-shaped families gain share as the range grows)**, concentrated at the small layers (72% at `u = 7`) and on the `v₂(x) ≥ 2` slices (`n ≡ 1, 49 (mod 96): 86%` of the tail); the tail's witnesses are genuinely asymmetric (no small closed family by direct probes — `z mod y` distinct across the cohort, `gcd(y, z)` large) and are the working domain of the span machinery of `FIRST_A_STRUCTURE.md`. The corrected first-worked distribution is led by `u = 3: 830,200` and `u = 7: 1,949,770` (87.0% at `u ≤ 7`; artifacts `verification_10M_1B_exact_rerun.json`, `verification_100M_1B_exact_rerun.json`). The retired files' competing claims — "2,852,233 hard cases with largest first-working `A = 151`" and the 21.3% non-parametric share — are likewise enumeration artifacts of the defective verifier (the latter shared with the next re-run's own capture cap, corrected here).

No counterexample to (H24) is known. Two cautionary notes keep the record honest: this repository's own exact-criterion exhaustive verification is the certificate layer to `10^7` together with the corrected `10^9` hard-case sweeps (§6.5), while the literature's exhaustive record is the `~10^{18}` range; and the earlier `10^{21}`-type claims in this repository were withdrawn in `CORRECTED_CLAIM_AUDIT.md` and are **not** relied upon anywhere in this paper. Computation cannot close a universal claim, and nothing in §6.1–6.4 stands in for the missing theorem.

---

## 7. Conclusion

The Erdős–Straus conjecture is equivalent, in effective strength, to the single statement (H24) about primes `≡ 1 (mod 24)`. One direction is trivial; the other is Theorem 5.1, whose proof is elementary, complete, and machine-checked with no new axioms. The reduction has practical value: it eliminates the composite half of the resistant class with no casework (scaling, §3); it shows the certified partition meets the resistant class in exactly one prime residue (§4); and it converts any future analytic progress toward (H24) — a covering theorem over the span classes of §6.1, or a GRH-conditional span-reachability result — immediately into solutions, because the criterion-to-solution direction is constructive and formalized (§2.5).

The conjecture is not proved, here or in the literature; (H24) is open, and the honest open problem it poses is: *prove a reachability theorem for the span condition of §6.1, or exhibit a covering bound `B(p)`*. This is a sharper target than the conjecture itself, because every surrounding combinatorial ingredient is now either certified or reduced away.

---

## Appendix A. Provenance and reproducibility

**Lean formalization.** Lean 4.30.0 with Mathlib v4.30.0 (pinned, CI-enforced). The components of this paper:

| Component | Module | Status |
|---|---|---|
| Scaling lemma (`scaling`) | `Reduction.lean` | proven, 0 `sorry` |
| Mod-chain lemma (`mod8_of_12`) | `Reduction.lean` | proven, 0 `sorry` |
| Unconditional prime coverage (`prime_non24_isErdosStraus`) | `Reduction.lean` | proven, 0 `sorry` |
| Conditional reduction (`full_conjecture_of_h24`) | `Reduction.lean` | proven, 0 `sorry` |
| Constructive criterion (`u_method_core` + wrapper) | `CenteredCriterion.lean` | proven, 0 `sorry` |

Certified context modules: `DivisorResidue`, `ClassicalIdentities`, `OmegaCases`, `CenteredEquivalence`, `MainTheorem`, `Theorem4`, `NewTheorems` — together with `CenteredCriterion` and `Reduction`, the nine-module CI build set. Remaining unfinished goals in the root project: 3, census-enforced (all in `OmegaCases.lean`). Documented axioms: 2 — `erdos_straus_mod_12_1_not_div_5_conjecture` (whose content Theorem 5.1 shows follows from (H24)) and `divisor_residue_criterion_reverse`.

**Axiom dependency audit (added 2026-11-21).** `#print axioms` on the principal results — run as `lake env lean scripts/print_axioms.lean` (Lean 4.30.0, Mathlib v4.30.0; project build: 8,480 jobs, 0 errors):

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

Repository-internal documents cited in place: `STATUS.md` (standing determination), `CORRECTED_CLAIM_AUDIT.md` (withdrawals), `CENTERED_PRODUCT_SET_THEOREM.md` (exact centered criterion), `DETERMINISTIC_CASCADE_STATUS.md`, `MOD31_EXACT_REDUCTION.md`, `MOD35_CRT_SPAN.md`, `FIRST_A_STRUCTURE.md`, `README.md`, `ROADMAP.md`, `LEAN_PROGRESS.md`, and the verifier/dataset files cited in Appendix A.

All bibliographic details in the numbered list were verified against publisher/library records or the arXiv metadata during the 2026-11-21 revision (replacing the informal works-consulted of v1, which per the repository's claim-discipline had deliberately deferred unverified journal details).

---

*Author's note.* This paper is a working-research artifact of the `erdos-straus-conjecture` repository program, prepared as the companion handout to the v13 reviewer draft. Corrections are welcome and expected — that is the point of outside review.

---

**Revision note (v1.1, 2026-11-21).** This revision applies the corrections from the external mathematical review of the v1 draft (2026-11-21), plus one new finding made while applying them:

1. (Review, §6.1) The span-criterion exposition no longer assumes `(ℤ/uℤ)×` is cyclic: the finite-abelian formulation is primary, the single-generator discrete-log phrasing is restricted to the genuinely cyclic case (odd prime powers), the noncyclic case is handled by the coupled CRT decomposition (with `u = 35` as the worked example), and the dataset's noncyclic-`u` records are cited.
2. (Review, §6.1) The equivalence between the divisor form `P ≡ −M (mod u)` and the span form `P·M^{-1} ≡ −1 (mod u)` is now stated explicitly, with the exact coefficient window `[−e_j, e_j]` (and hence exponent window `[0, 2e_j]` for divisors of `M²`) and the role of `gcd(M, u) = 1` (proved for the (H24) case from `p ∤ u`).
3. (Review, Theorem 4.2) The first proof case no longer lists `1 (mod 12)` among the possible prime residues under `n ≢ 1 (mod 12)`.
4. (Review, §5, Remark 2) Effectiveness of a future proof of (H24) is now qualified: only an effective covering argument yields a solving procedure; a nonconstructive existence proof does not.
5. (Review, §6.2) The "prescribed residue class" claim is qualified with the additional effective input it requires (GRH-conditional Ankeny-type coset bounds or uniform Burgess coset estimates).
6. (Review, §6.4) The Mordell obstruction is stated in its precise identity framework (polynomial parametric solutions valid on an entire residue class), and the reference is corrected to 1969 (the book's actual publication year; v1 said 1967).
7. (Review, §6.5) The certificate dataset's "admissible" domain is now defined exactly, with its residue decomposition: 82,887 primes `≡ 1 (mod 24)` (the (H24) class) + 83,124 primes `≡ 13 (mod 24)`, summing to the 166,011 records. The two verification layers' independent methods are identified.
8. (New, found during item 7) The `10^9` hard-case-sweep claims were re-attributed and then resolved the same day: the cited artifact (`verification_100M_1B.json`) predates the 2026-08-28 exact-criterion fix (three-target targets), and the exact-criterion `verification_10M_1B.json` itself carries a missing-`2` factorization bug in `factor_x` — its 7 recorded no-solution cases are disproven by explicit witnesses under the exact criterion, and the corrected re-run (`sweep_exact/exact_span_sweep.c`) reproduces the committed populations exactly and finds **0 failures at `u ≤ 251`** on `[10^7, 10^9)` (largest first-working `u = 227`). Details in §6.5 and `sweep_exact/README.md`.
9. (Review, Appendix A / disclaimer) A Lean axiom dependency audit for the principal theorems is now recorded via `#print axioms` (`scripts/print_axioms.lean`); the abstract and disclaimer point to it.
10. (Review, editorial) "0 `sorry`s" → "0 `sorry` declarations" (2 places); "theorem-2" → "Theorem 2"; the composite-inheritance statement carries the "provided that prime factor has a solution" proviso; the `omega` remark reads "may fail on goals involving unfolded primality definitions"; the `(H24)'s` possessive was removed by rephrasing; the complete nine-module CI build set is named inline in §1; and the v1 informal works-consulted is replaced by verified formal references (above). A cross-reference error found during the pass was also fixed: the six identities used by the case partition live in `Identities.lean` (not `ClassicalIdentities.lean`, which contains a different, not-yet-imported identity set).
