# Global First-Hit Geometry Beyond Divisor-Modulus Ancestry

**Status:** exact conceptual distinction plus finite prime sampling. Not a global coverage theorem.

A realized primitive class at depth `A` is a class

\[
r\in P_A^{\rm real}
\]

represented by some divisor

\[
D\mid A^2
\]

which is not inherited from any smaller depth whose modulus divides

\[
m_A=4A-1.
\]

It generates the genuine Type-II progression

\[
\boxed{n\equiv-4D\pmod{m_A}.}
\]

However, divisor-modulus primitivity is **not** global first-hit primitivity. An unrelated earlier depth `B<A` with

\[
4B-1\nmid4A-1
\]

can still solve infinitely many or even most primes in this progression through CRT intersections.

## Regression example: A = 22339

Take

\[
A=22339=89\cdot251,
\qquad
m_A=89355=3\cdot5\cdot7\cdot23\cdot37.
\]

The realized primitive classes modulo `89355` are

\[
89,\ 251,\ 22361,\ 67079.
\]

Using representatives `D|A^2`, the corresponding Type-II progressions have smallest sampled primes:

| realized class | progression residue `-4D mod m_A` | first sampled prime | actual minimum Type-II depth |
|---:|---:|---:|---:|
| 89 | 88999 | 625129 | 3 |
| 251 | 88351 | 445771 | 3 |
| 22361 | 89266 | 178621 | 8 |
| 67079 | 89104 | 357169 | 3 |

Thus all four are immediately rescued by much smaller depths whose moduli are unrelated to the divisor-modulus ancestry chain.

## 100-prime sample in each primitive progression

For each of the four progressions above, the first 100 primes were tested against every square-completed Type-II layer through depth `1000`.

Results:

- all 400 sampled primes were solved by depth `<=105`;
- none required a depth anywhere near `22339`;
- the dominant first-hit depths were `3`, `5`, `8`, `10`, `12`, and nearby small layers.

Maximum first-hit depth observed in each 100-prime sample:

| realized class | maximum sampled minimum depth |
|---:|---:|
| 89 | 66 |
| 251 | 40 |
| 22361 | 105 |
| 67079 | 77 |

These are finite samples only, but they demonstrate the scale of the cross-modulus collapse.

## Correct hierarchy of residue notions

Three levels must be kept separate.

### 1. Realized layer

\[
R_A=\{D\bmod(4A-1):D\mid A^2\}.
\]

These are actual Type-II trap classes.

### 2. Divisor-modulus primitive layer

\[
P_A^{\rm real}
\]

removes classes inherited from earlier moduli dividing `4A-1`.

### 3. Global first-hit layer

A globally new depth-`A` contribution must survive **all** earlier depths, including those with non-dividing moduli.

This is a covering-system problem on the parameter of the progression rather than a simple divisor-lattice problem.

## Exact CRT formulation

Fix a depth-`A` progression

\[
n=a+m_A k,
\qquad
 a\equiv-4D\pmod{m_A}.
\]

An earlier Type-II trap at depth `B` has a residue

\[
n\equiv t\pmod{m_B},
\qquad
m_B=4B-1.
\]

Let

\[
g=\gcd(m_A,m_B).
\]

The two progressions intersect iff

\[
a\equiv t\pmod g.
\]

When they intersect, the earlier trap removes exactly one residue class of the parameter `k` modulo

\[
\boxed{m_B/g.}
\]

Therefore global first-hit analysis reduces exactly to a covering problem for `k` by residue classes whose moduli are the reduced quantities

\[
\frac{4B-1}{\gcd(4A-1,4B-1)}.
\]

This is the correct finite-state object.

## Why this is promising

The first realized high-omega example shows that divisor ancestry can leave genuine Type-II classes even when `4A-1` is highly composite. Yet the corresponding prime progressions appear to be demolished almost immediately by small unrelated depths.

That suggests a new structural target:

> Primitive divisor-lattice classes may be abundant, while genuinely new **global first-hit** classes may be extremely sparse because cross-modulus CRT intersections accumulate rapidly.

If that can be turned into an exact covering theorem for a suitable growing set of early depths, it would be much closer to explaining the observed universal Type-II computation.

## Next theorem target

For a fixed realized primitive progression at depth `A`, construct the exact parameter-space covering system produced by all earlier depths `B<A`.

The strongest useful outcome would be either:

1. prove the parameter integers are completely covered, so the depth-`A` progression contributes no globally new integers;
2. isolate finitely many uncovered parameter progressions and determine whether any contain primes;
3. prove that every uncovered progression is forced into another exact Type-II family.

The script `global_first_hit_progression_probe.py` provides finite prime sampling. A separate exact CRT-cover solver should be the next implementation.

## Claim boundary

The sample above does not prove that the four `A=22339` progressions are globally covered by earlier depths. It proves only that their first sampled primes are overwhelmingly rescued early. The exact CRT covering problem remains open and is the next computational/theoretical target.