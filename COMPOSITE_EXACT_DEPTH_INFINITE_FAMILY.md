# Infinite Family of Composite Exact Type-II Square Depths

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

## Theorem 2: a composite-modulus exact-depth backbone

Let

\[
q\equiv5\pmod8
\]

be prime, and define

\[
\boxed{A_q=\frac{3q+1}{4}.}
\]

Then `A_q` is a positive integer and

\[
\boxed{4A_q-1=3q}
\]

is composite.

Moreover, there are infinitely many primes `p == 1 (mod 4)` satisfying

\[
\boxed{\delta_{\rm sq}(p)=A_q.}
\]

In fact the target witness can always be chosen as

\[
\boxed{D=2.}
\]

### Proof

Since `q == 5 (mod 8)`,

\[
3q+1\equiv16\pmod{24},
\]

so

\[
A_q=\frac{3q+1}{4}\equiv4\pmod6.
\]

In particular `A_q` is even, hence

\[
2\mid A_q^2.
\]

Let

\[
m=4A_q-1=3q,
\qquad
 a\equiv-8\pmod m.
\]

Thus every integer

\[
n\equiv a\pmod m
\]

has a depth-`A_q` square-completed Type-II witness with `D=2`.

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

so `s >= 3`. Therefore

\[
m_B\ge3q=m,
\]

contradicting `B<A_q` and hence `m_B<m`.

Consequently

\[
\boxed{\gcd(m,m_B)\mid3}
\]

for every `B<A_q`.

On the other hand,

\[
a=-8\equiv1\pmod3.
\]

Let

\[
L=\operatorname{lcm}_{1\le B<A_q}(4B-1).
\]

The simultaneous congruences

\[
\boxed{
n\equiv-8\pmod{3q},
\qquad
n\equiv1\pmod L,
\qquad
n\equiv1\pmod4
}
\]

are CRT-compatible: every common divisor of `3q` and `L` divides `3`, and the first two target residues agree modulo `3`; the modulus `4` is coprime to all odd moduli involved.

Let

\[
n\equiv n_0\pmod M,
\qquad
M=\operatorname{lcm}(4,3q,L)
\]

be the resulting CRT progression.

For every earlier depth `B<A_q`,

\[
n\equiv1\pmod{4B-1}.
\]

By Lemma 1, residue `1` belongs to no earlier square-completed Type-II trap. Thus no member of this progression has square depth below `A_q`.

At the target layer,

\[
n\equiv-8\pmod{3q}=\pmod{4A_q-1},
\]

and `D=2|A_q^2`, so every member has a depth-`A_q` witness.

Finally the CRT progression is reduced. Every prime divisor of `L` sees residue `1`; the only new odd prime factor contributed by the target modulus is `q`, where the residue is `-8`, nonzero; and the residue modulo `4` is `1`. Thus

\[
\gcd(n_0,M)=1.
\]

Dirichlet's theorem on primes in arithmetic progressions gives infinitely many primes in this progression. Every such prime is `1 mod 4` and satisfies

\[
\delta_{\rm sq}(p)=A_q.
\]

## Corollary 3: infinitely many composite exact depths

There are infinitely many primes

\[
q\equiv5\pmod8.
\]

Therefore

\[
\boxed{
\left\{\frac{3q+1}{4}:q\text{ prime},\ q\equiv5\pmod8\right\}
\subseteq
\mathcal D^{\rm comp}_{\infty},
}
\]

where `D_comp_infty` denotes square-completion depths realized by infinitely many primes and having composite target modulus `4A-1`.

Hence the composite exact-depth spectrum is infinite and unbounded.

## Corollary 4: quantitative lower bound

Let

\[
N_{\rm comp}(X)
=
\#\{A\le X:4A-1\text{ composite and infinitely many primes have }\delta_{\rm sq}=A\}.
\]

The prime number theorem in arithmetic progressions gives

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

Thus the family has order `X/log X`, not merely infinitude.

## Corollary 5: realization inside a classical hard class

For every `q > 5` in the theorem,

\[
\gcd(3q,840)=3.
\]

The target residue `-8` is congruent to `1 mod 3`, so the construction can strengthen the congruence `n == 1 (mod 4)` to

\[
\boxed{p\equiv1\pmod{840}.}
\]

The combined progression remains reduced. Therefore for every prime

\[
q\equiv5\pmod8,\qquad q>5,
\]

there are infinitely many primes

\[
\boxed{p\equiv1\pmod{840}}
\]

with exact square-completion depth

\[
\boxed{\delta_{\rm sq}(p)=\frac{3q+1}{4}.}
\]

## Regression example

Take `q=13`. Then

\[
A_q=10,\qquad4A_q-1=39,\qquad D=2.
\]

Imposing the hard-core strengthening `p == 1 (mod 840)` gives a reduced CRT progression. One prime in this progression is

\[
\boxed{p=10,139,116,681}.
\]

Direct enumeration of all `B<=10` and all `E|B^2` verifies that its first square-completed Type-II witness is exactly

\[
(B,E)=(10,2).
\]

This finite example is only a regression check; the theorem is symbolic and does not depend on computation.

## Significance

This family is qualitatively different from the prime-modulus exact-depth backbone. Every target modulus here is deliberately composite:

\[
4A_q-1=3q.
\]

The proof works because `3` is the smallest possible `3 mod 4` factor. A new prime factor `q == 1 (mod 4)` cannot occur in any earlier modulus `4B-1`, while the target residue is arranged to agree modulo the only shared factor `3` with the universal safe residue `1`.

This gives an elementary infinite composite-modulus backbone inside the complete Type-II square-depth spectrum.

## Claim boundary / priority

The square-divisor Type-II criterion, CRT, Dirichlet's theorem, and the prime number theorem in arithmetic progressions are prior mathematics. The candidate contribution is the exact-depth synthesis above: the family

\[
A=(3q+1)/4,\quad q\equiv5\pmod8\text{ prime},
\]

as an infinite composite-modulus exact-depth backbone.

A targeted web/repository search on 2026-08-30 did not locate this exact family in the current Erdős--Straus depth-spectrum literature, including the public FCF/CENTL prime-modulus backbone and composite-core notes. That negative search is not a proof of novelty; broader historical review is still required before a publication-priority claim.

This theorem does **not** prove universal Type-II solvability or the Erdős--Straus conjecture.