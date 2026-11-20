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

## 7. Corrected u = 35 cohort and the saturation lemma

Re-run over the true cohort (`analysis/u35_layer_corrected.py`,
`analysis/u35_layer_corrected.json`): entrants 65 (first-A ≥ 35), successes 17
(first-A = 35), failures 48 (first-A ≥ 39). Results:

- **Exact verdict vs dataset:** 0 mismatches on all 65.
- **Coupled-CRT span criterion vs exact:** 0 mismatches on all 65.
- **Purity:** NO record in the cohort — success or failure — is QR-pure at 5
  or at 7. This is structural, not empirical: the forced factor 3 of
  x = (n+35)/4 has log pair (3, 1), odd in both components, so the old
  claim "all failures are non-QR-pure" was trivially true of the whole
  cohort. The discriminator is not purity.
- **Component-wise relaxations do not separate:** single-component integer
  spans explain only 10 of the 48 failures; the remaining 38 fail purely
  through the coefficient coupling.
- **Subgroup relaxation:** dropping all exponent caps, the generated
  subgroup of (Z/4) × (Z/6) contains (2,3) on 63 of 65 records; the two
  exceptions (n = 878,641, n = 7,559,161) fail only through exponent
  bounds.

**Saturation lemma (proved; applies at u = 35).** In the coupled span check,
the coefficient acting on a factor with log pair (a, b) may be reduced
modulo 12, because the 5-component is periodic with period 4, the
7-component with period 6, and their lcm is 12. Consequently every exponent
cap m may be replaced by min(m, 6) without changing the criterion; in
particular, when every exponent is ≥ 6 the criterion collapses to the
subgroup condition of (Z/4) × (Z/6). This is why the two exceptions above
are exactly the bound-limited records.

**Status of the closed form.** A residue-class closed form for the u = 35
stage does not follow from these data: the criterion depends on the
factorization structure of n(n+35)/4 (the log pairs), not only on a residue
of n. The exact bounded coupled-span check, with the saturation reduction,
remains the working criterion; the compact form stays deferred.

## 9. Corrected u = 31 cohort and its fingerprints

Re-run over the true cohort (`analysis/u31_layer_corrected.py`,
`analysis/u31_layer_corrected.json`): entrants 217 (first-A ≥ 31), successes
152 (first-A = 31), failures 65 (first-A ≥ 35). Results:

- **Exact verdict vs dataset:** 0 mismatches on all 217. **Log-span
  criterion (root 3, target 15) vs dataset:** 0 mismatches on all 217.
- **QR-pure obstruction:** 47 of the 65 failures are QR-pure at 31, and 0
  successes are — the parity-obstruction direction holds on the corrected
  cohort (this analysis is meaningful at u = 31, unlike u = 35: the forced
  factor 2 has even log, log₃2 = 24).
- **Cube-QNR rescue:** 0 of 65 failures admit a rescue witness (direction
  unchanged); 15 of the 152 successes are covered by the simple witness
  form, the rest by wider spans.
- **Span-delicate failures (non-QR-pure, no rescue): 18** — was 33 in the
  deprived chain. Failure slices by n mod 96: {1: 23, 25: 14, 49: 13,
  73: 15}; failure first-A histogram {39: 22, 47: 15, 35: 17, 43: 5, 51: 1,
  55: 2, 59: 2, 107: 1}.

## 11. u = 39 layer (new work, corrected semantics from the start)

`analysis/u39_layer.py` / `analysis/u39_layer.json`,
`MOD39_EXACT_REDUCTION.md`: u = 3·13, cohort 48 entrants (22 solve, 26
fail); exact criterion and coupled span verified 0/48 both ways; reduced
parity-coupled criterion (13-span reach with odd weight on the 2-mod-3
primes) verified 48/48; saturation at min(m, 6) (periods 2 and 12, lcm
12); subgroup relaxation exact on 46/48 (bound-limited exceptions
n = 118,801 and n = 1,915,201); purity structurally dead (forced 2 has log
pair (1, 1)); compact residue-form deferred. One more layer now carries
corrected, dataset-grounded semantics.

## 12. Reproduce

```bash
python3 analysis/layer4/first_a_mining.py            # T1-T4 tables
python3 analysis/layer4/forced_subclass_reconcile.py # base decomposition + chains
```
