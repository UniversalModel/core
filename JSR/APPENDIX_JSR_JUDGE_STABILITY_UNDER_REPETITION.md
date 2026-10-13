# APPENDIX JSR — JUDGE STABILITY UNDER REPETITION

## The noise floor of an LLM judge applied to normative criteria at scale

> *"A ranking that hides its own noise is not a measurement."*

| | |
|---|---|
| **Author** | Petar Nikolov |
| **Date** | 2026-08-03 · v1.1 2026-10-13 |
| **Framework** | U-Theory / U-Model · UMSG |
| **Status** | Empirical, measured on the live register |
| **Version** | 1.1 (v1.0 frozen as `APPENDIX_JSR_JUDGE_STABILITY_UNDER_REPETITION v1.0.md`) |
| **Peer review** | The core measurement was accepted after peer review as a lightning talk at AIMOS 2026 (Association for Interdisciplinary Metaresearch and Open Science, Wellington, 29 November – 2 December 2026): *"LLM-judge rank instability in a live public register: 1,439 organisations, two identical runs"* |
| **Epistemic Level** | **L1 — measured, not derived.** Every number here is an observation of a running system, reproducible from the deposited raw scores. No claim in this appendix follows from the triadic axioms; it constrains them. |
| **Prerequisites** | `APPENDIX_SSS` (the scoring engine), `APPENDIX_TAA` (the jury architecture this appendix argues is necessary), `THE HAND OF GOD` (HOG: a typed second judge and timestamped judgements) |
| **Function** | Establishes the resolution limit of a single-judge U-Score, and converts a published rank from a point into a band |
| **Invariant** | A rank may be reported only at a resolution the judge can reproduce |
| **Copyright** | © 2026 Petar Nikolov, CC BY 4.0 · code MIT |

---

## JSR.0 — Why this appendix exists

`APPENDIX_SSS` §Stage 2 specifies a jury: up to fifty models scoring every
principle in parallel, outliers filtered, agreement published. What runs in
production is the degenerate case of that specification — a jury of one —
because the compute available funded one model.

This appendix measures what that costs. It is not a defence of the single-judge
configuration; it is the evidence that the configuration is insufficient, stated
in numbers rather than in principle, so that the cost of the missing aggregation
layer is known before anyone relies on a published rank.

The register measured here is public and rebuilt nightly: seventeen tables,
about 4,300 institutions, scored against 45 published criteria on three axes and
combined as U = ∛(CODE × CREDO × RIGHTS).

**What version 1.1 adds.** Version 1.0 measured one judge against itself. In
the ten weeks that followed, the register measured five judges against each
other, a five-model jury, the effect of supplying an entity's own text instead
of its name, four training families against each other, and a judge that
returned a constant. It also added a second judge of a different kind: a typed
judge whose answers are probabilities over declared options, with every
judgement timestamped (`THE HAND OF GOD`). JSR.6–JSR.11 report these. The five
rosters of JSR.2 total **1,439 organisations** (89 + 190 + 215 + 383 + 562).

---

## JSR.1 — Design

Two arms, both run against the production code, the production prompt and the
production key. A study run any other way would not describe the tables it
claims to describe.

**Arm A — displacement against roster size.** Five rosters spanning 89 to 562
entities, four independent runs each, at the production temperature. Pairwise
comparison of runs within a roster: 6 pairs per roster.

**Arm B — displacement against temperature.** One roster, three temperatures,
three runs each: 3 pairs per temperature.

Nothing varies within a pair except the sampling. Same model, same prompt, same
criteria, same roster file, same day.

### Measures

| Symbol | Definition |
|---|---|
| `d̄` | mean absolute rank displacement between two runs, over entities present in both |
| `d_max` | largest displacement observed in a pair |
| `d̄/n` | displacement as a fraction of roster size — the scale-free form |
| `ρ` | Spearman rank correlation between the two runs |
| `\|ΔU\|` | mean absolute change in the score itself, on the 0–100 scale |

---

## JSR.2 — Results, Arm A

