# Global Type-II Wall and the Next Proof Target

**Status:** research-direction note; no proof of universal Type II or Erdős--Straus is claimed.

## 1. Exact global target

For prime `p == 1 (mod 4)`, complete Type II is equivalent to the square-completed criterion

\[
\boxed{
\exists A,D>0:
\qquad D\mid A^2,
\qquad 4A-1\mid p+4D,
\qquad p\nmid D.
}
\]

Pomerance--Weingartner record that every prime below `10^13` has a Type-II solution for the classical `m=4` problem and conjecture that this persists beyond `10^13`. They prove that analogous universality fails for every `m>=6`, so the `m=4` case is genuinely exceptional.

The global target of this repository is therefore mathematically natural:

\[
\boxed{\text{prove that every prime }p\text{ has some complete Type-II witness }(A,D).}
\]

This is stronger than Erdős--Straus itself, because a prime may in principle be solvable only through Type I.

## 2. What the current analytic results actually prove

### Fixed finite shift sets

For a fixed finite unit-partner shift set `U`, the integer Selberg sieve gives

\[
|E_U(N)|\ll_U \frac{N}{(\log N)^{1+|U|/2}}.
\]

For the audited `75`-shift window this gives the formal exponent `38.5`.

This is powerful but **fixed-depth**. The implied constant, the finite half-group cover, the Mertens-in-progression constants, the threshold prime `Q0(U)`, and the sieve-level choices all depend on `U`. The theorem therefore does not justify replacing `U` by a set growing with `N`.

### Growing cofactor depth

The one-parameter cofactor subsystem has the same local counting function as Dahan's one-parameter large-sieve system,

\[
\rho_J(q)=\#\{a\le J:4a\mid q+1\},
\]

which yields genuine uniform growing-depth estimates, including

\[
|E_{\rm cof}(N;J)|
\ll
N\exp\!\left(-(κ_0\lambda+o(1))(\log\log N)^2\right)
\]

for `J=(log N)^lambda`, and an optimized regime of the shape

\[
N\exp\!\left(-(0.199+o(1))\sqrt{\log N}\right).
\]

Dahan's complete two-parameter search gives still stronger subexponential thinning.

## 3. Why density cannot finish the theorem

Every bound currently available has the form

\[
|E(N)|\le N\,e^{-f(N)}
\]

with

\[
f(N)=o(\log N).
\]

Hence the upper bound itself still tends to infinity.

For example,

\[
N\exp(-c\sqrt{\log N})\to\infty,
\]

and likewise

\[
N\exp(-c(\log N)^{2/3})\to\infty.
\]

Therefore even a perfectly correct density theorem of these strengths cannot imply that the exceptional set is finite or empty.

The fixed-shift superlogarithmic statement

\[
|E(N)|\ll_A N/(\log N)^A
\quad\text{for every fixed }A
\]

has the same limitation: sets of infinite cardinality can be thinner than every fixed power of `1/log N`.

### Conclusion

\[
\boxed{\text{Further improvement of sieve exponents alone is not the missing final step.}}
\]

A universal proof needs an additional pointwise structural mechanism.

## 4. The required structural mechanism

A hypothetical Type-II survivor `p` must avoid every trap

\[
S_A=\{-4D\pmod{4A-1}:D\mid A^2\}
\]

for every positive `A`.

The next proof target should therefore be one of the following equivalent-style mechanisms.

### A. Descent

Prove that if `p` avoids all witnesses up to a sufficiently structured depth, then its arithmetic data force a smaller object satisfying the same obstruction. Iterating would terminate in an impossible base case.

### B. Forced composite rescue

Prime-modulus layers explain an infinite exact-depth backbone but do not cover every prime. Prove that every prime escaping the prime-modulus / easy boundary layers is forced into a **composite** modulus `4A-1` with some divisor `D|A^2` satisfying

\[
p\equiv-4D\pmod{4A-1}.
\]

### C. Finite-state rigidity

Show that the local residue/character states of a survivor cannot persist indefinitely: after finitely many transitions every allowable state must enter a Type-II trap.

Any of these would convert density information into pointwise existence.

## 5. Exact-depth work is now separate

The square-completed exact-depth spectrum is unbounded and has a prime-modulus backbone. The corrected files

- `TYPEII_DEPTH_UNBOUNDED.md`, and
- `TYPEII_DEPTH_LOG_LOWER_BOUND.md`

now use exact first hits rather than mere avoidance.

Those depth theorems are useful structural information, but exact-depth realizability is not the Erdős--Straus wall. A prime only needs **some** Type-II hit.

## 6. Recommended next attack

The highest-value next calculation/theorem search is:

> Condition on failure of the strongest cheap boundary/unit-partner layers and classify the first genuinely composite square-completion layers that can rescue the survivor. Search for a transition rule that reduces every remaining residue/character state to an earlier solved state.

Concretely:

1. work with the full trap `S_A`, not only a unit-partner slice;
2. prioritize composite `A` where completion contributes genuinely mixed divisors `D|A^2`;
3. quotient out trap residues already inherited/shadowed from smaller moduli;
4. compute the residual state graph exactly for the first several composite layers;
5. look for a monotone invariant, forced cycle contradiction, or descent map;
6. only after an exact pattern is identified, promote it to a theorem.

This is the point where computation can still help materially: not by extending the verified prime bound, but by discovering the finite arithmetic transition rule needed for a pointwise proof.

## 7. Claim boundary

- Erdős--Straus remains open.
- Universal prime Type II remains open.
- Finite verification, however large, does not settle either statement.
- Sieve sparsity does not imply finiteness.
- The plausible missing ingredient is structural rigidity/descent in the composite rescue core.
