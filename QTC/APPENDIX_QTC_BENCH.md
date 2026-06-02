# APPENDIX QTC-BENCH — BENCHMARK PROTOCOL FOR TRIADIC QUANTUM RECORDING
## Turning QTC-1 from a DFS demonstration into a measurable engineering program — the FPC → QTC → NDT bridge

> *"FPC measures where structure repeats; QTC tests whether repeated structure can be made physically protected."*
> — Petar Nikolov, May 2026

---

**Author:** Petar Nikolov · **Date:** 31 May 2026 · **Framework:** U-Theory v26/v27
**Status:** L1 (simulation results & physical bounds) · L2 (benchmark protocol & token-stability score) · L3 (QTC-2 coupling on real hardware)
**Prerequisites:** `APPENDIX_QTC` (the codec), `APPENDIX_FPC` (classical base), `APPENDIX_NDT` (N-adic), `APPENDIX_DP` §DP-S6, `APPENDIX_SSS`, `APPENDIX_QC_NISQ` (MELQ)
**Companions (runnable):** `qtc_bench.py` (this suite), `qtc_validation_phase1.py` (§8.1 of QTC), `qtc_phase2_qiskit.py` (Qiskit/Aer)
**Function:** Defines the measurement objects that move QTC from architecture toward an empirical program. Centerpiece: **QTC-2**, the prediction that classical compressibility forecasts quantum protectability.

> © 2026 Petar Nikolov · CC BY 4.0 (content) · MIT (code)

---

## 0. EXECUTIVE SUMMARY

`APPENDIX_QTC` proved a *mechanism* (decoherence-free, shared-Form encoding survives collective noise with no active correction). QTC-BENCH makes that mechanism **measurable**: a benchmark suite (run 31 May 2026, all asserts pass) that quantifies how much stabilization the triadic encoding actually saves, where it stops working, and — most importantly — whether a dataset's **classical FPC compressibility predicts its quantum protectability** (the **QTC-2** hypothesis). Headline simulated result: across a structure sweep, FPC compressibility $C_\text{FPC}$ and the stabilization-tax reduction $R_\text{QTC}$ co-move with **Spearman 0.983** (strictly monotonic, saturating once everything is protectable).

---

## 1. QTC-D2 — TERNARY IN ALPHABET, PENTADIC IN SUBSTRATE

A common confusion: *if the token is a qutrit, why call QTC "N=5"?* The two N's are different and both correct.

> **QTC-D2 (Two distinct N).** The Quantum Triadic Token is **ternary in alphabet** — its type-selector lives in the 3-dimensional space $\{|\mathsf F\rangle,|\mathsf P\rangle,|\mathsf A\rangle\}$ (a qutrit). QTC is **pentadic in substrate solvency** — the substrate additionally pays the anti-entropy currency $B_X$ (active QEC) and the coherence currency $B_Y$ (entanglement) of `APPENDIX_NDT`/`APPENDIX_DIM`.
>
> $$\boxed{\text{QTT is ternary in alphabet (qutrit }\Sigma_3\text{), pentadic in substrate solvency }(B_S,B_T,B_E,B_X,B_Y).}$$

The triad $\{$Form, Position, Action$\}$ is the *information* alphabet; $X$ (anti-entropy) and $Y$ (coherence) are *substrate* currencies the carrier must pay, not extra symbols.

---

## 2. THE BENCHMARK PROTOCOL

| Test | What it measures | Expected | Defense exercised |
|------|------------------|----------|-------------------|
| **T1** DFS vs exposed lifetime | fidelity decay under collective dephasing | DFS invariant; exposed decays | Form (DFS) |
| **T2** DFS + amplitude damping | boundary of protection | DFS no longer fully protected | (limit) |
| **T3/4** Imperfect collective | robustness curve $R_\text{QTC}(\eta)$ + active tax $B_X$ | partial protection 1→0 | Form + Action |
| **T5** FPC→QTC→readout | can an FPC link become entanglement? | reconstruction fidelity + link overhead | link = entanglement |
| **QTC-2** Compressibility vs protectability | $C_\text{FPC}$ vs $R_\text{QTC}$ across structure | monotonic positive coupling | the whole bridge |

