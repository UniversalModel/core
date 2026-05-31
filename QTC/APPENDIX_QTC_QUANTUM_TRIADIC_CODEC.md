# APPENDIX QTC — QUANTUM TRIADIC CODEC
## Superposition-Native Recording & Reproduction of Information by Dynamic Quantum Triadic Tokens; Recursive Triad Mapping; and Stabilization Reduction through Decoherence-Free Encoding — the N=5 (Pentadic) FPA Token

> *"We do not record with bits. We record with triadic tokens, where every position is itself a dynamic token. If we write in superposition — in the relations, not the local values — the need for stabilization drops, because the information lives where the noise cannot reach it."*
> — Petar Nikolov, May 2026
>
> *Editor's caveat (read precisely): this holds **only** for noise that shares the code's symmetry. Arbitrary superposition is **more** fragile, not less (§6.1); on today's superconducting hardware, whose native noise is independent, the benefit is ≈ 0 (§8.3, R ≈ 0 to −0.21). The quote is true for **collective-symmetric** noise, where the measured hardware result is R = +0.97.*

---

**Author:** Petar Nikolov
**Date:** 31 May 2026
**Framework:** U-Theory v26 + v27 appendix series — the quantum (N=5) lift of `APPENDIX_FPC`
**Status:** L2 (codec/architecture design) + L3 (the stabilization-reduction hypothesis) + L1 (the decoherence-free-subspace demonstration, established quantum physics)
**Version:** 1.0
**Epistemic Level:** L1 (>90%) for the DFS demonstration (§8) and the no-cloning / Holevo limits (§9); L2 (70–90%) for the QTT architecture; L3 for the claim that recursive triadic recording materially reduces real-device QEC overhead.
**Prerequisites:** `APPENDIX_FPC` (Triadic Compression — the classical codec), `APPENDIX_NDT` (N-Adic Decomposition; N=5 quantum substrate), `APPENDIX_DIM` (5D Coherence currency), `APPENDIX_DP` §DP-S6 / FH-QE (Entanglement = shared Form), `APPENDIX_QC_NISQ_TRIADIC_ARCHITECTURE`, `APPENDIX_TPL`
**Function:** Defines the **quantum recording substrate** for U-Theory: how information is written and reproduced when the storage unit is a dynamic triadic token (a qutrit-indexed register) instead of a bit.
**v26 Invariant:** Form ↔ Time · Position ↔ Space · Action ↔ Energy · (+ Coherence/Entanglement ↔ the N=5 currency $B_Y$)

> **Copyright © 2026 Petar Nikolov. All rights reserved. Content licensed under CC BY 4.0; reference code under MIT.**

---

## 0. EXECUTIVE SUMMARY

`APPENDIX_FPC` records arbitrary information classically as three sorted sets of Form/Position/Action primitives plus a link stream. **QTC is its quantum lift.** It replaces the dyadic storage unit — the bit — with a **dynamic Quantum Triadic Token (QTT)**: a qutrit-indexed register whose three irreducible kinds $\{\mathsf F,\mathsf P,\mathsf A\}$ can be held in **superposition**, and whose links are carried by **entanglement** rather than explicit indices.

> **Not a compressor (scope).** "Lift of `APPENDIX_FPC`" means QTC **reuses FPC's token model** (the F/P/A dictionary structure) — **not** that it compresses. A DFS encodes 1 logical qubit in ≥2 physical qubits: that is protection **overhead**, not data savings, and it does **not** beat the Holevo/Shannon bounds (§9). QTC is a **representation / error-protection** scheme, not a compression scheme; "lift" denotes structural reuse, not a compression bridge.

Four claims, each level-tagged:

1. **The storage unit is a dynamic triadic token, not a bit (L2).** Memory is a recursive, multidimensional lattice in which *every Position is itself a dynamic token* — a live quantum state, not a stored value. Recursion is intrinsic: a Position decomposes triadically too (§1, §4).
2. **A new record/reproduce model (L2).** WRITE = preparing the dynamic tokens' joint state; REPRODUCE = guided measurement = decode (§3). "Dynamic" means tokens *evolve* under gates that are themselves Actions.
3. **Recursive triad mapping in superposition builds dynamic constructions (L2/L3).** Tokens compose into trees of entangled sub-tokens — the $N^d$ branching of NDT realised as a quantum register hierarchy (§4–§5).
4. **Recording in superposition reduces the stabilization burden — but only the *right* superposition (L3, mechanism L1).** Arbitrary superposition is *more* fragile. The defensible claim is that encoding information in the **relational / shared-Form** degrees of freedom places it in a **decoherence-free subspace (DFS)** that collective noise cannot corrupt, so part of the protection becomes *intrinsic to the encoding* rather than added on top. **Verified** in §8: a shared-Form logical state keeps fidelity $=1.0000$ under collective dephasing for all noise angles, with zero active correction, while the exposed encoding collapses as $\cos^2\theta$.

> **Scope, up front (honest).** The **validated mechanism is a two-qubit (dyadic) decoherence-free subspace** — established physics [Lidar–Chuang–Whaley 1998]. The qutrit / F-P-A / recursive layer is **information ontology and a proposed direction — not the physical protection** measured here (full statement in §2.3). "Triadic" names the *token model*; the protection that was demonstrated does **not** depend on the number 3. A genuinely triadic mechanism (a qutrit DFS) is open work. The contribution is the **honest, two-sided hardware scope-boundary** (§8.3) and the **compressibility↔protectability correlation** (QTC-2), not the discovery of DFS.

---

## 1. FROM BITS TO DYNAMIC TRIADIC TOKENS

Classical and standard quantum memories store a **value** at an address: a bit, or a qubit amplitude, sitting at a fixed cell. QTC inverts this:

> **QTC-D1 (Recording substrate).** Information is not recorded in bits. It is recorded in **dynamic triadic tokens**. Each *Position* in the recursive map is not a passive cell holding a value — it **is** a dynamic token: a live, superposition-capable, gate-evolvable triadic register.

This has three consequences:

- **No dyadic substrate.** There is no underlying 0/1 layer being "interpreted" as a triad. The base unit is the ternary token itself — consistent with `APPENDIX_FPC` §2 (FPC-1): triadic structure is irreducible to dyadic (Peirce/Burch). The physical carrier of a trit is a **qutrit** (3-level system); the carrier of a token is a qutrit-indexed register.
- **Position is a token (recursion).** Because a Position itself answers *what / where / what-does-it-do*, it decomposes triadically. So "every position is a dynamic token" is literal: addresses are tokens-of-tokens, recursively (§4).
- **Dynamic, not static.** A token is a *process*, not a stored datum. It carries amplitude now and can evolve under Actions (gates) before being reproduced (§5). Recording is the configuration of an evolving field of tokens, not the freezing of values.

---

## 2. THE QUANTUM TRIADIC TOKEN (QTT)

Recall the classical FPC token $t=(\mathrm{fid},\mathrm{sid},\mathrm{pid},\mathrm{aid},r)$. Its quantum lift promotes each field to a quantum register and the **type-selector to a qutrit**.

### 2.1 The type qutrit

The ternary alphabet $\Sigma_3=\{\mathsf F,\mathsf P,\mathsf A\}$ becomes a 3-dimensional Hilbert space $\mathcal H_3=\mathrm{span}\{|\mathsf F\rangle,|\mathsf P\rangle,|\mathsf A\rangle\}$. A classical trit is a basis state; a **dynamic** trit is a qutrit:

$$|\tau\rangle = \alpha\,|\mathsf F\rangle + \beta\,|\mathsf P\rangle + \gamma\,|\mathsf A\rangle,\qquad |\alpha|^2+|\beta|^2+|\gamma|^2=1.$$

The amplitude weights connect to the triadic balance of `APPENDIX_FPC` §10 / `APPENDIX_SSS`: uniform $|\alpha|=|\beta|=|\gamma|$ ⇒ imbalance $\delta=0$ (a maximally balanced token); skew ⇒ high $\delta$.

### 2.2 The full token state

Each rank field becomes a register over its dictionary, and the token's binding becomes entanglement:

$$|t\rangle \;=\; \sum_{f,p,a} c_{f p a}\;|f\rangle_F\,|p\rangle_P\,|a\rangle_A \qquad(\text{generally non-separable}).$$

- **Separable** $c_{fpa}=u_f v_p w_a$: a definite (or independently-superposed) Form, Position, Action.
- **Entangled** (non-factorisable): the **link is physical** — which Form sits at which Position with which Action is encoded as a quantum correlation, not an index. This is exactly `APPENDIX_DP` §DP-S6 / FH-QE: *"Entanglement = shared Form."*

### 2.3 Scope of the "triadic" claim — what is and isn't doing the work

> **Honest scope (what the hardware actually validates).** The decoherence-free protection demonstrated in §8 and on hardware in §8.3 uses a **two-qubit (dyadic) construction** — the total-spin-0 subspace span{|01⟩, |10⟩} — i.e. a textbook **collective-dephasing DFS** (Lidar–Chuang–Whaley 1998). **It does not depend on the number 3.** The qutrit |F⟩, |P⟩, |A⟩ of §2.1 and the recursive RTD of §4 do **not** participate in any verified or measured result here. Therefore, stated plainly:
> - the **validated L1 core is dyadic** (a symmetry-protected qubit code), not triadic;
> - the qutrit / F-P-A / recursive layer (§1, §2, §4) is an **organizational/conceptual framing** and a *proposed, not-yet-validated* direction — it is **not** what does the protecting;
> - a genuinely *triadic* hardware claim would require a **qutrit (3-level) decoherence-free subspace** exploiting a 3-dimensional collective symmetry (qudit DFS/noiseless-subsystem codes under collective SU(d) noise are known to exist) — this is open work (roadmap: `QTC-BENCH` C-series).
>
> Until a qutrit-DFS is demonstrated, **"Triadic" in the title names the information *ontology*** (the F/P/A token model inherited from FPC), **not the physical protection mechanism.** If every mention of F/P/A were deleted from §8, the physics would be unchanged — that is the honest test, and we state its result openly here.

---

## 3. THE RECORD / REPRODUCE MODEL

| Operation | Classical FPC | QTC (quantum) |
|-----------|---------------|---------------|
| **WRITE (record)** | emit sorted sets + link tokens | **prepare** the joint state of the dynamic tokens (state synthesis) |
| **READ (reproduce)** | walk the link stream, rebuild atoms | **guided measurement** in the chosen basis = decode (Born-rule readout) |
| **EVOLVE** | (n/a — static record) | apply Actions = gates; tokens transform *in place* before readout |
| **LINK** | explicit `pid`/`fid` indices | **entanglement** between registers |
| **DEDUP** | one dictionary entry per repeated value (copying) | **shared** entangled reference (no-cloning forbids copying) — one Form, many Position-references |

> **The new model in one line:** *to record is to prepare a field of entangled dynamic triadic tokens; to reproduce is to measure it.* Reproduction is therefore not "reading bytes" but collapsing the recursive triadic state to the classical FPC record — i.e. **DECODE = MEASUREMENT** (and decoherence is the uninvited measurement; see §6).

---

## 4. RECURSIVE TRIADIC MAPPING IN SUPERPOSITION

