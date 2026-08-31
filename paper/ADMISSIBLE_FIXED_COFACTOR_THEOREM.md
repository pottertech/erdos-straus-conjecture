# Admissible Fixed-Cofactor Exact-Depth Theorem

**Status:** unconditional theorem schema. This unifies the previously proved fixed-cofactor families. It is a theorem about exact square-completed Type-II depth, not a proof of the Erdos--Straus conjecture. Novelty/priority remains subject to dedicated literature review.

## 1. Admissible fixed pair

Let `s>1` be a fixed odd integer with

\[
s\equiv 3\pmod 4,
\]

and let `d>=1` satisfy

\[
\gcd(s,4d)=1.
\]

Let `a` be the reduced residue class

\[
\boxed{a\equiv -s^{-1}\pmod{4d}.}
\]

Assume the following two local character conditions.

1. The target is square on every prime divisor of the fixed cofactor:

\[
\boxed{
\left(\frac{-d}{q}\right)=+1
\quad\text{for every prime }q\mid s.
}
\]

2. The target is nonsquare on the variable prime throughout the parameter progression: for every prime

\[
r\equiv a\pmod{4d}
\]

outside a finite set (equivalently, for the reduced classes under consideration),

\[
\boxed{
\left(\frac{-d}{r}\right)=-1.
}
\]

Call such a pair `(s,d)` **admissible**.

For a prime parameter `r` in the progression, define

\[
A=\frac{sr+1}{4}.
\]

Because `sr+1==0 (mod 4d)`, we have

\[
\boxed{d\mid A,}
\]

hence `d|A^2`. The target square-completion residue is

\[
\boxed{n\equiv -4d\pmod{sr}.}
\]

By admissibility, this target is a quadratic residue at every fixed prime coordinate dividing `s` and a quadratic nonresidue at the single variable coordinate `r`.

## 2. Reduction to finitely many exceptional layers

Choose square-safe CRT coordinates at every prime power not involving `r`, while preserving the required target residues on the prime factors of `s`. By the universal square-safe lemma, every earlier square-completed Type-II layer whose modulus is not divisible by `r` is avoided automatically.

After excluding the finitely many parameter primes `r<=s`, an earlier modulus containing `r` has the form

\[
4B-1=cr,
\]

where

\[
0<c<s,
\qquad
c\equiv3\pmod4.
\]

Thus only finitely many fixed cofactors `c` can occur.

## 3. Master exceptional-layer equation

Fix such a cofactor `c`, and put

\[
B=\frac{cr+1}{4}.
\]

Suppose a collision occurs at depth `B`. Then there exists a divisor

\[
E\mid B^2
\]

compatible with the target residue. The congruence modulo the variable prime gives

\[
E\equiv d\pmod r,
\]

so write

\[
E=rk+d,
\qquad k\ge0.
\]

Let

\[
F=\frac{B^2}{E}.
\]

The complementary congruence gives

\[
16dF=rh+1
\]

for some integer `h>=0`. Multiplying

\[
(rk+d)(rh+1)=16dB^2=d(cr+1)^2
\]

and cancelling the constant term yields the exact identity

\[
\boxed{
r(kh-dc^2)+k+dh-2dc=0.
}
\]

If `kh>dc^2`, then

\[
r(kh-dc^2)=2dc-k-dh.
\]

But AM--GM gives

\[
k+dh\ge2\sqrt{dkh}>2dc,
\]

so the right side is negative while the left side is positive, impossible.

If `kh=dc^2`, equality in AM--GM forces

\[
k=dc,\qquad h=c.
\]

This equality case is equivalent to the additional divisibility

\[
4d\mid B,
\]

or

\[
\boxed{16d\mid cr+1.}
\]

For any fixed `(s,d,c)`, this either is incompatible with the chosen parameter progression or contributes at most a fixed subprogression that can be separated explicitly. Outside that equality configuration, every collision therefore satisfies

\[
\boxed{kh<dc^2.}
\]

Hence, for fixed `s,d,c`, there are only finitely many possible pairs `(k,h)`. For each pair the master equation determines at most one rational value

\[
\boxed{
r=\frac{k+dh-2dc}{dc^2-kh}.}
\]

Consequently each exceptional cofactor `c` produces only finitely many possible collision parameters `r` (plus the explicitly handled equality configuration).

Since only finitely many `c<s` occur, the union of all bad parameter primes is finite.

## 4. Admissible-pair theorem

Dirichlet's theorem gives infinitely many primes

\[
r\equiv a\pmod{4d}
\]

because `a` is reduced. Removing the finite collision set leaves infinitely many prime parameters. For every remaining `r`, CRT supplies a reduced progression satisfying the target congruence at depth `A` and avoiding every earlier square-completed Type-II trap. Dirichlet applied to that refined progression then gives infinitely many primes `p` with

\[
\boxed{
\delta_{\rm sq}(p)=\frac{sr+1}{4}.
}
\]

Therefore:

> **Admissible fixed-cofactor theorem.**  For every admissible fixed pair `(s,d)`, all but finitely many prime parameters
> \[
> r\equiv -s^{-1}\pmod{4d}
> \]
> generate an exact square-completed Type-II depth
> \[
> \boxed{A=(sr+1)/4}
> \]
> that is realized by infinitely many primes.

## 5. Counting consequence

For each fixed admissible pair `(s,d)`, deleting finitely many prime parameters does not change the asymptotic count. The family contributes

\[
\boxed{
\frac{4}{s\varphi(4d)}\frac{X}{\log X}
}
\]

exact depths up to `X`.

For any fixed finite collection of admissible pairs whose target factorizations are distinct apart from finitely many swapped-prime coincidences, the contributions add after discarding those finite overlaps.

## 6. Previously proved families as instances

This theorem schema contains the explicit fixed-cofactor constructions already established on the research branch:

- `s=7, d=3`, parameter class `r==5 (mod 12)`;
- `s=11, d=6`, parameter class `r==13 (mod 24)`;
- `s=19, d=10`, parameter class `r==21 (mod 40)`;
- `s=23, d=20`, parameter class `r==73 (mod 80)`;
- the certified `s=31,43,47,59,67` rows;
- for every prime `s==3 (mod 8)`, the canonical choice
  \[
  d=(s+1)/2,
  \]
  which yields the infinite hierarchy proved in `INFINITE_FIXED_COFACTOR_HIERARCHY.md`.

The explicit small-family notes remain useful because they provide transparent collision tables, while the present theorem isolates the reusable mechanism.

## Claim boundary

The local quadratic-coordinate mechanism has close antecedents in contemporary reciprocity/square-lift work. The candidate contribution here is the fixed-cofactor **exact-first-hit finite-exception theorem** and its use to generate infinite exact-depth backbones. Do not claim novelty or priority without a dedicated literature audit.