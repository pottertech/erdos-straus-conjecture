# Paper 2 — Residual Prime Structure and Opposite-Residue Reachability in the Erdős–Straus Conjecture

**Subtitle:** A Structural Investigation of the Classical Modulo-840 Residual Classes

**Author:** Brodie Foxworth
**Status:** open research (living manuscript — grows as results are established)
**Relationship to Paper 1:** Paper 1 (`ROUTE2_CONDITIONAL_REDUCTION.md`, frozen at
`paper-v1.12`) establishes the conditional reduction and the constructive
framework; this paper investigates whether that framework can resolve the
conjecture.

> **Standing banner.** The Erdős–Straus conjecture is open and is not proved by
> this program. Nothing in this manuscript states or implies otherwise.
> Computational results are reported as exactly that, with the bound named
> (`[10^7, 10^9)`). Computation never closes a universal claim.

## 1. Introduction

**Research objective.** For every prime `p ≡ 1 (mod 24)` (the residual class of
the hypothesis (H24) left open by Paper 1's reduction), establish the existence
of an admissible parameter

> `u ∈ {3, 7, …, 2p−3}`, `gcd(M, u) = 1`, `M = p(p+u)/4`,

such that the divisor-residue set

> `D_u(M) = { d mod u : d ∣ M }`

contains two opposite residues:

> **`D_u(M) ∩ (−D_u(M)) ≠ ∅`.**

The three established layers, inherited from Paper 1 (all machine-checked or
review-accepted there; see `THEOREM_REGISTRY.md`):

| Layer | Criterion | Meaning | Status |
| --- | --- | --- | --- |
| One-sided reachability | `−1 ∈ D_u(M)` | a parametric witness exists | machine-checked |
| Centered reachability | `D ∩ (−D) ≠ ∅` | an admissible divisor-span witness exists | accepted math; formalization pending (R4) |
| Erdős–Straus representation | `4/p = 1/x + 1/y + 1/z` | explicit constructive solution | machine-checked |

One-sided ⟹ centered; centered ⟹ representation (constructive). The open
problem is establishing the middle layer universally.

**Known sufficient condition.** `|D_u(M)| > φ(u)/2` implies the collision
(pigeonhole; `−D` is the image of `D` under a bijection of the unit group).
Neither universal reachability nor a universal cardinality guarantee has been
established. Empirically (Lane L1, Paper-1 release `7cb5360`), the pigeonhole
condition already concludes **99.49%** of first-working-parameter collisions
over the verified sweep population (3,177,642 of 3,194,231); the **delicate
class — collision present, `|D| ≤ φ(u)/2` — counts 16,589 primes (0.52%)** and
is the principal structural object of this paper.

## 2. Mathematical foundation

Inherited from Paper 1 without re-proof: the conditional reduction
(`Reduction.lean`), the constructive divisor criterion (`CenteredCriterion.lean`),
the finite-search equivalence (`FiniteSearch.lean`), the parametric
divisibility biconditional, the one-sided criterion, and the qualified Mordell
obstruction. Full registry: `THEOREM_REGISTRY.md`.

## 3. Residual prime classification

The classical mod-840 reduction restricts the unresolved prime classes to
`p ≡ 1, 121, 169, 289, 361, 529 (mod 840)`. Each class reduces mod 5
(`1, 1, 1, 4, 4, 4` respectively) — the two groups {1, 121, 361} and
{169, 289, 529} are separated by the prime's residue **mod 5** (`+1` vs `−1`),
which is the structure investigated in §5.

## 4. Computational research population

| Population | Size | Provenance |
| --- | --- | --- |
| Hard-case sweep `[10^7, 10^9)` | 3,194,231 | verified sweep (three independent engines agree) |
| (H24) hard cases | 2,364,031 | sweep artifact `h24_hard_cases` |
| Mod-840 hard cases | 795,913 | ninth-review engine, re-executed, byte-verified |
| Mod-840 nonparametric-only cohort | 22,222 | the focused starting cohort |
| Pigeonhole-conclusive (Lane L1) | 3,177,642 (99.49%) | `analysis/collision_v01/` |
| Delicate class | 16,589 (0.52%) | fingerprinted sample committed |

**Scope guard.** The 22,222-prime cohort is a research starting point, not the
complete unresolved domain: every cohort prime already has a valid
representation; the eventual universal proof addresses all residual primes.

## 5. Modulo-5 structural separation

The twelfth review's observation: nonparametric-only rates group by the
prime's residue modulo 5 — `p ≡ 1 (mod 5)` at 4.09% vs `p ≡ 4 (mod 5)` at
1.50% (2.73×). Registry entry: `HYPOTHESIS_REGISTRY.md` (H-1, status:
empirical association, mechanism open). R2 quantifies: delicate rates by
mod-5 group, first-working-parameter distributions by mod-5 group, and
candidate explanations.

## 6. Divisor-residue set growth

Cardinality and subgroup structure of `D_u(M)`; the margin distribution
`2|D| − φ(u)` (Lane L1 histogram) and lower bounds on `|D|` from the distinct
prime factors of `M`.

## 7. Opposite-residue collisions

Structural sufficient conditions beyond the cardinality bound; the delicate
class's small-residue collision mechanism.

## 8. Parameter-layer analysis

Exact structural classifications for individual parameter layers (the
`MOD31_EXACT_REDUCTION.md` pattern from Paper 1's repository).

## 9. Universal reachability

Candidate lemmas and remaining proof obligations for
`∀ p ≡ 1 (mod 24): ∃ u: D_u(M) ∩ (−D_u(M)) ≠ ∅`.

## 10. Lean formalization

New theorems land in `ErdosStrausConjecture/ResidualPrimes/` with the
Paper-1 audit discipline (0 `sorry`, axiom census, CI gate).

Established so far (R4/R5, `CollisionReachability.lean`; seven audited
results, axiom trio only): the pigeonhole sufficiency
`2|D_u(M)| > phi(u) ⟹ D ∩ (−D) ≠ ∅`, and the exact equivalences
`D ∩ (−D) ≠ ∅ ⟺ ∃ d₁ d₂ ∣ M, (d₁ + d₂) % u = 0 ⟺ −1 ∈ D·D⁻¹`. The review's
boxed criterion is machine-checked; the factorization-window form
(`∏ q^[−e, e]` = D·D⁻¹) remains the R4-lane extension.

## 11. Conclusion

Established results, conjectures, and open questions grow with the
`EXPERIMENT_LOG.md` record.

## Appendix

Data, algorithms, and reproducibility: `DATA_MANIFEST.md` (SHA-256 manifest,
re-runnable via `tests/verify_manifest.py`).
