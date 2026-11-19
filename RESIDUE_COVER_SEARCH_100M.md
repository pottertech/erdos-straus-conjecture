# Finite Residue-Cover Search Through 10^8

**Date:** 2026-08-28

A residue-only search was run on the 26,399 corrected residual primes below `10^8` to test whether the short-relation phenomenon collapses to a simple CRT cover of the form

\[
n \bmod L \Longrightarrow \text{fixed gate or fixed route type}.
\]

Tested moduli included

`840, 1680, 2520, 4200, 8400, 9240, 12600, 18480, 27720, 55440`.

For every tested modulus below 55,440:

- no sufficiently populated residue class had a single fixed gate;
- no sufficiently populated residue class had a single fixed route type;
- only one class at modulus 55,440 reached 95% purity for a route type, and even that class still required gates as large as 227.

## Conclusion

This is a useful negative result. The corrected short-relation cascade does **not** appear reducible to a small fixed congruence partition in `n` alone. The prime-factor structure of

\[
M_u=n(n+u)/4
\]

is essential. Future proof work should combine congruence information with factor/residue information rather than search for a larger purely-CRT table.
