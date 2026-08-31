# Semiprime Mixed-Square Ancestry Density

**Status:** unconditional asymptotic theorem for divisor-modulus inheritance of the mixed-square pair. This is **not** an exact-depth realization theorem and is **not** a proof of Type-II universality.

Let

\[
A=uv,
\qquad u<v
\]

with distinct primes, and put

\[
m_A=4A-1.
\]

For an earlier depth `B<A`, write

\[
m_B=4B-1,
\qquad
Q_B=\{D\bmod m_B:D\mid B^2\}.
\]

When `m_B | m_A`, the semiprime mixed-square pair is inherited from depth `B` exactly when

\[
u^2\bmod m_B\in Q_B,
\]

in which case `v^2` is inherited automatically.

We count squarefree semiprime indices `A=uv<=X` with distinct primes and ask what proportion are already captured by a fixed collection of low-depth ancestors.

---

## 1. Fixed-modulus equidistribution for semiprimes

Fix an integer `M>=1`. Apart from the negligible subfamily in which one prime factor divides `M`, the ordered prime pairs

\[
(u,v),\qquad uv\le X,
\]

are asymptotically equidistributed among pairs of reduced residue classes modulo `M`.

For fixed reduced classes `a,b (mod M)`, the prime number theorem in arithmetic progressions, applied in the usual hyperbola decomposition, gives

\[
\#\{u<v:\ uv\le X,\ u\equiv a\ (M),\ v\equiv b\ (M)\}
=
\left(\frac{1}{\varphi(M)^2}+o(1)\right)S_2(X),
\]

where `S_2(X)` denotes the total number of squarefree semiprimes `uv<=X` with distinct prime factors, up to the harmless ordered/unordered normalization. Thus any condition depending only on the pair `(u mod M,v mod M)` has limiting density equal to the corresponding proportion of reduced residue pairs.

The finitely many cases with `u|M` or `v|M` contribute `o(S_2(X))` and do not affect the limiting densities below.

---

## 2. The universal depth-1 and depth-2 ancestors

### Depth 1

Here

\[
m_1=3,
\qquad
Q_1=\{1\}.
\]

If

\[
A=uv\equiv1\pmod3,
\]

then `3|m_A`. Since `u,v` are asymptotically coprime to `3`, the congruence `uv==1 (mod 3)` forces `u` and `v` into the same nonzero residue class modulo `3`, so

\[
u^2\equiv1\pmod3\in Q_1.
\]

Hence depth `1` captures the mixed-square pair whenever

\[
\boxed{A\equiv1\pmod3.}
\]

Among reduced semiprime residue pairs modulo `3`, this occurs with probability `1/2`.

### Depth 2

Here

\[
m_2=7,
\qquad
Q_2=\{1,2,4\},
\]

the complete set of nonzero quadratic residues modulo `7`.

If

\[
A=uv\equiv2\pmod7,
\]

then `7|m_A`. For every `u` coprime to `7`, the square `u^2` lies in `Q_2`, so depth `2` captures the mixed-square pair automatically.

Thus depth `2` captures whenever

\[
\boxed{A\equiv2\pmod7.}
\]

Among reduced semiprime residue pairs modulo `7`, this occurs with probability `1/6`.

### Combined density

Modulo `21`, the semiprime product is asymptotically uniform among the

\[
\varphi(21)=12
\]

unit classes. The condition `A==1 (mod 3)` occupies `6` of these classes; `A==2 (mod 7)` occupies `2`; their intersection occupies `1`. Therefore their union occupies

\[
6+2-1=7
\]

of the `12` unit classes.

Hence:

\[
\boxed{
\text{depths }1\text{ and }2\text{ already inherit at least }\frac7{12}+o(1)
}
\]

of all squarefree semiprime mixed-square layers.

Equivalently, at most

\[
\boxed{\frac5{12}+o(1)}
\]

survive these two ancestors.

---

## 3. Adding depth 3

At depth `3`,

\[
m_3=11,
\qquad
Q_3=\{1,3,9\}.
\]

The nonzero quadratic residues modulo `11` are

\[
\{1,3,4,5,9\}.
\]

Thus `Q_3` captures exactly `3/5` of the unit square classes.