> **Status: L3 / proposed architecture — NOT demonstrated** (cf. §11, ❓). No register-tree has been built or measured; §4–§5 are *design*, not validated results. The construction is also constrained by **no-cloning**: a shared-reference token tree cannot be freely copied, so the branching below is schematic, not an implemented data structure.

A Form may itself be a volume of sub-tokens; a Position may itself be a token. So the QTT mapping is **recursive and multidimensional**: $\mathrm{RTD}_q(V)$ decomposes $V$ into dynamic tokens, and any token whose internal complexity warrants it is decomposed again, to depth $d$. This realises the $N^d$ branching of `APPENDIX_NDT` (NDT-1) as a **register hierarchy**:

```
        |t⟩  (root token, qutrit-indexed, entangled)
       / | \
   |t_F⟩|t_P⟩|t_A⟩      each child is itself a dynamic triadic token
    /|\  /|\  /|\        ...recursed to depth d  →  up to N^d leaf tokens
```

For $N=3$ (classical/triadic) the tree branches by 3; on a coherence-paying substrate the tokens at each node may be superposed/entangled, lifting the construction to $N=4$ (anti-entropy) and $N=5$ (coherence) per NDT. **"Every Position is a dynamic token" is the base case of this recursion** — there are no leaf "values," only smaller tokens, down to the qutrit.

---

## 5. DYNAMIC CONSTRUCTIONS FROM QUANTUM TOKENS

Because tokens are processes, they compose into **dynamic constructions** — structures assembled, transformed, and queried while still coherent:

