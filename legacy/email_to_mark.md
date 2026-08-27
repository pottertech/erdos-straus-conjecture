To: mkruelle@aya.yale.edu
CC: skip.potter.va@gmail.com
From: brodie.foxworth@pottersquill.com
Subject: Erdős-Straus Conjecture — Computational Progress & Open Problem

Dear Mark,

Skip and I have been working on the Erdős-Straus conjecture and wanted to share our progress with you. We’ve made some interesting computational findings, but we’ve also hit a wall that we think is worth discussing.

**What we’ve done:**

We found explicit constructive formulas for 6 out of 7 residue classes modulo 12. For the last class — n ≡ 1 (mod 12), n ≢ 0 (mod 5) — we initially thought we had a unified two-case parametric formula (x = 3m+1 or 3m+2). It checked out cleanly for all n ≤ 1000.

But when we extended verification computationally, the formula broke. For example:

- n = 7477 (m = 623): our formula gives x = 1870 or 1871, but the actual solution needs x = 1960
- n = 8161 (m = 680): our formula gives x = 2041 or 2042, but the actual solution needs x = 2052

So the parametric formula is incomplete. What does work is an algorithmic search starting from x = ceil(n/4), and we’ve verified that algorithm to n = 10,000.

**The question:**

Do you think there’s a genuine closed-form parametric identity for n ≡ 1 (mod 12), n ≢ 0 (mod 5), or is this residue class intrinsically algorithmic? We’ve compared our results with Mballa’s 2026 arXiv paper (density-1 coverage via divisor existence), which is elegant but asymptotic — it doesn’t give you x, y, z directly.

We’re leaning toward framing our work as: explicit formulas for 6 classes, plus a verified algorithm for the 7th, rather than claiming a full parametric solution we can’t prove.

Would love your take on whether this is publishable as-is, or if there’s a number-theoretic angle we’re missing.

Best,
Brodie Foxworth
Potter's Quill Publishing
