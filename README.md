# Erdős–Straus Conjecture: exact verifiers, cascade reductions, and a Lean formalization

**The conjecture is not proved in this repository** — see [STATUS.md](STATUS.md) for the standing determination (2026-11-19): the exact residual gap and what would change it. It states that for every integer n ≥ 2 there exist positive integers x, y, z with 4/n = 1/x + 1/y + 1/z.

What is here, with verified status as of 2026-11-18:

1. Working Python verifiers for the exact u-method criteria (direct divisor-pair criterion and the centered product-set equivalent).
2. Proved finite-group cascade layers that reduce prime hard cases to a thin residual set — exact algebra, not heuristics.
3. Exhaustive computational solution-checking through 10^9, with sampling and exhaustion clearly separated.
4. A Lean 4 formalization with a documented axiom whitelist and an enforced census of unfinished goals.
5. An audit trail: two historical documents whose central claims were withdrawn on 2026-08-28, kept under correction banners rather than deleted.

## Start here

| Document | What it gives you |
|---|---|
| `CORRECTED_CLAIM_AUDIT.md` | The claims withdrawn on 2026-08-28 and why (counterexample n = 1129; parity error; the 87.5% claim; the three-target shortcut) |
| `DETERMINISTIC_CASCADE_STATUS.md` | The current proof-level position |
| `CENTERED_PRODUCT_SET_THEOREM.md` | The exact criterion every verifier implements |

## Mathematical status

Exact criterion for the u-method (u = 4x − n, M = nx, gcd(M, u) = 1):

> u-method succeeds ⟺ −1 ∈ S_u(M), the bounded centered signed prime-product set of M

Proved deterministic layers (finite-group-algebra statements; the finite numbers are cross-checks, not the proof):

1. **Shift-divisor reduction** — every residual hard case must have n ≡ 1 (mod 24), every odd prime factor of n+1 and every prime factor of n+4 ≡ 1 (mod 4).
2. **u = 7** — failure forces every prime divisor of M_7 into {1, 2, 4} (mod 7), and n ≡ 1 or 4 (mod 15).
3. **u = 11** — residue obstruction completely classified (all-QR case plus explicit small exceptions).
4. **u = 15** — failure ⟺ every prime divisor of M_15 lies in ⟨2⟩ = {1, 2, 4, 8} ⊂ (Z/15Z)×.
5. **u = 23** — 2 and 3 are forced centered generators (all-QR case plus explicit exceptions).

Finite cross-check through 10^7 (exact criterion): 48,711 corrected prime hard cases → 283 survivors after the five layers (≈ 99.42% reduction). Extending the same sweep through further moduli (31 → 63) leaves a single survivor, **n = 8,803,369**, whose first working u is 107 (centered witness with support 3).

> **Correction (2026-11-19):** a dataset reconciliation (`FIRST_A_STRUCTURE.md`) found the stage chain above omits the admissible layers u = 19 and 27, and its base includes 12,961 theorem2-solved 13-mod-24 primes. Corrected: true residual base is 35,750 (12,961 phantoms); the true chains — structured 7,272 → 2,137 → 1,054 → 681 → 388 → 150 → 109 → 35 → …, full residual 35,750 → 7,144 → 2,681 → 1,732 → 849 → 308 → 217 → 65 → … — terminate at the same single survivor (8,803,369, u = 107). The per-record span/exact layer verifications remain valid for the entrant sets they checked.

**Open:** a theorem-level obstruction at u = 31; a bounded-support deterministic cascade theorem; the structure of the residual class.

## Verification status — read the labels

| Ladder | Range | Nature |
|---|---|---|
| Exhaustive solution search (repo pipelines) | every checked hard case solved through 10^9 (results in `verification_*.json`; e.g. 10^8–10^9: 2,852,233 cases, 0 failures, max A = 151) | exhaustive |
| Exact-criterion hard-case cascade | prime hard cases through 10^7 | exhaustive |
| Largest-A sampling | 36 hard-case primes over 12 decades (10^10–10^21), max A = 7 | **sampling, not exhaustion** |

