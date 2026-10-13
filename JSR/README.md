# APPENDIX JSR — Judge Stability Under Repetition

**The noise floor of the LLM judges that score the U-Model register.** A ranking that hides its own noise is not a measurement, so the register measures how far its judges move when nothing in the question changes, and publishes the result.

The core measurement was **accepted after peer review** as a lightning talk at **AIMOS 2026** (Association for Interdisciplinary Metaresearch and Open Science, Wellington, 29 November – 2 December 2026): *"LLM-judge rank instability in a live public register: 1,439 organisations, two identical runs"*.

## Main results

| Section | Finding |
|---|---|
| JSR.2–JSR.4 | Across five rosters and 1,439 organisations, **four of five tables cannot reproduce an integer rank** between two identical runs. A published rank is a band, not a position |
| JSR.6 | On 190 central banks the best model reproduces its own ordering to within **5.9 places**, the weakest to **45.7** |
| JSR.7 | A five-model jury beat the average judge by 31% and **lost threefold to the best single judge**, contradicting the prior written before the run |
| JSR.8 | Supplying an entity's own text instead of its name raises scores **+5.9** points for familiar theories and **+14.4** for unfamiliar ones |
| JSR.9 | Four training families on 38 objects: disagreement between families is **4.22 times** each family's own noise (pilot scale) |
| JSR.10 | A judge can be stable and carry no information: κ = +0.006 with itself at T = 2.0, a constant at T = 0.3 |
| JSR.11 | **THE HAND OF GOD (HOG)**: a typed second judge whose noise is measured per packet, whose framing and evidence are varied on purpose, and whose every judgement is timestamped. Worked example: [HOG Record No. 1](../HOG/records/01_personal_happiness/) |

**JSR law.** *A rank is publishable only at the resolution its judge can reproduce. Below that resolution the ordering is sampling, not measurement.*

The appendix states its own limits: one provider in most measurements, a cross-family test at pilot scale only, and raw runs of the August measurements held with the register and not yet deposited. **JSR-4**, the test that aggregating independent judges lowers displacement at roster scale, remains open.

## Files

| File | SHA-256 |
|---|---|
| `APPENDIX_JSR_JUDGE_STABILITY_UNDER_REPETITION.md` (v1.1, canonical) | `7dc42817bb27b67641edea91766acf284baa0fab998855e93e50187749477d4b` |
| `APPENDIX_JSR_JUDGE_STABILITY_UNDER_REPETITION.md.pdf` (v1.1) | `2e807e510e52fe097485ba929ab12ad6eda66c12915d597e4885c289983c99ab` |
| `APPENDIX_JSR_JUDGE_STABILITY_UNDER_REPETITION v1.0.md` (2026-08-03, frozen) | `d2735bdb7e4bf1d8e4ed27d53cd94a1cb1ae865e5079d41ee5f08b345b1ae327` |

All three were timestamped with OpenTimestamps on 13 October 2026, anchored in Bitcoin. Proofs are in `time stamps/`:

```
ots verify "time stamps/APPENDIX_JSR_JUDGE_STABILITY_UNDER_REPETITION.md.ots"
```

## Links

- OSF (md): https://osf.io/74xgr/files/35fc2 · OSF (pdf): https://osf.io/74xgr/files/f2z7p
- U-Theory: https://doi.org/10.17605/OSF.IO/74XGR · Register: https://u-model.org
- HOG appendix: [../HOG](../HOG/)

Text: CC BY 4.0. Petar Nikolov · independent researcher, Sofia · ORCID 0009-0001-8669-2276
