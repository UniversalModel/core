# Peer Review — APPENDIX_TRC_TRIADIC_CHEMISTRY.md

*Adversarial multi-lens review of APPENDIX TRC (Triadic Chemistry) v1.1 — full document (740 lines) read in full.*
*Source: `C:\--- u-score\v.28\.md\APPENDIX_TRC_TRIADIC_CHEMISTRY.md`*

---

## 1. Verdict + Score

**VERDICT: Accept-with-major-revisions as a *pre-registration / specification document*. Reject if read as a chemistry contribution.**

It is an unusually disciplined, self-falsifying instrument-design document whose dominant failure mode is *not* overclaiming (it has near-fanatically inoculated itself against that) but **scientific emptiness in the regime it cares about**, plus **a few load-bearing methodological holes the prose papers over.** The single biggest unresolved threat is internal: by the document's own admission, F/P/A are likely three transforms of one electronic-structure object, the geometric novelty only bites near a zero, and the constraint-screen already supplies the L3 veto — so the committed deliverable (§8) may pass its own gates and still teach chemistry nothing.

**AGGREGATE SCORE: 6.5 / 10** — high marks for epistemic hygiene, falsifiability architecture, and dual-use seriousness; substantial deductions for an under-powered / under-specified test battery, a statistically fragile core wager, and chemistry proxies that are partly wrong or non-operational.

---

## 2. What Is Genuinely NEW (the novelty map)

### 2.1 Genuinely new in TRC (not in TRB / TSE / SSS / NDT)

