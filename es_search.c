
#include <stdint.h>
#include <math.h>

static unsigned __int128 isqrt128_fast(unsigned __int128 n) {
    if (n == 0) return 0;
    if (n <= (unsigned __int128)UINT64_MAX) {
        return (unsigned __int128)((uint64_t)sqrtl((long double)n));
    }
    int bits = 128 - __builtin_clzll((unsigned long long)(n >> 64)) - 64;
    if (bits < 0) bits = 0;
    unsigned __int128 shift = (unsigned __int128)1 << bits;
    long double approx = sqrtl((long double)(n >> bits));
    unsigned __int128 guess = (unsigned __int128)(approx * sqrtl((long double)shift));
    for (int i = 0; i < 6; i++) {
        if (guess == 0) guess = 1;
        unsigned __int128 q = n / guess;
        unsigned __int128 new_guess = (guess + q) >> 1;
        if (new_guess == guess) break;
        guess = new_guess;
    }
    while (guess * guess > n) guess--;
    while ((guess + 1) * (guess + 1) <= n) guess++;
    return guess;
}

/*
 * Search for t in [threshold, threshold + max_t) such that:
 *   F = t*t*A_sq - two_nx*t is a perfect square = s*s
 *   AND (2*n*t + s*A) % (2*A_sq) == 0  (ensures y integer)
 *   AND (2*n*t - s*A) % (2*A_sq) == 0  (ensures z integer)
 *   AND 2*n*t > s*A  (ensures z > 0)
 * Returns 1 if found, sets *out_t and *out_s. 0 if not found.
 */
int search_A_fast(long long n, long long A, long long max_t,
                  long long *out_t, long long *out_s) {
    long long x = (n + A) / 4;
    long long two_nx = 2 * n * x;
    long long A_sq = A * A;
    long long two_A_sq = 2 * A_sq;
    long long threshold = (two_nx + A_sq - 1) / A_sq;
    if (threshold < 1) threshold = 1;
    
    for (long long t = threshold; t < threshold + max_t; t++) {
        __int128 F = (__int128)t * t * A_sq - (__int128)two_nx * t;
        if (F < 0) continue;
        unsigned __int128 uF = (unsigned __int128)F;
        unsigned __int128 s128 = isqrt128_fast(uF);
        if (s128 * s128 != uF) continue;
        
        long long s = (long long)s128;
        
        /* Divisibility checks */
        long long num_y = 2 * n * t + s * A;
        long long num_z = 2 * n * t - s * A;
        if (num_y <= 0 || num_z <= 0) continue;
        if (num_y % two_A_sq != 0) continue;
        if (num_z % two_A_sq != 0) continue;
        
        *out_t = t;
        *out_s = s;
        return 1;
    }
    return 0;
}
