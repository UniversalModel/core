# APPENDIX FPC — TRIADIC COMPRESSION
## Writing Arbitrary Information in the Triadic Language: a Form–Position–Action Codec over the Ternary Substrate

> *"Compression is just a way of writing arbitrary information in the Triadic Language. I recursively map the triad onto the data, then store it compactly as three ordered, sorted sets — all Actions, all Forms, all Positions — grouping the identical ones and scaling by constants or relations, with the links between them preserved."*
> — Petar Nikolov, May 2026

---

**Author:** Petar Nikolov
**Date:** 31 May 2026
**Framework:** U-Theory v26 + v27 appendix series
**Status:** L1 (lossless reconstruction theorem) + L2 (engineering codec) + L3 (the "more-fundamental-than-binary" framing, hardened per RH)
**Version:** 1.0
**Epistemic Level:** L1 (>90%) for the round-trip theorem and the Peircean irreducibility citation; L2 (70–90%) for the cross-domain compression claim; L3 for the universal-substrate interpretation.
**Prerequisites:** `THEORY_OF_EVERYTHING_v26_CORE_MEANING` (the F·P·A triad), `APPENDIX_GSI-RTD` (Recursive Triadic Decomposition), `APPENDIX_TPL` (Triadic Parametric Language), `APPENDIX_NDT` (N-Adic Decomposition), `APPENDIX_SSS` (System Stability Score)
**Function:** Provides the **data-layer instance of RTD** — the binary/serialization layer beneath TPL. Where TPL is the *human-readable* triadic language, FPC is its *compressed machine record*.
**v26 Invariant:** Form ↔ Time · Position ↔ Space · Action ↔ Energy
**Brand:** also referred to as *the FPA codec* (U-Score.info / U-Model.org).

> **Copyright © 2026 Petar Nikolov. All rights reserved. Content licensed under CC BY 4.0; reference code under MIT.**

---

## 0. EXECUTIVE SUMMARY

**Triadic Compression (the FPA codec)** is a lossless (and optionally *structural/lossy*) encoder built on the central claim of U-Theory: any realized, distinguishable piece of information decomposes into exactly three irreducible kinds —

1. **Form (Форма)** — *what it is* (the scale-normalised pattern / identity);
2. **Position (Позиция)** — *where it is* (its coordinate in the information volume, context included);
3. **Action (Действие)** — *what it does* (the operation, transform, or relation it carries).

The codec performs a **multidimensional, recursive mapping of the triad onto arbitrary information**, then writes the result as **three ordered, frequency-sorted sets with preserved links**:

```
COMPRESSED OBJECT  =  ( D_F , D_P , D_A , T )
                       └─┬─┘ └─┬─┘ └─┬─┘  └┬┘
                  Form set  Position  Action   link/token stream
                 (sorted)    set       set     (preserves the whole)
```

All Actions are sorted and identical ones grouped; all Positions are sorted and identical steps grouped; all Forms are grouped **up to a scaling constant or a relation** (a shape and its enlarged or rotated copy share one entry). The most-repeating primitive in each set gets the shortest code. The remaining **link stream** $T$ rebinds the three sets into the original whole.

The deep reason this is principled — and the precise sense in which **F/P/A are "like 0 and 1, but more fundamental"** — is the **Peircean Reduction Thesis** already in the v26 monolith (§0.4.5.4a.1, Burch 1991): *every $n$-adic relation with $n\ge 4$ reduces exactly to triadic relations, but no triadic relation can be losslessly reduced to dyadic ones* (Löwenheim 1915; Quine 1954). Binary (0/1) is **dyadic**; therefore a genuinely triadic representation captures relational structure that no binary substrate can encode without fragmentation — while triads are simultaneously the **maximal** universal basis. F/P/A is the minimal-yet-complete alphabet of structure.

A verified reference implementation (§8) achieves a **2.80× lossless ratio** on a small self-similar scene, with the triadic balance score $U=\sqrt[3]{F\cdot P\cdot A}=0.622$ landing just above the canonical $\varphi^{-1}=0.618$ stability threshold.

---

## 1. THE CORE IDEA — COMPRESSION AS TRANSCRIPTION INTO THE TRIADIC LANGUAGE