---

## 3. MEASURED RESULTS (`qtc_bench.py`, 31 May 2026 — all asserts pass)

**T1 — Lifetime under collective dephasing.** F(DFS) = **1.0000** for every σ (steps 0–5); F(exposed) → 0.50. The collective channel is blind to the shared Form.

**T2 — Amplitude-damping boundary.** F(DFS) = 1.00 / 0.90 / 0.80 / 0.70 / 0.50 at γ = 0 / 0.1 / 0.2 / 0.3 / 0.5. DFS is **not** protected against this non-collective channel — the honest limit that mandates an active layer.

**T3/4 — Imperfect-collective robustness & tax reduction.**

| η (independent fraction) | F(DFS) | F(exposed) | $R_\text{QTC}$ |
|---|---|---|---|
| 0.0 | 1.0000 | 0.5002 | **1.000** |
| 0.2 | 0.9700 | 0.5008 | 0.940 |
| 0.4 | 0.9400 | 0.5036 | 0.879 |
| 0.6 | 0.9100 | 0.5167 | 0.814 |
| 0.8 | 0.8800 | 0.5767 | 0.716 |
| 1.0 | 0.8500 | 0.8500 | **0.000** |

$R_\text{QTC}$ runs from 1 (pure collective → full passive protection) to 0 (pure independent → no advantage) — exactly the "reduced, not zero" stabilization claim.

**T5 — FPC link → QTC entanglement → readout.** Reconstruction fidelity of a shared-Form link under collective dephasing = **1.0000**. Link overhead: classical FPC = 2 index bits (two tokens referencing one $D_F$ entry); QTC = **1 ebit** (the entanglement *is* the link, and it is DFS-protected). The classical link becomes a physical, protected correlation.

---

## 4. QTC-2 — RELATIONAL COMPRESSION–STABILIZATION COUPLING (centerpiece)

> **QTC-2.** The more a dataset's FPC representation compresses by **shared Forms and repeated relational Actions**, the more efficiently its QTC lift can be placed into symmetry-protected / DFS-like relational degrees of freedom — so the active correction tax falls:
> $$C_\text{FPC}\uparrow \;\Rightarrow\; B_X^\text{QEC}\downarrow \quad\text{(for a matching relational noise model).}$$

**Test design (two independent pipelines).** $C_\text{FPC}$ is computed by FPC bit-accounting; $R_\text{QTC}$ by a density-matrix noise simulation (shared-Form groups → DFS-protected units; unique Forms → exposed units) under imperfect-collective noise (η=0.25; per-protected-unit gain 0.925). Swept over a structure parameter $p$ (0 = all-unique/random → 1 = fully tiled):

| p | n_forms | $C_\text{FPC}$ | protected frac | $R_\text{QTC}$ |
|---|---|---|---|---|
| 0.0 | 48 | 0.862 | 0.000 | 0.000 |
| 0.1 | 44 | 0.907 | 0.167 | 0.154 |
| 0.3 | 34 | 1.058 | 0.583 | 0.539 |
| 0.5 | 26 | 1.268 | 0.917 | 0.848 |
| 0.6 | 21 | 1.405 | 1.000 | 0.925 |
| 1.0 | 3 | 2.710 | 1.000 | 0.925 |

$$\textbf{Spearman}(C_\text{FPC}, R_\text{QTC}) = 0.9832,\qquad \text{Pearson} = 0.7048.$$

