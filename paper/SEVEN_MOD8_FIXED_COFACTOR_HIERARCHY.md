# Canonical `s ≡ 7 (mod 8)` Fixed-Cofactor Hierarchy

**Status:** unconditional theorem, subject to the same prior-art/priority boundary as the other fixed-cofactor exact-depth results. This concerns exact square-completed Type-II depth, not the full Erdős--Straus conjecture.

Let

\[
s>3
\]

be a fixed prime satisfying

\[
\boxed{s\equiv7\pmod8.}
\]

Set

\[
\boxed{d=\frac{s-1}{2}}
\]

and take the variable prime parameter in the reduced progression

\[
\boxed{r\equiv s-2\pmod{2(s-1)}.}
\]

Put

\[
A=\frac{sr+1}{4}.
\]

We prove that, after deleting only finitely many parameter primes `r`, the depth `A` is realized as exact square-completed Type-II depth by infinitely many primes.

## 1. The witness divides the target depth

Because

\[
s=2d+1
\]

and

\[
r\equiv s-2=2d-1\pmod{4d},
\]

we have

\[
sr+1\equiv(2d+1)(2d-1)+1=4d^2\equiv0\pmod{4d}.
\]

Hence

\[
\boxed{d\mid A,}
\]

so `d|A^2` is a valid square-completion witness. The target modulus is

\[
4A-1=sr
\]

and the target residue is

\[
n\equiv-4d=-2(s-1)\pmod{sr}.
\]

## 2. Exactly one nonsquare coordinate

Modulo `s`,

\[
-d=-\frac{s-1}{2}\equiv\frac12\pmod s.
\]

Therefore

\[
\left(\frac{-d}{s}\right)
=\left(\frac{2}{s}\right)=+1
\]

because `s≡7 (mod 8)`.

Now `d=(s-1)/2≡3 (mod 4)`. The parameter progression gives

\[
r\equiv-1\pmod d
\]

and, since its modulus is `4d`, also

\[
r\equiv1\pmod4.
\]

Thus quadratic reciprocity for the odd integer `d` gives

\[
\left(\frac{-d}{r}\right)
=\left(\frac{d}{r}\right)
=\left(\frac{r}{d}\right)
=\left(\frac{-1}{d}\right)
=-1.
\]

Multiplication by `4` does not change quadratic character. Hence the target residue is square at the fixed prime `s` and nonsquare at the unique variable coordinate `r`.

By the single-nonsquare-coordinate reduction theorem, every earlier layer whose modulus is not divisible by `r` can be eliminated simultaneously by square-safe CRT coordinates.

## 3. Equality is impossible on the whole parameter progression

After discarding the finitely many parameters `r<=s`, every earlier modulus containing `r` has the form

\[
4B-1=cr,
\qquad
0<c<s,
\qquad
c\equiv3\pmod4.
\]

The master exceptional-layer equation says that a collision produces nonnegative integers `k,h` satisfying

\[
r(kh-dc^2)+k+dh-2dc=0.
\]

The AM--GM equality configuration would require

\[
16d\mid cr+1.
\]

Here `16d=8(s-1)`. But the parameter class satisfies

\[
r\equiv-1\pmod{s-1}.
\]

Hence equality would imply

\[
0\equiv cr+1\equiv1-c\pmod{s-1}.
\]

Since `0<c<s`, this forces `c=1`, incompatible with `c≡3 (mod 4)`. Thus the equality configuration is impossible for every parameter in the original progression.

Consequently every collision satisfies the strict finite bound

\[
\boxed{kh<dc^2.}
\]

For each fixed `c`, only finitely many pairs `(k,h)` occur, and each determines at most one rational parameter

\[
r=\frac{k+dh-2dc}{dc^2-kh}.
\]

Therefore each exceptional cofactor contributes only finitely many collision primes, and the union over all `c<s` is finite.

## 4. The hierarchy theorem

Dirichlet's theorem gives infinitely many primes in the reduced progression

\[
r\equiv s-2\pmod{2(s-1)}.
\]

Deleting the finite collision set still leaves infinitely many parameter primes. For each remaining `r`, CRT refines the target progression to avoid every earlier square-completed Type-II trap, and a second application of Dirichlet supplies infinitely many primes `p` on that exact-depth progression.

Hence:

> **Canonical `7 mod 8` hierarchy theorem.** For every fixed prime
> \[
> \boxed{s\equiv7\pmod8,}
> \]
> all but finitely many primes
> \[
> \boxed{r\equiv s-2\pmod{2(s-1)}}
> \]
> generate a depth
> \[
> \boxed{A=(sr+1)/4}
> \]
> that occurs infinitely often as exact square-completed Type-II depth.

## 5. Counting contribution

For each fixed admissible `s`, finite deletion does not alter the asymptotic. The family contributes

\[
\boxed{
\frac{4}{s\varphi(2(s-1))}\frac{X}{\log X}
}
\]

exact depths up to `X`.

Define the positive convergent series

\[
\boxed{
C_{7(8)}=
\sum_{\substack{s>3\ \mathrm{prime}\\s\equiv7\ (8)}}
\frac{4}{s\varphi(2(s-1))}.
}
\]

As with the `3 mod 8` hierarchy, the rigorous global lower bound is obtained by first fixing a finite set of cofactors, taking `X→∞`, and then taking the supremum over finite sets. This avoids any uniform prime-number-theorem assumption for a cofactor growing with `X`.

The previously proved `s=7,d=3` family is exactly the first member of this hierarchy. Other earlier explicit `7 mod 8` constructions may provide additional residue classes for the same fixed cofactor and should be counted separately only after disjointness of parameter classes is checked.

## Claim boundary

This theorem establishes an infinite hierarchy of exact square-completed Type-II depth families. It does not imply universal Type-II solvability and does not prove the Erdős--Straus conjecture. The fixed-cofactor mechanism should receive a dedicated literature audit before novelty or priority is asserted.