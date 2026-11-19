# Roadmap (2026-11-19)

Per the standing determination in [STATUS.md](STATUS.md) (no proof exists, here or in the
literature), four workstreams, in order of value:

## 1. Outside expert review — highest value

The v13 draft (`docs/manuscript_v13.md` on the open PR branch) and Kevin Potter's
divisor-residue criterion are the repo's strongest claim to new mathematics. Get a working
number theorist to read them closely — journal submission or an informal send to a
specialist. One such reading will find a hole, or confirm there is not one, faster than
another year of internal iteration.

## 2. Conditional proof as a paper result

Chebotarev and Linnik are proven theorems, so "the conjecture follows from these, by this
deduction" is legitimate and publishable if the deduction is airtight and every step is
written out on paper. The analytic work must exist as careful mathematics, not as Lean
axioms in a module that does not compile. A clean conditional theorem is a real
contribution and the natural home for the Burgess route.

## 3. Aim the mathematics at the one gap that matters

> **Progress 2026-11-19:** the u=31 layer now has an exact characterization
> (`MOD31_EXACT_REDUCTION.md`): span criterion verified with 0 mismatches on all 283
> stage entrants ≤ 10^7; QR-pure obstruction covers 60/93 failures; the cube-QNR
> rescue theorem (explicit witnesses, `q ≡ 29/15/30 mod 31` unconditional,
> `q ≡ 27/22 mod 31` when `n ≡ 1 or 49 mod 96`) excludes all remaining failures from
> admitting such factors. The full corrected cascade was independently re-derived
> with identical counts at every stage. The open part is unchanged: no covering
> theorem yet; the 33 non-QR-pure u=31 failures are span-delicate and fingerprinted.

The residual primes (n ≡ 1 mod 24; every odd prime factor of n+1 and every prime factor of
n+4 ≡ 1 mod 4) need a **termination theorem**: a proof that the modular cascade — or some
bounded set of u values — always succeeds. The plausible shape is a hybrid: finite cascade
for most residue patterns, character-sum input for the tail.

Literature constraint (Mordell 1967): a polynomial identity yielding solutions for
n ≡ r (mod m) can exist only when r is a quadratic non-residue mod m; since 1 is a
quadratic residue modulo every m, no finite system of polynomial identities covers those
classes. Identity-hunting alone cannot finish this, no matter how many moduli are
classified.

## 4. Close the repo's open items so the work can be judged — ✅ done 2026-11-19

- **PR #4 merged** (d28913b) after reconciling the branch's `ci.yml`/`verify.yml` with
  main's consolidated CI (the branch's four failing workflow files were dropped; post-
  merge main CI green, run 44447916354).
- **Issue #6 closed**: `NewTheorems.lean` fixed (verified witness 4/73 = 1/20 + 1/210 +
  1/30660; module in the CI build set), its two unused Burgess axioms removed (paper
  route per #2), `StructuralLemmas.lean` retired to `lean-archive/orphan-modules/`.
  Census now 3 unfinished goals in the root project; axiom whitelist down to 2
  (the residual-class hypothesis + the divisor-residue reverse criterion).
- **Issue #7 open**: the certificate generator is buggy (fails at n=15649; exact
  criterion certifies A=7) — dataset stays out of the repo (generation documented,
  strict audit gated) until fixed and the full range regenerates green.

None of #4 solves the conjecture; it makes routes 1–2 possible — nobody reviews work they
cannot build or audit.

## What will not do it

More compute. Verification at 10^12 or 10^15 is better evidence and still not a proof, and
the search pipelines have already squeezed that route.
