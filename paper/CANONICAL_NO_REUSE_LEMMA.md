# Universal No-Reuse Lemma for the Canonical Prime-Cofactor Families

**Status:** unconditional repair of the `k=0` gap in the canonical fixed-prime hierarchy.

The repaired fixed-cofactor theorem chooses the square-safe residue `1` on every coordinate outside the target primes. At an exceptional earlier modulus

\[
4B-1=cr,
\]

the degenerate master-equation case `k=0` means `E=d`. Such a collision requires simultaneously

\[
\boxed{d\mid B^2}
\]

and

\[
\boxed{c\mid4d+1.}
\]

We prove that these two conditions are incompatible for the canonical fixed-prime families in every residue class `s mod 8`.

For a positive integer `d`, define its least square-root closure

\[
\operatorname{src}(d)=\prod_p p^{\lceil v_p(d)/2\rceil}.
\]

Then

\[
\boxed{d\mid B^2\iff \operatorname{src}(d)\mid B.}
\]

Write `d=u w` with `u=src(d)`. Prime by prime,

\[
\boxed{w\le u.}
\]

We use this inequality in all four cases.

---

## 1. `s ≡ 3 (mod 8)`

Here

\[
d=\frac{s+1}{2},
\qquad
s=2d-1,
\qquad
r\equiv2d+1\pmod{4d}.
\]

Since `d≡2 (mod 4)`, write

\[
d=2m,
\qquad
m\text{ odd}.
\]

Let `u_0=src(m)` and `m=u_0w_0`, so `w_0<=u_0`.

An exceptional cofactor satisfies `c≡3 (mod 4)`. Suppose for contradiction that

\[
d\mid B^2,
\qquad
c\mid4d+1=8m+1.
\]

The 2-adic part of `d|B^2` forces `B` even, hence `c≡3 (mod 8)`. For every odd prime power in `m`, the condition `src(m)|B` and

\[
4B=cr+1\equiv c+1\pmod{u_0}
\]

give

\[
u_0\mid c+1.
\]

Put

\[
8m+1=ct.
\]

Modulo `u_0`, the product is `1` and `c≡-1`, so also

\[
t\equiv-1\pmod{u_0}.
\]

Because `8m+1≡1 (mod 8)` and `c≡3 (mod 8)`, also `t≡3 (mod 8)`. Thus

\[
c=u_0a-1,
\qquad
t=u_0b-1,
\]

with

\[
\boxed{a,b\ge4.}
\]

Expanding `ct=8u_0w_0+1` gives

\[
ab u_0-(a+b)=8w_0.
\]

But

\[
ab u_0-(a+b)\ge16u_0-8>8u_0\ge8w_0,
\]

a contradiction.

---

## 2. `s ≡ 7 (mod 8)`

Here

\[
d=\frac{s-1}{2},
\qquad
s=2d+1,
\qquad
r\equiv2d-1\pmod{4d},
\]

and `d` is odd. Put

\[
u=\operatorname{src}(d),
\qquad d=uw,
\qquad w\le u.
\]

Exceptional cofactors satisfy `c≡3 (mod 4)`. If `d|B^2`, then `u|B`; because

\[
4B=cr+1\equiv1-c\pmod u,
\]

we obtain

\[
u\mid c-1.
\]

If also `c|4d+1`, write `4d+1=ct`. Then `t≡1 (mod u)`. Since `ct≡1 (mod 4)` and `c≡3 (mod 4)`, also `t≡3 (mod 4)`. Hence

\[
c=ua+1,
\qquad t=ub+1,
\]

with

\[
\boxed{a,b\ge2.}
\]

Expansion gives

\[
ab u+(a+b)=4w.
\]

The left side is at least `4u+4`, whereas the right side is at most `4u`, contradiction.

---

## 3. `s ≡ 5 (mod 8)`

Take

\[
d=s-1.
\]

Then `v_2(d)=2`. Write

\[
d=4m,
\qquad m\text{ odd},
\]

and let

\[
u_0=\operatorname{src}(m),
\qquad m=u_0w_0,
\qquad w_0\le u_0.
\]

The canonical parameter class is

\[
r\equiv d-1\pmod{4d}.
\]

Exceptional cofactors now satisfy `c≡1 (mod 4)`.

