# Minimal Descent for Mixed-Signature Ancestry Survivors

**Status:** exact descent lemma plus finite structural census. The former five-factor ancestry-cover conjecture has been refuted in the all-`3 mod 4` branch; this note now records only the surviving mixed-signature descent result.

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

## Exact descent lemma through a 1 mod 4 prime factor

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

Thus

\[
\boxed{
\text{survivor at }m\text{ and }p\equiv1(4),\ p\mid m
\Longrightarrow
\text{strong survivor at }m/p.
}
\]

This statement is unconditional.

## Consequence for five-factor mixed-signature moduli

Suppose

\[
\omega(m)=5
\]

and at least one prime factor of `m` is `1 mod 4`. Then any ancestry survivor at `m` descends to a four-factor modulus

\[
d=m/p\equiv3\pmod4
\]

carrying a strong survivor.

Therefore every mixed-signature five-factor survivor must lie above a four-factor strong-survivor base. This remains a useful reduction even though universal five-factor ancestry coverage is false.

## Finite census through d < 100000

An exact scan of all `d < 100000` with

\[
d\equiv3\pmod4,
\qquad\omega(d)=4
\]

found:

- `1,448` four-factor moduli in total;
- `90` admitting at least one strong unit-square survivor;
- `1,358` with no strong survivor.

Thus only about `6.2%` of four-factor moduli in this range can serve as descent bases for a mixed-signature five-factor survivor.

Among the 90 strong bases:

- 67 have prime-mod-4 pattern `(1,1,1,3)`;
- 23 have pattern `(1,3,3,3)`;
- 84 of 90 are divisible by `5`.

The six exceptions not divisible by `5` below `100000` are

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

The new universal-prime-ancestor theorem also proves that every survivor modulus must avoid `3` and `7`.

## The all-3-mod-4 branch is not covered by this descent

If all five distinct prime factors of `m` are `3 mod 4`, removing one factor produces a modulus `1 mod 4`, so the descent lemma does not apply.

More importantly, the former hope that the many one- and three-prime ancestors would automatically cover this branch is false. The smallest admissible all-negative five-prime modulus

\[
6,407,731=11\cdot19\cdot23\cdot31\cdot43
\]

already has an explicit proper-ancestor survivor. See `MODULUS_ANCESTRY_FIVE_FACTOR_CONJECTURE.md` for the exact counterexample.

Therefore no proof target should continue to assert universal all-negative five-factor ancestry coverage.

## Revised theorem targets

The viable targets are now:

1. classify four-factor strong-survivor bases;
2. characterize which `1 mod 4` prime extensions of such bases preserve a survivor;
3. determine whether some mixed-signature condition stronger than `omega(m)>=5` forces coverage;
4. treat the all-negative branch using an additional mechanism beyond proper-ancestor inheritance.

The factor-`5` concentration in the finite four-factor census remains suggestive but is empirical only.

## Claim boundary

The descent lemma is unconditional. The finite census is exact in the stated range. The former global five-factor ancestry-cover conjecture is false and is no longer a research target.