# APPENDIX JSR — JUDGE STABILITY UNDER REPETITION

## The noise floor of an LLM judge applied to normative criteria at scale

> *"A ranking that hides its own noise is not a measurement."*

| | |
|---|---|
| **Author** | Petar Nikolov |
| **Date** | 2026-08-03 |
| **Framework** | U-Theory / U-Model · UMSG |
| **Status** | Empirical, measured on the live register |
| **Version** | 1.0 |
| **Epistemic Level** | **L1 — measured, not derived.** Every number here is an observation of a running system, reproducible from the deposited raw scores. No claim in this appendix follows from the triadic axioms; it constrains them. |
| **Prerequisites** | `APPENDIX_SSS` (the scoring engine), `APPENDIX_TAA` (the jury architecture this appendix argues is necessary) |
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

## JSR.6 — Falsifiability matrix

| Code | Claim | Falsifier | Status |
|---|---|---|---|
| **JSR-1** | Rank displacement between identical runs is a roughly constant *fraction* of roster size | Measure rosters spanning a wide range of n; if `d̄/n` varies rather than scattering about a constant, JSR-1 fails | **FALSIFIED.** `d̄/n` ranges 3.7%–14.7% across n = 89…562 and does not follow n. JSR.2 |
| **JSR-1b** | Relative displacement is governed by the dispersion of the scores, not by roster size | Hold n fixed and vary score dispersion; if displacement does not fall as dispersion rises, JSR-1b fails | **SUGGESTED, NOT ESTABLISHED.** r = −0.777 on five rosters. The controlled version has not been run |
| **JSR-2** | A rank reported as a point overstates the resolution of a single-judge U-Score | Show a roster where `d̄` is small enough that adjacent ranks are reproducible across runs | **SUPPORTED.** Four of five tables cannot reproduce an integer rank. JSR.4 |
| **JSR-3** | Displacement falls as sampling temperature falls | Run Arm B; if displacement is flat as temperature falls, JSR-3 fails | **PARTLY SUPPORTED.** Halves from 1.0 to 0.2; flat between 1.0 and 2.0. JSR.3 |
| **JSR-4** | Aggregating independent judges reduces displacement below the single-judge floor | Run the same rosters with a jury of ≥3 models from different families and compare `d̄` against the figures here | **NOT TESTED — no second judge is funded.** This is the declared open falsifier of this appendix |
| **JSR-5** | The instability is sampling, not roster drift | Hold the roster file fixed and vary only the run; if displacement vanishes, the cause was the roster | **Controlled by design:** every pair uses one frozen roster file |

**JSR-4 is the point of the appendix.** It is written, it is runnable, and it has
not been run, because running it requires a second model's compute. Every other
claim here is a description of a limitation; JSR-4 is the test that would remove
it.

---

## JSR.7 — Relation to other appendices

| Appendix | Relation |
|---|---|
| `APPENDIX_SSS` | Specifies the jury (Stage 2: up to 50 models, IQR filtering, published consensus). JSR measures the cost of not having it |
| `APPENDIX_TAA` | Specifies the agent roles, including the Generalizing agent (Σ) that would perform the aggregation JSR-4 requires |
| `APPENDIX_GSI-RTD` | "The orchestrator is a triadic aggregator" — the architectural statement that JSR-4 would test empirically |
| `APPENDIX_RH` | Source of the scope-discipline form used in JSR.5 |
| `APPENDIX_TEF` | Theory evaluation framework; JSR is an instance of a declared falsifier being run rather than argued |

---

> **JSR law.** *A rank is publishable only at the resolution its judge can
> reproduce. Below that resolution the ordering is sampling, not measurement.*

---

## JSR.8 — Reproduction

The raw per-run scores are deposited, not just the statistics, so the tables
above can be recomputed independently:

- `noise_study/summary.json` — computed statistics
- `noise_study/<roster>_T<temp>_run<k>.json` — every run, entity → U

Harness: `noise_study.py`. It imports the production scorer rather than
reimplementing it, so a divergence between the study and the live register is
impossible by construction.

Register: https://u-model.org · Method DOI: https://doi.org/10.17605/OSF.IO/74XGR

---

*Petar Nikolov · ORCID 0009-0001-8669-2276 · UMSG — Universal Model of
Sustainable Governance · 2026-08-03*
