# Unit-Partner Depth Analysis

**Status:** exact finite computation on the corrected residual population through `10^7`; interpretation note

The unit-partner cascade is extremely shallow in the shift parameter `u`, but it is not shallow in the quotient/cofactor

\[
a=K/d,\qquad K=\frac{n+u}{4}.
\]

This matters because recent fixed-depth sieve results bound *both* search parameters. The observed `u <= 299` phenomenon is therefore not the same statement as bounded two-parameter search depth.

## Corrected population through `10^7`

After the six classical mod-840 classes, corrected hard gate, and exact `n+1` / `n+4` shift reductions:

- residual primes: **3,649**;
- unit-partner failures with `u <= 299`: **1** (`n=2521`);
- unit-partner certificates: **3,648**.

For each certificate, let `d|K` be the first unit-partner divisor found and define `a=K/d`.

## Cofactor distribution

Among the 3,648 certificates:

- median `a`: **4,196**;
- 75th percentile: **19,263**;
- 90th percentile: **52,791**;
- 95th percentile: **95,744**;
- 99th percentile: **178,148**;
- 99.9th percentile: **340,644**;
- maximum: **1,085,959**.

Only:

- 188 certificates have `a <= 10`;
- 617 have `a <= 100`;
- 1,167 have `a <= 1,000`.

Thus most of the observed unit-partner coverage does **not** come from a bounded cofactor parameter.

## Consequence for the proof strategy

Benjamin Dahan's 2026 fixed-depth sieve controls a two-parameter search with both parameters bounded by a fixed depth `J`. That theorem cannot simply be read as a theorem about this unit-partner cascade, because our empirical strength is of a different form:

\[
\boxed{u\ \text{small, while }a\text{ may grow substantially with }n.}
\]

A useful analytic target is therefore a **one-sided-depth sieve**:

> for a fixed finite set of small shifts `u`, allow the complementary parameter `a` (or equivalently the divisor `d`) to vary through its full natural range and bound the primes for which neither unit-partner branch occurs.

This is narrower than the complete binary criterion but deeper in the unbounded divisor direction. It is the analytic statement most directly suggested by the verified `10^9` data.
