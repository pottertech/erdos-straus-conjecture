# Universal Prime Ancestors in the Square-Completed Ancestry System

**Status:** exact theorem. This is a structural pruning lemma for the modulus-ancestry program; it is not a proof of the Erdős--Straus conjecture.

Let

\[
p\equiv3\pmod4
\]

be prime and put

\[
B=\frac{p+1}{4}.
\]

Recall

\[
Q_B=\{D\pmod p:D\mid B^2\},
\]

while the unit square classes modulo `p` form the subgroup `QR(p)` of cardinality

\[
|QR(p)|=\frac{p-1}{2}=2B-1.
\]

We call `p` a **universal prime ancestor** when

\[
Q_B\supseteq QR(p).
\]

## Theorem

The only universal prime ancestors are

\[
\boxed{p=3\text{ and }p=7.}
\]

### Proof for p = 3 and p = 7

For `p=3`, `B=1`, hence

\[
Q_1=\{1\}=QR(3).
\]

For `p=7`, `B=2`, and the divisors of `B^2=4` are `1,2,4`, so

\[
Q_2=\{1,2,4\}=QR(7).
\]

Thus `3` and `7` are universal.

### No larger prime can be universal

Assume now `p>7`. Then `B>=3`.

Every divisor of `B^2` smaller than `B` is a proper divisor of `B^2`, and divisors of the square `B^2` pair around the central divisor `B`. More simply, for any positive integer `N`, the number of divisors of `N^2` is

\[
\tau(N^2)=2L+1,
\]

where `L` is the number of divisors of `N^2` strictly below `N`.

Any divisor `d<N` of `N^2` satisfies `d<=N^2/(2N)=N/2` whenever its complementary divisor `N^2/d` is strictly greater than `N`; equivalently, the below-`N` divisors inject into integers `1,...,\lfloor N/2\rfloor`. Hence

\[
\tau(N^2)\le 2\lfloor N/2\rfloor+1.
\]

For `N=B>=3`, this gives

\[
\tau(B^2)\le 2\lfloor B/2\rfloor+1<2B-1.
\]

Since reduction modulo `p` cannot create more residue classes than there are divisors,

\[
|Q_B|\le\tau(B^2)<2B-1=|QR(p)|.
\]

Therefore `Q_B` cannot contain every quadratic residue modulo `p`.

So no prime `p>7`, `p==3 (mod 4)`, is universal.

## Corollary: immediate pruning of survivor moduli

Let

\[
m\equiv3\pmod4
\]

be composite. If `3|m`, then the proper ancestor `d=3` already covers every unit square class of `m` after reduction modulo `3`. Likewise, if `7|m`, the ancestor `d=7` covers every unit square class after reduction modulo `7`.

Hence any modulus admitting a proper-ancestor survivor must satisfy

\[
\boxed{\gcd(m,21)=1.}
\]

In particular, every strong-survivor base in `FIVE_FACTOR_MINIMAL_DESCENT.md` must avoid both `3` and `7`. This is now a theorem rather than an empirical feature of the finite census.

## Why the theorem matters

The five-factor ancestry conjecture can therefore be restricted at once to moduli whose prime factors are all at least `5` and avoid `7`, with every `3 mod 4` factor at least `11`.

The result also shows that the ancestry proof cannot be reduced to a single larger prime ancestor: for every prime `p>=11`, the local set `Q_{(p+1)/4}` is too small to cover `QR(p)` by itself. Any proof beyond the `3` and `7` cases must use the simultaneous overlap of several proper ancestors, exactly as suggested by the current CRT/ancestry-lattice program.

## Claim boundary

This theorem classifies universal **prime** ancestors only. Composite ancestors can have much richer `Q_B` sets and their overlaps are the unresolved mechanism in the five-factor cover conjecture.