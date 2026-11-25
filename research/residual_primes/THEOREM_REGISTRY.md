# THEOREM_REGISTRY.md — Paper 2

Strict separation: proved theorems carry a module, an axiom-audit status, and
a CI-gate entry. Accepted-but-unformalized mathematics is labeled pending.
Nothing enters "proved" without `lake env lean` 0-`sorry`, the axiom census,
and the CI axiom gate.

## 1. Inherited from Paper 1 (frozen at `paper-v1.12`; 15 audited principal results)

| Theorem | Module | Axioms | Note |
| --- | --- | --- | --- |
| `Reduction.scaling` | `Reduction.lean` | `propext` | composites inherit from primes |
| `Reduction.mod8_of_12` | `Reduction.lean` | trio | |
| `Reduction.prime_non24_isErdosStraus` | `Reduction.lean` | trio | unconditional prime coverage |
| `Reduction.full_conjecture_of_h24` | `Reduction.lean` | trio | (H24) ⟹ conjecture |
| `MainTheorem.erdos_straus_except_residual_open_class` | `MainTheorem.lean` | trio | |
| `MainTheorem.residue_classification` | `MainTheorem.lean` | trio | seven-case partition |
| `CenteredEquivalence.theorem2` | `CenteredEquivalence.lean` | trio | search-domain bound `0 < u ≤ 2p` |
| `CenteredCriterion.u_method_core` | `CenteredCriterion.lean` | trio | witness ⟹ solution (constructive) |
| `CenteredCriterion.u_method_witness` | `CenteredCriterion.lean` | trio | constructive wrapper |
| `FiniteSearch.witness_extraction` | `FiniteSearch.lean` | trio | extraction direction of Theorem 5.2 |
| `FiniteSearch.finite_search_equivalence` | `FiniteSearch.lean` | trio | complete 5.2 biconditional |
| `FiniteSearch.parametric_divisibility` | `FiniteSearch.lean` | trio | `T ∣ M ⟹ y ∣ z` |
| `FiniteSearch.parametric_divisibility_iff` | `FiniteSearch.lean` | trio | complete `T ∣ M ⟺ y ∣ z` |
| `FiniteSearch.param_exists_iff_onesided` | `FiniteSearch.lean` | `propext, Quot.sound` | one-sided criterion `−1 ∈ D_u(M)` |
| `FiniteSearch.h213_parametric_u3` | `FiniteSearch.lean` | trio | `p ≡ 13 (mod 24) ⟹` witness at `u = 3`, `F(p) = 3` |

(Trio = `propext, Classical.choice, Quot.sound`. Two documented project axioms
remain in context modules, census-enforced; not used by the principal results.)

## 2. Accepted mathematics — formalization pending (Paper 2 targets)

| Statement | Source | Target module | Status |
| --- | --- | --- | --- |
| Collision equivalence: `−1 ∈ S_u(M) ⟺ D_u(M) ∩ (−D_u(M)) ≠ ∅` | sixth/ninth reviews (`S_u = D·D⁻¹`) | `ErdosStrausConjecture/ResidualPrimes/` | accepted math; formalization pending (R4) |
| Pigeonhole sufficiency: `|D_u(M)| > φ(u)/2 ⟹ D ∩ (−D) ≠ ∅` | ninth-review §5.3 | `ErdosStrausConjecture/ResidualPrimes/` | accepted math; formalization pending (R5) |

These enter the Paper-2 audited set upon R4/R5 completion (raising the joint
audited count to 17); Paper 1's registry stays frozen at 15.

## 3. Established in Paper 2 (R4/R5, module `ResidualPrimes.CollisionReachability`)

Machine-checked 2026-11-24; compile exit 0; axiom census (all seven): exactly
`[propext, Classical.choice, Quot.sound]`; no project axioms; 0 `sorry`.
Axiom audit artifact: `ErdosStrausConjecture_src/axiom_audit_collision.txt`
(hash-pinned in DATA_MANIFEST).

| Theorem | Statement | Registry lane |
| --- | --- | --- |
| `ResidualPrimes.card_le_totient_of_all_isUnit` | any finset of units of `ZMod u` has at most `phi(u)` members (the review's pigeonhole lemma) | support |
| `ResidualPrimes.isUnit_mem_union` | members of the union `D ∪ (−D)` are units under `gcd(M, u) = 1` | support |
| `ResidualPrimes.card_negResidues_eq` | `−D` has the same cardinality as `D` | support |
| `ResidualPrimes.pigeonhole_reachability` | **2·|D_u(M)| > phi(u) ⟹ D ∩ (−D) ≠ ∅** (R5 target) | principal |
| `ResidualPrimes.hasOppositePair_iff_collisionPair` | the collision condition ⟺ the pair condition `∃ d₁ d₂ ∣ M, (d₁ + d₂) % u = 0` | principal |
| `ResidualPrimes.mem_centered_neg_one_iff_collisionPair` | **−1 ∈ D·D⁻¹ ⟺** the collision-pair condition (R4 target) | principal |
| `ResidualPrimes.hasOppositePair_iff_centered_neg_one` | the review's boxed criterion ⟺ membership of −1 in the centered product set | principal |

Scope note (carried from the module docstring): the factorization-window
characterization of the centered product set (`∏ q^−e..e`-products over
`M`'s factorization equaling `D·D⁻¹`) is the R4-lane extension and is NOT
claimed. The joint audited set stands at 15 (Paper 1, frozen) + 7 = 22.

## 4. Rejected / superseded

None at initiation. Rejected hypotheses move here with a correction banner
(what was claimed, why it failed, what remains valid).
