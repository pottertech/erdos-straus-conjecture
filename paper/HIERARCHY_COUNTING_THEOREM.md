# Counting the Fixed-Cofactor Exact-Depth Hierarchy

**Status:** unconditional asymptotic lower-bound theorem assembled from the proved fixed-cofactor families. The statement is deliberately phrased as a `liminf`, so no uniform prime-number theorem over a growing family of cofactors is assumed.

Let

\[
N_\infty(X)
=
\#\{A\le X:\text{ infinitely many primes }p\text{ satisfy }\delta_{\rm sq}(p)=A\}.
\]

The already established prime and `3q` backbones give

\[
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}\ge\frac83.
\]

We now add the post-Jacobi fixed-cofactor hierarchy.

## 1. Canonical `s == 3 (mod 8)` hierarchy

For every fixed prime

\[
s>3,\qquad s\equiv3\pmod8,
\]
`INFINITE_FIXED_COFACTOR_HIERARCHY.md` proves that all but finitely many primes
\[
r\equiv s+2\pmod{2(s+1)}
\]
give exact depths
\[
A=\frac{sr+1}{4}.
\]
For fixed `s`, the number of such depths up to `X` is
\[
\pi\!\left(\frac{4X-1}{s};2(s+1),s+2\right)+O_s(1)
\]
and therefore
\[
\sim
\frac{4}{s\varphi(2(s+1))}\frac{X}{\log X}.
\]

Define the convergent positive series
\[
\boxed{
C_{3(8)}
=
\sum_{\substack{s>3\ \mathrm{prime}\\s\equiv3\ (8)}}
\frac{4}{s\varphi(2(s+1))}.
}
\]
Convergence follows, for example, from the standard lower bound
\[
\varphi(n)\gg \frac{n}{\log\log n},
\]
which makes the summand
\[
\ll\frac{\log\log s}{s^2}.
\]

For every **fixed finite** subset `S` of these cofactors, the corresponding target semiprime moduli `sr` are pairwise distinct apart from finitely many swapped-prime coincidences. After discarding those finite overlaps, the fixed-`S` prime number theorem in arithmetic progressions gives
\[
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}
\ge
\frac83+
\sum_{s\in S}
\frac{4}{s\varphi(2(s+1))}.
\]
Because this holds for every finite `S`, taking the supremum over finite subsets yields
\[
\boxed{
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}
\ge
\frac83+C_{3(8)}.
}
\]
No uniformity in `s` is used: `S` is fixed before `X\to\infty`.

## 2. Explicit disjoint `7 (mod 8)` families

Several proved families have fixed prime cofactor `s==7 (mod 8)` and therefore lie outside the canonical `3 (mod 8)` hierarchy. We include the following four families, whose theorem notes provide the exact first-hit proofs:

1. `s=7`, `d=3`, `r==5 (mod 12)`, contribution
\[
\frac17;
\]

2. `s=23`, `d=20`, `r==73 (mod 80)`, contribution
\[
\frac1{184};
\]

3. `s=31`, `d=17`, `r==57 (mod 68)`, contribution
\[
\frac1{248};
\]

4. `s=47`, `d=43`, `r==161 (mod 172)`, contribution
\[
\frac1{987}.
\]

Their target moduli have different fixed prime cofactors from one another and from all canonical `s==3 (mod 8)` rows. Any swapped-prime coincidences between two fixed families are finite, so they do not affect the asymptotic lower bound.

Define
\[
\boxed{
C_{\rm extra}
=
\frac17+\frac1{184}+\frac1{248}+\frac1{987}.
}
\]
Then
\[
\boxed{
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}
\ge
\frac83+C_{3(8)}+C_{\rm extra}.
}
\]

## 3. Explicit numerical certificate

The exact partial sum over all canonical hierarchy primes `s<=100000` is
\[
\boxed{
\sum_{\substack{s\le100000\ \mathrm{prime}\\s\equiv3\ (8)}}
\frac{4}{s\varphi(2(s+1))}
=
0.0676803077377\ldots
}
\]
(`2408` prime cofactors).

Also
\[
C_{\rm extra}
=
\frac17+\frac1{184}+\frac1{248}+\frac1{987}
=0.153337354\ldots
\]
so this finite certified collection alone gives
\[
\boxed{
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}
\ge
2.887684329\ldots
}
\]
without using the uncomputed tail of `C_{3(8)}`.

The full convergent hierarchy gives a strictly larger coefficient.

## 4. Interpretation

This result is a lower bound for the number of **depth values** that are each realized by infinitely many primes. It is not an assertion that a positive proportion of integers `n` require those depths, and it is not a proof of universal Type-II solvability or of the Erdős--Straus conjecture.

The important structural point is that the post-Jacobi contribution is itself infinite: exact-depth families exist for infinitely many distinct fixed target cofactors, not merely for the finite examples `7,11,19,23,...`.

## Claim boundary

The prime-modulus backbone and local quadratic/square-completion mechanisms have prior art. The candidate contribution is the fixed-cofactor exact-first-hit hierarchy, finite-exception reduction, and the resulting spectrum-count synthesis. Priority remains subject to dedicated literature review.