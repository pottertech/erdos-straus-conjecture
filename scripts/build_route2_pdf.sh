#!/usr/bin/env bash
# Build the route-2 conditional-reduction handout PDF.
# Requires: pandoc, a Gotenberg instance on localhost:3000 (chromium engine).
set -euo pipefail
cd "$(dirname "$0")/.."

ROOT2=ROUTE2_CONDITIONAL_REDUCTION.md
OUT=paper/route2_conditional_reduction.pdf
HTML=$(mktemp /tmp/route2_XXXX.html)

pandoc -s --mathml \
  --include-in-header=paper/route2_style.html \
  --metadata title="Route 2 - conditional reduction" \
  "$ROOT2" -o "$HTML"

# Gotenberg chromium conversion (the form requires the file named index.html)
cp "$HTML" "$(mktemp -d /tmp/route2html_XXXX)/index.html"
DIR=$(mktemp -d /tmp/route2html_XXXX)
cp "$HTML" "$DIR/index.html"

curl -sS --fail \
  -o "$OUT" \
  -F "files=@$DIR/index.html" \
  http://localhost:3000/forms/chromium/convert/html

rm -rf "$DIR" "$HTML"
echo "built: $OUT ($(du -h "$OUT" | cut -f1))"
