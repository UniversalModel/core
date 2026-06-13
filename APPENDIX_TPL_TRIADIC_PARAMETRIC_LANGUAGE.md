# APPENDIX TPL — TRIADIC PARAMETRIC LANGUAGE
## A Project Specification for a Low-Entropy, Guardrailed, Triadic Language

> **Document status:** Project appendix / language specification (v1.0)
> **Date:** 2026-05-02
> **Framework:** U-Theory v27 candidate
> **Level:** L1/L2 operational design; L3 only where claims concern universal language emergence.
> **Purpose:** Define a prototype language whose grammar forces every statement to separate Form, Position, and Action, while adding compact verification guardrails for source, confidence, scope, and time.

---

## 0. EXECUTIVE SUMMARY

TPL is a proposed **Triadic Parametric Language**: a controlled language for humans and AI agents designed to reduce ambiguity by forcing every sentence into three orthogonal layers:

1. **F — Form:** what the thing is.
2. **P — Position:** where, when, for whom, and under what frame it is true.
3. **A — Action:** what happens, changes, causes, permits, forbids, or follows.

The core idea is:

> Natural language often mixes identity, context, and action in the same phrase. TPL separates them, so errors become visible.

TPL is not intended to replace natural language. It is intended for **high-stakes cognition**:

- AI-to-AI communication
- legal reasoning
- scientific claims
- multi-agent coordination
- prompt engineering
- governance protocols
- theory formalization

---

## 1. WHY TPL EXISTS

Natural languages are powerful but noisy. They compress identity, context, intention, evidence, and modality into the same sentence. This creates:

- hidden assumptions
- ambiguous scope
- unclear source
- weak confidence tracking
- mixed metaphor and fact
- causal overclaiming

TPL is a response to that problem. It makes every statement pay three prices:

| U-Theory pillar | Language layer | Question answered |
|---|---|---|
| Form | F-layer | What exactly is being referred to? |
| Position | P-layer | In what frame is the claim true? |
| Action | A-layer | What happens, follows, changes, or is commanded? |

If any layer is missing, the sentence is unstable.

---

## 2. DESIGN PRINCIPLES

### 2.1 Orthogonality

No lexical item should do two jobs at once.

| Bad natural-language blend | TPL split |
|---|---|
| "The court obviously violated rights." | F=court/order/rights; P=case/date/jurisdiction/source; A=violated/claimed/verified |
| "This theory proves dark matter." | F=theory/dark-matter-model; P=L3 speculative scope; A=interprets, not proves |
| "AI understands." | F=AI-system/task; P=test conditions; A=passes/infers/generates |

### 2.2 Canonical order

TPL sentences flow:

```tpl
F -> P -> A -> G
```

where:

- **F** = Form core
- **P** = Position frame
- **A** = Action move
- **G** = Guardrails

Guardrails are optional in casual TPL but mandatory in court/science/AI modes.

### 2.3 Minimum complete clause

The smallest stable TPL clause is:

```tpl
F{entity:type} P{frame} A{predicate}
```

Example:

```tpl
F{order:judicial-act} P{case:20267810400584; date:2026-04-29} A{imposes:attachment}
```

Meaning:

> A judicial order, in case 20267810400584 on 2026-04-29, imposes an attachment.

---

## 3. CORE SYNTAX

### 3.1 Canonical clause

```tpl
CLAUSE := F_BLOCK P_BLOCK A_BLOCK G_BLOCK?
```

### 3.2 Blocks

```tpl
F_BLOCK := F{ form_item (; form_item)* }
P_BLOCK := P{ position_item (; position_item)* }
A_BLOCK := A{ action_item (; action_item)* }
G_BLOCK := G{ guard_item (; guard_item)* }
```

### 3.3 Items

```tpl
item := key:value
```

Examples:

```tpl
F{person:Georgi_Dichev; role:private_enforcement_agent}
P{jurisdiction:Bulgaria; source:public_registry; time:2026-05-02}
A{status:active; claim:debtor_in_public_award}
G{src:registry; conf:0.82; scope:legal-public; level:L1}
```

---

## 4. THE THREE LEXICAL LAYERS

### 4.1 F-words: Form lexicon

F-words identify objects, categories, agents, concepts, records, and structures.

| Class | Examples |
|---|---|
| person | judge, agent, debtor, creditor, researcher |
| document | order, complaint, article, registry-entry, appendix |
| theory object | triad, currency, dimension, meaning-ledger |
| system | court, AI-agent, organism, institution |
| evidence | URL, snapshot, SHA256, archive-entry |

F-layer must answer:

> What is the thing?

### 4.2 P-markers: Position lexicon

P-markers define frame, relation, time, space, jurisdiction, observer, scope, and dependency.

| Marker | Meaning |
|---|---|
| `case:` | legal/case frame |
| `time:` | time or date |
| `place:` | physical or jurisdictional location |
| `source:` | source frame |
| `observer:` | observer/task frame |
| `scope:` | domain limitation |
| `rel:` | relation to another F-object |
| `level:` | epistemic level L0-L4 |

