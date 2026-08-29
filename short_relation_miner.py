from math import isqrt, gcd
from collections import Counter
import argparse, json, time

CORE = (1, 121, 169, 289, 361, 529)


def small_primes(n=20000):
    bs = bytearray(b'\1') * (n + 1)
    bs[:2] = b'\0\0'
    for p in range(2, isqrt(n) + 1):
        if bs[p]:
            bs[p*p:n+1:p] = b'\0' * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if bs[i]]


PR = small_primes(12000)


def isprime32(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 3, 5, 7):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factor(n):
    out = {}
    for p in PR:
        if p * p > n:
            break
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            out[p] = c
        if n == 1:
            break
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def hard_gate(n):
    if n % 12 != 1 or n % 5 == 0:
        return False
    t = (n + 3) // 4
    while t % 2 == 0:
        t //= 2
    return all(p % 3 == 1 for p in factor(t))


def shift_reduced(n):
    for v in (n + 1, n + 4):
        z = v
        while z % 2 == 0:
            z //= 2
        if any(p % 4 == 3 for p in factor(z)):
            return False
    return True


def factor_M(n, u):
    x = (n + u) // 4
    fm = {n: 1}
    for p, e in factor(x).items():
        fm[p] = fm.get(p, 0) + e
    return x, fm


def one_factor_relation(n, u):
    if (n + u) % 4:
        return None
    x, fm = factor_M(n, u)
    if gcd(n * x, u) != 1:
        return None
    for p in fm:
        if p % u == u - 1:
            return ('p=-1', p, None, 'n' if p == n else 'x')
    for p, e in fm.items():
        if e >= 3 and pow(p, 3, u) == u - 1:
            return ('p^3=-1', p, None, 'n' if p == n else 'x')
    return None


def two_factor_relation(n, u):
    if (n + u) % 4:
        return None
    x, fm = factor_M(n, u)
    if gcd(n * x, u) != 1:
        return None
    ps = list(fm)
    for i, p in enumerate(ps):
        rp = p % u
        for q in ps[i+1:]:
            rq = q % u
            source = ('n' if p == n else 'x') + '+' + ('n' if q == n else 'x')
            if rp * rq % u == u - 1:
                return ('pq=-1', p, q, source)
            if (rp + rq) % u == 0:
                return ('p=-q', p, q, source)
    return None


def best_short_relation(n, u_max=299):
    cubic = None
    for u in range(3, u_max + 1, 4):
        rel = one_factor_relation(n, u)
        if rel:
            if rel[0] == 'p=-1':
                return u, rel
            if cubic is None:
                cubic = (u, rel)
    if cubic:
        return cubic
    for u in range(3, u_max + 1, 4):
        rel = two_factor_relation(n, u)
        if rel:
            return u, rel
    return None


def run(lo, hi, u_max=299, save_records=True):
    core = hard = tail = 0
    failures, records = [], []
    routes, sources, gates = Counter(), Counter(), Counter()
    for block in range(lo // 840, hi // 840 + 1):
        base = 840 * block
        for residue in CORE:
            n = base + residue
            if n < lo or n > hi or n < 2 or not isprime32(n):
                continue
            core += 1
            if not hard_gate(n):
                continue
            hard += 1
            if not shift_reduced(n):
                continue
            tail += 1
            best = best_short_relation(n, u_max)
            if not best:
                failures.append(n)
                continue
            u, (kind, p, q, source) = best
            routes[kind] += 1
            sources[source] += 1
            gates[u] += 1
            if save_records:
                records.append([n, u, kind, p, q, source])
    return {
        'range': [lo, hi], 'u_max': u_max,
        'core_primes': core, 'after_hard': hard, 'after_shift': tail,
        'failure_count': len(failures), 'failures': failures,
        'route_counts': dict(routes), 'source_counts': dict(sources),
        'u_counts': dict(sorted(gates.items())), 'records': records,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lo', type=int, default=2)
    ap.add_argument('--hi', type=int, required=True)
    ap.add_argument('--u-max', type=int, default=299)
    ap.add_argument('--json')
    ap.add_argument('--no-records', action='store_true')
    args = ap.parse_args()
    start = time.time()
    result = run(args.lo, args.hi, args.u_max, not args.no_records)
    result['seconds'] = time.time() - start
    print({k: v for k, v in result.items() if k != 'records'})
    if args.json:
        with open(args.json, 'w') as fh:
            json.dump(result, fh, indent=2)
