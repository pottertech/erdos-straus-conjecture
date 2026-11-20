# First-A Structure: the Empirical Covering Table and Corrections to the Stage Chain

**Date:** 2026-11-19
**Source data:** `results/layer4_certificates.jsonl` (166,011 admissible primes ≤ 10^7, per-record verified)
**Scripts:** `analysis/layer4/first_a_mining.py`, `analysis/layer4/forced_subclass_reconcile.py`

## 1. The first-A distribution (T1)

Over all 166,011 admissible primes (n ≡ 1 mod 12, n prime), the first-working
parameter A distributes as:

| A | count | A | count |
|---:|---:|---:|---:|
| 3 | 130,261 | 31 | 152 |
| 7 | 28,606 | 35 | 17 |
| 11 | 4,463 | 39 | 22 |
| 15 | 949 | 43 | 5 |
| 19 | 883 | 47 | 15 |
| 23 | 541 | 51 | 1 |
| 27 | 91 | 55 | 2 |
| 59 | 2 | 107 | 1 |

Max A = 107, attained once, at n = 8,803,369 (structured subclass; first works
at u = 107).

## 2. The class split (T2)

- Every record with n ≡ 13 (mod 24) — 83,124 of them — has first-A = **3**
  (Theorem 2 / the P = 2 path). No exceptions.
- The A > 3 records (35,750) all have n ≡ 1 (mod 24): exactly the residual
  class. First-A > 3 ⟺ n ≡ 1 (mod 24) ∧ the A = 3 criterion fails.

## 3. Covering table by n mod 96 (T4)

| n mod 96 | count | max A | admissible A-set |
|---|---:|---:|---|
| 13 | 20,824 | 3 | {3} |
| 37 | 20,734 | 3 | {3} |
| 61 | 20,802 | 3 | {3} |
| 85 | 20,764 | 3 | {3} |
| 1 | 20,716 | 55 | {3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55} |
| 25 | 20,700 | 59 | {3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 47, 55, 59} |
| 49 | 20,769 | 59 | {3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 59} |
| 73 | 20,702 | 107 | {3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 107} |

Four of the eight slices are pure A = 3 (all ≡ 13 mod 24). Per-record
verified. This is the empirical covering table the (H24) analysis needs:
first-A is constant 3 on the 13-mod-24 slices and takes 14 further values,
max 107, on the 1-mod-24 slices.

## 4. Two corrections to the documented stage chain

**4.1 The base set.** `is_hard_prime` (the corrected-cascade base) does not
exclude n ≡ 13 (mod 24). Its b₃ test flags 48,711 "corrected prime hard
cases", of which **12,961 are 13-mod-24 primes already solved at A = 3 by the
P = 2 path**. The true residual hard-case base is **35,750** (= exactly the
records with first-A > 3). The number 48,711 is internally exact but its
label overstates the residual class by the phantom count.

**4.2 The layer set.** The documented sequence of stages is
u ∈ {7, 11, 15, 23, 31, 35, 39, 43, 47, 51, 55, 59, 63} — it omits the
admissible values **19 and 27** (both ≡ 3 mod 4; 19 prime, 27 = 3³). The
omission is decisive: the documented stage counts (7,272 → 2,137 → 1,054 →
681 → 283 → 93 → 67 → …) are the exact counts of a chain that never tests
19 or 27. Of the documented 283 "u = 31 stage entrants", **174 are cases
whose true first-A is 19 (133) or 27 (41)**. The per-record verdicts inside
the chain were each independently verified exact at u = 31 (0 mismatches,
span vs exact), so the counts are true counts *of the deprived chain* —
they are not the residual narrowing.

**4.3 The true chains.** With the full admissible u-set and the exact
criterion, over the structured subclass (the doc's 7,272) and over the full
residual class:

| after stage | structured subclass | full residual class |
|---|---:|---:|
| base | 7,272 | 35,750 |
| u = 7 | 2,137 | 7,144 |
| u = 11 | 1,054 | 2,681 |
| u = 15 | 681 | 1,732 |
| u = 19 | 388 | 849 |
| u = 23 | 150 | 308 |
| u = 27 | 109 | 217 |
| u = 31 | 35 | 65 |
| u = 35 | 23 | 48 |
| u = 39 | 14 | 26 |
| u = 43 | 12 | 21 |
| u = 47 | 4 | 6 |
| u = 51 | 3 | 5 |
| u = 55 | 2 | 3 |
| u = 59 | 1 | 1 |
| u = 107 | 0 | 0 |

True u = 31 stage (full residual class): entrants 217, solve 152, fail 65.
True u = 35 stage: entrants 65, solve 17, fail 48. Both chains terminate:
**every residual prime ≤ 10^7 is settled**, the last at u = 107
(n = 8,803,369). The single-survivor record is unchanged.

## 5. What stays valid, what changes

- The span-criterion analyses in `MOD31_EXACT_REDUCTION.md` and
  `MOD35_CRT_SPAN.md` were verified per-record against the exact criterion
  with 0 mismatches on the entrant sets they name; those verifications stand.
  The *cohort semantics* change as above: the true u = 31 failure cohort is
  the 65-case set (structured: 35), not the 93-case deprived chain.
- The layer counts in `DETERMINISTIC_CASCADE_STATUS.md` and the two layer
  documents carry correction banners pointing here; the residual
  99.42 %-reduction claim is replaced by the corrected chains (full
  residual: 35,750 → 217 after u = 27 → 1 after u = 59; termination by the
  certificate data through u = 107).
- No covering theorem is claimed by this data — these are per-record
  verified facts through 10^7, and termination of the u-method on the
  residual class remains an empirical observation, not a theorem.

## 6. Reproduce

```bash
python3 analysis/layer4/first_a_mining.py            # T1-T4 tables
python3 analysis/layer4/forced_subclass_reconcile.py # base decomposition + chains
```