The lone "failure" in the 10M–100M run is the outlier n = 8,803,369, which resolves at u = 107 (see `OUTLIER_8803369_FAILURE_STATES.md`) — it is not an open case.

The literature's exhaustive-verification record is ≈ 10^18. Older repo wording ("known to hold for all n up to 10^21+") referred to the sampling row, not exhaustion; it is corrected here and in the banners of the withdrawn documents.

Regression guard pinned in CI: **n = 1129 fails at u = 7 and first succeeds at u = 11** — the counterexample behind the 2026-08-28 audit (`scripts/smoke_test.py`).

## Superseded documents — do not cite their central claims

- `UNIFIED_THEOREM.md` (2026-08-26): banner lists exactly what `CORRECTED_CLAIM_AUDIT.md` withdrew — deterministic coverage of n ≡ 13 (mod 24) and n ≡ 49 (mod 120) via u = 7, the resulting 87.5% claim, CRT cascades computed from the old three-target shortcut, and the 10^21 wording.
- `DETERMINISTIC_BOUND_PROOF.md` (2026-08-24): same withdrawals (Family A theorem, B1 claim).
- `LEAN_PROGRESS.md`: its "zero `sorry`" build claim is contradicted by the census below.

The text is preserved unmodified under the banners for the record.

## Lean formalization

One maintained project at the root (Lean/Mathlib **v4.30.0** — the tag is verified to exist on the Mathlib GitHub repo; the two retired side projects pinned v4.33.1 and diverged).

**Builds green (verified locally 2026-11-18; enforced in CI):**

- root library — root module + `Basic`, `CenteredCriterion`, `Identities`, `Mod12Case1` + `Main` exe — via `lake exe cache get && lake build`: 8,481 jobs, exit 0 (2026-11-19);
- nine additional modules, all verified compiling on v4.30.0 and built in CI: `DivisorResidue`, `ClassicalIdentities`, `OmegaCases`, `CenteredEquivalence`, `MainTheorem`, `Theorem4`, `NewTheorems`, `CenteredCriterion`, `Reduction`.
- `CenteredCriterion.lean` (added 2026-11-19, 0 sorries) machine-verified the constructive core used by every layer document: from `T ∣ (n·x)²` with `T ≡ −n·x (mod u)`, `u = 4x − n > 0`, it produces explicit positive `y, z` with `4·x·y·z = n·(x·y + x·z + y·z)`.
- `Reduction.lean` (added 2026-11-19, 0 sorries, 0 axioms) machine-verified the route-2 conditional reduction (`ROUTE2_CONDITIONAL_REDUCTION.md`): the scaling lemma (solution for `n` ⇒ solution for `n·k`), the **unconditional** coverage of every prime `n ≢ 1 (mod 24)`, and `full_conjecture_of_h24` — the full conjecture follows from the single-class hypothesis "every prime ≡ 1 (mod 24) has a representation". This strictly strengthens the standing determination: the hard core is now exactly one prime residue class.

