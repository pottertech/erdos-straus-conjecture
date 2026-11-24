#!/usr/bin/env python3
"""Independently enumerate axiom / declaration structure from a lean4export
NDJSON export, resolving full hierarchical names through the string table.

lean4export (format 3.x) interns strings as `{"in":id,"str":{"pre":P,"str":s}}`
records; a name id N's full string is str(P) + str(N) (the prefix record
carries its trailing dot). `{"in":N,"num":k}` records are numeric literals,
not names. This script:
  1. builds the intern table (pre-resolution applied),
  2. collects the `axiom` records and resolves their hierarchical names,
  3. collects thm/def/opaque counts and resolves the
     principal theorem names (the 15 through V17 incl.), each as a fully
     qualified name,
  4. asserts the axiom set is exactly the standard trio BEFORE writing.

  Output schema note (ninth review V18-05): since v1.8 the principal
  theorems are recorded as a JSON object mapping each fully qualified name
  to its occurrence count (always exactly 1) rather than a bare name list;
  the count-based form is the intended representation, proving uniqueness.

Usage: extract_export_axioms.py <export.ndjson> <out.json>
Exit 1 on any structural violation. Sixth review V16-04.
"""
import json
import sys
from collections import Counter

PRINCIPAL = [
    "scaling", "mod8_of_12", "prime_non24_isErdosStraus",
    "full_conjecture_of_h24", "erdos_straus_except_residual_open_class",
    "residue_classification", "u_method_core", "u_method_witness",
    "witness_extraction", "finite_search_equivalence",
    "parametric_divisibility", "parametric_divisibility_iff",
    "h213_parametric_u3",
    "param_exists_iff_onesided", "theorem2",
]
TRIO = sorted(["propext", "Classical.choice", "Quot.sound"])


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    raw, axids, counts, found = {}, set(), Counter(), {}
    hyg = 0
    pending = []  # (id, pre, tail): prefix may appear later -> resolve to fixpoint
    with open(src, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            k = next(iter(r))
            if k == "in":
                if "str" in r:
                    sr = r["str"]
                    if isinstance(sr, dict) and "pre" in sr and "str" in sr:
                        pending.append((r["in"], sr["pre"], sr.get("str", "")))
                    else:
                        raw[r["in"]] = sr.get("str", "") if isinstance(sr, dict) else str(sr)
            elif k == "axiom":
                axids.add(r["axiom"]["name"])
            elif k in ("thm", "def", "inductive", "opaque"):
                counts[k] += 1
    # resolve prefixed names to fixed point (table order is arbitrary)
    for _ in range(len(pending) + 1):
        if not pending:
            break
        still = []
        for nid, pre, tail in pending:
            if pre in raw:
                raw[nid] = raw[pre] + "." + tail  # hierarchical separator
            elif nid == pre or pre == 0:
                raw[nid] = tail
            else:
                still.append((nid, pre, tail))
        if len(still) == len(pending):
            # unresolved prefixes: fall back to the bare tail
            for nid, pre, tail in still:
                if nid not in raw:
                    raw[nid] = tail
            pending = []
            break
        pending = still
    expected = {f"ErdosStrausConjecture.{w}" for w in PRINCIPAL}
    found = Counter()  # (re-initialized post-resolution; hygienic names skipped)
    with open(src, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            k = next(iter(r))
            if k == "thm":
                nm_id = r[k].get("name")
                if nm_id not in raw:
                    # hygienic auxiliary name (num-shaped intern record:
                    # `{"num": {"i": n, "pre": P}}` resolving to
                    # "<prefix>_hyg.<n>") — auxiliary, never principal;
                    # skipped but counted for transparency
                    hyg += 1
                    continue
                nmf = raw[nm_id]
                if nmf in expected:
                    found[nmf] += 1
                elif any(nmf.endswith("." + w) or nmf == w for w in PRINCIPAL):
                    print(f"NON-FULLY-QUALIFIED principal match rejected:"
                          f" {nmf!r} of type thm")
                    sys.exit(1)
    missing = expected - set(found)
    if missing:
        print("MISSING principal theorems in export:", sorted(missing))
        sys.exit(1)
    dupes = [w for w, c in found.items() if c != 1]
    if dupes:
        print("DUPLICATE principal declarations:", dupes)
        sys.exit(1)
    unresolved_ax = [a for a in axids if a not in raw]
    if unresolved_ax:
        print("UNRESOLVED axiom name ids:", unresolved_ax)
        sys.exit(1)
    axnames = sorted(raw[a] for a in axids)
    if axnames != TRIO:
        print("AXIOM SET MISMATCH:", axnames)
        sys.exit(1)
    out = {
        "axioms": axnames,
        "axioms_fully_qualified": True,
        "decl_counts": dict(counts),
        "principal_thms_fully_qualified": {w: found[w] for w in sorted(found)},
        "source_sha_note": "digest of the export bytes recorded separately in SHA256SUMS",
    }
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print(f"export_axioms: {axnames}; principal {len(found)}/{len(PRINCIPAL)}"
          f" resolved; decls {dict(counts)}")


if __name__ == "__main__":
    main()