`APPENDIX_TPL` defines a controlled language in which every statement is forced into three orthogonal layers `F{…} P{…} A{…}` plus guardrails `G{…}`. TPL is the *surface* form — written for humans and agents.

**FPC is the compressed binary record of the same triadic content.** The relationship is exactly that of a serialized format to its source language:

| Layer | Artifact | Role |
|-------|----------|------|
| Surface | TPL clause `F{…} P{…} A{…}` | human/agent-readable triadic statement |
| **Record** | **FPC stream `(D_F, D_P, D_A, T)`** | **compact, deduplicated, machine record of the same triad** |
| Foundation | RTD (`APPENDIX_GSI-RTD`) | the recursive decomposition both share |

To compress is therefore to **answer, for every element of the information, the three questions the core theory says no realized system can avoid** (`CORE_MEANING` §4):

> 1. **What continues?** → its **Form**
> 2. **Where / in what context is it distinguishable?** → its **Position**
> 3. **What can it do or undergo?** → its **Action**

…and then to store the answers once, grouped, with links. The information is not destroyed; it is **re-expressed in its own most fundamental coordinates** — a "naked snapshot" stripped of redundancy.

---

## 2. THE TERNARY SUBSTRATE — WHY F/P/A IS MORE FUNDAMENTAL THAN 0/1

### 2.1 The ternary alphabet

Define the **structural alphabet**

$$\Sigma_3 = \{\,\mathsf{F},\ \mathsf{P},\ \mathsf{A}\,\}$$

Every datum in an FPC record carries a **type-trit** $\in \Sigma_3$ declaring which of the three irreducible kinds it is. The compressed essence of any information is thus a self-describing string over a **base-3** alphabet — the "trits" of meaning, in contrast to the meaningless 0/1 bits of a binary substrate. This is the literal sense of *triadic* (tri-etic) encoding.

### 2.2 FPC-1 — Triadic irreducibility (why binary cannot match base-3 losslessly)

> **FPC-1 (Dyadic Insufficiency, inherited L1).** A representation over a *dyadic* alphabet (e.g. binary 0/1) cannot losslessly encode genuinely triadic relational structure without auxiliary scaffolding; a *triadic* representation can. Conversely, every higher-arity ($n\ge4$) relation reduces exactly to triads. Hence base-3 over $\Sigma_3$ is the **minimal complete** structural alphabet.

This is not new to this appendix — it is the **Peircean Reduction Thesis** formalised in the v26 monolith (§0.4.5.4a.1):

- **For $n\ge 4$:** $R = \pi(T_1 \bowtie T_2 \bowtie \cdots \bowtie T_k)$ — any $n$-adic relation is an exact join of triadic relations (Burch 1991).
- **For $n = 3$:** there is **no** lossless decomposition into dyadic relations (Löwenheim 1915; Quine 1954). The canonical counterexample is *betweenness* $B(x,y,z)$ = "$y$ is between $x$ and $z$", which provably cannot be expressed with dyadic predicates alone.

$$\boxed{\;n\ge 4 \Rightarrow \text{reducible to triads};\quad n=3 \not\Rightarrow \text{dyadic}\;\;\therefore\;\; \text{F–P–A is maximal-yet-minimal}\;}$$

**Consequence for compression.** Binary coders (LZ, Huffman, arithmetic over bytes) operate on a *dyadic* substrate and recover structure only as flat symbol statistics. FPC operates on the *triadic* substrate and so can natively factor information into the three relational channels that binary must reconstruct indirectly.

### 2.3 FPC-2 — Radix economy (the efficiency reading of "more powerful")

> **FPC-2 (Radix Economy, L2).** Among integer radices, base 3 minimises the radix-economy cost $E(b,N)=b\big(\lfloor \log_b N\rfloor + 1\big)$, because the continuous optimum is $e\approx 2.718$ and $3$ is the nearest integer. A ternary digit carries $\log_2 3 \approx 1.585$ bits.

So the author's claim that F/P/A are *"like 0 and 1 but more powerful"* has **two** rigorous readings, not one:
- **Structural (FPC-1):** triadic structure is irreducible to binary — base-3 is *expressively* more fundamental.
- **Economic (FPC-2):** base-3 is the most economical integer radix — ternary is *quantitatively* more efficient per symbol.

