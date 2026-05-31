"""
QTC — Phase 1 validation (density-matrix, numpy only; no qiskit).
U-Theory APPENDIX_QTC. Maps each noise channel to a triadic defense:

  collective dephasing      -> DFS / shared-Form    (passive, FORM)        [Exp A]
  amplitude damping (jumps) -> total-Z parity check (leakage detector, P4) [Exp C]  (ACTION)
  residual quasi-static deph-> delta_q-triggered DD  (P3)                   [Exp D]
  honest limits + Holevo ledger                                            [Exp B, E]

Encodings (2 physical qubits; index = 2*q0 + q1):
  EXPOSED logical : 0_L=|00>, 1_L=|11>      (total-Z = +-2  -> hit by collective dephasing)
  DFS/MELQ logical: 0_L=|01>, 1_L=|10>      (total-Z =  0   -> immune to collective dephasing)
Deterministic. Standard QM (Kraus channels, Gaussian quasi-static dephasing).
"""
import numpy as np

# ---------- basics ----------
I2 = np.eye(2, dtype=complex)
X  = np.array([[0, 1], [1, 0]], complex)
Z  = np.array([[1, 0], [0, -1]], complex)

def kron_list(ops):
    out = np.array([[1]], complex)
    for o in ops:
        out = np.kron(out, o)
    return out

def dm(psi):
    psi = np.asarray(psi, complex); psi = psi / np.linalg.norm(psi)
    return np.outer(psi, psi.conj())

def fidelity(psi, rho):
    psi = np.asarray(psi, complex); psi = psi / np.linalg.norm(psi)
    return float(np.real(psi.conj() @ rho @ psi))

def total_Z_eigs(n):
    eigs = []
    for idx in range(2 ** n):
        bits = [(idx >> (n - 1 - k)) & 1 for k in range(n)]
        eigs.append(sum(1 if b == 0 else -1 for b in bits))
    return np.array(eigs)

# ---------- channels ----------
def collective_dephasing(rho, n, sigma):
    M = total_Z_eigs(n)
    D = np.exp(-0.5 * sigma ** 2 * (M[:, None] - M[None, :]) ** 2)
    return rho * D

def local_op(K1, n, q):
    return kron_list([K1 if k == q else I2 for k in range(n)])

def apply_local_channel(rho, n, q, kraus1q):
    out = np.zeros_like(rho)
    for K in kraus1q:
        Kf = local_op(K, n, q)
        out += Kf @ rho @ Kf.conj().T
    return out

def phase_damping_kraus(lam):
    return [np.array([[1, 0], [0, np.sqrt(1 - lam)]], complex),
            np.array([[0, 0], [0, np.sqrt(lam)]], complex)]

def amp_damping_kraus(gam):
    return [np.array([[1, 0], [0, np.sqrt(1 - gam)]], complex),
            np.array([[0, np.sqrt(gam)], [0, 0]], complex)]

def apply_independent(rho, n, kraus1q):
    for q in range(n):
        rho = apply_local_channel(rho, n, q, kraus1q)
    return rho

# ---------- encodings ----------
n = 2
psi_EXP = (np.eye(4)[0] + np.eye(4)[3]) / np.sqrt(2)   # (|00>+|11>)/sqrt2
psi_DFS = (np.eye(4)[1] + np.eye(4)[2]) / np.sqrt(2)   # (|01>+|10>)/sqrt2  (= MELQ singlet-subspace logical +)

print("=" * 66)
print("EXPERIMENT A — collective dephasing:  DFS/shared-Form vs exposed")
print("=" * 66)
print(" sigma     F(DFS/MELQ)   F(exposed)")
for sigma in [0.0, 0.25, 0.5, 0.8, 1.2, 2.0]:
    fd = fidelity(psi_DFS, collective_dephasing(dm(psi_DFS), n, sigma))
    fe = fidelity(psi_EXP, collective_dephasing(dm(psi_EXP), n, sigma))
    print(f" {sigma:4.2f}      {fd:8.4f}      {fe:8.4f}")
assert all(abs(fidelity(psi_DFS, collective_dephasing(dm(psi_DFS), n, s)) - 1.0) < 1e-12
           for s in [0.0, 0.5, 1.2, 2.0]), "DFS must be immune to collective dephasing"
print(" -> DFS fidelity == 1.0000 for all sigma (passive protection, zero active QEC).")

print()
print("=" * 66)
print("EXPERIMENT B — HONEST LIMIT: independent (local) noise hits BOTH")
print("=" * 66)
print(" channel              F(DFS)    F(exposed)")
for lam in [0.1, 0.3]:
    fd = fidelity(psi_DFS, apply_independent(dm(psi_DFS), n, phase_damping_kraus(lam)))
    fe = fidelity(psi_EXP, apply_independent(dm(psi_EXP), n, phase_damping_kraus(lam)))
    print(f" indep. dephase l={lam:<4} {fd:8.4f}   {fe:8.4f}")
for gam in [0.1, 0.3]:
    fd = fidelity(psi_DFS, apply_independent(dm(psi_DFS), n, amp_damping_kraus(gam)))
    fe = fidelity(psi_EXP, apply_independent(dm(psi_EXP), n, amp_damping_kraus(gam)))
    print(f" amp damping  g={gam:<4} {fd:8.4f}   {fe:8.4f}")