The case `c=1` cannot reuse `d`: here

\[
B=\frac{r+1}{4}\equiv\frac d4\pmod d,
\]

and `v_2(B)=0` while `v_2(d)=2`, so `d∤B^2`.

Assume `c>1`, `d|B^2`, and `c|4d+1=16m+1`. Since `src(d)=2u_0`, the condition `src(d)|B` implies, on the odd part,

\[
u_0\mid c-1.
\]

Writing `16m+1=ct`, we likewise have `t≡1 (mod u_0)`. Both `c` and `t` are `1 mod 4`, so

\[
c=u_0a+1,
\qquad t=u_0b+1,
\]

with

\[
\boxed{a,b\ge4.}
\]

Expansion gives

\[
ab u_0+(a+b)=16w_0.
\]

The left side is at least `16u_0+8`, while the right side is at most `16u_0`, contradiction.

---

## 4. `s ≡ 1 (mod 8)`

The naive witness `(s-1)/2` has a genuine `c=1` reuse problem and must **not** be used. Let

\[
e=v_2(s-1)\ge3
\]

and use the reinforced canonical witness

\[
\boxed{d=2^{e-3}(s-1).}
\]

Write

\[
s-1=2^e m,
\qquad m\text{ odd}.
\]

Then

\[
d=2^{2e-3}m.
\]

Let

\[
u_0=\operatorname{src}(m),
\qquad m=u_0w_0,
\qquad w_0\le u_0.
\]

The full square-root closure is

\[
\operatorname{src}(d)=2^{e-1}u_0.
\]

Choose the parameter class

\[
\boxed{r\equiv-s^{-1}\pmod{4d}.}
\]

It satisfies `r≡-1 (mod s-1)` and `r≡7 (mod 8)`.

If `d|B^2`, then `src(d)|B`, so

\[
2^{e+1}u_0\mid cr+1.
\]

On the odd part, `r≡-1 (mod u_0)`, hence

\[
u_0\mid c-1.
\]

On the 2-adic part, because

\[
s=1+2^e m\equiv1+2^e\pmod{2^{e+1}},
\]

one has

\[
r\equiv-s^{-1}\equiv2^e-1\pmod{2^{e+1}}.
\]

Thus `2^{e+1}|cr+1` forces

\[
\boxed{c\equiv2^e+1\pmod{2^{e+1}}.}
\]

If also `c|4d+1`, put `4d+1=ct`. The numerator is `1 mod 2^{e+1}` and `c^{-1}≡c` modulo `2^{e+1}`, so

\[
\boxed{t\equiv2^e+1\pmod{2^{e+1}}.}
\]

Therefore

\[
c=u_0a+1,
\qquad t=u_0b+1,
\]

with

\[
\boxed{a,b\ge2^e.}
\]

Now

\[
4d+1=2^{2e-1}u_0w_0+1,
\]

so expansion gives

\[
ab u_0+(a+b)=2^{2e-1}w_0.
\]

But

\[
ab u_0+(a+b)
\ge2^{2e}u_0+2^{e+1}
>2^{2e-1}u_0
\ge2^{2e-1}w_0,
\]

contradiction.

This also handles `c=1`, since the required congruence `c≡2^e+1 (mod 2^{e+1})` already fails.

---

## 5. Consequence

In every residue class `s mod 8`, the canonical fixed-prime data satisfy

\[
\boxed{
\neg\left(d\mid B_c^2\ \text{ and }\ c\mid4d+1\right)
}
\]

for every exceptional cofactor `c<s`.

Thus the `k=0` divisor-reuse case is impossible under the global square-safe assignment `n≡1` away from the target coordinates. Every actual collision has

\[
k\ge1,
\qquad h\ge1,
\qquad kh<dc^2,
\]

and the master-equation finite-exception proof is valid.

Accordingly the canonical hierarchy can be stated unconditionally for every fixed prime `s>3`, provided the `s≡1 (mod 8)` row uses the reinforced witness

\[
\boxed{d=2^{v_2(s-1)-3}(s-1)}
\]

rather than `(s-1)/2`.

## Claim boundary

This note repairs an internal proof gap. It does not alter the distinction between exact square-completed Type-II depth and the full Erdős--Straus conjecture, and it does not establish publication priority.