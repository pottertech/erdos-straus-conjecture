/* collision_margin_engine.c — research v0.1 (collision-research program, lane L1)
 *
 * Objective: for every hard-case prime p in [10^7, 10^9) (the sweep population:
 * p = 12k+1, 5 does not divide p, and every odd prime factor of (p+3)/4 is
 * 1 (mod 3) — factor 2 exempt), let u = first(p) be the first-working
 * admissible parameter (u = 3 (mod 4), u <= 255, gcd(M, u) = 1, M = p*x with
 * x = (p+u)/4, and the exact span criterion P | M^2, P = -M (mod u) satisfied).
 *
 * At that parameter compute D_u(M) = { d mod u : d divides M } (the one-sided
 * divisor-residue set; every d is a unit mod u by admissibility) and measure:
 *   (1) |D_u(M)| against phi(u)/2 — the pigeonhole sufficient condition
 *       (|D| > phi(u)/2 implies D and -D overlap, i.e. -1 in S_u(M) = D D^-1);
 *   (2) whether a collision d, d' in D_u(M) with d + d' = 0 (mod u) exists
 *       (this must hold for EVERY swept prime: by the prior verified sweeps
 *       each first-working u satisfies -1 in S_u(M), and the split of the
 *       centered witness into positive and negative parts yields the pair);
 *   (3) the minimal collision pair (d, u - d) when one exists.
 *
 * Populations reported: pigeonhole-conclusive ("pigeon"), pigeonhole-
 * insufficient but collision present ("delicate" — the structural research
 * object), and collisions absent (counted as engine mismatches; must be 0).
 * Cross-direction check on anchor primes: no collision at admissible
 * parameters below the first-working parameter (sampled).
 *
 * Build (research; sanitizer gate):
 *   cc -O2 -std=c17 -fsanitize=undefined -fno-sanitize-recover=undefined \
 *     collision_margin_engine.c -o collision_margin_engine
 *   ./collision_margin_engine --selftest
 *   ./collision_margin_engine 999999999
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>

typedef uint64_t u64;
typedef unsigned __int128 u128;

/* ---- factor sieve over [0, X] (half-sieve, smallest-odd-factor) ---- */
static uint16_t *sp;

static u64 gcd_u64(u64 a, u64 b) {
    while (b) { u64 t = a % b; a = b; b = t; }
    return a;
}

static int fac(int x, int *qs, int *es) {
    int n = 0;
    while (x > 1) {
        int q = (x % 2 == 0) ? 2 : (sp[x / 2] ? sp[x / 2] : x), e = 0;
        do { x /= q; e++; } while (x % q == 0);
        qs[n] = q; es[n] = e; n++;
    }
    return n;
}

/* ---- first-working parameter (the verified sweep algorithm, ceiling 255) ---- */
static int first(int p) {
    for (int u = 3; u <= 255; u += 4) {
        int x = (p + u) / 4;
        u64 M = (u64)p * (u64)x;
        if (gcd_u64(M, (u64)u) != 1) continue;
        u128 d[256], n[256];
        memset(d, 0, sizeof d);
        d[1] = 1;
        int qs[40], es[40];
        int nf = fac(x, qs, es);
        qs[nf] = p; es[nf] = 1; nf++;
        for (int i = 0; i < nf; i++) {
            int q = qs[i], e = es[i];
            memset(n, 0, sizeof n);
            u128 power = 1;
            u64 qr = 1;
            for (int j = 0; j <= 2 * e; j++) {
                for (int r = 0; r < u; r++)
                    if (d[r]) n[(int)((r * qr) % u)] = d[r] * power;
                if (j < 2 * e) power *= (u128)q;
                qr = (u64)qr * (u64)q % (u64)u;
            }
            memcpy(d, n, sizeof d);
        }
        u128 P = d[(u - (int)(M % (u64)u)) % u];
        if (!P) continue;
        u128 S = (u128)M * (u128)M;
        u128 Q = S / P;
        if (!(P * Q == S && ((u128)P + (u128)M) % u == 0 &&
              ((u128)Q + (u128)M) % u == 0)) continue;
        u128 yy = ((u128)P + (u128)M) / u, zz = ((u128)Q + (u128)M) / u;
        if (!(yy > 0 && zz > 0)) continue;
        return u;
    }
    return 0;
}

/* ---- phi for small u ---- */
static int phi_small(int u) {
    int phi = u;
    for (int q = 2; q * q <= u; q++) {
        if (u % q == 0) {
            phi -= phi / q;
            while (u % q == 0) u /= q;
        }
    }
    if (u > 1) phi -= phi / u;
    return phi;
}

