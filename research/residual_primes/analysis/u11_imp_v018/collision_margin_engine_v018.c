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

/* v0.8 (R8): the sub-fw no-collision theorem check + the delicate rescue scan.
 * Forward decls: subfw_check uses build_D/phi_small defined below first(). */
static int build_D(int p, int u, int x, int *minpair);
static int phi_small(int u);
static u64 subfw_checks = 0, subfw_coll = 0, subfw_pigeon = 0;
static u64 delres_total = 0, delres_pig = 0, delres_coll = 0, delres_nopig = 0;
static u64 delres_pignocoll = 0;
static u64 pig_u2[256] = {0}, coll_u2[256] = {0}, collfw_u2[256] = {0};
static u64 re_total[1024] = {0}, re_pig[1024] = {0}, re_del[1024] = {0};
static u64 re_dunit[1024] = {0}, re_dsmall[1024] = {0}, re_dlarge[1024] = {0};
static u64 re_rpig[1024] = {0}, re_rnop[1024] = {0};
static u64 unr_byu[256] = {0};
static int unr_p[400], unr_u[400], unr_cls[400];
static u64 unr_tot = 0;
static u64 u7_total[7] = {0}, u7_adm[7] = {0}, u7_span[7] = {0};
static u64 u7_fail[7] = {0}, u7_inad[7] = {0}, u7_fivex[7] = {0};
static u64 u7_n7[7] = {0}, u7_tp[7] = {0};
static u64 u7_pop[64] = {0};
static u64 u7_subfw_coll = 0;
/* v0.10 (E-014): the failing-class fingerprints (r7 in {1,2,4}) */
static u64 u7fc_span[7][4];
static u64 u7fc_span_miss = 0;
/* v0.11 (E-015): the spanner 5-depth census + the 125 | x' flag */
static u64 u7fc_sv5[7][4]; /* 0..2, then >= 3 */
static u64 u7fc_s125[7];   /* spanners with 125 | x' */
/* v0.12 (E-016): the depth-0 (5-free) spanner mechanism + the hard core */
static u64 u7fc_d0_pop[7][7];      /* spanner |D_7| buckets by class */
static u64 u7fc_d0_pure2[7];       /* minimal class-A witness = a pure 2-power */
static u64 u7fc_d0_mixed[7];       /* ... = an x-divisor with an odd part */
static u64 u7fc_fail_b840[7][6];   /* fail records by (r7, mod-840 class) */
static u64 u7fc_span_pigeon[7];    /* depth-0 spanners with |D| > 3 (pigeon) */
/* v0.13 (E-017): the generator census + the fail D-set shapes */
static u64 u7fc_gen[7][2];         /* [0]: generator 3 in D, [1]: generator 5 */
static u64 u7fc_gen_125[7][2];     /* the generator-divisor is 125-divisible */
static u64 u7fc_fset[7][64];       /* the fail D-set mask histogram */
static u64 u7fc_fsetv2[7][256];    /* mask x v2(x') bucket (0,1,2,>=3) */
/* v0.15 (E-021): the u = 11 layer census (2 is a primitive root mod 11: the
 * 2-orbit closure is the FULL unit group, so the u = 7 orbit-boundary
 * reading does not carry over verbatim; the census measures first). */
static u64 u11_total[12], u11_adm[12], u11_span[12], u11_fail[12], u11_inad[12];
static u64 u11_pop[12 * 12], u11_pop_span[12 * 12];
static u64 u11_fset[12][2048];     /* the fail D-set mask histogram (11-bit) */
static u64 u11_fcoll[12][2048];    /* the fail records WITH a collision: mask histogram */
static u64 u11_subfw_coll = 0;    /* census row, NOT an error gate (see comment) */
/* v0.16 (E-021 part 2): the composition-level condition census. 2 is a
 * primitive root mod 11, but -1 is a non-residue (11 = 3 (mod 4)): the
 * index-2 structure is the Legendre split, QR = {1,3,4,5,9} and the
 * non-residues {2,6,7,8,10}. The candidate condition (the H-7 analog):
 * x' has an odd prime divisor outside the QRs. Note 5 in QR here, unlike
 * the u = 7 layer where the prime 5 carried the escape residue. */
static u64 u11_qr[12][4];          /* [c9 * 2 + (u == 11)]: the non-QR-scan x span/fail */
static u64 u11_iffc[12][4];        /* [(coll ? 2 : 0) + (u == 11)]: the collision x span/fail */
static u64 u11_iff_mm = 0;         /* the iff mismatch census row (soft) */
/* v0.17 (E-022): the odd-part purity x v2-bucket x fate cells. The odd part
 * of x' is QR-pure when every odd prime divisor is in {1,3,4,5,9} (mod 11);
 * the firing condition (#36) is exactly the impure case. */
static u64 u11purity[12][2][4][2]; /* [r11][allQR][v2b][span?1:0] */
/* v0.18 (E-022 part 2): the impure-cell decomposition. In the QR-n_bar
 * classes x_bar in QR, so x' (always odd here) has an EVEN multiplicity
 * of non-QR odd primes; the count histogram x span/fail is the first
 * mechanism pass, with the non-QR prime residue multiset summary. */
static u64 u11pcnt[12][10][2];     /* [r11][count cap 9][span?1:0] */
static u64 u11pres[12][11][12][2]; /* [r11][first non-QR prime residue][count cap][span?1:0] */
/* v0.14 (E-018): the composition-level iff census (H-7's formal direction) */
static u64 u7fc_iff_span_yes[7][2];  /* [0]: span with the condition, [1]: span without */
static u64 u7fc_iff_fail_yes[7][2];  /* [0]: fail with the condition, [1]: fail without */
static u64 u7fc_iff_mismatch = 0;
static u64 u7fc_fail[7];
static u64 u7fc_v2[7][3], u7fc_v5[7][3], u7fc_in840[7][2];
static u64 u7fc_span_n[7], u7fc_fail_n[7];

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

