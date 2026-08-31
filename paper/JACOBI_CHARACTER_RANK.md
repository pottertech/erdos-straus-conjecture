# Exact Rank Growth of the Jacobi Ancestry Spectrum

**Status:** unconditional corollary of `JACOBI_SAFE_MAXIMALITY.md` and the prime number theorem in arithmetic progressions.

For each depth `A >= 1`, put

\[
m_A=4A-1
\]

and let

\[
v_A=(\operatorname{ord}_p(m_A)\bmod2)_p
\in\mathbf F_2^{(\mathcal P)}
\]

be the parity vector of the prime factorization of `m_A`.

Define the Jacobi ancestry space through depth `X` by

\[
\mathcal V_X
=\operatorname{span}_{\mathbf F_2}\{v_A:1\le A\le X\}.
\]

The vector `v_A` represents the quadratic character

\[
\chi_A(n)=\left(\frac{n}{4A-1}\right).
\]

Thus `dim V_X` measures the number of independent Jacobi-character directions introduced by the first `X` square-completed Type-II layers.

## Theorem 1: exact dimension formula

For every real `X >= 1`,

\[
\boxed{
\dim_{\mathbf F_2}\mathcal V_{\lfloor X\rfloor}
=
\pi(4\lfloor X\rfloor-1;4,3)
+
\pi\!\left(\frac{4\lfloor X\rfloor-1}{3};4,1\right),
}
\]

where `pi(y;4,a)` counts primes `p <= y` with `p == a (mod 4)`.

### Proof

By the span-classification theorem in `JACOBI_SAFE_MAXIMALITY.md`, the vector `v_A` is outside the span of all previous vectors if and only if one of two mutually exclusive conditions holds:

1. `m_A=4A-1` is prime;
2. `m_A=3q` with `q == 1 (mod 4)` prime.

Every such occurrence increases the dimension by exactly one, while every other layer increases it by zero.

The prime-target depths are in bijection with primes

\[
p=4A-1\le4X-1,
\qquad p\equiv3\pmod4,
\]

so their number is

\[
\pi(4X-1;4,3).
\]

The composite-new-direction depths are in bijection with primes

\[
q\le\frac{4X-1}{3},
\qquad q\equiv1\pmod4,
\]

via

\[
A=\frac{3q+1}{4}.
\]

Their number is

\[
\pi\!\left(\frac{4X-1}{3};4,1\right).
\]

The two sets are disjoint because the first has prime target modulus and the second has composite target modulus. Summing the rank increments proves the formula.

## Corollary 2: asymptotic rank growth

The prime number theorem in arithmetic progressions gives

\[
\pi(y;4,1)\sim\pi(y;4,3)\sim\frac12\frac{y}{\log y}.
\]

Therefore

\[
\boxed{
\dim\mathcal V_X
\sim
\frac{8}{3}\frac{X}{\log X}.
}
\]

More explicitly,

\[
\pi(4X;4,3)
\sim\frac{2X}{\log X},
\]

while

\[
\pi(4X/3;4,1)
\sim\frac{2X}{3\log X}.
\]

Thus the prime backbone contributes asymptotically three quarters of the new quadratic-character directions, while the composite `3q` backbone contributes one quarter:

\[
\boxed{
\frac{2}{2+2/3}=\frac34,
\qquad
\frac{2/3}{2+2/3}=\frac14.
}
\]

## Corollary 3: almost every layer is Jacobi-dependent

Since

\[
\dim\mathcal V_X=O(X/\log X),
\]

but there are `X` layers through depth `X`, the proportion of layers that introduce a genuinely new quadratic-character direction tends to zero:

\[
\boxed{
\frac1X\#\{A\le X:v_A\notin\operatorname{span}(v_1,\ldots,v_{A-1})\}
\sim\frac{8}{3\log X}\to0.
}
\]

Thus almost every layer is already Jacobi-dependent on earlier layers.

## Interpretation

This gives a precise structural meaning to the two symbolic backbones:

- prime target moduli generate all new `3 mod 4` prime-coordinate directions;
- composite targets `3q`, `q == 1 mod 4` prime, generate exactly the remaining new directions;
- every other layer contributes no new Jacobi character at all.

So the prime and `3q` backbones together form a basis-generation mechanism for the entire Jacobi ancestry spectrum.

This does **not** mean that all other Type-II layers are redundant as exact-depth layers. Jacobi character is only one coarse invariant. The certified layers `649` and `22339`, for example, are Jacobi-dependent yet still support exact-depth prime families through finer branch-dependent CRT/CSP information.

## Claim boundary

The vector-space representation of quadratic characters is standard. The candidate contribution is the exact rank-increment classification for the specific modulus sequence `4A-1`, inherited from the first-occurrence theorem, and the resulting exact/asymptotic dimension formula.

No claim is made that quadratic-character rank itself is a new concept, and the result should be compared with contemporary FCF/CENTL reciprocity-matrix and ancestry work before publication priority is asserted.