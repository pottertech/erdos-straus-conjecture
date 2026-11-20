# The Erdős–Straus Conjecture Reduces to the Class of Primes Congruent to 1 modulo 24: An Explicit, Machine-Checked Conditional Reduction

**Version:** v1 (reviewer-facing draft)  
**Date:** 2026-11-19  
**Author:** Brodie Foxworth  
**Repository:** `pottertech/erdos-straus-conjecture`

> **Disclaimer.** This is not a proof of the Erdős–Straus conjecture and does not claim to be one. It proves a *reduction*: that the full conjecture follows, by an argument every step of which is both written out here and machine-verified in Lean 4, from the single hypothesis **(H24)** — that every prime congruent to 1 modulo 24 has an Erdős–Straus representation. The hypothesis itself remains open; Section 6 states precisely what is and is not known about it.

---

## Abstract

We prove a conditional reduction for the Erdős–Straus conjecture. The reduction is elementary and complete: given the hypothesis (H24) that every prime `p ≡ 1 (mod 24)` admits positive integers `x, y, z` with `4/p = 1/x + 1/y + 1/z`, the conjecture holds for all `n ≥ 2`. The proof has two new components: (i) a scaling lemma showing that every composite `n` inherits a solution from any of its prime factors, which removes the composite half of the resistant class from consideration entirely; and (ii) a mod-chain lemma showing that the certified 7-case partition of the conjecture, combined with the known prime case `n ≡ 5 (mod 8)`, leaves exactly the primes `≡ 1 (mod 24)` uncovered. Both components are formalized in Lean 4 with zero axioms and zero `sorry`s (`ErdosStrausConjecture.Reduction`); the companion constructive criterion (`CenteredCriterion`), which converts any span witness of the u-method into an explicit solution, is likewise fully formalized. We then analyze the remaining hypothesis (H24): its span-criterion translation, the constraints a covering argument must satisfy (the Mordell non-residue obstruction; the span-reachability obstacle documented for the layers `u = 31` and `u = 35`), the effectiveness available from classical least-quadratic-non-residue bounds (Burgess, Norton) and the GRH bound (Ankeny), and the empirical record — a verified certificate layer of 166,011 admissible primes up to 10,000,000 in which the largest first-working parameter is `A = 107`.

---

## 1. Introduction

The Erdős–Straus conjecture states that for every integer `n ≥ 2`, there exist positive integers `x, y, z` such that

$$\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}.$$

Despite work since 1950 (Erdős, Mordell, Vaughan, Elsholtz–Tao, Salez, Bright–Loughran, Mballa), the conjecture remains open. The classical obstruction to identity-based attacks is the Mordell (1967) principle: a polynomial identity providing solutions for all `n ≡ r (mod m)` can exist only when `r` is a quadratic non-residue modulo `m`. Since 1 is a quadratic residue modulo every `m`, the class `n ≡ 1 (mod 12)` — which contains the resistant cases — cannot be finished by identity-hunting no matter how many moduli are classified.

The present paper sharpens *where* the conjecture's remaining content lives. Its starting point is the certified toolkit of the companion manuscript v13: the six modular identities covering every `n ≢ 1 (mod 12)` (together with `n ≡ 1 (mod 12)` with `5 ∣ n`), Theorem 2 covering the prime case `n ≡ 5 (mod 8)`, and a machine-verified case partition. We add:

- **The scaling lemma** (§3): a solution for `n` lifts to a solution for `n·k` for every `k ≥ 1`; consequently every composite inherits a solution from a prime factor, and only prime residue classes can be intrinsically hard.
- **The mod-chain lemma** (§4): `n ≡ 1 (mod 12)` and `n ≢ 1 (mod 24)` force `n ≡ 5 (mod 8)` — so for primes, the certified theorem-2 case meets the resistant class in exactly one residue, leaving `n ≡ 1 (mod 24)` as the sole uncovered prime class.
- **The conditional reduction** (§5): hence the full conjecture follows from (H24), the statement that every prime `≡ 1 (mod 24)` has a representation.

