# Claim Audit After Exact u-Method Correction

**Date:** 2026-08-28  
**Status:** Required corrections to earlier deterministic-subclass claims

## 1. Reason for the audit

Earlier repository documents used the shortcut

\[
\{-x,-xn,-xn^2\}\pmod u
\]

for the reduced divisor targets. The canonical verifier now uses the exact divisor-pair criterion, and the exact centered equivalent criterion is documented in `CENTERED_PRODUCT_SET_THEOREM.md`.

Any theorem whose proof depended on the old shortcut must therefore be rechecked.

## 2. The old `n ≡ 49 (mod 120) => u=7` claim is false

A concrete counterexample is

\[
n=1129\equiv49\pmod{120}.
\]

This is a prime hard case. For `u=7`,

\[
x=\frac{1129+7}{4}=284=2^2\cdot71,
\qquad M=nx.
\]

The exact centered product set

\[
\mathcal S_7(M)=\prod_{p^a\parallel M}\{p^{-a},\ldots,p^a\}\pmod7
\]

does **not** contain `-1 mod 7`. Hence `u=7` does not solve this case by the exact u-method criterion.

The first exact centered success is `u=11`.

Therefore statements in older documents such as `DETERMINISTIC_BOUND_PROOF.md` and `UNIFIED_THEOREM.md` asserting that all prime hard cases `n ≡ 49 (mod 120)` are solved by `u=7` are withdrawn pending a corrected proof.

## 3. The old `n ≡ 13 (mod 24) => u=7` proof contains a parity error

Older text argued that for

\[
n\equiv13\pmod{24},
\]

we have `n ≡ 5 (mod 8)` and, with `u=7`, that `2|x` for `x=(n+u)/4`.

But

\[
n+u\equiv5+7\equiv4\pmod8,
\]

so

\[
x=(n+u)/4\equiv1\pmod2.
\]

Thus `x` is **odd**, not even. The claimed deterministic factor 2 is not present.

The broader `n ≡ 13 (mod 24) => u=7` statement is also false computationally under the exact criterion. For prime hard cases below `10^6`, residue classes `61` and `109 mod 120` (both `13 mod 24`) contain many failures at `u=7`.

## 4. Corrected small-range residue audit

For prime hard cases below `10^6`, exact centered testing at `u=7` gives:

| n mod 120 | hard primes | u=7 failures |
|---:|---:|---:|
| 1 | 1,523 | 499 |
| 13 | 560 | 0 |
| 49 | 1,488 | 490 |
| 61 | 578 | 257 |
| 73 | 1,529 | 0 |
| 109 | 568 | 243 |

This table is computational evidence only. It does, however, show that the old residue-family partition does not support the previously claimed universal `u=7` theorem.

The classes `13 mod 120` and `73 mod 120` are especially interesting because no `u=7` failures occur below `10^6`; these should be investigated for a genuinely correct deterministic proof.

## 5. Claims that should no longer be cited as established

Until rederived from the exact criterion, do not cite the following as proved:

1. `n ≡ 13 (mod 24) => u=7` for every prime hard case.
2. `n ≡ 49 (mod 120) => u=7` for every prime hard case.
3. The resulting claim that `87.5%` of prime hard cases are deterministically covered with `u<=23`.
4. Any CRT cascade whose failure sets were computed from the old three-target reduction.

The computational verification using the new direct criterion remains valid for the ranges rerun with that verifier, but it is distinct from a deterministic residue-class theorem.

## 6. New proof target

The exact theorem to exploit is

\[
u\text{-method succeeds}\iff -1\in\mathcal S_u(nx)
\]

when `gcd(nx,u)=1`.

The next useful deterministic result would be a correct local-factor theorem proving `-1` belongs to this bounded product set for one or more residue subclasses. Empirically, the `13 mod 120` and `73 mod 120` classes are the first candidates to study.
