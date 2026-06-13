# TRIADIC BIOLOGY — A Plan

> **STATUS BANNER**
> **Type:** Specification / research plan. **Not** a runtime, benchmark, dataset, or result.
> **Maturity:** B3-pending (see §9.2 epistemic ladder). No deployed engine, no replication, no validation yet. Every empirical-sounding statement below is a *proposal to be tested*, not a finding.
> **Use:** **Research use only.** **NOT a medical device**, not diagnostic software, not clinical decision support. Produces no diagnosis, prognosis, or treatment for any individual. See §9 for the binding scope/limits/ethics.
> **Honesty contract:** Where this plan inherits a contested assumption (notably the F/P/A axis-assignment of proxies, §2.6) it says so in-line and routes the question to an experiment (§8) rather than asserting it. Several deliverables are explicitly *not runnable* with this plan's own compute and are marked accordingly.

---

## 0. What changed in this revision (critique applied)

This version is a hardening pass over the prior synthesis. The most consequential corrections:

- **Membrane potential / ion gradients / ATP-maintained order moved from Position to Action** (they are energy continuously paid by the Na⁺/K⁺-ATPase). The ischemia worked example was re-derived around a *genuine* Position proxy (perfusion territory / local pO₂ / capillary distance). See §2.6, §5.4.
- **Orthogonality is now treated as an open empirical question, not an axiom.** F, P, and A in current atlases are largely three transforms of one transcriptome and are probably correlated. The orthogonality / pillar-separability ablation is promoted to **Phase 0**, *ahead of* the geometric-vs-arithmetic test. See §8.3, §8.4.
- **The geometric-beats-arithmetic test (B3) now passes only if it survives anchor perturbation**, so it measures non-compensation in biology rather than the analyst's placement of collapse points. See §8.3.
- **The aggregation contradiction is resolved**: aggregation is geometric on child **U** everywhere; "Action sums additively" is corrected to a principled **AND/OR mix** distinguishing serial dependency from parallel redundancy. See §5.2.
- **"Weakest pillar names the mechanism" is demoted** from an asserted capability to a *pre-registered, falsifiable hypothesis whose validity is conditional on the proxy-to-axis assignment*. Cancer's contradictory tri-labeling is replaced by an honest "δ-spike = decoupling; mechanism axis is TBD." See §2.5, §8.2.
- **Position `(q,c)` is split into two non-compensatory sub-components** so "right cell, wrong niche" and "wrong cell, right niche" no longer collide. Two-axis edges (SIGNALS_TO) are re-typed. See §2.6, §4.3.
- **The project epistemic ladder is renamed B0–B4** so it cannot be confused with canon's L0–L4 (which reserves L3/L4 for cosmology/physical claims). An explicit mapping to canon is given. See §9.2.
- **Regulatory and dual-use claims are reframed as intentions, not settled facts.** A fragility map is intrinsically dual-use regardless of objective deny-lists; classification is not self-determined. See §9.4, §9.5.

---

## 1. Thesis

Living systems *may* be usefully modeled, scored, and triaged on a single set of three axes — **Form** (structure/identity, whose existential price is Time), **Position** (compartment + context, price Space), and **Action** (function/energy exchange, price Energy) — using the U-Theory stability accounting `U = ∛(F·P·A)`. The proposal is: map biological entities (biomolecule → organelle → cell → tissue → organ → organism, plus pathogens and microbiome) onto this triad; score each non-compensatorily; aggregate up the containment structure; continuously scan for the **weakest pillar of the weakest node**; and rank candidate stabilizing interventions by whole-organism leverage. If this works, Triadic Biology is a **hypothesis-generation and triage engine** indexed by *cell × location × interaction* rather than by *disease × specialty*.

**The thesis is a wager, not a result.** Its load-bearing empirical preconditions — that F/P/A are *separable* in real data (§8.3), and that the proxy-to-axis assignment is *defensible* (§2.6) — are tested before anything is claimed. If they fail, the wager is reported as lost.

---

## 2. Core Idea & the F/P/A → Biology Mapping

### 2.1 The invariant triad (canonical v26)

The mapping is intended to be scale-invariant: the *meaning* of F, P, A is identical for a protein and for a whole organism; only the measurable proxies change. This invariance is the claim that *licenses* recursion and cross-scale transfer — and it is exactly what §8.3 tests rather than assumes. **The v25.2 mirror (Space↔Form / Time↔Position) is forbidden.**

| Pillar | Biological meaning | Existential price | Invariant | Canonical failure mode |
|---|---|---|---|---|
| **FORM (F)** | What the entity *is* — structure, morphology, molecular/genomic/proteomic **identity** | **Time** (decay, mutation, misfolding, turnover) | Form ↔ Time | identity/structural collapse |
| **POSITION (P)** | *Where/in-what-context* — compartment, niche, neighbourhood, signalling frame; `P = (q, c)` = coordinate **plus** operational context, kept non-compensatory internally (§2.6) | **Space-context** (mislocalization, niche loss, displacement) | Position ↔ Space | loss of context / positional collapse |
| **ACTION (A)** | What the entity *does* — function, metabolism, flux, signalling, **and the energy continuously spent to maintain order** (ion gradients, Vₘ) | **Energy** (irreversible entropy export: ATP/ROS/heat) | Action ↔ Energy | functional / energetic failure |

### 2.2 The evaluation primitives (SSS, non-compensatory throughout)

```
U  = ∛(F · P · A)                       any pillar → 0  ⇒  U → 0
δ  = (max(F,P,A) − min(F,P,A)) / (max + 0.01)
SI = U / (1 + δ)²                        imbalance-penalized stability index
```

Geometric aggregation is the architectural keystone *under test*: a single collapsed pillar zeroes the system, and `δ` penalizes imbalance. Verdict bands (domain-tunable defaults, **not** universal constants):

- **SI ≥ 0.618** → Stable. Proceed.
- **0.38 ≤ SI < 0.618** → At-risk. Rebalance the weakest pillar.
- **SI < 0.38** → Critical. Stop; fix the weakest pillar first.

High-stakes tissues raise the threshold (e.g. cardiac conduction, brainstem → θ ≥ 0.90). **All numeric thresholds and anchors are free parameters of the model, not constants of biology** (see §5.1, §8.4).

### 2.3 Recursion & the assignment rule

Every node at every depth is itself a triad (`depth d ⇒ 3^d subsystems`, never enumerated, §7). Pillars are assigned by three orthogonal questions, each at the node's own scale:

```
FORM(e)     := identity/structure of e, vs its state-conditioned class ideal   (points DOWN-IN)
POSITION(e) := placement of e inside its PARENT (L+1) + operational context     (points UP-OUT)
ACTION(e)   := e's CONTRIBUTION to the ACTION of its parent (L+1)               (points UP-FUNCTIONAL)
```

**State-conditioning (fix D3/D6).** "Class ideal" is not static. Each node carries a **state vector** `s = (cell-cycle phase, differentiation stage, circadian phase, activation state)`. Proliferation is normal Form/Action in a crypt base cell in S-phase and pathological in a differentiated cardiomyocyte; "allowed action" and "ideal Form" are evaluated *conditional on `s`*. Form-time constants (a 5-day enterocyte vs. a lifelong cardiomyocyte) are per-cell-type parameters of the Form layer, not global.

### 2.4 The optional 4th axis (NDT N=4) — flagged as INTERPRETATION pending a falsifier

Biology is the canonical substrate that arguably pays a 4th currency `X` (anti-entropy / maintenance debt) via metabolism. The default model runs **3-adic** for SSS compatibility; every record carries an optional `X` slot so aging/repair/infection questions can be lifted to tetradic without schema change:

