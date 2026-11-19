# Type-II Depth Coordinates: Square Depth vs Dahan Pair Depth

**Status:** exact coordinate clarification. This note corrects a tempting but invalid comparison between two different notions of search depth.

The complete prime Type-II family is represented in the repository in two equivalent coordinate systems, but the natural depth parameter in each system is different.

## 1. Square-completion depth

The square-completed criterion is

\[
D\mid A^2,
\qquad
4A-1\mid n+4D.
\]

Define

\[
\delta_{\rm sq}(n)
=
\min A
\]

over all valid square-completed Type-II certificates.

`TYPEII_DEPTH_UNBOUNDED.md` and `TYPEII_DEPTH_LOG_LOWER_BOUND.md` concern this quantity.

## 2. Dahan two-parameter depth

Dahan's complete Type-II criterion uses coprime positive parameters `(u,a)` and a divisor witness

\[
s=4\alpha ua-1
\]

of

\[
an+u.
\]

The growing-depth search bounds

\[
u,a\le J,
\]

while the quotient `alpha` is part of the witness and is not bounded by `J`.

Define

\[
\delta_{\rm Dah}(n)
=
\min \max(u,a)
\]

over all valid Dahan Type-II certificates.

## 3. Exact coordinate map

As proved in `SQUARE_COMPLETION_DAHAN_MAP.md`,

\[
\boxed{A=\alpha ua},
\qquad
\boxed{D=\alpha u^2}.
\]

Conversely, from `D|A^2`,

\[
\alpha=\gcd(D,A^2/D),
\]

\[
u=\sqrt{D/\alpha},
\qquad
 a=\sqrt{(A^2/D)/\alpha}.
\]

Since

\[
A=\alpha ua\ge \max(u,a),
\]

every square-completed witness of depth `A` gives a Dahan witness of pair depth at most `A`.

Therefore

\[
\boxed{
\delta_{\rm Dah}(n)\le \delta_{\rm sq}(n).
}
\]

## 4. The converse implication is false

A small Dahan pair depth does **not** imply a small square depth, because `alpha` may be large:

\[
A=\alpha ua.
\]

Thus a certificate may have bounded `u,a` but an arbitrarily larger `A` if its divisor witness has large quotient `alpha`.

The finite record already illustrates the scale separation. For

\[
n=2,031,121,
\]

the minimum square-completion certificate recorded through `10^8` has

\[
A=624,
\qquad D=576.
\]

The recovered Dahan coordinates are only

\[
\alpha=4,
\qquad u=12,
\qquad a=13.
\]

So square depth `624` corresponds to Dahan pair depth `13`.

## 5. Consequence for the logarithmic lower bound

The progression argument proves that along an infinite sequence

\[
\delta_{\rm sq}(p)\gg\log p.
\]

This does **not** imply

\[
\delta_{\rm Dah}(p)\gg\log p.
\]

The inequality goes in the wrong direction for that inference:

\[
\delta_{\rm Dah}\le\delta_{\rm sq}.
\]

In particular, the square-depth lower bound cannot be used to claim that Dahan's two-parameter search must take `J` at least logarithmic in `p`.

A genuine lower bound for Dahan pair depth would require an obstruction that rules out **all** divisor witnesses `alpha` for each bounded pair `(u,a)`, not merely all square coordinates `A<=J`.

## 6. Relation to Dahan's growing-depth theorem

Dahan's growing-depth estimates with

\[
J=(\log N)^\lambda
\]

or optimized larger `J` are bounds on `u,a`, not on `A=alpha*u*a`.

Accordingly:

- the repo's square-depth lower bound and Dahan's growing-pair-depth upper-density theorem are compatible;
- neither directly matches the other's depth scale;
- comparisons between their asymptotics must first control `alpha`.

This distinction should be kept explicit in any manuscript or theorem statement.
