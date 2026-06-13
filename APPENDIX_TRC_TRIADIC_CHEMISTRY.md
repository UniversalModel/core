# APPENDIX TRC — TRIADIC CHEMISTRY
### An application of U-Theory to the domain `chemistry.substance` & `materials.system` — a sibling of TRB (`biology.organism`) and TSE (the stabilization-engineering umbrella)

> **CANONICAL HEADER**
> **Appendix code:** TRC · **Corpus:** U-Theory / Universal Model · **Parent record:** DOI 10.17605/OSF.IO/74XGR
> **Author:** Petar Nikolov (ORCID 0009-0001-8669-2276) · **Framework:** U-Theory v26 + v27/v28 appendix series · **Version:** 1.1 (critique-hardened)
> **Canonical triad instantiated:** **Form ↔ Time · Position ↔ Space · Action ↔ Energy** — the v25.2 mirror (Space↔Form / Time↔Position) is **forbidden, per canon §2.1**, exactly as in TRB/TSE. The framework is registered here onto *chemical substance and material* (atom → bond → molecule → phase → formulation → reaction). The governance gloss "Code/Credo/Rights" is **not** carried into the header — it is an L0 metaphor of uneven fit (see §A.1) on which nothing numeric depends, and is deliberately demoted out of the canonical statement.
> **What TRC adds over the parent:** a **new conformant `TriadicDomain` for chemistry and materials** — one recursive `ChemSystem` node type scored `U = ∛(F·P·A)` across four design layers (design, synthesis, use, societal telos), with chemistry-/materials-specific process-intrinsic proxies (DFT formation energy & convex-hull distance, reaction thermochemistry & kinetics, phase/solvation context, Ashby materials-selection) and a chemistry-specific dual-use firewall.
> **Objective instantiated (per single declared node only):** maximize **ℳ = ∫U dt** ≡ minimize **𝒮 = ∫(1−U) dt**; canon fixes **ℳ + 𝒮 = T** (MMT/MPI-1). **ℳ is never summed, compared, or allocated across substance-nodes** — that operation does not exist in TRC (the single canonical statement of this rule lives at §6.4; the renderer enforces it at §9.8 lint-4).
> **Implements:** the GSI-RTD `TriadicDomain` runtime (`embed_form / build_position_graph / enumerate_actions / execute_action / evaluate_sss`); the SSS scoring engine; the **LGP-12** control loop (the L1 design cycle DZ-1…DZ-12); the **SSS-Guard** ensemble gate.
> **Project epistemic ceiling: B3-pending** (canon-L2, never L3/L4). **Two B4 slots — *synthesis-action* and *deployment/societal* — are empty by intent. Any B4 sentence is a bug.**
> **Sibling appendices referenced:** TRB, TSE, SSS, MMT, GSI-RTD, NDT, RH. See §A and §10. (TRC is a **sibling domain appendix** alongside TRB and TSE — a *third* conformant domain registered onto chemistry/materials, not an umbrella over them and not a peer of the engine appendices it consumes.)
> **What this appendix *is* — and is *not* (read first):** TRC is U-Theory **applied to** chemistry and materials. **It is an instance of the framework, not evidence that the framework is true.** Its first job, like every appendix in this corpus, is to try to **falsify its own load-bearing assumptions** — that a substance's (and a route's) Form, Position, and Action carry *conditionally non-redundant* information, and that the non-compensatory geometric `U` beats a property-only, a **constraint-screened Ashby**, and an additive baseline against external ground truth (`E_hull`, ΔH_f, measured yields, recorded service outcomes) — **before** claiming anything about design, synthesizability, selection, or telos.

> **STATUS BANNER — the single canonical statement of scope/maturity/use (carried by reference, not re-typed, on every TRC artifact).**
> **Type:** **Specification** / pre-registration / engineering design + research plan for a triadic chemistry-and-materials stability-scoring and selection engine. **Not** a runtime, dataset, benchmark, validated result, **laboratory protocol**, or chemical/materials device.
> **Maturity: B3-pending.** No deployed engine, no replication, no validation. Every empirical-sounding statement below is *a proposal to be tested*, not a finding.
> **Use: Research use only. NOT a laboratory protocol and NOT actionable synthesis.** Operates on **substance-types, computed/abstract candidates, and simulated digital twins** — never a live process, a controlled procedure, or a fielded part. Produces **no operational synthesis routes, no quantities, no reaction/processing conditions, no fitness-for-service certification, and no diagnosis/prognosis/worth-judgment.** All "design / synthesis / route / make / select / use" language denotes *scoring and ranking of abstract candidates inside a digital twin*, addressed to **researchers about mechanisms, feasibility, and trade-offs** — there is **no actionable wet-chemistry output and no autonomous action**, ever. (Sections below say "RUO" and cross-reference this banner rather than restating it.)
> **Orientation rider (load-bearing — read before any number):** TRC scores the *stability/fit of substances, routes, and uses*. A **high U is good** when the declared `objective_sign = stabilize`; for a `suppress`-polarity node (an unwanted degradation product, a persistent pollutant, an entrenched harmful role) a **high U is the adversary's stability** and is read as bad news. The objective sign is **declared per node by a named accountable human** — the engine never decides what is "beneficial."
> **Honesty contract:** every numeric/verdict claim ships in a **claim envelope** with a B0–B4 level (§9.8); the renderer refuses any wording above its tag. **All worked examples in this document use computed or hand-assigned inputs and are SCORING-MECHANICS ILLUSTRATIONS ONLY — they carry ZERO separability or predictive evidence** (which lives exclusively in the §8 pre-registered tests, run on measured inputs). The fragility/feasibility/selection map is **dual-use**; the *"which substances are beneficial / worth making"* question is the **O5 eugenics-attractor scaled to substances** (O5b-chem), closed at **both** the worth-label and the cross-substance ℳ-allocation level (§6.4). The active "design the most stable matter" voice is **VISION/telos, confined to explicitly-marked VISION blocks**, never a section thesis and never a deliverable.
> **HARD DUAL-USE FIREWALL (single abstract statement; details §6.5, §9.7).** Net-harmful substances are a **TYPE-FORBIDDEN optimization target, not a feature.** TRC's leverage machinery is **sign-symmetric** — the same computation that finds a stabilizing lever would, sign-flipped, find a destabilizing or synthesis-enabling one — and **the sign-flip is prohibited at the objective level and refused at the output level.** No released TRC artifact produces, ranks, or optimizes operational routes, quantities, conditions, or destabilization/diversion targets for any forbidden class. **CWC / BWC / Australia Group / export-control (EU 2021/821) norms are honored as constraints on objectives.** No hazardous recipe, quantity, or condition appears anywhere in this document. The firewall is **necessary but not sufficient; residual risk and its open governance questions are acknowledged in writing** (§6.5, §9.7). To avoid functioning as a design brief for the prohibited capability, this document states the threat once, abstractly, and does **not** gloss *how* a sign-flip would be performed.
> **Symmetric-retirement contract:** every gated claim names *both* what its falsifier admits **and what a failed falsifier RETIRES** (§8, §9.9). A failed gate **removes** the claim from the ledger and the renderer (logged in `TRC-CHANGELOG`); it is never parked in INTERPRETATION forever.

---

## A. Relation to U-Theory canon and to TRB/TSE (placement in the corpus)

This section is what makes the document an *appendix* rather than a chemistry tutorial: it states how TRC sits inside U-Theory, which canonical claim it exercises, and how it stands as a **sibling of TRB and TSE**.

### A.0 What TRC IS — and is NOT (instance, not proof)

Triadic Chemistry is U-Theory **applied to** chemical substances and materials. **It is an instance of the framework, not evidence that the framework is true.** The thing to inherit from canon is canon's *falsifiability discipline*, not its conclusions — so TRC's first job is to try to falsify its own load-bearing assumption (separable F/P/A for substances and routes, §2.5, §8 TRC-P0) before claiming anything about chemistry. If F/P/A turn out collinear for chemical entities — plausible, since a single computed electronic structure dictates much of structure, energetics, and reactivity at once — the architecture has no independent inputs to be non-compensatory over. **If TRC-P0 fails, the entire four-layer engine (§3–§6) is deleted, not reinterpreted** — that null is reported as a clean narrowing of canon's universality claim by chemical reality (the cost is stated plainly here once, and not rhetorically re-celebrated elsewhere).

### A.1 The same invariant triad, registered onto chemical matter

Canon fixes one substrate-invariant triad — **Form ↔ Time · Position ↔ Space · Action ↔ Energy** — and asserts it is scale- and substrate-invariant: the *meaning* of F, P, A is identical across governance, organisms, diseases, and matter; only the measurable proxies change. Chemistry makes the labels unusually literal (and is registered at every scale, §2.3):

- **Form = what the substance IS** — composition, bonding/connectivity, stereochemistry/conformation, crystal structure & phase identity; its **persistent identity** as a defined chemical entity. *Price: Time* — decomposition, hydrolysis, oxidation/corrosion, racemization, polymorphic transition, radioactive decay.
- **Position = where / in what context** — phase, solvent, T/P/pH/redox environment, lattice site or binding-site fit, what it is adjacent to or embedded in, the use-context. *Price: Space-context.*
- **Action = what the substance DOES** — reactivity, catalytic turnover, energy released/absorbed, mechanical/physical function (cutting, conducting, storing charge). *Price: Energy.*

> **L0 framing caveat (not load-bearing).** The governance gloss "Code = molecular graph, Credo = solvent/phase, Rights = function" is apt in places and a stretch in others — "Credo = solvent" especially, since a solvent is a thermodynamic environment, not a normative belief system. **Nothing numeric depends on the names.** A reviewer may reject the nomenclature without touching a result; the operational content lives entirely in the proxies (§2.5) and the falsifiers (§8). The corpus structure is strictly nested:

```
U-Theory canon  (Form/Position/Action; U=∛(F·P·A); ℳ=∫U dt for a single declared node)
   ├── TRB  — Triadic Biology                    biology.organism
   ├── TSE  — Triadic Stabilization Engineering   the active-stabilization umbrella over TRB
   └── TRC  — Triadic Chemistry  ◄── this appendix (a sibling domain)
         ├── domain  = chemistry.substance / materials.system   atom → … → reaction → catalyst
         ├── axes     = F (identity ↔Time) · P (phase/context ↔Space) · A (reactivity/function ↔Energy)
         ├── payload  = the four design layers  L1 design · L2 synthesis · L3 use · L4 societal telos
         └── control layer = LGP-12 (the L1 design cycle), objective ℳ↑ / 𝒮↓ on one declared clock
```

### A.2 TRC *exercises* the cross-domain-transfer claim (β) — it does not assume it

The corpus transfer coefficient β predicts a stabilization heuristic learned in one `TriadicDomain` transfers to another in proportion to *triadic-structural* similarity, not surface analogy. β is *always computable*; what is at stake is its **validity**. Chemistry is a stress-test: **if F/P/A are not even separable on substances/routes (§8 TRC-P0), β-transfer into chemistry is undefined**, and the corpus universality claim is *narrowed by* chemical reality rather than confirmed by it. Reporting that narrowing is TRC's contribution to canon (TRB §A.2 posture).

### A.3 Runtime — chemistry is a *conformant domain*, not a parallel theory

TRC implements the GSI-RTD `TriadicDomain` interface (`embed_form` = structure/property embedding; `build_position_graph` = phase/solvation/context graph; `enumerate_actions` = candidate reactions/functions; `execute_action` = simulate reaction/use over a horizon; `evaluate_sss` = score `U`). The canonical search→scheduler→agents→cycle→score→learn machinery runs over chemistry with no bespoke orchestration. Every capability claimed below must be expressible through that interface — a hard consistency constraint, re-checked in §10.

### A.4 N-adic placement (NDT) — TRC *amends* NDT, it does not "obey" it

NDT treats triadic (N=3) as default and admits lifting only when a substrate *earns* an extra currency. Chemistry arguably pays a 4th currency `X` (**Freedom / Irreversibility** — foreclosed transformation paths: the cost to *reverse* a chemical state, e.g. a racemization barrier, the barrier separating a metastable polymorph from the ground state, a thermoset's irreversibility vs a thermoplastic's reprocessability). As in TRB §2.4, the default model runs **3-adic** (`U₃ = ∛(F·P·A)`); every record carries an optional `X` slot (`U₄ = (F·P·A·X)^¼`) that **renders no number until its independence falsifier (TRC-P7) admits it, and is removed from the ledger if P7 fails** (§8, §9.9). A 5th-slot "coherence" (long-range crystalline order, mesophase synchronization) is, as in TRB §5.5.2, an **aggregation-level** quantity, **not** a leaf pillar; gated by TRC-P8. TRC therefore populates a **classical** coherence analogue, not NDT's quantum 5th, and logs the disagreement for NDT maintenance.

### A.5 Epistemic stance inherited from canon (level-inflation forbidden)

Canon's RH ladder, quoted verbatim (RH §2 / RH_CRITICAL_REVIEW §67–77): **L0 = Meta-evaluation · L1 = Operational stability · L2 = Cross-domain analogy · L3 = Cosmological extension · L4 = Literal physical claim.** TRC keeps a renamed **B0–B4** ladder precisely so chemistry/materials claims cannot borrow canon's cosmological tiers (L3/L4). Every empirical TRC statement is at most **canon-L2**; the ceiling **B3-pending** is a *narrowing* of L2 to "testable-over-data, not yet validated," never L3/L4. Full mapping in §9.2.

| TRC level | Canon | What lives here in TRC |
|---|---|---|
| **B0** | L0 | "design the most stable matter / matter is triadic"; the Code/Credo/Rights gloss; the L4 civilizational-telos voice; **and the normative rule that L4 may override L1–L3 efficiency** (a value choice, not a model theorem — see R8 fix). Renders no number. |
| **B1** | L1 (Operational stability) | the geometric-zero keystone `U=∛(F·P·A)`; argmin weak-pillar; δ/SI algebra (computed over **leaf** pillars, §2.2); the route-aggregation algebra; `ℳ=∫U dt`; the DZ-1…DZ-12 cycle mechanics — true *of the model*. |
| **B2** | L2 | every empirical TRC claim is *at most* this — a substance's/route's/use's F/P/A scores, feasibility priors, the Ashby triadic fit. |
| **B3** | narrowing of L2→application | the P0/P-battery tests *as pre-registrations*; the design/synthesizability/selection/telos hypotheses (**project ceiling**). |
| **B4** | regulated, outside this plan | **EMPTY ×2 — by intent. Any B4 sentence is a bug.** Slot (i) *synthesis-action*: any output driving a real reaction → process-safety review, REACH/TSCA registration, a new project. Slot (ii) *deployment/societal*: any material released into a real use-context → LCA, environmental-fate review, named accountable authority, a new project. |

---

## 0. What TRC is, what it is not, and the four-layer design

TRC registers the SSS engine onto chemistry and materials (RUO; scope per the canonical banner) and organizes its payload as **four layers** — each a conformant use of the same `ChemSystem` node and the same non-compensatory primitives. **Whether the four layers carry distinct information, or are one U with relabeled anchors, is itself a pre-registered falsifier (TRC-P9, §8).**

- **L1 — TRIADIC DESIGN** (§3): inverse design / retrosynthesis as a **two-headed triadic search** over a *target's* (F,P,A) and a *route's* (F,P,A), coupled non-compensatorily.
- **L2 — SYNTHESIS / CREATION** (§4): scoring a *synthesized material together with its synthesis plan* for **stability** — thermodynamic + kinetic stability, formation energy, synthesizability, route robustness.
- **L3 — EXPLOITATION / USE** (§5): the **most stable USE** — materials selection by triadic fit, benchmarked against **constraint-screened** Ashby (not a weighted sum).
- **L4 — SOCIETAL / CIVILIZATIONAL TELOS** (§6): the **stable goals** a substance serves in society; the **dual-use / safety layer**.

> **Inherited verbatim from TRB §9 / TSE §9:** the claim envelope, the TESTABLE/INTERPRETATION/VISION cut, the B0–B4 ladder, the output lint, SSS-Guard, the multiplicity discipline (R7), the unit-of-independence discipline (R8), overclaim risks O1–O9, and the dual-use posture. TRC re-derives O5 at the substance/material macro-scale (O5b-chem) and adds chemistry-specific gates and overclaims (O10–O12).

---

## 1. Thesis

**What TRC delivers — and is judged on — are the pre-registered, runnable tests of §8**, not a discovery and not an engine:

- **(i) F/P/A separability** for real chemical entities and routes: do Form, Position, and Action carry *conditionally non-redundant* information, or are they three transforms of one electronic-structure calculation? (TRC-P0/P0b/P0c/P0d, §8.)
- **(ii) The non-compensatory geometric `U` beats the right baselines**: a property-only score, **constraint-screened Ashby**, and a plain additive/weighted-sum mix — at predicting external synthesizability/stability/selection outcomes, robustly to its own anchors, DFT functionals, and **cross-database correction schemes**, with the win **isolated to the near-zero/one-low-pillar regime** where non-compensation can actually differ from an average. (TRC-P1/P2/P2b/P4, §8.)

These tests are the product. The four-layer engine is **gated behind them and retired if they fail.** Any reference below to the engine "scaling toward" a hypothesis-generation tool is **aspiration, not a deliverable** (consolidated in §7); the committed deliverable is §8.

> **Epistemic placement (read first).** The four-layer logic, the leverage algebra, and the node/edge schema are **B1** (true of the model) once inputs exist. Every statement that a given candidate is a *real* stable substance, a *real* feasible route, a *real* best-fit material, or a *real* net-stabilizing societal role is **B3-pending** — a pre-registered prediction, never a finding. **The rule that L4 telos may override L1–L3 efficiency is B0/VISION, not B1** — it is a value choice, not a theorem of the model.

---

## 2. Core idea & the F/P/A → chemistry mapping across scales

> **Register tags carried throughout.** Every proxy-table cell is **TESTABLE** only where it names an operational measurement or computation with an external metric; the axis *names* ("Form is identity") are **INTERPRETATION**. The chemistry separability claim is **B3-pending** — that F, P, A carry conditionally non-redundant information is the wager TRC-P0 tests (§8), **not** an assumption of this section. No rendered number in this section exceeds **B2**; the worked example's figures are **illustrative** (see the §2.8 honesty riders).

### 2.1 The invariant triad, registered onto chemical matter (with prices and failure modes)

| Pillar | Chemical meaning — *what is scored* | Existential price (currency) | Invariant | Canonical failure mode |
|---|---|---|---|---|
| **FORM (F)** | composition, bonding/connectivity, stereochemistry/conformation, crystal structure & phase identity; its **persistent identity** as a defined chemical entity | **Time** — decomposition, hydrolysis, oxidation/corrosion, racemization, polymorphic transition, radioactive decay | Form ↔ Time | **identity collapse** — the substance is no longer what it was |
| **POSITION (P)** | phase, solvent, T/P/pH/redox environment, lattice/binding-site fit, neighbours, use-context. `P = √(q·c)` = locus `q` × context `c`, non-compensatory internally | **Space-context** — mislocalization, phase-mismatch, solvation/exclusion cost, leaching, wrong-compartment partitioning | Position ↔ Space | **positional collapse** — wrong phase / incompatible environment / no stable site |
| **ACTION (A)** | reactivity, catalytic turnover, energy released/absorbed, mechanical/physical function; the work it performs or enables | **Energy** — ΔG/ΔH of reaction, activation barriers, dissipation, energy to maintain a driven function | Action ↔ Energy | **functional / energetic failure** — kinetically inert when reactivity is required, **or** runaway when restraint is required (two-sided, §2.6) |

> **Declared orthogonality threat (a falsifier, not a footnote).** Both **Action** and **Position** are partly *task-relative* (§2.6, §5.1): the "useful-reactivity band" that defines a high Action score is set by the declared task, and the task fixes the use-context that defines Position. Action and Position therefore share a task variable *by construction*, which is a structural reason to expect their conditional dependence to be **non-zero before any data is seen.** This is not hidden as a caveat: it is the explicit motivation for testing **conditional** (not marginal) separability with the task held fixed (TRC-P0/P0e, §8).

### 2.2 The evaluation primitives (SSS, non-compensatory throughout) — δ on LEAF pillars

```
LEAF pillars: f.thermo, f.kinetic_persistence (Form);  p.locus q, p.context c (Position);  a.* (Action sub-scores)
F  = wgeomean(f.thermo, f.kinetic_persistence)         P = √(q·c)        A = wgeomean(a.*)   (band-centred, §2.6)
U  = ∛(F · P · A)                       any pillar → 0  ⇒  U → 0     (geometric-zero keystone, canonical SSS)
δ  = (max(L) − min(L)) / (max(L) + 0.01)   over the FULL LEAF SET L = {f.thermo, f.kinetic_persistence, q, c, a.*}
SI = U / (1 + δ)²                        imbalance-penalized stability index
weak_leaf   = argmin(L)                  weak_pillar = the pillar owning weak_leaf
```

> **δ/SI fix (critique C5/M5).** δ is computed over the **leaf** set, not the three top-level pillars, so an internally collapsed pillar (e.g. `q=0.01, c=1.0` → `P≈0.1`) is correctly flagged as **imbalanced**, not laundered as a "balanced low Position." To stop SI over-penalizing a legitimately strong-but-uneven candidate (e.g. all leaves ≥ 0.6 with one at 0.6), δ is **only consequential once a leaf is below the at-risk anchor** — `SI` uses `δ⋆ = δ · 𝟙[min(L) < 0.5]`; an all-competent node with mild spread is not punished, while a node with one near-collapsed leaf is.

**Worked contrast (scoring-mechanics illustration only — no separability/predictive evidence).** A candidate with **F=0.95, P=0.95, A=0.02 (kinetically inert)** has arithmetic mean 0.64 but **U = ∛(0.95·0.95·0.02) = 0.26** — correctly killed where an additive optimizer would shortlist an inert solid as a catalyst. Note that this divergence between geometric and arithmetic is **only large near a zero**; that is precisely why TRC-P0b/P2b must isolate the near-zero regime (§8), or the "geometric beats additive" claim passes trivially on rank-correlation.

Verdict bands are **domain-tunable defaults, not constants of chemistry**: `SI ≥ 0.618` (φ⁻¹) Stable · `0.38–0.618` At-risk · `<0.38` Critical. **High-stakes use-contexts raise θ** (pharma shelf-life, aerospace alloy, nuclear-waste form → θ ≥ 0.90). For `suppress`-polarity nodes the stakes-scaling runs the *other way* (lower the alarm threshold). **All thresholds, anchors, and normalization shapes are free parameters of the model, perturbed in TRC-P0b** (the single canonical statement of this caveat; see also §9.10-4).

### 2.3 Recursion across scales & the assignment rule

Every chemical entity at every scale is itself a triad (`ChemSystem`); `depth d ⇒ 3^d` sub-entities, **never enumerated**. Pillars are assigned by three orthogonal questions, each at the node's own scale, with a **state vector `s`** carrying conditions (T, P, pH, solvent, redox, irradiation, mechanical load) under which "ideal Form" and "allowed Action" are evaluated — a reaction normal in a reactor at 600 K / 100 bar is forbidden at the bench.

```
FORM(e)     := identity/structure of e vs its state-conditioned class ideal   (points DOWN-IN)
POSITION(e) := placement of e in its PARENT (L+1) + operational context        (points UP-OUT)
ACTION(e)   := e's CONTRIBUTION to the ACTION of its parent (L+1)              (points UP-FUNCTIONAL)
```

| Scale | FORM (identity/structure, ↔Time) | POSITION (phase/context/site, ↔Space) | ACTION (reactivity/function, ↔Energy) |
|---|---|---|---|
| **atom / ion** | element, oxidation state, isotope, electron config | lattice site / coordination sphere / solvation shell | electronegativity, ionization energy, redox potential, polarizability |
| **bond** | bond order, type (σ/π, ionic/covalent/metallic/H-bond), length | which atoms it joins; dihedral context | bond dissociation energy (BDE), vibrational mode, lability |
| **functional group** | group identity (–OH, –COOH, C=O, aryl), SMARTS pattern | position on the scaffold; neighbours; exposure | reactivity class, pKa, H-bond donor/acceptor |
| **molecule** | constitution + stereochem + tautomer (InChI/canonical SMILES) | phase, solvent, conformer ensemble, partitioning (logP) | ΔG_f, reactivity, binding affinity, spectroscopic/optical function |
| **supramolecular assembly** | host–guest topology, H-bond/π-stack network, MOF/cocrystal motif | medium, concentration, templating environment | self-assembly free energy, selective binding, gated transport |
| **material / phase** | crystal structure (space group), composition, microstructure, defects | bulk vs surface vs grain boundary; service environment (T, atmosphere, stress) | mechanical/electronic/catalytic function; phase stability |
| **formulation / system** | the multi-component recipe & physical state (the *device*) | the use-context | the delivered function |
| **reaction** (an *edge-as-node*) | transformation identity (reactants→products, mechanism class) | phase/solvent/catalyst environment | ΔG_rxn, ΔH_rxn, Eₐ, rate, selectivity, yield |
| **catalyst** | active-site structure, support, oxidation state | mounted phase / reactor context / poisoning environment | TOF, TON, selectivity, the ΔG‡ it lowers |

### 2.4 The optional 4th axis (NDT N=4) — gated, renders no number

Per §A.4: the default model runs **3-adic**; every record carries an optional `X` (Freedom/Irreversibility) slot that renders no number until TRC-P7 admits it and is removed if P7 fails. Candidate X-proxies: kinetic-trap depth, Gibbs-energy hysteresis of a phase transition, retrosynthetic step-irreversibility, end-of-life recyclability index. Coherence-as-5th-slot is aggregation-level (long-range crystalline order, mesophase synchronization), not a leaf pillar; gated by TRC-P8.

