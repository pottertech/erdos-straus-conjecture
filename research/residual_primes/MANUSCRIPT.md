# Paper 2 — Residual Prime Structure and Opposite-Residue Reachability in the Erdős–Straus Conjecture

**Subtitle:** A Structural Investigation of the Classical Modulo-840 Residual Classes

**Author:** Brodie Foxworth
**Status:** open research (living manuscript — grows as results are established)
**Version:** v1.22 (2026-11-28: the E-072 chain correction — the corrected sweep-wide chain through u = 83)
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
| u = 11 3-fate census (E-024) | 1,949,770 fw=7 / 279,515 fw=11 / 134,746 fw>11 = 2,364,031 exact | `analysis/u11_gate_v021/` |
| u = 15 layer census (E-029) | 3 populated classes 788,009/787,457/788,565 = 2,364,031 exact; the spans 59,759 + the still-failers 74,987 = 134,746 exact | `analysis/u15_class_v023/` |
| u = 19 layer census (E-036) | all 18 classes populated; the spans 42,804 + the residual 32,183 = 74,987 exact | `analysis/u19_class_v027/` |
| u = 23 layer census (E-037) | all 22 classes populated; the spans 21,626 + the residual 10,557 = 32,183 exact | `analysis/u23_class_v028/` |
| u = 31 layer census (E-039) | all 30 classes populated (u = 29 structurally empty); the spans 4,668 + the residual 5,889 = 10,557 exact | `analysis/u29_class_v029/` |
| u = 31 delicate rescue (E-041) | 2,613/2,613 off-parameter pigeon-rescued, zero no-sites | `analysis/u31_rescue_v031/` |
| u = 35 layer census (E-043) | the chain-critical cells; the spans 691 + the residual 5,198 = 5,889 exact (the rescue 11.73%) | `analysis/u35_class_v032/` |
| u = 39 layer census (E-044) | the chain-critical cells; the spans 733 + the residual 4,465 = 5,198 exact (the rescue 14.10%) | `analysis/u39_class_v033/` |
| u = 43 layer census (E-046) | the chain-critical cells; the spans 192 + the residual 4,273 = 4,465 exact (the rescue 4.30%) | `analysis/u43_class_v034/` |
| u = 47 layer census (E-048) | the chain-critical cells; the spans 303 + the residual 3,970 = 4,273 exact (the rescue 7.09%) | `analysis/u47_class_v035/` |
| u = 51 layer census (E-050) | the chain-critical cells; the spans 36 + the residual 3,934 = 3,970 exact (the rescue 0.90%) | `analysis/u51_class_v036/` |
| u = 55 layer census (E-052) | the chain-critical cells; the spans 49 + the residual 3,885 = 3,934 exact (the rescue 1.24%) | `analysis/u55_class_v037/` |
| the exactness program (E-054–E-057) | the fold skeleton, the CRT-pair form (U15ALG = 0 as a theorem), the general fold-pair form, the deficit corollary; U15Layer at 18 theorems + 3 defs | `ErdosStrausConjecture/ResidualPrimes/U15Layer.lean` |
| the general deficit corollary (E-059) | the general exactness family complete: the fold skeleton + the unconditional pair form + the general deficit corollary; U15Layer at 19 theorems + 3 defs | `ErdosStrausConjecture/ResidualPrimes/U15Layer.lean` |
| u = 59 layer census (E-061) | the chain-critical cells; the spans 44 + the residual 3,841 = 3,885 exact (the rescue 1.13%) | `analysis/u59_class_v038/` |
| u = 63 layer census (E-063) | the chain-critical cells; the spans 10 + the residual 3,831 = 3,841 exact (the rescue 0.26%) | `analysis/u63_class_v039/` |
| u = 67 layer census (E-065) | the chain-critical cells; the spans 2 + the residual 3,829 = 3,831 exact (the rescue 0.05%, the floor); the census program closed | `analysis/u67_class_v040/` |
| the orbit-window cell facts (E-067/E-068) | the (mod 3, mod 5) pair-orbit closures as theorems (the mod-5 QR pair {1,4}, the mod-3 two-orbit); U15Layer at 21 theorems + 3 defs | `ErdosStrausConjecture/ResidualPrimes/U15Layer.lean` |

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

