# Admissible Fixed-Cofactor Exact-Depth Theorem

**Status:** unconditional theorem schema. This unifies the proved fixed-prime-cofactor families. It concerns exact square-completed Type-II depth, not the full Erdős--Straus conjecture. Novelty/priority remains subject to literature review.

## Theorem setup

Let `s>1` be a fixed **odd squarefree** integer with

\[
s\equiv3\pmod4,
\]

and let `d>=1` satisfy `gcd(s,4d)=1`. Choose a reduced residue class `alpha (mod 16d)` such that

\[
\boxed{\alpha\equiv-s^{-1}\pmod{4d}.}
\]

Assume:

1. for every prime `q|s`,
\[
\boxed{\left(\frac{-d}{q}\right)=+1;}
\]

2. for every prime `r==alpha (mod 16d)`, apart from at most finitely many excluded primes,
\[
\boxed{\left(\frac{-d}{r}\right)=-1;}
\]

3. for every `0<c<s` with `c==3 (mod 4)`, the AM--GM equality configuration is excluded:
\[
\boxed{c\alpha+1\not\equiv0\pmod{16d}.}
\]

Call `(s,d,alpha)` an **equality-free admissible triple**.

For a prime parameter `r==alpha (mod 16d)`, put
\[
A=\frac{sr+1}{4}.
\]
The first congruence gives `d|A`, hence `d|A^2`. The target residue is
\[
\boxed{n\equiv-4d\pmod{sr}.}
\]
Because `s` is squarefree, hypothesis 1 makes this residue a square on every fixed prime coordinate dividing `s`; hypothesis 2 makes it nonsquare at the single variable coordinate `r`.

## Single-nonsquare reduction

Choose square-safe CRT coordinates away from `r`, preserving the target residues on the fixed factors of `s`. The universal square-safe lemma excludes every earlier layer whose modulus is not divisible by `r`.

After discarding the finitely many parameters `r<=s`, an earlier modulus containing `r` has the form
\[
4B-1=cr,
\qquad 0<c<s,
\qquad c\equiv3\pmod4.
\]
Only finitely many fixed cofactors `c` remain.

## Master exceptional-layer equation

For such a `c`, put `B=(cr+1)/4`. A collision gives `E|B^2` with `E==d (mod r)`, so write
\[
E=rk+d.
\]
Writing `F=B^2/E`, the complementary congruence has the form
\[
16dF=rh+1.
\]
Multiplication gives
\[
(rk+d)(rh+1)=d(cr+1)^2,
\]
and hence
\[
\boxed{r(kh-dc^2)+k+dh-2dc=0.}
\]

If `kh>dc^2`, AM--GM gives `k+dh>2dc`, contradicting the equation. If `kh=dc^2`, equality forces `k=dc`, `h=c` and therefore `16d|cr+1`, which is excluded by hypothesis 3 on the entire chosen parameter progression. Thus every collision satisfies
\[
\boxed{kh<dc^2.}
\]
For fixed `(s,d,c)` only finitely many pairs `(k,h)` lie in this region, and each determines at most one rational parameter
\[
\boxed{r=\frac{k+dh-2dc}{dc^2-kh}.}
\]
Hence every `c` contributes only finitely many collision primes, and so does their finite union.

## Equality-free admissible fixed-cofactor theorem

Dirichlet gives infinitely many primes `r==alpha (mod 16d)`. Removing the finite collision set still leaves infinitely many. For every remaining parameter, CRT gives a reduced progression satisfying the target depth and avoiding all earlier square-completed Type-II traps; a second application of Dirichlet gives infinitely many primes `p` with
\[
\boxed{\delta_{\rm sq}(p)=\frac{sr+1}{4}.}
\]

Thus every equality-free admissible triple generates an infinite exact-depth family.

A single class modulo `16d` contributes
\[
\boxed{\frac{4}{s\varphi(16d)}\frac{X}{\log X}}
\]
depths up to `X`. If the equality obstruction is known to be impossible on the coarser class modulo `4d`, that coarser progression may be retained and the contribution becomes
\[
\boxed{\frac{4}{s\varphi(4d)}\frac{X}{\log X}.}
\]

## Relation to the headline hierarchy

All headline applications use **prime** `s`, so the squarefree restriction is automatic. In particular, for every prime `s==3 (mod 8)`, the canonical choice
\[
d=(s+1)/2
\]
has an equality obstruction that is impossible throughout the original class
\[
r\equiv s+2\pmod{2(s+1)},
\]
and the previously proved hierarchy and its coefficient are unchanged.

## Claim boundary

For nonsquarefree fixed cofactors one can formulate a broader version by requiring the target to be a unit square modulo each full prime-power factor of `s`; that extension is not needed here. The local quadratic-coordinate mechanism has close antecedents in contemporary reciprocity/square-lift work. The candidate contribution is the fixed-cofactor exact-first-hit finite-exception theorem and its use to generate infinite exact-depth backbones.