# Fixed Finite Multi-Shift Sieve for the Untwisted Unit-Partner Branch

**Status:** unconditional theorem for every fixed finite shift set; not a finiteness theorem and not a proof of the Erdős--Straus conjecture

This note gives a complete upper-bound-sieve proof of the fixed-finite-set density statement suggested by `UNIT_PARTNER_HALF_GROUP_LEMMA.md`.

The proof is deliberately arranged as a sieve of the **integers** rather than a sieve inside the primes. This absorbs primality as one additional local residue class and avoids any Bombieri--Vinogradov remainder. The only analytic inputs are the standard Selberg/fundamental upper-bound sieve for a sequence with bounded local density and Mertens' theorem for primes in fixed arithmetic progressions.

The mechanism is closely parallel to Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035 (2026), Lemma 4.2 and Theorem 4.3. Dahan applies Selberg's upper-bound sieve in the form of Halberstam--Richert, *Sieve Methods* (1974), Theorem 3.2. The present argument uses the same fixed-point-free involution but a different fixed-shift family.

## Theorem

Let `U` be a fixed finite set of distinct positive integers satisfying

\[
u\equiv3\pmod4.
\]

Write

\[
P=|U|.
\]

For a prime `n == 1 (mod 4)` and `u in U`, set

\[
K_u(n)=\frac{n+u}{4}.
\]

Let `E_U(N)` be the primes `n <= N` for which every `u in U` fails the untwisted unit-partner condition

\[
\exists d\mid K_u(n):\qquad d\equiv-1\pmod u.
\]

Then

\[
\boxed{
|E_U(N)|\ll_U \frac{N}{(\log N)^{1+P/2}}.
}
\]

The implied constant depends on the fixed shift set `U`.

The same upper bound holds, a fortiori, for primes which fail **both** unit-partner branches at every shift in `U`, and for primes which fail the complete centered binary criterion at every shift in `U`, since either failure set is a subset of the untwisted-failure set.

## 1. Exact local structure

Suppose a fixed shift `u` fails. By `UNIT_PARTNER_HALF_GROUP_LEMMA.md`, if

\[
R_u(n)\subseteq(\mathbb Z/u\mathbb Z)^\times
\]

is the set of residue classes occupied by prime factors of `K_u(n)` that are coprime to `u`, then

\[
|R_u(n)|\le\frac{\varphi(u)}2.
\]

Extend `R_u(n)`, if necessary, to a set

\[
T_u\subseteq(\mathbb Z/u\mathbb Z)^\times,
\qquad |T_u|=\frac{\varphi(u)}2.
\]

There are only finitely many choices for `T_u`, depending on `u` alone. Put

\[
B_u=(\mathbb Z/u\mathbb Z)^\times\setminus T_u.
\]

Then

\[
|B_u|=\frac{\varphi(u)}2.
\]

For a fixed tuple

\[
T=(T_u)_{u\in U},
\]

let `E_T(N)` be the primes whose prime-factor residue sets are contained in these selected `T_u`. The full failure set `E_U(N)` is contained in the union of finitely many `E_T(N)`, so it suffices to prove the required estimate uniformly for each fixed tuple.

## 2. Residue classes removed by a rational prime

Choose a constant `Q0=Q0(U)` larger than

- every member of `U`,
- every absolute difference `|u-v|`, `u != v`,
- and `2P+2`.

Let `q>Q0` be prime.

For every `u in U` such that

\[
q\bmod u\in B_u,
\]

remove the residue class

\[
n\equiv-u\pmod q.
\]

Indeed, if `n == -u (mod q)`, then

\[
q\mid n+u=4K_u(n).
\]

Since `q` is odd,

\[
q\mid K_u(n).
\]

But `q mod u` lies in the forbidden set `B_u`, contradicting the condition defining `E_T(N)`.

Also remove

\[
n\equiv0\pmod q.
\]

This is the ordinary primality sieve class.

For `q>Q0`, all of these removed residue classes are distinct: `0` is different from every `-u`, and if

\[
-u\equiv-v\pmod q,
\]

then `q | u-v`, impossible by the choice of `Q0` unless `u=v`.

Define

\[
\rho_T(q)=\#\{u\in U:q\bmod u\in B_u\}.
\]

Thus the total number of residue classes removed modulo `q` is

\[
\boxed{\omega_T(q)=1+\rho_T(q).}
\]

Since `rho_T(q) <= P` and `q>2P+2`, the sieve is uniformly non-degenerate:

\[
0\le \frac{\omega_T(q)}q<1-c_U
\]

for a positive constant `c_U`.

