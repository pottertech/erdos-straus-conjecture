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
TRIO_ONLY = [
    "mod8_of_12",
    "prime_non24_isErdosStraus",
    "full_conjecture_of_h24",
    "erdos_straus_except_residual_open_class",
    "residue_classification",
    "u_method_core",
    "u_method_witness",
    "witness_extraction",
    "theorem2",
]
PROPEXT_ONLY = ["scaling"]
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
        short = name.split(".")[-1]
        axioms = {a.strip() for a in m.group(2).split(",") if a.strip()}
        results.setdefault(short, []).append(axioms)

    for short in PROPEXT_ONLY:
        if short not in results:
            errors.append(f"missing audit result for {short}")
        elif len(results[short]) != 1 or results[short][0] != {"propext"}:
            errors.append(f"{short}: unexpected axioms {results[short]}")

    for short in TRIO_ONLY:
        if short not in results:
            errors.append(f"missing audit result for {short}")
        elif len(results[short]) != 1 or results[short][0] != TRIO:
            errors.append(f"{short}: unexpected axioms {results[short]}")

    unexpected = set(results) - set(TRIO_ONLY) - set(PROPEXT_ONLY)
    if unexpected:
        errors.append(f"unexpected audited names: {sorted(unexpected)}")

    if errors:
        print("AXIOM AUDIT GATE: FAIL")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"AXIOM AUDIT GATE: PASS ({len(TRIO_ONLY) + len(PROPEXT_ONLY)} "
          f"principal results, expected axiom sets exact)")


if __name__ == "__main__":
    main()
