# Primitive Composite Layers in the Square-Completed Type-II Search

**Status:** exact structural pruning plus finite exploratory statistics; the general square-completed ancestry/shadow framework is prior art in the 2026 FCF/CENTL program, so no novelty claim is made for ancestry containment itself.

## Priority calibration

A literature audit found that FCF/CENTL had already developed the stronger square-completed shadow/ancestry framework by 2026-08-15.  In particular, their prime-index spectrum, multiplicative-shadow criterion, exponent-lattice shadow criterion, and related ancestry results subsume the general idea that later square-completed trap layers can be wholly shadowed by earlier divisor moduli.

Accordingly, the definitions and computations below should be treated as an **independent reproducible pruning implementation** for this repository, not as discovery of the shadow mechanism.

For square depth `A`, write

\[
m_A=4A-1
\]

and define the complete square-completed Type-II trap set

\[
T_A=\{-4D\pmod{m_A}: D\mid A^2\}.
\]

A prime `p` has a Type-II witness at depth `A` exactly when its residue modulo `m_A` lies in `T_A` (subject to `p\nmid D`).

## 1. Exact divisor-modulus inheritance

Let `B<A` and suppose

\[
m_B\mid m_A.
\]

If `r in T_A` also satisfies

\[
r\pmod{m_B}\in T_B,
\]

then every integer

\[
n\equiv r\pmod{m_A}
\]

already lies in a depth-`B` Type-II trap.  Therefore the progression `r mod m_A` contributes no new global coverage at depth `A`.

Call such a residue **divisor-modulus inherited**, and define

\[
P_A=T_A\setminus\bigcup_{\substack{B<A\\m_B\mid m_A}}
\{r\in T_A:r\bmod m_B\in T_B\}.
\]

If `P_A` is empty, the whole layer is redundant relative to smaller divisor moduli.

The ancestry relation itself has the elementary parametrization

\[
4B-1\mid4A-1
\iff
A=B+c(4B-1)
\]

for some integer `c>=1`; equivalently the modulus quotient is `4c+1`.

The accompanying script `composite_typeII_layer_pruner.py` computes these sets exactly.

## 2. Prime-index descendants are wholly inherited

Fix an ancestor depth `B`.  Suppose `A>B` is prime and

\[
A\equiv B\pmod{4B-1}.
\]

Then `m_B|m_A`.  Since `A` is prime, the only divisors of `A^2` are

\[
1,A,A^2.
\]

Modulo `m_B`, these reduce to

\[
1,B,B^2,
\]

all of which divide `B^2`.  Hence every trap at depth `A` is inherited from depth `B`.

Dirichlet gives infinitely many such prime `A` for every fixed `B`, because

\[
\gcd(B,4B-1)=1.
\]

This is a useful reproduction check, but it is **not new**: the stronger FCF/CENTL prime-index spectrum theorem already records complete shadow on ancestry edges into prime indices.

## 3. Finite exploratory pruning audit

An independent run through `A=2000` produced:

- 1493 composite-modulus layers;
- 572 completely divisor-modulus redundant composite layers;
- 921 composite layers with at least one primitive residue;
- redundant fraction approximately `0.3831`;
- mean primitive-residue fraction among composite layers approximately `0.3319`.

These are finite exploratory statistics only.

Early completely redundant layers include

\[
A=7,13,16,19,23,29,31,34,37,43,44,47,\ldots
\]

while early layers with primitive residues include

\[
A=4,9,10,14,22,24,25,28,30,36,39,40,\ldots
\]

## 4. Squarefree semiprimes: only two genuinely square-only directions

Let

\[
A=uv
\]

with distinct primes `u,v`.  The divisors of `A^2` are

\[
1,u,v,u^2,uv,v^2,u^2v,uv^2,u^2v^2.
\]

The López boundary pieces (`D|A` or `A|D`) already contain seven of these.  The only genuinely square-completed additions are

\[
\boxed{D=u^2\quad\text{and}\quad D=v^2.}
\]

Since `4uv == 1 (mod 4uv-1)`, their trap residues can be written

\[
\boxed{-4u^2\equiv-u/v},
\qquad
\boxed{-4v^2\equiv-v/u}
\pmod{4uv-1}.
\]

This agrees with the FCF/CENTL squarefree-semiprime mixed-residue description.  Therefore the first nontrivial square-completed composite rescue problem is only a **two-direction problem**, not a nine-divisor problem.

### Paired-inheritance lemma

Along any ancestry edge `m_B|m_A`, the two mixed directions are inherited together.

Indeed, suppose `u^2 mod m_B` equals some divisor `E|B^2`.  Because `A=uv == B (mod m_B)`,

\[
v^2=\frac{A^2}{u^2}
\equiv
\frac{B^2}{E}
\pmod{m_B},
\]

and `B^2/E` is again a divisor of `B^2`.  The converse follows by symmetry.

Thus a squarefree-semiprime layer cannot have exactly one mixed square direction inherited through a fixed ancestor: both survive or both disappear.

## 5. Three tiny ancestors eliminate many semiprime mixed layers

The depths `B=1,2,4` have a special property: their divisor-square residues contain **every unit square** modulo their moduli.

### B = 1, modulus 3

`Div(1^2)={1}`, which is the full nonzero square set modulo `3`.
Thus if

\[
A=uv\equiv1\pmod3,
\]

both mixed squares are inherited from depth `1`.

### B = 2, modulus 7

`Div(2^2)={1,2,4}`, exactly the quadratic residues modulo `7`.
Thus if

\[
A=uv\equiv2\pmod7,
\]

both mixed squares are inherited from depth `2`.

### B = 4, modulus 15

`Div(4^2) mod 15 = {1,2,4,8}`, which contains all unit squares `{1,4}` modulo `15`.
Thus if

\[
A=uv\equiv4\pmod{15},
\]

both mixed squares are inherited from depth `4`.

Therefore a squarefree-semiprime depth can contribute a primitive mixed-square rescue only if it avoids all three congruences

\[
\boxed{
A\not\equiv1\pmod3,
\qquad
A\not\equiv2\pmod7,
\qquad
A\not\equiv4\pmod{15}.
}
\]

As raw residue classes modulo `105`, these three filters remove `45/105 = 3/7` of all index classes.  Among squarefree semiprimes the observed removal is about one half in finite ranges (approximately `51.4%` through `A=100000`), but that latter figure is computational evidence only.

## 6. Important limitation

`P_A` is conservative.  A smaller modulus that does **not** divide `m_A` may still cover CRT subprogressions inside `r mod m_A`.  Thus `P_A != empty` does not mean the entire progression is globally new relative to the full earlier union.

The next stage should therefore operate only on the residual two-direction semiprime core and refine those classes by CRT against earlier primitive layers.

## 7. Next proof target

After ancestry pruning, the strongest concrete target is:

> Prove that every squarefree-semiprime mixed residue surviving the small-ancestor filters is either shadowed by another explicit ancestry family or forces a controlled Type-II successor.

Equivalently, study only

\[
-u/v,\quad -v/u\pmod{4uv-1}
\]

for semiprime indices `uv` outside the three tiny ancestor congruences.

A successful descent, finite transition grammar, or forced successor theorem on this reduced core would attack arithmetic rigidity directly rather than merely improve exceptional-set density.