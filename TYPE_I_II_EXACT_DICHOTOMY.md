# Exact Type-I / Type-II Dichotomy in Shift Coordinates

**Status:** exact algebraic identification with the classical Elsholtz--Tao / Pomerance--Weingartner Type-I/Type-II criteria, as restated by Dahan (2026). No novelty claim for the classical criteria.

This note puts the repository's corrected fixed-shift binary criterion into the standard Type-I/Type-II language and identifies the parameters exactly.

Throughout let `n` be prime, let

\[
c\equiv3\pmod4,
\qquad
K=\frac{n+c}{4},
\]

and assume the ordinary admissible-shift conditions under which `gcd(n,K)=1`.

The complete centered binary criterion asks for coprime positive factors `A,B` with

\[
AB\mid nK,
\qquad
A+B\equiv0\pmod c.
\]

Because `n` is prime and `gcd(n,K)=1`, this splits into exactly two branches depending on whether neither or one of the binary factors carries the prime `n`.

---

## 1. Type II: untwisted binary branch

Suppose neither factor contains `n`. Write

\[
A=a,
\qquad
B=b,
\qquad
K=abq.
\]

Then the binary congruence is

\[
\boxed{c\mid a+b}.
\]

Since

\[
4K=n+c,
\]

we also have

\[
\boxed{4ab\mid n+c}.
\]

Thus the fixed-shift untwisted branch is exactly the classical Type-II criterion

\[
\boxed{
 c\mid a+b,
 \qquad
 4ab\mid n+c.
}
\]

Conversely, these two divisibilities give

\[
q=\frac{n+c}{4ab},
\qquad
r=\frac{a+b}{c},
\]

and the explicit Type-II decomposition

\[
\boxed{x=abq},
\qquad
\boxed{y=anqr},
\qquad
\boxed{z=bnqr}.
\]

This is exactly the binary-sum family documented in `BINARY_SUM_TYPEII_EQUIVALENCE.md`.

### Type-II unit-partner slice

Setting one binary partner equal to `1`, say `a=1`, gives

\[
\boxed{b\equiv-1\pmod c},
\qquad
b\mid K.
\]

This is the repository's ordinary untwisted/cofactor unit-partner branch.

---

## 2. Type I: twisted binary branch

Suppose exactly one binary factor contains the prime `n`. Write

\[
A=na,
\qquad
B=b,
\qquad
K=abq.
\]

The complete binary congruence becomes

\[
\boxed{c\mid na+b}.
\]

Write

\[
na+b=cr
\]

with `r>0`. Since

\[
c=4abq-n,
\]

we obtain

\[
na+b=r(4abq-n),
\]

hence

\[
n(a+r)=b(4aqr-1). \tag{1}
\]

Because `b | K` and `gcd(n,K)=1`, the prime `n` does not divide `b`. Therefore (1) implies

\[
n\mid4aqr-1.
\]

Write

\[
4aqr-1=nf.
\]

Then (1) gives

\[
a+r=bf.
\]

Eliminating `r=bf-a` from the first equation yields

\[
4aq(bf-a)-1=nf,
\]

so

\[
f(4aqb-n)=4a^2q+1.
\]

But

\[
4aqb-n=4K-n=c.
\]

Therefore

\[
\boxed{cf=4a^2q+1},
\]

and hence

\[
\boxed{c\mid4a^2q+1}.
\]

Also `K=abq` gives

\[
\boxed{4aq\mid n+c},
\]

because

\[
\frac{n+c}{4aq}=b.
\]

Thus the complete twisted branch is exactly

\[
\boxed{
 c\mid4a^2q+1,
 \qquad
 4aq\mid n+c.
}
\]

This is precisely the standard Pomerance--Weingartner / Dahan Type-I closed criterion after identifying their parameters with

\[
 u=a,
 \qquad d=q,
 \qquad f=c.
\]

The divisor called `f` in that criterion is therefore literally the repository's shift `c`.

### Converse

Suppose positive integers `a,q,c` satisfy

\[
c\mid4a^2q+1
\]

and

\[
4aq\mid n+c.
\]

Define

\[
b=\frac{n+c}{4aq},
\qquad
f=\frac{4a^2q+1}{c}.
\]

Then `K=abq`. Set

\[
r=bf-a.
\]

A direct calculation gives

\[
cr=na+b.
\]

Thus

\[
c\mid na+b,
\]

so the twisted fixed-shift binary criterion holds.

The corresponding explicit denominators can be taken as

\[
\boxed{x=abq},
\qquad
\boxed{y=naqr},
\qquad
\boxed{z=bqr}.
\]

Exactly one of `y,z` carries the prime `n`, giving the Type-I shape.

### Type-I unit-partner slice

