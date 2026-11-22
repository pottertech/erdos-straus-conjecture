# The Non-Parametric Tail of the Exact-Criterion Sweeps

**Date:** 2026-11-21
**Data:** `sweep_exact/nonparametric_1e7_1e9.jsonl` (327,504 records, full
witnesses), produced by `sweep_exact/sweep_dump_nonparametric.c` — a
variant of the committed exact-criterion sweep engine with the
non-parametric capture cap removed. Companion to `LAYER_SWEEP_43_TO_107.md`
and `FIRST_A_STRUCTURE.md`.

## Why this document exists

The first resolved sweep run
(`sweep_exact/verification_10M_1B_exact_rerun.json`, committed with the
same-day reconciliation) stored non-parametric records in a fixed
`nonp[1024]` capture array. Every subsequent aggregate that said
"1,024 non-parametric first-hits, 0.032%" therefore reported a **capture
cap**, not a measurement. The uncapped dump below is the measurement.

## Headline correction

| cohort | hard cases (exact criterion) | non-parametric | share |
|---|---:|---:|---:|
| `≤ 10^7` (certificate layer) | 48,711 | 7,545 | 15.5% of the hard cohort; 4.5% of all admissible primes |
| `[10^7, 10^9)` (dump) | 3,194,231 | 327,504 | **10.25%** |

Terminology: *parametric* = the first-found witness has `z ≡ 0 (mod y)` —
the shape the six identity families produce. *Non-parametric* = every other
witness shape. The share **declines with range** (15.5% → 10.25%): the
identity-shaped families gain ground as `n` grows, but they do not close
the population.

## Structure of the tail (the 327,504 records)

- **Layer concentration:** 235,501 (72%) at `u = 7`; 44,434 at `u = 11`;
  26,327 at `u = 19`; 12,884 at `u = 23`; 5,349 at `u = 31`; the remaining
  layers ≤ 10^3-ish each. The tail is a *small-`u`* phenomenon.
- **Slices:** `n mod 96 ∈ {1: 140,738, 49: 141,317, 25: 23,713,
  73: 21,736}` — the `v₂(x) ≥ 2` slices `{1, 49}` hold **86%** of the tail,
  matching the forced-2 structure of `FIRST_A_STRUCTURE.md` §4.
- **Population:** all 327,504 records are `n ≡ 1 (mod 24)` (the class-13
  half is parametric at `A = 3`: 0 of its 830,200 sweep cases appear in the
  tail — purity of that class is structural).
- **Witness asymmetry:** `log₂(z/y)` spreads over ≈ 1–55 with a broad mass
  at 20–55 — genuinely asymmetric three-term solutions, not
  near-degenerate pairs; `z mod y` is distinct across probed cohorts (no
  small-remainder family), and `gcd(y, z)` is large (roughly
  `2^{log₂ y − small}`), so classical two-parameter family tests do not
  separate them.
- **Divisor shape:** every `u = 7` sub-tail record found its first witness
  with `d₁` a pure divisor of `x²` (no `n`-power factor in the first-found
  pair).

## What this means for the covering story

- The **identity-families + span-machinery** split is the right empirical
  description: ≈ 90% of hard cases resolve inside the closed identity
  families and 10% inside the span criterion's algorithmic domain — with
  the span side shrinking as a share.
- A *finite closed set of residue families covering the tail* is **not**
  supported by these probes; the honest covering-conjecture shape for
  ROUTE2's §6.3 remains: an effective covering bound `B(n)` proved over
  the span classes, with the tail characterized algorithmically (Section
  6.1 of the paper), not by residue closure.
- The ≤ 10^7 certificate layer's per-record non-parametric share (7,545)
  is now reproducible from committed data alone:
  `sum(r['z'] % r['y'] != 0 for r in records)`.

## Reproduce

```bash
cc -O2 -o sweep_dump_nonparametric sweep_dump_nonparametric.c -lm
./sweep_dump_nonparametric --selftest                       # 0 mismatches
./sweep_dump_nonparametric 10000001 999999999 nonparametric_1e7_1e9.jsonl > dump_summary.json
python3 - <<'EOF'
import json
recs = json.load(open("nonparametric_1e7_1e9.jsonl"))
print(len(recs))   # 327504
from collections import Counter
print(Counter(r["u"] for r in recs))
EOF
```