*The u = 11 layer (E-021–E-026, the first odd-composite layer).* The same
program run at the next H24-compatible layer, `u = 11`, with the census
corrected once and the correction stated in place (the historical trace lives
in the log entries; the facts below are the corrected ones).

**The class census and the empty class (E-021).** The H24 records distribute
over nine populated residue classes mod 11 (`r11 ∈ {1, 2, 3, 4, 5, 6, 7, 9,
10}`); the class `r11 = 8` is empty, and the gap is structural: `4·x = p + 11`
with `p ≡ 8 (mod 11)` forces `11 | x`, whose odd prime factor 11 carries
`11 % 3 = 2`, violating the hard-case predicate (every odd prime factor
`≡ 1 (mod 3)`). The span rates split into tiers — `r11 ∈ {7, 10}` at
17.33% / 17.41%, `r11 ∈ {2, 6}` at 15.25% / 15.28%, the rest at 7.44–8.90% —
and the u = 11 layer's own span total is 279,515 (11.82% of H24).

**The Legendre split and the QR-purity dichotomy (E-021/E-022).** At mod 11
the quadratic residues are `QR = {1, 3, 4, 5, 9}` (with −1 a non-residue,
`11 ≡ 3 (mod 4)`), and the span condition reads on the odd-part composition:
the census-level necessary direction — a QR-carrying odd prime factor of `x'`
is required for the u = 11 span — holds 0-mismatch over the tested population,
and is *sufficient* in exactly the classes `r11 ∈ {2, 6, 7, 10}` (the
span-side there: the QR status of the first non-QR odd prime decides). In the
QR classes `{1, 3, 4, 5, 9}` the condition is necessary-not-sufficient, and
the impure cells decompose further: the parity lock (the non-QR odd-prime
multiplicities are even in the QR-n̄ classes, odd in the non-QR classes,
exactly at full scale) and the count gradient (the span rate decays 0% →
13.79% → 6.28% → 0% over the non-QR counts 0/2/4/6+ at `r11 = 1`; the
residue signature `pres = 7` runs at 5.93% against 17.01–21.24% for the other
pres at equal counts, with the algebraic reading `7·9 ≡ 8 (mod 11)` on the
span-e targets).

**The route census (E-023).** The span criterion at u = 11 decomposes into two
routes (`d = e | x'` with `e ≡ −M̄`, and `d = p·e` with `e ≡ −x̄`); the census
is exact 0-mismatch and isolates a small minority whose hits live only in the
`x'^2`-window (2.0% at `r11 = 1`, 0.7% at `r11 = 4`, 1.46% at `r11 = 2`,
zero elsewhere — concentrated in the classes that also fail at u = 7).

**The fate-gate correction (E-024), stated in place.** The first u = 11
census (E-021 part 1) gated its cells on `first(p) ≠ 11` rather than on the
record's fate, mixing the fw = 7 spanners into the failure analysis — an error
the route census and a single prime ground-truth exposed. The corrected
3-fate census: **fw = 7 spanners 1,949,770 (82.49%), fw = 11 spanners 279,515
(11.82%), true fw > 11 failers 134,746 (5.70%)** — the populations sum to
2,364,031 exactly, and the rescue chain closes exactly:
279,515 + 134,746 = **414,261 = the E-014 u = 7 failing total**, i.e. the
u = 11 layer rescues precisely **67.38%** of the u = 7 failures. The
consequences, stated in place: the earlier "67.80% collision census" is
withdrawn (collisions among the *true* fw > 11 failers are 0, matching u = 7 —
the u = 7 absence is now a measured census row rather than a standing
principle); the parity lock, the count gradient, and the class-8 gap survive;
and the |D| = φ(u)−1-implies-failure heuristic is retired as a detection
heuristic, not a law.

