# EXPERIMENT_LOG.md — Paper 2

One entry per run: what ran, on which verified population, the key results
(with counts and the bound named), artifacts, and status. An entry's claims
are bounded by its data; universal claims never enter via this log.

## E-001 — Lane L1: pigeonhole margin at first-working parameters (2026-11-24)

- **What ran:** `sweep_exact/collision_margin_engine.c` (v0.1,
  SHA-256-pinned in DATA_MANIFEST), sanitizer-built, self-tested on the four
  release anchors + the cross-direction no-collision check below the
  first-working parameter; full run over the verified hard-case population
  `[10^7, 10^9)`.
- **Populations:** sweep 3,194,231 (matches the published sweep exactly);
  (H24) 2,364,031; collisions found at 100% of first-working parameters
  (MISMATCH 0).
- **Key results:** pigeonhole-conclusive 3,177,642 (99.49%); delicate
  (collision present, `|D| ≤ φ(u)/2`) 16,589 (0.52%); the `u = 3` and `u = 7`
  layers 100% pigeon-conclusive; delicate concentrates at higher layers
  (17.4% at `u = 19`, 77.6% at `u = 43`, 100% at `u ≥ 67` incl. both `u = 83`
  record primes — small-residue collision pairs, e.g. `(1, 82)` with margin
  −58 for `651,412,441`).
- **Artifacts:** `analysis/collision_v01/` (run output, stderr,
  sanitized self-test, 5,000-row delicate sample), hashes in
  DATA_MANIFEST.
- **Status:** complete; feeds H-2 and the R2 layer-conditioning tests.

## E-002 — R2: modulo-5 separation quantification (2026-11-24)

- **What ran:** engine v0.2 (adds the intrinsic parametric/nonparametric
  classification from the verified mod-840 procedure and mod-5 × mod-840 ×
  layer cross-tabulation), sanitizer-built, same anchors.
- **Key results:** see the E-002 result block once verified — target tables:
  (i) nonparametric-only rate per `p mod 5` group (independent check of the
  review's 4.09% / 1.50% / 2.73×), (ii) delicate rate per `p mod 5` group,
  (iii) first-working-parameter distribution per group, (iv) margin histogram
  per group; the layer-conditioned test of H-1's falsification criterion.
- **Artifacts:** `analysis/mod5_separation_v02/`.
- **Status:** complete (results recorded below and in
  `analysis/mod5_separation_v02/`).

### E-002 results (verified run, engine v0.2)

- **Independent reproduction of the review's figures — exact:** over the
  mod-840 cohort, the nonparametric-only rate by `p mod 5`:
  `+1 (mod 5)`: 16,267 / 398,126 = **4.09%**; `−1 (mod 5)`:
  5,955 / 397,787 = **1.50%**; ratio **2.73x** — matching the twelfth
  review's 4.09% / 1.50% / 2.73x exactly. Cohort populations near-equal in
  size (398,126 vs 397,787): the separation is in the rates, not the sizes.
- **Full-sweep mod-5 breakdown (new):** `+1 (mod 5)`:
  41,226 / 1,064,669 = 3.87%; `p ≡ 3 (mod 5)` (a third group absent from the
  mod-840 restriction): 16,834 / 1,065,189 = **1.58% — the lowest of all**;
  `−1 (mod 5)`: 31,023 / 1,064,373 = 2.91%; `p ≡ 2 (mod 5)`: no population.
  Notable: **no `p ≡ 3 (mod 5)` prime is classified only-parametric**
  (onlypar = 0 in that group) — an unexplained structural zero, logged for
  R3.
- Intrinsic classes over the mod-840 cohort (per class, onlypar/both/onlynon):
  `1: 5,648/118,829/5,502`; `121: 4,969/119,966/5,028`;
  `169: 2,224/125,512/1,939`; `289: 1,293/126,864/1,916`;
  `361: 6,189/126,258/5,737`; `529: 2,420/133,519/2,100`. Per-class totals and
  onlynon agree exactly with the ninth review's independently computed table.
- **Open reconciliation item (disclosed):** the onlyparam/both **split** —
  22,744 vs the review's 22,743 (one prime, class 529, classified
  only-parametric here; the review's engine aggregated it as both-type — or
  vice versa at aggregation). One prime in 795,913 (0.00013%); every other
  aggregate matches exactly. Tracked, not papered over: the two engines'
  candidate-enumeration orders differ in one corner (their structured
  `{1, p, p²} × {1, x, x²}` loop re-examines candidates the sorted-divisor
  loop also covers, with different early-break sequences), and the
  distinguishing prime can be isolated by a per-record diff once the review's
  per-record data is shared.
- **Bugs caught by the reconciliation (both fixed before any figure ships):**
  (i) the divisor-list cap (4096) silently truncated the candidate set for
  divisor-rich `x` — the layer-workflow's "capped loop reclassifies records"
  class; (ii) a 64-bit `p²·x` overflow in the candidate products — the same
  V14-01 overflow class. All candidate arithmetic now 128-bit, the divisor
  table uncapped with a hard assert.
- **Artifacts:** `analysis/mod5_separation_v02/` (engine v0.2, run output
  `full_run.txt`, stderr — sanitizer-silent — and the sanitized self-test),
  hashes below in DATA_MANIFEST.
- **Status:** complete. H-1 remains open (not layer-conditioned to
  resolution yet): the next sub-run cross-tabulates first-working layers by
  mod-5 group to test H-1's falsification criterion #1.

## E-003 — R4: collision equivalence formalized (pending)

Target: `ErdosStrausConjecture/ResidualPrimes/CollisionReachability.lean`,
theorem `opposite_collision_iff` (the collision equivalence) and
`pigeonhole_reachability` (the cardinality bound), 15 → 17 audited principal
theorems, CI-gated.
