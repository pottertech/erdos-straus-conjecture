# DATA_MANIFEST.md — Paper 2 (frozen research datasets, R1)

Every inventoried file is a committed repo artifact, hash-pinned below.
tests/verify_manifest.py recomputes these digests and fails on any
mismatch; run it before any analysis reuses a dataset. Provenance and
re-production commands live in Paper 1 Appendix A and
verification_nano/NANODA_RUN.md; the standing determination applies -
these datasets carry no universal claims.

## Verified computational datasets (19 artifacts)

| Path | SHA-256 | Bytes |
| --- | --- | --- |
| `results/layer4_certificates.jsonl` | `e864053e4e193fb8f781994994a1fc885c5c9e5fd02362f2018dceca3e50634f` | 28659492 |
| `sweep_exact/nonparametric_1e7_1e9.jsonl` | `f235af39a985de2e1ba14e9dae3dbaa112f83b20378b462881daf196b37a435d` | 53379971 |
| `sweep_exact/verification_10M_1B_exact_rerun.json` | `d9f7720bce9627c8fe126aebc5abfdcffa826ddf77dbcce517716555f242e2ea` | 1065 |
| `sweep_exact/verification_100M_1B_exact_rerun.json` | `b2fcbca453b767aac2ba956091f0de08de254e08a6f4b63263fd381cedec9867` | 1065 |
| `sweep_exact/verification_10M_100M_exact_rerun.json` | `c0ea3d42d3ab569e806ecd51dddc2d6156910a8c4b4020adaa21ed3cdccb0fa0` | 994 |
| `sweep_exact/third_party_independent_sweep.cpp` | `4ffeea9f144ef4fd16656dad9a016c7eee0e27b296b9a2c776f247427bddc70c` | 2125 |
| `sweep_exact/third_party_independent_mod840.cpp` | `3b5fafb47750c10fa8c19c7dc950be01b6a3c8c87043df039c523dace4163d40` | 3578 |
| `sweep_exact/third_party_mod840_output.txt` | `6b419d9167e720414d8047ca0e7fc21ce9f401c1abe7c836c7cee89ea37134da` | 834 |
| `sweep_exact/collision_margin_engine.c` | `cfcef28b6350369143e027e1e0e49aa1d425618c3ea277f1b94d22fc30cba0d2` | 10814 |
| `analysis/collision_v01/full_run.txt` | `249c9793747c6db2a4cbe3406c5ba0c7f5a900a4ff444a891fe7d5cab0882fbd` | 1506 |
| `analysis/collision_v01/full_run_stderr.txt` | `48d81fe19e47629e161deee5a78cbdef4990d9f77e5c71746f3c2a643ba98331` | 37 |
| `analysis/collision_v01/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `analysis/collision_v01/delicate_sample.jsonl` | `5b5bcfaa985636ed6185a796c42575c9a0ccf42d8a415973de377545e10a3bc4` | 378596 |
| `verification_nano/verification_provenance.json` | `779e80978ce0f1ee2da8b2c1e2348bf6721ffdb75a4586d1c0681166bc93c432` | 937 |
| `verification_nano/SHA256SUMS` | `4e10b9d5628cdb8e82dc3979f74c65e3c2d7f3f6cc1e105e251a7d6f08148ce5` | 1156 |
| `research/residual_primes/analysis/mod5_separation_v02/collision_margin_engine_v02.c` | `16e148fc363378429727cd0b30c994879c138a5e6c6b035a1afd84d8eb87c650` | 15183 |
| `research/residual_primes/analysis/mod5_separation_v02/full_run.txt` | `220e507ad40dd5f53746191fd7d3df4c33c68437d34cdf4dc4d752298016c02f` | 2249 |
| `research/residual_primes/analysis/mod5_separation_v02/full_run_stderr.txt` | `48d81fe19e47629e161deee5a78cbdef4990d9f77e5c71746f3c2a643ba98331` | 37 |
| `research/residual_primes/analysis/mod5_separation_v02/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |

## Population cross-reference (verified figures named with their bound)

| Population | Size | Source |
| --- | --- | --- |
| Hard-case sweep [10^7, 10^9) | 3,194,231 | verification_10M_1B_exact_rerun.json — zero failures at the engine ceiling |
| (H24) subclass | 2,364,031 | h24_hard_cases fields across the sweep artifacts |
| Mod-840 classes | 795,913 total | third_party_mod840_output.txt (independently re-executed, entry-for-entry) |
| Mod-840 nonparametric-only cohort | 22,222 | third_party_mod840_output.txt RES rows (sum verified) |
| Nonparametric JSONL records | 317,569 | nonparametric_1e7_1e9.jsonl (byte-verified at v1.6, zero failures) |
| Certificate-layer records (to 10^7) | 166,011 | layer4_certificates.jsonl (byte-verified at v1.6, zero failures) |
| Pigeonhole-conclusive / delicate | 3,177,642 / 16,589 | analysis/collision_v01/full_run.txt (MISMATCH 0) |
| Mod-5 nonparametric-only rates (E-002) | 4.09% / 1.50%, ratio 2.73x | analysis/mod5_separation_v02/full_run.txt |

## Frozen-source statement

The proof sources and engines for these datasets are frozen at the Paper-1
lineage (paper-v1.8 proof sources; Paper 2 adds research engines beside
them). Any change to a hash above is a data event and requires a CHANGELOG
entry.
