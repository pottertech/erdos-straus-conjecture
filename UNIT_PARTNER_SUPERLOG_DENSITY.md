# Super-Logarithmic Sparsity of Global Untwisted Unit-Partner Failures

**Status:** unconditional corollary of the certified fixed finite multi-shift sieve; not a finiteness theorem

Let `H(N)` denote the number of primes `n <= N`, `n == 1 (mod 4)`, for which the untwisted unit-partner branch fails at **every** admissible shift

\[
u\equiv3\pmod4.
\]

By `UNIT_PARTNER_MULTI_SHIFT_SIEVE.md`, for any fixed finite set `U` of admissible shifts,

\[
H(N)\le E_U(N)
\ll_U
\frac{N}{(\log N)^{1+|U|/2}}.
\]

Now fix any real `A>0`. Choose a fixed finite shift set `U_A` satisfying

\[
1+|U_A|/2\ge A.
\]

The shift set depends only on `A`, not on `N`. Therefore its implied sieve constant may be absorbed into a constant depending on `A`. Hence

\[
\boxed{
H(N)\ll_A\frac{N}{(\log N)^A}
\qquad\text{for every fixed }A>0.
}
\]

Thus primes that evade the untwisted unit-partner branch at **all** admissible shifts form a super-logarithmically sparse set: their counting function is smaller than `N/log^A N` for every fixed power `A`.

The same conclusion holds for primes which fail the complete centered binary criterion at every admissible shift, because complete-binary failure implies untwisted unit-partner failure.

## What this means

This is stronger than density zero and stronger than any one fixed logarithmic-power saving.

It still does **not** imply finiteness. An infinite set can have counting function `o(N/log^A N)` for every fixed `A`.

The permanent unit-partner exception `2521` is therefore compatible with this theorem. The theorem permits a finite exceptional set, or even an infinite sufficiently sparse one.

## Relation to current literature

Benjamin Dahan's 2026 fixed-depth sieve proves the analogous logarithmic-dimension phenomenon for a broader explicit Erdős--Straus witness system and obtains a super-logarithmic exceptional-set corollary from arbitrarily large fixed depth. The present statement is the corresponding consequence for the unit-partner shift family, with the fixed-finite-set sieve proved separately in `UNIT_PARTNER_MULTI_SHIFT_SIEVE.md`.

Reference: Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035 (2026), especially Lemma 4.2, Theorem 4.3, and Corollary 4.5.
