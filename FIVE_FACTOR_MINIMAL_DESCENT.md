# Minimal Descent for Mixed-Signature Ancestry Survivors

**Status:** the descent lemma is exact; the stronger hope that every descended strong four-factor base is killed by all `1 mod 4` extensions is false.

Let

\[
m\equiv3\pmod4
\]

and suppose a unit square class

\[
r\in QR(m)
\]

survives every proper square-completed ancestor. For each proper divisor

\[
1<e<m,\qquad e\mid m,\qquad e\equiv3\pmod4,
\]

write

\[
Q_{(e+1)/4}=\{D\pmod e:D\mid((e+1)/4)^2\}.
\]

## Exact descent lemma through a 1 mod 4 prime factor

Assume

\[
p\mid m,\qquad p\equiv1\pmod4,
\]

and put

\[
d=\frac{m}{p}.
\]

Then `d == 3 (mod 4)`. Since `d` is itself a proper ancestor divisor of `m`, survival at `m` implies

\[
r\pmod d\notin Q_{(d+1)/4}.
\]

Every proper `3 mod 4` divisor of `d` is also a proper ancestor divisor of `m`, so `r mod d` avoids those sets as well.

Hence `r mod d` is a **strong survivor** at `d`: it avoids both the depth attached to `d` itself and all proper `3 mod 4` ancestors of `d`.

Thus

\[
\boxed{
\text{survivor at }m,\ p\equiv1(4),\ p\mid m
\Longrightarrow
\text{strong survivor at }m/p.
}
\]

This implication remains unconditional.

## The extension-elimination conjecture is false

The natural next hope was that no strong four-factor base could be extended by another `1 mod 4` prime while retaining an ancestry survivor. That is false.

The exact mixed-signature counterexample is

\[
\boxed{m=352495=5\cdot11\cdot13\cdot17\cdot29}
\]

with surviving unit-square class

\[
\boxed{r=224316}.
\]

Removing the `1 mod 4` factor `29` gives

\[
\boxed{d=12155=5\cdot11\cdot13\cdot17}.
\]

By the descent lemma, `r mod 12155 = 5526` is a strong survivor at `d`. Yet adjoining `29` preserves a full proper-ancestor survivor at `m`.

Therefore the statement

\[
\text{strong four-factor base}
\Longrightarrow
\text{every }1\pmod4\text{ prime extension is covered}
\]

is false.

This is a useful correction: the descent lemma narrows the search but does not terminate it.

## Finite four-factor census remains valid

In the previously audited range `d < 100000`, the exact census found only a small fraction of four-factor moduli admitting strong survivors. That concentration remains useful as finite structure. In particular, strong bases are rare relative to all four-factor `3 mod 4` moduli.

But rarity is not enough for a universal extension theorem.

## All-negative branch also admits survivors

The all-`3 mod 4` branch does not close by ancestry either. For

\[
6,407,731=11\cdot19\cdot23\cdot31\cdot43,
\]

the full proper-ancestor system leaves thousands of unit-square survivor classes. See `MODULUS_ANCESTRY_FIVE_FACTOR_CONJECTURE.md`.

Thus neither signature branch supports a factor-count closure theorem.

## Correct interpretation of descent

The exact mixed-signature descent should now be used as a **state reduction**, not a terminal contradiction.

Given a survivor `(m,r)` and a `1 mod 4` factor `p`, the reduced state

\[
(d,r\bmod d),\qquad d=m/p,
\]

belongs to the strong-survivor set. The real question is then how strong-survivor states lift under multiplication by new prime factors.

That suggests a transition graph:

\[
(d,s)\xrightarrow{\ p\ }(dp,r),
\]

where `p == 1 (mod 4)`, `r mod d = s`, `r in QR(dp)`, and `r` survives all new ancestors containing `p`.

The counterexample

\[
(12155,5526)\xrightarrow{29}(352495,224316)
\]

is the first canonical regression edge for that graph.

## Revised theorem targets

The viable questions are now:

1. characterize which strong-survivor states admit infinitely many prime extensions;
2. determine whether extension survival is controlled by finitely many congruence classes of `p`;
3. test whether every persistent ancestry survivor is nevertheless captured by a non-ancestor complete Type-II layer;
4. classify cycles or monotone invariants in the survivor-transition graph.

These targets retain the useful exact descent while avoiding the refuted factor-count closure claim.

## Claim boundary

The descent lemma is unconditional. The mixed and all-negative counterexamples refute only proposed ancestry-closure statements. They are not Erdős--Straus counterexamples and do not establish failure of complete Type II.