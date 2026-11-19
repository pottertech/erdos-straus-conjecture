# Canonical Exact-Depth Hierarchy for Every Fixed Prime Cofactor

**Status:** unconditional theorem. This unifies and extends the previously proved `s≡3 (mod 8)` and `s≡7 (mod 8)` hierarchies to **every fixed prime `s>3`**. It concerns exact square-completed Type-II depth and does not prove the Erdős--Straus conjecture.

Let `s>3` be a fixed prime. We give a canonical witness `d_s` and a reduced arithmetic progression of variable primes `r` such that, after deleting only finitely many exceptional parameters, the depth

\[
A=\frac{sr+1}{4}
\]

is realized as exact square-completed Type-II depth by infinitely many primes.

The four residue classes of `s mod 8` are treated as follows.

---

## 1. `s ≡ 3 (mod 8)`

Take

\[
d=\frac{s+1}{2},
\qquad
r\equiv s+2\pmod{2(s+1)}.
\]

This is the previously proved canonical `3 mod 8` hierarchy. The target is square modulo `s`, nonsquare modulo `r`, and the AM--GM equality configuration is impossible throughout the parameter progression.

---

## 2. `s ≡ 7 (mod 8)`

Take

\[
d=\frac{s-1}{2},
\qquad
r\equiv s-2\pmod{2(s-1)}.
\]

This is the previously proved canonical `7 mod 8` hierarchy. Again the target is square modulo `s`, nonsquare modulo `r`, and equality is impossible throughout the parameter progression.

---

## 3. `s ≡ 1 (mod 8)`

Set

\[
\boxed{d=\frac{s-1}{2}}
\]

and choose primes

\[
\boxed{r\equiv s-2\pmod{2(s-1)}.}
\]

Write `s=2d+1`. The parameter class is

\[
r\equiv2d-1\pmod{4d}.
\]

Hence

\[
sr+1\equiv(2d+1)(2d-1)+1=4d^2\equiv0\pmod{4d},
\]

so

\[
\boxed{d\mid A.}
\]

Modulo the fixed prime `s`,

\[
-d\equiv\frac12\pmod s.
\]

Because `s≡1 (mod 8)`,

\[
\left(\frac2s\right)=+1,
\]

therefore

\[
\boxed{\left(\frac{-d}{s}\right)=+1.}
\]

Now `d=(s-1)/2` is divisible by `4`, and the parameter class gives

\[
r\equiv-1\pmod d,
\qquad
r\equiv7\pmod8.
\]

For every odd prime `q|d`, quadratic reciprocity gives

\[
\left(\frac qr\right)
=
\left(\frac rq\right)(-1)^{(q-1)/2}
=
\left(\frac{-1}{q}\right)(-1)^{(q-1)/2}
=+1.
\]

Also `(2/r)=+1` because `r≡7 (mod 8)`. Hence

\[
\left(\frac dr\right)=+1.
\]

Since `r≡3 (mod 4)`,

\[
\left(\frac{-1}{r}\right)=-1,
\]

so

\[
\boxed{\left(\frac{-d}{r}\right)=-1.}
\]

Thus `r` is the unique nonsquare target coordinate.

An earlier modulus containing `r` has the form

\[
cr=4B-1,
\qquad
0<c<s.
\]

Since `r≡3 (mod 4)`, necessarily

\[
c\equiv1\pmod4.
\]

The AM--GM equality configuration would require

\[
16d=8(s-1)\mid cr+1.
\]

Modulo `s-1`, the parameter class gives `r≡-1`, hence equality forces

\[
c\equiv1\pmod{s-1}.
\]

With `0<c<s`, this forces `c=1`. But for `c=1`,

\[
r+1\equiv s-1\pmod{2(s-1)},
\]

so `2(s-1)∤r+1`, a fortiori `8(s-1)∤r+1`. Thus equality is impossible on the full progression.

The fixed-cofactor finite-exception theorem therefore applies.

---

## 4. `s ≡ 5 (mod 8)`

Set

\[
\boxed{d=s-1}
\]

and choose primes

\[
\boxed{r\equiv s-2\pmod{4(s-1)}.}
\]

Writing `s=d+1`, the parameter class is `r≡d-1 (mod 4d)`. Since `s≡5 (mod 8)`, `d≡4 (mod 8)` and hence `4d|d^2`. Therefore

