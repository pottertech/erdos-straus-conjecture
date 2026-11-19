# Referee Audit of the Repaired v9 Fixed-Cofactor Hierarchy

**Status:** internal adversarial proof audit. This is not an independent publication-priority review.

The purpose of this note is to check the full logical chain of `composite_exact_typeii_depths_v9.tex` after the `k=0` repair.

## 1. Target witness and integrality

For each canonical fixed-prime row, the chosen parameter progression is a reduced congruence class and satisfies

\[
sr+1\equiv0\pmod{4d}.
\]

Hence

\[
A=(sr+1)/4
\]

is integral and

\[
d\mid A,
\]

so certainly `d|A^2`.

The target residue is

\[
n\equiv-4d\pmod{sr}.
\]

Because `gcd(d,sr)=1` after finitely many parameters `r` dividing fixed data are removed, this residue is reduced at both target prime coordinates.

## 2. Single nonsquare coordinate

In every row:

- `(-d/s)=+1`;
- `(-d/r)=-1` throughout the canonical parameter progression.

Thus the prescribed target residue is square at the fixed target prime `s` and nonsquare at the variable prime `r`.

At every prime-power coordinate not involving `s` or `r`, choose residue `1`. At prime powers over `s`, choose a square lift of the prescribed target square class modulo `s`. Such a lift exists because `s` is odd and the target class has a nonzero square root modulo `s`; Hensel lifting preserves a square root to every required power.

Therefore every earlier modulus not divisible by `r` receives a unit square at every prime-power factor and has Jacobi sign `+1`. The universal Jacobi obstruction excludes its full trap set.

## 3. Structure of the remaining layers

After removing finitely many parameter primes `r<=s`, every earlier modulus divisible by `r` is

\[
4B-1=cr
\]

with `0<c<s`. Its mod-4 class is forced by `cr≡3 (mod 4)`:

- if `r≡1 (mod 4)`, then `c≡3 (mod 4)`;
- if `r≡3 (mod 4)`, then `c≡1 (mod 4)`.

There are finitely many such fixed `c`.

## 4. Master equation is necessary for every collision

A collision at `cr` gives a divisor `E|B^2` with

\[
E\equiv d\pmod r.
\]

Therefore

\[
E=rk+d,
\qquad k\ge0.
\]

With `F=B^2/E`, reduction of `EF=B^2` modulo `r` yields

\[
16dF\equiv1\pmod r,
\]

so

\[
16dF=rh+1
\]

for some integer `h`. Because `16dF>=16`, one has

\[
\boxed{h\ge1.}
\]

Multiplication gives the exact identity

\[
\boxed{r(kh-dc^2)+k+dh-2dc=0.}
\]

No assumption about the chosen non-`r` CRT coordinates is used in deriving this necessary equation.

## 5. The degenerate `k=0` case

If `k=0`, then `E=d`. For this to be a valid earlier trap divisor, necessarily

\[
d\mid B^2.
\]

The global square-safe choice is residue `1` on the entire fixed cofactor `c`, because `c<s` and therefore `c` cannot contain the target prime `s`. Thus the same `E=d` matches the chosen `c`-coordinate only if

\[
1\equiv-4d\pmod c,
\]

i.e.

\[
c\mid4d+1.
\]

`CANONICAL_NO_REUSE_LEMMA.md` proves case by case that the two conditions

\[
d\mid B^2,
\qquad c\mid4d+1
\]

cannot occur simultaneously for the repaired canonical fixed-prime data. Hence

\[
\boxed{k\ge1}
\]

for every actual collision.

This is the step missing from the earlier pre-repair fixed-cofactor argument.

## 6. AM--GM equality

For `k,h>=1`, if `kh>dc^2`, then

\[
k+dh\ge2\sqrt{dkh}>2dc,
\]

which contradicts the sign required by the master equation.

If

\[
kh=dc^2,
\]

then equality in AM--GM forces

\[
k=dc,
\qquad h=c,
\]

and substitution into `16dF=rh+1` gives the equality congruence

\[
16d\mid cr+1.
\]

The canonical parameter progressions exclude this congruence for every permitted `c<s`. In the `s≡1 (mod 8)` row, the strengthened 2-adic witness is essential in the complete repair package.

Therefore every collision satisfies

\[
\boxed{1\le kh<dc^2.}
\]

## 7. Finiteness of exceptional parameters

Because `k,h` are now both positive,

\[
1\le k<dc^2,
\qquad
1\le h<dc^2.
\]

Thus there are finitely many pairs. For each pair with `kh<dc^2`, the master equation determines at most one rational value

\[
r=\frac{k+dh-2dc}{dc^2-kh}.
\]

Hence each fixed exceptional cofactor `c` supplies only finitely many prime collision parameters. The union over the finitely many `c<s` is finite.

This establishes the phrase **all but finitely many parameter primes**.

## 8. Existence of the final exact-depth prime progression

After removing the finite parameter collision set, choose the fixed target congruence modulo `sr` and the square-safe coordinates on every earlier prime-power coordinate. The compatibility conditions were built into the construction:

- target/common `s` coordinates agree by square lifting;
- every other non-`r` coordinate is freely set to `1`;
- there is no surviving trap on any `r`-bearing layer.

The resulting CRT class is reduced:

- modulo `s`, the target residue is nonzero;
- modulo `r`, the target residue is nonzero;
- every other prime divisor of the CRT modulus sees residue `1` or another unit square.

Dirichlet's theorem therefore gives infinitely many prime denominators in the final progression. The target depth `A` is valid, while every `B<A` has been excluded, proving exactness.

## 9. Counting and double counting

For a fixed cofactor `s`, deleting finitely many parameter primes does not change the PNT-in-progressions asymptotic. The family contribution is

\[
\frac{4}{s\varphi(M_s)}\frac{X}{\log X},
\]

where `M_s` is the fixed canonical parameter modulus.

For a fixed finite set of cofactors, distinct target semiprimes `sr` can coincide across two families only by swapping which prime is fixed. Since the set of fixed primes is finite, those coincidences form a finite set and do not affect the asymptotic.

The correct order of limits is:

1. fix a finite cofactor set;
2. take `X→∞` using PNT in fixed arithmetic progressions;
3. then take the supremum over finite cofactor sets.

Thus the convergent positive hierarchy series is legitimate without a uniform PNT for a cofactor growing with `X`.

## 10. Current audit verdict

After the `k=0` repair, no logical gap is presently identified in the canonical fixed-prime finite-exception chain.

The strongest claim justified by this internal audit is:

\[
\boxed{
\text{for every fixed prime }s>3,\text{ the repaired canonical progression has only finitely many bad }r.
}
\]

The separate questions of historical priority, optimality of the canonical progression, and whether a referee accepts the use/statement of the standard complete Type-II coordinate remain external-review issues.

This theorem does **not** imply universal Type-II solvability and does **not** prove the Erdős--Straus conjecture.