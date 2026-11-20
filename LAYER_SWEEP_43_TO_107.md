# Completing the Chain: Stages 43, 47, 51, 55, 59, 63, 107 (Corrected Cohorts)

**Date:** 2026-11-19
**Script/data:** `analysis/layer_sweep_43_107.py`, `analysis/layer_sweep_43_107.json`
**Semantics:** corrected cohorts from the start (`FIRST_A_STRUCTURE.md` §4.3):
entrants at u = records with first-A ≥ u; solve = first-A = u; fail = first-A > u.

## The verified table

| u | structure | forced | entrants | solve | fail | exact vs dataset | span vs exact | subgroup rel. |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 43 | C₄₂ (g=3), prime | none (v₂(x)=0 ∀) | 26 | 5 | 21 | 0 | 0 | 12 wrong |
| 47 | C₄₆ (g=5), prime | 2 and 3 (both QR) | 21 | 15 | 6 | 0 | 0 | 0 |
| 51 | C₂×C₁₆ (3·17) | none (v₂=0, 3∤) | 6 | 1 | 5 | 0 | 0 | 0 |
| 55 | C₄×C₁₀ (5·11) | 2 (odd log) | 5 | 2 | 3 | 0 | 0 | 0 |
| 59 | C₅₈ (g=2), prime | 3 (even log) | 3 | 2 | 1 | 0 | 0 | 1 |
| 63 | C₂×C₆ (3²·7) | 2 | 1 | 0 | 1 | 0 | 0 | 0 |
| 107 | C₁₀₆ (g=2), prime | — | 1 | 1 | 0 | 0 | 0 | 0 |

The **exact criterion agrees with the verified first-A dataset on all 42
records** across the seven stages, and the span criterion agrees with the
exact criterion on all of them. With this, **every stage of the corrected
chain 7 → 43 → 47 → 51 → 55 → 59 → 63 → 107 is characterized by span
methods, verified record by record**, and the chain terminates:
n = 8,803,369 fails u = 63 and solves at u = 107.

## Structural notes per layer

- **u = 43** (prime, no forced factor — x = 6m+11 is odd or even with m,
  never 2- or 3-divisible): single cyclic component C₄₂, target log 21.
  The subgroup relaxation (exponent caps dropped) is wrong on 12 of the 26
  records — at this layer the exponent bounds are the obstruction, unlike
  u = 35/47/51/55 where the relaxation is exact or nearly so. The bounded
  span check is the working criterion.
- **u = 47** (prime; x = 6m+12 forces both 2 and 3, both quadratic
  residues mod 47 — logs even): the parity argument is *alive* at this
  layer, and the subgroup relaxation is exactly right (0 wrong on all 21).
- **u = 51** (3·17; x = 6m+13: no forced factors): C₂×C₁₆; the C₂-component
  is automatic when an odd-class factor exists; subgroup exact (0/6).
- **u = 55** (5·11; x = 2(3m+7) forces 2 with an ODD 11-log): C₄×C₁₀;
  subgroup exact (0/5).
- **u = 59** (prime; x = 3(2m+5) forces 3, a QR mod 59): C₅₈; subgroup exact
  except 1 bound-limited record (of 3).
- **u = 63** (3²·7; terminal record fails), then **u = 107** solves it: the
  terminal case is exact at both stages.

## Saturation (general form)

For a layer with component orders d₁,…,d_k (Cyclic C_{d_i}), pair
coefficients are periodic modulo lcm(d₁,…,d_k); the exponent caps may be
replaced by min(mᵢ, L/2) where L = lcm. Applied: cap 21 (u=43), 23 (47),
8 (51, lcm 16), 10 (55, lcm 20), 29 (59), 53 (107).

## What remains (unchanged)

No covering theorem: each stage's span criterion is verified per record ≤
10^7, but no theorem predicts the survivor counts, and the u = 35/39-style
compact residue-class forms remain deferred (criterion is
factorization-dependent). The corrected chain — every stage now
characterized — is the base the hybrid termination route (ROADMAP #3)
would have to prove termination for. Termination through 10^7, terminating
at the single u = 107 record, remains an empirical fact, not a theorem.

## Reproduce

```bash
~/repos/openclaw-scientific-reasoning/.venv/bin/python analysis/layer_sweep_43_107.py
```
