# QTC — EXPERIMENT REPORT & SCALE-UP PLAN
## What we ran on real quantum hardware, and how to make the benefit large

**Author:** Petar Nikolov · **Date:** 31 May 2026 · **Framework:** U-Theory v26/v27 (`APPENDIX_QTC`, `APPENDIX_QTC_BENCH`)
**Hardware:** IBM `ibm_marrakesh` (Heron r2, 156 qubits), Open plan · **Scripts:** `qtc_hw_ibm.py`, `qtc_hw_collective.py`, `qtc_hw_phase3c.py` · **Provenance:** `IBM/*.txt`
**Status:** L1 (measured results) · L2 (scale-up design) · L3 (the "semantic ternary substrate" thesis)

> © 2026 Petar Nikolov · CC BY 4.0

---

# PART A — THE EXPERIMENT WE RAN (in detail)

## A.1 The question
*Does recording information in a **triadic superposition** (a relational, shared-Form state) instead of in bit-like states reduce decoherence — i.e. lower the active error-correction "stabilization tax" — on a real quantum processor?*

This operationalises the QTC thesis: **record not in bits but in dynamic triadic tokens**, where the protected information lives in the *relations* (entanglement = shared Form), not in fragile local amplitudes.

## A.2 The encoding under test (the ternary core)
We compare two ways to store one logical qubit in two physical qubits:

| Encoding | Logical \|0⟩, \|1⟩ | Total-Z (Δ) | Meaning |
|---|---|---|---|
| **Exposed** (bit-like) | \|00⟩, \|11⟩ | ±2 | independent amplitudes — sensitive to a shared phase |
| **DFS / shared-Form** | \|01⟩, \|10⟩ | 0 | one shared Form, two Position-references (entangled) |

The logical superposition tested is \|+_L⟩ = (\|0_L⟩+\|1_L⟩)/√2. The DFS pair sits in the *total-Z = 0* subspace, which is **invariant** under a collective (shared) Z rotation — it only picks up a global phase.

## A.3 Method — Loschmidt echo
For each encoding we ran the circuit:

```
prepare |+_L⟩  →  [ idle delay  OR  injected collective RZ(θ) ]  →  uncompute (inverse prep)  →  measure
```

Ideal evolution returns the state to \|00⟩, so **P(\|00⟩) = fidelity of the logical state to its ideal** (a Loschmidt/echo fidelity). The figure of merit is the **stabilization-tax reduction ratio**

$$R_\text{QTC} = \frac{B_X^\text{exposed} - B_X^\text{DFS}}{B_X^\text{exposed}},\qquad B_X \approx 1 - P(\|00⟩).$$

R = 0 → no benefit; R = 1 → full passive protection; R < 0 → DFS worse.

## A.4 The three runs

**Run 3a — native idle noise (independent), single rep.**
Idle delay 0 and 40 µs, 2048 shots. Result: P00(DFS,40µs)=0.297 vs P00(exposed,40µs)=0.420 → **R = −0.21**. DFS slightly *worse* (extra gates + T1 asymmetry; and the native noise is not collective).

**Run 3b — injected collective noise, 5 reps.**
A shared `RZ(θ)` on *both* qubits (θ = 0, π/4, π/2), 5 reps × 2048 shots:

| θ | P(\|00⟩) DFS | P(\|00⟩) exposed |
|---|---|---|
| 0 | 0.967 ± 0.005 | 0.964 ± 0.005 |
| π/4 | 0.969 ± 0.004 | 0.471 ± 0.010 |
| π/2 | **0.972 ± 0.003** | **0.011 ± 0.003** |

→ **R_QTC(collective, π/2) = +0.97.** DFS flat (global phase only); exposed follows cos²θ and collapses.

**Run 3c — natural collective fraction (MELQ proxy), 5 reps.**
Idle delay-sweep 0/20/40/80 µs, *no* injection — the on-chip probe of whether two qubits dephase collectively by themselves:

| delay | P(\|00⟩) DFS | P(\|00⟩) exposed | R_natural |
|---|---|---|---|
| 0 | 0.960 ± 0.004 | 0.961 ± 0.003 | −0.03 |
| 20 µs | 0.669 ± 0.011 | 0.663 ± 0.010 | +0.02 |
| 40 µs | 0.512 ± 0.015 | 0.518 ± 0.009 | −0.01 |
| 80 µs | 0.374 ± 0.012 | 0.377 ± 0.009 | −0.01 |