**The fw = 7 fate cells (E-026).** The u = 7 layer's span rate is
composition-independent across the u = 11 residue classes: the fw = 7 spanner
population sits at 213,553–217,315 per class (82.5%, spread 1.7%). The
class-constant ~116.3k QR-pure population of the QR classes (E-021 part 2's
mixed reading) decomposes exactly into 92,419 fw = 7 spanners + 23,816
fw > 11 failers per class — the QR-pure records split 79.5% span-at-7 /
20.5% fail-through-11 — and the fw > 11 failers are overwhelmingly QR-pure
(23,816 / 26,060 = 91.4% at `r11 = 1`), the failure-side shape of the
QR-purity dichotomy.

*The u = 15 layer (E-029–E-032, the first composite layer).* The program's
first squarefree-composite parameter, `u = 15 = 3·5` (composite parameters are
admissible for the (H24) class exactly when `u ≡ 3 (mod 4)`, which removes
`u = 5` a priori — the layer chain runs 3, 7, 11, 15, 19, …). Two findings
carry the layer:

**Three populated classes, one structural exclusion, one inert class
(E-029).** The census finds exactly three populated classes (`r15 ∈ {1, 4,
13}`, 788,009 / 787,457 / 788,565 = 2,364,031 exact); the class `r15 = 7` is
empty and the gap is structural: its H24 primes (`p ≡ 97 (mod 120)`) carry
`5 | (p + 3)/4` always, so the hard-case predicate (every odd prime factor
`≡ 1 (mod 3)`) rejects the whole class — the same shape as the class-8 gap of
the u = 11 layer. The class `r15 = 13` is populated but inert at this layer:
none of its records spans or fails at `u = 15`, all 788,565 having been
resolved earlier (`fw ∈ {7, 11}`). Admissibility is automatic here: for the
sweep primes `M15 = 4p² (mod 15)` is always a unit, so no record is
inadmissible, and the `fw = 3` boundary of E-012 extends (`fw = 3` count =
0). **The rescue chain closes exactly:** the u = 15 spans 59,759 plus the
true `fw > 15` failers 74,987 equal the E-024 true-u-11-failers 134,746
exactly — the u = 15 layer rescues **44.34%** of the u = 11 failures, and the
population still failing through every layer tested is now **74,987 = 3.17%
of (H24)**. Zero collisions among the true failers (the pattern holds), the
fail D-sets are fixed shapes again (inside the 2-orbit closure
`{1, 2, 4, 8}` mod 15), and every u = 15 spanner is pigeon-conclusive
(`|D| ∈ {6, 7, 8}`, uniformly `|D| = 8` at `r15 = 4`).

**The CRT pair-set algebra, made exact (E-030/E-031).** Compositeness makes
the Chinese remainder the structural question: the divisor-residue set
`D15 = {d mod 15 : d | M15}` projects to divisor sets `D3` and `D5`, and
`|D15| ≤ |D3| · |D5|` with a NON-free pairing — the deficit
`|D3|·|D5| − |D15|` is class-lawed at three of the four existing
`(r15, mask3, mask5)` cells, the fourth splitting by fate. The engine-verified
algebra explains it completely: writing each residue as its CRT pair in the
8-element pair group `(Z/3)`* × `(Z/5)`*, for every prime `q | x'` with pair
`g_q = (q (mod 3), q (mod 5))` and exponent `e_q` the divisor window is
`{1, g_q, …, g_q^{e_q}}`; the pair set is the product closure of those windows
scaled by the p-classes `(1, 1), (p (mod 3), p (mod 5))`. This generation
reproduces `D15` for **every record — 0 mismatches over 2,364,031**. The fail
shapes decode as orbit windows: the fail D-sets `{1, 2, 4}` and
`{1, 2, 4, 8}` are exactly the `(2, 2)`-orbit cut at the 2-exponent windows,
mechanizing the deficit cells (`deficit = |D3|·|D5| − the window size`).