- **Action = gate.** The Action channel is realised by unitary gates (qutrit/qubit gates, controlled operations). Applying an Action transforms a token *in place*: $|t\rangle \mapsto U_A|t\rangle$. The "transform/relation" that FPC §5 (FPC-3) stored as a group element $g=(s,a)$ is, here, an actually-executed unitary.
- **Composition.** Tokens combine by tensoring + entangling: a construction is $|\Psi\rangle=\mathcal{E}\big(\bigotimes_i |t_i\rangle\big)$ where $\mathcal E$ is an entangling circuit encoding the links. Self-similar structure (FPC's strong case) becomes *symmetry* of $|\Psi\rangle$ — and symmetry is exactly what protects it (§6).
- **Query before readout.** Amplitude amplification (Grover-style) over a Form register $\sum_k\alpha_k|f_k\rangle$ performs a *quantum dictionary lookup*; the construction can be searched/edited dynamically before measurement, unlike a frozen classical record.

This is the operational meaning of *"dynamic constructions from quantum tokens"*: the record is a live circuit-state, not a file.

---

## 5.1 QTC-COMPILER — TPL → FPC → QTC → readout (verified)

The end-to-end toolchain is realized and tested (companion: `qtc_compiler.py`):

```
TPL clause ──parse──▶ FPC record (D_F, D_P, D_A, T) ──quantum lift──▶ shared Form = entanglement
   ▲                                                                          │
   └──── FPC ◀── readout (measure = decode) ◀── DFS-protected QTT ◀───────────┘
```

On a 3-clause TPL corpus (two clauses sharing one Form), the compiler builds the FPC dictionaries, lifts the **shared Form into a DFS entangled bond** (the link becomes physical, not an index), applies collective dephasing, measures (= decode), and reconstructs the TPL. Verified run (31 May 2026):

- **Lossless TPL round-trip:** OK (reconstructed clauses == normalized input).
- **Shared-Form link fidelity under collective dephasing (σ=1.2): 1.0000** (DFS-protected).
- **Link overhead:** classical FPC = 9 index bits; QTC = **1 ebit** for the shared-Form bond.
- Lift circuit transpiles to depth 5 on `['rz','sx','x','cx']`.

This closes the chain **TPL (surface) → FPC (classical record) → QTC (quantum, protected) → readout → reconstruction**: an FPC link can be carried as protected entanglement and decoded back losslessly. A ready-to-run hardware version (`qtc_hw_ibm.py`, IBM Quantum) awaits a saved API key (Phase 3).

---

## 6. QTC-1 — STABILIZATION REDUCTION BY RELATIONAL (DECOHERENCE-FREE) ENCODING

### 6.1 The honest version of the claim

> **QTC-1 (Relational Encoding ⇒ Reduced Stabilization).** If information is recorded in the **relational / shared-Form degrees of freedom** of entangled triadic tokens — degrees that lie in a **decoherence-free subspace (DFS)** of the device's dominant (collective) noise — then the *active* error-correction overhead needed to preserve it is reduced, because protection becomes intrinsic to the encoding rather than added on top.

**Why the naïve reading is false (and must be stated).** Arbitrary superposition is *more* fragile than a basis state, not less — superpositions dephase. So "superpositions reduce stabilization" is false in general. It is true for a *specific, structured* class of superpositions: those whose information sits in noise-invariant (symmetry-protected) subspaces. The triad supplies exactly such a structure, because in the canon **the Form-link is non-local by nature** (`APPENDIX_DP` FH-P3: "Entanglement = shared Form, not a signal through space").

### 6.2 The mechanism (verified in §8)

For the most common device noise — **collective dephasing** — the subspace $\mathrm{span}\{|01\rangle,|10\rangle\}$ (total spin-$z$ = 0) is a DFS: every state in it acquires only a *global* phase and is therefore physically unchanged. In triad language:

- $\{|01\rangle,|10\rangle\}$ = **one shared Form with two Position-references** (an entangled Form-link);
- collective dephasing = **Action leakage** (`APPENDIX_DP`: decoherence = Lindblad Action leakage, the $Z_A$ dissipation);
- a logical token recorded in this subspace is invariant up to global phase ⇒ **no active correction is needed against this channel**.

### 6.3 The currency reading (NDT)

`APPENDIX_NDT` §4.3 identifies quantum error correction as the **anti-entropy payment** $B_X$ (the $N=4$ currency): syndrome measurements export entropy to keep coherence ($B_Y$) solvent. QTC-1 says: **encode in subspaces the noise does not couple to, and the $B_X$ bill drops** — you pay less anti-entropy tax to keep the same coherence, because the dominant noise channel is *blind* to your logical information. Stabilization is not eliminated (other noise channels remain); it is *reduced* in proportion to how much of the information lives in the protected, relational structure.

> **Bookkeeping caveat (L2).** The $B_X / B_Y$ currency labels are framework *bookkeeping*: nothing measured in §8/§8.3 depends on them — delete every $B_X/B_Y$ and the quantitative results are unchanged. They organize the accounting; they add **no predictive power** over the standard QEC statement ("a DFS needs no active correction against the noise it is symmetric to").

---

## 7. THE QUANTUM ↔ TRIAD DICTIONARY (canon, `APPENDIX_DP`)

| Quantum phenomenon | Triadic translation |
|--------------------|---------------------|
| Superposition | a dynamic token off the basis axes (qutrit $\alpha|\mathsf F\rangle+\beta|\mathsf P\rangle+\gamma|\mathsf A\rangle$) |
| **Entanglement** | **shared Form** — the link made physical (one Form, many Position-references) |
| **Decoherence** | **Action leakage** (Lindblad / $Z_A$ dissipation) into the environment |
| **Measurement** | **reproduction = decode** — collapse to the classical FPC record |
| Decoherence-free subspace | a Form-link the collective noise is blind to ⇒ passive stabilization |
| Coherence currency $B_Y$ (NDT 5D) | the resource a QTT spends to stay dynamic |

---

## 8. VERIFIED DEMONSTRATION — DFS PROTECTION WITHOUT ACTIVE QEC

Pure-Python statevector simulation (stdlib only, deterministic). Two qubits; basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$. Collective dephasing $U(\theta)$: $|0\rangle\!\to\!e^{-i\theta/2}|0\rangle$, $|1\rangle\!\to\!e^{+i\theta/2}|1\rangle$ on each qubit.

**Measured result (run 31 May 2026):**

```
theta      F(DFS, shared-Form)   F(exposed)
 0.000                 1.0000       1.0000
 0.393                 1.0000       0.8536
 0.785                 1.0000       0.5000
 1.571                 1.0000       0.0000
 2.356                 1.0000       0.5000
 3.142                 1.0000       1.0000
------------------------------------------------
mean over grid         1.0000       0.6423
ASSERTS PASSED (DFS invariant; exposed collapses at theta=pi/2).
```

The shared-Form (relational) logical state $(|01\rangle+|10\rangle)/\sqrt2$ keeps **fidelity 1.0000 for every noise angle** with **no active correction**; the exposed state $(|00\rangle+|11\rangle)/\sqrt2$ degrades as $\cos^2\theta$ (fully collapsing at $\theta=\pi/2$). This is the concrete, established-physics core of QTC-1.

```python
"""QTC demo — recording in the shared-Form (relational) subspace is a
decoherence-free subspace for collective dephasing: protected with no active QEC.
Basis |00>=0 |01>=1 |10>=2 |11>=3.  Pure stdlib, deterministic."""
import cmath, math

def dephase(theta):                      # phase per basis index, collective dephasing
    ph = {}
    for q0 in (0, 1):
        for q1 in (0, 1):
            ph[2*q0+q1] = cmath.exp(-1j*(theta/2)*((1-2*q0)+(1-2*q1)))
    return ph

def apply_channel(state, theta):
    ph = dephase(theta)
    return [ph[i]*a for i, a in enumerate(state)]

def fidelity(psi, phi):                  # |<psi|phi>|^2
    return abs(sum(a.conjugate()*b for a, b in zip(psi, phi)))**2

inv = 1/math.sqrt(2)
psi_DFS = [0, inv, inv, 0]               # (|01>+|10>)/sqrt2  — one shared Form, two Positions
psi_EXP = [inv, 0, 0, inv]               # (|00>+|11>)/sqrt2  — exposed to collective dephasing
grid = [0.0, math.pi/8, math.pi/4, math.pi/2, 3*math.pi/4, math.pi]

print("theta      F(DFS, shared-Form)   F(exposed)")
sd = se = 0.0
for th in grid:
    fd = fidelity(psi_DFS, apply_channel(psi_DFS, th))
    fe = fidelity(psi_EXP, apply_channel(psi_EXP, th))
    sd += fd; se += fe
    print(f"{th:6.3f}     {fd:18.4f}   {fe:10.4f}")
print("-"*48); print(f"mean over grid   {sd/len(grid):18.4f}   {se/len(grid):10.4f}")
assert all(abs(fidelity(psi_DFS, apply_channel(psi_DFS, th))-1.0) < 1e-12 for th in grid)
assert fidelity(psi_EXP, apply_channel(psi_EXP, math.pi/2)) < 0.01
print("ASSERTS PASSED (DFS invariant; exposed collapses at theta=pi/2).")
```

> **Reading.** The demo proves the *mechanism*, not the full engineering claim. Real devices face more than collective dephasing (amplitude damping, leakage, correlated-but-not-collective noise), so QTC-1 predicts *reduced*, not *zero*, stabilization. Quantifying the real-device reduction is open work (§11).

---

## 8.1 PHASE-1 VALIDATION SUITE (density-matrix, numpy — run 31 May 2026)

Beyond the single round-trip of §8, a five-experiment density-matrix suite validates each triadic defense against a distinct noise channel. Standard Kraus channels (collective dephasing, independent phase-damping, amplitude-damping) plus a Gaussian quasi-static dephasing model; fully deterministic; **all asserts pass**. Companion: `qtc_validation_phase1.py`.

| # | Noise channel | Triadic defense | Measured result |
|---|---------------|-----------------|-----------------|
| A | Collective dephasing | **Form** — DFS / shared-Form (MELQ subspace) | F(DFS) = **1.0000** for every σ; exposed → 0.5000 |
| B | Independent dephasing / amp-damping | *(none — honest limit)* | DFS degrades too (F ≈ 0.85 at λ=0.3) — DFS is **not** magic |
| C | Amplitude-damping **jumps** | **Action** — total-Z parity / leakage check (P4) | jump heralded & removed; post-selected F = **1.0000**, yield = 1−γ |
| D | Residual quasi-static dephasing | **δ_q-triggered DD** (P3) | coh 0.139 (no DD) → **0.48 with 2 pulses**; CPMG-8 needs 8 pulses |
| E | (accounting) | **Holevo ledger** (P6) | ≤ log₂3 = 1.585 bits/qutrit retrievable; 0.50 infidelity avoided @ σ=1 |

**Readings.**
- The $\{|01\rangle,|10\rangle\}$ code is *simultaneously* the **collective-dephasing DFS** (Form, passive) **and** a **dual-rail amplitude-damping *detecting* code**: an excitation/photon-loss jump leaves the total-$Z=0$ subspace and is heralded by the parity (Action) check — so the post-selected logical state is exact ($F=1$) at the cost of yield $1-\gamma$. Passive Form-protection and active Action-detection are the *same* code read on two channels.
- **δ_q-triggered Dynamical Decoupling** matches dense CPMG's protection with **4× fewer pulses** by firing only when the imbalance metric $\delta_q$ rises — i.e. the SSS / LGP-10 δ-monitoring loop (`APPENDIX_SSS` §8.5) applied to coherence.
- The **Holevo ledger** keeps the claim honest: QTC buys *stabilization-tax reduction and structure*, **not** extra retrievable bits.

This moves the "DFS reduces active stabilization" claim from *asserted* to **simulation-demonstrated** (still L2 until validated on hardware — see §11; Phase 2 = a Qiskit/Aer transpiler of qutrit tokens onto qubit pairs).

---

## 8.2 PHASE-2 VALIDATION (Qiskit 2.4 / Aer — run 31 May 2026)

The Phase-1 mechanisms reproduce on **real Qiskit circuits**, with the qutrit-token → 2-physical-qubit transpilation made explicit. Companion: `qtc_phase2_qiskit.py`. All asserts pass.

| Part | What | Measured result |
|------|------|-----------------|
| 1 | Collective dephasing (shared `RZ(θ)`, Gauss–Hermite average over θ), DFS vs exposed | F(DFS) = **1.0000** ∀σ; exposed → 0.918 (σ=0.3) … 0.506 (σ=1.5) |
| 2 | Aer `NoiseModel` (amp-damping γ + phase-damping λ per qubit), DFS raw vs total-Z parity post-select | γ=0.2, λ=0.1: F_raw 0.760 → **F_ps 0.950** (yield 0.80) |
| 3 | Transpile to IBM-like basis `['rz','sx','x','cx']` | DFS prep: depth 5, `{rz:2, sx:1, cx:1, x:1}`; qutrit token: depth 9; \|11⟩ leakage-flag pop = 0 |

**Notes.**
- Part 2 is *more honest* than the idealized §8.1 Exp C: with phase-damping λ>0 present, the total-Z parity heralds the amplitude **jumps** (leakage out of the code) but **not** the within-subspace dephasing, so post-selected fidelity is high (0.93–0.98) yet not exactly 1 — the residual is precisely what δ-triggered DD / active QEC must address.
- The qutrit token compiles to a depth-9 hardware circuit; the unused \|11⟩ codeword is a zero-cost **leakage detector** (P4).

Together with §8.1 this places the "DFS reduces active stabilization" claim on a real circuit simulator (Aer). Remaining gap to L1 = execution on **physical hardware** (Phase 3 / MELQ 2-node, `APPENDIX_QC_NISQ` QC-P7).

---

## 8.3 PHASE-3 HARDWARE RESULT (IBM `ibm_marrakesh`, Heron r2 — 31 May 2026)

First real-QPU run (`qtc_hw_ibm.py`, Loschmidt echo: prepare logical |+⟩ → idle delay → uncompute → measure; 2048 shots), least-busy backend **ibm_marrakesh** (156-qubit Heron r2), job `d8e7mmbalsvc738vt5mg`:

| encoding | delay | P(\|00⟩) = logical fidelity |
|---|---|---|
| DFS | 0 µs | 0.9653 |
| exposed | 0 µs | 0.9712 |
| DFS | 40 µs | 0.2974 |
| exposed | 40 µs | 0.4199 |

$$R_\text{QTC}^\text{hardware}(40\,\mu s) = -0.211.$$

> **Honest negative result — and why it confirms (not refutes) the scope.** On this device the passive DFS encoding did **not** beat the exposed one; it was slightly *worse*. The {|01⟩,|10⟩} subspace is a DFS only for **collective** dephasing, whereas a fixed-frequency transmon's idle decoherence is **independent** T1/T2 — precisely the regime where §6.2 and QTC-BENCH T3/4 predict $R_\text{QTC}\to 0$. The two extra $X$ gates and T1-asymmetry (the exposed code carries a T1-stable |00⟩ component) push it slightly negative. **Passive DFS alone buys nothing against independent noise; only the active layer (DD + parity, §8.1–8.2) does.** A positive hardware $R_\text{QTC}$ requires a channel with the matching collective symmetry — engineered correlated dephasing, or **MELQ across separated nodes** (`APPENDIX_QC_NISQ` QC-P7), where shared environments make dephasing genuinely collective. This is the empirical boundary QTC-1 always claimed: *reduced, not zero — and only for matching noise symmetries.* Provenance: `IBM/qtc_hw_result_marrakesh.txt`.

**Phase-3b — collective-noise confirmation (same chip, `qtc_hw_collective.py`, job `d8e7r887jphs739kbh50`, 5 reps × 2048 shots).** Injecting a *collective* Z rotation $RZ(\theta)$ on both qubits (the matching noise symmetry):

| θ | P(\|00⟩) DFS (n=5) | P(\|00⟩) exposed (n=5) |
|---|---|---|
| 0 | 0.967 ± 0.005 | 0.964 ± 0.005 |
| π/4 | 0.969 ± 0.004 | 0.471 ± 0.010 |
| π/2 | **0.972 ± 0.003** | **0.011 ± 0.003** |

$$R_\text{QTC}^\text{hardware}(\text{collective},\,\theta{=}\pi/2) = +0.971.$$

The DFS is **invariant** under the collective rotation (flat ~0.97, only a global phase); the exposed code follows $\cos^2\theta$ and collapses to ~0.01 at π/2. **On the same real device, the shared-Form symmetry protection is real and near-total when the noise has the matching collective symmetry.** The two runs together **bracket QTC-1 exactly**:

$$R_\text{QTC}^\text{hardware} = -0.21\ (\text{independent idle noise}) \quad\longrightarrow\quad +0.97\ (\text{collective noise}).$$

Passive protection appears **precisely when, and only when, the noise symmetry matches the code** — the cleanest possible confirmation of the mechanism *and* its honest scope, on real hardware. QPU usage for the run: 18 s. Provenance: `IBM/qtc_hw_collective_marrakesh.txt`.

**Phase-3c — natural collective fraction (MELQ proxy, `qtc_hw_phase3c.py`, job `d8e7u2o7jphs739kbl3g`, 5 reps, idle delay-sweep, NO injection).** A true 2-chip MELQ needs quantum networking (unavailable on the free plan), so we instead test whether two qubits on one chip dephase *collectively by themselves*:

| idle delay | P(\|00⟩) DFS (n=5) | P(\|00⟩) exposed (n=5) | R_QTC(natural) |
|---|---|---|---|
| 0 µs | 0.960 ± 0.004 | 0.961 ± 0.003 | −0.03 |
| 20 µs | 0.669 ± 0.011 | 0.663 ± 0.010 | +0.02 |
| 40 µs | 0.512 ± 0.015 | 0.518 ± 0.009 | −0.01 |
| 80 µs | 0.374 ± 0.012 | 0.377 ± 0.009 | −0.01 |

$R_\text{QTC}^\text{natural} \approx 0$ within error at every delay — **DFS and exposed decay identically**, so the device's idle noise is essentially **fully independent** (natural collective fraction ≈ 0). (This clean multi-rep value supersedes the single-rep −0.21 of §8.3's first idle run, which was within qubit-choice/run variance.) **Practical reading:** on today's superconducting transmons, passive shared-Form/DFS encoding gives **no free benefit**; the useful regime requires a genuinely collective (shared-environment) channel — trapped-ion platforms, or a real 2-node MELQ with a shared bath. QPU usage 26 s (cumulative across the three runs ≈ 50 s of the 600 s budget). Provenance: `IBM/qtc_hw_phase3c_marrakesh.txt`.

