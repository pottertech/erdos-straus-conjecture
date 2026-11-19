# An Infinite `7r` Exact-Depth Backbone Beyond the Jacobi-Safe Family

**Status:** unconditional symbolic theorem. This is the first infinite exact-depth family in this project whose composite target modulus lies outside the prime/`3q` Jacobi-new backbone. No publication-priority claim is made pending literature review.

## Theorem

Let

\[
r>5
\]

be a prime satisfying

\[
\boxed{r\equiv5\pmod{12}}.
\]

Set

\[
\boxed{A=\frac{7r+1}{4}}.
\]

Then `A` is an integer, `3|A`, and there are infinitely many primes `p` such that

\[
\boxed{\delta_{\rm sq}(p)=A.}
\]

The target witness may be taken to be

\[
\boxed{D=3},
\]

and the target modulus is

\[
\boxed{4A-1=7r}.
\]

Thus the exact-depth spectrum contains an infinite composite `7r` backbone lying strictly beyond the global Jacobi-safe `3q` family.

---

## 1. Arithmetic of the target branch

Write

\[
r=12n+5.
\]

Then

\[
A=\frac{7r+1}{4}
=\frac{84n+36}{4}
=3(7n+3),
\]

so

\[
D=3\mid A\mid A^2.
\]

The target residue is

\[
t=-4D=-12.
\]

Modulo `7`,

\[
-12\equiv2\pmod7,
\]

and `2` is a quadratic residue modulo `7`.

Modulo `r`, the target character is

\[
\left(\frac{-12}{r}\right)
=
\left(\frac{-3}{r}\right).
\]

For primes `r!=3`, the character of `-3` satisfies

\[
\left(\frac{-3}{r}\right)=
\begin{cases}
+1,&r\equiv1\pmod3,\\
-1,&r\equiv2\pmod3.
\end{cases}
\]

Since `r==5 (mod 12)` implies `r==2 (mod 3)`,

\[
\boxed{\left(\frac{-12}{r}\right)=-1.}
\]

Thus `r` is the unique nonsquare target coordinate, while the `7`-coordinate is square.

---

## 2. Single-bad-coordinate reduction

Apply the single-nonsquare-coordinate theorem with bad prime `r`.

Every earlier modulus `4B-1` not divisible by `r` can be assigned a unit-square residue compatible with the target `2 mod 7`; for instance, use the literal square `9` on every power of `7` and `1` on all other non-`r` prime-power coordinates. Such residues avoid every earlier Type-II square-completion trap by the universal Jacobi obstruction.

It remains only to inspect earlier moduli divisible by `r`.

Because

\[
4A-1=7r
\]

and `r==1 (mod 4)`, any earlier `r`-bearing modulus has the form

\[
4B-1=rs,
\qquad
s\equiv3\pmod4,
\qquad
s<7.
\]

The only possibility is

\[
\boxed{s=3}.
\]

Hence there is exactly one exceptional earlier layer,

\[
\boxed{B=\frac{3r+1}{4}},
\qquad
4B-1=3r.
\]

On this modulus choose the CRT residue

\[
p\equiv-12\pmod r,
\qquad
p\equiv1\pmod3.
\]

We now prove that this residue is never a depth-`B` trap when `r>5`.

---

## 3. The exceptional-layer Diophantine lemma

Suppose, for contradiction, that the exceptional residue is a trap at depth

\[
B=\frac{3r+1}{4}.
\]

Then there is a divisor

\[
E\mid B^2
\]

such that

\[
-4E\equiv-12\pmod r,
\qquad
-4E\equiv1\pmod3.
\]

Equivalently,

\[
E\equiv3\pmod r,
\qquad
E\equiv2\pmod3.
\]

Write

\[
\boxed{E=rk+3}.
\]

Since `r==2 (mod 3)` and `E==2 (mod 3)`,

\[
2k\equiv2\pmod3,
\]

so

\[
\boxed{k\equiv1\pmod3}.
\]

Let

\[
F=\frac{B^2}{E}.
\]

Modulo `r`,

\[
B\equiv4^{-1}\pmod r,
\]

so

\[
B^2\equiv16^{-1}\pmod r.
\]

Using `E==3 (mod r)` gives

\[
F\equiv48^{-1}\pmod r,
\]

or

\[
\boxed{48F=rh+1}
\]

for some positive integer `h`.

Also `B==1 (mod 3)`, hence `B^2==1 (mod 3)`. Since `E==2 (mod 3)`, one has

\[
F\equiv2\pmod3.
\]

Reducing `48F=rh+1` modulo `3`, with `r==2 (mod 3)`, yields

\[
0\equiv2h+1\pmod3,
\]

