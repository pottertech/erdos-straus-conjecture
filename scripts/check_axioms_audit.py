#!/usr/bin/env python3
"""Gate for the Lean proof-term axiom audit (print_axioms.lean output).

Per fourth external review V13-03: the audit is a CI regression gate, not a
manual report. Fails (exit 1) unless EVERY principal theorem named below
appears exactly once with the expected axiom set; any `sorryAx`, project
axiom, or unexpected dependency anywhere in the output is also a failure.

Expected sets (as recorded in Appendix A of the route-2 paper):
  scaling          -> {propext}                       (no classical.choice)
  all others       -> {propext, Classical.choice, Quot.sound}
"""
import re
import sys

TRIO = {"propext", "Classical.choice", "Quot.sound"}
NS = "ErdosStrausConjecture."
TRIO_ONLY = [
    "ErdosStrausConjecture.mod8_of_12",
    "ErdosStrausConjecture.prime_non24_isErdosStraus",
    "ErdosStrausConjecture.full_conjecture_of_h24",
    "ErdosStrausConjecture.erdos_straus_except_residual_open_class",
    "ErdosStrausConjecture.residue_classification",
    "ErdosStrausConjecture.u_method_core",
    "ErdosStrausConjecture.u_method_witness",
    "ErdosStrausConjecture.witness_extraction",
    "ErdosStrausConjecture.finite_search_equivalence",
    "ErdosStrausConjecture.parametric_divisibility",
    "ErdosStrausConjecture.parametric_divisibility_iff",
    "ErdosStrausConjecture.theorem2",
]
PROPEXT_ONLY = ["ErdosStrausConjecture.scaling"]
QUOT_ONLY = ["ErdosStrausConjecture.param_exists_iff_onesided"]
FORBIDDEN_SUBSTRINGS = ["sorryAx", "erdos_straus_mod_12_1_not_div_5_conjecture",
                        "divisor_residue_criterion_reverse"]


def main() -> None:
    text = sys.stdin.read()
    errors = []

    for bad in FORBIDDEN_SUBSTRINGS:
        if bad in text:
            errors.append(f"forbidden dependency in audit output: {bad}")

    results = {}
    # Lean wraps long `#print axioms` lines; re-join until the bracket closes
    joined, buf = [], None
    for line in text.splitlines():
        buf = line if buf is None else buf + " " + line.strip()
        if "depends on axioms" in buf and "]" in buf:
            joined.append(buf)
            buf = None
    if buf:
        joined.append(buf)

    for line in joined:
        line = line.strip()
        if "depends on axioms" not in line:
            continue
        m = re.match(r"'(.+?)' depends on axioms: \[(.*)\]", line)
        if not m:
            errors.append(f"unparseable audit line: {line!r}")
            continue
        name = m.group(1)
        axioms = {a.strip() for a in m.group(2).split(",") if a.strip()}
        results.setdefault(name, []).append(axioms)

    for fname in PROPEXT_ONLY:
        if fname not in results:
            errors.append(f"missing audit result for {fname}")
        elif len(results[fname]) != 1 or results[fname][0] != {"propext"}:
            errors.append(f"{fname}: unexpected axioms {results[fname]}")

    for fname in TRIO_ONLY:
        if fname not in results:
            errors.append(f"missing audit result for {fname}")
        elif len(results[fname]) != 1 or results[fname][0] != TRIO:
            errors.append(f"{fname}: unexpected axioms {results[fname]}")

    QUOT = {"propext", "Quot.sound"}
    for fname in QUOT_ONLY:
        if fname not in results:
            errors.append(f"missing audit result for {fname}")
        elif len(results[fname]) != 1 or results[fname][0] != QUOT:
            errors.append(f"{fname}: unexpected axioms {results[fname]}")

    unexpected = (set(results) - set(TRIO_ONLY) - set(PROPEXT_ONLY)
                  - set(QUOT_ONLY))
    if unexpected:
        errors.append(f"unexpected audited names: {sorted(unexpected)}")

    if errors:
        print("AXIOM AUDIT GATE: FAIL")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"AXIOM AUDIT GATE: PASS ({len(TRIO_ONLY) + len(PROPEXT_ONLY) + len(QUOT_ONLY)} "
          "principal "
          "results, fully-qualified names, expected axiom sets exact)")


if __name__ == "__main__":
    main()
