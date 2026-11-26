# Paper 2 — Residual Prime Structure and Opposite-Residue Reachability in the Erdős–Straus Conjecture

**Subtitle:** A Structural Investigation of the Classical Modulo-840 Residual Classes

**Author:** Brodie Foxworth
**Status:** open research (living manuscript — grows as results are established)
**Version:** v1.7 (2026-11-25: the R8 layers E-011–E-020 incorporated)
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
condition already concludes **99.48%** of first-working-parameter collisions
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
(`1, 1, 4, 4, 1, 4` respectively) — the two groups {1, 121, 361} and
{169, 289, 529} are separated by the prime's residue **mod 5** (`+1` vs `−1`),
which is the structure investigated in §5.

## 4. Computational research population

| Population | Size | Provenance |
| --- | --- | --- |
| Hard-case sweep `[10^7, 10^9)` | 3,194,231 | verified sweep (three independent engines agree) |
| (H24) hard cases | 2,364,031 | sweep artifact `h24_hard_cases` |
| Mod-840 hard cases | 795,913 | ninth-review engine, re-executed, byte-verified |
| Mod-840 nonparametric-only cohort | 22,222 | the focused starting cohort |
| Pigeonhole-conclusive (Lane L1) | 3,177,642 (99.48%) | `analysis/collision_v01/` |
| Delicate class | 16,589 (0.52%) | fingerprinted sample committed |
| Delicate rescue census (E-011) | 16,589 / 16,589 pigeon-certified off-parameter (bound u ≤ 255) | `analysis/rescue_r8_v08/` |

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

**E-011 empirical base (2026-11-25).** Over the verified sweep [10^7, 10^9)
(3,194,231 hard-case primes, MISMATCH 0), the existential cardinality target
(∃ admissible `u` with `|D_u(M)| > φ(u)/2`) is certified for the ENTIRE
population at the bound `u ≤ 255`: 3,177,642 (99.49%) by the pigeon bound at
the first-working parameter, and each of the remaining 16,589 delicate
records by an off-parameter admissible pigeon site (`rescued_pigeon` =
16,589/16,589; zero no-pigeon records; 59 distinct site layers with a
nearest-layer concentration). The sweep-wide sub-first-working census
(3,042,449 span-failing admissible sites: zero collisions, zero pigeons)
verifies the chain pigeonhole ⟹ collision ⟹ centered span at population
scale. This is computational support for the target, not a universal proof;
the theorem attempt continues against the registry-tracked mechanisms
(`research/residual_primes/EXPERIMENT_LOG.md`, E-011).

**Exact one-layer classifications (R8, E-012–E-018).** Within a single
parameter layer the span criterion is now settled in both directions, with
the machine-checkable statement and the census that tests it kept strictly
apart.