## 3. Exact mean local density

For each fixed `u`, Mertens' theorem in arithmetic progressions for the fixed modulus `u` gives

\[
\sum_{\substack{q\le z\\ q\bmod u\in B_u}}\frac1q
=
\frac{|B_u|}{\varphi(u)}\log\log z+O_u(1)
=
\frac12\log\log z+O_u(1).
\]

Summing over `u in U`,

\[
\sum_{Q_0<q\le z}\frac{\rho_T(q)}q
=
\frac P2\log\log z+O_U(1).
\]

Adding the primality class,

\[
\boxed{
\sum_{Q_0<q\le z}\frac{\omega_T(q)}q
=
\left(1+\frac P2\right)\log\log z+O_U(1).
}
\]

Because `omega_T(q)` is bounded in terms of `U`, the quadratic correction

\[
\sum_q\frac{\omega_T(q)^2}{q^2}
\]

converges. Hence

\[
\boxed{
V_T(z):=
\prod_{Q_0<q\le z}
\left(1-\frac{\omega_T(q)}q\right)
\asymp_U
(\log z)^{-1-P/2}.
}
\]

Thus the integer sieve has dimension

\[
\boxed{\kappa=1+\frac P2.}
\]

## 4. Selberg upper-bound sieve

Apply the standard Selberg/fundamental upper-bound sieve to the interval

\[
\mathcal A=\{1,2,\ldots,N\}
\]

with the residue sets just defined.

For squarefree `d` composed of sifting primes, the number of integers in `A` lying in the prescribed union of residue classes modulo `d` is

\[
\frac{N\omega_T(d)}d+R_d,
\]

where `omega_T` is multiplicative and the elementary counting error satisfies

\[
|R_d|\le \omega_T(d).
\]

This is exactly the standard bounded-remainder setup of the fundamental lemma of the Selberg sieve. Since `U` is fixed, `omega_T(q)` is uniformly bounded, and the dimension condition in Section 3 holds.

Choose a fixed sieve parameter large enough in terms of `U`, equivalently choose

\[
z=N^{\delta_U}
\]

with sufficiently small fixed `delta_U>0`. The fundamental upper-bound sieve gives

\[
S(\mathcal A,z)
\ll_U
N V_T(z)
\ll_U
\frac{N}{(\log N)^{1+P/2}}.
\]

Every prime `n>z` in `E_T(N)` survives this integer sieve: it is not `0 mod q`, and failure forces it to avoid every shifted forbidden class. The primes `n<=z` contribute only `O(z)`, which is absorbed by the displayed bound after decreasing `delta_U` if necessary.

Therefore

\[
|E_T(N)|
\ll_U
\frac{N}{(\log N)^{1+P/2}}.
\]

Finally sum over the finitely many tuples `T`. Their number depends only on `U`, so the logarithmic exponent is unchanged. This proves the theorem.

## 5. Relation to Dahan 2026

Dahan's Lemma 4.2 proves the same half-group bound for the modulus `4m` using the involution

\[
x\mapsto-x^{-1},
\]

and his Theorem 4.3 obtains

\[
N(\log N)^{-1-|\mathcal P|/2}
\]

for a fixed finite witness system. His proof sieves **inside the primes**, using Halberstam--Richert's Selberg upper-bound theorem and Bombieri--Vinogradov for the prime-sequence remainder.

The proof above instead includes the class `n == 0 (mod q)` and sieves the integer interval. This produces the same extra exponent `1` from primality while leaving only the elementary interval remainder `|R_d| <= omega_T(d)`. Thus Bombieri--Vinogradov is unnecessary for this fixed finite shift result.

References:

- Benjamin Dahan, *Sieve dimension and search depth for the Erdős--Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035 (2026), Lemma 4.2 and Theorem 4.3.
- H. Halberstam and H.-E. Richert, *Sieve Methods*, Academic Press, 1974; standard Selberg upper-bound/fundamental-lemma formulation.
- J. Friedlander and H. Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57, 2010, for standard modern sieve formulations.

## 6. What this theorem does not prove

The theorem is a density estimate. It does **not** imply that `E_U` is finite or empty for any fixed finite set `U`.

A single shift can have an infinite blind set: Dahan proves this unconditionally for `c=7` in his broader fixed-shift criterion. More generally, logarithmic-power decay is fully compatible with an infinite exceptional set.

The significance here is different: the exact unit-partner criterion now has a rigorous, explicit fixed-finite-set sieve exponent, and the verified `u<=299` cascade can be assigned a theorem-level asymptotic bound independently of the finite computation.