**The span-side mechanism (E-032).** The spanner shapes are fixed again: at
`r15 = 4` every spanner carries the **full unit group** (`|D| = 8`, all
27,488 records — the maximal pigeonhole certificate); `r15 = 1` has six
shapes. Every spanner is certified by the x′-window hit, the p-scaled window,
or both — at `r15 = 4` the off-orbit p-pair `(1, 4)` is itself a generator
needed for 19.1% of the spans — and the off-orbit odd-prime pairs number
0–4 per spanner with the mode 1–2: **one off-orbit odd-prime pair suffices
for about half the spans** of each class, while 2,563 spans need none (the
orbit + the p-scale sufficing).

*The prime-layer chain (E-034–E-037).* The census ladder extends to the
next prime layers, `u = 19` and `u = 23`. The prime layers differ from the
composite ones in two ways, both theorems now: the coprimality is automatic
(the E-034 module `U15Layer.lean` proves `x` and `M = p·x` coprime to `u = 15`
for `4·x = p + 15` — the census analog `admfail = 0` holds at 19 and 23, and
no structural class exclusions exist — all 18 (resp. 22) unit classes
populated, total 2,364,031 exact), and the `fw = 3` boundary holds at every
layer (`fw = 3` count = 0). The rescue chain closes exactly at both layers:
the u = 19 spans 42,804 + the true `fw > 19` failers 32,183 = 74,987 = the
u = 15 still-failers exact (the u = 19 layer rescues **57.09%**), and the
u = 23 spans 21,626 + the residual 10,557 = 32,183 exact (the u = 23 layer
rescues **67.20%**). The chain now reads

> u = 3 (0 spans) → 7 (1,949,770, 82.49%) → 11 (279,515, 11.82%) →
> 15 (59,759, 2.53%) → 19 (42,804, 1.81%) → 23 (21,626, 0.91%) →
> the residual **10,557 (0.447% of the hard-case class)**,

zero collisions among the true failers at every nontrivial layer, and the
composite-layer deficit bound is a theorem (`uDset15_card_le`: the
divisor-residue set at 15 never exceeds the product of the layer sets at 3
and 5 — the nonnegativity of the E-030 deficit as a theorem — with the
D-set-as-Finset foundation `uDset` now available at any modulus). The Lean
joint audited set stands at **65**.

*The u = 31 program (E-039–E-041, the collision-regime transition).* The
chain's admissible layers are exactly the `u ≡ 3 (mod 4)` parameters — the
u = 29 skip is structural once more: `u = 29 = 1 (mod 4)` forces
`p + 29 = 24k + 30`, never divisible by 4 evenly for `p = 24k + 1`, so no
(H24) record exists there (the u = 5 shape). At **u = 31** (prime, 30 unit
classes all populated, coprimality automatic) the chain closes exactly again:
the spans 4,668 + the true `fw > 31` failers 5,889 = 10,557 = the E-037
residual — the u = 31 layer rescues **44.21%**, the residual now **0.249%**
of the hard-case class. Two new facts at this layer:

**The zero-collision era ends (E-039).** The true failers at u = 7, 11, 15,
19, 23 carried zero collision pairs — an orbit-window regime — but at u = 31
**2,613 of the 5,889 failers (44.4%) carry a collision pair** (collision
presence without the span).

