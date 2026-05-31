"""
Genuine QUTRIT decoherence-free subspace — does the number 3 do physical work?
Two qutrits (spin-1, Sz eigenvalues m in {+1,0,-1}) under COLLECTIVE Sz dephasing.
The total-M=0 subspace is 3-DIMENSIONAL -> it encodes a LOGICAL QUTRIT that is decoherence-free.
A 2-qubit M=0 DFS is only 2-dim (a logical qubit), so it CANNOT hold a logical qutrit:
=> protecting a triadic (3-level) unit genuinely requires qutrit carriers. The "3" is load-bearing.
Honest control: under INDEPENDENT (non-collective) dephasing the qutrit DFS also degrades (no free lunch).
Pure numpy, deterministic.
"""
import numpy as np
from itertools import product

# basis: two qutrits, index = 3*a + b; level k in {0,1,2} -> spin-1 eigenvalue m
mval = {0: 1, 1: 0, 2: -1}
def Mtot(idx): return mval[idx // 3] + mval[idx % 3]
def mA(idx): return mval[idx // 3]
def mB(idx): return mval[idx % 3]
Mvals = np.array([Mtot(i) for i in range(9)])

def dm(psi):
    psi = np.array(psi, complex); psi /= np.linalg.norm(psi); return np.outer(psi, psi.conj())
def fid(psi, rho):
    psi = np.array(psi, complex); psi /= np.linalg.norm(psi); return float(np.real(psi.conj() @ rho @ psi))
def ket(a, b):
    v = np.zeros(9, complex); v[3 * a + b] = 1.0; return v

def collective_dephasing(rho, sigma):                 # same Sz phase on BOTH qutrits
    D = np.exp(-0.5 * sigma**2 * (Mvals[:, None] - Mvals[None, :])**2)
    return rho * D

def independent_dephasing(rho, lam):                  # each qutrit's phase independent
    mA_ = np.array([mA(i) for i in range(9)]); mB_ = np.array([mB(i) for i in range(9)])
    D = np.exp(-0.5 * lam**2 * ((mA_[:, None] - mA_[None, :])**2 + (mB_[:, None] - mB_[None, :])**2))
    return rho * D

# --- logical qutrit in the M=0 DFS:  |0L>=|+1,-1>, |1L>=|0,0>, |2L>=|-1,+1>  (all M=0) ---
L0, L1, L2 = ket(0, 2), ket(1, 1), ket(2, 0)
psi_dfs = (L0 + L1 + L2) / np.sqrt(3)
# --- exposed logical qutrit: M-spread  |+1,+1>(M=2), |0,0>(0), |-1,-1>(M=-2) ---
E0, E1, E2 = ket(0, 0), ket(1, 1), ket(2, 2)
psi_exp = (E0 + E1 + E2) / np.sqrt(3)

print("DFS logical basis  M-values:", [Mtot(np.argmax(np.abs(x))) for x in (L0, L1, L2)], "(all 0 -> protected)")
print("exposed logical basis M-values:", [Mtot(np.argmax(np.abs(x))) for x in (E0, E1, E2)])

print("\n=== Q1: collective Sz dephasing — logical QUTRIT, DFS vs exposed ===")
print(" sigma   F(qutrit-DFS)   F(exposed)")
for s in [0.0, 0.3, 0.6, 1.0, 1.5, 2.0]:
    fd = fid(psi_dfs, collective_dephasing(dm(psi_dfs), s))
    fe = fid(psi_exp, collective_dephasing(dm(psi_exp), s))
    print(f" {s:4.2f}    {fd:.4f}        {fe:.4f}")
assert all(abs(fid(psi_dfs, collective_dephasing(dm(psi_dfs), s)) - 1) < 1e-12 for s in [0.3, 1.0, 2.0]), \
    "qutrit DFS must be invariant under collective Sz dephasing"

print("\n=== Q2: the dimensional argument — why 3 is essential ===")
def dfs_dim(d, n=2):
    levels = [(d - 1) - 2 * k for k in range(d)]      # integer Sz-like eigenvalues, symmetric about 0
    return sum(1 for combo in product(range(d), repeat=n)
               if sum(levels[k] for k in combo) == 0)
print(f" dim(total-M=0 DFS): 2 qubits = {dfs_dim(2)}  |  2 qutrits = {dfs_dim(3)}  |  2 ququarts = {dfs_dim(4)}")
print(" -> 2-qubit DFS = 2-dim (holds a logical QUBIT). A logical QUTRIT (3 levels) needs the")
print("    2-qutrit M=0 subspace (3-dim). You cannot protect a triadic unit with the simplest qubit DFS.")
assert dfs_dim(2) == 2 and dfs_dim(3) == 3, "dimensional counts"

print("\n=== Q3: HONEST limit — independent (non-collective) dephasing breaks it too ===")
print(" lambda  F(qutrit-DFS)   F(exposed)")
for lam in [0.0, 0.3, 0.6, 1.0]:
    fd = fid(psi_dfs, independent_dephasing(dm(psi_dfs), lam))
    fe = fid(psi_exp, independent_dephasing(dm(psi_exp), lam))
    print(f" {lam:4.2f}    {fd:.4f}        {fe:.4f}")
print(" -> under INDEPENDENT noise the qutrit DFS degrades too (no free lunch) — same scope as the qubit case.")

print("\nALL QUTRIT-DFS ASSERTS PASSED.")
print("Load-bearing '3': (a) protected logical unit IS a qutrit (3 levels);")
print("                  (b) 2-qutrit M=0 DFS is exactly 3-dim — unattainable from a 2-qubit DFS.")
