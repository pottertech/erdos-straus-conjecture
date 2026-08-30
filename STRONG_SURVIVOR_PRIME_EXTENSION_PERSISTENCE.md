# Strong-Survivor Prime-Extension Persistence

**Status:** unconditional theorem about the proper-ancestor shadow system. It is not a Type-II universality theorem and makes no novelty claim pending a dedicated literature comparison.

## Setup

Let

\[
d\equiv3\pmod4
\]

be odd, and let `s mod d` be a **strong unit-square survivor**, meaning:

1. `s` is a unit square modulo `d`;
2. for every divisor
   \[
   e\mid d,\qquad e\equiv3\pmod4,
   \]
   including `e=d`,
   \[
   s\pmod e\notin Q_{(e+1)/4},
   \]
   where
   \[
   Q_B=\{D\pmod{4B-1}:D\mid B^2\}.
   \]

Fix a prime

\[
p\equiv1\pmod4,
\qquad p\nmid d,
\]

and put

\[
m=dp.
\]

We ask whether `s` can be lifted to a unit-square class `r mod m` that is itself strong at `m`.

## Theorem

For every fixed strong survivor `(d,s)`, **all sufficiently large primes**

\[
p\equiv1\pmod4,
\qquad p\nmid d,
\]

admit a strong survivor lift `r mod dp` satisfying

\[
r\equiv s\pmod d.
\]

Equivalently, strong ancestry-survivor states persist under every sufficiently large new `1 mod 4` prime extension.

## Proof

Choose a nonzero quadratic residue

\[
y\in QR(p).
\]

By CRT there is a unique class

\[
r\pmod{dp}
\]

with

\[
r\equiv s\pmod d,
\qquad
r\equiv y\pmod p.
\]

Because `s` is a unit square modulo `d` and `y` is a nonzero square modulo `p`, `r` is a unit square modulo `dp`.

We must avoid every `3 mod 4` divisor of `dp`, including `dp` itself.

### Old divisors

If

\[
e\mid d,
\qquad e\equiv3\pmod4,
\]

then

\[
r\equiv s\pmod e,
\]

so the strong-survivor hypothesis at `d` already gives

\[
r\pmod e\notin Q_{(e+1)/4}.
\]

Thus only divisors containing the new prime `p` require attention.

### New divisors

Every new `3 mod 4` divisor has the form

\[
e=pt,
\]

where

\[
t\mid d,
\qquad t\equiv3\pmod4.
\]

For strong survival at `dp`, allow also `t=d`, which corresponds to `e=dp` itself.

For fixed `t`, put

\[
B_{p,t}=\frac{pt+1}{4}.
\]

The lift is bad at `e=pt` only if there exists a divisor

\[
D\mid B_{p,t}^2
\]

such that

\[
r\equiv D\pmod{pt}.
\]

Reducing modulo `p`, this forces

\[
y\equiv D\pmod p.
\]

Therefore the number of quadratic-residue choices `y mod p` that can be bad because of this particular `t` is at most

\[
\tau(B_{p,t}^2),
\]

where `tau` is the divisor function. This is an upper bound because different divisors may yield the same residue modulo `p`, and some divisor residues may not be quadratic residues at all.

Let

\[
T_d=\{t:t\mid d,\ t\equiv3\pmod4\}.
\]

The total number of forbidden quadratic-residue choices is therefore at most

\[
\sum_{t\in T_d}\tau(B_{p,t}^2).
\]

The set `T_d` is fixed because `d` is fixed. Also

\[
B_{p,t}\ll_d p.
\]

By the standard divisor bound

\[
\tau(n)=n^{o(1)},
\]

uniformly as `n -> infinity`, we obtain

\[
\sum_{t\in T_d}\tau(B_{p,t}^2)=p^{o(1)}.
\]

On the other hand, the number of nonzero quadratic residues modulo the prime `p` is exactly

\[
\frac{p-1}{2}.
\]

Hence, for all sufficiently large such primes,

\[
\sum_{t\in T_d}\tau(B_{p,t}^2)
<
\frac{p-1}{2}.
\]

So at least one quadratic residue `y mod p` avoids every new ancestor and the new full layer `dp`. The corresponding CRT lift `r mod dp` is a strong survivor.

This proves the theorem.

## Corollary: arbitrarily high factor complexity

Suppose at least one strong survivor exists. Then strong survivors exist at moduli with arbitrarily many distinct prime factors.

Indeed, starting from `(d_0,s_0)`, choose a sufficiently large new prime

\[
p_1\equiv1\pmod4
\]

and lift to a strong survivor `(d_1,s_1)` with `d_1=d_0p_1`. Apply the theorem again to `(d_1,s_1)`, choose a new sufficiently large `p_2 == 1 (mod 4)`, and continue inductively.

Thus

\[
\boxed{
\text{there is no universal factor-count threshold that forces proper-ancestor coverage.}
\]

## Exact Type-II interpretation

This point is essential.

A strong survivor `(m,r)` is **not** a denominator-prime state that evades Type II. Instead, it is a square class at the depth

\[
A=\frac{m+1}{4}
\]

that is not inherited from any divisor-modulus ancestor.

Whenever an actual divisor `D|A^2` satisfies

\[
D\equiv r\pmod m,
\]

the progression

\[
\boxed{n\equiv-4D\equiv-4r\pmod m}
\]

is a valid square-completed Type-II progression at depth `A`.

Thus ancestry survival means **primitive rescue relative to the divisor-modulus ancestry system**, not failure of complete Type II.

For the semiprime mixed-square application, the relevant survivor classes are represented by actual divisors `D=u^2` or `v^2`, so they directly generate valid Type-II rescue progressions.

The prime-extension theorem therefore says that the ancestry geometry continues to produce non-inherited square classes at arbitrarily complicated moduli. It does **not** say that denominator primes become increasingly Type-II-resistant.

## Explicit seed and regression edge

The exact mixed-signature counterexample

\[
m=352495=12155\cdot29
\]

with survivor

\[
r=224316
\]

descends to the strong state

\[
\boxed{(d,s)=(12155,5526)}.
\]

A direct finite check found that every prime

\[
p<1000,
\qquad p\equiv1\pmod4,
\qquad p\nmid12155,
\]

admits at least one survivor lift of this fixed state; there are 77 such primes. This finite observation is consistent with, but not needed for, the theorem.

## Strategic consequence

Proper-ancestor inheritance is a **compression mechanism**, not a terminal solvability mechanism.

- inherited square classes can be removed from the list of genuinely new depth contributions;
- strong survivors identify primitive residue geometry that survives that compression;
- persistent towers show that new primitive geometry continues to appear at arbitrarily high factor complexity;
- none of this, by itself, identifies denominator primes that evade complete Type II.

The next meaningful question is therefore different:

> For a primitive square-completed progression at depth `A`, how much of that progression has already been solved by unrelated earlier depths whose moduli do not divide `4A-1`?

That is a global first-hit / cross-modulus problem rather than an ancestry problem.

## Literature / priority note

The FCF/CENTL program contains closely related square-lift, prime-extension-shadow, and survivor-tower machinery. A web audit located those neighboring frameworks but did not establish whether the exact divisor-function persistence theorem above is already present there or elsewhere. No novelty claim should be made without a file-by-file priority comparison.

## Claim boundary

This theorem concerns the internal square-completed **ancestor-shadow system**. It neither proves nor disproves the Erdős--Straus conjecture. Its correct interpretation is that proper ancestry alone does not exhaust the primitive square-completed residue geometry.