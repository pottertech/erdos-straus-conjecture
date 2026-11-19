# Route 2 — The Conditional Reduction: The Erdős–Straus Conjecture from a Single Prime Class

Status: **PROVED (conditional part) — machine-checked.** The reduction itself is
complete and unconditional; the residual hypothesis `(H24)` below is the
conjecture's hard core and remains open.

- Machine-check: `ErdosStrausConjecture.CenteredCriterion` (the constructive
  core) and `ErdosStrausConjecture.Reduction` (scaling + the conditional
  reduction). Zero `sorry`, zero axioms. CI compiles both on Lean 4.30.0 +
  Mathlib v4.30.0.
- Companion documents: `STATUS.md` (standing determination),
  `DETERMINISTIC_CASCADE_STATUS.md` (layer framework),
  `MOD31_EXACT_REDUCTION.md` / `MOD35_CRT_SPAN.md` (span structure).

---

## 0. The statement

**Theorem A (reduction; proved here and in Lean).**
Suppose

> **(H24)** every prime `p ≡ 1 (mod 24)` has an Erdős–Straus representation
> `4/p = 1/x + 1/y + 1/z`.

Then the full Erdős–Straus conjecture holds:

> for every integer `n ≥ 2`, `4/n = 1/x + 1/y + 1/z` has a solution in
> positive integers.

The Lean statement is
`ErdosStrausConjecture.full_conjecture_of_h24 : (∀ p, Nat.Prime p → p % 24 = 1 → IsErdosStraus p) → ∀ n, n ≥ 2 → IsErdosStraus n`.

So the whole conjecture is equivalent in strength — one direction trivially,
the other by Theorem A — to the single-class statement **(H24)**. Nothing
else is assumed, hidden or otherwise.

---

## 1. The toolkit (all machine-checked)

Everything Theorem A uses is already formalized in this repository:

1. **The seven-case modular partition**
   (`MainTheorem.lean: residue_classification`,
   `mod_3_zero`, `mod_3_two`, `mod_12_four`, `mod_12_seven`, `mod_12_ten`,
   `mod_12_one_mod_5_zero`): every `n ≥ 2` falls in exactly one of the seven
   residue cases, and the two classes that reach beyond the classical
   identities are (a) `n ≡ 5 (mod 8)` with `n` prime and (b) `n ≡ 1 (mod 12)`
   with `5 ∤ n`.

2. **The five-case identity cover** (the six modular identities): classes
   `n ≡ 0, 2 (mod 3)`, `n ≡ 4, 7, 10 (mod 12)`, and `n ≡ 1, 5 (mod 12)`
   handle their cases with explicit two- and three-term representations
   (`ClassicalIdentities`, `OmegaCases`).

3. **Theorem 2** (`CenteredEquivalence.lean`): every prime `n ≡ 5 (mod 8)`
   has `A = 3`.

4. **The residual-class lemma** (`MainTheorem.lean:
   erdos_straus_except_residual_open_class`): everything is covered except
   `C = {n ≥ 13 : n ≡ 1 (mod 12), 5 ∤ n, ¬(n prime ∧ n ≡ 5 (mod 8))}`,
   which the partition resolves further into the prime class `≡ 1 (mod 24)`
   and composites.

5. **The constructive criterion** (`CenteredCriterion.lean`): for `A` a
   divisor of `(n x)²·`-form span conditions — specifically, whenever there
   are positive `d₁, d₂` with `d₁ d₂ = (n x)²`, `u ∣ (d₁ + n x)`,
   `u ∣ (d₂ + n x)`, `x = (n + u)/4`, and `gcd(u, n x) = 1`, then
   `x, y = (d₁ + n x)/u, z = (d₂ + n x)/u` solve `4/n = 1/x + 1/y + 1/z`
   exactly (`u y z` identity proved by `ring`-normalization in Lean).

---

## 2. The scaling lemma (Section 0's engine for composites)

**Lemma A (scaling).** If `4/n = 1/x + 1/y + 1/z` and `k ≥ 1`, then
`4/(n k) = 1/(k x) + 1/(k y) + 1/(k z)`.

*Proof.* Multiply the identity `4 x y z = n (x y + x z + y z)` through by
`k³`:

```
4 (k x)(k y)(k z) = k³ · 4 x y z
                  = k³ · n (x y + x z + y z)
                  = (n k) (k² x y + k² x z + k² y z)
                  = (n k) ((k x)(k y) + (k x)(k z) + (k y)(k z)).
```

Every new denominator is positive. ∎ (This is `Reduction.scaling` in Lean.)

**Lemma B (prime descent).** Every composite `n ≥ 2` has a proper prime
divisor `p` with `n = p · (n / p)`, `p` prime, `n / p ≥ 1`.

*Proof.* `Nat.exists_prime_and_dvd` (Lean/Mathlib). ∎

**Corollary.** A solution for every prime implies a solution for every
composite, by Lemma A scaled with the factor `n / p`. This is why the
composite half of the residual class `C` costs nothing: composites inherit
solutions from their smallest prime factor — that factor is either a class
the certified identities already solve, or a prime `≡ 1 (mod 24)`, which is
exactly what (H24) supplies.

---

## 3. The mod-chain: why exactly `1 (mod 24)`

The certified partition leaves, for a prime `p`, only the sub-cases

