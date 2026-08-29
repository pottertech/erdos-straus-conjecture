# Dyachenko 2025 Claim Audit

**Status:** literature-safety note

Several recent repositories cite E. Dyachenko, arXiv:2511.07465, as though it supplied an unconditional universal existence theorem for the divisor-adaptive / ED2 family and therefore an unconditional proof of the Erdős--Straus conjecture for primes `P == 1 (mod 4)`.

That citation must not be used in this repository without qualification.

## What the paper's abstract and introduction claim

The abstract and introduction describe a central result labelled Theorem 10.21 and state that every prime

\[
P\equiv1\pmod4
\]

has a constructive ED2 representation.

Taken alone, that language sounds like a proof of the outstanding prime case.

## What the body and conclusion say

The same arXiv version contains explicit qualifications that conflict with reading the abstract as a completed global proof.

In particular:

1. Section 9 is titled **"Algorithm convergence and conditional completeness of coverage"**.
2. Section 9.13 introduces a **Canon Existence Hypothesis**.
3. Appendix D.7 is explicitly titled **"Conditional residue covering scheme"**.
4. The direct-algorithm discussion states that the global guarantee
   
   > for every `P` there exists a suitable pair `(r,s)` from a fixed finite list
   
   corresponds to that conditional covering scheme.
5. The conclusion states explicitly that the general case, with `P` running over infinite sets, is **not proven constructively in the present work**, and that the Appendix-D sections using Dirichlet's theorem and finite coverings are conditional in nature.
6. Appendix D.17 summarizes the covering component as a **conditional finite covering scheme**.

Therefore the paper cannot safely be cited as an unconditional theorem establishing a universal ED2 witness for every prime.

## Consequence for this repository

Do **not** use a statement of the form

\[
\text{Dyachenko proves every hard prime has a good divisor / ED2 witness.}
\]

as an input theorem.

The algebraic ED2 constructors and conditional parametrizations may still be useful and can be checked independently. But the missing global covering/existence assertion is exactly the kind of step that would solve the open conjecture and must be treated as unproved unless supported by a separate peer-reviewed theorem with complete hypotheses.

## External Lean repository caution

A recent Lean-oriented repository comments that Dyachenko proves its `good_divisor_exists` axiom unconditionally and with a small shift bound. The cited arXiv source does not justify that comment as written; the source itself retains conditional coverage hypotheses and explicitly disclaims a constructive proof of the general infinite case.

Accordingly, that external repository is useful for algebraic/formal cross-checking but **not** as evidence that the global number-theoretic existence axiom has been discharged.

## Publication rule

If Dyachenko 2511.07465 is cited in our manuscript, distinguish:

- algebraic identities / constructors: potentially usable after direct verification;
- computational observations: evidence only;
- affine-lattice parametrization: structural framework;
- universal coverage: **do not claim unconditional based on this version**.

This protects the current work from accidentally importing the very global existence statement it is trying to prove.