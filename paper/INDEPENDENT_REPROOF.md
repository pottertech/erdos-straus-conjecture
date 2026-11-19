# Independent Reconstruction of the Composite Exact-Depth Theorem

**Purpose.** This note independently reconstructs the symbolic theorem used in the manuscript without relying on the manuscript proof order or its computational examples. It is an audit trail, not a novelty claim.

## 1. Setup

For a prime denominator `p == 1 (mod 4)`, define

\[
\delta_{\rm sq}(p)
=
\min\{A\ge1:\exists D\mid A^2,\ 4A-1\mid p+4D\}.
\]

Fix a prime

\[
q\equiv1\pmod4,
\qquad
A=\frac{3q+1}{4}.
\]

Then

\[
4A-1=3q.
\]

Assume that `A` has a divisor

\[
D\mid A^2,
\qquad
D\equiv2\pmod3.
\]

We will reconstruct from first principles why infinitely many primes have exact square-completion depth `A`.

## 2. Safe residue lemma

For every positive integer `B` and every `E|B^2`,

\[
1\not\equiv -4E\pmod{4B-1}.
\]

Equivalently,

\[
4B-1\nmid4E+1.
\]

A short proof is as follows. Let

\[
g=\gcd(B,E),\qquad B=ga,\qquad E=gd,\qquad\gcd(a,d)=1.
\]

Since `E|B^2`, one has `d|g`; write `g=dh`. Thus

\[
B=dha,
\qquad
E=d^2h.
\]

If `4B-1 | 4E+1`, then modulo `4B-1`,

\[
E\equiv-B.
\]

Hence

\[
4B-1\mid E+B=dh(d+a).
\]

But `gcd(4B-1,dh)=1`, so `4B-1|d+a`, impossible because

\[
4dha-1>d+a.
\]

Therefore residue `1` is safe at every depth.

## 3. The new prime q cannot occur in an earlier modulus

Let `B<A` and put

\[
m_B=4B-1.
\]

Suppose `q|m_B`. Since `q == 1 (mod 4)` while `m_B == 3 (mod 4)`, the quotient

\[
s=\frac{m_B}{q}
\]

must satisfy `s == 3 (mod 4)`, so `s>=3`. Consequently

\[
m_B\ge3q=4A-1,
\]

contradicting `B<A`.

Thus

\[
q\nmid m_B
\]

for every earlier depth. Since the target modulus is `3q`, it follows that

\[
\gcd(3q,m_B)\mid3.
\]

This is the only gcd fact needed.

## 4. Compatibility of the target residue with the universal safe residue

The target witness `D` imposes

\[
p\equiv-4D\pmod{3q}.
\]

Because `D == 2 (mod 3)`,

\[
-4D\equiv1\pmod3.
\]

Therefore, for every earlier modulus `m_B`, the target congruence is compatible with

\[
p\equiv1\pmod{m_B},
\]

because every common divisor of `3q` and `m_B` divides `3` and the two residues agree modulo `3`.

Let

\[
L=\operatorname{lcm}_{1\le B<A}(4B-1).
\]

Then the simultaneous system

\[
p\equiv-4D\pmod{3q},
\qquad
p\equiv1\pmod L,
\qquad
p\equiv1\pmod4
\]

is CRT-compatible.

## 5. Exactness of the resulting depth

Let

\[
p\equiv p_0\pmod M,
\qquad
M=\operatorname{lcm}(4,3q,L),
\]

be the CRT class.

For every `B<A`, one has

\[
p\equiv1\pmod{4B-1}.
\]

By the safe-residue lemma, no divisor `E|B^2` can satisfy

\[
4B-1\mid p+4E.
\]

Hence no earlier square-completion witness exists.

At depth `A`, however,

\[
p\equiv-4D\pmod{3q}
\]

and `D|A^2`, so the target witness exists. Therefore every integer in this progression has square-completion depth exactly `A`, provided it lies in the prime-domain under consideration.

## 6. Reducedness and Dirichlet

Every prime divisor inherited from `L` sees residue `1`. The target modulus contributes the prime `q`; but `q\nmid A` because

\[
4A=3q+1\equiv1\pmod q.
\]

Hence `q\nmid D`, since `D|A^2`, and the target residue `-4D` is nonzero modulo `q`. The residue modulo `4` is `1`.

Thus

\[
\gcd(p_0,M)=1.
\]

Dirichlet's theorem gives infinitely many primes in the CRT progression. Every such prime satisfies

\[
\delta_{\rm sq}(p)=A.
\]

This independently reproduces the structural theorem.

## 7. Prime-factor form

If `A=(3q+1)/4` has any prime divisor

\[
\ell\equiv2\pmod3,
\]

then taking `D=ell` satisfies the hypothesis. Therefore

\[
q\equiv1\pmod4,
\quad
A=\frac{3q+1}{4},
\quad
A\text{ has a prime factor }2\pmod3
\]

implies that `A` is realized as exact square-completion depth for infinitely many primes.

## 8. Density-one reconstruction

For each odd prime `ell == 2 (mod 3)`, the condition `ell|A` is equivalent to one reduced residue class of `q` modulo `4ell`, because

\[
3q\equiv-1\pmod{4\ell}.
\]

Within the primes `q == 1 (mod 4)`, a fixed odd `ell` therefore captures relative density

\[
\frac1{\ell-1}.
\]

The factor `ell=2` captures relative density `1/2` through `q == 5 (mod 8)`.

For any finite set `S` of odd primes `ell == 2 (mod 3)`, CRT and the prime number theorem in fixed arithmetic progressions give exact relative density

\[
\frac12\prod_{\ell\in S}\left(1-\frac1{\ell-1}\right)
\]

for primes `q == 1 (mod 4)` avoiding the factor `2` and every prime in `S`.

Since

\[
\sum_{\ell\equiv2(3)}\frac1\ell=\infty,
\]

the finite products tend to zero. Taking the prime-size limit first for each fixed finite `S`, and only then enlarging `S`, proves that the successful structural condition has relative density `1` among primes `q == 1 (mod 4)`.

Because the map

\[
q\mapsto A=\frac{3q+1}{4}
\]

is injective and `A<=X` exactly when `q<=(4X-1)/3`, the prime number theorem in the class `1 mod 4` yields

\[
N_{\rm comp}(X)
\ge
\left(\frac23+o(1)\right)\frac{X}{\log X}.
\]

## 9. Audit conclusion

The symbolic theorem and the density-one corollary reconstruct without the computational certificates at depths 649 or 22339. Those examples are therefore supplementary rather than logically necessary to the main result.

This note does not establish publication priority. It establishes only that the current manuscript's central implication chain can be independently reconstructed from elementary congruence arguments plus Dirichlet/PNT in arithmetic progressions.