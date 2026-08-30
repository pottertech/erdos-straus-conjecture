# Five-Factor Modulus Ancestry Cover Conjecture

**Status:** exact formulation plus finite verification; open conjecture, not a theorem.

For any odd modulus

\[
m\equiv3\pmod4,
\]

write

\[
A=\frac{m+1}{4}.
\]

For every proper divisor

\[
1<d<m,\qquad d\mid m,\qquad d\equiv3\pmod4,
\]

set

\[
B=\frac{d+1}{4}
\]

and define the square-completed ancestor set

\[
Q_B=\{E\pmod d:E\mid B^2\}.
\]

A unit square class `r mod m` is called **proper-ancestor inherited** if for at least one such `d`,

\[
r\pmod d\in Q_B.
\]

This definition is independent of any particular factorization `A=uv` or any denominator prime `p`.

## Conjecture

If

\[
\boxed{\omega(m)\ge5}
\]

where `omega` is the number of distinct prime factors, then every unit square class modulo `m` is proper-ancestor inherited.

Equivalently:

\[
\boxed{
\omega(m)\ge5,\ m\equiv3\pmod4
\Longrightarrow
\bigcup_{\substack{d\mid m\\1<d<m\\d\equiv3(4)}}
\pi_d^{-1}(Q_{(d+1)/4})
\supseteq QR(m),
}
\]

where `QR(m)` denotes the unit square classes modulo `m` and `pi_d` is reduction modulo `d`.

## Why this would matter for semiprime Type-II depth

Suppose

\[
A=uv
\]

with distinct primes `u,v`, and `m=4uv-1`.  The genuinely square-only mixed directions are represented by the square classes `u^2` and `v^2` modulo `m`.

If the conjecture holds and `omega(m)>=5`, then `u^2` is inherited from some proper depth `B<A`; by the complementary pairing argument in `SEMIPRIME_MIXED_RESCUE_CORE.md`, `v^2` is inherited as well.  Therefore no squarefree-semiprime layer with `omega(4uv-1)>=5` can be structurally primitive.

This would prove the empirical observation from the semiprime census rather than merely record it.

## Exact finite evidence

The analyzer `modulus_ancestry_square_cover_analyzer.py` performs a complete unit-square-class test for each modulus, with no sampling and no denominator-prime search.

Independent finite checks performed during the 2026-08-30 audit found:

- every `m <= 100000`, `m == 3 (mod 4)`, with `omega(m)>=5` is fully covered by proper ancestors;
- the verification was extended through `m <= 250000` with no counterexample;
- in the semiprime-index census through `A <= 200000`, no structurally primitive `A=uv` had `omega(4uv-1)>=5`.

These are finite facts only.  They do not establish the conjecture.

## Why simple local counting is insufficient

For a prime ancestor divisor `q == 3 (mod 4)`, a primitive square class must avoid at least

\[
1,\quad B,\quad B^2\pmod q,
\qquad B=(q+1)/4.
\]

This yields the universal restrictions

\[
u\not\equiv\pm1,\ \pm2^{-1},\ \pm4^{-1}\pmod q.
\]

For large `q`, however, many square classes remain.  Thus a proof of the five-factor conjecture cannot follow from independent pigeonhole counting at individual prime divisors.

The crucial extra structure is that **all** proper divisors `d == 3 (mod 4)` of the same modulus `m` act simultaneously.  When `omega(m)` is large, the ancestry lattice contains many overlapping composite divisors, and their exact `Q_B` sets appear empirically to cover the full square subgroup.

## Relation to the FCF/CENTL reciprocity framework

FCF/CENTL has independently developed a reciprocity-matrix and ancestor-shadow framework for the Type A/B and square-completed geometry.  In particular, the relation `m=4A-1` imposes nontrivial left- and right-kernel constraints on the quadratic-signature matrix.

For squarefree semiprime `A=uv`, the right-kernel relation makes the two prime-factor signature columns dependent, while increasing `omega(m)` forces a large left-nullity.  This is qualitatively consistent with the disappearance of primitive high-omega layers.

However, the conjecture above is an **exact residue-cover statement**, stronger than a quadratic-signature rank statement.  No priority claim is made; a dedicated literature comparison is still required before publication.

## Proof targets

A proof would likely require one of the following.

1. **Ancestry-lattice induction.** Show that adding a fifth distinct prime factor forces enough new `3 mod 4` proper divisors that every surviving square class from the four-factor stage is captured.

2. **CRT decomposition.** Express the survivor set as a product/union of local square classes and prove that the composite-divisor ancestor conditions eliminate every CRT combination once five prime factors are present.

3. **Reciprocity plus exact lifting.** Use the low rank of the semiprime reciprocity matrix to reduce possible signatures, then upgrade signature membership to exact divisor-residue membership in some `Q_B`.

4. **Minimal-counterexample descent.** Assume a least modulus with five distinct factors and a surviving square class; remove one prime factor and exploit the survivor's forced behavior on the resulting proper divisor to construct an ancestor contradiction.

## Claim boundary

This conjecture does not prove universal Type II or the Erdős--Straus conjecture.  Even if proved, it would eliminate one large class of structurally primitive squarefree-semiprime depth layers.  The remaining cases `omega(4uv-1)<=4`, prime depths, prime powers, and higher-factor depth indices would still require analysis.