Four runs per roster, six pairwise comparisons each, temperature 2.0.

| Roster | n | d̄ places | d̄/n | d_max | ρ | mean \|ΔU\| | score SD |
|---|---:|---:|---:|---:|---:|---:|---:|
| Universities (world) | 89 | 13.1 | 14.7% | 61 | 0.761 | 2.60 | 4.07 |
| Central banks | 190 | 6.9 | 3.7% | 68 | 0.981 | 1.30 | 9.64 |
| Countries | 215 | 10.6 | 4.9% | 97 | 0.971 | 5.13 | 12.12 |
| Airlines | 383 | 35.5 | 9.3% | 230 | 0.900 | 3.94 | 5.75 |
| Media outlets | 562 | 71.6 | 12.7% | 538 | 0.812 | 3.71 | 8.35 |

**JSR-1 is refuted by its own data.** The appendix was drafted expecting `d̄/n`
to be roughly constant, on the strength of two earlier observations that
happened to agree (municipalities 11.7%, universities 14.7%). Across five
rosters it is not: it ranges from 3.7% to 14.7%, and it does not follow n —
the smallest roster is the least stable of all.

What the displacement does follow:

| Predictor | vs `d̄` (places) | vs `d̄/n` |
|---|---:|---:|
| roster size n | **+0.941** | +0.203 |
| entities per U point | +0.886 | +0.349 |
| dispersion of scores (SD) | −0.144 | **−0.777** |

Two different quantities with two different drivers:

- **Absolute displacement** tracks roster size almost perfectly. A bigger table
  moves an entity more places, which is arithmetic rather than a finding.
- **Relative displacement** — the fraction of the table an entity swings
  across, which is what decides whether a rank means anything — tracks the
  *dispersion of the scores*, negatively and strongly. The more tightly the
  judge packs its scores, the more of the table gets reordered by sampling.

Countries have an SD of 12.1 and move 4.9% of the table. World universities
have an SD of 4.1 and move 14.7%. There are only 89 universities and 215
countries; size is not what separates them.

**Caveat, stated at the same volume as the finding.** Five rosters is five
points. A correlation of −0.777 on n = 5 is suggestive, not established. The
mechanism is plausible — compressed scores mean smaller gaps between neighbours,
and a fixed amount of sampling jitter therefore crosses more of them — but this
appendix does not have the sample size to claim it. Testing it properly needs
rosters chosen to vary dispersion while holding n fixed, which is a study this
one implies rather than performs.

---

## JSR.3 — Results, Arm B

One roster (central banks, n = 190), three runs per temperature.

| Temperature | d̄ places | d_max | ρ | mean \|ΔU\| |
|---|---:|---:|---:|---:|
| 0.2 | 4.9 | 39 | 0.987 | 0.75 |
| 1.0 | 8.2 | 58 | 0.974 | 1.32 |
| 2.0 | 7.8 | 68 | 0.976 | 1.30 |

**JSR-3 holds only at the bottom of the range.** Dropping from 1.0 to 0.2 cuts
displacement roughly in half and halves the score jitter with it. Between 1.0
and 2.0 there is no detectable difference: 8.2 against 7.8 places, ρ 0.974
against 0.976, on three pairs each. Whatever the production temperature of 2.0
costs in stability, it is not measurably worse than 1.0.

This matters for a decision the register has already taken. Temperature 2.0 was
chosen deliberately, to stop the judge from returning near-identical scores for
different institutions. Arm B says that choice is not paid for in stability
relative to 1.0 — but that a move to 0.2 would buy about half the noise back.
What it would cost in discrimination is not measured here, and JSR.5 §4 refuses
to treat the trade as settled.

---

## JSR.4 — What the numbers mean for a published rank

The practical output of this appendix is a per-table resolution limit. Two
entities are distinguishable only if the gap between them survives resampling;
below roughly twice the mean displacement, an ordering is sampling.