---

## 8.4 A genuine qutrit DFS — how far the number 3 is load-bearing

**Status: L1 (numerical simulation, deterministic numpy) / L3 (interpretive claim).** Companion code: `qutrit_dfs.py`, `qutrit_dfs_verify.py`.

The §8 demonstration used a two-qubit dyadic DFS, span{|01⟩, |10⟩}. Reviewers correctly noted the qutrit / F–P–A "triadic" framing did no physical work there: the protected object was two-dimensional, so "3" was decorative. This section replaces that demo with a construction in which the number 3 is, in a precise and *limited* sense, load-bearing — and states plainly which parts of "three" are earned and which are not.

### Construction
Take two qutrits (spin-1, with $S_z$ eigenvalues $m\in\{+1,0,-1\}$). Subject both to the *same* collective dephasing $e^{-i\theta S_z}\otimes e^{-i\theta S_z}$ — the U(1) channel generated by total $S_z$. A coherence between basis kets of total magnetization $M$ and $M'$ is damped by $\exp(-\tfrac12\sigma^2(M-M')^2)$; any fixed-total-$M$ subspace is therefore a decoherence-free subspace (DFS). The **total-$M=0$ sector** is
$$\{\,|{+}1,{-}1\rangle,\ |0,0\rangle,\ |{-}1,{+}1\rangle\,\}\ -\ \textbf{3-dimensional},$$
an exact, no-overhead, leakage-free **logical qutrit**: three mutually coherent, equally protected levels.

