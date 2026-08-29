# Classical Modular Core Before the u-Method

**Date:** 2026-08-28  
**Status:** Classical reduction; use before defining any residual/hard family

The project previously carried a much larger `n ≡ 1 (mod 12)` residual family.  That is unnecessarily broad.  Standard modular identities reduce the prime problem much further before any divisor-product or u-method analysis is needed.

## 1. Reduction to primes

If a prime divisor `p|n` has

\[
\frac4p=\frac1a+\frac1b+\frac1c,
\]

then multiplying the three denominators by `n/p` gives a solution for `n`.  Hence it is enough to prove the conjecture for primes.

## 2. Reduction to `p ≡ 1 (mod 24)`

The standard elementary identities (together with the even cases) eliminate all prime residue classes except

\[
\boxed{p\equiv1\pmod{24}}.
\]

In particular the `p ≡ 5 (mod 8)` identity is important and was not being used as the canonical front-end reduction in older project notes.

A correct identity for `n=8k+5` is

\[
\frac4n
=
\frac1{2k+2}
+
\frac1{n(k+1)}
+
\frac1{2n(k+1)}.
\]

Equivalently,

\[
\left(x,y,z\right)
=
\left(\frac{n+3}{4},\frac{n(n+3)}8,\frac{n(n+3)}4\right).
\]

## 3. Mod-5 identities inside the residual `p ≡ 1 (mod 3)` class

For the residual primes, `p ≡ 1 (mod 3)`.  Thus `p ≡ 2 (mod 5)` is equivalent to `p ≡ 7 (mod 15)`, and `p ≡ 3 (mod 5)` is equivalent to `p ≡ 13 (mod 15)`.

For `n=15k+7`,

\[
\left(x,y,z\right)
=
\left(4k+2,\ 4n,\ 4n(2k+1)\right),
\]

which is the same as

\[
\left(\frac{2(2n+1)}{15},\ 4n,\ \frac{4n(2n+1)}{15}\right).
\]

For `n=15k+13`,

\[
\left(x,y,z\right)
=
\left(4k+4,\ 4n,\ 2n(k+1)\right),
\]

which is

\[
\left(\frac{4(n+2)}{15},\ 4n,\ \frac{2n(n+2)}{15}\right).
\]

Therefore a residual prime must have

\[
p\equiv1\text{ or }4\pmod5.
\]

(The case `p=5` is already solved and is not in `p ≡ 1 (mod 24)`.)

## 4. Mod-7 identities

The classical nonresidue classes modulo 7 also have explicit identities.

### `n ≡ 3 (mod 7)`

Write `n=7k+3`.  Then

\[
\left(x,y,z\right)
=
\left(2k+1,\ 2n,\ 2n(2k+1)\right)
\]

or equivalently

\[
\left(\frac{2n+1}{7},\ 2n,\ \frac{2n(2n+1)}7\right).
\]

**Note:** some secondary sources omit the factor `2` in the third denominator; that transcription is false.  The formula displayed here has been checked by exact polynomial identity.

### `n ≡ 5 (mod 7)`

Write `n=7k+5`.  Then

\[
\left(x,y,z\right)
=
\left(2k+2,\ 2n,\ n(k+1)\right)
\]

or

\[
\left(\frac{2(n+2)}7,\ 2n,\ \frac{n(n+2)}7\right).
\]

### `n ≡ 6 (mod 7)`

Write `n=7k+6`.  Then

\[
\left(x,y,z\right)
=
\left(2k+2,\ 2n,\ 2n(k+1)\right)
\]

or

\[
\left(\frac{2(n+1)}7,\ 2n,\ \frac{2n(n+1)}7\right).
\]

Hence a residual prime must satisfy

\[
p\equiv1,2,4\pmod7.
\]

## 5. Six classical residue classes modulo 840

Combining

\[
p\equiv1\pmod{24},
\qquad
p\equiv1,4\pmod5,
\qquad
p\equiv1,2,4\pmod7
\]

by CRT gives exactly six classes modulo

\[
\operatorname{lcm}(24,5,7)=840:
\]

\[
\boxed{
1,\ 121,\ 169,\ 289,\ 361,\ 529\pmod{840}.
}
\]

These are the classical modular-core candidates.  Any modern u-method/divisor-product analysis should start here, not from all `n ≡ 1 (mod 12)` values.

## 6. Connection to the corrected data

Modulo 120, the six classes reduce to only

\[
\boxed{1\text{ or }49\pmod{120}.}
\]

This explains a previously puzzling feature of the corrected `10^7` run: every case whose first-working u changed after fixing the old three-target shortcut lay in `1` or `49 mod 120`.  Those are precisely the genuinely classical residual mod-120 classes; the other classes being called “hard” in older project documents were already covered by standard identities.

## 7. Project policy

Going forward:

1. use the classical six-class set as the canonical prime residual population;
2. treat older `n ≡ 1 (mod 12), 5 ∤ n` hard-case counts as historical/nonminimal;
3. run corrected centered-capacity and u-method experiments primarily on the six classes;
4. keep computational evidence separate from universal theorem claims.
