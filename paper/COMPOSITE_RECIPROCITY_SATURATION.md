# Saturation of the New Composite Jacobi Directions

**Status:** unconditional synthesis of the Jacobi-rank theorem and the quantitative exceptional-set theorem.

Let

\[
m_A=4A-1,
\qquad
v_A=(\operatorname{ord}_p(m_A)\bmod2)_p.
\]

Call a depth `A` **Jacobi-new** if

\[
v_A\notin\operatorname{span}_{\mathbf F_2}\{v_B:B<A\}.
\]

By `JACOBI_SAFE_MAXIMALITY.md`, the composite Jacobi-new depths are exactly

\[
\boxed{
A_q=\frac{3q+1}{4},
\qquad q\equiv1\pmod4\text{ prime}.
}
\]

Let

\[
J_{\rm comp}(X)
=
\#\{A\le X:A\text{ is Jacobi-new and }4A-1\text{ is composite}\}.
\]

Then exactly

\[
\boxed{
J_{\rm comp}(X)
=
\pi\!\left(\frac{4X-1}{3};4,1\right).
}
\]

Now let `R_comp(X)` count those composite Jacobi-new depths for which the structural `3q` criterion proves infinite exact-depth prime realization, equivalently those `A_q` for which `A_q` has a prime divisor `ell == 2 (mod 3)`.

## Theorem: quantitative reciprocity saturation

\[
\boxed{
J_{\rm comp}(X)-R_{\rm comp}(X)
\ll
\frac{X}{(\log X)^{3/2}}.
}
\]

Consequently

\[
\boxed{
\frac{R_{\rm comp}(X)}{J_{\rm comp}(X)}
=
1+O\!\left(\frac1{\sqrt{\log X}}\right),
}
\]

where the expression is understood as a one-sided saturation estimate, i.e.

\[
1-O((\log X)^{-1/2})
\le
\frac{R_{\rm comp}(X)}{J_{\rm comp}(X)}
\le1.
\]

Thus asymptotically every genuinely new **composite** quadratic-character direction in the Type-II layer sequence is realized by infinitely many primes as an exact square-completion depth.

### Proof

Put

\[
Y=\frac{4X-1}{3}.
\]

The map

\[
q\longmapsto A_q=\frac{3q+1}{4}
\]

is a bijection between primes `q <= Y`, `q == 1 (mod 4)`, and composite Jacobi-new depths `A <= X`. Hence

\[
J_{\rm comp}(X)=\pi(Y;4,1).
\]

The only such parameters not certified by the structural exact-depth theorem are contained in the exceptional set

\[
\mathcal E(Y)
=
\left\{q\le Y:q\text{ prime},\ q\equiv1\pmod4,
\ A_q\text{ has no prime divisor }\ell\equiv2\pmod3\right\}.
\]

The quantitative half-dimensional sieve gives

\[
|\mathcal E(Y)|
\ll
\frac{Y}{(\log Y)^{3/2}}.
\]

Therefore

\[
J_{\rm comp}(X)-R_{\rm comp}(X)
\le |\mathcal E(Y)|
\ll
\frac{X}{(\log X)^{3/2}}.
\]

Also the prime number theorem in the progression `1 mod 4` gives

\[
J_{\rm comp}(X)
=\pi(Y;4,1)
\asymp
\frac{X}{\log X}.
\]

Dividing yields the stated relative error.

## Corollary: asymptotic size

Since

\[
J_{\rm comp}(X)
\sim
\frac{2}{3}\frac{X}{\log X},
\]

we have

\[
\boxed{
R_{\rm comp}(X)
=
\frac12\operatorname{Li}\!\left(\frac{4X-1}{3}\right)
+O\!\left(\frac{X}{(\log X)^{3/2}}\right)
}
\]

provided the fixed-modulus prime-counting error is absorbed into the displayed error term; without choosing a specific effective PNT error, the safe statement is

\[
R_{\rm comp}(X)
=
\pi\!\left(\frac{4X-1}{3};4,1\right)
+O\!\left(\frac{X}{(\log X)^{3/2}}\right).
\]

In particular,

\[
R_{\rm comp}(X)
\sim
\frac{2}{3}\frac{X}{\log X}.
\]

## Interpretation

The prime and `3q` backbones are exactly the layers that generate new Jacobi-character directions. The present result says that the composite half of that basis-generation mechanism is not merely algebraically available: almost every one of its prime parameters also carries an actual exact-depth Type-II prime family.

So, at the level of new quadratic-character directions,

\[
\boxed{
\text{algebraic availability}
\quad\text{and}\quad
\text{exact-depth realization}
}
\]

coincide asymptotically for the composite backbone.

The small exceptional set may still contain parameters whose depths are realized by other, non-`D == 2 (mod 3)` mechanisms; the theorem does not assert otherwise. Therefore `R_comp` is a certified-backbone count, not necessarily the complete count of exact depths among those exceptional parameters.

## Claim boundary

This theorem uses no new analytic input beyond the previously proved half-dimensional exceptional-set bound and no new algebraic input beyond the Jacobi-span classification. Its contribution is the synthesis: the exact-depth backbone asymptotically saturates the set of all new composite reciprocity directions.