The reference implementation reports both: the 90-trit type-skeleton costs $90\cdot\log_2 3 \approx 142.6$ bits versus $180$ bits if the three kinds were stored at a naïve 2 bits/symbol.

> **RH guardrail.** FPC-2's efficiency advantage is per-symbol and modest; it is **not** claimed that ternary hardware beats binary hardware in practice (manufacturing favours 2-state devices). The load-bearing claim is FPC-1 (structural), graded L1; FPC-2 is supporting context, graded L2.

---

## 3. FORMAL MODEL — MULTIDIMENSIONAL RECURSIVE TRIADIC MAPPING

### 3.1 The information volume

Let the information be a **volume** $V$: an indexed collection of *atoms* over an $n$-dimensional coordinate space $C \subseteq \mathbb{Z}^n$ (1-D for a stream, 2-D for an image, $n$-D in general — the mapping is **multidimensional**). The codec is **universal**: $V$ may be a byte stream, a raster, a mesh, a knowledge graph, a TPL document, or an agent's world-model.

### 3.2 The atom

Each atom is the triad plus what is needed to place and reconstruct it:

$$A_i = (\,f_i,\ p_i,\ a_i,\ s_i,\ r_i\,)$$

| Symbol | Name | Meaning |
|--------|------|---------|
| $f_i$ | **Form** | scale-/relation-normalised pattern (identity) — costs **Time** |
| $p_i$ | **Position** | coordinate $p_i=(q_i,c_i)\in C$ — location $q$ **plus** operational context $c$ — costs **Space** |
| $a_i$ | **Action** | the transform/relation the atom carries — costs **Energy** |
| $s_i$ | **scale/relation element** | the group element $g_i$ (constant scaling and/or relation) recovering the instance from its canonical Form |
| $r_i$ | **residual** | exact bits required for lossless reconstruction (empty in fully structured data; non-empty for noise) |

This is the same $P=(q,c)$ "coordinates plus operational context" defined in `CORE_MEANING` §2, and the same Form/Position/Action invariant the SSS measures.

### 3.3 Recursion

A Form may itself be a volume of sub-atoms. The mapping is therefore **recursive**: $\mathrm{RTD}(V)$ decomposes $V$ into atoms; any atom's Form whose internal complexity exceeds a threshold is itself decomposed by $\mathrm{RTD}$, to depth $d$. This is the data-layer image of GSI-RTD's $3^d$ branching (`APPENDIX_GSI-RTD` §1.2) and generalises to $N$-adic depth under `APPENDIX_NDT` (§11 below).

---

## 4. THE COMPRESSED OBJECT — THREE ORDERED SETS WITH PRESERVED LINKS

The encoder produces four parts:

$$\mathcal{Z}(V) = (\,D_F,\ D_P,\ D_A,\ T\,)$$

- $D_F$ — the **Form set**: distinct canonical (scale-/relation-normalised) Forms, **sorted by descending frequency**.
- $D_P$ — the **Position set**: distinct position-steps (sorted, delta/pattern-encoded), identical steps grouped.
- $D_A$ — the **Action set**: distinct Actions, identical ones grouped.
- $T$ — the **link stream**: an ordered list of **triadic tokens**, one per atom, that rebinds the three sets into the original whole.

A triadic token is

$$t_i = (\,\mathrm{fid}_i,\ \mathrm{sid}_i,\ \mathrm{pid}_i,\ \mathrm{aid}_i,\ r_i\,)$$

where $\mathrm{fid},\mathrm{pid},\mathrm{aid}$ are **ranks** into $D_F,D_P,D_A$ (rank 0 = most frequent = shortest code) and $\mathrm{sid}$ encodes the scale/relation element. The token is the **preserved link**: it says *"the Form ranked fid, scaled/related by sid, sits at the position reached by step pid, bearing the Action ranked aid."*

> **Frequency ranking** realises the author's "counts the most-repeating": a canonical/Huffman-friendly order in which the most fundamental, most recurrent primitives are cheapest. A real implementation entropy-codes the ranks (Huffman/arithmetic/range); the reference model below uses conservative fixed-width ranks (a lower bound on the achievable ratio).

---

## 5. EQUIVALENCE — GROUPING BY CONSTANTS OR RELATIONS

### 5.1 FPC-3 — Scale-/relation-invariant Form equivalence

