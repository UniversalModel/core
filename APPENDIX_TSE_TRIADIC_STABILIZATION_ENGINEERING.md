# APPENDIX TSE — TRIADIC STABILIZATION ENGINEERING
### An application of U-Theory to the *active stabilization* of living systems — the umbrella over `biology.organism` (TRB) and `clinic.pathology`

> **CANONICAL HEADER**
> **Appendix code:** TSE · **Corpus:** U-Theory / Universal Model · **Parent record:** DOI 10.17605/OSF.IO/74XGR
> **Author:** Petar Nikolov (ORCID 0009-0001-8669-2276) · **Framework:** U-Theory v26 + v27/v28 appendix series · **Version:** 1.1 (critique-hardened)
> **Canonical triad instantiated:** **Form ↔ Time · Position ↔ Space · Action ↔ Energy** (the v25.2 mirror Space↔Form / Time↔Position is **forbidden**, exactly as in canon §2.1). Code = Form, Credo = Position, Rights = Action, registered onto living systems *and* onto the pathologies that destabilize them.
> **What TSE adds over TRB:** a **second orthogonal axis** (clinic/pathology) and the **A×B cross-product** that links it to anatomy, plus a **stabilization-engineering control layer** that turns the static stability map into actively-maintained, *simulated*, guarded recommendations whose objective is the canon Meaning integral **ℳ = ∫U dt** — *of a single declared system, never aggregated across systems.*
> **Objective instantiated (per single declared node only):** maximize **ℳ = ∫U dt** (equivalently minimize the Stupidity integral **𝒮 = ∫(1−U) dt**); canon fixes **ℳ + 𝒮 = T** (MMT/MPI-1). **ℳ is never summed across nodes for allocation or comparison** — that operation does not exist in TSE (§4.4, §9.3-O5b, §9.9 lint-4).
> **Implements:** the GSI-RTD `TriadicDomain` runtime; the SSS scoring engine; **TRB** (Axis A); the new clinical Axis B; the **LGP-12** control loop; the **SSS-Guard** ensemble gate.
> **Project epistemic ceiling:** **B3-pending** (TRB ladder §9.2 = canon-L2, never L3/L4). **Two B4 slots — clinical and ecological — are empty by intent. Any B4 sentence is a bug.**
> **Sibling appendices referenced:** TRB, SSS, GSI-RTD, MMT, TAA, NDT, QMC, RH. See §A and §10. (TSE is the *umbrella over* TRB — Axis A *is* TRB — and a sibling *of* the engine appendices; "umbrella-over TRB" is the controlling framing, §A.1.)
> **What this appendix *is* — and is *not* (read first):** TSE is U-Theory **applied to** the active stabilization of living systems. **It is an instance of the framework, not evidence that the framework is true** (TRB NON-GOAL §9.6-5). Its first job, like every appendix in this corpus, is to try to *falsify its own load-bearing assumptions* — that a disease's F/P/A are separable, and that the A×B localization beats a comorbidity-frequency baseline *and the single-axis scores* — before claiming anything about mechanism, leverage, or therapy.

> **STATUS BANNER (carried on every TSE artifact)**
> **Type:** Specification / engineering design and research plan for a *dual-axis* triadic scoring-and-stabilization engine. **Not** a runtime, dataset, benchmark, validated result, medical device, conservation-management system, or biosecurity tool.
> **Maturity:** **B3-pending.** No deployed engine, no replication, no validation. Every empirical-sounding statement below is a *proposal to be tested*, not a finding.
> **Use:** **Research use only. NOT a medical device**, not diagnostic software, not clinical decision support; **NOT a conservation-decision, triage, biocontrol, or eradication tool.** Produces **no diagnosis, prognosis, or treatment for any individual organism** (human, animal, plant, microbe), and **no triage, ranking, or worth judgment** over any organism, species, population, or ecosystem. Operates on **entity-types and simulated digital twins.** A single private case may be scored *only* as a de-identified research record (SSS Mode B, §3.4) under §9.7 — never as live clinical input for an identified individual's care; all "treatment / therapy / intervention" language denotes **simulated, recommended** actions inside a digital twin, addressed to *researchers about mechanisms* — there is **no autonomous biological action.**
> **Orientation rider (load-bearing — read before any number):** TSE scores the *stability of systems* and *of pathologies*. On Axis A a **high U is good** (a stable cell). On Axis B a **high U is the adversary's stability** — a robust, entrenched disease. The objective sign (stabilize vs. minimize) is **declared per node**; the engine does not decide what is "beneficial."
> **Honesty contract:** every numeric/verdict claim ships in a TRB **claim envelope** with a B0–B4 level; the renderer refuses any wording above its tag. The dual-axis fragility map is **dual-use** (a stabilizer is a destabilizer sign-flipped, cheapest near criticality); the species-scale *"which organisms are useful"* question is the **O5 eugenics-attractor scaled to ecology** — a hard guardrail, **never a feature** (§9.7). The active/deliverable voice ("the New Biology," "stabilize the biosphere") is **VISION/telos, confined to explicitly-marked VISION blocks**, never a section thesis and never a deliverable (§9.4).

---

## A. Relation to U-Theory canon and to TRB (placement in the corpus)

This section is what makes the document below an *appendix* rather than a standalone plan: it states how TSE sits inside U-Theory, what canonical claim it exercises, and how it stands as the **umbrella over TRB**.

### A.1 TSE is the engineering discipline; TRB is its anatomical map

TRB delivers a **map**: a triadic knowledge graph (TB-KG) of `BioSystem` nodes scored `U = ∛(F·P·A)`, weak-zone scanned, leverage-ranked — a static account of *where, in the body's parts, stability is low.* TSE's proposed contribution is the **engineering discipline that turns that map into a control loop**: a closed cycle whose objective is to **raise the Meaning integral ℳ = ∫U dt of one declared system** by repeatedly localizing the highest-leverage weakest zone *within that system* and recommending an axis-typed corrective to its weakest pillar — each move *simulated, guarded, and re-scored* before it is ever surfaced.

> **What the revised TRB actually delivers — and what TSE may NOT inherit as settled (read first).** TRB's *product* is two pre-registered, runnable tests: **(i) F/P/A separability** in atlas data (P0/P0b) and **(ii) system-level coherence non-compensation** (P8). The aspiration that *"the weakest pillar names the disease mechanism"* is, in revised TRB, an **explicitly gated hypothesis (P2-mech)** — conditional on separability passing *and* on a defensible proxy-to-axis assignment — **retired if its gates fail** (TRB §2.5/§9.8). **TSE therefore does not treat TRB's weak-zone scan as a delivered mechanism-localizer.** Every TSE arrow that follows TRB's scan into "which pillar in which cell collapses" is a *hypothesis conditional on TRB's separability gate (P0-A) and P2-mech*, never a settled anatomical capability; the A×B payload sits *on top of* an Axis-A precondition that may itself fail and be reported as the most valuable negative.

The corpus structure is strictly nested. "Umbrella-over TRB" is the controlling relation; TSE is sibling only to the *engine* appendices (SSS/GSI-RTD), never a peer of TRB:

```
U-Theory canon  (Form/Position/Action; U=∛(F·P·A); ℳ=∫U dt for a single declared node)
   └── TSE  — Triadic Stabilization Engineering   ◄── this appendix (the umbrella)
         ├── Axis A = TRB (anatomy/structure)            organism → … → molecule
         ├── Axis B = clinic/pathology (NEW here)        health → … → symptom
         ├── A×B    = the cross-product (the payload)     disease ↔ weak cell/organ
         └── control layer = LGP-12 over A×B, objective ℳ↑ / 𝒮↓ on one declared clock
```

> **VISION (B0/L0).** "Triadic Stabilization Engineering = the New Biology" and "biology is the basis for actively stabilizing life" are **framing/telos**, not tested capabilities — the level of TRB's §A.1 nomenclature caveat. A reviewer may reject the slogan without touching a single number; the operational content lives entirely in the proxies (§3) and the falsifiers (§8). This is the *only* place the slogan is asserted; everywhere else the active voice is confined to a VISION block.

### A.2 The same invariant triad, registered onto life *and* onto pathology

Canon fixes one substrate-invariant triad — **Form ↔ Time, Position ↔ Space, Action ↔ Energy** (the mirror is forbidden, §2.1). TRB registers it onto living *structure*. TSE registers it a second time, onto *pathology* (a disease is a system; the SSS engine is substrate-agnostic — SSS.7 scores Marriage, Democracy, Internet, a Glass of Water by the same scripts). The *meaning* of F/P/A is identical across both registrations; only the proxies change (§3). This is the single statement of the invariant; later sections reference it rather than restate it.

### A.3 TSE *exercises* the cross-domain-transfer claim — twice

The corpus transfer coefficient β predicts a stabilization heuristic learned in one `TriadicDomain` transfers to another in proportion to *triadic-structural* similarity, not surface analogy. β is *always computable* (§5.4); what is at stake is its **validity**. TSE is a double stress-test: **if F/P/A are not even separable on diseases (Axis B, §8), or if the A×B link is an annotation artifact, then β-transfer into the clinic is invalid**, and the corpus universality claim is *narrowed by* clinical reality rather than confirmed by it. Reporting that narrowing is TSE's contribution to canon — not its failure (TRB §A.2 posture).

### A.4 Runtime — both axes are *conformant domains*, not parallel theories

Axis A (`biology.organism`) and Axis B (`clinic.pathology`) each implement the GSI-RTD `TriadicDomain` interface (`embed_form / build_position_graph / enumerate_actions / execute_action / evaluate_sss`). The canonical search→scheduler→agents→cycle→score→learn machinery runs over the **A×B matrix** with no bespoke orchestration. Every capability claimed below must be expressible through that interface — a hard consistency constraint, re-checked in §10.

### A.5 Epistemic stance inherited from canon (level-inflation forbidden)

Canon's RH ladder is **L0 = Meta-evaluation, L1 = Operational stability, L2 = Cross-domain analogy, L3 = Cosmological extension, L4 = Literal physical claim** (RH_CRITICAL_REVIEW §71–75, quoted verbatim as TRB §A.6/§8.5 carries it). TSE keeps TRB's renamed ladder **B0–B4** (not canon L0–L4) precisely so clinic/ecology claims cannot borrow canon's cosmological tiers (L3/L4). Every empirical TSE statement is at most **canon-L2** (cross-domain application); the ceiling **B3-pending** is a *narrowing* of L2 to "testable-over-data, not yet validated," never L3/L4. Full mapping in §9.2.

---

## 0. What TSE is, what it is not, and what is new in it

TSE is a hardening-and-extension pass over TRB. The structurally new objects, and the disciplines that govern them:

- **NEW — Axis B (clinic/pathology):** a second recursive `BioSystem`-typed tree `health → specialty → disease → syndrome → symptom/sign`, scored on F/P/A by the identical SSS pipeline, with an **orientation flip** (high U = robust adversary). §3.
- **NEW — the A×B cross-product:** a typed, evidence-bearing **bipartite graph** linking a disease (B) to the weak zones in specific cells/organs (A) it manifests in; the matrix view is its adjacency matrix. This is the payload: *disease → which pillar in which cell collapses → highest-leverage weakest-zone → intervention candidate.* §4.
- **NEW — the stabilization control layer:** the TRB LGP-12 loop run over A×B, with the objective **ℳ = ∫U dt of one declared node**, and the **SSS-Guard** gate on any irreversible (simulated) call. "Treatment" is precisely defined as restoring the weakest pillar of the highest-leverage cross-node on that pillar's own axis. §5.
- **NEW — the biosphere-scale extension:** the upward recursion of Axis A into ecology (population → … → biosphere), the corpus's most literal triad registration and its most epistemically exposed — **mostly B0–B2 telos**, gated by named data gaps (Linnean/Wallacean shortfalls), and with **cross-node ℳ-allocation explicitly forbidden** above the organism boundary (§4.4, §6). §6.
- **HARDENED — RH discipline:** the TESTABLE/INTERPRETATION cut applied to *three* surfaces (A, B, A×B); two empty B4 slots (clinical and ecological); the **O5 eugenics-attractor scaled to ecology** as a hard guardrail closed at *both* the worth-label and the ℳ-allocation that reconstructs the ordering; pre-registered separability gates with a **symmetric retirement rule.** §9.

