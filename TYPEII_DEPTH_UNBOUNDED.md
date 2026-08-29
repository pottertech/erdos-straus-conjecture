# Complete Type-II Square Depth Is Unbounded

**Status:** unconditional theorem; independently rederived here, but the unboundedness conclusion is prior art and is not claimed as new

## Literature / priority correction

A literature audit on 2026-08-29 found that the Free Computation Foundation / CENTL research library publicly recorded unbounded **square-completed Type-II first-hit depth** on 2026-08-15, before this branch. Their prime-modulus backbone is stronger in one direction: whenever `4A-1 > 7` is prime, depth `A` is realized by infinitely many Mordell-hard primes.

Accordingly, this note should be read as an independent elementary rederivation of unboundedness using the universal avoidance residue `1 mod (4A-1)`, not as a novelty claim. The separate quantitative Linnik consequence in `TYPEII_DEPTH_LOG_LOWER_BOUND.md` should be evaluated independently for priority.

For a prime `p == 1 (mod 4)`, use the square-completed Type-II criterion

\[
\exists A,D>0:
\qquad D\mid A^2,
\qquad 4A-1\mid p+4D,
\qquad p\nmid D.
\]

Define the square depth of `p` to be the least such `A` when a Type-II witness exists.

## Lemma: residue 1 is never a depth-A trap

Fix `A >= 1`. Suppose `D|A^2`. Then

\[
\boxed{4A-1\nmid 4D+1.}
\]

Proof. Let

\[
g=\gcd(A,D),\qquad A=g a,\qquad D=g d,\qquad \gcd(a,d)=1.
\]

Since `D|A^2`,

\[
gd\mid g^2a^2.
\]

Because `gcd(a,d)=1`, this implies `d|g`; write

\[
g=dh.
\]

Therefore

\[
\boxed{A=dha,\qquad D=d^2h}
\]

with positive integers `d,h,a` and `gcd(d,a)=1`.

Assume for contradiction that

\[
4A-1\mid4D+1.
\]

Since

\[
4A\equiv1\pmod{4A-1},
\qquad
4D\equiv-1\pmod{4A-1},
\]

we obtain

\[
D\equiv-A\pmod{4A-1},
\]

hence

\[
4A-1\mid D+A=dh(d+a).
\]

But

\[
\gcd(4A-1,dh)=1
\]

because `A=dha`. Thus

\[
4A-1\mid d+a.
\]

This is impossible, since

\[
4A-1=4dha-1>d+a
\]

for all positive `d,h,a`. Indeed

\[
4dha-1-(d+a)\ge4da-1-d-a>0.
\]

Contradiction. Therefore residue `1 mod (4A-1)` is never among the square-completed Type-II trap residues at depth `A`.

## Theorem: no finite square-depth bound can be universal

Fix any positive integer `J`, and set

\[
L_J=\operatorname{lcm}\bigl(840,\,3,7,11,\ldots,4J-1\bigr).
\]

By Dirichlet's theorem on primes in arithmetic progressions, there are infinitely many primes

\[
\boxed{p\equiv1\pmod{L_J}.}
\]

Such primes satisfy `p == 1 (mod 840)`, so they lie in the classical six-class core. Moreover, for every `1 <= A <= J`,

\[
p\equiv1\pmod{4A-1}.
\]

By the lemma, residue 1 modulo `4A-1` is not a square-completed Type-II trap for any divisor `D|A^2`. Therefore no such prime has a Type-II certificate with square depth `A <= J`.

Hence:

\[
\boxed{
\forall J\ge1,\quad
\text{infinitely many classical-core primes require Type-II square depth }>J.
}
\]

Equivalently, the minimum complete-Type-II square depth is unbounded on the primes.

## Consequences

1. The finite records `624` (through `10^8`) and `816` (through `10^9`) cannot stabilize to a universal constant.
2. Any proof strategy based on checking only finitely many fixed square depths `A` is impossible.
3. A successful Type-II proof must use genuinely growing depth, or a different structural argument that is not equivalent to a bounded square-depth cover.
4. This is consistent with the need for growing-depth large-sieve methods in current analytic work.

## Claim boundary

This theorem does **not** produce an Erdős--Straus counterexample. It only proves that the least Type-II depth, when measured by the square-completion parameter `A`, cannot be bounded by an absolute constant over all relevant primes.

The unboundedness conclusion itself is not claimed as new. Priority for any stronger quantitative consequence must be established separately.