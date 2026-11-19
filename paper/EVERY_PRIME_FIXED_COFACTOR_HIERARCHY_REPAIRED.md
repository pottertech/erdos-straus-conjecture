# Repaired Canonical Exact-Depth Hierarchy for Every Fixed Prime Cofactor

**Status:** unconditional theorem, incorporating the `k=0` no-reuse repair. This supersedes `EVERY_PRIME_FIXED_COFACTOR_HIERARCHY.md`.

For every fixed prime `s>3`, there is an explicit witness `d_s` and a reduced prime progression for `r` such that all but finitely many prime parameters generate

\[
A=\frac{sr+1}{4}
\]

as exact square-completed Type-II depth realized by infinitely many primes.

The corrected canonical table is:

| `s mod 8` | witness `d_s` | canonical prime progression for `r` |
|---|---:|---|
| `1` | `2^{v_2(s-1)-3}(s-1)` | `r ≡ -s^{-1} (mod 4d_s)` |
| `3` | `(s+1)/2` | `r ≡ s+2 (mod 2(s+1))` |
| `5` | `s-1` | `r ≡ s-2 (mod 4(s-1))` |
| `7` | `(s-1)/2` | `r ≡ s-2 (mod 2(s-1))` |

The `s≡1 (mod 8)` row differs from the earlier draft. The naive witness `(s-1)/2` permits an unavoidable `c=1`, `E=d` reuse. The reinforced 2-adic witness shown above is the minimal canonical repair used here.

The local character and equality-free arguments are as in the four residue-class proofs. The separate note `CANONICAL_NO_REUSE_LEMMA.md` proves that the degenerate `k=0` divisor-reuse condition is impossible in all four rows. Thus every remaining collision has

\[
k,h\ge1,
\qquad
kh<dc^2,
\]

and the master exceptional-layer equation leaves only finitely many bad parameter primes.

Therefore:

> **Repaired every-prime fixed-cofactor hierarchy theorem.** For every fixed prime `s>3`, all but finitely many primes in the corresponding canonical progression above generate a depth
> \[
> \boxed{A=(sr+1)/4}
> \]
> that occurs infinitely often as exact square-completed Type-II depth.

## Corrected counting function

Define

\[
c(s)=
\begin{cases}
\dfrac{4}{s\varphi(4\cdot2^{v_2(s-1)-3}(s-1))},&s\equiv1\pmod8,\\[7pt]
\dfrac{4}{s\varphi(2(s+1))},&s\equiv3\pmod8,\\[7pt]
\dfrac{4}{s\varphi(4(s-1))},&s\equiv5\pmod8,\\[7pt]
\dfrac{4}{s\varphi(2(s-1))},&s\equiv7\pmod8.
\end{cases}
\]

Equivalently, in the `1 mod 8` row, if `e=v_2(s-1)`, then the parameter modulus is

\[
4d_s=2^{e-1}(s-1).
\]

The positive series

\[
C_{\rm all}^{\rm repaired}
=
\sum_{\substack{s>3\\s\ \mathrm{prime}}}c(s)
\]

converges. Taking `X→∞` for each fixed finite cofactor set and then the supremum gives

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge\frac83+C_{\rm all}^{\rm repaired}.
}
\]

A finite exact certificate using all prime cofactors `5<=s<=10^6` gives

\[
\begin{aligned}
C_1(10^6)&=0.006681657710714896\ldots,\\
C_3(10^6)&=0.06768134901831344\ldots,\\
C_5(10^6)&=0.12763386380907094\ldots,\\
C_7(10^6)&=0.16664452081663197\ldots.
\end{aligned}
\]

Thus

\[
\sum_{5\le s\le10^6}c(s)
=
\boxed{0.36864139135473123\ldots}
\]

and hence the rigorous finite-certificate lower bound is

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge3.0353080580213976\ldots .
}
\]

All omitted terms are positive, so the full repaired hierarchy coefficient is larger.

## Supersession notice

The numerical bound `3.0505050297...` in the pre-repair every-prime note and v8 manuscript is obsolete. It used the too-dense naive `s≡1 (mod 8)` progression. The corrected advertised finite bound is `3.0353080580...`.

## Claim boundary

This theorem concerns exact square-completed Type-II depth. It does not prove universal Type-II solvability or the Erdős--Straus conjecture, and it does not establish publication priority.