so

\[
\boxed{h\equiv1\pmod3}.
\]

Now multiply

\[
E=rk+3
\]

and

\[
48F=rh+1.
\]

Since `EF=B^2` and

\[
48B^2
=48\frac{(3r+1)^2}{16}
=3(3r+1)^2,
\]

we obtain

\[
(rk+3)(rh+1)=3(3r+1)^2.
\]

Expanding and cancelling the constant term gives

\[
r^2kh+r(k+3h)+3
=27r^2+18r+3,
\]

hence

\[
\boxed{
r(kh-27)+k+3h-18=0.
}
\]

This relation, together with

\[
k,h\ge1,
\qquad
k\equiv h\equiv1\pmod3,
\]

has essentially no solutions.

---

## 4. Solving the small Diophantine equation

If `kh>27`, then by AM--GM

\[
k+3h\ge2\sqrt{3kh}>18.
\]

Both terms in

\[
r(kh-27)+k+3h-18
\]

would then be positive, contradiction.

If `kh=27`, the equation forces

\[
k+3h=18.
\]

Equality in the AM--GM bound occurs only at

\[
(k,h)=(9,3),
\]

which violates

\[
k\equiv h\equiv1\pmod3.
\]

Therefore

\[
\boxed{kh<27}.
\]

Since `r>0`, the equation becomes

\[
\boxed{
r=\frac{k+3h-18}{27-kh}},
\]

so necessarily

\[
k+3h>18.
\]

Now `k,h` are positive integers congruent to `1 mod 3`, with `kh<27`. The finite possibilities giving an integral positive `r` reduce to

\[
(k,h,r)=(25,1,5),\quad(1,19,5),\quad(1,25,29).
\]

The first triple cannot occur because

\[
F=\frac{rh+1}{48}=\frac6{48}
\]

is not an integer.

The third cannot occur because

\[
F=\frac{29\cdot25+1}{48}
=\frac{726}{48}
\]

is not an integer.

The only actual collision is

\[
(k,h,r)=(1,19,5),
\]

for which `B=4`, `E=8`, `F=2`.

Therefore:

\[
\boxed{
\text{for every prime }r\equiv5\pmod{12},\ r>5,
\text{ the unique exceptional layer is safe.}
}
\]

---

## 5. Dirichlet conclusion

Let

\[
L=\operatorname{lcm}_{1\le B<A}(4B-1).
\]

Choose the global residue modulo `L` by

- `-12 mod r` on the `r`-coordinate;
- a square lift congruent to `2 mod 7` on every `7`-power coordinate (e.g. the literal square `9`);
- `1` on every other prime-power coordinate.

Section 2 excludes every earlier modulus except `3r`, and Sections 3--4 exclude `3r` as well.

This residue is compatible with the target condition

\[
p\equiv-12\pmod{7r}
\]

and with

\[
p\equiv1\pmod4.
\]

Every local coordinate is nonzero, so the combined progression is reduced. Dirichlet's theorem gives infinitely many prime members.

Each member has target witness

\[
(A,D)=\left(\frac{7r+1}{4},3\right)
\]

and no witness at any smaller depth. Hence

\[
\boxed{
\delta_{\rm sq}(p)=\frac{7r+1}{4}
}
\]

for infinitely many primes `p`.

---

## 6. Counting consequence

Let `N_7(X)` count depths `A<=X` arising from this `7r` family. Since

\[
A=\frac{7r+1}{4},
\]

we have

\[
N_7(X)
=
\pi\!\left(\frac{4X-1}{7};12,5\right)+O(1).
\]

By the prime number theorem in arithmetic progressions,

\[
\boxed{
N_7(X)
\sim
\frac17\frac{X}{\log X}.
}
\]

The target moduli `7r` are disjoint from both the prime-target backbone and the composite `3q` backbone. Therefore, combining this family with the previous total-spectrum theorem improves the proven lower bound to

\[
\boxed{
N_\infty(X)
\ge
\left(\frac83+\frac17+o(1)\right)\frac{X}{\log X}
=
\left(\frac{59}{21}+o(1)\right)\frac{X}{\log X}.
}
\]

This is a strict improvement beyond Jacobi-rank saturation: the new `7r` depths are Jacobi-dependent but nevertheless exact-depth realized.

## Significance

This family proves that the Jacobi-new backbone is not the end of the symbolic exact-depth spectrum. A single nonsquare coordinate plus one exceptional ancestor can produce a new infinite exact-depth family even when the target character is already generated by earlier layers.

The natural next question is whether other fixed cofactors

\[
s\equiv3\pmod4
\]

produce analogous `sr` backbones with finitely many exceptional `r`-bearing layers.