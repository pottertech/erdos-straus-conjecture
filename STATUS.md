# Determination: the conjecture remains open (2026-11-19)

**Determination: no proof of the Erdős–Straus conjecture exists in this repository, or in the literature, as of 2026-11-19.**

## What does hold

- The exact criteria, the verifiers, and the certified Lean build set are green (CI run 44434792045 and successors); the two known-broken modules are tracked in issue #6.
- Everything reduces, by results that check out, to the resilient prime class n ≡ 1 (mod 12) with 5 ∤ n (for primes, residues 1, 13, 37, 49 mod 60 — provably infinite by Dirichlet).
- The proven deterministic cascade narrows hard cases further to n ≡ 1 (mod 24) with every odd prime factor of n+1 and every prime factor of n+4 ≡ 1 (mod 4) (`DETERMINISTIC_CASCADE_STATUS.md` §1). Each layer is finite-group algebra; the finite tables are cross-checks, not the proof.
- The strongest honest theorem, `erdos_straus_except_residual_open_class` (`MainTheorem.lean`), is exactly what its name says.

## The exact gap (proof-shaped)

1. **No covering theorem over the residual class.** Proven layers shrink the corrected prime hard cases 48,711 → 283 below 10^7; extending the same sweep through further moduli leaves a single survivor, n = 8,803,369 — settled by computation (first works at u = 107), not by a covering argument. There is no theorem that any finite set of u values, or any bound on A, reaches every prime in the residual class. Whether the cascade terminates for every such prime is open.
2. **The residual class is assumed in the Lean assembly.** `erdos_straus_mod_12_1_not_div_5_conjecture` (`Mod12Case1.lean`) is one of the four whitelisted axioms: the hard core sits in the development as a hypothesis.
3. **The analytic route is not a completed proof anywhere in the repo.** The Burgess-type inputs (`C_burgess`, `burgess_least_qnr_bound`) are axioms inside `NewTheorems.lean`, which does not compile on the pinned toolchain (issue #6); the v12 manuscript itself declines to claim the route as finished until its sieve and covering assumptions are formalized.
4. **Computation cannot close a universal claim.** Exhaustive verification to 10^9 (this repo) and ≈10^18 (literature) bound nothing universal. Note also: while the broad resilient class is provably infinite, the infinitude of the *narrow* forced-structure subclass is itself unproved; its members are empirically plentiful (48,711 prime hard cases below 10^7, 283 residual survivors).

## What would change this determination

- A **covering theorem**: some explicit finite set of u values — or a bound on A — provably reaching every prime in the residual class (equivalently, a termination theorem for the modular cascade over the class).
- The **analytic route completed**: the Burgess/least-QNR inputs proved rather than assumed, with the covering-set assumptions formalized to the bar set in the v12 manuscript's §5.1.

Until one of those exists, any claim of a proof — here or in the literature — is premature. Update this file only with new theorems or recorded corrections.
