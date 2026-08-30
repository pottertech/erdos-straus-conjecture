# Infinite Families of Composite Exact Type-II Square Depths

**Status:** unconditional theorem. Uses only the square-divisor Type-II criterion, an elementary avoidance lemma, CRT, Dirichlet's theorem, and the prime number theorem in arithmetic progressions. No claim of literature priority is made pending a broader review.

For a prime denominator `p == 1 (mod 4)`, define the square-completion Type-II depth

\[
\delta_{\rm sq}(p)
=
\min\left\{A\ge1:\exists D\mid A^2,\ 4A-1\mid p+4D\right\},
\]

with `infinity` if no such witness exists.

The square-divisor criterion itself is historical prior art (Mizony/Thépault lineage) and is equivalent, after a change of variables, to the complete prime Type-II criterion.

## Lemma 1: residue 1 is universally safe

For every `B >= 1` and every divisor `E | B^2`,

\[
\boxed{4B-1\nmid 4E+1.}
\]

Equivalently,

\[
\boxed{1\notin R_B:=\{-4E\pmod{4B-1}:E\mid B^2\}.}
\]

### Proof

Put

\[
g=\gcd(B,E),\qquad B=ga,\qquad E=gd,\qquad \gcd(a,d)=1.
\]

Since `E | B^2`,

\[
gd\mid g^2a^2.
\]

Thus `d | g`; write `g=dh`. Then

\[
B=dha,\qquad E=d^2h.
\]

Assume for contradiction that

\[
4B-1\mid4E+1.
\]

Modulo `4B-1`,

\[
4B\equiv1,\qquad4E\equiv-1,
\]

so, since `4` is invertible modulo the odd number `4B-1`,

\[
E\equiv-B\pmod{4B-1}.
\]

Hence

\[
4B-1\mid E+B=dh(d+a).
\]

But

\[
\gcd(4B-1,dh)=1
\]

because `B=dha`. Therefore

\[
4B-1\mid d+a.
\]

This is impossible because

\[
4B-1=4dha-1>d+a
\]

for positive `d,h,a`. Contradiction.

## Theorem 2: structural composite-modulus exact-depth criterion

Let

\[
q\equiv1\pmod4
\]

be prime and put

\[
\boxed{A_q=\frac{3q+1}{4}}.
\]

Suppose `A_q` has a divisor

\[
\boxed{D\mid A_q^2,\qquad D\equiv2\pmod3.}
\]

Equivalently, it is enough that `A_q` have at least one prime divisor `ell == 2 (mod 3)`.

Then

\[
\boxed{4A_q-1=3q}
\]

is composite, and there are infinitely many primes `p == 1 (mod 4)` such that

\[
\boxed{\delta_{\rm sq}(p)=A_q.}
\]

The depth-`A_q` witness is the chosen divisor `D`.

### Proof

Let

\[
m=4A_q-1=3q,
\qquad
 a\equiv-4D\pmod m.
\]

Since `D == 2 (mod 3)`,

\[
a=-4D\equiv1\pmod3.
\]

Every integer

\[
n\equiv a\pmod m
\]

has a depth-`A_q` square-completed Type-II witness because `D|A_q^2`.

Now consider any earlier depth

\[
1\le B<A_q,
\qquad m_B=4B-1.
\]

We claim

\[
q\nmid m_B.
\]

Indeed, if `q | m_B`, write `m_B=q s`. Because

\[
m_B\equiv3\pmod4,
\qquad q\equiv1\pmod4,
\]

we must have

\[
s\equiv3\pmod4,
\]

so `s >= 3`. Hence

\[
m_B\ge3q=m,
\]

contradicting `B<A_q`, which implies `m_B<m`.

Therefore

\[
\boxed{\gcd(m,m_B)\mid3}
\]

for every earlier `B`.

Let

\[
L=\operatorname{lcm}_{1\le B<A_q}(4B-1).
\]

The simultaneous congruences

\[
\boxed{
n\equiv-4D\pmod{3q},
\qquad
n\equiv1\pmod L,
\qquad
n\equiv1\pmod4
}
\]

are CRT-compatible. Every common divisor of `3q` and `L` divides `3`, and the first two residues agree modulo `3`; the modulus `4` is coprime to all odd moduli involved.

Let

\[
n\equiv n_0\pmod M,
\qquad
M=\operatorname{lcm}(4,3q,L)
\]

be the resulting CRT progression.

For every `B<A_q`,

\[
n\equiv1\pmod{4B-1}.
\]

By Lemma 1, residue `1` belongs to no earlier square-completed Type-II trap. Thus no member of this progression has square depth below `A_q`.

At the target layer,

\[
n\equiv-4D\pmod{3q}=\pmod{4A_q-1},
\]

with `D|A_q^2`, so every member has a depth-`A_q` witness.

The progression is reduced. Every prime divisor contributed by `L` sees residue `1`. The only new odd prime factor contributed by the target modulus is `q`, and `q\nmid D`: if `q|D` and `D|A_q^2`, then `q|A_q`, impossible because

\[
4A_q=3q+1\equiv1\pmod q.
\]

Hence the target residue `-4D` is nonzero modulo `q`. The residue modulo `4` is `1`. Therefore

\[
\gcd(n_0,M)=1.
\]