**The delicate-class shape re-emerges (E-040/E-041).** The mechanism census
decodes the regime: the collision rate by `|D31|` is 0% below 6, 100% at
6/7/9, and 50.2% at the |D| ≥ 11 mass bucket; **the (1, 30) unit pair
dominates — 2,176 of 2,613 = 83.3%** — exactly the *one-sided criterion*
`−1 ∈ D31(M)` (the divisor 1 carries the (1, …) side always, and
30 = −1 (mod 31)). The collision-carrying failers are pigeonhole-insufficient
at 31 (`|D| ≤ 11 < 15 = φ(31)/2`), carry the pair, and fail the parametric
span — **the delicate-class structure of the opening section, re-emerging at
a fresh layer as a per-layer fact**. And the E-011 rescue framework covers
them exactly: the off-parameter pigeon-rescue scan (the v0.31 engine, the
E-011 procedure verbatim) returns

> delicate 2,613 — rescued 2,613 (100%) — pigeon-without-collision 0 —
> no-site 0,

the exact analog of the original 16,589/16,589 row, so the census's
representation-completeness over the (H24) class holds through the new
regime with zero uncovered records.

*The chain links at u = 35 and u = 39 (E-043/E-044, the ladder's
decay).* The chain closes exactly at both links: the u = 35 spans 691 +
the residual 5,198 = 5,889 exact (the u = 35 layer rescues **11.73%** — the
first sharp ladder drop, from the 44–67% per-link range to the teens), and
the u = 39 spans 733 + the residual 4,465 = 5,198 exact (the rescue
**14.10%**). The still-failers are **4,465 = 0.189% of the hard-case
class**. The collision shares continue their layer alternation: 44.4% at 31,
26.0% at 35, **46.7% at 39** — the delicate-regime population oscillates
while the record counts fall. The ladder's consolidated view (the residual
record counts and the per-layer rescue rates):

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → the residual
> 4,465 (0.189%),

with the Ladder Consolidation note: from u = 31 onward the census carries
the chain-critical cells only (the class counts, the |D| histograms, the
collision counter — the full mask arrays would need 800 MB+ at the wider
residues, and the mask-shape detail is established at the earlier layers),
and every assertion row (the admissibility, the fw = 3 boundary, the
zero-... the collision-rate rows) is pinned per layer. The per-layer
span-rate decay (82.49%, 11.82%, 2.53%, 1.81%, 0.91%, 0.20%, 0.03%, 0.03%)
with the per-link rescue rates (11.82%... 44.21%, 11.73%, 14.10%) converges
toward the asymptotic regime the research program's next question targets:
the remaining 4,465 records under the future layers and the honest statement
the banner carries.

*The chain links at u = 43 and u = 47 (E-046/E-048, the ladder's late
decade)* and **the general composite D-set form (E-047)**. The chain closes
exactly at both prime links: the u = 43 spans 192 + the residual 4,273 =
4,465 exact (the u = 43 layer rescues **4.30%**), and the u = 47 spans 303 +
the residual 3,970 = 4,273 exact (the rescue **7.09%**). The still-failers
are **3,970 = 0.168% of the hard-case class**. The collision shares continue
their oscillation with an upward drift: 44.4% at 31, 26.0% at 35, 46.7% at
39, 23.1% at 43, **65.2% at 47**. The consolidated chain:

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → 43 (0.01%) →
> 47 (0.01%) → the residual **3,970 (0.168%)**,

and the composite-layer D-set foundation is now **general**: the theorem
`uDset_coprime_card_le` proves `|D_ab| ≤ |D_a| · |D_b|` for every nonzero
coprime pair `(a, b)` (the CRT decode injectivity via the exact toolchain
composition `Nat.modEq_and_modEq_iff_modEq_mul` with the coprime hypothesis,
the pair routing via `Nat.mod_mod_of_dvd`), with the u = 35 bound (5 × 7) as
the corollary — the Lean joint audited set stands at **68**, 0-`sorry`, and
the E-035 bound subsumed.