### Verified numbers
- **Q1 — collective $S_z$ dephasing.** $F(\text{qutrit-DFS}) = 1.0000$ for $\sigma\in\{0,0.3,0.6,1.0,1.5,2.0\}$. The channel acts as the **exact identity on the entire 3-D block** (not just the symmetric state): over 2000 random pure logical states $\max|1-F| = 1.1\times10^{-15}$; over 500 random mixed logical states $\|\Phi(\rho)-\rho\|_F = 0$; the entanglement (process) fidelity on the DFS block $= 1.0000000000$. By contrast an *exposed* logical qutrit $\{|{+}1,{+}1\rangle(M{=}2),|0,0\rangle(0),|{-}1,{-}1\rangle(M{=}{-}2)\}$ decays $1.000\to0.813\to0.562\to0.394\to0.338\to0.333$, approaching the $1/d=1/3$ floor of a uniformly dephased qutrit (the floor itself encodes $d=3$).
- **Q2 — DFS dimension vs carrier dimension.** The total-$M=0$ sector of two carriers has dimension 2 (qubits), 3 (qutrits), 4 (ququarts). **Caveat (load-bearing):** the $M=0$ subspace of *four qubits* has dimension $\binom{4}{2}=6$ and is equally decoherence-free, so it *also* hosts a logical qutrit.
- **Q3 — honest limit.** Under *independent* (per-carrier) dephasing the qutrit DFS degrades identically to the exposed code ($F: 1.000\to0.895\to0.696\to0.501$). No free lunch.