static void subfw_check(int p, int u, int x) {
    /* E-011 (R8) theorem-consistency check: below the first-working parameter
     * the span criterion fails, so by the R4/R5 machine-checked chain
     * (pigeonhole => collision, collision => the centered span) the collision
     * AND the pigeonhole condition must be absent at every admissible u where
     * the span fails. Counted softly; nonzero counts fail the run exit gate. */
    int mpS = 0;
    int popS = build_D(p, u, x, &mpS);
    subfw_checks++;
    if (mpS) subfw_coll++;
    if (2 * popS > phi_small(u)) subfw_pigeon++;
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
        if (!P) { subfw_check(p, u, x); continue; }
        u128 S = (u128)M * (u128)M;
        u128 Q = S / P;
        if (!(P * Q == S && ((u128)P + (u128)M) % u == 0 &&
              ((u128)Q + (u128)M) % u == 0)) { subfw_check(p, u, x); continue; }
        u128 yy = ((u128)P + (u128)M) / u, zz = ((u128)Q + (u128)M) / u;
        if (!(yy > 0 && zz > 0)) { subfw_check(p, u, x); continue; }
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

static int i840idx2(int u, int m5) {
    if (u <= 0 || u >= 256) return -1;
    if (m5 != 1 && m5 != 3 && m5 != 4) return -1;
    return (u * 4) + (m5 == 1 ? 0 : (m5 == 3 ? 1 : 2)); /* index into 1024-slot tables */
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
        /* v0.8 selftest: the rescue machinery on the delicate anchor
         * (651412441, fw = 83, margin -58). Silent unless a failure: the
         * printed selftest output stays byte-identical to v0.6/v0.7. */
        {
            int pa = 651412441, fa = expect[3];
            int pig_nocoll_here = 0;
            long pig_here = 0, coll_here = 0;
            for (int u2 = fa + 4; u2 <= 255; u2 += 4) {
                int x2 = (pa + u2) / 4;
                u64 M2 = (u64)pa * (u64)x2;
                if (gcd_u64(M2, (u64)u2) != 1) continue;
                int mp2 = 0;
                int pop2 = build_D(pa, u2, x2, &mp2);
                int pig2 = (2 * pop2 > phi_small(u2));
                if (pig2) { pig_here++; if (!mp2) pig_nocoll_here = 1; }
                if (mp2) coll_here++;
            }
            if (pig_nocoll_here) { printf("SELFTEST FAIL (rescue consistency)\n"); return 1; }
            (void)pig_here; (void)coll_here; /* silent by design: the printed
             * selftest output stays byte-identical to v0.6/v0.7 */
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
    u64 xall[256][5] = {{0}}, xnop[256][5] = {{0}}, xdel[256][5] = {{0}};
    u64 u11_g4 = 0, u11_g4_fivex = 0, u11_g4_notfivex = 0;
    u64 g3u7 = 0, g3u7_fivex = 0, g3u7_notfivex = 0, g3u7_E5[4] = {0};
    u64 w7par_p = 0, w7par_unit = 0, w7par_v5[4] = {0};
    u64 w7non_p = 0, w7non_unit = 0, w7non_v5[4] = {0}, w7non_over5 = 0;
    u64 sh_p = 0, sh_unit = 0, sh_v5[4] = {0};
    u64 xall840[256][5] = {{0}}, xnop840[256][5] = {{0}}; /* layer x mod-5 cross */
    static u64 shape_par_free[1024] = {0}, shape_par_p[1024] = {0};
    static u64 shape_non_free[1024] = {0}, shape_non_p[1024] = {0};
    static u64 slice_fivex[1024] = {0};
    static u64 slice_seen[1024] = {0};
    u64 del_total = 0, del_d1one = 0, del_unitpair = 0, del_small = 0, del_large = 0;
    u64 del_halfsquare = 0, del_bucket[4] = {0};
    FILE *del = fopen("delicate_sample.jsonl", "w");
    FILE *rfr = fopen("delicate_rescue.jsonl", "w");
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
        if (!pg) {
            /* the delicate class: the minimal collision pair shape */
            if (mp) {
                delicate++;
                int d1s = mp, d2s = (u - mp) % u;
                del_total++;
                int uhalf = u / 2;
                if (d1s == 1) {
                    del_d1one++;
                    if (d2s == u - 1) del_unitpair++;
                } else if (d1s <= uhalf) {
                    del_small++;
                } else {
                    del_large++;
                }
                if (d1s * d1s == u) del_halfsquare++;
                int mb = d1s == 1 ? 0 : (4 * d1s <= u ? 1 : (2 * d1s <= u ? 2 : 3));
                del_bucket[mb]++;
            }
        }
        p5_all[m5]++;
        if (in840) p5_mod840_all[m5]++;
        if (u < 256) {
            xall[u][m5]++;
            if (in840) xall840[u][m5]++;
            if (!pg) xdel[u][m5]++;
        }
        if (u < 256) {
            /* R7: the witness-shape fingerprint for every populated (layer, mod-5)
             * slice: the smallest parametric witness and the smallest nonparametric
             * companion (when present), each fingerprinted by p-containment and the
             * 5-valuation of x. */
            if (par || non) {
                u64 M = (u64)p * (u64)x;
                int target = (u - (int)(M % (u64)u)) % u;
                static u64 dsR[262144];
                int ndsR = 0;
                dsR[ndsR++] = 1;
                int qsR[40], esR[40];
                int nfR = fac(x, qsR, esR);
                for (int i = 0; i < nfR; i++) {
                    int q3 = qsR[i], e3 = esR[i];
                    int old3 = ndsR;
                    u64 powr3 = 1;
                    for (int j = 1; j <= 2 * e3; j++) {
                        powr3 *= (u64)q3;
                        for (int kk = 0; kk < old3; kk++) {
                            assert(ndsR < 262144);
                            dsR[ndsR++] = dsR[kk] * powr3;
                        }
                    }
                }
                for (int i = 0; i < ndsR; i++)
                    for (int j = i + 1; j < ndsR; j++)
                        if (dsR[j] < dsR[i]) { u64 t = dsR[i]; dsR[i] = dsR[j]; dsR[j] = t; }
                int found_par = 0, found_non = 0;
                for (int pa2 = 0; pa2 < 3; pa2++) {
                    u128 A = (pa2 == 0) ? 1 : (pa2 == 1 ? (u128)(u64)p : (u128)(u64)p * (u64)p);
                    if (A > (u128)M) break;
                    for (int i2 = 0; i2 < ndsR; i2++) {
                        u128 cand = A * (u128)dsR[i2];
                        if (cand > (u128)M) break;
                        if ((int)(u64)(cand % (u128)u) != target) continue;
                        int ispar = (int)((M % (u64)cand) == 0);
                        if (ispar && !found_par) {
                            found_par = 1;
                            int si = i840idx2(u, m5);
                            if (si >= 0) shape_par_free[si] += 1 - (pa2 > 0), shape_par_p[si] += (pa2 > 0);
                        } else if (!ispar && !found_non) {
                            found_non = 1;
                            int si = i840idx2(u, m5);
                            if (si >= 0) shape_non_free[si] += 1 - (pa2 > 0), shape_non_p[si] += (pa2 > 0);
                        }
                    }
                    if (found_par && found_non) break;
                }
                if (par) assert(found_par);
                if (non) assert(found_non);
            }
            int x5 = (int)(x % 5);
        if (x5 == 0) {
            int si = i840idx2(u, m5);
            if (si >= 0) slice_fivex[si]++;
        }
            { int si = i840idx2(u, m5); if (si >= 0 && (par || non)) slice_seen[si]++; }
        }
        if (u == 11 && m5 == 4) {
            u11_g4++;
            if (x % 5 == 0) u11_g4_fivex++; else u11_g4_notfivex++;
            if (par || non) {
                /* re-derive the smallest qualifying candidate in enumeration
                 * order and fingerprint its p-containment + 5-valuation */
                u64 M = (u64)p * (u64)x;
                int target = (11 - (int)(M % 11ULL)) % 11;
                // find smallest: A in {1, p} x (structured divisors of x^2, ascending)
                int found = 0;
                for (int pa2 = 0; pa2 < 2 && !found; pa2++) {
                    u128 A = (pa2 == 0) ? 1 : (u128)(u64)p;
                    /* smallest divisor d of M^2 with d <= M, d = A * (x-part),
                     * divisible-residue target: enumerate the ascending
                     * divisors of x (and x^2) */
                    static u64 ds2[262144];
                    int nds2 = 0;
                    ds2[nds2++] = 1;
                    int qs2[40], es2[40];
                    int nf2 = fac(x, qs2, es2);
                    for (int i = 0; i < nf2; i++) {
                        int q2 = qs2[i], e2 = es2[i];
                        int old2 = nds2;
                        u64 powr2 = 1;
                        for (int j = 1; j <= 2 * e2; j++) {
                            powr2 *= (u64)q2;
                            for (int kk = 0; kk < old2; kk++) {
                                assert(nds2 < 262144);
                                ds2[nds2++] = ds2[kk] * powr2;
                            }
                        }
                    }
                    for (int i = 0; i < nds2; i++)
                        for (int j = i + 1; j < nds2; j++)
                            if (ds2[j] < ds2[i]) { u64 t = ds2[i]; ds2[i] = ds2[j]; ds2[j] = t; }
                    for (int i2 = 0; i2 < nds2 && !found; i2++) {
                        u128 cand = A * (u128)ds2[i2];
                        if (cand > (u128)M) break;
                        if ((int)(u64)(cand % (u128)11U) != target) continue;
                        found = 1;
                        /* fingerprint: p-containment and 5-valuation of cand */
                        if (pa2 == 1) sh_p++; else sh_unit++;
                        int v5 = 0;
                        u128 c = cand;
                        assert(c % 5ULL != 0U || 1 == 1);
                        while (c % 5ULL == 0U && v5 < 3) { c /= 5ULL; v5++; }
                        if (c % 5ULL == 0U) v5 = 3; /* capped */
                        sh_v5[v5]++;
                    }
                }
                assert(found);
            }
        }
        if (u == 7 && m5 == 3) {
            g3u7++;
            u64 M = (u64)p * (u64)x;
            if (x % 5 == 0) g3u7_fivex++; else g3u7_notfivex++;
            // the M 5-depth (M = 5^E * odd part)
            int E5 = 0;
            { u64 c = M; while (c % 5ULL == 0U && E5 < 8) { c /= 5ULL; E5++; } }
            int e5cap = E5 > 3 ? 3 : (E5 < 0 ? 3 : E5);
            g3u7_E5[e5cap]++;
            if (!par && !non) { fprintf(stderr, "NOWIT7 %d\n", p); continue; }
            // enumerate the candidates in (A, ascending-ds) order once:
            //   record the first qualifying candidate of EACH kind with its shape
            int target = (7 - (int)(M % 7ULL)) % 7;
            static u64 ds3[262144];
            int nds3 = 0;
            ds3[nds3++] = 1;
            int qs3[40], es3[40];
            int nf3 = fac(x, qs3, es3);
            for (int i = 0; i < nf3; i++) {
                int q3 = qs3[i], e3 = es3[i];
                int old3 = nds3;
                u64 powr3 = 1;
                for (int j = 1; j <= 2 * e3; j++) {
                    powr3 *= (u64)q3;
                    for (int kk = 0; kk < old3; kk++) {
                        assert(nds3 < 262144);
                        ds3[nds3++] = ds3[kk] * powr3;
                    }
                }
            }
            for (int i = 0; i < nds3; i++)
                for (int j = i + 1; j < nds3; j++)
                    if (ds3[j] < ds3[i]) { u64 t = ds3[i]; ds3[i] = ds3[j]; ds3[j] = t; }
            int found_par = 0, found_non = 0;
            for (int pa2 = 0; pa2 < 3; pa2++) {
                u128 A = (pa2 == 0) ? 1 : (pa2 == 1 ? (u128)(u64)p : (u128)(u64)p * (u64)p);
                if (A > (u128)M) break;
                for (int i2 = 0; i2 < nds3; i2++) {
                    u128 cand = A * (u128)ds3[i2];
                    if (cand > (u128)M) break;
                    if ((int)(u64)(cand % (u128)7ULL) != target) continue;
                    int ispar = (int)((M % (u64)cand) == 0);
                    int v5 = 0;
                    { u128 c = cand; while (c % 5ULL == 0U && v5 < 3) { c /= 5ULL; v5++; }
                      if (c % 5ULL == 0U) v5 = 3; }
                    if (ispar && !found_par) {
                        found_par = 1;
                        w7par_p += (pa2 > 0); w7par_unit += 1 - (pa2 > 0);
                        w7par_v5[v5]++;
                    } else if (!ispar && !found_non) {
                        found_non = 1;
                        w7non_p += (pa2 > 0); w7non_unit += 1 - (pa2 > 0);
                        w7non_v5[v5]++;
                        int over5 = (v5 > e5cap) && (v5 < 3 || E5 > 3);
                        if (over5) w7non_over5++;
                    }
                }
                if (found_par && found_non) break;
            }
            if (par) {
                assert(found_par);   /* the both-class: a parametric witness exists */
                assert(found_non);   /* and, per the class-wide onlypar = 0, a nonparametric one too */
            } else {
                assert(found_non);   /* the onlynon-class records */
            }
        }
        /* v0.9 (E-013): the u = 7 layer classification within the (H24) class.
         * fw = 7 <=> the u = 7 span passed (u = 3 failed by E-012, formalized:
         * u3_span_fails_of_odd_x); fw > 7 <=> the span failed (admissible).
         * The explicit span-witness classes: T = p fires the congruences at
         * p = 3 (mod 7), T = x at p = 6 (mod 7) - hand claims the run must
         * verify 0-mismatch (u7_tp vs the class totals). All products u128:
         * p*p*x7 reaches ~2.5e26. */
        if (p % 24 == 1) {
            int r7 = p % 7;
            int x7 = (p + 7) / 4;
            u64 M7 = (u64)p * (u64)x7;
            if (r7 >= 1 && r7 <= 6) {
                u7_total[r7]++;
                int adm7 = (M7 % 7ULL != 0);
                if (adm7) {
                    u7_adm[r7]++;
                    u7_n7[r7]++;
                    if (u == 7) u7_span[r7]++;
                    else {
                        u7_fail[r7]++;
                        int mp7 = 0;
                        int pop7 = build_D(p, 7, x7, &mp7);
                        if (pop7 <= 6) u7_pop[r7 * 8 + pop7]++;
                        if (mp7) u7_subfw_coll++;
                    }
                    if (r7 == 3) {
                        int ok1 = (((u128)p + (u128)M7) % 7ULL == 0);
                        int ok2 = (((u128)p * (u128)x7 * (u128)x7 + (u128)M7) % 7ULL == 0);
                        u7_tp[r7] += (u64)(ok1 && ok2);
                    } else if (r7 == 6) {
                        int ok1 = (((u128)x7 + (u128)M7) % 7ULL == 0);
                        int ok2 = (((u128)p * (u128)p * (u128)x7 + (u128)M7) % 7ULL == 0);
                        u7_tp[r7] += (u64)(ok1 && ok2);
                    }
                } else u7_inad[r7]++;
                /* v0.10 (E-014): fingerprints for the r7 in {1,2,4} records */
                if (r7 == 1 || r7 == 2 || r7 == 4) {
                    if (u == 7) {
                        /* spanner: fingerprint the minimal span candidate P:
                         * enumerate the divisors of x^2 ascending + the
                         * p-scales, first (P + M) % 7 == 0 hit; classify
                         * A: P | x, B: P | x^2 (deeper window), C: p-containing */
                        u64 Mp = (u64)p * (u64)x7;
                        static u64 dsw[262144];
                        int ndw = 0;
                        dsw[ndw++] = 1;
                        int qsw[40], esw[40];
                        int nfw = fac(x7, qsw, esw);
                        for (int i = 0; i < nfw; i++) {
                            int q4 = qsw[i], e4 = esw[i];
                            int oldw = ndw;
                            u64 pw = 1;
                            for (int j = 1; j <= 2 * e4; j++) {
                                pw *= (u64)q4;
                                for (int kk = 0; kk < oldw; kk++) {
                                    assert(ndw < 262144);
                                    dsw[ndw++] = dsw[kk] * pw;
                                }
                            }
                        }
                        for (int i = 0; i < ndw; i++)
                            for (int j = i + 1; j < ndw; j++)
                                if (dsw[j] < dsw[i]) { u64 t = dsw[i]; dsw[i] = dsw[j]; dsw[j] = t; }
                        int hasA = 0, hasB = 0, hasC = 0;
                        for (int i2 = 0; i2 < ndw; i2++) {
                            u64 d0 = dsw[i2];
                            if ((d0 + Mp) % 7ULL == 0) {
                                if (x7 % d0 == 0) hasA = 1; else hasB = 1;
                            }
                            for (int pa3 = 1; pa3 <= 2; pa3++) {
                                u128 cand = (pa3 == 1) ? (u128)d0 * (u128)p
                                                       : (u128)d0 * (u128)p * (u128)p;
                                if ((cand + (u128)Mp) % 7ULL == 0) hasC = 1;
                            }
                        }
                        int e5s = 0;
                        { u64 c5 = (u64)x7; while (c5 % 5ULL == 0 && e5s < 3) { c5 /= 5ULL; e5s++; } }
                        int i5s = (e5s >= 3) ? 3 : e5s;
                        u7fc_sv5[r7][i5s]++;
                        if (x7 % 125ULL == 0) u7fc_s125[r7]++;
                        if (e5s == 0) {
                            /* the depth-0 (5-free) spanner: the |D| route + the
                             * minimal class-A witness's shape */
                            int mpd = 0;
                            int popd = build_D(p, 7, x7, &mpd);
                            if (popd <= 6) u7fc_d0_pop[r7][popd]++;
                            if (2 * popd > 6) u7fc_span_pigeon[r7]++;
                            /* the minimal class-A witness: the smallest
                             * x-divisor d with (d + M') % 7 == 0 */
                            static u64 dxw[262144];
                            int ndx = 0;
                            dxw[ndx++] = 1;
                            int qxw[40], exw[40];
                            int nfx = fac(x7, qxw, exw);
                            for (int i = 0; i < nfx; i++) {
                                int q6 = qxw[i], e6 = exw[i];
                                int oldx = ndx;
                                u64 px = 1;
                                for (int j = 1; j <= e6; j++) {
                                    px *= (u64)q6;
                                    for (int kk = 0; kk < oldx; kk++) {
                                        assert(ndx < 262144);
                                        dxw[ndx++] = dxw[kk] * px;
                                    }
                                }
                            }
                            for (int i = 0; i < ndx; i++)
                                for (int j = i + 1; j < ndx; j++)
                                    if (dxw[j] < dxw[i]) { u64 t = dxw[i]; dxw[i] = dxw[j]; dxw[j] = t; }
                            u64 dmin = 0;
                            for (int i2 = 0; i2 < ndx; i2++) {
                                if ((dxw[i2] + Mp) % 7ULL == 0) { dmin = dxw[i2]; break; }
                            }
                            if (dmin == 0) u7fc_span_miss++;
                            else {
                                /* the odd part of dmin (5-free record: no 5's) */
                                u64 dm = dmin;
                                while (dm % 2ULL == 0) dm /= 2ULL;
                                if (dm == 1) u7fc_d0_pure2[r7]++; else u7fc_d0_mixed[r7]++;
                            }
                            /* the generator census: 3 and 5 are the two
                             * elements of order 6 in (Z/7)* */
                            for (int gi = 0; gi < 2; gi++) {
                                int gres = (gi == 0) ? 3 : 5;
                                if (have[gres]) {
                                    u7fc_gen[r7][gi]++;
                                    /* the generator-divisor's 125-divisibility:
                                     * the 5-window depth beyond 1 */
                                    if (x7 % 125ULL == 0) u7fc_gen_125[r7][gi]++;
                                }
                            }
                        }
                        int cls = hasA ? 0 : (hasB ? 1 : (hasC ? 2 : 3));
                        u7fc_span[r7][cls]++;
                        if (cls == 3) u7fc_span_miss++;
                        u7fc_span_n[r7]++;
                    } else {
                        /* failer: the hard-core profile */
                        u7fc_fail[r7]++;
                        int v2 = 0, v5 = 0;
                        { u64 c = (u64)x7; while (c % 2ULL == 0 && v2 < 3) { c /= 2ULL; v2++; } }
                        { u64 c = (u64)x7; while (c % 5ULL == 0 && v5 < 3) { c /= 5ULL; v5++; } }
                        int i2b = (v2 >= 3) ? 2 : v2, i5b = (v5 >= 3) ? 2 : v5;
                        u7fc_v2[r7][i2b]++;
                        u7fc_v5[r7][i5b]++;
                        u7fc_in840[r7][in840 ? 1 : 0]++;
                        if (in840) {
                            int i840u = i840idx(r840);
                            if (i840u >= 0) u7fc_fail_b840[r7][i840u]++;
                        }
                        {
                            int mask = 0;
                            for (int rr = 1; rr < 7; rr++)
                                if (have[rr]) mask |= (1 << rr);
                            int v2f = 0;
                            { u64 c6 = (u64)x7; while (c6 % 2ULL == 0 && v2f < 3) { c6 /= 2ULL; v2f++; } }
                            int i6 = (v2f >= 3) ? 3 : v2f; /* 0: none, 1, 2, >=3 */
                            u7fc_fset[r7][mask]++;
                            u7fc_fsetv2[r7][(mask * 4) + i6]++;
                        }
                        u7fc_fail_n[r7]++;
                    }
                }
                /* v0.14 (E-018): the composition-level iff (H-7's direction):
                 * the span/fail split vs "x' has an odd prime divisor outside
                 * the 2-orbit closure - i.e. congruent to 3, 5, or 6 (mod 7)".
                 * (The v0.14 probe falsified the {3,5}-only form: the residue
                 * 6 is order 2, but 6*{1,2,4} = {6,5,3} escapes the orbit and
                 * the {3,5} products close the group with it.) The 5-divisible
                 * records (v5 >= 1) are excluded from the iff's domain (their
                 * span is certified by the 5-window / the E-013 classes). */
                if (r7 == 1 || r7 == 2 || r7 == 4) {
                    if (x7 % 5ULL != 0) {
                        /* the odd-prime scan: an odd q | x' with q % 7 in {3,5} */
                        int condfire = 0;
                        int qs8[40], es8[40];
                        int n8f = fac(x7, qs8, es8);
                        for (int i = 0; i < n8f; i++) {
                            int q8 = qs8[i];
                            if (q8 != 2 && q8 != 5 &&
                                (q8 % 7 == 3 || q8 % 7 == 5 || q8 % 7 == 6)) {
                                condfire = 1;
                                break;
                            }
                        }
                        int isspan = (u == 7);
                        int col = condfire ? 0 : 1;
                        if (isspan) u7fc_iff_span_yes[r7][col]++;
                        else u7fc_iff_fail_yes[r7][col]++;
                        /* the iff: span <=> condfire (within this domain) */
                        if ((isspan ? 1 : 0) != condfire) u7fc_iff_mismatch++;
                    }
                }
                if (x7 % 5 == 0) u7_fivex[r7]++;
            }
            /* v0.15 (E-021): the u = 11 layer census within the (H24) class.
             * fw = 11 <=> the u = 11 span passed (the u = 3 and u = 7 layers
             * failed or were inadmissible for this record); fw > 11 <=> the
             * span failed (admissible). The |D| histograms, the fail D-set
             * masks (residues 1..10), and the sub-fw collision gate. */
            {
                int r11 = p % 11;
                int x11 = (p + 11) / 4;
                u64 M11 = (u64)p * (u64)x11;
                u11_total[r11]++;
                int adm11 = (M11 % 11ULL != 0);
                if (adm11) {
                    u11_adm[r11]++;
                    int mp11 = 0;
                    int pop11 = build_D(p, 11, x11, &mp11);
                    /* the non-QR odd-prime scan (once per record): an odd
                     * prime q | x' with q % 11 outside {1,3,4,5,9} */
                    int c9 = 0;
                    {
                        int q9[40], ee9[40];
                        int n9 = fac(x11, q9, ee9);
                        for (int i = 0; i < n9 && c9 == 0; i++) {
                            int q8 = q9[i];
                            int r8 = q8 % 11;
                            if (q8 != 2 &&
                                (r8 == 2 || r8 == 6 || r8 == 7 ||
                                 r8 == 8 || r8 == 10)) {
                                c9 = 1;
                            }
                        }
                    }
                    /* the odd-part QR purity: every odd prime | x' in QR */
                    int allQR = 1;
                    {
                        int q9[40], ee9[40];
                        int n9b = fac(x11, q9, ee9);
                        for (int i = 0; i < n9b; i++) {
                            int q8 = q9[i];
                            int r8 = q8 % 11;
                            if (q8 != 2 &&
                                !(r8 == 1 || r8 == 3 || r8 == 4 ||
                                  r8 == 5 || r8 == 9)) { allQR = 0; break; }
                        }
                        if (n9b == 0) allQR = 1; /* x' pure-odd-part-1: QR-pure by convention */
                    }
                    /* the non-QR count (with multiplicity) and the first
                     * non-QR prime residue (the census fields) */
                    {
                        int q9[40], ee9[40];
                        int n9c = fac(x11, q9, ee9);
                        int cnt9 = 0, pres9 = 0;
                        for (int i = 0; i < n9c; i++) {
                            int q8 = q9[i];
                            int r8 = q8 % 11;
                            if (q8 == 2) continue;
                            if (!(r8 == 1 || r8 == 3 || r8 == 4 ||
                                  r8 == 5 || r8 == 9)) {
                                cnt9 += ee9[i];     /* with multiplicity */
                                if (pres9 == 0) pres9 = r8;
                            }
                        }
                        { int cap0 = (cnt9 >= 9) ? 9 : cnt9;
                          u11pcnt[r11][cap0][(u == 11) ? 1 : 0]++;
                          if (cnt9 > 0) {
                              int cap1 = (cnt9 >= 11) ? 11 : cnt9;
                              u11pres[r11][pres9][cap1][(u == 11) ? 1 : 0]++;
                          }
                        }
                    }
                    {
                        int v2b = 0;
                        {
                            u64 c7 = (u64)x11;
                            while (c7 % 2ULL == 0 && v2b < 3) { c7 /= 2ULL; v2b++; }
                        }
                        v2b = (v2b >= 3) ? 3 : v2b;
                        u11purity[r11][(allQR ? 1 : 0)][v2b][(u == 11) ? 1 : 0]++;
                    }
                    int isp11 = (u == 11);
                    u11_qr[r11][(c9 * 2) + (isp11 ? 1 : 0)]++;
                    u11_iffc[r11][((mp11 ? 1 : 0) * 2) + (isp11 ? 1 : 0)]++;
                    if ((isp11 ? 1 : 0) != c9) u11_iff_mm++;
                    if (u == 11) {
                        u11_span[r11]++;
                        if (pop11 <= 10) u11_pop_span[r11 * 12 + pop11]++;
                    } else {
                        u11_fail[r11]++;
                        if (pop11 <= 10) u11_pop[r11 * 12 + pop11]++;
                        int mask11 = 0;
                        for (int rr = 1; rr < 11; rr++)
                            if (have[rr]) mask11 |= (1 << rr);
                        u11_fset[r11][mask11]++;
                        /* E-021 census: at u = 7 no fail record ever paired (the
                         * {1,2}/{1,2,4} masks avoid opposite pairs), so the
                         * v0.7-era sub-fw collision gate passed there. At u = 11
                         * collisions DO occur among span-failers - the pair
                         * (d1, d2 in D, d1 + d2 == 0) is a different predicate
                         * from the span criterion (exists d | M, d == -M mod u),
                         * so the collision rate is a RESULT ROW here. */
                        if (mp11) { u11_subfw_coll++; u11_fcoll[r11][mask11]++; }
                    }
                } else u11_inad[r11]++;
            }
        }
        if (par && !non) { p5_onlypar[m5]++; if (in840) intr[i840idx(r840)][0]++; }
        else if (par && non) { p5_both[m5]++; if (in840) intr[i840idx(r840)][1]++; }
        else if (!par && non) {
            p5_onlynon[m5]++;
            if (in840) { intr[i840idx(r840)][2]++; p5_mod840_onlynon[m5]++; }
            if (u < 256) {
                xnop[u][m5]++;
                if (in840) xnop840[u][m5]++;
            }
        } else {
            mismatch++; fprintf(stderr, "NOWITNESS %d\n", p);
        }
        byu_all[u]++;
        if (pg) {
            pigeon++;
            if (in840) by840_pigeon[r840]++;
            byu_pigeon[u]++;
            if (m5 >= 1 && m5 <= 4) re_pig[(u * 4) + (m5 - 1)]++;
        } else {
            delicate++; delicate_total++;
            if (in840) by840_del[r840]++;
            byu_del[u]++;
            if (delicate_total <= 5000 && del)
                fprintf(del,
                    "{\"p\": %d, \"u\": %d, \"D\": %d, \"phi\": %d, "
                    "\"margin\": %d, \"pair\": [%d, %d]}\n",
                    p, u, pop, ph, margin, mp, u - mp);
            /* v0.8 R8: the per-slice reachability counters + the delicate
             * rescue scan (H-3 at the universal-cardinality target's
             * existential form, u' <= 255, admissible, u' != fw; note the
             * sub-fw pigeon sites are excluded by first()'s span-fail
             * theorem check above). */
            int d1s8 = mp, d2s8 = (u - mp) % u;
            (void)d2s8;
            int cls8 = (d1s8 == 1) ? 0 : (4 * d1s8 <= u ? 1 : (2 * d1s8 <= u ? 2 : 3));
            int si8 = (m5 >= 1 && m5 <= 4) ? ((u * 4) + (m5 - 1)) : -1;
            if (si8 >= 0) {
                re_total[si8]++;
                re_del[si8]++;
                if (cls8 == 0) re_dunit[si8]++;
                else if (cls8 == 1) re_dsmall[si8]++;
                else re_dlarge[si8]++;
            }
            int r_pig = 0, r_coll = 0;
            for (int u2 = u + 4; u2 <= 255; u2 += 4) {
                int x2 = (p + u2) / 4;
                u64 M2 = (u64)p * (u64)x2;
                if (gcd_u64(M2, (u64)u2) != 1) continue;
                int mp2 = 0;
                int pop2 = build_D(p, u2, x2, &mp2);
                int pig2 = (2 * pop2 > phi_small(u2));
                if (pig2) { pig_u2[u2]++; if (!r_pig) r_pig = u2; if (!mp2) delres_pignocoll++; }
                if (mp2) { coll_u2[u2]++; collfw_u2[u2] += (u2 == u) ? 1 : 0; if (!r_coll) r_coll = u2; }
            }
            delres_total++;
            if (r_pig) { delres_pig++; if (si8 >= 0) re_rpig[si8]++; }
            else {
                delres_nopig++;
                if (si8 >= 0) re_rnop[si8]++;
                unr_byu[u]++;
                if (unr_tot < 400) {
                    unr_p[unr_tot] = p; unr_u[unr_tot] = u; unr_cls[unr_tot] = cls8;
                }
                unr_tot++;
            }
            if (r_coll) delres_coll++;
            if (rfr) fprintf(rfr,
                "{\"p\": %d, \"u\": %d, \"D\": %d, \"phi\": %d, \"margin\": %d, \"cls\": %d, \"rescue_pig\": %d, \"rescue_coll\": %d}\n",
                p, u, pop, ph, margin, cls8, r_pig, r_coll);
        }
    }
    if (del) fclose(del);
    if (rfr) fclose(rfr);

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
    printf("DELICATE_SHAPE total=%lld with_d1=1 %d unit-pair=%d d1<=half=%lld d1>half=%lld square-root-pair=%lld\n",
           (long long)del_total, (int)del_d1one, (int)del_unitpair,
           (long long)del_small, (long long)del_large, (long long)del_halfsquare);
    printf("DELICATE_BUCKET d1=1 %ld d1<=u/4 %lld d1<=u/2 %lld d1>u/2 %lld\n",
           (long)del_d1one, (long long)del_bucket[1], (long long)del_bucket[2],
           (long long)del_bucket[3]);
    for (int uu = 0; uu < 256; uu++) {
        for (int g = 1; g <= 4; g++) {
            if (xdel[uu][g] > 0)
                printf("XDEL %d %d count=%lld\n", uu, g, (long long)xdel[uu][g]);
        }
    }
    for (int uu = 0; uu < 256; uu++) {
        for (int mb = 0; mb < 3; mb++) {
            int si = (uu * 4) + mb;
            if (si < 0 || si >= 1024) continue;
            if (slice_seen[si] == 0) continue;
            int m5v = (mb == 0) ? 1 : (mb == 1 ? 3 : 4);
            printf("XSHAPE u=%d m5=%d n=%lld parfree=%lld parp=%lld nonfree=%lld nonp=%lld fivex=%lld\n",
                   uu, m5v, (long long)slice_seen[si],
                   (long long)shape_par_free[si], (long long)shape_par_p[si],
                   (long long)shape_non_free[si], (long long)shape_non_p[si],
                   (long long)slice_fivex[si]);
        }
    }
    printf("G3U7 total=%lld fivex=%lld notfivex=%lld\n",
           (long long)g3u7, (long long)g3u7_fivex, (long long)g3u7_notfivex);
    printf("G3U7E5 depth0=%lld depth1=%lld depth2plus=%lld\n",
           (long long)g3u7_E5[0], (long long)g3u7_E5[1],
           (long long)g3u7_E5[2] + (long long)g3u7_E5[3]);
    printf("G3U7PAR shape: p-containing=%lld p-free=%lld v5[0]=%lld v5[1]=%lld v5[2]=%lld v5cap=%lld\n",
           (long long)w7par_p, (long long)w7par_unit,
           (long long)w7par_v5[0], (long long)w7par_v5[1],
           (long long)w7par_v5[2], (long long)w7par_v5[3]);
    printf("G3U7NON shape: p-containing=%lld p-free=%lld v5[0]=%lld v5[1]=%lld v5[2]=%lld v5cap=%lld over5=%lld\n",
           (long long)w7non_p, (long long)w7non_unit,
           (long long)w7non_v5[0], (long long)w7non_v5[1],
           (long long)w7non_v5[2], (long long)w7non_v5[3], (long long)w7non_over5);
    printf("U11G4 total=%lld fivex=%lld notfivex=%lld\n",
           (long long)u11_g4, (long long)u11_g4_fivex, (long long)u11_g4_notfivex);
    printf("U11G4SHAPE p-containing=%lld p-free=%lld v5[0]=%lld v5[1]=%lld v5[2]=%lld v5cap=%lld\n",
           (long long)sh_p, (long long)sh_unit,
           (long long)sh_v5[0], (long long)sh_v5[1], (long long)sh_v5[2], (long long)sh_v5[3]);
    for (int uu = 0; uu < 256; uu++) {
        for (int g = 1; g <= 4; g++) {
            if (xall[uu][g] > 0)
                printf("XULAYER %d %d all=%lld nop=%lld rate=%lld\n", uu, g,
                       (long long)xall[uu][g], (long long)xnop[uu][g],
                       (long long)(10000 * xnop[uu][g] / xall[uu][g]));
            if (xall840[uu][g] > 0)
                printf("XULAYER840 %d %d all=%lld nop=%lld rate=%lld\n", uu, g,
                       (long long)xall840[uu][g], (long long)xnop840[uu][g],
                       (long long)(10000 * xnop840[uu][g] / xall840[uu][g]));
        }
    }
    /* v0.8 R8 (E-011) rows: the per-layer reachability table, the delicate
     * rescue census, and the sub-fw theorem-consistency counters. */
    for (int si = 0; si < 1024; si++) {
        if (re_pig[si] + re_del[si] == 0) continue;
        int uu = si / 4, g = (si % 4) + 1;
        printf("XREACH u=%d m5=%d total=%lld pigeon=%lld del=%lld delunit=%lld dsmall=%lld dlarge=%lld rescuepig=%lld rescuenopig=%lld\n",
               uu, g,
               (long long)re_pig[si] + (long long)re_del[si],
               (long long)re_pig[si], (long long)re_del[si],
               (long long)re_dunit[si], (long long)re_dsmall[si],
               (long long)re_dlarge[si],
               (long long)re_rpig[si], (long long)re_rnop[si]);
    }
    printf("RESCUE8 delicate=%lld rescued_pigeon=%lld rescued_coll=%lld no_pigeon_anywhere=%lld\n",
           (long long)delres_total, (long long)delres_pig,
           (long long)delres_coll, (long long)delres_nopig);
    printf("RESCUE8CHECK pig_no_coll=%lld (must be 0: R5)\n",
           (long long)delres_pignocoll);
    for (int u2 = 3; u2 <= 255; u2 += 4)
        if (pig_u2[u2] || coll_u2[u2])
            printf("RESCUE8U u=%d pig=%lld coll=%lld collfw=%lld\n", u2,
                   (long long)pig_u2[u2], (long long)coll_u2[u2],
                   (long long)collfw_u2[u2]);
    printf("SUBFW checks=%lld collision=%lld pigeon=%lld\n",
           (long long)subfw_checks, (long long)subfw_coll,
           (long long)subfw_pigeon);
    for (int uu = 3; uu <= 255; uu += 4)
        if (unr_byu[uu])
            printf("RESCUE8HARDBYU u=%d n=%lld\n", uu, (long long)unr_byu[uu]);
    if (unr_tot <= 400) {
        for (int i2 = 0; i2 < (int)unr_tot; i2++)
            printf("RESCUE8HARD p=%d u=%d cls=%d\n", unr_p[i2], unr_u[i2], unr_cls[i2]);
    } else {
        printf("RESCUE8HARD first400 of %lld\n", (long long)unr_tot);
        for (int i2 = 0; i2 < 400; i2++)
            printf("RESCUE8HARD p=%d u=%d cls=%d\n", unr_p[i2], unr_u[i2], unr_cls[i2]);
    }
    for (int r7 = 1; r7 <= 6; r7++)
        if (u7_total[r7])
            printf("U7 r7=%d total=%lld adm=%lld span=%lld fail=%lld inad=%lld fivex=%lld\n",
                   r7,
                   (long long)u7_total[r7], (long long)u7_adm[r7],
                   (long long)u7_span[r7], (long long)u7_fail[r7],
                   (long long)u7_inad[r7], (long long)u7_fivex[r7]);
    for (int r7 = 1; r7 <= 6; r7++)
        if (u7_n7[r7])
            printf("U7WIT r7=%d n7=%lld wit_ok=%lld\n", r7,
                   (long long)u7_n7[r7], (long long)u7_tp[r7]);
    for (int r7 = 1; r7 <= 6; r7++)
        if (u7_fail[r7]) {
            printf("U7FAILPOP r7=%d", r7);
            for (int k2 = 0; k2 < 7; k2++)
                printf(" %lld", (long long)u7_pop[r7 * 8 + k2]);
            printf("\n");
        }
    for (int r7 = 1; r7 <= 6; r7++) {
        if (r7 != 1 && r7 != 2 && r7 != 4) continue;
        if (u7fc_span_n[r7] + u7fc_fail_n[r7] == 0) continue;
        printf("U7FC r7=%d span=%lld fail=%lld spanA=%lld spanB=%lld spanC=%lld\n",
               r7,
               (long long)u7fc_span_n[r7], (long long)u7fc_fail_n[r7],
               (long long)u7fc_span[r7][0], (long long)u7fc_span[r7][1],
               (long long)u7fc_span[r7][2]);
        printf("U7FCSPANV5 r7=%d depth0=%lld depth1=%lld depth2=%lld depth3=%lld d125=%lld\n",
               r7,
               (long long)u7fc_sv5[r7][0], (long long)u7fc_sv5[r7][1],
               (long long)u7fc_sv5[r7][2], (long long)u7fc_sv5[r7][3],
               (long long)u7fc_s125[r7]);
        printf("U7FAILPROFILE r7=%d v2_1=%lld v2_2=%lld v2_3=%lld v5_0=%lld v5_1=%lld v5_2=%lld in840=%lld non840=%lld\n",
               r7,
               (long long)u7fc_v2[r7][0],
               (long long)u7fc_v2[r7][1],
               (long long)u7fc_v2[r7][2],
               (long long)u7fc_v5[r7][0],
               (long long)u7fc_v5[r7][1],
               (long long)u7fc_v5[r7][2],
               (long long)u7fc_in840[r7][1], (long long)u7fc_in840[r7][0]);
    }
    printf("U7CHECK subfw_coll=%lld (must be 0)\n", (long long)u7_subfw_coll);
    for (int r7 = 1; r7 <= 6; r7++) {
        if (r7 != 1 && r7 != 2 && r7 != 4) continue;
        if (u7fc_d0_pure2[r7] + u7fc_d0_mixed[r7] == 0) continue;
        printf("U7D0MECH r7=%d pure2power=%lld mixed=%lld pigeon=%lld\n", r7,
               (long long)u7fc_d0_pure2[r7], (long long)u7fc_d0_mixed[r7],
               (long long)u7fc_span_pigeon[r7]);
        printf("U7D0POP r7=%d", r7);
        for (int k3 = 0; k3 < 7; k3++)
            printf(" %lld", (long long)u7fc_d0_pop[r7][k3]);
        printf("\n");
        printf("U7FAILB840 r7=%d c1=%lld c121=%lld c169=%lld c289=%lld c361=%lld c529=%lld\n",
               r7,
               (long long)u7fc_fail_b840[r7][0], (long long)u7fc_fail_b840[r7][1],
               (long long)u7fc_fail_b840[r7][2], (long long)u7fc_fail_b840[r7][3],
               (long long)u7fc_fail_b840[r7][4], (long long)u7fc_fail_b840[r7][5]);
    }
    for (int r7 = 1; r7 <= 6; r7++) {
        if (r7 != 2 && r7 != 4) continue;
        if (u7fc_gen[r7][0] + u7fc_gen[r7][1] == 0) continue;
        printf("U7D6GEN r7=%d gen3=%lld gen5=%lld gen3_d125=%lld gen5_d125=%lld\n",
               r7,
               (long long)u7fc_gen[r7][0], (long long)u7fc_gen[r7][1],
               (long long)u7fc_gen_125[r7][0], (long long)u7fc_gen_125[r7][1]);
    }
    for (int r7 = 1; r7 <= 6; r7++) {
        if (r7 != 1 && r7 != 2 && r7 != 4) continue;
        for (int m2 = 0; m2 < 64; m2++)
            if (u7fc_fset[r7][m2] > 0)
                printf("U7FAILSET r7=%d mask=%d n=%lld\n", r7, m2,
                       (long long)u7fc_fset[r7][m2]);
        for (int m2 = 0; m2 < 64; m2++)
            for (int i6 = 0; i6 < 4; i6++)
                if (u7fc_fsetv2[r7][(m2 * 4) + i6] > 0)
                    printf("U7FAILSETVM r7=%d mask=%d v2b=%d n=%lld\n", r7,
                           m2, i6, (long long)u7fc_fsetv2[r7][(m2 * 4) + i6]);
    }
    for (int r7 = 1; r7 <= 6; r7++) {
        if (r7 != 1 && r7 != 2 && r7 != 4) continue;
        printf("U7IFF r7=%d span_cond=%lld span_notcond=%lld fail_cond=%lld fail_notcond=%lld\n",
               r7,
               (long long)u7fc_iff_span_yes[r7][0],
               (long long)u7fc_iff_span_yes[r7][1],
               (long long)u7fc_iff_fail_yes[r7][0],
               (long long)u7fc_iff_fail_yes[r7][1]);
    }
    printf("U7IFFCHECK mismatch=%lld (must be 0; with the q residue in {3,5,6})\n",
           (long long)u7fc_iff_mismatch);
    printf("U7FCCHECK span_miss=%lld (must be 0)\n", (long long)u7fc_span_miss);
    printf("U11CHECK subfw_coll=%lld (must be 0)\n", (long long)u11_subfw_coll);
    for (int r11 = 1; r11 <= 10; r11++) {
        if (u11_total[r11] == 0) continue;
        printf("U11CLASS r11=%d total=%lld adm=%lld span=%lld fail=%lld inad=%lld\n",
               r11,
               (long long)u11_total[r11], (long long)u11_adm[r11],
               (long long)u11_span[r11], (long long)u11_fail[r11],
               (long long)u11_inad[r11]);
        printf("U11POP r11=%d", r11);
        for (int k4 = 0; k4 <= 10; k4++)
            printf(" %lld", (long long)u11_pop[r11 * 12 + k4]);
        printf("\n");
        printf("U11POPSPAN r11=%d", r11);
        for (int k5 = 0; k5 <= 10; k5++)
            printf(" %lld", (long long)u11_pop_span[r11 * 12 + k5]);
        printf("\n");
        for (int m3 = 0; m3 < 2048; m3++)
            if (u11_fset[r11][m3] > 0)
                printf("U11FAILSET r11=%d mask=%d n=%lld\n", r11, m3,
                       (long long)u11_fset[r11][m3]);
        for (int m3 = 0; m3 < 2048; m3++)
            if (u11_fcoll[r11][m3] > 0)
                printf("U11COLL r11=%d mask=%d n=%lld\n", r11, m3,
                       (long long)u11_fcoll[r11][m3]);
    }
    printf("U11COLLCHECK collisions=%lld among failers (census row, not an error gate)\n",
           (long long)u11_subfw_coll);
    for (int r11 = 1; r11 <= 10; r11++) {
        if (u11_total[r11] == 0) continue;
        /* the u11_qr[c9 * 2 + span] flat map:
         * [0] = cond-false fail, [1] = cond-false span,
         * [2] = cond-true fail, [3] = cond-true span */
        printf("U11IFF r11=%d cond_span=%lld cond_fail=%lld nocond_span=%lld nocond_fail=%lld\n",
               r11,
               (long long)u11_qr[r11][3], (long long)u11_qr[r11][2],
               (long long)u11_qr[r11][1], (long long)u11_qr[r11][0]);
        /* the u11_iffc[coll * 2 + span] flat map:
         * [0] = no-collision fail, [1] = no-collision span,
         * [2] = collision fail,  [3] = collision span */
        printf("U11COLLCELLS r11=%d coll_span=%lld coll_fail=%lld nocoll_span=%lld nocoll_fail=%lld\n",
               r11,
               (long long)u11_iffc[r11][3], (long long)u11_iffc[r11][2],
               (long long)u11_iffc[r11][1], (long long)u11_iffc[r11][0]);
    }
    printf("U11IFFCHECK mismatch=%lld (soft census row; the non-QR-odd-prime condition)\n",
           (long long)u11_iff_mm);
    for (int r11 = 1; r11 <= 10; r11++) {
        if (u11_total[r11] == 0) continue;
        for (int aq = 0; aq < 2; aq++)
            for (int vb = 0; vb < 4; vb++)
                if (u11purity[r11][aq][vb][0] + u11purity[r11][aq][vb][1] > 0)
                    printf("U11QRBKT r11=%d allQR=%d v2b=%d span=%lld fail=%lld\n",
                           r11, aq, vb,
                           (long long)u11purity[r11][aq][vb][1],
                           (long long)u11purity[r11][aq][vb][0]);
        /* the impure-cell decomposition: the count histogram (capped 9)
         * and the first-non-QR-prime-residue x count cells (capped 11) */
        for (int c10 = 0; c10 <= 9; c10++)
            if (u11pcnt[r11][c10][0] + u11pcnt[r11][c10][1] > 0)
                printf("U11PCNT r11=%d cnt=%d span=%lld fail=%lld\n",
                       r11, c10,
                       (long long)u11pcnt[r11][c10][1],
                       (long long)u11pcnt[r11][c10][0]);
        for (int pr = 0; pr < 11; pr++)
            for (int c11 = 0; c11 <= 11; c11++)
                if (u11pres[r11][pr][c11][0] + u11pres[r11][pr][c11][1] > 0)
                    printf("U11PRES r11=%d pres=%d cnt=%d span=%lld fail=%lld\n",
                           r11, pr, c11,
                           (long long)u11pres[r11][pr][c11][1],
                           (long long)u11pres[r11][pr][c11][0]);
    }
    return (mismatch || subfw_coll || subfw_pigeon || delres_pignocoll
            || u7_subfw_coll || u7fc_span_miss || u7fc_iff_mismatch) ? 1 : 0;
}
