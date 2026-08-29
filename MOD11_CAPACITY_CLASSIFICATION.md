# Exact Mod-11 Capacity Classification

**Date:** 2026-08-28  
**Status:** Exact finite-state consequence of the prime-modulus capacity theorem

Let

\[
x=\frac{n+11}{4},\qquad M=nx,
\]

with `gcd(M,11)=1`.  Use primitive root `g=2` modulo 11.  Since `|(Z/11Z)^*|=10`, the target `-1` has discrete log 5.

Pair inverse discrete-log classes and define capacities (prime valuations counted with multiplicity):

- `A1`: residues with logs `±1`, i.e. `{2,6}` modulo 11;
- `A2`: logs `±2`, residues `{4,3}`;
- `A3`: logs `±3`, residues `{8,7}`;
- `A4`: logs `±4`, residues `{5,9}`;
- `A5`: log `5`, residue `{10=-1}`.

By `PRIME_MODULUS_CAPACITY_THEOREM.md`, the u-method succeeds exactly when

\[
\exists |a_j|\le A_j:
\quad a_1+2a_2+3a_3+4a_4+5a_5\equiv5\pmod{10}.
\]

## Immediate branch

If

\[
A_5\ge1,
\]

then choose `a5=1`; success is immediate.

If

\[
A_1=A_3=A_5=0,
\]

then every attainable log is even, so the odd target 5 is impossible.  Thus this is an unconditional failure branch for `u=11`, regardless of `A2,A4`.

## Complete finite exceptional list when an odd-log factor is present

Assume `A5=0` and `A1+A3>0`.  Then failure occurs **if and only if** the four-vector

\[
(A_1,A_2,A_3,A_4)
\]

is one of the following 13 vectors:

\[
\begin{array}{llll}
(0,0,1,0),&(0,0,1,1),&(0,0,2,0),&(0,0,2,1),\\
(0,0,3,0),&(0,0,4,0),&(1,0,0,0),&(1,0,1,0),\\
(1,1,0,0),&(2,0,0,0),&(2,1,0,0),&(3,0,0,0),\\
(4,0,0,0).
\end{array}
\]

Equivalently, the maximal exceptional boxes (componentwise) are

\[
(0,0,2,1),\quad
(0,0,4,0),\quad
(1,0,1,0),\quad
(2,1,0,0),\quad
(4,0,0,0).
\]

Every capacity vector with an odd-log factor that is not contained in one of those boxes reaches 5 modulo 10.

### Why the list is finite

If `A1>=5` or `A3>=5`, an odd class alone reaches the target (`5*1=5`, `5*3=15=5 mod 10`).  If an odd class is present and either even capacity is sufficiently large, the even classes supply all even corrections modulo 10.  Thus only small capacities can fail.  Exhausting the bounded congruence in these small ranges gives exactly the list above; this is a finite check in `Z/10Z`, not a numerical experiment in `n`.

## Corrected residual sample below 10^6

Start from the corrected classical residual/hard population, apply the exact shift-divisor reduction, and then retain the 342 cases that fail `u=7`.  At `u=11`:

- **164** succeed;
- **178** fail.

The 178 failures have only two structural forms:

1. **152 cases:**
   \[
   A_1=A_3=A_5=0,
   \]
   so every prime factor of `M` lies in a quadratic-residue log class modulo 11;

2. **26 cases:**
   \[
   \boxed{(A_1,A_2,A_3,A_4,A_5)=(2,1,0,0,0).}
   \]

No other exact mod-11 failure vector occurs in this corrected sample.

This is computational evidence about the residual population, while the capacity criterion and the 13-vector failure classification are exact finite group statements.

## Next layer

The remaining 178 cases pass to `u=15`.  Because `(Z/15Z)^*` is not cyclic, the prime-capacity theorem cannot be used verbatim.  The correct next step is to build the same finite-state compression directly in the unit group

\[
(\mathbb Z/15\mathbb Z)^*\cong C_2\times C_4,
\]

and classify bounded signed factor capacities by the four inverse-pairs of units.  This will keep the cascade exact for composite u-values rather than reverting to an invalid single discrete-log coordinate.
