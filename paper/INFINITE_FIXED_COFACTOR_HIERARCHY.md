# Infinite Fixed-Cofactor Exact-Depth Hierarchy

**Status:** unconditional theorem. No novelty claim pending dedicated literature comparison.

This note upgrades the finite `7r,11r,19r,...` examples to an infinite hierarchy of fixed-cofactor exact square-completed Type-II depth families.

## 1. Setup

Let `s>3` be a fixed prime satisfying

\[
\boxed{s\equiv3\pmod8.}
\]

Define

\[
d=\frac{s+1}{2}
\]

and take the variable prime parameter `r` in the progression

\[
\boxed{
r\equiv s+2\pmod{2(s+1)}.
}
\]

Because `s+2` is coprime to `2(s+1)`, Dirichlet's theorem gives infinitely many primes in this progression.

Put

\[
A=\frac{sr+1}{4}.
\]

Since `r\equiv s+2 (mod 2(s+1))`,

\[
sr+1\equiv s(s+2)+1=(s+1)^2\equiv0\pmod{2(s+1)}.
\]

Hence

\[
\boxed{d\mid A,}
\]

so `d|A^2` is a valid square-completion witness.

The target modulus is

\[
m_A=sr
\]

and the target progression is

\[
\boxed{
n\equiv-4d=-2(s+1)\pmod{sr}.}
\]

## 2. Exactly one nonsquare coordinate

Modulo the fixed prime `s`,

\[
-2(s+1)\equiv-2\pmod s.
\]

For `s\equiv3 (mod 8)`, the standard supplementary laws give

\[
\left(\frac{-2}{s}\right)=+1.
\]

Thus the target residue is a quadratic residue modulo `s`.

Now write

\[
d=2m,
\qquad
m=\frac{s+1}{4}.
\]

Because `s\equiv3 (mod 8)`, `m` is odd. The parameter progression gives

\[
r\equiv s+2\equiv5\pmod8
\]

and also

\[
r\equiv1\pmod{s+1}.
\]

Therefore for every odd prime `q|m`,

\[
r\equiv1\pmod q.
\]

Since `r\equiv1 (mod 4)`, quadratic reciprocity gives

\[
\left(\frac q r\right)
=
\left(\frac r q\right)
=1.
\]

Hence

\[
\left(\frac m r\right)=1.
\]

But `r\equiv5 (mod 8)`, so

\[
\left(\frac2r\right)=-1,
\qquad
\left(\frac{-1}{r}\right)=1.
\]

Consequently

\[
\boxed{
\left(\frac{-d}{r}\right)=-1.
}
\]

Since multiplication by `4` does not change quadratic character,

\[
\boxed{
\left(\frac{-4d}{r}\right)=-1.
}
\]

Thus the target has exactly one nonsquare prime coordinate: the variable prime `r`.

By the single-nonsquare-coordinate reduction theorem, every earlier layer whose modulus is not divisible by `r` can be excluded simultaneously by choosing square-safe CRT coordinates.

## 3. Exceptional layers are finite

Exclude the finitely many parameter primes `r<=s`; this does not affect infinitude. Then every earlier modulus divisible by `r` has the form

\[
m_B=cr
\]

with

\[
0<c<s,
\qquad
c\equiv3\pmod4.
\]

For each such fixed `c`, put

\[
B=\frac{cr+1}{4}.
\]

The fixed-cofactor exceptional-layer lemma shows that any collision produces integers `k,h>=0` satisfying

\[
\boxed{
r(kh-dc^2)+k+dh-2dc=0}
\]

and

\[
\boxed{16d\mid rh+1.}
\]

The equality case `kh=dc^2` would require `4d|B`, equivalently

\[
8(s+1)\mid cr+1.
\]

But modulo `s+1` we have `r\equiv1`, so this would imply

\[
c+1\equiv0\pmod{s+1},
\]

impossible because `0<c<s`. Hence every collision satisfies the strict bound

\[
\boxed{kh<dc^2.}
\]

For fixed `s` and `c`, there are only finitely many positive pairs `(k,h)` in this range. For each pair, the collision equation determines at most one rational value

\[
r=\frac{k+dh-2dc}{dc^2-kh}.
\]

Therefore each exceptional cofactor `c` produces only finitely many possible integer, hence prime, collision parameters `r`.

There are only finitely many cofactors `c<s`. Their union is therefore a finite exceptional set

\[
\mathcal E_s.
\]

## 4. Infinite hierarchy theorem

Remove the finite set `\mathcal E_s` together with the finitely many primes `r<=s`. Dirichlet's theorem still leaves infinitely many primes

\[
r\equiv s+2\pmod{2(s+1)}.
\]

For every remaining prime `r`, the target progression

\[
n\equiv-2(s+1)\pmod{sr}
\]

can be refined by CRT to avoid every earlier square-completed Type-II trap. The refined progression is reduced, so Dirichlet supplies infinitely many primes `p` in it. For each such prime,

\[
\boxed{
\delta_{\rm sq}(p)=\frac{sr+1}{4}.
}
\]

Hence:

> **Infinite fixed-cofactor hierarchy theorem.**
> For every fixed prime `s>3` with `s\equiv3 (mod 8)`, all but finitely many primes
> \[
> r\equiv s+2\pmod{2(s+1)}
> \]
> generate a depth
> \[
> \boxed{A=(sr+1)/4}
> \]
> that occurs infinitely often as an exact square-completed Type-II depth.

This produces infinitely many distinct post-Jacobi fixed cofactors `s`.

## 5. Counting consequence

For each fixed admissible `s`, removing finitely many parameter primes does not alter the asymptotic count. The `s`-family contributes

\[
\pi\!\left(\frac{4X}{s};\,2(s+1),\,s+2\right)
\sim
\boxed{
\frac{4}{s\varphi(2(s+1))}\frac{X}{\log X}.
}
\]

For any finite set `S` of primes `s\equiv3 (mod 8)`, `s>3`, the corresponding target semiprime moduli are asymptotically disjoint, so their contributions add.

Because

\[
\frac{4}{s\varphi(2(s+1))}
\ll
\frac{\log\log s}{s^2},
\]

the positive series

\[
\boxed{
C_{3(8)}=
\sum_{\substack{s>3\ {m prime}\\ s\equiv3\ (8)}}
\frac{4}{s\varphi(2(s+1))}
}
\]

converges. Taking larger and larger finite sets gives the rigorous lower-bound contribution `C_{3(8)}` from this hierarchy.

A direct partial sum over admissible primes `s<=100000` already exceeds

\[
\boxed{0.0676803.}
\]

Combining this partial sum with the previously proved prime/`3q` coefficient `8/3` and the separate `7r`, `23r`, `31r`, and `47r` families gives the explicit numerical lower bound

\[
\boxed{
N_\infty(X)
\ge
\left(2.8876843+o(1)\right)\frac{X}{\log X}.
}
\]

The full convergent hierarchy gives a slightly larger coefficient.

## Claim boundary

This theorem concerns exact **square-completed Type-II depth**. It does not prove universal Type-II solvability and does not prove the Erdős--Straus conjecture. The fixed-cofactor hierarchy should receive a dedicated prior-art audit before novelty or priority is claimed.
