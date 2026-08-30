# Full Primitive-Layer Realization at Exact Type-II Square Depth 649

**Status:** unconditional, computationally assisted theorem.  No novelty claim pending dedicated comparison with the completed-depth literature.

Take

\[
A=649=11\cdot59,
\qquad
4A-1=2595=3\cdot5\cdot173.
\]

The realized divisor-modulus primitive classes at this layer are represented by

\[
\boxed{D\in\{11,59,7139,38291\}},
\]

with each `D|649^2`.

For each target divisor `D`, the script `exact_depth_649_full_layer_certificate.py` reconstructs every earlier complete square-completed Type-II trap with `B<649`, converts every CRT-compatible intersection into a forbidden congruence on the target progression parameter `k`, and verifies a compact prime-power CSP assignment avoiding all of them.

The resulting denominator progression is reduced, so Dirichlet's theorem supplies infinitely many primes in it.  Since the target `(A,D)` itself is a valid depth-649 certificate, every such prime has

\[
\boxed{\operatorname{depth}_{\rm sq}(p)=649.}
\]

All four primitive branches are globally realized.

The branches can also be intersected with classical Mordell-hard residue classes modulo 840:

| D | target residue mod 2595 | compatible hard-core class |
|---:|---:|---:|
| 11 | 2551 | 1 mod 840 |
| 59 | 2359 | 169 mod 840 |
| 7139 | 2584 | 169 mod 840 |
| 38291 | 2536 | 121 mod 840 |

Therefore exact square depth `649` occurs infinitely often inside the classical hard core.

## Relation to the finite census

FCF/CENTL's public square-completion census through `5e7` reports a maximum observed completed depth of `624`.  That finite plateau does not conflict with this theorem: the reduced exact-depth-649 progressions can have very large least primes.  The CRT/CSP construction proves infinite existence without locating a small representative.

This makes `649` an explicit example of the distinction between finite computational records and the global exact-depth spectrum.

## Reproduction

Run

```bash
python3 exact_depth_649_full_layer_certificate.py
```

The script regenerates all earlier trap congruences and checks each compact certificate exactly.

## Claim boundary

This theorem concerns the exact first-hit spectrum of standard prime Type II.  It does not prove universal Type-II solvability or the Erdős--Straus conjecture.