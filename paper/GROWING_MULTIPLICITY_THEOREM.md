# Growing Multiplicity of Exact-Depth Prime Families

**Status:** unconditional theorem using only fixed-modulus / polylogarithmic-modulus prime distribution (Siegel--Walfisz), Mertens in the class `2 mod 3`, and Chebyshev's inequality. No novelty claim is made pending literature review.

For prime

\[
q\equiv1\pmod4,
\qquad
A_q=\frac{3q+1}{4},
\]

write

\[
\nu_-(A_q)
=
\#\{\ell:\ell\mid A_q,\ \ell\text{ prime},\ \ell\equiv2\pmod3\}.
\]

Every such prime factor `ell` is a valid target divisor in the structural `3q` theorem. Hence it yields an infinite prime progression of exact square-completion depth `A_q` with target residue

\[
p\equiv-4\ell\pmod{3q}.
\]

The earlier multiplicity theorem showed that for every fixed `R`, relative density one of prime parameters have `nu_-(A_q) >= R`. The result below gives an explicit growing lower bound.

---

## Theorem — growing multiplicity on a density-one set

As `Y -> infinity`, for relative density one of primes

\[
q\le Y,
\qquad q\equiv1\pmod4,
\]

one has

\[
\boxed{
\nu_-(A_q)
\ge
\left(\frac12-o(1)\right)\log\log\log Y.
}
\]

Equivalently, relative density one of the corresponding composite exact depths `A_q` support at least

\[
\boxed{
\left(\frac12-o(1)\right)\log\log\log q
}
\]

pairwise distinct infinite prime progressions realizing exact square depth `A_q`.

---

## Proof

Fix a constant `C>0` and set

\[
z=(\log Y)^C.
\]

Let

\[
\mathcal L(z)
=
\{\ell\le z:\ell\text{ odd prime},\ \ell\equiv2\pmod3\}.
\]

For each prime parameter `q == 1 (mod 4)`, define

\[
X_z(q)
=
\sum_{\ell\in\mathcal L(z)}
1_{\ell\mid A_q}.
\]

Clearly

\[
X_z(q)\le\nu_-(A_q).
\]

Let

\[
\mathcal Q(Y)=\{q\le Y:q\text{ prime},\ q\equiv1\pmod4\},
\qquad
N(Y)=|\mathcal Q(Y)|.
\]

By the prime number theorem in the fixed class `1 mod 4`,

\[
N(Y)\sim\frac12\operatorname{Li}(Y).
\]

### 1. One-prime divisibility probabilities

For `ell in L(z)`,

\[
\ell\mid A_q
\iff
3q\equiv-1\pmod\ell.
\]

Together with `q == 1 (mod 4)`, CRT gives one reduced residue class modulo `4 ell`. Hence

\[
\#\{q\in\mathcal Q(Y):\ell\mid A_q\}
=
\pi(Y;4\ell,a_\ell).
\]

Since `4 ell <= 4(log Y)^C`, Siegel--Walfisz is uniform over all such moduli. Therefore, for every fixed large `K`,

\[
\pi(Y;4\ell,a_\ell)
=
\frac{\operatorname{Li}(Y)}{\varphi(4\ell)}
+O_K\!\left(\frac{Y}{(\log Y)^K}\right)
\]

uniformly in `ell in L(z)`.

Because

\[
\varphi(4\ell)=2(\ell-1),
\]

the relative probability inside `Q(Y)` is

\[
\frac1{\ell-1}+o(1)
\]

uniformly after summation over the polylogarithmically many `ell`.

Thus

\[
\mathbb E_Y X_z
=
\sum_{\ell\in\mathcal L(z)}\frac1{\ell-1}+o(1).
\]

Mertens' theorem in the progression `2 mod 3` gives

\[
\sum_{\substack{\ell\le z\\\ell\equiv2(3)}}\frac1\ell
=
\frac12\log\log z+O(1),
\]

and

\[
\frac1{\ell-1}=\frac1\ell+O(\ell^{-2}).
\]

Therefore

\[
\boxed{
\mu_z:=\mathbb E_Y X_z
=
\frac12\log\log z+O(1)
=
\frac12\log\log\log Y+O_C(1).
}
\]

(The fixed constant `C` changes only the bounded additive term.)

### 2. Two-prime correlations

For distinct `ell,r in L(z)`, simultaneous divisibility

\[
\ell r\mid A_q
\]

plus `q == 1 (mod 4)` defines one reduced CRT class modulo

\[
4\ell r.
\]

Since

\[
4\ell r\le4z^2=4(\log Y)^{2C},
\]

Siegel--Walfisz again applies uniformly. Hence

\[
\mathbb P_Y(\ell r\mid A_q)
=
\frac1{(\ell-1)(r-1)}+o(1)
\]

with a total summed error `o(1)` after choosing the Siegel--Walfisz power saving `K` sufficiently large relative to `C`.

Thus distinct small-prime divisibility events are asymptotically independent at the second-moment level.

### 3. Variance

Expanding the second moment,

\[
\operatorname{Var}_Y(X_z)
=
\sum_{\ell\in\mathcal L(z)}
\left(\frac1{\ell-1}-\frac1{(\ell-1)^2}\right)
+o(\mu_z).
\]

Therefore

\[
\boxed{
\operatorname{Var}_Y(X_z)=O(\mu_z).
}
\]

Since

\[
\mu_z\to\infty,
\]

Chebyshev's inequality gives, for every fixed `epsilon>0`,

\[
\mathbb P_Y\left(
|X_z-\mu_z|>\epsilon\mu_z
\right)
\ll
\frac1{\epsilon^2\mu_z}
\longrightarrow0.
\]

Hence for relative density one of prime parameters `q == 1 (mod 4)`,

\[
X_z(q)
=(1+o(1))\mu_z.
\]

In particular,

\[
\nu_-(A_q)
\ge X_z(q)
\ge
\left(\frac12-o(1)\right)\log\log\log Y.
\]

This proves the theorem.

### 4. Distinct exact-depth prime families

For all sufficiently large `Y`, the sieving primes satisfy

\[
\ell\le z=(\log Y)^C\ll q
\]

for all but a relative-density-zero initial segment of `q in Q(Y)`. Hence distinct witness primes `ell` give distinct target residues

\[
-4\ell\pmod{3q}.
\]

The structural `3q` theorem supplies a reduced Dirichlet progression for each such target residue, and every prime in that progression has exact square-completion depth `A_q`.

Thus the number of pairwise distinct infinite exact-depth prime progressions supported by a typical `A_q` grows at least as

\[
\left(\frac12-o(1)\right)\log\log\log q.
\]

---

## Interpretation

The density-one backbone is therefore not merely highly populated in depth space. A typical depth itself carries an increasing number of independent infinite prime families.

Schematically:

\[
\boxed{
\text{typical }A_q
\quad\Longrightarrow\quad
\text{at least }(1/2-o(1))\log\log\log q
\text{ distinct exact-depth prime progressions}.}
\]

This strengthens the earlier fixed-`R` multiplicity theorem while staying within classical polylogarithmic-modulus prime-distribution estimates.

## Claim boundary

The theorem gives only a lower bound for `nu_-(A_q)`. It does **not** claim the full normal order

\[
\nu_-(A_q)\sim\frac12\log\log q.
\]

Proving such a statement would require distribution control for prime divisors of `A_q` over a much larger range and is a separate analytic problem.

The theorem does not imply universal Type-II solvability or the Erdős--Straus conjecture.