| # | NEW construct / claim | Chemistry-specific or liftable to canon? |
|---|---|---|
| A1 | **F/P/A registered onto matter**: Form = composition/bonding/stereochem/crystal-phase identity (price Time = decomposition/hydrolysis/racemization/polymorph transition); Position = phase/solvent/T-P-pH-redox/lattice-site fit; Action = reactivity/catalytic turnover/energy released. | **Chemistry-specific.** The *axing* (which observable owns which pillar) is new content; the F/P/A template itself is inherited. Not liftable — it is the domain registration. |
| A2 | **Action as two-sided AND task-relative band**: band-centred normalization, score 1 inside a declared useful-reactivity band, → 0 on *both* inert and runaway extremes. | **Partly liftable.** "Fails high and low" Action is a genuine refinement of canon's monotone "more Action = more capacity"; lifts to any domain with a runaway-vs-inert failure mode. Flag to canon. |
| A3 | **E_hull-as-Position (q/locus axing) + C1 two-thermo split**: elemental formation energy → Form/`f.thermo`; energy-above-hull → Position/`q`; explicit Fe₃C correction of the earlier "ΔH_f = E_hull" category error. | **Chemistry-specific** adjudication. The *meta-move* — logging a disclosed observable-to-pillar conflict as prima-facie non-separability evidence (→ TRC-P0d) instead of laundering it — is liftable as canon hygiene. |
| A4 | **Leaf-set δ⋆ redefinition**: δ over the FULL LEAF set (not the 3 top pillars), gated by `𝟙[min(L)<0.5]` so `SI = U/(1+δ⋆)²`. | **Liftable to canon.** Real correction to TRB's pillar-level δ: (i) leaf-level δ stops `q=0.01, c=1.0` being laundered as "balanced low Position"; (ii) `min<0.5` gate stops punishing competent-but-uneven nodes. Promote into TRB/SSS. |
| A5 | **Four-layer L1→L2→L3→L4 pipeline** (Design / Synthesis / Use / Society) with distinct objectives (`U_design`, `U_made`, `U_soc`) and **TRC-P9** (layer-distinctness is itself falsifiable). | **Chemistry-specific as instantiated**; the stratification *pattern* is liftable. "L4-can-override" is a re-skin of canon's B0 telos voice (see honest flags). |
| A6 | **L1 two-headed triadic search** `U_design = ∛(U_target·U_route·F_acc)`, target-(F,P,A) × route-(F,P,A), serial-AND `U_route = wgeomean_k(U_step_k)`, LGP-12 / DZ-1…DZ-12 with firewall gate FIRST. | **Mostly inherited, thinly new.** Engine is **TSE's A×B one-directional-grounded cross-product** re-skinned. NEW = the DZ-12 cycle + retrosynthesis content. Flag as largely re-skin of TSE §4. |
| A7 | **L3 materials-selection-as-triadic-fit** `U(task)=∛(F_fit·P_fit·A_fit)` vs **constraint-screened Ashby** (screen-then-index); narrow declared novelty = graded leverage-localization. | **Chemistry-specific.** Honest baseline (not a strawman weighted sum) and the *narrowed* novelty claim are genuine new domain content. |
| A8 | **Provenance classes [M]/[C]/[I]** (measured / computed-DFT-MD-QM / inferred-QSPR) + named sources (ICSD/MP/OQMD/COD/CCDC, NIST/JANAF, Pourbaix, ORD). | **Liftable refinement.** The 3-way taxonomy (esp. computed-DFT = "model output, not measurement") is sharper than canon's `provenance[]` and lifts to any computational domain. |
| A9 | **Cross-database robustness** (MP-on-hull can be OQMD/AFLOW-off-hull by >0.05 eV/atom → robustness must perturb across databases), folded into **TRC-P0b**. | **Chemistry-specific** in form, **liftable** in spirit: "robustness must perturb across independent reference sources, not just numeric jitter." |
| A10 | **ΔG-gates-extent-not-possibility (C6)** + phonon/Born rider (C7, 0 K necessary-not-sufficient capped input) + anchors `ref_lo/ref_hi` = "most consequential free parameters." | **Chemistry-specific.** Only liftable nugget: "a necessary stability check must never be equated with persistence." |
| A11 | **Chemistry falsifiers TRC-P0c / P0d / P0e** (leakage audit; no single DFT observable loads two pillars; Action⊥Position with task held fixed) + the **declared orthogonality threat** (task variable is in *both* A and P by construction → test conditional, not marginal). | **The most important genuinely-new methodological item.** P0e + "task contaminates two pillars by construction" is **liftable to canon** — a general two-axis non-separability hazard wherever axes share a design variable. |
| A12 | **Two B4 slots empty by intent** ("any B4 sentence is a bug"): (i) synthesis → process-safety/REACH-TSCA; (ii) deployment → LCA/environmental-fate. | **Chemistry-specific** mapping; the ladder is inherited. The *named, deliberately-empty* regulated tier is a new disciplinary move bound to chemistry's regulatory surface. |
| A13 | **TYPE-FORBIDDEN deny-list as objective constraint** (CWC Sched 1–3, energetics, BWC toxins, 1988-UN drugs, Stockholm POPs) — deny-list labels never routes; aggregate-retrospective-L4-cost-only; incidental-discovery halt-and-redact (E3); named human + export-control reviewer. | **Chemistry-specific** content. **Liftable firewall pattern:** the deny-list constrains the *objective* not just the output, and incidental hazard triggers halt+redact+log — strengthens TSE's output-level firewall. |
| A14 | **Two-level O5b closure at the substance boundary**: (1) no cross-substance worth ranking; (2) no cross-substance ℳ-aggregation **OR** `Priority` leverage-ranking (Priority/cost across substances reconstructs worth without the word). | **Re-skin with one new edge.** ℳ-firewall is **TSE's**; NEW = closing the **Priority/leverage** worth-laundering channel. That second-level closure is liftable. |
| A15 | **L4 separability liability named (R4)**: magnitude `U_soc` and polarity `T_soc` share the same harm registries (GBD/TRI/USEtox) → L4-P0 separability is weaker than chemical-entity separability. | **Liftable.** Honest "magnitude and sign draw on one source" admission; generalizes to any telos-bearing layer (TSE's ECO layer has the same latent problem). |
| A16 | **Chemistry recursion schema**: atom→…→material→formulation→reaction-as-edge-node→catalyst, each a `ChemSystem` triad; typed edges each loading exactly one axis; **additive/dopant/solvent = a node with a causal edge, never a scalar copied into the host.** | **Chemistry-specific.** Recursion-into-triads is inherited; NEW = the entity ladder + the "additive-is-a-node-not-a-scalar" rule (liftable only as the generic "context-modifiers are graph nodes, not flattened parameters"). |
| A17 | **Classical-coherence 5th slot** (long-range crystalline order / mesophase) as an aggregation-level quantity, gated by TRC-P8, logging disagreement with NDT's quantum-5th reservation. | **Chemistry-specific instance of an inherited amendment** (TRB §5.5.7: coherence = aggregation-level, biology "4.5/5"). New content (crystal order ↔ Kuramoto), not new structure. |

### 2.2 Inherited (re-skinned, no new theory)

`U=∛(F·P·A)` + geometric-zero keystone + F↔Time/P↔Space/A↔Energy + φ⁻¹ default / stakes-scaling (**SSS**); `δ`/`SI`/verdict bands 0.38/0.618 (**TRB §2.2**, modified to δ⋆ = A4); weak-zone scan + `Priority` + FDR/empirical-null discipline (**TRB §5.4**); `ℳ=∫U dt`, `𝒮=∫(1−U)dt`, MMT/MPI-1 (canon via **TRB §5.3 / TSE §1**); cross-node ℳ-firewall (**TSE §4.4**); two-headed one-directional grounding (**TSE §4.2** — A6); claim envelope + TESTABLE/INTERPRETATION/VISION cut + lint (**TRB §9.7 / TSE §9.9**); consensus-% / CI / neutral-50 / coverage / LOW_EVIDENCE (**SSS §SSS.3/§6 → TRB §5.1**, verbatim — **no new uncertainty mechanism in TRC**); SSS-Guard + retrodictive/prospective-no-pass split (**SSS §SSS.8.5 → TRB §6.6 / TSE §5.3**); 4th axis X=Freedom (**TRB §5.5/§A.4**); 5th coherence slot (**TRB §5.5.7**); N-adic ladder (**NDT §2/§3**); symmetric-retirement contract (**TRB §9.8**); B0–B4 rename (inherited device); structural falsifiers P0/P0b/P1/P2/P4/P7/P8/P9 (inherited skeleton — only P0c/P0d/P0e new); RUO/"deliverable-is-the-battery" posture (inherited).

### 2.3 Honest flags — only relabeling despite looking new

- **A6** — strip retrosynthesis vocabulary and it is TSE's A×B one-directional cross-product; DZ-12 is new procedural detail, not a new coupling mechanism.
- **A14** — the aggregation half is pure TSE; only the Priority/leverage second-level closure is novel.
- **A17** — domain re-instantiation of TRB's existing coherence amendment; new content, not new structure.
- **"L4 can override L1–L3"** — flagged in TRC itself as B0/VISION, a value choice, not a B1 theorem; canon civilizational-telos voice re-skinned.
- **B0–B4 rename + P-gate skeleton** — inherited; only P0c/P0d/P0e/P9-as-applied and B4-empty-×2 are new.

### 2.4 Genuinely-liftable-to-canon shortlist (recommend promoting out of TRC)

1. **A4** — leaf-set δ⋆ with the `min<0.5` gate (fixes a real laundering bug in TRB's pillar-level δ; domain-agnostic).
2. **A11** — P0e + "task variable contaminates both Action and Position → test conditional not marginal separability."
3. **A2** — two-sided / task-relative Action band (canon's Action is monotone).
4. **A13/A14** — firewall as a constraint on the *objective* + closing the Priority/leverage channel + incidental-discovery halt-redact.
5. **A8** — the [M]/[C]/[I] provenance taxonomy (computed ≠ measured).

**Bottom line:** TRC's genuinely-new core is (i) the chemical *axing* of F/P/A incl. E_hull→Position and the C1 two-thermo split (A1/A3), (ii) the four-layer design→synthesis→use→society stratification with TRC-P9 (A5), (iii) materials-selection-as-triadic-fit vs constraint-screened Ashby (A7), (iv) the leaf-set δ⋆ fix (A4), and (v) the chemistry falsifiers P0c/P0d/P0e plus the "task contaminates two pillars" threat (A11). **On uncertainty/confidence specifically, TRC contributes nothing new** — every mechanism is verbatim SSS/TRB inheritance.

---

## 3. Strengths

1. **Pre-registered symmetric retirement with named deletions (§8 table; §9.9; §A.0).** Every gate names what a *failed* falsifier REMOVES, and TRC-P0 failure deletes §3–§6 outright. A chemistry-modeling paper that pre-commits to self-destruct on its own existential test is rare and genuinely good science. (Inherited from TRB §9.8 but correctly specialized.)

2. **The separability threat is foregrounded, not buried (§2.1 declared orthogonality threat; §2.5 data-independence warning; §9.10-1,2).** The document states *before any data* that Action and Position share a task variable by construction, that DFT-derived Action is a transform of Form, and that conditional (not marginal) testing is mandatory. Normally a reviewer must extract this admission; here it is the thesis.

3. **The E_hull category-error correction (§2.5, §2.8, C1/C2).** Distinguishing elemental formation energy (Form/`f.thermo`) from E_hull (Position/`q`) is chemically correct; the prior draft's "ΔH_f = E_hull = +0.055" was a real error now properly fixed. Folding the felt-ambiguity into TRC-P0d instead of laundering it is intellectually honest.

4. **The two-level O5b-chem closure (§6.4).** Recognizing that banning the *word* "worth" is insufficient because `Priority = Δℳ/cost` across substances reconstructs the worth ordering — and therefore banning the cross-substance ℳ-aggregation *operation* — is the correct closure, enforced at the type level (§9.8 lint-4).

5. **ΔG-gates-extent-not-possibility (§2.6, C6).** Scoring `ΔG_op` at operating activities against a yield/extent anchor, refusing "ΔG° ≥ 0 ⇒ Action = 0," is correct thermodynamics and avoids a classic undergraduate error.

6. **Dual-use firewall is architecture, not a disclaimer (§6.5, §9.7, §9.8).** Sign-symmetric leverage named as the hazard; sign-flip method deliberately undescribed; incidental-discovery halt with redaction; `FORBIDDEN_PENDING_REVIEW` default-deny; classification handed to a named human + export-control reviewer. Materially better than the typical "RUO" sticker.

---

## 4. Prioritized Issues

### 4.1 Blockers (must fix before the deliverable can be claimed sound)

**B1 — The §8 battery is pre-registered but NOT powered; the power claim is asserted, not demonstrated (§8 banner, §7 P0 row).** The document repeatedly says "a power calc precedes each test," but never gives a single n estimate or effect-size target. Conditional dCor/CMI at the *family* level (per R8) collapses effective sample size by 1–3 orders of magnitude — there are only ~10²–10³ well-characterized inorganic systems with cross-database hulls AND measured outcomes. With a pre-committed 0.6–0.8 "inconclusive" dead-band, the realistic outcome of TRC-P0/P0e is **"not yet decidable,"** so §3–§6 are neither admitted nor deleted; they hang. A pre-registration that cannot, at achievable n, exit its own dead-band is not yet a pre-registration. **Fix:** supply the actual power analysis — target effect size, family-level n, the CI width that clears 0.8 — for at least TRC-P0 and TRC-P4, or downgrade the deliverable to "design of a test that needs a data-acquisition project first."

**B2 — TRC-P0b's own escape hatch makes the geometric-vs-additive win nearly unwinnable as stated (§2.2 worked contrast; §8 P0b; §9.10-4).** Geom ≈ arith away from zeros, so the win must isolate to the "one-low-pillar subset." But on a bounded/normalized/clamped [0,1] feature set, genuine zeros are produced almost entirely by the constraint screen / anchor choice, not by chemistry — and §5.3 concedes the screen supplies the veto. So the residual ΔR² on the near-zero subset risks being a test of anchor placement, not non-compensation. **Fix:** P0b must hold anchors fixed across the geometric and additive arms AND show the near-zero subset is populated by chemically-real collapses (a measured inert-when-reactivity-required case), not clamping artifacts; state the minimum cell count for ΔR² ≥ 0.1 to be estimable.

**B3 — `U_robustness` (the L2 verdict pillar) is undefined as a computable object (§4.2).** L2's verdict `U_made = ∛(U_product·U_route·U_robustness)` depends on a process-window/yield-robustness pillar that is not derivable from the snapshot databases the document restricts itself to (it needs a calibrated process model or DoE — exactly what §9.10-5 / the V3 row admit do not exist). So a third of the most safety-critical layer's score is non-computable from any data TRC permits itself; either it defaults to neutral-0.50 (making L2 degenerate) or it silently imports the non-runnable V3 twin. **Fix:** state explicitly that `U_robustness` is `LOW_EVIDENCE`/neutral under snapshot-only constraint, and move L2 below the deliverable line with L1's route-search until V3 exists.

### 4.2 Majors

**M1 — Phonon/Born stability is mishandled as merely "capped" (§4.3, C7 rider).** 0 K dynamical stability is necessary-not-sufficient and DFT gives spurious imaginary modes — but the deeper problem is unaddressed: TRC's flagship Fe₃C and its whole metastability story rely on kinetically-trapped, above-hull phases (as do diamond, most steels, austenite, many cathodes). A 0 K phonon/Born check rewards the ground-state structure, frequently the *wrong* phase for the application; capping the input doesn't fix the sign of the error. **Fix:** down-weight or exclude phonon stability for any node flagged metastable-by-design, or `f.structural_integrity` systematically penalizes exactly the materials the framework most wants to score well.

**M2 — `P = √(q·c)` and the leaf-δ fix are in mutual tension (§2.2, §2.5).** Form's `F = wgeomean(f.thermo, f.kinetic_persistence)` with the Fe₃C `F = √(0.55·0.95) ≈ 0.72` shows a 0.55/0.95 split survives because `min(L)=0.55 ≥ 0.5` so δ⋆=0. Intended — but it means non-compensation is **only active below 0.5**, making the framework a thresholded screen with a geometric skin above 0.5, i.e. closer to constraint-screened Ashby than the novelty claim admits. **Fix:** state plainly that non-compensation is a sub-0.5 phenomenon and re-scope the novelty; TRC-P0b should report the fraction of decision-relevant candidates that ever fall below 0.5 on any leaf.

**M3 — Provenance class [I] (inferred/QSPR) is flagged but not quarantined the way [C] is (§2.5).** DFT-derived Action is correctly excluded from the separability claim, but logP/logS (RDKit Crippen, group-contribution) are QSPR models trained on the same structural descriptors that define Form, and they feed Position/`c`. They are flagged [I] but not excluded from P0 the way [C] Action is — the identical confound at the Form↔Position boundary that was only closed at Form↔Action. **Fix:** [I]-class Position proxies must be excluded from (or audited identically in) TRC-P0/P0d, or P0 passes on a Form↔Position leak named at §2.5(b) but not operationally closed.

**M4 — L4-P0 is conceded weaker than chemical separability, then still listed as a go/no-go gate (§6.2 R4, §8 L4-P0).** Magnitude `U_soc` and polarity `T_soc` share GBD/TRI/USEtox; the "held out where data permit" hedge does enormous work, but in practice the harm registries *are* the data. L4-P0 is structurally likely to fail or stay in the dead-band, retiring the societal triad to "a single contested aggregate." **Fix:** state the expected outcome up front (L4 likely collapses to one contested lifecycle aggregate), the way L3's "the screen already supplies the veto" is stated, so L4 is not oversold as a four-pillar societal model.

**M5 — Cross-database hull perturbation (the strongest robustness idea, §4.3) is asserted but not operationalized into a pass/fail rule (§8 P0b).** A compound on-hull in MP can be off-hull in OQMD/AFLOW by >0.05 eV/atom — right, and the best chemistry insight on anchors — but P0b just says "survives cross-DB correction-scheme perturbation" with no tolerance. Given 0.05 eV/atom swings flip `q` from 1.0 to <0.5 (across the M2 threshold), cross-DB perturbation alone could make the verdict bimodal for a large fraction of candidates. **Fix:** define the criterion quantitatively (e.g. "U-verdict band invariant under MP/OQMD/AFLOW hull substitution for ≥X% of candidates"), or the robustness gate is decorative.

### 4.3 Minors

- **m1 — `F_acc` binning: the geometric combine of `open → "low"` is unspecified (§3.2.2).** `{closed, partial, open} → {1.0, 0.5, → low}`; "→ low" is hand-waved, yet it controls whether open-catalogue targets are killed or merely penalized in `U_design = ∛(U_target·U_route·F_acc)`. Pin the value.
- **m2 — Missing-observable → neutral 0.50 interacts badly with the δ⋆ < 0.5 trigger (§2.2, §4.3).** A strong 0.95 leaf plus a missing leaf imputed near 0.50 can trip δ⋆ purely from data sparsity, not chemistry. The coverage/LOW_EVIDENCE machinery mitigates but the interaction is unstated.
- **m3 — The Fe₃C worked node hand-asserts `f.thermo ≈ 0.55`, `c ≈ 0.90`, Action band `≈ 0.88` (§2.8).** Correctly illustration-only, but since these are the most consequential free parameters, one sensitivity line (dropping any below 0.5 flips SI via δ⋆) would make the honesty rider concrete.
- **m4 — "Reaxys-class" sources (§2.5, §3.4, §9.6) are proprietary/licensed** yet listed as primary descriptors. For a reproducibility-oriented pre-registration, the battery should be runnable on open data (ORD/MP/OQMD/ICSD) alone, or state which gates are blocked without licensed corpora.
- **m5 — Ashby normalization `ref_hi = best attainable in the candidate set` (§5.3 M3 rider) makes `A_fit` candidate-set-dependent** — the same material's L3 fitness changes with the pool; flag this non-stationarity alongside `F_acc`'s catalogue-relativity.
- **m6 — RUO is asserted, but L1's DZ-10 emits `queue_for_lab` (§3.3).** The boundary between `queue_for_lab` and actionable wet chemistry rests entirely on the lint refusing conditions/quantities; state explicitly that the queue payload is scrubbed of operational detail.
- **m7 — Recyclability/end-of-life is double-counted as both an X/Freedom proxy (§2.4) and an L4 societal-Action benefit (§6.6 steel "recyclable").** Minor, but it muddies the gated 4th-axis independence test (TRC-P7).

---

## 5. On the Proposed Gaussian Stability Matrix (GSM) — adversarial assessment

The GSM is proposed as a drop-in **§2.9**: a distributional re-statement of the §2.2 primitives. Each point pillar-score becomes a **logit-normal** belief (Gaussian on the log-odds `z = logit(s)`, mapped back by the logistic), the twelve cells of a 4-layer × 3-pillar matrix are stacked into one multivariate normal `z ~ 𝒩(μ, Σ)`, beliefs propagate through the **unchanged** keystone `U = ∛(F·P·A)` by Monte-Carlo (K ≥ 10⁴, delta-method as a validated screen), and the output is a credible interval plus a failure probability `P_fail = P(U < φ⁻¹)`.

### Is it sound? — Largely yes, on its own narrow terms.

- **The link choice is honest and correct.** Modelling the Gaussian on log-odds, not on `[0,1]`, avoids mass outside the support and the false symmetry of a raw Gaussian on a bounded score. The "Gaussian" name is made faithful (on `z`, never on `s`).
- **Backward-compatibility is a genuine constraint, not a slogan.** Setting `μ_ij = logit(s_ij^point)` so that `Σ → 0` reproduces the §2.2 number exactly (the GSM ⊂ §2.2 limit) is a real, testable guard.
- **Non-compensation is preserved sample-by-sample.** Running the unchanged geometric keystone per draw means a cell with mass near 0 collapses the *whole posterior* of `U` — the keystone's defining property survives the distributional lift, which is the central design requirement.
- **It does not pretend to fix separability — it displays it.** `Σ` parameterizes the failure of separability as covariance: `ρ_FPA` ingests the measured conditional dCor/CMI from TRC-P0/P0e; `ρ_layer` reads TRC-P9. If P0 fails, `ρ_FPA → 1`, the posterior degenerates to a near-point with no triadic structure — the honest output, and the signal that §3–§6 are deleted. This correctly refuses to let GSM rescue a failed test.
- **The real affordance is well-motivated.** Distinguishing **known-low** (`P_fail ≈ 1`, tight) from **high-uncertainty** (`P_fail ≈ 0.5`, wide) as a *number*, and re-stating leverage as `ΔP_fail / cost` so that "buy-evidence" (shrink `τ`) and "intervene structurally" become comparable on one axis, is the one genuinely new thing GSM adds over the point-SI scan. It is also the principled discharge of SSS-L4.
- **Inheritance and firewall are respected.** GSM consumes (does not duplicate) coverage/consensus/provenance/neutral-50 as the diagonal `D`, and the P0/P0e/P9 statistics as the off-diagonal `R`. The O5b cross-substance prohibition is explicitly preserved (no cross-substance `ΔP_fail/cost`), the deny-list/halt/lint bind intervals and `P_fail` exactly as point scores, `P_fail` is rendered model-internal (never a physical hazard probability), and the L4 sign `T_soc` is not modelled by `Σ`. GSM is B1-pending and symmetric-retired by its own GSM-P1.

### What to fix (adversarial)

1. **GSM inherits B1's fatal problem and does not escape it.** GSM-P1 is a reliability-diagram calibration at the *same* family-level unit of independence (R8). `R` has up to **66 free off-diagonals** estimated at the same 10²–10³-class n that already cannot exit the §8 dead-band. Calibrating a 12-dimensional covariance at that n is *strictly harder* than the marginal P0 test that B1 already shows is under-powered. The honest status of GSM is therefore **"not yet decidable"** for the same reason TRC-P0 is — and GSM-P1 should say so with an explicit power/ECE-resolution analysis, or GSM is itself a funding proposal, not a runnable layer. *(This is the single most important GSM fix; it mirrors the document's own B1.)*

2. **The small-n correlation default is double-edged and under-disclosed in consequence.** Ledoit–Wolf/OAS shrinkage toward `R → I` is the right default, but shrinking toward independence makes `U`'s interval **narrower than reality** when true correlations are positive — i.e. it understates risk in exactly the separability-compromised regime TRC cares about. The mitigation (report at both `R̂` and a conservative `R_hi`, flip ⇒ `axis_unseparated`) is correct and should be made **mandatory and load-bearing**, not a §2.9.7 caveat — otherwise GSM's intervals are systematically over-confident at achievable n.

3. **The delta-method screen is unreliable precisely where it matters.** The document admits the Taylor expansion of `ln σ` and `ln U` breaks down near the zeros — the non-compensation regime. The stated rule (anything AT-RISK/CRITICAL is re-scored by Monte-Carlo) is sound, but the screen then buys little over just running MC, since the candidates that matter all fall through to MC anyway. Keep it only if the logged max-discrepancy gate is enforced; otherwise drop it as false economy.

4. **Bimodality is out of scope but is the chemically common case.** A polymorph that is "either stable or not" is genuinely bimodal; a single logit-normal cannot represent it and will report a misleadingly unimodal posterior. This is acknowledged but should be elevated to a named exclusion in the renderer (flag bimodal-suspect cells rather than silently averaging them).

5. **`τ` parameters multiply the free-parameter surface.** `τ_floor, κ, λ, ν, τ_LOW` are perturbed in TRC-P0b alongside the anchors — correct — but this widens an already-fragile robustness test (M5/B2). State the joint perturbation budget; otherwise P0b is asked to certify robustness over a parameter space it cannot cover at the available n.

**Net GSM verdict:** the *design* is sound, honest about its link function, faithful to the keystone and the firewall, and correctly scoped as canon-general (lift candidate) with a TRC-specific instance. Its decisive weakness is **not** conceptual but **evidential and identical to the document's own B1**: a 12-cell covariance cannot be calibrated at family-level n any more easily than the marginal P0 it sits on. Accept GSM as a gated, B1-pending §2.9 *only* if GSM-P1 ships the power/ECE-resolution analysis and the `R̂`-vs-`R_hi` over-confidence guard is made mandatory.

---

## 6. Single Most Important Change

**Supply the actual power / effect-size analysis for TRC-P0 and TRC-P0b at the declared family-level unit of independence, and state honestly whether the battery is decidable on currently-available open data — or reclassify the deliverable from "runnable pre-registered test" to "design of a test that first requires a data-acquisition project."**

Everything else is downstream of this. The document's entire epistemic edifice — symmetric retirement, B3-pending ceiling, "the §8 battery *is* the deliverable" — rests on the claim that these tests can actually be run and can actually pass or fail. But by the document's own three concessions (F/P/A are likely transforms of one structure; geom ≈ arith away from a zero; the screen already supplies the L3 veto), combined with a pre-committed 0.6–0.8 dead-band and a 1–3 order-of-magnitude n-collapse from family-level independence, the overwhelmingly probable real outcome is **"not yet decidable"** — neither the clean falsification that would honorably delete §3–§6, nor the pass that would license them. A pre-registration that most likely returns "inconclusive" is not yet a deliverable; it is a funding proposal for the data collection that would make the deliverable possible. Saying so plainly would be fully consistent with the document's own (admirable) honesty contract — and is the one change that would move it from 6.5 toward 8. *(The GSM extension does not relieve this; GSM-P1 inherits the identical, and harder, calibration problem — §5.)*
