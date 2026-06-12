# APPENDIX TRB — TRIADIC BIOLOGY
### An application of U-Theory to the domain `biology.organism`

> **CANONICAL HEADER**
> **Appendix code:** TRB · **Corpus:** U-Theory / Universal Model · **Parent record:** DOI 10.17605/OSF.IO/74XGR
> **Canonical triad instantiated:** **Code = Form (F) · Credo = Position (P) · Rights = Action (A)**, registered onto living systems (see §A.1).
> **DPR currencies:** canon prices stability in five — **Space, Time, Energy, Freedom/Irreversibility, Coherence/Entanglement.** F/P/A pay the first three. The other two are an **optional, gated extension** (§5.5), admitted only after the core tests pass.
> **Project epistemic ceiling:** **B3-pending.** Under canon's ladder every empirical biology statement here is at most **canon-L2** (cross-domain analogy); **no canon-L3/L4 (cosmological/physical/clinical) claim appears anywhere — any such sentence is a bug** (§8.5, §9.2).
> **Sibling appendices referenced:** GSI-RTD, QTC, QMC, NDT, UCT, RH. See §A and §10.

> **STATUS BANNER**
> **Type:** Specification / pre-registration. **Not** a runtime, benchmark, dataset, or result.
> **What TRB delivers:** a pre-registered, runnable test of **(i) F/P/A separability** in atlas data (P0/P0b) and **(ii) system-level coherence non-compensation** (P8). These tests are the product (§1). The per-cell *mechanism-localizer* ("the weakest pillar names the disease mechanism") is an **explicitly gated hypothesis** demoted behind those tests (§2.5, §8.2).
> **Maturity:** B3-pending. No deployed engine, no replication, no validation. Every empirical-sounding statement is a *proposal to be tested*.
> **Use:** **Research use only.** **NOT a medical device**, not diagnostic software, not clinical decision support; no diagnosis/prognosis/treatment for any individual. See §9.
> **Symmetric-retirement contract (read first):** every gated claim names *both* what its falsifier admits **and what a failed falsifier RETIRES** (§9.8). A failed gate **removes** a claim from the ledger; it is never parked in INTERPRETATION forever.

> **Revision history:** see `TRB-CHANGELOG`. This file states the corrected positions directly; the audit trail of prior critique rounds (R1–R10) and patch taxonomy lives in the external changelog, not inline.

---

## A. Relation to U-Theory canon (placement in the corpus)

This section states how Triadic Biology sits inside U-Theory, what canonical claim it exercises, and what it inherits (discipline) versus what it must not (conclusions).

**What TRB *is* — and is *not*.** Triadic Biology is U-Theory **applied to** living systems. **It is an instance of the framework, not evidence that the framework is true** (§9.6-5). The thing to inherit from canon is canon's *falsifiability discipline*, not its conclusions — so TRB's first job, like the corpus's, is to try to falsify its own load-bearing assumption (separable F/P/A, §8.3) before claiming anything about biology.

### A.1 The same invariant triad, registered onto life

Canon fixes one triad — **Code = Form, Credo = Position, Rights = Action** — and asserts it is *scale- and substrate-invariant*: the *meaning* of F, P, A is identical across governance, quantum systems, and organisms; only the measurable proxies change. Biology makes the labels unusually literal:

- **Code = Form** — the genome/epigenome/proteome: structure and identity literally encoded.
- **Credo = Position** — the niche/compartment/signalling frame the entity is embedded in: its relational "where-and-in-what-context."
- **Rights = Action** — the functions the entity is licensed and able to perform, and the energy continuously spent to maintain order.

The v25.2 mirror (Space↔Form / Time↔Position) is **forbidden** here exactly as in canon (§2.1).

*Caveat.* The labels **Code / Credo / Rights** are governance-derived. "Code = genome" is apt; "Credo = compartment" is a stretch. Their *fit to biology* is an **L0 framing convenience, not a load-bearing claim**: nothing numeric depends on the names; the operational content lives in the proxies (§5.1) and the falsifiers (§8). A reviewer may reject the nomenclature without touching a result.

### A.2 This appendix *exercises* the cross-domain-transfer claim — it does not assume it

The corpus's transfer coefficient β (structural isomorphism in triadic space, §6.5) predicts that a stabilization heuristic transfers between domains in proportion to *triadic-structural* similarity, not surface analogy. Biology is a stress-test: **if F/P/A are not even separable in biological data (§8.3), β-transfer into biology is undefined**, and the corpus's universality claim is *narrowed by* biology rather than confirmed by it. Reporting that narrowing, should it occur, is the appendix's contribution.

### A.3 Runtime — biology is a *conformant domain*, not a parallel theory

Triadic Biology implements the GSI-RTD `TriadicDomain` interface (`embed_form / build_position_graph / enumerate_actions / execute_action / evaluate_sss`) for `biology.organism` (§3, §10). The canonical search→scheduler→agents→cycle→score→learn machinery runs with no bespoke orchestration. Every capability claimed must be expressible through that interface — a hard consistency constraint, re-checked in §10.

### A.4 N-adic placement (NDT) — TRB *amends* NDT, it does not "obey" it

NDT's N-adic decomposition treats triadic (N=3) as default and admits lifting only when a substrate *earns* an extra currency. NDT places **biology at N=4** (anti-entropy currency) and reserves **N=5 for quantum substrates** ("nothing classical can" pay the coherence currency). TRB runs **3-adic by default** and, in §5.5, examines biology against canon's five currencies. Two findings are recorded as **amendments to NDT, not conformance**:

1. **Non-uniform lifting.** Biology does **not** lift to a clean 5-adic *per-node* score. One added currency (Freedom/Irreversibility) is a per-node pillar; the other (Coherence) is intrinsically an *aggregation-level* quantity. NDT-1's uniform per-node `U_N` formula must be **amended** to admit leaf-vs-relational currencies (§5.5.4).
2. **Classical 5th currency.** TRB instantiates the 5th-slot via *classical* synchronization (Kuramoto *r*), whereas NDT reserves the 5th currency for quantum coherence. TRB therefore populates a **classical coherence analogue of the 5th slot, not NDT's quantum 5th** (§5.5.7), and flags that NDT and TRB disagree on whether biology can touch the 5th slot at all. This disagreement is logged for NDT maintenance, not papered over.

### A.5 The five DPR currencies — forward pointer

| # | Canon currency | This appendix | Status |
|---|---|---|---|
| 1 | **Space** | Position (§2.1) | scored (B3-pending) |
| 2 | **Time** | Form (§2.1) | scored (B3-pending) |
| 3 | **Energy** | Action (§2.1) | scored (B3-pending) |
| 4 | **Freedom / Irreversibility** | optional §5.5 X-axis (potency / commitment) | per-node pillar; **gated by P7; removed if P7 fails** (§5.5.1, §9.8) |
| 5 | **Coherence** (classical; *not* Entanglement) | inter-node synchrony, distinct from intra-node δ (§5.5.2) | aggregation-level; **gated by P8; removed if P8 fails** (§5.5.2, §9.8) |

### A.6 Epistemic stance inherited from canon (level-inflation forbidden)

Canon's RH ladder is **L0 = Meta-evaluation, L1 = Operational stability, L2 = Cross-domain analogy, L3 = Cosmological extension, L4 = Literal physical claim** (RH_CRITICAL_REVIEW §71–75, quoted verbatim in §9.2). TRB keeps its own ladder (B0–B4) precisely so it cannot borrow canon's cosmological tiers (L3/L4) for biology. **Every empirical biology statement here is at most canon-L2.** The full mapping is tabulated in §8.5 and §9.2.

---

## 1. Thesis

**What TRB delivers — and is judged on — is two pre-registered, runnable tests:**

- **(i) F/P/A separability** in real atlas data: do Form, Position, and Action carry *independent, conditionally non-redundant* information, or are they three transforms of one transcriptome? (P0/P0b, §8.2–§8.3.)
- **(ii) System-level coherence non-compensation:** does a measured inter-node order parameter (Kuramoto *r*) explain system function that aggregated per-node F/P/A cannot — fibrillation as the clean case? (P8, §8.5.)

These two tests are the product. They are runnable, falsifiable, and their value does not depend on any downstream feature holding.

**The mechanism-localizer is a gated hypothesis, not the thesis.** The aspiration that *"the weakest pillar names the disease mechanism"* is **demoted to a pre-registered hypothesis (P2-mech)** whose validity is conditional on F/P/A separability passing first **and** on a defensible proxy-to-axis assignment (§2.6). It is delivered only if its gates pass, and **retired if they fail** (§9.8). Marketing it as a delivered capability would be selling a product deferred past every runnable test.

If (i) and (ii) pass, TRB scales toward a hypothesis-generation and triage engine indexed by *cell × location × interaction* rather than *disease × specialty*. If F/P/A are not separable, **that negative is the most valuable result the plan can produce**, and the wager is reported as lost.

---

## 2. Core Idea & the F/P/A → Biology Mapping

### 2.1 The invariant triad (canonical v26)

The mapping is intended to be scale-invariant: the *meaning* of F, P, A is identical for a protein and for a whole organism; only the proxies change. This invariance is what *licenses* recursion and cross-scale transfer — and it is exactly what §8.3 tests rather than assumes. **The v25.2 mirror (Space↔Form / Time↔Position) is forbidden.**

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

`U = ∛(F·P·A)` is the canonical SSS geometric-zero keystone. `δ` and `SI = U/(1+δ)²` are **TRB-introduced derived primitives** (not in APPENDIX_SSS), declared as such. Geometric aggregation is the architectural keystone *under test*: a single collapsed pillar zeroes the system; `δ` penalizes imbalance. Verdict bands (domain-tunable defaults, **not** universal constants):

- **SI ≥ 0.618** → Stable. Proceed.
- **0.38 ≤ SI < 0.618** → At-risk. Rebalance the weakest pillar.
- **SI < 0.38** → Critical. Stop; fix the weakest pillar first.

High-stakes tissues raise the threshold (e.g. cardiac conduction, brainstem → θ ≥ 0.90). **All numeric thresholds and anchors are free parameters of the model, not constants of biology** (the single canonical statement of this caveat; see §5.1, §8.3).

### 2.3 Recursion & the assignment rule

Every node at every depth is itself a triad (`depth d ⇒ 3^d subsystems`, never enumerated, §7). Pillars are assigned by three orthogonal questions, each at the node's own scale:

```
FORM(e)     := identity/structure of e, vs its state-conditioned class ideal   (points DOWN-IN)
POSITION(e) := placement of e inside its PARENT (L+1) + operational context     (points UP-OUT)
ACTION(e)   := e's CONTRIBUTION to the ACTION of its parent (L+1)               (points UP-FUNCTIONAL)
```

**State-conditioning.** "Class ideal" is not static. Each node carries a **state vector** `s = (cell-cycle phase, differentiation stage, circadian phase, activation state)`. Proliferation is normal in a crypt base cell in S-phase and pathological in a differentiated cardiomyocyte; "allowed action" and "ideal Form" are evaluated *conditional on `s`*. Form-time constants (a 5-day enterocyte vs a lifelong cardiomyocyte) are per-cell-type parameters.

