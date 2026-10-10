# -*- coding: utf-8 -*-
"""hog_calibration_reference.py: reference code for APPENDIX_HOG, section HOG.6.

Post-hoc calibration of Jev probabilities against recorded outcomes:
isotonic regression (PAVA, with tie pooling), Platt scaling, the Brier score,
expected calibration error (ECE) and out-of-fold evaluation.

The policy gates of HOG.6 are enforced in `recommend()` and `calibrate()`:
candidate eligibility uses the total closed outcomes of one decision class;
out-of-fold training uses smaller subsets of that eligible cohort. Below
PLATT_MIN_PAIRS no calibrator is evaluated; below ISOTONIC_MIN_PAIRS isotonic
is not evaluated. Low-level fit/out_of_fold remain research primitives.
These gates are a policy, not a theorem or proof of deployment readiness.
Random folds assume exchangeable observations; use a separate chronological
or grouped holdout for dependent outcomes and for final policy assessment.

numpy only.  `python hog_calibration_reference.py` runs the self-tests and the
synthetic comparison reported in HOG.6.4.

(c) 2026 Petar Nikolov - code MIT
"""
import itertools

import numpy as np

MIN_PAIRS = 20              # below this: no calibration statement at all
PLATT_MIN_PAIRS = 200       # below this: measure (Brier, reliability), never remap
ISOTONIC_MIN_PAIRS = 300    # below this: isotonic is not fitted, Platt at most


# ---------------------------------------------------------------- PAVA

def pava(y, w=None):
    """Weighted isotonic (non-decreasing) least-squares fit of y, in input order.

    Classic pool-adjacent-violators: a stack of blocks, merged while the last
    two violate monotonicity.  O(n).  Weights must be positive and finite.
    """
    y = np.asarray(y, dtype=float)
    w = np.ones_like(y) if w is None else np.asarray(w, dtype=float)
    if y.ndim != 1 or w.shape != y.shape:
        raise ValueError("y and w must be 1-D arrays of the same length")
    if not (np.all(np.isfinite(y)) and np.all(np.isfinite(w))):
        raise ValueError("y and w must be finite")
    if np.any(w <= 0):
        raise ValueError("weights must be positive")
    val, wt, cnt = [], [], []
    for yi, wi in zip(y, w):
        val.append(yi)
        wt.append(wi)
        cnt.append(1)
        while len(val) > 1 and val[-2] > val[-1]:
            wsum = wt[-2] + wt[-1]
            v = (val[-2] * wt[-2] + val[-1] * wt[-1]) / wsum
            c = cnt[-2] + cnt[-1]
            del val[-2:], wt[-2:], cnt[-2:]
            val.append(v)
            wt.append(wsum)
            cnt.append(c)
    return np.repeat(np.asarray(val), cnt)


# ---------------------------------------------------------------- calibrators

def _check(scores, labels):
    s = np.asarray(scores, dtype=float)
    y = np.asarray(labels, dtype=float)
    if s.ndim != 1 or s.shape != y.shape or s.size == 0:
        raise ValueError("scores and labels must be non-empty 1-D arrays of equal length")
    if not np.all(np.isfinite(s)) or np.any((s < 0) | (s > 1)):
        raise ValueError("scores must be probabilities in [0, 1]")
    if not np.all((y == 0) | (y == 1)):
        raise ValueError("labels must be 0 or 1")
    return s, y


def _prediction_scores(scores):
    s = np.asarray(scores, dtype=float)
    if s.ndim != 1 or not np.all(np.isfinite(s)) or np.any((s < 0) | (s > 1)):
        raise ValueError("prediction scores must be a 1-D array of finite probabilities in [0, 1]")
    return s


def _positive_integer(value, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value < 1:
        raise ValueError(name + " must be a positive integer")
    return int(value)


class Isotonic:
    """Isotonic calibration map.  Tied scores are pooled before PAVA, so one
    input score has exactly one calibrated value.  Between fitted points the
    map is linearly interpolated; outside them it is clipped."""

    def fit(self, scores, labels):
        s, y = _check(scores, labels)
        xs, inv = np.unique(s, return_inverse=True)
        cnt = np.bincount(inv).astype(float)
        mean = np.bincount(inv, weights=y) / cnt
        self.x_ = xs
        self.y_ = pava(mean, cnt)
        return self

    def predict(self, scores):
        return np.interp(_prediction_scores(scores), self.x_, self.y_)


def _expit(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -35.0, 35.0)))


