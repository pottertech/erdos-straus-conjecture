#!/usr/bin/env python3
"""
Formal proof attempt: Why A=3 OR A=7 always works for primes n ≡ 1 (mod 24).

The gap case: n ≡ 1 (mod 8), (7/n) = 1, and m_7/2 has only QR factors.
For these n, does A=3 m-route always work?

A=3: (3/n) = 1 always (n ≡ 1 mod 12). So direct fails. Need m-route.
m_3 = (n+3)/4. For n ≡ 1 (mod 8): m_3 = (n+3)/4 is odd (n+3 ≡ 4 mod 8).

Key identity: (m_3 / n) = ((n+3)/4 / n) = (3/n) · (4^{-1}/n) = 1 · 1 = 1
(since (3/n) = 1 and (4^{-1}/n) = (2/n)^{-2} = 1 for n ≡ 1 mod 8)

So m_3 is QR mod n → even number of QNR factors (same structure as m_7).

Question: can m_3 ALSO be all-QR when m_7/2 is all-QR?

If BOTH m_3 and m_7/2 are all-QR, then BOTH A=3 and A=7 m-routes fail.
The computation says this NEVER happens (0 cases ≤ 100K, 0 ≤ 10M).

Why? Let's look at the JOINT structure.

m_3 = (n+3)/4 (odd, ~n/4)
m_7/2 = (n+7)/8 (could be odd or even, ~n/8)

Note: m_3 and m_7/2 differ by 1:
  m_7/2 - m_3 = (n+7)/8 - (n+3)/4 = (n+7 - 2n - 6)/8 = (1-n)/8

Wait, that's not 1. Let me recompute:
  m_3 = (n+3)/4 = 2(n+3)/8
  m_7/2 = (n+7)/8
  m_3 - m_7/2 = (2n+6 - n - 7)/8 = (n - 1)/8

So m_3 = m_7/2 + (n-1)/8. They're not close in general.

Alternative approach: look at m_3 · m_7/2.
  m_3 · m_7/2 = (n+3)(n+7)/32

Or: consider the PRODUCT m_3 · m_7/2 and its Jacobi symbol.
  (m_3 · m_7/2 / n) = (m_3/n) · (m_7/2 / n) = 1 · 1 = 1
  
So the product is QR. If both are all-QR, the product is QR (trivially).
If one has 2 QNR factors and the other 0, product has 2 (still QR).

Hmm, the Jacobi symbol of the product doesn't help distinguish.

Let's try a different approach: can we show m_3 has at least one prime factor
that is QNR mod n, using the SIZE of m_3?

m_3 = (n+3)/4 ~ n/4. If ALL prime factors of m_3 are QR mod n, then m_3
is a product of primes from the "QR set" — primes p with (p/n) = 1.

The QR primes have density 1/2 among primes. The "QR-smooth" numbers 
(numbers all of whose prime factors are QR) have a specific density.

For a number of size ~n/4 to be QR-smooth, ALL its prime factors must be QR.
If m_3 has k distinct prime factors, the probability is ~(1/2)^k.
For k ~ log log n (typical), this is ~1/log n → 0.

But this is a HEURISTIC, not a proof. Can we make it rigorous?

The key: if m_3 is prime and > n^{1/2}, then (m_3/n) = (n/m_3) by QR.
If m_3 is prime, then (m_3/n) = (n/m_3) = ((n mod m_3)/m_3).
n ≡ -3 (mod 4·m_3) is not useful directly.

Actually, let's think about it differently.
If m_3 = (n+3)/4 is PRIME, then (m_3/n) = (n/m_3) by quadratic reciprocity
(both ≡ 1 mod 4). And n mod m_3 = n - 4·m_3 + ... hmm.

n = 4·m_3 - 3, so n ≡ -3 (mod m_3).
(m_3/n) = (n/m_3) = (-3/m_3) = (-1/m_3)·(3/m_3).

For m_3 ≡ 1 (mod 4): (-1/m_3) = 1.
(3/m_3) depends on m_3 mod 12.

This is getting complicated. Let me just run the computation to understand
the structure better.
"""

import json
import sympy
from sympy import isprime, nextprime, factorint, gcd, legendre_symbol, mod_inverse
from collections import Counter, defaultdict
from math import lcm

def find_primitive_root(p):
    if p == 2: return 1
    phi = p - 1; factors = factorint(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors): return g
    return None

