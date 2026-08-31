# Repair of the Fixed-Cofactor Finite-Exception Theorem: the `k=0` Case

**Status:** correction to the fixed-cofactor proof schema. This note supersedes any argument that treated `kh<dc^2` with merely nonnegative `k,h` as a finite set.

## 1. The gap

The master exceptional-layer equation is

\[
r(kh-dc^2)+k+dh-2dc=0,
\]

with

\[
16d\mid rh+1.
\]

AM--GM shows that, outside the equality configuration,

\[
kh<dc^2.
\]

However this product bound is finite only when

\[
\boxed{k\ge1,\qquad h\ge1.}
\]

The second inequality is automatic: from

\[
16dF=rh+1
\]

with positive integers `d,F`, the left side is at least `16`, so `h=0` is impossible for positive prime `r`.

But `k=0` is possible in principle. It means

\[
\boxed{E=d.}
\]

Thus the earlier layer is reusing the target divisor itself.

Any previous proof that concluded finiteness from `kh<dc^2` without separately excluding `k=0` is incomplete.

## 2. A canonical square-safe choice

In the single-nonsquare-coordinate construction, preserve the target residue on the target primes `s,r` and choose

\[
\boxed{n\equiv1}
\]

on every other prime-power coordinate.

Consider an exceptional earlier modulus

\[
4B-1=cr,
\qquad c<s.
\]

If `k=0`, then `E=d`. Such an `E` can be a trap divisor only if

\[
\boxed{d\mid B^2.}
\]

For the collision also to match the chosen square-safe coordinate modulo `c`, we need

\[
1\equiv-4d\pmod c,
\]

that is

\[
\boxed{c\mid4d+1.}
\]

Hence the degenerate `k=0` collision is excluded provided the following finite condition holds for every exceptional cofactor:

\[
\boxed{
\neg\left(d\mid B_c^2\ \text{ and }\ c\mid4d+1\right),
\qquad
B_c=\frac{c\alpha+1}{4},
}
\]

where `alpha` is the fixed parameter residue modulo `4d`. Changing the prime parameter by a multiple of `4d` changes `B` by a multiple of `cd`, so `B mod d`, and therefore the truth of `d|B^2`, is constant on the parameter progression.

For `c=1`, the congruence condition modulo `c` is vacuous, so the no-reuse condition simply requires

\[
\boxed{d\nmid B_1^2.}
\]

## 3. Repaired finite-exception theorem

A fixed-cofactor progression is now required to satisfy four ingredients:

1. local target square/non-square character conditions giving one nonsquare variable coordinate;
2. exclusion of the AM--GM equality configuration;
3. the finite **no-reuse condition** above for every exceptional cofactor `c`;
4. the usual reducedness conditions for the CRT progression.

Under these hypotheses, every actual collision has

\[
k\ge1,
\qquad h\ge1,
\qquad kh<dc^2.
\]

Thus

\[
1\le k<dc^2,
\qquad
1\le h<dc^2,
\]

and only finitely many pairs remain. Each pair determines at most one rational parameter

\[
r=\frac{k+dh-2dc}{dc^2-kh}.
\]

Therefore each fixed exceptional cofactor contributes only finitely many prime collision parameters. Removing their finite union and applying Dirichlet gives the exact-depth family.

> **Repaired fixed-cofactor theorem.** The finite-exception conclusion is valid when the equality-free hypotheses are supplemented by the finite no-reuse test
> \[
> \neg(d\mid B_c^2\ \&\ c\mid4d+1)
> \]
> for every exceptional cofactor `c` (with the evident `c=1` interpretation).

## 4. Consequence for the proposed canonical all-prime hierarchy

The previously proposed universal statement for **every** fixed prime cofactor requires a symbolic proof of this no-reuse condition. That proof has not yet been established.

Accordingly:

- the unrestricted all-prime hierarchy should **not** currently be advertised as a theorem;
- it remains a strong theorem-mining conjecture;
- any fixed cofactor for which the no-reuse condition is checked exactly is covered by the repaired theorem.

## 5. Finite certification through one million

An exact audit of the canonical candidate data for every prime cofactor

\[
5\le s\le10^6
\]

checked all divisors `c<s` of `4d+1` in the required residue class and tested the exact condition `d|B_c^2`.

Across all

\[
\boxed{78,496}
\]

prime cofactors in this range, the number of no-reuse failures was

\[
\boxed{0.}
\]

Thus, after the other local/equality hypotheses are verified by the displayed residue formulas, each of these finitely many fixed cofactors satisfies the repaired theorem.

This preserves a rigorous **computationally assisted** finite-cofactor spectrum lower bound, while the extension to every prime fixed cofactor remains pending a symbolic no-reuse lemma.

## Claim boundary

This correction strengthens the publication package by removing an implicit positivity assumption. Do not use `EVERY_PRIME_FIXED_COFACTOR_HIERARCHY.md` or the corresponding v8 manuscript statement as an unconditional theorem until the universal no-reuse step is proved or the manuscript is revised to the certified finite-cofactor formulation.