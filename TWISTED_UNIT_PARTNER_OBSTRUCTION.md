# Twisted Unit-Partner Obstruction

**Status:** exact local theorem; no global closure claim

Let

\[
K=\frac{n+u}{4},\qquad u\equiv3\pmod4,
\]

with `gcd(n,u)=1`. The twisted unit-partner branch asks for a divisor

\[
d\mid K
\]

such that

\[
nd\equiv-1\pmod u.
\]

Equivalently,

\[
d\equiv t:=-n^{-1}\pmod u.
\]

## Pairing involution

On the unit group `G=(Z/uZ)^×`, define

\[
\tau_t(r)=t r^{-1}.
\]

Then `tau_t` is an involution. If two prime-factor residue classes `r,s` of `K` satisfy `s=t r^{-1}`, their product gives a divisor of `K` congruent to `t`, hence a twisted unit-partner certificate.

Therefore failure of the twisted branch forces the occupied prime-factor residue classes to be an independent set for this involution, except possibly at fixed points.

The fixed-point equation is

\[
r^2\equiv t\pmod u.
\]

Thus the involution is fixed-point-free exactly when `t=-n^{-1}` is not a square modulo `u`.

## Prime shifts

Assume now that `u` is prime and `u == 3 (mod 4)`. Then

\[
\left(\frac{-n^{-1}}u\right)
=
\left(\frac{-1}u\right)
\left(\frac n u\right)
=-\left(\frac n u\right).
\]

Hence:

- if `(n/u)=+1`, then `-n^{-1}` is a quadratic nonresidue, `tau_t` has no fixed point, and twisted failure implies that the distinct prime-factor residue classes of `K` occupy at most `(u-1)/2` unit classes;
- if `(n/u)=-1`, then `-n^{-1}` is a quadratic residue, fixed points exist, and the simple half-group bound is not available without tracking their multiplicities.

This gives the exact local theorem

\[
\boxed{
\left(\frac n u\right)=+1
\ \&\
\#R_u(K)>\frac{u-1}{2}
\Longrightarrow
\exists d\mid K:\ nd\equiv-1\pmod u.
}
\]

## Composite shifts

For odd composite `u`, the same involution remains valid. A sufficient condition for it to be fixed-point-free is that `-n^{-1}` be a nonsquare modulo at least one prime-power divisor of `u`.

In particular, if some prime `p|u` satisfies

\[
p\equiv3\pmod4,
\qquad
\left(\frac n p\right)=+1,
\]

then

\[
\left(\frac{-n^{-1}}p\right)=-1,
\]

so the fixed-point equation has no solution modulo `p`, hence none modulo `u`. Under that sufficient condition the same `phi(u)/2` independent-set bound follows.

## Combined interpretation

The untwisted target `-1` is nonsquare for every admissible `u == 3 (mod 4)`, so its involution is always fixed-point-free.

The twisted branch adds another half-group restriction precisely at shifts where `-n^{-1}` is nonsquare. For prime shifts this is exactly the quadratic-residue condition `(n/u)=+1`.

This matches the exact scope of the quadratic-residue obstruction described in Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n == 1 (mod 24)*, arXiv:2608.24035 (2026), especially the discussion of the two-sided obstruction in Section 4.2.

## What this does not prove

It does not justify simply doubling the sieve dimension at every shift. At prime shifts with `(n/u)=-1`, the twisted involution has fixed points and must be handled separately.
