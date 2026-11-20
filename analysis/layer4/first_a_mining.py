#!/usr/bin/env python3
"""First-A structure mining over results/layer4_certificates.jsonl.

Extracts the empirical structure of the first-working parameter A across
the 166,011 certified admissible primes (<= 10,000,000):

  T1  distribution of first-A values (and cross-checks against the
      documented cascade layer counts);
  T2  the class split mod 24 (A = 3 should be exactly the prime class
      n = 13 (mod 24), per theorem2);
  T3  per-A structural fingerprints: v2(x) profile, n mod 4A residues;
  T4  the covering table: n mod 96 slices -> admissible first-A sets,
      counts, and observed maxima.

Stdlib only. Reproducible: read-only over the committed dataset.
"""
import json
import sys
from collections import Counter, defaultdict

PATH = "results/layer4_certificates.jsonl"


def v2(m: int) -> int:
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def main() -> None:
    counts_a = Counter()
    mods24_by_a = {a: Counter() for a in ()}
    classes24 = Counter((a,) for a in ())
    a_by_class24 = defaultdict(Counter)
    x_by_a = defaultdict(Counter)
    mod4a_by_a = defaultdict(Counter)
    mod8_a3 = Counter()
    slice_mod96 = defaultdict(Counter)
    mod28_a7 = Counter()
    total = 0
    worst = 0
    with open(PATH) as f:
        for line in f:
            r = json.loads(line)
            n, a, x = r["n"], r["A"], r["x"]
            total += 1
            worst = max(worst, a)
            counts_a[a] += 1
            c24 = n % 24
            a_by_class24[c24][a] += 1
            x_by_a[a][v2(x)] += 1
            mod4a_by_a[a][n % (4 * a)] += 1
            if a == 3:
                mod8_a3[n % 24] += 1
            if a == 7:
                mod28_a7[n % 28] += 1
            slice_mod96[n % 96][a] += 1

    print(f"total records: {total}")
    print(f"distinct A values: {len(counts_a)}; max A = {worst}")
    print("\nT1. first-A distribution:")
    for a in sorted(counts_a):
        print(f"  A={a:3d}: {counts_a[a]:7d}")
    print("\nT2. records by n mod 24:")
    for c in sorted(a_by_class24):
        print(f"  class {c:2d}: {sum(a_by_class24[c].values()):7d} "
              f"(top A: {sorted([(k, v) for k, v in a_by_class24[c].items()], key=lambda t: -t[1])[:4]})")
    print("\nT2b. A=3 records by n mod 24:")
    for c in sorted(mod8_a3):
        print(f"  {c:2d}: {mod8_a3[c]:6d}")
    print("\nT3a. v2(x) profiles per A (top values):")
    for a in sorted(x_by_a):
        print(f"  A={a:3d}: {dict(sorted(x_by_a[a].items()))}")
    print("\nT3b. n mod 4A residues per A (top 6 residues):")
    for a in sorted(mod4a_by_a):
        top = sorted(mod4a_by_a[a].items(), key=lambda t: -t[1])[:6]
        print(f"  A={a:3d}: residues={dict(top)} distinct={len(mod4a_by_a[a])}")
    print("\nT4. covering table by n mod 96 (slice -> A-set / count / max):")
    for s in sorted(slice_mod96):
        a_set = slice_mod96[s]
        print(f"  n%96={s:2d}: count={sum(a_set.values()):7d} maxA={max(a_set):3d} "
              f"As={sorted(a_set)}")
    print("\nT4b. cross-checks vs documented cascade layers:")
    print(f"  count(A=35)={counts_a.get(35, 0)} count(A>=39)="
          f"{sum(v for k, v in counts_a.items() if k >= 39)} "
          f"(MOD35 doc: 26 succeed / 67 fail of 93)")
    print(f"  count(A=31)={counts_a.get(31, 0)} (u31 stage: 283 entrants)")
    return


if __name__ == "__main__":
    main()