**Reading.** The coupling is **strictly monotonic** (Spearman 0.98): more compressible → less active correction. It **saturates** once `protected_fraction = 1` — you cannot protect more than 100% of units, so $R_\text{QTC}$ plateaus at 0.925 while $C_\text{FPC}$ keeps climbing (1.4 → 2.7); that ceiling is what depresses the *linear* Pearson to 0.70. Spearman is the correct statistic for the "more → more" claim.

**Status & falsifier.** Supported **in simulation (L2)** — Spearman 0.98 on synthetic data, and on **real files** (gzip ratio vs simulated $R_\text{QTC}$) Spearman 0.99 (Pearson 0.83). **Caveat:** the QTC-2 pipeline on real data still uses a *noise simulation*, not hardware logical-error metrics. The genuine test is the same experiment on hardware (Phase 3 / MELQ 2-node) under a truly collective noise channel: if the monotonic coupling vanishes on real devices, **QTC-2 is falsified.**

---

## 5. $R_\text{QTC}$ — THE STABILIZATION-TAX REDUCTION RATIO

$$R_\text{QTC} = \frac{B_X^\text{exposed} - B_X^\text{DFS}}{B_X^\text{exposed}}, \qquad B_X \approx 1 - F \;(\text{the infidelity the active layer must repair}).$$

- $R_\text{QTC} = 0$ → no benefit (noise fully non-collective);
- $R_\text{QTC} = 1$ → complete passive protection (noise fully collective);
- realistic regime: $0 < R_\text{QTC} < 1$ for partially-matching noise symmetries.

This keeps the claim honest: QTC does **not** say "no QEC needed"; it says "the active $B_X$ tax drops by $R_\text{QTC}$ for noise the relational encoding is blind to."

---

## 6. QTC-SSS — TOKEN STABILITY SCORE (pentadic)

Extending the FPC/SSS aggregator $U=\sqrt[3]{U_F U_P U_A}$ to the five currencies a QTT pays:

$$U_\text{QTT} = \sqrt[5]{\,U_F\,U_P\,U_A\,U_X\,U_Y\,}, \qquad
\delta_\text{QTT} = \frac{\max_i U_i - \min_i U_i}{\max_i U_i + \epsilon}, \qquad
SI_\text{QTT} = \frac{U_\text{QTT}}{(1+\delta_\text{QTT})^2}.$$

| Component | Meaning |
|-----------|---------|
| $U_F$ | identity / Form fidelity |
| $U_P$ | address / context (Position) localization fidelity |
| $U_A$ | gate / Action fidelity |
| $U_X$ | entropy-export / QEC efficiency (anti-entropy) |
| $U_Y$ | coherence / entanglement preservation |

**Non-compensatory** (geometric mean): high entanglement $U_Y$ must **not** mask low gate fidelity $U_A$ — a single failing currency collapses $U_\text{QTT}$, exactly as in SSS/NDT. This turns a quantum recording into a *measurement object*.

---

## 7. NOISE → TRIADIC FAILURE TAXONOMY

Making the `APPENDIX_DP` dictionary operational, not only interpretive:

| Quantum noise | Triadic interpretation | Currency failure | Protection |
|---|---|---|---|
| Collective dephasing | Action leakage **blind to shared Form** | $B_X$ tax if unprotected | **DFS** (Form) |
| Amplitude damping | loss of **Action** capacity | Energy/Action decay | QEC / relaxation codes + parity heralding |
| Leakage out of code space | **Position** escape | Space/Position failure | leakage-reduction units / \|11⟩ flag |
| Measurement crosstalk | unwanted **reproduction** | premature decode | shielding / basis control |
| Non-Markovian memory noise | **Form** history contamination | Time/Form drift | dynamical decoupling |

---

## 8. THE QTC NO-GO BOX (RH hardening)

