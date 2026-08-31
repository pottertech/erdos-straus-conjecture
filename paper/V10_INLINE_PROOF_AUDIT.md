# Line-by-Line Audit of the v10 Inlined Proofs

**Date:** 2026-08-31

**Scope:** the two arguments newly moved into `composite_exact_typeii_depths_v10.tex`: the complete Type-II square-coordinate equivalence and the four-case canonical no-reuse theorem.

## A. Complete Type-II coordinate

### A1. Forward map

Starting from Pomerance--Weingartner Corollary 2.4 (specialized to `m=4`), assume

`e | a+b` and `4ab | p+e`.

Set

`c=(a+b)/e`, `alpha=(p+e)/(4ab)`, `A=alpha a c`, `D=alpha a^2`.

Checks:

- `A,D` are positive integers.
- `A^2/D = alpha c^2`, hence `D|A^2`.
- `b=ce-a`.
- `alpha ab + D = alpha a(ce-a)+alpha a^2 = alpha ace = Ae`.
- therefore `p+4D = 4(alpha ab+D)-e = (4A-1)e`.

Verdict: correct.

### A2. Reverse map

Assume `D|A^2` and `p+4D=(4A-1)q`, `q>0`.

Set `E=A^2/D`, `alpha=gcd(D,E)`. Since `DE=A^2` is a square and `D/alpha,E/alpha` are coprime, both quotients are squares:

`D=alpha u^2`, `E=alpha c^2`, `A=alpha u c`.

Then

`p+q=4 alpha u(cq-u)`.

Let `t=cq-u`. Because `p+q>0` and `alpha,u>0`, `t>0`. Hence

`4ut | p+q`

and

`q | u+t` because `u+t=cq`.

This is Pomerance--Weingartner Corollary 2.4 with `(a,b,e)=(u,t,q)`.

Verdict: correct.

### A3. Editorial recommendation

In the final typeset version cite Pomerance--Weingartner explicitly at the first sentence of the proof (`\cite{PW}`), rather than relying only on the bibliography entry.

---

## B. Canonical no-reuse theorem

The common necessary conditions for a `k=0` collision are

`d|B^2` and `c|4d+1`.

The identity

`d|B^2 iff src(d)|B`

is correct prime by prime. Writing `d=uw`, `u=src(d)`, gives `w<=u` prime by prime.

### B1. `s == 3 (mod 8)`

Here `d=(s+1)/2=2m`, `m` odd, and `r==2d+1 (mod 4d)`.

- `d|B^2` forces `B` even.
- Since `4B=cr+1` and `r==5 (mod 8)`, `B` even forces `cr+1==0 (mod 8)`, hence `c==3 (mod 8)`.
- On the odd square-root closure `u0=src(m)`, `r==1 (mod u0)`, so `u0|c+1`.
- If `8m+1=ct`, then `t==-1 (mod u0)` and `t==3 (mod 8)`.
- Thus `c=u0 a-1`, `t=u0 b-1` with positive `a,b>=4`.
- Expansion gives `ab u0-(a+b)=8w0`.

The lower bound in v10 is `16u0-8>8u0`. This needs `u0>1`. If `u0=1`, then `m=1`, hence `s=3`, excluded by `s>3`. Therefore `u0>=3` and the strict inequality is valid.

Verdict: correct, with the excluded `u0=1` edge case now explicitly documented.

### B2. `s == 7 (mod 8)`

Here `d=(s-1)/2` is odd, `r==2d-1 (mod 4d)`, and exceptional `c==3 (mod 4)`.

- `u=src(d)|B` and `4B=cr+1==1-c (mod u)` give `u|c-1`.
- If `4d+1=ct`, then `t==1 (mod u)`.
- Since `ct==1 (mod 4)` and `c==3 (mod 4)`, `t==3 (mod 4)`.
- Thus `c=ua+1`, `t=ub+1`; positivity and the mod-4 conditions give `a,b>=2`.
- Expansion gives `ab u+(a+b)=4w`.
- LHS `>=4u+4`, RHS `<=4u`.

No small-value exception survives. (`u=1` would imply `d=1` and hence `s=3`, outside this case.)

Verdict: correct.

### B3. `s == 5 (mod 8)`

Here `d=s-1=4m`, `m` odd, `r==d-1 (mod 4d)`, exceptional `c==1 (mod 4)`.

`c=1`:

- `r+1=d(1+4n)` for some integer `n`.
- `B=(r+1)/4=m(1+4n)` is odd.
- `v2(d)=2`, hence `d` cannot divide `B^2`.

For `c>1`:

- the odd square-root closure gives `u0|c-1`;
- if `16m+1=ct`, also `u0|t-1`;
- `c,t==1 (mod 4)`;
- therefore `c=u0a+1`, `t=u0b+1` with `a,b>=4` (including the edge case `u0=1`);
- expansion gives `ab u0+(a+b)=16w0`;
- LHS `>=16u0+8`, RHS `<=16u0`.

Verdict: correct.

### B4. `s == 1 (mod 8)`

Let `e=v2(s-1)>=3`, `s-1=2^e m`, `m` odd, and

`d=2^(e-3)(s-1)=2^(2e-3)m`.

Then `src(d)=2^(e-1)u0`, where `u0=src(m)`.

- `d|B^2` implies `2^(e-1)u0|B`, hence `2^(e+1)u0|cr+1`.
- The parameter class gives `r==-1 (mod u0)` and `r==2^e-1 (mod 2^(e+1))`.
- Therefore `u0|c-1` and `c==2^e+1 (mod 2^(e+1))`.
- If `4d+1=ct`, then `t` has the same two congruences.
- Writing `c=u0a+1`, `t=u0b+1`, the 2-adic congruence gives `a==2^e (mod 2^(e+1))` after multiplication by the odd inverse of `u0`; hence positive `a,b>=2^e`.
- Expansion gives `ab u0+(a+b)=2^(2e-1)w0`.
- LHS `>=2^(2e)u0+2^(e+1)`, RHS `<=2^(2e-1)u0`.

The same congruence excludes `c=1` immediately.

Verdict: correct.

---

## C. Master-equation finiteness after no-reuse

Once `k=0` is excluded, `k>=1`; independently `h>=1`. The equality configuration `kh=dc^2` is separately excluded by the canonical congruence data. Therefore

`1 <= kh < dc^2`.

This bounds both positive integers `k,h` by `dc^2-1`, so there are finitely many pairs. Each pair determines at most one rational

`r=(k+dh-2dc)/(dc^2-kh)`.

Thus each fixed exceptional cofactor `c` contributes finitely many bad prime parameters, and there are finitely many `c<s`.

Verdict: correct.

---

## D. Audit conclusion

No new mathematical gap was found in the two proof blocks inlined into v10.

One editorial improvement is recommended before final arXiv freeze: explicitly mention in the `s==3 (mod 8)` no-reuse case that `u0=1` would force `s=3`, excluded by the theorem. This makes the strict inequality `16u0-8>8u0` visibly airtight to a referee.

External correctness and historical-priority review remain outstanding and are not replaced by this internal audit.