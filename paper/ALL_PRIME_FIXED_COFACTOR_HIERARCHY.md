# Canonical Fixed-Cofactor Hierarchy for Every Prime `s ≡ 3 (mod 4)`

**Status:** unconditional synthesis of the two canonical fixed-cofactor hierarchies already proved separately. It concerns exact square-completed Type-II depth, not the full Erdős--Straus conjecture.

Let `s>3` be a fixed prime with

\[
\boxed{s\equiv3\pmod4.}
\]

Write

\[
\chi_2(s)=\left(\frac2s\right)\in\{-1,+1\}
\]

and define

\[
\boxed{d_s=\frac{s-\chi_2(s)}2.}
\]

Thus

- if `s≡3 (mod 8)`, then `chi_2(s)=-1` and `d_s=(s+1)/2`;
- if `s≡7 (mod 8)`, then `chi_2(s)=+1` and `d_s=(s-1)/2`.

Choose the prime parameter progression

\[
\boxed{
r\equiv s-2\chi_2(s)\pmod{4d_s}.
}
\]

Equivalently,

- for `s≡3 (mod 8)`, `r≡s+2 (mod 2(s+1))`;
- for `s≡7 (mod 8)`, `r≡s-2 (mod 2(s-1))`.

For a prime parameter `r` in this progression put

\[
A=\frac{sr+1}{4}.
\]

The two already proved hierarchy theorems show that the corresponding witness `d_s` divides `A`, the target residue `-4d_s` is quadratic-residue at the fixed prime `s` and nonresidue at the variable prime `r`, and the AM--GM equality configuration is impossible on the entire parameter progression. Hence the fixed-cofactor finite-exception theorem applies.

Therefore:

> **Unified prime-cofactor hierarchy theorem.** For every fixed prime
> \[
> \boxed{s>3,\qquad s\equiv3\pmod4,}
> \]
> all but finitely many primes
> \[
> \boxed{
r\equiv s-2\chi_2(s)\pmod{2(s-\chi_2(s))}
> }
> \]
> generate a depth
> \[
> \boxed{A=(sr+1)/4}
> \]
> that occurs infinitely often as exact square-completed Type-II depth.

In particular, the post-Jacobi fixed-cofactor phenomenon is not confined to one residue class modulo `8`: it holds for **every prime fixed cofactor compatible with `s≡3 (mod 4)`**.

## Counting form

The fixed cofactor `s` contributes

\[
\boxed{
\frac{4}{s\varphi(2(s-\chi_2(s)))}\frac{X}{\log X}
}
\]

exact depths up to `X`. Consequently the two hierarchy series may be written as one positive convergent series

\[
\boxed{
C_{\rm fixed}=
\sum_{\substack{s>3\ \mathrm{prime}\\s\equiv3\ (4)}}
\frac{4}{s\varphi(2(s-\chi_2(s)))}
=C_{3(8)}+C_{7(8)}.
}
\]

The rigorous global lower bound is obtained by fixing a finite set of cofactors, taking `X→∞`, and then taking the supremum over finite sets. Thus

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge\frac83+C_{\rm fixed}.
}
\]

The one-million finite certificate gives

\[
C_{\rm fixed}>0.2343258698349454
\]

and hence

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge2.9009925365016116\ldots .
}
\]

## Claim boundary

This note is a synthesis of the separately proved `3 mod 8` and `7 mod 8` canonical hierarchies. It does not add a new local quadratic argument beyond those two proofs, but it gives the cleanest theorem statement for the manuscript. It does not prove universal Type-II solvability or the Erdős--Straus conjecture.