*The u = 3 layer (E-012).* For `4·x = n + 3` with `n` prime: the constructive
side is that every even `x` with `3 ∤ x` spans at `T = 2` (the
`n ≡ 5 (mod 8)` family, Paper 1's unconditional `p ≡ 13 (mod 24)` class);
the exclusion side is that under the hard-case predicate on `x` (every prime
divisor `≡ 1 (mod 3)`, no exemption) no span candidate exists. The predicate
itself rules out `2 ∣ x` (it would force `2 ≡ 1 (mod 3)`), so under the
predicate the criterion never holds: the composed iff
(`u3_span_iff_even_of_hard`) is correct as stated, and its even side is
vacuous under the predicate — the two results must not be conflated.

*The u = 7 layer (E-013/E-016, the population split).* For
`4·x = n + 7`, `n ≡ 1 (mod 24)`: the residue classes `r7 ∈ {3, 5, 6}` of
`n` span outright (a four-residue certificate `{1, n, x, n·x}`, pairwise
distinct in each class). The remaining classes `r7 ∈ {1, 2, 4}` —
1,194,364 sweep records — split at a composition-level boundary that the
v0.14 census tests on the 5-free population: for the 795,913 records with
`5 ∤ x'` (381,652 span + 414,261 fail), the u = 7 span holds **exactly
when `x'` has an odd prime divisor with residue `3`, `5`, or `6 (mod 7)`**
(0-mismatch; per-class cells 259,654 / 260,036 / 276,223). The remaining
398,451 spanners carry `v₅(x') ≥ 1` and satisfy the same condition by
arithmetic — the prime `5` itself has residue `5 (mod 7)`, and no fail
record is 5-divisible — so the classification

> **for `p ≡ 1 (24)` at `r7 ∈ {1, 2, 4}`: the u = 7 span holds iff
> `x'` carries an odd prime divisor outside `{1, 2, 4} (mod 7)`**

covers all 1,194,364 records, census-tested on 795,913 of them.

*The mechanism (E-014/E-016/E-017, H-7).* The failing records are exactly
whose divisor-residue sets never leave the 2-orbit closure: the fail
D-sets are fixed shapes, `{1, 2}` (38,813 records, all at `v₂(x') = 1`)
and `{1, 2, 4}` (96,161 / 135,528 / 143,759 per class) — always inside
`{1, 2, 4}`, never a generator or 6; the depth-0 spanners of `r7 = 2/4`
carry *both* order-6 generators as divisor-residues (124,508/124,508 and
132,464/132,464, 0-miss). The 5-primality reading that the E-014 entry
first stated was falsified by the E-015 depth census (381,652 depth-0
spanners are 5-free) and is corrected in the log, not silently rewritten.
The u = 7 hard core — the 414,261 fail records, **17.52% of the (H24)
class** — is fully rescued off-parameter by the E-011 census (zero
no-pigeon records at any admissible `u' ≤ 255`).

*Independent validation (E-020, R9).* A standalone Pollard-rho +
Miller-Rabin reimplementation (no shared code with the C engines)
reproduces: (i) the census invariants, including the cross-artifact
equalities (the iff span cells = the E-016 depth-0 census 381,652; the fail
cells = E-014's 414,261); (ii) a 9,223-record re-derivation sweep whose
classification is, however, defined from the condition under test, so its
zero cells are structural — a consistency check, not independent evidence;
and (iii) the genuinely independent leg, a 2,400-record from-scratch
opposite-pair re-derivation from independently factored divisor sets
(1,200 spanners carry the centered pair, 1,200 failers do not: 2,400/2,400
in agreement).

## 10. Lean formalization

New theorems land in `ErdosStrausConjecture/ResidualPrimes/` with the
Paper-1 audit discipline (0 `sorry`, axiom census, CI gate).

Established so far (R4/R5, `CollisionReachability.lean`; seven audited
results, axiom trio only): the pigeonhole sufficiency
`2|D_u(M)| > phi(u) ⟹ D ∩ (−D) ≠ ∅`, and the exact equivalences
`D ∩ (−D) ≠ ∅ ⟺ ∃ d₁ d₂ ∣ M, (d₁ + d₂) % u = 0 ⟺ −1 ∈ D·D⁻¹`. The review's
boxed criterion is machine-checked; the factorization-window form
(`∏ q^[−e, e]` = D·D⁻¹) remains the R4-lane extension.

Machine-checked 2026-11-25 (R8, joint audited set 15 + 31 = 46, all
results on the axiom trio `[propext, Classical.choice, Quot.sound]`,
0 `sorry`):

| Module | Content | Result |
| --- | --- | --- |
| `ResidualPrimes.U3Boundary` (5 theorems) | the u = 3 layer: the constructive even-`x` span at `T = 2`, the predicate exclusion, the composed iff (its even side vacuous under the predicate) | E-012; comment-only edits reviewed in PR #32 |
| `ResidualPrimes.U7Layer` (13 theorems) | the u = 7 layer: the per-class span/pigeon theorems at `r7 = 3/5/6`, the three conditional 5-window spans, the 2-orbit closure lemma, and both directions of the composition-level iff (`u7_span_fails_of_orbit_primes`, `u7_pigeon_of_orbit_breaker` with the `{n, x, q, 2q}` four-residue pigeon) | E-013/E-015/E-019 |

The iff's machine-checked directions cover the failing classes under a
span-test hypothesis; the census statement above names the population each
direction was tested on.

## 11. Conclusion

Established results, conjectures, and open questions grow with the
`EXPERIMENT_LOG.md` record.

## Appendix

Data, algorithms, and reproducibility: `DATA_MANIFEST.md` (SHA-256 manifest,
re-runnable via `tests/verify_manifest.py`).