The ancestor is present precisely when

\[
11\mid m_A
\iff
A\equiv3\pmod{11}.
\]

Conditional on `A==3 (mod 11)`, choose `u` uniformly in `F_11^*`; then `v` is forced to the unique class

\[
v\equiv3u^{-1}\pmod{11}.
\]

The value `u^2` is uniform over the five nonzero quadratic-residue classes, so the conditional probability of capture is exactly

\[
\frac35.
\]

The product class `A==3 (mod 11)` itself occurs with probability `1/10` among unit product classes modulo `11`. Therefore the unconditional depth-3 capture probability is

\[
\frac1{10}\cdot\frac35=\frac3{50}.
\]

Because `11` is coprime to `21`, fixed-modulus semiprime equidistribution modulo `231=21\cdot11` makes this condition asymptotically independent of the survivor condition from depths `1` and `2`.

The fraction surviving depths `1` and `2` is `5/12`, so depth `3` removes an additional fraction

\[
\frac5{12}\cdot\frac3{50}
=
\frac1{40}.
\]

Therefore:

\[
\boxed{
\text{depths }1,2,3\text{ inherit at least }
\frac7{12}+\frac1{40}
=
\frac{73}{120}+o(1)
}
\]

of all squarefree semiprime mixed-square layers.

Equivalently, the asymptotic proportion that can remain mixed-square primitive after these three ancestors is at most

\[
\boxed{
\frac{47}{120}+o(1)
\approx0.391666\ldots
}.
\]

---

## 4. General finite-ancestor product principle

The preceding calculation is an instance of a general fixed-modulus principle.

Let `B_1,...,B_k` be fixed ancestor depths whose moduli

\[
m_j=4B_j-1
\]

are pairwise coprime after any shared factors have been absorbed into a single finite CRT modulus. For each `j`, let

\[
\eta_j
=
\frac{|Q_{B_j}\cap QR^*(m_j)|}{|QR^*(m_j)|}
\]

be the fraction of unit square classes captured by depth `B_j`.

The ancestor `B_j` can act only on the product class

\[
A\equiv B_j\pmod{m_j},
\]

which occupies `1/\varphi(m_j)` of the unit product classes modulo `m_j`. Conditional on that product class, `u^2` is asymptotically uniform among the unit square classes, so the conditional capture probability is `eta_j`.

Thus, for pairwise-coprime ancestor moduli, the survivor proportion is multiplied by

\[
\boxed{
1-\frac{\eta_j}{\varphi(m_j)}
}
\]

when the new ancestor is added.

For overlapping moduli the exact density is still finite and computable: enumerate the reduced residue pairs modulo the fixed least common multiple and test the corresponding ancestor conditions. No growing-modulus uniformity is required.

This gives a systematic route to rigorous asymptotic upper bounds on the density of mixed-square primitive semiprime layers using any fixed finite ancestor set.

---

## 5. Interpretation

The finite census through `A<=100000` showed that a large majority of squarefree semiprime mixed-square pairs are inherited. The theorem above converts part of that empirical phenomenon into a rigorous asymptotic statement:

\[
\boxed{
\text{at least }60.833\%\text{ are already captured by depths }1,2,3.
}
\]

This is only a lower bound. Additional ancestors such as `B=6` (`m_B=23`, capture ratio `9/11`) and `B=12` (`m_B=47`, capture ratio `13/23`) can improve it by the same fixed-modulus method.

The result concerns only **divisor-modulus inheritance of the semiprime mixed-square pair**. A layer that survives these tests may still be inherited from another ancestor, may still be globally solved at a smaller non-dividing depth by cross-modulus CRT, or may be exact-depth realized by a more complicated branch-dependent construction. Conversely, this theorem does not produce an infinite family of exact depths outside the Jacobi-safe `3q` backbone.

## Claim boundary

The number-theoretic input is only the prime number theorem in fixed arithmetic progressions and the exact local ancestor-capture sets. No novelty claim is made for semiprime equidistribution in fixed residue classes.

The candidate contribution is the exact application to square-completed Type-II semiprime ancestry and the explicit `73/120` lower bound. This should still be checked against the contemporary squarefree-lift/ancestry literature before publication priority is claimed.