| Table | Ranks apart before a difference is reproducible | Read as |
|---|---:|---|
| Central banks | ~14 | rank is close to meaningful |
| Countries | ~21 | top and bottom quintiles separate |
| Universities | ~26 of 89 | only thirds separate |
| Airlines | ~71 | only thirds separate |
| Media outlets | ~143 of 562 | only quartiles separate |

So "third of 190 central banks" is a defensible statement. "Third of 562 media
outlets" is not: on this evidence the honest form is "in the top quarter".

The register currently publishes an integer rank in every table. That is more
precision than the judge supports in four of the five tables measured. The
correct fix is the one the certificates already gesture at — publish the band,
not the position — and the fix that would remove the need is JSR-4.

---

## JSR.5 — What this does not claim

Scope discipline, in the manner of `APPENDIX_RH`.

1. **It does not claim the scores are wrong.** Instability is not error. A judge
   can be unbiased and still imprecise; these measurements bound precision, not
   accuracy. Nothing here tests whether the ranking corresponds to institutional
   conduct in the world, and no experiment in this appendix could.

2. **It does not generalise beyond this judge.** One model family, one prompt,
   one criterion set. A different model may be steadier or worse; that is
   exactly the measurement the jury architecture would produce and this one
   cannot.

3. **It does not establish that temperature is the cause.** Arm B measures
   association between the sampling temperature and displacement. The production
   setting was chosen for a separate reason — to spread scores between similar
   entities — and this appendix does not evaluate whether that purpose is served.

4. **It does not license a lower temperature as a fix.** If a lower temperature
   reduces displacement while also compressing the score range, the ranking
   becomes stable and uninformative at once. That trade-off is not resolved
   here.

5. **It says nothing about the geometric mean.** A separate and unresolved
   result of the same register is that U = ∛(CODE × CREDO × RIGHTS) currently
   reorders nothing: zero of 215 countries and zero of 89 universities change
   rank under a plain arithmetic average, because the three axes move together.
   The non-compensatory property is therefore claimed and not demonstrated. That
   is a defect of the scoring, not of the sampling, and belongs to `APPENDIX_SSS`.

---

## JSR.6 — Five judges on one roster

The same frozen roster of 190 central banks was scored repeatedly by each of the
available models from one provider.

| Judge | Reproduces its own ordering to within |
|---|---:|
| best available model | **5.9 places** (mean displacement) |
| weakest model | **45.7 places** |

For comparison, the production judge measured 6.9 places at temperature 2.0
in JSR.2.

One further model returned nothing usable when asked for scores, and answered
40 of 51 when asked for a list instead. The output shape, not the model, was the
binding constraint. A factor of almost eight separates the best and the worst
judge on identical input. The choice of judge is therefore a larger source of
variance than the sampling temperature studied in JSR.3.

*Source:* `APPENDIX_TEF` §18.3; the per-model runs are held with the register.

---

## JSR.7 — A five-model jury

`APPENDIX_SSS` assumes that a jury beats a judge. The register tested the
assumption with five models from one provider, scored independently and
aggregated.

| Comparison | Result |
|---|---|
| jury against the **average** single judge | displacement **31% lower** on one roster, **9% lower** on another |
| jury against the **best** single judge | **three times worse** |

The prior written before the run was that the jury would win. It did not: a
jury of weaker judges from one lineage averaged their noise but also diluted the
best judge. This is published because it contradicts the prior.

**Reading.** Aggregation helps only when the judges are both competent and
independent. Five models from one provider are neither guaranteed to be, which
is the question JSR.9 takes up.

*Source:* `APPENDIX_TEF` §18.6.

---

## JSR.8 — Names against text (TEF-3)

Until August every score was the judge's own knowledge of an entity under its
name; the judge was given a list of names and nothing else. A controlled run on
9 August 2026 scored the same entities twice: once from the name, once with the
entity's own text supplied.

| Corpus | Mean score change, name → text |
|---|---:|
| theories certainly present in training data | **+5.9 points** |
| a corpus that is not in training data | **+14.4 points** |
| difference attributable to the object being unknown, not to the prompt | **8.4 points** (as reported from the run; the rounded figures above give 8.5) |