/* ---- intrinsic witness classification (verified mod840 procedure) ----
 * Candidates: divisors of M^2 bounded by M with d = -M (mod u);
 * par = M % d == 0 (parametric; the one-sided criterion),
 * non = a nonparametric witness exists (d does not divide M).
 * firstpar = the class of the smallest qualifying candidate. */
static int classify_witness(int p, int u, int x, int *par, int *non, int *firstpar) {
    u64 M = (u64)p * (u64)x;
    int target = (u - (int)(M % (u64)u)) % u;
    /* divisors of x^2 (full 2e window) */
    static u64 ds[262144];
    int nds = 0;
    ds[nds++] = 1;
    int qs[40], es[40];
    int nf = fac(x, qs, es);
    for (int i = 0; i < nf; i++) {
        int q = qs[i], e = es[i];
        int old = nds;
        u64 powr = 1;
        for (int j = 1; j <= 2 * e; j++) {
            powr *= (u64)q;
            for (int kk = 0; kk < old; kk++) {
                assert(nds < 262144);
                ds[nds++] = ds[kk] * powr;
            }
        }
    }
    /* ascending order is REQUIRED for the early-break loops below to be sound
     * (the verified mod840 procedure sorts likewise) */
    for (int i = 0; i < nds; i++)
        for (int j = i + 1; j < nds; j++)
            if (ds[j] < ds[i]) { u64 t = ds[i]; ds[i] = ds[j]; ds[j] = t; }
    *par = 0; *non = 0; *firstpar = -1;
    int got = 0;
    int nA = 0;
    u128 As[3];
    As[nA++] = 1;
    if ((u64)p <= M) As[nA++] = (u128)(u64)p;
    if ((u128)(u64)p * (u64)p <= (u128)M) As[nA++] = (u128)(u64)p * (u64)p;
    u128 Bs[3];
    int nB = 0;
    Bs[nB++] = (u128)1;
    if ((u64)x <= M) Bs[nB++] = (u128)(u64)x;
    if ((u128)(u64)x * (u64)x <= (u128)M) Bs[nB++] = (u128)(u64)x * (u64)x;
    for (int ia = 0; ia < nA; ia++) {
        u128 A = As[ia];
        for (int ib = 0; ib < nB; ib++) {
            u128 cand = A * Bs[ib];
            if (cand > (u128)M) break;
            if ((int)(u64)(cand % (u128)u) != target) continue;
            if (!got) { *firstpar = (int)(((u128)M % cand) == 0); got = 1; }
            if ((u128)M % cand == 0) *par = 1; else *non = 1;
        }
        for (int i2 = 0; i2 < nds; i2++) {
            u128 cand = A * (u128)ds[i2];
            if (cand > (u128)M) break;
            if ((int)(u64)(cand % (u128)u) != target) continue;
            if (!got) { *firstpar = (int)(((u128)M % cand) == 0); got = 1; }
            if ((u128)M % cand == 0) *par = 1; else *non = 1;
        }
    }
    assert(got);
    return 0;
}

/* ---- divisor-residue set D_u(M) (bitset), popcount, minimal collision pair ---- */
static int have[256], tmp[256];

static int build_D(int p, int u, int x, int *minpair) {
    u64 M = (u64)p * (u64)x;
    memset(have, 0, sizeof(int) * 256);
    have[1 % u] = 1;
    int qs[40], es[40];
    int nf = fac(x, qs, es);
    qs[nf] = p; es[nf] = 1; nf++;
    for (int i = 0; i < nf; i++) {
        int q = qs[i], e = es[i];
        memcpy(tmp, have, sizeof(int) * 256);
        u64 powr = 1;
        for (int k = 0; k <= e; k++) {
            for (int r = 0; r < u; r++) {
                if (tmp[r]) {
                    int nr = (int)(((u64)r * powr) % (u64)u);
                    have[nr] = 1;
                }
            }
            powr = (u64)powr * (u64)q % (u64)u;
        }
    }
    (void)M;
    int cnt = 0;
    for (int r = 0; r < u; r++) cnt += have[r];
    *minpair = 0;
    for (int r = 1; r < u; r++) {
        if (have[r] && have[(u - r) % u]) { *minpair = r; break; }
    }
    return cnt;
}

static int i840idx(int r) {
    switch (r) {
        case 1: return 0;
        case 121: return 1;
        case 169: return 2;
        case 289: return 3;
        case 361: return 4;
        case 529: return 5;
    }
    return -1;
}

