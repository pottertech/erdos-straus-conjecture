#!/bin/bash
# Chain 500M-1B after 200M-500M completes
cd /Users/skippotter/.openclaw/workspace/ErdosStrausConjecture

echo "Waiting for 200M-500M to complete..."
while pgrep -f "verify_100M_1B_corrected.py 200000001" > /dev/null 2>&1; do
    sleep 60
done

echo "Starting 500M-1B verification..."
python3 verify_100M_1B_corrected.py 500000001 1000000000 300 2>&1

echo "All verification complete."