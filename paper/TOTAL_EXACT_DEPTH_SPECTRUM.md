# Total Exact-Depth Spectrum and Jacobi-Rank Saturation

**Status:** unconditional synthesis of the prime-target CRT backbone, the composite `3q` theorem, the Jacobi-rank classification, and the quantitative exceptional-set bound.

Let

\[
N_\infty(X)
=
\#\{A\le X:\text{infinitely many primes }p\text{ satisfy }\delta_{\rm sq}(p)=A\}.
\]

This counts both prime-target and composite-target exact square-completion depths.

## Lemma 1: every prime target depth is realized infinitely often

Suppose

\[
r=4A-1
\]

is prime. Then infinitely many primes `p == 1 (mod 4)` satisfy

\[
\boxed{\delta_{\rm sq}(p)=A.}
\]

### Proof

Let

\[
L=\operatorname{lcm}_{1\le B<A}(4B-1).
\]

Since every earlier modulus is strictly smaller than the prime `r`,

\[
\gcd(r,L)=1.
\]

Take the target divisor `D=1`, so the target residue is

\[
p\equiv-4\pmod r.
\]

The system

\[
p\equiv-4\pmod r,
\qquad
p\equiv1\pmod L,
\qquad
p\equiv1\pmod4
\]

is CRT-compatible. Residue `1` avoids every earlier divisor-square Type-II layer by the universal Jacobi/square-safe lemma. The progression is reduced: its residue is `1` at every prime dividing `L` and `4`, while it is nonzero modulo `r`.

Dirichlet's theorem therefore gives infinitely many prime members. Every such prime has the target witness `(A,1)` and no witness below depth `A`.

## Theorem 2: total spectrum lower bound

Let

\[
\mathcal V_X
=
\operatorname{span}_{\mathbf F_2}\{v_A:1\le A\le\lfloor X\rfloor\}
\]

be the Jacobi ancestry space, where `v_A` is the parity vector of `4A-1`.

Then

\[
\boxed{
N_\infty(X)
\ge
\dim\mathcal V_X
-
O\!\left(\frac{X}{(\log X)^{3/2}}\right).
}
\]

Since

\[
\dim\mathcal V_X
=
\pi(4\lfloor X\rfloor-1;4,3)
+
\pi\!\left(\frac{4\lfloor X\rfloor-1}{3};4,1\right),
\]

we obtain

\[
\boxed{
N_\infty(X)
\ge
\pi(4X-1;4,3)
+
\pi\!\left(\frac{4X-1}{3};4,1\right)
-
O\!\left(\frac{X}{(\log X)^{3/2}}\right),
}
\]

with the harmless floor conventions understood.

Consequently,

\[
\boxed{
N_\infty(X)
\ge
\left(\frac83+o(1)\right)
\frac{X}{\log X}.
}
\]

### Proof

The Jacobi first-occurrence theorem says every new character direction is exactly one of two kinds.

### Prime new directions

These are the depths with

\[
4A-1=r\equiv3\pmod4
\]

prime. By Lemma 1, **every** such depth is realized by infinitely many primes.

Their exact count through depth `X` is

\[
\pi(4X-1;4,3).
\]

### Composite new directions

These are exactly

\[
A_q=\frac{3q+1}{4},
\qquad q\equiv1\pmod4\text{ prime}.
\]

The structural composite theorem realizes every such depth for which `A_q` has a prime divisor `ell == 2 (mod 3)`. The exceptional parameters satisfy

\[
E(Y)
\ll
\frac{Y}{(\log Y)^{3/2}},
\qquad
Y=\frac{4X-1}{3}.
\]

Therefore at least

\[
\pi(Y;4,1)
-
O\!\left(\frac{X}{(\log X)^{3/2}}\right)
\]

of the composite new directions are exact-depth realized.

Adding the two disjoint classes gives the theorem.

The prime number theorem in arithmetic progressions gives

\[
\pi(4X;4,3)
\sim
2\frac{X}{\log X},
\]

and

\[
\pi(4X/3;4,1)
\sim
\frac23\frac{X}{\log X}.
\]

Their sum is

\[
\frac83\frac{X}{\log X}.
\]

## Corollary 3: global reciprocity saturation

Let

\[
J(X)
=
\#\{A\le X:v_A\notin\operatorname{span}(v_1,\ldots,v_{A-1})\}.
\]

Then

\[
J(X)=\dim\mathcal V_X
\sim\frac83\frac{X}{\log X}.
\]

Let `R_new(X)` count Jacobi-new depths that are proved to be exact-depth realized by the prime and composite backbone constructions. Then

\[
\boxed{
J(X)-R_{\rm new}(X)
\ll
\frac{X}{(\log X)^{3/2}}.
}
\]

Hence

\[
\boxed{
1-O((\log X)^{-1/2})
\le
\frac{R_{\rm new}(X)}{J(X)}
\le1.
}
\]

So asymptotically **every genuinely new Jacobi-character direction in the layer sequence is realized as an exact Type-II square-completion depth by infinitely many primes**.

## Interpretation

The two basis-generating classes are not merely algebraic artifacts:

- the prime-target directions are all exact-depth realized;
- the composite `3q` directions are exact-depth realized with relative proportion tending to `1` at the quantitative rate `O((log X)^(-1/2))`.

Thus the algebraic first-occurrence spectrum and the provable exact-depth spectrum agree asymptotically on the entire Jacobi-new backbone.

This does not say that Jacobi-dependent depths fail to occur. The certified layers `649` and `22339` show the opposite: finer branch-dependent CRT/CSP mechanisms can realize depths that add no new Jacobi character.

## Claim boundary

The prime target construction is elementary CRT plus Dirichlet and is closely aligned with existing prime-backbone work in the contemporary literature. The candidate contribution is the combined quantitative relation between the total exact-depth spectrum and the exact Jacobi-rank formula.

The result does not prove universal Type-II solvability or the Erdős--Straus conjecture.