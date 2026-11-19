# Unit-Partner Slice of the Complete Binary Criterion

**Status:** exact identification with the classical/complete fixed-shift binary criterion; finite computation through `10^8`

For prime `n`, fix a shift

\[
c\equiv3\pmod4,
\qquad
K=\frac{n+c}{4}.
\]

Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035 (2026), Theorem 2.6 and Corollary 2.7, records the complete fixed-shift binary criterion:

- **untwisted branch:** coprime `d1,d2 | K` with
  \[
  d_1+d_2\equiv0\pmod c;
  \]
- **twisted branch:** divisors `d1,d2 | K`, with the stated coprimality, satisfying
  \[
  n d_1+d_2\equiv0\pmod c.
  \]

The one-divisor criterion found in the corrected computation is exactly the special slice in which one member of the divisor pair equals `1`.

## Untwisted unit-partner slice

Take `d2=1`.  The condition becomes

\[
\boxed{d+1\equiv0\pmod c},
\qquad d\mid K.
\]

Equivalently,

\[
d\equiv-1\pmod c.
\]

This is the `s=d` branch of `one_divisor_miner.py`.

## Twisted unit-partner slice

Again take the second divisor equal to `1`.  The condition becomes

\[
\boxed{nd+1\equiv0\pmod c},
\qquad d\mid K.
\]

Equivalently, the divisor `s=nd` of `nK` satisfies

\[
s\equiv-1\pmod c.
\]

This is the `s=n*d` branch of `one_divisor_miner.py`.

Thus the compact condition

\[
\boxed{\exists s\mid nK:\ s\equiv-1\pmod c}
\]

is exactly the union of the two **unit-partner** slices of the complete binary criterion.

## Corrected finite result through 10^8

On the 26,399 primes below `10^8` surviving the corrected classical-core, hard-gate, and shift reductions:

- **26,398** admit a unit-partner certificate for some `c <= 299`, `c ≡ 3 (mod 4)`;
- **0** reconstructed unit-partner certificates fail the original Erdős--Straus identity;
- the unique exception is
  \[
  \boxed{n=2521}.
  \]

For `2521`, the complete binary criterion succeeds at `c=31` with

\[
K=638=2\cdot11\cdot29,
\qquad
2+29=31,
\]

so this is a genuinely non-unit-partner untwisted certificate.

## Interpretation

The strongest finite statement is therefore not merely that support at most two suffices.  It is:

> **Unit-Partner Cascade Observation.** Through `10^8`, every corrected residual prime except the explicitly solved `2521` has a fixed-shift binary certificate in which one of the two coprime divisors is `1`.

This places the computation directly inside an established complete criterion and makes the open target much narrower.

A global theorem would need to show that, after classical reductions and perhaps finitely many explicit exceptions, some admissible shift `c` always has either

\[
d\mid K_c,\ d\equiv-1\pmod c,
\]

or

\[
d\mid K_c,\ nd\equiv-1\pmod c.
\]

Dahan proves that a *single fixed shift* cannot leave only finitely many failures (in particular at `c=7` there is an unconditional two-sided blind set), so any proof of this unit-partner cascade must genuinely vary the shift.

No novelty claim is made for the binary criterion itself; the contribution here is the corrected finite observation that its unit-partner slice alone captures all but one residual prime through `10^8`.
