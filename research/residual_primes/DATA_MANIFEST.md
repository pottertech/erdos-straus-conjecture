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

## Verified computational datasets (43 artifacts)

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

| `ErdosStrausConjecture/ResidualPrimes/U11Exact.lean` | `31040ac9919e71b01929a5d20aa49ba0a2291a26d41925843a7ac88daaa18d45` | 3221 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u11.txt` | `15bbea1fd2ed79e444bf75d3a97bb119b70bf4d271769c359057a8cd8f9a09a0` | 169 |
| `research/residual_primes/analysis/u11_exact_v04/collision_margin_engine_v04.c` | `1c9d060e96d7d0a2944e34d70b27439cc74b98bd675e543f5faa03dbd1d2f8e2` | 19359 |
| `research/residual_primes/analysis/u11_exact_v04/full_run.txt` | `ddaa23c93f9857cbee084ef1ab8068ecd25c2bdd68176017b11b7b9206c46408` | 5332 |

| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u11.log` | `c4333958400fad4545c10bfe794c3d655f79dcc371033eb73dc3ca7d43e9c0a3` | 116 |

| `ErdosStrausConjecture/ResidualPrimes/WindowForm.lean` | `364910f98645cbb4fc41c71169886685bda119e69ca7660198352379eded0f5b` | 3299 |
| `ErdosStrausConjecture/ResidualPrimes/U3Boundary.lean` | `2957eea51c2d58c6d2e3e9c782316217ca5c855e697fa7d31546170f6f8eb4db` | 9731 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u3.txt` | `9c39fa8b70002c11f7c6856f7e73f1ba367fc17bbac53c2ee195f4dfc4f8f99f` | 497 |
| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u3.log` | `0ffe315b72a359070cb726151f95c13195006b622b73178b6486d98c8e9d1463` | 1773 |
| `research/residual_primes/analysis/u7_layer_v09/collision_margin_engine_v09.c` | `aa7c5f515e0ca3ca6f3d9aab961e204396fdb014f483aaa8193dd78207235003` | 38904 |
| `research/residual_primes/analysis/u7_layer_v09/full_run.txt` | `75dd93e16147cbe4e6accf0f43cac6f1ebba66c1e1c0c861406b7b98ae3e7e68` | 16777 |
| `research/residual_primes/analysis/u7_layer_v09/full_run_stderr.txt` | `d28111cfdd34b41ae933796c351a8c29e371d372b361a1641998373f15ce89c3` | 78 |
| `research/residual_primes/analysis/u7_layer_v09/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `ErdosStrausConjecture/ResidualPrimes/U7Layer.lean` | `13ca88a3248322047e5424b6bbc911144ab6f2593b13f0e61a35e8bd364629cb` | 32292 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u7.txt` | `2a8c12daa0c8ed631656ed46fc47f7a67cd3c662a4f1423482b944247a0e4c0d` | 1185 |
| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u7.log` | `1fd21a9ef78756ec3d30e645db643e0fd1ce67212c661e216482f57f1e5f10f0` | 3044 |
| `research/residual_primes/analysis/crossval_r9/r9_crossval.py` | `79692a2192216ca42d9602d41b1cdd62965604b075a1a8d8ca2b9bd1e488dbaa` | 8218 |
| `research/residual_primes/analysis/crossval_r9/crossval_run.txt` | `be33f2666c1197740c94297f74d8ed68d59f8d2ddede63c69f09785ef5b94c56` | 470 |
| `research/residual_primes/analysis/u11_class_v015/collision_margin_engine_v015.c` | `0b547b0964bc91db87fad1cb6e3b6a3143cdeeeb581d5c6928c73d220a096e2d` | 57095 |
| `research/residual_primes/analysis/u11_class_v015/full_run.txt` | `1e5302670b17c50c63dd53c1f50be64212b3ed27562fcfe0e60fa91de749abe3` | 23323 |
| `research/residual_primes/analysis/u11_class_v015/full_run_stderr.txt` | `48dbf0e1fd2a0d99cadfd793475774b3d3cae0132eb48173b7b5921923bbd158` | 78 |
| `research/residual_primes/analysis/u11_class_v015/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u11_iff_v016/collision_margin_engine_v016.c` | `57209d4e6d3a6f72aee0eb5bffd33cc843e13f4d1ae4f52b43bf77153b65c06e` | 59844 |
| `research/residual_primes/analysis/u11_iff_v016/full_run.txt` | `c15921f825ef5e10ff3f430212213617254491683aca768705ee617a35fbd01b` | 24848 |
| `research/residual_primes/analysis/u11_iff_v016/full_run_stderr.txt` | `950791e4815897cf2fe4eb9c2723a4cd011e464ec13fda88744eb1babbca78be` | 78 |
| `research/residual_primes/analysis/u11_iff_v016/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u11_split_v017/collision_margin_engine_v017.c` | `dd7a8a022ebeff18a6dcb01eddb6c153f656da4c38c663b2387a92921a50f171` | 61733 |
| `research/residual_primes/analysis/u11_split_v017/full_run.txt` | `fe206cd7a3e1e958516754a20296d9794e34d51f7b2825f777f997b6de4baa3f` | 25557 |
| `research/residual_primes/analysis/u11_split_v017/full_run_stderr.txt` | `77ca7bafccbb2cc91a2d3b8708cc3c26dbb3602f6288b844aca98b4931d9865f` | 78 |
| `research/residual_primes/analysis/u11_split_v017/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u11_imp_v018/collision_margin_engine_v018.c` | `f87be737d4ca22a3cd6c1e67939b487cd515dacae78ad3f14e861d2be86f8fea` | 64299 |
| `research/residual_primes/analysis/u11_imp_v018/full_run.txt` | `d7fed59c6bb961ce5cda3b2dd4124aa67b65800b0e161a8053cf59501f36374b` | 32766 |
| `research/residual_primes/analysis/u11_imp_v018/full_run_stderr.txt` | `a7c85b256d5545e24ca548614ead7f2fa6b457ed4ea4500e565b777b96b24c2c` | 78 |
| `research/residual_primes/analysis/u11_imp_v018/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u11_route_v019/collision_margin_engine_v019.c` | `cf52a9f9163fb28ce4660bcea6efdd81d97c5011c02b70b6d2557427c485f7ec` | 68216 |
| `research/residual_primes/analysis/u11_route_v019/full_run.txt` | `b16ba2dd74015b8921a261f808b4f9e998977d718515d5efa22680c9288924e6` | 33869 |
| `research/residual_primes/analysis/u11_route_v019/full_run_stderr.txt` | `9d7b543a8be0a99858b496fe6e212d265c3c27a5a56ade7e9ec1e49cb09375bd` | 78 |
| `research/residual_primes/analysis/u11_route_v019/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u11_gate_v021/collision_margin_engine_v021.c` | `2f23110a4678207cfc98244d24813ca27de19ca768fe4cbefaa50c07452cbdbc` | 65978 |
| `research/residual_primes/analysis/u11_gate_v021/collision_margin_engine_v022.c` | `ee807432335a3ee97f087e91398cfcc8cbca2d7c27b685e05e46dc028ccc44bb` | 69883 |
| `research/residual_primes/analysis/u11_gate_v021/full_run.txt` | `5f958799d49a91d08231b26c643b90d9031482765353eae3e43f631153601469` | 32119 |
| `research/residual_primes/analysis/u11_gate_v021/full_run_v022.txt` | `62c1295af024817ea9df56a2e9191fd5b6d9c63f6ec06c2b94eb964d30d36cc1` | 33222 |
| `research/residual_primes/analysis/u11_gate_v021/full_run_stderr_v022.txt` | `8904d7eb954a97f4dcb6c1257f4ec840863f1d378cfca45ec5dad5e8a4704767` | 78 |
| `research/residual_primes/analysis/u11_gate_v021/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u11_gate_v021/sanitized_selftest_v022.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u15_class_v023/collision_margin_engine_v023.c` | `7e0a564c973254b9e9f2140a0778bfcf5e12aaa2c2d5b338fee433cd67e9c1a8` | 76368 |
| `research/residual_primes/analysis/u15_class_v023/full_run.txt` | `9ed44890512cc321f6eb90c54f71555c328a263987009ad3eed04e75548d0539` | 34402 |
| `research/residual_primes/analysis/u15_class_v023/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u15_crt_v024/collision_margin_engine_v024.c` | `1eb843fadb9396bd181589d89158b3f7e81eaf524144dfd53920656494b07d51` | 78424 |
| `research/residual_primes/analysis/u15_crt_v024/full_run.txt` | `16538776b25f3d599ad6a9a2318520d95e291cc6d05f2847f7df4667165a3ae8` | 34706 |
| `research/residual_primes/analysis/u15_crt_v024/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u15_alg_v025/collision_margin_engine_v025.c` | `3123304e8610c56fee57e6fc0dcbe4d7c91cae405e06d51153ac19cfa6966c97` | 86634 |
| `research/residual_primes/analysis/u15_alg_v025/full_run.txt` | `796e0fb7f5a0fddcc62365a5adf55ed0ba123eaa1c3c17ced93454ff8d601ff6` | 34996 |
| `research/residual_primes/analysis/u15_alg_v025/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u15_span_v026/collision_margin_engine_v026.c` | `88f6b1c2da51e53bc67d19d3bcc1c60a11d338e82e18d83e187ce718330d4741` | 93675 |
| `research/residual_primes/analysis/u15_span_v026/full_run.txt` | `292a41534ae842d3d5ba5f6320f2a38a4774e96a8cc98150ec74e804379626e8` | 35673 |
| `research/residual_primes/analysis/u15_span_v026/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u19_class_v027/collision_margin_engine_v027.c` | `d4cbf23f6faf21dca86c7814ce9b8f2cc31c749ab4885bae5bc80323ea09a045` | 97956 |
| `research/residual_primes/analysis/u19_class_v027/full_run.txt` | `24a133e21b78b437a71bc3837730233e8815ebf984dc9f883c60ab3f41de5f20` | 44535 |
| `research/residual_primes/analysis/u19_class_v027/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `ErdosStrausConjecture/ResidualPrimes/U15Layer.lean` | `a3cb7145b0f52b5b2b5886d6a0258b7b77db75a466d2afef03827935427a39ea` | 6583 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u15_layer.txt` | `a38782e5999fb5b20b8198302255c487d7e16da2024b893d097192e56369fa95` | 772 |
| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u15_layer.log` | `850a1be7a95ad817cfef9338e10a61d354885e536397bd72b8d4faef3fec6162` | 42 |
| `research/residual_primes/ErdosStrausConjecture_src/print_axioms_u15.lean` | `75767ad1453dd224d151937e974fb447300bc9c63d606f842c9d5d6fd8008422` | 457 |
| `ErdosStrausConjecture/ResidualPrimes/U11Layer.lean` | `db29e20293a0dde367d1b98e2324ef543733e60f4e837331e6232b6bbb0d5324` | 12770 |
| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u11_layer.txt` | `dcbdf3758a1698d6189723924535482333a19706f314b2f4ac12d9f125d73031` | 582 |
| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u11_layer.log` | `52373301989a17e7e601e7027292d64711adfc5aa5eeeef89a442b582361026a` | 42 |
| `research/residual_primes/ErdosStrausConjecture_src/print_axioms_u11.lean` | `f6ce2863438de302f592b1ec182860ca9304f8e9e8d83876a3a274ca92ad0613` | 391 |
| `research/residual_primes/analysis/u7_depth0_v012/collision_margin_engine_v012.c` | `94345ff42991aed7782d86ed3016ad942266880c7a579f2573dd25a9b8622c49` | 47981 |
| `research/residual_primes/analysis/u7_depth0_v012/full_run.txt` | `89e538cb6d0e7ce4d9462fece8257ebed7d4919ac779485af064338caa4c0fad` | 17982 |
| `research/residual_primes/analysis/u7_depth0_v012/full_run_stderr.txt` | `ced48829b8f603759a67be0da6c0f2e8a2d76b56f595a14eaf1019f9a0a77f0a` | 78 |
| `research/residual_primes/analysis/u7_depth0_v012/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u7_gen_v013/collision_margin_engine_v013.c` | `0b96d406677639a6243a58b8fe2a56f38b68810ea8081f9f999de08634a603d9` | 50574 |
| `research/residual_primes/analysis/u7_gen_v013/full_run.txt` | `1088555f5de3792862d9abecbe8c50bea73306991b52b202929594c144bd5a0c` | 18618 |
| `research/residual_primes/analysis/u7_gen_v013/full_run_stderr.txt` | `2c948e018241d1a63e7ba9e7624ee0e8221b399be426b5a88b440cc8402b0731` | 78 |
| `research/residual_primes/analysis/u7_gen_v013/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u7_iff_v014/collision_margin_engine_v014.c` | `db03cea8af13d14c23649b8736747c4e8a7b30dc034d640c9f55b904688ccfbf` | 53188 |
| `research/residual_primes/analysis/u7_iff_v014/full_run.txt` | `5bacb1541a55b94ba806b599be3ea3ce0bd9ab18d43e0623c6be9539d5c5aec5` | 18908 |
| `research/residual_primes/analysis/u7_iff_v014/full_run_stderr.txt` | `f2608b3fa2c0407276bb4f9f0644ed06dec99f6844bbc20e996152b6e89bb656` | 78 |
| `research/residual_primes/analysis/u7_iff_v014/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u7_fail_v010/collision_margin_engine_v10.c` | `adc68dc4fc5dce5988db9b4569facc95094cbffe5176a881506ef9cf7b9c5efa` | 43318 |
| `research/residual_primes/analysis/u7_fail_v010/full_run.txt` | `7aaa4a9cfa4b8705aeaf45b3eda959d7e852b9bc7f949dacd1f2a87361b769a7` | 17288 |
| `research/residual_primes/analysis/u7_fail_v010/full_run_stderr.txt` | `fe7b014d89ca3a7009fa8e5c747e5d86cde8daf24685cfd919252f4a23c2f4d7` | 78 |
| `research/residual_primes/analysis/u7_fail_v010/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/u7_span_depth_v011/collision_margin_engine_v011.c` | `5d5315278bcfa5275fd058305b142ca5f619d9c5acf8f23d14ed1fe98d5a50b8` | 44093 |
| `research/residual_primes/analysis/u7_span_depth_v011/full_run.txt` | `ed37bdfd136796ddd7852ffa7be80db596cb054f4c11c55edd621d9c2d8ab827` | 17525 |
| `research/residual_primes/analysis/u7_span_depth_v011/full_run_stderr.txt` | `2fa7c92b7a29bb1ae210d87658c8c950758380897bcda6edde96109d68c5c40f` | 78 |
| `research/residual_primes/analysis/u7_span_depth_v011/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |


| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_window.txt` | `f502a11a8b6bf19cce3e93ce02424a55a081a1c24d14eb6b4878b803491a557a` | 174 |
| `research/residual_primes/ErdosStrausConjecture_src/WindowForm.lean` | `364910f98645cbb4fc41c71169886685bda119e69ca7660198352379eded0f5b` | 3299 |

