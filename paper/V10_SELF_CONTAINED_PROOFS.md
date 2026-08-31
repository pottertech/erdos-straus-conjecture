# v10 self-contained proof insertions

**Purpose.** These are the two proof blocks that replace the two non-self-contained places in v9: Proposition 1 and the canonical no-reuse theorem. They are written for direct insertion into `composite_exact_typeii_depths_v10.tex`.

## 1. Complete prime Type-II coordinate

The completeness statement is prior mathematics. We use Pomerance--Weingartner, Corollary 2.4, specialized to `m=4`: for a prime `p`, a Type-II solution exists iff there are positive integers `a,b,e` with

\[
e\mid a+b,\qquad 4ab\mid p+e.
\]

The following gives the exact equivalence with the square coordinate used in the paper.

### Forward map

Assume the Pomerance--Weingartner conditions. Put

\[
c=(a+b)/e,
\qquad
\alpha=(p+e)/(4ab),
\]

and define

\[
A=\alpha ac,
\qquad
D=\alpha a^2.
\]

Then

\[
A^2/D=\alpha c^2\in\mathbf N,
\]

so `D|A^2`. Since `b=ce-a`,

\[
\alpha ab+D=\alpha a(ce-a)+\alpha a^2=\alpha ace=Ae.
\]

Hence

\[
p+4D=4(\alpha ab+D)-e=(4A-1)e,
\]

and therefore `4A-1 | p+4D`.

### Reverse map

Assume

\[
D\mid A^2,
\qquad
p+4D=(4A-1)q
\]

with `A,D,q>0`. Put `E=A^2/D` and `alpha=gcd(D,E)`. Because `DE=A^2` is a square and `D/alpha,E/alpha` are coprime, there are coprime positive integers `u,c` such that

\[
D=\alpha u^2,
\qquad
E=\alpha c^2,
\qquad
A=\alpha uc.
\]

Then

\[
p+4\alpha u^2=(4\alpha uc-1)q,
\]

so

\[
p+q=4\alpha u(cq-u).
\]

Let `t=cq-u`. Since the left side is positive, `t>0`. Consequently

\[
4ut\mid p+q
\]

and

\[
q\mid u+t
\]

because `u+t=cq`. Thus the Pomerance--Weingartner criterion holds with

\[
a=u,\qquad b=t,\qquad e=q.
\]

This proves the equivalence. The manuscript should explicitly say that no novelty is claimed for this parametrization.

---

## 2. Canonical no-reuse theorem

For a positive integer `d`, define

\[
\operatorname{src}(d)=\prod_p p^{\lceil v_p(d)/2\rceil}.
\]

Then

\[
d\mid B^2\iff \operatorname{src}(d)\mid B.
\]

Write `d=uw` with `u=src(d)`; prime by prime, `w<=u`.

At an exceptional earlier modulus `4B-1=cr`, the degenerate master-equation case `k=0` means `E=d`. Under the global square-safe assignment `n=1` away from the target primes, such a collision requires simultaneously

\[
d\mid B^2,
\qquad
c\mid4d+1.
\]

We rule this out in the four canonical residue classes.

### Case `s == 3 (mod 8)`

Here

\[
d=(s+1)/2=2m,
\qquad m\text{ odd},
\qquad r\equiv2d+1\pmod{4d}.
\]

Let `u0=src(m)` and `m=u0 w0`, with `w0<=u0`. Exceptional cofactors satisfy `c==3 (mod 4)`. If `d|B^2`, the 2-adic part makes `B` even, hence `c==3 (mod 8)`, and the odd part gives `u0|c+1`. If also `4d+1=8m+1=ct`, then `t==-1 (mod u0)` and `t==3 (mod 8)`. Thus

\[
c=u_0a-1,
\qquad t=u_0b-1,
\qquad a,b\ge4.
\]

Expanding `ct=8u0 w0+1` gives

\[
ab u_0-(a+b)=8w_0.
\]

But the left side is at least `16u0-8>8u0>=8w0`, contradiction.

### Case `s == 7 (mod 8)`

Here

\[
d=(s-1)/2
\]

is odd and

\[
r\equiv2d-1\pmod{4d}.
\]

Put `u=src(d)` and `d=uw`, `w<=u`. Exceptional cofactors satisfy `c==3 (mod 4)`. From `u|B` and

\[
4B=cr+1\equiv1-c\pmod u
\]

we get `u|c-1`. If `4d+1=ct`, then also `t==1 (mod u)`. Since `ct==1 (mod 4)` and `c==3 (mod 4)`, also `t==3 (mod 4)`. Hence

\[
c=ua+1,
\qquad t=ub+1,
\qquad a,b\ge2.
\]

Expansion yields

\[
ab u+(a+b)=4w,
\]

whose left side is at least `4u+4` while the right side is at most `4u`, contradiction.

### Case `s == 5 (mod 8)`

Take

\[
d=s-1=4m,
\qquad m\text{ odd},
\qquad r\equiv d-1\pmod{4d}.
\]

Let `u0=src(m)`, `m=u0w0`, `w0<=u0`. Exceptional cofactors satisfy `c==1 (mod 4)`. The case `c=1` cannot reuse `d`, since

\[
B=(r+1)/4\equiv d/4\pmod d
\]

has `v2(B)=0` while `v2(d)=2`. For `c>1`, `d|B^2` implies `u0|c-1`. If `4d+1=16m+1=ct`, then also `t==1 (mod u0)`. Both `c,t` are `1 (mod 4)`, so

\[
c=u_0a+1,
\qquad t=u_0b+1,
\qquad a,b\ge4.
\]

Expansion gives

\[
ab u_0+(a+b)=16w_0,
\]

but the left side is at least `16u0+8>16w0`, contradiction.

### Case `s == 1 (mod 8)`

Let

\[
e=v_2(s-1)\ge3,
\qquad s-1=2^e m,
\qquad m\text{ odd},
\]

and use the reinforced witness

\[
d=2^{e-3}(s-1)=2^{2e-3}m.
\]

Let `u0=src(m)`, `m=u0w0`, `w0<=u0`; then

\[
\operatorname{src}(d)=2^{e-1}u_0.
\]

The parameter class is

\[
r\equiv-s^{-1}\pmod{4d}.
\]

If `d|B^2`, then `src(d)|B`, so

\[
2^{e+1}u_0\mid cr+1.
\]

On the odd part, `r==-1 (mod u0)`, giving `u0|c-1`. On the 2-adic part,

\[
r\equiv2^e-1\pmod{2^{e+1}},
\]

so `2^{e+1}|cr+1` forces

\[
c\equiv2^e+1\pmod{2^{e+1}}.
\]

If also `4d+1=ct`, then the same congruences give

\[
t\equiv2^e+1\pmod{2^{e+1}}.
\]

Thus

\[
c=u_0a+1,
\qquad t=u_0b+1,
\qquad a,b\ge2^e.
\]

Since

\[
4d+1=2^{2e-1}u_0w_0+1,
\]

expansion gives

\[
ab u_0+(a+b)=2^{2e-1}w_0.
\]

But

\[
ab u_0+(a+b)\ge2^{2e}u_0+2^{e+1}>2^{2e-1}u_0\ge2^{2e-1}w_0,
\]

contradiction. This also excludes `c=1`.

Therefore the degenerate divisor-reuse case `k=0` is impossible for every canonical prime-cofactor family.