# Untwisted Exception Stratification Through 10^8

**Status:** exact finite computation plus exact all-shift classification for the listed small tail

The shallow unit-partner search through `u <= 299` is overwhelmingly untwisted, but a few corrected residual primes fail the untwisted branch in that 75-position window.

Using the exact untwisted all-shift identity

\[
(4ad-n)(4ar-1)=n+4a,
\]

and its finite bound

\[
a\le\lfloor(n+3)/8\rfloor,
\]

we can distinguish a shallow-window miss from a genuine permanent untwisted exception.

## Corrected residual population through 10^8

There are **26,399** corrected residual primes through `10^8` after the classical/hard/shift reductions.

Only **9** of them have no untwisted unit-partner witness with `u <= 299`:

\[
2521,
66529,
297889,
3842281,
5410441,
12150889,
15308329,
25569769,
86083321.
\]

The later five acquire untwisted witnesses quickly beyond the 299 window:

| n | first located larger untwisted u | divisor d | r=(d+1)/u |
|---:|---:|---:|---:|
| 297,889 | 911 | 37,350 | 41 |
| 3,842,281 | 81,751 | 245,252 | 3 |
| 5,410,441 | 28,327 | 339,923 | 12 |
| 12,150,889 | 315 | 4,409 | 14 |
| 15,308,329 | 311 | 637,860 | 2,051 |
| 25,569,769 | 671 | 913,230 | 1,361 |
| 86,083,321 | 467 | 76,587 | 164 |

Thus most shallow untwisted failures are merely **depth exceptions**.

## Permanent untwisted exceptions currently proved

### n = 2521

The finite all-shift untwisted search has no solution. The twisted all-shift search also has no solution. Thus `2521` is a permanent exception to the entire unit-partner slice.

It is nevertheless solved by the complete binary pair

\[
u=31,\quad A=2,\quad B=29.
\]

### n = 66529

The exact all-shift untwisted search also has no solution, so

\[
\boxed{66529\text{ is a permanent untwisted exception}.}
\]

However it is not a unit-partner exception. The twisted branch succeeds at

\[
u=19,
\qquad K=16637=127\cdot131,
\qquad d=131.
\]

Indeed,

\[
66529\cdot131+1=19\cdot458700.
\]

The corresponding explicit Erdős--Straus decomposition is

\[
\boxed{
\frac4{66529}
=
\frac1{16637}
+
\frac1{507708871715100}
+
\frac1{58254900}.
}
\]

## Structural hierarchy

The data now distinguish three genuinely different phenomena:

1. **ordinary untwisted success** within the 75-position window;
2. **untwisted depth exceptions**, which eventually succeed at a larger shift;
3. **permanent untwisted exceptions**, such as `2521` and `66529`.

The twisted branch then splits permanent untwisted exceptions again:

- `66529` is rescued by a twisted unit-partner certificate;
- `2521` is not, and requires a non-unit complete binary pair.

This is the correct exceptional-set stratification for a global proof. A final theorem should not demand untwisted success for every residual prime.