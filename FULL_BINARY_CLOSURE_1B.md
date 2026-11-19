# Full Binary Closure Through 10^9

**Status:** exact finite closure on the audited corrected residual population; not a proof of the global conjecture

The complete centered binary criterion asks for positive coprime integers `A,B` with

\[
AB\mid nK,
\qquad
A+B\equiv0\pmod u,
\qquad
K=\frac{n+u}{4}.
\]

The unit-partner slice is the special case `A=1` or `B=1`.

## Audited result

For every corrected residual prime

\[
n\le10^9,
\]

except `2521`, the audited unit-partner search already supplies a complete binary certificate with one partner equal to `1`.

For

\[
n=2521,
\]

take

\[
u=31,\qquad K=638,\qquad A=2,\qquad B=29.
\]

Then

\[
AB=58\mid2521\cdot638,
\qquad
\gcd(2,29)=1,
\qquad
A+B=31\equiv0\pmod{31}.
\]

Writing

\[
C=\frac{2521\cdot638}{2\cdot29}=27731,
\qquad
r=\frac{2+29}{31}=1,
\]

the generic binary endpoint gives

\[
X=638,\qquad Y=2\cdot27731=55462,\qquad Z=29\cdot27731=804199.
\]

Exact arithmetic verifies

\[
\frac4{2521}
=
\frac1{638}+
\frac1{55462}+
\frac1{804199}.
\]

Therefore:

\[
\boxed{
\text{Every audited corrected residual prime }n\le10^9\text{ satisfies the complete centered binary criterion.}
}
\]

This is stronger than the unit-partner statement only at the single integer `2521` within the audited range.

## Global theorem target

The finite result suggests the logically correct endgame:

1. prove that all but a controlled exceptional set admit a unit-partner certificate;
2. prove that every remaining permanent unit-partner exception admits a non-unit binary pair.

It is unnecessary, and false already at `2521`, to demand a unit-partner certificate for every residual prime.
