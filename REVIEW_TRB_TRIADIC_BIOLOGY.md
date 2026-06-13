# Peer Review — APPENDIX_TRB_TRIADIC_BIOLOGY.md

*Handling editor's consolidated review, synthesizing six referee reports (cell/molecular biology; computational-systems biology & data engineering; statistics/ML methodology; U-Theory canon consistency; adversarial completeness/falsifiability; scientific editing & publication-readiness).*

---

## 1. Verdict

**Major revisions required.** Aggregate score: **6.2 / 10.**

What this document honestly *is*: an unusually disciplined, self-aware **specification and pre-registration** — not yet a result, and not yet a finished appendix. Its epistemic hygiene is genuinely ahead of most work in this genre (it front-loads its own kill-switch, demotes FBA from measurement to model-output, names pseudoreplication and compositionality before a critic can, and mechanizes a level-inflation lint). But the same six referees converge on one structural fact: **by the document's own logic chain, its headline deliverable — "the weakest pillar names the disease mechanism" — rests on a precondition (F/P/A separability) the authors themselves rate as probably-false, against a most-weighted pillar (Action) they concede is unmeasured at single-cell scale.** The runnable tests (P0, P0b, P8) are the real product; the marketed product (per-cell mechanism triage) is deferred past every runnable test. The science is salvageable and in places excellent; the manuscript is honest about almost everything except the gap between what it tests and what it sells.

---

## 2. Top strengths (most genuine, across reviewers)

1. **P8 (coherence / fibrillation) is a legitimately clean, near-non-circular, runnable-now test.** Ventricular fibrillation is a system-output collapse while per-node Action stays above zero, so any predictive lift from the Kuramoto order parameter *r* cannot be an F/P/A relabelling. Its input (optical-mapping / ECG synchrony) is structurally independent of the transcriptome. Five of six referees single this out as the single best thing in the document. (§5.5.2, §8.5)

2. **§8.4's concession that the most-weighted pillar is unmeasured is the document's best moment of integrity.** It openly states Action/Energy — self-declared "the most important" — has no atlas-scale single-cell measurement and is filled by FBA, which is a model *prediction* (assumed objective + stoichiometry), not data, and it prices that confound honestly. Most frameworks never admit this.

3. **The Vₘ → Action re-axing genuinely de-circularizes the flagship ischemia example.** Moving resting potential / ion gradients out of Position (where it was downstream of Action) and rebuilding ischemia on perfusion is biologically correct (resting potential *is* continuously-paid Na/K-ATPase energy) and removes a circularity that would have made P2 self-confirming. (§0/A1, §2.6, §5.4)

4. **The statistical hardening (R3/R7/R8) is unusually competent for this genre.** Rejecting Pearson *r* for distance-correlation / conditional MI; CLR for compositional scRNA; empirical-null + FDR for the argmin-over-10⁴-nodes look-elsewhere problem; and — most importantly — naming the **donor, not the cell, as the unit of independence** (pseudoreplication). These are the exact errors most single-cell preprints commit. (§8.5)

5. **Phase 0 is correctly ordered and the kill-switch is front-loaded.** The separability ablation runs *ahead* of the headline geometric-vs-arithmetic test, with the explicit willingness to call a collinear result "the most valuable possible negative" and STOP. The canon inheritance is also faithful where checked: the SSS geometric-zero keystone, the GSI-RTD `TriadicDomain` interface (verified verbatim), and the Meaning–Stupidity identity ℳ+𝒮=T are correctly carried.

---

## 3. Prioritized issues (deduplicated, merged across reviewers)

### BLOCKER

