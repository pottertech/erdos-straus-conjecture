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
  · calc
      4 * K * (A * C * r) * (B * C * r)
          = 4 * K * (A * B * C) * C * r^2 := by ring
      _ = 4 * K * (n * K) * C * r^2 := by rw [hfac]
      _ = n * K * C * r^2 * (n + u) := by rw [← h4]; ring
      _ = n * (K * C * r * (A + B) + (A * B * C) * C * r^2) := by
            rw [← hsum, hfac]
            ring
      _ = n * (K * (A * C * r) + K * (B * C * r) + (A * C * r) * (B * C * r)) := by ring

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
