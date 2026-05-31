# QTC — Triadic Quantum Codec (engineering bundle)

**Honest scope.** The validated quantum mechanism is a standard **decoherence-free subspace (DFS)** — prior art (Lidar-Chuang-Whaley 1998; Knill-Laflamme-Viola 2000). The "triadic" framing is information **ontology, not a new physical mechanism** (see `APPENDIX_QTC_QUANTUM_TRIADIC_CODEC.md` Sec. 2.3 & 8.4).

**Contribution.** A clean, two-sided **hardware scope-boundary** measured on IBM `ibm_marrakesh`: passive DFS protection is *noise-symmetry-gated* — R_QTC ~ 0 under the device's native (independent) noise, ~ +0.97 under injected collective noise, with a crossover at collective-fraction eta* ~ 0.50. Plus the falsifiable **QTC-2** hypothesis (classical compressibility predicts quantum protectability; model-level Spearman ~ 0.99).

**Start here:** `TECHNICAL_NOTE_DFS_noise_symmetry.md` (standalone engineering note).
Full appendix: `APPENDIX_QTC_QUANTUM_TRIADIC_CODEC.md`. Benchmarks: `APPENDIX_QTC_BENCH.md`. Scale-up plan: `QTC_EXPERIMENT_DESIGN_AND_SCALEUP.md`.
Code: `qtc_*.py` (sims, hardware, compiler), `qutrit_dfs*.py`. Hardware provenance: `*_marrakesh.txt` (with IBM job IDs).
Classical base: `APPENDIX_FPC_TRIADIC_COMPRESSION.md` (repo root).

**Credential hygiene.** No API token is committed in this repository. IBM credentials are stored locally via `QiskitRuntimeService.save_account()`; the scripts never contain a token.