→ **R_natural ≈ 0** at all delays: DFS and exposed decay identically. The device's idle noise is essentially **fully independent** (natural collective fraction ≈ 0). Total QPU usage across all three runs ≈ **50 s** of the 600 s budget.

## A.5 What it proved
The three runs **bracket the claim** cleanly:

$$R_\text{QTC}^\text{hardware}:\quad \approx 0\ (\text{independent})\ \longrightarrow\ +0.97\ (\text{collective}).$$

**Passive shared-Form/DFS protection is real and *noise-symmetry-gated*: it appears precisely when, and only when, the noise has the matching (collective) symmetry.** This confirms both the mechanism *and* its honest scope on a real QPU.

## A.6 Honest limits of this experiment
- Two physical qubits, one logical qubit — the smallest possible code.
- Echo-fidelity at a few delays — not a logical *lifetime* or a multi-round *QEC syndrome rate*.
- The collective benefit (3b) used *injected* noise, not native correlated noise.
- The physics (DFS) is established prior art (Lidar–Zanardi–Whaley 1998; Knill–Laflamme–Viola 2000); we reproduced it honestly, we did not discover it.

---

# PART B — WHY A BIGGER BENEFIT NEEDS A DIFFERENT REGIME

The size of the benefit obeys, roughly,

$$\text{benefit} \;\sim\; (\text{collective-noise fraction})\times(\text{fraction of information held in protected relational DOF}).$$

Run 3c showed the first factor ≈ 0 on a transmon. So to **see** a large benefit you must move to a regime where the collective fraction is genuinely high, scale the protected structure, and measure the metrics that matter for fault tolerance. Three levers:

1. **Platform** — go where collective noise dominates (trapped ions, atoms, shared-bath systems).
2. **Scale** — multi-qubit collective-dephasing DFS / noiseless subsystems; many logical qubits; repeated QEC rounds.
3. **Metric** — logical T₂ lifetime and **QEC syndrome rate** (the actual $B_X$ tax), not single-shot echo fidelity.

---

# PART C — SCALE-UP EXPERIMENT PLAN

Each experiment lists: **platform · setup · metric · expected effect · cost · falsifier.**

### C.1 Trapped-ion DFS (collective-noise-native) — *the headline scale-up*
- **Platform:** trapped-ion QPU (Quantinuum H-series / IonQ), via cloud (AWS Braket / Azure Quantum). Dominant noise = **collective dephasing** from global magnetic-field fluctuations → the native regime where DFS wins.
- **Setup:** encode one logical qubit in the 2-ion DFS {\|01⟩,\|10⟩} vs a bare ion; run Ramsey/echo over increasing free-evolution time; also a 4-ion DFS (encodes 1 logical qubit robust to collective dephasing).
- **Metric:** logical **T₂*** (coherence time) DFS vs bare.
- **Expected effect:** **large** — literature reports order **10×–100×** T₂ improvement for DFS on ions (because the noise is collective). This is where your prescription pays off.
- **Cost:** modest paid cloud time (no free 10-min equivalent; budget a few $–$$).
- **Falsifier:** if DFS T₂ ≤ bare T₂ on ions, the collective-noise premise fails.

### C.2 Multi-qubit collective-dephasing DFS / noiseless subsystems (scaling law)
- **Platform:** ions (or any collective-noise device).
- **Setup:** the N-qubit collective-dephasing DFS encodes ~⌊N/2⌋ logical qubits in the total-Z=0 sector. Sweep N = 2, 4, 6, 8…; measure logical fidelity vs N at fixed evolution time.
- **Metric:** logical error rate vs N; protected-subspace fraction.
- **Expected effect:** protection holds as N grows while the *encoding rate* rises — demonstrates the structure scales, not just the toy case.
- **Falsifier:** if logical error grows with N as fast as physical, the subsystem isn't noiseless at scale.