Supplying text raises scores for everything, which is the prompt effect. It
raises them more than twice as much for work the model has not read, which is
the knowledge effect. A name-only register therefore scores the familiar higher
than the unfamiliar for reasons unrelated to the criteria. The fix is to supply
text, and it roughly triples input tokens.

*Source:* the run of 9 August 2026, reported in the project's funding
applications of 9–10 August; the raw runs are held with the register and are
not yet in the deposit.

---

## JSR.9 — Four training families (JSR-4 at pilot scale)

JSR-4 was the open falsifier of version 1.0: no second family had been run. On
9 August 2026 the same **38 objects** were scored **twice** by each of **four
training families**: Cohere command-a, Meta llama-3.3-70b, OpenAI gpt-oss-120b
and Alibaba qwen3.6. Each family was first measured against itself, so that the
distance between families could be read against a floor.

| Quantity | Points |
|---|---:|
| within-family disagreement (range over the four families) | 0.29 – 11.12 |
| within-family disagreement (mean) | **4.64** |
| between-family disagreement (mean of the six pairs) | **19.57** |
| ratio between : within | **4.22** |

Every one of the six between-family pairs cleared every family's own noise
floor.

**Reading.** Judges from one lineage agree with each other more than with anyone
outside it, and the gap is four times larger than their own instability. A jury
drawn from one provider (JSR.7) therefore measures shared ancestry as much as it
measures the entities. Agreement inside a family is not evidence of
correctness.

**What it does not show.** Thirty-eight objects is a pilot, not a roster. It
shows that families disagree beyond their noise; it does not show which family
is right, and it does not yet test JSR-4's actual claim, that aggregating
independent judges lowers displacement at roster scale. The pilot ran on free
tiers; the register cannot, because the nightly tables need about 802 calls per
judge per day against a free ceiling of 1,000, and free tiers rate-limit
silently.

*Source:* run of 9 August 2026, reported in the project's application of
10 August; raw runs held with the register.

---

## JSR.10 — A judge that returns a constant

The register later ran a four-agent panel: three small "specialist" models, one
per pillar, answering yes or no per criterion. Two failures are recorded.

1. **A specialist against itself.** On identical input at the production
   temperature 2.0, one specialist agreed with itself at **Cohen's κ = +0.006**:
   no better than chance. At temperature 0.3 it returned the same answer, all
   yes, for every country (entropy 0.000). Free models from other families gave
   the mirror constant, all no.
2. **A scorer that read the wrong input.** For two days in August the scoring
   agent was shown the specialists' answers and told in words not to use them.
   It used them: on the 166-party table the correlation between the number of
   "yes" answers on an axis and the score of that axis was **r = +0.931**, about
   4.2 points per yes. The artefact was visible in the published table, three
   adjacent countries in one alphabet tied at the top, before it was measured.
   The scorer was blinded on 11 August.

**Reading.** An instruction not to use an input is not a control on that input;
only withholding it is. And a judge can be perfectly stable and carry no
information: stability is necessary for a measurement, not sufficient.

*Source:* `APPENDIX_TEF` §18.3; register logs of 9–12 August 2026.

---

## JSR.11 — A typed second judge (THE HAND OF GOD)

`THE HAND OF GOD` (appendix HOG; the title is a brand name with no religious
meaning) adds a judge of a different kind: TypeSafe's Jev, a typed model that
does not write text. It returns a probability for a claim (Noul), a probability
distribution over declared options (Choice) or a position on anchored levels
(Score). HOG answers the problems of this appendix in four ways.

1. **Noise is measured per packet, then used.** Jev's own spread between
   identical calls was measured: up to **0.10** on a claim and up to **0.20** on
   the leading option of a choice (HOG.4). Differences inside that spread are
   read as ties, not as rankings. This is the JSR law applied to a single
   answer.
2. **Framing is varied on purpose.** Every question is asked from six angles:
   plain, reordered, facts only, sceptic, advocate and with option names hidden.
   An answer is reported as **robust** only when at least 80% of the angles
   agree, by a margin above the measured noise.