int main(int argc, char **argv) {
    int selftest = (argc > 1 && strcmp(argv[1], "--selftest") == 0);
    int hi = 999999999;
    if (!selftest && argc > 1) hi = atoi(argv[1]);
    int X = (hi + 255) / 4;

    sp = (uint16_t *)calloc((size_t)X / 2 + 2, sizeof(uint16_t));
    if (!sp) { fprintf(stderr, "alloc failed\n"); return 2; }
    for (int q = 3; (u64)q * q <= (u64)X; q += 2)
        if (!sp[q / 2])
            for (u64 j = (u64)q * q; j <= (u64)X; j += 2 * (u64)q)
                if (!sp[j / 2]) sp[j / 2] = (uint16_t)q;
    fprintf(stderr, "factor sieve ready\n");

    if (selftest) {
        int anchors[4] = {1129, 8803369, 32349601, 651412441};
        int expect[4] = {11, 107, 15, 83};
        for (int i = 0; i < 4; i++) {
            int u = first(anchors[i]);
            int ok = (u == expect[i]);
            int x = (anchors[i] + u) / 4;
            int mp = 0;
            int pop = build_D(anchors[i], u, x, &mp);
            int ph = phi_small(u);
            printf("ANCHOR %d u=%d %s | %s D=%d phi=%d margin=%d pair=(%d,%d) pigeon=%s\n",
                   anchors[i], u, ok ? "OK" : "FAIL",
                   mp ? "COLLISION" : "NO-COLLISION",
                   pop, ph, 2 * pop - ph, mp, mp ? (u - mp) : 0,
                   (2 * pop > ph) ? "yes" : "no");
            if (!ok || !mp) { printf("SELFTEST FAIL\n"); return 1; }
        }
        /* cross-direction: at admissible u below the anchor's first-working
           parameter, the span criterion fails, hence no collision (sampled) */
        int below1 = first(1129);   /* 11 */
        for (int u = 3; u < below1; u += 4) {  /* u = 3, 7 */
            int x = (1129 + u) / 4;
            u64 M = (u64)1129 * (u64)x;
            if (gcd_u64(M, (u64)u) != 1) continue;
            int mp = 0;
            build_D(1129, u, x, &mp);
            if (mp) {
                printf("CROSSDIR FAIL: collision at u=%d below first-working %d\n", u, below1);
                return 1;
            }
        }
        printf("SELFTEST PASS\n");
        return 0;
    }

    /* full sweep over the hard-case population */
    static unsigned char comp[999999999 / 12 + 2];
    for (int q = 5; (u64)q * q <= (u64)hi; q += 2)
        if (!sp[q / 2]) {
            int r = 0;
            while ((12 * r + 1) % q) r++;
            u64 k = r;
            if (12 * k + 1 == (u64)q) k += q;
            for (; k < 999999999 / 12 + 2ull; k += q) comp[k] = 1;
        }
    fprintf(stderr, "prime sieve ready\n");

    u64 sweep = 0, pigeon = 0, delicate = 0, mismatch = 0, h24 = 0;
    u64 by840_pigeon[840] = {0}, by840_all[840] = {0}, by840_del[840] = {0};
    u64 byu_pigeon[256] = {0}, byu_all[256] = {0}, byu_del[256] = {0};
    u64 margin_hist[64] = {0}; /* margin = 2|D| - phi, clamped at +63 */
    u64 p5_all[5] = {0}, p5_onlypar[5] = {0}, p5_both[5] = {0},
        p5_onlynon[5] = {0}, p5_mod840_all[5] = {0}, p5_mod840_onlynon[5] = {0};
    u64 intr[6][3] = {{0}}; /* intrinsic classes per mod-840 class (onlypar/both/onlynon) */
    FILE *del = fopen("delicate_sample.jsonl", "w");
    u64 delicate_total = 0;

    for (int k = 1; (u64)k < 999999999 / 12 + 2ull; k++) {
        if (comp[k]) continue;
        int p = 12 * k + 1;
        if (p > hi) break;
        if (p <= 10000000) continue;
        /* hard-case predicate: every ODD prime factor of (p+3)/4 is 1 (mod 3);
           factor 2 is exempt (parity-slip rule). */
        int qs[40], es[40];
        int nf = fac((p + 3) / 4, qs, es);
        int ok = 1;
        for (int i = 0; i < nf; i++)
            if (qs[i] != 2 && qs[i] % 3 != 1) { ok = 0; break; }
        if (!ok) continue;

        int u = first(p);
        if (u == 0) { mismatch++; fprintf(stderr, "NOFIRST %d\n", p); continue; }
        int x = (p + u) / 4;
        int mp = 0;
        int pop = build_D(p, u, x, &mp);
        int ph = phi_small(u);
        sweep++;
        h24 += (p % 24 == 1);
        if (!mp) { mismatch++; continue; }
        int margin = 2 * pop - ph;
        int mh = margin < 0 ? 0 : (margin > 63 ? 63 : margin);
        margin_hist[mh]++;
        int pg = (2 * pop > ph);
        int r840 = p % 840;
        int in840 = (r840 == 1 || r840 == 121 || r840 == 169 ||
                     r840 == 289 || r840 == 361 || r840 == 529);
        if (in840) by840_all[r840]++;
        int par = 0, non = 0, firstpar = -1;
        classify_witness(p, u, x, &par, &non, &firstpar);
        int m5 = p % 5;
        p5_all[m5]++;
        if (in840) p5_mod840_all[m5]++;
        if (par && !non) { p5_onlypar[m5]++; if (in840) intr[i840idx(r840)][0]++; }
        else if (par && non) { p5_both[m5]++; if (in840) intr[i840idx(r840)][1]++; }
        else if (!par && non) {
            p5_onlynon[m5]++;
            if (in840) { intr[i840idx(r840)][2]++; p5_mod840_onlynon[m5]++; }
        } else {
            mismatch++; fprintf(stderr, "NOWITNESS %d\n", p);
        }
        byu_all[u]++;
        if (pg) {
            pigeon++;
            if (in840) by840_pigeon[r840]++;
            byu_pigeon[u]++;
        } else {
            delicate++; delicate_total++;
            if (in840) by840_del[r840]++;
            byu_del[u]++;
            if (delicate_total <= 5000 && del)
                fprintf(del,
                    "{\"p\": %d, \"u\": %d, \"D\": %d, \"phi\": %d, "
                    "\"margin\": %d, \"pair\": [%d, %d]}\n",
                    p, u, pop, ph, margin, mp, u - mp);
        }
    }
    if (del) fclose(del);

    printf("SWEEP %llu H24 %llu PIGEON %llu DELICATE %llu MISMATCH %llu\n",
           (unsigned long long)sweep, (unsigned long long)h24,
           (unsigned long long)pigeon, (unsigned long long)delicate,
           (unsigned long long)mismatch);
    for (int i = 0; i < 6; i++) {
        int r[6] = {1, 121, 169, 289, 361, 529};
        printf("BY840 %d all=%lld pigeon=%lld delicate=%lld rate_del=%lld\n",
               r[i],
               (long long)by840_all[r[i]], (long long)by840_pigeon[r[i]],
               (long long)by840_del[r[i]],
               by840_all[r[i]] ? (long long)(10000 * by840_del[r[i]] / by840_all[r[i]]) : 0LL);
    }
    for (int u = 3; u <= 255; u += 4)
        if (byu_all[u])
            printf("BYU %d all=%lld pigeon=%lld delicate=%lld\n", u,
                   (long long)byu_all[u], (long long)byu_pigeon[u],
                   (long long)byu_del[u]);
    printf("MARGIN");
    for (int i = 0; i < 64; i++) printf(" %lld", (long long)margin_hist[i]);
    printf("\n");
    printf("DELICATE_TOTAL %llu (sample capped at 5000 in delicate_sample.jsonl)\n",
           (unsigned long long)delicate_total);
    for (int g = 1; g <= 4; g++) {
        printf("MOD5 %d all=%lld onlypar=%lld both=%lld onlynon=%lld rate_onlynon=%lld\n",
               g,
               (long long)p5_all[g], (long long)p5_onlypar[g],
               (long long)p5_both[g], (long long)p5_onlynon[g],
               p5_all[g] ? (long long)(10000 * p5_onlynon[g] / p5_all[g]) : 0LL);
        printf("MOD5MOD840 %d all=%lld onlynon=%lld rate=%lld\n", g,
               (long long)p5_mod840_all[g], (long long)p5_mod840_onlynon[g],
               p5_mod840_all[g] ? (long long)(10000 * p5_mod840_onlynon[g] / p5_mod840_all[g]) : 0LL);
    }
    for (int i = 0; i < 6; i++) {
        int r[6] = {1, 121, 169, 289, 361, 529};
        printf("INTR840 %d onlypar=%lld both=%lld onlynon=%lld\n", r[i],
               (long long)intr[i][0], (long long)intr[i][1], (long long)intr[i][2]);
    }
    return mismatch ? 1 : 0;
}
