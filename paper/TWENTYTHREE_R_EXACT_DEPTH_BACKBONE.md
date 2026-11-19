# An Infinite `23r` Exact-Depth Backbone

**Status:** unconditional theorem with a finite bounded Diophantine check. No novelty claim pending dedicated literature comparison.

Let

\[
r\equiv73\pmod{80}
\]

be prime, and put

\[
A=\frac{23r+1}{4},\qquad d=20.
\]

Since `23*73+1` is divisible by `80`, every such `r` satisfies

\[
20\mid A,
\]

so `d=20|A^2`. The target modulus is

\[
m_A=23r,
\]

and the target square-completed Type-II progression is

\[
n\equiv-80\pmod{23r}.
\]

## 1. One nonsquare coordinate

Modulo `23`,

\[
-80\equiv12,
\]

and `12` is a quadratic residue modulo `23`.

Modulo the variable prime `r`, the factor `16` is a square, so

\[
\left(\frac{-80}{r}\right)
=
\left(\frac{-5}{r}\right).
\]

For `r\equiv73 (mod 80)`, we have `r\equiv1 (mod 8)` and `r\equiv3 (mod 5)`. Hence

\[
\left(\frac{-1}{r}\right)=1,
\qquad
\left(\frac{5}{r}\right)=\left(\frac{r}{5}\right)=\left(\frac35\right)=-1,
\]

so

\[
\boxed{\left(\frac{-80}{r}\right)=-1.}
\]

Thus the target has exactly one nonsquare coordinate, namely `r`. By the single-nonsquare-coordinate reduction theorem, all earlier moduli not divisible by `r` can be avoided simultaneously by square-safe CRT coordinates.

## 2. Exceptional cofactors

The only earlier moduli divisible by `r` are

\[
cr,
\qquad
c\in\{3,7,11,15,19\},
\]

because `c<23` and `c\equiv3 (mod 4)`.

For an exceptional cofactor `c`, the fixed-cofactor lemma gives the necessary collision equation

\[
\boxed{
r(kh-20c^2)+k+20h-40c=0
}
\]

with

\[
\boxed{320\mid rh+1.}
\]

The equality case `kh=20c^2` would require `80|B`, equivalently `320|cr+1`. This is incompatible with `r\equiv73 (mod 80)` for every `c=3,7,11,15,19`. Therefore

\[
\boxed{kh<20c^2.}
\]

and every exceptional layer reduces to a finite calculation.

## 3. Finite calculation

Solving

\[
r=\frac{k+20h-40c}{20c^2-kh}
\]

for positive integers `k,h` with `kh<20c^2` and `r\equiv73 (mod 80)` gives:

- `c=3`: no integer candidate;
- `c=7`: no integer candidate;
- `c=11`: no integer candidate;
- `c=15`: the only candidate is `r=153`, which is composite;
- `c=19`: the only candidate is `r=233`, but its associated solution satisfies `rh+1\equiv160 (mod 320)`, so the necessary condition `320|rh+1` fails.

Hence no exceptional earlier layer can collide with the target progression.

## 4. Exact-depth theorem

We therefore obtain a reduced arithmetic progression satisfying

\[
n\equiv-80\pmod{23r}
\]

and avoiding every earlier square-completed Type-II trap. Dirichlet's theorem supplies infinitely many primes in this progression. For each such prime `p`, the target pair `(A,d)` is valid and no smaller depth is valid. Thus

\[
\boxed{
\delta_{\rm sq}(p)=\frac{23r+1}{4}
}
\]

for infinitely many primes `p`.

> **Theorem.** For every prime `r\equiv73 (mod 80)`, the depth
> \[
> \boxed{A=(23r+1)/4}
> \]
> occurs infinitely often as an exact square-completed Type-II depth.

## 5. Counting contribution

The prime progression `r\equiv73 (mod 80)` has density `1/\varphi(80)=1/32`. Since `A\sim23r/4`, the number of depths from this family up to `X` is

\[
\pi\!\left(\frac{4X}{23};80,73\right)
\sim
\boxed{\frac1{184}\frac{X}{\log X}}.
\]

## Claim boundary

This is an exact square-depth theorem, not a proof of universal Type-II solvability or of the Erdős--Straus conjecture. The local quadratic-residue mechanism and fixed-cofactor reduction should be compared carefully against current square-lift and reciprocity literature before novelty is asserted.