```
U₃ = ∛(F·P·A)                       (default)
U₄ = (F·P·A·X)^(1/4)                (aging / infection / repair — research mode)
X proxies: telomere length, NAD⁺/proteostasis capacity, autophagic flux,
           DNA-repair competence, immune reserve.
```

> **Epistemic note (B0/INTERPRETATION).** The statements "metabolism pays a 4th currency" and "infection collapses U₄ *before* visible structural damage" are **interpretation, not a tested model capability.** X's proxies are themselves near-immeasurable at single-cell scale (§8.4), and "before visible damage" has no operational time threshold as written. This claim stays in INTERPRETATION until §8.2 gives it a falsifier (a pre-registered time-ordering test on a stressor time-course with measured X-proxies). It must not appear in any rendered number or verdict.

### 2.5 Disease = which pillar fails — a HYPOTHESIS, conditional on proxy-axing

The aspiration is that the triad distinguishes disease *mechanism* by *which axis* collapses. **This is the plan's central value proposition and it is currently a hypothesis, not a demonstrated property** — because "which axis" depends entirely on the (contested) proxy-to-axis assignment (§2.6). It is pre-registered as prediction P2 (§8.2) with the explicit caveat that proxy-axing is an *assumption under test*.

- **Ischemia = Position-collapse** (the cell's perfusion/O₂ *context* is destroyed though the cell hasn't moved; Action then starves). The Position proxy is perfusion territory / local pO₂ / capillary distance — **not** Vₘ (which is Action; see §2.6).
- **Aging = triadic drift** — `dδ/dt = k_entropy − k_repair·U` (rising imbalance over time).
- **Cancer = δ-spike / triadic DECOUPLING — mechanism axis TBD (honest downgrade, fix A4).** The prior plan labeled cancer "Form-escape," then elsewhere "Position-collapse" (metastasis) and "Action-pathology" (proliferation) — three contradictory axis-labels for one disease. The model does **not** cleanly localize cancer to one axis. The defensible claim is narrower: cancer presents as a **high-δ decoupling event** (Form, Position, and Action stop co-varying); *which* axis is the binding constraint is case- and stage-specific and is an output to be validated, not asserted. "Names the mechanism" is downgraded to "flags decoupling; candidate mechanism axis reported with uncertainty."
- **Dysbiosis** — see §2.6/§4.3 for the corrected treatment (the microbiome is a *node with a causal edge*, not a scalar smuggled into every host cell's pillar).

### 2.6 Where the mapping is contested — and how this plan resolves it

The critique correctly identified that several proxies were mis-axed or double-loaded. Resolutions:

- **Energy-maintained order (Vₘ, ion gradients, electrochemical potential) is ACTION, not Position (fix A1/E1).** Resting membrane potential is maintained by the Na⁺/K⁺-ATPase burning a large share of cellular ATP; it is a *continuously-paid energy* quantity. In ischemia the causal chain is `ATP↓ (Action) → pump fails → Vₘ collapses`. Vₘ therefore scores **Action**. The Position pillar for ischemia uses genuine spatial-context proxies (capillary density, perfusion territory, local pO₂).
- **Form is identity-integrity, not damage-rate (fix A2).** Damage-rate proxies (DunedinPACE, γH2AX, mutation burden) measure a *Time-derivative of Form*, not Form itself. The Form pillar is split: `f.identity` (cell-type fidelity, fold integrity, karyotype/driver-mutation status — *is this still what it is?*) and `f.damage_rate` (the aging proxies) combined **non-compensatorily**. A young cell with a single driver mutation has corrupted identity despite a clean damage-rate; a healthy old neuron has high mutation burden but intact identity. The split prevents Form from silently becoming an aging meter.
- **Position `(q,c)` is two non-compensatory sub-components (fix A5/E2).** `p.locus = q` (literal/categorical localization correctness) and `p.context = c` (niche integrity, neighbours, dependency satisfaction) combine via their own geometric (non-compensatory) sub-score `P = √(q·c)`. "Right cell in a degraded niche" and "wrong cell in a fine niche" now score differently. Justification for one pillar not two: both are *Space-context* prices and are governed together by the same intervention class (re-localize vs. restore niche), but their independence is preserved internally.
- **Signaling is re-typed to avoid a two-axis edge (fix E2).** The prior `SIGNALS_TO : Position+Action` violated one-property-one-axis (K2). It is split into `SIGNALS_TO` (a Position edge: a context/dependency relation in the niche) and `INDUCES_ACTION` (an Action edge: the downstream functional effect). No single edge loads two axes.
- **Microbiome / immune system: node, not scalar-in-a-pillar (fix A6/E3).** The microbiome and immune system are **scored nodes** that influence host cells **through explicit causal edges** (`SUPPLIES`, `SIGNALS_TO`, `DISRUPTS`), and that edge-borne influence enters the roll-up via edge-weighted aggregation (§5.2, fix D2). They are **never** also copied as a scalar into a host cell's `p.context`, which would double-count their instability and break "mechanism falls out of the ontology." Because immunity is mobile, global, and lattice-structured (not a clean PART_OF tree), see §7's explicit tree-vs-lattice limitation — the geometric roll-up assumes a tree, and immunity is modeled as a *cross-cutting overlay with explicit edges*, with the consequence stated, not hidden.
- **Action is not a function of Action-data alone — acknowledged (E4).** Flux *feasibility* depends on substrate (Position) and enzyme presence (Form). The Action-Agent's "sees `h_a` only" (§6.1) is therefore an **architectural idealization, not a biological fact**; the agents are *informationally* siloed by construction, but the underlying biology is coupled, which is precisely why the orthogonality ablation (§8.3) is run first.

---

## 3. System Architecture

Triadic Biology implements the GSI-RTD `TriadicDomain` interface for `biology.organism`, so the canonical runtime (search → scheduler → agents → cycle → score → learn) operates on it with no bespoke orchestration.

```
                          TRIADIC BIOLOGY — SYSTEM ARCHITECTURE
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │                          A. DATA & KNOWLEDGE-GRAPH LAYER                            │
 │  Public ontologies/atlases → axis-typed ETL (one dataset → ONE axis)               │
 │  ┌── FORM sources ──┐   ┌── POSITION sources ──┐   ┌── ACTION sources ──┐          │
 │  │ CL, Tabula Sapiens│   │ UBERON, GO-CC, HPA   │   │ Reactome, KEGG,    │          │
 │  │ HCA, UniProt,     │   │ STRING/IntAct,       │   │ Recon3D (FBA*),    │          │
 │  │ AlphaFold, PDB    │   │ CellPhoneDB*, Visium │   │ BRENDA, GO-BP/MF   │          │
 │  └───────────────────┘   └──────────────────────┘   └────────────────────┘          │
 │   * FBA = MODEL OUTPUT not measurement;  CellPhoneDB = INFERRED from co-expression  │
 │     ⇒ F,P,A are largely 3 transforms of ONE transcriptome → ORTHOGONALITY UNTESTED  │
 │        ▼ TPL-guarded records  G{src;conf;level;mode}  (provenance on every fact)    │
 │   ┌──────────────────────── TB-KG (typed property graph) ────────────────────────┐ │
 │   │  node = BioSystem(F{} P{} A{} G{}, scale, state s)   recursive, self-similar  │ │
 │   │  edges: IS_A, PART_OF, LOCATED_IN, ADJACENT_TO, INTERACTS_WITH, SIGNALS_TO,   │ │
 │   │         INDUCES_ACTION, PERFORMS/ENABLES, CATALYZES, SUPPLIES/CONSUMES,       │ │
 │   │         REGULATES, DISRUPTS/HIJACKS   (each edge loads EXACTLY one axis)       │ │
 │   └──────────────────────────────────────────────────────────────────────────────┘ │
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │                       B. DYNAMIC U-SCORE ENGINE (the numeric core)                  │
 │  per node:  F,P,A ∈[0,1] (quantitative proxies, IQR-filtered; SSS jury ON A SUBSET) │
 │             U=∛(FPA)   δ=(max−min)/(max+.01)   SI=U/(1+δ)²   weak_pillar=argmin     │
 │  roll-up:   GEOMETRIC on child U everywhere + AND/OR mix (serial vs redundant)      │
 │             + edge-weighted context terms (SIGNALS_TO/SUPPLIES/DISRUPTS enter math) │
 │  dynamics:  U_org(t),  SI-dot (EWMA),  V_δ (CUSUM),  ℳ = ∫ U_org dt                 │
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │                  C. WEAK-ZONE SCAN  (localize → rank by leverage)                   │
 │  Stage 1  min-pillar targeting: hard gates G1–G4 (G4 = pillar collapse → reject)   │
 │           open-world guard: "absent in atlas" → UNKNOWN, never "forbidden"          │
 │  Stage 2  leverage: ∂U_org/∂U_n  &  counterfactual ΔMeaning ;                       │
 │           Priority = ΔMeaning / ∛(C_t·C_s·C_e)   (ties → cheapest)                  │
 │  trajectory tools: TAD (axis starvation) · DPA-SI (recovery ratio ρ) · activity|Δ| │
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │             D. AI / DIGITAL-TWIN CONTROL LOOP  (LGP-1…12, TAA agents)               │
 │   ┌─ Form-Agent ─┐ ┌─ Position-Agent ─┐ ┌─ Action-Agent ─┐ ┌─ Generalizer Σ ─┐     │
 │   │ h_f only     │ │ h_p only (graph) │ │ h_a only       │ │ fuse → g(f,p,a); │     │
 │   └──────────────┘ └──────────────────┘ └────────────────┘ │ name weakest +   │     │
 │   (informational siloing is an idealization; biology is coupled — see §2.6/E4) │   │
 │   twin layers: Action(FBA/ODE) · Position(reaction-diffusion) · Form(damage)  ┘     │
 │   loop: scan → detect → decompose → rank → leverage → propose → SSS-Guard → act     │
 │         → re-aggregate → learn (impact/weights, ε→UCB1→Thompson, transfer β)        │
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │            RH. RECURSIVE-HARDENING GOVERNANCE  (wraps every output)                 │
 │  claim envelope {register, epistemic_level B0–B4, provenance, external_truth}       │
 │  output lint: ban "health/diagnose/treat…" ≤B3 · no cross-person U · deny-list      │
 │  SSS-Guard: irreversible call ⇒ ≥2-of-3 SSS agree + external outcome metric         │
 └────────────────────────────────────────────────────────────────────────────────────┘

      Canonical chain:  U-Theory → GSI-RTD(search) → TS(scheduler) → TAA(agents)
                        → LGP-12(cycle) → Twin(environment) → SSS(score) → Learning → Gates
```

---

## 4. The Data Layer & Knowledge Graph

### 4.1 Design constraints inherited from canon

| # | Constraint | Consequence for the schema |
|---|---|---|
| K1 | F↔Time, P↔Space, A↔Energy mandatory | each node carries exactly one F-, one P-, one A-bundle; energy-maintained order (Vₘ) lives in A (§2.6) |
| K2 | Orthogonality / no cross-talk | three disjoint namespaces `f.* / p.* / a.*`; **no edge loads two axes** (SIGNALS_TO split, §2.6). *Whether the data honor this is an open question — §8.3.* |
| K3 | Non-compensatory | geometric aggregation everywhere; a zero pillar is representable and load-bearing |
| K4 | Position = `(q, c)`, non-compensatory inside | `p.locus = q` **and** `p.context = c`, combined `P=√(q·c)` (§2.6) |
| K5 | Recursion (3^d), tree-structured | one universal node type, self-similar — **with a stated lattice exception for immune/microbiome (§7)** |
| K6 | Group identical Forms; maximize Coverage/Cost not \|S\| | store **FormTypes** + `abundance`; near-identical subclones split at a defined threshold (§4.4, fix D1) |
| K7 | AD-RTD: `A → F\|A → P\|F,A` | "allowed action" = candidate `ENABLES` edge **gated by SI**, with an **open-world guard** (absence ≠ prohibition, §4.3) |
| K8 | TPL guardrails | every fact/score carries `G{src;conf;level;mode}` → confidence travels with data |

### 4.2 Real data sources (one dataset → one axis) — with independence caveats

- **Form (structure/identity):** Cell Ontology (CL), Tabula Sapiens / HCA (cell-type identity, K6 grouping), UniProt / Ensembl / RefSeq, PDB / AlphaFold DB (fold integrity), Reactome (complex composition).
- **Position (locus + context):** UBERON (anatomy), GO-CC (compartment), Human Protein Atlas (validated localization), STRING / IntAct / BioGRID (relational neighbourhood), CellPhoneDB / CellChat / NicheNet (cell–cell niche edges — **inferred from co-expression, not measured**), 10x Visium / Xenium / MERFISH (literal spatial coordinates `q`).
- **Action (function/energy):** Reactome / KEGG (reaction primitives), Recon3D / Human-GEM (genome-scale stoichiometry → **FBA flux is a model *prediction*, not a measurement** — see §8.4/B1), GO-BP/MF (functional labels), BRENDA / SABIO-RK (kinetics), and where available single-cell respirometry/metabolomics (sparse).
- **External ground truth (kept independent of scoring inputs):** DepMap/Achilles essentiality, gnomAD pLI/LOEUF, COSMIC/Open Targets, clinical/registry outcomes. **Independence is not assumed — it is audited.** Essentiality and constraint correlate with broad/high expression, which also feeds the Form pillar; §8 includes a mandatory **feature-leakage audit** before any of these is used as truth (fix B6).

> **Data-independence warning (load-bearing).** F (identity), P (niche, via CellPhoneDB), and A (function labels) are, in current atlases, three transforms of **one** scRNA matrix. The architecture's non-compensation only *means* something if the three inputs carry independent information. Establishing or refuting that independence is **Phase 0**, §8.3.

### 4.3 The node & edge model

Every node is one **`BioSystem`** at some scale ∈ {molecule, complex, organelle, cell, tissue, organ, system, organism}, plus non-host classes {virus, bacterium, microbiome, immune-overlay}, carrying a state vector `s` (§2.3). Surface form (TPL):

```tpl
F{cell:cardiomyocyte; state:differentiated; identity:cardiac-TF-program-intact;
  damage_rate:low; genome:diploid-no-driver}
P{locus:LV-myocardium; context:vascularized+normoxic+syncytium-coupled}   ; P = √(locus·context)
A{function:contraction; metab:fatty-acid-oxidation; Vm:-85mV; output:force; flux:Ca-cycling}
G{src:GTEx+echo; conf:0.82; scope:specific; level:B1; mode:assert}
```

Edges are typed; **each loads exactly one axis** (fix E2):

| Edge | Meaning | Axis loaded | Source |
|---|---|---|---|
| `IS_A`, `PART_OF`/`COMPOSES` | type subsumption, containment (recursion backbone) | Form | CL, UBERON, Reactome |
| `LOCATED_IN`, `ADJACENT_TO`/`IN_NICHE`, `INTERACTS_WITH`, `SIGNALS_TO` | placement, neighbourhood, PPI, ligand→receptor *context* | Position | HPA, Visium, STRING, CellChat |
| `INDUCES_ACTION` | the downstream *functional effect* of a signal | Action | NicheNet, Reactome |
| `PERFORMS`/`ENABLES`, `CATALYZES`/`TRANSPORTS`, `SUPPLIES`/`CONSUMES`, `REGULATES` | function & energy exchange | Action | GO-MF, Reactome, Recon3D |
| `DISRUPTS`/`HIJACKS` | pathogen entropy-export (decomposed into its F/P/A targets, not "all three at once") | per-target | VirHostNet, CARD |

**Allowed-action inference (K7) with an open-world guard (fix B3).** The graph never asserts "Form X may do Action Y" as a free fact. It proposes a candidate via `ENABLES`, then computes admissibility: `A_i` is admissible for `F_j` in `P_k` iff `SI(F_j,P_k,A_i) > θ` with a hard veto on any zero pillar (AD-RTD `A → F|A → P|F,A → evaluate → triage`). **Crucially, atlases are positive-only: "not observed" ≠ "forbidden."** An action absent from the healthy atlas defaults to `UNKNOWN` (flag `OPEN_WORLD`), **not** `FORBIDDEN`. Only an action that is *positively contradicted* (e.g. substrate provably absent in that compartment, `p.context → 0`) is vetoed. This mirrors the §9.3-O2 sparsity guard onto the K7 gate, so rare-but-normal states are not mass-flagged as pathology.

### 4.4 Identity resolution / entity merge (fix D1)

K6 grouping ("2×10⁹ identical cardiomyocytes = 1 node") requires a defined merge rule: Forms are clustered by an identity-feature distance with a tunable threshold `τ_merge`; a **near-identical variant** (e.g. a subclone carrying one driver mutation) whose `f.identity` distance exceeds `τ_merge` is **split into its own node** with its own `abundance`, even if morphologically similar — so emerging subclones are visible rather than averaged away. `τ_merge` is a calibrated parameter, reported, not magic.

---

## 5. The Dynamic U-Score Engine & Weak-Zone Scan

### 5.1 Per-node scoring

Each raw measurement is normalized to `[0,1]` against physiological reference anchors (`ref_lo` = collapse, `ref_hi` = ideal) with a clamped, monotone, saturating curve. When a pillar has several observables, the pillar score is itself a non-compensatory (weighted-geometric) combine. Instrumentation (corrected axing per §2.6):

| Pillar | Quantitative proxy | Example anchor (per cell type) |
|---|---|---|
| **Form / identity** | cell-type-program fidelity, fold integrity (pLDDT), karyotype, driver-mutation status | identity-match 1.0 → 1.0; lineage-confused → 0.0 |
| **Form / damage-rate** | epigenetic-clock acceleration, γH2AX, mutation burden, proteostasis | DunedinPACE 0.8 → 1.0; 1.5 → 0.0 |
| **Position / locus (q)** | localization correctness, compartment match | correct → 1.0; ectopic → 0.0 |
| **Position / context (c)** | niche-edge integrity, perfusion/pO₂, contact inhibition, dependency satisfaction | normoxic+coupled → 1.0; ischemic territory → 0.0 |
| **Action** | ATP production, OCR/ECAR, **Vₘ / ion-gradient maintenance**, FBA flux feasibility, functional output | Vₘ −85 mV → 1.0, −20 mV → 0.0; ATP 1.0× → 1.0, 0.3× → 0.0 |

> **Anchors are the most consequential free parameters in the model (fix B4/B4-derivation).** `ref_lo`/`ref_hi` *are* where the geometric zero bites, and they are **cell-type-specific** ("0.3× ATP" is lethal for a cardiomyocyte, normal for a quiescent lymphocyte; resting Vₘ differs by cell type). They are **not constants.** Derivation procedure: each anchor is fitted per cell type from the physiological range in reference data (e.g. the 1st/99th percentile of healthy distributions, or a literature-curated lethal threshold), recorded with provenance in `G{}`, and **subjected to the anchor-robustness ablation in §8.3** — any headline result that does not survive anchor perturbation is not reported as a finding.

**SSS jury — reserved for a subset, not every node (fix B5).** The SSS two-stage pipeline (Constructor emits up to N=12 falsifiable principles/pillar; AI jury of up to 50 models scores 0–100, IQR-filtered) is **compute-infeasible at every node × timestep** (10³–10⁴ nodes × longitudinal steps × 3 pillars × ~12 principles × up to 50 models = millions–billions of LLM calls). It is therefore applied **only** to (a) the top-K leverage nodes surfaced by the weak-zone scan, and (b) nodes flagged AT_RISK/CRITICAL. The vast majority of nodes carry **bare quantitative-proxy scores**; "SSS refines priors" is true only where the jury runs, and the plan says so rather than implying universal jury coverage.

**Missing-data discipline (SSS-L4 / Mode-B):** an unmeasured observable → neutral **50**, never dropped, never assumed healthy. Sparse nodes compress toward U≈0.50; `evidence_coverage` and `conf` travel with the value; coverage < 0.3 → flagged `LOW_EVIDENCE`, excluded from irreversible decisions.

### 5.2 Recursive aggregation — geometric throughout, with AND/OR redundancy (fix A3/A7/E5/D2)

The prior plan claimed "Action rolls up additively" while the code did only a geometric mean of child U — a self-contradiction, and biologically false (cardiac output is *not* the sum of cardiomyocyte forces; it depends on synchronization — a Position property — and total flux is bounded by shared substrate). **Resolution: aggregation is geometric on child U everywhere; "additive Action" is deleted.** What it was reaching for (redundancy) is captured properly by an **AND/OR-aware operator** that distinguishes serial dependency from parallel redundancy:

```python
def aggregate(n):
    for c in n.children: aggregate(c)            # post-order
    if n.redundancy == "serial":                 # AND: weakest-link (brainstem, conduction)
        n.U = wgeomean([c.U for c in n.children], [c.weight for c in n.children])
    elif n.redundancy == "parallel":             # OR: graceful degradation (nephrons, lobules, bilateral)
        # functional reserve: parent survives loss of some children;
        # U falls only as surviving capacity drops below demand
        n.U = reserve_aware_OR([c.U for c in n.children], [c.capacity for c in n.children], n.demand)
    else:                                         # mixed: serial backbone over parallel pools
        n.U = mixed_AND_OR(n.children)
    # context terms: edge-weighted influence of NON-child neighbours enters here (fix D2)
    n.U *= context_factor(n, edges=[SIGNALS_TO, SUPPLIES, DISRUPTS])
    childU = [c.U for c in n.children]
    n.delta = (max(childU)-min(childU))/(max(childU)+0.01)
    n.SI = n.U/(1+n.delta)**2
    if any(c.U < 0.38 for c in n.children) and n.redundancy == "serial":
        n.flag = "weakest-link block: fix critical serial child first"
```

- **Serial (AND):** one survival-critical, irreplaceable component at U≈0 zeroes the parent (cardiac arrest = one system → 0 → organism → 0). Correct for brainstem, conduction system, single points of failure.
- **Parallel (OR) / functional reserve (fix A7):** redundant pools (a million nephrons, liver lobules, bilateral organs) degrade *gracefully* — losing one of a million nephrons does **not** crush kidney U. The geometric-everywhere assumption (pure serial AND) is biologically wrong here, so it is **not** used; reserve-aware OR is.
- **Edge-weighted context (fix D2):** the Position-context that the *thesis* depends on (ischemia, dysbiosis) now actually enters the math via `INTERACTS_WITH / SIGNALS_TO / SUPPLIES / DISRUPTS` edges, not just `PART_OF`. The previous version's roll-up ignored exactly the edges that carry the mechanism.

`weight` and `redundancy` and `capacity/demand` are per-node functional parameters (e.g. brainstem serial weight ≈ 1.0; a single nephron parallel weight ≈ tiny), reported and calibrated, not magic.

### 5.3 Temporal dynamics & Meaning

The tree is re-scored each timestep `t` (longitudinal cohort cadence or simulated trajectory). Note: re-scoring the *whole* tree each step is itself the §5.1/B5 cost driver — so re-scoring is **budgeted** to changed/at-risk subtrees, not literally the whole forest each step.

- **SI-velocity** (EWMA) — declining SI flags a weak zone before threshold crossing.
- **δ-volatility** (CUSUM) — rising imbalance = early decompensation signal.
- **DPA-SI recovery ratio** `ρ = (peak_next − dip)/dip_depth`; `ρ < 0.618` ⇒ structural decline → flag for redesign.

Organism **Meaning** = time-integral of stability (dual of the Stupidity integral `∫(1−U)dt`):

```
ℳ_org = ∫ U_org(t) dt  ≈  Σ ½(U(tᵢ)+U(tᵢ₊₁))(tᵢ₊₁−tᵢ)      (trapezoidal)
```

`ℳ_org` is the headline *model-internal* objective an intervention maximizes; the optimization target is `∂ℳ/∂(intervention)` over the horizon. **ℳ_org is a model coverage/stability indicator, never an organism worth metric (§9.3-O5).**

### 5.4 The weak-zone scan (the payload) — re-derived ischemia example

**Stage 1 — localization.** Scan every node; flag canonical-gate trips:

```python
for n in all_nodes:
    n.weak_pillar = argmin(n.F, n.P, n.A)
    if min(n.F,n.P,n.A) ≈ 0 or n.SI < 0.38:  flag CRITICAL   # G4 pillar-collapse / stop-fix
    elif n.SI < 0.618:                        flag AT_RISK    # rebalance weakest pillar
    # weak_pillar is a HYPOTHESIS about mechanism, valid only if §8.3 proxy-axing holds
```

**Stage 2 — leverage ranking.** Because aggregation is weighted-geometric (on serial subtrees), organism U is most sensitive where a factor is smallest:

```
∂U_org/∂U_n = (U_org / U_n) · Π_{k∈path(n→root)} (weight_k / W_parent(k))      (serial paths)
```

Use the exact counterfactual: raise the weakest pillar to a feasible target, re-aggregate, measure `ΔU_org` and `ΔMeaning`, rank by

```
Priority = ΔMeaning / ∛(C_time · C_space · C_energy)            (ties → cheapest)
```

Output = an ordered intervention queue. A CRITICAL *serial* survival-critical node is forced to the top regardless of cost.

**Worked example (cardiomyocyte, ischemia) — corrected (fix A1).** Healthy: F=0.92, P=0.90, A=0.88 → U=0.900, SI=0.828 (STABLE). Acute capillary occlusion: the binding deficit is the cell's **perfusion/O₂ context** — a genuine *Position-context* proxy (capillary distance ↑, local pO₂ ↓). Vₘ collapse and ATP drop are **Action** symptoms downstream of that context loss, *not* the Position proxy. Scored: `P.context → 0.18` (perfusion territory destroyed though the cell hasn't moved) drives `P=√(locus·context)` down; Action then starves (`A → 0.40`, Vₘ depolarizing). U=0.41, δ high, SI critical. The scan localizes the **binding constraint to Position-context**; the canonically-correct first move is **reperfusion** (restore the spatial/context price), not an inotrope (Action) or gene therapy (Form). The mechanism label is a *hypothesis from the ontology* — and it is honest precisely because the Position proxy is no longer Vₘ (which would have made it circular). This example is now non-circular *by construction*, and its correctness is exactly what prediction P2 (§8.2) tests.