### 2.5 Per-pillar proxies from REAL data — measured vs computed vs inferred (the load-bearing honesty table)

Each raw observable is normalized to `[0,1]` against process-intrinsic reference anchors (`ref_lo` = collapse, `ref_hi` = ideal) with a clamped, monotone-or-band-centred saturating curve (Action and Freedom are **two-sided**, §2.6). **FORM is scored from the *process/structure*, never from a nomenclature/registry definition** — a substance whose Form rests only on an unverified catalogue entry is tagged `LATTICE_APPROX` and held to a higher evidence bar (the mirror of TSE §3.2's "nosology-stability is NOT a Form proxy"). Every cell carries a **provenance class**: **[M] measured** · **[C] computed** (DFT/MD/QM — a *model output*, not a measurement) · **[I] inferred** (QSPR/group-contribution, correlated-by-construction with its inputs).

| Pillar (↔ price) | Process-intrinsic proxy | Real source / descriptor | Provenance | Failure mode |
|---|---|---|---|---|
| **FORM / identity** | canonical structure match (InChIKey/canonical SMILES); stereochemical & tautomeric integrity; crystal space-group / polymorph identity | **PubChem** CID + InChI; **RDKit** canonical SMILES, `FindMolChiralCenters`; **ICSD / Materials Project / COD** space group; **CCDC** polymorph | [M] / [C] | hydrolyzed, racemized, wrong polymorph, decomposed |
| **FORM / persistence-rate** — *how fast does identity erode over Time?* | thermodynamic depth (formation energy referenced to elements) + decomposition/corrosion propensity; thermal-decomposition onset; oxidative/hydrolytic lability | **NIST WebBook** ΔH_f, T_decomp; **Materials Project / OQMD** formation energy; **RDKit** count of hydrolyzable bonds (SMARTS) | [M] ΔH_f, T_decomp / [C] E_f | high lability / shallow thermodynamic depth with low barrier → short shelf-life |
| **POSITION / locus (q)** — literal phase/site | phase at service conditions; correct lattice/binding-site occupancy; compartment match; **energy above the convex hull `E_hull`** as a metastability-vs-competing-phases quantity (see axis note below) | **NIST** phase diagrams; **Materials Project / OQMD** phase diagram, convex hull & **Pourbaix** (aqueous stability) | [M] / [C] | wrong phase / ectopic precipitation / amorphous when crystalline required |
| **POSITION / context (c)** — environment integrity | solvation fit & miscibility; T/P/pH/redox window; substrate availability; compatibility with adjacent materials (galvanic, chemical) | **logP / logS** (RDKit `Crippen MolLogP`); Hansen parameters; **Pourbaix** window; ORD reaction *conditions* fields | [M] solubility / [C] Pourbaix / **[I]** logP, logS (QSPR — flag) | leaches / immiscible / outside its stability window / starved of substrate |
| **ACTION** (two-sided, §2.6) | reaction thermodynamics & kinetics; catalytic turnover; mechanical/physical function | **ΔG_rxn/ΔH_rxn** (NIST; MP reaction energies); **Eₐ / rate / yield / selectivity** from the **Open Reaction Database (ORD)** and **Reaxys-class** sets; **BDE**; **TOF/TON**; **Ashby property axes** for materials | [M] yield, rate, TOF, mech. props / [C] Eₐ (DFT-NEB), BDE | inert when reactivity required **OR** runaway when restraint required (both extremes → 0) |

> **E_hull axis assignment — disclosed conflict, resolved one way, used as a separability liability (critique C2).** `E_hull` (energy above the convex hull) is the distance to the hull of *competing phases at the same composition* — it answers "is there a more stable arrangement *available in this composition's neighbourhood*," which is a **Position-context** question (where does this phase sit relative to its competitors?). **TRC therefore assigns `E_hull` to POSITION/locus, canonically, here and in §4.3** — earlier drafts that placed it under Form/thermo are superseded. The fact that one observable felt assignable to *either* Form or Position is **not laundered away: it is logged as direct prima-facie evidence that F and P may not be separable for chemical entities, and is folded into TRC-P0d** (does any single DFT-derived observable carry comparable conditional dependence on two pillars?). The thermodynamic-depth quantity that *does* sit under Form is the **formation energy referenced to elemental standard states**, which is a different number from `E_hull` and must not be conflated with it (see §2.8 honesty rider).

> **Data-independence warning (load-bearing, mirroring TRB §4.2 — two layers; this is the single canonical statement, cross-referenced elsewhere).** **(a) Shared upstream calculation.** Many "Action" and "Position" descriptors for *molecules* are **computed from the same molecular graph that defines Form** — RDKit logP, TPSA, predicted pKa, group-contribution ΔG_f, and DFT properties all take the **structure as input**. An `A_predicted × F_structure` product multiplies a number by a transform of itself — the **DFT-from-one-structure** confound (TRB's FBA-from-Form analogue). **(b) Definitional leakage via the composition label:** "one resource → one axis" is really "one composition → three axes." Consequences, pre-registered for TRC-P0: (i) **DFT/QSPR-derived Action and Freedom proxies are EXCLUDED from the input-independence claim**; (ii) separability is tested on **measured** Action (real ORD yields/rates, measured TOF, measured mechanical properties) wherever it exists; (iii) a **shared-upstream-feature audit** traces every proxy to its raw source. *If F/P/A turn out collinear for chemical entities, the architecture has no independent inputs to be non-compensatory over (see §A.0 for the consequence).*

### 2.6 Where the chemistry mapping is contested — and how this plan resolves it

- **Reactivity is ACTION, not Form — but not a function of Action-data alone.** Reactivity is partly intrinsic (Form: bond strengths) and partly contextual (Position: solvent, catalyst, substrate). The Action pillar scores the **realized energetic transformation** *in a stated environment*, not a structure-only reactivity index that would smuggle Form into Action.
- **Solvent / T / P / pH is POSITION, not Action.** The environment is *where the substance sits*; the energy released/absorbed in it is Action. In corrosion the chain is `aggressive environment (Position-context) → oxidation proceeds (Action) → metal identity lost (Form)`; the axis-matched first move is to fix the environment, not to "make the metal less reactive."
- **Thermodynamic depth (formation energy from elements) is FORM/persistence; the convex-hull/competing-phase distance `E_hull` is POSITION/locus; the kinetic barrier (Eₐ to decompose) gates the *Time* price.** Split Form non-compensatorily: `f.thermo` (formation-energy depth) and `f.kinetic_persistence` (barrier out of the current basin). **A metastable substance with a deep kinetic trap has modest thermodynamic Form yet intact persistence** — the cementite case below.
- **Action is two-sided AND task-relative.** A one-sided "more reactive = better" ramp would score an explosively over-reactive substance as healthy. Action uses a **band-centred** normalization: `s = 1` inside a *declared-task* useful-reactivity band, falling to 0 on *both* sides (inert *and* uncontrolled). Because the band is task-set, **Action is not a substance-intrinsic scalar without a declared task** — which is exactly the orthogonality threat declared in §2.1 and tested in TRC-P0e. The non-compensatory keystone survives — either extreme zeroes the term — only the *shape* changes; TRC-P0b perturbs the functional form.
- **ΔG gates EXTENT, not possibility (critique C6).** A positive standard `ΔG°_rxn` does **not** forbid a reaction — it sets the equilibrium position; coupled reactions, product removal, and non-standard activities routinely drive `ΔG° > 0` reactions forward (Le Chatelier; driven synthesis). The Action proxy therefore scores **`ΔG` evaluated at the operating activities/temperature of the declared state `s`** against an extent/yield anchor — it is `ΔG_op ≫ 0 with no coupling → low extent → low Action`, **never** "`ΔG° ≥ 0 ⇒ Action = 0`." Kinetic accessibility (a clearable barrier) is scored separately; an infeasible step is one with neither attainable driving force *nor* a crossable barrier in the declared context.
- **Position = `(q, c)`, non-compensatory inside.** `p.locus = q` (right polymorph/phase, hull placement) and `p.context = c` (right T/pH/solvent/neighbours) combine via `P = √(q·c)`; a zero in either zeroes P and (via the leaf-level δ, §2.2) flags imbalance.
- **A mixture/additive is a NODE with a causal edge, not a scalar in another node's pillar** (TRB §2.6 microbiome rule). An inhibitor, dopant, or solvent is a scored `ChemSystem` influencing the host through explicit `STABILIZES`/`CATALYZES`/`POISONS`/`SUPPLIES` edges, **never** copied as a number into the host's `p.context`.

### 2.7 The node & edge model — one axis per edge

```tpl
F{ entity:"Fe3C cementite"; structure:orthorhombic-Pnma(62); composition:Fe0.75C0.25;
   identity:carbide-phase-intact; thermo:ΔHf_from_elements≈small (sign functional-dependent, illustrative);
   kinetic_persistence:high }
P{ locus:bulk-crystalline-phase-in-pearlite; E_hull:metastable-vs-(Fe+C)-tie-line;
   context:ambient-T+dry-atmosphere+embedded-in-ferrite-matrix }      ; P = √(locus·context)
A{ function:provides-hardness+wear-resistance;
   reaction:metastable→3Fe(α)+C(graphite) [kinetically suppressed at service T]; mech:high-hardness/brittle }
s = (T=298K, P=1bar, atmosphere=dry, mechanical_load=service)
G{ src:MaterialsProject:mp-510623 + NIST-FeC-phase-diagram; conf:0.80; scope:specific; level:B2; mode:assert }
```

Edges are typed; **each loads exactly one axis** (TRB K2 / TSE §3.3; no edge double-loads):

| Edge | Meaning | Axis loaded | Real source |
|---|---|---|---|
| `IS_A`, `COMPOSED_OF` / `PART_OF`, `POLYMORPH_OF` | type subsumption, containment (recursion backbone) | Form | PubChem, ICSD, Reaxys class hierarchy |
| `IN_PHASE`, `DISSOLVED_IN`, `ADSORBED_ON`, `OCCUPIES_SITE`, `ADJACENT_TO`, `COEXISTS_WITH`, `ON_HULL_WITH` | placement, solvation, lattice site, neighbourhood *context*, hull position | Position | NIST phase diagrams, MP convex hull, Hansen params |
| `REACTS_WITH`, `DECOMPOSES_TO`, `CATALYZES`, `CONDUCTS`/`STORES`, `BINDS` | the *energetic transformation or physical function* | Action | ORD, KEGG-rxn, NIST thermochem |
| `STABILIZES` / `POISONS` / `CORRODES` / `DESTABILIZES` (per-target) | an additive/environment's effect, decomposed into its F/P/A target | per-target | inhibitor DBs, corrosion data, ORD conditions |

*Edge-independence caveat (TRB M-2):* when a `REACTS_WITH` (Action) edge and an `ADJACENT_TO`/`COEXISTS_WITH`/`ON_HULL_WITH` (Position) edge are both re-typed from **one** computed reaction-network / phase-diagram prediction, they are **correlated by construction and are not independent evidence** for separability. **Open-world guard:** a phase/reaction *absent from ICSD/MP/ORD* is `UNKNOWN` (`OPEN_WORLD`), **never** `FORBIDDEN`; only a positively-contradicted entity (imaginary phonons; no attainable driving force *and* no crossable barrier in any enumerated accessible context) is vetoed.

### 2.8 ONE fully worked node example — Fe₃C cementite (SCORING-MECHANICS ILLUSTRATION ONLY — ZERO separability/predictive evidence)

> **READ FIRST.** Every number below is illustrative and/or hand-anchored to a textbook-known case; F, P, and A here draw on **partially shared upstream data** (one DFT relaxation yields structure *and* energetics), so this node **cannot demonstrate separability** — it shows *scoring mechanics* only. Separability is deferred to TRC-P0 on a measured battery.

**The substance.** Cementite, Fe₃C, **Materials Project `mp-510623`**, orthorhombic **Pnma (62)** — the hard, brittle carbide that, interleaved with ductile ferrite as pearlite, gives carbon steel its hardness and edge-holding.

**Two thermodynamic quantities that must not be conflated (critique C1).**
- **Formation energy from elemental standard states (Fe + C):** for Fe₃C this is **small and of functional-dependent sign** — reported in the literature anywhere from slightly negative to slightly positive (≈ −0.02 to +0.03 eV/atom across GGA/GGA+U/experiment). It feeds **Form/`f.thermo`**.
- **Energy above the convex hull, `E_hull` (distance to the Fe–C tie-line, i.e. bcc-Fe + graphite):** this is **positive** (cementite is metastable with respect to decomposition into iron + graphite) and feeds **Position/`q`**.

These are **different numbers measuring different things**; the earlier draft's "ΔH_f = E_hull = +0.055 eV/atom" was a category conflation and is corrected. The illustrative scores below treat `f.thermo` as *modest* (shallow/uncertain elemental formation depth) and `q` as *metastable-but-present* (positive but small `E_hull`); **no claim is made that any of these is the verified mp-510623 value** — they are placeholders demonstrating the split, and any real use must pull and cite the live mp-510623 figures with the M/C provenance and the functional recorded.

**FORM (↔ Time).** `f.identity` = carbide phase, space group → **1.0** [M/C]. `f.thermo ≈ 0.55` (shallow / sign-uncertain elemental formation depth — *modest* Form penalty) [C, illustrative]. `f.kinetic_persistence ≈ 0.95` — Fe₃C → 3Fe(α) + C(graphite) is kinetically suppressed at service T, so the carbide persists indefinitely in a knife [M, metallurgical knowledge]. Non-compensatory: **F = √(0.55·0.95) ≈ 0.72**. The split captures *both* truths a one-number Form would lose.

**POSITION (↔ Space).** `p.locus = q ≈ 0.90` — bulk crystalline carbide in a ferrite matrix, correct phase for the role, but *metastable above the Fe–C hull* (the `E_hull` discount lives here, not in Form) [C/M]. `p.context = c ≈ 0.90` — ambient T, dry atmosphere, mechanical-service load; benign for cementite (it would oxidize/decarburize at high T in air, not in kitchen use) [M-inferred]. **P = √(0.90·0.90) = 0.90.**

**ACTION (↔ Energy), band-centred (§2.6).** Useful Action is **mechanical** — hardness and wear resistance — not chemical reactivity. Cementite sits in the **high-hardness band** (exactly where the knife wants it; the decomposition Action is suppressed). Band-centred score → **A ≈ 0.88** [M, mechanical-property data]. (Scored *as a chemical reagent*, its near-inert ambient reactivity would score Action *low* — same substance, different task/state `s`.)

**Aggregate (leaf-level δ, §2.2).** Leaves `L = {f.thermo 0.55, f.kinetic_persistence 0.95, q 0.90, c 0.90, a.mech 0.88}`.
```
U  = ∛(F · P · A) = ∛(0.72 · 0.90 · 0.88) = ∛(0.570) ≈ 0.829
δ  = (0.95 − 0.55)/(0.95 + 0.01) = 0.417     ; min(L)=0.55 ≥ 0.5  ⇒ δ⋆ = 0  (no near-collapse) ⇒ SI = U ≈ 0.83
weak_leaf = f.thermo (0.55)  ⇒ weak_pillar = Form
```
Because no leaf is below the 0.5 at-risk anchor, the **SI over-penalty fix** (§2.2) keeps SI ≈ U ≈ 0.83 (STABLE) rather than dragging a competent-but-uneven node into AT-RISK — the behaviour the old top-three-pillar δ produced.

**Reading (TESTABLE register, claim-envelope B2).** *"Model fragility index for entity-type Fe₃C-in-service = SI≈0.83 (model-internal, not a materials qualification). Weakest leaf = Form/thermodynamic-depth; HYPOTHESIS that the cheapest stability lever is Form/persistence (e.g. alloying to deepen the carbide or stabilize against graphitization), conditional on TRC-P0 separability holding."* The renderer **never** prints "Fe₃C's stability is 0.83" as a measured property; the number is a model-internal index with provenance `mp-510623 + NIST`, `level: B2`. The "alloying" lever is named only as a research hypothesis about a *substance type*, never an operational recipe.

**Honesty riders.** (1) Formation-energy and `E_hull` are distinct (above) and any headline must use the real, separately-cited mp-510623 values and survive TRC-P0b anchor/functional-form perturbation. (2) `f.kinetic_persistence`, `c`, and the Action band edges are **anchor choices** — the most consequential free parameters — subject to ±20%-value, ramp↔logistic↔trapezoid-shape, *and* cross-database ablation; the verdict is not a finding. (3) This single node draws on shared upstream data and **cannot demonstrate separability** (see READ FIRST).

---

## 2.9 The 4-Layer Gaussian Stability Matrix (GSM) — uncertainty-aware `U`, gated extension of §2.2

> **READ FIRST — what GSM is and is NOT.** GSM is a **distributional re-statement** of the §2.2 primitives: it replaces each point leaf/pillar score with a *belief distribution* over that score, propagates those beliefs through the **unchanged** keystone `U = ∛(F·P·A)`, and reports a **credible interval and a failure probability** instead of a bare number. It changes **no axis assignment, no anchor, no verdict band (φ⁻¹≈0.618 stays, §2.2), and no firewall rule.** It is **B1-pending** (true *of the model* once GSM-P1 calibrates; an INTERPRETATION decoration until then) and is **gated and retired by GSM-P1** exactly like every other optional TRC layer (§9.9). It adds nothing to the separability question (TRC-P0); it *inherits* that liability and merely makes it visible as covariance. Every number below is a **SCORING-MECHANICS ILLUSTRATION ONLY, with ZERO separability or predictive evidence** (the §2.8 READ-FIRST banner applies verbatim).

### 2.9.1 Motivation — the gap a point-SI cannot close

The §2.2 pipeline emits one number per leaf and one `U` per node. It therefore **cannot distinguish two failure-shaped situations that demand opposite actions**:

- a **known-low** leaf — measured, well-covered, genuinely near collapse (`a ≈ 0.05`, coverage `≈ 0.9`): *the lever is real, act on the substance type*; and
- a **high-uncertainty** leaf — the SSS-L4 neutral-50 default fired because the observable was missing (`a ≈ 0.50`, coverage `≈ 0.1`): *do not act; buy evidence first.*

Both can produce the same `SI`, and the second is exactly the `evidence_sparse` / `dft_only` case the §9.8 lint already tags but cannot **quantify**. GSM makes the difference first-class: a leaf is not a scalar `s ∈ [0,1]` but a **distribution** whose **mean** answers "how low?" and whose **variance** answers "how sure?". The probabilistic weak-zone (§2.9.5) then targets `P(failure)`, so a wide-but-central leaf is correctly demoted relative to a tight-but-low one — directly discharging SSS's named open problem SSS-L4 ("report confidence separately") *beyond* the inherited mechanisms (consensus-%, coverage-tagged neutral-50, the claim-envelope `conf`/`evidence`, external-ground-truth agreement), which GSM **subsumes as inputs** rather than restates (§2.9.6).

### 2.9.2 The object — a 4×3 array of logit-normal cells with cross-cell covariance

GSM arranges the node's beliefs as a **4-layer × 3-pillar matrix** — the four TRC layers (L1 design, L2 synthesis, L3 use, L4 societal telos, §3–§6) crossed with the canonical pillars (F, P, A):

```
            FORM (F)        POSITION (P)     ACTION (A)
  L1 design   s_11             s_12             s_13
  L2 synth    s_21             s_22             s_23
  L3 use      s_31             s_32             s_33
  L4 society  s_41             s_42             s_43          (each cell s_ij ∈ (0,1) is a RANDOM VARIABLE)
```

**Honest support — "Gaussian in logit space," not a Gaussian on [0,1].** A raw Gaussian on a pillar score is *wrong*: its support is `(−∞,∞)`, it puts mass outside `[0,1]`, and it is symmetric where stability scores are not. GSM instead models each cell as a **logit-normal** — a Gaussian on the **log-odds** `z = logit(s) = ln(s/(1−s))`, mapped back by the logistic `s = σ(z) = 1/(1+e^{−z})`. The name "Gaussian" is faithful **on `z`, never on `s`.** This is the single load-bearing modelling choice; the Beta alternative and the reasons to prefer one or the other are stated honestly in §2.9.7.

Stack the twelve log-odds into a vector `z = (z_11, …, z_43) ∈ ℝ¹²`. GSM's full object is **one multivariate normal**

```
        z  ~  𝒩( μ , Σ )         μ ∈ ℝ¹²        Σ ∈ ℝ^{12×12}  (symmetric PSD)
        s_ij = σ(z_ij)           ⇒  each cell is logit-normal on (0,1)
```

— so the cells are not independent: **`Σ` carries the correlations across pillars and across layers that TRC's own falsifiers (TRC-P0, P0e, P9) probe.** GSM does not *assume* separability; it *parameterizes the failure of separability* and lets the propagated interval widen accordingly. `μ_ij` is set so that `σ(μ_ij)` equals the §2.2 point score for the cell (`μ_ij = logit(s_ij^{point})`), so **GSM with `Σ → 0` reproduces the §2.2 number exactly** — a strict, testable backward-compatibility constraint (the GSM⊂§2.2 limit, §2.9.4).

### 2.9.3 The covariance `Σ` — where evidence and non-separability live

`Σ = D R D` separates **per-cell uncertainty** (diagonal scale `D`) from **cross-cell dependence** (correlation matrix `R`):

- **Diagonal `D = diag(τ_ij)` — evidence-driven log-odds spread (the SSS-L4 hook).** Each `τ_ij` is the standard deviation of the cell's log-odds and is set *from evidence*, not by hand, tied to the inherited coverage/consensus fields (§9.8 envelope):

  ```
  τ_ij = τ_floor + κ · (1 − coverage_ij) + λ · (1 − consensus_pct_ij) + ν · 𝟙[provenance ∈ {C, I}]
  ```

  so a **measured, high-coverage, high-consensus** cell is *tight* (small `τ`, the logit-normal collapses toward a spike at `σ(μ)`), while a **neutral-50, low-coverage** cell is *wide* (large `τ`: `μ = logit(0.5) = 0` and broad spread — "centred but ignorant," exactly the desired reading). `coverage_ij < 0.3` (`LOW_EVIDENCE`, §9.10-8) forces `τ_ij ≥ τ_LOW` so such cells **never render decision-grade** — the distributional teeth on the inherited neutral-50 rule. (`τ_floor, κ, λ, ν, τ_LOW` are free parameters perturbed in GSM-P1 / TRC-P0b alongside the anchors.)

- **Off-diagonal `R` — the dependence structure, estimated, never assumed.** `R` has three named blocks, each a hypothesis GSM exposes rather than hides:
  - **within-layer, across-pillar `ρ_FPA`** — the F/P/A conditional dependence inside one layer. This is **the same quantity TRC-P0/P0e measure** (and is expected non-zero a priori because Action and Position both carry the task variable, §2.1). GSM ingests the *measured* conditional dCor/CMI from the TRC-P0 battery as `ρ_FPA` and lets `U`'s interval widen when F/P/A move together.
  - **within-pillar, across-layer `ρ_layer`** — e.g. a substance whose synthesis-Form is fragile tends to have a fragile use-Form. This is **the same redundancy TRC-P9 measures**; GSM reads `ρ_layer` straight from the P9 layer-orthogonality test.
  - **off-block `ρ_cross`** — residual cross-layer-cross-pillar terms, defaulted to 0 unless data support them (admitted only if it survives the same conditional, family-level, FDR-corrected bar as any TRC-P falsifier, §8).

  **`R` is shrunk to a PSD estimate** (Ledoit–Wolf / OAS toward the identity) so that at small family-level `n` (R8) the off-diagonals are pulled toward independence rather than over-fit — the honest default when correlation is under-determined (caveat §2.9.7-2).

> **Provenance discipline (mandatory, §9.3).** `Σ` is **not** an engine output trusted on faith: every off-diagonal entry carries `G{src;version;date}` and the test (P0/P0e/P9 run) that estimated it, exactly as §9.3 requires of every value. A `Σ` whose off-diagonals were *assumed* rather than estimated is `axis_unseparated` (§9.8) and renders no interval — only the `Σ → 0` point fallback (§2.9.4).

### 2.9.4 Propagation — `U` of correlated logit-normals (Monte-Carlo primary, delta-method check)

`U = ∛(F·P·A)` of correlated logit-normals **is not Gaussian and has no closed form** (the geometric mean of dependent logit-normals). GSM specifies **two** propagators; the cheap one must agree with the expensive one or the cheap one is not used.

**(A) Monte-Carlo (primary, decision-grade).**

```
for k = 1..K (K ≥ 10⁴, fixed seed, logged):
    z^(k) ~ 𝒩(μ, Σ)                              # one draw of all 12 log-odds, jointly
    s^(k)_ij = σ(z^(k)_ij)                        # back to (0,1), per cell
    per layer i:  F_i,P_i,A_i from the §2.2 leaf roll-up on row i's cells (P=√(q·c), wgeomean for F/A)
                  U_i^(k) = ∛(F_i · P_i · A_i)    # UNCHANGED keystone — non-compensation preserved
    node:         U_node^(k) = wgeomean_i(U_i^(k))  or the declared one-directional layer-coupling (§3.1; NEVER cross-substance)
report per cell / per layer / per node:
    mean, median, and the 5th/50th/95th percentiles  →  90% credible interval  [U_.05, U_.95]
    SI distribution via the §2.2 δ⋆/SI map applied per draw (δ⋆ is itself now a random variable)
```

Because each draw runs the **unchanged** geometric keystone, **non-compensation is preserved sample-by-sample**: a cell whose mass piles near 0 drives `U^(k) → 0` on (almost) every draw, so the *whole posterior* of `U` collapses toward 0 — no amount of certainty elsewhere rescues it (§2.9.5). The credible interval is **percentile-based** (not mean ± k·sd), because `U`'s posterior is skewed and bounded.

**(B) Delta-method / moment approximation (fast screen, must be validated against A).** For triage over a 10³–10⁶ screen, approximate in log space. With `Y = ln U = ⅓(ln F + ln P + ln A)` and the logit-normal moments:

```
E[ln s_ij] ≈ ln σ(μ_ij) − ½ τ_ij² σ(μ_ij)(1−σ(μ_ij))(1−2σ(μ_ij))/…   (2nd-order Taylor of ln σ(z))
Var[ln U]  ≈ (1/9) gᵀ Σ_lns g          # g = leaf→ln-pillar Jacobian; Σ_lns = covariance pushed to ln s
E[U] ≈ exp(E[ln U] + ½ Var[ln U])      # log-normal-style back-transform (APPROXIMATE)
```

The delta-method is **explicitly only a screen**: it is *unreliable near the zeros* — exactly the regime where non-compensation matters (and where TRC-P0b must isolate the win, §2.2) and where the Taylor expansion of `ln σ` and `ln U` both break down. GSM's rule: **delta-method may rank candidates, but any cell flagged AT-RISK/CRITICAL by it is re-scored by Monte-Carlo before any verdict.** A logged max-discrepancy `|U_.05^{MC} − U_.05^{delta}|` over the screen is reported; if it exceeds a pre-set tolerance the delta-method is disabled for that battery (a convenience, never an authority).

### 2.9.5 Probabilistic weak-zone — risk = `P(U < φ⁻¹)`, uncertainty-aware leverage

The §2.2/§4.5/§5.2 weak-zone scan localizes by `argmin`; GSM re-states it on the posterior. **Risk** of a cell, a layer, or the node is the **posterior failure probability** against the (stakes-scaled) verdict threshold `θ` (default `φ⁻¹ ≈ 0.618`, §2.2):

```
P_fail(layer i) = P( U_i < θ )            ≈ (1/K) Σ_k 𝟙[ U_i^(k) < θ ]
P_fail(cell ij) = P( s_ij < θ_leaf )      against the leaf at-risk anchor (default 0.5, §2.2)
```

This separates the two §2.9.1 cases by construction: a **known-low** cell has `P_fail ≈ 1` (tight mass below `θ`); a **neutral-50 / high-uncertainty** cell has `P_fail ≈ 0.5` with a **wide** interval (mass straddling `θ`) — same point score, different risk **and** different recommended action.

**Uncertainty-aware leverage (the controller's target).** The §4.5/§5.4 leverage primitive `Priority = Δℳ/∛(C_time·C_space·C_energy)` is re-stated on **risk reduction per cost**:

```
GSM-Priority(cell ij) = E[ ΔP_fail(node) | intervene on cell ij ] / ∛(C_time · C_space · C_energy)
                      = ( P_fail(node)  −  P_fail(node | s_ij ← target) ) / cost
```

i.e. the controller targets **the cell that most reduces the node's probability of failure per unit cost** — which automatically prefers (i) a high-risk cell over a merely low-mean one, and (ii) a **buy-evidence** action (shrink `τ_ij` by measuring the missing observable) when the cell's risk is *driven by variance, not by a low mean*. "Measure the unmeasured Action" and "deepen the kinetic trap" become **comparable moves on one axis (expected risk reduction)** — the genuinely new affordance GSM adds over the point-SI scan.

> **Firewall and boundary unchanged and binding (no new surface).** GSM-Priority is, like §4.5/§5.4 leverage, **strictly within ONE declared node** — there is **no** cross-substance/cross-task/cross-design `P_fail` comparison, ranking, aggregation, or budget triage; that operation does not exist in GSM, for the same O5b-chem reason it does not exist in §6.4 (a cross-substance `ΔP_fail/cost` ranking would reconstruct the worth ordering without the word "worth"). The §6.5 deny-list, the incidental-discovery halt, and the §9.8 lint apply to GSM intervals and `P_fail` exactly as to point scores; a wide interval is **never** a licence and `P_fail` is **never** rendered as a measured hazard probability (O10, O12). The L4 row's `P_fail` is a *magnitude/entrenchment* probability only — the telos sign `T_soc` remains human-declared and is **not** modelled by `Σ` (§6.2; L4 separability is weaker than chemical separability, §9.10-11).

### 2.9.6 Integration with the inherited uncertainty stack (what GSM consumes, not duplicates)

| Inherited mechanism | Owner | How GSM uses it (consumes as INPUT) |
|---|---|---|
| neutral-50 for missing observable | SSS-L4 (§9.10-8) | sets `μ = logit(0.5) = 0` **and** forces large `τ` (wide, not falsely precise) |
| `evidence_coverage`, `LOW_EVIDENCE` (<0.3) | §4.3 / §9.10-8 | drives `τ` up via `κ·(1−coverage)`; `<0.3` forces `τ ≥ τ_LOW` ⇒ no decision-grade interval |
| consensus-% (agreement, **not** correctness) | SSS / O6 (§9.5) | drives `τ` via `λ·(1−consensus)`; GSM **keeps O6**: low spread = high agreement, *not* validated truth |
| provenance class [M]/[C]/[I] | §2.5 / §9.3 | adds `ν` to `τ` for computed/inferred cells; off-diagonals from one shared calc flagged (§2.5(a)) |
| CI interval in the claim envelope | §9.8 | GSM's percentile credible interval **is** this CI, now propagated through `U` rather than per-pillar |
| TRC-P0 / P0e conditional dCor/CMI | §8 | **becomes** the within-layer `ρ_FPA` block of `R` |
| TRC-P9 layer-orthogonality | §8 | **becomes** the within-pillar across-layer `ρ_layer` block of `R` |
| SSS-Guard ≥2-of-3 + external metric | §9.4 / §9.8 | unchanged gate on the *verdict*; GSM additionally requires the three instances' `P_fail` to agree within tolerance |

**The honest line:** GSM is *not* a new uncertainty theory. It is a **propagation layer** that takes the already-shipping uncertainty quantities (coverage, consensus, provenance, neutral-50) as the diagonal of `Σ`, takes the already-pre-registered separability/orthogonality statistics (P0/P0e/P9) as the off-diagonal of `Σ`, and pushes them through the unchanged keystone to a calibrated `P_fail`. Its novelty is exactly and only: **(i)** distinguishing known-low from high-uncertainty as a number, **(ii)** non-compensation preserved at the *distributional* level, and **(iii)** leverage on `ΔP_fail/cost` including the buy-evidence move. If any of these three fails to add signal over the point-SI pipeline, GSM is retired (GSM-P1).

### 2.9.7 Honest caveats (load-bearing — read before any interval)

1. **Logit-normal vs Beta — a real, unforced choice.** Both put all mass on `(0,1)`. The **logit-normal** is chosen because the multivariate normal on `z` gives a *clean correlation structure* (`Σ` is just a covariance; cross-cell dependence is linear-in-log-odds and trivially PSD-shrinkable) — the whole point, since the correlations are the object of interest. The **Beta** is arguably the more natural likelihood for a bounded score, with interpretable `(α,β)` pseudo-counts mapping onto "n agreeing jury models," **but** a *correlated multivariate Beta* has no canonical form and no clean covariance parameterization, so the cross-pillar/cross-layer structure GSM exists to capture would become ad-hoc. GSM uses logit-normal for the **joint** object and notes a per-cell Beta as an admissible **marginal** alternative; the choice is a free parameter **perturbed in GSM-P1 / TRC-P0b** (logit-normal vs Beta-marginal must not flip a verdict, or the verdict is an artifact of the link function). Neither captures genuine **bimodality** (a polymorph that is either stable or not); a true bimodal belief needs a mixture and is out of scope.
2. **Correlation estimation at small `n` is the central weakness.** `R` has up to 66 free off-diagonals; the family-level unit of independence (R8) makes `n` small (and the §8 power-budget already names this n-collapse). GSM **mandates** PSD shrinkage toward the identity (Ledoit–Wolf/OAS) and **forbids** rendering any off-diagonal that has not cleared the conditional, FDR-corrected, family-level bar (§2.9.3). When `n` is too small, `R → I` (independence) is the honest default — which makes `U`'s interval *narrower than reality* if the true correlations are positive, so GSM additionally reports the interval **both** at `R̂` and at a conservative `R_hi` (off-diagonals at the upper CI of the dCor estimate); a verdict that flips between them is `axis_unseparated`, not decision-grade.
3. **`Σ` does not fix separability — it displays it.** If TRC-P0 fails (F/P/A collinear), `ρ_FPA → 1`, the three pillars carry one piece of information, and `U`'s interval becomes degenerate (the geometric mean of three perfectly-correlated logit-normals). GSM then **correctly reports a near-point posterior with no triadic structure** — the *honest* output, and also the signal that §3–§6 are deleted (§A.0). GSM is **not** a way to rescue a failed separability test; it is a way to *see it in the variance*.
4. **`P_fail` is a model-internal probability, never a physical/hazard probability (O10/O12).** `P(U < φ⁻¹)` is the posterior probability that the *model's stability index* is below threshold given the *belief distribution* — **not** the probability the substance fails in service, decomposes, or detonates. The renderer prints "*posterior probability that the model stability index for substance-type X is below θ = …, model-internal*," never "X has a 30% chance of failing." The φ⁻¹ threshold is a tunable default, not a constant of chemistry (§2.2, §9.10-4).
5. **GSM is gated, B1-pending, and retired if it does not calibrate.** Until GSM-P1 passes, GSM is INTERPRETATION: it may widen intervals and generate "buy-evidence" hypotheses, but **no `P_fail` is rendered decision-grade and no GSM-Priority drives an irreversible action.** The point-SI pipeline (§2.2) remains the gated load-bearing surface; GSM sits *above* it and is removed cleanly (from ledger and renderer, logged in `TRC-CHANGELOG`) if its falsifier fails — symmetric-retirement contract (§8, §9.9).

### 2.9.8 Worked 4×3 example (SCORING-MECHANICS ILLUSTRATION ONLY — ZERO separability/predictive evidence)

> Illustrative numbers, hand-assigned to show the matrix mechanics and the known-low-vs-uncertain split. **No claim** that these are any real substance's values; the §2.8 READ-FIRST banner applies verbatim.

**Means `σ(μ_ij)` (the §2.2 point scores) and per-cell coverage:**

| layer ↓ / pillar → | F mean (cov) | P mean (cov) | A mean (cov) |
|---|---|---|---|
| **L1 design** | 0.80 (0.7) | 0.75 (0.6) | 0.70 (0.5) |
| **L2 synthesis** | 0.72 (0.8) | 0.68 (0.6) | **0.30 (0.85)** ← known-low |
| **L3 use** | 0.85 (0.9) | 0.82 (0.8) | 0.78 (0.7) |
| **L4 society** | 0.60 (0.4) | **0.50 (0.10)** ← neutral-50, sparse | 0.55 (0.3) |

`τ` from §2.9.3 (`τ_floor=0.15, κ=1.0, λ=0.5, ν=0.1`, consensus folded in): the **L2-Action** cell is *tight* (coverage 0.85 ⇒ small `τ`); the **L4-Position** cell is *wide* (coverage 0.10 ⇒ `τ ≥ τ_LOW`). `R`: within-layer `ρ_FPA = 0.5` (positive, as expected pre-data, §2.1), within-pillar `ρ_layer = 0.3`, off-block 0, OAS-shrunk, PSD.

**Monte-Carlo (`K = 50 000`) result (illustrative):**

```
Layer U (median [5%,95%])         P_fail = P(U_i < 0.618)
  L1  0.748  [0.66, 0.82]              0.06     STABLE, tight
  L2  0.520  [0.44, 0.60]              0.97     CRITICAL — driven by the tight low-A cell (non-compensation)
  L3  0.816  [0.75, 0.87]              0.01     STABLE, tight
  L4  0.547  [0.30, 0.74]              0.55     AT-RISK but WIDE — risk is from IGNORANCE, not known collapse
node  0.642  [0.49, 0.74]              0.41     (wgeomean over layers; dragged by L2; widened by L4)
```

**Reading (TESTABLE register, claim-envelope B1-pending).** Two cells are at risk **for opposite reasons**, and GSM says so:

- **L2-Action** — `P_fail ≈ 0.97`, *narrow* interval: the synthesis-Action is **known-low** (a measured, well-covered near-inert step). The non-compensation keystone, applied per draw, collapses the *whole* L2 posterior below `θ` regardless of L2's healthy F and P. **Recommended move:** a Form/Position lever on the synthesis route (a research hypothesis about a *substance type*, never a recipe, §3.3), conditional on TRC-P0.
- **L4-Position** — `P_fail ≈ 0.55`, *wide* `[0.30, 0.74]`: the societal-context cell fired the **neutral-50 default** because the observable was missing (`coverage 0.10`, `LOW_EVIDENCE`). GSM tags it `low_score_cause = evidence_sparse` (§9.8) and renders it **not decision-grade**. **Recommended move (the new affordance):** *buy evidence* — its `GSM-Priority` for "measure the missing L4-context observable / obtain the named-human telos declaration" beats any structural lever because shrinking `τ` there reduces node `P_fail` most per cost.

The renderer prints "*posterior P(model stability index < θ) for substance-type X: L2 ≈ 0.97 (known-low, measured), L4 ≈ 0.55 (wide, low-evidence — not decision-grade), model-internal*"; it **never** prints "X will fail," never compares this `P_fail` to another substance's, and the L4 sign remains a human-declared `T_soc` (§6.2).

### 2.9.9 Falsifier — does GSM's `P_fail` calibrate? (pre-registered, symmetric retirement)

GSM earns its place only if its claimed probabilities are **honest frequencies**. The test is a **reliability diagram**, run at the family-level unit of independence (R8), with study-level FDR (§8). *(This is the §2.9 instance of the §8 falsifier matrix; the GSM-P1/P2 row is mirrored there.)*

| # | Claim under test | Falsifier | Pass → admits | **FAIL → REMOVES** |
|---|---|---|---|---|
| **GSM-P1** | GSM's `P(U < φ⁻¹)` is **calibrated** against external outcomes (predicted failure-probability matches observed failure-frequency), **and** the interval width / `ΔP_fail` localization adds signal over point-SI | bin held-out family-level cases by predicted `P_fail`; the **reliability curve departs from the diagonal** beyond CI, **OR** Expected Calibration Error exceeds a pre-set bound, **OR** the `τ`-driven width carries no information about point-SI's own error (wide intervals are not where point-SI is more often wrong) | GSM admitted as a B1-pending uncertainty layer; `P_fail` and credible intervals render decision-grade under SSS-Guard | **GSM removed from ledger and renderer**; TRC reverts to the §2.2 point-SI pipeline + the inherited neutral-50 / `LOW_EVIDENCE` tags (logged in `TRC-CHANGELOG`) |
| **GSM-P2** | the propagated interval is **link-robust** (logit-normal vs Beta-marginal) and **`Σ`-honest** (verdict stable between `R̂` and conservative `R_hi`, §2.9.7-2) | a verdict (STABLE/AT-RISK/CRITICAL or a leverage target) **flips** under the logit-normal↔Beta swap OR between `R̂` and `R_hi` at achievable family `n` | the distributional verdict is robust to the link/correlation choice | the affected verdict is `axis_unseparated`; GSM renders only the `Σ→0` point fallback for it |

**Reliability-diagram protocol (GSM-P1, the load-bearing test).** Predict `P_fail` for a held-out battery of material classes / reaction families whose **measured** outcomes are known (decomposed/did-not, on-hull/off-hull per ICSD, route succeeded/failed at a recorded yield). Bin by predicted `P_fail ∈ {[0,0.1),…,[0.9,1]}`; plot **observed failure-frequency vs predicted `P_fail`**; a calibrated GSM lies on the diagonal within binomial CI. Report **ECE** and a calibration slope; **the 0.6–0.8 "inconclusive" band discipline (§8) applies** — a slope whose CI cannot exclude "no better than point-SI's implicit 0/1 confidence" is *not* a pass, and a power calc precedes the run (the family-level `n` is the same small budget §8 flags). External truth must pass the **leakage audit (TRC-P0c)** — `P_fail` calibrated against an outcome that leaks from the same DFT features that set `μ`/`τ` is unusable.

**Symmetric retirement.** A failed GSM-P1 **deletes** GSM from the ledger and renderer; the point-SI pipeline (§2.2) and the inherited uncertainty tags survive unchanged. The firewall (§6.4–6.5), the §9.8 lint, and the hazardous-synthesis refusal are **ungated and never retired** — they bind GSM intervals and `P_fail` exactly as they bind point scores.

### 2.9.10 Epistemic status & scope (TRC-specific instance vs canon-general construct)

- **Epistemic level.** GSM is **B1-pending** (true *of the model* — a propagation identity — once GSM-P1 calibrates; INTERPRETATION until then). It makes **no** B2/B3 empirical claim of its own beyond what TRC-P0/P0e/P9 already carry; it **inherits** TRC's B3-pending ceiling and adds no B4 surface. **Any B4 GSM sentence is a bug** (§9.2).
- **Scope — what is TRC-specific vs canon-general.** The **construct "GSM"** — *a layer×pillar matrix of logit-normal cells under one multivariate normal in log-odds, propagated through `U=∛(F·P·A)` by Monte-Carlo to a credible interval and `P(U<φ⁻¹)`, with evidence-driven diagonal and separability-statistic off-diagonal* — is **canon-general**: nothing in it is chemistry-specific, and it is a candidate to be **lifted to canon (SSS)** as the principled discharge of the SSS-L4 "report confidence separately" open problem, applicable verbatim to TRB (organism layers) and TSE (the A×B dual axis). The **instance documented here** — the 4 layers = {design, synthesis, use, telos}, the `τ`-from-chemistry-coverage map, the `E_hull`/formation-energy provenance feeding `ν`, the L4 sign-not-modelled rule — is **TRC-specific**. Recommended placement: **add to TRC now (this §2.9, gated by GSM-P1); assess for lifting to canon** once GSM-P1 has passed in **at least two** domains (the cross-domain comparability question is itself SSS-L5, still open). Until then GSM lives in the appendix, not the core.
- **Relation to inherited constructs.** GSM **consumes and does not duplicate**: SSS consensus-%/CI/neutral-50/SSS-L4 (§2.9.6); the §2.2 `δ`/`SI`/`evidence_coverage`/`LOW_EVIDENCE` map (run unchanged per Monte-Carlo draw); the claim-envelope `conf`/`evidence` (the envelope gains a `dist:{link, mu, tau, P_fail, ci90}` block, no new top-level surface, §9.8); the symmetric-retirement contract (§9.9); and the SSS-Guard gate (now also requiring `P_fail` agreement across the 3 instances). It does **not** touch NDT's 4th/5th-currency lift (GSM is orthogonal: it adds *uncertainty over* a `U`, not a new currency *into* `U`, §A.4), the dual-use firewall, or the cross-substance ℳ-/`P_fail`-aggregation prohibition (which GSM strictly preserves, §2.9.5, §6.4).

> **Boxed law (GSM, one line).** *A stability score without its variance hides whether a low number means "known-fragile" or "we don't yet know"; GSM carries the belief distribution through the unchanged non-compensatory keystone so the controller can act on the fragile and buy evidence on the unknown — and is deleted if its probabilities do not calibrate.*

---

## 2.10 The weak-zone scheduler — compute/experiment allocation as multi-agent orchestration

> **Register banner (read first).** This section makes **one** claim, and it is an **AI-orchestration** claim, not a chemistry claim. TRC introduces **no new chemistry**: every estimator the scheduler calls — DFT energy-above-hull, formation energy, NEB/phonon, retrosynthesis search, Ashby indices, standard UQ — is a mature, externally-owned method (§2.5, §4.3, §5.4). What this section claims is that a **triadic orthogonal decomposition (F/P/A × L1–L4) plus a non-compensatory combiner `U=∛(F·P·A)`** lets the *already-built* GSI-RTD scheduler allocate the next agent-call / DFT job / lab experiment **without any bespoke chemistry orchestration**, and that the weakest pillar of the weakest node is a usable **bottleneck/routing signal**. The claim is **B1-pending of the model** (the allocation algebra is a reused identity) and its **value over baselines is B3-pending and conditional on separability (TRC-P0/P0e)** — stated as a falsifiable benchmark in §2.10.7. **If P0 fails, this entire section is deleted with §3–§6 (§A.0): a non-separable F/P/A makes the "weakest-pillar names the agent" signal an artifact, and the scheduler reduces to a fancier scalarization with no edge over a plain BO/active-learning loop.**

### 2.10.0 What is new here, and what is emphatically not (honest positioning)

Multi-agent chemistry AI **already exists and is productized.** ReAct/tool-use LLM agents (ChemCrow), capability-modular planners over real hardware (Coscientist), autonomous self-driving labs with active-learning routing (A-Lab and the Bayesian-optimization SDL family), epistemic-role multi-agent hypothesis engines with a resource-allocating supervisor and Elo ranking (AI co-scientist), and retrosynthesis planners (ASKCOS/AiZynthFinder) all decompose and orchestrate. **TRC does not invent any of that and must not claim to.**

What is *absent* across that prior art — and is the only thing TRC asserts as novel-in-combination — is the pairing of:

1. a **fixed, problem-orthogonal decomposition** in which each cell `(pillar ∈ {F,P,A}) × (layer ∈ {L1…L4})` is a **typed, agent-owned sub-problem with a clean interface** (the §A.3 `TriadicDomain` contract), rather than an *emergent* ReAct split, an *epistemic-role* split (generate/critique/rank), a *capability* split (planner/coder), or a *domain-specific pipeline*; and
2. a **non-compensatory combiner** whose weakest factor both **(i) vetoes the aggregate** (geometric zero, §2.2) **and (ii) names the responsible agent** as the compute-/experiment-routing signal — where the prior art aggregates compensatorily (weighted sums, Pareto, Elo, LLM-judge) or with a bare pass/fail gate.

| System (prior art) | Decomposition axis | Orthogonal F/P/A-like cells? | Non-compensatory + **names the agent**? | Reusable scheduler? |
|---|---|---|---|---|
| ChemCrow (ReAct tool-use) | emergent per-query | no | no (safety gates only) | no |
| Coscientist | capability/role modules | no | no | no |
| A-Lab / BO self-driving labs | recipe parameter vector + acquisition | no | partial gate / weighted-sum / Pareto | no (bespoke) |
| AI co-scientist | epistemic roles + Elo tournament | no | no (compensatory ranking) | supervisor, task-specific |
| Retrosynthesis (ASKCOS etc.) | retrosynthetic tree | no | no (route cost) | no |
| **TRC (this section)** | **F/P/A × L1–L4 typed cells** | **yes (by construction; tested by P0/P9)** | **yes — geometric veto + weak-pillar→agent** | **yes (reused GSI-RTD `TS`, no chemistry glue)** |

> The bridge to self-driving labs is the precise gap in row "A-Lab / BO": those loops route the next experiment by an **acquisition function over a flat recipe space** with a compensatory or pass/fail objective. They have **no triadic bottleneck signal** — nothing that says "the limiting sub-problem is *Position* of *route-step-2*, so dispatch the Position-agent / run the phase-field DFT job, not the kinetics NEB." TRC's contribution is to supply exactly that routing primitive on top of the same estimators. **Whether it beats the BO baseline is unproven until §2.10.7.**

### 2.10.1 The scheduler is reused, not written (the conformance claim)

Per §A.3, TRC is a **conformant `TriadicDomain`**, so the multi-agent scheduler is the **existing GSI-RTD operator**, instantiated on chemistry with zero new orchestration. The domain implements only the contract surface and inherits the rest:

```
TRC supplies (the §A.3 + §2.2 + §4.3/§5.4 + §22.1-cost contract):
    decompose(node)            -> (F, P, A) leaf scores            # §2.2 pipeline
    expected_si(node)          -> E[SI]   (point §2.2  or  GSM posterior §2.9)
    risk(node)                 -> P(U < φ⁻¹)                       # §2.9.5  (or 1−SI fallback if GSM ungated)
    cost(node, move)           -> (C_time, C_space, C_energy)      # §22.1 cost-triad
GSI-RTD supplies (reused verbatim, no chemistry inside):
    TS : {nodes} × Budget -> Queue ⊂ {nodes}                       # the scheduler operator
    TAA pillar-agents (role ∈ {form, position, action, generalizer})
    the LGP-12 / 4-phase cycle  +  the generation loop
    the β structural-similarity transfer rule  +  the learning law
```

The cost triad is itself triadic — `C_time` is the Form cost, `C_space` the Position cost, `C_energy` the Action cost — so an estimator's price is booked on the same axes it informs. **A "DFT job," an "agent-call," and a "lab experiment" are all just `moves` with a `cost(node, move)` and an expected effect on `expected_si`/`risk`;** the scheduler does not distinguish them except by price and payoff. That is what makes the *same* operator schedule simulation budget at L1/L2 and physical experiments at the self-driving-lab boundary.

### 2.10.2 The allocation rule — steepest-`U`-ascent on the weakest pillar of the weakest node, under cost

The selection is the **two-stage GSI-RTD `TS`**, mapped onto TRC primitives. The first stage is the non-compensatory veto; the second is the leverage rank. Both already exist (§3.5/§4.5/§5.6 do the per-layer version; this is the cross-layer scheduler that drives *which* node-cell gets the next move).

**Stage 1 — hard gates (non-compensatory at the gate; any failure → drop the candidate move).** Mapping the GSI-RTD gates G1–G4 to TRC:

```
G1   E[SI](node)         ≥ θ_SI            (default 0.15)        # don't spend on hopeless nodes …
G2   risk(node)          ≤ θ_R             (default 0.85)        #   … unless (see force-promote) it is a CRITICAL serial key
G3   cost(node, move)    ≤ budget_remaining  on ALL THREE axes  # §22.1 triadic budget, every axis
G4   min(F, P, A)(node)  >  0   over LEAVES (§2.2 leaf set)      # PILLAR-COLLAPSE GATE — the weakest-pillar veto
```

> G4 is the keystone, stated on the **leaf** set (§2.2 δ-fix): a node with an internally collapsed pillar (`q=0.01,c=1 ⇒ P≈0.1`) is *not* schedulable as "balanced-low." `LOW_EVIDENCE` cells (coverage `<0.3`, §4.3) do **not** trip G4 — a missing observable is `UNKNOWN`, never `0` (open-world guard) — they instead become high-priority **buy-evidence** moves in Stage 2.

**Stage 2 — leverage rank = steepest-`U`-ascent per unit cost.** Among gate survivors, the scheduler maximizes the expected **gain in the node's stability per unit triadic cost**, which is identically the §3.5/§4.5 leverage primitive lifted to the scheduler and (when GSM is gated) re-stated on risk reduction (§2.9.5):

```
                  E[ ΔU(node) | apply move ]                E[ ΔP_fail(node) | apply move ]      (GSM form,
Priority(move) =  ───────────────────────────     ≡        ───────────────────────────────       §2.9.5)
                   ∛( C_time · C_space · C_energy )           ∛( C_time · C_space · C_energy )

   subject to:   move acts ONLY on  weak_pillar(node) = pillar_owning(argmin_leaf(node))   (axis-matched, §3.5)
   tie-break:    cheapest ∛-cost  →  then highest E[SI]  →  then redundancy-discounted (×(1−Redundancy)^γ)
   force-promote: a CRITICAL serial key step (one non-negotiable bond/phase) bypasses G1/G2 cost-ranking (§3.3, §4.5)
```

Two facts make this "steepest-`U`-ascent on the weakest pillar," not just an acquisition function:

- **Why the weakest pillar is the steepest direction.** Because `U=∛(F·P·A)`, the partial derivative `∂U/∂(pillar) = U/(3·pillar)` is **largest for the smallest pillar.** Per unit improvement on a leaf, the marginal `U`-gain is greatest on `argmin`. So "raise the weakest pillar" is **not a heuristic — it is the gradient-ascent direction of `U`** (this is the algebraic content of GSI-RTD §LGP-5 "steepest ascent in triadic space," §546, instantiated). A compensatory weighted sum has constant partials and therefore **no** such bottleneck direction — which is exactly why the prior-art BO/weighted-sum loops cannot emit this signal.
- **Why it is non-compensatory across nodes too.** The *weakest node* is selected first (lowest `E[SI]` among gate survivors that are still recoverable), and within it the *weakest pillar*; a strong pillar elsewhere cannot buy down the queue position of a collapsed one. This is the cross-layer analogue of the per-layer "a strong pillar cannot rescue a collapsed one."

**The routing readout (the named-agent signal).** The scheduler does not return a scalar; it returns a **typed dispatch**:

```
weak_pillar(node) = F   →  dispatch FORM-agent     →  move ∈ {structure/scaffold/phase edit, formation-energy DFT, phonon/Born check}
weak_pillar(node) = P   →  dispatch POSITION-agent →  move ∈ {phase-field / E_hull / Pourbaix / μ-window DFT, solvent/context re-select}
weak_pillar(node) = A   →  dispatch ACTION-agent   →  move ∈ {ΔG_rxn / NEB barrier calc, alternative disconnection, lab kinetics run}
low_score_cause = evidence_sparse  →  BUY-EVIDENCE move (measure the missing observable / run the one experiment), §2.9.5
high δ⋆ (no single argmin)         →  GENERALIZER (Σ) re-couples; no single-pillar move dispatched
```

This is the bridge claim made concrete: where A-Lab's decision layer asks "which recipe next?", the triadic scheduler asks "which *axis* of which *node* is binding, and what is the cheapest move that lifts it?" — and the answer **names the owning agent and the class of estimator/experiment to run.**

### 2.10.3 The closed loop — scan → route → agent acts → re-score → learn

The macro-loop is the GSI-RTD generation loop (§23.1) and the per-node loop is the TAA 4-phase / LGP-12 cycle (DZ-1…DZ-12 in §3.3); both are **reused, not authored.** One generation:

```
 ┌──────────────────────────────────────────────────────────────────────────────────────┐
 │  TRC WEAK-ZONE SCHEDULER LOOP  (one generation g)                                       │
 │                                                                                         │
 │  (1) SCAN     every active node n:  decompose→(F,P,A); E[SI](n); risk(n)=P(U<φ⁻¹)      │
 │               pillar-agents run Phase-I reconnaissance IN PARALLEL, NO CROSS-TALK       │
 │               (shared-nothing; only the Σ/generalizer sees all three reports)           │
 │                     │                                                                   │
 │  (2) ROUTE    TS:   Stage-1 hard gates G1–G4  →  survivors                              │
 │               Stage-2 Priority = E[ΔU]/∛(cost)  on weak_pillar(weakest node)            │
 │               → ExecutionQueue of typed dispatches  (axis-matched; §2.10.2)             │
 │                     │                                                                   │
 │  (3) ACT      the named agent runs ONE move  (agent-call │ DFT job │ lab experiment)     │
 │               under the triadic budget; CRITICAL serial key is force-promoted           │
 │                     │                                                                   │
 │  (4) RE-SCORE re-run §2.2 / §2.9 on the touched node;  recompute U, δ⋆, SI, P_fail      │
 │               KEEP-RULE (TSE twin):  accept the move iff ΔU > 0 in a held-out twin;     │
 │               else revert (no compensation laundering)                                  │
 │                     │                                                                   │
 │  (5) LEARN    budget.deduct(cost);  impact^(g+1)=(1−λ)impact^(g)+λ·observed_SI;         │
 │               policy:  ε-greedy(g≤5) → UCB1(6–20) → Thompson(20+);                       │
 │               β-transfer priors across SLICES OF ONE DESIGN PROGRAM ONLY (firewall)     │
 │                     │                                                                   │
 │  HALT (Prop. 22.1): run only if a queue exists with coverage ≥ θ_cov, cost ≤ budget on  │
 │  all 3 axes, SI ≥ θ_stab;  else DECOMPOSE the goal further (do not run).                 │
 └──────────────────────────────────────────────────────────────────────────────────────┘
```

```python
# The loop is the reused gsi_runtime; only the four contract methods are TRC's.
def trc_generation(nodes, budget, kb):
    # (1) SCAN — pillar-siloed, parallel, shared-nothing
    for n in nodes:
        n.F, n.P, n.A = decompose(n)                 # §2.2 leaf pipeline (jury reserved for top-K)
        n.esi  = expected_si(n)                       # point SI (§2.2) or GSM posterior (§2.9)
        n.risk = risk(n)                              # P(U < φ⁻¹) (§2.9.5) or 1−SI fallback
    # (2) ROUTE — the reused two-stage TS
    survivors = [n for n in nodes if hard_gates(n, budget)]      # G1–G4; G4 = min-leaf > 0
    def priority(n):
        wp   = pillar_owning(argmin(leaves(n)))                   # weakest pillar = steepest ∂U
        move = cheapest_axis_matched_move(n, wp, budget)          # FORM/POSITION/ACTION/BUY-EVIDENCE
        dU   = expected_delta_U(n, move)                          # steepest-U-ascent numerator
        c    = cost(n, move)                                      # (C_time, C_space, C_energy)
        return (dU / geomean(c)) * (1 - redundancy(n))**GAMMA, move
    queue = sorted(((priority(n), n) for n in survivors),
                   key=lambda x: x[0][0], reverse=True)
    queue = force_promote_critical_serial_keys(queue)            # §3.3/§4.5
    # (3) ACT + (4) RE-SCORE — one move, twin keep-rule
    for (score, move), n in queue:
        if not budget.affordable(move): continue
        result = dispatch_agent(move)                            # agent-call | DFT | lab experiment
        n_new  = rescore(n, result)                              # §2.2/§2.9
        if delta_U_in_twin(n, n_new) > 0: commit(n_new)          # else revert — no compensation
        budget.deduct(cost(n, move))                             # (5) LEARN ↓
        kb.update_impact(n, result, lam=0.3); kb.step_policy(g)  # ε→UCB1→Thompson
    return halt_or_next_generation(nodes, budget)                # Prop. 22.1
```

> **The whole point, restated:** TRC writes the four bracketed contract methods and inherits the loop. There is **no** TRC-specific scheduler, queue, agent-router, budget, transfer, or learning code. That is the "conformant domain" payoff (§A.3) — and it is also the **liability**: every property below is only as good as the §2.2 scores fed in, which are only meaningful if P0 holds.

### 2.10.4 Why a triad helps multi-agent AI specifically (the four mechanisms, each conditional)

1. **Clean parallelism (Phase-I).** The three pillar-agents scan a node **independently, no cross-talk, shared-nothing** (only Σ aggregates). Sync is at generation barriers, giving `O(sync_points × N)` coordination, not `O(steps × N²)`. **Conditional on P0:** if F/P/A are entangled, the agents' interfaces *leak* — the Form-agent's output depends on the Position-agent's intermediate state — and the shared-nothing model breaks (you are forced back to a single coupled solver). Separability is the *precondition* for the parallelism, not a bonus.
2. **The bottleneck names the agent (routing).** `argmin`-leaf → owning pillar → owning agent → estimator class. A monolithic agent must *discover* the bottleneck by trial; the triadic decomposition *reads it off the score*. **Conditional on P0/P1:** the named axis is only the real mechanism if proxy-axing is stable (TRC-P1, O8-CHEM); otherwise it is "δ-spike, axis TBD."
3. **Interpretable, uncertainty-aware aggregate (active learning).** `risk = P(U<φ⁻¹)` and `GSM-Priority` distinguish **known-low** (act structurally) from **high-variance** (buy evidence) — the genuinely new affordance over a bare acquisition function, which treats both identically. **Conditional on GSM-P1 calibrating** (§2.9.9); ungated, the loop falls back to the point-SI scan.
4. **Zero bespoke orchestration (reuse).** The conformance claim (§2.10.1). **Unconditional of P0** (it is true of the model regardless), but **worthless if P0 fails**, because there is then nothing worth orchestrating triadically.

### 2.10.5 The firewall binds the scheduler (no new surface)

The scheduler is **sign-symmetric** (a leverage-finder; §9.7), so the firewall constrains it exactly as it constrains the point-SI scan, with **no exception for being "just a scheduler":**

- **No cross-substance triage.** `Priority` ranks **moves within ONE declared node/design program** only. There is **no** cross-substance / cross-task `Priority`, `ΔU/cost`, or `ΔP_fail/cost` queue — that operation does not exist (O5b-chem, §6.4): a cross-substance `Δℳ/cost` ranking reconstructs the worth ordering without the word "worth." β-transfer priors move **only across slices of one program** (§3.3 DZ-12).
- **Type-forbidden targets are never queued.** Deny-listed objectives (§6.5) are dropped at the lint **before** scoring (DZ-1/DZ-3); the scheduler never enumerates, ranks, or routes toward them. The incidental-discovery halt fires inside the loop.
- **No autonomous action (B4 empty).** "Lab experiment" as a `move` is **human-in-the-loop, human-on-top** (§9.4): the scheduler emits `queue_for_lab`, never an executed synthesis. SSS-Guard (≥2-of-3 + external metric) gates the *recommendation*, not an actuator. Any real wet-chemistry dispatch is a **new B4 project**, outside this plan. The bridge-to-SDL claim is therefore a claim about *routing logic*, **not** a claim that TRC drives a robot.

### 2.10.6 Failure modes of the scheduler (named, with guards)

| # | Failure mode | Symptom | Guard (reused) |
|---|---|---|---|
| **SCH-1** | **Separability leak (the dominant risk)** | weak-pillar signal flips under proxy reassignment; parallel agents need cross-talk | TRC-P0/P0e/P1; on fail → §3–§6 deleted, scheduler reduces to flat-space scalarization (no claimed edge) |
| **SCH-2** | **Look-elsewhere on `argmin`** over 10⁴–10⁶ candidates | a "weakest node/cell" flag is search noise | empirical null at the unit of independence (family/system, **never the row**, R8) + FDR q-value on every dispatch (§3.5, §4.5) |
| **SCH-3** | **Reward hacking via compensation** | a move raises mean `U` by padding a strong pillar | axis-matched constraint (move acts only on weak pillar) + twin **keep-rule** (commit iff held-out ΔU>0) |
| **SCH-4** | **Greedy myopia** | steepest-ascent stalls in a local weak-zone | optional MCTS/UCB1 upgrade (GSI-RTD §20.4bis, `O(√(T ln T))` regret); policy schedule ε→UCB1→Thompson |
| **SCH-5** | **Negative β-transfer** | SI_with_transfer < SI_without for ≥5 candidates | set β=0, flag domain pair non-isomorphic (GSI-RTD FM-7); on distribution shift β→0.1 (FM-4) |
| **SCH-6** | **`LOW_EVIDENCE` mis-veto** | a missing observable scored 0 trips G4 | open-world guard: missing → `UNKNOWN`/neutral-0.5, becomes a buy-evidence move, never a collapse |
| **SCH-7** | **`P_fail` over-trust** | routing on an uncalibrated posterior | GSM gated by GSM-P1; ungated → point-SI fallback, no `P_fail`-driven irreversible move (§2.9.7-5) |

### 2.10.7 Falsifier — does triadic scheduling actually beat the baselines? (pre-registered, symmetric retirement)

> The value claim of this section is **unproven until this test passes.** It is the scheduling analogue of TRC-P2/P4 and inherits the §8 discipline verbatim: conditional dCor/CMI never Pearson; the **0.6–0.8 band is "inconclusive → never a pass";** unit of independence = chemical system / reaction family / materials chemical-system **never the candidate row** (R8); a **power calc precedes the run**; study-level FDR.

**The benchmark (head-to-head, same task, same tools, same budget).** Fix a closed-loop discovery/selection task with a **measured external outcome** and a **fixed estimator/experiment toolset** (e.g. an A-Lab-style solid-state synthesizability panel with held-out ICSD/ORD outcomes, or a materials-selection panel with held-out service-failure data). Hold the tool *implementations* identical across arms; vary only the **orchestration/aggregation discipline**:

| Arm | Decomposition | Aggregation / routing | Role |
|---|---|---|---|
| **B0 — monolithic ReAct** | none (emergent) | LLM-judge "done?" | ChemCrow-class baseline |
| **B1 — BO / active learning** | flat recipe vector | acquisition fn over **weighted-sum / Pareto** objective | A-Lab / SDL baseline (the bridge target) |
| **B2 — ad-hoc multi-agent** | epistemic roles + Elo/vote | compensatory ranking | AI-co-scientist-class baseline |
| **TRC — triadic scheduler** | **F/P/A × L1–L4 typed cells** | **`U=∛(F·P·A)` veto + weak-pillar→agent routing** | the system under test |

| # | Claim under test | Falsifier | Pass → admits | **FAIL → REMOVES** |
|---|---|---|---|---|
| **TRC-SCH1** | triadic routing reaches the target with **fewer experiments/compute** (or higher hit-rate) than the **strongest** of B0/B1/B2 at equal budget | the budget-to-target / hit-rate CI **includes 0** (no advantage) vs the strongest baseline, at the family unit | the triadic scheduler is kept as a delivered orchestration discipline | **the scheduler claim is retired**; TRC reverts to using B1 (BO/AL) routing on its scores — no orchestration novelty asserted |
| **TRC-SCH2** | the **win is isolated to the bottleneck regime** (one-low-pillar nodes), where non-compensatory routing can differ from an average | no ΔΔ advantage **on the one-low-pillar subset** (away from zeros, steepest-`U`-ascent ≈ acquisition on a smooth objective, so any "win" is from the estimators, not the discipline) | the *discipline* (not the estimators) carries the win | the apparent win is attributed to tooling, not triadic routing → retired as ornamentation |
| **TRC-SCH3** | the named-agent dispatch is **correct** (the flagged pillar is the true binding axis on held-out outcomes) | dispatch label flips under proxy reassignment, or no lift over a base-rate null at AUC ≥ 0.70 (= TRC-P1) | the routing readout is a delivered feature | reverts to "weakest node, axis TBD" — routes by node, not by pillar (the agent-naming value is lost) |

**The honest prior, stated up front.** Two outcomes are *a priori* plausible and the test is built to catch both: **(a)** if F/P/A are entangled (P0 fails), the triadic arm has no clean interfaces, the weak-pillar signal is noise, and it should *lose or tie* B1 — in which case the section is correctly deleted; **(b)** even if P0 holds, away from the one-low-pillar regime `∛(F·P·A) ≈ mean(F,P,A)` and steepest-`U`-ascent ≈ a smooth acquisition function, so any global win could be tooling, not discipline — which is exactly why TRC-SCH2 isolates the bottleneck subset. **The defensible value of triadic scheduling, if any, lives precisely in the near-zero/one-collapsed-pillar regime** — the same regime where the geometric `U` itself earns its keep (TRC-P0b). Outside it, this section honestly expects to tie the baselines.

**Symmetric retirement.** A failed TRC-SCH1/SCH2 **deletes the scheduling-value claim** from the ledger and renderer (logged in `TRC-CHANGELOG`); TRC then keeps the §2.2 scoring but routes with a standard BO/AL loop and asserts **no** orchestration advantage. The firewall (§2.10.5, §6.4–6.5) and the no-autonomous-action rule are **ungated and never retired.**

> **Boxed law (scheduler, one line).** *A triadic decomposition turns "which experiment next?" into "which axis of which node is binding, and what is the cheapest move that lifts it?" — routing the next agent-call / DFT job / lab experiment to the steepest-`U`-ascent on the weakest pillar of the weakest node, with the existing GSI-RTD operator and no bespoke chemistry orchestration; this is genuine value over a flat-space acquisition loop ONLY where F/P/A are separable (P0) and ONLY in the one-low-pillar bottleneck regime, and is deleted if it does not beat the baselines there (TRC-SCH1/2).*

---

## 3. L1 — TRIADIC DESIGN (inverse design & retrosynthesis as triadic search)

> **VISION (B0 — telos, renders no number, not a deliverable).** *"Design is the act of raising a substance's integrated stability ℳ = ∫U dt toward a declared goal."* This orients the objective sign; it ships no number. The deliverable everywhere else is *a ranked, gated, multiplicity-corrected hypothesis queue of candidate (substance, route) pairs*, gated behind §8. (RUO; scope per the canonical banner.)

### 3.1 The two triads of a design — target and route

- **TARGET node** `t = ChemSystem(target)` — *Is this the right structure (F), can it exist and function in the intended use-context/phase (P), and does it do the required job (A)?*
- **ROUTE node** `r = RouteSystem(t)` — *Do the intermediates hold their identity (F), are the required conditions/phases/separations attainable (P), and do the reactions proceed and deliver yield (A)?*

| Pillar (↔ price) | TARGET meaning | ROUTE meaning | Real proxy (target / route) | Failure mode |
|---|---|---|---|---|
| **FORM (↔ Time)** | composition, topology, conformation, crystal/phase identity; persistence | intermediate/product identity integrity; stereochemical fidelity; protecting-group survival | target: SMILES/InChI + bond graph, DFT/MLIP formation energy (**MP/OQMD/ICSD**) ・ route: per-step intermediate stability, e.e./d.r. retention | identity collapse |
| **POSITION (↔ Space)** | phase, solvent, T/P window, lattice/binding-site fit, declared use-context; `E_hull` placement; `P=√(q·c)` | attainability of each step's conditions/medium/separation; reagent availability | target: solvation/lattice fit, convex-hull placement, application envelope ・ route: condition-window feasibility (**ORD / Reaxys-class**), feedstock availability | positional collapse |
| **ACTION (↔ Energy)** | reactivity/function the target must deliver; energy released/absorbed (extent at operating activities, §2.6) | each step proceeding: feasibility, ΔG‡/rate, yield, selectivity, atom/energy economy | target: function metric vs spec ・ route: per-step yield, kinetic feasibility, **thermochemistry (NIST)**, atom economy | functional collapse (off-spec, or a step at catastrophically low extent) |

> **The separability shadow, declared up front.** Many target proxies are *computed from the same structure graph* (DFT formation energy, predicted reactivity, conformer stability). A naïve Action proxy read off the SMILES is **a transform of Form** and is **EXCLUDED from the separability claim**. L1's Action axis is restricted, for the separability test, to **measured-or-independently-simulated** quantities (TRC-P0-CHEM, §8).

### 3.2 The scoring / search algebra (non-compensatory throughout)

Per node the SSS primitives are reused verbatim (`U`, `δ` over leaves, `SI`, `weak_pillar`); pillar scores come from the SSS Stage-2 pipeline (up to 50 AI-jury models score ≈12 falsifiable principles per pillar 0–100 → IQR-filter → weighted per-principle mean → pillar average → ÷100 → geometric mean); Specific mode scores uncovered principles **neutral 50** (SSS-L4); the jury runs **only on a leverage-selected subset**.

**3.2.1 The route is a non-compensatory chain.**
```
U_step_k = ∛(F_k · P_k · A_k)                  per step
U_route  = wgeomean_k( U_step_k, weight_k )     serial AND — one dead step ⇒ U_route → 0
                                                (convergent branches that pool product use reserve-aware OR, TRB §5.2)
```

**3.2.2 The design score — target × route, coupled non-compensatorily (one-directional grounding).** Following the TSE §4.2 one-directional-grounding fix (**no bidirectional fixed point**), the route grounds the target's **synthesizability**, single pass, read-only on the route:
```
U_design(t, r) = ∛( U_target(t) · U_route(r) · F_acc )      a zero in ANY ⇒ U_design → 0
   where  F_acc ∈ {closed, partial, open}                   = catalogue-relative retrosynthetic closure (see honesty rider)
```
> **F_acc honesty rider (critique R3).** Closure on "purchasable/known precursors" is **not a property of the route** — it is a property of a *commercial-catalogue snapshot* (which catalogue, which date, which retro depth). Rendering it as a smooth `∈(0,1]` gave false precision. It is therefore **binned** `{closed, partial, open}` (mapped to `{1.0, 0.5, → low}` for the geometric combine) and tagged `catalogue_relative, non_stationary, snapshot_date` — it is never reported as a continuous score and never as a route property.

`U_route` and `F_acc` are **read** by the design score; `U_target` is computed independently and **not re-written** by the route — so `U_design` is a function of independently-measured inputs and TRC-P2-CHEM can bite. **Compensation is forbidden across the two heads.** Any `(target, route)` ranking is **B3-pending**, tagged `low_score_cause ∈ {evidence_sparse, genuinely_infeasible, lattice_approx, axis_unseparated}`.

**3.2.3 The integrated objective ℳ = ∫U dt (per single declared design only).** On a **single declared clock**, `ℳ + 𝒮 = T` (MMT/MPI-1); the solvency gate `dℳ = 𝟙_solvent(τ)·U_design(τ) dτ` makes degradation first-class. **ℳ is a coverage/stability indicator, never a worth metric, and is never summed/compared/allocated across distinct designs** (the canonical statement of this rule is §6.4). Inverse design maximizes ℳ of *one declared target spec*; ranking *which target a finite budget should fund across distinct programs* is an external governance decision, never an engine output.

### 3.3 Retrosynthesis as triadic search — the LGP-12 design cycle

```
TRC-L1 DESIGN CYCLE  (= LGP-12 over the target×route search)                       register
──────────────────────────────────────────────────────────────────────────────  ────────
DZ-1  SPEC        declare target functional spec + use-context (L3 hook) +          B0 (telos→spec)
                  objective_sign + value_frame + accountable_authority              ← firewall gate FIRST
DZ-2  GENERATE    inverse-design / generative proposal of candidate TARGETS         B3-pend
DZ-3  SCORE-T     score each target F/P/A → U_target, δ, SI; drop type-FORBIDDEN     ← dual-use firewall
                  targets at the lint (§9.7), never enumerate them
DZ-4  RETRO       expand AND-OR retrosynthetic tree per surviving target            HYPOTHESIS
DZ-5  SCORE-R     score each step F/P/A → U_step; roll up U_route (serial AND);      B3-pend
                  resolve F_acc (binned, catalogue-relative)
DZ-6  COUPLE      U_design = ∛(U_target · U_route · F_acc) (one-directional)         B1 (algebra)
                  cross-head compensation REJECTED
DZ-7  WEAK-ZONE   weak_pillar per node; flag CRITICAL / AT_RISK; attach q-value (R7)  ← §3.5
DZ-8  LEVERAGE    Priority = Δℳ / ∛(C_time·C_space·C_energy)  (ties → cheapest)      ← within ONE design only
DZ-9  REDESIGN    axis-matched fix on the weakest pillar (compensation forbidden)    cross-axis move REJECTED
DZ-10 GUARD       SSS-Guard: retrodictive ≥2-of-3 + external metric | prospective    see SSS-Guard
                  → no `pass`, only queue_for_lab. NO autonomous synthesis action.
DZ-11 REPORT      claim envelope per surviving (target, route) — TESTABLE register   B3-pending
DZ-12 LEARN       update step/feasibility priors; ε→UCB1→Thompson; transfer β
                  applied only across slices of ONE design program
```
A CRITICAL serial step (a single non-negotiable key bond-formation) is **force-promoted** regardless of cost.

### 3.4 Tie to generative chemistry / retrosynthesis tools (the proxy sources)

TRC-L1 is a **scoring-and-search wrapper, not a model.** Each tool feeds **exactly one head**, with mandatory `G{src; conf; level; mode}` (accession + version + date):
- **Target generation (DZ-2):** generative molecular models (VAE/diffusion/autoregressive SMILES & SELFIES) and inorganic/materials crystal-diffusion generators — outputs are **candidate Forms**, scored, never trusted.
- **Target Form grounding:** **RDKit**, **PubChem / ChEMBL**, **Materials Project / OQMD / ICSD** (formation energy, convex-hull distance), **NIST** thermochemistry.
- **Retrosynthesis (DZ-4):** template-based/template-free retro predictors and MCTS planners produce the AND-OR tree; **ORD** and **Reaxys-class** corpora supply per-step feasibility/condition/yield **priors**; building-block catalogues resolve **F_acc**.
- **External ground truth (independence-audited, leakage-flagged):** held-out *measured* yields/conditions (ORD), measured synthesizability, measured function (ChEMBL potency, measured material property), convex-hull experimental confirmation (ICSD presence). An SA-style synthesizability heuristic derived from the same fragment statistics that feed the route priors is **leakage and is flagged** (the TRB P0c analogue). Where two proxies trace to one upstream corpus (TRB M-2), they count as one input for separability.

### 3.5 Weak-zone scan + axis-matched redesign (leverage, compensation forbidden)

**Stage 1 — localize.** `weak_pillar = argmin` over leaves; flag **CRITICAL** (leaf ≈ 0 or `SI < 0.38`) and **AT_RISK** (`SI < 0.618`); open-world guard applies. **Stage 2 — leverage rank.** `Priority = Δℳ/∛(C_t·C_s·C_e)`, ties → cheapest; CRITICAL serial-key step force-promoted.

**Redesign is axis-matched — compensation rejected at DZ-9:** Form deficit → scaffold/disconnection edit; Position deficit → re-select phase/solvent/use-context or an attainable condition window; Action deficit → edit for required reactivity or a disconnection whose key step *proceeds at adequate extent*; high-δ → re-couple. Fixing a route problem by improving the target (or an Action deficit with a Form edit) is **rejected** — the geometric mean means a strong pillar cannot rescue a collapsed one.

**Multiplicity discipline (R7/R8).** `argmin` over a 10³–10⁶-candidate enumeration is a **look-elsewhere** problem; required: an **empirical null** resampled at the **unit of independence = reaction family / scaffold series / materials chemical-system, never the molecule-row** (R8), and an **FDR q-value** on every flag; a flag must clear an **absolute** band **and** multiplicity-corrected significance, else "not distinguishable from search noise."

### 3.6 L1 worked example — SCORING-MECHANICS ILLUSTRATION ONLY, ZERO predictive evidence

> **READ FIRST.** Illustrative model-internal scores on a **benign** target, assigned *knowing* the textbook answer; demonstrates internal consistency only, **not** that the engine generates non-obvious correct predictions. No quantities, conditions, or operable instructions appear.

**Target spec:** a thermally stable, solution-processable small-molecule organic semiconductor for a benign electronic use (`objective_sign = stabilize`; `value_frame` research-utility, contested, named authority on file; passes the firewall gate at DZ-1). **Target** `t`: `F_t=0.88`, `P_t=0.74`, `A_t=0.80`; `U_target = ∛(0.88·0.74·0.80)=0.806`. **Retro tree** `r` (3 key steps): step-1 `U=0.82`, step-2 `U=0.41` (low-extent coupling, `A_2=0.30`, weak_pillar=Action), step-3 `U=0.78`; `U_route ≈ 0.58`; `F_acc = closed (1.0)`. **Coupled:** `U_design = ∛(0.806·0.58·1.0) = 0.78` — the leverage scan localizes the binding constraint to **route step-2's Action pillar**, not the cosmetically lower target Position; the correct first move is **route redesign on the Action axis**, and an attempt to "fix" by editing target packing (Position) is **rejected** (step-2 stays at 0.41, `U_route` stays ≈0.58 — the geometric zero bites the unaddressed step). **Twin re-score:** an alternative disconnection lifts step-2 to `U=0.74`; `U_route: 0.58→0.75`; `U_design: 0.78→0.84`. **SSS-Guard:** a held-out ORD reaction-outcome metric *exists* for the alternative coupling class → runs **retrodictive** (≥2-of-3 + external yield metric) → passes as a **B3-pending research hypothesis on a known case.** A genuinely novel disconnection with no external metric emits `UNVALIDATED_HYPOTHESIS` + `queue_for_lab` — **never `pass`.**

**Report (claim envelope, verbatim register):** *"Model flags route step-2 of candidate (target T × route R) weakest on Action (reaction-extent); HYPOTHESIS for study; mechanism-axis conditional on proxy-axing (O8-CHEM). Highest-leverage simulated move (within one design): alternative disconnection on the Action axis. Δℳ>0, keep-rule holds in twin; SSS-Guard retrodictive 2/3 + external ORD metric. Level: B3-pending. Model-internal design-fitness index for an entity-type; NOT a synthesis instruction, NOT actionable chemistry."*

---

## 4. L2 — SYNTHESIS / CREATION: building the most stable substances

> **Layer scope.** L1 designs *what* to make; L2 asks: **given a target substance, how stable is it, and how stable is the route that makes it — and which leaf of which step is the binding constraint?** RUO (scope per the canonical banner); produces stability *scores/rankings over entity-types and digital twins*, never quantities, conditions, or steps. L2 is the **most dual-use-sensitive layer** (firewall §6.5).

### 4.1 The triad registered onto a made substance + its route

| Pillar | Price | What it IS (product) | What it IS (a synthesis step) | Failure mode |
|---|---|---|---|---|
| **FORM (F)** | **Time** | structural identity *and its persistence* (decomposition, polymorphic transition, racemization, corrosion, amorphization) | identity of the intended intermediate/product *as actually formed* (right phase, stoichiometry, no off-target phase) | identity collapse |
| **POSITION (P)** | **Space-context** | the phase/hull placement relative to competitors (`E_hull`); solvation/lattice/interface context; what it is embedded in | the *conditions context* a step requires (phase field, solvent, T–P window, atmosphere, coexisting phases); `P=√(q·c)` | context collapse: the required phase field/window does not exist or is not reachable |
| **ACTION (A)** | **Energy** | reactivity *and the energy budget that maintains/forms it*: the formation reaction's driving force at operating activities, and kinetic accessibility | the step's reaction: adequate driving force at operating activities **and** a clearable barrier (§2.6) | energetic failure: negligible extent at operating activities, or an uncrossable barrier |

**FORM is scored from the *process / first-principles object*, never a registry's nominal definition** (`LATTICE_APPROX`, higher bar) — sharp in materials, where the *nominal* compound and the *phase that actually forms* are different objects (kinetic vs thermodynamic product).

### 4.2 Primitives & the route-level U and ℳ

```
U_product = ∛(F_prod · P_prod · A_prod)                          # the made thing, on the shelf
U_step_i  = ∛(F_i · P_i · A_i)                                    # each step as its own triad
U_route   = geometric weakest-link over serial steps             # AND: one infeasible step zeroes the route
            (reserve-aware OR only where genuinely redundant)
U_made    = ∛( U_product · U_route · U_robustness )               # the L2 verdict on a *synthesized substance*
```
`U_robustness` is the **process-window / yield-robustness** pillar-of-pillars: width of the feasible `(T, P, μ, composition)` window combined with byproduct/competing-phase load (selectivity) — the materials analogue of TRB's δ-penalty. **Computability fix (review B3):** process-window width is **not derivable from the snapshot databases TRC restricts itself to** (it needs a calibrated process model or experimental DoE — the V3 dynamic twin §7 declares non-runnable). Under the snapshot-only constraint `U_robustness` is therefore **`LOW_EVIDENCE` / neutral-0.50, never silently imported from V3**, so `U_made` cannot be scored **decision-grade** until V3 exists — L2 sits **below the deliverable line** with L1's route-search (§7), not above it; the §8 committed product is the separability/baseline battery, not a scored `U_made`. Stability/utility is a **trajectory**: `ℳ_made = ∫₀ᵀ U_made(τ) dτ` (trapezoidal), solvency-gated, `ℳ + 𝒮 = T`; a decomposition/corrosion interval contributes **zero** meaning. Mixed timescales (ms surface reaction vs years of shelf aging) require a **currency-resolved sum** `∑_c ∫U_c dτ`. **`ℳ_made` is per-declared-substance-node, never summed across substances** (§6.4).

### 4.3 Per-node scoring — real, versioned, process-intrinsic proxies

| Pillar | Process-intrinsic proxy (versioned source) | Collapse → ideal anchor |
|---|---|---|
| **FORM / thermodynamic depth** | **formation energy referenced to elements** (fixed-version DFT; **NIST-JANAF/WebBook** experimental ΔH_f as [M] anchor) | shallow/positive elemental-formation energy with low decomposition barrier → 0; deep → 1 |
| **FORM / structural integrity** | computed **phonon stability** (no imaginary modes) and **elastic-tensor Born stability** — a 0 K *necessary, not sufficient* dynamical check; as-formed phase purity (see rider) | dynamically unstable / wrong phase → 0; phonon-and-Born-stable single phase → high (capped, not 1) |
| **FORM / persistence (Time price)** | decomposition onset, polymorphic-transition proximity, corrosion/oxidation susceptibility, aging/racemization | decomposes/transforms within horizon → 0; persistent → 1 |
| **POSITION / locus (q)** | **energy above the convex hull** `E_hull` (eV/atom) — distance to competing phases (the canonical home of `E_hull`, §2.5); which phase field / μ-window the target occupies; lattice/interface compatibility | `E_hull ≥ ~0.1 eV/atom` → 0; `E_hull = 0` (on hull) → 1; `~0.025 eV/atom (≈k_BT@300K)` band = `METASTABLE_BAND` |
| **POSITION / context (c)** | **chemical-potential / environmental reachability** of that window (μ_O–T grand-potential; pymatgen reaction-energy context); atmosphere/solvent compatibility | required μ/context not co-reachable with route → 0; co-reachable → 1 |
| **ACTION / thermodynamic feasibility** | **reaction energy `ΔG_rxn` at operating activities** (§2.6; **NIST-JANAF/WebBook**; **ORD** characterized outcomes as external truth) | negligible extent at operating activities → 0; strongly downhill, well-posed → 1 |
| **ACTION / kinetic accessibility** | **activation-barrier proxy** for the rate-limiting step (NEB/TS `E_a`; nucleation/diffusion-barrier proxy; **synthesizability classifiers** as a learned A-prior; **ICSD "has been made" flag** as a weak [M] anchor) | uncrossable barrier / unsynthesized-low-score → 0; low barrier, ICSD-attested → 1 |

> **Phonon/Born rider (critique C7 + review M1).** A phonon/elastic-stability check is a **0 K computational necessary condition, not the empirical persistence** the Form/Time price captures: DFT artifacts produce spurious small imaginary modes for some *real* materials, and many dynamically stable structures are never synthesizable. It is therefore one capped input to `f.structural_integrity`, never equated with "structural integrity," and never a substitute for the measured persistence proxy. **Metastable-by-design fix (review M1):** a 0 K phonon/Born check rewards the *ground-state* structure, which is frequently the **wrong** phase for the application — TRC's own flagship Fe₃C, and diamond, hardened steels, retained austenite, and many battery cathodes, are kinetically-trapped above-hull phases whose function *depends* on metastability. Capping the input does not fix the **sign** of this error. Therefore, for any node flagged `METASTABLE_BAND` / metastable-by-design (§4.3 locus row), `f.structural_integrity` is **down-weighted or excluded** and persistence is carried by the measured `f.kinetic_persistence` (trap depth, §2.8) instead — otherwise the proxy systematically penalizes exactly the materials the framework most wants to score well.

> **Anchors are the most consequential free parameters (single canonical statement; see also §9.10-4).** `ref_lo/ref_hi` are *exactly where the geometric zero bites* — system-, functional-, and **database-correction-scheme**-specific, **not constants of chemistry.** An `E_hull` from a GGA(+U) set is not comparable to an r²SCAN or experimental hull, and **a compound on-hull in Materials Project can be off-hull in OQMD/AFLOW by more than 0.05 eV/atom purely from differing elemental-reference and anion-correction schemes** — so robustness must include **cross-database** perturbation (TRC-P0b), not only ±20% on a single anchor. Every anchor records `G{src;version;functional;correction_scheme}`. A "geometric beats baseline" win that vanishes under anchor, functional-form, OR cross-database perturbation is an **artifact, not a finding.** *Missing-data discipline (SSS-L4/Mode-B):* an unmeasured observable → neutral **0.50**, never dropped; coverage `< 0.3` → `LOW_EVIDENCE`, excluded from any irreversible ranking. The SSS jury is **reserved for top-K leverage / at-risk nodes**.

### 4.4 The node & route model — one recursive node, one axis per edge

A synthesized material *and* its route share one universal recursive `ChemSystem` node (`F{} P{} A{} G{}` + state `s`); `d ⇒ 3^d` subsystems, never enumerated. A **synthesis plan** is a DAG of step-nodes, each its own F/P/A triad. Edge axis-loading: `IS_PHASE_OF / COMPOSES / POLYMORPH_OF` → Form; `COEXISTS_WITH / IN_PHASE_FIELD / ON_HULL_WITH / INTERFACES_WITH / EMBEDDED_IN` → Position; `REACTS_TO / TRANSFORMS_TO / CATALYZES / DECOMPOSES_TO` → Action; `DESTABILIZES` (per-target) decomposed into F/P/A. *Independence caveat (TRB M-2):* when a `COEXISTS_WITH` (Position) and a `REACTS_TO` (Action) edge are **both derived from one DFT phase-diagram computation**, they are correlated by construction and excluded from the separability claim. Open-world guard as §2.7.

### 4.5 L2 weak-zone scan — which step's leaf is the binding constraint

Stage 1: `weak_leaf = argmin`; flag CRITICAL / AT_RISK; a missing phase → UNKNOWN, never FORBIDDEN. Stage 2: `Priority = Δℳ/∛(C_t·C_s·C_e)`; a CRITICAL serial step is force-promoted. Intervention is **axis-matched, compensation forbidden**: Form→change target phase/polymorph or stabilize identity; Position→change environment/phase context so the window exists; Action→a different formation reaction / driving-force or barrier change (a catalyzed pathway *as a scoring target*, never a procedure); high-δ→re-couple.

> **Worked example — choosing the most stable route to a target oxide (SCORING-MECHANICS ILLUSTRATION ONLY; NO conditions disclosed).** Three candidate routes to one **on-hull** target phase (high `F_prod` for all). The L2 question is which *route* is most stable to make, and where each is fragile.
>
> | Route | F_step (worst) | P_step (worst) | A_step (worst) | U_route | δ (leaf) | SI | weak pillar | verdict |
> |---|---|---|---|---|---|---|---|---|
> | **R1** direct | 0.90 | 0.88 | **0.20** (rate-limiting step: uncrossable barrier in the accessible window) | **0.499** | 0.78 | 0.157 | **Action** | **CRITICAL** — kinetic dead step |
> | **R2** mediated | 0.85 | **0.30** (an intermediate's required phase window does not co-reach the next step's context) | 0.80 | **0.586** | 0.65 | 0.215 | **Position** | **CRITICAL** — context gap |
> | **R3** balanced | 0.78 | 0.75 | 0.72 | **0.749** | 0.08 | 0.749 | — (balanced) | **STABLE** |
>
> The arithmetic mean would rank R1 (0.66) and R3 (0.75) close and call R2 (0.65) worst. The **geometric, non-compensatory** score reports R1 and R2 both **CRITICAL** despite respectable averages — each has *one collapsed leaf* an additive score launders away. **R3 is the most stable route** because its leaves are jointly paid and balanced (δ=0.08; the SI over-penalty fix keeps SI≈U since no leaf is near-collapse). *Honesty riders:* (i) the barrier proxy `A_step` is frequently a learned synthesizability score or NEB on a model surface, **not a measured barrier** — so "R1 is Action-limited" reintroduces the DFT-from-one-object circularity that TRC-P2 must test against measured/ICSD outcomes; (ii) every flag carries a **multiplicity-corrected q-value**; (iii) **no conditions, temperatures, quantities, or procedures appear.**

**Multiplicity (R7/R8):** Stage-1 extreme-value over **10⁴–10⁶** candidates is a look-elsewhere problem; required: empirical null at the **unit of independence = chemical system / phase diagram / source-dataset / synthesis-campaign, never the candidate row**; **FDR** across the whole scan; effect size **AND** significance jointly, else "not distinguishable from scan noise."

---

## 5. L3 — EXPLOITATION / USE: materials selection by triadic fit

> **Layer scope.** L3 takes the substance as given and asks: **of the materials that already exist, which is the *most stable to USE* for a declared task?** RUO (scope per the canonical banner); produces **no safety certification, no fitness-for-service sign-off**; "selection / fit / use" denote *simulated rankings of material-types against a declared task, addressed to engineers about trade-offs*, never an autonomous specification of a load-bearing part.

> **The most stable use is the material whose intrinsic Form, use-Position, and delivered Action jointly maximize `U(task) = ∛(F_fit · P_fit · A_fit)` — non-compensatorily — for that task.** A material excellent on two pillars and collapsed on the third is *unfit*, because the geometric mean zeroes it.

All three pillars are **task-relative** — properties of the *(material, task)* pair, not the material alone — which is exactly what makes "wrong material" a *zeroed pillar*, and which is also the orthogonality threat declared in §2.1 (Action and Position both carry the task variable).

### 5.1 The triad registered onto USE — three task-relative fits

| Pillar (task-fit) | What it measures in USE | Price | Material-science content | Failure mode |
|---|---|---|---|---|
| **FORM_fit (F)** | does intrinsic structure & properties meet the task's Form-demand (stiffness, hardness, toughness, strength, density, conductivity, transparency)? **+ does Form persist over use-life?** | **Time** (corrosion, fatigue, creep, wear, embrittlement, ageing) | property vector from Materials Project / MPDS / MatWeb / Granta-style; durability from corrosion/fatigue/creep data | property shortfall *or* in-service identity loss |
| **POSITION_fit (P)** | does the use-environment/context suit the material — T, atmosphere, chemical contact, mounting, adjacency, regulatory/contact constraints? `P=√(q·c)` | **Space-context** | service conditions vs stability window (Pourbaix/Ellingham, service-T limits, contact compatibility, food-/bio-contact compliance) | context exclusion: the environment forbids or destroys the material |
| **ACTION_fit (A)** | does the material perform the named function — and how efficiently (energy/work per unit function)? | **Energy** | function-specific performance index (Ashby index `M`); energy cost of the function | functional failure: cannot do the thing, or at prohibitive energy cost |

The same material scores differently for different tasks: copper is `A_fit ≈ 1` for a busbar and `A_fit ≈ 0` for a cutting edge.

### 5.2 Selection primitives & the time-integrated objective

`U(task) = ∛(F_fit·P_fit·A_fit)`, `δ` over leaves, `SI = U/(1+δ⋆)²`, `weak_pillar = argmin`. Bands are **task-tunable defaults** (SI ≥ 0.618 Fit · 0.38–0.618 Marginal · <0.38 Unfit); high-consequence tasks raise θ (structural/pressure-bearing/implant → θ ≥ 0.90). Use is a **trajectory**: `ℳ(material|task) = ∫₀^{T_service} U(task,τ) dτ` (trapezoidal), solvency-gated, `ℳ + 𝒮 = T_service`. **`ℳ(material|task)` is a per-(material, task) fitness indicator, never a worth ranking over materials in the abstract** (§6.4).

### 5.3 The Ashby connection — the HONEST baseline is constraint-screened Ashby (critique M1)

> **Correction of the earlier strawman.** Competent Ashby selection is **NOT** a bare weighted sum. It is **constraint-screen-then-objective**: hard constraints (a fracture-toughness floor, a service-T limit, a food-contact requirement) are applied as **screening boxes that eliminate candidates** *before* any performance-index ranking. **That screening step is already non-compensatory** — it is precisely how real practice kills a glass knife (a toughness-floor violation), not a weighted sum laundering it. So TRC's L3 novelty is **narrow**: it claims only that folding the screen *and* the index into a single **continuous, leaf-level geometric `U`** (i) gives a graded, leverage-localizable "which axis is binding" signal where the binary screen gives only pass/fail, and (ii) avoids a *post-screen* compensatory weighted sum among the survivors.

```
Ashby (honest baseline):  screen on hard constraints (NON-compensatory)  →  rank survivors by  M (often via weighted sum)
TRC L3:                   one continuous non-compensatory  U = ∛(F_fit · P_fit · A_fit)  with leverage localization
```

The Ashby index `M` lives **inside `A_fit`** (and partly `F_fit`); Ashby's binary constraint-screen becomes the **continuous Position/Form pillars**; Form-durability is Ashby's objective-over-life made explicit via `ℳ = ∫U dt`. **Divergence declared on purpose:** the testable payload is whether continuous geometric `U` beats **constraint-screened Ashby with a post-screen weighted-sum index** at rejecting two-strong/one-marginal candidates and at correctly localizing the binding axis on held-out service-failure data (TRC-P4). **If it does not beat the constraint-screened baseline, L3 is retired to constraint-screened Ashby** — and the honest expectation, stated up front, is that much of the "non-compensation novelty" is already delivered by the screen, so the win (if any) is in the *graded localization*, not the veto.

> **Ashby-index derivation rider (critique M3).** An Ashby index (e.g. `M = E^{1/2}/ρ` for a light, stiff beam) is *derived* by eliminating a free variable under a stated constraint — so **which `M` applies is fixed by the task geometry (a Position fact)**. `A_fit` therefore declares, per task, the constraint and free variable, selects the corresponding `M`, and normalizes `M` to `[0,1]` against task-relative anchors (`ref_lo` = the index value that fails the spec; `ref_hi` = the best attainable in the candidate set). This entanglement of `M`-selection with the task is itself part of the Action/Position orthogonality threat (§2.1).

### 5.4 Per-pillar scoring (task-relative anchors)

Each raw property is normalized against **task-relative anchors** (`ref_lo` = collapse *for this task*, `ref_hi` = fully satisfied). Sources: Materials Project / OQMD / AFLOW / NOMAD (computed, cross-database-perturbed); MatWeb / MPDS / NIST / Granta-class (measured handbook); NIST corrosion/fatigue/creep; Ashby process charts; NIST-JANAF / Ellingham, computed Pourbaix, FDA/EU food-contact lists, ISO 10993 biocompatibility, building/pressure codes (context); the Ashby index `M` + energy-per-function (Action). **Anchors are the most consequential free parameters** (§4.3 canonical statement). Missing property → neutral 0.5 (`LOW_EVIDENCE` if coverage < 0.3); SSS jury reserved for top-K / near-boundary candidates.

### 5.5 Worked example — the steel knife (SCORING-MECHANICS ILLUSTRATION ONLY)

> **READ FIRST.** Consistency illustration on a textbook-known case; proxies were assigned *knowing* steel is the right kitchen-knife material. **This proves only that a hand-assigned 0.05 yields a low geometric mean — it is tautological and carries ZERO predictive evidence.** The only non-tautological content is the *directional* property gap (glass `K_IC ≈ 0.7` vs steel ≈ 50 MPa·m^½; lead's food-contact toxicity). The evidence claims L3 makes live in TRC-P0/P0b/P4.

**Task `t`:** *cut bread in a domestic kitchen over a multi-year service life.* Form-demand: hardness (~6–7 GPa), enough fracture toughness to survive drops/lateral loads, corrosion resistance. Position: wet, mildly acidic, intermittent; **food-contact (hard constraint)**; hand-held; dishwasher cycling. Action: sever crust + crumb at low cutting energy, repeatably, holding an edge.

| Candidate | F_fit (property · durability) | P_fit (locus · context) | A_fit (cutting) | U(task) | δ (leaf) | SI | Verdict |
|---|---|---|---|---|---|---|---|
| **Martensitic stainless (e.g. AISI 420 / X50CrMoV15), hardened** | 0.90 | 0.93 (forgeable; food-contact compliant; survives wet/acid) | 0.88 (keen edge; low cutting energy) | **∛(0.90·0.93·0.88) = 0.903** | 0.054 | **0.903** | **Fit** ✓ |
| **Soda-lime glass "knife"** | **0.05** (hard ~5–6 GPa but `K_IC ≈ 0.7 MPa·m^½` — *toughness fails the constraint screen*; shatters) | 0.70 | 0.60 (sharp initially) | **∛(0.05·0.70·0.60) ≈ 0.30** | 0.93 | **0.080** | **Unfit** ✗ — F_fit toughness-floor violation |
| **Lead "knife"** | 0.10 (far too soft, ~0.04 GPa) | **0.0** (lead = **food-contact toxicity veto** — constraint-screen exclusion) | **0.05** (cannot hold an edge) | **∛(0.10·0.0·0.05) = 0.000** | 1.0 | **0.000** | **Unfit** ✗ — Position veto AND Action collapse |

**What the triad does (relative to the HONEST baseline).** A **constraint-screened Ashby selector would *also* kill the glass knife** (toughness-floor violation) and the lead knife (food-contact exclusion) — that veto is **not** TRC's novelty. TRC's narrow added value, *if TRC-P4 supports it*, is that the same continuous `U` (a) reports `weak_pillar = Form (toughness)` and `weak_pillar = Position (food-contact)` as **graded, leverage-rankable localizations** rather than a binary screen result, and (b) refuses a *post-screen* weighted sum among survivors. The **steel wins** by being the only candidate **simultaneously solvent in all three prices** — Time (holds its edge, resists corrosion → high `ℳ`), Space-context (food-safe, survives the wet kitchen), Energy (cuts at low work). The renderer prints *"model selection-fitness index for material-type AISI-420 against task=kitchen-bread-cutting, model-internal, NOT a fitness-for-service certification,"* never "this knife's stability is 0.90."

### 5.6 Mismatch detection — the wrong material as a zeroed pillar

```python
def detect_mismatch(material, task):
    F, P, A = fit_scores(material, task)            # task-relative, §5.4
    leaves = leaf_scores(material, task)            # f.*, q, c, a.*
    U  = (F*P*A) ** (1/3)
    d  = (max(leaves) - min(leaves)) / (max(leaves) + 0.01)
    dstar = d if min(leaves) < 0.5 else 0.0
    SI = U / (1 + dstar)**2
    wp = pillar_owning(argmin(leaves))
    if violates_hard_constraint(material, task):    # food-contact toxicity, code non-compliance, toughness floor
        return Mismatch(class="CONSTRAINT_SCREEN_VETO", pillar=wp, U=0.0)   # the Ashby screen, made continuous
    if SI < 0.38:   return Mismatch(class=f"{wp}_COLLAPSE", pillar=wp, U=U, SI=SI)   # Unfit
    if SI < 0.618:  return Mismatch(class=f"{wp}_MARGINAL", pillar=wp, U=U, SI=SI)   # Marginal
    return Fit(U=U, SI=SI, weak_pillar=wp)
```

Mismatch classes carry **axis-matched, compensation-forbidden** remedies: FORM_COLLAPSE (property) → change grade / heat-treat / alloy; FORM_COLLAPSE (durability) → coating / corrosion-resistant grade / shot-peening; POSITION (veto/collapse) → change context or context-fit; ACTION_COLLAPSE → a material with the right index `M`; COUPLING (high δ⋆) → rebalance. **Open-world guard:** property-not-in-DB → `UNKNOWN`/`LOW_EVIDENCE`, never "fails"; only a positively-contradicted constraint vetoes. **Multiplicity (R7/R8):** empirical null at the **unit of independence = material family / alloy system / supplier-lot, never the datasheet row**; FDR q-value on every "significantly better fit" flag.

---

## 6. L4 — Societal / civilizational telos + the dual-use firewall (the most load-bearing layer)

> **Hard rule.** This layer contains **no operational synthesis routes, no quantities, no conditions, and no actionable hazard detail** — the firewall is realized at the framework/scoring level only. Any sentence that reads as a recipe is a bug. (RUO; scope per the canonical banner.)

### 6.0 What this layer IS — and is NOT

L4 answers one question only: *what stable goals does this substance serve in society, and does its dominant societal Action raise or lower civilization's integrated stability ℳ = ∫U dt?* It does **not** answer "is this molecule good," does **not** rank substances against each other for funding or deployment (§6.4 firewall), and does **not** — anywhere — emit operational means to make, deploy, or weaponize a harmful substance.

> The relation to L3 is the deliberate, declared divergence (mirrors TSE vs SSS §9.11): **L1–L3 reward intrinsic efficiency**; **L4 can override that reward to zero or negative** when the substance's societal Action is net-destructive. **This override is a NORMATIVE value choice (B0/VISION), not a model theorem (B1)** — the engine does not derive that destruction is bad; a named human declares it (§6.2). A locally perfect explosive is an L1–L3 success and an L4 failure; the geometric mean and the declared telos sign make the L4 verdict dominate, not average against, the efficiency verdict.

### 6.1 The societal triad registered onto a substance-in-society

| Societal pillar (↔ Price) | What it IS (L4 meaning) | Process-intrinsic proxy (versioned) | Failure mode |
|---|---|---|---|
| **Form** (↔ Time) — endurance of the *role* | the durable societal function — place in supply chains, infrastructure, the regulated inventory | inventory persistence (EPA TSCA / EU REACH registration class), substitutability index, criticality of the function | role dissolution |
| **Position** (↔ Space) — societal context of use | *where in the societal order* the substance acts — consumer/industrial/restricted; exposure context | use-context class, exposure population & route, containment level, regulatory schedule (REACH Annex XIV/XVII, Rotterdam PIC, **CWC schedules as *context labels*, never synthesis maps**) | context collapse: dispersal into unintended compartments |
| **Action** (↔ Energy) — net societal contribution, with sign | *what the substance does to society* | **polarity-signed net-contribution proxy** from public, aggregate harm/benefit registries (§6.2) | functional inversion |

The societal triad is an **L0 framing**; every empirical L4 claim is at most canon-L2; the ceiling is B3-pending — *any B4 (validated-policy) sentence in L4 is a bug.*

### 6.2 The telos / polarity term — `T_soc`, declared not inferred

```
T_soc ∈ { beneficial(+), neutral(0), net-harmful(−) }     # declared per node by a named human, never inferred
objective_sign = stabilize  if T_soc = beneficial
               = suppress    if T_soc = net-harmful        # raise societal U by REDUCING this substance's role
U_soc = ∛(F_soc · P_soc · A_soc)        # magnitude: how entrenched / coherent the societal role is
ℳ_soc = ∫ U_soc dt   for ONE declared substance-node       (never summed across substances — §6.4)
```
For a `suppress`-polarity node, high `U_soc` is *bad news, read as such*: a destructive role deeply entrenched and hard to retire is a **robust adversary of ℳ**, exactly as a high-`U_disease` is a robust pathology in TSE; the stakes-scaling runs the other way.

> **How a beneficial-vs-harmful telos is scored WITHOUT any actionable harmful detail.** The Action-pillar score for a `net-harmful` node is built **only from aggregate, public, retrospective harm registries** — disease/mortality burden (**WHO GBD**), poisoning incidence (**WHO INTOX / poison-control aggregate statistics**), addiction/overdose burden (**UNODC / EMCDDA aggregate epidemiology**), pollutant release & persistence (**US EPA TRI**, **EU E-PRTR**), regulatory-restriction status as a *signal* (Stockholm POPs, Montreal phase-out, REACH SVHC). **None of these is a property of a molecule that helps anyone synthesize, formulate, or deploy it.** A `beneficial` node is scored symmetrically from aggregate benefit registries (WHO Essential Medicines coverage; emissions avoided; agricultural yield secured).

> **Magnitude/sign double-use — a NAMED separability liability (critique R4).** The claimed separation is "magnitude `U_soc` = entrenchment; sign `T_soc` = declared by a human." But the same harm registries (GBD/TRI/USEtox) that justify a human's `net-harmful` *declaration* also feed the Position (dispersal/exposure) and Action (toxicity burden) *magnitude* scores. **Magnitude and polarity are therefore NOT independent**, and the societal-triad separability (L4-P0) is *weaker than* the chemical-entity separability (TRC-P0). This is flagged here as a load-bearing liability, not buried, and is the explicit reason L4-P0 is pre-registered with the sign-source registries *held out* from the magnitude proxies wherever the data permit (§8).

### 6.3 The value-frame is contested and named — never objective fact

"Beneficial" is a **human value choice imported under governance**, not a fact the engine discovers (mirrors TSE's NCP fix). Any L4 beneficiality judgment must cite a value-frame, flagged `contested: true`: **green-chemistry / lifecycle frames** (the 12 Principles; **E-factor**; **atom economy**; **PMI**; ISO 14040/14044 **LCA**, USEtox characterization factors) and **hazard / persistence frames** (**GHS**; **PBT / vPvB** from REACH Annex XIII; OECD persistence/bioaccumulation endpoints). Each frame ranks substances differently; L4 records the **chosen frame as a contested claim with a named accountable authority**, never objective fact.

> **The green-chemistry connection (MMT Patch W solvency).** A substance whose **E-factor is high, whose USEtox toxicity factors are large, and which meets PBT/vPvB criteria** is, under a green-chemistry frame, a candidate `net-harmful`/`neutral-with-cost` node — its societal Action *spends* civilizational stability faster than it produces it. This is the chemistry realization of the canon solvency rule: **a substance can be locally efficient (high L3 Action) yet societally insolvent.** The non-compensatory mean enforces this: an excellent catalytic Action cannot rescue a collapsed societal-Position (uncontainable release) or a net-negative societal-Action telos.

### 6.4 The substance-boundary firewall — `ℳ` is per-substance, never allocated across substances (THE CANONICAL STATEMENT of the no-aggregation rule)

> **The single most important ethics correction in L4 — the analog of the TSE organism-boundary firewall (§4.4) and the O5b ban; all other sections cross-reference here.** **O5b-chem** is: *"higher U_soc = a worthier substance; defund/ban the low-U ones; spend the budget where Δℳ/cost is highest."* The label-ban alone is **not sufficient**, because `ℳ = ∫U dt` plus `Priority = Δℳ/∛(C_t·C_s·C_e)`, run *across substances*, would allocate a finite R&D/regulatory/procurement budget across chemicals — **reconstructing the identical worth ordering without the word "worthier."** L4 closes this at **two levels:**
>
> 1. **(label)** No cross-substance worth *ranking* exists — no operation returns "substance A is more valuable to society than B."
> 2. **(operation)** No cross-substance **ℳ-aggregation or leverage-ranking** exists — no `ℳ_total = ∑∫U_soc dt` over a portfolio, no `Priority` comparison across the substance boundary.
>
> The leverage primitive remains admissible **only inside one declared substance-node** (e.g. "for *this* polymer, the weakest societal leaf is Position — uncontainable microplastic release — so the matched lever is context/end-of-life redesign"). Any **cross-substance allocation** — which chemical to ban, fund, stockpile, or phase out — is an **external governance decision supplied to the engine, never an engine output.** *"Who decides which substances are useful"* is a **hard ethical guardrail and an open governance problem the engine does not solve** — written down, not declared solved.

### 6.5 The HARD dual-use firewall — type-forbidden targets (single abstract statement)

> Per the header: TRC's leverage machinery is **sign-symmetric**, so the stabilization and the weaponization/synthesis-enablement computations are the same computation with the sign flipped, and **the sign-flip is prohibited.** This document **states the prohibition once and does not describe *how* a flip would be performed** — to avoid functioning as a design brief for the prohibited capability, the earlier draft's repeated "cheapest-flip / criticality-proximity" glosses are removed.

**TYPE-FORBIDDEN optimization targets (the deny-list — constrains objectives, not just outputs).** A net-harmful substance is **not a feature and not a permissible optimization target.** The framework refuses to *design for, optimize toward, synthesize, formulate, scale, or operationally improve* any of: chemical-weapon agents and precursors (**CWC** Schedules 1–3 used **only as deny-list labels, never routes**); explosives/energetic materials and their precursors; biological-weapon agents/toxins (**BWC**); illicit drugs and precursors (1988 UN Convention / INCB scheduling); persistent pollutants (**Stockholm Convention** POPs). For every forbidden class the framework provides **only** the L4 societal-cost *scoring* (aggregate, retrospective, public) and the conclusion *"net-harmful → do not optimize"* — **no** structures, routes, precursors-as-recipe, conditions, quantities, yields, scale-up, or destabilization/diversion analyses. Export-control norms (CWC/BWC, Australia Group, EU 2021/821) are honored as **constraints on objectives.**

> **Who classifies, and the incidental-discovery procedure (critique E3 — the gap the old "residual risk acknowledged" line papered over).** The pre-enumeration `target_type_check` presumes a target is declared and classifiable; a *novel* agent or a precursor with a *benign declared use* defeats it. TRC therefore specifies, not just acknowledges: (1) **classification authority** — forbidden-class membership is adjudicated by a **named accountable human + an export-control/biosafety reviewer of record**, never by the engine, and a candidate that is *ambiguous* is treated as `FORBIDDEN_PENDING_REVIEW`, not `ALLOWED`; (2) **incidental-discovery halt** — if leverage analysis on a node declared `benign` surfaces a destabilization/synthesis-enablement path, the run **halts, redacts the path, emits no leverage output, and logs a flagged incident to the reviewer of record** (the path is never returned to the requester); (3) the firewall is **ungated and never retired** (§9.9). **Residual risk remains and is acknowledged in writing:** the boundary is partly social/operational, the classification of novel candidates is genuinely hard, and these controls are **necessary but not sufficient.**

### 6.6 L4 worked example — a societal-telos read on two material *classes* (SCORING-MECHANICS ILLUSTRATION ONLY, B2; NO synthesis content)

> Scores are illustrative, carry zero predictive evidence, and contain **no synthesis, formulation, or hazard-actionable detail** — only public aggregate societal-outcome framing.

**Class A — a stable structural steel (`T_soc = beneficial`, `stabilize`).** Societal Form 0.86 (durable infrastructural role; long inventory persistence; hard to substitute), Position 0.82 (industrial + consumer, well-contained, low diffuse release), Action **+**0.80 (enables construction/transport/energy infrastructure; LCA cost real but offset; recyclable). `U_soc = ∛(0.86·0.82·0.80) = 0.827` → **STABLE / net-stabilizing**; ℳ_soc over service life is positive. (Connects upward from the L3 steel-knife.)

**Class B — a `net-harmful` class declared `suppress` (an entrenched legacy POP under Stockholm Convention).** The engine renders **no structure, no route, no property that enables making or deploying it** — only the societal read from public aggregate registries: societal Form **0.78** (the destructive *role* is durably entrenched — *high Form here is read as "hard to retire," i.e. bad*), Position **0.30** (context collapsed outward — listed as uncontainable/persistent in public registries), Action **−**0.70 (dominant Action is poisoning/persistence; large USEtox burden, listed for global phase-out). Magnitude `U_soc = ∛(0.78·0.30·0.70) = 0.555`; with `suppress`, **read as a robust adversary of ℳ**, binding weakness at **Position**. The axis-matched, compensation-forbidden lever (within this one node) is **context/Position retirement** — phase-out, containment, remediation, substitution — *as a policy direction supplied to and adjudicated by the named authority,* never an engine-issued mandate and **never ranked against Class A for budget** (§6.4). `𝒮_soc = ∫(1−U_soc)dt` accrues for as long as the role persists — the L4 statement that *a substance whose dominant Action is destruction lowers ℳ even when locally "efficient."* (Per §6.2, the magnitude here shares registries with the sign source — an acknowledged L4-P0 separability liability, not independent evidence.)

---

## 7. Phased roadmap (the committed deliverable is §8; the engine is aspiration, not product)

| Phase | Goal | Runnable here? | Gate / ceiling |
|---|---|---|---|
| **P0** | F/P/A conditional separability over a chemistry/materials panel (MP/OQMD + held-out ICSD/ORD; molecular battery) | **yes** (mandatory go/no-go) | conditional dCor/CMI at the system/dataset/family unit, **DFT/QSPR-derived Action excluded, measured/ICSD/ORD Action where it exists, task held fixed**; no U rendered until it passes |
| **P0b** | geometric > arithmetic / weighted-sum, robust to anchor, form, AND cross-database; win isolated to the one-low-pillar regime | **yes** | survives ±20% anchor + normalization-form + **cross-DB correction-scheme** perturbation, and shows ΔR² *on the near-zero subset*, else retired |
| **P0c / P0d / P0e** | (c) `E_hull`/ICSD truth independent of Form inputs; (d) no single DFT observable carries comparable conditional dependence on two pillars (the E_hull-axis liability); (e) Action/Position still separable with task held fixed | **yes** | leakage / two-pillar-loading / task-conditioned tests; failures restrict admissible proxies |
| **P1** | the flagged weak leaf / mismatch names the failure mode (ORD / service-failure held-out) | **yes** | AUC ≥ 0.70 vs degree/base-rate null; multiplicity-corrected |
| **P2 / P2b** | route-grounded `U_made`/`U_design` and the geometric `U` beat `U_product`, thermo-only, **constraint-screened Ashby**, AND a plain additive mix at **measured** stability/synthesizability/service-life | **yes** | ΔR² ≥ 0.1 vs the *strongest* baseline (unit = chemical system / family) |
| **P4** | triadic selection beats **constraint-screened Ashby (screen + post-screen index)**, especially at graded axis-localization | **yes** | beats the constraint-screened baseline on held-out tasks, else retired to constraint-screened Ashby |
| **P9** | the four LAYERS (L1–L4) carry distinct information | **yes** | L1–L4 `U`-scores not mutually rank-redundant beyond a threshold, else the layering is reported as relabeling and collapsed |
| **L4-P0 / L4-P1** | societal F/P/A separable (class level, sign-source registries held out) + telos beats a flat lifecycle index at retrodicting restrictions | **yes** | dCor/CMI at class level with sign/magnitude registries separated; retired if it adds nothing over the lifecycle index |
| **V3 / dynamic twin** | prospective twin-ranked route/selection vs **characterized** outcomes from a collaborator's existing library (no new hazardous chemistry); degradation/corrosion/turnover trajectory twin | **no** — needs collaborator/governance; **research-grade, not runnable** (no calibrated cross-process rate constants from snapshot databases) | on-ramp toward a separate, non-hazardous B4 qualification project |

The committed product of TRC is the **pre-registered separability + geometric-vs-baseline + weak-leaf/selection + layer-orthogonality tests** — **not** a synthesis planner, a process-design tool, or a materials-qualification system. Every "scales toward an engine" sentence elsewhere is aspiration that lives and dies by this table.

---

## 8. Validation — pre-registered falsifiers (each designed to be falsified) + symmetric retirement

> **All independence/separability thresholds are stated on a normalized nonlinear dependence statistic — distance correlation (dCor) or conditional mutual information (CMI), in *conditional* form — NEVER on Pearson |r|.** The **0.6–0.8 band is pre-committed "inconclusive → never a pass."** The **unit of independence is the chemical system / material class / reaction family — never the individual conformer, the single DFT cell, or one datasheet row** (R8). A **power calc precedes each test**; if the CI cannot exclude the 0.6–0.8 dead zone the test is "not yet decidable," never a borderline pass; **study-level FDR across the full P-battery.**

| # | Claim under test | Falsifier (conditional dCor/CMI, family-level) | Pass → admits | **FAIL → REMOVES** |
|---|---|---|---|---|
| **TRC-P0** | F, P, A carry conditionally independent, non-redundant information for substances & routes | a pillar's conditional dependence given the other two ≈ 0, or pairwise in the 0.6–0.8 dead-band at achievable family *n* (likely: structure-derived Form, structure-derived reactivity, DFT energy are three transforms of one structure graph) | each pillar adds conditional dependence (CI below 0.6) **and** held-out variance for an external stability/synthesizability outcome | **STOP** — the triadic frame is retired; reverts to single-axis (property-only) scoring; **§3–§6 deleted** (§A.0) |
| **TRC-P0b** | geometric `U` beats arithmetic / weighted-sum, robustly, *in the regime where it can differ* | the win vanishes under ±20% anchor OR form OR **cross-database** perturbation, OR there is no ΔR² advantage **on the one-low-pillar subset** (rank-correlation away from zeros makes geom≈arith) | non-compensatory aggregation kept as core | **geometric aggregation retired as an anchor/form/DB artifact or as trivial-away-from-zeros** |
| **TRC-P0c** | external stability truth (`E_hull`, ICSD) is independent of Form inputs | `E_hull` recoverable from the same DFT features that feed Form (leakage audit) | the truth metric is usable | that "truth" is unusable; substitute an independent measured outcome |
| **TRC-P0d** | no single DFT-derived observable loads two pillars comparably (the `E_hull`-axis liability, §2.5) | one observable (e.g. `E_hull`) carries comparable conditional dependence on both Form and Position | the per-axis proxy assignment stands | the offending observable is dropped from one pillar; if none survives, P0 is endangered |
| **TRC-P0e** | Action and Position separable with the task held fixed | conditional dependence persists at the 0.6–0.8 dead-band with task fixed | the task-relative pillars are admissible | Action and Position are merged into one task-fit axis; the triad in chemistry is reduced |
| **TRC-P1** | the flagged weak leaf / mismatch names the failure mode | the axis-label flips under documented proxy reassignment, or no lift over a base-rate null on held-out characterized reactions/service failures | the localizer is a delivered, gated feature | **reverts to "δ-spike / decoupling, axis TBD"** (O8) |
| **TRC-P2 / P2b** | the coupled/route-grounded geometric `U` beats `U_target`/`U_route`/thermo-only/**constraint-screened Ashby** AND a plain additive mix at a held-out **measured** outcome | ΔR² CI includes 0 against the **strongest** baseline | one-directional grounding / non-compensatory coupling kept | **retired as ornamentation** |
| **TRC-P4** | triadic selection beats **constraint-screened Ashby** (screen + post-screen index), esp. at graded axis-localization | no better than constraint-screen + `M = E^{1/2}/ρ` post-screen on a held-out task panel | the selection layer is kept | **retired to constraint-screened Ashby selection** |
| **TRC-P7 / P8** | the optional 4th (Freedom) / 5th (coherence) currency is independent / earns a number | fails its independence / aggregation-level test | the currency is admitted | **removed from the ledger and renderer** |
| **TRC-P9** | the four layers L1–L4 carry distinct information | L1–L4 `U`-scores mutually rank-redundant beyond threshold | the layering is kept | **the layering is reported as relabeling; collapse to fewer layers** |
| **L4-P0 / L4-P1** | societal F/P/A separable (class level, **sign-source registries held out from magnitude**); the telos sign adds signal over a flat lifecycle index | dead-band dependence; `U_soc` with `T_soc` no better than the strongest single lifecycle index at retrodicting phase-outs | the societal triad / polarity machinery is kept | **societal triad / polarity term retired**; L4 reports a single contested aggregate |
| **GSM-P1 / GSM-P2** (§2.9.9) | GSM's `P(U<φ⁻¹)` is **calibrated** vs external outcomes and its `τ`-width/`ΔP_fail` localization adds signal over point-SI (P1); the interval is **link-robust** (logit-normal↔Beta) and **`Σ`-honest** (`R̂`↔`R_hi`) (P2) | reliability curve off the diagonal beyond CI, OR ECE over bound, OR width carries no info about point-SI's error (P1); a verdict flips under the link swap or `R̂`↔`R_hi` at achievable family `n` (P2) | GSM admitted as a B1-pending uncertainty layer; `P_fail` / credible intervals render decision-grade under SSS-Guard | **GSM removed from ledger & renderer**; revert to the §2.2 point-SI pipeline + inherited neutral-50 / `LOW_EVIDENCE` tags (P1); the affected verdict is `axis_unseparated`, only the `Σ→0` point fallback renders (P2) |
| **TRC-P10 (TMAC value)** = **TMAC-P10 / TMAC-P11** (§11.7) | the **multi-agent value** claim: the orthogonal F/P/A × L1–L4 decomposition + non-compensatory **combiner** (veto) + weakest-pillar / `GSM-Priority` **scheduler** (routing) beats a **monolithic ReAct** agent and an **ad-hoc / compensatory BO-active-learning** loop at *equal tools, equal budget*, with the win **isolated to the one-low-pillar regime** (P10); and the advantage is **caused by the non-compensatory routing, not the extra compute** — a weighted-sum-router ablation does **not** recover it and the win survives cost-charging parallel compute on the Action axis (P11). **Downstream of and conditional on TRC-P0/P0e/P9** (no separability ⇒ nothing orthogonal to orchestrate ⇒ not run) | budget-to-target / hit-rate CI **includes 0** (or favours a baseline) vs the **strongest** baseline at achievable family *n*; OR the win vanishes off the one-low-pillar subset; OR the weighted-sum-router ablation matches it; OR it disappears once parallel compute is cost-charged | the **triadic decomposition + non-compensatory scheduler** is a delivered, gated **multi-agent orchestration** value (B3-pending until passed) | **the multi-agent value claim is RETIRED** (symmetric); TMAC reverts to "a conformant `TriadicDomain` object with no demonstrated routing edge over a monolithic / ad-hoc agent" — §11 becomes documentation, not a result; if TRC-P0 fails, §11 is deleted **with** §3–§6 (§A.0) |

**Worked falsifier intuition (TRC-P1).** Take a held-out slice of MP/OQMD, compute F/P/A from *independently-sourced* proxies, aggregate `U`, and check whether `U` rank-orders the *withheld* external outcome. If a candidate that is thermodynamically deep but kinetically inert (A→0) or in the wrong phase field (P→0) is correctly driven to U≈0 — rather than rewarded for a high average — that is the System-A non-compensation signature, but **only the one-low-pillar subset (TRC-P0b) is diagnostic**, since away from zeros geometric≈arithmetic.

**Symmetric retirement.** A claim whose gate fails is **deleted from the ledger and the renderer**, logged in `TRC-CHANGELOG`. The firewall (§6.4–6.5) and the hazardous-synthesis refusal are **not gated and never retired.** Reporting the narrowing is TRC's contribution to canon (TRB §A.2) — stated once, here.

---

## 9. RH discipline — scope, limits, real data layer, ethics, non-goals (the governing section)

### 9.1 The central cut, on four surfaces (TESTABLE / INTERPRETATION / VISION)

The triad here is an **accounting frame and a materials-/reaction-selection search heuristic** — *not* an ontology of matter, *not* a "stability of a substance" oracle, *not* a recipe generator. Three strictly separated registers, enforced in code on **every** TRC surface — the **substance**, **route**, **use** (Ashby-fit), and **societal** (L4) score:

- **TESTABLE** — a statement about what *the TRC model does* over data, admitted only with (i) an operational procedure, (ii) a falsifiable prediction, (iii) an **external** ground-truth metric *independent of the score being validated*.
- **INTERPRETATION** — framing/metaphor. May generate hypotheses and label axes; **no number/verdict/colour/ranking/arrow rendered to a user may be in INTERPRETATION language.** The renderer prints *"model stability index for substance-type X, model-internal,"* never *"X's stability is 0.41,"* and never *"material M is the right choice for task T."*
- **VISION** — telos/motivation ("design the most stable matter"; "L4 may override efficiency"). Confined to explicitly-marked VISION blocks; renders **no** number/verdict/ranking/allocation; never a section thesis, never a deliverable.

The chemistry separability liability is a **single computed electronic structure** shared across axes (substance), one reaction-prediction model→one embedding→three axes (route), and a single property datasheet feeding both property and selection metric (use); plus the magnitude/sign registry double-use (L4, §6.2). **The headline deliverable is therefore demoted, by construction, to a hypothesis gated behind TRC-P0.**

### 9.2 Maturity and the epistemic ladder

Per §A.5 / the header: **B3-pending**, two empty B4 slots (*synthesis-action*, *deployment/societal*), B0–B4 ↔ canon L0–L4, the B1→L1 row uses canon's real meaning (*Operational stability*). The L4-override-efficiency rule is **B0**, not B1 (§6.0, R8 fix). Every artifact carries a `level` tag; the lint refuses any wording exceeding it. **No statement occupies canon-L3/L4; any B4 sentence is a bug.**

### 9.3 The real data layer — one resource → one axis, with independence caveats

Provenance is mandatory: every principle/node/score/edge carries `G{src; conf; level; mode}` with **accession + version + date** (an MP `mp-id` + DB release + functional + correction scheme, a PubChem CID + retrieval date, an ORD reaction id). **Unsourced principles are B0 and cannot enter scoring.** Resources are partitioned so that — wherever possible — **one dataset populates exactly one axis**: FORM (structure/identity ↔ Time; formation-energy *depth from elements*) from PubChem / ChEMBL / RDKit / ICSD / MP / OQMD + NIST decomposition/corrosion data; POSITION (phase/environment/hull ↔ Space; **`E_hull` lives here**, §2.5) from NIST phase diagrams, MP convex hull / Pourbaix / chemical-potential diagrams, solvent/partition descriptors, Ashby property space; ACTION (reactivity/function ↔ Energy; extent at operating activities) from ORD / Reaxys-class, NIST thermochemistry, DFT reaction/activation energies, Ashby property axes. **External ground truth (leakage-audited, TRC-P0c):** DFT `E_hull`, experimental ΔH_f, measured decomposition/shelf-life, measured yields, ICSD presence. The **two-layer data-independence warning of §2.5 (the single canonical statement) governs throughout**, and DFT-derived Action is excluded from the separability claim.

### 9.4 Regulatory & safety boundary — INTENT, not settled fact

TRC is *designed* research-use-only and to sit outside chemical-process and product regulation — **but classification is regulator-adjudicated, not self-determined.** A stability-and-selection engine keyed by *substance × environment × reaction* that *ranks routes and candidates* is exactly what a regulator and an export-control officer scrutinize, so this is **intent**, not settled fact.
- **Not a laboratory protocol** (scope per the canonical banner): operates on substance-types, computed candidates, and digital twins; produces no routes, quantities, conditions, or parameters; no actionable wet-chemistry output, ever.
- **Human-in-the-loop and human-on-top; no autonomous/closed-loop action; no laboratory, pilot, or plant pathway; no autonomous specification of any load-bearing/safety-critical part.** SSS-Guard governs *simulated/recommended* scores only.
- Any future intent to drive a real synthesis (synthesis-action B4) or release a real material (deployment B4) is a **new B4 project** with process-safety review, regulatory registration (REACH/TSCA-class), life-cycle/environmental-fate assessment, and a named accountable authority.

### 9.5 Named overclaim risks (O1–O12)

**Inherited O1–O9 (TRB/TSE) re-derived for chemistry; domain-specific O10–O12:**
- **O1** "TRC measures a substance's intrinsic worth / safety" — banned-output lexicon ≤B3; TRC scores *stability/fit*, not virtue or safety.
- **O2** "Low U = a dangerous/bad molecule" — every U ships with `evidence_confidence`; low-evidence scores are "not interpretable"; U is a model-internal index, never a hazard rating.
- **O3** "TRC designs/synthesizes/replaces chemists" — recommendations address *researchers about mechanisms/feasibility*, never a bench operator with a procedure.
- **O4** "the triad is proven chemistry" — B2 only; separability untested until TRC-P0.
- **O5 — the eugenics-attractor analogue, scaled to substances:** "higher-U substances are *worthier*." U is a stability/fit index, **never** a worth metric over substances, and **never aggregated across substances** (§6.4).
- **O5b-chem — O5 at the macro-unit (L4).** The single most dangerous reading. Closed at **two levels** (§6.4): no cross-substance worth ranking; no cross-substance ℳ-aggregation or leverage-ranking — because `Priority = Δℳ/cost` across substances reconstructs the worth ordering without the word "worth."
- **O6** "the AI jury is objective" — consensus measures *agreement*, not correctness.
- **O7** "real-time reactor/part model" — "trajectory" = simulated ageing/turnover, never live process control or fielded-part monitoring.
- **O8-CHEM** "the weakest pillar names the mechanism" — gated (TRC-P1); INTERPRETATION until proxy-axing is stable.
- **O9** quantum/coherence over-reading — any "coherence" term is **classical** (long-range order / domain correlation), not entanglement; renders no number until gated.
- **O10 (chem)** "the U-score *is* the measured stability / formation energy" — banned; U is a model-internal index until TRC-P1 passes against external truth. **`E_hull` and elemental formation energy are distinct quantities (§2.8) and neither is `U`.**
- **O11 (chem)** "the triadic scan *is* the synthesis plan / deployment decision" — hypothesis-generation, never a route (O3) and never an L4 deployment plan (O5b).
- **O12 (chem)** "efficient destructive Action = it should be used / TRC proves matter is triadic" — **efficiency of Action is never licence**; a material that performs a destructive Action efficiently scores high `A_fit` and **must still be type-forbidden at L4** (the L4-override is B0/VISION, §6.0). TRC is an *instance*, not evidence.

### 9.6 Data ethics & provenance

Public chemistry/materials databases first (PubChem, ChEMBL, ORD, MP, OQMD, ICSD, NIST). Provenance mandatory; unsourced principles are B0. Proprietary/Reaxys-class data, if ever used, respects its license and is never re-published as a route. No human-subject data; the binding sovereignty constraint is **export-control and dual-use law** (§6.5).

### 9.7 The dual-use firewall — governing rule (cross-references §6.4–6.5)

The full firewall is stated abstractly in the header and realized in L4 §6.4–6.5. Governing rule: TRC's leverage-finder is **sign-symmetric**, so the deny-list constrains **objectives** and the lint constrains **outputs**, and **both are necessary, neither sufficient.** Net-harmful substances are **type-forbidden optimization targets**; no released artifact produces, ranks, or optimizes operational routes, quantities, conditions, or destabilization/diversion targets for any forbidden class; CWC/BWC/Australia Group/EU 2021/821 honored; **classification authority and the incidental-discovery halt are specified in §6.5; residual risk acknowledged in writing.** **L4 is judged, not just efficiency-scored** — "which substances are beneficial" is a **contested, accountable-human governance decision supplied to the engine, never an engine output.** This document deliberately does not describe *how* a destabilizing sign-flip would be performed.

### 9.8 Mechanizing the discipline — claim envelope and output lint

```
{ axis ∈ {substance, route, use, L4},
  register ∈ {TESTABLE, INTERPRETATION, VISION},
  epistemic_level ∈ {B0,B1,B2,B3,B4},
  text, value,                                   # model-internal index, never "worth"
  evidence{ n_valid_models, consensus_pct, mode ∈ {abstract, specific}, coverage },
  provenance[],                                  # accession + version + date + functional + correction_scheme, MANDATORY
  external_ground_truth{ metric, value, agreement, mode ∈ {retrodictive, prospective} },
  dist?{ link ∈ {logit_normal, beta_marginal}, mu, tau, P_fail, ci90 },  # OPTIONAL GSM block (§2.9); B1-pending, decision-grade only after GSM-P1; no new top-level surface
  objective_sign ∈ {stabilize, suppress},        # declared per target; suppress on a beneficial substrate = firewall trip
  target_type_check ∈ {ALLOWED, FORBIDDEN_PENDING_REVIEW, TYPE_FORBIDDEN},  # ambiguous ⇒ PENDING, not ALLOWED
  T_soc ∈ {beneficial, neutral, net-harmful},    # L4 only; declared, not inferred
  value_frame{ name, contested:true, anthropocentric:bool },  # required iff a beneficiality judgment present
  accountable_authority }                        # named human, for any beneficiality / objective / L4 / classification claim
```

**The output lint refuses (renders nothing on a refusal):** (1) any claim above **B3** — *any synthesis-action or deployment B4 sentence is a bug*; (2) any ≤B3 claim using **banned lexicon** (worth/safe/dangerous/cure/conscious/vitality/"worthier substance"/"best material"/"cull"/"eradicate"/"useful species"/"most energetic"/"most detonable"/"most toxic"/diagnose/treat/"qualified"/"fit for service"); (3) any decision-grade B3 claim lacking an **external ground-truth metric** or **≥2-of-3 SSS-Guard agreement**, *and* any prospective-mode claim asserting `pass` rather than `queue_for_V3`/`queue_for_lab`/`queue_for_test`; (4) **any cross-substance/cross-task/cross-design U aggregation OR cross-node ℳ-aggregation / leverage-ranking / worth ranking / budget triage** (the O5b realization at *both* levels — a hard type-level refusal; §6.4); (5) any **substance-U, route-U, use-fit, or societal score** rendered before its gate (TRC-P0 family) passes; (6) **any TYPE_FORBIDDEN or FORBIDDEN_PENDING_REVIEW target, any operational synthesis route/quantity/condition output for any substance, or any destabilization/diversion query** — refused unconditionally and logged to the reviewer of record (incidental-discovery halt, §6.5); (7) any beneficiality / "which substances society should pursue" claim lacking a **`value_frame`(contested) + named `accountable_authority`**; (8) any weak-zone flag lacking a **multiplicity-corrected q-value** clearing an absolute band — else "not distinguishable from screening noise"; (9) any substance-intrinsic score rendered as a **measured physical quantity / hazard rating** (O10), or attributed to a specific synthesis step or actor.

Every weak-leaf flag is tagged `low_score_cause ∈ {evidence_sparse, genuinely_imbalanced, lattice_approx, dft_only, axis_unseparated}`; only `genuinely_imbalanced` on a *gated, measured-input* axis is a candidate hypothesis. A `dft_only` Action flag renders as *"not yet interpretable — separability / measurement pending."*

### 9.9 Symmetric retirement rule (consolidated)

| Gated claim | Gate | Pass → | **Fail → REMOVE** |
|---|---|---|---|
| Failure-mode / mismatch localizer | TRC-P0 + TRC-P1 | delivered, gated feature | **reverts to "δ-spike, axis TBD"** |
| Geometric > arithmetic / weighted-sum (incl. near-zero-regime, cross-DB) | TRC-P0b / P2b | engine's core | **retired as anchor/form/DB artifact or trivial-away-from-zeros; revert to single-index** |
| Triadic selection beats constraint-screened Ashby (L3) | TRC-P4 | the selection layer | **retired to constraint-screened Ashby** |
| Inverse-design / retrosynthesis triadic search (L1) | TRC-P0(route) / P2 | delivered, gated | **retired; the engine is a substance-scorer, not a route-search engine** |
| `U` predicts real stability | TRC-P1 / P2 | the stability claim stands | **the U-score is decorative; report it predicts no measured stability** |
| The four layers carry distinct information | TRC-P9 | the layering kept | **layering reported as relabeling; collapsed** |
| Societal triad / telos sign (L4) | L4-P0 / L4-P1 | societal read kept | **retired to a single contested aggregate** |
| Gaussian Stability Matrix interval / `P_fail` (§2.9) | GSM-P1 / P2 | `P_fail` + credible interval render decision-grade (B1-pending) | **GSM removed from ledger & renderer; revert to §2.2 point-SI + inherited neutral-50/`LOW_EVIDENCE`** (P2-fail ⇒ affected verdict `axis_unseparated`, `Σ→0` fallback only) |
| TMAC multi-agent orchestration value: triadic decomposition + non-compensatory scheduler beats monolithic / ad-hoc baselines (§11) | TRC-P10 (= TMAC-P10 / P11) | the multi-agent decomposition + non-compensatory routing is a delivered, gated value (B3-pending) | **the multi-agent value claim is removed**; TMAC reverts to "a conformant domain object, no demonstrated routing edge"; §11 is documentation, not a result (and is deleted with §3–§6 if TRC-P0 fails, §A.0) |
| Optional 4th/5th currency | TRC-P7 / P8 | admitted | **removed from ledger & renderer** |

The firewall (§6.4–6.5) and the hazardous-synthesis refusal are **ungated and never retired.**

### 9.10 Caveats TRC must carry (the consolidated list)

1. **Separability is the load-bearing untested assumption** — F/P/A are likely three transforms of one electronic-structure calculation; if collinear (TRC-P0 fails), §3–§6 are deleted (§A.0).
2. **DFT-derived Action is broken *by construction*** against DFT-derived Form (same relaxed cell) — excluded; the test re-runs on a measured-Action subset.
3. **`E_hull` truth may leak into Form** (same DFT total energies) — leakage audit (TRC-P0c) mandatory; and **`E_hull` is a Position quantity, distinct from elemental formation energy (Form)** — the two were conflated in an earlier draft and are now separated (§2.5, §2.8). The fact that one observable felt assignable to two pillars is itself a separability liability (TRC-P0d).
4. **All thresholds and anchors are tunable, domain-calibrated defaults, not constants of chemistry** — φ⁻¹≈0.618, the SI bands, `ref_lo`/`ref_hi`, the band-centred Action shape; high-stakes raises θ; headlines must survive ±20% anchor *and* functional-form *and* **cross-database** perturbation (TRC-P0b).
5. **Snapshot, not trajectory** — the objective is `ℳ=∫U dt`, but a *dynamic* twin of degradation/corrosion/turnover is **research-grade, not runnable** (no calibrated cross-process rate constants from snapshot databases).
6. **Computed-structure nodes are `LATTICE_APPROX`** — a DFT-relaxed/model-predicted structure is a model output (and a phonon/Born check is a 0 K necessary, not sufficient, condition, §4.3), held to the higher bar.
7. **Commensurability, task-relativity, and timescales** — F/P/A are different *kinds* of quantity, so the normalization does all the work; **Action and Position both carry the task variable** (orthogonality threat, §2.1, TRC-P0e); degradation runs over hours–years and reactions over seconds → currency-resolved ℳ.
8. **Missing-data discipline** — unmeasured observable → neutral 0.50, never dropped (SSS-L4/Mode-B); coverage <0.3 → `LOW_EVIDENCE`, excluded from decision-grade output.
9. **Multiplicity** — argmin over a 10³–10⁶ screen is a look-elsewhere problem; every flag carries an empirical-null + FDR q-value at the **material-class/reaction-family** unit of independence (R8).
10. **The hard dual-use firewall (§6.5, §9.7) is necessary but not sufficient** — no hazardous-substance optimization, routes, conditions, quantities, or destabilization/diversion analyses; classification authority and incidental-discovery halt specified; residual risk acknowledged; CWC/export-control norms respected.
11. **L4 magnitude and polarity share harm registries** — societal separability (L4-P0) is weaker than chemical separability (§6.2), pre-registered with sign-source registries held out from the magnitude proxies.

---

## 10. Cross-appendix coherence + glossary

### 10.1 Coherence (where TRC diverges on purpose)

- **vs. SSS** — TRC reuses the SSS engine unchanged (Constructor + ≤50-model jury, IQR → weighted → geometric → consensus, φ⁻¹≈0.618 stakes-adjustable θ, Modes A/B). **Declared divergence:** SSS sells cross-system comparability; **TRC reverses this for worth on purpose** — no task-free material ranking, no cross-substance/cross-task/cross-design ℳ-allocation (the O5b-chem firewall, §6.4).
- **vs. TRB / TSE** — TRC inherits the `F{}P{}A{}G{}` node schema, the U/δ/SI primitives (δ now over **leaves**), the weak-zone scan with R7/R8, the TESTABLE/INTERPRETATION/VISION cut, the B0–B4 ladder, the claim envelope + refusing lint, the symmetric-retirement rule, and the O5b firewall — specialized to substances, routes, *(material, task)* fit, and societal role. The chemistry-specific confound is the **DFT-from-one-structure** analogue of TRB's FBA-from-transcriptome confound.
- **vs. GSI-RTD** — TRC implements the `TriadicDomain` interface; a *conformant domain*, not a parallel theory.
- **vs. MMT** — `ℳ = ∫U dt` on a **single declared clock**; `𝒮 = ∫(1−U)dt`; `ℳ+𝒮=T`; the solvency rule (Patch W) realized as "locally efficient yet societally insolvent" (§6.3). No statement occupies canon-L3/L4; both B4 slots stay empty.
- **vs. NDT — TRC AMENDS NDT** — non-uniform lifting (Freedom per-node via TRC-P7; coherence aggregation-level via TRC-P8), and a **classical** 5th-slot analogue where NDT reserves the 5th for quantum substrates — disagreement logged.
- **vs. Ashby (external method, HONEST baseline declared)** — TRC *embeds* the Ashby index `M` inside `A_fit`/`F_fit` and *wraps* it in two further non-compensatory pillars, and benchmarks against **constraint-screened Ashby (screen + post-screen index), NOT a bare weighted sum** (§5.3) — the testable payload (TRC-P4/P0b), retired if it does not beat that baseline, with the honest expectation that the screen already supplies most of the non-compensation.
- **vs. UCT** — TRC contains **no "proof" of anything about chemistry** — only within-model theorems (B1), bridges (B2), and pre-registered predictions (B3-pending).

### 10.2 Glossary

| Term | Definition |
|---|---|
| **F / P / A** | Form (identity/structure, ↔Time; depth = *elemental* formation energy), Position (locus `q` incl. `E_hull` + context `c`, ↔Space; `P=√(q·c)`), Action (reactivity/function + energy at operating activities, ↔Energy; two-sided & task-relative, §2.6) — the three candidate orthogonal axes (separability tested, TRC-P0/P0e). |
| **U** | `∛(F·P·A)` — non-compensatory geometric stability score; any pillar → 0 ⇒ U → 0. |
| **δ / SI** | `δ=(max−min)/(max+0.01)` over the **LEAF set**; `SI=U/(1+δ⋆)²`, `δ⋆=δ·𝟙[min(leaves)<0.5]` (no over-penalty of competent-but-uneven nodes); bands 0.38 / 0.618 (tunable). **TRB-introduced, leaf-corrected here.** |
| **weak_leaf / weak_pillar** | `argmin` over leaves / the pillar owning it; **names the failure mode only as a gated hypothesis (TRC-P1)** (O8). |
| **E_hull** | DFT energy above the convex hull (distance to competing phases) — a **Position/locus** quantity and an external truth metric (leakage-audited, TRC-P0c); **distinct from elemental formation energy.** |
| **elemental formation energy** | depth referenced to elemental standard states — the **Form/thermo** quantity; for Fe₃C it is small/sign-uncertain, unlike `E_hull` (§2.8). |
| **ChemSystem / RouteSystem** | the universal recursive node types: `F{} P{} A{} G{} + state s`; `d ⇒ 3^d` subsystems. |
| **F_acc** | catalogue-relative retrosynthetic closure `{closed, partial, open}` — binned, non-stationary, **not** a route property (§3.2.2). |
| **U_design / U_route / U_made** | `∛(U_target·U_route·F_acc)` (one-directional grounding); serial-AND route roll-up; `∛(U_product·U_route·U_robustness)`. |
| **ℳ, 𝒮** | Meaning `∫U dt` and Stupidity `∫(1−U)dt` for **one declared node**; `ℳ+𝒮=T`; coverage/stability indicator, never a worth rank; **never aggregated across substances** (§6.4). |
| **T_soc / objective_sign** | L4 societal polarity `{beneficial, neutral, net-harmful}` (declared by a named human) → `{stabilize, suppress}`; high U on a suppress node = a robust adversary of ℳ. Magnitude and sign share registries — a flagged separability liability (§6.2). |
| **constraint-screened Ashby** | the HONEST L3 baseline: hard-constraint screening (already non-compensatory) then a post-screen index — what TRC-P4 must beat (§5.3). |
| **LATTICE_APPROX** | flag for FORM defined only by a map/registry/computed structure — higher evidence bar. |
| **provenance class [M]/[C]/[I]** | measured / computed (model output) / inferred (QSPR). |
| **Open-world guard** | "absent from atlas/DB" → `UNKNOWN`, never `FORBIDDEN`; only positively-contradicted entities are vetoed. |
| **R7 / R8** | multiplicity (empirical null + FDR q-value) / unit of independence (chemical system / material class / reaction family / supplier-lot — never the molecule/cell/datasheet row). |
| **DFT-from-one-structure confound** | the chemistry analogue of TRB's FBA-from-Form confound; DFT-derived Action excluded from the separability claim. |
| **substance-boundary firewall** | the type-level ban on cross-node ℳ-aggregation/leverage-ranking — closes the O5b allocation leak (§6.4). |
| **sign-symmetric leverage / sign-flip prohibition** | the same leverage computation, sign-flipped, would destabilize/enable synthesis; the flip is prohibited and its method is not described (§6.5). |
| **incidental-discovery halt** | if a `benign` node's leverage analysis surfaces a destabilization path, the run halts, redacts, and logs to the reviewer of record (§6.5). |
| **SSS-Guard** | gate on any irreversible (simulated) call: retrodictive accepts iff ≥2-of-3 SSS agree AND agree with an external metric; prospective has no `pass`, only `queue_for_lab/V3`. |
| **B0–B4 ↔ canon L0–L4** | telos/VISION (incl. the L4-override rule) · true-of-model · bridge · testable-pending = ceiling · validated = EMPTY ×2. |
| **TriadicDomain** | the GSI-RTD interface chemistry implements; TRC is a *conformant domain*. |
| **Symmetric retirement rule** | every gated claim names what a *failed* falsifier REMOVES, not only what a passed one admits (§8, §9.9). |
| **TMAC** | the Triadic Multi-Agent Chemistry topology (§11): one agent per (layer, pillar) cell + a per-layer generalizer + a node generalizer, run shared-nothing over the GSI-RTD `TriadicDomain`; **no new orchestration** — the value claim is gated by TMAC-P10/P11 (§11.7). |

---

## 11. TMAC — Triadic Multi-Agent Chemistry: the agent topology over the conformant domain

> **Leading thought — P. Nikolov.**
> *Let's be cynical: we are not curing chemistry. We are sorting its laundry.*
>
> Tip the socks, shirts and briefs into one drawer and every morning is a war — you dig, you curse, you never find the matching pair. Put them in three bags — socks, shirts, briefs — and you are dressed in thirty seconds.
>
> Chemistry has always been one drawer. Triadic Chemistry is three bags: **Form, Position, Action.** I did not invent a new sock. I stopped letting people dump them together and call the rummaging "expertise."
>
> Most of the cost in chemical design is not ignorance — it is **disorder**: a combinatorial dig through an undivided pile. Sort the pile and the search collapses from a *product* to a *sum*; hand each bag to its own agent and they search in parallel; and the **empty bag tells you instantly why you have nothing to wear.** That is the whole contribution — not new clothes, a closet that finally has drawers.
>
> And the catch is in the same joke: three bags help **only if the things actually separate.** If chemistry's socks are sewn to its shirts, the sorting leaks — and that is the one test that decides whether any of this is real (**P0**). We are not changing chemistry — we are changing its underwear.

> **READ FIRST — what §11 IS and is NOT.** §11 contributes **no new chemistry and no new theory.** Every scoring primitive (`U=∛(F·P·A)`, δ⋆/SI over leaves, the GSM `P_fail`), every axis assignment (§2), every proxy (§2.5), every falsifier (§8), and the entire firewall (§6.4–6.5, §9.7) are **inherited unchanged** from the sections above. §11 specifies only the **agent topology and message flow** by which the *already-specified* TRC domain object is driven by the *already-specified* GSI-RTD runtime (`search → scheduler → TAA-agents → cycle → score → learn`). Its single defensible claim is an **AI-orchestration** claim — that an *orthogonal* F/P/A × L1–L4 decomposition turns a monolithic design/discovery problem into clean, agent-owned sub-problems that parallelize and that surface a bottleneck — and that claim is **strictly conditional on the §8 separability falsifiers (TRC-P0/P0e/P9) and is itself benchmark-gated by TMAC-P10/P11 (§11.7).** Until those pass, §11 is **INTERPRETATION/B1-pending**: a true-of-the-architecture mapping, not evidence it beats a baseline. **This is the whole point of the section: the value is real only if it is benchmarkable, and it is unproven until it is benchmarked.**

> **Honest positioning vs prior art (stated once, here).** Multi-agent chemistry AI is **solved territory** — LLM tool-use agents (ChemCrow, Coscientist; ReAct/AutoGen/CrewAI role-agents), autonomous self-driving labs (A-Lab and the BO-driven acceleration platforms), and hypothesis-generation systems (the AI co-scientist with its supervisor + Elo tournament) all exist and several are productized. **TMAC does not claim to invent agentic chemistry, closed-loop discovery, tool-use, or multi-agent orchestration.** Across that prior art the decomposition is *emergent* (ReAct), by *epistemic role* (generate/critique/rank), by *capability* (planner/coder/automation), or a *domain-specific pipeline / retro-tree*; and the aggregation is almost universally **compensatory** (weighted sum, Pareto, Elo, LLM-judge) or a bare pass/fail gate. TMAC's only novel-in-combination levers are the two TRC already owns: **(i)** a fixed, problem-**orthogonal** typed factorization (F/P/A × L1–L4) where each cell is an agent-owned sub-problem with a clean interface, and **(ii)** a **non-compensatory** geometric combiner whose weakest factor both *vetoes* the aggregate and *names the responsible agent* as the compute/experiment-routing signal. Neither piece is new alone (non-compensatory MCDA is standard; orthogonal decomposition is old); the **combination, applied as the agent-scheduling primitive,** is the claim — and it is gated.

### 11.1 The topology — `4 × 3 + 4 + 1` agents over the GSM grid

TMAC instantiates exactly the §2.9 Gaussian Stability Matrix as a **runtime org chart**: the 4-layer × 3-pillar GSM cell `s_ij` becomes a **pillar-agent** `Aᵢⱼ`, each row gets a **layer-generalizer** `Σᵢ`, and the node gets a single **node-generalizer** `Σ_node`. There is one agent per scored cell and one generalizer per aggregation level — no more, no less.

```
                                  Σ_node   (node verdict: U_node, P_fail(node), weak-zone routing)
                                     │   reads ONLY the four Σᵢ reports (one-directional, §3.2.2)
            ┌────────────────┬───────┴────────┬────────────────┐
           Σ_L1             Σ_L2             Σ_L3             Σ_L4         (layer generalizers)
       (design row)     (synthesis row)   (use row)      (society row)
        ┌──┼──┐          ┌──┼──┐          ┌──┼──┐          ┌──┼──┐
       F11 P12 A13      F21 P22 A23      F31 P32 A33      F41 P42 A43     (12 pillar agents)
        │   │   │        │   │   │        │   │   │        │   │   │
      embed build enum  …   …   …        …   …   …        …   …   …
      _form _pos _act
            domain-interface calls (§11.3) — each agent OWNS one (layer, pillar) sub-problem
```

| Agent | `role` tag (§23.2) | Owns (the clean sub-problem) | Reads | Writes |
|---|---|---|---|---|
| `Fᵢ₁` Form-agent, layer i | `'form'` | identity/structure scoring for layer i: `embed_form` → `f.thermo, f.kinetic_persistence` | only its own layer-i Form inputs + `state s` | cell belief `(μ_i1, τ_i1)` |
| `Pᵢ₂` Position-agent, layer i | `'position'` | phase/context/hull for layer i: `build_position_graph` → `q, c`; `E_hull` lives here (§2.5) | only its own layer-i Position inputs + `s` | cell belief `(μ_i2, τ_i2)` |
| `Aᵢ₃` Action-agent, layer i | `'action'` | reactivity/function for layer i: `enumerate_actions` + `execute_action` → `a.*` (band-centred, two-sided, §2.6) | only its own layer-i Action inputs + `s` | cell belief `(μ_i3, τ_i3)` |
| `Σᵢ` layer-generalizer | `'generalizer'` | roll up row i: `P=√(q·c)`, `F/A=wgeomean`, `Uᵢ=∛(F·P·A)`, `δ⋆/SI`, `P_fail(layer i)` | the three cells of **its** row only | layer verdict + `weak_leaf(i)` |
| `Σ_node` node-generalizer | `'generalizer'` | node roll-up `U_node=wgeomean_i(Uᵢ)` or the **one-directional** L-coupling (§3.1; NEVER cross-substance); node weak-zone; GSM-Priority routing | the four `Σᵢ` reports only | node verdict + routing signal |

The **agent count is `4·3 + 4 + 1 = 17`** for one declared node at the four canonical layers — the exact `3N+1`-per-level scaling of TAA's "N problems → N teams" rule (here N = 4 layers, plus the node-level Σ). Recursion (§2.3, `depth d ⇒ 3^d` sub-entities) is **never enumerated**: a pillar-agent that needs a child node spawns a child TMAC sub-team **only when the scheduler's leverage rank (§11.4) selects that cell** — the agent tree is grown lazily by the weakest-pillar signal, not eagerly by the combinatorial table (§6.1 coverage-gap discipline; the Scheduler Sufficiency Conjecture, GSI-RTD §6.1, governs "how many cells is enough").

### 11.2 The clean interface per agent — a typed contract, not a conversation

Each pillar-agent's sub-problem is defined by **one typed input/output contract**, not by a shared chat transcript. This is the orthogonality guarantee made executable (TAA Minimal Canonical Instruction Set rule 2, "keep their analyses orthogonal"; GSI-RTD §5.2 shared-nothing model):

```
PillarAgent[i,j] :  (state s, layer_inputs_ij)  ⟶  CellBelief{ mu, tau, provenance[], coverage, consensus_pct, low_score_cause }
                    └─────────── disjoint per (i,j) ───────────┘        └──── the §2.9.3 (μ,τ) of GSM cell s_ij ────┘
```

- **Input disjointness (the silo).** `layer_inputs_ij` is the slice of the §2.5 proxy table for layer i, pillar j — and *only* that slice. A Form-agent never sees ORD yields; an Action-agent never sees the space-group registry. The `state s` (T, P, pH, solvent, redox, load) is the **only shared read**, and it is **read-only and immutable within a generation** (GSI-RTD §5.2 "agents share no mutable state during a single LGP cycle"). One axis per edge (§2.7) is what makes the slices disjoint: an `IS_A`/`COMPOSED_OF` edge feeds only Form-agents, an `IN_PHASE`/`ON_HULL_WITH` edge only Position-agents, a `REACTS_WITH`/`CATALYZES` edge only Action-agents.
- **Output typing (the envelope).** Every agent emits exactly the §9.8 claim envelope's per-cell content, now as the GSM `(μ, τ)` pair (§2.9.3) plus its provenance, coverage, consensus, and `low_score_cause` tag. **No agent emits a verdict, a colour, a ranking, or an arrow** — those are generalizer-only (TAA rule 3). A pillar-agent emitting `dft_only` Action renders `"not yet interpretable — separability/measurement pending"` (§9.8), so the silo cannot manufacture false confidence.
- **No cross-talk in reconnaissance (TAA Phase I).** During the scoring phase the twelve pillar-agents run **independently and in parallel, no cross-talk** — they do not read each other's `(μ, τ)`. Cross-cell information enters *only* as the GSM covariance `Σ` off-diagonals (`ρ_FPA`, `ρ_layer`, §2.9.3), and `Σ` is **provenance-gated**: an off-diagonal that was *assumed* rather than *estimated from a P0/P0e/P9 run* is `axis_unseparated` and renders no coupling (§2.9.3). Crucially, **the agents do not negotiate the correlations — they report marginals, and the framework reads the dependence from the falsifier statistics.** This is the design discipline that keeps "clean interfaces" from being a fiction (see §11.6).

### 11.3 The EXACT mapping onto the GSI-RTD `TriadicDomain` (so the existing runtime drives it)

TMAC writes **zero orchestration.** The five-method `TriadicDomain` contract (§A.3) is implemented once for chemistry, and the pillar-agents are nothing but the natural owners of those methods. The mapping is one-to-one:

| `TriadicDomain` method (GSI-RTD §A.3 / §20.3.2 / §22.1) | TMAC owner | Returns | TRC section |
|---|---|---|---|
| `embed_form(node, s)` | the layer's **Form-agent** | structure/identity embedding → `f.thermo, f.kinetic_persistence` | §2.5, §3.1 |
| `build_position_graph(node, s)` | the layer's **Position-agent** | phase/solvation/hull context graph → `q, c` (`E_hull` on Position) | §2.5, §2.7 |
| `enumerate_actions(node, s)` | the layer's **Action-agent** | candidate reactions/functions (open-world guard, §2.7) | §2.6, §3.4 |
| `execute_action(node, action, s)` | the layer's **Action-agent** | simulate reaction/use over horizon → `a.*` (extent at operating activities, §2.6) | §2.6, §3.3 |
| `evaluate_sss(node)` | the **generalizer** `Σᵢ` / `Σ_node` | `U, δ⋆, SI`, GSM `P_fail`, `weak_leaf` | §2.2, §2.9 |
| `expected_si(s)`, `risk(s)` | per-cell, from the GSM posterior | `E[SI]` = posterior mean of `Uᵢ`; `Risk` = `P_fail` / interval width (§2.9.5) | §2.9.4–5 |
| `cost(s)` = `(C_time, C_space, C_energy)` | per cell/agent | Form-axis = wall-time of `embed_form`+DFT; Position-axis = memory/DB calls; Action-axis = compute/sim/jury tokens (GSI-RTD §22.1) | §11.4 |

Because the estimator contract is **estimator-agnostic** (GSI-RTD §20.3.2 — "what matters is that `E[SI_i]` and `Risk(S_i)` are produced; how is a domain implementation choice"), TMAC supplies them straight from the §2.9 GSM Monte-Carlo posterior (the `(c)` Monte-Carlo / `(b)` Bayesian-posterior estimator families), and the **existing** `TriadicScheduler`/`TriadicAgent`/`TriadicBudget`/`SSSEvaluator` classes (§23.2) and the `gsi_runtime` loop (§23.1) drive it with **no bespoke code**. Reference skeleton (structural only, RUO — no executable chemistry, no synthesis):

```python
class ChemTriadicDomain(TriadicDomain):                 # the ONE object TRC supplies (§A.3)
    def embed_form(self, node, s):            ...        # owned by Form-agent  (role='form')
    def build_position_graph(self, node, s):  ...        # owned by Position-agent (role='position')
    def enumerate_actions(self, node, s):     ...        # owned by Action-agent (role='action')
    def execute_action(self, node, a, s):     ...        # owned by Action-agent
    def evaluate_sss(self, node):             ...        # owned by Σ (role='generalizer'); §2.2 + §2.9 keystone UNCHANGED
    def expected_si(self, node):   return gsm_posterior_mean_U(node)      # §2.9.4
    def risk(self, node):          return gsm_P_fail(node)                # §2.9.5
    def cost(self, node):          return (C_time, C_space, C_energy)     # §22.1

# everything below is INHERITED, not written by TRC:
#   TriadicScheduler  (§23.2) — hard_gates G1–G4 + geometric Score; G4 = the weakest-pillar gate
#   gsi_runtime       (§23.1) — GENERATE→SCHEDULE→EXECUTE(Multi-LGP+TAA)→EVALUATE(SSS)→FEEDBACK→PRUNE
#   Parallel-LGP      (§5.2)  — shared-nothing execution, conflict detection, barrier sync
#   Learning Law      (§26.3) — impact/weight/policy updates;  β-transfer (§26.4)
```

> **Firewall is a hard gate, not an agent opinion.** `DZ-1`/`DZ-3` (§3.3) place the **dual-use type-check FIRST**: `target_type_check ∈ {ALLOWED, FORBIDDEN_PENDING_REVIEW, TYPE_FORBIDDEN}` (§9.8) is evaluated **before** any pillar-agent is spawned. A `TYPE_FORBIDDEN` node is **never enumerated** and never assigned a team; the incidental-discovery halt (§6.5) interrupts any run whose leverage analysis surfaces a destabilization path. The firewall binds the agent topology exactly as it binds point scores — it is **ungated and never retired** (§9.9). TMAC adds **no autonomous action**: `DZ-10` produces `queue_for_lab`, never `pass`; there is no closed-loop wet-chemistry call (§9.4).

### 11.4 Where orthogonality buys parallelism — and the bottleneck signal

**Parallelism (the upside, conditional).** If the §11.2 input slices are genuinely disjoint, the twelve pillar-agents have **no data dependency** within a generation, so they execute concurrently under the shared-nothing model with coordination cost **`O(sync_points × N)`, not `O(steps × N²)`** (GSI-RTD §5.2). The only synchronization is the three generation-level barriers — **LGP-4 (Impact Ranking)**, **LGP-9 (Resource Allocation / budget check)**, **LGP-12 (Final Audit / Σ roll-up)** — at which the generalizers, *not* the pillar-agents, exchange information. Conflict detection is inherited verbatim: two agents conflict iff `Position(Sᵢ)==Position(Sⱼ) AND Action(Sᵢ)≠Action(Sⱼ)`, resolved lexicographically by `E[SI]` then `Risk` then timestamp (§5.2). In chemistry such conflicts are rare *because the Scheduler assigns agents to non-overlapping regions of triadic space* — which is exactly the orthogonality premise, restated as a runtime property.

**The bottleneck signal (the genuinely-new affordance).** The non-compensatory combiner makes the **weakest pillar name the responsible agent**:

```
weak_leaf  = argmin over leaves L = {f.thermo, f.kinetic_persistence, q, c, a.*}       (§2.2)
weak_pillar = the pillar owning weak_leaf      ⇒      the AGENT to which the next compute/experiment is routed
```

Because `U=∛(F·P·A)` collapses to 0 if any pillar collapses, the gradient of the aggregate w.r.t. each pillar is **largest at the smallest pillar** — so the cell that most limits `U_node` is, by construction, the cell whose agent the controller should fund next. The routing target is the GSM uncertainty-aware leverage (§2.9.5):

```
GSM-Priority(cell ij) = E[ΔP_fail(node) | intervene on cell ij] / ∛(C_time · C_space · C_energy)
```

This is what no prior-art combiner does: a weighted-sum / Pareto / Elo / LLM-judge aggregate gives a *ranking*, not a *responsible sub-problem*. `GSM-Priority` does both — and it makes **two kinds of move comparable on one axis**: a *structural* lever ("the synthesis-Action is known-low → re-route to the Action-agent for an axis-matched route edit," §3.5) and a *buy-evidence* lever ("the L4-context cell is wide because the observable is missing → re-route compute to *measuring* it, shrinking `τ`," §2.9.5). The weakest-pillar routing is therefore the **active-learning policy**: it says *which agent's sub-problem is limiting and where the next unit of compute/experiment should go.* **Hard boundary unchanged:** `GSM-Priority` is strictly **within ONE declared node** — there is no cross-substance/cross-task `P_fail` ranking or ℳ-allocation, for the O5b-chem reason in §6.4 (a cross-substance `ΔP_fail/cost` ranking would reconstruct the worth ordering without the word "worth").

### 11.5 The two nested cycles and the learning loop (inherited, not invented)

TMAC runs the corpus's two nested cycles unchanged:

- **Per-node (the TAA 4-phase / LGP-12 = TRC DZ-1…DZ-12 cycle, §3.3).** Phase I Reconnaissance (pillar-agents scan in parallel, no cross-talk) → Phase II Triadic Analysis (`Σᵢ`/`Σ_node` find `weak_leaf`) → Phase III Solution (each agent proposes a fix **only on its own axis**, compensation rejected at DZ-9) → Phase IV Execution & Audit (Position plans, Action executes the *simulated* step, Form guards identity, Σ computes final SI / `P_fail`). The firewall gate is DZ-1, first.
- **System-level (the `gsi_runtime` generation loop, §23.1).** `GENERATE (rtd_decompose over target×route) → SCHEDULE (triadic_scheduler, G1–G4 + geometric Score) → EXECUTE (Multi-LGP batches of TMAC teams) → EVALUATE (sss/GSM) → FEEDBACK (knowledge_base.update + budget.deduct) → PRUNE & EXPAND`. Halting obeys Proposition 22.1: run only if a queue exists with coverage ≥ θ, cost ≤ budget on all three axes, SI ≥ θ_stability; otherwise **decompose the goal further** (spawn child TMAC teams).
- **Learning Law (§26.3) and β-transfer (§26.4).** Across generations the impact `impact^{(g+1)}(f,p,a) = (1−λ)·impact^{(g)} + λ·observed_SI` (λ=0.3), the correlation-driven weight update, and the policy schedule (ε-greedy → UCB1 → Thompson) adapt the scheduler — making the static two-stage filter an **adaptive active-learning policy** judged by regret/convergence (§20.6). **β-transfer is the cross-program prior**, applied *only across slices of ONE design program* (DZ-12), with β = the §26.4 triadic structural-similarity (Form-embedding cosine, Position-graph isomorphism, Action-set Jaccard); on negative transfer (SI_with < SI_without for ≥5 candidates) **β→0** and the domain pair is flagged non-isomorphic (FM-7). **Note:** this β is the *transfer coefficient* (§26.4), **not** the unrelated hallucination-rate β.

### 11.6 The honesty bar — TMAC's value is CONDITIONAL on separability and degrades gracefully if it fails

This is the load-bearing caveat, not a footnote. **Every TMAC value claim is downstream of the §8 separability falsifiers, because the "clean interfaces" are a fiction exactly to the degree that F/P/A are entangled.**

- **If TRC-P0 / P0e fail (F/P/A conditionally collinear for substances/routes — *the a-priori-likely outcome*, since one electronic-structure calculation dictates structure, energetics, and reactivity at once, §2.5(a) DFT-from-one-structure confound):** the pillar-agents' input slices are **not disjoint** — they are three transforms of one calculation. Then (i) the "no-cross-talk parallelism" is illusory because the agents are scoring correlated views of the same number; (ii) the GSM off-diagonal `ρ_FPA → 1`, so `U`'s posterior degenerates to a near-point with **no triadic structure** (§2.9.7-3) and the bottleneck signal becomes **misleading** — `argmin` over collinear leaves is dominated by anchor/normalization choice, not by a real limiting sub-problem; and (iii) §3–§6 are **deleted** (§A.0), so TMAC has nothing to orchestrate. **In that world TMAC reduces to a fancier scalarization with no edge over a monolithic agent — and the section is retired with the engine.**
- **If TRC-P9 fails (the four layers are mutually rank-redundant):** the four-row topology collapses — the layer-generalizers `Σᵢ` are scoring relabelings of one `U`, so the `4×3` grid is over-parameterized and should collapse to fewer rows (§8 TRC-P9 "layering reported as relabeling"). The parallelism across layers is then spurious.
- **The graceful-degradation contract.** TMAC inherits the symmetric-retirement rule (§9.9): a failed separability gate **removes** the multi-agent decomposition from the renderer and reverts to the single-axis (property-only) scorer — the agents are deleted, not reinterpreted. **`Σ` does not rescue this** — it *displays* it (§2.9.7-3): a degenerate posterior is the honest signal that the topology has no orthogonality to exploit. The firewall, the lint, and the hazardous-synthesis refusal survive any such retirement (§9.9).

### 11.7 The benchmark — TMAC's orchestration value is UNPROVEN until this passes (pre-registered, symmetric retirement)

The value claim ("orthogonal decomposition + non-compensatory routing beats the alternatives") is **not a theorem and not a finding — it is a wager with a falsifier.** Per the §8 discipline (conditional dCor/CMI where relevant; family-level unit of independence R8; 0.6–0.8 inconclusive band; power calc first; study-level FDR; leakage audit). This is the §11 instance of the §8 matrix; the **TRC-P10 (TMAC value)** row is mirrored in the §8 matrix (just as GSM-P1/P2 is), under the same symmetric-retirement contract.

| # | Claim under test | Falsifier | Pass → admits | **FAIL → REMOVES** |
|---|---|---|---|---|
| **TMAC-P10** | the **orthogonal F/P/A × L1–L4 decomposition + weakest-pillar / `GSM-Priority` routing** reaches a fixed target (a held-out (substance, route) goal on MP/OQMD/ORD-class data) **with fewer simulated experiments / less compute, or at higher hit-rate,** than **(i)** a monolithic ReAct-style tool-use agent and **(ii)** a standard BO / active-learning loop with a **compensatory** scalarization (weighted sum / Pareto) — *same task, same tools, same budget* | the budget-to-target / hit-rate CI **includes 0** (or favours a baseline) against the **strongest** baseline, at achievable family-level *n* | the triadic decomposition + non-compensatory routing is a delivered, gated orchestration value | **the orchestration claim is retired**; TMAC reverts to "a conformant domain object with no demonstrated routing advantage over a monolithic / ad-hoc agent" — the §11 topology is documentation, not a result |
| **TMAC-P11** | the advantage is **caused by the non-compensatory bottleneck signal**, not by the extra agents/compute | an **ablation** — replace the geometric `Score`/`GSM-Priority` routing with a compensatory weighted-sum router while holding the agent topology and budget fixed — **recovers the same budget-to-target** (the routing rule carries no signal); OR the advantage vanishes once parallel-agent compute is **cost-charged on the Action axis** (it was buying speed with tokens, not with structure) | the non-compensatory routing is the operative lever | **the routing discipline is retired as ornamentation**; any speedup is attributed to parallel compute, not to the triadic combiner |

**Protocol sketch (TMAC-P10/P11).** Fix a panel of held-out design/discovery goals with **measured** outcomes (ICSD on-hull confirmation; recorded ORD route success at a yield threshold; measured material property meeting a spec). Run, on identical tools and an identical triadic budget `(T,S,E)`: **(A)** TMAC (this topology, geometric `Score` + `GSM-Priority` routing); **(B)** a monolithic ReAct tool-use agent over the same tools; **(C)** a BO/active-learning loop with a weighted-sum acquisition; **(D)** the TMAC topology with its router swapped to a weighted sum (the P11 ablation). Primary metric: **simulated experiments (or compute) to first target hit** and **hit-rate at fixed budget**, with the **0.6–0.8 inconclusive-band** discipline and a power calc preceding the run. **The win must be isolated to the regime where non-compensation can differ from an average — the one-low-pillar / near-zero subset (TRC-P0b, §2.2)** — or it passes trivially. The whole benchmark is **downstream of and conditional on TRC-P0/P0e/P9**: if separability fails, TMAC-P10/P11 are not run (there is nothing orthogonal to exploit), and the topology is retired with §3–§6.

> **Boxed law (TMAC, one line).** *An orthogonal F/P/A × L1–L4 factorization makes chemistry tractable for multi-agent AI only if the axes are actually separable; given separability, the non-compensatory combiner turns the weakest pillar into both a veto and an address — naming which agent's sub-problem is the bottleneck and where the next experiment goes — and the whole topology is deleted if it does not beat a monolithic or compensatory baseline at equal budget.*

### 11.8 Epistemic status & scope of §11

- **Epistemic level.** The topology↔interface mapping (§11.1–§11.5) is **B1** (true *of the architecture* — a wiring identity over the inherited classes) once inputs exist; the **orchestration value claim** (§11.4, §11.7) is **B3-pending** — a pre-registered prediction gated by TMAC-P10/P11, never a finding. **No §11 sentence is B4**; TMAC drives only the simulated/RUO surface (§9.4), and any B4 (real synthesis/deployment) sentence is a bug.
- **What is TRC-specific vs canon-general.** The **construct** "one agent per (layer, pillar) GSM cell + per-row + node generalizers, run shared-nothing over the five-method `TriadicDomain`, routed by weakest-pillar `GSM-Priority`" is **canon-general** (it is just TAA's `3N+1` topology applied to the GSM grid and is liftable to TRB/TSE verbatim). The **instance** — the four layers = {design, synthesis, use, telos}, the chemistry proxy slices (§2.5) as the agent input contracts, `E_hull` on the Position-agent, the firewall-first DZ-1 gate — is **TRC-specific.** Recommended placement: keep §11 in TRC, gated by TMAC-P10/P11; assess for lifting once the benchmark has passed in **at least two** domains (the cross-domain comparability question is SSS-L5, still open).
- **Relation to inherited constructs.** §11 **consumes and does not duplicate**: the §23.2 classes, the §23.1 loop, the §5.2 Parallel-LGP model, the §20 scheduler (G1–G4 + geometric Score), the §26.3/§26.4 Learning Law and β-transfer, the §2.9 GSM, the §3.3 DZ cycle, and the entire firewall/lint (§6.4–6.5, §9.7, §9.8). It adds **no new axis, no new currency, no new aggregation, and no new orchestration** — only the agent-ownership wiring and its benchmark.

---

> **Net.** TRC registers the U-Theory triad onto chemistry and materials as a **sibling of TRB and TSE**: one recursive `ChemSystem` node scored `U = ∛(F·P·A)` — identity (F↔Time; elemental formation depth), phase/context/hull (P↔Space; `E_hull` lives here), reactivity/function (A↔Energy; extent at operating activities, ΔG gating extent not possibility) — non-compensatorily, with δ/SI computed over leaves, across four layers. **L1** makes inverse design a two-headed triadic search (target × route, coupled one-directionally); **L2** scores a made substance with its route for stability and integrates it as `ℳ = ∫U dt`; **L3** selects materials by triadic fit, benchmarked honestly against **constraint-screened Ashby** (whose screen already supplies the veto — TRC's narrow claim is graded axis-localization); **L4** judges the substance's *societal* Action under a declared, human-owned telos sign. The objective is `ℳ` of **one declared node, never aggregated across substances/tasks/designs**; the ceiling is **B3-pending**, both B4 slots **empty by intent**; the hard boundaries are "not a laboratory protocol," "no cross-substance worth ranking or ℳ-allocation," and the **sign-symmetric, type-forbidden firewall** against explosives, CW/BW agents and precursors, illicit drugs, and net-harmful pollutants — no hazardous recipe anywhere, the threat stated once and its method never described. Its first job is to try to **kill its own load-bearing assumptions**: prove a substance's and a route's F/P/A are *conditionally* separable with the task held fixed (TRC-P0/P0e), that `E_hull` does not double-load two pillars (TRC-P0d), that the four layers are non-redundant (TRC-P9), and that geometric `U` beats a property-only, a **constraint-screened-Ashby**, and an additive baseline *in the regime where it can differ* against real `E_hull` / formation-enthalpy / measured-stability / service-outcome truth (TRC-P0b/P1/P2/P4) — **before** claiming anything about design, synthesis, selection, or telos. *"Design the most stable matter" is VISION/telos that orients the sign — never a deliverable, never a ranking, and never an arbiter of which substances are allowed to exist.*

---

**Author:** Petar Nikolov (ORCID 0009-0001-8669-2276) · **Parent record:** DOI 10.17605/OSF.IO/74XGR · **Brand:** U-Score.info / U-Model.org / 911.bg
**Copyright © 2026 Petar Nikolov. All rights reserved. Content licensed under CC BY 4.0; reference code under MIT.**
**Canonical invariant:** Form ↔ Time · Position ↔ Space · Action ↔ Energy. **Project epistemic ceiling: B3-pending. Both B4 slots (synthesis-action, deployment/societal) empty by intent. RUO — NOT a laboratory protocol, NOT a chemical/materials device, NO hazardous synthesis anywhere.**