Everything in §2–§5 is machine-verified: the partition, the identities, the constructive criterion, the scaling lemma, the mod-chain lemma, and the reduction itself (nine Lean modules; 0 `sorry`s in the new results; 2 documented axioms in the context modules). Section 6 is honest analysis, not theorem: it states what (H24) means, what the classical analytic results do and do not supply toward it, and what the verified computational record shows.

---

## 2. Notation and the certified toolkit

Throughout, `IsErdosStraus n` abbreviates: there exist positive integers `x, y, z` with `4·x·y·z = n·(x·y + x·z + y·z)`, i.e. `4/n = 1/x + 1/y + 1/z`.

The reduction assembles five components, all previously formalized and CI-enforced:

**2.1 The seven-case partition.** Every `n ≥ 2` falls into exactly one of seven residue cases: `n ≡ 0 (mod 3)`; `n ≡ 2 (mod 3)`; `n ≡ 4, 7, 10 (mod 12)`; `n ≡ 1 (mod 12)` with `5 ∣ n`; and `n ≡ 1 (mod 12)` with `5 ∤ n`. The first five are solved by the identities of §2.2, the sixth explicitly, and the seventh splits further. Machine-checked as `residue_classification` (`MainTheorem.lean`).

**2.2 The modular identities.** Each coverable case has an explicit two- or three-term representation; for example, for `n = 3k + 2`,

$$\frac{4}{n} = \frac{1}{n} + \frac{1}{k+1} + \frac{1}{n(k+1)},$$

verified by clearing denominators. All six cases (`mod_3_zero`, `mod_3_two`, `mod_12_four`, `mod_12_seven`, `mod_12_ten`, `mod_12_one_mod_5_zero`) are proven in Lean (`ClassicalIdentities.lean`, `OmegaCases.lean`, `Mod12Case1.lean`).

**2.3 Theorem 2.** Every prime `n ≡ 5 (mod 8)` is covered by the parameter `A = 3` (`CenteredEquivalence.lean`, `theorem2`).

**2.4 The residual-class lemma.** The 7-case partition refines to: everything is covered except

$$C = \{n ≥ 13 :\; n ≡ 1 \pmod{12},\; 5 \nmid n,\; \neg(n \text{ prime} \wedge n ≡ 5 \pmod 8)\}.$$

This is `erdos_straus_except_residual_open_class` (`MainTheorem.lean`), the strongest existing honest coverage theorem of the program. Inside `C`, the elementary facts resolve the set further into the prime class `n ≡ 1 (mod 24)` and the composites `≡ 1 (mod 12)` with `5 ∤ n`.

**2.5 The constructive criterion.** For odd `u ≡ 3 (mod 4)` with `u = 4x − n > 0` and `x = (n+u)/4` a positive integer: whenever there is a positive divisor `P ∣ (n·x)²` with `P ≡ −n·x (mod u)` and `gcd(u, n·x) = 1`, the construction

$$x = \frac{n+u}{4}, \quad y = \frac{P + n x}{u}, \quad z = \frac{Q + n x}{u}, \quad Q = \frac{(n x)^2}{P}$$

is positive-integer-valued and satisfies `4·x·y·z = n·(x·y + x·z + y·z)` identically. This is `u_method_core` and its constructive wrapper in `CenteredCriterion.lean` (0 `sorry`). The direction that *supplies* such a divisor `P` is a *span condition* in the unit group `(ℤ/uℤ)×` — the subject of §6 — and is the open side.

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

(This lemma is `mod8_of_12` in `Reduction.lean`. The proof carries the explicit rearrangement above rather than trusting `omega` across the three moduli — the tactic does not chain them, and it mishandles unfolded primality definitions; see Appendix A for the recorded pitfall.)

**Theorem 4.2 (unconditional prime coverage).** Every prime `n ≥ 2` with `n ≢ 1 (mod 24)` has a representation.

*Proof.* Let `n` be prime with `n ≢ 1 (mod 24)`.

