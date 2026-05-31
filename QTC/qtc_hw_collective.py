"""
QTC Phase-3b — confirm the DFS mechanism on real hardware by INJECTING collective noise.
Idle-noise run (qtc_hw_ibm.py) was independent T1/T2 -> DFS gave no benefit (R<0), as predicted.
Here we inject a COLLECTIVE Z rotation (same RZ(theta) on BOTH qubits) between prep and echo:
  DFS {|01>,|10>} (total-Z=0)  -> only a GLOBAL phase -> echo recovers -> P(00) stays high
  exposed {|00>,|11>}           -> RELATIVE phase     -> echo gives P(00) = cos^2(theta) -> drops
A positive R_QTC here = the symmetry protection is real on the device (gated by noise symmetry).

Reads the saved IBM account (run setup once via QiskitRuntimeService.save_account). qiskit-ibm-runtime>=0.40.
"""
import math
SHOTS = 2048
THETAS = [0.0, math.pi/4, math.pi/2]      # exposed P(00) ~ cos^2(theta): 1.0, 0.5, 0.0

def prep(qc, dfs):
    qc.h(0); qc.cx(0, 1)
    if dfs: qc.x(1)
def inv_prep(qc, dfs):
    if dfs: qc.x(1)
    qc.cx(0, 1); qc.h(0)

def build(dfs, theta):
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(2)
    prep(qc, dfs); qc.barrier()
    qc.rz(theta, 0); qc.rz(theta, 1)       # SAME theta on both = collective Z rotation
    qc.barrier(); inv_prep(qc, dfs); qc.measure_all()
    return qc

def main():
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    try:
        service = QiskitRuntimeService()
    except Exception as e:
        print("No saved IBM account — run setup first."); print(e); return
    backend = service.least_busy(operational=True, simulator=False)
    print(f"backend: {backend.name} ({backend.num_qubits} qubits)")
    pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

    import numpy as np
    from collections import defaultdict
    REPS = 5
    labels, circuits = [], []
    for _ in range(REPS):
        for dfs in (True, False):
            for th in THETAS:
                labels.append(("DFS" if dfs else "exposed", round(th, 4)))
                circuits.append(pm.run(build(dfs, th)))

    print(f"submitting {len(circuits)} circuits ({REPS} reps x {2*len(THETAS)} configs), {SHOTS} shots each ...")
    job = SamplerV2(mode=backend).run(circuits, shots=SHOTS)
    print("job id:", job.job_id(), "— waiting ...")
    res = job.result()

    agg = defaultdict(list)
    for i, key in enumerate(labels):
        agg[key].append(res[i].data.meas.get_counts().get('00', 0) / SHOTS)

    print(f"\n enc       theta      P(|00>) mean +/- std   (n={REPS})")
    stats = {}
    for enc in ("DFS", "exposed"):
        for th in [round(t, 4) for t in THETAS]:
            v = np.array(agg[(enc, th)]); stats[(enc, th)] = (v.mean(), v.std())
            print(f" {enc:<8}  {th:5.3f}    {v.mean():.4f} +/- {v.std():.4f}")

    th = round(math.pi / 2, 4)
    md, sd = stats[("DFS", th)]; me, se = stats[("exposed", th)]
    if me < 1:
        R = 1 - (1 - md) / (1 - me)
        print(f"\n R_QTC (collective, theta=pi/2) = {R:.3f}")
        print(f"   DFS P(00) = {md:.3f} +/- {sd:.3f}   vs   exposed P(00) = {me:.3f} +/- {se:.3f}")
        print(" R_QTC>0 => DFS invariant under collective Z (global phase) while exposed rotates")
        print("   => shared-Form symmetry protection is REAL on the device (noise-symmetry-gated).")
    try:
        print("\n QPU usage (billed seconds):", job.usage())
    except Exception as _e:
        print("\n (usage unavailable:", _e, ")")

if __name__ == "__main__":
    main()
