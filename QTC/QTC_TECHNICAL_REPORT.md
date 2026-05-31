# TECHNICAL REPORT — Quantum Triadic Codec (QTC)
## A Superposition-Native Recording Architecture that Reduces the Quantum Stabilization Tax

**Author:** Petar Nikolov · **Date:** 31 May 2026 · **Framework:** U-Theory v26/v27
**Companion appendices:** `APPENDIX_QTC_QUANTUM_TRIADIC_CODEC.md` (full spec), `APPENDIX_FPC_TRIADIC_COMPRESSION.md` (classical base), `APPENDIX_NDT`, `APPENDIX_DP` (§DP-S6), `APPENDIX_QC_NISQ` (MELQ)
**Reference code:** `qtc_codec_reference.py` (DFS round-trip), `qtc_validation_phase1.py` (5-experiment suite), `fpc_codec_reference.py` (classical codec)
**Status:** L1 (validation results & physical bounds) · L2 (codec architecture) · L3 (real-device stabilization-reduction claim)

> © 2026 Petar Nikolov · CC BY 4.0 (content) · MIT (code)

---

## ABSTRACT

The Quantum Triadic Codec (QTC) records information **not in bits but in dynamic triadic tokens** — qutrit-indexed registers whose three irreducible kinds (Form, Position, Action) can be held in superposition and whose links are carried by entanglement. Its central engineering claim is that recording information in the **relational / shared-Form** degrees of freedom places it in a **decoherence-free subspace (DFS)** that the dominant (collective) device noise cannot corrupt, so part of the error protection becomes intrinsic to the encoding rather than added on top — **reducing the active error-correction (stabilization) tax**. A five-experiment density-matrix validation confirms the mechanism: the shared-Form logical state holds fidelity **1.0000** under collective dephasing of arbitrary strength with **zero active correction**, while the same code simultaneously **heralds** amplitude-damping jumps (post-selected fidelity 1.0000) and a δ-triggered dynamical-decoupling loop matches dense CPMG protection with **4× fewer pulses**. The advantage is in stabilization and structure, not retrievable bits — the Holevo bound is respected throughout.

---

## 1. PROBLEM & THESIS

Fault-tolerant quantum computing is dominated by the cost of **stabilization**: active quantum error correction (QEC) continuously spends measurement and entropy budget to keep fragile amplitudes alive. In U-Theory terms (`APPENDIX_NDT` §4.3) this is the **anti-entropy tax** $B_X$ paid to keep the coherence currency $B_Y$ solvent.

**Thesis.** If we stop recording in bits (a *dyadic* substrate) and instead record in **dynamic triadic tokens** whose information lives in *relations* (shared Form = entanglement), then the dominant collective noise is **blind** to that information, and the active stabilization tax drops. The naïve reading — "superposition reduces stabilization" — is false in general (arbitrary superposition is *more* fragile); the defensible claim is specifically about **symmetry-protected, relational** superposition encoding.

---

## 2. ARCHITECTURE (in brief)

- **Unit of storage — the Quantum Triadic Token (QTT).** A qutrit type-register $\alpha|\mathsf F\rangle+\beta|\mathsf P\rangle+\gamma|\mathsf A\rangle$ plus value-registers over the Form/Position/Action dictionaries. The classical FPC token $t=(\mathrm{fid},\mathrm{sid},\mathrm{pid},\mathrm{aid},r)$ lifts field-by-field to quantum registers.
- **Every Position is a dynamic token.** Memory is a recursive, multidimensional lattice; addresses are tokens-of-tokens down to the qutrit. Tokens are *processes* (gate-evolvable), not stored values.
- **Links = entanglement.** The binding "which Form, at which Position, with which Action" is a quantum correlation, not an index (`APPENDIX_DP`: *entanglement = shared Form*).
- **Record = state preparation. Reproduce = measurement (decode).** Decoherence is the uninvited measurement (Action leakage / Lindblad).
- **Recursion → N-adic.** A token-tree branches by $N$ to depth $d$ ($N^d$ leaves), giving the $N=3$→$5$ family of `APPENDIX_NDT`.

