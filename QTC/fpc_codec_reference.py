from collections import Counter, namedtuple
from math import log2, ceil

Atom = namedtuple("Atom", "form scale action row col")

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

def _scale(cells, s):
    return frozenset((r*s+dr, c*s+dc) for (r, c) in cells
                     for dr in range(s) for dc in range(s))

def _transform(cells, action):
    h, w = _bbox(cells)
    if action == "IDENT":  return cells
    if action == "ROT90":  return frozenset((c, h-1-r) for (r, c) in cells)
    if action == "ROT180": return frozenset((h-1-r, w-1-c) for (r, c) in cells)
    if action == "INVERT":
        full = {(r, c) for r in range(h) for c in range(w)}
        return frozenset(full - set(cells))
    raise ValueError(action)

def render_atom(a):
    moved = _transform(_scale(BASE_FORMS[a.form], a.scale), a.action)
    return frozenset((r + a.row, c + a.col) for (r, c) in moved)

def build_canvas(atoms):
    cells = set()
    for a in atoms: cells |= render_atom(a)
    return frozenset(cells)

def _rank(items):
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

def balance(c, atoms):
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
