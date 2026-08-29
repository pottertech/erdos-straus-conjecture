# Literature Alignment: Type A, Shift-Divisor, and Cofactor Layers

**Status:** terminology / priority audit

This repository's untwisted unit-partner branch is not a new characterization. It should be aligned explicitly with the recent literature before publication.

## 1. Fixed-shift Type A

At a fixed admissible shift `c`, put

\[
K_c=\frac{n+c}{4}.
\]

The untwisted unit-partner condition is

\[
\exists d\mid K_c:
\qquad
1+d\equiv0\pmod c.
\]

Benjamin Dahan, arXiv:2608.24035 (2026), Proposition 5.4, identifies exactly this restriction `d_1=1`, `d_2=d` of his fixed-shift divisor criterion with Lopez's **Type A** condition.

Therefore throughout future papers we should write:

> untwisted unit-partner = Lopez Type A / unit-partner slice of the untwisted fixed-shift divisor criterion.

No novelty should be claimed for the criterion itself.

## 2. Cofactor-layer parameter

Given a Type-A witness, write

\[
K_c=a d.
\]

Here

\[
a=K_c/d
\]

is the **complementary cofactor** used in this repository's `a`-layer analysis.

This must not be confused with Dahan's fixed-shift modulator

\[
a_{\mathrm{Dahan}}=\frac{1+d}{c},
\]

which is the quantity called `r` in the unit-partner notes here.

Thus the finite observation

\[
\text{minimum cofactor }a\le143
\]

through the corrected `10^8` residual population is a different depth statistic from Dahan's two-parameter search depth.

## 3. Shift-divisor form

Eliminating the fixed shift from Type A yields the exact equivalent condition

\[
\boxed{
\exists \alpha,q>0:
\quad
q\mid n+4\alpha,
\qquad
q\equiv-1\pmod{4\alpha}.
}
\]

This is the same shift-divisor family that appears in recent ED2-style formalizations as the `s=1` slice of the divisor-adaptive family.

A recent Lean repository by Suro-One/Auro Zera contains the machine-checked theorem `ES_of_shift_divisor` with exactly this hypothesis and explicitly records the rigidity contrapositive: a counterexample would have to avoid such a divisor for every `alpha`.

Therefore the algebraic shift-divisor family itself is not new.

## 4. What this repository adds empirically / organizationally

The current work contributes a different organization and audit trail:

1. derives the shift-divisor condition from the corrected centered/binary criterion;
2. proves the all-shift finite identity
   \[
   (4\alpha d-n)(4\alpha r-1)=n+4\alpha;
   \]
3. proves the finite cofactor bound
   \[
   \alpha\le\lfloor(n+3)/8\rfloor;
   \]
4. measures the **minimum complementary-cofactor depth** on the corrected classical residual population;
5. finds that through `10^8`, every non-permanent untwisted case has minimum cofactor at most `143`;
6. separates permanent Type-A failures (`2521`, `66529` in the corrected residual population examined) from mere shallow-window failures;
7. connects those failures to the twisted unit-partner and complete binary layers.

These are the claims that should be evaluated for novelty, rather than the underlying Type-A / shift-divisor criterion.

## 5. Permanent examples

The values

\[
2521,\qquad66529
\]

have also appeared previously in recent computational/formal work as exceptional values for the simplest single-divisor/shift-divisor slice. They must not be advertised as newly discovered numbers.

Our contribution is the exact classification within the present corrected cascade:

- `66529` is permanently untwisted/Type-A exceptional but has a twisted unit-partner certificate;
- `2521` is permanently exceptional to both unit-partner branches and needs a non-unit complete binary pair.

## 6. Dahan's growing-depth theorem

Dahan's Theorem 4.17 already proves a growing-depth result for his broader two-parameter Type-II criterion. For

\[
J=(\log N)^\lambda,
\]

he obtains

\[
|E_2(N;J)|
\ll
N\exp\!\left(-\left(\frac{3}{2\pi^2}\lambda^2+o(1)\right)(\log\log N)^3\right).
\]

This does **not** imply the same bound for the Type-A/cofactor-layer slice, which is narrower and uses different parameters. Future work should compare the two search spaces explicitly rather than treating one theorem as a corollary of the other.

## Publication rule

Any manuscript based on this repository should distinguish clearly between:

- known criteria / parametrizations;
- new equivalences or reorganizations;
- finite computational observations;
- genuinely new proved analytic statements.

In particular, phrases such as "new criterion" should not be used for the Type-A, shift-divisor, or complete fixed-shift binary criteria without a separate priority review.