# Bibliography and provenance audit

**Status:** publication-hardening note; not a novelty proof.

## Core historical and modern references

1. **Léon Thépault (1979).** Historical source cited in later expositions as a readers' correspondence item in *Pour la Science*, no. 19 (1979). Later sources attribute the divisor-square Type-II construction to this item. The original primary text should be inspected if obtainable before publication.

2. **Michel Mizony and Marie-Line Gardes, _Un point sur la conjecture d'Erdős et Straus_ (Université Claude-Bernard Lyon 1, 2012/2013 exposition).** This source explicitly cites Thépault, records the square-divisor construction, and discusses the least square-completion parameter. Public PDF: `SurErdos_Straus_2013a.pdf` on the Lyon 1 site.

3. **Christian Elsholtz and Terence Tao, _Counting the number of solutions to the Erdős–Straus equation on unit fractions_, J. Aust. Math. Soc. 94 (2013), 50–105; arXiv:1107.1010.** Standard modern Type-I/Type-II framework and solution counting.

4. **Carl Pomerance and Andreas Weingartner, _Exceptions to the Erdős–Straus–Schinzel conjecture_, Ramanujan Journal 69 (2026); arXiv:2511.16817.** Modern complete prime Type-I/Type-II criteria and the general m/n framework.

5. **Benjamin Dahan, _Sieve dimension and search depth for the Erdős–Straus conjecture, n ≡ 1 (mod 24)_, arXiv:2608.24035 (2026).** Modern fixed/growing search-depth formulation for the prime problem.

6. **Free Computation Foundation / CENTL, Erdős–Straus research library (2026).** Relevant public notes include `SQUARE-COMPLETION-PRIOR-ART.md`, `PRIME-MODULUS-BACKBONE.md`, `DEPTH-SPECTRUM.md`, and `CURRENT-FRONTIER`. These explicitly mark the square-divisor mechanism as prior art and develop prime-modulus exact-depth/shadow theory.

## Claim boundary for the present manuscript

Do **not** claim novelty for:

- the divisor-square criterion `D | A^2`, `4A-1 | p+4D`;
- the standard Type-I/Type-II dichotomy;
- CRT, Dirichlet's theorem, or PNT in arithmetic progressions;
- the existence of an exact-depth prime-modulus backbone.

The candidate contribution is restricted to:

- the symbolic composite target family `4A_q-1=3q` with `A_q=(3q+1)/4`;
- the criterion that a divisor `D | A_q^2`, `D ≡ 2 (mod 3)` yields infinitely many primes of exact square-completion depth `A_q`;
- the prime-factor corollary;
- the relative-density-one theorem among primes `q ≡ 1 (mod 4)`;
- the lower bound `N_comp(X) >= (2/3+o(1)) X/log X`;
- the general finite exact-depth CRT certificate theorem and the certified full-layer examples, subject to their separate machine verification.

## Priority search result as of 2026-08-30

Targeted searches of arXiv/web results and the public CENTL repository did not locate the exact algebraic family

`A=(3q+1)/4`, `4A-1=3q`

combined with the `2 mod 3` factor criterion or the resulting density-one exact-depth statement. This is only a negative search result, not proof of first discovery.

## Before submission

- obtain/inspect the original Thépault 1979 item if possible;
- verify the exact publication metadata for the Mizony–Gardes exposition used in the bibliography;
- add DOI or stable publisher links for Elsholtz–Tao and Pomerance–Weingartner;
- have an external number theorist review the symbolic theorem and density argument;
- avoid phrases such as "first", "new", or "novel" in the abstract until the external priority review is complete.
