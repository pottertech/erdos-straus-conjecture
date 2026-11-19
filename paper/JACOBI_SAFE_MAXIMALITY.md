# Maximality of the `3q` Backbone for Jacobi-Safe CRT

**Status:** unconditional structural theorem. This strengthens the earlier square-safe maximality result. No publication-priority claim is made pending comparison with the full reciprocity/ancestry literature.

For

\[
m_A=4A-1,
\]

write the parity vector of its prime factorization as

\[
v_A=(v_p(m_A))_{p\ {m prime}}\in\mathbf F_2^{(\mathcal P)},
\qquad
v_p(m_A)=\operatorname{ord}_p(m_A)\pmod2.
\]

Equivalently, `v_A` records the squarefree kernel of `m_A` modulo squares.

For every integer `n` coprime to `m_A`, the Jacobi character is

\[
\chi_A(n):=\left(\frac{n}{m_A}\right)
=\prod_p\left(\frac np\right)^{v_p(m_A)}.
\]

Thus multiplication of Jacobi characters corresponds exactly to addition of parity vectors over `F_2`.

The divisor-square trap residues at depth `A` satisfy

\[
\boxed{
\chi_A(-4D)=-1
\qquad(D\mid A^2),
}
\]

by the divisor-Jacobi reciprocity lemma.

## Theorem 1: span classification

Let

\[
V_{A-1}=\operatorname{span}_{\mathbf F_2}\{v_B:1\le B<A\}.
\]

Then

\[
\boxed{
v_A\notin V_{A-1}}
\]

if and only if one of the following holds:

1. `m_A=q` is prime (necessarily `q == 3 mod 4`);
2. `m_A=3q`, where `q == 1 mod 4` is prime.

Equivalently, for every other composite target modulus,

\[
\boxed{v_A\in V_{A-1}.}
\]

### Proof

Let `r` be a prime divisor of `m_A` that occurs to odd exponent.

### Prime coordinate `r == 3 mod 4`

The depth

\[
B_r=\frac{r+1}{4}
\]

is integral and satisfies

\[
m_{B_r}=4B_r-1=r.
\]

Hence the unit vector `e_r` occurs as an earlier parity vector unless

\[
B_r=A.
\]

But `B_r=A` is equivalent to

\[
m_A=r,
\]

i.e. the target modulus itself is the prime `r`.

Thus, outside the prime-target case, every target coordinate `r == 3 mod 4` is individually contained in `V_{A-1}`.

### Prime coordinate `r == 1 mod 4`

The depth

\[
C_r=\frac{3r+1}{4}
\]

is integral and satisfies

\[
m_{C_r}=3r.
\]

Its parity vector is

\[
v_{C_r}=e_3+e_r.
\]

Also

\[
m_1=3,
\qquad v_1=e_3.
\]

Therefore, whenever `C_r<A`,

\[
e_r=v_{C_r}+v_1\in V_{A-1}.
\]

The only way `C_r=A` is

\[
m_A=3r.
\]

Thus, outside a target of the form `3q` with `q == 1 mod 4` prime, every target coordinate `r == 1 mod 4` is individually contained in `V_{A-1}`.

If the target is neither prime nor `3q` prime, every unit coordinate occurring in `v_A` belongs to `V_{A-1}`. Therefore their sum `v_A` also belongs to `V_{A-1}`.

Conversely, if `m_A=q` is prime, the new coordinate `e_q` has not appeared earlier. If `m_A=3q` with `q == 1 mod 4` prime, the coordinate `q` first appears only at depth `A`; the earlier span contains `e_3` but not `e_q`, so `e_3+e_q=v_A` is not in the earlier span.

This proves the classification.

## Theorem 2: maximality of Jacobi-safe CRT

Consider any exact-depth construction that attempts to avoid every earlier layer solely by enforcing

\[
\boxed{
\chi_B(n)=+1
\qquad\text{for every }B<A.
}
\]

Such a construction can succeed at a composite target depth only when

\[
\boxed{
4A-1=3q,
\qquad q\equiv1\pmod4\text{ prime}.
}
\]

### Proof

Suppose first that the target modulus is composite and not of the form `3q` with `q` prime. By Theorem 1,

\[
v_A=\sum_{B\in S}v_B
\]

for some finite subset `S` of earlier depths.

For every integer `n` coprime to the relevant moduli,

\[
\chi_A(n)
=
\prod_{B\in S}\chi_B(n).
\]

If the construction enforces

\[
\chi_B(n)=+1
\]

at every earlier depth, then

\[
\chi_A(n)=+1.
\]

But a target divisor-square witness has

\[
n\equiv-4D\pmod{m_A},
\qquad D\mid A^2,
\]

and therefore

\[
\chi_A(n)=\chi_A(-4D)=-1.
\]

Contradiction.

Thus no Jacobi-safe CRT construction can produce an exact-depth target outside the prime and `3q` cases.

For a composite target `m_A=3q`, the earlier span fixes only the `3`-coordinate. The Jacobi-safe requirement at the earlier modulus `3` is

\[
\left(\frac{-4D}{3}\right)=+1,
\]

which is equivalent to

\[
D\equiv2\pmod3.
\]

This is exactly the structural `3q` backbone criterion already proved. Hence the `3q` family is both possible and maximal.

## Corollary: hierarchy of exact-depth mechanisms

There is a strict conceptual hierarchy:

\[
\boxed{
\text{square-safe CRT}
\subseteq
\text{Jacobi-safe CRT}
\subsetneq
\text{full branch-dependent CRT/CSP}.
}
\]

For composite target moduli, the first two mechanisms have the same maximal symbolic backbone:

\[
4A-1=3q,
\qquad q\equiv1\pmod4\text{ prime}.
\]

The full CSP mechanism is strictly stronger: the certified layers `A=649` and `A=22339` lie outside the `3q` family and are not Jacobi-safe, yet possess exact reduced survivor progressions.

This explains why those layers genuinely require finer branch-dependent congruence information rather than a global quadratic-character sign choice.

## Finite regression

An incremental parity-vector computation through `A <= 10000` finds exactly the two classes predicted by Theorem 1 as new vectors:

- prime `m_A`;
- `m_A=3q` with prime `q == 1 mod 4`.

No other exception occurs in that range. This computation is only a regression check; the proof above is symbolic.

## Prior-art boundary

The relation between divisor classes and Jacobi-sign kernels has close antecedents in FCF/CENTL reciprocity work, including Type A/B divisor-Jacobi statements and signature-space methods. No novelty is claimed for representing quadratic characters by `F_2` parity vectors.

The candidate contribution is the exact first-occurrence span classification for the moduli `4A-1` and its consequence that the `3q` family is maximal for every global Jacobi-safe CRT exact-depth construction.

This theorem does not imply universal Type-II solvability or the Erdős--Straus conjecture.