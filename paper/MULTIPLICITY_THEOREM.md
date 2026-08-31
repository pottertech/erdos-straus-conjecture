# Multiplicity of composite exact-depth prime families

**Status:** unconditional consequence of the symbolic composite-backbone theorem.

For prime `q == 1 (mod 4)`, put

\[
A_q=\frac{3q+1}{4}.
\]

Let

\[
\nu_-(A_q)=\#\{\ell\text{ prime}:\ell\mid A_q,\ \ell\equiv2\pmod3\}.
\]

Each such prime divisor `ell` is an admissible target witness `D=ell` in the structural theorem. Thus every such `ell` produces an infinite reduced arithmetic progression of primes `p` with exact square-completion depth `A_q` and target congruence

\[
p\equiv -4\ell\pmod{3q}.
\]

These target residue classes are pairwise distinct: if

\[
-4\ell_1\equiv-4\ell_2\pmod{3q},
\]

then, since `gcd(4,3q)=1`, one has `3q | (ell_1-ell_2)`. But both primes divide `A_q`, hence are at most `A_q<3q`; therefore `ell_1=ell_2`.

## Theorem 1: prescribed multiplicity

Let

\[
S=\{\ell_1,\ldots,\ell_R\}
\]

be any finite set of distinct primes satisfying

\[
\ell_i\equiv2\pmod3.
\]

Then there are infinitely many primes

\[
q\equiv1\pmod4
\]

such that every `ell_i` divides `A_q=(3q+1)/4`.

Consequently, for infinitely many composite exact depths `A_q`, there are at least `R` pairwise distinct infinite prime progressions whose members all have exact depth `A_q`.

### Proof

Let

\[
P=\prod_{i=1}^R\ell_i.
\]

The conditions `ell_i | A_q` are equivalent to

\[
3q\equiv-1\pmod{4\ell_i}.
\]

Together with `q == 1 (mod 4)`, CRT gives one residue class `q == a (mod 4P)`. This class is reduced: modulo every `ell_i`, the residue is `-3^{-1}`, which is nonzero, and modulo `4` it is `1`. Dirichlet's theorem therefore gives infinitely many prime `q` in this class. For each such `q`, all primes in `S` divide `A_q`, and each gives a distinct exact-depth target progression by the structural theorem.

## Theorem 2: density-one unbounded multiplicity

For every fixed integer

\[
R\ge1,
\]

the set of primes `q == 1 (mod 4)` satisfying

\[
\boxed{\nu_-(A_q)\ge R}
\]

has relative natural density `1` among primes `q == 1 (mod 4)`.

Equivalently: for every fixed `R`, almost every prime parameter `q == 1 (mod 4)` gives a composite exact depth `A_q` supporting at least `R` pairwise distinct infinite prime progressions of exact-depth denominators.

### Proof

Fix `epsilon>0`. Because

\[
\sum_{\ell\equiv2(3)}\frac1\ell=\infty,
\]

we may choose `R` pairwise disjoint finite sets

\[
S_1,\ldots,S_R
\]

of odd primes `ell == 2 (mod 3)` such that for every `j`,

\[
\prod_{\ell\in S_j}\left(1-\frac1{\ell-1}\right)<\frac{\epsilon}{R}.
\]

For a fixed finite set `S_j`, CRT and the prime number theorem in arithmetic progressions give the exact limiting relative density

\[
\prod_{\ell\in S_j}\left(1-\frac1{\ell-1}\right)
\]

of primes `q == 1 (mod 4)` for which none of the primes in `S_j` divides `A_q`.

By the union bound, the upper relative density of primes `q == 1 (mod 4)` for which at least one block `S_j` contributes no divisor of `A_q` is less than `epsilon`.

Outside this exceptional set, each of the `R` disjoint blocks contributes at least one distinct prime divisor `ell == 2 (mod 3)` of `A_q`. Hence

\[
\nu_-(A_q)\ge R.
\]

Since `epsilon` is arbitrary, the relative density is `1`.

## Corollary 3: multiplicity tends to infinity in density

The quantity `nu_-(A_q)` tends to infinity in probability with respect to primes `q == 1 (mod 4)`: for every fixed `R`,

\[
\frac{\#\{q\le Y:q\text{ prime},\ q\equiv1\pmod4,\ \nu_-(A_q)\ge R\}}
{\pi(Y;4,1)}\to1.
\]

Therefore a density-one set of composite exact depths in the `3q` backbone carries not merely one but arbitrarily many distinct infinite exact-depth prime families.

## Claim boundary

This is a multiplicity theorem for exact square-completion Type-II depth. It does not imply that every prime denominator has Type II, and it does not prove the Erdős--Straus conjecture.

The proof uses only the already-established structural backbone theorem, finite CRT, Dirichlet's theorem, the prime number theorem in fixed arithmetic progressions, and the divergence of the reciprocal sum over primes `2 mod 3`.