> **Critique applied in v1.1 (the consequential corrections).**
> - **The A↔B coupling is now strictly one-directional (A grounds B), not a bidirectional fixed point.** The prior mutually-defining iteration had no external referent and no falsifier; it is removed. Grounding is a single pass, and the grounded score must beat *both* `U_B` *and* `U_A` against external outcomes or it is retired (§4.2, §8 TSE-P2).
> - **Disease FORM proxies are now process-intrinsic** (lesion/biomarker durability), not nosology-derived ("ICD-revision stability" measured the committee, not the disease); all map-defined FORM is `LATTICE_APPROX` (§3.2).
> - **Cross-node ℳ-aggregation and leverage-ranking are forbidden above the organism boundary** — closing the worth-ranking leak the O5b *label*-ban left open (§4.4, §6.1, §9.3-O5b, §9.9 lint-4).
> - **SSS-Guard splits retrodictive (validation) from prospective (no external metric exists) gating**; prospective hypotheses have *no `pass` state* — only `queue for V3` (§5.3).
> - **Planetary boundaries demoted** from independent anchor to contested B1/B2 framing; **E2 retired as conceded-circular**; E1 (food-web topology, measured structure) is the load-bearing ecological falsifier (§6.3, §6.5).
> - **Worked examples (§5.5, §6.4) are relabeled consistency illustrations on known cases carrying zero predictive evidence** (retrodiction theater warning).
> - **δ-fall keep-rule softened; suppress-polarity threshold sign corrected; `sens()` defined; three missing falsifiers added** (leverage primitive, `U_disease`-predicts-resistance, symptom-readout); Mode B reconciled with the banner; IPBES-NCP acknowledged as anthropocentric/contested.

> **Inherited verbatim from TRB §9:** the claim envelope, the TESTABLE/INTERPRETATION cut, the B0–B4 ladder, the output lint, SSS-Guard, the multiplicity discipline (R7), the unit-of-independence discipline (R8), overclaim risks O1–O9, and the dual-use posture. TSE re-derives O5 at population/species scale (O5b) and adds the second-axis gates.

---

## 1. Thesis — what TSE actually delivers, and the telos that motivates it

> **VISION (B0 — telos, renders no number, not a deliverable).** *Biology is not only a map of organisms; it is the basis for actively stabilizing them — reducing the entropy of living systems to raise survival.* This motivates TSE and orients the objective's sign. It is not a tested capability and ships no number.

**The engineering claim (B1→B3-pending).** To "stabilize" a declared living system is, in canon terms, to keep it **solvent in all three prices** — Position/Space, Form/Time, Action/Energy — for as much of its clock as possible, i.e. to maximize, *for that single node on a single declared clock*:

```
ℳ(S,T) = ∫₀ᵀ U_S(τ) dτ          (Meaning  — time-integrated solvency)
𝒮(S,T) = ∫₀ᵀ (1 − U_S(τ)) dτ     (Stupidity — time-integrated insolvency)
ℳ + 𝒮 = T                        (the clock is fully partitioned — canon MMT/MPI-1)
```

Reducing 𝒮 *is* reducing the integrated entropy the system fails to export. Because U is **non-compensatory** (the geometric mean), ℳ is dominated by the *weakest pillar of the weakest node over time* — so the controller does not chase average U, it chases the **lowest-U trajectory segment**, where dℳ/dt is most negative.

> **The boundary that makes ℳ safe (load-bearing).** ℳ is defined and optimized **only on a single declared node.** There is **no operation in TSE that sums ℳ across nodes, compares ℳ between nodes, or allocates a budget across nodes by ℳ-leverage above the organism boundary** (§4.4). Cross-node leverage ranking *within one organism* (which of my tissues to repair first) is admissible engineering; cross-*organism*/population/species ℳ-allocation is the eugenics attractor wearing an optimizer's clothes and is **type-forbidden** (§9.3-O5b).

> **Epistemic placement (read first).** The control *cycle*, the leverage algebra, and the A×B schema are **B1** (true of the model) once their inputs exist. Every statement that a given cross-node is a *real* weak zone, or that an axis-typed move *would* help a real organism, is **B3-pending** — a pre-registered prediction, never a finding.

---

## 2. The two orthogonal axes and the cross-product matrix

### 2.1 Two orthogonal triadic decompositions of one organism

TSE decomposes the *same* living system twice, along axes that are not reducible to each other:

- **AXIS A (Anatomy / structure) = TRB.** `organism → system → organ → tissue → cell → complex → molecule`. The `PART_OF` / `IS_A` tree, scored F/P/A, weak-zone scanned. **Indexed by location/structure.** Answers *"where, in the body's parts, is stability low?"*
- **AXIS B (Clinic / pathology) = new in TSE.** `health → medical specialty → disease → syndrome → symptom/sign`. **Also** scored F/P/A. **Indexed by manifestation/dysfunction.** Answers *"which named pathological process is present, and how entrenched is it?"*

Neither reduces to the other: one disease (B) projects onto many weak zones in A (sepsis hits endothelium, mitochondria, immune cells, kidney tubule); one weak cell (A) participates in many diseases (B). **The payload of TSE is the cross-product A×B** (§4), not either axis alone.

> **Why B is a DAG, not a tree.** The clinical hierarchy is **not** a clean `PART_OF` tree the way anatomy is — it is poly-hierarchical and overlapping. Axis B is therefore a **DAG/overlay** and inherits TRB's tree-vs-lattice limitation (§TRB-7) by default. Nodes whose definition is map-dependent are tagged `LATTICE_APPROX` and held to a higher evidence bar.

### 2.2 The orientation problem (load-bearing — read before any number)

The entity scored on Axis B is a *pathology*, so the sign is inverted, and this must be declared per node or every downstream verdict is backwards:

- **U_disease** measures how *entrenched/robust the pathological process is* — pathophysiological coherence, chronicity, resistance to dissolution. **A high U_disease is the adversary's stability** — semantically *bad* for the patient. The therapeutic objective is to **minimize U_disease**, the mirror of Axis A's maximize-U_organism.
- This is not a second formula; it is the same `U = ∛(F·P·A)` with a declared **polarity tag**: `polarity ∈ {stabilize, suppress}`. Axis-A nodes are `stabilize` (raise U); Axis-B disease/syndrome nodes are `suppress` (lower U). The *only legitimate way* to lower a B-node's U is to **restore the weakest pillar of the A-node(s) it manifests in** — TSE never optimizes "make the disease unstable" as a free-standing objective on a host substrate; that, pointed at a host or beneficial organism, *is* the weaponization sign-flip (§9.7).
- **Meaning under inversion.** TRB's objective `ℳ_org = ∫U_org dt` is unchanged and lives on Axis A. Axis B contributes a *dual* quantity `𝒮_disease = ∫U_disease dt` (accumulated entrenchment over the episode), a component of the organism's Stupidity integral, obeying `ℳ + 𝒮 = T` only on a single declared clock (TRB R5/R10). **Therapy maximizes ℳ_org by minimizing 𝒮_disease — the same optimization viewed from the two axes.**

> The output lint (§9.9) hard-rejects any rendered verdict whose wording implies "high disease U = healthy" or "low disease U = sick patient." A disease U is a **model-internal entrenchment index for a pathology type**, never a patient state.

> **A second, distinct triad must never be conflated with Axis B.** The corpus contains a *treatment* triad (LGP-M: Form = drug/device, Position = care environment, Action = procedure/regimen) that scores a *care plan*. **Axis B scores the *disease-as-system*, not its treatment.** The treatment triad is the *output* of the cross-product's leverage step (§5.1), routed to the LGP-12 intervention step — never part of Axis B.

---

## 3. Axis B — the clinical node, scored on the disease-as-system triad

### 3.1 The node schema and real ontology grounding

Axis B reuses TRB's `BioSystem` envelope (`F{} / P{} / A{} / G{}` provenance / state `s`) but instantiates a new node class, **`ClinSystem`**, at five scales, each bound to a **real, versioned clinical ontology** so nodes are populated from data, not invented.

| Scale | Node class | Primary ontology (real) | Identifier (illustrative) | What the node is |
|---|---|---|---|---|
| **health** | root (`stabilize` baseline) | — | — | the well-functioning reference (links to the Axis-A root) |
| **specialty** | domain partition (governance only; no leaf score) | UMLS semantic network; ICD-11 chapters | ICD-11 Chapter BA–BE (circulatory) | grouping frame |
| **disease** | `ClinSystem(disease)` | **Mondo** ⟂ **ICD-11**, **SNOMED CT**, **Orphanet/OMIM** | Mondo:0005009 (heart failure); ICD-11 **BD1x**; SNOMED 84114007 | a persistent pathological entity, scored triadically |
| **syndrome** | `ClinSystem(syndrome)` | Mondo / Orphanet; SNOMED | e.g. cardiorenal syndrome | a co-occurring cluster bridging diseases |
| **symptom / sign** | `ClinSystem(phene)` | **HPO**; SNOMED clinical-finding | HP:0002094 (dyspnea), HP:0000969 (edema) | the surface reading of an instability |

```tpl
# B-node at the "disease" scale
F{ entity:"heart failure, reduced EF"; mechanism:"neurohormonal vicious cycle (RAAS/sympathetic)";
   lesion_durability:fibrosis-persistent-on-CMR; chronicity:registry-recurrence-index;
   biomarker_trajectory:NT-proBNP-non-resolving;
   nosology:{MONDO:0005009, ICD-11:BD1x, SNOMED:84114007}; form_class:LATTICE_APPROX }
P{ locus:{UBERON:LV-myocardium}; context:{comorbid:[DM2,CKD]}; specialty:Cardiology;
   distinguishability:0.74 (vs HFpEF, non-cardiac dyspnea) }     ; P = √(locus · context)
A{ progression:NYHA-decline-slope; damage_throughput:catabolic-load; mortality_burden:high; entropy_export:cardiac-cachexia }
s = (decompensation_state, volume_status, rhythm)
G{ src:MONDO+HPOA+DisGeNET+registry+imaging-cohort; conf:0.74; level:B2; mode:assert }
```

**Cross-ontology mapping is itself a real, audited artifact:** **UMLS Metathesaurus** CUIs and **Mondo** `exactMatch`/`closeMatch` axioms bridge ICD-11 ↔ SNOMED ↔ OMIM ↔ Orphanet; the **HPOA** disease–phenotype file supplies disease→symptom edges. Every mapping carries `G{src; conf; level; mode}` and a `mapping_quality ∈ {exact, narrow, broad, inferred}` flag — a `broad`/`inferred` map cannot enter an irreversible decision.

> **Honest gap (B-data-1).** ICD-11 is billing-shaped, SNOMED record-shaped, HPO phenotype/genetics-shaped, Mondo the research unifier; they disagree on granularity. Axis B does **not** resolve this; it records the disagreement as `mapping_quality` and treats map-dependent nodes as `LATTICE_APPROX`, mirroring TRB §7.

### 3.2 Assigning F / P / A to a disease and to a symptom

The invariant is **Form ↔ Time, Position ↔ Space, Action ↔ Energy** (stated once in §A.2; not restated per-pillar). A central v1.1 correction lives here.

#### For a DISEASE — FORM is now scored from the *process*, not the *nosology*

> **The §C3 fix.** The prior FORM proxies ("diagnostic-criteria completeness," "definitional stability across ICD-11 revisions") measured *committee behavior*, not biology, and were definitionally entangled with the same ontology that supplies POSITION and the cross-links — the shared-annotation artifact TSE-P0(B) is meant to catch. FORM is now built from **process-intrinsic, instrument-measurable** durability; any disease whose FORM still rests on map definitions is tagged `form_class: LATTICE_APPROX` and held to the higher bar.