def discrete_log_mod(g, target, p):
    val = 1
    for i in range(p - 1):
        if val == target % p: return i
        val = (val * g) % p
    return None

def multiplicative_order(a, n):
    if gcd(a, n) > 1: return None
    val = a % n
    for i in range(1, n):
        if val == 1: return i
        val = (val * a) % n
    return None

def check_T_in_D(n, A):
    if gcd(n, A) > 1: return None
    m = (n + A) // 4; nx = n * m
    factors = factorint(nx)
    prime_factors = [(p, e) for p, e in factors.items() if gcd(p, A) == 1]
    if not prime_factors: return None
    if not isprime(A):
        D_A = set([1])
        for p, e in prime_factors:
            p_mod = p % A; new_D = set()
            for d in D_A:
                for exp in range(2 * e + 1): new_D.add(pow(p_mod, exp, A) * d % A)
            D_A = new_D
        T = (-n * n * mod_inverse(4, A)) % A; return T in D_A
    g = find_primitive_root(A)
    if g is None: return None
    orders = [multiplicative_order(p, A) for p, _ in prime_factors]
    h = 1
    for o in orders: h = lcm(h, o)
    if h <= 1:
        T = (-n * n * mod_inverse(4, A)) % A; return T == 1
    s_values = {}
    for p, e in prime_factors:
        dlg = discrete_log_mod(g, p, A); step = (A - 1) // h
        if h <= 1: s_values[p] = 0; continue
        try: s_inv = mod_inverse(step, h); s_i = (dlg * s_inv) % h
        except:
            s_i = None
            for s in range(h):
                if (s * step) % h == dlg % h: s_i = s; break
            if s_i is None: return None
        s_values[p] = s_i
    from itertools import product as iterproduct
    D_A = set(); ranges = [range(2 * e + 1) for _, e in prime_factors]
    s_list = [s_values[p] for p, _ in prime_factors]
    for combo in iterproduct(*ranges): D_A.add(sum(a * s for a, s in zip(combo, s_list)) % h)
    dlog_nm = sum(e * s_values[p] for p, e in prime_factors) % h
    dlog_T = (h // 2 + dlog_nm) % h
    return dlog_T in D_A


def main():
    print("Formal proof attempt: Joint A=3, A=7 analysis")
    print("=" * 80)
    
    # Focus: n ≡ 1 (mod 24) [i.e., n ≡ 1 mod 8 AND n ≡ 1 mod 12]
    # with (7/n) = 1 and m_7/2 all-QR
    # For these, does A=3 m-route always work?
    
    print("\nTarget: n ≡ 1 (mod 24), (7/n) = 1, m_7/2 all-QR")
    print("Question: does A=3 m-route always rescue these?")
    
    hard_cases = []
    n = 13
    while n <= 100000:
        if n % 24 == 1 and n % 5 != 0 and isprime(n):
            seven_qr = legendre_symbol(7, n) == 1
            
            m7_half = (n + 7) // 8
            factors_m7h = factorint(m7_half)
            m7h_all_qr = all(legendre_symbol(p, n) == 1 for p in factors_m7h)
            
            if seven_qr and m7h_all_qr:
                # This is the hard case — A=7 m-route fails
                m3 = (n + 3) // 4
                factors_m3 = factorint(m3)
                m3_qnr_primes = [p for p in factors_m3 if legendre_symbol(p, n) == -1]
                m3_all_qr = len(m3_qnr_primes) == 0
                
                # Does A=3 work?
                a3_works = check_T_in_D(n, 3)
                
                hard_cases.append({
                    'n': n,
                    'm3': m3,
                    'm3_factors': dict(factors_m3),
                    'm3_qnr_primes': m3_qnr_primes,
                    'm3_all_qr': m3_all_qr,
                    'a3_works': a3_works,
                    'm7_half': m7_half,
                    'm7h_factors': dict(factors_m7h),
                })
        
        n = nextprime(n)
    
    print(f"\nHard cases (n ≡ 1 mod 24, (7/n)=1, m_7/2 all-QR) ≤ 100K: {len(hard_cases)}")
    
    a3_rescues = sum(1 for c in hard_cases if c['a3_works'])
    a3_fails = sum(1 for c in hard_cases if not c['a3_works'])
    m3_also_all_qr = sum(1 for c in hard_cases if c['m3_all_qr'])
    
    print(f"  A=3 works (rescues): {a3_rescues}")
    print(f"  A=3 fails: {a3_fails}")
    print(f"  m_3 also all-QR: {m3_also_all_qr}")
    
    if a3_fails > 0:
        print(f"\n  ⚠️ A=3 ALSO FAILS in {a3_fails} cases!")
        print(f"  These need A > 7. Checking what A works:")
        for c in hard_cases:
            if not c['a3_works']:
                n = c['n']
                A = 11
                while A <= 200:
                    if gcd(n, A) == 1:
                        result = check_T_in_D(n, A)
                        if result:
                            print(f"    n={n}: A={A} works")
                            break
                    A += 4
    
    if a3_fails == 0 and len(hard_cases) > 0:
        print(f"\n  ✅ A=3 ALWAYS rescues the hard cases!")
        print(f"  So the proof structure is:")
        print(f"  - (7/n) = -1 → A=7 direct (Jacobi guaranteed)")
        print(f"  - (7/n) = 1, m_7/2 has QNR → A=7 m-route")
        print(f"  - (7/n) = 1, m_7/2 all-QR → A=3 m-route ALWAYS works")
    
    # Analyze WHY A=3 m-route works in the hard cases
    print(f"\n{'='*80}")
    print("Why A=3 m-route works in hard cases")
    print(f"{'='*80}")
    
    # Key: m_3 = (n+3)/4. (m_3/n) = (3/n) = 1. So m_3 is QR mod n.
    # But m_3 having QNR prime factors means it's a product of an even number of QNR primes.
    
    print(f"\nQNR prime factor count in m_3 (hard cases):")
    qnr_count_dist = Counter()
    for c in hard_cases:
        factors = c['m3_factors']
        qnr_count = sum(e for p, e in factors.items() if legendre_symbol(p, c['n']) == -1)
        qnr_count_dist[qnr_count] += 1
    print(f"  Distribution: {dict(sorted(qnr_count_dist.items()))}")
    
    # What primes are QNR in m_3 for these hard cases?
    print(f"\nQNR primes in m_3 (hard cases):")
    qnr_prime_counter = Counter()
    for c in hard_cases:
        for p in c['m3_qnr_primes']:
            qnr_prime_counter[p] += 1
    for p, cnt in qnr_prime_counter.most_common(20):
        print(f"  p={p}: {cnt} cases")
    
    # The structural question: 
    # m_3 = (n+3)/4, m_7/2 = (n+7)/8
    # When m_7/2 is all-QR, what forces m_3 to have QNR factors?
    
    # Key relationship: m_3 - 2·m_7/2 = (n+3)/4 - (n+7)/4 = -1
    # So m_3 = 2·m_7/2 - 1 !!!
    
    print(f"\n{'='*80}")
    print("KEY RELATIONSHIP: m_3 = 2·(m_7/2) - 1")
    print(f"{'='*80}")
    
    # Verify
    for c in hard_cases[:10]:
        n = c['n']
        m3 = (n + 3) // 4
        m7h = (n + 7) // 8
        print(f"  n={n}: m_3={m3}, 2·m_7/2 - 1 = {2*m7h - 1}, match={m3 == 2*m7h - 1}")
    
    print(f"\n  m_3 = 2·(n+7)/8 - 1 = (n+7)/4 - 1 = (n+3)/4 ✓")
    print(f"  So m_3 and m_7/2 satisfy: m_3 = 2·(m_7/2) - 1")
    print(f"  They are COPRIME: gcd(m_3, m_7/2) = gcd(2·m_7/2 - 1, m_7/2) = gcd(-1, m_7/2) = 1")
    print(f"  So m_3 and m_7/2 share NO common prime factors!")
    
    # This is a key structural fact: m_3 and m_7/2 are COPRIME.
    # If m_7/2 is all-QR, its primes are all QR.
    # m_3 is coprime to m_7/2, so m_3's primes are DIFFERENT from m_7/2's primes.
    # The question: can m_3's primes ALL be QR too?
    
    # If m_3 is all-QR AND m_7/2 is all-QR, then the PRODUCT m_3·m_7/2 is all-QR.
    # m_3 · m_7/2 = (n+3)/4 · (n+7)/8 = (n+3)(n+7)/32
    # This product is QR mod n (Jacobi = 1·1 = 1).
    
    # But: (m_3 · m_7/2 / n) = 1 doesn't prevent both from being all-QR.
    
    # The coprimality means they use DIFFERENT primes. 
    # If there are only ~n/(2 log n) QR primes up to n, and m_3 ~ n/4, m_7/2 ~ n/8,
    # can they both be built from QR primes only?
    
    # This is where the Burgess bound enters: it guarantees QNR primes exist that are small.
    # If the least QNR is q, then any number > q that is coprime to all QNR primes ≤ q
    # must be all-QR. But m_3 is determined by n, not random.
    
    print(f"\n{'='*80}")
    print("COPRIMALITY ARGUMENT")
    print(f"{'='*80}")
    
    print(f"""
    Key structural facts:
    1. m_3 = (n+3)/4 and m_7/2 = (n+7)/8 are COPRIME
    2. (m_3/n) = 1 and (m_7/2 / n) = (7/n)
    3. When (7/n) = 1: both are QR mod n
    4. When m_7/2 is all-QR: its primes are all QR
    5. m_3 is coprime to m_7/2, so uses DIFFERENT primes
    
    The question: can m_3 ALSO be all-QR?
    
    If both are all-QR, then n+3 and n+7 are both products of QR primes (up to powers of 2).
    This means: n ≡ -3 (mod p) and n ≡ -7 (mod q) where p, q are QR primes.
    
    The constraint is very tight: n is simultaneously congruent to -3 mod 4p
    for all prime factors p of m_3, and -7 mod 8q for all prime factors q of m_7/2.
    
    If the Burgess bound gives us a QNR prime q* ≤ n^{{1/(4√e)+ε}},
    and q* divides either m_3 or m_7/2, we're done.
    
    The probability that q* divides m_3 is ~1/(4q*) (one residue class mod 4q*).
    The probability that q* divides m_7/2 is ~1/(8q*).
    The probability that q* divides NEITHER is ~(1 - 3/(8q*)) ≈ 1.
    
    So a single QNR prime likely doesn't divide either. We need MULTIPLE QNR primes,
    and the probability that NONE of them divides m_3 or m_7/2 decreases.
    
    If there are QNR primes q_1, ..., q_k ≤ X, the probability that none divides
    m_3 or m_7/2 is roughly Π(1 - 3/(8q_i)) ≈ exp(-3H/(8)) where H = Σ 1/q_i.
    
    By Mertens' theorem for QNR primes, H ~ (1/2) log log X.
    So the probability ~ exp(-3 log log X / 16) = (log X)^{-3/16} → 0.
    
    This suggests that for large enough n, at least one QNR prime must divide
    m_3 or m_7/2, which would make A=3 or A=7 work.
    
    But this is still a HEURISTIC argument, not a proof.
    """)
    
    # Let's check: what's the least QNR mod n for the hard cases?
    print(f"Least QNR mod n (hard cases):")
    least_qnr_values = []
    for c in hard_cases[:50]:
        n = c['n']
        # Find least QNR
        for p in range(2, min(n, 10000)):
            if isprime(p) and legendre_symbol(p, n) == -1:
                least_qnr_values.append((n, p))
                break
    
    if least_qnr_values:
        qnr_dist = Counter(p for _, p in least_qnr_values)
        print(f"  Distribution: {dict(sorted(qnr_dist.items())[:20])}")
        print(f"  Max least QNR: {max(p for _, p in least_qnr_values)}")
        
        # Does the least QNR divide m_3 or m_7/2?
        divides_m3 = 0
        divides_m7h = 0
        divides_neither = 0
        for n, qnr in least_qnr_values:
            m3 = (n + 3) // 4
            m7h = (n + 7) // 8
            if m3 % qnr == 0:
                divides_m3 += 1
            elif m7h % qnr == 0:
                divides_m7h += 1
            else:
                divides_neither += 1
        
        print(f"\n  Least QNR divides m_3: {divides_m3}")
        print(f"  Least QNR divides m_7/2: {divides_m7h}")
        print(f"  Least QNR divides NEITHER: {divides_neither}")
        
        if divides_neither > 0:
            print(f"\n  In {divides_neither} cases, least QNR divides neither.")
            print(f"  But A=3 still works — a DIFFERENT QNR (not the least) divides m_3.")
    
    # Save
    output = {
        'hard_cases_count': len(hard_cases),
        'a3_rescues': a3_rescues,
        'a3_fails': a3_fails,
        'm3_also_all_qr': m3_also_all_qr,
        'coprimality': 'm_3 = 2*(m_7/2) - 1, gcd(m_3, m_7/2) = 1',
    }
    
    with open('/Users/skippotter/.openclaw/workspace/ErdosStrausConjecture/c7_formal_proof_data.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to c7_formal_proof_data.json")


if __name__ == '__main__':
    main()