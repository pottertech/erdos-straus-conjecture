# Normal Order of Exact-Depth Witness Multiplicity

**Status:** unconditional theorem using Bombieri--Vinogradov, Mertens in the progression `2 mod 3`, and a second-moment argument. No novelty claim is made pending literature review.

For prime

\[
q\equiv1\pmod4,
\qquad
A_q=\frac{3q+1}{4},
\]

let

\[
\nu_-(A_q)
=
\#\{\ell:\ell\mid A_q,\ \ell\text{ prime},\ \ell\equiv2\pmod3\}.
\]

Every such prime factor `ell` supplies, through the structural `3q` theorem, a distinct infinite prime progression with exact square-completion depth `A_q`.

The earlier multiplicity notes proved fixed-`R` density one and then a growing lower bound of order `log log log q`. Bombieri--Vinogradov permits the full normal order.

---

## Theorem — normal order

For relative density one of primes

\[
q\equiv1\pmod4,
\]

one has

\[
\boxed{
\nu_-(A_q)
=
\left(\frac12+o(1)\right)\log\log q.
}
\]

Consequently, for relative density one of the composite exact depths

\[
A_q=\frac{3q+1}{4},
\]

the number of pairwise distinct infinite prime progressions realizing exact square depth `A_q` has normal order

\[
\boxed{\frac12\log\log q.}
\]

---

## Proof

Fix once and for all a constant

\[
0<\theta<\frac14.
\]

For `Y` large, put

\[
z=Y^\theta.
\]

Let

\[
\mathcal L(z)
=
\{\ell\le z:\ell\text{ odd prime},\ \ell\equiv2\pmod3\}.
\]

For prime parameters

\[
\mathcal Q(Y)=\{q\le Y:q\text{ prime},\ q\equiv1\pmod4\},
\]

define

\[
X_z(q)
=
\sum_{\ell\in\mathcal L(z)}1_{\ell\mid A_q}.
\]

We first prove that `X_z` has normal order `(1/2) log log Y` on `Q(Y)`.

### 1. First moment

For `ell in L(z)`,

\[
\ell\mid A_q
\iff
3q\equiv-1\pmod\ell.
\]

Together with `q == 1 (mod 4)`, this defines one reduced residue class `a_ell mod 4ell`. Therefore

\[
\#\{q\in\mathcal Q(Y):\ell\mid A_q\}
=
\pi(Y;4\ell,a_\ell).
\]

Let

\[
N(Y)=|\mathcal Q(Y)|\sim\frac12\operatorname{Li}(Y).
\]

Bombieri--Vinogradov, restricted to the moduli `4ell <= 4Y^theta`, gives for every fixed large `A_0`

\[
\sum_{\ell\in\mathcal L(z)}
\left|
\pi(Y;4\ell,a_\ell)
-
\frac{\operatorname{Li}(Y)}{\varphi(4\ell)}
\right|
\ll_{A_0}
\frac{Y}{(\log Y)^{A_0}}.
\]

Because

\[
\varphi(4\ell)=2(\ell-1),
\]

we obtain

\[
\mathbb E_Y X_z
=
\sum_{\ell\in\mathcal L(z)}\frac1{\ell-1}+o(1).
\]

Mertens in the class `2 mod 3` yields

\[
\sum_{\substack{\ell\le z\\\ell\equiv2(3)}}\frac1{\ell-1}
=
\frac12\log\log z+O(1).
\]

Since `z=Y^theta`,

\[
\log\log z
=
\log(\theta\log Y)
=
\log\log Y+O_\theta(1).
\]

Hence

\[
\boxed{
\mu_Y:=\mathbb E_Y X_z
=
\frac12\log\log Y+O_\theta(1).
}
\]

### 2. Second moment

For distinct `ell,r in L(z)`, simultaneous divisibility

\[
\ell r\mid A_q
\]

and `q == 1 (mod 4)` define one reduced residue class modulo

\[
4\ell r.
\]

Because

\[
4\ell r\le4Y^{2\theta}
\]

and `2theta<1/2`, the moduli lie within a Bombieri--Vinogradov range (with room for the usual logarithmic loss).

Moreover a modulus `ell r` with distinct primes has only boundedly many ordered representations by `(ell,r)`. Therefore summing the progression errors over all distinct pairs is bounded by the Bombieri--Vinogradov modulus sum:

