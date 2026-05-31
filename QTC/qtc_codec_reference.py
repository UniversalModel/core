import cmath, math

def dephase(theta):
    ph = {}
    for q0 in (0, 1):
        for q1 in (0, 1):
            ph[2*q0+q1] = cmath.exp(-1j*(theta/2)*((1-2*q0)+(1-2*q1)))
    return ph

def apply_channel(state, theta):
    ph = dephase(theta)
    return [ph[i]*a for i, a in enumerate(state)]

def fidelity(psi, phi):
    return abs(sum(a.conjugate()*b for a, b in zip(psi, phi)))**2

inv = 1/math.sqrt(2)
psi_DFS = [0, inv, inv, 0]
psi_EXP = [inv, 0, 0, inv]
grid = [0.0, math.pi/8, math.pi/4, math.pi/2, 3*math.pi/4, math.pi]

print("theta      F(DFS, shared-Form)   F(exposed)")
sd = se = 0.0
for th in grid:
    fd = fidelity(psi_DFS, apply_channel(psi_DFS, th))
    fe = fidelity(psi_EXP, apply_channel(psi_EXP, th))
    sd += fd; se += fe
    print(f"{th:6.3f}     {fd:18.4f}   {fe:10.4f}")
print("-"*48); print(f"mean over grid   {sd/len(grid):18.4f}   {se/len(grid):10.4f}")
assert all(abs(fidelity(psi_DFS, apply_channel(psi_DFS, th))-1.0) < 1e-12 for th in grid)
assert fidelity(psi_EXP, apply_channel(psi_EXP, math.pi/2)) < 0.01
print("ASSERTS PASSED (DFS invariant; exposed collapses at theta=pi/2).")
