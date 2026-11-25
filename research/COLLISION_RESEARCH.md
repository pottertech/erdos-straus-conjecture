# Universal opposite-residue reachability — research program (v0.1)

> **Standing banner.** This is the research phase of the Erdős–Straus program,
> separate from the frozen manuscript (`ROUTE2_CONDITIONAL_REDUCTION.md`,
> frozen at `paper-v1.12`). The Erdős–Straus conjecture remains **open and
> unproved** by this program; everything here is conditional analysis,
> machine-verified criteria, and empirical structure over verified populations.
> Computation never closes a universal claim.

## R. The problem

For every prime `p ≡ 1 (mod 24)` (the residual class of (H24)), prove that
there exists an admissible parameter

> `u ∈ {3, 7, …, 2p−3}`, `gcd(p(p+u)/4, u) = 1`,

with

> **`D_u(M) ∩ (−D_u(M)) ≠ ∅`**, where `M = p(p+u)/4`
> and `D_u(M) = { d mod u : d ∣ M }`.

Equivalently (ninth-review §5.3, mathematically accepted): the centered product
set satisfies `S_u(M) = D·D⁻¹`, so the span criterion −1 ∈ S_u(M) holds exactly
when `D` contains two opposite residues. Every swept hard-case prime already
satisfies this at its first-working parameter (zero failures across
3,194,231 primes through 10⁹, verified by three independent engines); the
open problem is universal proof.

## R.1 The three established conditions

| Layer | Criterion | Meaning | Status |
| --- | --- | --- | --- |
| One-sided reachability | `−1 ∈ D_u(M)` | a parametric witness exists | machine-checked (`param_exists_iff_onesided`), audited |
| Centered reachability | `D ∩ (−D) ≠ ∅` | an admissible divisor-span witness exists | accepted math (ninth-review §5.3); formalization pending (lane L2) |
| Erdős–Straus representation | `4/p = 1/x + 1/y + 1/z` | explicit constructive solution | machine-checked (`u_method_witness`), audited |

Implications: one-sided ⟹ centered; centered ⟹ representation (constructive).
The last implication is unconditional and formalized; the first is
elementary-split and accepted; the middle open problem is the second layer.

## R.2 Known sufficient condition

**Pigeonhole (ninth-review §5.3, accepted; not formalized).** Negation is a
bijection of `(ℤ/uℤ)*`, so `|−D| = |D|`; if `|D| > φ(u)/2` then `D` and `−D`
cannot be disjoint. Cyclic and noncyclic groups alike. Sufficient, not
necessary — and the empirical margin data (lane L1, this release) quantifies
how often it already concludes the collision.

## R.3 Research lanes

- **L1 — margin computation (this release).** For every hard-case prime in
  `[10^7, 10^9)`, at the first-working parameter: `|D_u(M)|`, `φ(u)/2`, the
  pigeonhole verdict, the minimal collision pair. Engine:
  `sweep_exact/collision_margin_engine.c` (sanitizer-gated, self-tested on the
  four release anchors with the cross-direction no-collision check below the
  first-working parameter). Results: `analysis/collision_v01/`.
- **L2 — formalization.** Machine-check (a) the collision equivalence
  `−1 ∈ S_u(M) ⟺ D ∩ (−D) ≠ ∅`, (b) the pigeonhole sufficiency
  `|D| > φ(u)/2 ⟹ −1 ∈ S_u(M)`. Both are accepted math from the review cycle
  but are not yet among the audited principal declarations.
- **L3 — cohort structure.** The 22,222-prime mod-840 research cohort; the
  3-vs-3 rate split (classes 1/121/361 near 4.2% vs 169/289/529 near 1.5%);
  which structural features of `M`'s factorization correlate with the split.
- **L4 — structural sufficient conditions.** Growth of `|D_u(M)|` across
  parameter layers; opposite-residue collisions by structure rather than
  cardinally; the (H24)-predicate converse cases (e.g. `p = 97`-type primes
  where `u = 3` succeeds outside the hard-case predicate).

## R.4 Lane L1 — v0.1 results (first verified run, 2026-11-24)

