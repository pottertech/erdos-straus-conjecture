#!/usr/bin/env python3
"""Verify every SHA-256 recorded in DATA_MANIFEST.md against the repo bytes.

Usage: python3 tests/verify_manifest.py [repo_root]
Exit 0 iff every manifest entry matches. Run before reusing any dataset.

The manifest's artifact tables are the source of truth for the expected
row count: every table row that looks like an artifact entry must parse
as (path, sha256, bytes), and each entry's digest AND byte size are
checked against the committed file, which must also be git-tracked
(that is, part of the checkout this verification runs on, not merely
untracked-but-present on some working tree). A row that fails to parse fails
the run; there is no minimum-count threshold to hide behind.
"""
import hashlib
import os
import re
import sys

ROW_RE = re.compile(r"\| `([^`]+)` \| `([0-9a-f]{64})` \| (\d+) \|")
CANDIDATE_RE = re.compile(r"^\| `[^`]+` \|")


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    doc = os.path.join(root, "research", "residual_primes", "DATA_MANIFEST.md")
    text = open(doc, encoding="utf-8").read()
    rows = []
    bad = 0
    for line in text.splitlines():
        match = ROW_RE.search(line)
        if match:
            rows.append((match.group(1), match.group(2), int(match.group(3))))
        elif CANDIDATE_RE.match(line):
            print(f"UNPARSED MANIFEST ROW: {line.strip()}")
            bad += 1
    if not rows:
        print("FAIL: no manifest rows parsed")
        return 1
    for path, want, want_bytes in rows:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            print(f"MISSING: {path}")
            bad += 1
            continue
        data = open(full, "rb").read()
        if len(data) != want_bytes:
            print(f"SIZE MISMATCH: {path}\n  want {want_bytes}\n  got  {len(data)}")
            bad += 1
            continue
        if os.system(f"git -C {os.getcwd()} ls-files --error-unmatch -- {path} > /dev/null 2>&1") != 0:
            print(f"NOT GIT-TRACKED: {path} (present on disk but untracked)")
            bad += 1
            continue
        got = hashlib.sha256(data).hexdigest()
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
