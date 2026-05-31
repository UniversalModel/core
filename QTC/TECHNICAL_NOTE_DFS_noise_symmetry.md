# Noise-Symmetry-Gated Decoherence-Free Encoding on a Superconducting Quantum Processor
### A controlled hardware study, with a compressibility–protectability correlation

**Author:** Petar Nikolov · **Date:** 31 May 2026 · **Hardware:** IBM `ibm_marrakesh` (Heron r2, 156 qubits)
**Software:** qiskit 2.4.1, qiskit-aer 0.17.2, qiskit-ibm-runtime 0.47.0
**Code & data:** `qtc_hw_ibm.py`, `qtc_hw_collective.py`, `qtc_hw_phase3c.py`, `qtc_hw_c3_sweep.py`, `qtc_validation_phase1.py`, `qtc_phase2_qiskit.py`, `qtc2_realdata.py`; raw logs in `IBM/*.txt`.

> **Scope.** This note reports an *engineering* result, not new physics. Decoherence-free subspaces (DFS) are established prior art [1,2]. The contribution is (i) a clean, two-sided **hardware** demonstration that passive DFS protection is *noise-symmetry-gated* — it helps only when the device noise shares the code's symmetry — and (ii) a model-level **correlation between classical compressibility and quantum protectability** worth further study. A separate document covers the broader (U-Theory) motivation; it is deliberately omitted here.

---

## Abstract

We encode one logical qubit in two physical qubits two ways: a **decoherence-free** code in the collective-dephasing-invariant subspace span{|01⟩,|10⟩}, and an **exposed** code span{|00⟩,|11⟩}. Using a Loschmidt-echo protocol on a superconducting processor (`ibm_marrakesh`), we measure the logical fidelity of each under (a) the device's native idle noise and (b) injected collective dephasing, and we sweep the collective fraction η of an injected mixture. We find: under **native** (independent) noise the DFS gives **no benefit** (stabilization-tax-reduction ratio R ≈ 0 to −0.21); under **collective** noise it gives near-total protection (R = +0.97 ± small); and R(η) crosses zero at **η\* ≈ 0.5**. We also report, in simulation and on real files, a strong rank correlation (Spearman ≈ 0.98–0.99) between a dataset's classical compressibility and its protectability under a fixed collective-noise model. The results are a compact, reproducible confirmation that passive symmetry-protected encoding is useful **iff** the dominant noise matches the code's symmetry — a practical truth for choosing where such encodings pay off.

---

## 1. Background

A decoherence-free subspace is a set of states left invariant (up to a global phase) by a symmetric noise channel; information encoded there is passively protected without active error correction [1]; the more general object is the noiseless subsystem [2]. For two qubits under **collective dephasing** (the same fluctuating phase on both), the total-spin-$z=0$ subspace span{|01⟩,|10⟩} is decoherence-free, while span{|00⟩,|11⟩} acquires a relative phase and dephases. We use these as the **DFS** and **exposed** logical codes, respectively. Both encode one logical qubit; the DFS costs the standard 2-physical-for-1-logical overhead.

## 2. Methods

**Encodings.** Logical |+⟩ states: DFS = (|01⟩+|10⟩)/√2; exposed = (|00⟩+|11⟩)/√2.

**Loschmidt echo.** prepare |+_L⟩ → [idle delay OR injected dephasing] → uncompute (inverse prep) → measure. Ideal evolution returns |00⟩, so **P(|00⟩) = logical fidelity**.

**Figure of merit.** Stabilization-tax-reduction ratio
$$R = 1 - \frac{1-F_\text{DFS}}{1-F_\text{exposed}},\qquad F \equiv P(|00\rangle),$$
with $R=0$ no benefit, $R=1$ full passive protection, $R<0$ DFS worse.

**Injected noise.** Collective: same RZ(θ) on both qubits. Tunable mixture (C.3): collective angle θ·η on both + differential angle θ·(1−η) as +/− on the two qubits (θ=π/2); η is the collective fraction.

**Runtime.** Backend ibm_marrakesh (Heron r2, 156q), 2048 shots, 5 repetitions per configuration (except the first idle run, 1 rep); optimization_level-1 transpilation; SamplerV2. Total QPU usage across all runs ≈ 80 s. Simulation cross-checks: pure-numpy density matrix (Phase 1) and Qiskit/Aer noise model (Phase 2).

## 3. Results

**(3a) Native idle noise, 40 µs (1 rep).** P(|00⟩): DFS 0.297, exposed 0.420 → **R = −0.21**. DFS slightly *worse* (gate overhead + T1 asymmetry; native noise not collective).

**(3c) Native idle delay-sweep (5 reps).** DFS ≈ exposed at every delay → **R_natural ≈ 0** (within ±0.02); the natural collective fraction is ≈ 0.

| idle delay | P(|00⟩) DFS | P(|00⟩) exposed | R |
|---|---|---|---|
| 0 µs | 0.960 ± 0.004 | 0.961 ± 0.003 | −0.03 |
| 20 µs | 0.669 ± 0.011 | 0.663 ± 0.010 | +0.02 |
| 40 µs | 0.512 ± 0.015 | 0.518 ± 0.009 | −0.01 |
| 80 µs | 0.374 ± 0.012 | 0.377 ± 0.009 | −0.01 |

**(3b) Injected collective dephasing (5 reps).**

| θ | P(|00⟩) DFS | P(|00⟩) exposed |
|---|---|---|
| 0 | 0.967 ± 0.005 | 0.964 ± 0.005 |
| π/4 | 0.969 ± 0.004 | 0.471 ± 0.010 |
| π/2 | 0.972 ± 0.003 | 0.011 ± 0.003 |