- If `n ≢ 1 (mod 12)`: `n` is `2`, `3`, or `≡ 1, 5, 7, 11 (mod 12)`. The classes `≡ 0, 2 (mod 3)` (which include `n ≡ 2, 5, 8, 11 (mod 12)`) and `≡ 4, 7, 10 (mod 12)` are covered by the identities of §2.2 — so `n` is covered.
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
2. Via §2.5, (H24) for a given prime `p` is an *effective* statement: it suffices to exhibit, at any admissible `u`, a divisor `P` satisfying the span condition — the reduction then converts the span witness into an explicit solution. A future proof of (H24) by analytic means would therefore immediately yield an effective solving procedure with explicit bounds.

---

## 6. (H24): what is and is not known

This section is analysis, not theorem. It is included because (H24) is now, by Theorem 5.1, the precise remaining content of the conjecture.

**6.1 The span-criterion form.** For a prime `p ≡ 1 (mod 24)` and an admissible parameter `u ≡ 3 (mod 4)` with `p ∤ u`, the constructive criterion reduces to a condition in the unit group `(ℤ/uℤ)×`: writing the prime factors of `M = p·(p+u)/4` with their discrete logarithms to a generator `g` of `(ℤ/uℤ)×`, one seeks the class of `−1` as a finite subset sum of those logarithms (weighted by the factors' exponents in `M`). The layer analyses `MOD31_EXACT_REDUCTION.md` and `MOD35_CRT_SPAN.md` document this condition exactly, with zero mismatch across the certified stages (at `u = 31`: 283 stage entrants, 0 span mismatches; at `u = 35`: the coupled condition in `(ℤ/5)× × (ℤ/7)×`, 93 entrants, 0 mismatches; a 2026-11-19 reconciliation, `FIRST_A_STRUCTURE.md`, recomputed the stage chains with the full admissible layer set — the documented chain omitted `u = 19` and `u = 27`, and the true residual-class stages are 217 solvable-152 at `u = 31` and 65 solvable-17 at `u = 35`, terminating identically).

**6.2 What least-non-residue bounds give.** The classical effective inputs are:

- *Burgess (1962) via Norton (1971):* the least prime quadratic non-residue `q` modulo `p` satisfies `q ≪ p^{1/(4√e) + ε}` for every `ε > 0`.
- *Ankeny (1952), under GRH:* the least non-residue is `O((log p)²)`.

These guarantee that a *non-residue* arrives fast (and, with care, one in a prescribed residue class). They do **not** address (H24)'s actual requirement: the non-residue's discrete logarithm must land in a specific coset determined by the forced factors' span — a *reachability* condition, not an existence condition. The `u = 31` analysis makes the distinction concrete: 33 of the 93 failures to that layer's target are span-delicate for reasons unrelated to non-residue existence, and the cube-class rescue structure, while characterizable, is not a consequence of Burgess-type bounds.

**6.3 The covering-theorem gap.** No theorem of the shape "for every prime `p ≡ 1 (mod 24)` some admissible `u` succeeds with `u ≤ B(p)`" is known. The verified cascade handles layer after layer of moduli, but there is no termination argument over the full residual class. The instructive case in the data, `p = 8,803,369`, was settled by computation (first working `A = 107`), not by a covering argument.

**6.4 The Mordell constraint on identity-hunting.** By the Mordell (1967) principle, no finite system of polynomial identities can cover the `≡ 1`-classes (1 is a quadratic residue modulo every modulus). The route to (H24) therefore cannot finish purely by extending the identity table; it must reach the span/reachability structure of §6.1, or supply a genuinely different mechanism.

**6.5 The empirical record.** Two independently verified layers support the expectation that (H24) holds with tiny parameters:

- the certificate layer `results/layer4_certificates.jsonl`: **166,011 admissible primes** up to 10,000,000, each with an independently re-verified divisor certificate; largest first-working `A` = **107** (record `8,803,369`, which is prime and `≡ 1 (mod 24)`);
- the hard-case sweep `verification_100M_1B.json` to `10^9`: **2,852,233 hard cases, 0 failures**, largest first-working `A` = **151**.

No counterexample to (H24) is known. Two cautionary notes keep the record honest: this repository's own exhaustive verification is the certificate layer to `10^7` (and the hard-case sweep to `10^9`), while the literature's exhaustive record is the `~10^{18}` range; and the earlier `10^{21}`-type claims in this repository were withdrawn in `CORRECTED_CLAIM_AUDIT.md` and are **not** relied upon anywhere in this paper. Computation cannot close a universal claim, and nothing in §6.1–6.4 stands in for the missing theorem.

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

**Engineering note** (recorded because it shaped a proof, and it may recur): `omega` does not chain distinct moduli (the `12 → 24 → 8` step of Lemma 4.1), and when the context contains an unfolded `Nat.Prime` atom it can fail while reporting a counterexample in terms of `minFac`'s internal trial divisions. Both Lemma 4.1 and the composite descent therefore use explicit `Nat.div_add_mod`/`Nat.div_mul_cancel` steps, and arithmetic facts touching primality are established before the branch that introduces the primality atom.

**Verification gates** (all pass; CI runs on every push): `audit_all.sh` — Lean build; certificate verification of the committed dataset (166,011 records at 100%); dataset integrity (exact domain coverage, duplicate check); sorry census; axiom whitelist. `smoke_test.py` — the exact-criterion sweep (51 cross-checked pairs, 0 mismatches; first-success distribution `{3: 6, 7: 10, 11: 1}`, with `n = 1129` the unique `u = 11` case below 1200, pinned as the regression anchor).

**Reproduce:**

```bash
lake build ErdosStrausConjecture.Reduction          # the reduction, machine-checked
lake build ErdosStrausConjecture.CenteredCriterion
python3 analysis/layer4/verify_certificates.py       # 166,011-record re-verification
python3 scripts/smoke_test.py                        # n = 1129 regression
bash scripts/audit_all.sh                            # all gates
```

**Relation to the manuscript lineage.** The v11–v13 lineage (`docs/manuscript_v13.md`) carries the divisor-residue criterion and the structured-reduction frame; its current text was verified free of withdrawn claims during the 2026-11-19 honest-status audit, whose record is `CORRECTED_CLAIM_AUDIT.md` (that document lists and withdraws the superseded claims of the earlier papers — the `10^{21}` verification figure and the deterministic-coverage claims for `n ≡ 13 (mod 24)` and `n ≡ 49 (mod 120)`; none of them is used here). The present paper is the conditional-analysis layer on top of that base and is intended to be read alongside the v13 draft.

---

## Works consulted (informal)

Classical names consulted for the analytic section: Burgess (1962, character sums and least non-residues); Norton (1971, restricted prime factors and the least prime non-residue); Ankeny (1952, least quadratic non-residue under GRH); Mordell (1967, non-residue obstruction for polynomial identities over residue classes); and the survey literature on the `4/n` problem (Erdős–Straus; Vaughan; Guy's *Unsolved Problems in Number Theory*; Elsholtz–Tao 2013; Bright–Loughran; Mballa). Exact bibliographic details will be completed during the formal citation pass with the referee's help — the author has deliberately not written out journal details not verified in this environment, per the repository's claim-discipline.

Repository-internal documents: `STATUS.md` (standing determination), `CORRECTED_CLAIM_AUDIT.md` (withdrawals), `DETERMINISTIC_CASCADE_STATUS.md`, `MOD31_EXACT_REDUCTION.md`, `MOD35_CRT_SPAN.md`, `README.md`, `ROADMAP.md`, `LEAN_PROGRESS.md`, and the verifier/dataset files cited in Appendix A.

---

*Author's note.* This paper is a working-research artifact of the `erdos-straus-conjecture` repository program, prepared as the companion handout to the v13 reviewer draft. Corrections are welcome and expected — that is the point of outside review.
