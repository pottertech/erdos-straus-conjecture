import Mathlib
import ErdosStrausConjecture.Basic

namespace ErdosStrausConjecture

/-- Generic endpoint for the centered one-product relation.
If `n*x = s*k`, `s + 1 = u*r`, and `4*x = n+u`, then the u-method
produces the explicit denominators `x`, `n*x*r`, and `k*r`. -/
theorem short_product_endpoint
    (n x u s k r : Nat)
    (hn : 0 < n) (hx : 0 < x) (hk : 0 < k) (hr : 0 < r)
    (h4 : 4 * x = n + u)
    (hfac : s * k = n * x)
    (hrel : u * r = s + 1) :
    IsErdosStraus n := by
  refine ⟨x, (n * x) * r, k * r, hx, ?_, ?_, ?_⟩
  · exact Nat.mul_pos (Nat.mul_pos hn hx) hr
  · exact Nat.mul_pos hk hr
  · have h4z : (4 * x : ℤ) = n + u := by exact_mod_cast h4
    have hfz : (s * k : ℤ) = n * x := by exact_mod_cast hfac
    have hrz : (u * r : ℤ) = s + 1 := by exact_mod_cast hrel
    have hz :
        (4 * x * ((n * x) * r) * (k * r) : ℤ) =
        n * (x * ((n * x) * r) + x * (k * r) + ((n * x) * r) * (k * r)) := by
      push_cast
      linear_combination
        (n * r * x * k * r) * h4z +
        (n * r * x * k) * hrz +
        (n * r * x) * hfz
    exact_mod_cast hz

/-- Complete centered binary endpoint.
If `A*B*C = n*K`, `A+B = u*r`, and `4*K=n+u`, then
`K`, `A*C*r`, and `B*C*r` form an Erdős--Straus decomposition.
No primality assumption on `A` or `B` is required. -/
theorem centered_binary_endpoint
    (n K u A B C r : Nat)
    (hn : 0 < n) (hK : 0 < K) (hA : 0 < A) (hB : 0 < B)
    (hC : 0 < C) (hr : 0 < r)
    (h4 : 4 * K = n + u)
    (hfac : (A * B) * C = n * K)
    (hsum : u * r = A + B) :
    IsErdosStraus n := by
  refine ⟨K, A * C * r, B * C * r, hK, ?_, ?_, ?_⟩
  · positivity
  · positivity
  · have h4z : (4 * K : ℤ) = n + u := by exact_mod_cast h4
    have hfz : ((A * B) * C : ℤ) = n * K := by exact_mod_cast hfac
    have hsz : (u * r : ℤ) = A + B := by exact_mod_cast hsum
    have hz :
        (4 * K * (A * C * r) * (B * C * r) : ℤ) =
        n * (K * (A * C * r) + K * (B * C * r) + (A * C * r) * (B * C * r)) := by
      push_cast
      linear_combination
        (C * r * r * (4 * K - n)) * hfz +
        (n * C * r * r * K) * h4z -
        (n * C * r * K) * hsz
    exact_mod_cast hz

/-- Untwisted unit-partner endpoint from the complete fixed-shift binary criterion.
If `K = d*q` and `d + 1 = c*r`, then the divisor pair `(d,1)` is a
unit-partner certificate at shift `c`. -/
theorem unit_partner_untwisted
    (n K c d q r : Nat)
    (hn : 0 < n) (hK : 0 < K) (hq : 0 < q) (hr : 0 < r)
    (h4 : 4 * K = n + c)
    (hKfac : d * q = K)
    (hrel : c * r = d + 1) :
    IsErdosStraus n := by
  have hk : 0 < n * q := Nat.mul_pos hn hq
  have hfac : d * (n * q) = n * K := by
    rw [← hKfac]
    ring
  exact short_product_endpoint n K c d (n * q) r hn hK hk hr h4 hfac hrel

