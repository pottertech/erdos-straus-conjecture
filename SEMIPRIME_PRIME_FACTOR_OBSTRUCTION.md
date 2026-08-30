# Universal Prime-Factor Obstruction for Primitive Semiprime Type-II Layers

**Status:** exact elementary consequence of the square-completed ancestor criterion. No claim of Type-II universality.

Let

\[
A=uv
\]

with distinct primes `u<v`, and let

\[
m=4uv-1.
\]

Suppose a proper prime divisor

\[
q\mid m,
\qquad q\equiv3\pmod4
\]

is present. Put

\[
B=\frac{q+1}{4}.
\]

Then `q=4B-1`, so depth `B` is a proper divisor-modulus ancestor of depth `A`.

The ancestor trap set uses

\[
Q_B=\{D\pmod q:D\mid B^2\}.
\]

Regardless of the factorization of `B`, the three divisors

\[
1,\quad B,\quad B^2
\]

belong to `Q_B`.

Therefore, if the mixed square direction at `A` is structurally primitive, it is necessary that

\[
\boxed{u^2\not\equiv1,B,B^2\pmod q.}
\]

Because

\[
B\equiv4^{-1}\pmod q,
\]

this is equivalently

\[
\boxed{
u\not\equiv \pm1,\ \pm2^{-1},\ \pm4^{-1}\pmod q.
}
\]

The same condition holds symmetrically for `v`.

## Immediate gcd consequences

A primitive mixed pair cannot have a proper `3 mod 4` prime divisor `q` of `m` satisfying any of

\[
q\mid u^2-1,
\]

\[
q\mid 4u^2-1,
\]

or

\[
q\mid16u^2-1.
\]

Thus every `3 mod 4` prime factor of `m` must avoid three universal quadratic targets before the fuller divisor set `Q_B` is even used.

Also, since

\[
4uv\equiv1\pmod q,
\]

the middle condition

\[
u^2\equiv B\equiv4^{-1}\pmod q
\]

is equivalent to

\[
u^2\equiv uv\pmod q,
\]

hence to

\[
\boxed{u\equiv v\pmod q.}
\]

Therefore a primitive semiprime layer also requires

\[
\boxed{q\nmid u-v}
\]

for every proper prime divisor `q == 3 (mod 4)` of `4uv-1`.

## Saturation at q = 3 and q = 7

For `q=3`, the unit square set has one class and the universal target `1` already captures it.

For `q=7`, the unit square set is

\[
\{1,2,4\},
\]

and for `B=2` the universal divisors `1,B,B^2` give exactly

\[
\{1,2,4\}.
\]

Hence a structurally primitive semiprime layer must satisfy

\[
\boxed{3\nmid4uv-1,\qquad7\nmid4uv-1.}
\]

Equivalently,

\[
uv\not\equiv1\pmod3,
\qquad
uv\not\equiv2\pmod7.
\]

This recovers the earlier exact `3/7` raw index-class elimination modulo `21` from a single prime-factor obstruction.

## Example q = 11

Here `B=3` and

\[
Q_3=\{1,3,9\}\pmod{11}.
\]

These are exactly the three universal classes `1,B,B^2`. The only missed unit square classes are

\[
4,5.
\]

Thus if `11 | 4uv-1` and the semiprime layer is primitive, then

\[
u^2\equiv4\text{ or }5\pmod{11},
\]

so

\[
u\equiv\pm2\text{ or }\pm4\pmod{11}.
\]

## Research significance

This lemma converts factorization of `4uv-1` into mandatory residue exclusions on `u` and `v`. Rich factorization supplies many simultaneous local restrictions.

The full ancestor set `Q_B` can only strengthen these exclusions. For example, at `q=23` (`B=6`) the complete `Q_6` leaves only two of eleven unit square classes, far stronger than the three universal targets alone.

A plausible descent theorem would show that a number `4uv-1` with sufficiently many suitable `3 mod 4` prime factors cannot support all of the required simultaneous exclusions. The finite census in `SEMIPRIME_ANCESTOR_CAPTURE_RIGIDITY.md` is consistent with this direction, but no such global theorem is claimed yet.