---

## 3. THE STABILIZATION-REDUCTION MECHANISM

For the most common device noise — **collective dephasing** — the subspace $\mathrm{span}\{|01\rangle,|10\rangle\}$ (total spin-$z=0$) is a decoherence-free subspace: every state in it acquires only a *global* phase and is physically unchanged. In triad language this subspace is **one shared Form with two Position-references** — exactly the Mirror-Entangled Logical Qubit (MELQ) of `APPENDIX_QC_NISQ` §QC.13.3. Information recorded there needs **no active correction** against the dominant channel; only the residual non-collective noise requires the active (Action) layer.

---

## 4. VALIDATION RESULTS (density-matrix, `qtc_validation_phase1.py`, 31 May 2026)

Each noise channel is met by a distinct triadic defense. Standard Kraus channels; deterministic; **all asserts pass.**

| # | Noise channel | Triadic defense | Measured result |
|---|---------------|-----------------|-----------------|
| **A** | Collective dephasing | **Form** — DFS / shared-Form (MELQ) | F = **1.0000** for every σ; exposed → 0.5000 |
| **B** | Independent dephasing / amp-damping | *(honest limit — none)* | DFS degrades too (F≈0.85 @ λ=0.3) |
| **C** | Amplitude-damping **jumps** | **Action** — total-Z parity (leakage check) | heralded & removed; post-select F = **1.0000**, yield 1−γ |
| **D** | Residual quasi-static dephasing | **δ-triggered DD** | 0.139 (no DD) → **0.48 with 2 pulses** (CPMG: 8) |
| **E** | accounting | **Holevo ledger** | ≤ log₂3 = 1.585 bits/qutrit; 0.50 infidelity avoided @ σ=1 |

**Key findings.**
1. **Passive Form-protection is exact and free** against collective dephasing (Exp A).
2. **One code, two channels.** $\{|01\rangle,|10\rangle\}$ is simultaneously the collective-dephasing DFS *and* a dual-rail amplitude-damping **detecting** code: a jump leaves the total-$Z=0$ subspace and is heralded by the parity/Action check, so the accepted logical state is exact (Exp C). Passive Form + active Action are the same code on two channels.
3. **Adaptive stabilization is cheaper.** A δ-triggered DD loop (fire only when the imbalance metric rises) matches dense CPMG with 4× fewer pulses (Exp D) — the SSS/LGP-10 δ-monitoring loop applied to coherence.
4. **Honest scope.** DFS is not magic (Exp B); QTC buys stabilization-tax reduction + structure, not extra retrievable bits (Exp E, Holevo).

---

## 5. HONEST LIMITS (per `APPENDIX_RH`)

- **Holevo:** ≤ log₂3 ≈ 1.585 retrievable bits per qutrit — no unbounded lossless classical compression.
- **No-cloning:** a superposed Form cannot be copied; dedup becomes a *shared* entangled reference (consistent with "one Form, many Positions").
- **Threshold theorem:** passive DFS covers only the noise it is symmetric to; residual noise still needs active codes. QTC *lowers* the tax, it does not repeal QEC.
- **Substrate:** a real QTT needs a coherence-solvent substrate (qutrits / qubit-pairs); classical simulation illustrates but does not deliver the benefit.
- The real-device stabilization-reduction claim remains **L3** until hardware validation (§6).

---

## 6. ROADMAP