\[
sr+1\equiv(d+1)(d-1)+1=d^2\equiv0\pmod{4d},
\]

so

\[
\boxed{d\mid A.}
\]

Modulo `s`,

\[
-d=-(s-1)\equiv1\pmod s,
\]

therefore

\[
\boxed{\left(\frac{-d}{s}\right)=+1.}
\]

The parameter class gives

\[
r\equiv-1\pmod d,
\qquad
r\equiv3\pmod8.
\]

Here `v_2(d)=2`. For every odd prime divisor `q|d`, the same reciprocity calculation as above gives `(q/r)=+1`; the factor `2^2` is a square. Hence

\[
\left(\frac dr\right)=+1.
\]

Since `r≡3 (mod 4)`, `(-1/r)=-1`, and therefore

\[
\boxed{\left(\frac{-d}{r}\right)=-1.}
\]

Again `r` is the unique nonsquare target coordinate.

Every exceptional earlier cofactor satisfies `c≡1 (mod 4)`. Equality would require

\[
16(s-1)\mid cr+1.
\]

Modulo `s-1`, `r≡-1`, so equality forces `c=1`. But for `c=1`,

\[
r+1\equiv s-1\pmod{4(s-1)},
\]

so `4(s-1)∤r+1`, and equality is impossible.

The fixed-cofactor finite-exception theorem applies.

---

## 5. Unified theorem

Combining the four cases gives:

> **Every-prime fixed-cofactor hierarchy theorem.** For every fixed prime
> \[
> \boxed{s>3,}
> \]
> there is an explicit reduced arithmetic progression of primes `r` and an explicit divisor witness `d_s` such that all but finitely many prime parameters in that progression generate
> \[
> \boxed{A=(sr+1)/4}
> \]
> as an exact square-completed Type-II depth realized by infinitely many primes.

A convenient table is

| `s mod 8` | witness `d_s` | canonical prime progression for `r` |
|---|---:|---|
| `1` | `(s-1)/2` | `r ≡ s-2 (mod 2(s-1))` |
| `3` | `(s+1)/2` | `r ≡ s+2 (mod 2(s+1))` |
| `5` | `s-1` | `r ≡ s-2 (mod 4(s-1))` |
| `7` | `(s-1)/2` | `r ≡ s-2 (mod 2(s-1))` |

Thus the post-Jacobi hierarchy is indexed not merely by infinitely many fixed cofactors but by **every fixed prime cofactor `s>3`**.

## 6. Counting series

For a fixed cofactor, the corresponding asymptotic contribution is

\[
c(s)\frac{X}{\log X},
\]

where

\[
c(s)=
\begin{cases}
\dfrac{4}{s\varphi(2(s-1))},&s\equiv1\pmod8,\\[6pt]
\dfrac{4}{s\varphi(2(s+1))},&s\equiv3\pmod8,\\[6pt]
\dfrac{4}{s\varphi(4(s-1))},&s\equiv5\pmod8,\\[6pt]
\dfrac{4}{s\varphi(2(s-1))},&s\equiv7\pmod8.
\end{cases}
\]

The positive series

\[
\boxed{
C_{\rm all}=\sum_{\substack{s>3\\s\ \mathrm{prime}}}c(s)
}
\]

converges. For every finite set of cofactors the corresponding target semiprime families are asymptotically disjoint up to finitely many swapped-prime coincidences; taking `X→∞` first and then the supremum over finite sets gives

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge\frac83+C_{\rm all}.
}
\]

A finite certificate using only prime cofactors `s<=10^6` gives

\[
\sum_{\substack{5\le s\le10^6\\s\ \mathrm{prime}}}c(s)
=
\boxed{0.3838383630433429\ldots},
\]

and hence the explicit rigorous lower bound

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge3.0505050297100094\ldots .
}
\]

All omitted terms are positive, so the full canonical hierarchy gives a strictly larger coefficient.

## Claim boundary

This theorem concerns exact square-completed Type-II depth. It does not prove universal Type-II solvability, does not prove that every prime has a Type-II solution, and does not prove the Erdős--Straus conjecture. The fixed-cofactor hierarchy and finite-exception mechanism require a dedicated literature audit before novelty or priority is claimed.