- `p ≡ 1 (mod 12), 5 ∤ p, p prime, p ≡ 5 (mod 8)` — `theorem2` covers
  (`p ≡ 13 (mod 24)`); and
- `p ≡ 1 (mod 12), 5 ∤ p, p prime, p ≡ 1 (mod 8)` — this is `p ≡ 1 (mod 24)`
  in force, the class of **(H24)**.

The mod-chain lemma `Reduction.mod8_of_12` supplies the bridge that makes
this tight and machine-checked: if `n ≡ 1 (mod 12)` and `n ≢ 1 (mod 24)`,
then `n ≡ 5 (mod 8)`, because `n mod 24 ∈ {1, 13}` when `n ≡ 1 (mod 12)`,
and `13 mod 8 = 5`. In residue symbols: `(1/12)` splits over `(1/24)`,
and `13 = 1 + 12 ≡ 5 (mod 8)`. There is no other gap.

So Theorem A's proof structure is precisely:

```
n ≥ 2
 ├─ n prime
 │   ├─ n ≡ 1 (mod 24)   supplied by (H24)
 │   └─ n ≢ 1 (mod 24)   covered by partition + identities + theorem2
 └─ n composite
     └─ scale a solution for a prime factor p ∣ n
         (p prime → same branch, composites never recurse further)
```

No circularity: the composite branch consults only prime factors; every
prime either uses (H24) or a certified identity; done.

---

## 4. What (H24) means

This is the honest state of the analytical residue, stated precisely.

**(H24) restated in the span criterion.** For a prime `p ≡ 1 (mod 24)` and
`u` odd with `u ∣ (p + ...)`, the centered criterion at `u` reduces (via
`d₁ d₂ = (p x)²`, `u ∣ (d₁ + p x)`, `u ∣ (d₂ + p x)`) to the span condition

> `−1 ∈ S_u(p · (p + u)/4)` in `(ℤ/uℤ)×`, with

the same machinery the layer documents (MOD31, MOD35) already verified
layer-by-layer for concrete `u`. The constructive criterion in
`CenteredCriterion.lean` converts any span witness into an explicit
solution.

**What is known about (H24):**

1. **For every prime `p ≡ 1 (mod 24)` in the certificate dataset**
   (166,011 records, `results/layer4_certificates.jsonl`), the u-method
   succeeds; the largest first-working `A` in the dataset is **107**
   (record `8,803,369`, which is prime and `≡ 1 (mod 24)`), and across the
   full 10^9 hard-case sweep in `verification_100M_1B.json` the maximum is
   `A = 151`. Empirically (H24) holds with
   a tiny, bounded `A`.

2. **No covering/termination theorem exists.** The corrected cascade
   narrows case after case but has no theorem that the cascade reaches
   *every* prime `≡ 1 (mod 24)`, and no bound argument closes the class
   universally. 8,803,369 was settled by computation (first works at
   `u = 107`), not by a covering argument.

3. **The analytic route is not complete anywhere.** Burgess-type least
   quadratic-nonresidue bounds (Norton 1971, giving
   `≪ p^{1/(4√e)+ε}` for some prime non-residue) supply the *existence*
   of a fast non-residue but do not control the span's arithmetic — the
   span condition needs the non-residue's discrete logarithm to land in a
   specific coset, not merely to exist (this is exactly the structure
   documented in `MOD31_EXACT_REDUCTION.md`).

4. **Under GRH / Chebotarev.** The least prime non-residue is
   `O((log p)²)` under GRH, and Chebotarev (unconditional, with Linnik /
   the Chebotarev density theorem + effective versions) can in principle
   target primes `u` in prescribed Frobenius classes — but the span-side
   requirement couples the choice of `u` with the discrete-log
   arithmetic, and *that* coupling is the real open part. The v12
   manuscript's §5.1 hedge remains the correct summary: not a completed
   proof until the sieve and covering assumptions are fully formalized.

---

## 5. What this changes, concretely

Before this document: the Lean development carried `axiom
erdos_straus_mod_12_1_not_div_5_conjecture`, which assumes the *whole*
class `n ≡ 1 (mod 12), 5 ∤ n, n ≥ 13` — a class spanning composites and
primes. After:

- The formal content of that axiom is now **known to follow**
  (machine-checked, `Reduction.full_conjecture_of_h24`) from the strictly
  weaker statement (H24) about primes `≡ 1 (mod 24)` alone.
- The conditional-paper form of route 2 is realized exactly here:
  **(H24) stated as a hypothesis, the reduction proved, the constructive
  criterion proved, and the analytic residue documented.** The conjecture
  is *not* proved — it is reduced, honestly and completely, to the single
  class statement (H24), whose non-triviality is documented in
  `STATUS.md` and `DETERMINISTIC_CASCADE_STATUS.md`.

---

## 6. Falsification and reproducibility

- The Lean reduction: `lake build ErdosStrausConjecture.Reduction`
  (and `…CenteredCriterion`) — CI builds both on every push.
- The certificate dataset backing note (4)(1):
  `analysis/layer4/verify_certificates.py` re-verifies all 166,011
  records from `results/layer4_certificates.jsonl`.
- Any future counterexample to (H24) — a prime `≡ 1 (mod 24)` with no
  solution — would falsify Theorem A's applicability, not its validity:
  Theorem A is a proven implication, and its antecedent is what remains
  open.
