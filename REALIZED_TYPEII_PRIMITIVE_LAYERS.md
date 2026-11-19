# Realized Primitive Square-Completed Type-II Layers

**Status:** exact divisor-lattice definition plus finite census. This replaces ambient quadratic-residue survivor heuristics when making claims about actual Type-II trap classes.

For depth

\[
A\ge1,
\qquad m_A=4A-1,
\]

the actual square-completed Type-II residue set is

\[
R_A=\{D\bmod m_A:D\mid A^2\}.
\]

Every class in `R_A` is realized by an actual divisor `D|A^2` and therefore gives a valid depth-`A` Type-II progression

\[
\boxed{n\equiv-4D\pmod{m_A}.}
\]

This is the correct residue object for complete Type-II layer analysis.

## Divisor-modulus ancestry

If

\[
m_B=4B-1\mid m_A
\]

with `B<A`, then a realized class `r in R_A` is inherited from depth `B` whenever

\[
r\pmod{m_B}\in R_B.
\]

Define the realized primitive remainder

\[
P_A^{\rm real}
=
R_A\setminus
\bigcup_{\substack{B<A\\m_B\mid m_A}}
\pi_{m_B}^{-1}(R_B).
\]

Every member of `P_A^real` is a genuine Type-II divisor class that is not explained by any smaller divisor-modulus ancestor.

This notion is weaker than global first-hit depth: an unrelated earlier modulus `m_B` not dividing `m_A` can still solve subprogressions after CRT refinement.

## Exact finite census through A = 200000

An independent exact run of `realized_typeII_primitive_analyzer.py` through

\[
A\le200000
\]

found `148,198` depths with at least one realized primitive class.

Grouped by the number of distinct prime factors of `4A-1`:

| omega(4A-1) | primitive depths |
|---:|---:|
| 1 | 32,044 |
| 2 | 66,566 |
| 3 | 41,588 |
| 4 | 7,716 |
| 5 | 283 |
| 6 | 1 |

Thus actual primitive Type-II classes persist well beyond four-factor moduli.

## First observed five-factor example

The first example in this scan is

\[
\boxed{A=22339=89\cdot251}
\]

with

\[
\boxed{m_A=89355=3\cdot5\cdot7\cdot23\cdot37.}
\]

The realized primitive residue classes are

\[
\boxed{89,\ 251,\ 22361,\ 67079\pmod{89355}.}
\]

These are represented by actual divisors of `A^2`. For example,

\[
89\mid A^2,
\qquad
251\mid A^2,
\]

and the larger classes arise from higher divisor representatives modulo `m_A`.

Therefore the earlier heuristic

\[
\omega(4A-1)\ge5\Rightarrow\text{complete ancestry inheritance}
\]

is false even on the realized Type-II divisor lattice.

## First observed six-factor example

The unique primitive layer with six distinct modulus factors below `A=200000` is

\[
\boxed{A=181624=2^3\cdot73\cdot311}
\]

with

\[
\boxed{m_A=726495
=3\cdot5\cdot7\cdot11\cdot17\cdot37.}
\]

It has two realized primitive classes:

\[
\boxed{4976,\ 90821\pmod{726495}.}
\]

They are represented by actual divisors

\[
4976\mid A^2,
\qquad
6629276\mid A^2,
\qquad
6629276\equiv90821\pmod{726495}.
\]

This gives an exact regression case for any future factor-count or ancestry-closure conjecture.

## Why ambient QR survivors are insufficient

A unit square class modulo `m_A` need not be represented by any divisor of `A^2`. Therefore ambient quadratic-residue survivor calculations can exhibit persistent states that have no direct Type-II interpretation.

The realized set `R_A` prevents this error by construction.

Future structural claims about complete Type II should state explicitly whether they concern:

1. ambient quadratic residues;
2. realized divisor classes `D|A^2`;
3. global first-hit classes after all earlier moduli are considered.

These are different objects.

## Next research target: global first-hit pruning

Divisor-modulus ancestry is only the first compression layer. The real next object is

\[
F_A
=
P_A^{\rm real}
\setminus
\{\text{classes already globally covered by earlier depths after CRT refinement}\}.
\]

A class in `F_A` would represent a genuinely new depth-`A` contribution to complete Type II, not merely a new contribution relative to divisor-modulus ancestors.

The next analyzer should therefore take each realized primitive progression

\[
n\equiv-4D\pmod{4A-1}
\]

and compute its coverage by all earlier depth progressions using exact CRT intersections.

That cross-modulus first-hit geometry is the correct next step toward understanding why finite complete-Type-II depth searches close every prime seen so far.

## Claim boundary

The census above is exact in the stated finite range. It does not prove that primitive realized layers persist indefinitely, and it does not establish universal Type II. It corrects the search space so that subsequent computations and theorems concern actual Type-II divisor classes rather than ambient square classes.