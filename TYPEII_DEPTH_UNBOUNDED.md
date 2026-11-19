# Complete Type-II Square Depth Is Unbounded

**Status:** unconditional theorem; the exact prime-modulus backbone is prior art (FCF/CENTL, 2026-08-15), independently checked here. No novelty claim.

For a prime `p == 1 (mod 4)`, use the square-completed Type-II criterion

\[
\exists A,D>0:
\qquad D\mid A^2,
\qquad 4A-1\mid p+4D,
\qquad p\nmid D.
\]

Define `depth_sq(p)` to be the least such `A` when a Type-II witness exists.

## 1. Neutral-residue lemma

Fix `A >= 1`. If `D|A^2`, then

\[
\boxed{4A-1\nmid 4D+1.}
\]

Proof. Put

\[
g=\gcd(A,D),\qquad A=ga,\qquad D=gd,\qquad \gcd(a,d)=1.
\]

Since `D|A^2`, we have `gd|g^2a^2`; hence `d|g`. Write `g=dh`. Then

\[
A=dha,\qquad D=d^2h.
\]

If `4A-1|4D+1`, then, because `4A == 1 (mod 4A-1)`, we obtain

\[
4A-1\mid D+A=dh(d+a).
\]

Also `gcd(4A-1,dh)=1`, so `4A-1|d+a`. But

\[
4A-1=4dha-1>d+a
\]

for positive `d,h,a`, a contradiction. Therefore

\[
\boxed{1\notin S_A},\qquad
S_A:=\{-4D\pmod{4A-1}:D\mid A^2\}.
\]

So residue `1 mod (4A-1)` avoids every depth-`A` Type-II square trap.

## 2. Exact prime-modulus backbone

Let `k` satisfy

\[
q=4k-1>7
\]

with `q` prime. Define

\[
L_{k-1}=\operatorname{lcm}(840,3,7,11,\ldots,4k-5).
\]

Since `q` is prime and larger than every number `4j-1` with `j<k`,

\[
\gcd(q,L_{k-1})=1.
\]

By the Chinese remainder theorem there is a reduced residue class `r` modulo

\[
M_k=qL_{k-1}
\]

such that

\[
r\equiv1\pmod{L_{k-1}},
\qquad
r\equiv-1\pmod q.
\]

Because `gcd(r,M_k)=1`, Dirichlet's theorem gives infinitely many primes

\[
p\equiv r\pmod{M_k}.
\]

For every `j<k`,

\[
p\equiv1\pmod{4j-1},
\]

and the neutral-residue lemma gives `p mod (4j-1) notin S_j`. Hence no square-completed Type-II witness occurs at depth `<k`.

At depth `k`, choose

\[
D=k.
\]

Then `D|k^2` and

\[
p+4D\equiv -1+4k=q\equiv0\pmod q.
\]

Thus depth `k` succeeds. The coprimality condition `p\nmid D` is automatic: a prime `p == -1 (mod q)` cannot lie in `(0,q)` except at `q-1`, which is even, so `p>q>k`.

Therefore

\[
\boxed{\operatorname{depth}_{\rm sq}(p)=k}
\]

for infinitely many primes `p`; all may simultaneously be chosen with

\[
p\equiv1\pmod{840}.
\]

### Exact-depth theorem

\[
\boxed{
4k-1>7\text{ prime}
\Longrightarrow
\text{infinitely many Mordell-hard primes have exact square depth }k.
}
\]

Because there are infinitely many primes `q == 3 (mod 4)`, there are infinitely many such `k=(q+1)/4`. Hence the finite square-completed Type-II depth spectrum is unbounded.

## 3. Why this repair matters

An earlier version of this note used only primes

\[
p\equiv1\pmod{\operatorname{lcm}(840,3,7,\ldots,4J-1)}
\]

to avoid all depths `<=J`. That argument correctly proves **avoidance through depth `J`**, but by itself does not prove that those primes ever possess a later Type-II witness, because universal Type-II existence is open.

The prime-modulus backbone above fixes that logical gap: it forces an actual hit at depth `k` while forcing every earlier depth to fail. The resulting depths are therefore finite exact first-hit depths, not merely lower bounds conditional on later existence.

## 4. Consequences

1. Complete square-completed Type-II first-hit depth is genuinely unbounded among primes that actually have Type-II witnesses.
2. No proof or algorithm equivalent to checking only a fixed finite set of square depths can cover all Type-II-solvable primes.
3. The finite computational records `624` (through `10^8`) and `816` (through `10^9`) cannot stabilize to a universal constant.
4. This theorem concerns **square-completion depth**. It must not be conflated with Dahan's pair depth `max(u,a)`.

## 5. Priority boundary

The Free Computation Foundation / CENTL research library publicly recorded the square-completed prime-modulus exact-depth backbone on 2026-08-15. Their formulation likewise uses the neutral residue `1`, the forced target `-1` at a prime modulus `4k-1`, CRT, and Dirichlet realization.

Accordingly, the exact-depth backbone and unboundedness theorem are prior art and are not claimed as discoveries of this project. The separate Linnik quantitative refinement is treated in `TYPEII_DEPTH_LOG_LOWER_BOUND.md` and has its own priority caveat.

This theorem does **not** prove Erdős--Straus. It proves a structural statement about the depth of the classical strong/Type-II certificate family.