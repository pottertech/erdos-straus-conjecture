# Citation-Level Audit of the Unit-Partner Fixed-Shift Sieve

**Status:** completed for fixed finite shift sets

This note records exactly which ingredients are internal and which are standard analytic inputs for `UNIT_PARTNER_MULTI_SHIFT_SIEVE.md`.

## Internal exact ingredients

The repository proves directly:

1. For every `u == 3 (mod 4)`, the involution
   \[
   r\mapsto-r^{-1}
   \]
   on `(Z/uZ)^×` is fixed-point-free.
2. If `K=(n+u)/4` has no divisor `d == -1 (mod u)`, the distinct unit residue classes occupied by prime factors of `K` have cardinality at most `phi(u)/2`.
3. For distinct fixed shifts `u != v`, the sieve residue classes `-u` and `-v` modulo a rational prime `q` are distinct once `q>|u-v|`.
4. If `q|n+u` and `q` is odd, then `q|K=(n+u)/4`.

These steps require no analytic number theory.

## Standard analytic input 1: Mertens/PNT in fixed arithmetic progressions

For a fixed modulus `u` and a fixed set `B` of reduced residue classes modulo `u`,

\[
\sum_{\substack{q\le z\\q\bmod u\in B}}\frac1q
=
\frac{|B|}{\varphi(u)}\log\log z+O_u(1).
\]

Only fixed moduli are used in the theorem. No uniformity in a growing modulus is required.

For a half-sized forbidden set `B_u`, this contributes exactly

\[
\frac12\log\log z+O_u(1)
\]

to the sieve density.

## Standard analytic input 2: Selberg upper-bound/fundamental sieve lemma

The integer interval

\[
\mathcal A=[1,N]\cap\mathbb Z
\]

is sifted by finitely many residue classes modulo each rational prime `q`.

For squarefree `d`, CRT gives a multiplicative residue-count function `omega(d)` and

\[
|\mathcal A_d|
=
\frac{N\omega(d)}d+R_d,
\qquad
|R_d|\le\omega(d).
\]

For a fixed shift set, `omega(q)` is uniformly bounded and `omega(q)/q` stays uniformly below `1` after discarding finitely many small primes. The standard fundamental lemma of the Selberg sieve therefore gives

\[
S(\mathcal A,z)
\ll
N\prod_{q\le z}\left(1-\frac{\omega(q)}q\right)
\]

for `z=N^delta` with sufficiently small fixed `delta>0` depending only on the fixed sieve dimension.

A standard reference is:

- H. Halberstam and H.-E. Richert, *Sieve Methods*, Academic Press, 1974, the Selberg upper-bound/fundamental-lemma material (Dahan cites Theorem 3.2 of this source in his fixed-depth proof).

A modern reference is:

- J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57, 2010.

## Direct comparison with Dahan 2026

Benjamin Dahan, arXiv:2608.24035, proves in Lemma 4.2 that if an integer `M` has no divisor `-1 mod 4m`, then its prime-factor residue set occupies at most half of `(Z/4mZ)^×`, via the same fixed-point-free involution.

His Theorem 4.3 then considers a fixed finite witness set `P` and obtains

\[
|E_P(N)|\ll_P N(\log N)^{-1-|P|/2}.
\]

Dahan sieves the sequence of primes directly. His proof uses:

- PNT in fixed arithmetic progressions to compute the mean local density;
- Selberg's upper-bound sieve in Halberstam--Richert's form;
- Bombieri--Vinogradov to control the remainder for the prime sequence.

Our fixed-shift proof has the same local-dimension calculation but instead sieves the integer interval and includes `n == 0 (mod q)` as an additional forbidden class. This supplies the primality exponent `1` inside the sieve and leaves the elementary remainder `|R_d| <= omega(d)`. Therefore Bombieri--Vinogradov is not needed for the fixed finite unit-partner theorem.

## Certified conclusion

For every fixed finite set `U` of `P` admissible shifts,

\[
\boxed{
|E_U(N)|\ll_U N(\log N)^{-1-P/2}.
}
\]

This is now the certified status used by the repository.

For the actual computational shift set

\[
U=\{3,7,11,\ldots,299\},
\qquad P=75,
\]

one obtains

\[
\boxed{
|E_U(N)|\ll N(\log N)^{-77/2}.
}
\]

## Why this still does not prove finiteness

The fixed-shift-set constant depends on `U`. The theorem is not uniform in a shift set whose cardinality grows with `N`.

Trying to let `P=P(N)` grow introduces at least three new issues:

1. the number of possible local half-group profiles grows rapidly with the moduli;
2. the sieve dimension itself grows, so fixed-dimension fundamental-lemma constants are no longer uniform;
3. Mertens/PNT-in-AP input must become uniform in the growing shift moduli.

Dahan's Section 4.3 handles an analogous growing-depth problem by switching to a large-sieve/Bombieri--Vinogradov architecture rather than extrapolating Theorem 4.3. The same distinction must be respected here.

Thus the fixed 75-window theorem is rigorous and very strong as a density statement, but it cannot be iterated formally into a proof that there are only finitely many exceptions.
