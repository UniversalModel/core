# U-Model Simulations

## 📁 Available Simulations

### `dimensional_stability_toymodel.py`

**Purpose:** Demonstrates the Dimensional Stability Theorem (DST) numerically.

**What it does:**
- Simulates a system with Form (F), Position (P), and Action (A) components
- Shows that stable configurations maintain F + P + A ≈ const
- Visualizes the stability basin and perturbation responses

**Requirements:**
```bash
pip install numpy matplotlib scipy
```

**Usage:**
```bash
python dimensional_stability_toymodel.py
```

**Expected Output:**
- Console: Stability metrics and convergence data
- Plot: F-P-A trajectory in phase space

---

## 🔬 Reproducing Results

To reproduce the results from DST v23.2:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python simulations/dimensional_stability_toymodel.py`
4. Compare output with Table 3 in DST document

---

## 📊 Validation Status

| Simulation | Status | Last Run | Notes |
|------------|--------|----------|-------|
| DST Toymodel | ✅ Verified | 2026-01-30 | Matches analytical predictions |

---

## 🧪 Adding New Simulations

To contribute a new simulation:

1. Follow the naming convention: `{theorem_name}_{type}.py`
2. Include docstring with:
   - Purpose
   - Inputs/Outputs
   - Expected results
3. Add entry to this README

---

## 📬 Contact

For simulation-related questions: petar@u-model.org
