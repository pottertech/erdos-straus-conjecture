# Quantitative Exceptional-Set Bound for the Composite Exact-Depth Backbone

**Status:** unconditional theorem, conditional only on standard published sieve inputs (Bombieri--Vinogradov and the upper-bound half-dimensional sieve). No novelty claim is made for the sieve machinery itself.

For primes

\[
q\equiv1\pmod4,
\qquad
A_q=\frac{3q+1}{4},
\]

let

\[
\mathcal E(Y)
=
\left\{q\le Y:q\text{ prime},\ q\equiv1\pmod4,
\ A_q\text{ has no prime divisor }\ell\equiv2\pmod3\right\}.
\]

The structural theorem in `COMPOSITE_EXACT_DEPTH_INFINITE_FAMILY.md` shows that every prime parameter outside \(\mathcal E(Y)\) yields a composite target depth \(A_q\) that is realized as exact square-completion Type-II depth by infinitely many primes.

## Theorem 1: quantitative exceptional-set bound

\[
\boxed{
|\mathcal E(Y)|
\ll
\frac{Y}{(\log Y)^{3/2}}.
}
\]

Consequently

\[
\boxed{
\frac{|\mathcal E(Y)|}{\pi(Y;4,1)}
\ll
\frac1{\sqrt{\log Y}}.
}
\]

Thus the earlier relative-density-one theorem has an explicit rate of convergence.

## Proof

We apply an upper-bound sieve to the prime sequence

\[
\mathcal A(Y)
=
\left\{A_q=\frac{3q+1}{4}:
q\le Y,\ q\text{ prime},\ q\equiv1\pmod4\right\}.
\]

Let

\[
\mathcal P
=
\{\ell:\ell\text{ odd prime},\ \ell\equiv2\pmod3\}.
\]

For a squarefree integer \(d\) supported on \(\mathcal P\), the condition \(d\mid A_q\) is equivalent to

\[
3q\equiv-1\pmod d,
\qquad
q\equiv1\pmod4.
\]

By CRT there is a unique reduced residue class \(a_d\pmod{4d}\) satisfying these two congruences. Hence

\[
|\mathcal A_d(Y)|
:=
\#\{q\le Y:q\text{ prime},\ q\equiv1\pmod4,\ d\mid A_q\}
=
\pi(Y;4d,a_d).
\]

Take

\[
X=\frac12\operatorname{Li}(Y).
\]

Since \(d\) is odd,

\[
\varphi(4d)=2\varphi(d),
\]

so the expected local density relative to the base class \(q\equiv1\pmod4\) is

\[
g(d)=\frac1{\varphi(d)}.
\]

For a prime \(\ell\in\mathcal P\),

\[
\boxed{g(\ell)=\frac1{\ell-1}.}
\]

Thus

\[
|\mathcal A_d(Y)|
=Xg(d)+r_d(Y),
\]

with

\[
r_d(Y)
=
\pi(Y;4d,a_d)-\frac{\operatorname{Li}(Y)}{\varphi(4d)}.
\]

### 1. Sieve dimension

Define the sifting product

\[
V(z)
=
\prod_{\substack{\ell<z\\ \ell\in\mathcal P}}
\left(1-\frac1{\ell-1}\right).
\]

Because

\[
\frac1{\ell-1}=\frac1\ell+O\!\left(\frac1{\ell^2}\right)
\]

and Mertens' theorem in arithmetic progressions gives

\[
\sum_{\substack{\ell<z\\ \ell\equiv2\ (3)}}\frac1\ell
=
\frac12\log\log z+O(1),
\]

we obtain

\[
\log V(z)
=-\frac12\log\log z+O(1),
\]

hence

\[
\boxed{V(z)\asymp(\log z)^{-1/2}.}
\]

This is a sieve of dimension \(1/2\).

### 2. Level of distribution

Bombieri--Vinogradov implies that for every fixed \(A_0>0\) there is \(B=B(A_0)\) such that, with

\[
D=\frac{Y^{1/2}}{(\log Y)^B},
\]

one has

\[
\sum_{d\le D}
\max_{(a,4d)=1}
\left|
\pi(Y;4d,a)-\frac{\operatorname{Li}(Y)}{\varphi(4d)}
\right|
\ll_{A_0}
\frac{Y}{(\log Y)^{A_0}}.
\]

Restricting to squarefree \(d\) supported on \(\mathcal P\) can only decrease this sum, so

