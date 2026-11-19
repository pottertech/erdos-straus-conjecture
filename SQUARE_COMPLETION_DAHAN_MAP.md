# Square-Completed Type A as a Compression of the Complete Type-II Parameters

**Status:** exact algebraic equivalence / literature alignment

Recent Type-A/B work records the exact square completion

\[
\text{prime Type II}
\iff
\exists A,D>0:
D\mid A^2,
\quad
4A-1\mid n+4D,
\quad n\nmid D.
\]

This note identifies those coordinates exactly with the two-parameter Type-II criterion of Dahan (2026), Theorem 3.9. The result is a change of variables, not a new completeness theorem.

## 1. Dahan coordinates

Dahan's Type-II criterion can be written as the existence of positive integers

\[
u,a,\alpha
\]

such that the divisor witness

\[
s=4\alpha ua-1
\]

satisfies

\[
s\mid an+u.
\]

The search-depth parameters are `u,a`; `alpha=(s+1)/(4ua)` is the witness quotient.

We may assume

\[
\gcd(u,a)=1.
\]

## 2. Compress to square-completion coordinates

Define

\[
\boxed{A=\alpha ua,}
\qquad
\boxed{D=\alpha u^2.}
\]

Then

\[
4A-1=s
\]

and

\[
A^2=\alpha^2u^2a^2
=D\,(\alpha a^2),
\]

so

\[
\boxed{D\mid A^2.}
\]

Now multiply `n+4D` by `a`:

\[
a(n+4D)=an+4\alpha u^2a.
\]

Modulo

\[
s=4\alpha ua-1,
\]

we have

\[
4\alpha u^2a
=u(4\alpha ua)
\equiv u\pmod s.
\]

Hence

\[
a(n+4D)\equiv an+u\pmod s.
\]

Since `s == -1 (mod a)`, `gcd(s,a)=1`. Therefore

\[
\boxed{
s\mid an+u
\iff
s\mid n+4D.
}
\]

Thus Dahan's witness becomes exactly

\[
\boxed{4A-1\mid n+4D.}
\]

## 3. Recover Dahan coordinates from D | A^2

Conversely suppose

\[
D\mid A^2.
\]

Put

\[
E=\frac{A^2}{D}
\]

and define

\[
\boxed{\alpha=\gcd(D,E).}
\]

We claim that

\[
\boxed{D/\alpha=u^2,}
\qquad
\boxed{E/\alpha=a^2}
\]

for coprime positive integers `u,a`.

This is checked prime by prime. If

\[
v_p(A)=t,
\qquad
v_p(D)=r,
\qquad 0\le r\le2t,
\]

then

\[
v_p(E)=2t-r
\]

and

\[
v_p(\alpha)=\min(r,2t-r).
\]

If `r <= t`, then

\[
v_p(D/\alpha)=0,
\qquad
v_p(E/\alpha)=2(t-r),
\]

while if `r >= t`,

\[
v_p(D/\alpha)=2(r-t),
\qquad
v_p(E/\alpha)=0.
\]

Thus both quotients are perfect squares and no prime divides both square roots. Define

\[
u=\sqrt{D/\alpha},
\qquad
a=\sqrt{E/\alpha}.
\]

Then

\[
\gcd(u,a)=1
\]

and

\[
A^2=D E
=\alpha^2u^2a^2.
\]

All quantities are positive, so

\[
\boxed{A=\alpha ua.}
\]

Therefore

\[
4A-1=4\alpha ua-1.
\]

As in Section 2, the congruence

\[
4A-1\mid n+4D
\]

is equivalent to

\[
4\alpha ua-1\mid an+u.
\]

This is exactly Dahan Theorem 3.9(ii).

## 4. Exact dictionary

The two coordinate systems are therefore related by

\[
\boxed{
A=\alpha ua,
\qquad
D=\alpha u^2,
\qquad
A^2/D=\alpha a^2.
}
\]

and inversely

\[
\boxed{
\alpha=\gcd(D,A^2/D),
\qquad
u=\sqrt{D/\alpha},
\qquad
a=\sqrt{(A^2/D)/\alpha}.
}
\]

The Dahan witness is

\[
\boxed{s=4A-1.}
\]

## 5. Example: n = 2521

The square-completed certificate

\[
A=12,
\qquad
D=16
\]

has

\[
A^2/D=144/16=9,
\]

so

\[
\alpha=\gcd(16,9)=1,
\qquad
u=4,
\qquad
a=3.
\]

The witness is

\[
s=4A-1=47.
\]

Indeed

\[
47\mid 3\cdot2521+4=7567.
\]

This is precisely Dahan Theorem 3.9 with the small coprime pair

\[
(u,a)=(4,3).
\]

## 6. Strategic meaning

The square-completion viewpoint and the two-parameter large-sieve viewpoint are two coordinate systems on the **same complete Type-II family**.

The square-completion coordinates are useful when importing López Type-A congruence/shadow machinery because Type A is obtained simply by replacing

\[
D\mid A^2
\]

with the stronger restriction

\[
D\mid A.
\]

The Dahan coordinates are superior for growing-depth analysis because the coprime pair `(u,a)` gives distinct residue classes for prime witnesses and leads directly to the `tau_3`-type large sieve.

Accordingly:

- do not claim a new Type-II completeness theorem from square completion;
- use square completion as a structural bridge from Type A to complete Type II;
- use Dahan's coordinates for the strongest established growing-depth density bounds.