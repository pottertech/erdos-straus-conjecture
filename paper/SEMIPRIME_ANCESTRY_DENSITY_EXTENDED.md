# Extended Semiprime Ancestry-Density Bound

This note strengthens `SEMIPRIME_ANCESTRY_DENSITY.md` by adding two further fixed ancestors whose moduli are coprime to the modulus `231` already used for depths `1,2,3`.

We retain the setup

\[
A=uv,
\qquad u<v\text{ distinct primes},
\]

and study divisor-modulus inheritance of the mixed-square pair `(u^2,v^2)`.

From depths `1,2,3`, the previously proved survivor proportion is at most

\[
\frac{47}{120}+o(1).
\]

## Depth 6

Here

\[
m_6=23.
\]

The exact local capture calculation gives

\[
\eta_6=\frac9{11},
\]

meaning that, conditional on the ancestor being present (`A == 6 mod 23`), `9` of the `11` unit square classes are inherited.

Since `phi(23)=22`, the unconditional capture probability for this ancestor is

\[
\frac{1}{22}\frac9{11}=\frac9{242}.
\]

The modulus `23` is coprime to `231`, so fixed-modulus semiprime equidistribution gives asymptotic independence from the earlier survivor condition. Thus the survivor proportion is multiplied by

\[
1-\frac9{242}=\frac{233}{242}.
\]

## Depth 12

Here

\[
m_{12}=47.
\]

The exact local capture ratio is

\[
\eta_{12}=\frac{13}{23}.
\]

Because `phi(47)=46`, the unconditional capture probability is

\[
\frac1{46}\frac{13}{23}=\frac{13}{1058}.
\]

Again `47` is coprime to `231*23`, so the survivor factor is

\[
1-\frac{13}{1058}=\frac{1045}{1058}.
\]

## Theorem

Among squarefree semiprime indices `A=uv`, the asymptotic proportion whose mixed-square pair survives all five fixed ancestors

\[
B\in\{1,2,3,6,12\}
\]

is at most

\[
\boxed{
\frac{47}{120}\cdot\frac{233}{242}\cdot\frac{1045}{1058}
=
\frac{208069}{558624}
\approx0.3724669903.
}
\]

Consequently the inherited proportion is at least

\[
\boxed{
1-\frac{208069}{558624}
=
\frac{350555}{558624}
\approx0.6275330097.
}
\]

Thus

\[
\boxed{
\text{at least }62.7533\%+o(1)
}
\]

of squarefree semiprime mixed-square layers are already inherited by these five fixed ancestors.

This is an unconditional asymptotic statement obtained from fixed-modulus prime/semiprime equidistribution and exact finite local capture sets. It does not assert that the remaining `37.2467%` are globally primitive: further divisor ancestors or non-dividing earlier layers can capture additional cases.

## Generalization

For any additional fixed ancestor `B` with modulus `m_B=4B-1` coprime to the accumulated CRT modulus and exact unit-square capture ratio `eta(B)`, the survivor bound is multiplied by

\[
1-\frac{\eta(B)}{\varphi(m_B)}.
\]

This makes the search for stronger rigorous density bounds a finite optimization problem: choose a collection of pairwise-coprime high-capture ancestor moduli, compute their exact local capture ratios, and multiply the corresponding survivor factors. For overlapping moduli, replace the product rule by exact enumeration modulo the finite least common multiple.

## Claim boundary

This theorem is about inheritance of the semiprime **mixed-square pair** only. It is not a Type-II universality theorem and it does not create an exact-depth family outside the `3q` backbone.