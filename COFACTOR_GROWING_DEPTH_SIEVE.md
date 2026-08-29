# Growing-Depth Sieve for the Cofactor Shift-Divisor Family

**Status:** unconditional theorem by direct specialization of the one-parameter large-sieve argument in Dahan (2026); no priority claimed for the analytic mechanism

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

## 2. Exact match with Dahan's one-parameter counting function

Benjamin Dahan, arXiv:2608.24035 (2026), Section 4.3, studies a one-parameter witness system whose large-sieve counting function is

\[
\rho_J(q)=\#\{u\le J:4u\mid q+1\}.
\]

This is exactly the same arithmetic function after renaming `u` as the cofactor-layer parameter `a`.

The actual residue classes removed modulo `q` are different affine classes, but the large-sieve upper bound uses their number and pairwise distinctness, not their location. Consequently Dahan's one-parameter proof applies verbatim to the cofactor prime-witness system.

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

The one-parameter modulus is only `4a <= 4J`, so the Bombieri--Vinogradov step is valid with the sharper lower cutoff `J^3` used in Dahan's one-parameter discussion.

## 4. Polylogarithmic growing depth

Let

\[
J=(\log N)^\lambda,
\qquad \lambda\ge1
\]

be fixed.

The one-parameter large-sieve argument therefore gives

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

Dahan's Table 1 records the optimized one-parameter regime using the sharper `J^3` cutoff. Because our local counting function is identical, the same optimization applies:

\[
\boxed{
J=\exp\!\big((0.308+o(1))\sqrt{\log N}\big)
}
\]

is compatible with the bound

\[
\boxed{
|E_{\mathrm{cof}}(N;J)|
\ll
N\exp\!\big(-(0.199+o(1))\sqrt{\log N}\big).
}
\]

The numerical constants are inherited from the same one-parameter large-sieve optimization and are not claimed as new.

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

The large-sieve machinery and the constants above come directly from Dahan's one-parameter analysis. The contribution here is the exact identification that the complementary-cofactor shift-divisor subsystem has the same local counting function, allowing the theorem to be transferred to this separately parametrized Type-A/ED2 slice.

Any publication should cite Dahan explicitly and should not present the analytic machinery or constants as new.