Dirichlet's theorem gives infinitely many primes in this progression, every one congruent to `1 mod 4`, and every one satisfies

\[
\delta_{\rm sq}(p)=A_q.
\]

## Corollary 3: prime-factor formulation

For prime `q == 1 (mod 4)`, put `A_q=(3q+1)/4`. If `A_q` has any prime divisor

\[
\ell\equiv2\pmod3,
\]

then `D=ell` satisfies the theorem. Hence

\[
\boxed{
A_q\text{ has a prime factor }2\pmod3
\Longrightarrow
A_q\in\mathcal D^{\rm comp}_{\infty}.
}
\]

Thus the only obstruction to this particular universal-safe-residue construction is that every prime factor of `A_q` be `1 mod 3`.

## Corollary 4: fixed-witness arithmetic progressions

Fix any positive integer

\[
d\equiv2\pmod3,
\qquad 3\nmid d.
\]

There is a unique reduced residue class `a_d mod 4d` satisfying

\[
3a_d\equiv-1\pmod{4d}.
\]

For every prime

\[
q\equiv a_d\pmod{4d},
\]

we have

\[
d\mid \frac{3q+1}{4}=A_q,
\]

so taking `D=d` in Theorem 2 gives infinitely many prime denominators of exact depth `A_q`.

Dirichlet's theorem gives infinitely many such primes `q`. Therefore every fixed `d == 2 (mod 3)` generates its own infinite composite exact-depth subfamily.

## Corollary 5: the elementary D=2 backbone

Taking `d=2` gives

\[
3q\equiv-1\pmod8
\iff
q\equiv5\pmod8.
\]

Thus every prime

\[
q\equiv5\pmod8
\]

gives the exact depth

\[
\boxed{A_q=\frac{3q+1}{4}}
\]

with witness `D=2`.

Consequently the composite exact-depth spectrum is infinite and unbounded.

## Corollary 6: quantitative lower bound

Let

\[
N_{\rm comp}(X)
=
\#\{A\le X:4A-1\text{ composite and infinitely many primes have }\delta_{\rm sq}=A\}.
\]

Already the `D=2` subfamily gives

\[
\pi(Y;8,5)\sim\frac14\operatorname{Li}(Y).
\]

Since

\[
A_q\le X
\iff
q\le\frac{4X-1}{3},
\]

we obtain

\[
\boxed{
N_{\rm comp}(X)
\ge
\pi\!\left(\frac{4X-1}{3};8,5\right)
=
\left(\frac13+o(1)\right)\frac{X}{\log X}.
}
\]

The more general fixed-`d` families can only enlarge this lower-bound set.

## Corollary 7: realization inside a classical hard class

If `q>5`, `q == 1 (mod 4)`, and the theorem's divisor `D` also satisfies

\[
-4D\equiv1\pmod{\gcd(3q,840)},
\]

then the construction can impose

\[
p\equiv1\pmod{840}
\]

instead of merely `p == 1 (mod 4)`.

In particular, for the `D=2`, `q == 5 (mod 8)`, `q>5` subfamily,

\[
\gcd(3q,840)=3,
\qquad -8\equiv1\pmod3,
\]

so infinitely many exact-depth primes lie in the classical hard class

\[
\boxed{p\equiv1\pmod{840}}.
\]

## Regression example

Take `q=13`. Then

\[
A_q=10,\qquad4A_q-1=39,\qquad D=2.
\]

Imposing `p == 1 (mod 840)` gives a reduced CRT progression. One prime in this progression is

\[
\boxed{p=10,139,116,681}.
\]

Direct enumeration of all `B<=10` and all `E|B^2` verifies that its first square-completed Type-II witness is exactly

\[
(B,E)=(10,2).
\]

This finite example is only a regression check; the theorem is symbolic and does not depend on computation.

## Significance

The family is qualitatively different from the prime-modulus exact-depth backbone. Every target modulus is deliberately composite:

\[
4A_q-1=3q.
\]

The proof works because `3` is the smallest positive `3 mod 4` cofactor. A new prime factor `q == 1 (mod 4)` cannot occur in any earlier modulus `4B-1`, while the chosen target divisor `D == 2 (mod 3)` makes the target residue agree modulo the only possible shared factor `3` with the universal safe residue `1`.

This gives an elementary composite-modulus backbone inside the complete Type-II square-depth spectrum, with a structural criterion on `A_q` and infinitely many fixed-witness arithmetic subfamilies.

## Claim boundary / priority

The square-divisor Type-II criterion, CRT, Dirichlet's theorem, and the prime number theorem in arithmetic progressions are prior mathematics. The candidate contribution is the exact-depth synthesis above, especially the structural family

\[
A_q=(3q+1)/4,
\quad q\equiv1\pmod4\text{ prime},
\quad A_q\text{ possessing a prime factor }2\pmod3,
\]

as an infinite composite-modulus exact-depth backbone.

Targeted web/repository searches on 2026-08-30 did not locate this exact family in the current Erdős--Straus depth-spectrum literature, including the public FCF/CENTL prime-modulus backbone and composite-core notes. That negative search is not a proof of novelty; broader historical review is still required before a publication-priority claim.

This theorem does **not** prove universal Type-II solvability or the Erdős--Straus conjecture.
