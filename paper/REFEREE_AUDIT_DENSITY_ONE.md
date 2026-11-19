# Referee Audit: Density-One Composite-Modulus Exact-Depth Backbone

**Purpose:** adversarial audit of the symbolic theorem in `paper/composite_exact_typeii_depths_v3.tex`.

## Main theorem under audit

For prime

\[
q\equiv1\pmod4,
\qquad
A_q=\frac{3q+1}{4},
\]

if `A_q` has a divisor `D|A_q^2` with `D==2 (mod 3)`, then infinitely many primes `p==1 (mod 4)` satisfy

\[
\delta_{\rm sq}(p)=A_q,
\]

with target modulus

\[
4A_q-1=3q.
\]

For relative density one of primes `q==1 (mod 4)`, such a divisor exists.

## Audit 1: integrality and target modulus

Because `q==1 (mod 4)`,

\[
3q+1\equiv0\pmod4,
\]

so `A_q` is integral. Also

\[
4A_q-1=3q.
\]

No hidden parity hypothesis is needed beyond `q==1 (mod 4)`.

## Audit 2: target witness

If `D|A_q^2`, then every integer

\[
n\equiv-4D\pmod{3q}
\]

has a square-completed Type-II witness at depth `A_q`.

The prime-Type-II coprimality condition `p\nmid D` is automatic for all primes in the final reduced progression because `q\nmid D` and all other fixed prime divisors of `D` divide the earlier-lcm modulus, where the denominator residue is `1`.

## Audit 3: why q cannot occur earlier

Suppose `B<A_q` and `q|(4B-1)`. Write

\[
4B-1=qs.
\]

Since `4B-1==3 (mod 4)` and `q==1 (mod 4)`,

\[
s\equiv3\pmod4,
\]

hence `s>=3`. Therefore

\[
4B-1\ge3q=4A_q-1,
\]

contradiction. Thus `q` divides no earlier modulus.

Consequently every common divisor of `3q` and an earlier `4B-1` divides `3`.

## Audit 4: compatibility with the universal safe residue

The target residue is

\[
-4D\equiv-D\pmod3.
\]

If `D==2 (mod 3)`, then

\[
-4D\equiv1\pmod3.
\]

Thus it agrees modulo every possible target/earlier gcd with the earlier safe residue `1`.

The CRT system

\[
n\equiv-4D\pmod{3q},
\qquad
n\equiv1\pmod L,
\qquad
n\equiv1\pmod4
\]

is therefore compatible, where

\[
L=\operatorname{lcm}_{B<A_q}(4B-1).
\]

## Audit 5: universal-safe-residue lemma

The lemma states that for every `B>=1` and every `E|B^2`,

\[
4B-1\nmid4E+1.
\]

The proof reduces a hypothetical divisibility to

\[
4B-1\mid d+a
\]

with

\[
B=dha,
\]

and then uses

\[
4dha-1>d+a.
\]

The boundary case `d=h=a=1` gives `3>2`, so there is no exceptional small case.

Hence every earlier depth is avoided simultaneously by forcing denominator residue `1` modulo every earlier modulus.

## Audit 6: reducedness

Every prime factor from the earlier lcm sees denominator residue `1`.

The only new odd prime factor in the target modulus is `q`. Since

\[
4A_q=3q+1\equiv1\pmod q,
\]

we have `q\nmid A_q`, hence `q\nmid D` for every `D|A_q^2`. Therefore the target residue `-4D` is nonzero modulo `q`.

Modulo `2`, the denominator is forced to `1`.

Thus the final CRT progression is reduced and Dirichlet applies.

## Audit 7: prime-factor reformulation

Because

\[
A_q\equiv1\pmod3,
\]

`3\nmid A_q`.

A divisor `D|A_q^2` with `D==2 (mod 3)` exists whenever `A_q` has a prime divisor `ell==2 (mod 3)`; choose `D=ell`.

Conversely, if every prime divisor of `A_q` is `1 mod 3`, then every divisor of `A_q^2` is `1 mod 3`, so this particular safe-residue construction has no admissible `D`.

This is a classification of the construction, not a classification of the full exact-depth spectrum.

## Audit 8: density-one argument

Among primes `q==1 (mod 4)`:

- `2|A_q` iff `q==5 (mod 8)`, so avoiding `2` has relative density `1/2`.
- For each fixed odd prime `ell==2 (mod 3)`,
  \[
  ell|A_q
  \iff
  q\equiv-3^{-1}\pmod\ell.
  \]
  This is one nonzero residue among the `ell-1` possible prime residue classes modulo `ell`.

For any **fixed finite** set `S` of odd primes `ell==2 (mod 3)`, PNT in arithmetic progressions modulo

\[
8\prod_{\ell\in S}\ell
\]

and CRT give the exact relative density

\[
\frac12\prod_{\ell\in S}
\left(1-\frac1{\ell-1}\right)
\]

for primes `q==1 (mod 4)` avoiding all corresponding divisibilities.

No uniformity in the modulus is invoked: `S` is fixed before the limit in `q`.

Then `S` is enlarged. Since

\[
\sum_{\ell\equiv2(3)}\frac1\ell=\infty,
\]

also

\[
\sum_{\ell\equiv2(3)}\frac1{\ell-1}=\infty,
\]

and therefore

\[
\prod_{\ell\in S}
\left(1-\frac1{\ell-1}\right)\to0.
\]

Hence the exceptional set has upper relative density zero. This proves relative natural density one for the structural family.

## Audit 9: counting constant

The successful prime parameters satisfy

\[
\#\{q\le Y:q\text{ prime}, q==1 (mod 4), \text{successful}\}
=
\left(\frac12+o(1)\right)\frac{Y}{\log Y}.
\]

The map

\[
q\mapsto A_q=\frac{3q+1}{4}
\]

is injective, and

\[
A_q\le X
\iff
q\le\frac{4X-1}{3}.
\]

Thus

\[
N_{\rm comp}(X)
\ge
\left(\frac12+o(1)\right)
\frac{(4/3)X}{\log X}
=
\left(\frac23+o(1)\right)
\frac{X}{\log X}.
\]

No double counting occurs because distinct `q` give distinct depths `A_q`.

## Audit 10: claim boundary

The theorem proves:

1. a density-one family in the prime parameter `q==1 (mod 4)`;
2. infinitely many prime denominators at each successful depth;
3. a lower bound of `(2/3+o(1)) X/log X` for composite-target depths in the infinite-realization spectrum.

It does **not** prove:

- that every composite target depth occurs;
- that every `A_q` occurs;
- universal Type-II solvability;
- the Erdős--Straus conjecture;
- publication priority over all historical literature.

## Publication recommendation

The symbolic theorem and density-one argument are suitable as the main paper. The `A=649` and `A=22339` finite certificates should be retained as secondary examples or supplementary material, not as the primary novelty claim.
