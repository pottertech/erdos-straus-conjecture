# Binary-Sum Polynomial Family

**Status:** exact algebraic family derived from the complete centered binary criterion; no novelty or priority claim.

The complete centered binary criterion says that for

\[
K=\frac{n+u}{4},
\]

an Erdős--Straus decomposition follows whenever there are coprime positive divisors `A,B` with `AB | nK` and

\[
A+B\equiv0\pmod u.
\]

This note isolates a particularly transparent polynomial specialization in which the binary relation is built in from the start.

## 1. General r-family

Let `A,B,q,r,u,n` be positive integers satisfying

\[
A+B=ur
\]

and define

\[
K=ABq,
\qquad
n=4ABq-u.
\]

Then automatically

\[
4K=n+u.
\]

Set

\[
\boxed{x=ABq},
\qquad
\boxed{y=Anqr},
\qquad
\boxed{z=Bnqr}.
\]

Then

\[
\boxed{
\frac4n=\frac1x+\frac1y+\frac1z.
}
\]

### Direct proof

Because `A+B=ur`,

\[
\frac1y+\frac1z
=
\frac{A+B}{ABnqr}
=
\frac{ur}{ABnqr}
=
\frac{u}{ABnq}.
\]

Also

\[
\frac1x=\frac1{ABq}=\frac{n}{ABnq}.
\]

Therefore

\[
\frac1x+\frac1y+\frac1z
=
\frac{n+u}{ABnq}
=
\frac{4ABq}{ABnq}
=
\frac4n.
\]

Equivalently, exact cross-multiplication gives

\[
4xyz=n(xy+xz+yz).
\]

No primality assumption on `A`, `B`, or `q` is needed.  Coprimality of `A,B` is required only when interpreting this as a centered support-two divisor certificate; the displayed unit-fraction identity itself is algebraically valid whenever the parameters are positive integers satisfying the stated equations.

## 2. The r = 1 binary-sum family

The cleanest specialization is

\[
r=1,
\qquad
u=A+B.
\]

Then

\[
\boxed{n=4ABq-A-B}
\]

has the explicit decomposition

\[
\boxed{
\frac4{4ABq-A-B}
=
\frac1{ABq}
+
\frac1{Aq(4ABq-A-B)}
+
\frac1{Bq(4ABq-A-B)}.
}
\]

This is a three-parameter polynomial family in `A,B,q`.

If `A+B ≡ 3 (mod 4)`, then `n ≡ 1 (mod 4)`, so this family naturally intersects the difficult Erdős--Straus residue regime rather than merely reproducing even or elementary cases.

## 3. Unit-partner family as A = 1

The ordinary unit-partner slice is obtained by setting

\[
A=1.
\]

Then `B+1=ur`, and the construction becomes

\[
K=Bq,
\qquad
n=4Bq-u,
\]

with

\[
x=Bq,
\qquad
y=nqr,
\qquad z=Bnqr.
\]

Thus the cofactor/shift-divisor family is a strict one-sided slice of the full binary-sum polynomial family.

The full binary criterion can succeed even when every `A=1` slice fails, because two nontrivial complementary factors may satisfy `A+B ≡ 0 (mod u)`.

## 4. The n = 2521 rescue

The corrected `10^9` audit identifies

\[
n=2521
\]

as the permanent exception to the tested unit-partner slices, while the full centered binary criterion succeeds at `u=31` using

\[
A=2,
\qquad
B=29.
\]

This is exactly the `r=1` polynomial family:

\[
A+B=31=u,
\qquad
q=11,
\]

so

\[
K=ABq=2\cdot29\cdot11=638
\]

and

\[
n=4ABq-A-B
=4\cdot2\cdot29\cdot11-2-29
=2521.
\]

The explicit decomposition is

\[
\boxed{x=638},
\]

\[
\boxed{y=2\cdot2521\cdot11=55,462},
\]

\[
\boxed{z=29\cdot2521\cdot11=804,199}.
\]

Hence

\[
\boxed{
\frac4{2521}
=
\frac1{638}
+
\frac1{55,462}
+
\frac1{804,199}.
}
\]

This explains the finite `2521` rescue structurally: it is not an isolated accidental divisor certificate, but a genuine binary-sum case with both partners nontrivial.

## 5. Revised proof target

The corrected finite computation suggests a two-stage deterministic target.

### Stage A: unit-partner sieve

Find `u` and a divisor `B` such that

\[
B\equiv-1\pmod u.
\]

This is the `A=1` slice and covers essentially the entire corrected residual population in the current finite audit.

### Stage B: nontrivial binary rescue

For every number permanently avoiding Stage A, prove that some gate admits

\[
\boxed{A+B\equiv0\pmod u}
\]

with `A,B>1`, `gcd(A,B)=1`, and `AB | n(n+u)/4`.

The `2521` example shows that Stage B is not artificial: it is exactly what is needed beyond the unit-partner subsystem.

A universal theorem of this form would be stronger and more structurally faithful than trying to prove that the unit-partner family alone is universal.

## 6. Publication caution

The algebraic identity above is elementary and may overlap with existing parametrized Erdős--Straus identities.  No novelty claim is made here.  Any publication should perform a dedicated literature comparison before claiming priority for this parameterization or its interpretation.
