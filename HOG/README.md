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
| `THE HAND OF GOD.md` | `75974a76d565980d6990399af36e73c0e68342e78e91924c126688b56b4c8e3a` |
| `THE HAND OF GOD.md.pdf` | `234afbb2d6b87d730aa295b0317f2d1bfacdb3d0d2e8ccd9f18e33d446da0a97` |
| `hog_calibration_reference.py` | `9fe00c439305b3f11d8b94f8761ed48cbc7e8dfa2b26d4602274830a27a06fa4` |

These hashes were timestamped with OpenTimestamps on 2026-10-10; the proofs are kept by
the author.

## License and author

Text: CC BY 4.0 · Code: MIT.
Petar Nikolov · ORCID [0009-0001-8669-2276](https://orcid.org/0009-0001-8669-2276) ·
U-Theory: https://doi.org/10.17605/OSF.IO/74XGR
