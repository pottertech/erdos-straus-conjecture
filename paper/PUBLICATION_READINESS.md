# Publication Readiness: Composite Exact Type-II Depths

**Working paper:** `paper/composite_exact_typeii_depths.tex`

**Recommended title:** *An Infinite Composite-Modulus Exact-Depth Family for Type-II Erdős–Straus Solutions*

## 1. Headline theorem — symbolic, unconditional, computation-free

For every prime

\[
q\equiv5\pmod8,
\qquad
A_q=\frac{3q+1}{4},
\]

there are infinitely many primes `p == 1 (mod 4)` such that

\[
\boxed{\delta_{\rm sq}(p)=A_q.}
\]

The target modulus is deliberately composite:

\[
\boxed{4A_q-1=3q.}
\]

The target divisor is always

\[
\boxed{D=2.}
\]

No finite search, SAT solver, or unproved covering assertion enters this theorem.

### Proof ingredients

1. historical square-divisor Type-II criterion;
2. self-contained equivalence with the complete standard prime Type-II criterion;
3. universal safe residue lemma `1 not in R_B` for every earlier square-completion layer;
4. elementary observation that `q` cannot divide any earlier modulus `4B-1`;
5. CRT;
6. Dirichlet's theorem on primes in arithmetic progressions.

## 2. Quantitative corollary — symbolic

If

\[
N_{\rm comp}(X)
=\#\{A\le X:4A-1\text{ composite and infinitely many primes have exact square depth }A\},
\]

then

\[
\boxed{
N_{\rm comp}(X)
\ge
\pi\!\left(\frac{4X-1}{3};8,5\right)
=
\left(\frac13+o(1)\right)\frac{X}{\log X}.
}
\]

This uses the prime number theorem in arithmetic progressions only.

## 3. Hard-core corollary — symbolic

For every prime `q == 5 (mod 8)`, `q>5`, there are infinitely many primes

\[
\boxed{p\equiv1\pmod{840}}
\]

with

\[
\boxed{\delta_{\rm sq}(p)=\frac{3q+1}{4}.}
\]

This places the infinite composite exact-depth family directly inside the classical Mordell-hard residue core.

## 4. Regression check — not part of proof

For `q=13`:

\[
A=10,\qquad4A-1=39,\qquad D=2.
\]

A prime in the strengthened hard-core CRT progression is

\[
\boxed{p=10,139,116,681}.
\]

Exact enumeration of every `B<=10` and every divisor `E|B^2` gives first hit

\[
\boxed{(B,E)=(10,2)}.
\]

The symbolic theorem does not depend on this example.

## 5. Secondary theorem — finite exact-depth certificate

For arbitrary composite target `(A,D)`, the target progression

\[
n=a+(4A-1)k,
\qquad a\equiv-4D\pmod{4A-1},
\]

meets an earlier trap `(B,E)` in either no points or exactly one residue class of `k` modulo

\[
\frac{4B-1}{\gcd(4A-1,4B-1)}.
\]

Avoiding the finite union of all such classes and requiring a reduced resulting `n`-progression yields, by Dirichlet, infinitely many exact-depth primes.

This theorem is ordinary CRT and does not depend on a particular search algorithm.

## 6. Computationally assisted examples

### A = 649

\[
649=11\cdot59,
\qquad
4A-1=2595=3\cdot5\cdot173.
\]

All four realized divisor-modulus primitive branches

\[
D\in\{11,59,7139,38291\}
\]

have independently reconstructible finite certificates proving infinite exact-depth realization.

Verifier:

```bash
python3 exact_depth_649_full_layer_certificate.py
```

The verifier's optional hard-core CRT overlap check was independently audited and corrected on 2026-08-30: compatibility is modulo `gcd(pe,reduced_mod)`, not `min(pe,reduced_mod)`. The exact-depth assignments were unaffected.

### A = 22339

\[
22339=89\cdot251,
\qquad
4A-1=89355=3\cdot5\cdot7\cdot23\cdot37.
\]

All four realized primitive branches

\[
D\in\{89,251,22361,67079\}
\]

have full earlier-layer avoidance certificates.

