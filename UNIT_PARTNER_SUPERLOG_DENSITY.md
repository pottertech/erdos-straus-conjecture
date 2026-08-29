# Super-Logarithmic Sparsity of Global Untwisted Unit-Partner Failures

**Status:** corollary of the fixed-finite-set multi-shift sieve; not a finiteness theorem

Let `H(N)` denote the number of primes `n <= N`, `n == 1 (mod 4)`, for which the untwisted unit-partner branch fails at **every** admissible shift

\[
u\equiv3\pmod4.
\]

For any fixed finite set `U` of admissible shifts, the globally failing set is contained in the set failing all shifts in `U`. The multi-shift half-dimensional sieve gives

\[
H(N)\le E_U(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
\]

Now fix any real `A>0`. Choose a finite shift set `U` with

\[
1+|U|/2\ge A.
\]

Since `U` is fixed once `A` is fixed, its implied constant may be absorbed into a constant depending on `A`. Therefore

\[
\boxed{
H(N)\ll_A\frac{N}{(\log N)^A}
\qquad\text{for every fixed }A>0.
}
\]

Thus primes that evade the untwisted unit-partner branch at every shift have counting function smaller than `N / log^A N` for every fixed power `A`.

This is a strong density statement but **does not imply that the set is finite**. A set may be infinite while having super-logarithmically sparse counting function.

Benjamin Dahan's 2026 fixed-depth sieve establishes an analogous super-logarithmic sparsity phenomenon for a related broader Erdős--Straus search; the present corollary is the unit-partner/shift notation specialization developed in this repository.