| `research/residual_primes/ErdosStrausConjecture_src/axiom_audit_u11b.txt` | `ec3393fec0a5fe32698cff05ec7e50007e3fba2c7b2bdc95c74795743d752cbc` | 170 |
| `research/residual_primes/ErdosStrausConjecture_src/lake_build_u11b.log` | `58d3332d9137f4de5c03d6eb40c5302729cf35e582d65630f2517504ab0d2df5` | 116 |

| `research/residual_primes/analysis/u7_g3_probe_v05/collision_margin_engine_v05.c` | `ba259e6499ba6db7bfcfead174e2d2cf759c9f9124415f58eb03e14b6c6e8353` | 23604 |
| `research/residual_primes/analysis/u7_g3_probe_v05/full_run.txt` | `5b212bb9879995452ec6bf9f3735638e1aafba009dabe19f7f3fd72b8af0125f` | 5618 |

| `research/residual_primes/analysis/delicate_r6_v06/collision_margin_engine_v06.c` | `df6f085531673c22bf1cc5a910bbe597e2b7453e850e339a2a99ce52c30edcfd` | 25135 |
| `research/residual_primes/analysis/delicate_r6_v06/full_run.txt` | `a3ceb2b287c4d79fae338722186169f632045a6ec0b0f6533af872cbd7207db5` | 6334 |
| `research/residual_primes/analysis/delicate_r6_v06/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |

| `research/residual_primes/analysis/layers_r7_v07/collision_margin_engine_v07.c` | `50b78e5f184eae1622bf03799aba5f8bc3439ca0e66b2883a23f3d28cefea99e` | 29083 |
| `research/residual_primes/analysis/layers_r7_v07/full_run.txt` | `1952e0dab641a12a295014636bebe050cdcab5e317a53ad05ba4d60f117b35f9` | 9219 |
| `research/residual_primes/analysis/layers_r7_v07/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |
| `research/residual_primes/analysis/rescue_r8_v08/collision_margin_engine_v08.c` | `63fd0b7229ba793d79c96c444337f2f3f141569e16640aa3e8da11b32baddc15` | 35913 |
| `research/residual_primes/analysis/rescue_r8_v08/full_run.txt` | `8547eb3bf6101333bdfa4f683213086cb07cf526977bfe3605c838ec13616075` | 16008 |
| `research/residual_primes/analysis/rescue_r8_v08/full_run_stderr.txt` | `de905eab2fd8c1f638123b61b5532aaa44fd991f634d85ef39541bec422d2dcf` | 78 |
| `research/residual_primes/analysis/rescue_r8_v08/sanitized_selftest.txt` | `934ec74d9f44bfcd5ca2ddabf1a1f19d5ad73f0bc6ef25a4037c7d12a3a5d992` | 350 |

## Frozen-source statement

The datasets above are frozen as hash-pinned here. The pinned bytes are
identical at Paper-1 tags paper-v1.8 and paper-v1.12 (spot-verified
2026-11-24 against the manifest digests), and Paper 1's current release
line is paper-v1.12, as MANUSCRIPT.md and THEOREM_REGISTRY.md state;
the hashes in this manifest, not a tag name, are the freeze. Paper 2
adds research engines beside them. Any change to a hash above is a
data event and requires a CHANGELOG entry.
