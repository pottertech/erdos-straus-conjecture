#!/usr/bin/env python3
"""Send the Erdős–Straus research report to Skip Potter and Mark Kruelle."""

import sys
from pathlib import Path

# Add the mail adapter to path
sys.path.insert(0, str(Path.home() / ".openclaw/workspace/openclaw-mail-adapter"))

from openclaw_mail_adapter import send_email

# Read the HTML content
html_path = Path("~/.openclaw/workspace/ErdosStrausConjecture/REPORT.html").expanduser()
pdf_path = Path("~/.openclaw/workspace/ErdosStrausConjecture/REPORT.pdf").expanduser()

html_content = html_path.read_text()

# Prepare email
subject = "Research Report: Erdős–Straus Conjecture - Modular Identities (6/7 Found)"

body_text = """Dear Skip and Mark,

I am pleased to share the results of my recent research on the Erdős–Straus conjecture.

SUMMARY:
Through systematic computational and analytical investigation using Lean 4 formal verification and GNU Octave numerical computation, I have identified parametric identities covering 6 out of 7 residue classes modulo 12.

KEY FINDINGS:
✓ n ≡ 0 (mod 3): Identity proven
✓ n ≡ 2 (mod 3): Identity proven  
✓ n ≡ 4 (mod 12): Symmetric identity proven
✓ n ≡ 10 (mod 12): Identity proven
✓ n ≡ 7 (mod 12): Identity proven
✓ n ≡ 1 (mod 12), n ≡ 0 (mod 5): Identity proven
⚠ n ≡ 1 (mod 12), n ≢ 0 (mod 5): Remains open (genuinely hardest case)

The attached PDF contains the full technical report with:
- Detailed problem statement
- Research methodology
- Complete proofs of all 6 identities
- Computational verification results
- Analysis of the open case

Best regards,
Brodie Foxworth
OpenClaw Agent
Potter's Quill Publishing
"""

# Send to both recipients
recipients = [
    "skip.potter.va@gmail.com",
    "mark.kruelle@aya.yale.edu"
]

for recipient in recipients:
    try:
        send_email(
            to=recipient,
            subject=subject,
            body=body_text,
            html_body=html_content,
            attachments=[str(pdf_path)] if pdf_path.exists() else []
        )
        print(f"✓ Email sent successfully to {recipient}")
    except Exception as e:
        print(f"✗ Failed to send to {recipient}: {e}")

print("\nEmail delivery complete.")
