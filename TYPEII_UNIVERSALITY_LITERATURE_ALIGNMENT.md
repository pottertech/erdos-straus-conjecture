# Literature Alignment: Universal Type II for the Erdős--Straus Case m=4

**Status:** literature alignment / claim-boundary note

The square-completed criterion used in this repository is a complete coordinate form of standard prime Type II for the ordinary Erdős--Straus equation

\[
\frac4p=\frac1x+\frac1y+\frac1z.
\]

The natural global target suggested by the computation is:

> Does every prime `p` admit a Type-II solution?

This is not merely an internally generated strengthening.  Pomerance and Weingartner, in *Exceptions to the Erdős--Straus--Schinzel Conjecture*, explicitly record that for the ordinary `m=4` case every prime below `10^13` has a Type-II solution and conjecture that this persists beyond `10^13`.

Their generalized `m/p` problem behaves differently: for every `m >= 6` they prove the existence of primes with no Type-II solution.  Thus the possible universality of Type II is special to the classical `m=4` Erdős--Straus case (and they also record analogous evidence for `m=5`).

## Relevance to the square-completion program

For prime `p == 1 (mod 4)`, the square-completed criterion is

\[
\boxed{
\exists A,D>0:
\quad D\mid A^2,
\quad 4A-1\mid p+4D,
\quad p\nmid D.
}
\]

Therefore proving universal existence of such `(A,D)` is exactly a route to universal Type II for the classical Erdős--Straus equation.

This is a stronger statement than merely proving that every prime has either Type I or Type II, but it is independently supported by published computation through `10^13`.

## Interaction with the depth lower bound

`TYPEII_DEPTH_UNBOUNDED.md` and `TYPEII_DEPTH_LOG_LOWER_BOUND.md` prove that, even if universal Type II is true, its minimum square-completion depth cannot be bounded by an absolute constant and must be at least logarithmic along an infinite sequence of primes.

Thus a proof of the Pomerance--Weingartner `m=4` Type-II universality conjecture cannot come from any fixed finite list of square depths.  It must be genuinely adaptive/growing-depth.

## Claim boundary

This note does not claim a proof of universal Type II.  The published evidence through `10^13` and our exact square-completion computations are finite evidence.  The global existence statement remains open.
