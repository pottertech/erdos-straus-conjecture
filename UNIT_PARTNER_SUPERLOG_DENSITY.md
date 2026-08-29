# Super-Logarithmic Sparsity Target for Global Untwisted Unit-Partner Failures

**Status:** conditional corollary of the multi-shift sieve proposition pending analytic audit; not a finiteness theorem

Let `H(N)` denote the number of primes `n <= N`, `n == 1 (mod 4)`, for which the untwisted unit-partner branch fails at **every** admissible shift

\[
u\equiv3\pmod4.
\]

For any fixed finite set `U` of admissible shifts, the globally failing set is contained in the set failing all shifts in `U`. If the multi-shift upper-bound-sieve proposition is completed, then

\[
H(N)\le E_U(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
\]

Now fix any real `A>0`. Choose a finite shift set `U` with

\[
1+|U|/2\ge A.
\]

Since `U` is fixed once `A` is fixed, its implied constant may be absorbed into a constant depending on `A`. The resulting target corollary is

\[
\boxed{
H(N)\ll_A\frac{N}{(\log N)^A}
\qquad\text{for every fixed }A>0.
}
\]

Thus, once the sieve proposition is fully audited, primes that evade the untwisted unit-partner branch at every shift would have counting function smaller than `N / log^A N` for every fixed power `A`.

This would be a strong density statement but **would not imply that the set is finite**. A set may be infinite while having super-logarithmically sparse counting function.

Benjamin Dahan's 2026 fixed-depth sieve proves an analogous super-logarithmic sparsity phenomenon for a related broader Erdős--Straus search. That result supports the proposed sieve architecture here, but this repository does not claim the unit-partner statement as an established corollary until the parameter correspondence and sieve hypotheses are checked exactly.