```
QTC DOES NOT:
1. store infinite classical information   (Holevo: <= log2(3) bits per qutrit);
2. clone quantum Forms                     (no-cloning);
3. remove active QEC                        (only reduces the B_X tax by R_QTC);
4. make ARBITRARY superposition stable      (only relational/symmetry-protected encodings);
5. prove cosmic dimensional ascent          (NDT pathway is L3, separate);
6. replace Shannon compression              (FPC/QTC factor structure, not raw entropy);
7. claim present-day hardware suffices       (needs coherence-solvent substrate; Phase 3).
```

---

## 9. DEPENDENCY GRAPH (FPC → QTC → NDT)

```
CORE invariant   Form↔Time · Position↔Space · Action↔Energy
        ↓
FPC              triadic record (D_F, D_P, D_A, T)            [classical]
        ↓
QTC              dynamic QTT  Σ c_fpa |f⟩|p⟩|a⟩               [qutrit alphabet]
        ↓
DFS / shared-Form encoding   passive protection vs matching noise
        ↓
lower B_X tax (R_QTC), preserved B_Y coherence                [pentadic substrate]
        ↓
NDT              N=5 substrate pathway
```

No inverted-mapping error: the canon **Form ↔ Time, Position ↔ Space, Action ↔ Energy** is preserved, with Coherence/Entanglement as the N=5 currency $B_Y$.

---

## 10. FALSIFIABILITY MATRIX

| Prediction | Test | Status | If falsified |
|---|---|---|---|
| DFS lifetime invariant under collective dephasing | T1 | 🟢 Demonstrated (F=1.0 ∀σ) | refutes the DFS mechanism |
| DFS bounded by amplitude damping | T2 | 🟢 Demonstrated (decays with γ) | would over-state protection |
| $R_\text{QTC}$ runs 1→0 with noise non-collectivity | T3/4 | 🟢 Demonstrated | refutes "reduced not zero" framing |
| FPC link encodable as DFS-protected entanglement | T5 | 🟢 Demonstrated (recon F=1, 1 ebit) | refutes link=entanglement |
| **QTC-2:** $C_\text{FPC}$ predicts $R_\text{QTC}$ | sweep | 🟡 **Simulation: Spearman 0.98**; hardware pending | refutes the FPC→QTC bridge |

---

## 11. RELATIONS & INTEGRATION

| Appendix | Role |
|---|---|
| `APPENDIX_QTC` | The codec QTC-BENCH measures (§8.1/§8.2 are its first validations). |
| `APPENDIX_FPC` | Source of $C_\text{FPC}$; QTC-2 links its compressibility to protectability. |
| `APPENDIX_NDT` | The N=5 substrate; $B_X$/$B_Y$ currencies that $R_\text{QTC}$ and QTC-SSS account. |
| `APPENDIX_DP` §DP-S6 | The noise→triad dictionary made operational (§7). |
| `APPENDIX_SSS` | Parent of QTC-SSS (non-compensatory geometric mean). |
| `APPENDIX_QC_NISQ` | MELQ = the shared-Form DFS realised across nodes (hardware path, Phase 3). |

---

## 12. ONE-LINE LAW

$$\boxed{\;\text{FPC measures where structure repeats; QTC tests whether repeated structure can be made physically protected.}\;}$$

---

## REFERENCES
Burch (1991) Peircean Reduction · Lidar, Chuang, Whaley (1998) DFS · Knill, Laflamme, Viola (2000) noiseless subsystems · Holevo (1973) · Wootters & Zurek (1982) · Nielsen & Chuang (2010). U-Theory: `APPENDIX_QTC`, `APPENDIX_FPC`, `APPENDIX_NDT`, `APPENDIX_DIM`, `APPENDIX_DP`, `APPENDIX_SSS`, `APPENDIX_QC_NISQ`.

---

*Appendix QTC-BENCH · U-Theory v26/v27 · © 2026 Petar Nikolov · CC BY 4.0 / MIT*
*"FPC measures where structure repeats; QTC tests whether repeated structure can be made physically protected."*

*End of APPENDIX QTC-BENCH v1.0.*