/-- Twisted unit-partner endpoint from the complete fixed-shift binary criterion.
If `K = d*q` and `n*d + 1 = c*r`, then the divisor pair `(n*d,1)` is a
unit-partner certificate at shift `c`. -/
theorem unit_partner_twisted
    (n K c d q r : Nat)
    (hn : 0 < n) (hK : 0 < K) (hq : 0 < q) (hr : 0 < r)
    (h4 : 4 * K = n + c)
    (hKfac : d * q = K)
    (hrel : c * r = n * d + 1) :
    IsErdosStraus n := by
  have hfac : (n * d) * q = n * K := by
    rw [← hKfac]
    ring
  exact short_product_endpoint n K c (n * d) q r hn hK hq hr h4 hfac hrel

/-- One-factor endpoint: a factor `p | n*x` with `p ≡ -1 (mod u)`. -/
theorem short_relation_p_neg_one
    (n x u p k r : Nat)
    (hn : 0 < n) (hx : 0 < x) (hk : 0 < k) (hr : 0 < r)
    (h4 : 4 * x = n + u)
    (hfac : p * k = n * x)
    (hrel : u * r = p + 1) :
    IsErdosStraus n :=
  short_product_endpoint n x u p k r hn hx hk hr h4 hfac hrel

/-- Cubic one-factor endpoint: `p^3 | n*x` and `p^3 ≡ -1 (mod u)`. -/
theorem short_relation_p_cubed_neg_one
    (n x u p k r : Nat)
    (hn : 0 < n) (hx : 0 < x) (hk : 0 < k) (hr : 0 < r)
    (h4 : 4 * x = n + u)
    (hfac : p^3 * k = n * x)
    (hrel : u * r = p^3 + 1) :
    IsErdosStraus n :=
  short_product_endpoint n x u (p^3) k r hn hx hk hr h4 hfac hrel

/-- Two-factor product endpoint: `p*q | n*x` and `p*q ≡ -1 (mod u)`. -/
theorem short_relation_pq_neg_one
    (n x u p q k r : Nat)
    (hn : 0 < n) (hx : 0 < x) (hk : 0 < k) (hr : 0 < r)
    (h4 : 4 * x = n + u)
    (hfac : (p * q) * k = n * x)
    (hrel : u * r = p * q + 1) :
    IsErdosStraus n :=
  short_product_endpoint n x u (p*q) k r hn hx hk hr h4 hfac hrel

/-- Two-factor opposite-residue endpoint.
If `n*x = p*q*k` and `p+q = u*r`, the centered ratio `p/q` is `-1 mod u`.
The explicit denominators are `x`, `p*k*r`, and `q*k*r`. -/
theorem short_relation_p_neg_q
    (n x u p q k r : Nat)
    (hn : 0 < n) (hx : 0 < x) (hp : 0 < p) (hq : 0 < q)
    (hk : 0 < k) (hr : 0 < r)
    (h4 : 4 * x = n + u)
    (hfac : (p * q) * k = n * x)
    (hrel : u * r = p + q) :
    IsErdosStraus n := by
  refine ⟨x, p * k * r, q * k * r, hx, ?_, ?_, ?_⟩
  · positivity
  · positivity
  · have h4z : (4 * x : ℤ) = n + u := by exact_mod_cast h4
    have hfz : ((p * q) * k : ℤ) = n * x := by exact_mod_cast hfac
    have hrz : (u * r : ℤ) = p + q := by exact_mod_cast hrel
    have hz :
        (4 * x * (p * k * r) * (q * k * r) : ℤ) =
        n * (x * (p * k * r) + x * (q * k * r) + (p * k * r) * (q * k * r)) := by
      push_cast
      linear_combination
        (k * r * k * p * q * r) * h4z +
        (k * r * r * u) * hfz +
        (k * r * n * x) * hrz
    exact_mod_cast hz

end ErdosStrausConjecture