| Pillar (↔ price) | Pathology meaning — *what is scored* | Real **process-intrinsic** proxy | Canonical failure mode of the *disease* |
|---|---|---|---|
| **FORM (↔ Time)** — what it *IS*, how durably it persists | lesion/mechanism durability; chronicity vs self-limiting; resistance to resolution | **lesion persistence on serial imaging** (e.g. fibrosis on CMR/CT); **biomarker-trajectory durability** (non-resolving vs decaying); **histological chronicity grade**; monogenic penetrance (OMIM) where a true molecular lesion exists. *Nosology-stability is NOT a FORM proxy; map-defined FORM ⇒ `LATTICE_APPROX`.* | **identity collapse of the disease** = a self-limiting / ill-defined process (LOW Form = fragile *as an entity*, easy to dislodge — good for the patient) |
| **POSITION (↔ Space)** — *where* and *in what context* | anatomical/systemic localization; Axis-A context; comorbidity placement; distinguishability; spread/contagion | UBERON/Axis-A localization; weight of `MANIFESTS_IN` edges; comorbidity-network centrality; differential-diagnosis ambiguity | **positional collapse** = no stable locus / fully confounded |
| **ACTION (↔ Energy)** — what it *DOES* | progression rate; metabolic/entropic burden; throughput of damage; mortality/morbidity hazard | progression slope (NYHA transition, eGFR decline/yr); case-fatality / hazard ratio; DALY burden (GBD); entropy-export proxy (catabolic/cytokine load) | **functional collapse** = a non-progressive, low-burden indolent process |

A **high U_disease** (entrenched, durable-lesion, well-localized, fast-progressing) is the **most dangerous adversary**. The **weakest pillar of the disease names the cheapest place to attack it** (§4) — the therapeutic mirror of TRB's weakest-pillar-to-stabilize.

#### For a SYMPTOM / SIGN (an HPO phene)

| Pillar | Symptom meaning | Real proxy | Failure mode |
|---|---|---|---|
| **FORM (↔ Time)** | how stably the symptom persists / recurs / decays | temporal pattern (constant / episodic / decaying); test-retest reproducibility | a fleeting, non-reproducible sign (low Form = noise) |
| **POSITION (↔ Space)** | localizing value — does it point to a specific Axis-A locus? | HPO term specificity (information content in the HPO DAG); inverse of #diseases annotated | a non-localizing symptom (fatigue, malaise) |
| **ACTION (↔ Energy)** | functional impact it reports — severity, disability, energetic cost | HPO severity modifier; functional-status delta (6-min-walk, SOFA component); PRO | a symptom reporting no functional loss |

> **The symptom is an *organism-level* readout, never a per-cell measurement (§M7 fix).** A symptom's value is the `MANIFESTS_IN` edge back to Axis A, but a symptom such as dyspnea is multi-cause and localizes to no single cell. The earlier claim that the symptom layer "backfills TRB's missing per-cell Action data" is **withdrawn**: at most it provides an *organism-/organ-level* Action proxy; any per-cell readout is **P-B3-pending and expected to be weak** (one symptom → many cells). The renderer never attributes a symptom score to a specific cell.

### 3.3 Edge schema (each edge loads exactly one axis — TRB K2 inherited)

| Edge | Meaning | Axis loaded | Real source |
|---|---|---|---|
| `IS_A`, `SUBTYPE_OF` | disease/syndrome subsumption | **Form** | Mondo, ICD-11, SNOMED hierarchy |
| `MANIFESTS_IN` (B→A) | disease/symptom localizes to an Axis-A organ/tissue/cell *context* | **Position** | HPO↔UBERON, SNOMED finding-site |
| `PRESENTS_AS` | disease → symptom/sign as a *contextual co-occurrence* | **Position** | HPOA disease–phenotype annotations |
| `PROGRESSES_TO`, `DERANGES` (B→A) | the *functional/energetic effect* the disease exerts on an Axis-A node | **Action** | Reactome disease pathways, DisGeNET |
| `COMORBID_WITH` | disease–disease co-occurrence context | **Position** | comorbidity networks, de-identified EHR co-occurrence (RUO) |
| `CAUSED_BY` | etiological link to an Axis-A `DISRUPTS`/pathogen node | per-target | OMIM, ClinVar, CARD/VirHostNet |

`MANIFESTS_IN` and `PROGRESSES_TO` are the **cross-product edges.** Following TRB fix E2, `PRESENTS_AS` (Position) is split from `DERANGES` (Action), so **no edge loads two axes.**

### 3.4 Scoring mechanics (identical SSS pipeline, substrate re-instantiated)

```
U_disease = ∛(F · P · A)                  any pillar → 0 ⇒ U → 0   (non-compensatory)
δ        = (max(F,P,A) − min(F,P,A)) / (max + 0.01)
SI       = U / (1 + δ)²
weak_pillar(disease) = argmin(F, P, A)    # the disease's most fragile face = cheapest attack axis
```

- **Constructor (SSS Stage 1):** reads the clinical case definition / epidemiological context (ICD-11 + Mondo definition + HPOA + imaging/biomarker cohort + a registry slice) and extracts N≈12 **falsifiable principles per pillar**. For a private instance the **de-identified documented case IS the system** (SSS Mode B) — general knowledge forbidden, missing principle → **neutral 50**.
- **AI jury (SSS Stage 2):** up to 50 OpenRouter models score each principle 0–100; **IQR-filter → weighted per-principle mean → pillar averages → geometric mean → U → consensus %.** Reliability floor ≥3–5 valid responses. The jury maps to TAA's four roles. As in TRB §5.1/B5, the **50-model jury runs only on a leverage-selected subset**; the bulk carry bare quantitative-proxy scores.
- **Two modes (SSS A/B):** **Mode A** scores the disease *type* against an injected domain reference; **Mode B** scores *one de-identified documented case* using only the provided document. The **A−B gap measures deviation of this case from the type**.

> **Mode B reconciled with the banner (§Mo8 fix).** "Operates on entity-types and digital twins, never on a live person" and Mode B ("a case IS the system") are reconciled as follows: **Mode B is admissible only on a de-identified research record under §9.7** (HIPAA Safe Harbor / GDPR, IRB, not sent to external APIs, not persisted), and is **never** live decision support for an identified individual's care. A "case" in TSE is a *research record*, not a patient at the bedside. The banner's absolute is therefore: never *live clinical input for an identified individual* — de-identified research records are the only individual-grain data TSE touches.

- **Thresholds are stakes-scaled and polarity-aware (sign corrected — §Mi4 fix).** φ⁻¹ ≈ **0.618** is the provisional baseline. **For `suppress`-polarity (disease) nodes the stakes-scaling runs the *other way*:** raising θ flags *fewer* diseases as "entrenched," which is *less* cautious for a high-mortality disease — so high-mortality / high-DALY diseases get a **lowered alarm threshold** (flag entrenchment earlier), the mirror of the raised θ used for `stabilize` nodes. The verdict reads: **U_disease ≥ θ_suppress ⇒ "entrenched/robust pathology — high therapeutic resistance"** (alarming), not "stable = good." All thresholds are **tunable, domain-calibrated defaults, not biological constants** (TRB NON-GOAL 10).

---

## 4. The A×B cross-product — binding clinic to anatomy (the payload)

### 4.1 The link object — a typed bipartite edge, not a number

The cross-product is a sparse, **typed, evidence-bearing bipartite graph** `L ⊆ B × A`, each edge axis-loaded so the one-property-one-axis invariant survives the join. The matrix view is the *adjacency matrix* of this graph; the graph is primary because edges carry provenance, weights, and an axis label a bare matrix cell cannot.

```
ManifestsEdge  e = (b ∈ B, a ∈ A,
                    rel  ∈ {LOCALIZES_TO, DYSREGULATES, READS_OUT, GENE_DRIVES, PATHWAY_PERTURBS},
                    axis ∈ {Form, Position, Action},          # which pillar of a the disease attacks
                    w    ∈ [0,1],                             # evidence-weighted strength
                    G{src; conf; level; mode})                # provenance, as every TRB fact
```

