import Mathlib

namespace ErdosStrausBinaryEndpoint

def IsErdosStraus (n : Nat) : Prop :=
  ∃ (x y z : Nat), x > 0 ∧ y > 0 ∧ z > 0 ∧
    4 * x * y * z = n * (x * y + x * z + y * z)

/-- Complete centered binary endpoint.
If `A*B*C = n*K`, `A+B = u*r`, and `4*K = n+u`, then
`X=K`, `Y=A*C*r`, `Z=B*C*r` give an Erdős--Straus decomposition. -/
theorem full_binary_endpoint
    (n K u A B C r : Nat)
    (hn : 0 < n) (hK : 0 < K)
    (hA : 0 < A) (hB : 0 < B) (hC : 0 < C) (hr : 0 < r)
    (h4 : 4 * K = n + u)
    (hfac : A * B * C = n * K)
    (hsum : u * r = A + B) :
    IsErdosStraus n := by
  refine ⟨K, A * C * r, B * C * r, hK, ?_, ?_, ?_⟩
  · positivity
  · positivity
  · have h4z : (4 * K : ℤ) = n + u := by exact_mod_cast h4
    have hfz : (A * B * C : ℤ) = n * K := by exact_mod_cast hfac
    have hsz : (u * r : ℤ) = A + B := by exact_mod_cast hsum
    have hz :
        (4 * K * (A * C * r) * (B * C * r) : ℤ) =
        n * (K * (A * C * r) + K * (B * C * r) + (A * C * r) * (B * C * r)) := by
      push_cast
      calc
        4 * K * (A * C * r) * (B * C * r)
            = 4 * n * K^2 * C * r^2 := by rw [hfz]; ring
        _ = n * K * C * r^2 * (n + u) := by rw [← h4z]; ring
        _ = n * (K * C * r * (A + B) + A * B * C^2 * r^2) := by
              rw [← hsz, hfz]
              ring
        _ = n * (K * (A * C * r) + K * (B * C * r) + (A * C * r) * (B * C * r)) := by ring
    exact_mod_cast hz

/-- The exceptional certificate for n=2521 closes through the full binary endpoint. -/
theorem erdos_straus_2521 : IsErdosStraus 2521 := by
  apply full_binary_endpoint 2521 638 31 2 29 27731 1
  · norm_num
  · norm_num
  · norm_num
  · norm_num
  · norm_num
  · norm_num
  · norm_num
  · norm_num
  · norm_num

end ErdosStrausBinaryEndpoint
