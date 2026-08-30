# First All-Negative Five-Factor Primitive Semiprime Layer

**Status:** exact finite counterexample to the heuristic that `omega(4uv-1)>=5` should force proper-ancestor inheritance of the squarefree-semiprime mixed pair. This is not an Erdős--Straus counterexample.

## 1. The example

Take

\[
\boxed{m=98,800,627=19\cdot31\cdot43\cdot47\cdot83}.
\]

All five prime factors are `3 mod 4`, so

\[
m\equiv3\pmod4.
\]

Set

\[
A=\frac{m+1}{4}=24,700,157.
\]

Then

\[
\boxed{A=251\cdot98,407}
\]

is squarefree semiprime.

Write

\[
u=251,
\qquad
v=98,407.
\]

The two genuinely square-only semiprime directions are

\[
u^2\pmod m
\qquad\text{and}\qquad
v^2\pmod m.
\]

Numerically,

\[
u^2=63,001,
\]

while `v^2` is reduced modulo `m` in the table below.

## 2. Exact proper-ancestor audit

Because `m` is a product of five distinct `3 mod 4` primes, the proper divisors `d|m` with `d==3 (mod 4)` are exactly the one-prime and three-prime products. There are 15.

For each such `d`, put

\[
B=\frac{d+1}{4},
\qquad
Q_B=\{E\pmod d:E\mid B^2\}.
\]

Exact computation gives:

| d | B | u^2 mod d | inherited? | v^2 mod d | inherited? |
|---:|---:|---:|:---:|---:|:---:|
| 19 | 5 | 16 | no | 17 | no |
| 31 | 8 | 9 | no | 14 | no |
| 43 | 11 | 6 | no | 13 | no |
| 47 | 12 | 21 | no | 27 | no |
| 83 | 21 | 4 | no | 48 | no |
| 25,327 | 6,332 | 12,347 | no | 7,237 | no |
| 27,683 | 6,921 | 7,635 | no | 9,004 | no |
| 38,399 | 9,600 | 24,602 | no | 17,041 | no |
| 48,887 | 12,222 | 14,114 | no | 9,593 | no |
| 62,651 | 15,663 | 350 | no | 35,230 | no |
| 67,811 | 16,953 | 63,001 | no | 52,172 | no |
| 74,119 | 18,530 | 63,001 | no | 67,942 | no |
| 110,639 | 27,660 | 63,001 | no | 37,896 | no |
| 120,931 | 30,233 | 63,001 | no | 25,031 | no |
| 167,743 | 41,936 | 63,001 | no | 134,259 | no |

Therefore neither semiprime mixed direction is inherited from any proper ancestor.

By the exact complementary-pairing theorem in `SEMIPRIME_MIXED_RESCUE_CORE.md`, it would have been enough to test one direction; the table records both as an independent regression check.

Hence

\[
\boxed{
A=24,700,157=251\cdot98,407
\text{ is a structurally primitive squarefree-semiprime layer}
}
\]

with

\[
\boxed{\omega(4A-1)=5.}
\]

## 3. Minimality inside the all-negative five-prime signature

The audit exhaustively enumerated every product

\[
m=p_1p_2p_3p_4p_5<98,800,627
\]

of five distinct primes `p_i == 3 (mod 4)`.

Any product containing `3` or `7` cannot carry a proper-ancestor survivor because those are universal prime ancestors. For the remaining products, the audit factored

\[
A=(m+1)/4
\]

and, whenever `A` was squarefree semiprime, tested both semiprime square directions against every proper `3 mod 4` ancestor.

No smaller modulus in this all-negative five-prime signature produced a primitive squarefree-semiprime layer.

Thus `m=98,800,627` is the first such example in that exact ordered search.

## 4. Wider restricted scan

A further exact scan of all-negative five-prime products `m<2*10^9` generated from `3 mod 4` primes below `200` found:

- `1,464` cases for which `A=(m+1)/4` is squarefree semiprime;
- `92` cases in which the semiprime mixed pair is primitive with respect to every proper ancestor.

This restricted census is finite evidence only, but it shows that the `omega=5` primitive phenomenon is not isolated.

## 5. What this refutes

The earlier census through `A<=100000` found no primitive semiprime layer with `omega(4A-1)>=5`. That observation was correctly labeled finite evidence, but it motivated the stronger heuristic that sufficiently rich factorization of `4uv-1` might force inheritance.

The example above proves that the naive threshold

\[
\omega(4uv-1)\ge5
\]

is insufficient.

Together with `ALL_NEGATIVE_ANCESTRY_ANTI_COVER.md`, it shows that factor count alone is the wrong invariant in the all-negative squarefree regime.

## 6. Revised structural target

A viable theorem must use more than `omega(m)`. Candidate invariants include:

1. the mod-4 signature of the prime factors of `m`;
2. the exact local capture ratios of the prime and composite ancestors;
3. quadratic-reciprocity constraints tying `u,v` to the factors of `m=4uv-1`;
4. the distribution of the relevant semiprime square class inside the CRT product, rather than coverage of all square classes;
5. interaction with Type-I or with the current depth rather than proper ancestors alone.

## Claim boundary

This is a counterexample to a proposed **proper-ancestor inheritance heuristic**, not to Type-II solvability and not to the Erdős--Straus conjecture. The current depth `A` still contains `u^2` and `v^2` as divisors of `A^2`; primitiveness here means only that no smaller divisor-modulus depth shadows the mixed pair.