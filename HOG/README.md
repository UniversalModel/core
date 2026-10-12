# THE HAND OF GOD — Appendix HOG

**Jev as the typed decision hand of the Lady Galaxy Protocol** (U-Theory / U-Model).

This appendix defines how a typed probabilistic judge (TypeSafe Jev) is attached to the
Lady Galaxy Protocol: where it is called, what it is asked, how its answers are read, when
its probabilities may be corrected, how it is kept from the Forbidden Action, and where it
must not be used.

| File | What it is |
|---|---|
| `THE HAND OF GOD.md` | The appendix (source) |
| `THE HAND OF GOD.md.pdf` | The same appendix as an A4 PDF |
| `hog_calibration_reference.py` | Reference code for section HOG.6: isotonic regression (PAVA with tie pooling), Platt scaling, Brier score, ECE, out-of-fold evaluation and the calibration gate. numpy only |
| `THE_HAND_OF_GOD_*.jpg`, `THE_HAND_OF_GOD_ma_musk.png` | Images used by the appendix |

## Reproduce

```bash
pip install numpy
python hog_calibration_reference.py
```

This runs tests T1–T4, the synthetic comparison and the fresh-data gate check reported
in HOG.6.4. Seeds are fixed; the output matches the tables in the appendix.

## Status

L1 — operational. Every number in the appendix is marked *measured*, *synthetic* or
*specified*. No outcome of a Jev judgment has been recorded yet, so Jev's probabilities
are **uncalibrated** for this workflow (HOG.6.1). The falsifiers are listed in HOG.10.

## Integrity

| File | SHA-256 |
|---|---|
| `THE HAND OF GOD.md` | `d0003dacd1af44c5409b5834ca460c17b458ba118726fec4029890cb8ece955c` |
| `THE HAND OF GOD.md.pdf` | `bdd813b5ccac8d41574a0cf7fb8b9d76b19e04e9e864d00d802ef9462b07dbd3` |
| `hog_calibration_reference.py` | `9fe00c439305b3f11d8b94f8761ed48cbc7e8dfa2b26d4602274830a27a06fa4` |

These hashes (version 1.2) were timestamped with OpenTimestamps on 2026-10-10; the proofs
are kept by the author. Version 1.0 is in this repository's history (commit `fbc0f453`);
its md and pdf hashes were `75974a76…8e3a` and `234afbb2…0a97`, also timestamped.

Version 1.2 states that the title is a marketing name with no religious meaning.
Version 1.1 (commit `00054508`, md `abda801b…298e`, pdf `ba206565…f038`) added HOG.7.5: every Jev opinion and every project milestone receives an
OpenTimestamps proof, so the decision record cannot be rewritten afterwards.

## License and author

Text: CC BY 4.0 · Code: MIT.
Petar Nikolov · ORCID [0009-0001-8669-2276](https://orcid.org/0009-0001-8669-2276) ·
U-Theory: https://doi.org/10.17605/OSF.IO/74XGR
