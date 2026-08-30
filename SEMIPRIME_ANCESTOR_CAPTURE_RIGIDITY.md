# Semiprime Ancestor Capture and Factorization Rigidity

**Status:** exact local definitions plus finite exploratory census; no universality or novelty claim.

Let

\[
A=uv
\]

with distinct primes `u<v`, and put

\[
m_A=4uv-1.
\]

For every earlier depth `B<A` with

\[
m_B=4B-1\mid m_A,
\]

define

\[
Q_B=\{D\pmod{m_B}:D\mid B^2\}.
\]

The semiprime mixed square-completion pair is inherited from `B` exactly when

\[
u^2\pmod{m_B}\in Q_B,
\]

in which case `v^2` is inherited automatically.

## Capture ratio

Let `QR^*(m_B)` denote the unit quadratic-residue classes modulo `m_B`. Define

\[
\eta(B)=\frac{|Q_B\cap QR^*(m_B)|}{|QR^*(m_B)|}.
\]

This is the fraction of possible unit square classes that depth `B` shadows whenever `m_B | m_A`.

The accompanying exact script `ancestor_capture_ratio_analyzer.py` computes `eta(B)` and the missed square classes.

For small `B`, notable values are:

| B | m_B | captured / unit square classes | eta(B) |
|---:|---:|---:|---:|
| 1 | 3 | 1/1 | 1 |
| 2 | 7 | 3/3 | 1 |
| 4 | 15 | 2/2 | 1 |
| 10 | 39 | 5/6 | 0.8333... |
| 6 | 23 | 9/11 | 0.8181... |
| 30 | 119 | 15/24 | 0.625 |
| 3 | 11 | 3/5 | 0.6 |
| 12 | 47 | 13/23 | 0.5652... |

The missed unit-square classes in several strong cases are especially small:

- `B=10`, modulus `39`: only `16` is missed;
- `B=6`, modulus `23`: only `8,16` are missed;
- `B=3`, modulus `11`: only `4,5` are missed.

Thus a primitive semiprime layer satisfying one of these divisibility conditions must place `u^2` in a very small exceptional square-class set.

## Finite factorization-complexity signal through A = 100000

Among the `23,313` squarefree semiprime indices `A<=100000`:

- `15,433` are inherited by at least one earlier divisor-modulus ancestor;
- `7,880` have a structurally primitive mixed pair.

For the `7,880` primitive indices, the number `omega(m_A)` of distinct prime factors of `m_A=4A-1` is distributed as:

- `omega=1`: 3,218;
- `omega=2`: 3,918;
- `omega=3`: 716;
- `omega=4`: 28;
- `omega>=5`: 0.

Hence

\[
\boxed{7136/7880\approx0.9056}
\]

of the primitive semiprime indices in this range have `m_A` with at most two distinct prime factors.

The inherited population behaves very differently:

- `omega=1`: 4;
- `omega=2`: 5,187;
- `omega=3`: 7,572;
- `omega=4`: 2,494;
- `omega=5`: 175;
- `omega=6`: 1.

These are finite statistics only. They strongly suggest that increasing divisor complexity of `4uv-1` creates enough independent ancestor tests to make primitive survival rare.

## Research target

The natural theorem target is now a factorization-rigidity statement rather than a density estimate. A useful form would be:

> If `4uv-1` has sufficiently rich `3 mod 4` divisor structure, then one proper ancestor `B` satisfies `u^2 mod (4B-1) in Q_B`.

Even a weaker theorem bounding the number of distinct prime factors of `4uv-1` for primitive semiprime layers would be substantial structural progress.

A practical next step is to search for incompatible combinations among the high-capture ancestors. For example:

- if `23 | 4uv-1`, primitive survival forces `u^2 mod 23` into `{8,16}`;
- if `39 | 4uv-1`, primitive survival forces `u^2 mod 39` to equal `16`;
- if `11 | 4uv-1`, primitive survival forces `u^2 mod 11` into `{4,5}`.

The goal is to prove that sufficiently many such simultaneous constraints cannot coexist with `uv=(m_A+1)/4` and primality of `u,v`, or force a smaller ancestor by CRT/descent.

## Claim boundary

This note does not prove that `omega(4uv-1)` is bounded for primitive layers, and it does not prove Type-II universality. The concentration observed through `A=100000` is a theorem-mining signal that must be converted into an exact argument before publication as a mathematical result.