| Edge `rel` | Meaning (B→A) | Axis loaded on the A-node | Join key / resource |
|---|---|---|---|
| `LOCALIZES_TO` | disease/symptom localizes to an anatomical structure | Position | **HPO** phenotype → **UBERON**/`PATO`; HPO `phenotype_to_anatomy` |
| `GENE_DRIVES` | a disease gene maps to the cell/molecule expressing it | Form | **DisGeNET**, **Open Targets**, **OMIM**/**Orphanet** → Ensembl/UniProt → CL/Tabula Sapiens cell node |
| `PATHWAY_PERTURBS` | a disease perturbs a reaction/pathway in a node | Action | **Reactome** disease pathways → reaction → A-node `CATALYZES/REGULATES` |
| `DYSREGULATES` | disease alters a node's niche/context | Position(context) | DisGeNET + CellPhoneDB/NicheNet (inferred — flag) |
| `READS_OUT` | a sign/symptom is the surface reading of a system's state | Action (of the parent system) | HPO sign → affected system; mechanistic literature (B2) |

**Join-key normalization is the load-bearing engineering:**
- **Disease identity:** **MONDO** as the merge hub so `I21 ≡ OMIM:608557 ≡ MONDO:0005068` collapse to one B-node (TRB §4.4 K6).
- **Phenotype→anatomy:** **HPO**→`UBERON` cross-refs — the *primary, curated* `LOCALIZES_TO` builder.
- **Gene→cell:** gene–disease (DisGeNET/Open Targets/OMIM) gives the gene; HPA/Tabula Sapiens give the expressing cell type. **Independence caveat (TRB §4.2):** expression-derived links feed *both* the A-node Form pillar and this edge, so the join can manufacture correlation — a **feature-leakage audit (TRB P0c) is mandatory before any A×B propagation result is reported.**

`w` is the source's own confidence, carried in `G{}`.

### 4.2 How scores propagate across the link — *one-directional grounding* (the §C1/M5 fix)

> **The bidirectional fixed-point coupling is removed.** The prior design grounded `U_B` in `U_A` *and* loaded `U_A` by `U_B`, then iterated to a fixed point — a mutually-defining value with **no external referent and no falsifier**; it could be tuned to any ordering via κ and the damping factor. v1.1 keeps only **one-directional grounding (A → B), single pass**, and makes the grounded score earn its place against external truth (§8 TSE-P2).

Let the adjacency of `L` be **M** (`|A|×|B|`, `M[a,b]=w`), partitioned into axis-slices `M_F, M_P, M_A`. Grounding is a **single, non-compensatory pass**, A → B only:

```
g_χ(b) = wgeomean_{a : M_χ[a,b]>0} ( U_A-pillar_χ(a), weight = M_χ[a,b] )   # linked-anatomy ground term, χ∈{F,P,A}
F_B*(b) = √( F_B(b) · g_F(b) )      # combine intrinsic clinical score with anatomical ground, non-compensatorily
P_B*(b) = √( P_B(b) · g_P(b) )
A_B*(b) = √( A_B(b) · g_A(b) )
U_B*(b) = ∛( F_B* · P_B* · A_B* )
```

A disease is only as "structurally real" as the integrity of the cells whose Form it corrupts: if the linked anatomical Form-zone is itself collapsing, the disease's Form-grounding pulls `F_B*` down. **The A-node scores `U_A` are *not* modified by `U_B`** — Axis A is computed by TRB independently, then read (not written) by the grounding pass. This makes `U_B*` a *function of two independently-measured inputs*, so it has an external referent and the §8 falsifier can bite.

> **The honest reverse direction.** "A robust disease loads the host node it sits on" is intuitively real, but encoding it as a back-write created the circularity. If a disease-load-on-host effect is wanted, it must be a **separately-measured, externally-anchored** quantity (e.g. an observed biomarker of host damage), entered as its own A-node Action input with its own provenance — **never** a re-read of `U_B`. Until such a measurement exists, B→A back-loading renders no number.

### 4.3 The three reads that make the engine diagnostic→therapeutic

1. **Disease → weak zone (B→A localization).** Given an active disease `b`, follow its `PROGRESSES_TO` edges into Axis A and run the **TRB weak-zone scan (§5.4) restricted to the projected sub-forest**: which Axis-A cell/organ has the collapsing pillar `b` exploits? *Note (revised-TRB consistency):* "which collapsing pillar" is a **TRB-gated hypothesis (P2-mech), not a settled localization** — valid only if Axis-A separability (P0-A) holds and the proxy-axing is stable; absent those, the scan reports a `δ-spike, axis TBD`, not a named mechanism axis.
2. **Weakest-pillar → highest-leverage intervention (A leverage rank, *within one organism only*).** Reuse TRB's leverage primitive: `Priority = ΔMeaning / ∛(C_time · C_space · C_energy)` (ties → cheapest), **applied only across nodes inside one declared organism** (§4.4). The intervention must act on the **weakest pillar's own axis** (compensation forbidden, TRB §6.4): Form→repair/identity-restoration; Position→reperfusion/niche-restoration; Action→energy/function reset.
3. **Symptom → instability (A surface reading).** A symptom's `Action` proxy is a *noisy organism-/organ-level estimate* of the Axis-A node's `Action` deficit it reports — never a per-cell measurement (§3.2).

> **The honest direction of inference.** A×B is a **hypothesis-routing engine**: `disease → candidate collapsing pillar in candidate cell → candidate highest-leverage weakest-zone → candidate intervention`. Every arrow is a research hypothesis carrying a multiplicity-corrected q-value (TRB-R7), **not** a diagnosis. The matrix does not *know* which cell is collapsing in a given patient; it *ranks where to look.*

### 4.4 The organism-boundary firewall on leverage and ℳ (the §C4 fix)

> **The single most important ethics correction in v1.1.** The O5b ban (§9.3) forbids the *operation* "return species A is worthier than B." But the objective `ℳ = ∫U dt` plus the leverage rule `Priority = ΔMeaning/∛(C·C·C)` would, if run across ecological nodes, allocate finite budget across populations/species — reconstructing the *identical ordering* the worth-ban tries to prevent, just without the word "worth." TSE closes this:

- **ℳ is per-node and never aggregated across nodes for allocation or comparison.** There is no `ℳ_total = ∑ ∫U dt` operation in TSE above a single organism.
- **The leverage primitive is admissible only across nodes *inside one declared organism*** (which tissue to repair first). It is **type-forbidden across the organism boundary** — no cross-population, cross-species, or cross-ecosystem `Priority` comparison exists. The §6.1 phrase "raise the biosphere's ℳ" is **VISION/telos only** and renders no number, no ranking, no allocation.
- Any multi-organism / multi-population allocation is an **external governance decision** supplied to TSE under §9.7, never a TSE output. The lint (§9.9 rule 4) refuses any cross-organism leverage or ℳ-aggregation, exactly as it refuses cross-person U.

---

## 5. The stabilization-engineering control layer — from map to active maintenance

### 5.1 "Treatment" defined, and the cross-node weak-zone score

> **Definition (TSE-treatment).** A *treatment* is an **axis-typed intervention that restores the weakest pillar `π* = argmin(F,P,A)` of the highest-leverage cross-node `(a*,b*)` — leverage ranked only within one organism (§4.4)** — acting **on `π*`'s own canonical axis (compensation forbidden)**, **simulated on the digital twin first**, must **pass SSS-Guard**, and is kept only if **re-scoring shows Δℳ > 0 and the keep-rule of §5.4 holds.**

> **The digital twin is research-grade, not runnable now (inherited from revised TRB §6.2/M-3).** The coupled dynamic twin TSE simulates on (Action-FBA + Position reaction-diffusion + Form-damage) has **no calibrated cross-layer constants and cannot be calibrated from snapshot atlases** — its trajectories are *illustrative, not validated*. What is runnable is the **KG + static per-node A×B scoring**; every "simulate on the twin" step below is a research-grade dynamic claim, never a runtime, and never live physiology (§9.3-O7). The twin is a simulation, not a person.

Two non-compensatory rules make this precise:

1. **Leverage, not severity.** The target is the node where a feasible pillar-restoration buys the most organism Meaning per price; a CRITICAL *serial* survival-critical node is force-promoted (TRB §5.4).
2. **Axis-match (compensation forbidden, TRB §6.4):**

| Weakest pillar `π*` | Allowed intervention class | Examples (simulated/recommended) |
|---|---|---|
| **Form** (identity/damage) | repair / identity-restoration | gene editing, partial epigenetic reprogramming, chaperone therapy, senolytics |
| **Position** (locus/context) | context / niche-restoration | reperfusion, re-vascularization, differentiation therapy, ECM normalization, FMT |
| **Action** (function/energy) | function / energy-reset | metabolic reprogramming, mTOR modulation, ion-pump support, anti-inflammatory `A_loss` reduction |
| **Coupling** (δ high) | re-coupling / combination | combination triad therapy (HYPOTHESIS — twin runs a 2×2×2 factorial in-silico first) |

Restoring an Action deficit with a Form tool is **rejected at synthesis (LGP-6)**: the geometric mean means a compensating pillar cannot rescue a collapsed one.

**The cross-node weak-zone score:**

```
For disease b with weak pillar πB = argmin(F_b,P_b,A_b):
   targets(b)     = { a : MANIFESTS_IN(b→a), κ ≥ κ_min }
   bind_pillar(a) = argmin(F_a, P_a, A_a)
   CrossWeak(a,b) = κ(b→a) · (1 − U_a) · sens(πB → bind_pillar(a))
```

`CrossWeak` is high exactly when a penetrant disease (large κ) localizes to a genuinely weak host node (low `U_a`) whose collapsing pillar is the one the disease reads out.

> **`sens()` defined (the §Mo6 fix).** `sens(πB → π_a)` is **not** a free knob; it is the **empirically-measured conditional probability that the disease's weak pillar `πB` co-collapses with host pillar `π_a`**, estimated from the cross-axis annotation base (HPOA + Reactome disease-pathway + DisGeNET) as `P(host-pillar π_a deranged | disease-pillar πB weak)`, smoothed and shrunk to a prior. It carries its own `G{src; conf; level}` and **enters the §4.1 feature-leakage audit**, because its training annotations partly overlap the edge weights `w`. Where the estimate has insufficient support it falls to the diagonal-only prior (`sens=1` iff `πB=π_a`, else a small floor) and the cross-node is flagged `sens_sparse`. The §5.5 value `0.9` is illustrative of a well-supported diagonal `Position→Position` estimate, not invented.

> **Honesty rider (B2/B3).** `κ`, `sens`, and the `READS_OUT` map are **B2 bridges** from association databases — associations, not mechanisms. Any cross-node *hypothesis* is **B3-pending**, tagged `low_score_cause ∈ {evidence_sparse, genuinely_imbalanced, lattice_approx, sens_sparse, axis_unseparated}`; only `genuinely_imbalanced` on a gated axis is a candidate hypothesis. The cross-product inherits TRB's **multiplicity discipline (R7)**: `argmin/argmax` over a 10³×10⁴ matrix is a look-elsewhere problem — every cross-flag carries an **empirical-null + FDR q-value** and must clear an absolute deficit band, or it is emitted as "not distinguishable from scan noise."

### 5.2 The closed cycle — LGP-12 over the A×B matrix

```
TSE CONTROL CYCLE (= TRB LGP-12, dual-axis)                              register
─────────────────────────────────────────────────────────────────────  ────────
LGP-1  SCAN A×B   score Axis A (TRB) and Axis B (clinic) trees;          B3-pend
                  emit U,δ,SI per node; build MANIFESTS_IN/READS_OUT
LGP-2  DETECT     𝒫 = {(a,b): SI_a<θ_tissue ∨ U_b>θ_path};               ← cross weak-zone scan
                  attach empirical-null q-value (R7) + low_score_cause
LGP-3  DECOMPOSE  per cross-node: host deficits d_F,d_P,d_A;             HYPOTHESIS
                  π* = argmin; flag entangled (high δ); disease weak πB
LGP-4  RANK       Impact via geometric-mean leverage → Pareto-80 set     (within-organism only, §4.4)
LGP-5  LEVERAGE   L = ΔℳH / ∛(C_t·C_s·C_e); serial-critical → top        (within-organism only)
LGP-6  SYNTHESIS  pillar-agent proposes axis-typed move on π*            cross-axis move REJECTED
                  (polarity-checked: host=stabilize, lesion=suppress)
LGP-7  SELECT     η = ΔℳH/Cost; max-η feasible under (T,S,E) budget
LGP-8  PLAN       topological order; planned U-trajectory U_planned(t)
LGP-9  ALLOCATE   resource gaps across the three prices (one organism)
LGP-10 PULSE      re-run twin; ε = U_planned − U_actual;
                  ε ≥ 0.10 → re-enter LGP-5;  U↓ → EMERGENCY revert
        ── SSS-GUARD GATE (irreversible / decision-grade only) ──        see §5.3
LGP-11 REPORT     milestone card per move (TESTABLE register only)
LGP-12 AUDIT      Δℳ_total(one node), ΔSI, keep-rule §5.4; PEC=Δℳ/Cost;
                  then LEARN (impact/weights; ε→UCB1→Thompson; transfer β)
```

**Where the SSS engine runs (TRB B5).** The full two-stage jury runs **only** on (a) top-K leverage cross-nodes and (b) AT_RISK/CRITICAL nodes; the rest carry bare quantitative-proxy scores. SSS is invoked a second time as the SSS-Guard ensemble before any irreversible/decision-grade recommendation.

### 5.3 SSS-Guard — retrodictive vs prospective gating (the §M2 fix)

SSS is the single point of architectural failure, so the cycle **never acts on one verdict.** v1.1 splits the gate by whether an external metric *can* exist:

- **Retrodictive / validation mode (an external outcome metric exists).** Any irreversible (simulated) call requires **3 independent SSS instances; accept only if ≥2-of-3 agree within tolerance AND the verdict agrees with the external biological/clinical outcome metric.** This is the *validation* path — it can only confirm hypotheses whose answer is already externally checkable, and that is its point.
- **Prospective mode (the hypothesis is genuinely novel — *no* external metric exists).** This is the engine's actual purpose, and here **there is no `pass` state.** The only admissible outputs are **`UNVALIDATED_HYPOTHESIS`** and **`queue_for_V3`** (wet-lab / collaborator / IRB). The gate **must not** stretch a weak proxy into a faux-external metric to manufacture a pass; if no genuine external metric exists, the call cannot be "accepted," only queued. This blocks the tautology trap (an engine that only "passes" things already in the literature) by making novelty a *queue*, not a *verdict*.
- In **either** mode, if no feasible queue raises organism U above threshold within budget, the engine returns **`DECOMPOSE_FURTHER`** rather than a false plan. SSS-Guard governs **simulated/recommended** actions only — there is **no autonomous biological action** (TRB NON-GOAL 6).

### 5.4 Audit, learning, the keep-rule, and the Meaning trajectory

A move is *kept* only if `Δℳ > 0` **and** `ΔSI > 0` **and the keep-rule below holds.**

> **The δ keep-rule, corrected (the §M6 fix).** The prior hard rule "δ must fall on every kept move" wrongly rejects valid sequential interventions: raising the weakest pillar *past* the others makes a previously-strong pillar the new minimum and can *raise* δ transiently while genuinely improving the system. The corrected rule: **keep iff (δ falls) OR (the previous minimum pillar rises above the previously-second pillar)** — i.e. the move must either flatten the profile *or* demonstrably lift the binding constraint; whichever the leverage math prefers. A move that raises average U purely by widening a decoupling (the binding pillar unchanged, a strong pillar inflated) is still rejected.

`PEC = Δℳ/Cost` is logged per move. **LEARN** updates (TRB §6.5): `impact^(g+1)=(1−λ)impact^(g)+λ·observed_ΔSI` (λ=0.3); weights by `corr(contribution,ΔSI)`; exploration ε-greedy→UCB1→Thompson; cross-domain transfer `β=(cosF+subgraph-iso-P+jaccard-A)/3` (always computable; validity B3-pending), applied **within and across slices of a single organism's matrix**, and only if it beats cold-start. The headline report is the currency-resolved **Meaning curve** `ℳ_org(t) = ∫U_org(t)dt` (single node) before/after the queue.

### 5.5 Worked example — HFrEF (Axis B) localized to ventricular-cardiomyocyte ischemia (Axis A)

> **READ FIRST — this is a *consistency illustration on a known case*, carrying ZERO predictive evidence (the §M1 fix).** The proxies below were assigned *knowing* that reperfusion is the textbook-correct move for ischemia; the example therefore shows only that **the machinery is internally consistent and reproduces a known answer when fed inputs consistent with it** — classic retrodiction. It is **not** evidence the engine generates non-obvious correct predictions. The *only* evidence claims TSE makes are the held-out tests TSE-P0/P1/P2/E1 (§8). All numbers are illustrative model-internal scores in B3-pending claim envelopes; not a clinical statement about any person.

**Axis-B node** `b = HFrEF` (MONDO:0005009, ICD-11 BD1x), `suppress` polarity, Mode A:
- `F_b = 0.86` — durable lesion (persistent LV fibrosis on CMR), non-resolving NT-proBNP trajectory, chronic-progressive (`form_class: LATTICE_APPROX` cross-check passes because FORM rests on imaging/biomarker, not ICD stability).
- `P_b = 0.71` — `P=√(locus·context)`: localizes to LV myocardium but HFpEF/non-cardiac-dyspnea confounders lower `context`.
- `A_b = 0.86` — relentless progression, high DALY burden.
- `U_b = ∛(0.86·0.71·0.86) = 0.806`. **Polarity = suppress; high U_b ⇒ a robust, entrenched adversary.** Disease weak pillar `πB = Position`.

**Axis-A target via `MANIFESTS_IN`:** `b → a` = ventricular cardiomyocyte (CL:0002131) in LV myocardium, `κ = 0.74`. Edges: `LOCALIZES_TO` via HPO `HP:0001635 → UBERON LV` (Position, `w=0.93`, curated); `PATHWAY_PERTURBS` via Reactome hypoxia/OXPHOS-failure → vCM **Action** (`w=0.88`); `GENE_DRIVES` (atherogenic substrate) → hepatocyte/endothelial **Form** (`w=0.6`).

**Axis-A node** `a = vCM`, ischemic (TRB §5.4 corrected example): `F_a=0.92` (identity intact), `P_a=0.30` where `P=√(q·c)`, `q=0.95` locus correct but `c=0.18` perfusion/pO₂ context destroyed, `A_a=0.40` (Vₘ depolarizing, ATP↓ — downstream Action of the Position-context loss). `U_a = 0.475`; `δ = 0.667`; `SI = 0.171` → **CRITICAL.** Host bind pillar `π* = Position`.

**Cross-node** `CrossWeak = κ·(1−U_a)·sens(Position→Position) = 0.74·0.525·0.9 ≈ 0.35` (well-supported diagonal `sens`) — survives the empirical-null/FDR band (`genuinely_imbalanced`). vCM is on a **serial survival-critical** subtree, force-promoted (LGP-5).

**One-directional grounding A→B (§4.2):** the disease's Position-grounding is pulled by the vCM's collapsed Position pillar: `P_B*(HFrEF) = √(0.71·0.30) = 0.461`; `U_B* = ∛(0.86·0.461·0.86) ≈ 0.69`. **`U_a` is NOT re-written by `U_b`** — the join is read-only on Axis A, so this number is a function of two independently-measured inputs (TRB Axis-A scoring + clinical Axis-B scoring), which is what lets TSE-P2 (§8) falsify it.

**Axis-typed selection (LGP-6/7):** `π* = Position` ⇒ **only Position-axis interventions are admissible** — reperfusion / re-vascularization. An inotrope (Action) or gene therapy (Form) is **rejected**: it raises a non-binding pillar while `P_a` stays ≈0.30 and `U_a` stays ≈0.47. This is non-circular **only because** the Position proxy is perfusion territory, not Vₘ (TRB §2.6) — *and it is retrodiction: the proxies were chosen knowing reperfusion is right.*

**Twin simulation (LGP-8/10):** Position restores `c: 0.18→0.85` (reperfusion); Action recovers `A_a: 0.40→0.80`. Re-score: `P_a=0.90`, `U_a=0.872`, `SI: 0.171→0.79` (STABLE); `Δℳ>0`; `δ: 0.667→0.13` (falls — keep-rule §5.4 satisfied). The symptom layer is the *organism-level* readout: **dyspnea (HP:0002094)** and **edema (HP:0000969)** are `PRESENTS_AS`/`MANIFESTS_IN` surface signs whose Action proxy estimated the renal/pulmonary Position-context collapse — **not** a per-cell measurement.

> **Whether the disease U "re-reads lower" is now an *external* question (§M5 fix).** Because back-loading is removed, "restore host pillar → disease U drops" is **no longer true by construction.** The claim that suppressing the host deficit lowered the pathology is tested against an **external disease-activity metric** (biomarker / imaging — e.g. NT-proBNP decline, EF recovery), not against a coupled re-read. If the external metric does not move, the framework has produced a falsifiable miss, as it should.

**SSS-Guard:** because a registry reperfusion-survival association *exists*, this runs in **retrodictive mode**: 3 SSS instances, 2-of-3 agree STABLE AND agree with the external metric → passes as a **B3-pending research hypothesis on a known case.** A genuinely novel cross-node with no such metric would instead emit `UNVALIDATED_HYPOTHESIS` + `queue_for_V3` — never `pass` (§5.3).

**Report (LGP-11, claim envelope, verbatim register):**
> `"Model flags cross-node (vCM[CL:0002131] × HFrEF[MONDO:0005009]) weakest on Position-context (perfusion); HYPOTHESIS for study; mechanism-axis conditional on proxy-axing (TRB §2.6/O8). Highest-leverage simulated move (within-organism): niche/perfusion restoration. Δℳ>0, keep-rule holds in twin; SSS-Guard retrodictive 2/3 + external metric. Level: B3-pending. Model-internal fragility index for an entity-type; NOT a clinical measurement, NOT advice for any individual."`

The renderer **never** prints "the patient's heart stability is 0.475" — banned lexicon (O2/B4).

> **Sepsis, for contrast (that the triad discriminates, TRB R9).** Sepsis (Mondo:0001327): **F≈0.55** (Form-fragile *as an entity* — heterogeneous, but scored from lesion/biomarker durability, not Sepsis-1/2/3 definitional churn, which is `LATTICE_APPROX`-flagged), **P≈0.45** (poorly localized — systemic), **A≈0.90** (catastrophic energetic derangement). `U_disease = 0.617`; `weak_pillar = Position`. Less entrenched than HFrEF but far more violent in Action — the non-compensatory mean refuses to average that violence away.

### 5.6 The completing currencies (Freedom, Coherence)

TSE inherits TRB §5.5: **Freedom/Irreversibility** is a per-node 4th pillar; **Coherence** is an *aggregation-level* relational input (Kuramoto `r`), not a 5th leaf factor. Both are **two-sided** (band-centred, interior optimum) and stay **INTERPRETATION — render no number — until P7/P8 pass.** Following revised TRB, the admission gates are **per-currency and symmetric**: **Freedom is admitted only by P7 (independence of Freedom from Form) and removed from the ledger if P7 fails; Coherence is admitted only by P8 (system-level coherence non-compensation) and removed from the roll-up if P8 fails** (TRB §9.8). The CytoTRACE/potency proxy for Freedom is **transcriptome-derived and carries the same separability shadow as FBA-Action** (excluded from the input-independence claim until it earns it), and the coherence term is **admissible only where a parent-level order parameter is actually measured (heart/brain); elsewhere it is UNKNOWN, never silently 1.0.** The control cycle **may not select a Freedom- or Coherence-typed intervention as a decision-grade move** until those falsifiers clear. Their dual-use surface (forced de-differentiation; induced fibrillation/seizure, cheap near criticality) is governed in §9.7.

> **Carried verbatim from revised TRB §5.5.3/§A.4 — two corrected canon facts.** (1) **The QTC parallel** (coherence is *conditionally* protected, never automatic) transfers as a **structural lesson, not verbatim**: under a device's **native (independent) noise the coherence benefit is `R ≈ 0`** — *not* the older "≈ −0.21" figure — rising to `R = +0.97` only under **collective-symmetric** noise (QMC §184 attributing the experiment to QTC §8.3, accession `IBM/qtc_hw_collective_marrakesh.txt`); QTC's substrate is quantum/symmetry-gated, biology's is classical/threshold-gated, so the shared invariant is *earned, conditional protection that must be tested (P8)*, not a fifth factor written into a product. (2) **NDT is amended, not obeyed:** biology lifts **non-uniformly** (Freedom per-node, Coherence aggregation-level — no clean per-node `U₅`), and TSE/TRB populate the 5th slot via **classical Kuramoto coherence, not NDT's reserved quantum 5th** — biology gets *coherence, not entanglement* (≈ "4.5 of 5" currencies), the entanglement reading rendering no number (O9).

---

## 6. Biosphere-scale extension — nested triadic systems (Axis A↑)

This is the upward continuation of Axis A into ecology — the corpus's most literal triad registration *and* its most epistemically exposed part. **The ceiling here is *lower* than TRB's: most of this section is B0–B2; the buildable B3-pending hooks are few and narrow (E1). Nothing here is B3-validated, nothing is B4. Cross-node ℳ-allocation is forbidden above the organism boundary (§4.4) — so this section can *describe* fragility but can never *rank which population gets the budget.*** That ranking is the eugenics attractor scaled to ecology and does not exist in TSE.

### 6.1 The upward recursion — one node type, six new strata

```
  ... molecule → cell → tissue → organ → system → ORGANISM   ← TRB stops here
                                                   │ (hinge)
                                          population → species → community → ecosystem → biome → BIOSPHERE
                                                   └─────────────── TSE §6 ──────────────────┘
```

| Scale | **Form** (↔Time) | **Position** (↔Space) | **Action** (↔Energy) |
|---|---|---|---|
| **Population** | genetic/age structure; *Nₑ*; heterozygosity | occupied range; patch occupancy; connectivity | recruitment − mortality; biomass production |
| **Species** | taxonomic identity; genetic diversity; trait integrity | geographic range (EOO/AOO); niche breadth | trophic function; pollination/dispersal/decomposition |
| **Community / guild** | composition; functional-group representation | spatial co-occurrence; habitat extent | aggregate process rate |
| **Ecosystem** | community structure + functional completeness; **food-web topology** | biome placement; area; fragmentation; abiotic envelope | **energy & nutrient flux** (GPP/NPP/respiration; N/P/C cycling) |
| **Biome** | characteristic community-type integrity | global extent; latitude/altitude band | biome-scale contribution to planetary cycles |
| **Biosphere** | total biodiversity | planetary spatial integrity (intact vs converted) | global biogeochemical cycles |

> **VISION (B0).** "The biosphere is a meta-organism whose `ℳ` we raise" is **framing, not a tested model capability**, and — critically — **`ℳ` is never aggregated across ecological nodes (§4.4)**, so "raise the biosphere's ℳ" is a *direction*, not an *allocation*. Gaia-style organism analogies are contested in ecology and are *not* asserted as fact. No number rendered to a user may use meta-organism language, and **no leverage rule ever ranks ecological nodes against each other for intervention budget.**

The schema, primitives, AND/OR roll-up, and per-node `ℳ=∫U dt` carry up *syntactically* (**B1**). Whether they carry up *meaningfully* is the open question, and at this scale it is *harder* than TRB's already-unsettled separability problem.

### 6.2 Node/edge schema and the data-gap partition

The `BioSystem` node extends to an **`EcoSystem` node**, edges still loading exactly one axis: `IS_A`/`PART_OF` (Form, GBIF/Catalogue-of-Life/RESOLVE); `OCCUPIES_RANGE`/`IN_BIOME`/`PREYS_ON`/`POLLINATES` (Position — the *dependency* relation, GBIF/IUCN/Map-of-Life/WDPA/GLOBI/Mangal); `TRANSFERS_ENERGY_TO`/`FIXES`/`CYCLES_NUTRIENT` (Action — energy *actually moved*, split per TRB fix E2; Ecopath/FLUXNET/MODIS-GPP); `THREATENS`/`DISRUPTS` (per-target, IUCN Threats Classification).

> **The Linnean & Wallacean shortfalls are this section's `Phase-0`.** The **Linnean shortfall** (most species undescribed — *Form* unknown for the majority of nodes) and the **Wallacean shortfall** (distributions poorly known — *Position* unknown) make a literal biosphere U-scan **not runnable.** Any biosphere-`U` is computed over a *massively incomplete, non-randomly missing* node set. This is the load-bearing limitation, not a footnote.

**Buildable now** (Form: GBIF; Position: IUCN EOO/AOO, WDPA, ESA-CCI/Hansen land-cover; Action: FLUXNET/MODIS GPP, Ecopath flux *models* — model output, not measurement) versus **conceptual/data-gap** (genome-resolved Form for most species; niche-context for most invertebrates/fungi/microbes/marine taxa; a *complete* food web — which exists for no real ecosystem).

### 6.3 Scoring, roll-up, and the ecological weak-zone scan

Per-node scoring is identical to TRB §5.1. Several ecological pillars are **two-sided** (interior optima — oligotrophic *and* eutrophic both *change* function), so they use band-centred normalization (TRB R2).

> **"Changed" ≠ "collapsed" (the §M3 value-judgment fix).** An oligotrophic system is **not collapsed** — it is a different valid state. The band-centred score measures *distance from a declared reference band*, and **which state counts as "degraded" is a value judgment supplied externally under governance, never inferred by TSE.** The engine reports "ecological state moved by Δ from reference band"; it does **not** report "this state is bad."

> **Planetary boundaries demoted to contested B1/B2 framing (the §M3 fix).** The Rockström/Steffen planetary boundaries are **global** control variables with contested and revised thresholds; several (biosphere integrity, novel entities) are themselves unquantified. They are **not** decomposable to per-node ground truth, and their Action variables (GPP/NPP) *overlap the node Action proxies*, so they are **removed from the leakage-independent anchor list.** They may be cited as *contested framing*, never as fixed external truth. The remaining genuinely-external anchors are the **IUCN Red List of Ecosystems** (ordinal, for nodes whose Form is *not* scored from it — see §6.5) and **IUCN range thresholds** + protected-fraction (Position).

Roll-up uses TRB's AND/OR operator: **serial (AND) = keystone / foundation / sole engineer** (collapse cascades); **parallel (OR) = functional redundancy** (a redundant guild degrades gracefully).

> **Keystone/redundancy is `LATTICE_APPROX` for ecology (the §Mo7 fix).** Keystone status is **context-dependent** (a species is keystone in one season/site, redundant in another), and "functional redundancy" vs "response diversity" is contested. The serial/parallel node tag is therefore an approximation held to the higher bar, expected to misclassify, and is exactly what E1 is designed to *falsify*.

The weak-zone scan ports with multiplicity discipline (R7) made *more* mandatory: `argmin` over ~10⁵–10⁶ nodes on non-random missingness means **`evidence_sparse` is the *default* hypothesis for a low ecological score**; only nodes surviving the empirical-null + FDR control are emitted, and a weak zone that is really a data gap is reported as *"not distinguishable from sampling bias,"* never as a finding.

### 6.4 Worked example — a coral-reef ecosystem node (consistency illustration, B2; NOT a real assessment)

> **READ FIRST — like §5.5, a consistency illustration carrying zero predictive evidence.** Scores are illustrative and almost certainly correlated (bleaching hits cover, context-readout, and flux because they share remote-sensing/survey signals — the separability problem at ecosystem scale). The clean "Position is binding" story is **conditional on a separability test not yet run for any ecosystem** and may fail.

A central Great Barrier Reef ecosystem node. **Baseline (healthy):** Form 0.88, Position 0.85 (SST anomaly +0.4°C, aragonite Ωₐ=3.6), Action 0.83 → `U=0.853`, `δ=0.056`, `SI=0.765` → **STABLE.** **Marine-heatwave stress** — binding deficit is **Position-context** (SST +2.5°C, Ωₐ=2.6 sub-saturating — the corals have not moved, their *context* turned hostile): Form 0.55, **Position 0.22**, Action 0.45 (flux collapses with the context loss — Action's role is *shown*, not just asserted: with `P=0.22` and `A=0.45`, `U=∛(0.55·0.22·0.45)=0.388`, `δ=0.589`, `SI=0.154` → **CRITICAL**).

The scan localizes the binding constraint to **Position-context**; the illustrated first lever is **context restoration** (warming driver, MPA placement, assisted thermal adaptation) rather than coral outplanting alone — because outplanting into a context with `P→0.22` cannot raise `U` (the geometric zero bites the unaddressed pillar). **This is a fragility *description*, never an intervention directive and never a ranking of this reef against another reef for budget (§4.4).**

### 6.5 The ecological falsifier (E2 retired; E1 carries the load)

- **E1 — serial/parallel structure predicts collapse pattern (B3-pending, runnable now — the load-bearing ecological test).** Nodes tagged `serial` (keystone/foundation, by interaction-network centrality) cause larger `ΔU`-cascades on simulated removal than `parallel` (redundant) nodes. *Falsifier:* cascade size uncorrelated with the model's serial/parallel tag on held-out food webs (GloBI/Mangal/Web-of-Life vs the published secondary-extinction literature). **The cleanest B3-pending test in TSE** — food-web topology is *measured structure*, not a transcriptome transform, so it sidesteps the §8.3 collinearity worry, and it directly tests the `LATTICE_APPROX` keystone tag (§6.3).
- **~~E2 (Position-anchored fragility retrodiction)~~ — RETIRED as conceded-circular (the §M4 fix).** E2 proposed validating low-SI against IUCN-RLE at-risk listings, but §6.2/§6.3 build the Form anchor *from* RLE collapse criteria — so the leakage audit cannot separate them; "low SI predicts at-risk" would merely restate "at-risk ecosystems are at-risk." E2 is **removed**, not parked. If a future RLE-independent Form source is built, an RLE-validated test can be *re-proposed* then. Until then TSE leans on E1 alone.

Everything else — the biosphere meta-organism, "stabilize all beneficial life," the recursion past the ecosystem — is **VISION (B0–B1)** and is marked as such wherever it renders.

---

## 7. Phased roadmap

| Phase | Goal | Runnable here? | Gate / ceiling |
|---|---|---|---|
| **P0-A** | Axis-A pillar separability (TRB Phase-0) | yes (tissue slice) | conditional dCor/CMI independence, donor-level, no Pearson \|r\|; **FBA-Action excluded, measured Action where it exists** (TRB §8.4/B-2); pass before any A verdict |
| **P0-B** | **Axis-B disease pillar separability** | yes (disease panel) | **TSE-P0(B)**; B-axis renders no number until it passes (§9.1) |
| **P0-A×B** | **cross-link beats marginal A, B AND single-axis vs external localization truth** | yes (held-out) | **TSE-P0(A×B)**; A×B payload retired if it fails (§9.10) |
| **V1** | retrodiction — A×B edges recover known disease–tissue associations | yes | AUC ≥ 0.70 vs curated gold standard (TSE-P1) |
| **V2** | blind prediction — grounded `U_B*` beats `U_B`, `U_A`, AND plain A+B regression | yes | ΔR² ≥ 0.1 vs *the strongest* of those baselines (TSE-P2) |
| **V3** | prospective causal (twin → wet-lab) | **no** — needs collaborator/IRB | the on-ramp to clinical B4 |
| **ECO** | biosphere extension to a B2 model + E1 only | E1 yes; whole-biosphere no | stays B0 telos if no external metric reached |

The committed product of TSE is the **pre-registered dual-axis separability test (P0-B, P0-A×B)** plus E1, **not** the diagnostic→therapeutic engine. (TRB B-1 fix: *do not sell the deferred product.*)

---

## 8. Validation and falsifiers (pre-registered; all designed to be falsified)

- **TSE-P0(B) — disease separability.** F, P, A of a disease carry **conditionally independent** information across a disease panel. *(All thresholds on dCor/CMI, conditional, donor/cohort-level — never Pearson |r| — exactly as TRB §8.5; the **0.6–0.8 band is pre-committed "inconclusive → never a pass."**)* *Falsifier:* pairwise |dCor| > 0.8, or a pillar's conditional dependence given the other two is near zero, or it lands in the 0.6–0.8 band at achievable donor *n* (the most likely failure — disease proxies may all be downstream of one severity construct). *Success:* each pillar adds conditional dependence with a CI **below 0.6** on held-out diseases. *The §C3 FORM fix raises the chance of passing honestly by removing nosology-shared FORM.*
- **TSE-P0(A×B) — cross-link validity.** The model's A×B links predict an *external* localization ground truth (lesion histology, GWAS-to-cell-type colocalization) better than the marginal A and B scores alone, with a **feature-leakage audit**. *Falsifier:* no lift beyond a comorbidity-frequency / degree-preserving random-bipartite null.
- **TSE-P1 (join validity):** disease→anatomy edges recover known disease–tissue associations on a held-out set. *Falsifier:* no better than a degree-preserving random null. *Success:* AUC ≥ 0.70.
- **TSE-P2 (propagation lift — corrected, the §C2 fix):** grounded `U_B*` predicts severity/outcome class better than **(a) intrinsic `U_B` alone, (b) `U_A` alone, AND (c) an unconstrained ordinary A+B regression.** *Falsifier:* ΔR² CI includes 0 against **the strongest** of those three baselines — in particular, if a plain linear A+B mix matches `U_B*`, the non-compensatory geometric grounding (§4.2) is ornamentation and is **retired.** *Success:* ΔR² ≥ 0.1 vs the strongest baseline (donor/cohort the unit of independence — TRB R8; multiplicity-corrected per R7).
- **TSE-P2b (disease-U external validity — NEW, the §Mo5 fix):** `U_disease` (entrenchment) predicts an **external therapeutic-resistance / chronicity metric** (e.g. relapse rate, time-to-refractory, line-of-therapy count) beyond a plain severity baseline. *Falsifier:* no lift over severity → "disease robustness" is not triadically structured and the polarity model is decorative. *This tests the orientation flip itself, which nothing previously did.*
- **TSE-P2c (leverage primitive — NEW, the §Mo4 fix):** ranking interventions by `Priority = Δℳ/∛(C·C·C)` predicts better simulated/wet-lab `ΔU` outcomes than ranking by severity, by cost alone, or by clinician judgment. *Falsifier:* leverage ranking no better than severity ranking against a held-out outcome null. *Nothing previously tested the leverage rule; E1 tests cascade structure, not the primitive.*
- **TSE-P3 / mechanism (O8):** the pillar a disease is flagged on is **stable under proxy-reassignment.** *Falsifier:* the label flips → the attribution is INTERPRETATION, not a finding. *This is TSE's clinical mirror of TRB's gated mechanism-localizer (P2-mech): if the gate fails the mechanism-axis claim is **retired** (reverts to "δ-spike / decoupling, axis TBD"), per the symmetric retirement rule (§9.10) — never parked in INTERPRETATION forever.*
- **P-B3 (symptom-as-surface-reading):** a symptom's Action proxy correlates with the Axis-A `Action` deficit of the *organ/system* it `MANIFESTS_IN` (NOT per-cell — §3.2), across an independent modality. *Falsifier:* no relationship beyond a base-rate null. *Expected to be weak; per-cell attribution is forbidden regardless of outcome.*
- **E1 (ecological):** as §6.5. (E2 retired.)

**Multiplicity & independence (TRB R7/R8) apply in full** — the *now-larger* A×B×ECO scan space demands a **study-level FDR plan across both axes and all P-tests**. The independent sample is the **disease / cohort / registry / donor / food-web**, never the patient-row or the cell.

---

## 9. RH discipline — scope, epistemics, ethics, non-goals (the governing section)

### 9.1 The central cut, on three surfaces

The TESTABLE / INTERPRETATION boundary is enforced on **every** TSE surface — A scores, B scores, and A×B link weights:

- **TESTABLE** — a statement about what *the TSE model does* over data, admitted only with (i) an operational procedure, (ii) a falsifiable prediction, (iii) an **external** ground-truth metric independent of the score being validated.
- **INTERPRETATION** — framing/metaphor; may generate hypotheses and label axes. **No number, verdict, colour, ranking, or arrow rendered to a user may be in INTERPRETATION language.** The renderer prints *"model fragility index for entity-type X, model-internal,"* never *"X's stability is 0.41,"* and never *"disease D is localized to cell C"* — only *"the model flags a hypothesised A×B link {D↔C}; HYPOTHESIS for study."*
- **VISION** — telos/motivation ("the New Biology," "stabilize the biosphere," "reduce entropy to maximize survival"). Confined to explicitly-marked VISION blocks; renders **no** number, verdict, ranking, or allocation; is **never** a section thesis and never a deliverable (§9.4).

The B-axis and cross-link inherit A's separability liabilities **in sharper form**:

| Surface | Separability liability (declared) | Gate |
|---|---|---|
| **A pillars** | three transforms of one transcriptome; **FBA-Action is computed *from* Form's data — broken *by construction*, not merely correlated, so it is EXCLUDED from the separability claim** (revised TRB §8.4/B-2); pLDDT dropped as a per-cell Form proxy; Phase-0 Action restricted to **measured** Action (Seahorse/respirometry) where it exists | TRB Phase-0 (P0/P0b on dCor/CMI, conditional, donor-level — no Pearson \|r\|) |
| **B pillars** | a disease's F/P/A risk being scored from **one** clinical source → one annotation → three axes; *mitigated in v1.1 by process-intrinsic FORM (§3.2)* | **TSE-P0(B)** — runs *before* any B verdict renders |
| **A×B link** | "disease D collapses pillar P in cell C" conditional on both axes being separable *and* the link not being a shared-annotation artifact | **TSE-P0(A×B)** — INTERPRETATION until it beats external localization truth AND single-axis scores |

The headline deliverable is therefore **demoted, by construction, to a hypothesis gated behind TSE-P0(B) and TSE-P0(A×B).**

### 9.2 Epistemic ladder — inherited B0–B4, two empty B4 slots

Canon's ladder, quoted verbatim (RH_CRITICAL_REVIEW §71–75, as carried by TRB §A.6/§8.5): **L0 = Meta-evaluation · L1 = Operational stability · L2 = Cross-domain analogy · L3 = Cosmological extension · L4 = Literal physical claim.** The B0–B4 column below maps onto **L0–L2 only**; **no TSE statement occupies canon-L3 or L4.** (The B1→L1 row uses canon's real meaning, *Operational stability*, not "within-model proof.")

| TSE level | Canon | What lives here in TSE |
|---|---|---|
| **B0** | L0 | "stabilize the biosphere / heal all life," Code/Credo/Rights framing — the *telos* (VISION). Renders no number. |
| **B1** | L1 | geometric-zero keystone; argmin weak-pillar; A×B matrix algebra; the LGP-12 cycle; one-directional grounding. |
| **B2** | L2 | every empirical TSE claim is *at most* this — A/B scores, link weights, ECO scores. |
| **B3** | narrowing of L2→application | the P0/V tests *as pre-registrations*; the leverage/intervention hypotheses (**project ceiling**). |
| **B4** | regulated, outside this plan | the diagnostic engine; any therapeutic or conservation action — **EMPTY (×2)**. |

**TSE has *two* empty B4 slots, both empty:** **Clinical B4** (individual care — prospective trials, IRB, SaMD/CDS pathway) and **Ecological B4** (acting on a population/species/ecosystem — ecological-risk assessment, Cartagena-Protocol-aligned biosafety for any release/biocontrol/gene-drive, independent EIA, community/rights-holder consent). Every artifact carries a `level` tag; the lint refuses any claim whose wording exceeds it. **Any B4 sentence — clinical or ecological — is a bug.**

### 9.3 Named overclaim risks

Inherited unchanged from TRB §9.3: **O1** (health/vitality/consciousness — banned ≤B3), **O2** (low U = dying), **O3** (diagnoses/treats/replaces clinicians), **O4** (triad is proven biology — B2), **O5** (higher U = worthier *organism* — **the eugenics attractor**; U never computed across persons), **O6** (jury is objective), **O7** (real-time body model), **O8** (weakest pillar names the mechanism — conditional on proxy-axing), **O9** (biology is quantum-coherent — Coherence is *classical* Kuramoto).

**New in TSE:**
- **O5b — "Higher U = a worthier *species / population / ecosystem*; cull the low-U ones" — the eugenics-attractor SCALED TO ECOLOGY.** The single most dangerous reading; a banned use. Realized at **two** levels, not one: **(label)** no cross-species/population worth *ranking* exists; **(operation)** no cross-organism **ℳ-aggregation or leverage-ranking** exists either (§4.4) — closing the leak whereby `Priority = Δℳ/cost` across populations would reconstruct the worth ordering without the word "worth." Three sub-bans: **(i)** no cross-species worth ranking; **(ii)** no score-driven triage of the biosphere — *"which organisms are useful"* is **not a TSE output and not a TSE-decidable question**; beneficiality is a *value choice made by accountable humans under governance*, supplied as input; **(iii)** no worth gradient over humans dressed as ecology. *"Who decides which organisms are useful"* is a **hard ethical guardrail and an open governance problem the engine does not solve** — acknowledged in writing, not declared solved.
- **O10 — "a symptom's U *is* the underlying organ's instability"** (and "*the cell's*" — banned outright; symptoms are organism-level, §3.2). Double-loads the matrix — banned until TSE-P0(A×B) passes.
- **O11 — "the dual-axis scan is the therapy / the conservation plan."** The scan is *hypothesis generation indexed by cell × location × manifestation* — not a treatment plan (O3) and not an ecosystem intervention plan (O5b-ii).
- **O12 — "TSE proves biology/ecology is triadic, or that stabilization is the meaning of life."** TSE is an *instance*, not evidence. *"ℳ = ∫U dt is the objective"* and *"heal all life"* are **B0/VISION telos.**

### 9.4 The VISION / ENGINEERING separation — the spine

| Claim | Register | Level | Renders a number? |
|---|---|---|---|
| "Biology is the basis for actively stabilizing life; reduce entropy to maximize survival." | VISION / telos | B0 | **No** |
| "ℳ = ∫U dt is the stabilization objective (per single node)." | VISION grounding (canon identity) | B0→B1 | Only as a *model-internal coverage indicator* on one node's rendered U, never as worth, never aggregated |
| "Stabilize the biosphere / heal all beneficial life." | VISION / telos | B0 | **No — telos, not a deliverable, not an allocation** |
| "TSE runs a dual-axis A×B scan and emits a ranked (within-organism), multiplicity-corrected weak-zone hypothesis queue." | ENGINEERING | B3-pending | Yes, iff TSE-P0(A/B/A×B) pass and the lint clears |
| "TSE localizes disease D to pillar P in cell C and recommends intervention I." | ENGINEERING, gated | B3-pending; B4 if ever acted on an individual/site | Hypothesis only; B4 empty |

> **The load-bearing sentence:** *the dual-axis scan is engineering; "stabilize the biosphere / heal all life" is VISION/telos — never a deliverable, never a ranking, never an allocation.* The active/deliverable voice (including the "New Biology" subtitle) lives only in VISION blocks; it may motivate but it may not ship as a number, verdict, ranking, or plan.

### 9.5 Real ontologies / resources (provenance is mandatory)

Every principle/node/link carries `G{src; conf; level; mode}` (accession + version + date). Unsourced principles are **B0 and cannot enter scoring.** **Axis A:** CL, UBERON, Reactome, GO, BioGRID/STRING, cell-type atlases. **Axis B:** ICD-11, SNOMED CT, MONDO, HPO/HPOA, DOID, Orphanet, OMIM, UMLS, **plus process-intrinsic FORM sources** (imaging cohorts/CMR/CT, biomarker-trajectory registries, histopathology grading); for a specific instance, the supplied **de-identified case definition IS the system** (SSS Mode B, §3.4). **A×B external ground truth (kept independent of scoring inputs, leakage-audited):** HPO↔UBERON, OMIM/Orphanet gene→tissue, GWAS-to-cell-type colocalization, lesion histology, DepMap, gnomAD, registry outcomes, GBD mortality. **Ecological (B0/B2 telos surface):** NCBI Taxonomy, GBIF, IUCN Red List (+ Red List of Ecosystems — *not* used to both score Form and validate, §6.5), WDPA, RESOLVE ecoregions, ENVO, GLOBI/Mangal/Web-of-Life, Ecopath (model output), FLUXNET/MODIS; **planetary boundaries cited only as contested B1/B2 framing (§6.3), never as anchor.**

> **The value-frame is itself contested and anthropocentric (the §Mo10 fix).** **IPBES "nature's contributions to people" (NCP)** is cited as *an* externally-authored value frame so that "beneficial" is visibly a human value choice imported under governance — but NCP is **anthropocentric by construction** (contributions *to people*) and therefore *is itself a worth-ranking of nature by human utility* (pollinators "valuable," "pests" not). Importing it does **not** neutralize the value judgment; a non-anthropocentric frame (e.g. intrinsic-value or ecocentric) would rank differently. TSE records the chosen frame *as a contested claim with a named authority*, never as objective fact, and the choice of frame is itself an accountable governance decision.

> *Reproducibility-metadata note (out of the spec body, retained for correctness).* The SSS Constructor CLI default model string should be current; as of this revision the recommended Sonnet ID is **`claude-sonnet-4-6`** (the older `claude-3-7-sonnet` snapshot is retired). This is a CLI default, affects no score, and is recorded here only so reproducibility metadata is correct.

### 9.6 Regulatory boundary — INTENT for *both* tiers, not settled fact

TSE is *designed* RUO and to sit outside both clinical and ecological regulation — **but classification is regulator-adjudicated, not self-determined** (TRB §9.4). A weak-zone map keyed by *cell × location × disease* that *ranks interventions* is exactly what a regulator scrutinizes, so this is **intent**, not settled fact. **Clinical:** not a medical device / diagnostic / CDS; recommendations address researchers about mechanisms; individual care is a new clinical-B4 project. **Ecological:** not a conservation-management / biocontrol / eradication / release / gene-drive tool; acting on a real population/site is a new ecological-B4 project. Across both: provenance on every artifact; RUO banner on every artifact; **human-in-the-loop and human-on-top; no autonomous/closed-loop action; no emergency/triage/monitoring pathway.**

### 9.7 Data ethics, dual-use, and the "who decides which organisms are useful" guardrail

Public ontology/literature first. Non-public human data, if ever used: de-identification (HIPAA Safe Harbor / GDPR), consent + IRB, never for individual care, never sent to external model APIs, minimized and not persisted (this is the §3.4 Mode-B envelope). Ecological data respects indigenous/community data sovereignty (CARE principles).

**Dual-use — stated honestly, not solved.** A *"find the weakest pillar and the cheapest flip"* engine is a **destabilization-target finder with the sign flipped** — stabilization and weaponization computations are *identical*; the fragility map is dual-use *regardless of stated objective* (TRB §9.5). TSE makes this hazard **strictly larger** along three axes, each acknowledged rather than declared eliminated:
1. **The clinical axis adds disease-targeting surface.** "Disease D destabilizes pillar P in cell C, cheapest flip X" is, sign-flipped, "to *induce* D, hit pillar P in cell C via X." **No released TSE artifact produces or ranks pathogen-targeting-of-hosts maps, induced-disease maps, or destabilization queries over A×B.**
2. **Coherence/Freedom add desynchronization and de-differentiation surface, cheapest near criticality** — induced fibrillation/seizure (Coherence), forced de-differentiation/oncogenesis (Freedom). Criticality-proximity of any beneficial system is **sensitive** and never published as a convenient "cheapest flip."
3. **The ecological extension adds species-/ecosystem-destabilization surface — the gravest.** "Cheapest stabilizing intervention for ecosystem E" is, sign-flipped, "cheapest collapse of E / cheapest eradication of population P / cheapest trophic-cascade trigger." **No released TSE artifact ranks ecosystem-, population-, or species-destabilization, desynchronization, or eradication targets;** ecosystem criticality-proximity is sensitive.

**The "who decides which organisms are useful" guardrail (the hardest new problem) — an unsolved governance boundary, never a feature:**
- The objective sign (stabilize vs. suppress) and the beneficiality judgment for *any* target are **externally supplied, justified, audited, and authorized** — never inferred by TSE. The judgment "this organism is beneficial / this is a pest" is recorded as a claim envelope with `register: VISION`, an external value-frame citation *flagged as contested/anthropocentric* (§9.5), and a **named accountable human authority**; an objective lacking that envelope is rejected at the lint.
- **No cross-species, no cross-population worth ranking, AND no cross-organism ℳ-aggregation/leverage allocation is computable, period** (§4.4) — the architecture provides no operation returning "species A is worthier than B" *and none returning "spend the budget on A because Δℳ/cost is higher."* The O5b ban is realized in the type system at *both* levels.
- **Residual risk acknowledged, not solved.** An objective deny-list constrains *objectives*, not *outputs*; the controls (public-data-first, no destabilization queues released, gated+logged access, value-frame-with-named-authority, organism-boundary ℳ-firewall, human-on-top) are **necessary but not sufficient**, and the boundary is **partly social/operational, not purely technical.**

### 9.8 Explicit NON-GOALS

Inherited from TRB §9.6 (abbreviated): (1) not a diagnosis/prognosis/treatment recommender for any individual; (2) not a measure of health/wellness/vitality/fitness/life-death/consciousness; (3) not a real-time physiological simulator; (4) **not an organism/person ranking or worth metric (no cross-individual U)**; (5) not a proof that biology is triadic; (6) not autonomous; (7) not a replacement for clinicians/biologists/ecologists/validation/regulatory review; (8) not a source of B4 claims; (9) not a destabilization/weaponization tool (incl. Coherence-desync and Freedom-de-differentiation); (10) not a universal-constant engine (0.618 and every anchor/threshold are tunable defaults); (11) not a mechanism-localizer until the relevant Phase-0 passes.

New in TSE: **(12)** not a single-axis collapse (A×B is a hypothesis surface — O10); **(13)** not a cross-species/cross-population worth/usefulness/triage engine (O5b-i/iii); **(14)** not an originator of the "which organisms are useful" judgment (beneficiality is an accountable, contested external input — O5b-ii); **(15)** not a conservation-management/biocontrol/eradication/release/gene-drive planner and not an ecological closed-loop actor (ecological B4 empty); **(16)** not a biosphere-healing deliverable ("heal all life" is B0 telos — O12); **(17)** not a destabilization/eradication target-finder at population/ecosystem scale (§9.7); **(18 — NEW)** **not a cross-organism resource-allocator** — no ℳ-aggregation or leverage-ranking exists above the organism boundary (§4.4); the engine cannot decide which population/species/ecosystem receives intervention budget.

### 9.9 Mechanizing the discipline — claim envelope and output lint

```
{ axis ∈ {A, B, A×B, ECO},
  register ∈ {TESTABLE, INTERPRETATION, VISION},
  epistemic_level ∈ {B0,B1,B2,B3,B4},
  text, value,
  evidence{ n_valid_models, consensus_pct, mode ∈ {A_abstract, B_specific} },
  provenance[],                              # accession+version+date, mandatory
  external_ground_truth{ metric, value, agreement, mode ∈ {retrodictive, prospective} },
  objective_sign ∈ {stabilize, suppress},    # declared per target (§9.3-O5b)
  value_frame{ name, contested:true, anthropocentric:bool },  # required iff a beneficiality judgment present (§9.5)
  accountable_authority }                    # named human, required for any beneficiality/objective claim
```

The **output lint refuses** (TSE renders nothing on a refusal): (1) any claim above **B3** — *any clinical or ecological B4 sentence is a bug*; (2) any ≤B3 claim using **banned lexicon** (health/diagnose/treat/cure/conscious/vitality/"worthier organism/species"/"cull"/"eradicate"/"useful species"…); (3) any decision-grade B3 claim lacking an **external ground-truth metric** or **≥2-of-3 SSS-Guard agreement** — *and any prospective-mode claim asserting `pass` rather than `queue_for_V3` (§5.3)*; (4) any **cross-person, cross-population, cross-species U aggregation, OR any cross-organism ℳ-aggregation / leverage-ranking / worth ranking / triage** (the O5b realization at *both* the worth-label and the allocation level — a hard type-level refusal, §4.4); (5) any **A×B link, B-axis U, ECO-node U, Coherence/Freedom score** rendered before its gate passes; (6) any **destabilization / desynchronization / de-differentiation / eradication** target query, pathogen-targeting-of-hosts map, or ecosystem-collapse map; (7) any beneficiality/objective-sign claim lacking a **`value_frame` (flagged contested) + named `accountable_authority`**; (8) any weak-zone flag (A, B, or ECO) lacking a **multiplicity-corrected q-value** clearing an absolute verdict band — else emitted as *"not distinguishable from scan noise"*; (9) any symptom score **attributed to a specific cell** (organism-/organ-level only, §3.2).

Every weak-zone flag is emitted as a research hypothesis tagged `low_score_cause ∈ {evidence_sparse, genuinely_imbalanced, lattice_approx, sens_sparse, axis_unseparated}`; only `genuinely_imbalanced` on a *gated* axis is a candidate biological hypothesis. A flag on an un-gated axis is `axis_unseparated` and renders as *"not yet interpretable — axis separability pending."*

### 9.10 Symmetric retirement rule (closing the unfalsifiability shield)

"INTERPRETATION-until-falsifier" must not become a motte that can never be stormed. Pre-registered alongside each gate:
- If **TSE-P0(B)** fails (disease F/P/A collinear), the **B-axis is retired** from rendering — removed from scorer and UI; TSE reports *"the clinic/pathology axis is not separable; the dual-axis claim is narrowed to single-axis (anatomy) scoring."*
- If **TSE-P0(A×B)** fails (links don't beat marginal A,B *and single-axis* against external localization truth), the **cross-product payload is retired** — TSE reports *"A×B localization is not supported; the engine is two independent maps, not a localizing engine"* (the most valuable possible negative).
- If **TSE-P2** fails (grounded `U_B*` doesn't beat the strongest of `U_B`/`U_A`/plain A+B regression), the **non-compensatory grounding (§4.2) is retired as ornamentation** — TSE reports the propagation adds nothing over a linear mix.
- If the **ecological extension** never reaches a B2 model with an external metric (E1), it **stays B0 telos forever and renders no number.**

Reporting any narrowing is **TSE's contribution to canon** (universality *narrowed by* clinic/ecology, not confirmed by it — TRB §A.2), not its failure.

### 9.11 Cross-appendix coherence

- **vs. SSS** — TSE reuses the SSS engine unchanged on both axes (Constructor + ≤50-model jury, IQR → weighted → geometric → consensus, φ⁻¹≈0.618 stakes-adjustable θ, Modes A/B). **Declared divergence (TRB m-10):** SSS *does* score and rank a named individual and sells cross-system comparability; TSE **reverses this for worth** *on purpose* (the eugenics attractor) and extends the divergence to species/populations (O5b) *and to ℳ-allocation* (§4.4). High cross-domain U is *structurally* valid but *metrically* provisional (SSS-L5); cross-**worth** ranking and cross-**organism allocation** are *banned*, not provisional.
- **vs. TRB (revised)** — Axis A *is* TRB; TSE adds B, A×B, the control layer, and the ecological telos, inherits TRB's registers/ladder/SSS-Guard/dual-use posture/non-goals, and extends each. **TSE inherits revised TRB's re-scope:** TRB's *product* is the two runnable tests (P0/P0b separability, P8 coherence non-compensation), and its mechanism-localizer ("weakest pillar names the mechanism") is a **demoted, gated hypothesis (P2-mech), retired if its gates fail** — so **TSE does not present Axis-A mechanism-localization as a settled TRB capability**, and the A×B payload is explicitly *downstream of* an Axis-A precondition (P0-A) that may fail. TSE carries TRB's corrected canon facts verbatim (QTC native-noise `R ≈ 0`, not −0.21; the L0–L4 ladder; NDT *amended*, not obeyed; FBA-Action excluded from separability; coherence is classical, "4.5/5"). The clinical B4 slot TRB left empty stays empty; TSE names and leaves empty a second ecological B4 slot.
- **vs. GSI-RTD** — both axes implement the `TriadicDomain` interface; the canonical runtime runs on the A×B matrix with no bespoke orchestration.
- **vs. canon (ℳ = ∫U dt)** — Form↔Time / Position↔Space / Action↔Energy held exactly; `ℳ=∫U dt` is the stabilization objective **of a single declared node**, `𝒮_disease=∫U_disease dt` its dual, with `ℳ+𝒮=T` on a single clock. No statement here occupies canon-L3/L4; **both clinical-tier B4 slots stay empty.**

---

## 10. Glossary

| Term | Definition |
|---|---|
| **TSE** | Triadic Stabilization Engineering — the engineering discipline (this appendix, umbrella over TRB) that turns the triadic stability map into actively-maintained, simulated, guarded recommendations; objective ℳ = ∫U dt of a single declared node. |
| **Axis A** | Anatomy/structure decomposition = TRB: `organism → … → molecule`. Polarity `stabilize`. |
| **Axis B** | Clinic/pathology decomposition (new): `health → … → symptom`, a DAG. Polarity `suppress`. |
| **A×B** | the typed, evidence-bearing bipartite graph linking a disease (B) to weak zones in cells/organs (A) — the payload. Grounding is **one-directional (A→B), single pass** (§4.2). |
| **`ClinSystem` / `EcoSystem`** | the `BioSystem`-typed node classes for Axis B and the ecological extension. |
| **U / δ / SI** | `∛(F·P·A)` (any pillar→0 ⇒ U→0); `δ=(max−min)/(max+0.01)`; `SI=U/(1+δ)²`. |
| **polarity** | `{stabilize, suppress}` per node: stabilize ⇒ raise U (host); suppress ⇒ lower U (disease). The orientation flip; suppress-θ is *lowered* for high-mortality diseases (§3.4). |
| **U_disease** | entrenchment of a pathology-as-system; high = robust adversary. A model-internal index for a *type*, never a patient state. |
| **CrossWeak / sens** | `κ·(1−U_a)·sens(πB→bind_pillar(a))`; `sens` = empirically-estimated `P(host pillar deranged | disease pillar weak)`, leakage-audited, not a free knob (§5.1). |
| **ℳ, 𝒮** | Meaning `∫U dt` and Stupidity `∫(1−U)dt` for **one declared node**; `ℳ+𝒮=T`. **Never aggregated across nodes** (§4.4). |
| **organism-boundary firewall** | the type-level ban on cross-organism ℳ-aggregation / leverage-ranking — closes the O5b allocation leak (§4.4). |
| **Treatment (TSE)** | axis-typed restoration of the weakest pillar of the highest-leverage cross-node (leverage ranked within one organism), on that pillar's own axis (compensation forbidden), simulated, SSS-Guard-gated, kept only if ℳ↑ and the §5.4 keep-rule holds. |
| **LGP-12** | the 12-step control loop run over the A×B matrix. |
| **SSS-Guard** | gate on any irreversible (simulated) call: **retrodictive mode** (external metric exists) accepts iff ≥2-of-3 SSS agree AND agree with the metric; **prospective mode** (no metric) has no `pass`, only `queue_for_V3`; else `DECOMPOSE_FURTHER` (§5.3). |
| **B0–B4** | epistemic ladder (telos/VISION · proved-in-model · bridge · testable-pending = ceiling · validated = EMPTY ×2). Renamed from canon L0–L4. |
| **claim envelope / output lint** | the per-emission record and the renderer that refuses any claim exceeding its tag (full schema §9.9). |
| **O5 / O5b** | the eugenics attractor (no cross-person U) and its ecological scaling — banned at *both* the worth-label and the ℳ-allocation level (§4.4). |
| **Linnean / Wallacean shortfalls** | the named ecological data gaps (Form / Position unknown for most species) that make a literal biosphere U-scan not runnable. |
| **mapping_quality / low_score_cause / form_class** | `{exact,narrow,broad,inferred}` cross-ontology map flag; weak-zone cause tag; `LATTICE_APPROX` flag for map-defined FORM (§3.2). |

---

> **Net.** TSE proposes to make TRB a *verb*: take TRB's anatomical map (Axis A) and the SSS engine, add a clinical/pathology axis (Axis B) scored by the identical pipeline with a declared polarity flip, ground them into the A×B matrix **one-directionally (A→B)**, and run one disciplined control cycle — scan A×B → localize the highest-leverage weakest cross-node *within one organism* → restore its weakest pillar on that pillar's own axis (compensation forbidden) → simulate on the twin → pass SSS-Guard (or, for genuine novelty, *queue* it — there is no prospective `pass`) → re-score and keep only if ℳ rises and the binding constraint lifts. The objective is ℳ = ∫U dt **of a single node, never aggregated across nodes**; the safety floor is SSS-Guard and the B3 ceiling; the hard boundaries are "not a medical device," "no cross-individual or cross-species worth ranking," and "no cross-organism resource allocation." Everything testable is engineering at B3-pending, and its first job is to try to kill its own load-bearing assumptions: **prove a disease's F, P, A are separable (TSE-P0(B)), that the A×B projection beats a comorbidity-frequency baseline *and the single-axis scores* (TSE-P0(A×B), TSE-P2), and that disease entrenchment predicts real resistance (TSE-P2b) — before claiming anything about mechanism, leverage, or therapy.** "Stabilize the biosphere / heal all life" is VISION/telos that orients the sign — never a deliverable, never a ranking, and never an arbiter of which organisms are allowed to persist.

---

**Author:** Petar Nikolov (ORCID 0009-0001-8669-2276) · **Parent record:** DOI 10.17605/OSF.IO/74XGR · **Brand:** U-Score.info / U-Model.org / 911.bg
**Copyright © 2026 Petar Nikolov. All rights reserved. Content licensed under CC BY 4.0; reference code under MIT.**
**Canonical invariant:** Form ↔ Time · Position ↔ Space · Action ↔ Energy. **Project epistemic ceiling: B3-pending. Both B4 slots (clinical, ecological) empty. RUO — NOT a medical device.**
