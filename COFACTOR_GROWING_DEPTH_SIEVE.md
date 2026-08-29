# Growing-Depth Sieve for the Cofactor Shift-Divisor Family

**Status:** unconditional theorem by transfer of the one-parameter large-sieve argument in Dahan (2026), with the local hypotheses checked below; no priority claimed for the analytic mechanism

The cofactor-layer / shift-divisor family asks for

\[
\exists a,q>0:
\qquad
q\mid n+4a,
\qquad
q\equiv-1\pmod{4a}.
\]

Composite `q` are allowed. To obtain a uniform growing-depth upper bound, restrict to the weaker subsystem in which `q` itself is prime. Failure of the full family implies failure of this prime-witness subsystem, so any upper bound for prime-witness failures is automatically an upper bound for failures of the complete cofactor family.

## 1. Prime witness residue classes

Fix a cofactor depth `J`.

Let `q` be prime. A layer `a <= J` can use `q` as a witness exactly when

\[
4a\mid q+1.
\]

The divisibility

\[
q\mid n+4a
\]

is then equivalent to the single forbidden residue class

\[
\boxed{n\equiv-4a\pmod q.}
\]

For

\[
q>4J,
\]

these classes are pairwise distinct as `a` varies, since

\[
-4a\equiv-4b\pmod q
\]

with `1 <= a,b <= J` implies `q | 4(a-b)`, hence `a=b`.

Therefore the number of classes removed modulo `q` is

\[
\boxed{
\rho_J(q)=\#\{a\le J:4a\mid q+1\}.
}
\]

## 2. Match with Dahan's one-parameter sieve data

Benjamin Dahan, arXiv:2608.24035 (2026), Section 4.3, studies the one-parameter system

\[
s\mid n+u,
\qquad
s\equiv-1\pmod{4u},
\]

whose prime-witness counting function is

\[
\rho_J(q)=\#\{u\le J:4u\mid q+1\}.
\]

Our affine form `n+4a` is **not literally the same witness system** as Dahan's `n+u`. The transfer rests instead on the following exact agreement of the large-sieve inputs:

1. for a witness prime `q`, admissible parameters are selected by the same progression
   \[
   q\equiv-1\pmod{4a};
   \]
2. each admissible parameter removes exactly one residue class of `n mod q`;
3. for `q>4J`, those classes are pairwise distinct;
4. the number of removed classes is exactly the same function `rho_J(q)`;
5. after restricting to `n == 1 (mod 24)` and writing `n=24k+1`, multiplication by `24^{-1} mod q` simply transports the classes to distinct affine classes in `k`, so their location does not change the large-sieve cardinality calculation;
6. the progression moduli controlling the prime witnesses are `4a <= 4J`, exactly the one-parameter modulus range used in Dahan's sharper Bombieri--Vinogradov cutoff.

Dahan's Section 4.4 explicitly notes that the regimes in his Table 1 come from the same large sieve and that only the local counting function `rho(p)` changes. Thus the one-parameter proof transfers to this cofactor prime-witness system after the six checks above; it should not be described as a literal identity of affine families.

## 3. Mean size

Dahan's Lemma 4.21 gives

\[
\sum_{a\le J}\frac1{\varphi(4a)}
=
\kappa_0\log J+O(1),
\]

where

\[
\boxed{
\kappa_0
=
\frac{\zeta(2)\zeta(3)}{3\zeta(6)}
=0.647865\ldots
}
\]

Equivalently, after summing prime witnesses over the admissible progressions,

\[
\sum_q\frac{\rho_J(q)}q
\]

has main size `kappa_0 log J` times the logarithmic length of the prime-sifting interval.

The one-parameter modulus is only `4a <= 4J`, so the Bombieri--Vinogradov step is valid with the sharper lower cutoff `J^3` explicitly recorded by Dahan for the one-parameter system.

## 4. Polylogarithmic growing depth

Let

\[
J=(\log N)^\lambda,
\qquad \lambda\ge1
\]

be fixed.

The transferred one-parameter large-sieve argument gives

\[
\boxed{
E_{\mathrm{prime\ cof}}(N;J)
\ll
N\exp\!\left(
-(\kappa_0\lambda+o(1))(\log\log N)^2
\right),
}
\]

where `E_prime cof` counts primes for which no prime witness occurs at any cofactor layer `a <= J`.

Since every full cofactor-family failure is also a prime-subsystem failure,

\[
E_{\mathrm{cof}}(N;J)
\subseteq
E_{\mathrm{prime\ cof}}(N;J),
\]

and hence

\[
\boxed{
|E_{\mathrm{cof}}(N;J)|
\ll
N\exp\!\left(
-(\kappa_0\lambda+o(1))(\log\log N)^2
\right).
}
\]

This is an unconditional **uniform growing-depth theorem** for the actual shift-divisor / complementary-cofactor family.

## 5. Optimized one-parameter depth

Dahan's Table 1 records the optimized one-parameter regime and states that using the sharper `J^3` cutoff improves it to

\[
\boxed{
J=\exp\!\big((0.308+o(1))\sqrt{\log N}\big)
}
\]

with

\[
\boxed{
|E_{\mathrm{cof}}(N;J)|
\ll
N\exp\!\big(-(0.199+o(1))\sqrt{\log N}\big).
}
\]

These numerical constants are inherited from Dahan's one-parameter optimization and are not claimed as new.

## 6. Relation to the finite computation

The audited corrected residual population through `10^8` displays a much stronger finite phenomenon:

- every non-permanent untwisted / shift-divisor case has complementary-cofactor depth at most `143`;
- the only permanent untwisted exceptions found in that population are `2521` and `66529`.

The asymptotic theorem above does **not** prove a universal constant depth such as `143`, nor finiteness of permanent failures. It proves instead that allowing a slowly growing cofactor depth makes the exceptional set quantitatively very thin.

## 7. Comparison with Dahan's two-parameter theorem

Dahan's broader two-parameter criterion has mean witness count of order `(log J)^2`, yielding

\[
N\exp(-c(\log\log N)^3)
\]

at polylogarithmic depth and an optimized `exp(-c (log N)^(2/3))` bound.

The cofactor-layer family is one-dimensional: its mean witness count is only order `log J`, so its natural large-sieve exponents are `(log log N)^2` and optimized `sqrt(log N)`.

This is a genuine distinction of search spaces, not a defect in the proof.

## 8. Publication / priority note

The large-sieve machinery, `kappa_0`, and the optimized constants above come directly from Dahan's one-parameter analysis. The contribution here is the identification and hypothesis check showing that the complementary-cofactor shift-divisor subsystem has the same prime-witness local counting data, so the analytic bound transfers to this differently located affine family.

Any publication should cite Dahan explicitly, should not call the two affine witness systems identical, and should not present the analytic machinery or constants as new.