# Single-Nonsquare-Coordinate Reduction for Exact Type-II Square Depth

**Status:** unconditional structural reduction theorem. It turns a global exact-depth problem into finitely many local checks when the target residue is quadratic-residue at every target prime except one. No novelty claim pending literature comparison.

Let

\[
A\ge1,
\qquad
m_A=4A-1,
\qquad
D\mid A^2,
\]

and write

\[
t\equiv-4D\pmod{m_A}.
\]

Assume `gcd(t,m_A)=1`.

For every earlier depth `B<A`, let

\[
m_B=4B-1,
\qquad
R_B=\{-4E\pmod{m_B}:E\mid B^2\}.
\]

Every element of `R_B` has Jacobi symbol `-1` modulo `m_B`; in particular every unit square modulo `m_B` is safe.

## Theorem — one bad prime coordinate

Suppose there is a prime

\[
r\mid m_A
\]

such that

1. `t` is a quadratic nonresidue modulo `r`;
2. for every prime `p|m_A`, `p!=r`, the class `t mod p` is a nonzero quadratic residue modulo `p`.

Let

\[
L=\operatorname{lcm}_{1\le B<A}m_B.
\]

Choose a unit residue class `c mod L` prime-power coordinate by prime-power coordinate as follows.

- On powers of `r`, choose any unit lift congruent to `t mod r`.
- On powers of every other target prime `p|m_A`, choose a square lift congruent to `t mod p`.
- On all remaining prime-power coordinates, choose an arbitrary unit square (for example `1`), except that further square choices may be adjusted if useful on exceptional ancestors.

Then the target congruence

\[
n\equiv t\pmod{m_A}
\]

is CRT-compatible with `n==c (mod L)` at every shared target prime.

Moreover, for every earlier depth `B<A` satisfying

\[
r\nmid m_B,
\]

the residue `c mod m_B` is a unit square modulo `m_B`, hence

\[
c\pmod{m_B}\notin R_B.
\]

Therefore **all earlier layers not divisible by `r` are excluded simultaneously**.

The exact-depth problem reduces entirely to the finite exceptional set

\[
\boxed{
\mathcal B_r(A)=\{B<A:r\mid4B-1\}.
}
\]

If the square coordinates can be chosen so that

\[
c\pmod{m_B}\notin R_B
\qquad(B\in\mathcal B_r(A)),
\]

then, after also imposing `n==1 (mod 4)`, the combined CRT progression is reduced and Dirichlet's theorem gives infinitely many primes `p` with

\[
\boxed{\delta_{\rm sq}(p)=A.}
\]

### Proof

At every prime-power coordinate other than `r`, the selected residue is a square. Hence if `r` does not divide `m_B`, the full residue modulo `m_B` is a unit square by CRT. The universal Jacobi obstruction excludes every Type-II square-completion trap at depth `B`.

Only moduli containing `r` can see the one nonsquare local coordinate. Those are precisely the members of `\mathcal B_r(A)`, so checking them is sufficient.

Target compatibility holds because on every prime dividing `gcd(m_A,L)` the selected coordinate reduces to `t` modulo that prime; higher powers occurring only in `L` may be chosen freely subject to that reduction. All coordinates are units, so the final CRT residue is coprime to the combined modulus. Dirichlet then supplies infinitely many prime members. The target congruence gives the depth-`A` witness and the local exclusions rule out every `B<A`.

## Size of the exceptional set

The reduction is especially effective when `r` is large.

If `r==1 (mod 4)`, then any modulus `m_B` divisible by `r` has the form

\[
m_B=rs,
\qquad
s\equiv3\pmod4,
\qquad
rs<m_A.
\]

Thus the number of exceptional layers is on the order of

\[
\frac{m_A}{4r},
\]

rather than `A`.

The analogous statement for `r==3 (mod 4)` has `s==1 (mod 4)`.

## Application 1: A=649

For

\[
649=11\cdot59,
\qquad
m_A=2595=3\cdot5\cdot173,
\]

all four branches

\[
D\in\{11,59,7139,38291\}
\]

are square at the `3`- and `5`-coordinates and nonsquare at `r=173`.

There are only three exceptional earlier layers:

\[
\mathcal B_{173}(649)=\{130,303,476\}.
\]

The twelve local checks in `EXACT_DEPTH_649_THREE_ANCESTOR_PROOF.md` are all safe, proving exact depth `649` for infinitely many primes in all four branches.

## Application 2: A=22339

For

\[
22339=89\cdot251,
\qquad
m_A=89355=3\cdot5\cdot7\cdot23\cdot37,
\]

and

\[
D\in\{89,251,1988171,5607089\},
\]

the target residue `-4D` is a quadratic residue at `3,5,7,23` and a quadratic nonresidue at the unique bad coordinate

\[
r=37.
\]

Hence every earlier layer not divisible by `37` is excluded automatically. There are only

\[
\boxed{603}
\]

earlier `37`-bearing moduli.

Choosing square lifts on `3,5,7,23`, setting all otherwise-free coordinates to `1`, and using the square coordinate

\[
67\mapsto4
\]

for the branches `D=251` and `D=1988171` (while retaining `67->1` for the other two branches) avoids every one of those 603 exceptional layers. The reduced verifier `verify_depth_22339_single_bad_coordinate.py` reconstructs and checks these local trap sets directly.

Thus the former all-layer CSP proof reduces to one universal square-safe argument plus `603*4` finite local checks.

## Interpretation

This theorem identifies an intermediate mechanism strictly stronger than global Jacobi-safe CRT and much simpler than the full branch-dependent CSP:

\[
\text{global square/Jacobi safety}
\quad\longrightarrow\quad
\text{single-bad-coordinate finite exceptions}
\quad\longrightarrow\quad
\text{full CSP}.
\]

The depths `649` and `22339` lie outside the Jacobi-new `3q` backbone, but their exact-depth proofs have only one genuinely nonsquare local coordinate. This explains why a small amount of branch-dependent information suffices even though a globally Jacobi-safe construction is impossible.

## Claim boundary

The theorem is a sufficient reduction, not a classification of all exact-depth mechanisms. It does not imply universal Type-II solvability or the Erdős--Straus conjecture.