### C.3 Tunable collective-fraction sweep on transmons (map the crossover)
- **Platform:** IBM transmons (cheap, what we already use).
- **Setup:** inject a *mixture* — fraction η of a shared RZ(θ) (collective) plus (1−η) independent RZ — and sweep η ∈ [0,1]. We measured only the endpoints (η≈0 native → R≈0; η=1 injected → R=+0.97).
- **Metric:** R_QTC(η) curve → the **crossover η\*** where R becomes positive.
- **Expected effect:** a smooth 0→1 curve; locates how collective the noise must be to pay off. Directly informs which real platforms qualify.
- **Cost:** tiny (minutes of QPU).
- **✅ MEASURED (ibm_marrakesh, 5 reps, 31 May 2026, `qtc_hw_c3_sweep.py`):** a clean crossover curve — R_QTC = −20.3 (η=0) → −3.4 (0.25) → **−0.01 (0.50)** → +0.78 (0.75) → **+0.96 (η=1)**. DFS and exposed are mirror images crossing at **η\* ≈ 0.50**: passive DFS pays off **only when >50% of the dephasing is collective**. Transmons sit at η≈0 (Run 3c) → no benefit; ion traps sit near η≈1 → large benefit. QPU usage 29 s. Provenance: `IBM/qtc_hw_c3_sweep_marrakesh.txt`.
- **Falsifier:** if R stays ≤0 for all η<1, passive DFS needs perfectly collective noise (too fragile to be useful).

### C.4 QTC-2 at scale on real datasets — *the genuine novelty test*
- **Goal:** turn QTC-2 (FPC compressibility predicts QTC protectability) from a simulation correlation into a **validated predictive law on real data**.
- **Setup:** take many real corpora of varying structure (images, text, sensor time-series); compute each one's **FPC compressibility** $C_\text{FPC}$ (independent classical pipeline); build the QTC lift (shared-Form groups → DFS-protected units); under a *fixed collective noise model* (Aer first, then ion hardware on a subset) measure the **active-correction tax / logical error** and hence $R_\text{QTC}$.
- **Metric:** correlation (Spearman) between $C_\text{FPC}$ and $R_\text{QTC}$ **across real datasets**, with the two computed by independent pipelines.
- **Expected effect:** if QTC-2 is a real law, structured data is measurably cheaper to protect → a *usable* rule: "compress classically first to choose the cheapest quantum encoding."
- **✅ MEASURED (local, real files + controls, 31 May 2026, `qtc2_realdata.py`):** **gzip ratio** (independent classical pipeline) vs **R_QTC** (noise-sim pipeline) across 8 datasets → **Spearman 0.99, Pearson 0.83**. Already-compressed PNG/RAR and random → R=0; markdown/code → 0.36–0.48; tiled synthetic → 0.93. Supports QTC-2 **at the model level** on real data. Caveat: gzip and the 4-byte relational redundancy both measure redundancy (different algorithms), and R_QTC is still a noise *simulation* — the deep physical claim needs the hardware logical-error version (Stage 3+).
- **Falsifier:** if the correlation vanishes on real data / hardware (r≈0), QTC-2 is refuted — this is the experiment that could make or break the *novel* claim.

### C.5 Dual-rail erasure + DD stack (best near-term practical payoff)
- **Platform:** superconducting (dual-rail transmons/cavities) — an active 2023–24 research front.
- **Setup:** the {\|01⟩,\|10⟩} code is a **dual-rail erasure-detecting** code (a damping jump leaves the subspace → heralded). Combine with **dynamical decoupling** for the residual dephasing. Run repeated detection rounds.
- **Metric:** **erasure-detection rate** + post-selected logical fidelity + logical error per round vs a bare qubit.
- **Expected effect:** **real and near-term** — converting damping into detectable erasures meaningfully lowers QEC overhead (erasure qubits are a hot path to fault tolerance).
- **Falsifier:** if heralded post-selection doesn't beat the bare logical error at acceptable yield, the dual-rail advantage doesn't materialise here.

### C.6 Logical-level metrics over many rounds (the fault-tolerance question)
- For C.1/C.2/C.5: run **repeated stabilizer/echo rounds** and measure the **QEC syndrome rate** (the literal $B_X$ anti-entropy tax) DFS vs bare, and the logical $T_2$ over time — the quantities that decide whether the encoding helps a real fault-tolerant machine, not just a single echo.

---

# PART D — THE "TERNARY CODE WITH SPECIAL MEANINGS (0,1,2)" THESIS (honest)

Your framing — *record in triadic superpositions; it is a ternary code, but 0/1/2 carry special meanings* — deserves a precise, honest articulation.

