# Complete Square-Completed Type-II Audit Through 10^9

**Status:** exact finite computation. This is not a proof of the Erdős--Straus conjecture.

## Result

On every prime

\[
n\le10^9
\]

in the six classical residual classes modulo `840`, the complete square-completed prime Type-II criterion succeeds with

\[
\boxed{A\le816.}
\]

The audited population contains

\[
\boxed{1,587,581}
\]

primes.

Results:

- certificates: `1,587,581`;
- failures: `0`;
- bad reconstructions: `0`;
- maximum minimum square-completion depth: `816`.

The machine-readable summary is `square_completed_typeII_1B_summary.json`.

## The unique new depth record

The previous `10^8` audit had maximum minimum depth

\[
A=624
\]

at

\[
n=2,031,121.
\]

Extending to `10^9`, exactly one prime is not covered by `A<=624`:

\[
\boxed{n=605,531,161.}
\]

Its first square-completed Type-II certificate occurs at

\[
\boxed{A=816,\qquad D=16.}
\]

Since

\[
4A-1=3263,
\]

we have

\[
605,531,161+4\cdot16
=605,531,225
=3263\cdot185,575.
\]

Thus

\[
4A-1\mid n+4D.
\]

Also

\[
D=16\mid816^2.
\]

## Recovered Dahan coordinates

For

\[
A=816,\qquad D=16,
\]

put

\[
E=\frac{A^2}{D}=41,616.
\]

Then

\[
\alpha=\gcd(D,E)=16,
\]

and

\[
\frac D\alpha=1=1^2,
\qquad
\frac E\alpha=2601=51^2.
\]

Hence the canonical coordinates are

\[
\boxed{\alpha=16,\qquad u=1,\qquad a=51.}
\]

The divisor witness is

\[
s=4A-1=3263.
\]

Indeed

\[
51n+1=3263\cdot9,464,324.
\]

Thus

\[
v=9,464,324.
\]

The recovered shift is

\[
\frac{u+v}{a}
=\frac{1+9,464,324}{51}
=185,575,
\]

which satisfies

\[
185,575\equiv3\pmod4.
\]

Finally

\[
K=\frac{n+185,575}{4}
=151,429,184
=\alpha uv.
\]

## Exact decomposition

The corresponding Type-II denominators are

\[
\boxed{x=151,429,184,}
\]

\[
\boxed{y=494,113,427,376,}
\]

\[
\boxed{z=4,676,449,569,436,933,824.}
\]

Exact integer arithmetic verifies

\[
4xyz=n(xy+xz+yz),
\]

so

\[
\frac4n=\frac1x+\frac1y+\frac1z.
\]

## Cumulative depth profile

Among the `1,587,581` audited primes:

| maximum A | covered primes |
|---:|---:|
| 5 | 662,193 |
| 10 | 1,284,796 |
| 20 | 1,497,424 |
| 50 | 1,579,257 |
| 100 | 1,586,592 |
| 200 | 1,587,509 |
| 300 | 1,587,567 |
| 624 | 1,587,580 |
| 816 | 1,587,581 |

Thus only one audited prime through `10^9` requires `A>624`.

## Strategic consequence

The failed ancestry-cover heuristics should not distract from the stronger observed fact: the **complete** Type-II criterion remains extraordinarily shallow on the entire six-class prime population through `10^9`.

The next useful questions are therefore:

1. why the minimum square-completion depth is usually tiny;
2. what arithmetic feature forces the isolated jump from `624` to `816`;
3. whether the record depth remains slowly growing beyond `10^9`;
4. whether one can prove a density or deterministic bound directly for complete Type II rather than for a proper-ancestor subsystem.

## Claim boundary

This is finite verification through `10^9`, not a universal bound `A<=816`. No claim is made that `816` suffices beyond the audited range.