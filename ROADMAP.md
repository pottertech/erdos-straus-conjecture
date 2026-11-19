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

The residual primes (n ≡ 1 mod 24; every odd prime factor of n+1 and every prime factor of
n+4 ≡ 1 mod 4) need a **termination theorem**: a proof that the modular cascade — or some
bounded set of u values — always succeeds. The plausible shape is a hybrid: finite cascade
for most residue patterns, character-sum input for the tail.

Literature constraint (Mordell 1967): a polynomial identity yielding solutions for
n ≡ r (mod m) can exist only when r is a quadratic non-residue mod m; since 1 is a
quadratic residue modulo every m, no finite system of polynomial identities covers those
classes. Identity-hunting alone cannot finish this, no matter how many moduli are
classified.

## 4. Close the repo's open items so the work can be judged

- **Merge PR #4** after two decisions: (a) reconcile the branch's `ci.yml`/`verify.yml`
  with main's consolidated CI; (b) the 166,011-certificate dataset — commit it under
  `results/` or document its generation procedure so the strict audit can pass.
- **Clear issue #6**: fix or formally retire `NewTheorems.lean` (false `decide` witness at
  ~line 24) and `StructuralLemmas.lean` (tactic errors plus 5 unfinished goals); restate
  the main theorem as conditional rather than letting an axiom carry the residual class.

None of #4 solves the conjecture; it makes routes 1–2 possible — nobody reviews work they
cannot build or audit.

## What will not do it

More compute. Verification at 10^12 or 10^15 is better evidence and still not a proof, and
the search pipelines have already squeezed that route.
