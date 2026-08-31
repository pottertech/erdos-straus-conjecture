# Universal Square-Safe Residues and a General Exact-Depth Overlap Criterion

**Status:** unconditional theorem. No novelty claim is made pending a direct comparison with the existing square-shadow / ancestry literature.

For a depth `B >= 1`, write

\[
m_B=4B-1,
\qquad
R_B=\{-4E\pmod{m_B}: E\mid B^2\}.
\]

The earlier manuscript used only the fact that residue `1` is never in `R_B`. The stronger statement is that **no square residue is ever in `R_B`**.

## Theorem 1: every square residue is universally safe

For every positive integers `B,t` and every divisor `E | B^2`,

\[
\boxed{t^2\not\equiv -4E\pmod{4B-1}.}
\]

Equivalently,

\[
\boxed{R_B\cap \{x^2\bmod m_B:x\in\mathbb Z\}=\varnothing.}
\]

### Proof

Put

\[
m=4B-1.
\]

First note that

\[
\gcd(B,m)=1,
\]

and hence every divisor `E | B^2` is coprime to `m`.

We claim that for every prime `r | B`,

\[
\left(\frac r m\right)=1,
\]

where the symbol is the Jacobi symbol.

If `r` is odd, then `m == -1 (mod r)`, and quadratic reciprocity for the Jacobi symbol gives

\[
\left(\frac r m\right)
\left(\frac m r\right)
=(-1)^{((r-1)/2)((m-1)/2)}.
\]

Since `m == 3 (mod 4)`, the right side is

\[
(-1)^{(r-1)/2}.
\]

But

\[
\left(\frac m r\right)
=\left(\frac{-1}r\right)
=(-1)^{(r-1)/2},
\]

so

\[
\left(\frac r m\right)=1.
\]

If `r=2`, then `2|B` implies

\[
m=4B-1\equiv7\pmod8,
\]

and therefore

\[
\left(\frac2m\right)=1.
\]

Every prime divisor of `E` divides `B`, so multiplicativity yields

\[
\boxed{\left(\frac E m\right)=1.}
\]

Since `m == 3 (mod 4)`,

\[
\left(\frac{-1}m\right)=-1,
\qquad
\left(\frac4m\right)=1.
\]

Therefore

\[
\boxed{
\left(\frac{-4E}{m}\right)=-1.
}
\]

If `t^2 == -4E (mod m)`, then the right side is coprime to `m`, so `t` is coprime to `m`; every coprime square has Jacobi symbol `+1`, contradiction.

Hence no trap residue `-4E` is a square modulo `m_B`.

---

## The ancestral-overlap modulus

For a target depth `A`, define

\[
m_A=4A-1,
\]

and

\[
L_{A-1}=\operatorname{lcm}_{1\le B<A}(4B-1).
\]

Define the total ancestral overlap

\[
\boxed{
H_A=\gcd(m_A,L_{A-1}).
}
\]

Thus `H_A` contains exactly the prime-power part of the target modulus that already occurs among earlier depth moduli.

## Theorem 2: square-safe overlap criterion

Let `A,D` be positive integers with

\[
D\mid A^2.
\]

Suppose the target residue

\[
a=-4D
\]

is a square modulo `H_A`; that is, there exists an integer `t` such that

\[
\boxed{t^2\equiv -4D\pmod{H_A}.}
\]

Then there are infinitely many primes `p == 1 (mod 4)` for which

\[
\boxed{\delta_{\rm sq}(p)=A.}
\]

### Proof

Because `D | A^2` and `gcd(A,m_A)=1`,

\[
\gcd(D,m_A)=1.
\]

Hence the target residue `a=-4D` is a unit modulo `m_A`, and therefore the square root `t` modulo `H_A` is a unit modulo `H_A`.

Extend `t` to a residue modulo `L_{A-1}` that is coprime to `L_{A-1}`: on every prime-power coordinate dividing `H_A`, retain the chosen square root; on every prime-power coordinate of `L_{A-1}` not dividing `H_A`, choose any nonzero residue, for example `1`.

Now impose

\[
\boxed{
n\equiv -4D\pmod{m_A},
\qquad
n\equiv t^2\pmod{L_{A-1}},
\qquad
n\equiv1\pmod4.
}
\]

The first two congruences are CRT-compatible exactly because

\[
\gcd(m_A,L_{A-1})=H_A
\]

and

\[
t^2\equiv-4D\pmod{H_A}.
\]

The modulus `4` is coprime to all odd moduli involved.

For every earlier `B<A`, one has `m_B | L_{A-1}`, so

\[
n\equiv t^2\pmod{m_B}.
\]

By Theorem 1 this square residue cannot equal any earlier trap residue

\[
-4E\pmod{m_B},\qquad E\mid B^2.
\]

Therefore no earlier square-completed Type-II witness exists.

At depth `A`, however,

\[
n\equiv-4D\pmod{m_A},
\qquad D\mid A^2,
\]

so the target witness exists.

The resulting CRT progression is reduced. On every prime factor inherited from `L_{A-1}`, the residue is the square of a unit; on every prime factor of `m_A` not contained in `L_{A-1}`, the residue is `-4D`, also a unit; and the residue modulo `4` is `1`.

Dirichlet's theorem therefore gives infinitely many prime members, every one congruent to `1 mod 4` and every one having exact square-completion depth `A`.

---

## Corollary: the `3q` backbone is a special case

Let

\[
q\equiv1\pmod4\text{ be prime},
\qquad
A=\frac{3q+1}{4}.
\]

Then

\[
m_A=3q.
\]

The prime `q` cannot occur in an earlier modulus `4B-1`, because any such earlier multiple of `q` congruent to `3 mod 4` would be at least `3q=m_A`. Hence

\[
H_A\mid3.
\]

For `D|A^2` with `D == 2 (mod 3)`,

\[
-4D\equiv1\pmod3,
\]

which is a square. Thus Theorem 2 recovers the structural `3q` exact-depth family from the manuscript.

---

## Finite sanity check

The criterion is sufficient, not universal. A direct finite scan of small depths finds both successes and failures. For example:

- `A=4`, `H_A=3`, and `D=2` succeeds;
- `A=10`, `H_A=3`, and `D=2` succeeds;
- `A=22`, `H_A=3`, and `D=2` succeeds;
- `A=7`, `H_A=3`, no divisor `D|A^2` satisfies the square-overlap condition;
- `A=9`, `H_A=35`, no divisor `D|A^2` satisfies it.

Thus the theorem supplies a broad structural exact-depth mechanism but does not collapse the full Type-II problem.

## Significance and claim boundary

The candidate structural contribution is the use of the full square-safe residue set, rather than a single safe residue, to obtain the overlap criterion

\[
\boxed{
-4D\in QR(H_A)
\Longrightarrow
A\text{ is infinitely prime-realized as an exact square depth}.
}
\]

No priority claim is made. The result must be compared directly with the existing square-shadow, extension-shadow, reciprocity, and modulus-ancestry literature before publication language is chosen.

This theorem does not prove universal Type-II solvability or the Erdős--Straus conjecture.