---

## 6. The AI / Digital-Twin Control Loop

### 6.1 The four agents (TAA)

- **Form-Agent** → encodes `h_f` from genome/epigenome/proteome.
- **Position-Agent** → encodes `h_p` from compartment/niche/context (owns relation-graph reasoning).
- **Action-Agent** → encodes `h_a` from flux/function/energy.
- **Generalizer Σ** → fuses the three, computes the admissibility gate `g(f,p,a)`, names the weakest pillar, and recommends intervention.

> **Honest idealization.** "Each agent sees only its axis" is an *informational* design choice, not a claim that the underlying biology is separable. Action feasibility genuinely depends on substrate (Position) and enzyme (Form) (§2.6/E4). The siloing is what makes the orthogonality ablation (§8.3) *meaningful* — if the agents can't reach atlas-level performance while siloed, that is itself evidence the axes aren't separable in the data.

### 6.2 The digital twin

The twin holds the entity forest plus per-entity continuous state in three coupled layers: **Action layer** (FBA on Recon3D + ODE kinetics), **Position layer** (reaction-diffusion / agent-based niche field of O₂, morphogens, ECM), **Form layer** (slow damage accumulation, repair, epigenetic drift, with per-cell-type Form-time constants per §2.3). It reproduces aging (rising δ) and cancer (δ-spike with F–P–A decoupling) via `dδ/dt = k_entropy − k_repair·U`. `execute_action(a, state)` advances the layers; the twin **is** a concrete `TriadicDomain`. **The twin is a simulation, not a person; nothing in it is live physiology (§9.3-O7).**