**The combinatorial anchor problem (stated, with a fallback).** State-conditioning (cell-type × cycle × diff-stage × circadian × activation) multiplied by per-cell-type anchoring (§5.1) yields *thousands* of anchors no reference data can populate. Fallback: when a (cell-type × state) cell lacks a fitted anchor, the score falls back to the nearest available conditioning level, and **any score against a defaulted/un-conditioned anchor is tagged `LOW_CONF_ANCHOR`** and excluded from the §8.3 anchor-perturbation ablation (you cannot perturb an anchor that was never conditioned).

### 2.4 The optional 4th axis (NDT N=4) — gated, renders no number

Biology arguably pays a 4th currency `X` (anti-entropy / maintenance debt) via metabolism. The default model runs **3-adic**; every record carries an optional `X` slot so aging/repair/infection questions can be lifted to tetradic without schema change:

```
U₃ = ∛(F·P·A)                       (default)
U₄ = (F·P·A·X)^(1/4)                (aging / infection / repair — research mode)
X proxies: developmental potency / reprogramming-barrier height, telomere & repair reserve,
           NAD⁺/proteostasis capacity, autophagic flux, immune reserve.
```

> **Gate and retirement.** `U₄` is **INTERPRETATION — it renders no number or verdict — until P7 (independence) admits it** (§5.5.1, §8.5). The admission gate is **P7 alone** (statistical independence of Freedom from Form). P6 (time-ordering under infection) is a *separate downstream claim about infection dynamics*, not the admission gate (§2.5, §8.2; reconciled once in §9.8). **If P7 fails, the X-axis is removed from the ledger and from §5.5 — not parked in INTERPRETATION** (§9.8).
>
> *Granularity caveat.* X-proxies (telomere length, NAD⁺, autophagic flux, DNA-repair competence, reprogramming-barrier height) are **not in scRNA atlases** and are population/bulk/live-imaging measurements. The 4th pillar is therefore populated at **coarser granularity than F/P/A** (per-cell-*type*, not per-cell), which the `U₄` product silently mixes — so P6/P7 run only on the modalities that carry X, and any U₄ is tagged with its X-granularity.

### 2.5 Disease = which pillar fails — a GATED HYPOTHESIS, not a delivered feature

The aspiration is that the triad distinguishes disease *mechanism* by *which axis* collapses. **This is a hypothesis gated behind F/P/A separability (P0) and behind proxy-axing being defensible (§2.6), not a demonstrated property** — because "which axis" depends entirely on the (contested) proxy-to-axis assignment. It is pre-registered as P2-mech (§8.2) and **retired if its gates fail** (§9.8).

- **Ischemia = Position-collapse** (the cell's perfusion/O₂ *context* is destroyed though the cell hasn't moved; Action then starves). The Position proxy is perfusion territory / local pO₂ / capillary distance — **not** Vₘ (which is Action; §2.6). *Measurability caveat:* per-cell pO₂/perfusion is **not** single-cell-resolved in any cited atlas; in current data ischemia Position-context is a hypoxia-**response** signature (HIF targets, glycolytic shift) inferred from the cell's own Action/Form — which **reintroduces a circularity the model must own** (§5.4). The worked example states this rather than presenting a measured perfusion number.
- **Aging = triadic drift** — `dδ/dt = k_entropy − k_repair·U` (rising imbalance over time). The rate constants have **no atlas source** and are free research-grade parameters (§6.2).
- **Cancer = δ-spike / triadic DECOUPLING — mechanism axis TBD.** The defensible claim is narrow: cancer presents as a **high-δ decoupling event** (Form, Position, and Action stop co-varying); *which* axis is the binding constraint is case- and stage-specific, an output to be validated, not asserted. "Names the mechanism" is downgraded to "flags decoupling; candidate mechanism axis reported with uncertainty."
- **Dysbiosis** — the microbiome is a *node with a causal edge*, not a scalar smuggled into every host cell's pillar (§2.6/§4.3).

**Optional currency-4/5 re-reading (gated by P7/P8, not asserted).** Once Freedom and Coherence are admitted, these examples *could* be described more richly — but these are *additional gated hypotheses*, not new assertions: cancer plausibly recruits a **Coherence collapse** (loss of tissue-level coordination) and, in *some* subtypes, a **Freedom-band violation toward de-differentiation** (§5.5.5) — falsified if Coherence/Freedom proxies add nothing beyond F/P/A; aging plausibly = drift **+ Freedom depletion + Coherence erosion** — falsified if reserve and inter-system synchrony do not decline with age *beyond* F/P/A drift; **ischemia stays Position** (the lens must *discriminate* — a currency set that explained every disease would explain none).

### 2.6 Where the mapping is contested — and how this plan resolves it

Several proxies were mis-axed or double-loaded. Resolutions:

- **Energy-maintained order (Vₘ, ion gradients) is ACTION, not Position.** Resting potential is maintained by the Na⁺/K⁺-ATPase burning a large share of cellular ATP — a *continuously-paid energy* quantity. In ischemia the chain is `ATP↓ (Action) → pump fails → Vₘ collapses`. Vₘ scores **Action**; ischemia Position uses spatial-context proxies. (This re-axing de-circularizes the flagship ischemia example.)
- **Form is identity-integrity, not damage-rate.** The Form pillar splits non-compensatorily into `f.identity` (cell-type fidelity, fold integrity, karyotype/driver status — *is this still what it is?*) and `f.damage_rate` (aging proxies). A young cell with a single driver has corrupted identity despite a clean damage-rate; a healthy old neuron has high mutation burden but intact identity. The split prevents Form from silently becoming an aging meter. *Note (B-2):* **pLDDT is a reference-level, cell-*invariant* fold confidence — not an in-cell folding measurement** — so it is **dropped as a per-cell Form proxy**; in-cell fold integrity requires a proteostasis readout (aggregation reporters, thermal proteome profiling) where it exists, else the per-cell fold-integrity claim is omitted (§5.1).
- **Position `(q,c)` is two non-compensatory sub-components.** `p.locus = q` (literal/categorical localization) and `p.context = c` (niche integrity, neighbours, dependency satisfaction) combine via `P = √(q·c)`. "Right cell in a degraded niche" and "wrong cell in a fine niche" now score differently. One pillar not two: both are *Space-context* prices governed by the same intervention class (re-localize vs restore niche), but their independence is preserved internally.
- **Signaling is re-typed to avoid a two-axis edge.** `SIGNALS_TO` (a Position edge: context/dependency) and `INDUCES_ACTION` (an Action edge: downstream effect) are split. No single edge loads two axes. *Caveat (M-2):* both are commonly re-typed from **one** NicheNet/CellChat ligand→target inference, so they are **perfectly correlated by construction and are not independent evidence** — noted at §4.3.
- **Microbiome / immune system: node, not scalar-in-a-pillar.** They are **scored nodes** influencing host cells through explicit causal edges (`SUPPLIES`, `SIGNALS_TO`, `DISRUPTS`); edge-borne influence enters the roll-up via edge-weighted aggregation (§5.2), and is **never** also copied as a scalar into a host cell's `p.context`. Because immunity is mobile and lattice-structured, see §7's tree-vs-lattice limitation.
- **Action is not a function of Action-data alone — acknowledged.** Flux feasibility depends on substrate (Position) and enzyme presence (Form). The Action-Agent's "sees `h_a` only" (§6.1) is an *architectural idealization, not a biological fact* — which is precisely why the orthogonality ablation (§8.3) is run first.

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
 │  │ HCA, UniProt      │   │ STRING/IntAct,       │   │ Recon3D (FBA*),    │          │
 │  │                   │   │ CellPhoneDB*, Visium │   │ BRENDA, Seahorse†  │          │
 │  └───────────────────┘   └──────────────────────┘   └────────────────────┘          │
 │   * FBA = MODEL OUTPUT computed FROM the transcriptome (= Form's data); NOT measured │
 │     CellPhoneDB = INFERRED from co-expression; † Seahorse/respirometry = sparse,     │
 │     the ONLY measured-Action source ⇒ F,P,A largely 3 transforms of ONE transcriptome│
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
 │                       B. STATIC U-SCORE ENGINE (the numeric core)                   │
 │  per node:  F,P,A ∈[0,1] (quantitative proxies, IQR-filtered; SSS jury ON A SUBSET) │
 │             U=∛(FPA)   δ=(max−min)/(max+.01)   SI=U/(1+δ)²   weak_pillar=argmin     │
 │  roll-up:   GEOMETRIC on child U everywhere + AND/OR mix (serial vs redundant)      │
 │             + edge-weighted context terms (SIGNALS_TO/SUPPLIES/DISRUPTS enter math) │
 │  (static per-node scoring is runnable; the DYNAMIC twin below is research-grade §6.2)│
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │                  C. WEAK-ZONE SCAN  (localize → rank by leverage)                   │
 │  Stage 1  min-pillar targeting: hard gates G1–G4 (G4 = pillar collapse → reject)   │
 │           open-world guard: "absent in atlas" → UNKNOWN, never "forbidden"          │
 │           multiplicity control: empirical-null + donor-preserving FDR (§5.4)         │
 │  Stage 2  leverage: ∂U_org/∂U_n  &  counterfactual ΔMeaning ;                       │
 │           Priority = ΔMeaning / ∛(C_t·C_s·C_e)   (ties → cheapest)                  │
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │             D. AI / DIGITAL-TWIN CONTROL LOOP  (research-grade; §6.2)                │
 │   ┌─ Form-Agent ─┐ ┌─ Position-Agent ─┐ ┌─ Action-Agent ─┐ ┌─ Generalizer Σ ─┐     │
 │   │ h_f only     │ │ h_p only (graph) │ │ h_a only       │ │ fuse → g(f,p,a); │     │
 │   └──────────────┘ └──────────────────┘ └────────────────┘ │ name weakest +   │     │
 │   (informational siloing is an idealization; biology is coupled — §2.6, §6.1)  │   │
 │   twin layers: Action(FBA/ODE) · Position(reaction-diffusion) · Form(damage)  ┘     │
 │   loop: scan → detect → decompose → rank → leverage → propose → SSS-Guard → act     │
 │         → re-aggregate → learn (impact/weights, ε→UCB1→Thompson, transfer β)        │
 └───────────────────────────────────────────┬────────────────────────────────────────┘
                                              ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │            RH. RECURSIVE-HARDENING GOVERNANCE  (wraps every output)                 │
 │  claim envelope {register, epistemic_level B0–B4, provenance, external_truth}       │
 │  output lint: ban "health/diagnose/treat…" ≤B3 · no cross-person U · deny-list      │
 │  SSS-Guard: irreversible call ⇒ ≥2-of-3 SSS agree + external outcome metric          │
 └────────────────────────────────────────────────────────────────────────────────────┘

      Canonical chain:  U-Theory → GSI-RTD(search) → TS(scheduler) → TAA(agents)
                        → LGP-12(cycle) → Twin(environment) → SSS(score) → Learning → Gates
```

---

## 4. The Data Layer & Knowledge Graph

### 4.1 Design constraints inherited from canon

| # | Constraint | Consequence for the schema |
|---|---|---|
| K1 | F↔Time, P↔Space, A↔Energy mandatory | each node carries exactly one F-, one P-, one A-bundle; energy-maintained order (Vₘ) lives in A |
| K2 | Orthogonality / no cross-talk | three disjoint namespaces `f.* / p.* / a.*`; no edge loads two axes. *Whether the data honor this is the open question — §8.3.* |
| K3 | Non-compensatory | geometric aggregation everywhere; a zero pillar is representable and load-bearing |
| K4 | Position = `(q, c)`, non-compensatory inside | `p.locus = q` **and** `p.context = c`, combined `P=√(q·c)` |
| K5 | Recursion (3^d), tree-structured | one universal node type — **with a stated lattice exception for immune/microbiome (§7)** |
| K6 | Group identical Forms; maximize Coverage/Cost not \|S\| | store **FormTypes** + `abundance`; near-identical subclones split at a defined threshold (§4.4) |
| K7 | AD-RTD: `A → F\|A → P\|F,A` | "allowed action" = candidate `ENABLES` edge gated by SI, with an **open-world guard** (absence ≠ prohibition, §4.3) |
| K8 | TPL guardrails | every fact/score carries `G{src;conf;level;mode}` → confidence travels with data |

### 4.2 Real data sources (one dataset → one axis) — with independence caveats

- **Form (structure/identity):** Cell Ontology (CL), Tabula Sapiens / HCA (cell-type identity, K6 grouping), UniProt / Ensembl / RefSeq, Reactome (complex composition). *(pLDDT/AlphaFold dropped as a per-cell Form proxy — cell-invariant, §2.6.)*
- **Position (locus + context):** UBERON (anatomy), GO-CC (compartment), Human Protein Atlas (validated localization), STRING / IntAct / BioGRID (relational neighbourhood), CellPhoneDB / CellChat / NicheNet (cell–cell niche edges — **inferred from co-expression, not measured**), 10x Visium / Xenium / MERFISH (literal spatial coordinates `q`).
- **Action (function/energy):** Reactome / KEGG (reaction primitives), Recon3D / Human-GEM (genome-scale stoichiometry → **context-specific FBA via GIMME / iMAT / tINIT / Compass is a *model prediction computed from the transcriptome*, not a measurement** — see §8.4/B-2), GO-BP/MF (functional labels), BRENDA / SABIO-RK (kinetics), and **measured Action where it exists** (Seahorse OCR/ECAR, respirometry, metabolomics — sparse).
- **External ground truth (kept independent of scoring inputs):** DepMap/Achilles essentiality, gnomAD pLI/LOEUF, COSMIC/Open Targets, clinical/registry outcomes. **Independence is audited, not assumed:** essentiality and constraint correlate with broad/high expression, which also feeds Form; §8 includes a mandatory **feature-leakage audit** (P0c) before any of these is used as truth.

> **Data-independence warning (load-bearing, two layers).**
> **(a) Shared upstream matrix.** F (identity), P (niche via CellPhoneDB), and A (function labels / FBA) are, in current atlases, three transforms of **one** scRNA matrix. **FBA-Action is worse than correlated with Form — it is computed *from* Form's expression data** (the transcriptome is FBA's *input*), so an FBA-Action × expression-Form product multiplies a number by a transform of itself. Establishing input-independence is **Phase 0**, §8.3, and FBA-Action is **excluded from the separability claim** (§8.4/B-2).
> **(b) Definitional leakage via the cell-type annotation.** "One dataset → one axis" is really **"one annotation → three axes"**: the cell-type label propagates into `f.identity`, the expected niche/compartment, and the chosen FBA cell-model — manufacturing correlation that is *definitional, not biological*, and invisible to any statistical separability test. A **shared-upstream-feature audit** (§8.3) traces every proxy to its raw measurement and flags any value derived from the annotation; pillars are scored from disjoint raw feature sets where possible.

### 4.3 The node & edge model

Every node is one **`BioSystem`** at some scale ∈ {molecule, complex, organelle, cell, tissue, organ, system, organism}, plus non-host classes {virus, bacterium, microbiome, immune-overlay}, carrying a state vector `s` (§2.3). Surface form (TPL):

```tpl
F{cell:cardiomyocyte; state:differentiated; identity:cardiac-TF-program-intact;
  damage_rate:low; genome:diploid-no-driver}
P{locus:LV-myocardium; context:vascularized+normoxic+syncytium-coupled}   ; P = √(locus·context)
A{function:contraction; metab:fatty-acid-oxidation; Vm:-85mV; output:force; flux:Ca-cycling}
G{src:GTEx+echo; conf:0.82; scope:specific; level:B1; mode:assert}
```

Edges are typed; **each loads exactly one axis**:

| Edge | Meaning | Axis loaded | Source |
|---|---|---|---|
| `IS_A`, `PART_OF`/`COMPOSES` | type subsumption, containment (recursion backbone) | Form | CL, UBERON, Reactome |
| `LOCATED_IN`, `ADJACENT_TO`/`IN_NICHE`, `INTERACTS_WITH`, `SIGNALS_TO` | placement, neighbourhood, PPI, ligand→receptor *context* | Position | HPA, Visium, STRING, CellChat |
| `INDUCES_ACTION` | the downstream *functional effect* of a signal | Action | NicheNet, Reactome |
| `PERFORMS`/`ENABLES`, `CATALYZES`/`TRANSPORTS`, `SUPPLIES`/`CONSUMES`, `REGULATES` | function & energy exchange | Action | GO-MF, Reactome, Recon3D |
| `DISRUPTS`/`HIJACKS` | pathogen entropy-export (decomposed into its F/P/A targets) | per-target | VirHostNet, CARD |

*Edge-independence caveat (M-2):* when `SIGNALS_TO` (Position) and `INDUCES_ACTION` (Action) are re-typed from **one** NicheNet/CellChat ligand→target inference, they are **correlated by construction and do not count as independent evidence** for separability.

**Allowed-action inference (K7) with an open-world guard.** The graph never asserts "Form X may do Action Y" as a free fact. It proposes a candidate via `ENABLES`, then computes admissibility: `A_i` is admissible for `F_j` in `P_k` iff `SI(F_j,P_k,A_i) > θ` with a hard veto on any zero pillar (AD-RTD `A → F|A → P|F,A → evaluate → triage`). **Atlases are positive-only: "not observed" ≠ "forbidden."** An action absent from the healthy atlas defaults to `UNKNOWN` (flag `OPEN_WORLD`), **not** `FORBIDDEN`. Only an action *positively contradicted* (e.g. substrate provably absent, `p.context → 0`) is vetoed — so rare-but-normal states are not mass-flagged as pathology.

### 4.4 Identity resolution / entity merge

K6 grouping ("2×10⁹ identical cardiomyocytes = 1 node") requires a merge rule: Forms are clustered by an identity-feature distance with a tunable threshold `τ_merge`; a **near-identical variant** (a subclone carrying one driver mutation) whose `f.identity` distance exceeds `τ_merge` is **split into its own node** with its own `abundance`, so emerging subclones are visible rather than averaged away. `τ_merge` is calibrated and reported, not magic.

---

## 5. The U-Score Engine & Weak-Zone Scan

### 5.1 Per-node scoring

Each raw measurement is normalized to `[0,1]` against physiological reference anchors (`ref_lo` = collapse, `ref_hi` = ideal) with a clamped, monotone, saturating curve (but see §5.5.5 — Action also has a two-sided regime that the monotone ramp under-models, fixed *now*). When a pillar has several observables, the pillar score is itself a non-compensatory (weighted-geometric) combine. Instrumentation (corrected axing per §2.6):

| Pillar | Quantitative proxy | Example anchor (per cell type) |
|---|---|---|
| **Form / identity** | cell-type-program fidelity, karyotype, driver-mutation status (*in-cell* fold integrity only where a proteostasis readout exists; pLDDT dropped) | identity-match 1.0 → 1.0; lineage-confused → 0.0 |
| **Form / damage-rate** | epigenetic-clock acceleration, γH2AX, mutation burden, proteostasis | DunedinPACE 0.8 → 1.0; 1.5 → 0.0 |
| **Position / locus (q)** | localization correctness, compartment match | correct → 1.0; ectopic → 0.0 |
| **Position / context (c)** | niche-edge integrity, perfusion/pO₂ (inferred), contact inhibition, dependency satisfaction | normoxic+coupled → 1.0; ischemic territory → 0.0 |
| **Action** | **measured** OCR/ECAR / respirometry where it exists, else FBA flux feasibility (model prediction, excluded from separability), **Vₘ / ion-gradient maintenance**, functional output | Vₘ −85 mV → 1.0, −20 mV → 0.0; **OCR/biosynthetic flux** low in quiescence is normal (not steady-state [ATP]) |

> **Anchors are the most consequential free parameters (single canonical statement).** `ref_lo`/`ref_hi` *are* where the geometric zero bites, and they are **cell-type-specific and not constants.** Each anchor is fitted per cell type from the physiological range in reference data (1st/99th percentile of healthy distributions, or a literature-curated lethal threshold), recorded with provenance in `G{}`, and **subjected to the anchor-robustness ablation in §8.3** — both anchor *values* (±20%) and the *functional form* of the normalization (ramp ↔ logistic ↔ trapezoid). Any headline result that does not survive both is not reported as a finding. *Disambiguation:* "low Action in quiescence" means low ATP *turnover/OCR* (true), **not** 30%-of-normal ATP *concentration* (near-catastrophe in any viable cell).

**SSS jury — reserved for a subset, not every node.** The SSS two-stage pipeline (Constructor emits up to N=12 falsifiable principles/pillar; AI jury of up to 50 models scores 0–100, IQR-filtered) is **compute-infeasible at every node × timestep** (10³–10⁴ nodes × steps × 3 pillars × ~12 principles × up to 50 models = millions–billions of calls). It is applied **only** to (a) top-K leverage nodes from the weak-zone scan and (b) nodes flagged AT_RISK/CRITICAL. The majority of nodes carry **bare quantitative-proxy scores**; "SSS refines priors" is true only where the jury runs.

**Missing-data discipline (SSS-L4 / Mode-B):** an unmeasured observable → neutral **50**, never dropped, never assumed healthy. Sparse nodes compress toward U≈0.50; `evidence_coverage` and `conf` travel with the value; coverage < 0.3 → `LOW_EVIDENCE`, excluded from irreversible decisions.

### 5.2 Recursive aggregation — geometric throughout, with AND/OR redundancy

Aggregation is **geometric on child U everywhere**; the earlier "Action rolls up additively" claim is deleted (cardiac output is *not* the sum of cardiomyocyte forces; it depends on synchronization — a Position/Coherence property — and total flux is bounded by shared substrate). What "additive" was reaching for (redundancy) is captured by an **AND/OR-aware operator** distinguishing serial dependency from parallel redundancy:

```python
def aggregate(n):
    for c in n.children: aggregate(c)            # post-order
    if n.redundancy == "serial":                 # AND: weakest-link (brainstem, conduction)
        n.U = wgeomean([c.U for c in n.children], [c.weight for c in n.children])
    elif n.redundancy == "parallel":             # OR: graceful degradation (nephrons, lobules, bilateral)
        n.U = reserve_aware_OR([c.U for c in n.children], [c.capacity for c in n.children], n.demand)
    else:                                         # mixed: serial backbone over parallel pools
        n.U = mixed_AND_OR(n.children)
    # context terms: edge-weighted influence of NON-child neighbours enters here
    n.U *= context_factor(n, edges=[SIGNALS_TO, SUPPLIES, DISRUPTS])
    childU = [c.U for c in n.children]
    n.delta = (max(childU)-min(childU))/(max(childU)+0.01)
    n.SI = n.U/(1+n.delta)**2
    if any(c.U < 0.38 for c in n.children) and n.redundancy == "serial":
        n.flag = "weakest-link block: fix critical serial child first"
```

- **Serial (AND):** one survival-critical, irreplaceable component at U≈0 zeroes the parent (cardiac arrest = one system → 0 → organism → 0). Correct for brainstem, conduction, single points of failure.
- **Parallel (OR) / functional reserve:** redundant pools (a million nephrons, liver lobules, bilateral organs) degrade *gracefully* — losing one of a million nephrons does not crush kidney U. Pure serial AND is biologically wrong here; reserve-aware OR is used instead.
- **Edge-weighted context:** the Position-context the *thesis* depends on (ischemia, dysbiosis) enters the math via `INTERACTS_WITH / SIGNALS_TO / SUPPLIES / DISRUPTS`, not just `PART_OF` — the edges that carry the mechanism.

`weight`, `redundancy`, `capacity/demand` are per-node functional parameters (brainstem serial weight ≈ 1.0; a single nephron parallel weight ≈ tiny), reported and calibrated, not magic.

### 5.3 Temporal dynamics & Meaning

The tree is re-scored each timestep `t`; re-scoring is **budgeted** to changed/at-risk subtrees, not the whole forest.

- **SI-velocity** (EWMA) — declining SI flags a weak zone before threshold crossing.
- **δ-volatility** (CUSUM) — rising imbalance = early decompensation signal.
- **DPA-SI recovery ratio** `ρ = (peak_next − dip)/dip_depth`; `ρ < 0.618` ⇒ structural decline → flag for redesign.

Organism **Meaning** = time-integral of stability, dual of the Stupidity integral:

```
ℳ_org = ∫ U_org(t) dt  ≈  Σ ½(U(tᵢ)+U(tᵢ₊₁))(tᵢ₊₁−tᵢ)      (trapezoidal)
```

**Canonical complementarity.** Canon fixes the duality **ℳ + 𝒮 = T**, where `𝒮 = ∫(1−U)dt` is Stupidity and `T` the elapsed window — the two integrals *partition the clock*. Two riders keep this consistent with the optional five-currency lift: **(i)** the identity needs `U∈[0,1]`; the band-centred currencies of §5.5.5 preserve this (both extremes drive the score → 0). **(ii)** It is clean only on a *single declared clock*: an organism-level ℳ over mixed-timescale currencies must be the **currency-resolved sum** `∑_c ∫U_c dt`, not one `∫U dt`, or the fast currencies (Coherence, ms) are aliased against the slow ones (Freedom, years). ℳ is always computed on the **rendered** score (`U₃` today; `U₄/U₅` only once P7/P8 admit them). **ℳ_org is a model coverage/stability indicator, never an organism-worth metric (§9.3-O5).**

### 5.4 The weak-zone scan (the payload) — ischemia example

**Stage 1 — localization.** Scan every node; flag canonical-gate trips:

```python
for n in all_nodes:
    n.weak_pillar = argmin(n.F, n.P, n.A)
    if min(n.F,n.P,n.A) ≈ 0 or n.SI < 0.38:  flag CRITICAL   # G4 pillar-collapse / stop-fix
    elif n.SI < 0.618:                        flag AT_RISK    # rebalance weakest pillar
    # weak_pillar is a HYPOTHESIS about mechanism, valid only if §8.3 separability holds
```

**Stage 2 — leverage ranking.** Because aggregation is weighted-geometric on serial subtrees, organism U is most sensitive where a factor is smallest:

```
∂U_org/∂U_n = (U_org / U_n) · Π_{k∈path(n→root)} (weight_k / W_parent(k))      (serial paths)
Priority = ΔMeaning / ∛(C_time · C_space · C_energy)            (ties → cheapest)
```

Output = an ordered intervention queue. A CRITICAL *serial* survival-critical node is forced to the top regardless of cost.

**Multiplicity discipline — the scan's biggest statistical liability.** Stage 1 computes `argmin` and an extreme-value flag over **10³–10⁴ nodes** — a textbook **look-elsewhere** problem: even under a pure null, the minimum of 10⁴ noisy scores is *expected* to look alarming. Required, pre-registered:

- **An empirical null per scan**, built by **donor-level** resampling that **preserves the pillar covariance under H₀** (label-shuffling that breaks the donor structure, §8.5-R8, is non-exchangeable and miscalibrates q-values). Flag a node only when its SI falls below the null tail at a controlled level.
- **FDR across the whole scan** (Benjamini–Hochberg / local-FDR q-values); every flag carries its **q-value** in the claim envelope (§9.7).
- **Selection-independent filtering.** The §9.7 `low_score_cause` tag removes `evidence_sparse` and `lattice_approx` nodes *before* FDR — but the `genuinely_imbalanced` filter must use a **selection-independent statistic or a conditional/selective-FDR (conditional BH)** procedure, because filtering on the same SI the FDR then evaluates is post-selection inference that invalidates BH. A uniform-p QQ calibration check is reported as a deliverable.
- **Effect size *and* significance, jointly.** A node can be the *weakest* and still be biologically fine; a flag must clear an **absolute** deficit band (§2.2) *and* the multiplicity-corrected significance, or it is reported as "**not distinguishable from scan noise.**"

**Worked example (cardiomyocyte, ischemia).** Healthy: F=0.92, P=0.90, A=0.88 → U=0.900, SI=0.828 (STABLE). Acute capillary occlusion: the binding deficit is the cell's **perfusion/O₂ context** — a *Position-context* proxy. Vₘ collapse and ATP drop are **Action** symptoms downstream of that context loss, not the Position proxy. The scan localizes the **binding constraint to Position-context**; the canonically-correct first move is **reperfusion** (restore the spatial/context price), not an inotrope (Action) or gene therapy (Form). **Honesty rider (M-7):** per-cell pO₂/perfusion is **not measured** in any cited atlas. In current data the Position-context value is a hypoxia-**response** transcriptional signature (HIF targets, glycolytic shift) inferred from the cell's own Action/Form — so **no confident "P.context = 0.18" is asserted as if perfusion were measured per cell.** Dropping Vₘ removed a circular-but-measurable proxy and replaced it with a non-circular-but-currently-unmeasurable one; that trade-off is owned, and it is exactly what P2-mech (§8.2) must test once spatially-resolved perfusion data exist.

### 5.5 The DPR ledger extension — currencies 4 & 5 (OPTIONAL; gated behind the core)

> **Scope of this section.** §5.5 is an **optional appendix-within-the-appendix.** The runnable product (§1) is the three-currency core. The five-currency completion **adds nothing to the runnable per-node engine, makes the Phase-0 separability problem strictly harder, and widens the dual-use surface** (§5.5.4, §9.5). It is therefore **gated entirely behind P0/P0b passing**, and each added currency is **admitted to rendered numbers only by its own falsifier (P7, P8) and removed if that falsifier fails** (§9.8). It is offered for canon-coherence — a *chosen, non-unique* frame (§9.6-5) — not as a claim that biology *is* five-adic.

Canon prices stability in **five** currencies; F/P/A pay three. The remaining two enter at **different structural levels**, which is why biology does *not* collapse into a tidy 5-adic per-node score (§A.4).

| # | Canon DPR currency | Pays for (biology) | Measurable proxy | Failure mode |
|---|---|---|---|---|
| 4 | **Freedom / Irreversibility** | foreclosed fates; cost to *reverse* a state | developmental potency, reprogramming-barrier height, telomere & repair reserve | commitment trap / loss of regenerative freedom |
| 5 | **Coherence** (classical; not Entanglement) | inter-part synchrony holding parts as one system | Kuramoto order parameter *r*, conduction synchrony, EEG phase-locking | desynchronization (fibrillation) / pathological hyper-coherence (seizure) |

#### 5.5.1 Freedom/Irreversibility — a per-node 4th pillar (gated by P7)

The §2.4 X-axis **is** the canonical **Freedom/Irreversibility** currency — the price paid in *foreclosed options*. Naming it does real work: it supplies an operational, non-circular proxy distinct from "damage" — the **height of the barrier to *reverse* a committed state** (Yamanaka reprogramming *efficiency* / barrier height; CytoTRACE-style potency). And it **double-dissociates from Form in principle**: a healthy terminally-differentiated cardiomyocyte has high Form-identity and near-zero Freedom; a healthy stem cell has high Freedom with intact (stem) identity.

*Caveats it must carry:* CytoTRACE/potency is **transcriptome-derived**, so it shares Form's upstream matrix and is subject to the same separability shadow (excluded from the input-independence claim exactly as FBA-Action is, §8.4/B-2); reprogramming-barrier height is a **population/cell-type assay**, so the "per-node 4th pillar" is at best a per-cell-*type* annotation. It lifts the score to `U₄ = (F·P·A·X)^¼` and **renders no number until P7 admits it; if P7 fails, Freedom is removed from the ledger** (§9.8).

#### 5.5.2 Coherence is **not** a per-node pillar — an aggregation-level currency (gated by P8)

A 5-adic leaf score `U₅ = (F·P·A·X·C)^{1/5}` is a **category error**: coherence lives in the *correlations among nodes*, not inside any one node — a single cell has no coherence with itself. Three consequences:

- **It is not δ.** δ (§2.2) is *intra-node* imbalance (are F, P, A balanced within one node). Coherence is *inter-node* synchronization (do many sibling nodes act as one in time). A tissue can be δ-balanced cell-by-cell yet completely desynchronized (fibrillation), and the reverse. Coherence is a genuinely **new relational input the roll-up does not currently contain**.
- **It enters at the roll-up, not the leaf** — modifying how children combine, alongside the AND/OR operator and `context_factor`, with its proxy supplied as a *parent-level* measurement, never derived from any single child.
- **Its proxy is measured, not another transcriptome transform.** The Kuramoto order parameter *r* ∈ [0,1] (cardiac conduction synchrony, EEG phase-locking) is **measured directly** — the input-independence the §8.3 worry demands and the F/P/A proxies struggle to provide.

**The clean case (the strongest argument it is a distinct currency).** In *early* ventricular fibrillation individual myocytes stay electrically active — per-node Action sits **above the system-output level** — yet the ventricle produces **no net output** because cells are desynchronized. The defensible claim is *non-compensation at the system level*: **system function falls below the floor that aggregating per-node F/P/A would predict** — invisible to any leaf-only model. *(Biology rider, M-6: in **sustained** VF per-cell energetics also collapse, so "Action above zero" applies to **early** VF only.)* Symmetrically, *hyper*-coherence is also pathology (a seizure) — §5.5.5. Pending **P8 (§8.5)**.

**Coverage, not universality (M-6).** A parent-level order parameter exists essentially only in **heart** (optical mapping/ECG) and **brain** (EEG) — ~2 of dozens of organ systems. A cardiac P8 pass validates a *relational order parameter and the aggregation operator*, **not** the per-node leaf triad, and does **not** license a coherence term elsewhere. The coherence roll-up term is **admissible only for nodes with a measured parent-level order parameter; elsewhere it is UNKNOWN (open-world) and must not silently default to 1.0.** Coherence coverage is reported as a fraction of nodes.

#### 5.5.3 The cross-appendix invariant: coherence is *conditionally* protected (the QTC parallel)

Biological coherence is not free: it is sustained only when *coupling* exceeds *heterogeneity/noise* — the **Kuramoto synchronization transition**. Below the critical coupling *r* collapses; above it, the population phase-locks. This is **structurally the same story as APPENDIX QTC**, where decoherence-free-subspace protection was found to be **noise-symmetry-gated**: under the device's **native (independent) noise the benefit is ≈ 0** (`R ≈ 0`; QMC §184 attributing the experiment to QTC §8.3, accession `IBM/qtc_hw_collective_marrakesh.txt`), rising to `R = +0.97` only under **collective-symmetric** noise.

> *Coherence is preserved iff the environment respects a symmetry (QTC) or a coupling-vs-heterogeneity threshold (biology). It is never automatic.*

The structural lesson carries into biology, but **it does not "transfer verbatim"**: QTC's substrate is quantum and symmetry-gated; biology's is classical and threshold-gated. The shared invariant is *conditional, earned protection* — which must be *tested* (P8), never assumed by writing a fifth factor into a product.

#### 5.5.4 The discipline cost, stated plainly

Completing canon's ledger is theoretically tidy but **makes the Phase-0 separability problem strictly harder, not easier.** Three axes already risk collinearity (§8.3); five raise the bar. The accounting:

- **Freedom (X)** is a *per-node* 4th pillar → lifts to `U₄`; gated by **P7** (removed if P7 fails).
- **Coherence** is an *aggregation-level* quantity → it modifies the roll-up (an **inter-node synchronization** input, distinct from the intra-node δ), **not** a 5th leaf factor; gated by **P8** (removed if P8 fails).
- There is therefore **no clean per-node `U₅`** in biology. NDT lifting to N=5 is *non-uniform* here (§A.4): +1 leaf currency, +1 relational currency — which is recorded as an **amendment to NDT-1**, not conformance.
- Both currencies stay INTERPRETATION (render no number) until their falsifiers pass. The extension is a **B2 bridge**, not a B3 measurement, and **not** a claim that biology is five-adic.

#### 5.5.5 Two-sided currencies — and a fix to a *core* pillar (Action)

The `U = ∛(F·P·A)` machinery assumes each pillar is **monotone** (the §5.1 one-sided ramp). That fails wherever *both* extremes are pathological:

- **Freedom:** too little = commitment trap (senescent/locked cell); too much = de-differentiation / re-acquired stemness (oncogenic). Healthy tissue sits in a **band**.
- **Coherence:** too little = fibrillation; too much = pathological hyper-synchrony (seizure), loss of functional segregation.
- **Action (a CORE pillar — fix applied NOW):** Action *also* has a two-sided regime (excitotoxicity, ROS over-production) the one-sided ramp under-models — meaning a hyperactive/excitotoxic cell could be scored healthy. **Because Action affects rendered `U₃`, the band-centred normalization is applied to the Action pillar now**, not deferred with currencies 4–5.

**Architectural consequence.** A two-sided currency uses a **band-centred score** — `s = 1` inside the healthy band `[o_lo, o_hi]`, falling toward 0 on *both* sides (trapezoid, or Gaussian in distance-from-optimum), the band a per-cell-type provenance-tagged anchor. **The non-compensatory keystone survives** — either extreme drives the score → 0, zeroing the term and hence `U` — only the *shape* of the normalization changes, which is exactly why P0b perturbs the functional *form* of normalization (§8.3), not only anchor values.

#### 5.5.6 Commensurability & timescales (two assumptions the product makes)

Multiplying scores into one `U` only means something if two assumptions hold; both worsen at higher N:

- **Commensurability.** The currencies are different *kinds* of quantity (a perfusion distance, an identity-match, an ATP flux, a barrier height, a phase-order parameter). **The normalization is doing all the work of making them multipliable** — so any `U₄/U₅` headline must be robust to the normalization's *functional form* (§5.5.5), or it was a normalization artifact.
- **Timescales.** Coherence runs in **milliseconds**, Action in seconds–minutes, Position-context in minutes–hours, Form in hours–years, Freedom across the lifespan. A single instantaneous `U` conflates them and `ℳ = ∫U dt` risks **aliasing** — hence the **currency-resolved** ℳ of §5.3.

#### 5.5.7 "Coherence", not "Entanglement" — biology populates 4.5 of 5 currencies

Canon's fifth currency is named **Coherence/Entanglement**; **biology gets *coherence*, not *entanglement*.** Classical synchronization (two phase-locked oscillators) is an ordinary product-of-marginals-plus-correlation — no Bell violation, no monogamy, nothing non-classical. No functionally-relevant macroscopic biological entanglement is claimed. Biology therefore **populates 4 of 5 DPR currencies plus a classical coherence analogue of the 5th** — call it **4.5/5**, not a five-currency tally for appearance's sake. The canon label is kept only because the *structural role* (a relational, between-parties order, conditionally protected, §5.5.3) is the same role entanglement plays in QTC — **the label tracks the ledger position, not shared physics.** Reading it as "biology is quantum-entangled" is the level-inflation §9.2 exists to stop; logged as overclaim **O9**, and **the entanglement reading renders no number** (§9.7).

---

## 6. The AI / Digital-Twin Control Loop

### 6.1 The four agents (TAA)

- **Form-Agent** → encodes `h_f` from genome/epigenome/proteome.
- **Position-Agent** → encodes `h_p` from compartment/niche/context (owns relation-graph reasoning).
- **Action-Agent** → encodes `h_a` from flux/function/energy.
- **Generalizer Σ** → fuses the three, computes the admissibility gate `g(f,p,a)`, names the weakest pillar, recommends intervention.

> **Honest idealization, and its limits.** "Each agent sees only its axis" is an *informational* design choice, not a claim the biology is separable. The siloed-agent test is a **secondary diagnostic, not the definition of separability** (M-9): low siloed performance could mean *noisy proxies*, not entangled axes. The **primary** separability test is conditional-incremental-information (does a pillar add held-out variance *given* the other two, §8.3), not agent performance.

### 6.2 The digital twin — research-grade, not runnable now

The twin holds the entity forest plus per-entity state in three coupled layers: **Action** (FBA on Recon3D + ODE kinetics), **Position** (reaction-diffusion / agent-based niche field of O₂, morphogens, ECM), **Form** (slow damage, repair, epigenetic drift). It is intended to reproduce aging (rising δ) and cancer (δ-spike) via `dδ/dt = k_entropy − k_repair·U`.

> **Downgrade (M-3).** The coupled three-layer *dynamic* twin is **research-grade, NOT runnable now.** Organism-scale coupled dynamic-FBA + reaction-diffusion + slow-damage with calibrated cross-layer constants **does not exist**: the RD diffusion/consumption constants are unmeasured at per-cell-type resolution; the `dδ/dt` law has **no source for its rate constants** (free parameters); the layers span the ms-to-years timescales §5.5.6 flags as un-co-integrable; and **atlases are snapshots, not trajectories — you cannot calibrate a dynamic twin from snapshots** (§8.4-4). What **is** runnable is the **KG + static per-node scoring** (§3-B). The dynamic twin's trajectories are **illustrative, not validated**; its cross-layer coupling constants and their (absent) data sources are declared, and the multiscale integration scheme is stated as future work. **The twin is a simulation, not a person; nothing in it is live physiology (§9.3-O7).**

### 6.3 The LGP-12 loop

```
LGP-1  SCAN       twin emits (F,P,A)_e per entity; U₀,δ₀,SI₀ per node and organism
LGP-2  DETECT     Problem set 𝒫 = {e : SI_e < θ_tissue}; instability weight w_e   ← WEAK-ZONE SCAN
LGP-3  DECOMPOSE  per zone: deficits d_F,d_P,d_A; DominantAxis = argmax (GATED HYPOTHESIS, §2.5)
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
| **Action (function/energy)** | function / energy-reset | metabolic reprogramming, mTOR modulation, anti-inflammatory reduction, ion-pump support |
| **Coupling (δ high)** | re-coupling / combination | combination triad therapy (predicted superadditive — a HYPOTHESIS); twin tests a 2×2×2 factorial in-silico first |

**Anomaly = disallowed action / wrong position = pathology — with the open-world guard (§4.3).** Pathology is "an edge the atlas *forbids*," never "an edge the atlas *didn't happen to sample*." An action merely *absent* from the atlas is `UNKNOWN`, not pathology.

### 6.5 Learning across cycles (GSI-RTD §26)

- **Impact (empirical Bayes):** `impact^(g+1) = (1−λ)·impact^(g) + λ·observed_ΔSI`, λ=0.3.
- **Weights (gradient-free):** `w_j^(g+1) = w_j^(g) + α·corr(contribution, ΔSI)`.
- **Exploration:** ε-greedy (cycles 1–5) → UCB1 (6–20) → Thompson (20+); plus AD-RTD anti-bias ε≈10% random Form/Position variants.
- **Cross-domain transfer (Prop 26.1):** `impact_new = β·impact_source + (1−β)·prior`, `β = (cosine-F + subgraph-iso-P + jaccard-A)/3` — structural isomorphism, not assumed analogy. Transfer must beat cold-start (§7, P3 gate).

### 6.6 Safety gate

Any irreversible call (gene edit, ablation) must pass **SSS-Guard**: 3 independent SSS instances; accept only if ≥2 agree within tolerance **and** the verdict agrees with an **external** biological/clinical outcome metric. Never act on a single SSS verdict. If no feasible queue raises organism U above threshold within budget, the engine returns `DECOMPOSE_FURTHER` rather than emit a false plan. **There is no autonomous biological action of any kind (§9.6-6); SSS-Guard governs *simulated/recommended* actions only.**

---

## 7. Phased Roadmap (Pilot → Whole Organism)

Each stage is gated by the *prior* stage passing its falsifiers. **Phase 0 is mandatory** — the two experiments that must run *first*. The "status" column means **data availability**, *not* greenlit: every "data available" row below P0 is **conditional on P0 passing**.

| Phase | Scope | Key deliverables | Gate to advance | Data status |
|---|---|---|---|---|
| **P0 — Foundations & go/no-go** | one tissue slice | **(a) Orthogonality / pillar-separability ablation** (§8.3) — are F,P,A separable in real atlas data? **(b) Anchor-robust geometric-vs-arithmetic test (P0b)** — does geometric U beat the arithmetic mean *and survive anchor value + form perturbation*? **(c) feature-leakage + shared-upstream-feature audit** | **If F/P/A are collinear (likely) OR the geometric win is an anchor artifact → STOP and report the negative.** Otherwise proceed | **data available — but see M-1: may be UNDERPOWERED at donor n; run the power calc first** |
| **P1 — Cardiac LV pilot** | LV, ~11 cell lineages, depth-2 | TB-KG slice; per-node U/δ/SI; ranked weak-zone list; ischemia example | P2-mech pre-registration met **and** retrodiction V1 passes | data available (cond. on P0) |
| **P2 — Whole heart** | 4 chambers + conduction + vessels | recursive `U_org` roll-up (serial/parallel-aware §5.2); organ-outcome classifier | organ AUC ≥ 0.70 vs HFrEF | data available (cond. on P0) |
| **P3 — Multi-organ** | + lung (HLCA) + kidney (KPMP) | cross-organ transfer (β); transfer must beat cold-start | transfer beats cold-start | data available (cond. on P0) |
| **P4 — Inter-organ coupling** | heart–kidney axis; immune system as cross-cutting Position **overlay** (lattice, not tree) | inter-organ weak zones (cardiorenal) *emerge* from aggregation | emergent coupling reproduced | partial data |
| **P5 — Whole-organism dynamic** | HCA-v2 abstracted to 10³–10⁴ system nodes | navigable weak-zone map; `U_org(t)`, `ℳ_org`; budgeted scheduler | **adversarial planted-lesion recall (below) + prospective causal evidence (V3) on ≥1 prior stage + SSS-Guard ensemble** | **not runnable; research-grade** |

**Tree-vs-lattice limitation, stated not hidden.** The recursion (`3^d`) and geometric roll-up assume `PART_OF` is a **tree**. The immune system and microbiome are **mobile, global, lattice-structured** — *part of* many tissues at once — so they are modeled as a **cross-cutting overlay** connected by explicit edges (§4.3); their influence enters via edge-weighted context (§5.2), not by pretending they sit in one tree location. Organism-level roll-up over the overlay is approximate; any weak-zone claim depending on it is tagged `LATTICE_APPROX` and held to a higher evidence bar.

**P5 falsifiability — adversarial planted-lesion recall (M-10).** The Scheduler-Sufficiency Conjecture is open, and a missed weak zone can always be blamed on an omitted node. The coverage-saturation criterion (`∂Coverage/∂n < ε`) only tests whether *adding* nodes stops changing coverage — it is **silent about excluded zones**. P5's falsifiability is therefore restored by a **planted-lesion recall test**: hide a known clinically-important vulnerable cell type from the scan's node set and verify the leverage ranking **degrades measurably** — real recall on planted ground truth, not internal convergence. If recall fails, P5 is reported not-yet-validatable.

---

## 8. Validation & Falsifiable Predictions

Validation binds model outputs to an **independent** ground-truth modality. The central trap is **circularity** — never validate against a label derived from the same data that produced the score, and never trust an axis whose proxy is downstream of (or computed from) another axis (the Vₘ error and the FBA-from-Form confound).

### 8.1 Evidence bars

- **V1 — Retrodiction:** low-U cells coincide with known disease-vulnerable ones. Runnable now.
- **V2 — Blind prediction:** U on *healthy baseline* predicts which cells degrade under a *held-out* stressor. Runnable now (ischemia time-courses, Sci-Plex, doxorubicin atlases).
- **V3 — Prospective causal:** stabilizing the prescribed weakest pillar raises real resilience. **Not runnable by this plan's compute** — needs a wet-lab collaborator or in-silico causal-surrogate; designable, not executable here.

### 8.2 The falsifiable predictions

> **All independence/separability thresholds below are stated on the chosen normalized dependence statistic — distance correlation (dCor) or normalized conditional mutual information (CMI), computed on CLR/ILR features, in conditional form — NEVER on Pearson |r|** (§8.5 rejects |r|; the earlier draft's |r| thresholds are removed). The estimator, k-NN/bandwidth settings, CLR composition, and feature set are pre-registered (§8.5), because these thresholds are estimator-dependent in a way Pearson *r* is not. Every threshold is tied to a stated minimal meaningful effect + power at realistic **donor** *n* (§8.5-R8), or pre-registered fixed with a ±50% sensitivity analysis.

| # | Claim | Falsifier (on dCor/CMI, conditional, donor-level) | Pre-registered success | If falsifier fires |
|---|---|---|---|---|
| **P0** | F, P, A carry **conditionally independent** information on real atlas data | any pillar's conditional dCor/CMI given the other two is **near zero** (it adds no information), **or** pairwise dCor sits in the pre-committed **0.6–0.8 "inconclusive" band** at the achievable donor *n* | each pillar adds conditional dependence with a CI **below 0.6** *and* adds held-out predictive variance for an external fragility outcome given the other two | **STOP** — non-compensation has no independent inputs; report the negative (§1) |
| **P0b** | Geometric U beats arithmetic mean **robustly** | win disappears under ±20% anchor-value **or** ramp↔logistic↔trapezoid form perturbation | geometric beats arithmetic across the full anchor-value *and* anchor-form envelope | geometric aggregation **retired** as an anchor artifact in biology |
| **P0c** | DepMap/gnomAD truth is independent of Form inputs | leakage audit shows essentiality/constraint is recoverable from the same expression features that feed Form | truth features pass the leakage audit (no recovery from Form inputs) | that "truth" is unusable; find an independent outcome |
| **P1** | Lowest baseline `SI` cell type = cell lost earliest in ischemia (vCM) | baseline SI ranks vCM in the *most-stable* tertile | Spearman ρ ≥ 0.5, p < 0.05 | retrodiction fails; P1 not passed |
| **P2-mech** | The weakest *pillar* names the *mechanism* — **gated by P0 + proxy-axing (§2.6)** | vCM's lowest pillar is Form while measured Action scores high; or the axis-label **flips** under documented proxy reassignment | mechanism map matches expert pre-registration **and is stable under the enumerated proxy-reassignment set** (a stability statistic with a pass threshold, §8.5) | **mechanism-localizer RETIRED** from the delivered feature set (§9.8); reverts to "δ-spike, axis TBD" |
| **P3** | Low baseline-SI leaves degrade most under a **held-out** stressor (blind, OOD) | no monotone SI→damage relationship | negative slope, R² ≥ 0.3 beyond a marker-count null | predictive claim not supported |
| **P4** | Recursive `U_LV` tracks organ-level clinical class (HFrEF vs healthy) | failing hearts score ≥ healthy | classifier AUC ≥ 0.70 | roll-up not validated at organ scale |
| **P5** | Prescribed weakest-pillar intervention raises resilience > control | *(V3 — deferred; designed, not run)* | pre-registered, requires collaborator | — |

### 8.3 Baselines & the two decisive tests (run FIRST, in Phase 0)

The triad must beat non-trivial baselines: **B0** random, **B1** marker-count/library-size, **B2** single-pillar (Action-only), **B3** arithmetic mean `(F+P+A)/3`, **B4** generic anomaly score.

1. **Separability — the decisive gate is *conditional incremental validity* (M-1).** Pairwise low input-dependence is **neither necessary nor sufficient** for non-compensation to be useful. So the *necessary screen* is the pairwise dCor/CMI test (P0), but the **decisive** test is: does each pillar add **held-out predictive variance for an independent fragility outcome, given the other two**, with the FBA confound and the leakage audit controlled? The **shared-upstream-feature audit** (trace every proxy to raw measurement; flag annotation-derived values; score from disjoint raw feature sets) runs here. **FBA-derived Action and CytoTRACE-derived Freedom are EXCLUDED from the input-independence claim** (B-2): either restrict Phase-0 Action to **measured** Action (Seahorse/respirometry/metabolomics) where it exists, **or** prove input-independence by showing FBA flux predicts held-out *measured* flux better than expression alone on the same cells. *If F/P/A are collinear — likely — the architecture has no independent inputs to be non-compensatory over: the most valuable possible negative.*
2. **Anchor-robust geometric-vs-arithmetic (P0b).** Geometric and arithmetic means diverge *only* near a collapse anchor; anchors are hand-fit, so a naive "geometric beats arithmetic" win could merely reflect anchor placement *or band shape*. **P0b counts only if it survives perturbation of `ref_lo`/`ref_hi` (±20%) AND of the functional form of the normalization** (ramp ↔ logistic ↔ trapezoid).

Only if P0 and P0b pass does "geometric U beats arithmetic" become meaningful.

### 8.4 Honest data gaps

1. No cell-type-resolved gold-standard "fragility" label exists; truth is assembled, ordinal, noisy → caps achievable ρ (hence the modest ≥0.5 thresholds).
2. **(B-2) The Action↔Energy axis — declared the most important pillar — has essentially no per-cell measurement.** Single-cell respirometry does not exist at atlas scale; **context-specific FBA is a *model output computed FROM the transcriptome*** (Form's data) via GIMME/iMAT/tINIT/Compass — so an FBA-Action × expression-Form product is *a number multiplied by a transform of itself*, broken **by construction**, not merely correlated. A dCor/CMI test can *pass* while the two are one axis transformed twice (a lossy LP bottleneck hides functional dependence). Hence FBA-Action is excluded from the separability claim and the test is also run on a **measured-only Action subset** where respirometry exists.
3. The Position graph (CellPhoneDB) is *inferred* from co-expression, not a measured physical relation; per-cell perfusion/pO₂ is not single-cell-resolved (§5.4 ischemia rider).
4. Atlases are snapshots, not trajectories; **a dynamic twin cannot be calibrated from snapshots** (§6.2 downgrade).
5. **External "truth" may leak into Form:** DepMap essentiality and gnomAD constraint correlate with broad/high expression, which feeds Form. A **feature-leakage audit is mandatory (P0c)** before either is used as truth.

### 8.5 The optional currencies (P7, P8), the statistical protocol, and the canon L-mapping

The five-currency completion (§5.5) earns its place only if the two added currencies pass the *same* independence / non-circularity bar as F/P/A. Two pre-registered predictions, each with a **retirement consequence**:

| # | Claim | Falsifier (dCor/CMI, conditional, donor-level) | Pre-registered success | If falsifier fires |
|---|---|---|---|---|
| **P7 (Freedom — the admission gate for U₄)** | Freedom (potency / reprogramming-barrier / telomere reserve) carries information **independent of Form-identity** | the reprogramming-barrier proxy is fully predicted by identity proxies (conditional dCor/CMI ≈ 0), **or** pairwise dependence in the 0.6–0.8 band at achievable donor *n* | double-dissociation holds — at matched Form-identity, stem vs terminally-differentiated cells separate on Freedom (conditional dependence CI **below 0.6**); barrier-height adds held-out variance beyond identity | **Freedom REMOVED from the ledger and from §5.5; U₄ never rendered** (§9.8) |
| **P8 (Coherence — the admission gate for the coherence roll-up term)** | System function depends on a Coherence order parameter (Kuramoto *r*) **not recoverable from the mean of per-node F/P/A**, gated by a coupling-vs-heterogeneity threshold | tissue function fully predicted by mean per-node U with *no* added variance from *r*; **or** no synchronization transition exists in the coupling–heterogeneity plane | *r* explains held-out variance in conduction/contractile output beyond mean-U (**ΔR² ≥ 0.1, CI excludes 0, at the real heart-level donor *n***); a Kuramoto transition is reproduced; **early fibrillation flagged as Coherence collapse — system output below the floor predicted by aggregated per-node F/P/A while individual-cell A stays above zero** | **Coherence term REMOVED from the roll-up; U₅/r-verdict never rendered** (§9.8) |

**P8 is the cleanest non-circular test in the appendix** (fibrillation is invisible to per-node scores by construction, so any lift from *r* cannot be a relabelling) **— but only in electrophysiological tissues (heart/brain)**, and the **three-modality independence** below is mandatory or it re-closes its own circle. **P7 is runnable** on potency/reprogramming atlases with the §8.4 leakage audit applied to the potency proxy (potency correlates with proliferation, which feeds Action).

**P6 (X) is a separate downstream claim, NOT the U₄ admission gate (M-4).** P6 asks whether, under infection, U₄ declines *before* structural Form damage — a **time-ordering** test about infection dynamics. **It does not admit U₄ to rendered numbers; P7 (independence) does.** P6 runs only on modalities that carry X-proxies (population/bulk/live-imaging, §2.4), and a failed P6 retires *the infection-dynamics claim*, not the Freedom currency itself (which is governed by P7).

**Statistical protocol for P0/P7/P8 (hardened).**

1. **Nonlinear, conditional dependence — never Pearson *r*.** Use distance correlation (dCor) or (conditional) mutual information / HSIC, framed as *conditional* redundancy (does pillar X add information *given* the others?). The `< 0.6 / > 0.8` thresholds are restated on the **normalized** dependence statistic; the **0.6–0.8 band is pre-committed as "inconclusive → never reported as a pass."**
2. **Compositionality.** F/P/A proxies from one scRNA matrix are compositional (shared library-size constraint) — manufacturing spurious correlation. Dependence is computed on **CLR/ILR-transformed** features. **Pre-register the CLR composition, zero-handling/pseudocount, and a positive control** (a known-independent and a known-redundant feature pair) — CLR/dCor inherits the arbitrariness of the reference set, a p-hacking surface.
3. **ΔR² (P8) via a proper nested-model test.** The bar is *out-of-sample* improvement of (mean-U + *r*) over mean-U, with a **permutation null** (shuffle *r* against outcome) and **ΔR² reported with a CI**. **Three-modality independence is mandatory:** the coupling *source* (gap-junction expression), the *r* *measurement* (optical mapping / ECG synchrony), and the *function outcome* (ejection fraction) must come from **three independent modalities**.
4. **Unit of independence = the donor, not the cell (pseudoreplication).** Cells within one donor share batch/genotype/microenvironment; treating 10⁴–10⁶ cells as independent **manufactures false confidence**. The independent unit is the **donor / preparation / heart** (atlases supply *tens*). Dependence and ΔR² use a **hierarchical / mixed-effects** model; power *n* is the donor count.
5. **Power calc before the test, and honour a null (M-1).** Compute the expected CI width on the dependence statistic at realistic donor *n*; **if it cannot exclude the 0.6–0.8 dead zone, the test is declared *underpowered* → "not yet decidable,"** never a borderline pass. **This is run for P0 now:** state the minimum donor *n* at which a dCor/CMI CI excludes both 0.6 and 0.8, and whether any existing atlas supplies it. **If none does, P0 is "currently underpowered — the foundational test cannot yet be run,"** and the *decisive* gate is the conditional-incremental-validity test (§8.3-1).
6. **Study-level multiplicity.** Beyond the per-node FDR (§5.4), declare the **full family** of tests (P0–P8 × tissues/atlases) up front and **control FDR across the battery** — the look-elsewhere logic applies to the test suite too.

**Canon L-level mapping (for corpus filing) — quoted verbatim from RH_CRITICAL_REVIEW §71–75.**
Canon's ladder is: **L0 = Meta-evaluation · L1 = Operational stability · L2 = Cross-domain analogy · L3 = Cosmological extension · L4 = Literal physical claim.**

| Content | Project level | Canon level |
|---|---|---|
| "Form↔Time / Position↔Space / Action↔Energy is the deep structure of life"; "biology is triadic/pentadic" | B0 / INTERPRETATION | **L0** (Meta-evaluation / framing) |
| `U=∛(FPA)`, δ, SI, the aggregation theorems — true *of the model* | B1 | **L1** (Operational stability) |
| The F/P/A→biology mapping; the optional five-currency completion (§5.5) | B2 | **L2** (Cross-domain analogy) |
| Every weak-zone / mechanism / prediction output (P0–P8) | B3-pending | a *narrowing* of **L2→application**; **never L3** |
| Any clinical claim | B4 (empty) | **L4 — outside this appendix** |

**No statement in this appendix occupies canon-L3 or L4.** The B1→canon-L1 mapping uses canon's real definition (Operational stability), not "within-model proof."

---

## 9. RH Discipline — Scope, Limits, Ethics, Non-Goals

### 9.1 The central cut: Testable vs Interpretation

The triad is an **accounting frame and decision-support search heuristic**, not an ontology of life and not a health meter. Two strictly separated registers, enforced in code:

- **TESTABLE** — statements about what *our model does* over biological data, admitted only with an operational procedure, a falsifiable prediction, and an external ground-truth metric.
- **INTERPRETATION** — framing/metaphor ("Form↔Time is the deep structure of life," "metabolism pays a 4th currency"). May generate hypotheses and label axes; **no number, verdict, or colour rendered to a user may be in INTERPRETATION language.** The UI prints "model fragility index for entity-type X, model-internal, not a clinical measurement," never "X's stability is 0.41."

### 9.2 Epistemic ladder — B0–B4, mapped to canon's real ladder

Canon RH fixes **L0 = Meta-evaluation, L1 = Operational stability, L2 = Cross-domain analogy, L3 = Cosmological extension, L4 = Literal physical claim** (RH_CRITICAL_REVIEW §71–75). Re-using L0–L4 with biology-specific meanings would be exactly the level-inflation RH exists to prevent. **TRB therefore uses its own ladder B0–B4** and states the mapping explicitly:

| Project level | Meaning | Maps to canon |
|---|---|---|
| **B0** | metaphor / framing | canon **L0** (Meta-evaluation / framing) |
| **B1** | proved-within-the-model's-axioms (true of the *model*) | canon **L1** (Operational stability) |
| **B2** | bridge-to-biology, plausible (every empirical biology claim is at most this) | canon **L2** (Cross-domain analogy) |
| **B3** | application/measurement: testable over data, **pending** (project ceiling) | a *narrowing* of canon L2→application; **not** canon L3 |
| **B4** | clinically validated (prospective, controlled, replicated) — **currently empty** | a regulated claim *outside* this plan |

**Project ceiling: B3-pending.** Every emitted artifact carries a `level` tag; the renderer refuses any claim whose wording exceeds its tag. **Any B4 sentence is a bug.** Under canon's ladder essentially every empirical statement here is L2 — the rename keeps that honest instead of inflating biology claims into canon's cosmology tiers.

### 9.3 Named overclaim risks (each pre-empted)

- **O1** "It measures health/vitality/consciousness" — banned-output lexicon for any field ≤ B3.
- **O2** "Low U = the patient is unstable/dying" — every U ships with `evidence_confidence`; low-evidence scores are "not interpretable."
- **O3** "It diagnoses / treats / replaces clinicians" — confined to entity-type/mechanism level; recommendations address **researchers about mechanisms**, never patients/HCPs about a named individual.
- **O4** "The triad is proven biology" — B2 tag + "competing decomposition exists; separability untested until §8.3."
- **O5** "Higher U = a better/worthier organism" — **the eugenics attractor.** U is never computed across persons, never used to compare organism worth. *Divergence from SSS, on purpose:* APPENDIX_SSS *does* score and rank a named individual and sells cross-system comparability; **TRB deliberately diverges from SSS here** to avoid the eugenics attractor — this is not inherited, it is a chosen break.
- **O6** "The AI jury is objective" — consensus measures *agreement*, not correctness; always reported beside external ground truth.
- **O7** "It models the body dynamically in real time" — "dynamic" = across simulated trajectories, never live physiology; and the dynamic twin is research-grade (§6.2).
- **O8** "The weakest pillar names the disease mechanism" — a **gated hypothesis** (P2-mech), reported with the caveat that re-axing a proxy can flip the label, and **retired if its gates fail** (§9.8). Until P2-mech passes with proxy-reassignment stability, it is INTERPRETATION.
- **O9** "Biology is quantum-coherent / entangled" — the Coherence currency is **classical** inter-node synchrony (Kuramoto *r*); the *entanglement* half of canon's currency name has **no established multicellular referent and is not claimed** (§5.5.7). Any quantum-biological reading is banned-output lexicon and renders no number.

### 9.4 Regulatory boundary — stated as INTENT, not settled fact

**Triadic Biology is designed to be research-use-only:** not a medical device, not diagnostic software, not clinical decision support; no diagnosis/treatment/prognosis for any individual; recommendations addressed to researchers about mechanisms. **However, classification is not self-determined.** Correct framing: *"We **intend** RUO and have **designed** to stay outside even FDA Non-Device CDS; whether a regulator agrees — especially once a weak-zone map is keyed by cell × location and ranks interventions — is adjudicated case-by-case, not by us."* Any flat assertion that it "falls outside" regulation is itself an overclaim and is withdrawn. Rules unchanged: no individual diagnosis; RUO banner on every artifact; human-in-the-loop and human-on-top; no emergency/triage/monitoring pathway. Any future intent to inform individual care is a **new project at B4** with prospective trials, IRB, and the appropriate SaMD/CDS pathway.

### 9.5 Data ethics, privacy & dual-use — the deny-list is necessary but NOT sufficient

Public ontology/literature first (CL, UBERON, Reactome, GO, BioGRID/STRING). Provenance mandatory: every principle carries accession + version + date; unsourced principles are B0 and cannot enter scoring. If non-public human data is ever used: de-identification (HIPAA Safe Harbor / GDPR), consent + IRB, never used for individual care, never sent to external model APIs, minimized and not persisted.

**Dual-use — stated honestly, not solved.** A "find the weakest pillar of the weakest node and the cheapest flip" engine is a **destabilization-target finder with the sign flipped** — the *stabilization* and *weaponization* computations are the same; the fragility map is the dual-use artifact *regardless of stated objective*. An objective deny-list is **necessary but not sufficient** (it constrains objectives, not outputs). Controls: (a) deny-list + human-review gate; (b) **fragility maps for pathogen-targeting-of-hosts are not produced or released**; (c) access to ranked organism-level fragility outputs is gated and logged; (d) residual risk is acknowledged in writing. Permitted polarity is **stabilization of beneficial systems and study of pathology**, never weaponizable destabilization.

**The optional five-currency extension widens the dual-use surface.** A **Coherence** target is a *desynchronization* weapon (induced fibrillation/seizure); a **Freedom** target is *forced de-differentiation* (oncogenic). These are **more** concerning for one structural reason central to this plan: **coherence attacks are cheap near criticality** — a small, well-timed perturbation desynchronizes a coupled system sitting just above its Kuramoto threshold, so the cost-to-destabilize collapses exactly where the system is most ordered. The §9.5 controls extend to currencies 4–5: **no released artifact ranks desynchronization or de-differentiation targets**, criticality-proximity is treated as sensitive, residual risk acknowledged.

### 9.6 Explicit NON-GOALS

1. Not a diagnosis/prognosis/treatment recommender for any individual.
2. Not a measure of health, wellness, vitality, fitness, life/death, or consciousness.
3. Not a real-time physiological simulator (no live monitoring).
4. Not an organism/person ranking or worth metric (no cross-individual U).
5. Not a proof that biology is triadic (chosen, non-unique frame; separability untested until §8.3).
6. Not autonomous (no closed-loop action on any biological/clinical system).
7. Not a replacement for clinicians, biologists, lab validation, or regulatory review.
8. Not a source of B4 claims until prospective, controlled, replicated validation exists.
9. Not a destabilization / weaponization tool — including the desynchronization (Coherence) and forced-de-differentiation (Freedom) surfaces, **especially the cheapness of coherence attacks near criticality** (§9.5).
10. Not a universal-constant engine — 0.618 and every anchor are tunable, domain-calibrated defaults, not laws.
11. **Not a mechanism-localizer until P2-mech passes** — "the weakest pillar names the mechanism" is a gated hypothesis, retired if its gates fail (§2.5, §9.8).

### 9.7 Mechanizing the discipline

Every emitted item is a **claim envelope** `{register, epistemic_level B0–B4, text, value, evidence{n_valid_models, consensus_pct, mode}, provenance[], external_ground_truth{metric, value, agreement}}`. An **output lint** rejects: any claim above B3; any ≤B3 claim using the banned lexicon (health/diagnose/treat/conscious/…); any decision-grade B3 claim lacking an external metric or <2-of-3 SSS-Guard agreement; any cross-person aggregation; any deny-listed destabilization target. The weak-zone scan emits each flag as a **research hypothesis** (`"model flags {node} weakest on {pillar}; HYPOTHESIS for study; mechanism-axis conditional on proxy-axing"`), tagged `low_score_cause ∈ {evidence_sparse, genuinely_imbalanced, lattice_approx}` — only `genuinely_imbalanced` is a candidate biological hypothesis. Additional clauses: (i) any rendered number/verdict for **currencies 4–5** (`U₄`, `U₅`, an *r*-derived verdict, a Freedom/Coherence score) is rejected until **P7 / P8** pass, **and is permanently rejected if P7/P8 fail** (§9.8); (ii) the **entanglement** reading of the Coherence currency is banned-output lexicon (O9) — biology's fifth slot renders only as classical *coherence*; (iii) every weak-zone flag carries a **multiplicity-corrected q-value** and clears an absolute verdict band, or is emitted as "not distinguishable from scan noise."

### 9.8 The symmetric retirement rule (a failed falsifier REMOVES a claim)

Deferral-to-a-falsifier is only honest if a *failed* falsifier costs something. The INTERPRETATION register cannot be an unfalsifiability shield where a claim parks forever. Therefore, for **every** gated claim, the pre-registration names what a *failed* falsifier **RETIRES**, not only what a passed one admits:

| Gated claim | Gate | Pass → | **Fail → REMOVE** |
|---|---|---|---|
| Mechanism-localizer ("weakest pillar names the mechanism") | P0 + P2-mech | delivered, gated feature | **removed from delivered features; reverts to "δ-spike, axis TBD"** (§2.5) |
| Geometric > arithmetic aggregation in biology | P0b | kept as the engine's core | **retired as an anchor/form artifact in biology** (§8.3) |
| Freedom / Irreversibility currency (`U₄`) | P7 | admitted to rendered numbers | **removed from the ledger and from §5.5; U₄ never rendered** |
| Coherence currency (roll-up term, `U₅`/r-verdict) | P8 | admitted to the roll-up | **removed from the roll-up; r-verdict never rendered** |
| 4th-currency infection-dynamics claim ("X declines before Form damage") | P6 | infection time-ordering supported | **infection-dynamics claim removed** (does *not* govern Freedom admission — that is P7) |

A claim whose gate fails is **deleted from the ledger and the renderer**, logged in `TRB-CHANGELOG` as a retired claim. This is the move that converts the apparatus from "an elaborate frame erected on a precondition the authors expect to fail" into a falsifiable program whose value does not depend on that precondition holding.

---

## 10. Cross-appendix coherence (consistency checks against the corpus)

Triadic Biology is filed as a sibling to the corpus's other applications, required to be *consistent with their hard-won lessons*, not merely to reuse their vocabulary.

- **vs. APPENDIX QTC.** QTC established that (i) a triadic framing can be *imposed* on a substrate whose protected structure is lower-dimensional (the validated DFS code is **dyadic**, not triadic), and (ii) coherence protection is *noise-symmetry-gated* (**R ≈ 0 under native independent noise → R = +0.97 under collective-symmetric noise**; QMC §184 / QTC §8.3, accession `IBM/qtc_hw_collective_marrakesh.txt`). The structural lesson transfers — biology's "are F/P/A even separable?" *is* QTC's imposed-vs-derived question, and biology's coherence is threshold-gated as QTC's was symmetry-gated — but **it does not transfer *verbatim*** (quantum/symmetry vs classical/threshold). Consistency requires TRB *test* separability and threshold-gating rather than assert them — which Phase 0 and P8 do.
- **vs. APPENDIX QMC.** QMC's E/O fork separates *epistemic* from *objective* interpretations, refusing to let interpretation masquerade as mechanism. TRB's TESTABLE-vs-INTERPRETATION cut (§9.1), with the rule that *no rendered number may be in INTERPRETATION language*, is the same discipline at the output boundary. The optional currencies sit on the INTERPRETATION side until P7/P8 pass — or are retired (§9.8).
- **vs. GSI-RTD.** Biology implements the `TriadicDomain` interface (§A.3); it is a *conformant domain*. Consistency check: every capability is expressible through `embed_form / build_position_graph / enumerate_actions / execute_action / evaluate_sss`.
- **vs. NDT — TRB AMENDS NDT (does not "obey" it).** Biology is canon's clearest worked example that N-adic lifting is substrate-dependent — but TRB's two findings are **amendments**, not conformance: (a) lifting is **non-uniform** (Freedom is per-node, Coherence is aggregation-level), so NDT-1's uniform per-node `U_N` must be revised; (b) TRB populates the 5th slot via **classical** Kuramoto coherence, where **NDT reserves the 5th for quantum substrates** ("nothing classical can") and places biology at N=4. TRB therefore touches a classical coherence analogue of the 5th slot, and **NDT and TRB disagree on whether biology can reach the 5th slot at all** — logged for NDT maintenance.
- **vs. UCT.** TRB contains **no "proof" of anything about biology** — only within-model theorems (B1), bridges (B2), and pre-registered predictions (B3-pending). "Proof" is reserved for the model's own algebra.

**Net.** The appendix's epistemic posture *is* the corpus's — *try to kill the load-bearing assumption first* — applied to a substrate where that assumption (orthogonal F/P/A) is, if anything, **less** likely to hold than in governance. That is why the runnable separability and coherence tests (P0/P0b/P8) are the product, and the five-currency completion is offered as an optional B2 bridge that is *retired* if its falsifiers fail.

---

## 11. Glossary

| Term | Definition |
|---|---|
| **F / P / A** | Form (structure/identity, ↔Time), Position (locus `q` + context `c`, ↔Space), Action (function + energy-maintained order incl. Vₘ, ↔Energy) — the three candidate orthogonal axes (separability tested, §8.3). |
| **U** | `∛(F·P·A)` — non-compensatory geometric stability score; any pillar → 0 ⇒ U → 0 (canonical SSS keystone). |
| **δ (delta)** | `(max−min)/(max+0.01)` — *intra-node* pillar imbalance; high δ = decoupling. **TRB-introduced derived primitive.** |
| **SI** | `U/(1+δ)²` — imbalance-penalized Stability Index; bands 0.38 / 0.618 (tunable). **TRB-introduced derived primitive.** |
| **X (4th axis / Freedom)** | Optional Freedom/Irreversibility slot (NDT N=4); `U₄=(FPA·X)^¼`. Proxy: developmental potency / reprogramming-barrier height / telomere & repair reserve. **Admission gated by P7 (independence); removed if P7 fails. P6 = a separate infection-dynamics claim, not the admission gate** (§2.4, §8.5, §9.8). |
| **Coherence (5th slot, classical)** | inter-node synchrony holding parts as one system; an **aggregation-level** quantity, *not* a leaf pillar (a naive `U₅` is a category error). Distinct from intra-node δ. Proxy: **Kuramoto *r***, conduction synchrony, EEG phase-locking. **Admission gated by P8; removed if P8 fails. Admissible only where a parent-level order parameter is measured (heart/brain), else UNKNOWN** (§5.5.2, §9.8). Biology gets *coherence*, **not entanglement** (§5.5.7). |
| **ℳ (Meaning)** | `∫ U_org dt` (currency-resolved over mixed timescales) — accumulated model-internal stability; a coverage indicator, never a worth rank. `ℳ + 𝒮 = T`. |
| **Weak-zone scan** | Locate lowest-SI nodes and rank by leverage (`ΔMeaning / ∛cost`), with donor-preserving empirical-null + FDR/q-value control (§5.4). |
| **Weakest pillar** | `argmin(F,P,A)` — the targeted axis; **names the mechanism only as a gated hypothesis (P2-mech), retired if its gates fail** (§2.5, §9.8). |
| **Non-compensatory** | A strong pillar cannot rescue a collapsed one; geometric mean + δ enforce this. |
| **AND/OR aggregation** | Serial subtrees use weakest-link geometric roll-up; parallel/redundant pools use reserve-aware OR (graceful degradation) — brainstem vs nephrons (§5.2). |
| **BioSystem** | The universal recursive node type: `F{} P{} A{} G{} + state s`. |
| **TB-KG** | Triadic Biological Knowledge Graph — typed property graph of BioSystems + single-axis-labeled edges. |
| **Open-world guard** | "Absent from atlas" → `UNKNOWN`, never `FORBIDDEN`; only positively-contradicted actions are vetoed (§4.3). |
| **TriadicDomain** | The GSI-RTD interface biology implements (`embed_form / build_position_graph / enumerate_actions / execute_action / evaluate_sss`); biology is a *conformant domain*, not a parallel theory. |
| **Symmetric retirement rule** | Every gated claim names what a *failed* falsifier REMOVES, not only what a passed one admits — a failed gate deletes the claim (§9.8). |
| **Unit of independence / pseudoreplication** | The independent sample for P0/P7/P8 is the **donor / tissue / preparation / heart** (tens), not the cell (millions); power is computed on donor count; underpowered tests are "not yet decidable" (§8.5). |
| **FBA-from-Form confound** | context-specific FBA is computed *from* the transcriptome (Form's data), so FBA-Action is excluded from the input-independence claim; separability uses measured Action where it exists (§8.4). |
| **Canon L0–L4** | RH ladder: **L0 Meta-evaluation · L1 Operational stability · L2 Cross-domain analogy · L3 Cosmological · L4 Literal physical**. Project B0–B4 maps onto L0–L2 only; every empirical biology claim is at most canon-L2 (§9.2). |

---

*Triadic Biology's job is narrow and falsifiable, and its first job is to try to kill itself: prove that Form/Position/Action carry **independent, conditionally non-redundant** information in real data, and that **non-compensatory** geometric aggregation beats arithmetic averaging **robustly to its own anchors and their functional form** — before claiming anything about mechanism or fragility. Those two tests, plus the system-level coherence test (P8), **are** the deliverable. If they pass, scale. If F/P/A aren't separable, or the geometric win is an anchor artifact, the triad in biology is falsified — and we report that as the most valuable result this plan can produce.*

*The optional five-currency completion (§5.5) does not relax this bar — it raises it, and each added currency is **removed** if its falsifier fails (§9.8). Registering biology against canon's currency set gives U-Theory a biological instance of its ledger, but only on the same terms as F/P/A: Freedom as a per-node pillar (P7), Coherence as an aggregation-level quantity (P8), each admitted to rendered numbers only after passing an independence/non-circularity test — otherwise reported as a frame biology declined. Biology is an **application** of the framework, never its proof. The most valuable thing biology can tell U-Theory is the same as the most valuable thing it can tell a clinician: where, precisely, the pretty picture stops predicting.*
