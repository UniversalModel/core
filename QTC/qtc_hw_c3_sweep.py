"""
QTC C.3 — collective-fraction sweep on real hardware: map R_QTC(eta) and find the crossover.
Inject a coherent two-qubit dephasing split into a COLLECTIVE (same-sign) and a DIFFERENTIAL
(opposite-sign) part, budgeted by eta:
   theta_c = THETA*eta  (collective, same sign on both)   -> hurts EXPOSED, not DFS
   theta_d = THETA*(1-eta) (differential, +/- on the two) -> hurts DFS, not exposed
   net: q0 gets RZ(theta_c+theta_d), q1 gets RZ(theta_c-theta_d)
eta=1 -> pure collective (DFS wins);  eta=0 -> pure differential (exposed wins).  Reads saved IBM account.
"""
import math
SHOTS = 2048; REPS = 5; THETA = math.pi/2
ETAS = [0.0, 0.25, 0.5, 0.75, 1.0]

def prep(qc, dfs):
    qc.h(0); qc.cx(0,1)
    if dfs: qc.x(1)
def inv_prep(qc, dfs):
    if dfs: qc.x(1)
    qc.cx(0,1); qc.h(0)
def build(dfs, eta):
    from qiskit import QuantumCircuit
    tc, td = THETA*eta, THETA*(1-eta)
    qc = QuantumCircuit(2); prep(qc, dfs); qc.barrier()
    qc.rz(tc+td, 0); qc.rz(tc-td, 1)
    qc.barrier(); inv_prep(qc, dfs); qc.measure_all()
    return qc

def main():
    import numpy as np
    from collections import defaultdict
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    service = QiskitRuntimeService()
    backend = service.least_busy(operational=True, simulator=False)
    print(f"backend: {backend.name} ({backend.num_qubits} qubits)")
    pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

    labels, circuits = [], []
    for _ in range(REPS):
        for dfs in (True, False):
            for eta in ETAS:
                labels.append(("DFS" if dfs else "exposed", eta))
                circuits.append(pm.run(build(dfs, eta)))
    print(f"submitting {len(circuits)} circuits ({REPS} reps x {2*len(ETAS)} configs), {SHOTS} shots ...")
    job = SamplerV2(mode=backend).run(circuits, shots=SHOTS)
    print("job id:", job.job_id(), "— waiting ...")
    res = job.result()

    agg = defaultdict(list)
    for i, key in enumerate(labels):
        agg[key].append(res[i].data.meas.get_counts().get('00',0)/SHOTS)

    print(f"\n eta(collective frac)   P00 DFS (n={REPS})    P00 exposed        R_QTC")
    prev = None; crossover = None
    for eta in ETAS:
        md = np.mean(agg[("DFS",eta)]); me = np.mean(agg[("exposed",eta)])
        sd = np.std(agg[("DFS",eta)]); se = np.std(agg[("exposed",eta)])
        R = (1-(1-md)/(1-me)) if me < 0.999 else float('-inf')
        diff = md - me
        if prev is not None and prev[1] < 0 <= diff:
            crossover = prev[0] + (eta-prev[0]) * (-prev[1])/(diff-prev[1])
        prev = (eta, diff)
        Rs = f"{R:+.3f}" if R != float('-inf') else "  -inf"
        print(f" {eta:5.2f}                  {md:.4f}+/-{sd:.4f}   {me:.4f}+/-{se:.4f}   {Rs}")
    if crossover is not None:
        print(f"\n crossover eta* (DFS overtakes exposed) ~ {crossover:.2f}")
    print(" R_QTC rises from negative (differential/independent) to ~+1 (collective). Maps the useful regime.")
    try: print(" QPU usage (billed seconds):", job.usage())
    except Exception as e: print(" (usage:", e, ")")

if __name__ == "__main__":
    main()
