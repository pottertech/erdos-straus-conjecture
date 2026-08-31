# Erdős--Kac Law for Exact-Depth Multiplicity

**Status:** rigorous corollary of the general sieve-theoretic Erdős--Kac framework of Martin--Troupe, together with Bombieri--Vinogradov and Mertens in arithmetic progressions. No novelty claim is made for the probabilistic machinery itself.

For prime parameters

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

Every such prime divisor \(\ell\) gives a distinct target residue

\[
p\equiv-4\ell\pmod{3q}
\]

and, by the structural exact-depth theorem, a distinct infinite arithmetic progression of primes whose exact square-completion Type-II depth is \(A_q\).

## Theorem: Gaussian law

Let

\[
\mu(Y)
=
\sum_{\substack{\ell\le Y\\ \ell\equiv2\ (3)\\ \ell\text{ odd prime}}}
\frac1{\ell-1},
\]

and

\[
\sigma^2(Y)
=
\sum_{\substack{\ell\le Y\\ \ell\equiv2\ (3)\\ \ell\text{ odd prime}}}
\frac1{\ell-1}
\left(1-\frac1{\ell-1}\right).
\]

Then

\[
\mu(Y)=\frac12\log\log Y+O(1),
\qquad
\sigma^2(Y)=\frac12\log\log Y+O(1).
\]

For every real \(u\),

\[
\boxed{
\lim_{Y\to\infty}
\frac{1}{\pi(Y;4,1)}
\#\left\{
q\le Y:\ q\text{ prime},\ q\equiv1\pmod4,
\frac{\nu_-(A_q)-\mu(Y)}{\sigma(Y)}\le u
\right\}
=
\Phi(u),
}
\]

where

\[
\Phi(u)=\frac1{\sqrt{2\pi}}
\int_{-\infty}^{u}e^{-t^2/2}\,dt.
\]

Equivalently, because \(\mu(Y),\sigma^2(Y)=\tfrac12\log\log Y+O(1)\),

\[
\boxed{
\frac{
\nu_-(A_q)-\frac12\log\log q
}{
\sqrt{\frac12\log\log q}
}
\Longrightarrow N(0,1)
}
\]

over primes \(q\equiv1\pmod4\).

The prime factor \(2\) changes \(\nu_-(A_q)\) by at most one, so including or excluding \(2\) does not affect the limiting distribution.

## Proof via the Martin--Troupe framework

Let

\[
\widetilde{\mathcal A}
=
\left\{
A_q=\frac{3q+1}{4}:q\text{ prime},\ q\equiv1\pmod4
\right\}.
\]

For a cutoff \(X\), the condition \(A_q\le X\) is equivalent to

\[
q\le Y_X:=\frac{4X-1}{3}.
\]

Let

\[
\widetilde{\mathcal P}
=
\{\ell:\ell\text{ odd prime},\ \ell\equiv2\pmod3\}.
\]

Define the strongly additive function

\[
g(n)=\sum_{\substack{\ell\mid n\\ \ell\in\widetilde{\mathcal P}}}1.
\]

Thus \(g(A_q)\) is \(\nu_-(A_q)\) with the possible factor \(2\) omitted.

### Local densities

For squarefree \(d\) supported on \(\widetilde{\mathcal P}\),

\[
d\mid A_q
\iff
3q\equiv-1\pmod d,
\qquad q\equiv1\pmod4.
\]

Because \(3\) is invertible modulo such \(d\), CRT gives one reduced residue class \(a_d\pmod{4d}\). Therefore

\[
\#\{A_q\le X:d\mid A_q\}
=
\pi(Y_X;4d,a_d).
\]

Take

\[
\mathcal X=\frac12\operatorname{Li}(Y_X).
\]

Since \(d\) is odd,

\[
\varphi(4d)=2\varphi(d),
\]

so the expected relative density is

\[
\frac{1}{\varphi(d)}.
\]

In the notation of the Martin--Troupe general sieve framework, this means

\[
\frac{h(d)}{d}=\frac1{\varphi(d)},
\qquad
h(d)=\frac{d}{\varphi(d)}.
\]

In particular, for \(\ell\in\widetilde{\mathcal P}\),

\[
\frac{h(\ell)}{\ell}=\frac1{\ell-1}.
\]

Hence the mean and variance parameters for \(g\) are exactly

\[
\mu(Y)=\sum_{\substack{\ell\le Y\\\ell\in\widetilde{\mathcal P}}}
\frac1{\ell-1},
\]

and

\[
\sigma^2(Y)=
\sum_{\substack{\ell\le Y\\\ell\in\widetilde{\mathcal P}}}
\frac1{\ell-1}
\left(1-\frac1{\ell-1}\right).
\]

Mertens' theorem in the progression \(2\pmod3\) gives

\[
\mu(Y)=\frac12\log\log Y+O(1),
\qquad
\sigma^2(Y)=\frac12\log\log Y+O(1).
\]

### Remainder terms

Write

\[
r_d(X)
=
\pi(Y_X;4d,a_d)
-
\frac{\operatorname{Li}(Y_X)}{\varphi(4d)}.
\]

The Bombieri--Vinogradov theorem gives the average control of these remainder terms required in the general Martin--Troupe theorem, exactly as in their derivation of their shifted-prime Erdős--Kac theorem. Restricting the moduli to squarefree products of primes in \(\widetilde{\mathcal P}\) only reduces the relevant sums.

The additive function \(g\) is nonnegative, strongly additive, and satisfies \(g(\ell)=1\) on \(\widetilde{\mathcal P}\). Its variance diverges like \(\tfrac12\log\log Y\). Thus the hypotheses of the general distribution theorem apply with \(Q(T)=T\).

The conclusion is the stated Gaussian law for the odd part of \(\nu_-\). Adding the possible factor \(2\) changes the random variable by at most one, which is negligible after division by \(\sigma(Y)\to\infty\).

## Interpretation for exact-depth prime families

For each witness prime

\[
\ell\mid A_q,
\qquad \ell\equiv2\pmod3,
\]

the structural theorem gives a distinct infinite arithmetic progression of primes \(p\) with

\[
\delta_{\rm sq}(p)=A_q.
\]

Therefore the number of these explicitly certified infinite exact-depth prime progressions has a Gaussian limiting distribution with both mean and variance asymptotic to

\[
\frac12\log\log q.
\]

In particular, the previously proved normal-order statement

\[
\nu_-(A_q)
=
\left(\frac12+o(1)\right)\log\log q
\]

for relative density one of prime parameters follows immediately.

## Prior-art boundary

The Erdős--Kac machinery here is prior mathematics. In particular:

- Martin and Troupe, *The distribution of sums and products of additive functions*, J. Théorie des Nombres de Bordeaux 32 (2020), develop a general sieve-theoretic Erdős--Kac framework and explicitly derive shifted-prime variants using Bombieri--Vinogradov.
- Earlier shifted-prime additive-function distribution theory goes back at least to Halberstam and Hildebrand.

The candidate contribution is the application to the multiplicity function naturally attached to the composite exact-depth backbone

\[
A_q=(3q+1)/4,
\]

and its interpretation as the number of distinct infinite exact-depth prime progressions arising from witness primes \(\ell\equiv2\pmod3\).

No claim is made that the Gaussian-limit machinery itself is new.