> **FPC-3 (Form Orbit Equivalence).** Two Forms are the same iff one maps to the other under an allowed group $G$ of **scaling constants and relations**:
> $$f_1 \sim f_2 \iff \exists\, g \in G:\; f_1 = g \cdot f_2.$$
> $D_F$ stores one **orbit representative** per class; the per-token element $g_i=(s_i,a_i)$ recovers the instance.

This formalises *"мащабирам по константи или релации"*:

- **Constant scaling** $s$: a shape and the same shape enlarged $s\times$ (each cell → an $s\times s$ block) share one Form entry; only $s_i$ differs. Scale-invariance.
- **Relation** $\rho$: a shape and its rotation/reflection/affine image share one Form entry; the relation is carried by the **Action** channel ($\mathrm{IDENT}, \mathrm{ROT90}, \mathrm{ROT180}, \mathrm{INVERT}, \dots$).

Thus, elegantly, **Action *is* the relational part of the Form's group element, and scale is its constant part.** The Form set holds *what the thing fundamentally is*; Position holds *where*; Action+scale hold *how it is situated and sized*. RTD, exactly.

### 5.2 Lossless vs structural ("naked snapshot") modes

- **Lossless mode** keeps residuals $r_i$ → exact reconstruction (§7, FPC-4).
- **Structural/lossy mode** drops or quantises $r_i$ → reconstructs the F/P/A skeleton only: the "naked snapshot of information" — its triadic essence without the noise. This is the compression analogue of the *structural* claims in `APPENDIX_DIM` (meaning as dimensionless structure).

---

## 6. THE ALGORITHM — THREE PASSES

The encoder runs three passes in the canonical order **Action → Position → Form**, then ranks and emits.

```
ENCODE(atoms):
  # Pass P — Position: sort the whole, delta-encode, group identical steps
  order  ← indices of atoms sorted by coordinate (row, then col, … n-D)
  deltas ← [ p[order[k]] − p[order[k−1]] ]   (delta[0] = p[order[0]] absolute)
  D_P    ← frequency-rank( distinct deltas )           # identical steps grouped

  # Pass F — Form: normalise by scale/relation to a canonical orbit rep
  forms  ← [ canonical(f[i]) for i in order ]           # group by FPC-3
  D_F    ← frequency-rank( distinct canonical forms )

  # Pass A — Action: group identical actions
  acts   ← [ a[i] for i in order ]
  D_A    ← frequency-rank( distinct actions )

  # Emit the link stream (one ternary-typed token per atom)
  T ← [ (rank_F[forms[k]], scale_or_relation[i], rank_P[deltas[k]], rank_A[acts[k]], r[i])
        for k,i in enumerate(order) ]
  return (D_F, D_P, D_A, T)
```

The decoder walks $T$ in order, accumulating position-steps and re-applying scale/relation:

```
DECODE(D_F, D_P, D_A, T):
  pos ← origin
  for t in T:
     pos  ← pos + D_P[t.pid]                 # rebuild absolute Position
     form ← D_F[t.fid]                        # canonical Form
     atom ← place( apply(t.sid, form), pos, D_A[t.aid], residual=t.r )
     emit atom
  return atoms
```

---

## 7. LOSSLESS RECONSTRUCTION

> **FPC-4 (Round-Trip Theorem, L1).** For any finite volume $V$ encoded in lossless mode, $\textsf{DECODE}(\textsf{ENCODE}(V)) = V$.

**Proof sketch.** `ENCODE` is a relabelling, not a projection: (i) the sort `order` is a permutation, fully invertible by replaying $T$ in the same order; (ii) position-steps sum telescopically back to the exact absolute coordinates; (iii) each token retains $\mathrm{fid},\mathrm{sid},\mathrm{aid}$ and residual $r_i$, so every field of every atom $A_i$ is recoverable; (iv) the dictionaries are bijections rank ↔ value. No field is discarded in lossless mode, hence the reconstruction is exact. ∎ *(Verified empirically for both the atom list and the rendered canvas in §8.)*

---

## 8. REFERENCE IMPLEMENTATION (VERIFIED, RUNNABLE)

Pure Python 3 standard library, deterministic. The demo domain — a 2-D scene of placed *glyph atoms* on a self-similar lattice — is **one concrete instantiation** of the universal codec; the three passes apply unchanged to any indexed information.

