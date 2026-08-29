# Why the Existing Fixed-Depth Sieve Theorem Does Not Yet Prove the Unit-Partner Cascade

**Status:** literature alignment / proof-gap note

Benjamin Dahan's 2026 preprint proves an unconditional fixed-depth upper bound for failures of a two-parameter, factorization-free criterion on primes `n ≡ 1 (mod 24)`.  For fixed depth `J`, the failure set has density bounded by a negative power of `log N` whose exponent grows with the finite covering used by the sieve.

This is highly relevant to the corrected project, but it does **not** immediately prove the much narrower unit-partner observation.

## Logical direction

Let

- `F_complete(J)` be the primes not solved by Dahan's complete/two-parameter search through depth `J`;
- `F_unit(J)` be the primes not solved by the unit-partner slice through the corresponding finite family of shifts.

Every unit-partner certificate is a valid complete binary certificate, but not every complete binary certificate has one divisor equal to `1`. Therefore

\[
\boxed{F_{\mathrm{complete}}(J)\subseteq F_{\mathrm{unit}}(J).}
\]

Consequently, an **upper bound** for `F_complete(J)` does not give an upper bound for `F_unit(J)`.  The narrower unit-partner failure set can be substantially larger.

A proof of the empirical unit-partner cascade therefore needs additional input specific to one of

\[
d\mid K_c,\qquad d\equiv-1\pmod c,
\]

or

\[
d\mid K_c,\qquad nd\equiv-1\pmod c.
\]

## Fixed-shift obstruction transfers

The logical implication works usefully in the opposite direction for lower bounds.  Dahan proves that at the fixed shift `c=7` there is an unconditional asymptotic set of primes for which **both branches of the complete divisor criterion fail**.  Such primes necessarily fail every unit-partner certificate at `c=7` as well.

Thus a single fixed shift cannot prove the unit-partner cascade globally.  Any successful theorem must genuinely vary the shift.

## Current proof target

The audited computation through `10^9` suggests the following much stronger finite pattern:

> For every corrected residual prime `n <= 10^9` except `2521`, some shift `c <= 299`, `c ≡ 3 (mod 4)`, has a unit-partner divisor `d|K_c` satisfying either `d ≡ -1 (mod c)` or `nd ≡ -1 (mod c)`.

To convert this into a theorem, one possible route is a sieve designed specifically for the unit-partner events.  For the untwisted branch, the generalized-shift identity

\[
n+4a=c(4ar-1)
\]

shows that the problem is a divisor-in-progression question for the shifted integers `n+4a`.  The twisted branch gives an analogous constrained divisor condition.

The existing fixed-depth sieve machinery is therefore evidence that such a program is plausible, but the transfer is not automatic and no global proof is claimed here.

Reference: Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035 (2026).