P-layer must answer:

> Under what conditions is this statement valid?

### 4.3 A-words: Action lexicon

A-words encode change, causality, modality, command, obligation, inference, and status.

| Class | Examples |
|---|---|
| physical | moves, binds, consumes, emits |
| legal | files, orders, appeals, violates, requests |
| epistemic | claims, proves, suggests, falsifies, supports |
| causal | causes, enables, blocks, increases, reduces |
| modal | must, may, cannot, should, forbidden |
| computational | parses, verifies, hashes, routes, decomposes |

A-layer must answer:

> What happens or follows?

---

## 5. PARAMETRIC GUARDRAILS

Guardrails are compact markers that prevent overclaiming.

```tpl
G{src:<source>; conf:<0..1>; scope:<domain>; level:<L0..L4>; time:<date>; mode:<assert|hyp|cmd|query>}
```

### 5.1 Required guardrails

| Guard | Meaning | Example |
|---|---|---|
| `src` | source type | `src:official_registry` |
| `conf` | confidence | `conf:0.91` |
| `scope` | valid domain | `scope:legal-public` |
| `level` | epistemic level | `level:L1` |
| `mode` | speech act | `mode:assert` |

### 5.2 Level tags

| Level | Meaning |
|---|---|
| L0 | meta / formatting / evaluation |
| L1 | directly observed / operational |
| L2 | model-based / cross-domain |
| L3 | speculative but structured |
| L4 | unproven physical/metaphysical extension |

### 5.3 Safe claim transformation

Natural:

> Meaning creates matter.

Unsafe TPL:

```tpl
F{meaning} P{universe} A{creates:matter}
```

Hardened TPL:

```tpl
F{meaning-gradient:informational-constraint; substrate:TSE}
P{framework:U-Theory; level:L3; domain:cosmological-model}
A{may-stabilize:triadic-structure; not_claim:established_physics}
G{src:APPENDIX_GEN+MMT; conf:0.35; scope:speculative-model; mode:hyp}
```

---

## 6. NESTED TRIADS

Complex ideas are built by nesting clauses.

```tpl
F{
  claim:(
    F{system:language}
    P{domain:high-stakes-reasoning}
    A{requires:guardrails}
  )
}
P{framework:TPL; level:L2}
A{supports:reduced_miscommunication}
G{src:APPENDIX_TPL; conf:0.70; mode:hyp}
```

Reading:

> The claim that high-stakes language requires guardrails, in the TPL framework, supports reduced miscommunication.

---

## 7. EXAMPLES

### 7.1 Simple factual statement

Natural:

> The file exists in the active folder.

TPL:

```tpl
F{file:APPENDIX_TPL_TRIADIC_PARAMETRIC_LANGUAGE.md}
P{path:C:\--- u-score\v.28\.md; time:2026-05-02}
A{status:exists}
G{src:filesystem; conf:1.00; scope:local; level:L1; mode:assert}
```

### 7.2 Legal evidence statement

Natural:

> The URL is broken but Wayback preserved a snapshot.

TPL:

```tpl
F{url:domino.vks.bg/...; snapshot:Wayback}
P{time_checked:2026-05-02; source:web+archive}
A{original:connection_refused; archive:preserved}
G{src:HTTP+Wayback; conf:0.92; scope:technical-evidence; level:L1; mode:assert}
```

### 7.3 Theory statement

Natural:

> Meaning is dimensionless but stability is dimensional.

TPL:

```tpl
F{meaning:scalar; stability:multi-currency}
P{framework:U-Theory; source:APPENDIX_DIM; level:L3}
A{relation:meaning_dimensionless; relation:stability_dimensional}
G{src:DIM; conf:0.68; scope:theory-internal; mode:hyp}
```

### 7.4 AI coordination command

Natural:

> Agent A should verify the source before drafting.

TPL:

```tpl
F{agent:A; task:drafting; artifact:source}
P{workflow:legal-evidence; before:final_text}
A{must:verify_source; then:draft}
G{src:workflow-rule; conf:0.95; scope:AI-agent; level:L1; mode:cmd}
```

---

## 8. ERROR MODEL

TPL treats communication failure as triadic imbalance:

| Error type | Missing layer | Example |
|---|---|---|
| identity error | F failure | unclear "he", "it", "this" |
| scope error | P failure | true in one jurisdiction, false in another |
| causal error | A failure | correlation stated as cause |
| overclaim error | G failure | L3 claim stated as L1 |

### 8.1 Stability index

For an utterance:

$$
SI_{TPL} = \frac{\sqrt[3]{U_F U_P U_A}}{(1+\delta)^2}
$$

where:

$$
\delta = \frac{\max(U_F,U_P,U_A)-\min(U_F,U_P,U_A)}{\max(U_F,U_P,U_A)+0.01}
$$

Guardrail quality can be added:

$$
SI_{TPL+G} = SI_{TPL} \cdot (1 + \lambda G_q)
$$

where `G_q` is guardrail completeness/accuracy and `lambda` is calibrated by experiment.