### 6.3 The LGP-12 loop

```
LGP-1  SCAN       twin emits (F,P,A)_e per entity; U₀,δ₀,SI₀ per node and organism
LGP-2  DETECT     Problem set 𝒫 = {e : SI_e < θ_tissue}; instability weight w_e   ← WEAK-ZONE SCAN
LGP-3  DECOMPOSE  per zone: deficits d_F,d_P,d_A; DominantAxis = argmax (HYPOTHESIS, §2.5); flag entangled
LGP-4  RANK       Impact(e) via geometric-mean leverage → Pareto-80 set
LGP-5  LEVERAGE   L_e = ΔU_org / Cost(e); weakest-pillar zones get the ∂U/∂U_weakest multiplier
LGP-6  SYNTHESIS  Σ + pillar agents propose axis-typed interventions, each costed (C_T,C_S,C_E)
LGP-7  SELECT     η = Benefit/Cost; pick max-η feasible under (T,S,E) budget
LGP-8  PLAN       topological order; planned U-trajectory
LGP-9  ALLOCATE   resource gaps across the three prices
LGP-10 PULSE      re-run twin; ε=U_planned−U_actual; ε≥0.10 → re-enter LGP-5; U↓ → EMERGENCY revert
LGP-11 REPORT     milestone card per intervention (all in TESTABLE register, §9.1)
LGP-12 AUDIT      ΔU_total, ΔSI, δ₀→δ_final (must fall), PEC = ΔU/Cost; then LEARN
```

