#!/usr/bin/env python3
"""Verify every SHA-256 recorded in DATA_MANIFEST.md against the repo bytes.

Usage: python3 tests/verify_manifest.py [repo_root]
Exit 0 iff every manifest entry matches. Run before reusing any dataset.
"""
import hashlib
import os
import re
import sys


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    doc = os.path.join(root, "research", "residual_primes", "DATA_MANIFEST.md")
    text = open(doc, encoding="utf-8").read()
    rows = re.findall(r"\| `([^`]+)` \| `([0-9a-f]{64})` \| \d+ \|", text)
    if len(rows) < 19:
        print(f"FAIL: expected 19 manifest rows, parsed {len(rows)}")
        return 1
    bad = 0
    for path, want in rows:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            print(f"MISSING: {path}")
            bad += 1
            continue
        got = hashlib.sha256(open(full, "rb").read()).hexdigest()
        if got != want:
            print(f"HASH MISMATCH: {path}\n  want {want}\n  got  {got}")
            bad += 1
    if bad:
        print(f"MANIFEST VERIFY: FAIL ({bad} bad of {len(rows)})")
        return 1
    print(f"MANIFEST VERIFY: PASS ({len(rows)} digests match)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
