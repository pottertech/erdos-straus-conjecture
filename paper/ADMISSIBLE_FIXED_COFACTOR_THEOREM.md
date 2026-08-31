# Admissible Fixed-Cofactor Exact-Depth Theorem

**Status:** unconditional theorem schema. This unifies the previously proved fixed-cofactor families. It concerns exact square-completed Type-II depth, not the full Erdős--Straus conjecture. Novelty/priority remains subject to literature review.

## 1. Equality-free admissible parameter progression

Let `s>1` be a fixed odd integer with

\[
s\equiv3\pmod4,
\]

and let `d>=1` satisfy

\[
\gcd(s,4d)=1.
\]

Choose a reduced residue class `alpha (mod 16d)` satisfying

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

3. for every integer `c` with
\[
0<c<s,\qquad c\equiv3\pmod4,
\]
the AM--GM equality configuration is excluded on the parameter progression:
\[
\boxed{c\alpha+1\not\equiv0\pmod{16d}.}
\]

Call `(s,d,alpha)` an **equality-free admissible triple**.

For a prime parameter
\[
r\equiv\alpha\pmod{16d},
\]
put
\[
A=\frac{sr+1}{4}.
\]
Because `alpha==-s^{-1} (mod 4d)`,
\[
\boxed{d\mid A,}
\]
so `d|A^2`. The target square-completion residue is
\[
\boxed{n\equiv-4d\pmod{sr}.}
\]
It is square at each fixed prime coordinate dividing `s` and nonsquare at the single variable coordinate `r`.

## 2. Reduction to the `r`-bearing earlier layers

Choose square-safe CRT coordinates at all prime powers not involving `r`, preserving the prescribed target residues on the fixed factors of `s`. The universal square-safe lemma then eliminates every earlier layer whose modulus is not divisible by `r`.

After discarding the finitely many parameters `r<=s`, every earlier modulus containing `r` has the form
\[
4B-1=cr,
\]
with
\[
0<c<s,\qquad c\equiv3\pmod4.
\]
Thus only finitely many fixed cofactors `c` need inspection.

## 3. Master exceptional-layer equation

Fix such a `c` and put
\[
B=\frac{cr+1}{4}.
\]
A collision gives a divisor `E|B^2` satisfying `E==d (mod r)`, so write
\[
E=rk+d.
\]
With
\[
F=B^2/E,
\]
the complementary congruence has the form
\[
16dF=rh+1.
\]
Multiplying gives
\[
(rk+d)(rh+1)=d(cr+1)^2,
\]
and hence
\[
\boxed{r(kh-dc^2)+k+dh-2dc=0.}
\]

If `kh>dc^2`, AM--GM gives
\[
k+dh>2dc,
\]
contradicting the displayed equation. If `kh=dc^2`, equality in AM--GM forces
\[
k=dc,\qquad h=c,
\]
and hence
\[
16d\mid cr+1.
\]
But `r==alpha (mod 16d)` and hypothesis 3 says
\[
c\alpha+1\not\equiv0\pmod{16d},
\]
so the equality case is impossible throughout the chosen prime progression.

Therefore every collision satisfies
\[
\boxed{kh<dc^2.}
\]
For fixed `(s,d,c)` only finitely many nonnegative pairs `(k,h)` satisfy this bound, and each determines at most one rational value
\[
\boxed{r=\frac{k+dh-2dc}{dc^2-kh}.}
\]
Thus each `c` contributes only finitely many collision primes `r`; the union over all `c<s` is finite.

## 4. The theorem

Dirichlet gives infinitely many primes
\[
r\equiv\alpha\pmod{16d}
\]
because `alpha` is reduced. Removing the finite collision set still leaves infinitely many parameter primes. For every remaining `r`, CRT gives a reduced progression satisfying the target congruence at depth `A` and avoiding all earlier square-completed Type-II traps. A second application of Dirichlet therefore gives infinitely many primes `p` with
\[
\boxed{\delta_{\rm sq}(p)=\frac{sr+1}{4}.}
\]

> **Equality-free admissible fixed-cofactor theorem.** For every equality-free admissible triple `(s,d,alpha)`, all but finitely many primes `r==alpha (mod 16d)` generate a depth `A=(sr+1)/4` that occurs infinitely often as an exact square-completed Type-II depth.

## 5. Counting consequence

A fixed equality-free admissible triple contributes
\[
\boxed{\frac{4}{s\varphi(16d)}\frac{X}{\log X}}
\]
exact depths up to `X` when one works with the single class `alpha (mod 16d)`.

If the equality obstruction is known to be impossible on a coarser reduced class modulo `4d` (as in the canonical `s==3 (mod 8)` hierarchy and several explicit small families), one may retain that coarser progression and obtain the larger contribution
\[
\boxed{\frac{4}{s\varphi(4d)}\frac{X}{\log X}.}
\]

For any fixed finite collection of families with distinct target factorizations, the contributions add after discarding the finitely many swapped-prime coincidences.

## 6. Relation to the proved families

The explicit branch notes verify the stronger coarse-progression condition directly for their stated residue classes. In particular, the canonical prime-cofactor hierarchy
\[
s\equiv3\pmod8,\qquad d=(s+1)/2,
\]
has an equality obstruction that is impossible for every parameter in the original class, so its previously stated coefficient
\[
\frac{4}{s\varphi(2(s+1))}
\]
remains unchanged.

## Claim boundary

The local quadratic-coordinate mechanism has close antecedents in contemporary reciprocity/square-lift work. The candidate contribution is the fixed-cofactor exact-first-hit finite-exception theorem and its use to generate infinite exact-depth backbones. Do not claim novelty or priority without a dedicated literature audit.