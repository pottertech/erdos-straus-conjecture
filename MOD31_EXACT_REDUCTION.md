# Exact Mod-31 Reduction from the Forced Factor 2

**Date:** 2026-11-19
**Status:** exact criterion stated and verified (0 mismatches, all 283 stage entrants ≤ 10^7); QR-pure and cube-QNR components proved; full residue-class closed form open (see "What remains")

## Setup

After the shift-divisor reduction we have

\[
n\equiv1\pmod{24}.
\]

For `u=31`,

\[
x=\frac{n+31}{4}=\frac{(24m+1)+31}{4}=6m+8,
\]

hence

\[
\boxed{2\mid x}\qquad\text{but } 3\nmid x\ \text{in general},
\]

so the forced centered generator is `2` only (unlike `u=23`, where `6 | x` forces
both 2 and 3). Writing `n = 24m+1`: `v_2(x) = 1` on `n ≡ 25, 73 (mod 96)` and
`v_2(x) ≥ 2` on `n ≡ 1, 49 (mod 96)`.

If `31 | nx` (i.e. `n ≡ 93 mod 124`) the divisor pair `d_1 = d_2 = nx` works and
`u=31` succeeds trivially. Everything below assumes `gcd(nx, 31) = 1`.

## Discrete logs modulo 31

Use primitive root `3`. Then

\[
\log_3(2)=24\equiv-6,\qquad \log_3(-1)=15,
\]

`\log_3(q)` is even exactly for quadratic residues `\pmod{31}`, and `2` is itself a
cube modulo 31 (`24 = 3·8`). The exact criterion for `u=31`:

\[
u\text{-method succeeds}\iff 15\in\Big\{\textstyle\sum_{p^e\| nx} c_p\log_3(p): |c_p|\le e\Big\}\pmod{30}.
\]

This span formulation was compared against the exact centered/divisor-pair
criteria on **all 283 entrants** of the `u=31` stage below 10^7: **0 mismatches**
(`analysis/u31_layer.json`, `analysis/u31_classification_verify.py`).

## Immediate obstruction: QR purity

If every prime divisor of `M = nx` is a quadratic residue modulo 31, every
centered log sum is even, while the target `15` is odd. Therefore `u=31` fails.

This accounts for **60 of the 93 failures** at the `u=31` stage.

## Rescue theorem: cube-QNR prime factors

Let `q | M` be a quadratic nonresidue with discrete log `s = 3u`, `u ∈ {1, 3, 5, 7, 9}`
(the odd cube classes: `q ≡ 27, 29, 30, 15, 22 mod 31` respectively). Then the
witness

\[
15 \;=\; 3u \;+\; 6k,\qquad c_q = +1,\quad c_2 = k\ (k = (5-u)/2 \in \{2,1,0,\mp1,\mp2\})
\]

is available whenever `v_2(nx) ≥ |k|`. Explicitly:

| log `s` | `q mod 31` | required `v_2(nx)` |
|---:|---:|---:|
| 15 | 30 (−1) | ≥ 0 (coefficient 0 on 2) |
| 9 | 29 | ≥ 1 (always true) |
| 21 | 15 | ≥ 1 (always true) |
| 3 | 27 | ≥ 2 (`n ≡ 1 or 49 mod 96`) |
| 27 | 22 | ≥ 2 (`n ≡ 1 or 49 mod 96`) |

**Theorem (cube-QNR rescue).** If `M = nx` has a quadratic nonresidue prime
factor `q` with `q ≡ 29, 15, or 30 (mod 31)`, then `u=31` succeeds with witness
`c_q = ±1, c_2 ∈ {0, ±1}`. The same holds for `q ≡ 27 or 22 (mod 31)` whenever
`n ≡ 1 or 49 (mod 96)`.

*Proof.* The coefficients above give `c_q·s + c_2·24 ≡ 15 (mod 30)`; all ranges
are respected by the stated `v_2` conditions. ∎

Empirically, **none of the 93 failures** contains any cube-QNR factor (0/93), so this
theorem excludes all such cases from the failure set; on the success side it
supplies direct witnesses for 15 of the 190 successes (the remaining 75
cube-QNR successes are rescued by wider combinations — double-coefficients on
`q`, or additional QR shifts — same span condition, different witnesses).

## What remains open (the 33 non-QR-pure failures)

The remaining failures have QNR factors, all with **odd discrete logs
`≢ 0 (mod 3)`** (non-cube QNRs), and still fail — the mod-3 component of the
target `15` must be cancelled by another non-cube QNR, which forces
coefficient patterns that the mod-10 span then misses. The full span
condition remains the exact characterization; a compact closed form over
residue classes for these configurations (33 cases ≤ 10^7, all fingerprinted in
`analysis/u31_layer.json`) is the next layer task, feeding the hybrid
termination route in ROADMAP #3.

## Independent replication of the full corrected cascade (2026-11-19)

`analysis/u31_layer_analysis.py` recomputed the entire documented cascade
independently (shift-divisor + exact u = 7, 11, 15, 23, then 31…63) over all
prime hard cases up to 10^7:

| stage | this run | DETERMINISTIC_CASCADE_STATUS.md |
|---|---:|---:|
| corrected prime hard cases | 48,711 | 48,711 |
| after shift-divisor reduction | 7,272 | 7,272 |
| after exact u=7 | 2,137 | 2,137 |
| after exact u=11 | 1,054 | 1,054 |
| after exact u=15 | 681 | 681 |
| after exact u=23 | 283 | 283 |
| after u=31 | 93 | 93 |
| after u=35, 39, 43, 47 | 67, 29, 25, 9 | 67, 29, 25, 9 |
| after u=51, 55, 59, 63 | 7, 5, 2, 1 | 7, 5, 2, 1 |

Single residual survivor: `n = 8,803,369` (first works at u = 107, settled by
computation, not by a covering argument).