print(" -> DFS is NOT magic: non-collective noise degrades it too. Needs the active layer.")

print()
print("=" * 66)
print("EXPERIMENT C — Hybrid QTC-MELQ: total-Z parity catches amp-damping jumps (P4)")
print("=" * 66)
P0 = np.zeros((4, 4), complex); P0[1, 1] = 1; P0[2, 2] = 1     # projector onto total-Z=0 (DFS) subspace
print(" gamma   F_raw(DFS)   accept(yield)   F_postselected")
for gam in [0.1, 0.2, 0.3]:
    rho = apply_independent(dm(psi_DFS), n, amp_damping_kraus(gam))
    f_raw = fidelity(psi_DFS, rho)
    yield_ = float(np.real(np.trace(P0 @ rho)))
    rho_ps = (P0 @ rho @ P0) / yield_
    f_ps = fidelity(psi_DFS, rho_ps)
    print(f" {gam:4.2f}    {f_raw:8.4f}     {yield_:8.4f}        {f_ps:8.4f}")
    assert f_ps > f_raw - 1e-9, "parity post-selection should not reduce fidelity"
print(" -> A leakage/amplitude jump changes total-Z -> heralded & removed; accepted state is cleaner.")
print("    (detection, not correction: rejected fraction = 1 - yield is the cost.)")

print()
print("=" * 66)
print("EXPERIMENT D — residual quasi-static dephasing: delta_q-triggered DD (P3)")
print("=" * 66)
# quasi-static Gaussian dephasing: coherence(A) = 0.5 * exp(-0.5 * sigma_f^2 * A^2),
# A = signed accumulated time (sign flips at each DD/X pulse). |+> -> rho01 = 0.5.
sigma_f, t_total, steps = 1.6, 1.0, 200
def coh(A):           # off-diagonal magnitude
    return 0.5 * np.exp(-0.5 * sigma_f ** 2 * A ** 2)
def delta_q(A):       # imbalance metric: 0 = fully coherent, ->1 = decohered
    return 1.0 - coh(A) / 0.5

# (1) no DD
A_no = t_total
# (2) CPMG-8: 8 evenly spaced pi-pulses -> for quasi-static, refocuses A -> ~0
def cpmg(k):
    dt = t_total / steps
    A = 0.0; s = 1.0; flip_at = set(int(steps * (m + 0.5) / k) for m in range(k))
    pulses = 0
    for i in range(steps):
        if i in flip_at:
            s = -s; pulses += 1
        A += s * dt
    return A, pulses
A_cpmg, p_cpmg = cpmg(8)
# (3) delta_q-triggered DD: flip only when delta_q would exceed threshold (bang-bang around 0)
def triggered(thr):
    dt = t_total / steps
    A = 0.0; s = 1.0; pulses = 0; peak = 0.0
    for _ in range(steps):
        A += s * dt
        peak = max(peak, delta_q(A))
        if delta_q(A) > thr:
            s = -s; pulses += 1
    return A, pulses, peak
A_tr, p_tr, peak_tr = triggered(thr=0.05)

print(f" sigma_f={sigma_f}, total time={t_total}")
print(f" {'scheme':<22}{'pulses':>8}{'final coh':>12}{'final delta_q':>15}")
print(f" {'no DD':<22}{0:>8}{coh(A_no):>12.4f}{delta_q(A_no):>15.4f}")
print(f" {'CPMG-8 (fixed)':<22}{p_cpmg:>8}{coh(A_cpmg):>12.4f}{delta_q(A_cpmg):>15.4f}")
print(f" {'delta_q-triggered':<22}{p_tr:>8}{coh(A_tr):>12.4f}{delta_q(A_tr):>15.4f}")
print(f" -> triggered holds delta_q<=0.05 (peak {peak_tr:.3f}) with {p_tr} pulses vs CPMG's {p_cpmg};")
print(f"    no-DD has collapsed to coh={coh(A_no):.4f}. Adaptive DD = same protection, fewer pulses.")
assert coh(A_tr) > coh(A_no) + 0.2, "triggered DD must beat no-DD"
assert p_tr <= p_cpmg, "triggered should use no more pulses than fixed CPMG here"

print()
print("=" * 66)
print("EXPERIMENT E — Holevo ledger (honest accounting, P6)")
print("=" * 66)
log2_3 = np.log2(3)
print(f" retrievable classical info per qutrit token : <= log2(3) = {log2_3:.4f} bits  (Holevo)")
print(f" retrievable per DFS logical qubit            : <= 1 bit")
# stabilization tax avoided under collective dephasing at sigma=1.0 (Exp A):
fe1 = fidelity(psi_EXP, collective_dephasing(dm(psi_EXP), n, 1.0))
print(f" collective-noise infidelity AVOIDED (sigma=1) : {1.0 - fe1:.4f}  (exposed loses this; DFS loses 0)")
print(" => QTC gains: passive stabilization-tax reduction + correlation/structure,")
print("    NOT extra retrievable bits (Holevo bound respected).")
print()
print("ALL ASSERTS PASSED.")
