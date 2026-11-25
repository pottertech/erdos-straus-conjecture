# DATA_MANIFEST.md — Paper 2 (frozen research datasets, R1)

Every inventoried file is hash-pinned below. All but the three engine
sources are committed repo artifacts; the engines
(`sweep_exact/collision_margin_engine.c`,
`research/residual_primes/analysis/mod5_separation_v02/collision_margin_engine_v02.c`,
`research/residual_primes/analysis/layer_mod5_v03/collision_margin_engine_v03.c`)
are pinned from the author's verified local copies and are reported
MISSING by the verifier until the author commits them (the .gitignore
exceptions for all three paths are in place). With the engines
outstanding, verification stands at 22 of 25.
tests/verify_manifest.py recomputes these digests and byte sizes and
fails on any mismatch or unparsed row; run it before any analysis
reuses a dataset. Provenance and
re-production commands live in Paper 1 Appendix A and
verification_nano/NANODA_RUN.md; the standing determination applies -
these datasets carry no universal claims.

## Verified computational datasets (33 artifacts)

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
| Nonparametric JSONL records | 317,569 | nonparametric_1e7_1e9.jsonl (byte-verified at v1.6, zero failures; despite the extension the file is a single top-level JSON array, not line-delimited, and its records key the prime as `n`, not `p`) |
| Certificate-layer records (to 10^7) | 166,011 | layer4_certificates.jsonl (byte-verified at v1.6, zero failures) |
| Pigeonhole-conclusive / delicate | 3,177,642 / 16,589 | analysis/collision_v01/full_run.txt (MISMATCH 0) |
| Mod-5 nonparametric-only rates (E-002) | 4.09% / 1.50%, ratio 2.73x | analysis/mod5_separation_v02/full_run.txt |

| `ErdosStrausConjecture/ResidualPrimes/CollisionReachability.lean` | `e6b127aef7c78504b03fd4aa5e9c1cca4886704195cef796d52f1243c2790741` | 9564 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_collision.txt` | `95583aad2f69fa79131e9e6bb7a4df04675f5241ddac698ad388365cb742cee6` | 733 |
| `research/residual_primes/ErdosStrausConjecture_src/lake_build_r4.log` | `f625222c55621e422d1d682b815232cc97edc5cb1b23430648ff3620129b3208` | 314 |

| `research/residual_primes/analysis/layer_mod5_v03/collision_margin_engine_v03.c` | `1b1befe9ad92b074abaf1b3228dd756fcb7c696c082f735c728a107a73831cf1` | 16213 |
| `research/residual_primes/analysis/layer_mod5_v03/r3_full_run.txt` | `ed5583954dbd37bc0b92889f47364970c2cc9a2bff2b3b13cfdfeedd6a6eeff9` | 5209 |
| `research/residual_primes/analysis/layer_mod5_v03/v03_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |

| `ErdosStrausConjecture/ResidualPrimes/U11Exact.lean` | `4f07c14687e958990796ae8241d8f111a5b45516154a7ac7a1f681c5ef57e063` | 2040 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u11.txt` | `15bbea1fd2ed79e444bf75d3a97bb119b70bf4d271769c359057a8cd8f9a09a0` | 169 |
| `research/residual_primes/analysis/u11_exact_v04/collision_margin_engine_v04.c` | `1c9d060e96d7d0a2944e34d70b27439cc74b98bd675e543f5faa03dbd1d2f8e2` | 19359 |
| `research/residual_primes/analysis/u11_exact_v04/full_run.txt` | `ddaa23c93f9857cbee084ef1ab8068ecd25c2bdd68176017b11b7b9206c46408` | 5332 |

| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u11.log` | `c4333958400fad4545c10bfe794c3d655f79dcc371033eb73dc3ca7d43e9c0a3` | 116 |

| `ErdosStrausConjecture/ResidualPrimes/WindowForm.lean` | `364910f98645cbb4fc41c71169886685bda119e69ca7660198352379eded0f5b` | 3299 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_window.txt` | `f502a11a8b6bf19cce3e93ce02424a55a081a1c24d14eb6b4878b803491a557a` | 174 |
| `research/residual_primes/ErdosStrausConjecture_src/WindowForm.lean` | `364910f98645cbb4fc41c71169886685bda119e69ca7660198352379eded0f5b` | 3299 |

## Frozen-source statement

The datasets above are frozen as hash-pinned here. The pinned bytes are
identical at Paper-1 tags paper-v1.8 and paper-v1.12 (spot-verified
2026-11-24 against the manifest digests), and Paper 1's current release
line is paper-v1.12, as MANUSCRIPT.md and THEOREM_REGISTRY.md state;
the hashes in this manifest, not a tag name, are the freeze. Paper 2
adds research engines beside them. Any change to a hash above is a
data event and requires a CHANGELOG entry.