3. **Evidence is removed on purpose.** The strongest fact is withheld, or one
   assumption is changed, and the answer is asked again. An answer that flips
   is reported as depending on that fact.
4. **Every judgement is timestamped.** OpenTimestamps, anchored in Bitcoin, so
   that neither the judged nor the judge can rewrite a ranking afterwards (law
   HOG-7). Only hashes leave the machine.

**A worked example.** HOG Assessment Record No. 1 built a definition of personal
happiness from **222** typed judgements in five rounds. Two of its three lines
were chosen robustly (0.79 and 0.83, six of six angles, in every scenario); the
third was only prevailing (0.46). The record publishes what it does not show:
the judge did not confirm that the definition is complete. Every packet, raw
answer and result is public:
https://github.com/UniversalModel/core/tree/main/HOG/records/01_personal_happiness

**What it does not show.** Jev is a second family, but one judge. Its
probabilities are not calibrated against recorded outcomes yet, and agreement
across its six angles is agreement of one model with itself under different
framings, not independent confirmation. HOG makes instability visible and
bounded; it does not remove the need for JSR-4 at roster scale.

---

## JSR.11A — Self-application

The register scores the theory of the person who built it. U-Theory ranks
**55th of 5,476** theories and patents under its own criteria, with a median of
932 across its 33 records. Both figures are published, and the falsifier that
requires self-application is the first row of the public table.

---

## JSR.12 — Falsifiability matrix

| Code | Claim | Falsifier | Status |
|---|---|---|---|
| **JSR-1** | Rank displacement between identical runs is a roughly constant *fraction* of roster size | Measure rosters spanning a wide range of n; if `d̄/n` varies rather than scattering about a constant, JSR-1 fails | **FALSIFIED.** `d̄/n` ranges 3.7%–14.7% across n = 89…562 and does not follow n. JSR.2 |
| **JSR-1b** | Relative displacement is governed by the dispersion of the scores, not by roster size | Hold n fixed and vary score dispersion; if displacement does not fall as dispersion rises, JSR-1b fails | **SUGGESTED, NOT ESTABLISHED.** r = −0.777 on five rosters. The controlled version has not been run |
| **JSR-2** | A rank reported as a point overstates the resolution of a single-judge U-Score | Show a roster where `d̄` is small enough that adjacent ranks are reproducible across runs | **SUPPORTED.** Four of five tables cannot reproduce an integer rank. JSR.4 |
| **JSR-3** | Displacement falls as sampling temperature falls | Run Arm B; if displacement is flat as temperature falls, JSR-3 fails | **PARTLY SUPPORTED.** Halves from 1.0 to 0.2; flat between 1.0 and 2.0. JSR.3 |
| **JSR-4** | Aggregating independent judges reduces displacement below the single-judge floor | Run the same rosters with a jury of ≥3 models from different families and compare `d̄` against the figures here | **OPEN AT ROSTER SCALE.** A single-provider jury of five lost three times to the best single judge (JSR.7). Four families were compared at pilot scale (JSR.9), which tests independence, not aggregation. The roster-scale run is not funded |
| **JSR-5** | The instability is sampling, not roster drift | Hold the roster file fixed and vary only the run; if displacement vanishes, the cause was the roster | **Controlled by design:** every pair uses one frozen roster file |
| **JSR-6** | Judges from different training families disagree by more than each family's own noise | Score one frozen set twice per family; if any between-family distance falls inside a family's own floor, JSR-6 fails | **SUPPORTED AT PILOT SCALE.** Ratio 4.22; all six pairs clear every floor; n = 38 objects. JSR.9 |
| **JSR-7** | A jury of five models from one provider beats its best member | Compare the jury's displacement with each member's | **FALSIFIED.** It beat the average member by 31% (9% on a second roster) and lost to the best member threefold. JSR.7 |
| **JSR-8** | Name-only scoring is neutral between familiar and unfamiliar entities (TEF-3) | Score the same entities from names and from supplied text; compare the change for familiar and unfamiliar corpora | **FALSIFIED.** +5.9 points for familiar, +14.4 for unfamiliar; 8.4 points attributable to the object being unknown. JSR.8 |
| **JSR-9** | A stable judge is an informative judge | Measure a judge's agreement with itself and the information in its answers | **FALSIFIED.** A specialist at κ = +0.006 with itself at T = 2.0 returned a constant at T = 0.3. JSR.10 |