\[
\sum_{\substack{\ell,r\in\mathcal L(z)\\\ell\ne r}}
\left|
\pi(Y;4\ell r,a_{\ell r})
-
\frac{\operatorname{Li}(Y)}{\varphi(4\ell r)}
\right|
\ll_{A_0}
\frac{Y}{(\log Y)^{A_0}}.
\]

Thus

\[
\mathbb E_Y[X_z(X_z-1)]
=
\sum_{\ell\ne r}
\frac1{(\ell-1)(r-1)}+o(1).
\]

Combining diagonal and off-diagonal terms gives

\[
\operatorname{Var}_Y(X_z)
=
\sum_{\ell\in\mathcal L(z)}
\left(
\frac1{\ell-1}-\frac1{(\ell-1)^2}
\right)
+o(\mu_Y).
\]

Hence

\[
\boxed{
\operatorname{Var}_Y(X_z)=O(\log\log Y).
}
\]

Since

\[
\mu_Y\sim\frac12\log\log Y,
\]

we have

\[
\frac{\operatorname{Var}_Y(X_z)}{\mu_Y^2}
=O\!\left(\frac1{\log\log Y}\right)
\to0.
\]

Chebyshev's inequality therefore implies that, for relative density one of `q in Q(Y)`,

\[
\boxed{
X_z(q)
=
\left(\frac12+o(1)\right)\log\log Y.
}
\]

### 3. Large prime factors contribute only `O(1)`

The integer

\[
A_q=\frac{3q+1}{4}
\]

satisfies

\[
A_q<Y
\]

for `q<=Y` and `Y` sufficiently large.

Any distinct prime divisor of `A_q` exceeding

\[
z=Y^\theta
\]

contributes a factor greater than `Y^theta`. If there are `k` such distinct prime factors, their product divides `A_q<Y`, so

\[
Y^{\theta k}<Y.
\]

Therefore

\[
\boxed{k<1/\theta.}
\]

Thus the number of prime divisors `ell == 2 (mod 3)` of `A_q` above `z` is bounded by a constant depending only on the fixed `theta`:

\[
\nu_-(A_q)-X_z(q)=O_\theta(1).
\]

Since `log log Y -> infinity`, this bounded contribution is negligible. Hence, for relative density one of `q in Q(Y)`,

\[
\boxed{
\nu_-(A_q)
=
\left(\frac12+o(1)\right)\log\log Y.
}
\]

Finally the initial segment `q<Y^{1/2}` contains `o(pi(Y;4,1))` primes. On the remaining relative-density-one set,

\[
\log\log q
=
\log\log Y+O(1),
\]

so the same statement is equivalently

\[
\boxed{
\nu_-(A_q)
=
\left(\frac12+o(1)\right)\log\log q.
}
\]

This proves the theorem.

---

## Corollary — normal order of exact-depth progression multiplicity

Distinct witness primes `ell|A_q`, `ell == 2 (mod 3)`, give distinct residues

\[
-4\ell\pmod{3q}
\]

for all sufficiently large `q` except a relative-density-zero initial range, since each such `ell` divides `A_q<q` up to a harmless fixed factor and distinct divisors cannot differ by `3q`.

Each residue supports an infinite reduced Dirichlet progression of primes with exact square-completion depth `A_q`.

Therefore the number `M(A_q)` of these pairwise distinct exact-depth prime progressions satisfies

\[
\boxed{
M(A_q)
=
\left(\frac12+o(1)\right)\log\log q
}
\]

for relative density one of prime parameters `q == 1 (mod 4)`.

Here `M(A_q)` counts the canonical prime-divisor witness families supplied by the structural theorem; other exact-depth branches may exist and are not counted.

---

## Claim boundary

The theorem establishes a normal order for the number of prime divisors `ell == 2 (mod 3)` of the shifted prime value `(3q+1)/4`, restricted to prime `q == 1 (mod 4)`, and translates those factors into exact-depth prime families.

It does **not** establish an Erdős--Kac central limit theorem for `nu_-(A_q)`. Such a Gaussian distribution statement would require higher-moment or characteristic-function control beyond the second-moment argument used here.

It also does not imply universal Type-II solvability or the Erdős--Straus conjecture.