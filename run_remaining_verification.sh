#!/bin/bash
# Queue up remaining verification ranges to run sequentially
cd /Users/skippotter/.openclaw/workspace/ErdosStrausConjecture

echo "Starting 200M-500M verification..."
python3 verify_100M_1B_corrected.py 200000001 500000000 300 2>&1

echo "Starting 500M-1B verification..."
python3 verify_100M_1B_corrected.py 500000001 1000000000 300 2>&1

echo "All verification ranges complete."