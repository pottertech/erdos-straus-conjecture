# Primary-Source Audit of the Complete Prime Type-II Square Coordinate

**Date:** 2026-08-31

**Purpose:** make the foundational coordinate used in v9 explicitly equivalent to a modern primary-source complete Type-II criterion.

## Primary source

Pomerance--Weingartner, *Exceptions to the Erdős--Straus--Schinzel conjecture* (2026), Corollary 2.4, specialized to `m=4`:

> For prime `p`, a Type-II solution of `4/p` exists if and only if there are positive integers `a,b,e` with
> 
> `e | a+b` and `4ab | p+e`.

This criterion is complete for prime Type-II solutions.

## Square coordinate

The manuscript uses the equivalent condition

\[
\exists A,D>0:\qquad D\mid A^2,\qquad 4A-1\mid p+4D.
\]

For prime `p`, the harmless condition `p\nmid D` follows for an actual Type-II solution / reduced target progression; it can also be retained explicitly in the proposition.

## From Pomerance--Weingartner to the square coordinate

Assume

\[
e\mid a+b,
\qquad
4ab\mid p+e.
\]

Write

\[
c=\frac{a+b}{e},
\qquad
\alpha=\frac{p+e}{4ab}.
\]

Thus

\[
a+b=ce,
\qquad
p+e=4\alpha ab.
\]

Define

\[
\boxed{A=\alpha ac,\qquad D=\alpha a^2.}
\]

Then

\[
\frac{A^2}{D}=\alpha c^2\in\mathbb N,
\]

so

\[
D\mid A^2.
\]

Also, since `b=ce-a`,

\[
\alpha ab+D
=\alpha a(ce-a)+\alpha a^2
=\alpha ace
=Ae.
\]

Therefore

\[
\begin{aligned}
p+4D
&=(4\alpha ab-e)+4D\\
&=4(\alpha ab+D)-e\\
&=4Ae-e\\
&=(4A-1)e.
\end{aligned}
\]

Hence

\[
\boxed{4A-1\mid p+4D.}
\]

## From the square coordinate to Pomerance--Weingartner

Assume

\[
D\mid A^2,
\qquad
p+4D=(4A-1)q
\]

for some positive integer `q`.

Put

\[
E=\frac{A^2}{D}.
\]

Let

\[
\alpha=\gcd(D,E).
\]

Because

\[
DE=A^2
\]

is a square and `D/alpha`, `E/alpha` are coprime, both quotients are squares. Thus there are coprime positive integers `u,c` with

\[
\boxed{D=\alpha u^2,\qquad E=\alpha c^2,\qquad A=\alpha uc.}
\]

The square congruence becomes

\[
p+4\alpha u^2=(4\alpha uc-1)q.
\]

Rearranging,

\[
p+q=4\alpha u(cq-u).
\]

Define

\[
\boxed{t=cq-u.}
\]

The positivity of the Type-II construction gives `t>0`; equivalently this follows from `p+q>0` in the displayed identity.

Now

\[
4ut\mid p+q
\]

because

\[
p+q=4\alpha ut,
\]

and

\[
q\mid u+t
\]

because

\[
u+t=cq.
\]

Thus the Pomerance--Weingartner criterion holds with

\[
\boxed{a=u,\qquad b=t,\qquad e=q.}
\]

Therefore the square-divisor coordinate is complete for prime Type-II solutions.

## Manuscript recommendation

Replace the currently unproved Proposition 1 in the next manuscript revision by a short proof or an appendix containing the two maps above, citing Pomerance--Weingartner Corollary 2.4 as the complete modern criterion.

This strengthens the paper's claim boundary:

- completeness of the coordinate is prior mathematics;
- the explicit coordinate equivalence is included for self-containment;
- no novelty is claimed for the parametrization.