Setting the non-`n` binary partner equal to `1`, i.e. `b=1`, gives

\[
K=aq
\]

and

\[
\boxed{na+1\equiv0\pmod c}.
\]

This is the repository's twisted unit-partner branch.

---

## 3. The complete two-branch criterion

For a prime `n` and an admissible shift `c`, the complete binary criterion is therefore equivalent to the disjunction

### Type II

\[
\boxed{
\exists a,b>0:
\quad c\mid a+b,
\quad4ab\mid n+c.
}
\]

### Type I

\[
\boxed{
\exists a,q>0:
\quad c\mid4a^2q+1,
\quad4aq\mid n+c.
}
\]

This is the cleanest exact formulation of the repository's current endgame.

---

## 4. What the finite 10^9 certificate counts do -- and do not -- say

The audited corrected residual population through `n <= 10^9` contains `195,271` primes.

The first unit-partner certificates chosen by the current bounded cascade split as:

- `111,002` untwisted/unit-partner certificates -- therefore explicitly Type II;
- `84,268` twisted/unit-partner certificates -- therefore explicitly Type I;
- `1` bounded unit-partner failure, `n=2521`, rescued by a non-unit Type-II pair `(a,b)=(2,29)` at `c=31`.

These counts classify the **certificates selected by the current search**, not the intrinsic solution type of each `n`. A prime first found on the Type-I branch may also possess a Type-II solution at another shift, and a permanent failure of the Type-II unit-partner slice does not imply failure of full Type II.

### n = 66529 demonstrates the distinction

The earlier unit-partner stratification identified

\[
n=66529
\]

as a permanent failure of the **untwisted unit-partner** slice. It is also found very cheaply by the Type-I unit-partner branch at

\[
c=19,
\quad a=131,
\quad q=127,
\quad b=1.
\]

However, `66529` also has a small non-unit Type-II solution. Take

\[
q=2,
\qquad r=1,
\qquad a=5,
\qquad b=1706,
\qquad c=a+b=1711.
\]

Then

\[
4abq=4\cdot5\cdot1706\cdot2=68240=n+c.
\]

Equivalently,

\[
4qn+1=532233=39\cdot13647,
\]

with

\[
39\equiv13647\equiv-1\pmod8.
\]

The resulting Type-II denominators are

\[
\boxed{x=17060},
\qquad
\boxed{y=665290},
\qquad
\boxed{z=226996948}.
\]

Thus `66529` is a decisive warning against identifying an all-shift **unit-partner** exception with a Type-II exception.

### n = 2521

The case

\[
n=2521
\]

is a permanent failure of both bounded unit-partner slices in the audited cascade, but full non-unit Type II succeeds with

\[
c=31,
\quad a=2,
\quad b=29,
\quad q=11.
\]

---

## 5. Four-cell proof hierarchy

The exact dichotomy exposes four natural levels:

| branch | unit partner | non-unit |
|---|---|---|
| Type II | `a=1` or `b=1` | `a,b>1` |
| Type I | `b=1` after orienting the `n`-factor | `a,b>1` in fixed-shift form |

The audited `10^9` population is closed using certificates from only the first three cells:

1. Type-II unit partner;
2. Type-I unit partner;
3. non-unit Type II (`2521` in the selected closure certificate set).

This statement is about one successful certificate per prime. It does **not** assert that the three cells are disjoint, nor that a prime found in the Type-I cell lacks a Type-II certificate.

No audited residual prime through `10^9` needs the fourth cell, non-unit Type I, in order to obtain some solution under the current certificate selection.

This is finite evidence only. A global proof cannot simply discard the fourth cell without a theorem showing that the first three always suffice.

---

## 6. Revised research target

The most precise current theorem target is:

> Prove that every prime in the classical residual Erdős--Straus core satisfies at least one of:
>
> 1. a Type-II unit-partner criterion;
> 2. a Type-I unit-partner criterion;
> 3. the full Type-II criterion.

If that statement is false, characterize the residual set that genuinely requires non-unit Type I.

A useful immediate subproblem is to measure full Type-II coverage independently of the unit-partner cascade. The `66529` example shows that this can be substantially larger than the Type-II unit-partner coverage.

This formulation is preferable to an undifferentiated divisor-distribution conjecture because every branch is exact, constructive, and tied directly to the complete classical Type-I/Type-II dichotomy.

## 7. Literature / priority note

The Type-I and Type-II closed criteria are classical in the modern literature, especially Elsholtz--Tao and Pomerance--Weingartner, and are restated and algorithmically developed by Benjamin Dahan (2026). The algebra above records the exact variable map to the repository's centered fixed-shift criterion. No priority claim is made for the solvability criteria themselves.
