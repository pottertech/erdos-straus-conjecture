# Complete Centered Binary Criterion

**Status:** exact algebraic equivalence

Let

\[
K=\frac{n+u}{4},
\qquad
M=nK,
\qquad
u\equiv3\pmod4,
\]

with `gcd(M,u)=1`.

The centered product criterion says that the `u`-method succeeds exactly when there are signed prime exponents

\[
-v_p(M)\le c_p\le v_p(M)
\]

such that

\[
\prod_{p\mid M}p^{c_p}\equiv-1\pmod u.
\]

Split the positive and negative exponents:

\[
A=\prod_{c_p>0}p^{c_p},
\qquad
B=\prod_{c_p<0}p^{-c_p}.
\]

Then

\[
(A,B)=1,
\qquad AB\mid M,
\]

and the centered congruence is

\[
AB^{-1}\equiv-1\pmod u,
\]

which is equivalent to

\[
\boxed{A+B\equiv0\pmod u.}
\]

Conversely, any coprime positive integers `A,B` with `AB|M` and `u|A+B` define an admissible signed exponent vector and hence an exact centered certificate.

Therefore:

\[
\boxed{
\text{the }u\text{-method succeeds}
\iff
\exists A,B>0:\ (A,B)=1,\ AB\mid nK,\ u\mid A+B.
}
\]

## Prime n: untwisted and twisted branches

When `n` is prime and `gcd(n,K)=1`, the prime `n` can occur in at most one of `A,B`.

### Untwisted branch

If neither member contains `n`, then

\[
A B\mid K,
\qquad
u\mid A+B.
\]

### Twisted branch

If, say, `A=nA_0`, then

\[
A_0B\mid K,
\qquad
u\mid nA_0+B.
\]

(The case where `n` occurs in `B` is symmetric after swapping the pair.)

These are the complete fixed-shift binary branches.

## Unit-partner slice

The unit-partner criterion is the special case where one binary member equals `1`.

Untwisted unit partner:

\[
B=1,\qquad d=A\mid K,\qquad d\equiv-1\pmod u.
\]

Twisted unit partner:

\[
B=1,\qquad d=A_0\mid K,\qquad nd\equiv-1\pmod u.
\]

Thus the unit-partner search is a strict slice of the complete binary criterion.

## The permanent 2521 exception

For

\[
n=2521,
\qquad u=31,
\qquad K=638=2\cdot11\cdot29,
\]

the pair

\[
A=2,\qquad B=29
\]

satisfies

\[
(A,B)=1,\qquad AB\mid K,\qquad A+B=31.
\]

So the complete binary criterion succeeds although, as proved separately, no unit-partner certificate exists at any shift.

This demonstrates why a global theorem should target the complete binary criterion, while using the unit-partner sieve as the dominant branch plus explicit treatment of any residual non-unit exceptions.
