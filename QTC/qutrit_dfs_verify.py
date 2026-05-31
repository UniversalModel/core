"""
Rigorous verification that the collective-Sz channel acts as EXACT IDENTITY on the whole
3-dim M=0 qutrit-DFS block (not just the symmetric state): random pure + random mixed logical
states, plus the entanglement (process) fidelity. Deterministic via fixed seed.
"""
import numpy as np, itertools
np.random.seed(0)

ms = [1, 0, -1]
basis = list(itertools.product(ms, ms))            # 9 two-qutrit states (m1,m2)
M = np.array([a + b for (a, b) in basis])
def dephase(rho, sigma):
    D = np.exp(-0.5 * sigma**2 * (M[:, None] - M[None, :])**2)
    return rho * D

dfs = [(1, -1), (0, 0), (-1, 1)]                   # M=0 subspace, 3-dim
dfs_idx = [basis.index(s) for s in dfs]

SIGMA = 2.0                                        # worst case in the sweep
# (1) random pure logical states
maxinf_pure = 0.0
for _ in range(2000):
    c = np.random.randn(3) + 1j * np.random.randn(3)
    psi = np.zeros(9, complex); psi[dfs_idx] = c; psi /= np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    F = np.real(psi.conj() @ dephase(rho, SIGMA) @ psi)
    maxinf_pure = max(maxinf_pure, abs(1 - F))
# (2) random mixed logical states  ‖Φ(ρ)-ρ‖_F
maxdev_mixed = 0.0
for _ in range(500):
    A = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
    r3 = A @ A.conj().T; r3 /= np.trace(r3)
    rho = np.zeros((9, 9), complex)
    for i, ii in enumerate(dfs_idx):
        for j, jj in enumerate(dfs_idx):
            rho[ii, jj] = r3[i, j]
    maxdev_mixed = max(maxdev_mixed, np.linalg.norm(dephase(rho, SIGMA) - rho))
# (3) entanglement (process) fidelity on the DFS block (max-entangled DFS<->3-dim reference)
Omega = np.zeros(9 * 3, complex)
for r in range(3):
    Omega[dfs_idx[r] * 3 + r] = 1 / np.sqrt(3)
rhoO = np.outer(Omega, Omega.conj())
Dfull = np.zeros((27, 27))
for s in range(9):
    for sp in range(9):
        f = np.exp(-0.5 * SIGMA**2 * (M[s] - M[sp])**2)
        for r in range(3):
            Dfull[s * 3 + r, sp * 3 + r] = f      # Phi⊗I : damping depends only on system index
# Phi⊗I applied elementwise needs full 27x27 mask; build it properly:
mask = np.zeros((27, 27))
for s in range(9):
    for r in range(3):
        for sp in range(9):
            for rp in range(3):
                mask[s * 3 + r, sp * 3 + rp] = np.exp(-0.5 * SIGMA**2 * (M[s] - M[sp])**2)
Fe = np.real(Omega.conj() @ (rhoO * mask) @ Omega)

print(f"sigma = {SIGMA}")
print(f"(1) 2000 random PURE logical states  : max|1-F|        = {maxinf_pure:.3e}")
print(f"(2)  500 random MIXED logical states : max||Phi(rho)-rho||_F = {maxdev_mixed:.3e}")
print(f"(3) entanglement (process) fidelity on DFS block        = {Fe:.10f}")
assert maxinf_pure < 1e-12 and maxdev_mixed < 1e-12 and abs(Fe - 1) < 1e-12
print("PASS: collective Sz channel = EXACT identity on the entire 3-dim qutrit-DFS block.")
