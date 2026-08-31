# An Infinite `19r` Exact-Depth Backbone

**Status:** unconditional theorem, with a finite bounded Diophantine check. No novelty claim pending dedicated literature comparison.

Let

\[
r\equiv21\pmod{40}
\]

be prime, and define

\[
A=\frac{19r+1}{4},\qquad d=10.
\]

Because `19r+1\equiv0 (mod 40)`, we have `10|A`, hence

\[
d=10\mid A^2.
\]

The target modulus is

\[
m_A=4A-1=19r,
\]

and the target Type-II square-completion progression is

\[
n\equiv-40\pmod{19r}.
\]

We prove that this progression contains a reduced arithmetic subprogression avoiding every earlier square-completed Type-II layer. Dirichlet's theorem then gives infinitely many primes of exact square depth `A`.

## 1. One nonsquare coordinate

Modulo `19`,

\[
-40\equiv17.
\]

The quadratic residues modulo `19` are

\[
1,4,9,16,6,17,11,7,5,
\]

so `17` is a square modulo `19`.

For the variable prime `r`, since `r\equiv21 (mod 40)` we have `r\equiv5 (mod 8)` and `r\equiv1 (mod 5)`. Quadratic reciprocity gives

\[
\left(\frac{-40}{r}\right)
=
\left(\frac{-10}{r}\right)
=-1.
\]

Thus the target residue has exactly one nonsquare target coordinate: the prime `r`.

By the single-nonsquare-coordinate reduction theorem, choose square residues on every prime-power coordinate not involving `r` while preserving the target residue modulo `19`. Then every earlier layer whose modulus is not divisible by `r` is automatically avoided by the universal square-safe lemma.

Hence only earlier moduli divisible by `r` need inspection.

## 2. Exceptional cofactors

An earlier modulus divisible by `r` has the form

\[
m_B=cr=4B-1
\]

with `c<19` and `c\equiv3 (mod 4)`. Therefore

\[
\boxed{c\in\{3,7,11,15\}.}
\]

For each such `c`, let

\[
B=\frac{cr+1}{4}.
\]

The fixed-cofactor exceptional-layer lemma says that a collision produces integers `k,h>=0` satisfying

\[
\boxed{
r(kh-10c^2)+k+10h-20c=0
}
\]

and

\[
\boxed{160\mid rh+1.}
\]

The equality case `kh=10c^2` would require `40|B`, equivalently

\[
160\mid cr+1.
\]

This is impossible for `r\equiv21 (mod 40)` and each `c=3,7,11,15`. Hence every collision satisfies

\[
\boxed{kh<10c^2.}
\]

The search region is therefore finite and depends only on `c`.

## 3. Finite exceptional-layer check

For `kh<10c^2`, solve

\[
r=\frac{k+10h-20c}{10c^2-kh}
\]

subject to

\[
r>1,\qquad r\equiv21\pmod{40},\qquad 160\mid rh+1.
\]

The exhaustive bounded check is:

- `c=3`: no integer candidate;
- `c=7`: no integer candidate;
- `c=11`: the equation plus `r\equiv21 (mod 40)` leaves only `r=21` and `r=61`; `r=21` is composite, while the `r=61` solutions fail `160|rh+1`;
- `c=15`: no integer candidate.

Therefore none of the four exceptional earlier layers can intersect the chosen target progression.

The accompanying script `verify_19r_backbone_exceptional_layers.py` checks this finite table directly from the displayed equations.

## 4. Exact-depth theorem

We have constructed a reduced arithmetic progression satisfying

\[
n\equiv-40\pmod{19r}
\]

and avoiding every earlier square-completed Type-II trap. By Dirichlet's theorem, that progression contains infinitely many primes `p`. For each such prime, `(A,d)=( (19r+1)/4,10 )` is a valid square-completed Type-II certificate, while no smaller depth is valid. Thus

\[
\boxed{
\delta_{\rm sq}(p)=\frac{19r+1}{4}
}
\]

for infinitely many primes `p`.

Hence:

> **Theorem.** For every prime `r\equiv21 (mod 40)`, the depth
> \[
> \boxed{A=(19r+1)/4}
> \]
> occurs infinitely often as an exact square-completed Type-II depth.

## 5. Counting consequence

The primes `r\equiv21 (mod 40)` have relative density `1/\varphi(40)=1/16` among the primes. Since `A\sim19r/4`, the number of depths from this family with `A<=X` is

\[
\pi\!\left(\frac{4X}{19};40,21\right)
\sim
\frac1{16}\frac{4X/19}{\log X}
=
\boxed{\frac1{76}\frac{X}{\log X}}.
\]

This family is disjoint from the prime-modulus and `3q`, `7r`, and `11r` backbones at the level of target modulus factorization.

## Claim boundary

This proves an infinite exact square-depth family. It does not prove universal Type-II solvability and does not prove the Erdős--Straus conjecture. The quadratic-coordinate mechanism and the finite exceptional-layer reduction should be compared carefully with contemporary square-lift and reciprocity literature before novelty is asserted.