### 6.4 Axis-typed interventions (compensation forbidden)

An intervention must act on the weakest pillar's own axis:

| Weakest pillar | Intervention class | Examples |
|---|---|---|
| **Form (identity/damage)** | repair / identity-restoration | gene editing, partial epigenetic reprogramming, chaperone therapy, senolytics |
| **Position (locus/context)** | context / niche-restoration | reperfusion, differentiation therapy, ECM normalization, re-vascularization, FMT |
| **Action (function/energy)** | function / energy-reset | metabolic reprogramming, mTOR modulation, anti-inflammatory `A_loss` reduction, ion-pump support |
| **Coupling (δ high)** | re-coupling / combination | combination triad therapy (predicted superadditive — a HYPOTHESIS); twin tests a 2×2×2 factorial in-silico first |

**Anomaly = disallowed action / wrong position = pathology — with the open-world guard (§4.3).** A Form executing an action the healthy atlas *positively contradicts* (substrate-impossible) is an Action-pillar pathology; a Form in a *positively implausible* `LOCATED_IN` is a Position-collapse (metastasis = right Form, illicit Position). But an action merely *absent* from the atlas is `UNKNOWN`, not pathology — rare-but-normal states are protected. Pathology is "an edge the atlas *forbids*," never "an edge the atlas *didn't happen to sample*."

