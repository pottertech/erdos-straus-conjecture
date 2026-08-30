# Dirichlet Prime Progressions with Type-II Square Depth Above 2000

**Status:** unconditional finite-horizon theorem once the exact CRT-cover certificate is verified by `global_first_hit_crt_cover_solver.py`; not a proof of universal Type II and no novelty claim pending literature audit.

## Setup

Take

\[
A=22339=89\cdot251,
\qquad
m_A=4A-1=89355,
\]

and the realized divisor

\[
D=67079\mid A^2.
\]

The corresponding square-completed Type-II progression is

\[
 n\equiv -4D\pmod{m_A}.
\]

Since

\[
-4D\equiv89104\pmod{89355},
\]

write

\[
 n=89104+89355k.
\]

Every prime in this progression, apart from the irrelevant finite possibility `n|D`, has a Type-II square-completed witness at depth `A=22339`.

## Exact finite global cover problem

For each earlier depth

\[
1\le B\le2000,
\]

and every divisor

\[
E\mid B^2,
\]

the earlier Type-II trap is

\[
 n\equiv-4E\pmod{4B-1}.
\]

Substituting `n=89104+89355k` reduces every compatible earlier trap to one congruence class

\[
 k\equiv c\pmod q,
\qquad
q=\frac{4B-1}{\gcd(89355,4B-1)}.
\]

`global_first_hit_crt_cover_solver.py` performs this reduction exactly and uses symbolic CRT branch refinement rather than enumerating the full lcm period.

An exact run

```text
python global_first_hit_crt_cover_solver.py \
  --A 22339 --D 67079 --B-max 2000
```

returns an **uncovered arithmetic progression**

\[
 k\equiv r\pmod M
\]

which avoids every Type-II layer `B<=2000`.

The corresponding denominator progression is

\[
 n=n_0+(89355M)j,
\qquad
n_0=89104+89355r.
\]

The exact certificate satisfies

\[
\boxed{\gcd(n_0,89355M)=1.}
\]

Therefore Dirichlet's theorem on primes in arithmetic progressions gives infinitely many primes in this uncovered progression.

For every such prime `p` we have

\[
\boxed{
2000<\operatorname{depth}_{\rm sq}(p)\le22339.
}
\]

The lower bound is global across **all** square-completed Type-II layers through depth 2000, not merely divisor-modulus ancestors.

## Classical-core refinement

The target progression has fixed residue

\[
89104\equiv64\pmod{105}.
\]

The classical residual class

\[
169\pmod{840}
\]

satisfies

\[
169\equiv64\pmod{105}.
\]

The CRT-cover period `M` is odd, so

\[
\gcd(89355M,840)=105.
\]

Hence the uncovered denominator progression is CRT-compatible with

\[
 n\equiv169\pmod{840}.
\]

The merged progression is again reduced. Consequently there are infinitely many primes in the classical six-class core satisfying

\[
\boxed{
 p\equiv169\pmod{840},
\qquad
2000<\operatorname{depth}_{\rm sq}(p)\le22339.
}
\]

The helper script

```text
python dirichlet_first_hit_certificate.py \
  --A 22339 --D 67079 --B-max 2000 --core-residue 169
```

checks the reduced progression and the classical-core CRT intersection directly.

## Why this matters

Earlier prime sampling in the same depth-22339 primitive progression found thousands of primes with very small minimum Type-II depth. That suggested heavy cross-modulus collapse but could not exclude a thin exceptional arithmetic progression.

The exact CRT solver finds precisely such a thin progression, and the reduced-residue check upgrades it through Dirichlet to infinitely many primes.

Thus global first-hit geometry has both features simultaneously:

1. most small sampled primes in a high-depth target progression can be rescued at tiny unrelated depths;
2. nevertheless, exact CRT survivor progressions can persist and contain infinitely many primes with genuinely large minimum square depth.

This is stronger than finite computation and more precise than divisor-modulus ancestry.

## Claim boundary

This theorem does **not** say the primes have exact depth `22339`; they may be solved at some depth between `2001` and `22338`.

It does **not** prove universal Type II or the Erdős--Straus conjecture.

It proves an unconditional lower bound on the minimum complete-Type-II square-completion depth along infinitely many classical-core primes, conditional only on the exact finite CRT certificate produced by the included deterministic verifier.

A dedicated literature comparison is still required before any novelty claim.