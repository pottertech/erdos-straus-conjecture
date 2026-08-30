# Five-Factor Modulus Ancestry Cover — Refuted

**Status:** **FALSE.** The former five-factor ancestry-cover conjecture is refuted by an exact all-negative five-prime counterexample. This file is retained as a correction record so later work does not accidentally rely on the conjecture.

## Former conjecture

For an odd modulus

\[
m\equiv3\pmod4,
\qquad A=\frac{m+1}{4},
\]

and every proper divisor

\[
1<d<m,\qquad d\mid m,\qquad d\equiv3\pmod4,
\]

put

\[
B=\frac{d+1}{4},
\qquad
Q_B=\{E\pmod d:E\mid B^2\}.
\]

The former conjecture asserted that if `omega(m)>=5`, then every unit square class modulo `m` is inherited from at least one proper `3 mod 4` ancestor:

\[
QR(m)\subseteq
\bigcup_{\substack{d\mid m\\1<d<m\\d\equiv3(4)}}
\pi_d^{-1}(Q_{(d+1)/4}).
\]

That assertion is false.

## Exact counterexample

Take

\[
\boxed{m=6,407,731=11\cdot19\cdot23\cdot31\cdot43}.
\]

All five prime factors are `3 mod 4`, so `m == 3 (mod 4)` and `omega(m)=5`.

The unit square class

\[
\boxed{r=3,990,232}
\]

is a quadratic residue modulo every prime factor:

| p | r mod p |
|---:|---:|
| 11 | 4 |
| 19 | 4 |
| 23 | 8 |
| 31 | 5 |
| 43 | 4 |

Each displayed residue is a nonzero square modulo `p`; by CRT, `r` is a unit square class modulo `m`.

For a product of five distinct `3 mod 4` primes, the proper divisors that are `3 mod 4` are exactly the one-prime and three-prime products. There are 15 of them. Exact divisor-set evaluation gives:

| d | B=(d+1)/4 | r mod d | in Q_B? |
|---:|---:|---:|:---:|
| 11 | 3 | 4 | no |
| 19 | 5 | 4 | no |
| 23 | 6 | 8 | no |
| 31 | 8 | 5 | no |
| 43 | 11 | 4 | no |
| 4,807 | 1,202 | 422 | no |
| 6,479 | 1,620 | 5,647 | no |
| 7,843 | 1,961 | 5,988 | no |
| 8,987 | 2,247 | 4 | no |
| 10,879 | 2,720 | 8,518 | no |
| 13,547 | 3,387 | 7,414 | no |
| 14,663 | 3,666 | 1,896 | no |
| 18,791 | 4,698 | 6,540 | no |
| 25,327 | 6,332 | 13,893 | no |
| 30,659 | 7,665 | 4,562 | no |

Thus

\[
\boxed{
r\notin
\bigcup_{\substack{d\mid m\\1<d<m\\d\equiv3(4)}}
\pi_d^{-1}(Q_{(d+1)/4})
}
\]

while `r in QR(m)`.

Hence the five-factor ancestry-cover conjecture is refuted.

## Why the earlier finite evidence missed this

The previous exhaustive modulus-level audit stopped at

\[
m\le250,000.
\]

But after the exact pruning lemma `gcd(m,21)=1`, the smallest modulus having five distinct prime factors all `3 mod 4` is already

\[
11\cdot19\cdot23\cdot31\cdot43
=6,407,731.
\]

Therefore the old finite range did not test the all-`3 mod 4` five-factor branch at all.

The earlier computation remains valid for the moduli it actually tested; the extrapolated five-factor conjecture does not.

## Additional exact checks

An independent CRT-level scan of the next several five-prime all-negative moduli also found survivors. Therefore the counterexample is not an isolated boundary accident. No replacement universality conjecture should be stated from the old `omega(m)>=5` heuristic without substantially stronger hypotheses.

## What survives from the ancestry program

Several exact pieces remain valid and useful:

1. the square-completed Type-II criterion itself;
2. the definition of ancestor sets `Q_B`;
3. the minimal-descent implication through a `1 mod 4` prime factor;
4. the theorem that `3` and `7` are the only universal prime ancestors;
5. the finite census of strong four-factor bases in the range actually checked.

What fails is the global leap

\[
\omega(m)\ge5\Longrightarrow\text{complete proper-ancestor coverage}.
\]

## Revised research direction

The correct next question is not whether five factors automatically force ancestry coverage. Instead:

> Which arithmetic signatures of the factorization of `m` force ancestor coverage, and which signatures admit persistent CRT survivor classes?

The mixed-signature case and the all-negative case must be treated separately. The all-negative branch demonstrably admits survivors and therefore requires an additional mechanism beyond proper-ancestor inheritance.

## Claim boundary

This counterexample refutes only the proposed **ancestry-cover lemma**. It is not a counterexample to the Erdős--Straus conjecture, nor to Type-II solvability. It only shows that this proposed structural route cannot by itself establish universal Type-II coverage.