### Resolving the three claims honestly
**(a) A true logical qutrit is protected — TRUE.** The protected unit is genuinely three-dimensional (three coherent, equally protected levels; exact identity on the whole block). Strictly more than the dyadic §8 demo. "Triadic" is load-bearing here *for the dimension of the protected information* — and only for that.

**(b) Qutrits are the minimal carrier — SOFTEN (not strictly necessary).** Two qutrits give the minimal *carrier count* (2) whose collective-$S_z$ $M{=}0$ sector is *exactly* 3-dimensional — a zero-overhead, exact-fit, leakage-free encoding. This is minimality/economy, **not necessity**: a logical qutrit also fits the 6-dim $M{=}0$ DFS of $\ge4$ qubits. Qudit carriers are **sufficient and natural, not required.**

**(c) Same DFS principle, not a new mechanism — CONCEDE.** The protection is the standard collective-dephasing / fixed-$M$-degeneracy DFS (Zanardi–Rasetti; Lidar–Chuang–Whaley), lifted to higher carrier dimension. The generator ($S_z^{\text{tot}}$), the channel (U(1)), and the DFS condition (one $M$-eigenspace) are identical to the qubit case. $F=1.0000$ is a *definitional consequence* of encoding into one $M$-eigenspace, not a new effect. There is **no $\mathbb{Z}_3$ / three-fold symmetry mechanism.**

### Honest verdict: is this "more than three numbers"?
**Earned:** a genuine 3-level protected logical unit (verified exactly), not a relabeled qubit — a real improvement over §8; the three levels are typed/non-permutable in an information reading; and "3 is complete" Peirce-style for *this carrier* (the $M{=}0$ sector of two qutrits is exhausted by exactly three states). **Not earned:** no new mechanism ("3" does informational/bookkeeping work, not protective work); not strict necessity (4 qubits also work); not a hardware result (L1 simulation; protects collective $S_z$ only — independent and collective-$S_x$ noise break it). 

> **In short:** the qutrit DFS makes "3" load-bearing for the **dimension of the protected object and the minimal carrier count**, and for nothing else. The criticism that triadic framing does no work on the *mechanism* still stands; what changes versus §8 is that the protected object is now honestly three-dimensional.

---

## 9. RESOURCE LIMITS & HONESTY (per RH)

- **Holevo bound (L1).** A qutrit yields at most $\log_2 3\approx1.585$ *retrievable* classical bits. QTC therefore gives **no unbounded lossless classical compression**. Its advantages are: compact representation of *correlated / non-local* structure (entangled links), in-place processing (quantum search/edit before readout), and reduced stabilization — **not** beating Shannon/Holevo for retrievable bits.
- **No-cloning (L1).** A superposed Form cannot be copied. Classical FPC dedup (copy identical forms into one entry) is replaced by **shared entanglement** (one Form, many Position-references) — which is precisely the canon's "shared Form." Consistent, but it constrains how dictionaries are built.
- **Threshold theorem (L1).** Below a noise threshold, fault-tolerant QEC works but is costly. QTC-1 *lowers the cost*, it does not repeal the theorem: passive (DFS/symmetry) protection covers the noise it is symmetric to; the rest still needs active codes.
- **Substrate requirement (NDT §3.2, L2).** A genuine QTT needs a coherence-solvent substrate (qutrits/qubits with $B_Y>0$). Classical simulation of QTT does not deliver the stabilization benefit — it only illustrates it (as §8 does).

---

## 10. INTEGRATION WITH THE U-THEORY CORPUS

| Component | Relationship to QTC |
|-----------|---------------------|
| `APPENDIX_FPC` | QTC is its **N=5 quantum lift**: dynamic tokens replace bits; entanglement replaces explicit links. |
| `APPENDIX_NDT` | Supplies the $N=3\!\to\!5$ family; QEC = anti-entropy ($B_X$) tax that QTC-1 reduces (§6.3). |
| `APPENDIX_DIM` | 5D = Coherence/Entanglement currency $B_Y$ — the resource a QTT spends. |
| `APPENDIX_DP` §DP-S6 / FH-QE | Entanglement = shared Form; decoherence = Action leakage; the quantum↔triad dictionary (§7). |
| `APPENDIX_QC_NISQ_TRIADIC_ARCHITECTURE` | The device-level triadic architecture QTC records onto. |
| `APPENDIX_TAA` | Form/Position/Action agents prepare and measure the corresponding registers; Σ-agent assembles links. |
| `APPENDIX_SSS` | Token balance (amplitude uniformity, $\delta$) scores representation stability (§2.1). |
| `APPENDIX_TPL` | The surface triadic language QTC stores in superposed, recursive form. |

---

## 11. FALSIFIABILITY MATRIX