def _logit(p):
    p = np.clip(np.asarray(p, dtype=float), 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def _xent(t, p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return float(-np.sum(t * np.log(p) + (1 - t) * np.log(1 - p)))


class Platt:
    """Platt scaling on the logit of the score: p = expit(a * logit(s) + b).
    Platt's (1999) smoothed targets; Newton steps with backtracking."""

    def fit(self, scores, labels):
        s, y = _check(scores, labels)
        f = _logit(s)
        n1 = y.sum()
        n0 = y.size - n1
        t = np.where(y > 0.5, (n1 + 1) / (n1 + 2), 1 / (n0 + 2))
        a, b = 1.0, 0.0
        for _ in range(100):
            p = _expit(a * f + b)
            g = np.array([np.sum((p - t) * f), np.sum(p - t)])
            v = p * (1 - p)
            h = np.array([[np.sum(v * f * f), np.sum(v * f)],
                          [np.sum(v * f), np.sum(v)]]) + 1e-9 * np.eye(2)
            step = np.linalg.solve(h, g)
            loss, lam = _xent(t, p), 1.0
            while lam > 1e-8:
                a2, b2 = a - lam * step[0], b - lam * step[1]
                if _xent(t, _expit(a2 * f + b2)) <= loss + 1e-12:
                    break
                lam /= 2
            a, b = a2, b2
            if np.max(np.abs(lam * step)) < 1e-10:
                break
        self.a_, self.b_ = float(a), float(b)
        return self

    def predict(self, scores):
        return _expit(self.a_ * _logit(_prediction_scores(scores)) + self.b_)


class Identity:
    """The raw score, unchanged.  The baseline every calibrator must beat."""

    def fit(self, scores, labels):
        _check(scores, labels)
        return self

    def predict(self, scores):
        return _prediction_scores(scores)


# ---------------------------------------------------------------- metrics

def brier(p, y):
    """Mean squared error of probabilities against 0/1 outcomes (Brier 1950)."""
    p, y = _check(p, y)
    return float(np.mean((p - y) ** 2))


def ece(p, y, bins=10):
    """Expected calibration error: equal-width bins, weighted by bin size."""
    p, y = _check(p, y)
    bins = _positive_integer(bins, "bins")
    idx = np.clip((p * bins).astype(int), 0, bins - 1)
    total = 0.0
    for b in range(bins):
        m = idx == b
        if m.any():
            total += m.mean() * abs(p[m].mean() - y[m].mean())
    return float(total)


def reliability(p, y, bins=5):
    """Rows (bin, n, mean stated, observed frequency) for a reliability table."""
    p, y = _check(p, y)
    bins = _positive_integer(bins, "bins")
    idx = np.clip((p * bins).astype(int), 0, bins - 1)
    rows = []
    for b in range(bins):
        m = idx == b
        if m.any():
            rows.append((b, int(m.sum()), float(p[m].mean()), float(y[m].mean())))
    return rows


def out_of_fold(make, scores, labels, k=5, seed=0):
    """Out-of-fold predictions: each point is calibrated by a map fitted
    without it.  In-sample calibration error of isotonic regression is near
    zero by construction and says nothing."""
    s, y = _check(scores, labels)
    k = _positive_integer(k, "k")
    if not 2 <= k <= s.size:
        raise ValueError("k must be between 2 and the number of observations")
    fold = np.random.default_rng(seed).permutation(s.size) % k
    pred = np.full_like(s, np.nan)
    for j in range(k):
        tr = fold != j
        values = _prediction_scores(make().fit(s[tr], y[tr]).predict(s[~tr]))
        if values.shape != s[~tr].shape:
            raise ValueError("calibrator returned the wrong number of predictions")
        pred[~tr] = values
    if not np.all(np.isfinite(pred)):
        raise ValueError("out-of-fold predictions are incomplete")
    return pred


# ---------------------------------------------------------------- policy

def recommend(n_pairs):
    """HOG.6 gate for one decision class with n_pairs closed outcomes."""
    if isinstance(n_pairs, (bool, np.bool_)) or not isinstance(n_pairs, (int, np.integer)) or n_pairs < 0:
        raise ValueError("n_pairs must be a non-negative integer")
    if n_pairs < MIN_PAIRS:
        return "none"          # report the count, make no calibration statement
    if n_pairs < PLATT_MIN_PAIRS:
        return "measure"       # Brier and reliability table only; no remapping
    if n_pairs < ISOTONIC_MIN_PAIRS:
        return "platt"
    return "platt_or_isotonic"  # isotonic only if it beats Platt out of fold


def calibrate(scores, labels, k=5, seed=0):
    """Apply the gate.  Returns (method, fitted map or None, report)."""
    s, y = _check(scores, labels)
    rec = recommend(s.size)
    report = {"n": int(s.size), "gate": rec,
              "calibration_established": False, "authorizes_deployment": False,
              "eligibility_basis": "total_cohort_size; OOF training subsets are smaller",
              "validation": "random OOF for candidate selection, not an independent final holdout"}
    if rec == "none":
        return rec, None, report
    report.update(brier_raw=brier(s, y), ece_raw=ece(s, y, bins=5),
                  reliability_raw=reliability(s, y, bins=5))
    if rec in ("none", "measure"):
        return rec, None, report
    candidates = [("identity", Identity), ("platt", Platt)]
    if rec == "platt_or_isotonic":
        candidates.append(("isotonic", Isotonic))
    oof = {name: out_of_fold(make, s, y, k, seed)
           for name, make in candidates}
    for name, pred in oof.items():
        report["brier_oof_" + name] = brier(pred, y)
        report["ece_oof_" + name] = ece(pred, y)
    choice = "platt"
    if rec == "platt_or_isotonic" and report["brier_oof_isotonic"] < report["brier_oof_platt"]:
        choice = "isotonic"
    if report["brier_oof_" + choice] >= report["brier_oof_identity"]:
        return "identity", Identity().fit(s, y), report   # no calibrator beats the raw score
    model = (Isotonic if choice == "isotonic" else Platt)().fit(s, y)
    return choice, model, report


# ---------------------------------------------------------------- self-tests

def _brute_isotonic(y, w):
    """Exhaustive optimum over every split into contiguous blocks (small n)."""
    n = len(y)
    best, best_fit = np.inf, None
    for cuts in itertools.product((0, 1), repeat=n - 1):
        bounds = [0] + [i + 1 for i, c in enumerate(cuts) if c] + [n]
        fit = np.empty(n)
        means = []
        for a, b in zip(bounds[:-1], bounds[1:]):
            m = np.sum(y[a:b] * w[a:b]) / np.sum(w[a:b])
            fit[a:b] = m
            means.append(m)
        if np.all(np.diff(means) >= -1e-12):
            sse = float(np.sum(w * (y - fit) ** 2))
            if sse < best - 1e-12:
                best, best_fit = sse, fit
    return best, best_fit


def _chat_wrapper_value_at(scores, labels, x):
    """Faithful reproduction of the wrapper from the source conversation
    (argsort, PAVA on labels, first index per unique score, np.interp).
    Kept only to demonstrate the tie defect described in HOG.6.3."""
    s = np.asarray(scores, dtype=float)
    y = np.asarray(labels, dtype=float)
    order = np.argsort(s)
    fitted = pava(y[order])
    us, ui = np.unique(s[order], return_index=True)
    return float(np.interp(x, us, fitted[ui])), fitted


def _selftest():
    rng = np.random.default_rng(20261010)
    worst = 0.0
    for _ in range(400):
        n = int(rng.integers(1, 10))
        y = rng.normal(size=n)
        w = rng.uniform(0.2, 3.0, size=n)
        sse_brute, fit_brute = _brute_isotonic(y, w)
        fit = pava(y, w)
        worst = max(worst, abs(float(np.sum(w * (y - fit) ** 2)) - sse_brute),
                    float(np.max(np.abs(fit - fit_brute))))
        assert np.all(np.diff(fit) >= -1e-12)
    print("T1 PAVA equals the exhaustive optimum on 400 random weighted cases; max deviation %.1e" % worst)
    assert worst < 1e-9

    v_chat, fitted = _chat_wrapper_value_at([0.5, 0.5], [0, 1], 0.5)
    v_ref = float(Isotonic().fit([0.5, 0.5], [0, 1]).predict([0.5])[0])
    print("T2 two identical scores 0.5 with outcomes 0 and 1: source wrapper fits %s and maps 0.5 -> %.2f;"
          " reference maps 0.5 -> %.2f" % (np.round(fitted, 2).tolist(), v_chat, v_ref))
    assert v_chat == 0.0 and abs(v_ref - 0.5) < 1e-12

    s = rng.uniform(size=50)
    y = (rng.uniform(size=50) < s).astype(float)
    m = Isotonic().fit(s, y)
    print("T3 isotonic map is non-decreasing and preserves the mean: %s, |mean diff| %.1e"
          % (bool(np.all(np.diff(m.y_) >= -1e-12)),
             abs(np.average(m.y_, weights=np.unique(s, return_counts=True)[1]) - y.mean())))
    for n, want in ((5, "none"), (50, "measure"), (250, "platt"), (500, "platt_or_isotonic")):
        assert recommend(n) == want
    print("T4 gates: 5->none, 50->measure, 250->platt, 500->platt_or_isotonic")


def _simulate(n, shape, seed):
    """Synthetic judge.  NOT Jev data.
    'sigmoid': stated = expit(2*logit(q)), an overconfident logistic distortion
               (Platt's own model, so it favours Platt).
    'step':    true frequency 0.55 for every stated value below 0.95 and 0.90
               above it, the shape described in the source conversation."""
    rng = np.random.default_rng(seed)
    if shape == "sigmoid":
        q = rng.beta(2, 2, size=n)
        stated = _expit(2.0 * _logit(q))
    else:
        stated = np.where(rng.uniform(size=n) < 0.4,
                          rng.uniform(0.95, 1.0, size=n), rng.uniform(0.5, 0.95, size=n))
        q = np.where(stated >= 0.95, 0.90, 0.55)
    y = (rng.uniform(size=n) < q).astype(float)
    return stated, y


def _comparison():
    print("\nSynthetic comparison, out-of-fold (5 folds), mean over 20 seeds. Not Jev data.")
    print("%-8s %6s | %-24s | %-24s | %-24s" % ("shape", "n", "Brier raw / Platt / iso",
                                                "ECE raw / Platt / iso", "iso beats Platt (Brier)"))
    for shape in ("sigmoid", "step"):
        for n in (100, 300, 1000, 5000):
            acc = {k: [] for k in ("br", "bp", "bi", "er", "ep", "ei")}
            wins = 0
            for seed in range(20):
                s, y = _simulate(n, shape, 1000 * n + seed)
                pp = out_of_fold(Platt, s, y, seed=seed)
                pi = out_of_fold(Isotonic, s, y, seed=seed)
                acc["br"].append(brier(s, y))
                acc["bp"].append(brier(pp, y))
                acc["bi"].append(brier(pi, y))
                acc["er"].append(ece(s, y))
                acc["ep"].append(ece(pp, y))
                acc["ei"].append(ece(pi, y))
                wins += brier(pi, y) < brier(pp, y)
            mean = {k: float(np.mean(v)) for k, v in acc.items()}
            print("%-8s %6d | %.4f / %.4f / %.4f | %.4f / %.4f / %.4f | %2d of 20"
                  % (shape, n, mean["br"], mean["bp"], mean["bi"],
                     mean["er"], mean["ep"], mean["ei"], wins))


def _gate_check(seeds=50, n_test=20000):
    """Where should the isotonic gate sit?  The whole policy is scored on fresh
    data it never saw: fit on n points (choosing Platt or isotonic by
    out-of-fold Brier on those same n points), then score on n_test new points
    from the same synthetic judge.  Not Jev data."""
    print("\nGate check: test Brier on %d fresh points, mean over %d seeds. Not Jev data." % (n_test, seeds))
    print("%-8s %5s | %-12s %-12s %-12s | %s" % ("shape", "n", "Platt only", "select OOF", "difference",
                                               "isotonic chosen"))
    for shape in ("sigmoid", "step"):
        for n in (300, 1000):
            p_only, select, chosen = [], [], 0
            for seed in range(seeds):
                s, y = _simulate(n, shape, 7000 * n + seed)
                st, yt = _simulate(n_test, shape, 9000 * n + seed)
                platt = Platt().fit(s, y)
                b_p = brier(out_of_fold(Platt, s, y, seed=seed), y)
                b_i = brier(out_of_fold(Isotonic, s, y, seed=seed), y)
                model = Isotonic().fit(s, y) if b_i < b_p else platt
                chosen += b_i < b_p
                p_only.append(brier(platt.predict(st), yt))
                select.append(brier(model.predict(st), yt))
            print("%-8s %5d | %.5f      %.5f      %+.5f     | %2d of %d"
                  % (shape, n, np.mean(p_only), np.mean(select),
                     np.mean(select) - np.mean(p_only), chosen, seeds))


if __name__ == "__main__":
    _selftest()
    _comparison()
    _gate_check()
