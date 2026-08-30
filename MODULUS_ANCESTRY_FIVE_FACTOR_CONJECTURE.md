# Five-Factor Modulus Ancestry Cover — Refuted

**Status:** **FALSE.** The former five-factor ancestry-cover conjecture is refuted in both the mixed-signature and all-`3 mod 4` branches. This file is retained as a correction record so later work does not accidentally rely on the conjecture.

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

The former conjecture asserted that `omega(m)>=5` forces every unit square class modulo `m` into at least one proper ancestor set. That assertion is false.

## Smaller mixed-signature counterexample

Take

\[
\boxed{m=352495=5\cdot11\cdot13\cdot17\cdot29}
\]

and

\[
\boxed{r=224316}.
\]

The class `r` is a unit square modulo every prime factor of `m`:

\[
r\equiv1\pmod5,
\quad4\pmod{11},
\quad1\pmod{13},
\quad4\pmod{17},
\quad2\pmod{29},
\]

and each displayed residue is a nonzero quadratic residue. Hence `r in QR(m)` by CRT.

The proper divisors of `m` that are `3 mod 4` are exactly

\[
11,55,143,187,319,715,935,1595,2431,4147,5423,12155,20735,27115,70499.
\]

Exact evaluation gives:

| d | B=(d+1)/4 | r mod d | in Q_B? |
|---:|---:|---:|:---:|
| 11 | 3 | 4 | no |
| 55 | 14 | 26 | no |
| 143 | 36 | 92 | no |
| 187 | 47 | 103 | no |
| 319 | 80 | 59 | no |
| 715 | 179 | 521 | no |
| 935 | 234 | 851 | no |
| 1595 | 399 | 1016 | no |
| 2431 | 608 | 664 | no |
| 4147 | 1037 | 378 | no |
| 5423 | 1356 | 1973 | no |
| 12155 | 3039 | 5526 | no |
| 20735 | 5184 | 16966 | no |
| 27115 | 6779 | 7396 | no |
| 70499 | 17625 | 12819 | no |

Therefore `r` survives every proper square-completed ancestor of `m`.

This counterexample is especially important because it lies in the **mixed-signature** branch. It shows that the exact descent lemma through a `1 mod 4` prime factor does not imply that every strong four-factor base is killed by all further `1 mod 4` extensions.

Indeed, removing the factor `29` gives the strong four-factor base

\[
12155=5\cdot11\cdot13\cdot17.
\]

Thus the proposed extension-elimination target is false.

## All-negative counterexample

The all-`3 mod 4` branch also fails. Take

\[
\boxed{m=6,407,731=11\cdot19\cdot23\cdot31\cdot43}
\]

with survivor

\[
\boxed{r=3,990,232}.
\]

This class is a unit square modulo `m` and avoids all 15 proper `3 mod 4` ancestor sets. An exact scan shows that the full proper-ancestor system at this modulus leaves 3,824 unit-square survivors, while the ten three-prime ancestors alone leave 133,588.

So the failure is not an isolated class and is not repaired by using the entire all-negative ancestor lattice.

## Why the earlier finite evidence missed the failure

The original exhaustive modulus-level audit stopped at

\[
m\le250000.
\]

The mixed-signature counterexample already occurs at `352495`, just beyond that range. The smallest admissible five-prime all-negative modulus is much larger:

\[
11\cdot19\cdot23\cdot31\cdot43=6,407,731.
\]

The finite audit remains valid on its stated range; only the extrapolated threshold conjecture fails.

## What remains valid

The following pieces remain exact and useful:

1. the square-completed Type-II criterion;
2. the ancestor sets `Q_B` and divisor-modulus inheritance;
3. the descent lemma through a `1 mod 4` prime factor;
4. the strong-survivor notion for the descended four-factor modulus;
5. the universal saturation at prime ancestors `3` and `7`;
6. the finite semiprime and strong-base censuses in their stated ranges.

What fails is every implication of the form

\[
\omega(m)\ge5\Longrightarrow\text{complete proper-ancestor coverage}.
\]

## Revised research direction

Proper-ancestor inheritance is a useful pruning device, not a universal closure mechanism. The next structural object should be the **persistent survivor class itself**.

For a survivor `(m,r)`, record its compatible residues on every prime factor and every composite ancestor. The research question becomes:

> What additional Type-II layer, non-ancestor transition, or arithmetic relation necessarily captures a persistent CRT survivor?

The mixed example `m=352495` is a particularly good regression target because it is small and descends to a known strong four-factor base.

## Claim boundary

These counterexamples refute only the proposed ancestry-cover lemma. They are not counterexamples to the Erdős--Straus conjecture and do not show failure of complete Type II. They show that ancestry alone cannot establish universal Type-II coverage.