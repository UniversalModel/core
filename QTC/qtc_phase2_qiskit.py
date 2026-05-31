"""
QTC — Phase 2 (Qiskit/Aer): qutrit-token transpilation + DFS stabilization benchmark.
U-Theory APPENDIX_QTC. Requires qiskit>=2, qiskit-aer.

Encodings on 2 physical qubits (index |q0 q1>):
  EXPOSED logical : (|00>+|11>)/sqrt2   (Bell |Phi+>)        total-Z = +-2 -> hit by collective dephasing
  DFS/MELQ logical: (|01>+|10>)/sqrt2   (Bell |Psi+>)        total-Z =  0  -> immune to collective dephasing
  QTT type qutrit : {|00>=F, |01>=P, |10>=A},  |11> = leakage flag (4th, unused level)

Part 1: collective dephasing (shared RZ(theta), Gauss-Hermite average over theta~N(0,sigma)) -> DFS vs exposed
Part 2: Aer NoiseModel (amplitude + phase damping per qubit) -> DFS raw vs total-Z parity post-selected
Part 3: transpile DFS prep + qutrit token onto an IBM-like basis; report depth/op-counts; |11> leakage flag
Deterministic (Gauss-Hermite grid; seeded simulator).
"""
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector, DensityMatrix, state_fidelity
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, amplitude_damping_error, phase_damping_error

# ---------- prep circuits ----------
def exposed_prep():
    qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1)            # (|00>+|11>)/sqrt2
    return qc
def dfs_prep():
    qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1); qc.x(1)   # (|01>+|10>)/sqrt2
    return qc

IDEAL_EXP = Statevector(exposed_prep())
IDEAL_DFS = Statevector(dfs_prep())

# ---------- Part 1: collective dephasing ----------
def collective_fidelity(prep, ideal_sv, sigma, N=48):
    nodes, weights = hermegauss(N)                 # for integral with weight e^{-x^2/2}
    acc = np.zeros((4, 4), complex)
    for x, w in zip(nodes, weights):
        theta = sigma * x
        qc = prep.copy(); qc.rz(theta, 0); qc.rz(theta, 1)   # SAME theta on both = collective
        acc += w * DensityMatrix(qc).data
    acc /= np.sqrt(2 * np.pi)                       # normalise the Gaussian average (trace -> 1)
    return state_fidelity(ideal_sv, DensityMatrix(acc))

print("=" * 64)
print("PART 1 — collective dephasing (Qiskit, Gauss-Hermite avg): DFS vs exposed")
print("=" * 64)
print(" sigma     F(DFS/MELQ)   F(exposed)")
for sigma in [0.0, 0.3, 0.6, 1.0, 1.5]:
    fd = collective_fidelity(dfs_prep(), IDEAL_DFS, sigma)
    fe = collective_fidelity(exposed_prep(), IDEAL_EXP, sigma)
    print(f" {sigma:4.2f}      {fd:8.4f}      {fe:8.4f}")
assert all(abs(collective_fidelity(dfs_prep(), IDEAL_DFS, s) - 1.0) < 1e-9 for s in [0.3, 1.0, 1.5]), \
    "DFS must be immune to collective dephasing in Qiskit too"
print(" -> DFS F == 1.0000 for all sigma; exposed decays. Confirms passive Form-protection on real circuits.")

# ---------- Part 2: Aer noise model (independent) + parity heralding ----------
def noisy_dm(prep, gam, lam):
    nm = NoiseModel()
    err = amplitude_damping_error(gam).compose(phase_damping_error(lam))
    nm.add_all_qubit_quantum_error(err, ['id'])
    qc = prep.copy(); qc.id(0); qc.id(1); qc.save_density_matrix()
    sim = AerSimulator(method='density_matrix', noise_model=nm)
    res = sim.run(qc, seed_simulator=7).result()
    return res.data(0)['density_matrix'].data

P0 = np.zeros((4, 4), complex); P0[1, 1] = 1; P0[2, 2] = 1     # total-Z = 0 subspace {|01>,|10>}
print()
print("=" * 64)
print("PART 2 — Aer NoiseModel (amp+phase damping): DFS raw vs parity post-selected")
print("=" * 64)
print(" gamma  lam    F_raw(DFS)   yield     F_postselected")
for gam, lam in [(0.10, 0.05), (0.20, 0.10), (0.30, 0.15)]:
    rho = noisy_dm(dfs_prep(), gam, lam)
    f_raw = float(np.real(IDEAL_DFS.data.conj() @ rho @ IDEAL_DFS.data))
    y = float(np.real(np.trace(P0 @ rho)))
    rho_ps = (P0 @ rho @ P0) / y
    f_ps = float(np.real(IDEAL_DFS.data.conj() @ rho_ps @ IDEAL_DFS.data))
    print(f" {gam:4.2f}  {lam:4.2f}   {f_raw:8.4f}    {y:7.4f}    {f_ps:8.4f}")
    assert f_ps > f_raw - 1e-9
print(" -> total-Z parity heralds the amplitude-damping jumps (leakage out of the code) -> cleaner accepted state.")

# ---------- Part 3: transpilation onto IBM-like basis ----------
print()
print("=" * 64)
print("PART 3 — transpile qutrit token + DFS prep onto IBM-like basis ['rz','sx','x','cx']")
print("=" * 64)
basis = ['rz', 'sx', 'x', 'cx']
tq_dfs = transpile(dfs_prep(), basis_gates=basis, optimization_level=3)
print(f" DFS logical prep   : depth={tq_dfs.depth():2d}  ops={dict(tq_dfs.count_ops())}")

# QTT type qutrit (|00>=F,|01>=P,|10>=A) equal superposition; |11> amplitude 0 = leakage flag
amps = np.array([1, 1, 1, 0], complex) / np.sqrt(3)
qutrit = QuantumCircuit(2); qutrit.initialize(amps, [0, 1])
tq_qutrit = transpile(qutrit, basis_gates=basis, optimization_level=3)
leak = abs(Statevector(qutrit).data[3]) ** 2
print(f" QTT qutrit (F,P,A) : depth={tq_qutrit.depth():2d}  ops={dict(tq_qutrit.count_ops())}")
print(f" leakage-flag |11> population (should be 0): {leak:.6f}")
assert leak < 1e-12, "leakage flag must be empty for a valid qutrit token"
print(" -> qutrit token compiles to hardware gates; |11> is the unused 4th level = free leakage detector (P4).")

print()
print("qiskit", __import__('qiskit').__version__, "| ALL PHASE-2 ASSERTS PASSED.")
