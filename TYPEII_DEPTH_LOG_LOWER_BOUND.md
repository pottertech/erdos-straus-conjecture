# Logarithmic Lower Bound for Exact Complete Type-II Square Depth

**Status:** unconditional quantitative corollary of the exact prime-modulus backbone plus Linnik's theorem; proof audited. Novelty is not established.

## 1. Why the earlier formulation needed repair

An avoidance progression of the form

\[
p\equiv1\pmod{\operatorname{lcm}(840,3,7,\ldots,4J-1)}
\]

proves that no square-completed Type-II witness occurs at depth `<=J`. It does **not**, by itself, prove that such a prime has any later Type-II witness, because universal Type-II existence remains open.

Therefore the statement

\[
\operatorname{depth}_{\rm sq}(p)>J
\]

is unconditional only if `depth_sq` is allowed to take the value `infinity`. It is not enough to establish a lower bound for a finite minimum depth.

The exact prime-modulus backbone repairs this: it simultaneously avoids every earlier layer and forces an actual hit at the target layer.

## 2. Exact-depth backbone

Let

\[
q=4k-1>7
\]

be prime. Put

\[
L_{k-1}=\operatorname{lcm}(840,3,7,11,\ldots,4k-5),
\qquad
M_k=qL_{k-1}.
\]

Since `q` is prime and exceeds every earlier layer modulus,

\[
\gcd(q,L_{k-1})=1.
\]

Choose by CRT a reduced residue `r_k mod M_k` satisfying

\[
r_k\equiv1\pmod{L_{k-1}},
\qquad
r_k\equiv-1\pmod q.
\]

For every prime

\[
p\equiv r_k\pmod{M_k},
\]

the neutral-residue lemma `1 notin S_j` eliminates every square depth `j<k`, while at depth `k` the choice `D=k` gives

\[
p+4k\equiv-1+4k=q\equiv0\pmod q.
\]

Hence

\[
\boxed{\operatorname{depth}_{\rm sq}(p)=k}.
\]

Dirichlet gives infinitely many such primes for every backbone index `k`.

## 3. Size of the CRT modulus

We only need an upper bound. Since

\[
L_{k-1}\mid 840\,\operatorname{lcm}(1,2,\ldots,4k),
\]

the standard Chebyshev/PNT estimate

\[
\log\operatorname{lcm}(1,2,\ldots,x)=\psi(x)=O(x)
\]

gives

\[
\log L_{k-1}=O(k).
\]

Also `q=4k-1`, so

\[
\log M_k
=\log q+\log L_{k-1}
=O(k).
\]

## 4. Linnik least-prime bound

Let `p_k` be the least prime in the reduced progression

\[
p\equiv r_k\pmod{M_k}.
\]

Linnik's theorem gives an absolute constant `C` such that

\[
p_k\ll M_k^C.
\]

Therefore

\[
\log p_k
\le C\log M_k+O(1)
=O(k).
\]

But the construction proves the exact identity

\[
\operatorname{depth}_{\rm sq}(p_k)=k.
\]

Consequently

\[
\boxed{
\operatorname{depth}_{\rm sq}(p_k)
\gg
\log p_k.
}
\]

There are infinitely many eligible `k`, because primes `q == 3 (mod 4)` are infinite and `k=(q+1)/4`. Distinct exact depths force the resulting `p_k` to be distinct. Thus:

### Theorem

There exists an infinite sequence of Mordell-hard primes with **finite exact** complete-Type-II square depth satisfying

\[
\boxed{
\operatorname{depth}_{\rm sq}(p)
\gg
\log p.
}
\]

This is stronger than a bare avoidance statement: every prime in the constructed sequence has an explicitly guaranteed Type-II first hit at the stated depth.

## 5. Consequences

1. Logarithmic-scale **finite square depth** is genuinely necessary along an infinite sequence.
2. Any universal procedure restricted to square-completion depth `o(log p)` misses infinitely many primes that nevertheless have a complete Type-II witness.
3. This avoids the logical ambiguity between `depth > J` and `depth = infinity`.
4. The statement concerns square-completion depth only. It does **not** imply a lower bound of this size for Dahan's pair depth `max(u,a)`, because the square coordinate includes the additional factor `alpha`.

## 6. Priority boundary

The underlying square-completed exact-depth backbone is prior art: FCF/CENTL publicly recorded it on 2026-08-15.

A targeted search on 2026-08-29 did not locate this specific quantitative combination of that backbone with Linnik's theorem to obtain an infinite exact-depth sequence satisfying

\[
\operatorname{depth}_{\rm sq}(p)\gg\log p.
\]

That search is not sufficient to establish novelty. The result should therefore be described as an **unconditional quantitative corollary derived here, with novelty unclaimed pending publication-grade prior-art review**.

No Erdős--Straus counterexample or universal Type-II theorem is implied.