**B-1. The headline deliverable is conditional on a precondition the authors rate as probably-false, leaving no committed product.** *(§1, §2.5, §7, §8.3; raised by the adversarial-completeness, biology, and data-engineering lenses.)*
The thesis is "weakest pillar names the mechanism." But §2.5/O8 demote it to a hypothesis conditional on correct proxy-axing; §4.2/§8.3 concede F/P/A are "largely three transforms of one transcriptome" and call collinearity "likely"; and §7 states that if they are collinear the architecture "has no independent inputs to be non-compensatory over" → STOP. The flagship feature therefore depends on a chain whose first link the authors expect to break.
**Fix:** Either (a) **rename the thesis** from a mechanism-triage engine to "a pre-registered test of whether F/P/A are separable in atlas data, and whether system-level coherence is non-compensatory" — make the *runnable tests* the product — or (b) name one organ system with **measured** (not FBA-inferred) Action at single-cell scale and commit to running the full mechanism-localization claim there now, accepting falsification.

**B-2. Action — the most-weighted pillar — is computed *from* the Form pillar's data, so the central separability claim is broken by construction, not merely "maybe correlated."** *(§4.2, §5.1, §8.3, §8.4; data-engineering and biology lenses, with statistics concurring.)*
Context-specific FBA (GIMME / iMAT / tINIT / Compass) takes the transcriptome as its **input**. So Action-from-FBA is a deterministic function of Form's expression data — not a correlate. A Phase-0 |r| or even dCor/MI test can *pass* while the two axes are one axis transformed twice, because a lossy LP bottleneck hides functional dependence from these statistics. Every U that multiplies an FBA-Action against an expression-Form multiplies a number by a transform of itself. The same shadow afflicts the Freedom proxy (CytoTRACE is transcriptome-derived) and pLDDT (a reference-level, cell-*invariant* fold confidence, not an in-cell folding measurement — a category error as a per-cell Form proxy).
**Fix:** Name the FBA integration method explicitly and **exclude transcriptome-derived FBA-Action from the input-independence claim**. Either restrict Phase-0 Action to **measured** Action (Seahorse OCR/ECAR, respirometry, metabolomics) where it exists, or prove input-independence by showing FBA flux predicts held-out *measured* flux better than expression alone on the same cells. Replace pLDDT with an in-cell proteostasis readout (aggregation reporters, thermal proteome profiling) or drop the per-cell fold-integrity claim.

**B-3. The INTERPRETATION/TESTABLE register is a structural unfalsifiability shield for the entire currency-4/5 layer.** *(§9.1, §9.2, §9.7, §2.4, §5.5; adversarial-completeness lens.)*
A claim becomes TESTABLE only *after* its falsifier passes and "renders no number" while INTERPRETATION. Therefore a falsifier can never falsify the claim it gates: if P6/P7/P8 fail, Freedom and Coherence simply stay in INTERPRETATION forever, having committed to nothing and lost nothing. The document spots this for P5 but not for the whole five-currency layer built into the same apparatus.
**Fix:** Add a **symmetric retirement rule**. For each deferred currency, pre-register what a *failed* falsifier RETIRES, not only what a passed one admits — e.g. "If P7 fails, Freedom is **removed** from the ledger and from §5.5, not parked in INTERPRETATION." Deferral-to-falsifier is a motte that can never be stormed without it.

**B-4. The headline falsifier table is stated on the linear statistic the document itself declares invalid.** *(§8.2 / §8.5; statistics lens.)*
The §8.2 P0/P7 rows still set thresholds on Pearson |r| ("|r| > 0.8", "mean pairwise |r| < 0.6", "|r(Freedom,Form)| > 0.8"), directly contradicting the R3 hardening in §8.5 ("the independence tests above must not rest on Pearson *r* … a low Pearson *r* is not evidence of independence"). The patch updated the prose but never the pre-registered criteria. A reader executing the pre-registration runs the wrong test.
**Fix:** Rewrite every P0/P7/P8 success/falsifier cell to state thresholds on the chosen normalized dependence statistic (dCor or normalized CMI on CLR/ILR features, conditional form), delete every "|r|" from those columns, and pre-register the exact estimator, bandwidth/k-NN settings, and feature set, since these thresholds are estimator-dependent in a way Pearson *r* is not.

