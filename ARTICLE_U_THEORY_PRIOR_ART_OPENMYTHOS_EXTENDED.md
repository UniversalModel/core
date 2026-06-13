# U-Theory Prior Art Note — Supplementary Sections 18–23
## Extension of `ARTICLE_U_THEORY_PRIOR_ART_OPENMYTHOS.md`

> **Scope.** This extension does not revise Sections 1–17 of the original note. It adds six sections that lock the chronology against externally verifiable public sources, documents new architectural correspondences discovered after the original note was written, and refines the attribution request into a diagnostic test. The epistemic posture of the original article is preserved: this is still an authorship and prior-art claim, still falsifiable, and still narrower than any theft claim.

---

## 18. External Chronological Verification (L1 — calendar claim)

The original note (§1) documents the U-Theory internal record with dated file references. This section complements that by locking the OpenMythos side of the calendar against independent third-party sources that cannot have been influenced by the U-Theory repository.

### 18.1 The U-Theory record (internal, dated)

- `APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md` — formal derivation declared on **26 March 2026**, Sofia, Petar Nikolov, with historical note in §11 and Declaration of the Author at the top of the document.
- Runtime implementation (`gsi_runtime.py`) and multi-domain prototype (`gsi_multi_domain.py`) — dated **27 March 2026**.
- Parent DOI on OSF: [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR).

### 18.2 The OpenMythos record (external, independent)

The first verifiable public appearance of OpenMythos in third-party channels:

| Source | Date | Nature of evidence |
|---|---|---|
| Kye Gomez public announcement on X/Twitter, [@KyeGomezB](https://x.com/KyeGomezB/status/2045659150340723107) | 18 April 2026, 20:22 UTC | First-party launch announcement |
| [MarkTechPost editorial coverage](https://www.marktechpost.com/2026/04/19/meet-openmythos-an-open-source-pytorch-reconstruction-of-claude-mythos-where-770m-parameters-match-a-1-3b-transformer/) by Asif Razzaq | 19 April 2026 | Third-party technology press |
| [Dataconomy editorial coverage](https://dataconomy.com/2026/04/20/openmythos-project-attempts-to-reconstruct-claude-mythos-design/) | 20 April 2026 | Third-party technology press |
| DeepWiki index of `kyegomez/OpenMythos` | Last indexed 19 April 2026 (commit `806a8d`) | Third-party code-indexing infrastructure |
| First community issues opened on the repository | 20–22 April 2026 (issues #8, #9, #20, #23, #24, #25, #28, #44, #46, #48, #51) | Independent public interaction with the repo |

### 18.3 The verified gap

The earliest externally auditable date at which OpenMythos can be said to have entered the public record is **18 April 2026**. The U-Theory GSI-RTD record is dated **26 March 2026**. The gap is **23 days**, independently verifiable in both directions: U-Theory's side carries a DOI and repository history; OpenMythos's side carries social-media timestamps, third-party editorial dates, and an external code-indexing date that is not under either party's control.

This matters because the original note's calendar claim (§7) rests on the existence of a dated public U-Theory record that predates OpenMythos. That claim is now locked on both sides of the comparison, not just on the U-Theory side.

### 18.4 What external verification does not settle

External verification does not by itself decide the question of conceptual borrowing. An independent author can reach a triadic design in 23 days without ever having seen U-Theory. What external verification settles is only the narrow calendar point: if there is any attribution question to be asked, the dated record makes clear which party is being asked to cite which.

---

## 19. What Third-Party Coverage Implicitly Concedes

This section is an observation about language, not a claim about intent. It notes that the editorial community, without any knowledge of U-Theory, reached instinctively for triadic grammar when describing OpenMythos.

### 19.1 MarkTechPost (19 April 2026)

> OpenMythos instantiates this as a three-part structure: Prelude → Recurrent Block → Coda. The Prelude and Coda are standard transformer layers that run exactly once. The Recurrent Block is the computational core, looped up to T=16 times.

The editor — with no exposure to U-Theory — describes the architecture in explicitly triadic terms: "three-part structure," three named stages, each playing a distinct role. This is exactly the grammar U-Theory had already formalized four weeks earlier.

### 19.2 Dataconomy (20 April 2026)

> The OpenMythos architecture comprises three parts: Prelude, Recurrent Block, and Coda. Both Prelude and Coda are standard transformer layers, executed once, while the Recurrent Block functions repeatedly up to 16 times.

Again: "three parts." Again: three functional roles. Again: exactly the triadic decomposition grammar that U-Theory had formalized.

### 19.3 The interpretive move

Neither publication knew about U-Theory. That is the point. Two independent editors, reading the OpenMythos documentation cold, independently chose the words "three-part" and "three parts" as the most natural description of the architecture. The triadic framing is not imposed by U-Theory — it is what the architecture itself looks like when summarized by a disinterested third party.

This is exactly the condition under which a prior-art note is strongest: the downstream description of the later system reaches for the same grammar as the earlier dated record, even without knowledge of it. The coincidence is in the structure, not in the vocabulary.

### 19.4 The epistemic weight of this observation

L2 claim — structural. This does not prove copying. It proves only that the triadic framing is the natural description of the OpenMythos architecture, which is the same framing U-Theory had already published. That is enough to support the attribution request; it is not enough to support a theft claim.

---

## 20. The `swarms_corp` Context

The original note treated OpenMythos as a standalone release. This section adds context about its author's broader public portfolio, because that portfolio shifts the priors of the coincidence argument (§9) in a specific direction.

### 20.1 What the record shows

Kye Gomez's public X/Twitter profile describes him as "22 y/o Founder · @swarms_corp — Building The Agent Economy." The GitHub organization `kyegomez` maintains `swarms` and related multi-agent orchestration libraries. This is public, first-party, and unambiguous.

### 20.2 Why this is relevant to attribution

GSI-RTD is not a generic transformer paper. Its central claim (§5–§6 of the appendix) is explicitly that **intelligence emerges from orchestrated coordination of many narrow agents**, each specialized along one triadic axis. The document states this directly:

> GSI is orchestrated coordination of many narrow agents, each specialized along one triadic axis (Form, Position, Action, or Stability), operating under a shared evaluation function (SSS) and a shared procedural cycle (LGP-12).

That is the core design-space coordinate of `swarms_corp` itself. OpenMythos was released by the founder of a multi-agent orchestration company, into a public design space in which U-Theory had already published a formally dated triadic agent architecture twenty-three days earlier.

This does not demonstrate awareness. It demonstrates that the two projects occupy **overlapping public design space**, which is exactly the condition under which citation norms apply. It is also the condition under which an independent-reconstruction claim (§6 of the original note) becomes weaker: not because independence is impossible, but because the author was already publishing into the multi-agent orchestration space that U-Theory had formally mapped.

### 20.3 What this does not claim

This does not claim:
- that Kye Gomez saw U-Theory before publishing OpenMythos;
- that OpenMythos was developed inside `swarms_corp` using U-Theory artifacts;
- that any commercial relationship exists between the two projects.

It claims only that the design-space overlap extends beyond one repository into the author's broader public portfolio, which tightens the coincidence argument of §9.

---

## 21. Direct Public-Language Correspondence Table

The original note (§10) gave a conceptual correspondence table. This section supplies a stricter version using only publicly scraped OpenMythos wording alongside publicly dated U-Theory wording. Every left-column cell is from the OpenMythos public documentation or editorial coverage quoted under fair-use excerpts. Every right-column cell is from a dated file in the U-Theory record.

### 21.1 Architectural stages

| OpenMythos public description (April 2026) | U-Theory GSI-RTD public description (26–27 March 2026) |
|---|---|
| "Three-part structure: Prelude → Recurrent Block → Coda" | "A System is anything for which Form, Position, and Action can be defined … S = (F, P, A)" |
| "Prelude: standard transformer layers that process the raw token embeddings and produce an 'injection signal' e" | "Form (F) — structure, shape, what-it-is … Computational representation: Embedding vector in semantic space" |
| "Recurrent Block: looped stage that updates hidden state using hₜ₊₁ = A·hₜ + B·e + Transformer(hₜ, e) … re-injection is deliberate: without it, the hidden state would drift away from the original input signal" | "Position (P) — context, location, where/when … Computational representation: Graph node with typed edges and metadata" (context anchoring) |
| "Coda: final transformer layers that refine the recurrent output before it reaches the output layer" | "Action (A) — process, transformation, how … Computational representation: Action primitive with parameters and preconditions" (executable output) |

### 21.2 Stability and control

| OpenMythos mechanism | GSI-RTD / SSS prior art |
|---|---|
| LTI injection with ρ(A) < 1 enforced by construction to prevent residual explosion | "Non-compensatory stability: a system is not truly stable if one pillar collapses and the other two merely look strong on average … U = ∛(F·P·A) … explicit rejection of arithmetic averaging" |
| ACT halting: "harder positions receive more computation; tokens that have already converged halt early" | AD-RTD §1.1: "Fix the bottleneck first … prioritize the steepest axis" / Scheduler §20: resource-bounded selective traversal with per-axis weighting |
| Depth-wise LoRA: per-iteration differentiation "without adding substantial parameters" | GSI-RTD §5–§6: "orchestrated coordination of many narrow agents, each specialized along one triadic axis" — structural specialization under a shared parameter core |
| MoE with shared + routed experts: "shared experts absorb common cross-domain patterns while routed experts specialize" | TAA §1: "three orthogonal pillar agents and one generalizing agent" — three specialists + one generalist, the exact same split |

### 21.3 The TAA–MoE correspondence is the tightest

Of all the pairings, the TAA / shared-routed MoE correspondence is the strongest, because it is not a generic "three parts" resemblance. TAA specifies a **four-agent shell**: three pillar agents (F, P, A) plus a generalizer. OpenMythos's MoE layer specifies a **four-class expert structure**: routed experts specializing per token (three or more narrow specializations) plus **shared experts** that "absorb common cross-domain patterns."

Three specialists plus one generalizer is a less common design choice than it looks. The literature OpenMythos cites — DeepSeekMoE, Universal Transformer, Parcae — does not prescribe the three-plus-one split as a design rule. TAA does, explicitly, under the triadic axiom, and in a document dated three weeks earlier.

L2 claim — this is a specific co-occurrence of a non-trivial design choice, not a generic resemblance.

---

## 22. The Reverse Test (Fairness Check)

A good prior-art argument should survive a fairness test: if a neutral third party encountered the U-Theory record first and then encountered OpenMythos, would they read OpenMythos as an implementation of U-Theory?

### 22.1 The test

Imagine a reader who has read the GSI-RTD appendix cold, without any knowledge of OpenMythos. They then open OpenMythos's README for the first time. What do they see?

They see a system whose input is processed into an **embedding signal** that persists through iteration (the Form axis), whose **context is anchored** against drift by injecting that signal at every step (the Position axis), whose **output is produced** by a final stage after iteration (the Action axis), whose **stability is enforced non-compensatorily** by a hard spectral constraint plus halting (the SSS discipline), and whose **specialization splits** into shared-plus-routed experts (the TAA four-agent shell pattern).

If they then read OpenMythos's own explanation, they are told the design is derived from Universal Transformer, Parcae, DeepSeek-V2, ACT, and depth-wise LoRA.

The reader now holds two possible explanations of the same artifact:
1. OpenMythos is an independent reconstruction from the cited sources.
2. OpenMythos is a late-arriving implementation of a design space U-Theory had already mapped.

Both are possible. The point of the reverse test is not to force a choice. It is to observe that a reader who had seen U-Theory first would, without controversy, read OpenMythos as sitting inside that conceptual shadow. The readability of U-Theory → OpenMythos is symmetric with the readability of OpenMythos → U-Theory. Both directions make sense.

### 22.2 Why this strengthens the attribution case

The fairness of the reading is exactly what citation norms are designed to handle. Citations are not reserved for proven ancestry; they are used for legitimate conceptual neighborhood. Two projects that can be read into each other's conceptual shadow by a neutral reader trigger citation norms, regardless of whether direct ancestry can be shown.

That is why the requested remedy is so narrow (§15 of the original note): a single line of attribution in the OpenMythos references section, acknowledging U-Theory as dated prior art in the adjacent conceptual space.

---

## 23. Attribution Request as a Diagnostic Tool

This section reframes the request in §14 of the original note. The request is for a citation line. But the request is also a diagnostic — its response tells us something about the nature of the overlap.

### 23.1 Three possible responses

The OpenMythos maintainer can respond to an attribution request in one of three ways:

1. **Acknowledge and cite.** This closes the attribution question, preserves the historical record, and costs the OpenMythos project nothing. It is the baseline case.
2. **Dispute on evidence.** The maintainer could produce a dated public source predating 26 March 2026 that packages the same six-trait joint signature (§9 of the original note) independently of U-Theory. This would defeat the priority claim cleanly, and under §12 of the original note, the claim would be withdrawn. This is also a productive outcome.
3. **Decline without evidence.** The maintainer could decline citation while producing no predating public source with the joint signature.

### 23.2 What response (3) reveals

Response (3) is the diagnostic case. Declining citation while having no alternative dated source that carries the joint signature does not disprove the prior-art claim. It leaves the dated public U-Theory record standing as the best available answer to the question "where did this conceptual scaffold come from?"

This is not a gotcha. It is just a statement of how epistemic priority works: absence of an earlier joint-signature source, combined with presence of a dated public U-Theory record carrying that exact joint signature, leaves the U-Theory record as the calendar answer by default.

### 23.3 What this means for the request

The request remains what it was in the original note: attribution, not damages. But the request is now framed so that its rejection carries its own informational content. Either a cite appears, or an earlier joint-signature source is produced, or the dated public U-Theory record remains the best available prior art by the simple fact that no alternative has been presented.

All three outcomes are acceptable from a U-Theory standpoint. All three resolve the attribution question on evidence. None of them require a plagiarism claim, a takedown, or a damages theory. This is exactly the proportionality property described in §15 of the original note.

---

## 24. Closing Epistemic Summary

The extension in Sections 18–23 does not strengthen any claim beyond the original note's epistemic boundary. It does the following:

- **Locks the calendar** on both sides (§18), using third-party sources that neither party controls.
- **Documents the grammar** that independent editors used to describe OpenMythos (§19), showing that the triadic framing is the natural description even without U-Theory exposure.
- **Contextualizes the author** (§20), showing that OpenMythos was released into the multi-agent orchestration design space that U-Theory had formally mapped.
- **Tightens the correspondence table** (§21), replacing interpretive pairings with direct public-language quotations.
- **Applies a fairness test** (§22), showing that the U-Theory → OpenMythos reading is symmetric with the OpenMythos → U-Theory reading.
- **Reframes the request** (§23) as a diagnostic rather than a demand, so that all three possible responses resolve the attribution question on evidence.

The original note's posture is preserved: this is an authorship claim and a request for citation. It is not a takedown. It is not a damages claim. It is not a proof of theft. It is a calendar claim supported by a joint-signature argument, extended by externally verifiable dates and by the author-portfolio context of the OpenMythos release.

The strongest sentence of the original note (§13) still summarizes the complete position:

> U-Theory established public prior art for a triadic architecture of intelligence before OpenMythos appeared publicly. OpenMythos may still be an independent implementation built from the looped-transformer literature it cites, but that description is not a rebuttal to prior art. Its public architecture remains reasonably readable as a semantic recoding, and in several places an architectural operationalization, of a conceptual design space already articulated by U-Theory.

Sections 18–23 add evidence supporting that sentence. They do not replace it.

---

## 25. Suggested Revised PR Statement (Updated for External Verification)

The following one-paragraph statement replaces the PR statement in §16 of the original note, because the chronology is now externally verified on both sides:

> The public OpenMythos release dated 18 April 2026 entered a design space that the public U-Theory record dated 26–27 March 2026 had already mapped. The earlier record defines an AI triad of Form, Position, and Action, a recursive multi-agent architecture, a triadic scheduler over large combinatorial search spaces, a four-agent shell of three specialists plus one generalizer, and a non-compensatory System Stability Score logic in which the weakest bottleneck determines real robustness. OpenMythos's three-stage Prelude-Recurrent-Coda architecture, its spectral-radius stability constraint, its adaptive halting, and its shared-plus-routed expert split are each readable as engineering operationalizations of items already present in the earlier record. The request is attribution: a single citation line acknowledging the U-Theory record as dated prior art in the same conceptual space. The request is not damages, takedown, or any commercial claim. It is the minimum correct response when a maintainer becomes aware of earlier public work in the same conceptual space, and it is the response that citation norms in both open-source and academic practice are designed to produce.

---

*Extension authored: 24 April 2026, Sofia.*  
*Parent article: `ARTICLE_U_THEORY_PRIOR_ART_OPENMYTHOS.md`.*  
*Author: Petar Nikolov. ORCID: [0009-0001-8669-2276](https://orcid.org/0009-0001-8669-2276). DOI of parent framework: [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR).*
