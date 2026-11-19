# Two-Hierarchy Spectrum Counting Theorem

**Status:** unconditional counting synthesis from the prime/`3q` backbone and the two canonical fixed-cofactor hierarchies. The numerical constant below is a rigorous finite partial-sum certificate, not an extrapolation.

Let

\[
N_\infty(X)=\#\{A\le X:\text{ infinitely many primes }p\text{ satisfy }\delta_{\rm sq}(p)=A\}.
\]

The previously established prime-target and composite `3q` backbones give

\[
\liminf_{X\to\infty}\frac{N_\infty(X)\log X}{X}\ge\frac83
\]

before the post-Jacobi fixed-cofactor families are added.

## 1. The two canonical hierarchy series

For primes `s≡3 (mod 8)`, the canonical hierarchy contributes for each fixed cofactor

\[
\frac{4}{s\varphi(2(s+1))}\frac{X}{\log X}.
\]

Define

\[
C_{3(8)}=
\sum_{\substack{s>3\ \mathrm{prime}\\s\equiv3\ (8)}}
\frac{4}{s\varphi(2(s+1))}.
\]

For primes `s≡7 (mod 8)`, the new canonical hierarchy contributes

\[
\frac{4}{s\varphi(2(s-1))}\frac{X}{\log X}
\]

for each fixed cofactor, and we define

\[
C_{7(8)}=
\sum_{\substack{s>3\ \mathrm{prime}\\s\equiv7\ (8)}}
\frac{4}{s\varphi(2(s-1))}.
\]

Both positive series converge because their terms are

\[
\ll\frac{\log\log s}{s^2}.
\]

## 2. Rigorous order of limits

For any fixed finite set `S` of fixed cofactors, the prime number theorem in fixed arithmetic progressions applies separately to every family. Distinct fixed cofactors give distinct semiprime target moduli except when the variable prime in one family equals the fixed cofactor in another; for a fixed finite `S` there are only finitely many such swapped-prime coincidences. They do not affect the asymptotic.

Therefore contributions add for every fixed finite set. Taking `X→∞` first and then taking the supremum over finite subsets gives

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge
\frac83+C_{3(8)}+C_{7(8)}.
}
\]

No uniform prime-number theorem with a cofactor growing with `X` is used.

## 3. Finite one-million certificate

A direct exact prime/totient computation through `s<=1,000,000` gives

\[
\sum_{\substack{s\le10^6\ \mathrm{prime}\\s\equiv3\ (8)}}
\frac{4}{s\varphi(2(s+1))}
=
\boxed{0.06768134901831344\ldots}
\]

from `19,652` cofactors, and

\[
\sum_{\substack{s\le10^6\ \mathrm{prime}\\s\equiv7\ (8)}}
\frac{4}{s\varphi(2(s-1))}
=
\boxed{0.16664452081663197\ldots}
\]

from `19,669` cofactors.

Hence the finite subset alone proves

\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge
2.9009925365016116\ldots .
}
\]

Because all omitted hierarchy terms are positive, the full two-hierarchy coefficient is strictly larger.

## 4. Double-counting policy

Earlier explicit families with fixed cofactors `7,23,31,47,...` should **not** simply be added on top of `C_{7(8)}`: their parameter progressions can intersect the new canonical `7 mod 8` progression infinitely often. Such an explicit family may improve the coefficient only after the union of parameter residue classes for that fixed cofactor is counted exactly.

The displayed `2.9009925365...` lower bound deliberately avoids that issue and uses only the two canonical hierarchy families plus the established prime/`3q` contribution.

## Claim boundary

This counts exact **square-completed Type-II depths** that are each realized by infinitely many primes. It does not prove that every prime has a Type-II solution and does not prove the Erdős--Straus conjecture.