*The chain link at u = 51 (E-050, the asymptotic regime).* The chain
closes exactly once more: the u = 51 spans 36 + the residual 3,934 =
3,970 = the E-048 residual (the u = 51 layer rescues **0.90%** — the
second sharp drop; the per-link rescues are now under one percent).
The still-failers are **3,934 = 0.166% of the hard-case class**. The
collision share alternates on (65.2% at 47 → 34.0% at 51). The
asymptotic-regime note, stated honestly: the census ladder's per-link
rescues have entered the sub-one-percent regime, so the census ladder
ALONE will not drain the residual — the structure question (the
pair-window algebra's full exactness as a theorem, with the D-set
foundation and the general composite bound in place from E-035/E-047)
is the necessary direction of the program. The consolidated chain:

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → 43 (0.01%) →
> 47 (0.01%) → 51 (0.002%) → the residual **3,934 (0.166%)**,

and the zero-collision rows hold at
`fw3 = 0` everywhere with the admissibility automatic per E-034.

*The chain link at u = 55 (E-052, the band confirmed).* The chain closes
exactly once more: the u = 55 spans 49 + the residual 3,885 = 3,934 = the
E-050 residual (the u = 55 layer rescues **1.24%** — the alternation
0.90 → 1.24 continues within the **sub-two-percent asymptotic band**, now
confirmed across two links). The still-failers are **3,885 = 0.164% of the
hard-case class**. The collision share alternates (34.0% at 51 → 40.5% at
55). The consolidated chain:

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → 43 (0.01%) →
> 47 (0.01%) → 51 (0.002%) → 55 (0.002%) → the residual **3,885 (0.164%)**,

with every assertion row (the admissibility, the fw = 3 boundary, the
collision counter) pinned per layer, and the asymptotic-regime reading of
the u = 51 note standing.

