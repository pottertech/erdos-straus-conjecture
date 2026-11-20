# Mod-35 Layer: Coupled-CRT Span, Forced Factor 3

> **⚠️ Correction (2026-11-19, `FIRST_A_STRUCTURE.md`):** this document's 93
> stage entrants come from the deprived chain analyzed in
> `MOD31_EXACT_REDUCTION.md` (layer set omits u = 19 and 27). The true
> u = 35 stage over the full residual class has **65 entrants (17 solve,
> 48 fail)**. The coupled-CRT criterion is re-verified on the corrected
> cohort with **0 mismatches vs the exact criterion** and 0 vs the verified
> dataset (`analysis/u35_layer_corrected.py`); see `FIRST_A_STRUCTURE.md` §7
> for the cohort, the structural purity note, and the saturation lemma.
> The criterion itself is unchanged and exact.

**Date:** 2026-11-19
**Status:** exact criterion (coupled-CRT span) verified with 0 mismatches on all 93 stage entrants ≤ 10^7; compact closed form deferred — see "Why the coupled case is harder"

## Setup

For `u=35 = 5·7` and `n ≡ 1 (mod 24)`, writing `n = 24m + 1`:

\[
x=\frac{n+35}{4}=6m+9=3(2m+3),
\]

so the forced factor is

\[
\boxed{3\mid x}
\]

(with `v_3(x) = 1 + v_3(2m+3)`; no forced 2). If `35 | nx` the divisor pair
`d_1 = d_2 = nx` works and the layer succeeds trivially.

## Structure

`(Z/35Z)^× ≅ (Z/5)^× × (Z/7)^×` (cyclic orders 4 and 6; generators 2 and 3).
Targets: `−1 = (2^2 mod 5, 3^3 mod 7)` — component logs `(2, 3)`.
The forced factor `3` has component logs `(3, 1)`: **odd in both components.**

The exact criterion for `u=35` is the coupled span:

\[
u\text{-method succeeds}\iff (2,3)\in\Big\{\sum_p c_p(a_p,b_p): |c_p|\le e_p\Big\}
\]

where `(a_p, b_p)` are the component logs of `p^e ‖ nx` (None for unit
residues) and the **same coefficient `c_p` acts in both components**. This
coupling is what distinguishes composite moduli from the prime-modulus layers.

## Verification (2026-11-19, run through the OSR stack)

`analysis/u35_layer_analysis.py` (pack venv, SymPy), data in
`analysis/u35_layer.json`:

- entrants = the 93 survivors of the `u=31` stage;
- exact split: **26 succeed, 67 fail** (matches the documented table: 67
  survivors after `u=35`);
- coupled-CRT span vs exact criteria on all 93 entrants: **0 mismatches**;
- **all 67 failures are non-QR-pure at 35** — with the forced `3` carrying
  odd logs in both components, the prime-modulus parity argument (used at
  u=31 for 60/93) has no analogue; failures here are coupled-CRT misses.

## Why the coupled case is harder (and what is deferred)

At prime moduli the even-log warehouse factorizes a parity argument; here the
per-factor coefficient couples the mod-4 and mod-6 components, so sufficiency
arguments (like the cube-QNR witness at u=31) must construct coefficients that
simultaneously hit `-1` in `(Z/5)^×` and `(Z/7)^×`. The full residue-class
closed form for the 67 survivors is deferred; the span criterion above is
exact and verified. This block is the working form for the hybrid termination
route (ROADMAP #3).
