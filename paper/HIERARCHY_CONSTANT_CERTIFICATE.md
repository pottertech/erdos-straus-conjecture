# Fixed-Cofactor Hierarchy Constant Certificate

This note records a finite, reproducible numerical lower bound derived from the proved fixed-cofactor hierarchy. It is **not** an additional analytic assumption.

Using every prime cofactor
\[
s\le10^6,\qquad s\equiv3\pmod8,
\]
the exact finite family count contains
\[
\boxed{19,652}
\]
canonical cofactors and has partial coefficient
\[
\boxed{
\sum_{\substack{s\le10^6\ \mathrm{prime}\\s\equiv3(8)}}
\frac{4}{s\varphi(2(s+1))}
=0.0676813490183\ldots .
}
\]

Adding the already-proved prime/`3q` base coefficient
\[
\frac83
\]
and the four explicitly disjoint `7 (mod 8)` fixed-cofactor families
\[
\frac17+\frac1{184}+\frac1{248}+\frac1{987},
\]
gives the fully finite certified bound
\[
\boxed{
\liminf_{X\to\infty}
\frac{N_\infty(X)\log X}{X}
\ge
2.88768537044\ldots .
}
\]

The proof of the lower bound uses only fixed finite subfamilies before taking `X -> infinity`; therefore no PNT uniformity in a growing cofactor is assumed. Positivity of the remaining hierarchy terms means the full series gives a strictly larger coefficient.

The accompanying script `hierarchy_constant_certificate.py` reproduces the finite sum from scratch.