**Resolved on 2026-11-19 (issue #6):**

- `NewTheorems.lean` — `decide` had exposed a **false witness** in `example_73` (4·20·263·51180 = 1,076,827,200 ≠ 1,057,711,600 = 73·(20·263 + 20·51180 + 263·51180), which does not satisfy 4/73). Replaced with the verified witness 4/73 = 1/20 + 1/210 + 1/30660; the module compiles and is built in CI. Its two unused axiomatic Burgess statements (`C_burgess`, `burgess_least_qnr_bound`) were removed — unproven analytic inputs belong in the completed conditional paper (ROADMAP #2), not as dead Lean axioms.
- `StructuralLemmas.lean` — tactic errors on v4.30.0 plus 5 unfinished goals, and imported by nothing. Formally retired to `lean-archive/orphan-modules/`.

**Unfinished goals** (census enforced by `scripts/audit_all.sh` §4): **17 `sorry`/`admit` proof terms across 8 files** — root project 3 (`OmegaCases.lean` ×3, enforced against the documented count), `lean-archive/` 14 (9 in the retired side projects, 5 in `orphan-modules/StructuralLemmas.lean`). Earlier comments claiming "zero sorries" predate the census and are flagged where they appear.

**Documented axioms** (whitelist enforced by `audit_all.sh` §5):

| Axiom | File | Meaning |
|---|---|---|
| `erdos_straus_mod_12_1_not_div_5_conjecture` | `Mod12Case1.lean` | **assumes the residual open class itself** (n ≡ 1 mod 12, 5 ∤ n, n ≥ 13) — the conjecture's hard core, taken as hypothesis; see `STATUS.md`. Machine-checked note (2026-11-19, `Reduction.lean`): its formal content follows from the strictly weaker hypothesis (H24) "every prime ≡ 1 (mod 24) has a representation"; see `ROUTE2_CONDITIONAL_REDUCTION.md` |
| `divisor_residue_criterion_reverse` | `DivisorResidue.lean` | reverse direction of the divisor-residue criterion |

Removed on cleanup passes: two placeholder axioms stated as `True` (`burgess_bound`, `grh_character_sum` — unused) on 2026-11-18, and the two unused axiomatic Burgess statements (`C_burgess`, `burgess_least_qnr_bound`) on 2026-11-19.

**Strongest honest theorem:** `erdos_straus_except_residual_open_class` (`MainTheorem.lean`) — everything except the residual open class, conditional on the whitelisted axioms. It compiles on the pinned toolchain and is in the CI build set.

**Retired** (`lean-archive/`): the `ErdosStrausLean/` and `ErdosStraus/` side projects (moved 2026-11-18) and `orphan-modules/StructuralLemmas.lean` (moved 2026-11-19 — see Resolved above). Do not build or cite these.

## CI

`.github/workflows/ci.yml` runs on every push/PR to main:

1. **smoke-math** — `scripts/smoke_test.py` (stdlib only): reproduces the exact-criterion sweep (51 cross-checked pairs, 0 mismatches, first-success distribution {3: 6, 7: 10, 11: 1}, the single u=11 case being exactly n = 1129).
2. **repo-audit** — `audit_all.sh` (convenience mode): sorry census vs documented count, axiom whitelist, and full certificate checks (the committed dataset `results/layer4_certificates.jsonl` — 166,011 records, verified per-record, max A = 107, exact domain coverage).
3. **lean-build** — elan + `lake exe cache get`, then the root library and the nine-module certified set.

The earlier workflows (`verify.yml`, `lean_action_ci.yml`) failed continuously on main from 2026-08-29 because they referenced files that do not exist (`code/verify.py`, `requirements.txt`, `paper/manuscript.tex`); they were retired and consolidated here (issue #5).

## Verify locally

```bash
# exact centered criterion cross-check (needs sympy)
python3 corrected_centered_criterion.py --limit 100000 --u-max 79

# centered verifier self-test (stdlib only)
python3 finite_abelian_centered_verifier.py

# CI smoke test (stdlib only; pins the n = 1129 regression)
python3 scripts/smoke_test.py

# repository audit (documented Lean state + axiom whitelist)
bash scripts/audit_all.sh

# Lean (toolchain pinned by lean-toolchain = Mathlib v4.30.0)
lake exe cache get && lake build
```

## Layout

- Verifiers: `corrected_centered_criterion.py`, `finite_abelian_centered_verifier.py`, `scripts/smoke_test.py`, `analysis/layer4/`
- Search pipelines: `verify_*.py` with results in `verification_*.json`
- Cascade and hard-case tools: `phase2_n1mod24.py`, `hard_case_scan.py`, `exact_residue_cascade.py`, `neg1_route_analysis.py`, and related scripts
- Documents: root `*.md` (some superseded — banners mark them); `paper/` holds the route-2 handout PDF (build artifact — regenerate with `scripts/build_route2_pdf.sh`, requires pandoc + Gotenberg on :3000)
- Retired Lean projects: `lean-archive/`