Verifier:

```bash
python3 exact_depth_22339_full_layer_certificate.py
```

These examples should be presented as reinforcement that the composite spectrum extends beyond the elementary `3q` backbone, not as the main theorem.

## 7. Prior-art boundary

### Known / prior mathematics

Do **not** claim novelty for:

- the Erdős–Straus Type-I/Type-II dichotomy;
- the square-divisor condition `D|A^2`, `4A-1 | p+4D`;
- the corresponding Egyptian-fraction identity;
- CRT or Dirichlet/PNT in arithmetic progressions;
- the existence of a prime-modulus exact-depth backbone;
- the general observation that the exact-depth spectrum has nontrivial arrivals and gaps.

Relevant modern/historical sources include Mizony--Gardes, Elsholtz--Tao, Pomerance--Weingartner, Dahan, and the public FCF/CENTL depth-spectrum work.

### Candidate contribution

The strongest defensible candidate contribution is:

> The explicit infinite composite-target exact-depth family
> \[
> A=(3q+1)/4,\qquad q\equiv5\pmod8\text{ prime},
> \]
> together with the `X/(3 log X)` lower bound and hard-core realization.

Secondary candidate contributions:

- the finite exact-depth CRT certificate formulation for arbitrary target layers;
- full-layer composite realizations at `649` and `22339`.

A targeted search through 2026-08-30 has not located the exact `3q` family in the public literature inspected so far. **This is not a proof of priority.**

## 8. Required work before arXiv/submission

### Mathematical audit

- [x] Repair explicit `p == 1 (mod 4)` condition in the symbolic CRT theorem.
- [x] Independently verify the `q=13` regression example.
- [x] Include a self-contained equivalence proof between square-completion coordinates and complete prime Type II.
- [x] Separate square depth from Dahan pair depth.
- [ ] Have an independent mathematician audit the universal-safe-residue lemma and the `q`-cannot-occur-earlier argument.
- [ ] Audit the asymptotic constant `1/3` in the counting corollary independently.

### Prior-art audit

- [ ] Search MathSciNet / zbMATH / Google Scholar for combinations of `3q`, `(3q+1)/4`, Type II, Thépault, Mizony, Gardes, López, Mordell, and exact/minimal depth.
- [ ] Review historical French literature cited by Mizony--Gardes, especially Thépault-related parametrizations.
- [ ] Compare the theorem explicitly against every FCF/CENTL composite-spectrum and square-completion note, not only the prime-modulus backbone.
- [ ] Search theses and non-arXiv preprints for minimal Type-II depth spectra.

### Reproducibility

- [x] Keep the main theorem computation-free.
- [x] Keep 649/22339 certificate scripts deterministic and reconstruction-based.
- [ ] Add unit/regression tests for the two certificate verifiers.
- [ ] Add SHA-256 checksums for final verifier scripts in the paper supplement.
- [ ] Archive a release of the exact paper/code version at Zenodo or another DOI-bearing repository before submission.

### Manuscript

- [x] Pivot title and abstract to the infinite composite family.
- [x] Make claim boundary explicit: no universal Type-II result and no Erdős–Straus proof.
- [ ] Compile the LaTeX cleanly under a minimal TeX Live environment.
- [ ] Add theorem/lemma cross-references and exact page/section citations to prior work.
- [ ] Replace provisional FCF/CENTL repository citation with stable archived URLs/commit hashes.
- [ ] Decide whether the 22339 example belongs in the main paper or supplementary material.

## 9. Recommended publication shape

A concise number-theory note is stronger than a long exploratory paper.

Suggested structure:

1. Introduction and exact-depth definition.
2. Complete Type-II equivalence.
3. Universal safe residue.
4. Main `3q` composite exact-depth theorem.
5. Quantitative and hard-core corollaries.
6. General finite CRT certificate theorem.
7. One compact full-layer example (`A=649`).
8. `A=22339` in an appendix or supplement.
9. Prior-art and claim-boundary discussion.

The symbolic theorem should occupy the center of the paper. The computational certificates should demonstrate reach, not carry the main mathematical claim.