### 6.5 Learning across cycles (GSI-RTD §26)

- **Impact (empirical Bayes):** `impact^(g+1) = (1−λ)·impact^(g) + λ·observed_ΔSI`, λ=0.3.
- **Weights (gradient-free):** `w_j^(g+1) = w_j^(g) + α·corr(contribution, ΔSI)`.
- **Exploration:** ε-greedy (cycles 1–5) → UCB1 (6–20) → Thompson (20+); plus AD-RTD anti-bias ε≈10% random Form/Position variants.
- **Cross-domain transfer (Prop 26.1):** `impact_new = β·impact_source + (1−β)·prior`, `β = (cosine-F + subgraph-iso-P + jaccard-A)/3` — structural isomorphism, **not** assumed biological analogy. Transfer must beat cold-start to be kept (§7, P2 gate).

### 6.6 Safety gate

Any irreversible call (gene edit, ablation) must pass **SSS-Guard**: 3 independent SSS instances; accept only if ≥2 agree within tolerance **and** the verdict agrees with an **external** biological/clinical outcome metric. Never act on a single SSS verdict (SSS is the single point of architectural failure). If no feasible queue raises organism U above threshold within budget, the engine returns `DECOMPOSE_FURTHER` rather than emit a false plan. **In this plan there is no autonomous biological action of any kind (§9.6-6); SSS-Guard governs *simulated/recommended* actions only.**

---

## 7. Phased Roadmap (Pilot → Whole Organism)

Each stage is gated by the *prior* stage passing its falsifiers. **Phase 0 is new and mandatory** — the two experiments that must run *first* (critique P0).

| Phase | Scope | Systems | Key deliverables | Gate to advance | Status |
|---|---|---|---|---|---|
| **P0 — Foundations & go/no-go** | one tissue slice; no scaling | n/a | **(a) Orthogonality / pillar-separability ablation** (§8.3) — are F,P,A empirically separable in real atlas data? **(b) Anchor-robust geometric-vs-arithmetic test (B3)** — does geometric U beat the arithmetic mean *and survive anchor perturbation*? **(c) feature-leakage audit** of DepMap/gnomAD truth | **If F/P/A are collinear (likely) OR B3 fails under anchor perturbation → STOP and report the negative result.** Otherwise proceed | **runnable now** |
| **P1 — Cardiac LV pilot** | LV, ~11 cell lineages, depth-2 | ~11–30 | TB-KG slice (HCA/CL/UBERON/Reactome/CellPhoneDB); per-node U/δ/SI; ranked weak-zone list; corrected ischemia example | P2(mech) pre-registration met **and** retrodiction V1 passes | runnable now |
| **P2 — Whole heart** | 4 chambers + conduction + vessels | ~50 | recursive `U_org` roll-up (serial/parallel-aware §5.2); organ-outcome classifier | organ AUC ≥ 0.70 vs HFrEF (P4 below) | runnable now |
| **P3 — Multi-organ** | + lung (HLCA) + kidney (KPMP) | ~150 | cross-organ transfer (β=structural-similarity); transfer must beat cold-start | transfer beats cold-start | runnable now |
| **P4 — Inter-organ coupling** | heart–kidney axis; immune system as cross-cutting Position **overlay** (lattice, not tree — §below) | ~500 | inter-organ weak zones (cardiorenal) *emerge* from aggregation | emergent coupling reproduced | partial data |
| **P5 — Whole-organism dynamic** | HCA-v2 abstracted to 10³–10⁴ system nodes | 10³–10⁴ | navigable weak-zone map; `U_org(t)`, `ℳ_org`; budgeted scheduler | **requires prospective causal evidence (V3) on ≥1 prior stage** + SSS-Guard ensemble + a *falsifiable* sufficiency criterion (below) | **not runnable; research-grade** |

**Tree-vs-lattice limitation (fix E3), stated not hidden.** The recursion (`3^d`) and the geometric roll-up assume `PART_OF` is a **tree**. The immune system and microbiome are **mobile, global, lattice-structured** — they are *part of* many tissues at once. They are therefore modeled as a **cross-cutting overlay** connected by explicit edges (§4.3), and their influence enters via edge-weighted context (§5.2), **not** by pretending they sit in one place in the tree. Consequence: organism-level roll-up over the immune overlay is approximate, and any weak-zone claim that depends on it is tagged `LATTICE_APPROX` and held to a higher evidence bar.

**Combinatorial & sufficiency honesty.** Depth-3 is `3³ = 27` per node and explodes multiplicatively; it is never enumerated. Scale-up uses *budgeted* selection (compute spent on high-`|Δ|` regions) and **decomposes-further-rather-than-runs** when no queue meets coverage ∧ budget ∧ stability. The **Scheduler-Sufficiency Conjecture** (no proof a chosen subset is "sufficient") is open — and its honest consequence is stated: **P5 risks being unfalsifiable, because a missed weak zone can always be blamed on an omitted node.** Mitigation: a pre-committed saturation criterion `n*` where `∂Coverage/∂n < ε` on held-out perturbations, declared *before* scaling; if coverage never saturates, P5 is reported as not-yet-validatable rather than dressed as complete.

---

## 8. Validation & Falsifiable Predictions

Validation binds model outputs to an **independent** ground-truth modality. The central trap is **circularity** — never validate against a label derived from the same data that produced the score, and never trust an axis whose proxy is downstream of another axis (the Vₘ error, now fixed).

### 8.1 Evidence bars

- **V1 — Retrodiction:** low-U cells coincide with known disease-vulnerable ones. Runnable now.
- **V2 — Blind prediction:** U on *healthy baseline* predicts which cells degrade under a *held-out* stressor. Runnable now (ischemia time-courses, Sci-Plex, doxorubicin atlases).
- **V3 — Prospective causal:** stabilizing the model-prescribed weakest pillar raises real resilience. **Not runnable by this plan's compute** — needs a wet-lab collaborator or an in-silico causal-surrogate model; designable and pre-registerable, **not executable here.**

### 8.2 The falsifiable predictions

| # | Claim | Falsifier | Pre-registered success |
|---|---|---|---|
| **P0** | F, P, A carry **independent** information on real atlas data | pairwise pillar correlation \|r\| > 0.8 (collinear) ⇒ non-compensation has no independent inputs | mean pairwise \|r\| < 0.6 on held-out tissues |
| **P0b** | Geometric U beats arithmetic mean **robustly** | B3 win disappears when `ref_lo` perturbed ±20% | geometric beats arithmetic across the anchor-perturbation envelope |
| **P1** | Lowest baseline `SI` cell type = cell lost earliest in ischemia (vCM) | baseline SI ranks vCM in the *most-stable* tertile | Spearman ρ ≥ 0.5, p < 0.05 |
| **P2 (mech)** | The weakest *pillar* names the *mechanism* — **conditional on proxy-axing being correct (§2.6)** | vCM's lowest pillar is Form while OXPHOS Action scores high; or the axis-label flips when a proxy is re-axed | mechanism map matches expert pre-registration, **and is stable under documented proxy reassignment** |
| **P3** | Low baseline-SI leaves degrade most under a **held-out** stressor (blind, OOD) | no monotone SI→damage relationship | negative slope, R² ≥ 0.3 beyond a marker-count null |
| **P4** | Recursive `U_LV` tracks organ-level clinical class (HFrEF vs healthy) | failing hearts score ≥ healthy | classifier AUC ≥ 0.70 |
| **P5** | Prescribed weakest-pillar intervention raises resilience > control | *(V3 — deferred; designed, not run)* | pre-registered, requires collaborator |
| **P6 (X)** | Under infection, U₄ (with measured X-proxies) declines *before* structural Form damage | no consistent time-ordering of X-decline vs Form-decline | pre-registered time-ordering test on a stressor time-course; **until run, the U₄ claim stays in INTERPRETATION (§2.4)** |

