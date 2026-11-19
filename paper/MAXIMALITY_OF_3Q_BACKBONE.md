# Maximality of the `3q` Composite Backbone for Universal Square-Safe CRT

**Status:** unconditional structural theorem. No publication-priority claim is made pending comparison with the full ancestry/reciprocity literature.

This note classifies exactly when the universal-square safe-residue method from `SQUARE_SAFE_OVERLAP_CRITERION.md` can produce an exact-depth prime family.

For `A >= 1`, write

\[
m_A=4A-1,
\qquad
L_{A-1}=\operatorname{lcm}_{1\le B<A}(4B-1),
\qquad
H_A=\gcd(m_A,L_{A-1}).
\]

The square-safe overlap theorem says that a target branch `(A,D)`, `D|A^2`, gives infinitely many primes of exact square depth `A` whenever

\[
-4D
\]

is a square modulo `H_A`.

## 1. First occurrence of an odd modulus

For an odd integer `s`, let `beta(s)` be the least positive integer `B` satisfying

\[
s\mid4B-1.
\]

Equivalently, `beta(s)` is the least positive residue of `4^{-1} mod s`. Since `s == 1 or 3 (mod 4)`,

\[
\boxed{
\beta(s)=
\begin{cases}
(s+1)/4,&s\equiv3\pmod4,\\[4pt]
(3s+1)/4,&s\equiv1\pmod4.
\end{cases}}
\]

If `s|m_A`, then `4A == 1 (mod s)`, so

\[
A\equiv\beta(s)\pmod s.
\]

Thus `s` occurs in an earlier modulus `4B-1`, `B<A`, if and only if

\[
\boxed{\beta(s)<A.}
\]

## 2. When is the ancestral overlap proper?

### Theorem 1

If

\[
H_A<m_A,
\]

then

\[
\boxed{m_A=p^e}
\]

or

\[
\boxed{m_A=3p^e},
\]

where `p` is an odd prime. In the second case necessarily

\[
p^e\equiv1\pmod4.
\]

Conversely, every target modulus of one of these forms has `H_A<m_A` at its top prime-power coordinate.

### Proof

If `H_A<m_A`, choose a prime power

\[
s=p^e\parallel m_A
\]

whose full exponent is absent from `H_A`. Then `s` has not occurred at an earlier depth, so

\[
\beta(s)=A.
\]

If `s == 3 (mod 4)`, then `A=(s+1)/4`, hence

\[
m_A=4A-1=s=p^e.
\]

If `s == 1 (mod 4)`, then `A=(3s+1)/4`, hence

\[
m_A=4A-1=3s=3p^e.
\]

Conversely, in each displayed form the top prime power first occurs at depth `A`, so it is absent from `L_{A-1}`.

## 3. Composite prime powers are blocked

Suppose

\[
m_A=p^e,
\qquad e>1.
\]

Since `m_A == 3 (mod 4)`,

\[
p\equiv3\pmod4,
\qquad e\text{ odd}.
\]

Also `p` occurs at an earlier depth, so

\[
p\mid H_A.
\]

We prove that every divisor `D|A^2` satisfies

\[
\left(\frac Dp\right)=1.
\]

Let `r` be an odd prime divisor of `A`. From

\[
4A=p^e+1
\]

we get

\[
p^e\equiv-1\pmod r.
\]

Since `e` is odd,

\[
\left(\frac pr\right)=\left(\frac{-1}r\right).
\]

Quadratic reciprocity, using `p == 3 (mod 4)`, gives

\[
\left(\frac rp\right)
=
\left(\frac pr\right)(-1)^{((p-1)/2)((r-1)/2)}
=
\left(\frac{-1}r\right)^2
=1.
\]

The only remaining possible prime divisor of `A` is `2`. If `2|A`, then

\[
p^e\equiv7\pmod8.
\]

Because `e` is odd and `p==3 (mod 4)`, this forces

\[
p\equiv7\pmod8,
\]

and hence

\[
\left(\frac2p\right)=1.
\]

Therefore every prime divisor of `A`, including `2` when present, is a quadratic residue modulo `p`. Hence every `D|A^2` satisfies

\[
\left(\frac Dp\right)=1.
\]

But

\[
\left(\frac{-4D}p\right)
=
\left(\frac{-1}p\right)
\left(\frac Dp\right)
=-1.
\]

Thus `-4D` is not a square modulo `p`, hence not modulo `H_A`.

So

\[
\boxed{m_A=p^e,\ e>1\Longrightarrow
\text{the square-safe overlap criterion never succeeds}.}
\]

The only prime-power targets admitted by the mechanism are the prime targets `e=1`.

