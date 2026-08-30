# Minimal Descent for the Five-Factor Ancestry Conjecture

**Status:** exact descent lemma plus finite structural census; not a proof of the five-factor conjecture.

Let

\[
m\equiv3\pmod4
\]

and suppose a unit square class

\[
r\in QR(m)
\]

survives every proper square-completed ancestor, meaning that for every proper divisor

\[
1<e<m,\qquad e\mid m,\qquad e\equiv3\pmod4,
\]

we have

\[
r\pmod e\notin Q_{(e+1)/4},
\]

where

\[
Q_B=\{D\pmod{4B-1}:D\mid B^2\}.
\]

## Descent lemma through a 1 mod 4 prime factor

Assume

\[
p\mid m,\qquad p\equiv1\pmod4,
\]

and put

\[
d=\frac{m}{p}.
\]

Then

\[
d\equiv3\pmod4.
\]

Because `d` is itself a proper ancestor divisor of `m`, survival at `m` implies

\[
r\pmod d\notin Q_{(d+1)/4}.
\]

Moreover, every proper divisor

\[
1<e<d,\qquad e\mid d,\qquad e\equiv3\pmod4
\]

is also a proper ancestor divisor of `m`. Therefore

\[
r\pmod e\notin Q_{(e+1)/4}
\]

for all such `e`.

Hence the reduced square class `r mod d` avoids both:

1. the full layer `Q_{(d+1)/4}` attached to `d` itself;
2. every proper `3 mod 4` ancestor of `d`.

Call such a class a **strong survivor** at modulus `d`.

Thus:

\[
\boxed{
\text{survivor at }m\text{ and }p\equiv1(4),\ p\mid m
\Longrightarrow
\text{strong survivor at }m/p.
}
\]

This is an exact descent statement.

## Consequence for a hypothetical five-factor counterexample

Suppose

\[
\omega(m)=5.
\]

If `m` has at least one prime factor `p == 1 (mod 4)`, any survivor at `m` descends to a four-factor modulus

\[
d=m/p\equiv3\pmod4
\]

carrying a strong survivor.

Therefore the five-factor conjecture can fail in this case only above a four-factor **strong-survivor base**.

This is substantially narrower than the set of all four-factor moduli.

## Finite census through d < 100000

An exact scan of all `d < 100000` with

\[
d\equiv3\pmod4,
\qquad \omega(d)=4
\]

found:

- `1,448` four-factor moduli in total;
- only `90` admitting even one strong unit-square survivor;
- `1,358` with no strong survivor at all.

Thus only about `6.2%` of four-factor moduli in this range can even serve as a descent base for a five-factor counterexample having a `1 mod 4` prime factor.

Among the 90 strong bases:

- 67 have prime-mod-4 pattern `(1,1,1,3)`;
- 23 have pattern `(1,3,3,3)`;
- 84 of 90 are divisible by `5`.

The six exceptions not divisible by `5` below `100000` are:

\[
62491=11\cdot13\cdot19\cdot23,
\]

\[
70499=11\cdot13\cdot17\cdot29,
\]

\[
81719=11\cdot17\cdot19\cdot23,
\]

\[
84227=11\cdot13\cdot19\cdot31,
\]

\[
89947=11\cdot13\cdot17\cdot37,
\]

\[
99671=11\cdot13\cdot17\cdot41.
\]

These data suggest that strong four-factor survivors themselves occupy a highly restricted arithmetic family.

## The all-3-mod-4 branch

The descent lemma above removes a `1 mod 4` prime factor while preserving a `3 mod 4` modulus. If all five distinct prime factors of `m` are `3 mod 4`, removing one factor produces a modulus `1 mod 4`, so this direct descent does not apply.

Therefore a proof of the five-factor conjecture naturally splits into two cases:

1. **mixed-signature case:** at least one prime factor of `m` is `1 mod 4`; reduce to classification/elimination of strong four-factor bases;
2. **all-negative case:** all five prime factors are `3 mod 4`; use the many three-factor `3 mod 4` ancestor divisors instead.

This split is exact and should guide the next proof stage.

## Next theorem targets

The most promising targets are now:

1. classify all four-factor moduli admitting a strong survivor;
2. prove that no strong four-factor base can be extended by an additional `1 mod 4` prime while preserving a survivor;
3. separately prove full ancestry coverage when `m` is a product of five `3 mod 4` primes.

Any combination of (2) and (3) proves the five-factor modulus conjecture.

## Claim boundary

The descent lemma is unconditional. The finite census and observed concentration around the factor `5` are computational evidence only. No classification theorem for strong four-factor bases is claimed yet.