*The exactness program (E-054–E-057, the census algebra formalized).* The
pair-window algebra's structure is now a theorem. The fold skeleton
(`uDset_fold_image`): for the fold of coprime factorizations
`D_u(m₁ · m₂)` is **exactly the image of the divisor-pair product** under
`(d₁, d₂) ↦ (d₁ · d₂) % u` (the divisor split via
`Nat.gcd_mul_gcd_eq_iff_dvd_mul_of_coprime`). The fold's CRT-pair form
(`crtPair_fold_image15`, the general `crtPair2_fold_image`): the realized
`(u₁, u₂)`-pairs at any composite layer are **exactly the divisor-product's
paired-residue image** — the exact statement of the census algebra
**U15ALG mismatch = 0** (the E-031 fold, engine-verified 0-mismatch), and it
holds unconditionally. The deficit corollary (`uDset15_card_le_fold`): the
composite layer's residues never exceed the **full divisor-product count**
`∏ (e_q + 1)` — the product of the two factors' divisor counts,
`|D(m₁)| · |D(m₂)|` — via the CRT decode's
injectivity on the bounded residues. The supporting pieces: the mem-level
CRT-pair routing (`uDset_mem_crt_pair`), the **general** decode injectivity
(`crtPair2_injOn_lt`, any nonzero coprime `a, b` — the general form of
`crtPair_injOn15`). The general fold deficit corollary (`uDset_card_le_fold`, E-059) completed
the general family in its first form: the divisor-residue set at **any**
composite layer (of nonzero coprime factors) never exceeds the folded
factorization's full divisor-product count, via the count chain (the
injectivity + the general pair form + `card_image_le` + `card_product`),
with the zero-exclusion stated honestly (the hypotheses require
`u₁ ≠ 0` and `u₂ ≠ 0`, so the coprime pair `u₁ = 0`, `u₂ = 1` lies outside
that theorem's scope). The strengthened form (`uDset_card_le_fold'`,
E-077) drops the u-side hypotheses entirely: the bound holds at **any**
layer `u`, because the residue set is an image of the divisor set, so its
count is bounded by the divisor count outright (`card_image_le`), and the
coprime divisor-count equality (`Nat.Coprime.card_divisors_mul`) splits
that count over the factors. Only the m-coprimality hypothesis remains,
and the zero-exclusion is gone with the hypotheses that caused it. The orbit-window program (E-067/E-068) starts at the cell level: the
**mod-5 ±1-orbit closure** (`prod_qr_mod5` — a positive integer with all
prime divisors QR mod 5, the pair `{1, 4}`, is a QR mod 5; the
divisor-status induction, the `prod_mod_qr` pattern specialized) and the
**mod-3 two-orbit closure** (`prod_orbit_mod3` — the {1, 2}-orbit
composition, first-try clean once the pattern was established). Both
orbit-closure theorems were removed from `U15Layer` at E-077, in the
same change that strengthened the fold corollary; they are not part of
the module state the audited count below reflects. Both halves
of the `(mod 3, mod 5)` pair-orbit are theorems: each is a product-closure
statement about a positive integer whose prime divisors lie in the named
residue set. The Lean joint audited set
stands at **74**, 0-`sorry` (recounted name by name at the E-070
correction, PR #85/#87 — which regenerated the U15Layer axiom audit in
full, finding 74 against the previously stated 82; the E-074 extension of
the audit to all 25 declarations — including the fail-shape cell fact
`prod_in_clo4_mod15` — brought the count to 75: 60 audited src theorem
names + the 15 nano theorems; the E-077 and E-078 changes bring it to
74: 59 audited src theorem names + the 15 nano theorems, the fold
corollary's restatement counting one for one, `count_add_le_count_mul`
adding one, and the two orbit closures' removal taking away two). The ResidualPrimes modules sit outside the
certified CI build (the root library and the five modules it imports);
U15Layer compiles separately, and its axiom audit and compile record are
pinned in the manifest. The general exactness family is complete: the fold
skeleton, the pair form (unconditional), the deficit corollary
(strengthened at E-077).

*The chain link at u = 59 (E-061, the band steadies).* The chain closes
exactly once more: the u = 59 spans 44 + the residual 3,841 = 3,885 = the
E-052 residual (the u = 59 layer rescues **1.13%** — the band steadies:
1.24 → 1.13 across the composite layers, three consecutive links within the
sub-two-percent asymptotic band). The still-failers are **3,841 = 0.162% of
the hard-case class**. The collision share alternates on (40.5% at 55 →
51.3% at 59). The consolidated chain:

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → 43 (0.01%) →
> 47 (0.01%) → 51 (0.002%) → 55 (0.002%) → 59 (0.002%) → the residual
> **3,841 (0.162%)**.

*The chain link at u = 63 (E-063, the composite drop).* The chain closes
exactly once more: the u = 63 spans 10 + the residual 3,831 = 3,841 = the
E-061 residual (the u = 63 layer rescues **0.26%** — the composite layers
now land under half a percent per link: 1.13 at 59 → 0.26 at 63). The
still-failers are **3,831 = 0.162% of the hard-case class**. The collision
share alternates on (51.3% at 59 → 38.6% at 63). The consolidated chain:

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → 43 (0.01%) →
> 47 (0.01%) → 51 (0.002%) → 55 (0.002%) → 59 (0.002%) → 63 (0.0004%) →
> the residual **3,831 (0.162%)**.

*The chain link at u = 67 (E-065, the floor) and the census program's
close.* The chain closes exactly once more: the u = 67 spans 2 + the
residual 3,829 = 3,831 = the E-063 residual (the u = 67 layer rescues
**0.05%** — **the ladder's floor reached** (0.26 → 0.05; two records at
u = 67)). The still-failers are **3,829 = 0.162% of the hard-case class**.
The collision share alternates on (38.6% at 63 → 17.5% at 67). The
consolidated chain:

> u = 3 (0) → 7 (82.49%) → 11 (11.82%) → 15 (2.53%) → 19 (1.81%) →
> 23 (0.91%) → 31 (0.20%) → 35 (0.03%) → 39 (0.03%) → 43 (0.01%) →
> 47 (0.01%) → 51 (0.002%) → 55 (0.002%) → 59 (0.002%) → 63 (0.0004%) →
> 67 (0.00008%) → the residual **3,829 (0.162%)**.

Honest verdict, recorded: **the census program is complete** — the
per-link rescues have reached the data's resolution floor, and every
further link is below it; the remaining increments are structural (the
orbit-window cell equality) or nil.

**CORRECTED (E-072, the fate-list artifact):** the chain lists in this
manuscript's tail sections carried an inflated residual (the u = 27 link
missing from the per-layer fate lists from E-039 on); the corrected
sweep-wide chain, derived from the committed v0.28 BYU table (which sums
to the sweep exactly — the complete first-working distribution):

> u = 3 (830,200, the F(p) = 3 class) → 7 (82.47%) → 11 (67.47%) →
> 15 (44.34%) → 19 (57.08%) → 23 (67.19%) → **27 (3,818; 36.16%)** →
> 31 (4,668; 69.26%) → 35 (691; 33.36%) → 39 (733; 53.11%) →
> 43 (192; 29.67%) → 47 (303; 66.59%) → 51 (36; 23.68%) →
> 55 (49; 42.24%) → 59 (44; 65.67%) → 63 (10; 43.47%) → 67 (2; 15.38%) →
> 71 (6; 54.54%) → 75 (2; 40%) → 79 (1; 33.33%) → 83 (2; 100%) →
> the (H24) residual **ZERO**.

The per-link rescues fluctuate (15.4% to 82.5%) — the "asymptotic band" and
"ladder floor" readings withdrawn as artifacts. The empirical statement:
every hard-case prime in [10^7, 10^9) has F(p) ≤ 83 (the standing banner
untouched; computation never closes a universal claim). The per-layer span
counts and the collision/cell observations stand as stated.

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

Machine-checked 2026-11-26 (R8, joint audited set 15 + 35 + 5 = 55, all
results on the axiom trio `[propext, Classical.choice, Quot.sound]`, with
`qr_closed_mod11` on `propext` alone; 0 `sorry`):

| Module | Content | Result |
| --- | --- | --- |
| `ResidualPrimes.U3Boundary` (5 theorems) | the u = 3 layer: the constructive even-`x` span at `T = 2`, the predicate exclusion, the composed iff (its even side vacuous under the predicate) | E-012; comment-only edits reviewed in PR #32 |
| `ResidualPrimes.U7Layer` (13 theorems) | the u = 7 layer: the per-class span/pigeon theorems at `r7 = 3/5/6`, the three conditional 5-window spans, the 2-orbit closure lemma, and both directions of the composition-level iff (`u7_span_fails_of_orbit_primes`, `u7_pigeon_of_orbit_breaker` with the `{n, x, q, 2q}` four-residue pigeon) | E-013/E-015/E-019 |
| `ResidualPrimes.U11Layer` (7 theorems) | the u = 11 layer: the class-8 structural gap (`u11_no_hardcase_record_mod8`), the v2-bucket degeneracy (`u11_x_odd`), the explicit-witness spans at `r11 = 7` (d = p) and `r11 = 10` (d = x), the QR multiplicative closure (`qr_closed_mod11`, propext), the divisor-status induction (`prod_mod_qr`), and the main QR-purity dichotomy theorem (`u11_span_fails_of_qr_pure_x`: for QR-n̄ classes with QR-pure odd `x'`, no divisor of `(p·x)²` carries a non-QR residue, so the span criterion fails — the E-022 census fact as a theorem) | E-025/E-027 |

The iff's machine-checked directions cover the failing classes under a
span-test hypothesis; the census statement above names the population each
direction was tested on.

## 11. Conclusion

Established results, conjectures, and open questions grow with the
`EXPERIMENT_LOG.md` record.

## Appendix

Data, algorithms, and reproducibility: `DATA_MANIFEST.md` (SHA-256 manifest,
re-runnable via `tests/verify_manifest.py`).
