# Global Count of Infinite Exact-Depth Prime Families

**Status:** unconditional quantitative corollary of the composite `3q` backbone and the first-moment distribution of witness primes.

For every prime

\[
q\equiv1\pmod4,
\qquad
A_q=\frac{3q+1}{4},
\]

define

\[
\nu_-(A_q)
=
\#\{\ell\mid A_q:\ell\text{ prime},\ \ell\equiv2\pmod3\}.
\]

Each such witness prime `ell` gives a distinct target residue

\[
p\equiv-4\ell\pmod{3q}
\]

and, by the structural exact-depth theorem, a distinct infinite arithmetic progression of primes with exact square-completion depth `A_q`.

Let

\[
M(X)
=
\sum_{\substack{q\equiv1\ (4)\ {m prime}\\ A_q\le X}}
\nu_-(A_q).
\]

Thus `M(X)` counts the distinct explicitly certified infinite prime progressions supplied by prime witnesses across the composite backbone through depth `X`.

## Theorem

\[
\boxed{
M(X)
\sim
\frac13\frac{X\log\log X}{\log X}.
}
\]

Equivalently, if

\[
Y=\frac{4X-1}{3},
\]

then

\[
\boxed{
\sum_{\substack{q\le Y\\q\equiv1\ (4)\ {m prime}}}
\nu_-(A_q)
\sim
\frac14\frac{Y\log\log Y}{\log Y}.
}
\]

### Proof

Fix any constant

\[
0<\theta<\frac14.
\]

Split

\[
\nu_-(A_q)
=
\nu_{-,\le Y^\theta}(A_q)
+
\nu_{-,>Y^\theta}(A_q).
\]

### 1. Small witness primes

For an odd prime

\[
\ell\le Y^\theta,
\qquad
\ell\equiv2\pmod3,
\]

the condition

\[
\ell\mid A_q
\]

is equivalent to one reduced residue class for `q` modulo `4ell`. Hence

\[
\#\{q\le Y:q\equiv1\pmod4\text{ prime},\ \ell\mid A_q\}
=
\pi(Y;4\ell,a_\ell)
\]

for one reduced class `a_ell`.

Summing over `ell <= Y^theta` and using Bombieri--Vinogradov (the moduli `4ell` lie below `Y^theta`, well inside the level `Y^{1/2}`) gives

\[
\sum_{\substack{q\le Y\\q\equiv1\ (4)\ {m prime}}}
\nu_{-,\le Y^\theta}(A_q)
=
\frac12\operatorname{Li}(Y)
\sum_{\substack{\ell\le Y^\theta\\\ell\equiv2\ (3)\\\ell\ {m odd}}}
\frac1{\ell-1}
+o\!\left(\frac{Y}{\log Y}\right).
\]

Mertens' theorem in the progression `2 mod 3` gives

\[
\sum_{\substack{\ell\le Y^\theta\\\ell\equiv2\ (3)}}
\frac1{\ell-1}
=
\frac12\log\log Y+O_\theta(1).
\]

Therefore

\[
\sum_q\nu_{-,\le Y^\theta}(A_q)
=
\left(\frac14+o(1)\right)
\frac{Y\log\log Y}{\log Y}.
\]

The possible witness `ell=2` contributes at most `pi(Y;4,1)`, which is only `O(Y/log Y)` and is absorbed in the lower-order term relative to `Y log log Y/log Y`.

### 2. Large witness primes

Since

\[
A_q=\frac{3q+1}{4}\ll Y,
\]

the number of distinct prime divisors of `A_q` exceeding `Y^theta` is uniformly bounded.

Indeed, if `k` distinct primes exceeding `Y^theta` divide `A_q`, then

\[
Y^{\theta k}
<
\prod_{j=1}^k\ell_j
\le A_q
\ll Y.
\]

Thus

\[
k\le\frac1\theta+O(1),
\]

and hence

\[
\nu_{-,>Y^\theta}(A_q)=O_\theta(1)
\]

uniformly in `q`.

Summing over the `O(Y/log Y)` primes `q == 1 mod 4` gives

\[
\sum_q\nu_{-,>Y^\theta}(A_q)
=O_\theta\!\left(\frac{Y}{\log Y}\right),
\]

which is lower order.

Combining the two ranges proves

\[
\sum_{\substack{q\le Y\\q\equiv1\ (4)\ {m prime}}}
\nu_-(A_q)
\sim
\frac14\frac{Y\log\log Y}{\log Y}.
\]

Finally `Y=(4X-1)/3`, so

\[
\frac14\,Y
\sim
\frac13\,X,
\qquad
\log Y\sim\log X,
\qquad
\log\log Y\sim\log\log X,
\]

and therefore

\[
M(X)
\sim
\frac13\frac{X\log\log X}{\log X}.
\]

## Interpretation

The number of composite backbone depths through `X` is only of order

\[
\frac{X}{\log X},
\]

but a typical such depth carries about

\[
\frac12\log\log X
\]

distinct prime witnesses. Consequently the total number of explicitly certified infinite exact-depth prime progressions grows by the additional factor `log log X`:

\[
\boxed{
\text{certified prime families through depth }X
\asymp
\frac{X\log\log X}{\log X}.
}
\]

This counts witness-indexed target progressions, not individual prime denominators. Each counted progression contains infinitely many primes by Dirichlet's theorem.

## Claim boundary

The prime-distribution inputs (Bombieri--Vinogradov and Mertens in progressions) are standard. The candidate contribution is their application to count the multiplicity of the exact-depth prime families attached to the composite backbone.