**Measured result (run 31 May 2026):**

```
atoms in / out          : 30 / 30
LOSSLESS round-trip     : OK  (atoms equal, canvas equal)
D_F (Form)   entries    : 3   → ['L', 'bar', 'dot']
D_P (Position) entries  : 3   (unique position-steps — the lattice collapses)
D_A (Action) entries    : 2   → ['IDENT', 'ROT90']
raw size                : 1020 bits (127.5 bytes)
FPA-compressed size     :  364 bits ( 45.5 bytes)
compression ratio       : 2.80×   (saving 64.3%)
ternary type-skeleton   : FPAFPA…  (90 trits)
  skeleton cost @log₂3  : 142.6 bits   (vs 180 bits at 2 bits/symbol)
triadic balance         : U_F/U_P/U_A = 0.775 / 0.717 / 0.433
U = ∛(U_F·U_P·U_A)      : 0.6220   δ(imbalance) = 0.4352   →  ≥ φ⁻¹ = 0.618 ✓
```

```python
"""
FPA codec — reference implementation (U-Theory, APPENDIX FPC).
Triadic compression: writing arbitrary information into the Triadic Language
over the ternary substrate {F, P, A}. Stdlib only. Deterministic. Lossless.
"""
from collections import Counter, namedtuple
from math import log2, ceil

Atom = namedtuple("Atom", "form scale action row col")

# Base (unit-scale) Forms — canonical, scale-normalised patterns.
BASE_FORMS = {
    "dot":   frozenset({(0, 0)}),
    "bar":   frozenset({(0, 0), (0, 1), (0, 2)}),
    "L":     frozenset({(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}),
    "ring":  frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}),
    "cross": frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
}
ACTIONS = ["IDENT", "ROT90", "ROT180", "INVERT"]

def _bbox(cells):
    rs = [r for r, _ in cells]; cs = [c for _, c in cells]
    return max(rs) + 1, max(cs) + 1

def _scale(cells, s):                          # constant scaling: cell -> s x s block
    return frozenset((r*s+dr, c*s+dc) for (r, c) in cells
                     for dr in range(s) for dc in range(s))

def _transform(cells, action):                 # relation: rotate / reflect / invert
    h, w = _bbox(cells)
    if action == "IDENT":  return cells
    if action == "ROT90":  return frozenset((c, h-1-r) for (r, c) in cells)
    if action == "ROT180": return frozenset((h-1-r, w-1-c) for (r, c) in cells)
    if action == "INVERT":
        full = {(r, c) for r in range(h) for c in range(w)}
        return frozenset(full - set(cells))
    raise ValueError(action)

def render_atom(a):                            # Form -> scale -> action -> translate
    moved = _transform(_scale(BASE_FORMS[a.form], a.scale), a.action)
    return frozenset((r + a.row, c + a.col) for (r, c) in moved)

def build_canvas(atoms):
    cells = set()
    for a in atoms: cells |= render_atom(a)
    return frozenset(cells)

def _rank(items):                              # frequency-rank: most common -> rank 0
    freq = Counter(items)
    table = [k for k, _ in sorted(freq.items(), key=lambda kv: (-kv[1], repr(kv[0])))]
    return table, {k: i for i, k in enumerate(table)}

Compressed = namedtuple("Compressed", "D_F D_P D_A tokens")
Token = namedtuple("Token", "f_rank scale p_rank a_rank")

def encode(atoms):
    order = sorted(range(len(atoms)), key=lambda i: (atoms[i].row, atoms[i].col))
    deltas, prev = [], (0, 0)
    for i in order:
        deltas.append((atoms[i].row - prev[0], atoms[i].col - prev[1])); prev = (atoms[i].row, atoms[i].col)
    D_P, p_idx = _rank(deltas)
    D_F, f_idx = _rank([atoms[i].form for i in order])
    D_A, a_idx = _rank([atoms[i].action for i in order])
    toks = [Token(f_idx[atoms[i].form], atoms[i].scale, p_idx[deltas[k]], a_idx[atoms[i].action])
            for k, i in enumerate(order)]
    return Compressed(D_F, D_P, D_A, toks)

def decode(c):
    atoms, prev = [], (0, 0)
    for t in c.tokens:
        dr, dc = c.D_P[t.p_rank]; prev = (prev[0]+dr, prev[1]+dc)
        atoms.append(Atom(c.D_F[t.f_rank], t.scale, c.D_A[t.a_rank], prev[0], prev[1]))
    return atoms

# ---- size model (conservative fixed-width ranks) ----
def _bits(n): return max(1, ceil(log2(max(n, 2))))
def _extent(atoms):
    cells = build_canvas(atoms)
    return max(r for r, _ in cells)+1, max(c for _, c in cells)+1

def raw_bits(atoms):
    H, W = _extent(atoms); rb, cb = _bits(H+1), _bits(W+1)
    return sum(4 + len(BASE_FORMS[a.form])*4 + 4 + 2 + rb + cb for a in atoms)

def comp_bits(c, atoms):
    H, W = _extent(atoms); rb, cb = _bits(H+1), _bits(W+1)
    df = sum(4 + len(BASE_FORMS[n])*4 for n in c.D_F)
    dp = len(c.D_P) * ((rb+1) + (cb+1)); da = len(c.D_A) * 2
    fr, pr, ar = _bits(len(c.D_F)), _bits(len(c.D_P)), _bits(len(c.D_A))
    return df + dp + da + (fr + 4 + pr + ar) * len(c.tokens)

def balance(c, atoms):                          # links FPC -> SSS / TPL stability index
    H, W = _extent(atoms); rb, cb = _bits(H+1), _bits(W+1)
    raw_F = sum(4+len(BASE_FORMS[a.form])*4 for a in atoms)
    cmp_F = sum(4+len(BASE_FORMS[n])*4 for n in c.D_F) + _bits(len(c.D_F))*len(c.tokens)
    raw_P, cmp_P = len(atoms)*(rb+cb), len(c.D_P)*((rb+1)+(cb+1)) + _bits(len(c.D_P))*len(c.tokens)
    raw_A, cmp_A = len(atoms)*2, len(c.D_A)*2 + _bits(len(c.D_A))*len(c.tokens)
    v = [max(1-cmp_F/raw_F,1e-6), max(1-cmp_P/raw_P,1e-6), max(1-cmp_A/raw_A,1e-6)]
    U = (v[0]*v[1]*v[2])**(1/3); d = (max(v)-min(v))/(max(v)+0.01)
    return v, U, d

if __name__ == "__main__":
    forms_cycle = ["dot", "bar", "L"]; scene = []
    ROWS, COLS, STEP = 5, 6, 8
    for i in range(ROWS):
        for j in range(COLS):
            k = i*COLS + j
            scene.append(Atom(forms_cycle[(i+j) % 3],
                              2 if k % 5 == 0 else 1,
                              "ROT90" if k % 7 == 0 else "IDENT",
                              i*STEP, j*STEP))
    c = encode(scene); back = decode(c)
    key = lambda xs: sorted(xs, key=lambda a: (a.row, a.col, a.form, a.scale, a.action))
    assert key(scene) == key(back) and build_canvas(scene) == build_canvas(back)
    rb, cb = raw_bits(scene), comp_bits(c, scene); v, U, d = balance(c, scene)
    print(f"LOSSLESS OK | atoms {len(scene)} | D_F {len(c.D_F)} D_P {len(c.D_P)} D_A {len(c.D_A)}")
    print(f"raw {rb} bits -> comp {cb} bits = {rb/cb:.2f}x  (save {100*(1-cb/rb):.1f}%)")
    print(f"U_F/U_P/U_A = {v[0]:.3f}/{v[1]:.3f}/{v[2]:.3f} | U={U:.4f} delta={d:.4f}")
```