\[
\sum_{\substack{d\le D\\p\mid d\Rightarrow p\in\mathcal P}}
|r_d(Y)|
\ll_{A_0}
\frac{Y}{(\log Y)^{A_0}}.
\]

### 3. Upper-bound half-dimensional sieve

Choose a fixed admissible sieve parameter \(s>1\) and put

\[
z=D^{1/s}.
\]

Then \(\log z\asymp\log Y\). The standard upper-bound beta sieve in dimension \(1/2\) gives

\[
S(\mathcal A,\mathcal P,z)
\ll
X V(z)
+
\sum_{d\le D}|r_d(Y)|.
\]

Using the two estimates above,

\[
S(\mathcal A,\mathcal P,z)
\ll
\frac{Y}{\log Y}\frac1{\sqrt{\log Y}}
+
\frac{Y}{(\log Y)^{A_0}}.
\]

Taking \(A_0>3/2\),

\[
\boxed{
S(\mathcal A,\mathcal P,z)
\ll
\frac{Y}{(\log Y)^{3/2}}.
}
\]

Every parameter in \(\mathcal E(Y)\) has no prime factor from \(\mathcal P\) at all, and therefore in particular avoids every \(\ell<z\) from \(\mathcal P\). Hence

\[
|\mathcal E(Y)|
\le
S(\mathcal A,\mathcal P,z),
\]

which proves the theorem.

The prime \(2\equiv2\pmod3\) was omitted from \(\mathcal P\) only to keep the odd-modulus bookkeeping clean. Omitting a sieving prime enlarges the sifted set, so the upper bound remains valid.

## Corollary 2: quantitative exact-depth count

Let

\[
N_{\rm comp}(X)
=
\#\{A\le X:4A-1\text{ composite and infinitely many primes }p
\text{ satisfy }\delta_{\rm sq}(p)=A\}.
\]

Set

\[
Y=\frac{4X-1}{3}.
\]

The map

\[
q\mapsto A_q=\frac{3q+1}{4}
\]

is injective. Every prime \(q\equiv1\pmod4\) outside \(\mathcal E(Y)\) contributes a distinct exact depth \(A_q\le X\). Therefore

\[
N_{\rm comp}(X)
\ge
\pi(Y;4,1)-|\mathcal E(Y)|.
\]

The fixed-modulus prime number theorem and Theorem 1 give

\[
\boxed{
N_{\rm comp}(X)
\ge
\frac12\operatorname{Li}\!\left(\frac{4X-1}{3}\right)
-
O\!\left(\frac{X}{(\log X)^{3/2}}\right).
}
\]

In particular,

\[
N_{\rm comp}(X)
\ge
\left(\frac23+O\!\left(\frac1{\sqrt{\log X}}\right)\right)
\frac{X}{\log X}
\]

in the lower-bound sense, and hence recovers the earlier

\[
N_{\rm comp}(X)
\ge
\left(\frac23+o(1)\right)\frac{X}{\log X}.
\]

## Interpretation

The earlier theorem said that the structural factor criterion succeeds for relative density one of prime parameters \(q\equiv1\pmod4\). The present theorem quantifies the exceptional set:

\[
\boxed{
\text{exceptional proportion among }q\equiv1\pmod4
=O((\log Y)^{-1/2}).
}
\]

The exponent \(3/2\) has the expected sieve interpretation:

- one factor \((\log Y)^{-1}\) comes from requiring \(q\) itself to be prime;
- one factor \((\log Y)^{-1/2}\) comes from requiring \((3q+1)/4\) to avoid the half-density set of primes \(\ell\equiv2\pmod3\).

This is structurally consistent with classical half-dimensional-sieve phenomena and with the \((\log N)^{-3/2}\) scale that appears in recent Erd\H{o}s--Straus sieve work, although the sets being counted are different.

## Inputs and claim boundary

The new candidate contribution is the application of the standard half-dimensional upper-bound sieve to this exact-depth exceptional set. The analytic inputs are standard prior mathematics:

1. Bombieri--Vinogradov for primes in arithmetic progressions;
2. Mertens' theorem for primes in the progression \(2\pmod3\);
3. the upper-bound beta/half-dimensional sieve (Iwaniec, 1976; later standard formulations).

The theorem does **not** give a matching lower bound for \(|\mathcal E(Y)|\). In particular, it does not prove

\[
|\mathcal E(Y)|\asymp Y(\log Y)^{-3/2}.
\]

A matching lower bound would require substantially more information and is not claimed.

The theorem also does not imply universal Type-II solvability or the Erd\H{o}s--Straus conjecture.