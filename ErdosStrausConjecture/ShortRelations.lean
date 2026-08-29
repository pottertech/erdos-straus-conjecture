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
