# Positive-Divisor Support Through 10^8

**Status:** exact finite computation; no global claim

The one-divisor collapse can be refined by asking for the minimum number of prime factors, counted with multiplicity, needed to build a divisor

\[
s\mid M_u=n\frac{n+u}{4}
\]

with

\[
s\equiv-1\pmod u.
\]

The search minimizes this positive support over all

\[
u=3,7,11,\ldots,299.
\]

On the 26,399 corrected residual primes below `10^8`:

| minimum positive support | count |
|---:|---:|
| 1 | 21,399 |
| 2 | 4,952 |
| 3 | 47 |
| no positive-divisor witness through `u<=299` | 1 |

Thus every one-divisor certificate in the tested range can be chosen with support at most three, and only 47 cases need support three.

The unique positive-divisor failure is again

\[
\boxed{n=2521}.
\]

It is separately solved at `u=31` by the opposite-residue pair `2+29=31`.

## Exact two-factor pigeonhole lemma

Let `u ≡ 3 (mod 4)` and suppose `gcd(M,u)=1`.  On the unit group

\[
G=(\mathbb Z/u\mathbb Z)^\times
\]

define

\[
T(r)=-r^{-1}.
\]

Because `u ≡ 3 (mod 4)`, the congruence

\[
r^2\equiv-1\pmod u
\]

has no solution, so `T` is fixed-point-free.

Let `R` be the set of distinct residue classes modulo `u` occupied by prime factors of `M`. If `R` contains both `r` and `T(r)`, then two prime factors `p,q|M` satisfy

\[
pq\equiv-1\pmod u,
\]

and their product is a one-divisor certificate.  Therefore a failure of every support-one and support-two positive certificate forces

\[
R\cap T(R)=\varnothing,
\]

hence

\[
\boxed{|R|\le \frac{\varphi(u)}2.}
\]

This is the same fixed-point-free involution mechanism used in Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035 (2026), to obtain fixed-depth sieve bounds for divisor criteria.

## Research target

The empirical problem has now been reduced to two layers:

1. prove that some gate produces more than half-group prime-residue occupancy, forcing support at most two; or
2. handle the very small exceptional occupancy patterns where a three-factor positive product reaches `-1`.

Only one tested integer, `2521`, escapes the positive-divisor route entirely through `u<=299`, and it already has an explicit signed two-factor endpoint.
