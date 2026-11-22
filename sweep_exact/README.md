# Exact-criterion sweep re-run (2026-11-21)

Corrected, independently re-implemented replacement for the retired hard-case
sweep artifacts. Everything here runs under the exact one-divisor criterion
(`CENTERED_PRODUCT_SET_THEOREM.md`: exists `d | (n·x)^2` with
`d ≡ -n·x (mod u)`, `gcd(M, u) = 1`, `u = 4x - n` prime ≡ 3 (mod 4) ≤ 251).

## Files

- `exact_span_sweep.c` — C engine, predicates mirrored 1:1 from the committed
  verifiers (`verify_10M_to_1B.py`: prime population via `check_B3_fast`,
  two-branch divisor enumeration, `is_parametric` = `z % y == 0` on the
  first-found pair). Built-in self-test: independent brute-force enumeration
  on prime hard cases in `[10^5, 3·10^5)` (1,326 cases, 0 mismatches) plus the
  pinned regression anchor `n = 1129 → first u = 11`.
- `verification_10M_1B_exact_rerun.json` — `[10^7+1, 10^9)`:
  3,194,231 / 3,194,231 solved, 0 failures, max first-u 227 (n = 32,349,601).
  Reconciles the committed `verify_10M_to_1B.py` population exactly.
- `verification_100M_1B_exact_rerun.json` — `[10^8+1, 10^9)`:
  2,850,823 / 2,850,823 solved, 0 failures, max first-u 167 (n = 332,555,521).
  Total reconciles exactly with the sum of the committed `corrected.py`
  sub-range artifacts (345,956 + 2,504,867).
- `no_solution_at_large_u.py` / `no_solution_at_large_u.json` — targeted
  follow-up on the 7 cases `verify_10M_to_1B.py` recorded as unsolved within
  `u ≤ 251`: **all 7 resolve under the exact criterion within `u ≤ 251`**
  (first u ∈ {3, 31, 71, 151}).
- `seven_case_witnesses.json` — independent sympy-verified witnesses
  (`d1, d2, y, z` + the exact identity `4xyz = n(xy+xz+yz)`) for all 7.

## What was wrong with the retired artifacts

1. `verification_100M_1B.json` (2,852,233 claimed) — produced before the
   2026-08-28 verifier correction by a script using the withdrawn
   three-target shortcut `{-x·n^j}` (not equivalent to the exact criterion)
   and a different membership predicate (pollard-rho fallback instead of
   `check_B3_fast` trial-to-50000); its total matches no artifact family.
2. `verify_10M_to_1B.py` — despite using the exact criterion, its `factor_x`
   divides by **odd primes only** (no 2). For `n ≡ 13 (mod 24)`, `x` is even
   at every admissible `u`, so its divisor enumeration was corrupted on
   exactly that half of the population: the 7 recorded "no solutions" are
   spurious (witnesses above), and the 21.3% non-parametric share is an
   enumeration artifact — the run's own `nonp[1024]` capture array **capped at 1,024**: the
   uncapped re-run (`sweep_dump_nonparametric.c`, committed next to this file) streams
   every record and finds **327,504 / 3,194,231 = 10.25%**
   (`nonparametric_1e7_1e9.jsonl`, each with its full witness; 15.5% of the ≤10^7 hard
   cohort — 7,545 records in the certificate layer — so the identity-shaped families gain
   share as the range grows).
   `factor_x` treats any post-trial remainder as a single prime and iterates
   a non-ascending divisor list with a break-at-limit — both silently drop
   valid divisors.

## Reproduce

```bash
cc -O2 -o exact_span_sweep exact_span_sweep.c -lm
./exact_span_sweep --selftest
./exact_span_sweep 10000001 999999999 > verification_10M_1B_exact_rerun.json 2> sweep.log
./exact_span_sweep 100000001 999999999 > verification_100M_1B_exact_rerun.json 2> sweep100.log
python3 no_solution_at_large_u.py
python3 - <<'EOF'   # re-verify the 7 witnesses (summary)
import json
w = json.load(open("seven_case_witnesses.json"))
print(all(c["identity_verified"] for c in w["cases"]), len(w["cases"]))
EOF
```