### D.1 What is genuinely bold / potentially novel
- The carrier is a **qutrit** (3-level system): $\Sigma_3 = \{|\mathsf F\rangle, |\mathsf P\rangle, |\mathsf A\rangle\}$ — a literal base-3 alphabet. The radix-economy argument (base 3 nearest *e*) and the **Peircean irreducibility** (triadic relations don't reduce to dyadic; `APPENDIX_FPC` FPC-1) make ternary the minimal-complete structural alphabet.
- The **special meanings** are the contribution: 0,1,2 are **not arbitrary** — they are **Form, Position, Action**, the three ontological invariants of U-Theory. A QTT is therefore a *semantic* ternary unit: each trit names *what kind* of structural primitive it is. This is what distinguishes it from generic ternary computing.
- The **compression↔protection bridge** (QTC-2): classical structure (shared Forms) maps to physically protected relational DOF. If validated (C.4), this is a real, novel, usable principle.

### D.2 What is prior art (must be stated)
- **Qutrit / qudit / ternary quantum computing** already exists (qutrit gates, ternary logic, Setun's classical ternary). The base-3 *carrier* is not new.
- **DFS / noiseless subsystems** (the protection mechanism) are established (1998–2000).
- So the *physics and the radix* are known; the **semantic assignment (0,1,2 = F/P/A) + the compression-protection law** are the bold, U-Theory-specific parts.

### D.2.1 What is new vs known DFS prior art

| Aspect | Known prior art | New in this work |
|---|---|---|
| Collective-dephasing DFS span{\|01⟩,\|10⟩} | Lidar–Chuang–Whaley 1998 | — (reused) |
| Noiseless subsystems | Knill–Laflamme–Viola 2000 | — (reused) |
| Dynamical decoupling | standard | — (reused) |
| Dual-rail erasure detection | active 2023–24 | — (reused) |
| **Two-sided hardware scope boundary** — native-noise null (R≈0) + collective +0.97, η\* ≈ 0.50 crossover | — | **this work (ibm_marrakesh)** |
| **Compressibility ↔ protectability correlation (QTC-2)** | — | **this work — hypothesis (sim + gzip, Spearman ≈ 0.99)** |
| **Unified triadic framing** (FPC→QTC→NDT; F/P/A token ontology) | — | **this work — conceptual/organizational, not the mechanism** |

> Honest one-liner: *QTC does not discover decoherence-free subspaces; it reinterprets them as shared-Form relational recording, integrates them with the FPC/NDT/SSS accounting, and validates on hardware the exact boundary condition — passive protection appears only when the noise symmetry matches the encoded relation.*

### D.3 What would substantiate "revolutionary"
The word is aspirational until at least one of these is shown:
1. **QTC-2 holds as a real predictive law** on real data/hardware (C.4) — *compress-to-choose-encoding* becomes a tool.
2. A **semantic-ternary advantage** beyond generic qutrit computing — e.g. the F/P/A typing makes encodings/error-models or world-models for AI measurably better than untyped qutrits.
3. **Large logical-lifetime gains** in the right regime (C.1/C.2) that a bit-based encoding cannot match at equal overhead.
Until then, the honest status is: **a bold, coherent, falsifiable reframing** with one established-physics demonstration and a clear path to test the novel parts.

---

# PART E — STAGED ROADMAP & DECISION GATES

| Stage | Experiment | Platform | Cost | Gate (go/no-go) |
|---|---|---|---|---|
| 1 | C.3 collective-fraction sweep | IBM (free/cheap) | minutes | locate η\*; cheap, do first |
| 2 | C.4 QTC-2 on real data (Aer) | local + Aer | free | r>0 across datasets → continue |
| 3 | C.1 ion DFS T₂ | Quantinuum/IonQ (cloud) | $–$$ | ≥3× T₂ gain → strong result |
| 4 | C.5 dual-rail erasure + DD | SC dual-rail | cloud/collab | beats bare logical error → practical |
| 5 | C.2 multi-qubit DFS scaling + C.6 logical metrics | ions / FT testbed | $$ | scaling holds → publishable |

**Smallest high-value next step:** Stage 1 (C.3, on the hardware we already have) + Stage 2 (C.4, free, local) — together they map the crossover *and* test the novel QTC-2 law without new credentials or cost.

---

> **One line.** *We showed on a real QPU that triadic shared-Form recording protects information exactly when the noise is collective (R: 0 → +0.97); the bold open question is whether classical compressibility predicts that protection (QTC-2) and whether semantic ternary (0,1,2 = Form, Position, Action) buys more than generic qutrits — both are now concrete, falsifiable experiments.*

*QTC Experiment Report & Scale-up Plan · U-Theory v26/v27 · © 2026 Petar Nikolov · CC BY 4.0*