### MAJOR

**M-1. The decisive gate (P0) is likely un-decidable at the donor *n* the document's own R8 mandates, and it tests the wrong quantity anyway.** *(§8.2, §8.3, §8.5; statistics lens.)*
R8 sets the unit of independence at the donor (tens), and R3 pre-commits the 0.6–0.8 band as "inconclusive, never a pass." A dCor/CMI estimate on n≈20–50 donors — biased and high-variance at small *n* — will, in most realistic cases, straddle that dead zone, so the "try to kill the load-bearing assumption first" posture cannot fire. Separately, low pairwise input-dependence is **neither necessary nor sufficient** for non-compensatory U to be useful: the real question is whether each pillar adds held-out predictive variance for an *independent fragility outcome given the other two*.
**Fix:** Do the power calculation **now**: state the minimum donor *n* at which a dCor/CMI CI excludes both 0.6 and 0.8, and whether any existing atlas supplies it. If none does, demote P0 from "runnable-now mandatory gate" to "currently underpowered — the foundational test cannot yet be run." Reframe P0 as a *necessary screen* and make the *decisive* gate the conditional-incremental-validity test (conditional ΔR² against external fragility truth, with the FBA confound and leakage audit controlled).

**M-2. Definitional leakage via the cell-type annotation: "one dataset → one axis" is really "one annotation → three axes," invisible to any statistical separability test.** *(§4.2, §4.3; data-engineering lens.)*
The cell-type label propagates into f.identity (Form), the expected niche/compartment (Position), and the chosen functional program / FBA cell-model (Action). All three pillars share one upstream cause, manufacturing correlation that is *definitional*, not biological — and undetectable by §8.3. The same applies to the edge layer: SIGNALS_TO (Position) and INDUCES_ACTION (Action) re-typed from one NicheNet/CellChat ligand→target inference are perfectly correlated by construction.
**Fix:** Add a **shared-upstream-feature audit** to Phase 0: trace every proxy to its raw measurement and flag any value derived from the annotation. Score pillars from disjoint raw feature sets where possible (Position-context from spatial-neighbor composition independent of the focal cell's own type; Action from measured flux). State in §4.2 that "one annotation → three axes" is itself an open separability liability, and note in §4.3 that the two re-typed edges are not independent evidence.

**M-3. The digital twin is asserted "runnable now" but is research-grade and contradicts the document's own snapshot admission.** *(§6.2, §7 P1–P3; data-engineering lens.)*
Organism/organ-scale coupled dynamic-FBA + reaction-diffusion + slow-damage with calibrated cross-layer constants does not exist; the RD layer's diffusion/consumption constants are unmeasured at per-cell-type resolution; the `dδ/dt = k_entropy − k_repair·U` law has no source for its rate constants; and the layers span the ms-to-years timescales §5.5.6 itself flags as un-co-integrable. "Runnable now" contradicts §8.4-4's admission that atlases are snapshots, not trajectories — you cannot calibrate a dynamic twin from snapshots.
**Fix:** Downgrade the twin. The KG + static per-node scoring (P1) may be runnable; the coupled three-layer *dynamic* twin is research-grade (mark it like P5). Declare the cross-layer coupling constants and their data sources (or admit they are free parameters), state the multiscale integration scheme, and concede the trajectories are illustrative, not validated, tying this to the §5.5.6 timescale-aliasing concern.

**M-4. The patch round left the 4th-currency (X / Freedom) gated by two different falsifiers in different sections.** *(§2.4 + glossary X-row → P6; vs §5.5.1, §5.5.4, §8.5, glossary Freedom-row → P7; adversarial-completeness and publication lenses; confirmed in source.)*
P6 (§8.2, line 580) is a **time-ordering** test (does X decline before Form damage under infection); P7 (§8.5, line 607) is a **statistical-independence** test (does Freedom carry information independent of Form). The same object — explicitly "the §2.4 X-axis, named" (line 422/426) — is told to a reader as unlocked by both. The §2.4 note and glossary X-row say "until P6"; lines 55, 426, 449, 607, 749 say "until P7."
**Fix:** Decide the relation and state it once. Most defensibly: **P7 (independence) gates admission** of U₄ to a rendered number, and P6 (time-ordering) is a separate downstream claim about infection dynamics. Update the §2.4 note, line 580, and both glossary rows so every cross-reference names the same gate, and add one sentence at the P6/P7 site stating they gate the same axis on different questions.

**M-5. The five-currency completion is scope-creep that the document shows makes its own decisive test harder, with no offsetting runnable deliverable.** *(§5.5; adversarial-completeness lens.)*
§5.5.4 states plainly that adding Freedom and Coherence "makes the Phase-0 separability problem strictly harder, not easier." Currency 4 renders no number until P7; currency 5 is conceded not to be a per-node pillar at all (a naive U₅ is "a category error") and renders nothing until P8. The completion adds zero to the runnable per-node engine, raises the bar on the gating test, and widens the dual-use surface — justified only by "canon coherence," which §9.6/§10 elsewhere call a *chosen*, non-unique frame.
**Fix:** Move §5.5 to an explicitly optional appendix-within-the-appendix and gate the entire five-currency layer behind P0/P8 passing first. Do not complete the ledger until the three-currency core is shown separable.

**M-6. P8's cleanliness does not generalize, and at tissue scale it tests the coherence currency, not the per-node F/P/A model.** *(§5.5.2, §8.5; biology and data-engineering lenses.)*
The Kuramoto *r* is a parent-level electrophysiology measurement available essentially only in heart (optical mapping/ECG) and brain (EEG) — ~2 of dozens of organ systems. A cardiac pass therefore validates a relational order parameter and the aggregation operator, **not** the per-node leaf triad, and does not license a coherence term in the roll-up for the unmeasured majority of nodes. (Two minor biology corrections ride along: in *sustained* VF per-cell energetics also collapse, so "Action well above zero" applies to early VF only; and the conjunction "three matched modalities × independent hearts × tight ΔR² CI" is exactly the regime R8 calls underpowered — name the dataset and donor *n*.)
**Fix:** State that the coherence roll-up term is admissible only for nodes with a **measured** parent-level order parameter; elsewhere it is UNKNOWN (open-world) and must not silently default to 1.0. Confine P8's positive result to electrophysiological tissues, report coherence coverage as a fraction of nodes, and run the R8 power calc on ΔR²≥0.1 at the real donor *n* before calling P8 "runnable now."

**M-7. Several worked-example numbers smuggle measurements the document elsewhere says it cannot make.** *(§5.4 ischemia P.context→0.18; §5.5.1 Freedom proxies; biology lens.)*
The ischemia example assigns a confident P.context = 0.18 from "capillary distance up, local pO₂ down" — but per-cell pO₂ and perfusion territory are **not** single-cell-resolved in any cited atlas (§8.4-3 concedes the Position graph is *inferred*). The non-circularity gained by dropping Vₘ was real, but it traded a circular-but-measurable proxy for a non-circular-but-unmeasurable one, unflagged. Likewise reprogramming-barrier height is a population/cell-type assay, not a per-node observable, so the "per-node 4th pillar" is at best a per-cell-*type* annotation.
**Fix:** State that ischemia P.context is, in current data, a hypoxia-**response** transcriptional signature (HIF targets, glycolytic shift) inferred from the cell's own Action/Form — which reintroduces a circularity the document must own — and do not present 0.18 as if perfusion were measured per cell. Demote reprogramming-barrier height to a per-cell-type annotation.

**M-8. The empirical-null / FDR machinery is under-specified in ways that can silently break the very control R7 was added to provide.** *(§5.4, §8.5; statistics lens.)*
The document does not state what is shuffled against what; label-shuffling that does not preserve the donor structure (R8) or the pillar covariance under H₀ is non-exchangeable and miscalibrates q-values. Filtering to `genuinely_imbalanced` *before* FDR using the same SI statistic the FDR then evaluates is post-selection inference that invalidates BH. Separately, **no family-wise/FDR control exists across the headline battery** (P0–P8, multiple tissues/atlases) — the same look-elsewhere logic R7 applies to nodes applies to the test suite.
**Fix:** Specify the resampling unit (donor-level, per R8) and what is permuted (preserving pillar covariance under H₀); use a selection-independent filter or a selective-FDR (conditional BH) procedure; report a uniform-p QQ calibration check as a deliverable. Add a study-level multiplicity plan that declares the full family of tests/tissues up front and controls FDR across the battery.

**M-9. Test thresholds and the geometric-vs-arithmetic result are analyst-chosen free parameters with no power link, and the keystone normalization is half-fixed.** *(§5.5.5, §5.5.6, §8.2, §8.3; statistics, adversarial, and biology lenses.)*
ΔR²≥0.1, the 0.6/0.8 bands, ρ≥0.5, R²≥0.3, the ±20% anchor envelope, AUC≥0.70 are magic numbers; the document disciplines anchors with perturbation but not the *thresholds themselves*, leaving a goalpost surface. Worse, §5.5.5 concedes Action *also* has a two-sided regime (excitotoxicity, ROS over-production) the one-sided ramp under-models — so a **core pillar**, not just a deferred currency, can score a hyperactive/excitotoxic cell as healthy, and §5.5.6 admits the normalization "is doing all the work" of making pillars multipliable, meaning the geometric-zero keystone is partly an artifact of analyst-chosen band *shape*.
**Fix:** Derive each threshold from a stated minimal meaningful effect + power at realistic donor *n*, or pre-register them fixed with a ±50% sensitivity analysis. Apply the band-centred normalization to the Action pillar **now** (it affects rendered U₃), and extend P0b's pre-registration to perturb the functional *form* of normalization (ramp ↔ logistic ↔ trapezoid), not only ±20% anchor values.

**M-10. P5 (the whole-organism weak-zone map) is admitted unfalsifiable and the proposed fix does not restore falsifiability.** *(§7, §A.2; adversarial-completeness lens.)*
A missed weak zone "can always be blamed on an omitted node." The coverage-saturation criterion (∂Coverage/∂n < ε) only tests whether *adding* nodes stops changing coverage; it is silent about the zones the scan *excluded*, because a missed zone is one never scored.
**Fix:** Replace coverage-saturation with an **adversarial planted-lesion recall test**: hide a known clinically-important vulnerable cell type from the scan's node set and verify the leverage ranking degrades measurably — real recall on planted ground truth, not internal convergence.

**M-11. Two unsourced/contradicted canon citations, and a misstated canon ladder, slip past the RH discipline the appendix is built on.** *(§5.5.3, §9.2, §A.4, §A.6, §10; canon-consistency lens; verified against sources.)*
(a) TRB cites QTC native-noise correlation as **R ≈ −0.21** (§5.5.3 line 439, §10 line 708). The in-corpus source (QMC §184, attributing the experiment to QTC §8.3) reports **R ≈ 0** under native noise; −0.21 appears nowhere else in the corpus and is presented as an established sibling result underpinning a "transfers verbatim" argument. (b) The canon RH ladder is misstated: TRB calls canon L0 "metaphor" and L1 "within-model proof," but RH_CRITICAL_REVIEW §71–75 defines **L0 = Meta-evaluation, L1 = Operational stability, L2 = Cross-domain analogy, L3 = Cosmological, L4 = Literal physical** — so the B1→canon-L1 mapping is wrong. (c) TRB claims to "obey" NDT while amending NDT's uniform per-node U_N formula (splitting into a leaf + a relational currency) and scoring biology on currency 5 via *classical* Kuramoto sync, where NDT reserves the 5th for quantum substrates ("nothing classical can") and places biology at N=4.
**Fix:** Replace −0.21 with the sourced **R ≈ 0** (cite QMC §7 / QTC §8.3 with accession), and soften "transfers verbatim." Quote the canon RH ladder verbatim and re-derive the B0–B4 mapping against the real definitions. State plainly that TRB **amends** NDT-1 (non-uniform lifting; leaf-vs-relational currencies) and that NDT should be updated — drop the claim biology "obeys" NDT — and reconcile the classical-coherence-as-5th-currency choice with NDT's quantum-exclusive 5th.

### MINOR

**m-1. Externalize the patch history and dissolve the inline "(fix …)" scars.** *(§0; publication lens.)* Three stacked changelogs (R1–R10) plus ~60–80 inline `(fix A1/E2/D3 …)` tags reference a critique taxonomy never defined in the document. Delete §0 (replace with a one-line "Revision history: see TRB-CHANGELOG"), and let each corrected statement simply *be* the statement.

**m-2. Cut redundancy ~35–45% and add a "how to read this" map.** *(whole document; publication lens.)* The five-currency caveats are restated 5+ times (header, §A.4–A.6, §0, §5.5.x, §8.5, §9.3, §10, glossary); "anchors are free parameters" appears in §2.2/§5.1/§5.5.6/§8.3. Pick one canonical home per caveat, collapse §5.5.1–5.5.7 into ~three, trim the glossary to one-line definitions (move the R6/R7/R8/R10 mini-essays to the changelog), move §1 Thesis above §A, and add an audience map (implementers: §3–§7; reviewers/ethics: §8–§9; corpus maintainers: §A, §10).

**m-3. Disambiguate ATP-rate from ATP-level in the anchor example.** *(§5.1; biology lens.)* "0.3× ATP is normal for a quiescent lymphocyte" conflates low ATP *turnover/OCR* (true) with 30%-of-normal ATP *concentration* (near-catastrophe in any viable cell). Pick proxies actually low in quiescence (OCR, biosynthetic flux) and drop the implied 0.3× steady-state [ATP].

**m-4. Give contact inhibition one home.** *(§2.5, §5.1; biology lens.)* It is loaded both as per-node Position-context *and* as the cancer coherence-collapse signature — the cross-axis double-loading the document bans (K2/E2). Assign it to the relational/coherence quantity OR per-cell niche-dependency, not both.

**m-5. Recharacterize the somite-clock example.** *(§2.5, §5.5.5; biology lens.)* The segmentation clock is high local coherence with a controlled spatial phase gradient (a travelling-wave *mode*), not "partial desynchronization." It does not support the "too-little-coherence is normal" leg; use functional segregation in cortical dynamics instead, or describe it correctly.

**m-6. Carry the §2.4 "X-proxies near-immeasurable at single-cell scale" caveat into P6/P7.** *(§2.4, §8.5; biology lens.)* Telomere length, NAD⁺, autophagic flux, and DNA-repair competence are not in scRNA atlases; specify that X-proxy tests run only on population/bulk or live-imaging modalities, conceding the 4th pillar is populated at coarser granularity than F/P/A — which the U₄ product silently mixes.

**m-7. State the combinatorial anchor problem and the fallback behavior.** *(§2.3, §5.1, §8.3; biology lens.)* State-conditioning (cell-type × cycle × diff-stage × circadian × activation) multiplied by per-cell-type anchoring yields thousands of anchors no reference data can populate. Specify the fallback when a (cell-type × state) cell lacks a fitted anchor, and tag any score against a defaulted/un-conditioned anchor as low-confidence — otherwise the §8.3 ablation perturbs anchors that were never conditioned.

**m-8. Pre-register the CLR composition and the proxy-reassignment set.** *(§8.5, §8.2 P2-mech; statistics lens.)* CLR/dCor inherits the arbitrariness of the reference feature set and pseudocount (a new p-hacking surface); pre-register the composition, zero-handling, and a positive control (known-independent and known-redundant features). "Stable under documented proxy reassignment" is unfalsifiable until the finite candidate re-axing set and a stability statistic with a pass threshold are enumerated.

**m-9. Pick one operationalization of "separability."** *(§6.1, §8.3; statistics lens.)* Statistical dependence (dCor/CMI) and "siloed agents reach atlas performance" measure different things; low siloed performance could mean noisy proxies, not entangled axes. Make conditional-incremental-information primary; demote the agent test to a secondary diagnostic with its confound stated.

**m-10. Acknowledge the O5 divergence from SSS and source the SI/δ primitives.** *(§9.3-O5, §2.2; canon lens.)* SSS *does* score and rank a named individual (Ivan P., U=0.8364) and sells cross-system comparability; TRB's O5 reverses this. Say "we diverge from SSS here, on purpose (the eugenics attractor)" rather than implying O5 is inherited. Separately, `SI = U/(1+δ)²` and `δ=(max−min)/(max+0.01)` are not in APPENDIX_SSS — label them TRB-introduced derived primitives or cite the real source.

**m-11. Rename biology's 5th currency "Coherence" and report 4.5/5.** *(§5.5.7, O9, §10; adversarial and canon lenses.)* The document concedes biology instantiates only the coherence half and "declines" entanglement (no multicellular referent). Carrying the "Entanglement" label forward only to keep a five-currency tally intact is appearance over reporting; state biology populates 4 of 5 DPR currencies plus a classical coherence analogue of the 5th.

**m-12. Relabel the Phase-table "status" column.** *(§7; publication lens.)* Marking P1–P3 "runnable now" while P0 "may well STOP the project" conflates "data exist to attempt" with "greenlit." Relabel ("data available" vs "greenlit") or footnote that every "runnable now" below P0 is conditional on P0 passing.

---

## 4. The single most important thing to change

**Stop selling the deferred product. Re-title and re-scope the appendix so that what it actually delivers — a pre-registered, runnable test of (i) F/P/A separability and (ii) system-level coherence non-compensation (P0, P0b, P8) — *is* the thesis, and the per-cell mechanism-localizer is explicitly demoted to a hypothesis gated behind those tests, with a symmetric retirement rule that lets a failed falsifier remove a claim rather than park it in INTERPRETATION forever.**

This one move dissolves the document's deepest structural objection (B-1, B-3, M-5): it converts an elaborate apparatus erected on a precondition the authors expect to fail into an honest, falsifiable program whose value does not depend on that precondition holding. Everything else — the FBA-Action independence proof (B-2), the |r|→dCor table fix (B-4), the P0 power calculation (M-1), the P6/P7 reconciliation (M-4) — is necessary cleanup, but they are repairs to a frame; this is the frame.

---

## 5. Reviewer score table

| Reviewer lens | Score /10 |
|---|---|
| Skeptical cell/molecular biologist (mappings, proxies, single-cell measurability) | 6.0 |
| Computational/systems biology + data engineer | 6.5 |
| Statistician / ML methodologist | 6.5 |
| U-Theory RH / canon-consistency reviewer | 7.0 |
| Adversarial completeness skeptic (falsifiable vs self-immunizing) | 5.0 |
| Scientific editor / structure & publication-readiness | 6.0 |
| **Aggregate (handling editor)** | **6.2** |

*Calibration note: the spread (5.0–7.0) is itself informative. The high mark (canon consistency) reflects that the document is faithful to its parent framework; the low mark (adversarial completeness) reflects that fidelity-to-framework and delivery-of-a-falsifiable-result are not the same thing — the gap between them is exactly the major-revision burden above. The science is real; the manuscript oversells its readiness and under-delivers its committed product.*
