# Certified Fixed-Cofactor Exact-Depth Backbones

**Status:** unconditional theorem schema plus finitely verified rows. No novelty claim pending comparison with current square-lift / reciprocity literature.

The fixed-cofactor exceptional-layer lemma gives a uniform construction of exact square-completed Type-II depth families.

For a fixed odd cofactor `s\equiv3 (mod 4)`, choose a divisor witness `d` and a reduced prime progression

\[
r\equiv a\pmod M,
\qquad M=4d,
\]

such that:

1. `sr+1\equiv0 (mod 4d)`, so `d | A` for
   \[
   A=(sr+1)/4;
   \]
2. `-d` is a quadratic residue modulo the fixed cofactor `s`;
3. `-d` is a quadratic nonresidue modulo every prime `r\equiv a (mod M)`;
4. for every exceptional cofactor `c<s`, `c\equiv3 (mod 4)`, the bounded collision equation
   \[
   r(kh-dc^2)+k+dh-2dc=0
   \]
   has no admissible prime solution in the chosen progression subject to
   \[
   16d\mid rh+1,
   \]
   and the equality configuration `kh=dc^2` is excluded.

Then the single-nonsquare-coordinate reduction makes every earlier modulus not containing `r` square-safe, and the finite exceptional check excludes all remaining earlier layers. Hence

\[
\boxed{
\delta_{\rm sq}(p)=\frac{sr+1}{4}
}
\]

for infinitely many primes `p`, for every prime `r` in the prescribed progression.

## Certified rows

The following rows satisfy all four conditions. The first three (`s=7,11,19`) are proved in dedicated notes; `s=23` also has a dedicated note. The later rows are certified by the common verifier `verify_fixed_cofactor_backbone_table.py`.

| `s` | `d` | prime progression for `r` | target modulus | asymptotic contribution to depth count |
|---:|---:|---:|---:|---:|
| 7 | 3 | `r ≡ 5 (mod 12)`, `r>5` | `7r` | `1/7` |
| 11 | 6 | `r ≡ 13 (mod 24)` | `11r` | `1/22` |
| 19 | 10 | `r ≡ 21 (mod 40)` | `19r` | `1/76` |
| 23 | 20 | `r ≡ 73 (mod 80)` | `23r` | `1/184` |
| 31 | 17 | `r ≡ 57 (mod 68)` | `31r` | `1/248` |
| 43 | 22 | `r ≡ 45 (mod 88)` | `43r` | `1/430` |
| 47 | 43 | `r ≡ 161 (mod 172)` | `47r` | `1/987` |
| 59 | 30 | `r ≡ 61 (mod 120)` | `59r` | `1/472` |
| 67 | 34 | `r ≡ 69 (mod 136)` | `67r` | `1/1072` |

For each row, the target progression is

\[
n\equiv-4d\pmod{sr}.
\]

The fixed `s`-coordinate is a square, while the variable `r`-coordinate is a nonsquare throughout the listed prime progression.

## Counting consequence

If a row has modulus `M` for the prime parameter and target cofactor `s`, its contribution is

\[
\pi\!\left(\frac{4X}{s};M,a\right)
\sim
\frac{4}{s\varphi(M)}\frac{X}{\log X}.
\]

The five rows `s=31,43,47,59,67` contribute together

\[
\frac1{248}+\frac1{430}+\frac1{987}+\frac1{472}+\frac1{1072}
\approx0.0104224906.
\]

Combining the known prime/Jacobi-new backbone coefficient `8/3` with the certified post-Jacobi rows through `s=67` gives the explicit lower bound

\[
\boxed{
N_\infty(X)
\ge
\left(2.8839935228\ldots+o(1)\right)\frac{X}{\log X}.
}
\]

Here `N_\infty(X)` counts depths `A<=X` that occur as exact square-completed Type-II depth for infinitely many primes.

## Interpretation

These rows show that the post-Jacobi mechanism is not an isolated phenomenon. Once the target has a single nonsquare coordinate, the global exact-depth problem reduces to a finite list of variable-prime-bearing ancestors, and each of those ancestors is controlled by a bounded Diophantine equation depending only on fixed integers `(d,c)`.

This does **not** yet prove an infinite hierarchy in the cofactor `s`: the table is finite. The next publishable target is to identify a parametric rule producing infinitely many admissible fixed cofactors `s` and witnesses `d` for which the exceptional-layer equations are uniformly impossible.