Engine: `sweep_exact/collision_margin_engine.c`
(SHA-256 `cfcef28b63503691…` — full digests in the file table below), built
`-O2 -std=c17 -fsanitize=undefined -fno-sanitize-recover=undefined`,
self-tested on the four release anchors (11/107/15/83 first-working
parameters, each with its collision pair and margin reported) plus the
cross-direction check (no collision at sampled admissible parameters below
the first-working parameter — the sweep's per-prime criterion carries over).
Run: sanitizer-silent, over the complete verified hard-case population.

**Population agreement:** sweep 3,194,231 (matches the published sweep
exactly), (H24) 2,364,031, and **collision-engine mismatches 0** — every one
of the 3,194,231 first-working parameters yields a divisor-residue collision
`d, d′ ∈ D_u(M)`, `d + d′ ≡ 0 (mod u)`, consistent two-direction with the
span-criterion sweeps (a prime with a witness must produce a collision; none
produces one where no witness exists).

**Headline: the pigeonhole sufficient condition already concludes
3,177,642 of 3,194,231 (99.49%) of the collisions at first-working
parameters.** The delicate class — collision present, `|D| ≤ φ(u)/2` — is
**16,589 primes (0.52%)**, enumerated in `analysis/collision_v01/delicate_sample.jsonl`
(5,000-row cap; full count recorded).

Layer structure of the delicate class:

| first-working `u` | population | delicate | delicate rate |
| --- | --- | --- | --- |
| 3 | 830,200 | 0 | 0% |
| 7 | 1,949,770 | 0 | 0% |
| 11 | 279,515 | 6,075 | 2.17% |
| 15 | 59,759 | 0 | 0% |
| 19 | 42,804 | 7,434 | 17.36% |
| 23 | 21,626 | 1,275 | 5.89% |
| 27 | 3,818 | 998 | 26.14% |
| 31 | 4,668 | 405 | 8.67% |
| 43 | 192 | 149 | 77.60% |
| 83 | 2 | 2 | 100% |

Both record primes (`287,567,281`, `651,412,441`, `u = 83`) are delicate:
`|D| = 12` against `φ(83)/2 = 41` (margin −58) — their collisions come from
the small-residue part of `D` (pair `(1, 82)`, i.e. a divisor `≡ −1 (mod u)`
exists), not from cardinality. The two dominant layers (`u = 3`, `u = 7` —
87.0% of the sweep) are **fully pigeonhole-conclusive**: delicate = 0.

Mod-840 breakup of the delicate class (rate per class): `1: 3,301/129,979 (2.53%)`;
`121: 2,527/129,963 (1.94%)`; `169: 2,782/129,675 (2.14%)`; `289: 1,255/130,073 (0.96%)`;
`361: 3,598/138,184 (2.60%)`; `529: 3,126/138,039 (2.26%)` — the class-289
minimum echoes the earlier nonparametric-only rate split (3-vs-3) as a
second, different observable.

Margin histogram (2|D| − φ(u), even values; sanitized run
`analysis/collision_v01/full_run.txt`): 16,589 at ≤ 0 (the delicate class),
then 905,847 at +2, 188,849 at +4, **1,744,460 at +6**, and a heavy tail.
The +6 peak — a margin of 6 — suggests |D| typically exceeds φ(u)/2 by at
least 3 residues, which is the quantity a universal proof would have to
manage.

**Consequences for the proof program.** A universal argument may split:
(i) produce *some* admissible `u` with `|D_u(M)| > φ(u)/2` structurally
(e.g. via a lower bound on the distinct-prime-factor count of
`M = p(p+u)/4` against `φ(u)/2` for small `u` layers), and (ii) treat the
delicate remainder — concentrated at large first-working parameters and
characterized by small `|D|` — by its own structure (the small-residue
collision pairs, as in the record primes). Lane L2 (formalizing the
collision equivalence and the pigeonhole bound) is the next machine-checked
step; both statements are review-accepted mathematics.

File digests (SHA-256):
`sweep_exact/collision_margin_engine.c` =
`cfcef28b…`; `analysis/collision_v01/full_run.txt` = `249c9793…`;
`analysis/collision_v01/delicate_sample.jsonl` = `5b5bcfaa…`;
`analysis/collision_v01/sanitized_selftest.txt` = `934ec74d…`.

## R.5 Standing discipline (from the OSR layer-workflow, adopted)

- No claim ships from a single hand derivation; cross-check algebra against
  the repo verifiers (0 mismatches, both directions).
- Parity-slip rule: conditions over odd prime factors must not reject the
  factor 2.
- Computation never closes the universal claim; sweeps report exactly what
  they verified, with the bound named.
- Superseded results get correction banners, never silent edits.