---

## 9. ENTROPY HYPOTHESIS

TPL does not claim every sentence is shorter. It claims that for high-stakes semantic transfer:

> TPL should reduce entropy per verified semantic unit.

Define:

$$
E_{TPL} = \frac{S_{verified}}{H(message) + C_{parse} + C_{guard}}
$$

where:

- `S_verified` = verified semantic units transferred.
- `H(message)` = Shannon entropy or compressed length.
- `C_parse` = parsing cost.
- `C_guard` = guardrail overhead.

Prediction:

> In complex domains, TPL should outperform natural language once ambiguity-repair cost is included.

Falsifier:

> If TPL has equal or higher total cost per verified semantic unit after training and tooling, the minimal entropy claim fails.

---

## 10. TPL MODES

| Mode | Purpose | Guardrails required |
|---|---|---|
| `casual` | notes, brainstorming | optional |
| `research` | theory claims | src, conf, level, scope |
| `legal` | evidence and complaints | src, time, jurisdiction, conf, hash if available |
| `agent` | AI-to-AI task routing | src, mode, task, dependency |
| `compiler` | machine parsing | all fields strict |

---

## 11. MVP PROJECT PLAN

### Phase 1 — Controlled notation

Deliverables:

- TPL grammar v0.1
- 50 example sentences
- dictionary of 100 F-words, 50 P-markers, 100 A-words
- guardrail schema

Success:

> A human can translate short legal/scientific claims into TPL consistently.

### Phase 2 — Parser

Deliverables:

- JSON representation:

```json
{
  "F": {"file": "APPENDIX_TPL_TRIADIC_PARAMETRIC_LANGUAGE.md"},
  "P": {"path": "C:\\--- u-score\\v.28\\.md"},
  "A": {"status": "exists"},
  "G": {"source": "filesystem", "confidence": 1.0}
}
```

- syntax validator
- missing-layer detector
- overclaim detector (`level:L3` + `mode:assert` warning)

Success:

> Parser identifies incomplete clauses and rejects layer mixing.

### Phase 3 — Translation tests

Datasets:

- legal facts
- theory claims
- AI task instructions
- scientific hypotheses

Metrics:

- parse success
- ambiguity reduction
- human agreement
- repair cost
- verified semantic units per token

### Phase 4 — AI-agent protocol

Use TPL as an internal message format:

```tpl
F{task:review; file:APPENDIX_MMT}
P{agent:critic; scope:L3_claims}
A{find:overclaims; output:patch_suggestions}
G{mode:cmd; conf:1.00; deadline:session}
```

Success:

> Multi-agent workflows show fewer missed assumptions and cleaner handoffs.

---

## 12. PROTOTYPE LEXICON

### 12.1 F dictionary starter

```txt
person, agent, court, judge, file, document, claim, theory, system,
triad, form, position, action, meaning, currency, dimension, source,
evidence, snapshot, hash, task, model, parser, grammar, clause
```

### 12.2 P dictionary starter

```txt
time, place, path, jurisdiction, case, source, observer, scope,
level, domain, before, after, relation, dependency, frame, version
```

### 12.3 A dictionary starter

```txt
exists, claims, supports, contradicts, verifies, falsifies, causes,
enables, blocks, reduces, increases, requires, permits, forbids,
routes, parses, compiles, archives, scores, maps, decomposes
```

---

## 13. RELATION TO U-THEORY

| U-Theory component | TPL implementation |
|---|---|
| Form | F-block |
| Position | P-block |
| Action | A-block |
| Stability | complete triadic clause |
| Meaning | verified semantic transfer |
| Guardrails | epistemic payment / verification tax |
| GSI-RTD | recursive triadic decomposition of thought |
| RH hardening | level tags and safe wording |
| TEF | claim evaluation metadata |

TPL is therefore the **linguistic interface of U-Theory**.

---

## 14. RISKS

| Risk | Mitigation |
|---|---|
| Too rigid for humans | Use modes: casual/research/legal/compiler |
| Too verbose | Use abbreviations and tooling |
| False precision | Require confidence and source tags |
| Ontology lock-in | Keep dictionaries extensible |
| AI hallucination in TPL form | Guardrails do not prove truth; they expose evidence status |
| Ambiguous mapping from natural language | Build translation guidelines and test inter-annotator agreement |

---

## 15. RESEARCH PREDICTIONS

| Prediction | Test |
|---|---|
| TPL lowers error in high-complexity domains | legal/scientific translation benchmark |
| TPL raises inter-agent coordination reliability | multi-agent workflow A/B test |
| Guardrail density has a knee | vary G-marker density and measure error/cost |
| Orthogonal F/P/A layers increase parse agreement | compare with natural-language annotations |
| TPL is adopted by AI agents before humans | monitor agent protocol emergence |

---

## 16. ONE-LINE SUMMARY

> **TPL is U-Theory turned into language: every sentence must name its Form, locate its Position, declare its Action, and pay its epistemic guardrail tax.**

---

*End of APPENDIX TPL v1.0.*