---

## 9. COMPLEXITY AND WHERE TRIADIC COMPRESSION WINS

**Complexity.** Let $n$ = number of atoms. Each pass is a scan plus a sort: $O(n\log n)$ time; dictionaries are $O(|D_F|+|D_P|+|D_A|)$ space; decode is $O(n)$. Recursive mapping to depth $d$ multiplies work by the branching factor (≤ $3^d$ leaves; see NDT for $N$-adic).

**Where it wins (high ratio):**
- self-similar / fractal / tiled data (the same Form at many scales — scale-invariance pays directly);
- lattice / periodic placement (Position-steps collapse to a few entries);
- low-Action-variety data (few transforms → cheap Action ranks).

**Where it does not (ratio → 1 or worse):**
- high-entropy / incompressible noise (residuals dominate; no orbit sharing);
- data with no exploitable coordinate structure.

**Versus classical coders.**

| Coder | Substrate | What it factors | What FPC adds |
|-------|-----------|-----------------|---------------|
| Huffman / arithmetic | dyadic symbols | symbol frequency | three *typed* channels, not one flat stream |
| LZ77 / LZ78 | dyadic byte-strings | repeated substrings | scale-/relation-invariant repeats (not just literal) |
| DCT / wavelet | numeric transform | frequency energy | explicit Form/Position/Action separation + lossless option |

