# Fixed Unit-Partner Families

**Status:** exact infinite-family identities extracted from the complete binary criterion

The unit-partner slice gives explicit arithmetic-progression families.

Let

\[
K=\frac{n+u}{4},\qquad u\equiv3\pmod4.
\]

## Untwisted fixed family

Fix positive integers `u,d` with

\[
d\equiv-1\pmod u.
\]

Whenever

\[
d\mid K,
\]

or equivalently

\[
\boxed{n\equiv-u\pmod{4d}},
\]

the unit-partner pair `(d,1)` satisfies the untwisted binary criterion.

Writing

\[
n=4dt-u,
\qquad
r=\frac{d+1}{u},
\]

one has

\[
K=dt
\]

and the explicit decomposition

\[
\boxed{
\frac4n=
\frac1{dt}
+
\frac1{n d t r}
+
\frac1{n t r}.
}
\]

This is a polynomial identity in the progression parameter `t`.

### Example: `u=7,d=13`

Since `13 == -1 (mod 7)`, every

\[
\boxed{n\equiv45\pmod{52}}
\]

is solved.  Writing `n=52t-7`, so that `K=13t` and `r=2`,

\[
\frac4n=
\frac1{13t}
+
\frac1{26nt}
+
\frac1{2nt}.
\]

### Example: `u=7,d=34`

Since `34 == -1 (mod 7)`, every

\[
\boxed{n\equiv129\pmod{136}}
\]

is solved.

## Twisted fixed family

Fix `u,d`.  The unit-partner twisted branch requires

\[
d\mid K
\]

and

\[
nd\equiv-1\pmod u.
\]

Thus `n` lies in the simultaneous congruences

\[
\boxed{n\equiv-u\pmod{4d}},
\qquad
\boxed{n\equiv-d^{-1}\pmod u},
\]

when `d` is invertible modulo `u`.

Writing `K=dt` and

\[
r=\frac{nd+1}{u},
\]

the pair `(nd,1)` gives

\[
\boxed{
\frac4n=
\frac1{dt}
+
\frac1{n d t r}
+
\frac1{t r}.
}
\]

### Example: `u=11,d=5`

The two congruences combine to

\[
\boxed{n\equiv189\pmod{220}}.
\]

Every positive integer in this progression is therefore solved by the twisted unit-partner identity.

## Most frequent fixed pairs in the corrected `n <= 10^8` residual data

The counts below are empirical frequencies of the *first unit-partner certificate returned by the current search order*; they are not disjoint mathematical density statements.

| branch | `u` | `d` | progression | observed count |
|---|---:|---:|---|---:|
| untwisted | 7 | 13 | `n == 45 (mod 52)` | 2,202 |
| untwisted | 7 | 34 | `n == 129 (mod 136)` | 1,068 |
| twisted | 11 | 5 | `n == 189 (mod 220)` | 905 |
| twisted | 11 | 9 | `n == 61 (mod 396)` | 674 |
| twisted | 7 | 17 | `n == 401 (mod 476)` | 553 |
| untwisted | 7 | 41 | `n == 157 (mod 164)` | 525 |
| untwisted | 7 | 62 | `n == 241 (mod 248)` | 502 |
| twisted | 7 | 38 | `n == 905 (mod 1064)` | 480 |
| twisted | 7 | 19 | `n == 221 (mod 532)` | 473 |
| untwisted | 11 | 87 | `n == 337 (mod 348)` | 363 |

The top 10 fixed `(branch,u,d)` families account for roughly 29% of the `10^8` unit-partner certificates returned by the current ordering.  The top 100 account for roughly 63.5%.

This does **not** imply that a finite set of polynomial congruence identities closes the conjecture.  The classical residual classes are precisely where finite congruence-cover approaches face strong obstructions.  The value of this catalog is instead to identify large unconditional subfamilies and to isolate what remains after they are removed.
