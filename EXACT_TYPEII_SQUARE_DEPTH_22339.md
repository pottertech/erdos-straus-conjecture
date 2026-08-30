# Infinite Prime Family of Exact Type-II Square Depth 22339

**Status:** unconditional, computationally assisted theorem.  The finite congruence system is generated and checked exactly by `exact_depth_22339_csp_certificate.py`.  No finite prime sampling is used in the proof.  No novelty claim is made pending a dedicated literature review.

For a prime `n == 1 (mod 4)`, define the complete Type-II square depth to be the least positive integer `A` for which there exists

\[
D\mid A^2,
\qquad
4A-1\mid n+4D,
\qquad
n\nmid D.
\]

This is the standard square-completed coordinate form of prime Type II.

## Theorem

There are infinitely many primes

\[
\boxed{p\equiv169\pmod{840}}
\]

whose minimum complete Type-II square depth is exactly

\[
\boxed{22339}.
\]

In particular, exact finite square depth 22339 occurs infinitely often inside one of the six classical Mordell-hard residue classes.

## Target depth

Take

\[
A=22339,
\qquad
D=67079.
\]

One checks exactly that

\[
D\mid A^2.
\]

The layer modulus is

\[
m_A=4A-1=89355,
\]

and the Type-II trap progression is

\[
\boxed{n\equiv-4D\equiv89104\pmod{89355}}.
\]

Thus every sufficiently large prime in this progression has a valid depth-22339 Type-II certificate using `(A,D)`.

## Earlier layers as a parameter-space covering problem

Write

\[
n=89104+89355k.
\]

For every earlier depth

\[
1\le B<22339
\]

and every divisor

\[
E\mid B^2,
\]

the corresponding earlier Type-II trap is

\[
n\equiv-4E\pmod{4B-1}.
\]

Put

\[
g_B=\gcd(89355,4B-1),
\qquad
q_B=\frac{4B-1}{g_B}.
\]

If the target progression and the earlier trap are CRT-compatible, then the earlier trap removes exactly one residue class

\[
\boxed{k\equiv c\pmod{q_B}}.
\]

Running this construction for every `B<22339` and every `E|B^2` produces exactly

- `14,210` distinct reduced `k` moduli;
- `577,670` forbidden congruence classes.

The certificate script reconstructs this system from first principles.

## Prime-power CSP certificate

Each forbidden congruence

\[
k\equiv c\pmod q
\]

is decomposed across the prime-power factors of `q`.

A prime-power modulus gives a unary exclusion.  A composite modulus gives one forbidden tuple across its prime-power coordinates.

The certificate is deliberately compact:

1. at each maximal prime-power coordinate, choose the least nonnegative residue satisfying all unary exclusions;
2. replace only the following nine prime coordinates:

\[
\boxed{
19\mapsto4,
\ 41\mapsto2,
\ 47\mapsto3,
\ 107\mapsto2,
\ 293\mapsto1,
\ 331\mapsto1,
\ 853\mapsto1,
\ 5227\mapsto1,
\ 5569\mapsto1.
}
\]

The verifier then checks every one of the `577,670` forbidden classes and finds no violation.

By the Chinese remainder theorem, these compatible prime-power coordinates determine a nonempty arithmetic progression

\[
k\equiv k_0\pmod M,
\]

where `M` is the product of the maximal prime-power coordinate moduli.

Every integer in the resulting `k` progression avoids every Type-II layer

\[
B=1,2,\ldots,22338.
\]

## Reducedness and Dirichlet

The associated denominator progression is

\[
n\equiv n_0\pmod{89355M}.
\]

The verifier checks locally, for every prime dividing the period, that

\[
n_0\not\equiv0\pmod p.
\]

Since also

\[
\gcd(89104,89355)=1,
\]

we obtain

\[
\boxed{\gcd(n_0,89355M)=1}.
\]

Therefore Dirichlet's theorem on primes in arithmetic progressions gives infinitely many primes in this progression.

For all but finitely many of those primes, `p>D`, so the usual condition `p\nmid D` is automatic.  Every such prime:

- has no Type-II square-completed certificate with depth `<22339`;
- has the explicit depth-22339 certificate `(A,D)=(22339,67079)`.

Hence

\[
\boxed{\operatorname{depth}_{\rm sq}(p)=22339}
\]

for infinitely many primes.

## Classical hard-core intersection

The target progression satisfies

\[
89104\equiv64\pmod{105}.
\]

The classical residue

\[
169\pmod{840}
\]

also reduces to `64 mod 105`.

Since the `k`-period `M` is odd, imposing the additional CRT condition

\[
k\equiv3\pmod8
\]

is compatible with the exact-depth certificate and yields

\[
\boxed{n\equiv169\pmod{840}}.
\]

The combined progression remains reduced.  Dirichlet therefore gives infinitely many exact-depth-22339 primes specifically in the classical residue class `169 mod 840`.

## Why this matters

Earlier results established that square-completed Type-II depth is unbounded and can be forced above a prescribed finite threshold.  This theorem is stronger in a different direction: it realizes a specific large finite depth as the **exact first successful depth** for infinitely many classical-core primes.

It also demonstrates that the global first-hit problem is inherently cross-modulus.  Divisor-modulus ancestry alone does not determine first-hit depth; exact CRT interaction among all earlier layers is required.

## Literature / priority boundary

FCF/CENTL publicly records an infinite exact-depth backbone for prime-modulus indices and finite square-completion depth censuses.  Dahan (2026) studies fixed and growing search depth analytically.  The present construction uses a composite high-depth target and an explicit global CRT/CSP avoidance certificate across *all* earlier square-completed layers.

A quick literature audit did not establish whether this precise global exact-depth construction is already present elsewhere.  Absence from a search is not a priority proof.  Accordingly:

- the theorem may be used internally as an unconditional mathematical result;
- no novelty or priority claim should be made until a dedicated comparison with the FCF/CENTL corpus and historical square-completion literature is complete.

## Reproduction

Run

```bash
python3 exact_depth_22339_csp_certificate.py
```

The verifier regenerates all earlier trap congruences, rebuilds the compact prime-power certificate, verifies all forbidden classes, verifies reducedness, and checks compatibility with the classical residue `169 mod 840`.

## Claim boundary

This theorem does **not** prove universal Type-II solvability and does not prove the Erdős--Straus conjecture.  It proves only that one particular large minimum Type-II square depth, 22339, occurs for infinitely many primes.