### 8.3 Baselines & the two decisive tests (re-ordered)

The triad must beat non-trivial baselines: **B0** random, **B1** marker-count/library-size, **B2** single-pillar (Action-only), **B3** arithmetic mean `(F+P+A)/3`, **B4** generic anomaly score.

**The two most important experiments run FIRST, in Phase 0 (critique P0):**

1. **Orthogonality / separability ablation (P0).** Measure empirical correlation of F, P, A on real atlas data and test whether the three pillar-agents, siloed, carry independent signal. *If F/P/A are collinear — likely, since all derive from one transcriptome — the non-compensatory architecture has no independent inputs to be non-compensatory over.* That is the **most valuable possible negative result** and it is sought *ahead of* B3.
2. **Anchor-robust geometric-vs-arithmetic (P0b → B3).** Geometric and arithmetic means diverge *only* when a pillar is near its collapse anchor. Because anchors are hand-fit (§5.1/B4), a naive "geometric beats arithmetic" win could merely reflect anchor placement. **B3 counts only if it survives perturbation of `ref_lo`/`ref_hi`** (±20% envelope). Without anchor-robustness, a B3 win is not evidence for non-compensation in biology.

Only if P0 and P0b pass does "geometric U beats arithmetic" become a meaningful claim. Ablations additionally drop each pillar, vary N, and swap SI↔U / geometric↔arithmetic.

### 8.4 Honest data gaps

1. No cell-type-resolved gold-standard "fragility" label exists; truth is assembled, ordinal, noisy → caps achievable ρ (hence the modest ≥0.5 thresholds).
2. **The Action↔Energy axis — declared the most important pillar — has essentially no per-cell training data.** Single-cell respirometry does not exist at atlas scale; **FBA flux is a *model output* (a prediction from stoichiometry + an assumed objective), not a measurement.** So the most-weighted pillar will in practice be filled by transcriptomic proxies the plan itself calls "poor," or by FBA. **Consequence priced honestly:** the B3 test partly compares an FBA-derived (predicted) Action multiplied against measured F and P — Action is a *different kind of quantity* than F and P, which is a confound the §8.3 design must control for (e.g. by also running B3 with a measured-only Action subset where respirometry exists).
3. The Position graph (CellPhoneDB) is *inferred* from co-expression, not a measured physical relation — feeding directly into the §8.3 separability concern.
4. Atlases are snapshots, not trajectories (SSS-L3); the dynamic model needs scarce longitudinal data.
5. **External "truth" may leak into Form (fix B6):** DepMap essentiality and gnomAD constraint correlate with broad/high expression, which feeds Form. A **feature-leakage audit is mandatory (P0c)** before either is used as ground truth, or "SI predicts fragility" risks restating "highly-expressed genes are highly expressed."

---

## 9. RH Discipline — Scope, Limits, Ethics, Non-Goals

### 9.1 The central cut: Testable vs Interpretation

The triad is an **accounting frame and decision-support search heuristic**, not an ontology of life and not a health meter. Two strictly separated registers, enforced in code:

- **TESTABLE** — statements about what *our model does* over biological data, admitted only with an operational procedure, a falsifiable prediction, and an external ground-truth metric.
- **INTERPRETATION** — framing/metaphor (e.g. "Form↔Time is the deep structure of life," "metabolism pays a 4th currency"). May generate hypotheses and label axes; **no number, verdict, or colour rendered to a user may be in INTERPRETATION language.** The UI prints "model fragility index for entity-type X, model-internal, not a clinical measurement," never "X's stability is 0.41."

### 9.2 Epistemic ladder — RENAMED B0–B4 to avoid colliding with canon (fix C1)

Canon RH fixes L0–L4 with L2 = cross-domain analogy, **L3 = cosmological extension, L4 = literal physical claim**. Re-using L0–L4 with biology-specific meanings would be exactly the level-inflation RH exists to prevent. **This project therefore uses its own ladder B0–B4** and states the mapping to canon explicitly:

| Project level | Meaning | Maps to canon |
|---|---|---|
| **B0** | metaphor / framing | canon L0 (metaphor) |
| **B1** | proved-within-the-model's-axioms (true of the *model*, not biology) | canon L1 |
| **B2** | bridge-to-biology, plausible (every empirical biology claim here is at most this) | **canon L2 (cross-domain analogy)** |
| **B3** | application/measurement: testable over data, **pending** (project ceiling) | a *narrowing* of canon L2→application; **not** canon L3 |
| **B4** | clinically validated (prospective, controlled, replicated) — **currently empty** | a regulated claim *outside* this plan |

**Project ceiling: B3-pending.** Every emitted artifact carries a `level` tag; the renderer refuses any claim whose wording exceeds its tag. **Any B4 sentence is a bug.** Note that under *canon's* ladder, essentially every empirical statement in this plan is L2 — the rename keeps that honest instead of inflating biology claims into canon's cosmology tiers.

### 9.3 Named overclaim risks (each pre-empted)

- **O1** "It measures health/vitality/consciousness" — banned-output lexicon for any field ≤ B3.
- **O2** "Low U = the patient is unstable/dying" — every U ships with `evidence_confidence`; low-evidence scores are "not interpretable" (snapshot ≠ trajectory; sparsity artifact).
- **O3** "It diagnoses / treats / replaces clinicians" — architecturally confined to entity-type/mechanism level; recommendations address **researchers about mechanisms**, never patients/HCPs about a named individual.
- **O4** "The triad is proven biology" — B2 tag + "competing decomposition exists; orthogonality untested until §8.3" note.
- **O5** "Higher U = a better/worthier organism" — **the eugenics attractor.** U is never computed across persons, never used to compare organism worth; any whole-organism scalar is a "model coverage indicator," not a worth rank.
- **O6** "The AI jury is objective" — consensus measures *agreement*, not correctness; always reported beside external ground truth.
- **O7** "It models the body dynamically in real time" — "dynamic" = across *model generations* / simulated trajectories, never live physiology.
- **O8 (new)** "The weakest pillar names the disease mechanism" — this is a **hypothesis conditional on proxy-axing (§2.5/§2.6)**, pre-registered as P2(mech), reported with the explicit caveat that re-axing a proxy can flip the label. Until P2(mech) passes with proxy-reassignment stability, it is INTERPRETATION.

### 9.4 Regulatory boundary — stated as INTENT, not settled fact (fix C6)

**Triadic Biology is designed to be research-use-only and to stay outside clinical regulation:** not a medical device, not diagnostic software, not clinical decision support; producing no diagnosis/treatment/prognosis for any individual; recommendations addressed to researchers about mechanisms. **However, classification is not self-determined.** The correct framing is: *"We **intend** RUO and have **designed** to stay outside even FDA Non-Device CDS; whether a regulator agrees — especially once a weak-zone map is keyed by cell × location and ranks interventions — is adjudicated case-by-case, not by us."* The prior plan's flat assertion "falls *outside* even FDA Non-Device CDS" is itself an overclaim and is withdrawn. Rules unchanged: no individual diagnosis; RUO banner on every artifact; human-in-the-loop and human-on-top; no emergency/triage/monitoring pathway. Any future intent to inform individual care is a **new project at B4** with prospective trials, IRB approval, and the appropriate SaMD/CDS pathway.

