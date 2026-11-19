# Full Primitive-Layer Realization at Exact Type-II Square Depth 22339

**Status:** unconditional, computationally assisted theorem.  All four realized divisor-modulus primitive classes at depth `22339` are certified to contain reduced arithmetic progressions of primes whose minimum complete Type-II square depth is exactly `22339`.  No novelty claim is made pending a dedicated priority review.

## Layer

Take

\[
A=22339=89\cdot251,
\qquad
m_A=4A-1=89355.
\]

The realized divisor-modulus primitive classes at this layer are represented by

\[
\boxed{D\in\{89,251,22361,67079\}},
\]

with each `D|A^2`.

Their Type-II denominator progressions are

\[
n\equiv-4D\pmod{89355}.
\]

Explicitly:

| D | target residue mod 89355 | compatible classical hard-core class |
|---:|---:|---:|
| 89 | 88999 | 169 mod 840 |
| 251 | 88351 | 361 mod 840 |
| 22361 | 89266 | 121 mod 840 |
| 67079 | 89104 | 169 mod 840 |

## Global first-hit certification

For a fixed target `D`, write

\[
n=a_D+89355k.
\]

Every earlier square-completed Type-II layer

\[
1\le B<22339,
\qquad E\mid B^2,
\]

induces, when CRT-compatible with the target progression, one forbidden class

\[
k\equiv c\pmod{
(4B-1)/\gcd(89355,4B-1)
}.
\]

The exact verifier `exact_depth_22339_full_layer_certificate.py` reconstructs the complete earlier-layer system independently for each of the four `D` values and expresses the problem over maximal prime-power coordinates.

For every target class it then:

1. constructs the least-unary-safe coordinate assignment;
2. applies a small explicit list of coordinate overrides;
3. verifies every unary exclusion;
4. verifies every composite forbidden tuple;
5. checks the resulting denominator progression is reduced prime-by-prime;
6. checks compatibility with the listed classical residue class modulo `840`.

The numbers of earlier constraints are approximately `5.76e5`--`5.78e5` per target class.  No prime sampling enters the proof.

## Theorem

For every

\[
D\in\{89,251,22361,67079\},
\]

there exists a reduced arithmetic progression of denominator primes on which

\[
D\mid22339^2,
\qquad
89355\mid p+4D,
\]

while every complete square-completed Type-II layer of depth

\[
B<22339
\]

fails.

Therefore Dirichlet's theorem gives infinitely many primes from each of the four target progressions satisfying

\[
\boxed{
\operatorname{depth}_{\rm sq}(p)=22339.
}
\]

In particular, infinitely many such exact-depth primes occur in each of the classical hard-core classes

\[
\boxed{
121,\ 169,\ 361\pmod{840}.
}
\]

The class `169 mod 840` is realized by two different primitive divisor branches at the same depth.

## Significance

This is stronger than exhibiting one exact-depth residue class.  The entire realized primitive part of this composite layer survives the full global earlier-depth covering system strongly enough to contain reduced prime progressions.

Thus `A=22339` is a robust composite point of the square-completed exact-depth spectrum:

\[
\boxed{
P_{22339}^{\rm real}
\text{ is globally realized branch-by-branch by infinitely many primes.}
}
\]

This demonstrates that the composite residual spectrum is not merely a finite-computation artifact of divisor-modulus ancestry.  At least at this layer, every primitive square-divisor direction remains genuinely new after *all* unrelated earlier moduli are included.

## Relation to current public work

FCF/CENTL proves an infinite exact-depth backbone when `4a-1` is prime and gives an exact classification for prime-valued indices `a`.  Their public synthesis explicitly identifies the remaining completed-depth spectrum problem with composite indices and notes that finite data contain many realized composite depths.

The present theorem concerns the composite index

\[
22339=89\cdot251
\]

and uses full cross-modulus CRT avoidance of all earlier completed layers, rather than the prime-modulus backbone.

A public-web search did not locate the value `22339` or this four-branch global certificate in the current FCF/CENTL library.  This is not a proof of novelty or priority.  A repository-level comparison is still required before publication claims.

## Reproduction

Run

```bash
python3 exact_depth_22339_full_layer_certificate.py
```

The script regenerates the complete finite congruence systems for all four target classes and verifies the compact certificates.

## Claim boundary

This theorem is about the exact spectrum of standard prime Type II.  It does **not** prove that every prime has a Type-II solution and does not prove the Erdős--Straus conjecture.