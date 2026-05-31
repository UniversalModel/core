"""
QTC — Phase 3 HARDWARE test (IBM Quantum, real QPU).  READY TO RUN — needs your IBM key.
U-Theory APPENDIX_QTC / QTC-BENCH. qiskit-ibm-runtime >= 0.40.

Minimal Loschmidt-echo experiment, sized for the ~10-min free Open-plan budget:
  prepare logical |+_L>  ->  idle delay (let device noise act)  ->  uncompute (inverse prep)  ->  measure.
  P(|00>) = fidelity of the logical state to ideal.  Compare DFS vs exposed:
    DFS logical : (|01>+|10>)/sqrt2   (total-Z=0; protected vs the COLLECTIVE part of device dephasing)
    exposed     : (|00>+|11>)/sqrt2   (total-Z=+-2; fully exposed)
  If the device has any correlated/collective dephasing, P00(DFS) > P00(exposed) at the same delay.

----------------------------------------------------------------------------------------
SECURITY — do NOT paste your token into a chat. Run this ONCE locally to save it:

    from qiskit_ibm_runtime import QiskitRuntimeService
    QiskitRuntimeService.save_account(
        channel="ibm_quantum_platform",
        token="<YOUR_IBM_CLOUD_API_KEY>",
        instance="<YOUR_INSTANCE_CRN>",     # from quantum.cloud.ibm.com -> Instances
        overwrite=True)

Then just run:  python qtc_hw_ibm.py
The token is stored in ~/.qiskit/qiskit-ibm.json — this script never contains it.
----------------------------------------------------------------------------------------
"""
SHOTS = 2048
DELAYS_US = [0, 40]          # idle time in microseconds (keep small -> tiny QPU time)

def prep(qc, dfs):
    qc.h(0); qc.cx(0, 1)
    if dfs: qc.x(1)
def inv_prep(qc, dfs):
    if dfs: qc.x(1)
    qc.cx(0, 1); qc.h(0)

def build(dfs, delay_us):
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(2)
    prep(qc, dfs); qc.barrier()
    if delay_us > 0:
        qc.delay(delay_us, 0, unit='us'); qc.delay(delay_us, 1, unit='us')
    qc.barrier(); inv_prep(qc, dfs); qc.measure_all()
    return qc

def main():
    try:
        from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
        from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    except Exception as e:
        print("Install: pip install qiskit qiskit-ibm-runtime  (", e, ")"); return
    try:
        service = QiskitRuntimeService()                 # uses your saved account
    except Exception as e:
        print("No saved IBM account. See the SECURITY block at the top of this file to save your key.")
        print("Details:", e); return

    backend = service.least_busy(operational=True, simulator=False)
    print(f"backend: {backend.name}  ({backend.num_qubits} qubits)")
    pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

    labels, circuits = [], []
    for dfs in (True, False):
        for d in DELAYS_US:
            labels.append(("DFS" if dfs else "exposed", d))
            circuits.append(pm.run(build(dfs, d)))

    sampler = SamplerV2(mode=backend)
    job = sampler.run(circuits, shots=SHOTS)
    print("job id:", job.job_id(), "— waiting for QPU result ...")
    res = job.result()

    print("\n enc       delay(us)   P(|00>) = logical fidelity")
    p = {}
    for i, (enc, d) in enumerate(labels):
        counts = res[i].data.meas.get_counts()
        p00 = counts.get('00', 0) / SHOTS
        p[(enc, d)] = p00
        print(f" {enc:<8}  {d:7d}     {p00:.4f}")

    dmax = max(DELAYS_US)
    if p.get(('exposed', dmax), 1) < 1:
        R = 1 - (1 - p[('DFS', dmax)]) / (1 - p[('exposed', dmax)])
        print(f"\n R_QTC (hardware, delay={dmax}us) = {R:.3f}")
        print(" R_QTC>0 => DFS retained more logical fidelity than exposed = real stabilization-tax reduction.")
        print(" (Expect modest R on fixed-frequency transmons: their dephasing is mostly independent, not collective.)")

if __name__ == "__main__":
    main()