## 4. Targets `3p^e` with `e>1` are blocked

Suppose

\[
m_A=3p^e,
\qquad p^e\equiv1\pmod4,
\qquad e>1.
\]

Both `3` and `p` occur at earlier depths, so

\[
3p\mid H_A.
\]

Let `D|A^2`.

### Case 1: `D == 1 (mod 3)`

Then

\[
-4D\equiv2\pmod3,
\]

which is not a square modulo `3`.

### Case 2: `D == 2 (mod 3)`

We show that `-4D` is a quadratic nonresidue modulo `p`.

From

\[
4A=3p^e+1
\]

we have, for every odd prime `r|A`,

\[
3p^e\equiv-1\pmod r.
\]

#### If `e` is even

Then

\[
1=\left(\frac{-3}r\right).
\]

For odd primes `r != 3`,

\[
\left(\frac{-3}r\right)=1
\iff
r\equiv1\pmod3.
\]

Also an odd square is `1 mod 8`, so `p^e == 1 (mod 8)` and

\[
3p^e+1\equiv4\pmod8,
\]

which makes `A` odd. Thus every prime divisor of `A` is `1 mod 3`, and every `D|A^2` is `1 mod 3`. Case 2 cannot occur.

#### If `e` is odd

Then `p^e == 1 (mod 4)` implies

\[
p\equiv1\pmod4.
\]

For every odd prime divisor `r|A`, quadratic reciprocity gives

\[
\boxed{
\left(\frac rp\right)=\left(\frac{-3}r\right).
}
\]

Hence an odd prime divisor `r|A` has Legendre symbol `-1 mod p` exactly when

\[
r\equiv2\pmod3.
\]

We must again handle `r=2` separately. If `2|A`, then

\[
3p^e\equiv7\pmod8,
\]

so, with `e` odd,

\[
p\equiv5\pmod8.
\]

Therefore

\[
\left(\frac2p\right)=-1.
\]

Thus the same rule extends to the factor `2`: every prime divisor of `A` that is `2 mod 3` contributes a factor `-1` to `(D/p)`, while every prime divisor that is `1 mod 3` contributes `+1`.

If `D == 2 (mod 3)`, the total exponent parity in `D` of prime factors congruent to `2 mod 3` is odd. Consequently

\[
\left(\frac Dp\right)=-1.
\]

Since `p == 1 (mod 4)`,

\[
\left(\frac{-4D}p\right)
=
\left(\frac Dp\right)
=-1.
\]

So the target residue is not a square modulo `p`, hence not modulo `H_A`.

Combining the cases,

\[
\boxed{m_A=3p^e,\ e>1\Longrightarrow
\text{the square-safe overlap criterion never succeeds}.}
\]

## 5. Complete classification

### Theorem 2 - maximality of the composite square-safe backbone

The universal-square safe-residue CRT mechanism can produce infinitely many primes of exact square-completion depth only in the following target-modulus situations:

1. **Prime target modulus**
   \[
   m_A=q\equiv3\pmod4\text{ prime},
   \]
   where `H_A=1`.

2. **Composite target modulus**
   \[
   \boxed{m_A=3q,\qquad q\equiv1\pmod4\text{ prime}.}
   \]
   Here
   \[
   H_A=3,
   \]
   and a branch `D|A^2` succeeds exactly when
   \[
   \boxed{D\equiv2\pmod3,}
   \]
   because then
   \[
   -4D\equiv1\pmod3
   \]
   is a square.

All composite prime-power targets and all `3p^e` targets with `e>1` are blocked by quadratic reciprocity.

Therefore

\[
\boxed{
\text{The }3q\text{ family is the maximal composite backbone obtainable from a single universal-square safe-residue CRT construction.}
}
\]

## 6. Consequence for the manuscript

The density-one `3q` theorem is not merely a convenient subfamily of the square-safe method. It exhausts the composite part of that entire mechanism.

To go beyond the `3q` backbone one must use genuinely richer information than one globally square-safe residue class: branch-dependent CRT assignments, multi-coordinate avoidance, divisor-modulus primitive structure, or the full CSP certificate method used at depths `649` and `22339`.

## Claim boundary / prior art

The proof uses classical quadratic reciprocity and the universal square-safe Jacobi obstruction. Public FCF/CENTL work already contains closely related divisor-Jacobi and reciprocity-signature theorems, so no novelty claim is made for those ingredients.

The candidate contribution is the exact classification of the ancestral-overlap modulus together with the maximality conclusion for the global square-safe CRT construction. This must still be checked against the full contemporary ancestry/shadow literature before publication priority is claimed.

This theorem does not imply universal Type-II solvability or the Erdős--Straus conjecture.