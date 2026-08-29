# Logarithmic Lower Bound for Complete Type-II Square Depth Along an Infinite Sequence

**Status:** unconditional corollary of the depth-avoidance progression plus standard PNT-in-AP and Linnik theorems; mathematical proof audited, novelty not established

## Priority status

The underlying fact that square-completed Type-II first-hit depth is unbounded is prior art: the Free Computation Foundation / CENTL research library recorded a stronger prime-modulus realization theorem on 2026-08-15.

The literature search performed for this branch did **not** locate this specific Linnik-based quantitative conclusion

\[
\operatorname{depth}_{II}(p)\gg\log p
\]

along an infinite sequence. That absence is not a priority proof. Until a publication-grade search is completed, this result should be described as an unconditional quantitative corollary derived here, with novelty explicitly unclaimed.

Let `depth_II(p)` denote the least square-completion parameter `A` for which

\[
\exists D\mid A^2:\qquad 4A-1\mid p+4D
\]

(with the usual prime Type-II coprimality condition).

`TYPEII_DEPTH_UNBOUNDED.md` proves that residue `1 mod (4A-1)` is never a depth-`A` trap. Hence, with

\[
L_J=\operatorname{lcm}(840,3,7,11,\ldots,4J-1),
\]

every prime

\[
p\equiv1\pmod{L_J}
\]

satisfies

\[
\boxed{\operatorname{depth}_{II}(p)>J.}
\]

## Size of the avoidance modulus

Every prime

\[
q\le4J,\qquad q\equiv3\pmod4,
\]

occurs as one of the numbers `4A-1` and therefore divides `L_J`.

Consequently

\[
\log L_J
\ge
\sum_{\substack{q\le4J\\q\equiv3\ (4)}}\log q.
\]

The prime number theorem in arithmetic progressions gives

\[
\sum_{\substack{q\le x\\q\equiv3\ (4)}}\log q
=\frac{x}{2}+o(x).
\]

At `x=4J`,

\[
\log L_J\ge(2+o(1))J.
\]

On the other hand,

\[
L_J\mid\operatorname{lcm}(1,2,\ldots,4J)\cdot840,
\]

so the standard Chebyshev/PNT estimate for the full lcm gives

\[
\log L_J=O(J).
\]

Thus

\[
\boxed{\log L_J=\Theta(J).}
\]

## Linnik progression prime

By Linnik's theorem, the least prime in the reduced progression

\[
p\equiv1\pmod{L_J}
\]

satisfies

\[
p_J\ll L_J^C
\]

for an absolute constant `C`.

Therefore

\[
\log p_J\le C\log L_J+O(1)=O(J).
\]

Since `depth_II(p_J)>J`, we obtain

\[
\boxed{
\operatorname{depth}_{II}(p_J)\gg\log p_J.
}
\]

As `J -> infinity`, the moduli `L_J` grow and the corresponding progression primes cannot remain bounded. Hence this yields an infinite sequence of classical-core primes with minimum complete-Type-II square depth at least a positive constant times their logarithm.

## Consequences

1. Complete Type-II square depth is not merely unbounded; logarithmic-scale square depth is necessary along an infinite sequence.
2. Any universal Type-II algorithm/proof whose allowed **square-completion depth** is `o(log p)` must fail on infinitely many relevant primes.
3. This statement does **not** imply a logarithmic lower bound for Dahan's pair depth `max(u,a)`: the coordinate map contains the additional unbounded witness quotient `alpha`.
4. The computational records `624` through `1e8` and `816` through `1e9` are compatible with an intrinsically growing square-depth function.

## Claim boundary

This is a lower bound on the minimum **square-completion depth** of the Type-II certificate family along an infinite sequence. It is not evidence for Erdős--Straus counterexamples: those primes may and generally do have valid Type-II certificates at larger square depth, or Type-I certificates.

No novelty claim is made pending a dedicated historical and contemporary literature review.