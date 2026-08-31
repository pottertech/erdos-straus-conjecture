# Fixed-Cofactor Exceptional-Layer Lemma

**Status:** exact algebraic lemma. This is a reduction tool for constructing infinite exact square-completed Type-II depth families; by itself it does not prove the Erdős–Straus conjecture.

Let a target depth be parametrized by

\[
A=\frac{sr+1}{4},\qquad m_A=sr,
\]

where `s` is fixed, `r` is an odd prime, and `sr\equiv3\pmod4`. Let `d|A^2` be a fixed target divisor, so the target prime progression satisfies

\[
n\equiv -4d\pmod{sr}.
\]

Suppose that every target prime coordinate except the variable prime `r` is assigned a unit square residue. Then every earlier layer whose modulus is not divisible by `r` is excluded by the universal square-safe residue lemma. Only earlier layers with modulus

\[
m_B=cr,\qquad c<s,\qquad cr\equiv3\pmod4,
\]

can remain exceptional.

Fix such a cofactor `c`, and put

\[
B=\frac{cr+1}{4}.
\]

Assume a collision occurs at depth `B`. Then there is a divisor

\[
E\mid B^2
\]

whose trap residue agrees with the target progression on the shared `r`-coordinate. Hence

\[
E\equiv d\pmod r,
\]

so for some integer `k>=0`,

\[
E=rk+d.
\]

Let

\[
F=\frac{B^2}{E}.
\]

Since

\[
16EF=(cr+1)^2,
\]

and `E\equiv d (mod r)`, reduction modulo `r` gives

\[
16dF\equiv1\pmod r.
\]

Therefore there is an integer `h>=0` such that

\[
16dF=rh+1.
\]

Substituting `E=rk+d` and `16dF=rh+1` into `16EF=(cr+1)^2` and cancelling one factor of `r` yields the exact identity

\[
\boxed{
 r(kh-dc^2)+k+dh-2dc=0.
}
\]

Equivalently, when `kh\ne dc^2`,

\[
\boxed{
 r=\frac{k+dh-2dc}{dc^2-kh}.
}
\]

This equation depends on the variable prime `r` only through the final rational expression; the admissible search region is controlled entirely by the fixed pair `(d,c)`.

## AM--GM reduction

If `kh>dc^2`, then

\[
k+dh\ge2\sqrt{dkh}>2dc,
\]

so both terms in

\[
r(kh-dc^2)+k+dh-2dc
\]

are positive, impossible. Thus every collision satisfies

\[
kh\le dc^2.
\]

If equality holds, AM--GM forces

\[
\boxed{k=dc,\qquad h=c.}
\]

In that equality configuration,

\[
E=d(cr+1)=4dB,
\qquad
F=\frac{B}{4d},
\]

so it can occur only if

\[
\boxed{4d\mid B.}
\]

Consequently, whenever the target congruence class for `r` rules out `4d|B` for every exceptional cofactor `c`, all collisions satisfy the strict finite bound

\[
\boxed{kh<dc^2.}
\]

Together with the necessary divisibility

\[
\boxed{16d\mid rh+1,}
\]

this reduces every exceptional layer to a finite Diophantine verification depending only on fixed integers `d,c` and the prescribed congruence class of `r`.

## Interpretation

This lemma explains why fixed-cofactor backbones can be proved uniformly for arbitrarily large variable primes. Once all non-`r` coordinates are made square-safe, the global first-hit problem collapses to finitely many cofactors `c<s`; each such cofactor is governed by a bounded equation with `kh<dc^2`.

The previously proved `7r` and `11r` backbones are the first two instances. The `19r` construction uses `d=10` and exceptional cofactors `c=3,7,11,15`.