→ **R(collective, π/2) = +0.97.** DFS flat (global phase only); exposed follows cos²θ.

**(C.3) Collective-fraction sweep (5 reps), the central result.**

| η (collective frac) | P(|00⟩) DFS | P(|00⟩) exposed | R |
|---|---|---|---|
| 0.00 | 0.019 ± 0.002 | 0.954 ± 0.006 | −20.3 |
| 0.25 | 0.140 ± 0.007 | 0.804 ± 0.007 | −3.4 |
| 0.50 | 0.471 ± 0.012 | 0.476 ± 0.007 | −0.01 |
| 0.75 | 0.811 ± 0.010 | 0.148 ± 0.005 | +0.78 |
| 1.00 | 0.959 ± 0.004 | 0.016 ± 0.002 | +0.96 |

DFS and exposed are mirror images crossing at **η\* ≈ 0.50**: passive DFS pays off **only when more than half the dephasing is collective**. Native transmon noise sits at η ≈ 0 (3c); ion-trap noise sits near η ≈ 1.

**Simulation agreement.** Phase 1 (numpy density matrix) and Phase 2 (Aer noise model) reproduce all of the above qualitatively and quantitatively; the {|01⟩,|10⟩} code additionally heralds amplitude-damping jumps via a total-Z parity check (dual-rail erasure detection), giving post-selected fidelity ≈ 0.95–1.0 at yield 1−γ.

## 4. A compressibility–protectability correlation

We tested whether a dataset's **classical compressibility** predicts the fraction of it that can be placed in protected (relational) degrees of freedom and hence its **R** under a fixed collective+independent noise model. Two independent pipelines: (i) compressibility — gzip ratio (real files) or a triadic bit-accounting (synthetic); (ii) protectability — R from a density-matrix noise simulation driven by the data's repeated-structure fraction.

- Synthetic corpora, structure sweep: **Spearman(C, R) = 0.98** (monotonic, saturating once everything is protectable).
- Real files + controls (markdown, code, PNG, RAR, random, tilings): **Spearman(gzip-ratio, R) = 0.99, Pearson = 0.83**; already-compressed/random → R = 0, text/code → 0.36–0.48, tilings → 0.93.

This is a **model-level** correlation (R from a noise *simulation*, and both measures track redundancy via different algorithms). It motivates, but does not establish, a predictive law; the genuine test is logical error rates on real datasets on hardware (§6).

## 5. Discussion

The headline is a clean **noise-symmetry gate**: $R$ runs from strongly negative (independent/differential noise) through zero (η\*≈0.5) to ≈+1 (collective). Passive DFS is therefore **not a free lunch** on today's superconducting transmons, whose native noise is essentially independent (η≈0) — measured directly, not assumed. The same encoding gives near-total protection exactly when the noise is collective. This is consistent with, and a hardware confirmation of, the established DFS theory [1,2]; the value here is the *controlled, two-sided, reproducible* demonstration on a current device, including a reported **negative** result.

**Where the benefit is expected to be large:** platforms with intrinsically collective noise — **trapped ions** (global magnetic-field fluctuations), where DFS coherence-time gains of order 10×–100× are reported in the literature. The η\*≈0.5 crossover gives a concrete admission criterion: passive DFS helps a platform only if its collective-noise fraction exceeds ~0.5.

## 6. Limitations

- Smallest code (1 logical in 2 physical); echo fidelity at a few delays, not logical $T_2$ over many QEC rounds.
- The collective benefit (3b/C.3) used *injected* coherent dephasing, not native correlated noise.
- The compressibility–protectability correlation (§4) is model-level; R comes from a noise simulation, not measured logical error.
- No multi-node / cross-chip test (requires quantum networking, unavailable on the open plan).

## 7. Conclusion

Passive symmetry-protected (DFS) encoding works **iff** the dominant device noise shares the code's symmetry — demonstrated cleanly on a superconducting QPU with a crossover at η\*≈0.5, including an honestly-reported native-noise null result. A classical-compressibility ↔ quantum-protectability correlation (Spearman ≈0.99 at model level) is reported as a hypothesis for further test. The natural next experiment is trapped-ion DFS, where the collective-noise regime is native.

## Data & code availability
All circuits, simulations, and raw job logs are included: hardware scripts (`qtc_hw_*.py`), simulators (`qtc_validation_phase1.py`, `qtc_phase2_qiskit.py`, `qtc_bench.py`, `qtc2_realdata.py`), and provenance (`IBM/qtc_hw_*_marrakesh.txt`, with IBM job IDs).

## Credential hygiene
No API token is committed in this repository. IBM credentials are stored locally via `QiskitRuntimeService.save_account()` and read from `~/.qiskit/qiskit-ibm.json`; the scripts never contain a token. If a token is ever pasted into a public chat or otherwise exposed, **rotate/revoke it immediately** at the IBM Quantum Platform.

## References
[1] Lidar, Chuang, Whaley, *Decoherence-Free Subspaces for Quantum Computation*, PRL 81, 2594 (1998).
[2] Knill, Laflamme, Viola, *Theory of Quantum Error Correction for General Noise*, PRL 84, 2525 (2000).
[3] Holevo, *Bounds for the quantity of information transmitted by a quantum channel* (1973).
[4] Nielsen & Chuang, *Quantum Computation and Quantum Information* (2010).

---

*Engineering technical note. Prior art: DFS [1,2]. Contribution: controlled two-sided hardware validation of noise-symmetry-gating (η\* crossover) + a compressibility–protectability correlation hypothesis.*