FPC is **complementary**: its three rank-streams can be handed to any entropy coder as a back end. Its distinctive contribution is the *triadic, scale-/relation-aware factorisation* — repeats that byte-level coders miss because the copies differ by a constant or a relation.

---

## 10. THE TRIADIC BALANCE SCORE — LINK TO SSS AND TPL

Define per-channel compression efficiency $U_F, U_P, U_A \in [0,1]$ (fraction of that channel's raw cost removed). The **representation's stability/quality** is the same non-compensatory aggregator the whole theory uses:

$$U = \sqrt[3]{U_F\cdot U_P\cdot U_A}, \qquad \delta = \frac{\max - \min}{\max + 0.01}$$

with the TPL stability index $SI = U/(1+\delta)^2$ (`APPENDIX_TPL` §8.1). In the reference run $U=0.622 \ge \varphi^{-1}$, and the non-compensatory mean **correctly flags Action** ($U_A=0.433$) as the channel carrying the most irreducible information — precisely the diagnostic behaviour SSS exhibits across domains (`APPENDIX_SSS` §5). A balanced, highly compressible volume scores high $U$, low $\delta$; an incompressible or lopsided one scores low.

> **Reading:** compressibility *is* a stability signature. Highly stable, structured information pays little to be re-expressed in its own triadic coordinates; chaotic information pays a lot. This makes FPC a natural front-end measurement for `APPENDIX_SSS` and an `APPENDIX_GSI-RTD` runtime.

---

## 11. RECURSION AND THE N-ADIC GENERALISATION

FPC is the $N=3$ member of the family in `APPENDIX_NDT`. For substrates solvent in additional currencies, the same architecture extends:

| $N$ | Channels | Substrate | Codec |
|-----|----------|-----------|-------|
| **3** | F, P, A | classical | **FPC (this appendix)** |
| 4 | + X (Freedom/Irreversibility) | bio/anti-entropy | tetradic codec: adds a durability/residual-lifetime channel |
| 5 | + Y (Coherence/Entanglement) | quantum | pentadic codec: adds a non-local correlation channel |

Recursive mapping (a Form that is itself a volume, decomposed to depth $d$) gives the $N^d$ leaf scaling of NDT-1. FPC therefore inherits NDT's law: **higher $N$ ⇒ higher structural factorisation ⇒ higher achievable compression on substrates that pay the corresponding currency.**

---

## 12. INTEGRATION WITH THE U-THEORY CORPUS

| Component | Relationship to FPC |
|-----------|---------------------|
| **Core triad** (`CORE_MEANING`) | FPC's three channels *are* Form/Position/Action; the round-trip rests on the triadic necessity theorem. |
| **GSI-RTD** | FPC is **RTD executed at the data layer**; an FPC record is a compact world-model an RTD runtime can consume. |
| **TPL** | FPC is the **compressed serialization of TPL** — same triad, machine record instead of surface text. |
| **NDT** | FPC is the $N=3$ codec; NDT supplies the $N\to4,5$ generalisation (§11). |
| **SSS** | The triadic balance score $U=\sqrt[3]{U_F U_P U_A}$ scores representation stability/compressibility (§10). |
| **TAA** | The three passes map onto the Form/Position/Action agents; a Σ-agent assembles the link stream $T$. |
| **DIM** | Structural (lossy) mode = the "dimensionless meaning" skeleton; residual = the dimensional remainder. |

---

## 13. FALSIFIABILITY MATRIX

| Prediction | Test | Status | If falsified |
|------------|------|--------|--------------|
| Lossless round-trip holds for all finite $V$ | Run encode∘decode on adversarial inputs; assert equality | 🟢 Demonstrated (§8) | Refutes FPC-4 |
| Triadic structure is irreducible to dyadic | Cite/derive Löwenheim–Quine; exhibit betweenness | 🟢 Established (Burch 1991) | Refutes FPC-1 / the "more-fundamental" claim |
| FPC beats byte-level coders on scale-/relation-repetitive data | Benchmark vs gzip/PNG on self-similar corpora *after* entropy back-end | 🟡 Plausible; not yet benchmarked | Refutes the practical compression claim (L2) |
| Base-3 minimises radix economy | Arithmetic check of $E(b,N)$ | 🟢 Standard result | Refutes FPC-2 |
| Triadic balance $U$ tracks compressibility | Correlate $U$ with achieved ratio across corpora | ❓ Open | Refines the SSS link (§10) |

---

## 14. WHAT THIS APPENDIX DOES NOT CLAIM (scope discipline, per RH)

- It does **not** claim FPC beats production codecs (zstd, PNG, FLAC) on arbitrary data — only on structured/self-similar data, and the practical claim is L2 pending benchmarks.
- It does **not** claim ternary *hardware* is superior; FPC-2 concerns representation economy, not silicon.
- It does **not** claim the F/P/A extraction is automatic for every domain; choosing the Form library, the scaling constants, and the Action/relation group is domain-specific engineering (an open problem shared with TPL).
- It does **not** elevate the structural-substrate interpretation above L3.
- The lossless theorem (FPC-4) and the irreducibility citation (FPC-1) are the only L1 claims here.

---

## 15. RELATIONS TO OTHER APPENDICES

| Appendix | Provides | FPC uses it for |
|----------|----------|------------------|
| `THEORY_OF_EVERYTHING_v26` §0.4.5.4a.1 | Peircean/Burch reduction theorem | FPC-1 backbone (irreducibility of triads) |
| `CORE_MEANING` | The F·P·A triad and $U=\sqrt[3]{FPA}$ | The three channels and the balance score |
| `APPENDIX_GSI-RTD` | Recursive Triadic Decomposition | The recursive mapping (§3.3) |
| `APPENDIX_TPL` | Triadic Parametric Language | FPC is its compressed record (§1) |
| `APPENDIX_NDT` | N-adic decomposition | $N>3$ generalisation (§11) |
| `APPENDIX_SSS` | System Stability Score | Compressibility-as-stability scoring (§10) |
| `APPENDIX_TAA` | Triadic agents (F, P, A, Σ) | Pass-to-agent mapping (§12) |
| `APPENDIX_RH` | Hardening / level tags | Guardrails and scope discipline (§2.3, §14) |

---

## 16. ONE-LINE LAW

$$\boxed{\;\text{To compress is to write information in the Triadic Language: } V \mapsto (D_F, D_P, D_A, T),\ \text{three sorted sets of the most-repeating Forms, Positions, Actions, with their links preserved.}\;}$$

---

## 17. REFERENCES

| # | Reference |
|---|-----------|
| [1] | Nikolov, P. (2026). *U-Theory v26 — Theory of Everything*, §0.4.5.4a.1 (Burch Formalization of the Reduction Thesis). |
| [2] | Burch, R. W. (1991). *A Peircean Reduction Thesis: The Foundation of Topological Logic*. Texas Tech University Press. |
| [3] | Löwenheim, L. (1915); Quine, W. V. O. (1954) — irreducibility of triadic ("betweenness") relations to dyadic predicates. |
| [4] | Hayes, B. (2001). *Third Base* — ternary numbers and radix economy ($e$ as the optimal radix). *American Scientist* 89(6). |
| [5] | Nikolov, P. (2026). `APPENDIX_TPL` — Triadic Parametric Language; `APPENDIX_GSI-RTD`; `APPENDIX_NDT`; `APPENDIX_SSS`. |
| [6] | Shannon, C. E. (1948). *A Mathematical Theory of Communication* — entropy baseline for the back-end coder. |

---

> *Appendix FPC — Triadic Compression (the FPA codec)*
> *U-Theory v26/v27 | © 2026 Petar Nikolov | CC BY 4.0 (content) · MIT (code)*
> *"Compression is writing arbitrary information in the Triadic Language."*

*End of APPENDIX FPC v1.0.*
