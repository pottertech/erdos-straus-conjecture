# Asymptotic Anti-Cover Theorem for All-Negative Squarefree Moduli

**Status:** unconditional asymptotic theorem about the square-completed proper-ancestor system. It explains structurally why the former five-factor ancestry-cover conjecture fails. It is not a proof or disproof of the Erdős--Straus conjecture.

## 1. Setup

Fix an odd integer `k>=3`. Let

\[
m=p_1p_2\cdots p_k
\]

be squarefree, where the distinct primes satisfy

\[
p_i\equiv3\pmod4.
\]

Because `k` is odd,

\[
m\equiv3\pmod4.
\]

For every proper divisor

\[
1<d<m,
\qquad d\mid m,
\qquad d\equiv3\pmod4,
\]

put

\[
B_d=\frac{d+1}{4}
\]

and

\[
Q_d:=Q_{B_d}
=\{E\pmod d:E\mid B_d^2\}.
\]

A unit square class `r mod m` is inherited from `d` when

\[
r\pmod d\in Q_d.
\]

Let `C(m)` be the union of all proper-ancestor inherited unit square classes and let

\[
S(m)=QR(m)\setminus C(m)
\]

be the survivor set.

## 2. Exact coverage fraction for one ancestor

Suppose `d` is the product of `j` of the primes, where `j` is odd and `j<k`.

Because `m` is squarefree, CRT gives

\[
QR(m)\cong QR(d)\times QR(m/d).
\]

Therefore reduction from `QR(m)` to `QR(d)` has fibers of equal size. The fraction of global square classes inherited from this one ancestor is exactly

\[
\frac{|Q_d\cap QR(d)|}{|QR(d)|}
\]

and hence at most

\[
\frac{|Q_d|}{|QR(d)|}.
\]

Now

\[
|Q_d|\le \tau(B_d^2),
\]

where `tau` is the divisor-counting function, while

\[
|QR(d)|=\frac{\varphi(d)}{2^j}.
\]

Thus

\[
\boxed{
\frac{|\text{classes inherited from }d|}{|QR(m)|}
\le
\frac{2^j\tau(B_d^2)}{\varphi(d)}.
}
\]

This bound is exact apart from replacing `|Q_d cap QR(d)|` by `|Q_d|`.

## 3. Classical divisor bound

Use the standard estimate

\[
\tau(N)\ll_\varepsilon N^\varepsilon
\]

for every fixed `epsilon>0`.

Applied to `N=B_d^2`, this gives

\[
\tau(B_d^2)\ll_\varepsilon B_d^{2\varepsilon}
\ll_\varepsilon d^{2\varepsilon}.
\]

For fixed `j`, as the smallest prime factor of `d` tends to infinity,

\[
\varphi(d)
=d\prod_{p\mid d}\left(1-\frac1p\right)
=(1+o(1))d.
\]

Hence for every proper ancestor having fixed `j`,

\[
\frac{|\text{classes inherited from }d|}{|QR(m)|}
\ll_{\varepsilon,k}
 d^{-1+2\varepsilon}.
\]

Choosing any fixed `epsilon<1/2` shows that this fraction tends to zero as the smallest prime factor tends to infinity.

## 4. Anti-cover theorem

For fixed odd `k`, the number of proper `3 mod 4` ancestors is finite:

\[
\sum_{\substack{1\le j<k\\j\text{ odd}}}\binom{k}{j}
=2^{k-1}-1.
\]

Let

\[
P=\min_i p_i.
\]

Every nontrivial proper ancestor satisfies `d>=P`. By the union bound and the estimate above,

\[
\frac{|C(m)|}{|QR(m)|}
\le
\sum_{d}\frac{2^{\omega(d)}\tau(B_d^2)}{\varphi(d)}
=o_{k}(1)
\]

as

\[
P\to\infty.
\]

Therefore

\[
\boxed{
\frac{|S(m)|}{|QR(m)|}=1-o_k(1)
}
\]

for squarefree products of a fixed odd number `k` of distinct `3 mod 4` primes whose smallest prime factor tends to infinity.

In particular:

\[
\boxed{
\text{for every fixed odd }k\ge3,
\text{ all sufficiently large such moduli have proper-ancestor survivors.}
}
\]

This is the opposite asymptotic behavior from the former ancestry-cover conjecture: proper ancestors cover a vanishing fraction of square classes rather than all of them.

## 5. Five-factor consequence

For `k=5`, the proper `3 mod 4` ancestors are exactly the five one-prime products and the ten three-prime products, for a total of 15.

Hence if

\[
m=p_1p_2p_3p_4p_5,
\qquad p_i\equiv3\pmod4,
\]

and the five primes are all sufficiently large, then not only does an ancestry survivor exist, but the proportion of unit square classes that survive tends to `1` as `min p_i -> infinity`.

The explicit counterexample

\[
6,407,731=11\cdot19\cdot23\cdot31\cdot43
\]

shows that survivor behavior begins already at the first admissible all-negative five-prime modulus after excluding the universal prime ancestors `3` and `7`.

## 6. Exact first example

For

\[
m=6,407,731,
\]

the global square group has

\[
|QR(m)|
=\prod_{p\mid m}\frac{p-1}{2}
=155,925
\]

classes.

The explicit regression in `verify_all_negative_five_factor_counterexample.py` verifies that

\[
r=3,990,232
\]

survives all 15 proper ancestors.

A complete CRT enumeration performed during the audit found `3,824` survivors for this modulus, about `2.45%` of all unit square classes. This numerical percentage is finite evidence only; the asymptotic theorem above is independent of that enumeration.

## 7. Strategic consequence

Proper-ancestor inheritance cannot be the missing universal mechanism in the all-negative branch. Any successful global Type-II strategy must add information not contained in the union of lower-depth square-completed ancestor sets.

Possible additional mechanisms include:

1. the full current depth `Q_{(m+1)/4}` rather than proper ancestors only;
2. Type-I certificates;
3. relations coupling the depth index `A=(m+1)/4` to the factorization of `m`;
4. a descent using parameters other than proper modulus divisors.

The mixed-signature descent through `1 mod 4` prime factors remains valid and is logically separate from this anti-cover theorem.

## 8. Reference for the analytic input

The only asymptotic input needed is the classical divisor bound

\[
\tau(N)\ll_\varepsilon N^\varepsilon.
\]

This is standard in multiplicative number theory; for example it is recorded as the crude divisor bound in modern analytic-number-theory treatments. No delicate sieve theorem is required here.

## Claim boundary

This theorem concerns only the **proper-ancestor coverage model**. A surviving square class modulo `m` is not an Erdős--Straus counterexample. The theorem shows that a proposed proof mechanism is asymptotically insufficient in the all-negative squarefree regime.