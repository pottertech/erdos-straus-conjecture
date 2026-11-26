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
| `ResidualPrimes.five_divides_x` (U11Exact) | 4 ∣ p + 11 ∧ p ≡ 4 (mod 5) ⟹ 5 ∣ (p + 11)/4 | principal (R3) |
| `ResidualPrimes.five_pow_ne_neg_one` (U11Exact) | every 5-power in ZMod 11 differs from −1 (the 5-window miss) | principal (R3) |
| `ResidualPrimes.cast_prod_finsupp` (WindowForm) | the residue cast distributes over Finsupp products | support (R4) |
| `ResidualPrimes.window_iff_inCentered` (WindowForm) | the factorization-window span ⟺ D·D⁻¹ (the §5.3 bridge) | principal (R4) |
| `ResidualPrimes.five_divides_x_u7` (U11Exact) | 4 ∣ p + 7 ∧ p ≡ 3 (mod 5) ⟹ 5 ∣ (p + 7)/4 | principal (R3) |
| `ResidualPrimes.five_pow_three_eq_neg_one_mod_seven` (U11Exact) | 5³ ≡ −1 (mod 7) (the u = 7 window reach) | principal (R3) |

Scope note (carried from the module docstring): the factorization-window
characterization of the centered product set (`∏ q^−e..e`-products over
`M`'s factorization equaling `D·D⁻¹`) is the R4-lane extension and is NOT
claimed. The joint audited set stands at 15 (Paper 1, frozen) + 9 = 24:
the U11Exact pair audited on `propext, Quot.sound` (`five_divides_x`) and
the trio (`five_pow_ne_neg_one`); see E-005.
WindowForm’s two audited on `propext, Quot.sound` and the trio respectively
(E-006), bringing the total to 28: the U11Exact additions `five_divides_x_u7`
and `five_pow_three_eq_neg_one_mod_seven` audited on `propext, Quot.sound`
(E-007).
U3Boundary's five audited (all trio; E-012) bring the joint audited set to
15 + 18 = 33.
U7Layer's seven audited (the two spans on `propext, Quot.sound`, the
rest on the trio; E-013) bring the joint audited set to 15 + 25 = 40.
The three conditional 5-window spans audited on exactly
`propext, Quot.sound` (E-015) and the three E-019 items on the trio
(the 2-orbit closure lemma `prod_in_orbit_clo_two`, both directions of
E-018's composition-level iff: the fail route
`u7_span_fails_of_orbit_primes` and the span route
`u7_pigeon_of_orbit_breaker`, `U7Layer.lean` at 13 theorems) bring the
joint audited set to 15 + 31 = 46; the u = 11 layer's first four theorems (U11Layer.lean, E-025: the class-8 structural gap, the v2-degeneracy lemma, the explicit-witness spans at r11 = 7/10; three duo-audited on `propext, Quot.sound`, one on the trio) bring the joint audited set to 15 + 35 + 5 + 5 = 60 (the u = 11 layer's 7 theorems total: the class-8 gap, the v2 degeneracy, the explicit-witness spans at r11 = 7/10, the QR-closure machinery (prod_mod_qr, qr_closed_mod11), and the main QR-purity dichotomy).

## 4. Established in Paper 2 (R8 piece 3, module `ResidualPrimes.U3Boundary`)

Machine-checked 2026-11-25; compile exit 0 (8477 jobs); axiom census (all
five): exactly `[propext, Classical.choice, Quot.sound]`; no project axioms;
0 `sorry`. Audit artifact: `ErdosStrausConjecture_src/axiom_audit_u3.txt`
(build log `lake_build_u3.log`), hash-pinned in DATA_MANIFEST. Empirical
counterpart: E-011 (the sweep-wide census, engine v0.8) — the
population-scale picture the run verified (the constructive even-x
direction is `u3_span_of_even_x`; the composed iff's even side is
vacuous under the hard-case predicate, which rules out 2 ∣ x).

| Theorem | Statement | Registry lane |
| --- | --- | --- |
| `ResidualPrimes.prod_mod_one_of_primes_mod` | prime divisors all 1 (mod 3) (with 0 < T) ⟹ T ≡ 1 (mod 3) | support |
| `ResidualPrimes.u3_span_of_even_x` | 4·x = n + 3 ∧ 2 ∣ x ∧ 3 ∤ x ⟹ the u = 3 span criterion holds at `T = 2` | principal |
| `ResidualPrimes.isErdosStraus_of_even_x` | the same hypotheses yield an explicit positive solution (the sharpened, primality-free F(p) = 3 family) | principal |
| `ResidualPrimes.u3_span_fails_of_odd_x` | under the hard-case predicate (x's prime divisors ≡ 1 (mod 3)), x odd ⟹ no u = 3 span candidate exists | principal |
| `ResidualPrimes.u3_span_iff_even_of_hard` | the composed iff under the hard-case predicate: u = 3 span ⟺ 2 ∣ x, where the predicate rules out 2 ∣ x, so the criterion never holds under it | principal |

## 5. Established in Paper 2 (R8 piece 4, module `ResidualPrimes.U7Layer`)

Machine-checked 2026-11-25; compile exit 0; axiom census: the two span
theorems exactly `[propext, Quot.sound]`, the three pigeon theorems and the
two supports on the standard trio; no project axioms; 0 `sorry`. Audit
artifact: `ErdosStrausConjecture_src/axiom_audit_u7.txt` (build log
`lake_build_u7.log`), hash-pinned in DATA_MANIFEST. Empirical counterpart:
E-013 (engine v0.9, the full-scale u = 7 census).

| Theorem | Statement | Registry lane |
| --- | --- | --- |
| `ResidualPrimes.mem_divResidues` | a divisor of `M` (with `0 < M`) contributes its residue to `divResidues u M` | support |
| `ResidualPrimes.cast_ne_of_mod_ne` | unequal `% 7` residues cast to unequal `ZMod 7` elements | support |
| `ResidualPrimes.u7_span_of_mod7_three` | 4·x = n + 7 ∧ n ≡ 3 (mod 7) ⟹ the u = 7 span criterion holds at `T = n` | principal |
| `ResidualPrimes.u7_span_of_mod7_six` | 4·x = n + 7 ∧ n ≡ 6 (mod 7) ⟹ the u = 7 span criterion holds at `T = x` | principal |
| `ResidualPrimes.u7_pigeon_of_mod7_three` | 4·x = n + 7 ∧ n ≡ 3 (mod 7) ⟹ hasOppositePair 7 (n·x) (pigeon via the audited R5 theorem) | principal |
| `ResidualPrimes.u7_pigeon_of_mod7_five` | the same at n ≡ 5 (mod 7) with 2 ∣ x (the sweep's n ≡ 1 (mod 8) family) | principal |
| `ResidualPrimes.u7_pigeon_of_mod7_six` | the same at n ≡ 6 (mod 7) | principal |
| `ResidualPrimes.u7_span_of_fivex_pm1` | 4·x = n + 7 ∧ n ≡ \u00b11 (mod 7) ∧ 125 ∣ x ⟹ the u = 7 span at `T = 5` | principal |
| `ResidualPrimes.u7_span_of_fivex_pm2` | the same at n ≡ \u00b12 (mod 7), 125 ∣ x, span at `T = 125` | principal |
| `ResidualPrimes.u7_span_of_fivex_pm3` | the same at n ≡ \u00b13 (mod 7), 3125 ∣ x, span at `T = 3125` | principal |

## 6. Rejected / superseded

None at initiation. Rejected hypotheses move here with a correction banner
(what was claimed, why it failed, what remains valid).