| Prediction | Test | Status | If falsified |
|------------|------|--------|--------------|
| Shared-Form (relational) encoding is a DFS for collective dephasing | Statevector / hardware fidelity vs noise angle | 🟢 Demonstrated (§8) | Refutes the QTC-1 mechanism |
| Recording in DFS reduces *active* QEC overhead on real devices | Benchmark logical-qubit lifetime / syndrome rate, DFS-encoded vs exposed | 🟢 **Confirmed on hardware, noise-symmetry-gated** (§8.3, `ibm_marrakesh`): independent idle noise → R = −0.21 (no benefit); collective injected noise → **R = +0.97** (near-total). Sim agrees (§8.1, §8.2). Real-device *idle* benefit is 🟡 (needs collective noise / MELQ to be useful in practice) | Refutes QTC-1 only if R stays ≤0 under genuinely collective noise |
| Amplitude-damping jumps are heralded by total-Z parity (dual-rail) | Post-selected fidelity vs yield under amp-damping | 🟢 Demonstrated (§8.1 Exp C: F=1.0, yield 1−γ) | Refutes the leakage-detector patch (P4) |
| δ_q-triggered DD matches CPMG with fewer pulses | Pulse count vs coherence under quasi-static dephasing | 🟢 Demonstrated (§8.1 Exp D: 2 vs 8 pulses) | Refutes the adaptive-DD patch (P3) |
| Recursive triadic register hierarchy realises $N^d$ branching | Build small qutrit/qubit register tree; measure scaling | ❓ Awaits hardware | Refines NDT mapping at the data layer |
| Entanglement implements the FPC link with no index overhead | Encode an FPC record as an entangled state; reproduce by measurement | ❓ Open | Refutes the "link = entanglement" model |
| QTT respects Holevo / no-cloning | Theoretical | 🟢 Established | Would overturn known QM (not expected) |

---

## 12. WHAT THIS APPENDIX DOES NOT CLAIM (scope discipline, per RH)

- It does **not** claim superposition reduces stabilization *in general* — only relational/symmetry-protected (DFS) encoding does; arbitrary superposition is more fragile.
- It does **not** claim QTC beats classical compression on retrievable bits (Holevo forbids it).
- It does **not** claim QEC is unnecessary — only that part of the protection can be made intrinsic, reducing (not eliminating) active overhead.
- It does **not** claim a working QTT exists today; it specifies the architecture and the substrate requirement (NDT §3.2).
- Only §8's DFS demonstration and the §9 limits are L1; the codec architecture is L2; the real-device stabilization-reduction claim is L3.

---

## 13. RELATIONS TO OTHER APPENDICES

| Appendix | Provides | QTC uses it for |
|----------|----------|------------------|
| `APPENDIX_FPC` | Classical triadic codec, tokens, dictionaries | The structure being lifted to quantum (§2, §3) |
| `APPENDIX_NDT` | N-adic family, QEC = $B_X$ tax | N=5 lift; stabilization-as-currency (§6.3) |
| `APPENDIX_DIM` | Coherence currency $B_Y$ | The dynamic token's resource |
| `APPENDIX_DP` | Entanglement = shared Form; decoherence = Action leakage | The quantum↔triad dictionary (§7) |
| `APPENDIX_QC_NISQ_TRIADIC_ARCHITECTURE` | Triadic quantum device architecture | Recording substrate |
| `APPENDIX_RH` | Hardening / level tags | Guardrails on QTC-1 (§6.1, §12) |

---

## 14. ONE-LINE LAW

$$\boxed{\;\text{Record not in bits but in dynamic triadic tokens; write the relations in superposition, and the noise that is blind to those relations needs no correction.}\;}$$

> *Measured boundary (§8.3): true for **collective-symmetric** noise (hardware R = +0.97); for today's transmons' native **independent** noise the benefit is ≈ 0 (R ≈ 0 to −0.21). **Reduced, not zero — and only for matching symmetry.** Note also (§2.3): the validated code is a two-qubit (dyadic) DFS — "triadic" here names the information ontology, not the protection mechanism.*

---

## 15. REFERENCES

| # | Reference |
|---|-----------|
| [1] | Nikolov, P. (2026). `APPENDIX_FPC` — Triadic Compression (the classical FPA codec). |
| [2] | Nikolov, P. (2026). `APPENDIX_NDT`, `APPENDIX_DIM`, `APPENDIX_DP` (§DP-S6 / FH-QE), `APPENDIX_QC_NISQ_TRIADIC_ARCHITECTURE`. |
| [3] | Lidar, D. A., Chuang, I. L., Whaley, K. B. (1998). *Decoherence-Free Subspaces for Quantum Computation*. Phys. Rev. Lett. 81, 2594. |
| [4] | Knill, E., Laflamme, R., Viola, L. (2000). *Theory of Quantum Error Correction for General Noise* (noiseless subsystems). Phys. Rev. Lett. 84, 2525. |
| [5] | Holevo, A. S. (1973). *Bounds for the quantity of information transmitted by a quantum channel.* |
| [6] | Wootters, W., Zurek, W. (1982). *A single quantum cannot be cloned.* Nature 299, 802. |
| [7] | Nielsen, M., Chuang, I. (2010). *Quantum Computation and Quantum Information* (qutrits, threshold theorem, Lindblad decoherence). |

---

> *Appendix QTC — Quantum Triadic Codec (the pentadic / N=5 FPA token)*
> *U-Theory v26/v27 | © 2026 Petar Nikolov | CC BY 4.0 (content) · MIT (code)*
> *"Record with triadic tokens, not bits; write the relations in superposition."*

*End of APPENDIX QTC v1.0.*