- **Phase 1 — done (this report):** density-matrix validation of the four mechanisms. ✅
- **Phase 2 — Qiskit/Aer transpiler: ✅ done (31 May 2026, `qtc_phase2_qiskit.py`, qiskit 2.4 / aer 0.17).** Qutrit token → 2 qubits (|11⟩ = leakage flag); collective dephasing F(DFS) = 1.0000 vs exposed → 0.51; Aer amp+phase damping with total-Z parity heralding lifts F 0.76 → 0.95; DFS prep transpiles to depth 5 on `['rz','sx','x','cx']`. Claim now L2 on a real circuit simulator; physical hardware = Phase 3.
- **Phase 3 — first real-QPU run: ✅ done (31 May 2026, IBM `ibm_marrakesh`, Heron r2, `qtc_hw_ibm.py`).** Honest **negative**: $R_\text{QTC}=-0.21$ — passive DFS gave no benefit under the device's *independent* T1/T2 noise, exactly as the scope predicts (DFS protects *collective* dephasing only). Confirms "reduced, not zero — only for matching noise symmetry."
- **Phase 3b — ✅ done (IBM `ibm_marrakesh`, `qtc_hw_collective.py`, 5 reps):** injected collective Z → **R_QTC = +0.97** (DFS flat 0.972±0.003 vs exposed → 0.011±0.003 at θ=π/2). The two runs bracket the claim: **R = −0.21 (independent) → +0.97 (collective)** — protection is real and noise-symmetry-gated. Only 18 s QPU used.
- **Phase 3c — ✅ measured (IBM `ibm_marrakesh`, `qtc_hw_phase3c.py`, 5 reps idle sweep):** natural collective fraction ≈ 0 — DFS ≈ exposed at all delays (R_natural ≈ 0 ± 0.02) → **no free benefit on transmons**. A true cross-chip **MELQ 2-node** (entanglement between separate QPUs) needs quantum networking, beyond the free plan / current IBM cloud — the remaining frontier.
- **Practical-benefit summary (honest):** the DFS/DD/dual-rail techniques are established prior art (DFS: Lidar–Zanardi–Whaley 1998; noiseless subsystems: Knill–Laflamme–Viola 2000). On transmons passive DFS ≈ 0 gain (measured); on collective-noise platforms (trapped ions) DFS gives large gains; DD gives ~2–10× T2 in practice; dual-rail erasure detection is an active real direction. This work's contribution is the **unifying triadic framing + an honest, hardware-validated demonstration + the falsifiable QTC-2 hypothesis** — conceptual/organizational value, not a new physical speedup.
- **Patches in flight:** P4 leakage-as-detector (validated), P5 noise-adaptive Form basis, P6 Holevo ledger (validated), δ-triggered DD (validated).

---

## 7. PLACE IN U-THEORY

QTC is the **N=5 (pentadic) lift of FPC**: FPC writes arbitrary information in the Triadic Language as three sorted sets + links; QTC makes those tokens dynamic qutrit states and the links entanglement. It draws coherence-currency from `APPENDIX_DIM` (5D $B_Y$), generalises via `APPENDIX_NDT`, realises `APPENDIX_DP`'s "entanglement = shared Form", and reuses `APPENDIX_QC_NISQ`'s MELQ. Compressibility/balance is scored by the same non-compensatory $U=\sqrt[3]{F\cdot P\cdot A}$ of `APPENDIX_SSS`.

---

## 8. ONE-LINE & REFERENCES

> **Record with triadic tokens, not bits; write the relations in superposition, and the noise that is blind to those relations needs no correction.**

**References:** Burch (1991) Peircean Reduction Thesis · Lidar, Chuang, Whaley (1998) Decoherence-Free Subspaces · Knill, Laflamme, Viola (2000) Noiseless Subsystems · Holevo (1973) · Wootters & Zurek (1982) No-cloning · Nielsen & Chuang (2010). U-Theory: `APPENDIX_FPC`, `APPENDIX_QTC`, `APPENDIX_NDT`, `APPENDIX_DIM`, `APPENDIX_DP`, `APPENDIX_QC_NISQ`, `APPENDIX_SSS`.

---

*Technical Report — QTC · U-Theory v26/v27 · © 2026 Petar Nikolov · CC BY 4.0 / MIT*
