"""
QTC Phase-3c — measure the NATURAL collective-noise fraction on a real chip (MELQ proxy).

True 2-chip MELQ needs quantum networking (entanglement between separate QPUs) -> NOT on the free plan.
Instead: an idle delay-sweep (NO injected noise) comparing DFS vs exposed on one chip. This is the
direct on-chip probe of whether two qubits dephase COLLECTIVELY by themselves:
  if natural noise had a collective component, DFS would decay SLOWER than exposed (R_QTC>0).
From the earlier idle run we expect R<=0 (transmon noise is mostly independent) -> quantifies how far
real hardware is from the regime where the DFS discovery pays off for free.

Reads the saved IBM account. qiskit-ibm-runtime>=0.40.
"""
SHOTS = 2048
DELAYS_US = [0, 20, 40, 80]
REPS = 5

def prep(qc, dfs):
    qc.h(0); qc.cx(0, 1)
    if dfs: qc.x(1)
def inv_prep(qc, dfs):
    if dfs: qc.x(1)
    qc.cx(0, 1); qc.h(0)
def build(dfs, d):
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(2)
    prep(qc, dfs); qc.barrier()
    if d > 0:
        qc.delay(d, 0, unit='us'); qc.delay(d, 1, unit='us')   # natural idle noise only (no injection)
    qc.barrier(); inv_prep(qc, dfs); qc.measure_all()
    return qc

def main():
    import numpy as np
    from collections import defaultdict
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    try:
        service = QiskitRuntimeService()
    except Exception as e:
        print("No saved IBM account."); print(e); return
    backend = service.least_busy(operational=True, simulator=False)
    print(f"backend: {backend.name} ({backend.num_qubits} qubits)")
    pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

    labels, circuits = [], []
    for _ in range(REPS):
        for dfs in (True, False):
            for d in DELAYS_US:
                labels.append(("DFS" if dfs else "exposed", d))
                circuits.append(pm.run(build(dfs, d)))
    print(f"submitting {len(circuits)} circuits ({REPS} reps x {2*len(DELAYS_US)} configs), {SHOTS} shots ...")
    job = SamplerV2(mode=backend).run(circuits, shots=SHOTS)
    print("job id:", job.job_id(), "— waiting ...")
    res = job.result()

    agg = defaultdict(list)
    for i, key in enumerate(labels):
        agg[key].append(res[i].data.meas.get_counts().get('00', 0) / SHOTS)

    print(f"\n delay(us)   P00 DFS (n={REPS})     P00 exposed         R_QTC(natural)")
    for d in DELAYS_US:
        vd = np.array(agg[("DFS", d)]); ve = np.array(agg[("exposed", d)])
        md, me = vd.mean(), ve.mean()
        R = (1 - (1 - md) / (1 - me)) if me < 1 else 0.0
        print(f" {d:7d}    {md:.4f} +/- {vd.std():.4f}   {me:.4f} +/- {ve.std():.4f}   {R:+.3f}")
    print("\n R_QTC(natural) ~ 0 or negative  =>  device noise is ~independent (no free collective benefit).")
    print(" A positive natural R would mean genuine collective (shared-environment) dephasing.")
    try:
        print(" QPU usage (billed seconds):", job.usage())
    except Exception as e:
        print(" (usage unavailable:", e, ")")

if __name__ == "__main__":
    main()
