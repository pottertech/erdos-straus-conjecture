# The Non-Parametric Tail of the Exact-Criterion Sweeps (full admissible u-set)

**Date:** 2026-11-22 (second revision: full admissible u-set after external
review F-01/F-02)
**Data:** `sweep_exact/nonparametric_1e7_1e9.jsonl` (317,569 records, full
witnesses), produced by `sweep_exact/sweep_dump_nonparametric.c`.
Companion to `LAYER_SWEEP_43_TO_107.md` and `FIRST_A_STRUCTURE.md`.

## History of this measurement

- 2026-11-21 first resolution run: committed with a `nonp[1024]` capture
  array — every aggregate that said "1,024 non-parametric (0.032%)" was a
  capture-cap artifact.
- Cap removed (`sweep_dump_nonparametric.c`): 327,504 records — but with a
  **prime-only** u-set (the engine's u-list enumerated primes only, missing
  composite layers 15, 27, 35, 39, 51, 55, 63, 75).
- **External review F-01 (2026-11-22)** produced an exact certificate
  resolving `n = 32,349,601` at `u = 15` — a composite the engine never
  tested (the engine had reported first-u = 227 for it). Both engines were
  fixed to the **full admissible u-set** (every integer `u ≡ 3 (mod 4)` up
  to 251), with the three review anchors added to the self-test
  (`1129 → 11`, `8803369 → 107`, `32349601 → 15`); 0 mismatches.

## Headline correction (full u-set)

| cohort | hard cases (exact criterion) | non-parametric | share |
|---|---:|---:|---:|
| `≤ 10^7` (certificate layer, class 1 mod 24 only) | 35,750 | 7,545 | 21.1%; 4.5% of all admissible primes |
| `[10^7, 10^9)` (dump, full u-set) | 3,194,231 | 317,569 | **9.94%** |

The non-parametric share **declines with range**. Terminology:
*parametric* = the first-found witness has `z ≡ 0 (mod y)` (the shape the
identity families produce); *non-parametric* = every other shape.

## Stage-level corrections from the full u-set

- **Max first-working u collapses to 83** (at `n = 287,567,281`); the
  prime-only engine's 227 (and the 15-layer cases it could not see) were
  artifacts of the restricted u-set. The recorded distribution
  (`verification_10M_1B_exact_rerun.json`): `3: 830,200; 7: 1,949,770;
  11: 279,515; 15: 59,759; 19: 42,804; 23: 21,626; 27: 3,818; 31: 4,668;
  35: 691; 39: 733; 43: 192; 47: 303; 51: 36; 55: 49; 59: 44; 63: 10;
  67: 2; 71: 6; 75: 2; 79: 1; 83: 2`.
- **0 failures** persists at `u ≤ 251` with the full set.
- Parity interaction (external review F-02): `x = (n+u)/4` is even for
  `n ≡ 5 (mod 8)` at `u ≡ 3 (mod 8)` and for `n ≡ 1 (mod 8)` at
  `u ≡ 7 (mod 8)` — so the retired verifiers' missing-factor-2 bug struck
  **both prime classes at alternating parameter parities**, not one class.
- The certificate layer (`≤ 10^7`) was already generated with the full
  admissible u-set: its first-A distribution (and max A = 107) required no
  correction.

## Structure of the tail (the 317,569 records, full u-set)

- **Layer concentration:** 235,501 (74%) at `u = 7`; 44,434 at `u = 11`;
  11,400 at `u = 15`; 14,733 at `u = 19`; 7,167 at `u = 23`; 1,585 at
  `u = 27`; 1,831 at `u = 31`; the remaining layers ≤ 1,500 each. The
  composite layers enter the tail exactly as they enter the first-worked
  distribution.
- **Slices:** `n mod 96 ∈ {1: 137,672, 49: 135,957, 25: 22,684,
  73: 21,256}` — the `v₂(x) ≥ 2` slices hold **86%** of the tail.
- **Population:** all records are `n ≡ 1 (mod 24)`; the class-13 half of
  the sweep cohort (830,200 records at `u = 3`) is parametric without
  exception.
- **Witness asymmetry:** `log₂(z/y)` spreads broadly (mass at 20–55);
  `z mod y` distinct across probed cohorts; `gcd(y, z)` large. No small
  closed family separates the tail by direct probes.

## Covering shape (revised and honest)

Identity-shaped families carry ≈ 90% of the hard cohort and *gain share
with range*; the remaining ~10% are exactly the span machinery's domain.
A finite closed set of residue families covering the tail is not supported
by these probes; the covering conjecture's viable form is an **effective
covering bound `B(n)` over the span classes** (paper §6.3, §6.5), with the
finite-search equivalence `0 < u ≤ 2p, u ≡ 3 (mod 4), p ∤ u` (added to the
paper at review) bounding the search domain for each prime.

## Reproduce

```bash
cc -O2 -o sweep_dump_nonparametric sweep_dump_nonparametric.c -lm
./sweep_dump_nonparametric --selftest    # three anchors + brute cross-check
./sweep_dump_nonparametric 10000001 999999999 nonparametric_1e7_1e9.jsonl > dump_summary.json
```
