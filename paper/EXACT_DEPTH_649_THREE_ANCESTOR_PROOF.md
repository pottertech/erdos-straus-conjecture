# Exact Square Depth 649 from Three Exceptional Ancestors

**Status:** unconditional theorem with only twelve small finite local checks. This replaces the large CSP as a proof of the four explicit depth-649 branches. No novelty claim pending literature comparison.

Take

\[
A=649=11\cdot59,
\qquad
m_A=4A-1=2595=3\cdot5\cdot173.
\]

Consider the four target divisors

\[
\boxed{D\in\{11,59,7139,38291\}},
\]

where

\[
7139=11^2\cdot59,
\qquad
38291=11\cdot59^2,
\]

so every `D` divides `649^2`.

For each such `D`, put

\[
t_D\equiv-4D\pmod{2595}.
\]

We prove that infinitely many primes `p` satisfy

\[
\delta_{\rm sq}(p)=649
\]

with target witness `(649,D)`.

---

## 1. Local character pattern of the four target branches

For all four target divisors,

\[
t_D\equiv1\pmod3.
\]

Modulo `5`, one has

\[
t_D\equiv1\text{ or }4\pmod5,
\]

so the target class is a square modulo `5`.

Modulo `173`, the target classes are

\[
\begin{array}{c|cccc}
D&11&59&7139&38291\\ \hline
t_D\bmod173&129&110&162&114
\end{array}
\]

and each is a quadratic nonresidue modulo `173`.

Thus the only nonsquare prime coordinate of the target modulus is the factor `173`.

---

## 2. A global CRT residue on all earlier moduli

Let

\[
L=\operatorname{lcm}_{1\le B<649}(4B-1).
\]

We prescribe a residue `c_D` modulo the prime-power coordinates of `L` as follows.

1. On the `173`-coordinate,
   \[
   c_D\equiv t_D\pmod{173}.
   \]

2. On every power of `5` occurring in `L`, set
   \[
   c_D\equiv t_D\pmod5
   \]
   using the literal integer `1` or `4`. Both are squares modulo every power of `5`.

3. On every other prime-power coordinate of `L`, set
   \[
   c_D\equiv1.
   \]

By CRT this defines a reduced residue class modulo `L`.

It is compatible with the target condition

\[
p\equiv t_D\pmod{2595},
\]

because the common prime factors of `2595` and `L` are among `3,5,173`, and the prescribed residues agree with `t_D` modulo each of those primes.

We also impose

\[
p\equiv1\pmod4.
\]

---

## 3. Every earlier modulus not containing 173 is automatically safe

Let

\[
m_B=4B-1,
\qquad B<649,
\]

and suppose `173` does not divide `m_B`.

Every prime-power component of `c_D mod m_B` is then either `1`, or the component `4` on a power of `5`. Hence

\[
c_D\pmod{m_B}
\]

is a unit square modulo `m_B`.

For every divisor `E|B^2`, the Type-II trap residue

\[
-4E\pmod{m_B}
\]

has Jacobi symbol `-1` modulo `m_B`, whereas a unit square has Jacobi symbol `+1`. Therefore

\[
c_D\notin\{-4E\pmod{m_B}:E\mid B^2\}.
\]

So every earlier layer not divisible by `173` is excluded simultaneously by the universal square-safe/Jacobi obstruction.

---

## 4. There are only three earlier moduli containing 173

Because

\[
4B-1<4\cdot649-1=2595
\]

and `173==1 (mod 4)`, any earlier modulus divisible by `173` has the form

\[
4B-1=173s,
\qquad s\equiv3\pmod4,
\qquad s<15.
\]

Thus

\[
s\in\{3,7,11\}.
\]

The only exceptional earlier depths are therefore

\[
\boxed{B=130,303,476},
\]

with moduli

\[
519=3\cdot173,
\qquad
1211=7\cdot173,
\qquad
1903=11\cdot173.
\]

On these moduli the global CRT class is respectively the unique class satisfying

\[
\begin{array}{ll}
B=130:& p\equiv t_D\pmod{173},\quad p\equiv1\pmod3,\\
B=303:& p\equiv t_D\pmod{173},\quad p\equiv1\pmod7,\\
B=476:& p\equiv t_D\pmod{173},\quad p\equiv1\pmod{11}.
\end{array}
\]

A target collision at depth `B` would require a divisor `E|B^2` with

\[
-4E\equiv c_D\pmod{4B-1}.
\]

Equivalently, `E` would have to lie in the following residue class modulo `4B-1`:

\[
\begin{array}{c|rrrr}
B & D=11 & D=59 & D=7139 & D=38291\\ \hline
130 & 11 & 59 & 392 & 404\\
303 & 530 & 1097 & 565 & 404\\
476 & 184 & 1097 & 1603 & 404
\end{array}
\]

Direct enumeration of the divisors of the three fixed squares

\[
130^2,\qquad303^2,\qquad476^2
\]

shows that none of these twelve residue classes occurs. The check involves only `27`, `9`, and `45` divisors respectively and is reproduced by `verify_depth_649_three_ancestor.py`.

Hence all three exceptional earlier layers are avoided for all four target branches.

---

## 5. Dirichlet conclusion

Combine the congruences

\[
p\equiv t_D\pmod{2595},
\qquad
p\equiv c_D\pmod L,
\qquad
p\equiv1\pmod4.
\]

They are CRT-compatible by construction.

The resulting progression is reduced:

- every coordinate other than `173` is `1` or `4`, hence nonzero;
- the `173`-coordinate is one of `129,110,162,114`, also nonzero;
- each target residue `t_D=-4D` is a unit modulo `2595` because `D|649^2` and `gcd(649,2595)=1`.

Dirichlet's theorem therefore gives infinitely many prime members.

Every such prime has a depth-649 target witness `(649,D)` and, by Sections 3--4, has no square-completion Type-II witness at any depth `B<649`. Therefore

\[
\boxed{\delta_{\rm sq}(p)=649}
\]

for infinitely many primes in each of the four target branches.

## Theorem

For each

\[
D\in\{11,59,7139,38291\},
\]

there is a reduced arithmetic progression containing infinitely many primes `p` such that

\[
\boxed{\delta_{\rm sq}(p)=649}
\]

with target witness `(649,D)`.

The proof uses the universal square-safe obstruction on every earlier modulus except the three fixed ancestors `130,303,476`, followed by twelve finite divisor checks.

## Significance

The original exact-depth-649 proof used a full branch-dependent CSP over all `648` earlier layers. The present argument shows that the global obstruction has **rank-one local complexity**: one nonsquare target prime coordinate (`173`) creates only three exceptional ancestor layers; all remaining layers are dispatched at once by quadratic-residue safety.

This gives a substantially more conceptual explanation for the exact depth `649` result and suggests a general research mechanism: target moduli with only one nonsquare prime coordinate and few earlier multiples of that prime may admit finite-exception CRT proofs beyond the Jacobi-safe `3q` backbone.

## Claim boundary

This proves exact square-completion Type-II depth `649`; it does not prove the Erdős--Straus conjecture or universal Type-II solvability. The twelve local checks are finite exact verification, not an asymptotic assumption.