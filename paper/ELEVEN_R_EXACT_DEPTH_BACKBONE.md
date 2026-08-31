# An Infinite `11r` Exact-Depth Backbone

**Status:** unconditional symbolic theorem. This is a second infinite composite exact-depth family beyond the global Jacobi-safe `3q` backbone. No publication-priority claim pending literature review.

## Theorem

Let `r` be a prime satisfying

\[
\boxed{r\equiv13\pmod{24}}.
\]

Set

\[
\boxed{A=\frac{11r+1}{4}}.
\]

Then infinitely many primes `p` satisfy

\[
\boxed{\delta_{\rm sq}(p)=A}.
\]

A target witness is

\[
\boxed{D=6},
\]

and

\[
\boxed{4A-1=11r}.
\]

---

## 1. Target arithmetic

Write `r=24n+13`. Then

\[
A=\frac{11r+1}{4}
=\frac{264n+144}{4}
=6(11n+6),
\]

so `D=6|A`.

The target residue is

\[
t=-24.
\]

Modulo `11`,

\[
-24\equiv9\pmod{11},
\]

a square.

Modulo `r`,

\[
\left(\frac{-24}{r}\right)
=
\left(\frac{-6}{r}\right)=-1
\]

for `r==13 (mod 24)`; equivalently the progression was chosen so that the target has exactly one nonsquare coordinate, the variable prime `r`.

The single-nonsquare-coordinate reduction therefore excludes every earlier layer not divisible by `r`.

Because the fixed cofactor is `11`, the only earlier `r`-bearing moduli are

\[
3r\quad\text{and}\quad7r,
\]

corresponding to

\[
B_3=\frac{3r+1}{4},
\qquad
B_7=\frac{7r+1}{4}.
\]

It remains to show that neither can contain a divisor-square trap congruent to the target on the `r`-coordinate.

---

## 2. The `3r` exceptional layer

Let

\[
B=\frac{3r+1}{4}.
\]

A collision would require `E|B^2` with

\[
E\equiv6\pmod r.
\]

Choosing the safe cofactor residue `1 mod 3` also forces

\[
E\equiv2\pmod3.
\]

Write

\[
E=rk+6.
\]

Since `r==1 (mod 3)`, the condition `E==2 (mod 3)` gives

\[
\boxed{k\equiv2\pmod3}.
\]

Let `F=B^2/E`. Since `B^2==1/16 (mod r)` and `E==6 (mod r)`,

\[
F\equiv96^{-1}\pmod r,
\]

so

\[
\boxed{96F=rh+1}
\]

for a positive integer `h`.

Here `B==1 (mod 3)`, hence `F==2 (mod 3)`, and reducing the last relation modulo `3` yields

\[
\boxed{h\equiv2\pmod3}.
\]

Now

\[
96B^2
=6(3r+1)^2.
\]

Multiplying `E=rk+6` and `96F=rh+1` gives

\[
(rk+6)(rh+1)=6(3r+1)^2,
\]

hence

\[
\boxed{
r(kh-54)+k+6h-36=0.
}
\]

If `kh>54`, AM--GM gives

\[
k+6h\ge2\sqrt{6kh}>36,
\]

so both terms are positive, impossible. If `kh=54`, equality forces `(k,h)=(18,3)`, inconsistent with `k,h==2 (mod 3)`. Therefore `kh<54`.

With `k,h==2 (mod 3)`, `kh<54`, and `k+6h>36`, the only integral positive values produced by

\[
r=\frac{k+6h-36}{54-kh}
\]

are

\[
(k,h,r)=(2,11,1),(2,23,13),(2,26,61),(26,2,1).
\]

For the two prime candidates, the required integrality

\[
F=\frac{rh+1}{96}\in\mathbf Z
\]

fails:

\[
13\cdot23+1=300\not\equiv0\pmod{96},
\]

\[
61\cdot26+1=1587\not\equiv0\pmod{96}.
\]

Thus the `3r` layer never collides.

---

## 3. The `7r` exceptional layer

Now let

\[
B=\frac{7r+1}{4}.
\]

Again a collision implies

\[
E=rk+6,
\]

and, with `F=B^2/E`,

\[
96F=rh+1.
\]

Since

\[
96B^2=6(7r+1)^2,
\]

we obtain

\[
\boxed{
r(kh-294)+k+6h-84=0.
}
\]

AM--GM gives `kh<294`; the equality case would require `(k,h)=(42,7)` and is incompatible with the actual congruence data.

The divisibility `96|rh+1` gives, in particular,

\[
rh\equiv-1\pmod{24}.
\]

Since

\[
r\equiv13\pmod{24}
\]

and `13^{-1}==13 (mod 24)`,

\[
\boxed{h\equiv11\pmod{24}}.
\]

Under

\[
kh<294,
\qquad
k+6h>84,
\qquad
h\equiv11\pmod{24},
\]

the integral positive solutions of

\[
r=\frac{k+6h-84}{294-kh}
\]

reduce to

\[
(k,h,r)=(26,11,1),(2,107,7),(2,131,22).
\]

None is a prime congruent to `13 mod 24`. Hence the `7r` exceptional layer is also impossible.

---

## 4. Dirichlet conclusion

Choose a global CRT residue on the lcm of all earlier moduli by

- matching `-24 mod r` on the unique nonsquare `r`-coordinate;
- using a square lift of `-24 mod 11 == 9` on all powers of `11`;
- using `1` on every other prime-power coordinate.

Every earlier modulus not divisible by `r` receives a unit square and is safe by the universal Jacobi obstruction. Sections 2--3 rule out the only two `r`-bearing layers.

The global residue is compatible with

\[
p\equiv-24\pmod{11r}
\]

and with `p==1 (mod 4)`, and is reduced. Dirichlet's theorem therefore supplies infinitely many prime members. Every such prime has target witness `(A,6)` and no witness below depth `A`.

Thus

\[
\boxed{
\delta_{\rm sq}(p)=\frac{11r+1}{4}
}
\]

for infinitely many primes `p`.

---

## 5. Counting consequence

The depths satisfy `A<=X` exactly when

\[
r\le\frac{4X-1}{11}.
\]

Therefore

\[
N_{11}(X)
=
\pi\!\left(\frac{4X-1}{11};24,13\right),
\]

and the prime number theorem in arithmetic progressions gives

\[
\boxed{
N_{11}(X)
\sim
\frac1{22}\frac{X}{\log X}.
}
\]

The target moduli `11r` are disjoint from the prime, `3q`, and `7r` families. Combining the previous coefficient `59/21` with `1/22` gives

\[
\boxed{
N_\infty(X)
\ge
\left(\frac{59}{21}+\frac1{22}+o(1)\right)\frac{X}{\log X}
=
\left(\frac{1319}{462}+o(1)\right)\frac{X}{\log X}.
}
\]

Numerically,

\[
\frac{1319}{462}\approx2.85498.
\]

## Significance

The `7r` family is not isolated. A second fixed cofactor admits the same mechanism: one nonsquare variable-prime coordinate and finitely many exceptional `r`-bearing ancestors, each eliminated by a small Diophantine argument.

This strongly suggests a hierarchy of fixed-cofactor exact-depth backbones.