### 9.5 Data ethics, privacy & dual-use — the deny-list is necessary but NOT sufficient (fix C5)

Public ontology/literature first (CL, UBERON, Reactome, GO, BioGRID/STRING). Provenance mandatory: every principle carries accession + version + date; unsourced principles are B0 and cannot enter scoring. If non-public human data is ever used: de-identification (HIPAA Safe Harbor / GDPR), consent + IRB, never used for individual care, never sent to external model APIs, minimized and not persisted.

**Dual-use — stated honestly, not solved.** A "find the weakest pillar of the weakest node and the cheapest flip" engine is a **destabilization-target finder with the sign flipped** — the *stabilization* and *weaponization* computations are the same; the fragility map is the dual-use artifact *regardless of stated objective*. An objective deny-list ("how to destabilize host X") is **necessary but not sufficient** governance, because it constrains *objectives*, not *outputs*. Honest controls: (a) the deny-list and human-review gate remain; (b) **fragility maps for pathogen-targeting-of-hosts are not produced or released**; (c) access to ranked organism-level fragility outputs is gated and logged; (d) the residual risk is acknowledged in writing rather than declared eliminated. Permitted polarity is **stabilization of beneficial systems and study of pathology**, never weaponizable destabilization — and the plan concedes this boundary is partly social/operational, not purely technical.

### 9.6 Explicit NON-GOALS

1. Not a diagnosis/prognosis/treatment recommender for any individual.
2. Not a measure of health, wellness, vitality, fitness, life/death, or consciousness.
3. Not a real-time physiological simulator (no live monitoring).
4. Not an organism/person ranking or worth metric (no cross-individual U).
5. Not a proof that biology is triadic (chosen, non-unique frame; orthogonality untested until §8.3).
6. Not autonomous (no closed-loop action on any biological/clinical system).
7. Not a replacement for clinicians, biologists, lab validation, or regulatory review.
8. Not a source of B4 claims until prospective, controlled, replicated validation exists.
9. Not a destabilization / weaponization tool (residual dual-use risk acknowledged, §9.5).
10. Not a universal-constant engine — 0.618 and every anchor are tunable, domain-calibrated defaults, not laws.
11. **Not a mechanism-localizer until P2(mech) passes** — "the weakest pillar names the mechanism" is a hypothesis, not a delivered feature (§2.5).

### 9.7 Mechanizing the discipline

Every emitted item is a **claim envelope** `{register, epistemic_level B0–B4, text, value, evidence{n_valid_models, consensus_pct, mode}, provenance[], external_ground_truth{metric, value, agreement}}`. An **output lint** rejects: any claim above B3; any ≤B3 claim using the banned lexicon (health/diagnose/treat/conscious/…); any decision-grade B3 claim lacking an external metric or <2-of-3 SSS-Guard agreement; any cross-person aggregation; any deny-listed destabilization target. The weak-zone scan emits each flag as a **research hypothesis** (`"model flags {node} weakest on {pillar}; HYPOTHESIS for study; mechanism-axis conditional on proxy-axing"`), tagged with `low_score_cause ∈ {evidence_sparse, genuinely_imbalanced, lattice_approx}` — only `genuinely_imbalanced` is a candidate biological hypothesis (a flagged weak zone is frequently a data gap, not a biology gap).

---

## 10. Glossary

| Term | Definition |
|---|---|
| **F / P / A** | Form (structure/identity, ↔Time), Position (locus `q` + context `c`, ↔Space), Action (function + **energy-maintained order incl. Vₘ**, ↔Energy) — the three candidate orthogonal axes (separability tested, §8.3). |
| **U** | `∛(F·P·A)` — non-compensatory geometric stability score; any pillar → 0 ⇒ U → 0. |
| **δ (delta)** | `(max−min)/(max+0.01)` — pillar imbalance; high δ = decoupling. |
| **SI** | `U/(1+δ)²` — imbalance-penalized Stability Index; verdict bands 0.38 / 0.618 (tunable defaults). |
| **X (4th axis)** | Optional anti-entropy / maintenance-debt slot (NDT N=4); `U₄=(FPA·X)^¼`. **INTERPRETATION until P6 gives it a falsifier (§2.4).** |
| **ℳ (Meaning)** | `∫ U_org dt` — accumulated model-internal stability; the headline optimization target (a coverage indicator, never a worth rank). |
| **Weak-zone scan** | Locate lowest-SI nodes (min-pillar targeting) and rank by leverage (`ΔMeaning / ∛cost`). |
| **Weakest pillar** | `argmin(F,P,A)` — the targeted axis; **names the mechanism only as a hypothesis conditional on proxy-axing (§2.5).** |
| **Non-compensatory** | A strong pillar cannot rescue a collapsed one; geometric mean + δ enforce this. |
| **AND/OR aggregation** | Serial subtrees use weakest-link geometric roll-up; parallel/redundant pools use reserve-aware OR (graceful degradation) — distinguishes brainstem from nephrons (§5.2). |
| **BioSystem** | The universal recursive node type (one schema, all scales): `F{} P{} A{} G{} + state s`. |
| **TB-KG** | Triadic Biological Knowledge Graph — typed property graph of BioSystems + single-axis-labeled edges. |
| **Open-world guard** | "Absent from atlas" → `UNKNOWN`, never `FORBIDDEN`; only positively-contradicted actions are vetoed (§4.3). |
| **TPL guard `G{}`** | `{src; conf; level; mode}` provenance attached to every fact/score. |
| **TriadicDomain** | The GSI-RTD interface (`embed_form / build_position_graph / enumerate_actions / execute_action / evaluate_sss`) that Triadic Biology implements for `biology.organism`. |
| **TAA agents** | Form / Position / Action pillar agents (informationally siloed — an idealization, §6.1) + Generalizer Σ. |
| **LGP-12** | The 12-step scan→detect→…→audit→learn control loop. |
| **AD-RTD** | Action-Driven decomposition: `A → F\|A → P\|F,A → evaluate → triage` (engineering mode). |
| **SSS / AI jury** | System Stability Score pipeline; applied **only to a leverage-selected subset** of nodes, not every node (§5.1/B5). |
| **SSS-Guard** | Irreversible (simulated/recommended) decisions require ≥2-of-3 independent SSS instances agreeing **and** an external outcome metric. |
| **TAD / DPA-SI** | Trajectory weak-zone tools: per-axis resource accumulation; dip/peak SI recovery ratio ρ. |
| **Mode A / Mode B** | Abstract (scores the entity *type*) vs Specific (scores one instance, missing → 50). |
| **Cross-domain transfer (β)** | `impact_new = β·impact_source + (1−β)·prior`, β = structural isomorphism in triadic space. |
| **Epistemic levels B0–B4** | metaphor / proved-within-model / bridge-to-biology / testable-pending / clinically-validated (the last empty). **Renamed from canon L0–L4 to avoid level-inflation (§9.2).** |
| **Claim envelope** | Per-output record carrying register, epistemic level, evidence, provenance, external-truth slot; gated by the output lint. |
| **Tree-vs-lattice** | Roll-up assumes `PART_OF` is a tree; immune/microbiome are cross-cutting overlays (lattice) handled by explicit edges and flagged `LATTICE_APPROX` (§7). |

---

*Triadic Biology's job is narrow and falsifiable, and its first job is to try to kill itself: prove that Form/Position/Action carry **independent** information in real data and that **non-compensatory** geometric aggregation beats arithmetic averaging **robustly to its own anchors** — before claiming anything about mechanism or fragility. If those Phase-0 tests pass, scale. If F/P/A aren't separable, or the geometric win is an anchor artifact, we have falsified the triad in biology, and we report that as the most valuable result this plan can produce.*