**JSR-4 is still the point of the appendix.** Its pilot (JSR.9) showed that the
families it needs genuinely disagree, which is why it matters. Running it at
roster scale requires the compute of several families. Every other claim here
describes a limitation; JSR-4 is the test that would remove it.

---

## JSR.13 — Relation to other appendices

| Appendix | Relation |
|---|---|
| `APPENDIX_SSS` | Specifies the jury (Stage 2: up to 50 models, IQR filtering, published consensus). JSR measures the cost of not having it |
| `APPENDIX_TAA` | Specifies the agent roles, including the Generalizing agent (Σ) that would perform the aggregation JSR-4 requires |
| `APPENDIX_GSI-RTD` | "The orchestrator is a triadic aggregator" — the architectural statement that JSR-4 would test empirically |
| `APPENDIX_RH` | Source of the scope-discipline form used in JSR.5 |
| `APPENDIX_TEF` | Theory evaluation framework; JSR is an instance of a declared falsifier being run rather than argued. TEF §18.3–18.6 are the source of JSR.6, JSR.7 and JSR.10 |
| `THE HAND OF GOD` (HOG) | A typed second judge whose noise is measured per packet, whose framing and evidence are varied on purpose, and whose every judgement is timestamped. JSR.11 |
| `APPENDIX_LGP` | Every pillar reading of LGP-3 and LGP-10 inherits the noise of the judge that made it; a pillar change inside the judge's band is not a change (JSR law) |
| `APPENDIX_POS` | A rank or score inside its noise band is not evidence of readiness; it cannot open the commitment gate |
| `APPENDIX_GEN_LMP1` (v1.3.1) | The P-LMP-5 register test reads sustained U on the band, never on the integer rank (its §12.10 cites JSR.4) |
| `APPENDIX_MASTER_INTEGRATION_MAP` | Registers JSR in Ring D (meta / evaluation), with cross-links and reading order |

---

> **JSR law.** *A rank is publishable only at the resolution its judge can
> reproduce. Below that resolution the ordering is sampling, not measurement.*

---

## JSR.14 — Reproduction

The raw per-run scores are deposited, not just the statistics, so the tables
above can be recomputed independently:

- `noise_study/summary.json` — computed statistics
- `noise_study/<roster>_T<temp>_run<k>.json` — every run, entity → U

Harness: `noise_study.py`. It imports the production scorer rather than
reimplementing it, so a divergence between the study and the live register is
impossible by construction.

The measurements added in version 1.1 (JSR.6–JSR.10) were run on the register
itself in August 2026. Their summaries are published in `APPENDIX_TEF` §18 and
in the project's applications; their raw runs are held with the register and
are not yet part of this deposit. That is a gap in reproducibility, stated here
rather than left for a reader to find. HOG Record No. 1 (JSR.11) is fully
deposited: packets, raw answers and results.

Register: https://u-model.org · Method DOI: https://doi.org/10.17605/OSF.IO/74XGR

---

*Version history: v1.1 (2026-10-13) adds JSR.6–JSR.11A: five judges on one
roster, a five-model jury, names against text, four training families, a
constant judge, the typed second judge of HOG, and self-application; extends the
falsifiability matrix with JSR-6 to JSR-9; records the AIMOS 2026 acceptance.
v1.0 (2026-08-03) is frozen as `APPENDIX_JSR_JUDGE_STABILITY_UNDER_REPETITION v1.0.md`,
SHA-256 `d2735bdb…e327`.*

*Petar Nikolov · ORCID 0009-0001-8669-2276 · UMSG — Universal Model of
Sustainable Governance · 2026-08-03 · v1.1 2026-10-13*
