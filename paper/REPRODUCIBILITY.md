# Reproducibility guide for the composite exact-depth manuscript

This guide separates the computation-free symbolic theorem from the supplementary finite certificates.

## 1. Symbolic theorem: no large computation required

The main theorem for

`A_q=(3q+1)/4`, `4A_q-1=3q`

is proved symbolically from:

1. the historical square-divisor Type-II coordinate;
2. the universal safe-residue lemma `1 notin R_B`;
3. the observation that for `B<A_q`, a prime `q == 1 (mod 4)` cannot divide `4B-1`;
4. CRT;
5. Dirichlet's theorem on primes in arithmetic progressions.

The density-one theorem additionally uses only finite CRT equidistribution/PNT in fixed arithmetic progressions and divergence of the reciprocal sum over primes `2 mod 3`.

The independent proof reconstruction is in:

`paper/INDEPENDENT_REPROOF.md`

The density proof audit is in:

`paper/DENSITY_ONE_REFEREE_AUDIT.md`

## 2. Small symbolic regression suite

Run:

```bash
python3 paper/symbolic_backbone_regression.py
```

Expected final line:

```text
PASS: symbolic backbone regression suite
```

The cases exercise different target witnesses:

| q | A=(3q+1)/4 | witness D |
|---:|---:|---:|
| 13 | 10 | 2 |
| 29 | 22 | 11 |
| 73 | 55 | 5 |
| 113 | 85 | 17 |
| 193 | 145 | 29 |

The suite checks the theorem's local arithmetic conditions and the universal-safe-residue lemma through every earlier depth for each small test case. It is a regression check, not a proof dependency.

## 3. Supplementary full-layer certificates

These are not needed for the density-one theorem.

Run:

```bash
python3 exact_depth_649_full_layer_certificate.py
python3 exact_depth_22339_full_layer_certificate.py
```

Each verifier reconstructs all earlier square-divisor Type-II congruences from first principles and checks a compact prime-power CRT certificate.

## 4. Manuscript source

Current preprint candidate:

`paper/composite_exact_typeii_depths_v3.tex`

Before release, perform a clean LaTeX build from an empty auxiliary-file directory and verify:

- no undefined references;
- no missing citations;
- no overfull equations affecting readability;
- theorem numbering is stable;
- the abstract and counting theorem both state the `2/3` constant;
- the square-divisor mechanism is explicitly labeled prior art.

## 5. Priority boundary

See:

- `paper/REFERENCES_AUDIT.md`
- `paper/PRIORITY_AUDIT.md`
- `paper/SUBMISSION_CHECKLIST.md`

A negative literature search is not a priority proof. Do not use "first", "novel", or equivalent priority language until an external historical review has been completed.
