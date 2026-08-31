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

The purpose here is to classify the possible target moduli for this mechanism.

---

## 1. First occurrence of an odd modulus

For an odd integer `s`, let `beta(s)` be the least positive integer `B` satisfying

\[
s\mid4B-1.
\]

Equivalently, `beta(s)` is the least positive residue of `4^{-1} mod s`.

Because `s == 1 or 3 (mod 4)`, one has the explicit formula

\[
\boxed{
\beta(s)=
\begin{cases}
(s+1)/4,&s\equiv3\pmod4,\\[4pt]
(3s+1)/4,&s\equiv1\pmod4.
\end{cases}}
\]

Indeed these are positive integers less than or equal to `s` and satisfy `4 beta(s) == 1 (mod s)`.

Now let `s|m_A`. Since `4A == 1 (mod s)`,

\[
A\equiv\beta(s)\pmod s.
\]

Thus `s` occurs in an earlier modulus `4B-1`, `B<A`, if and only if

\[
\boxed{\beta(s)<A.}
\]

---

## 2. When is the ancestral overlap proper?

### Theorem 1

If

\[
H_A<m_A,
\]

then the target modulus has one of the two forms

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

whose full exponent is not present in `H_A`. Then `s` has not occurred at any earlier depth, so

\[
\beta(s)=A.
\]

If `s == 3 (mod 4)`, then

\[
A=(s+1)/4,
\]

hence

\[
m_A=4A-1=s=p^e.
\]

If `s == 1 (mod 4)`, then

\[
A=(3s+1)/4,
\]

hence

\[
m_A=4A-1=3s=3p^e.
\]

This proves necessity.

Conversely, if `m_A=p^e == 3 (mod 4)`, then the top prime power `p^e` first occurs at

\[
A=(p^e+1)/4.
\]

If `m_A=3p^e` with `p^e == 1 (mod 4)`, then `p^e` first occurs at

\[
A=(3p^e+1)/4.
\]

Thus in either case the top prime-power coordinate is absent from `L_{A-1}`, so `H_A<m_A`.

---

## 3. Composite prime powers are always blocked

Suppose

\[
m_A=p^e,
\qquad e>1.
\]

Since `m_A == 3 (mod 4)`, one has

\[
p\equiv3\pmod4,
\qquad e\text{ odd}.
\]

Also `p` already occurs at an earlier depth, so

\[
p\mid H_A.
\]

We show that every divisor `D|A^2` makes `-4D` a quadratic nonresidue modulo `p`.

Let `r` be any prime divisor of `A`. Since

\[
4A=p^e+1,
\]

we have

\[
p^e\equiv-1\pmod r.
\]

Taking Legendre symbols and using that `e` is odd,

\[
\left(\frac p r\right)=\left(\frac{-1}r\right).
\]

Quadratic reciprocity, with `p == 3 (mod 4)`, gives

\[
\left(\frac r p\right)
=
\left(\frac p r\right)
(-1)^{((p-1)/2)((r-1)/2)}
=
\left(\frac{-1}r\right)^2
=1.
\]

Thus every prime divisor of `A` is a quadratic residue modulo `p`. Hence for every `D|A^2`,

\[
\left(\frac D p\right)=1.
\]

But

\[
\left(\frac{-4D}p\right)
=
\left(\frac{-1}p\right)
\left(\frac Dp\right)
=-1.
\]

Therefore `-4D` is not a square modulo `p`, and hence not a square modulo `H_A`.

So:

\[
\boxed{m_A=p^e,\ e>1\quad\Longrightarrow\quad
\text{the square-safe overlap criterion never succeeds}.}
\]

The only prime-power targets admitted by the mechanism are therefore the prime-modulus case `e=1`, i.e. the already-known prime backbone.

---

## 4. Targets `3p^e` with `e>1` are always blocked

Now suppose

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

which is not a square modulo `3`. Hence the overlap criterion fails.

### Case 2: `D == 2 (mod 3)`

We show that the target residue is a quadratic nonresidue modulo `p`.

Let `r|A` be prime. From

\[
4A=3p^e+1
\]

we obtain

\[
3p^e\equiv-1\pmod r.
\]

Equivalently,

\[
p^e\equiv-3^{-1}\pmod r.
\]

#### If `e` is even

Taking Legendre symbols gives

\[
1=\left(\frac{-3}r\right).
\]

For primes `r != 3`, the quadratic character of `-3` satisfies

\[
\left(\frac{-3}r\right)=1
\iff
r\equiv1\pmod3.
\]

Thus every prime divisor of `A` is `1 mod 3`, so every divisor `D|A^2` is also `1 mod 3`. Case 2 cannot occur.

#### If `e` is odd

Since `p^e == 1 (mod 4)`, we have

\[
p\equiv1\pmod4.
\]

Taking Legendre symbols in `p^e == -3^{-1} (mod r)` gives

\[
\left(\frac p r\right)
=
\left(\frac{-3}r\right).
\]

Because `p == 1 (mod 4)`, quadratic reciprocity has no sign, so

\[
\boxed{
\left(\frac r p\right)=\left(\frac{-3}r\right).
}
\]

Thus a prime divisor `r|A` has Legendre symbol `-1 mod p` exactly when

\[
r\equiv2\pmod3.
\]

If `D == 2 (mod 3)`, the total exponent parity in `D` of prime factors `r == 2 (mod 3)` is odd. Consequently

\[
\left(\frac D p\right)=-1.
\]

Since `p == 1 (mod 4)`,

\[
\left(\frac{-4D}p\right)
=
\left(\frac Dp\right)
=-1.
\]

So the target residue is not a square modulo `p`, hence not modulo `H_A`.

Combining the cases:

\[
\boxed{m_A=3p^e,\ e>1\quad\Longrightarrow\quad
\text{the square-safe overlap criterion never succeeds}.}
\]

---

## 5. Complete classification

### Theorem 2 — maximality of the composite square-safe backbone

The universal-square safe-residue CRT mechanism produces infinitely many primes of exact square-completion depth only in the following target-modulus situations:

1. **Prime target modulus**
   \[
   m_A=q\equiv3\pmod4\text{ prime},
   \]
   where `H_A=1`. This is the prime-modulus exact-depth backbone.

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

Therefore:

\[
\boxed{
\text{The }3q\text{ family is the maximal composite backbone obtainable from a single universal-square safe-residue CRT construction.}
}
\]

---

## 6. Consequence for the manuscript

The density-one `3q` theorem is not merely a convenient subfamily of the square-safe method. It exhausts the composite part of that entire mechanism.

To go beyond the `3q` backbone one must use genuinely richer information than one globally square-safe residue class: for example branch-dependent CRT assignments, multi-coordinate avoidance, divisor-modulus primitive structure, or the full CSP certificate method used at depths `649` and `22339`.

This explains structurally why those later composite examples require more complicated machinery.

## Claim boundary / prior art

The proof uses classical quadratic reciprocity and the universal square-safe Jacobi obstruction. Public FCF/CENTL work already contains closely related divisor-Jacobi and reciprocity-signature theorems, so no novelty claim is made for those ingredients.

The candidate contribution is the exact classification of the ancestral-overlap modulus together with the maximality conclusion for the global square-safe CRT construction. This must still be checked against the full contemporary ancestry/shadow literature before publication priority is claimed.

This theorem does not imply universal Type-II solvability or the Erdős--Straus conjecture.