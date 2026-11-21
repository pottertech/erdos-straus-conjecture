import ErdosStrausConjecture.Reduction
import ErdosStrausConjecture.CenteredCriterion
import ErdosStrausConjecture.MainTheorem

/-!
# Axiom dependency audit for the route-2 conditional reduction

Run with:  lake env lean scripts/print_axioms.lean

Expected for every principal result: only `propext`, `Classical.choice`,
`Quot.sound` (the logical baseline of Lean/Mathlib) — and in particular
none of the two documented project axioms
(`ErdosStrausConjecture.erdos_straus_mod_12_1_not_div_5_conjecture`,
`ErdosStrausConjecture.divisor_residue_criterion_reverse`) and no `sorryAx`.

A successful build and a zero-`sorry` census do not establish this by
themselves; `#print axioms` does, because it inspects the full transitive
dependency closure of each proof term.
-/

#print axioms ErdosStrausConjecture.scaling
#print axioms ErdosStrausConjecture.mod8_of_12
#print axioms ErdosStrausConjecture.prime_non24_isErdosStraus
#print axioms ErdosStrausConjecture.full_conjecture_of_h24
#print axioms ErdosStrausConjecture.erdos_straus_except_residual_open_class
#print axioms ErdosStrausConjecture.residue_classification
#print axioms ErdosStrausConjecture.u_method_core
#print axioms ErdosStrausConjecture.u_method_witness
#print axioms ErdosStrausConjecture.theorem2
