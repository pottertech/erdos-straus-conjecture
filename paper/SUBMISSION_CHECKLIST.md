# Submission Checklist — Composite Exact-Depth Paper

## Mathematically established on the research branch

- [x] Definition of square-completion exact depth is explicit.
- [x] Square-divisor coordinate is separated from novelty claims and attributed to the Thépault/Mizony/Gardes lineage.
- [x] Universal safe-residue lemma (`1` is not a trap at any depth) has a self-contained proof.
- [x] Structural theorem for `A=(3q+1)/4`, `q == 1 (mod 4)`, with a divisor `D|A^2`, `D == 2 (mod 3)` has a symbolic proof.
- [x] Prime-factor corollary: a prime factor `ell == 2 (mod 3)` of `A` suffices.
- [x] Fixed-witness arithmetic subfamilies are proved by Dirichlet.
- [x] Density-one result among primes `q == 1 (mod 4)` is proved by finite CRT/PNT-in-AP densities followed by the divergent reciprocal-prime product limit.
- [x] Counting consequence `N_comp(X) >= (2/3+o(1)) X/log X` is derived with injective map `q -> (3q+1)/4`.
- [x] Hard-core subfamily `p == 1 (mod 840)` is proved for the `D=2`, `q == 5 (mod 8)`, `q>5` subfamily.
- [x] Independent reconstruction of the symbolic theorem is stored in `paper/INDEPENDENT_REPROOF.md`.
- [x] Referee audit of the density argument is stored separately.
- [x] Computational examples at depths 649 and 22339 are logically supplementary, not needed by the symbolic theorem.

## Prior-art status

- [x] The divisor-square Type-II mechanism is explicitly treated as prior art.
- [x] Historical trail reaches Léon Thépault's 1979 `Pour la Science` correspondence, as discussed by Mizony/Gardes and later historical work.
- [x] Public FCF/CENTL work was checked for the prime-modulus backbone, composite-rescue program, exact-depth spectrum, and divisor-square prior-art calibration.
- [x] Targeted searches for the exact signatures `(3q+1)/4`, `4A-1=3q`, and the `2 mod 3` prime-factor criterion did not locate a matching theorem in the checked current corpus.
- [ ] Broader historical search outside arXiv/web-indexed material, especially French literature and older Erdős–Straus bibliographies.
- [ ] Ask an external number theorist whether the `3q` construction is recognizable under another classical parametrization.
- [ ] Do not make a first-discovery/priority claim until those two checks are complete.

## Manuscript hardening

- [ ] Compile `paper/composite_exact_typeii_depths_v3.tex` from a clean environment.
- [ ] Resolve every LaTeX warning and undefined reference.
- [ ] Add complete bibliographic entries for Thépault/Mizony-Gardes, Elsholtz–Tao, Pomerance–Weingartner, Dahan, and relevant FCF/CENTL public notes.
- [ ] Replace any phrase such as “new,” “first,” or “novel” with neutral wording unless priority is externally confirmed.
- [ ] State clearly that `delta_sq` is the exact depth in this complete Type-II square-completion coordinate and is not Dahan's pair depth.
- [ ] Keep the density-one theorem before computational examples.
- [ ] Move large certificate details for 22339 to appendix/supplement if manuscript length grows.
- [ ] Include exact reproduction commands and expected summary output for the 649 and 22339 verifiers.

## Independent verification before posting

- [ ] Have a second person read only the theorem statements and reconstruct the proofs.
- [ ] Have an independent implementation verify the 649 certificate without importing functions from the existing verifier.
- [ ] Have an independent implementation verify the 22339 certificate or omit it from the first version of the paper if audit cost is too high.
- [ ] Check the `q=13`, `A=10`, `D=2` regression example independently.
- [ ] Check several additional symbolic-family examples with different `D`, including an odd prime `D == 2 (mod 3)`, to guard against a hidden `D=2` specialization.

## Recommended first preprint scope

The cleanest first version should make these the main results:

1. universal safe-residue lemma;
2. structural composite exact-depth theorem for `4A-1=3q`;
3. prime-factor criterion `ell == 2 (mod 3)`;
4. density-one theorem among prime parameters `q == 1 (mod 4)`;
5. lower bound `(2/3+o(1)) X/log X`;
6. finite CRT certificate theorem;
7. depth 649 as the principal computational example;
8. depth 22339 as optional second example or supplement.

## Claim boundary for abstract/submission

Safe language:

> We exhibit a density-one family, within the prime parameter line `A=(3q+1)/4`, of composite target moduli `4A-1=3q` supporting infinitely many primes whose first square-completed Type-II witness occurs exactly at depth `A`.

Do **not** claim:

- a proof of the Erdős–Straus conjecture;
- universal Type-II solvability;
- that every composite target depth is realized;
- that the density-one family has publication priority until the historical review is complete.
