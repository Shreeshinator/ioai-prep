#!/usr/bin/env python3
"""Independent numerical checks for INAIO 2026 Stage 1, Alternate paper (28 Feb 2026).

Run:  python3 -I verify.py      (stdlib + numpy only)

Every answer is recomputed by brute force, enumeration, simulation or exact
fractions, independently of the hand working in SOLUTIONS.md.
"""
import re
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from math import cos, exp, floor, isclose, log, log2, pi, sqrt
from statistics import NormalDist

import numpy as np

ANSWERS = []


def answer(label, value, note=""):
    ANSWERS.append((label, value))
    print(f"  => {label}: {value}" + (f"   [{note}]" if note else ""))


def header(title):
    print("\n" + "=" * 78 + f"\n{title}\n" + "=" * 78)


# =============================================================================
header("A1.1 Cracking the Imperial Glyphs")
# Cross-situational learning: a glyph means a word if they occur in exactly
# the same set of sentences.
pairs = [
    ("this is a beautiful apple", "這美蘋果"),
    ("this is a very beautiful apple", "這很美蘋果"),
    ("this is an apple on a tree", "這蘋果樹"),
    ("they serve green apples in the palace", "服綠蘋果宮"),
    ("does the tree make the apple beautiful", "樹造蘋果美"),
    ("there is a palace on the black mountain", "這黑山宮"),
    ("the mountain paints the palace black", "山塗宮黑"),
    ("this is a sweet apple", "這甜蘋果"),
]
words = ["apple", "beautiful", "very", "tree", "serve", "green", "palace",
         "make", "black", "mountain", "paint", "sweet"]
glyphs = list(dict.fromkeys(g for _, s in pairs for g in s))  # order of first appearance
lexicon = {}
for w in words:
    occ_w = {i for i, (e, _) in enumerate(pairs) if w in e}
    lexicon[w] = "".join(g for g in glyphs
                         if {i for i, (_, s) in enumerate(pairs) if g in s} == occ_w)
print("  lexicon:", lexicon)
known = set("".join(lexicon.values()))
# Word order from "Does the tree make the apple beautiful?" = 樹 造 蘋果 美
assert pairs[4][1] == lexicon["tree"] + lexicon["make"] + lexicon["apple"] + lexicon["beautiful"]
opts = {"A": "山造蘋果甜", "B": "土造蘋果很甜", "C": "蘋果造土甜",
        "D": "土塗宮甜", "E": "土造蘋果甜", "F": "蘋果造甜山"}
pat = "^(.)" + lexicon["make"] + lexicon["apple"] + lexicon["sweet"] + "$"
ok = [k for k, v in opts.items() if (m := re.match(pat, v)) and m.group(1) not in known]
print("  'soil' has no known glyph, so the subject must be a new glyph (土).")
answer("A1.1", ",".join(ok))


# =============================================================================
header("A1.2 Filtering Fakes with Faulty Oracle (conceptual; option elimination)")
# Small text-only LLM + web retrieval, input = French headline + article body.
reliable = {
    "F2": "web retrieval can look up dates",
    "F4": "pure text entailment, both texts are in the prompt",
    "F5": "language ID of French text is easy",
    "F7": "topic classification is a core LLM skill",
    "F8": "spotting quotes is easy",
}
unreliable = {
    "F1": "LLMs see tokens, not characters -> bad at counting (and it is trivially computable)",
    "F3": "guess of a guess (outlet -> its leaning), subjective, model bias",
    "F6": "outlet guessing is hallucination-prone; fakes are copied across many sites",
}
options = {"A": {"F1", "F2", "F4"}, "B": {"F2", "F3", "F4"}, "C": {"F1", "F4", "F6"},
           "D": {"F3", "F4", "F5"}, "E": {"F1", "F3", "F4"}, "F": {"F1", "F3", "F6"}}
for k, s in options.items():
    print(f"  {k} {sorted(s)} contains reliable feature(s): {sorted(s & set(reliable)) or '-'}")
answer("A1.2", ",".join(k for k, s in options.items() if s == set(unreliable)))


# =============================================================================
header("A1.3 Smart Professor Search")


def ed(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        prev, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (ca != cb))
    return d[-1]


def ned(a, b):
    return 1 - ed(a, b) / max(len(a), len(b))


def ind(a, b):
    return 1.0 if a == b else 0.0


cands = {
    "A": lambda p, q: ind(p[0], q[0]) * (ned(p[2], q[2]) + ned(p[1], q[1])) / 2,
    "B": lambda p, q: ned(p[0], q[0]) * exp(-2 * (1 - ned(p[2], q[2])) - (1 - ned(p[1], q[1]))),
    "C": lambda p, q: ind(p[0], q[0]) * exp(-2 * (1 - ned(p[2], q[2])) - (1 - ned(p[1], q[1]))),
    "D": lambda p, q: ind(p[0], q[0]) * exp(-(1 - ned(p[2], q[2])) - 2 * (1 - ned(p[1], q[1]))),
    "E": lambda p, q: ind(p[0], q[0]) * (2 * ned(p[2], q[2]) + ned(p[1], q[1])),
    "F": lambda p, q: ind(p[0], q[0]) * (exp(-2 * (1 - ned(p[2], q[2]))) + exp(-(1 - ned(p[1], q[1])))),
}
rng = np.random.default_rng(0)
depts, titles = ["CS", "CE", "EE", "ME"], ["Dr.", "Prof.", "Mr.", "Ms."]
names = ["Alice Johnson", "Alice Jonson", "Alan Johnson", "Bob Smith", "Rob Smith", "Ann Lee"]
profiles = [(d, t, n) for d in depts for t in titles for n in names]
passing = []
for k, f in cands.items():
    bad = set()
    for _ in range(4000):
        p = profiles[rng.integers(len(profiles))]
        q = profiles[rng.integers(len(profiles))]
        s = f(p, q)
        if (abs(s - 1) < 1e-12) != (p == q):
            bad.add("rule1 (=1 iff identical)")
        if p[0] != q[0] and s != 0:
            bad.add("rule2 (dept differ -> 0)")
        if abs(s - f(q, p)) > 1e-12:
            bad.add("rule3 (symmetry)")
        if not (-1e-12 <= s <= 1 + 1e-12):
            bad.add("rule5 (range [0,1])")
    # rule 4: same-size mismatch u (= 1 - NED) in the name vs in the title, department equal
    g = {"A": lambda nn, nt: (nn + nt) / 2, "B": lambda nn, nt: exp(-2 * (1 - nn) - (1 - nt)),
         "C": lambda nn, nt: exp(-2 * (1 - nn) - (1 - nt)), "D": lambda nn, nt: exp(-(1 - nn) - 2 * (1 - nt)),
         "E": lambda nn, nt: 2 * nn + nt, "F": lambda nn, nt: exp(-2 * (1 - nn)) + exp(-(1 - nt))}[k]
    if not all(g(1 - u, 1) < g(1, 1 - u) for u in np.linspace(0.05, 1, 20)):
        bad.add("rule4 (name mismatch must hurt more)")
    print(f"  {k}: {'OK' if not bad else 'violates ' + ', '.join(sorted(bad))}")
    if not bad:
        passing.append(k)
answer("A1.3", ",".join(passing))


# =============================================================================
header("A1.4 Recursive V-67 Outbreak")
N, M, R = Fr(8), Fr(8), Fr(0)
for t in range(3):
    X = 2 * N + (2 + 4 * t) * M
    N, M, R = N / 2 + Fr(3, 4) * X, M / 2 + Fr(1, 4) * X, R + N / 2 + M / 2
    print(f"  start of day {t + 1}: N={N}, M={M}, R={R}   (X_{t}={X})")
answer("A1.4", f"R3 = {R}", "option D")


# =============================================================================
header("A1.5 Pikachu's Path (knight on 4x4, (0,0) -> (3,3), no revisits)")
n = 4
moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
best = [0, None]
count_by_len = {}


def dfs(cell, seen, path):
    if cell == (n - 1, n - 1):
        L = len(path)
        count_by_len[L] = count_by_len.get(L, 0) + 1
        if L > best[0]:
            best[0], best[1] = L, list(path)
        return  # the goal pad ends the path
    for dx, dy in moves:
        nx, ny = cell[0] + dx, cell[1] + dy
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
            seen.add((nx, ny)); path.append((nx, ny))
            dfs((nx, ny), seen, path)
            seen.discard((nx, ny)); path.pop()


dfs((0, 0), {(0, 0)}, [(0, 0)])
print("  number of simple paths by #pads:", dict(sorted(count_by_len.items())))
print("  one longest path:", best[1])
# Also check: even if the path may pass THROUGH (3,3) before ending there? Not
# allowed: landing on it twice is forbidden, so the path must end at its first visit.
answer("A1.5", best[0], "option E")


# =============================================================================
header("A2.1 Phulera Godown (L1 median vs Itakura-Saito)")
xs, ys = [40, 120, 220, 80], [180, 80, 120, 20]


def l1_argmin_range(vals):
    grid = np.arange(0, 260.5, 0.5)
    cost = np.array([sum(abs(g - v) for v in vals) for g in grid])
    mins = grid[np.isclose(cost, cost.min())]
    return mins.min(), mins.max()


(xlo, xhi), (ylo, yhi) = l1_argmin_range(xs), l1_argmin_range(ys)
xS, yS = Fr(int(xlo + xhi), 2), Fr(int(ylo + yhi), 2)
print(f"  L1 argmin x in [{xlo},{xhi}], y in [{ylo},{yhi}] -> G_S = ({xS}, {yS})")


def is_cost(u, vals):
    return sum(p / u - log(p / u) - 1 for p in vals)


def golden(f, a, b, it=200):
    g = (sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(it):
        if f(c) < f(d):
            b, d = d, c; c = b - g * (b - a)
        else:
            a, c = c, d; d = a + g * (b - a)
    return (a + b) / 2


uP, vP = golden(lambda u: is_cost(u, xs), 1, 400), golden(lambda v: is_cost(v, ys), 1, 400)
print(f"  IS argmin numerically: ({uP:.6f}, {vP:.6f});  means: ({Fr(sum(xs), 4)}, {Fr(sum(ys), 4)})")
xP, yP = Fr(sum(xs), 4), Fr(sum(ys), 4)
assert isclose(uP, float(xP), abs_tol=1e-6) and isclose(vP, float(yP), abs_tol=1e-6)
D2 = (xS - xP) ** 2 + (yS - yP) ** 2
print(f"  D^2 = {D2}  ->  D = {sqrt(D2)}")
answer("A2.1", floor(sqrt(D2)))


# =============================================================================
header("A2.2 Blind Board Gambit")
G = {"A": 2100, "B": 1800, "C": 1600}
An = {"X": 2000, "Y": 1700, "Z": 1500}


def pwin(r, s):
    return 1 / (1 + 10 ** ((s - r) / 400))


def match_win(anand, gukesh):
    # enumerate all 8 win/loss patterns of the 3 boards; keep those with >= 2 wins
    p = [pwin(An[a], G[g]) for a, g in zip(anand, gukesh)]
    return sum(float(np.prod([p[i] if w else 1 - p[i] for i, w in enumerate(ws)]))
               for ws in product([1, 0], repeat=3) if sum(ws) >= 2)


gukesh_opts = [("B", "C", "A"), ("C", "A", "B"), ("C", "B", "A")]
table = []
for perm in permutations("XYZ"):
    exp_win = sum(match_win(perm, g) for g in gukesh_opts) / 3
    actual = match_win(perm, ("C", "A", "B"))
    table.append((exp_win, perm, actual))
    print(f"  Anand {perm}: expected over 3 options = {exp_win:.5f}, vs actual (C,A,B) = {actual:.5f}")
table.sort(reverse=True)
best_exp, best_perm, p_actual = table[0]
print(f"  Anand's choice: {best_perm} (margin over 2nd best {best_exp - table[1][0]:.5f})")
print(f"  100p = {100 * p_actual:.6f}")
answer("A2.2", floor(100 * p_actual))


# =============================================================================
header("A2.3 Crude Curve Forecast")
# labelled points from the graph; "18-" is just before the jump, "18+" just after
pts = [(0, 58, 0), (6, 45, 0), (12, 64, 0), (18, 51, -1), (18, 26, +1), (24, 45, 0),
       (30, 32, 0), (36, 71, 0), (42, 58, 0), (48, 71, 0), (54, 52, 0), (60, 65, 0)]


def design(t, side, tauC, tauD, tauF, tauE):
    hD = 1.0 if (t > tauD or (t == tauD and side >= 0)) else 0.0
    hC = 1.0 if t >= tauC else 0.0
    hF = 1.0 if t >= tauF else 0.0
    # columns: A, B, C, D, F, E
    return [1, t, (1 - exp(-(t - tauC))) * hC, hD, (t - tauF) * hF, cos(2 * pi * t / tauE)]


fits = []
for tauC, tauD, tauF in permutations([18, 30, 42]):
    for tauE in [6, 12, 24]:
        Amat = np.array([design(t, s, tauC, tauD, tauF, tauE) for t, _, s in pts])
        yv = np.array([p for _, p, _ in pts], float)
        coef, *_ = np.linalg.lstsq(Amat, yv, rcond=None)
        rss = float(np.sum((Amat @ coef - yv) ** 2))
        fits.append((rss, tauC, tauD, tauF, tauE, coef))
fits.sort(key=lambda f: f[0])
rss, tauC, tauD, tauF, tauE, coef = fits[0]
print(f"  best taus: tauC={tauC}, tauD={tauD}, tauF={tauF}, tauE={tauE}; RSS={rss:.4f} "
      f"(next best RSS={fits[1][0]:.1f})")
print("  A,B,C,D,F,E =", np.round(coef, 4))
P75 = float(np.array(design(75, 0, tauC, tauD, tauF, tauE)) @ coef)
P75_round = float(np.array(design(75, 0, tauC, tauD, tauF, tauE)) @ np.array([50, 0.5, 20, -25, -1, 8]))
print(f"  P(75) with fitted params = {P75:.4f}; with rounded params (50,0.5,20,-25,-1,8) = {P75_round:.4f}")
answer("A2.3", floor(P75))


# =============================================================================
header("A2.4 Catalyst Constraint")
a, b, Ctot = 2, 3, 5
gA, gB = np.meshgrid(np.linspace(0, Ctot, 1001), np.linspace(0, Ctot, 1001))
tot_grid = np.where(gA + gB <= Ctot + 1e-12, 10 * gA - a * gA ** 2 + 20 * gB - b * gB ** 2, -np.inf)
i, j = np.unravel_index(tot_grid.argmax(), tot_grid.shape)
print(f"  2-D grid (cA + cB <= 5) best total={tot_grid[i, j]:.6f} at cA={gA[i, j]:.3f}, cB={gB[i, j]:.3f}")
print(f"  unconstrained optima cA=10/(2a)={10 / (2 * a)}, cB=20/(2b)={20 / (2 * b):.4f}, sum>{Ctot} so budget binds")
cA, cB = Fr(2), Fr(3)
tot = 10 * cA - a * cA ** 2 + 20 * cB - b * cB ** 2
print(f"  exact at (2,3): marginal gains {10 - 2 * a * cA} = {20 - 2 * b * cB}; total = {tot}")
answer("A2.4", floor(tot))


# =============================================================================
header("A2.5 Pit-Stop Paradox")
pSC = Fr(2, 5)
strat = {"No": [Fr(50, 100), Fr(25, 100), Fr(10, 100), Fr(15, 100)],
         "SC": [Fr(5, 100), Fr(10, 100), Fr(5, 100), Fr(80, 100)]}
hwin = {"No": [Fr(20, 100), Fr(85, 100), Fr(10, 100), Fr(50, 100)],
        "SC": [Fr(40, 100), Fr(15, 100), Fr(90, 100), Fr(55, 100)]}
prior = {"No": 1 - pSC, "SC": pSC}
joint = {(c, i): prior[c] * strat[c][i] * hwin[c][i] for c in prior for i in range(4)}
pH = sum(joint.values())
post = (joint[("No", 0)] + joint[("SC", 0)]) / pH
print(f"  P(H wins) = {pH} = {float(pH):.4f};  P(neither & H) = {joint[('No', 0)] + joint[('SC', 0)]}")
print(f"  P(neither | H) = {post} = {float(post):.5f}")
answer("A2.5", floor(100 * post))


# =============================================================================
header("B1 Code Triage")
n1, n2, n3 = 500, 350, 150
sens = [Fr(84, 100), Fr(70, 100), Fr(80, 100)]
spec = [Fr(90, 100), Fr(88, 100), Fr(89, 100)]
TP = [sens[0] * n1, sens[1] * n2, sens[2] * n3]
c3_to_1, c1_to_3 = Fr(10), Fr(25)
c1_to_2 = n1 - TP[0] - c1_to_3
c3_to_2 = n3 - TP[2] - c3_to_1
c2_off = n2 - TP[1]
FP_spec = [(1 - spec[0]) * (n2 + n3), (1 - spec[1]) * (n1 + n3), (1 - spec[2]) * (n1 + n2)]
print(f"  TP = {[int(v) for v in TP]};  row-forced: C1->C2={c1_to_2}, C3->C2={c3_to_2}, C2 off-diag total={c2_off}")
print(f"  FP implied by stated specificities: {[float(v) for v in FP_spec]}  (sum {float(sum(FP_spec))})")
print(f"  FP total forced by rows: {c1_to_2 + c1_to_3 + c2_off + c3_to_1 + c3_to_2}  -> data are slightly inconsistent")
print(f"  FP2 forced = {c1_to_2 + c3_to_2} -> true spec2 = {float(1 - (c1_to_2 + c3_to_2) / (n1 + n3)):.4f} "
      f"(stated 0.88 => specs are 2-dp rounded)")


def full_table(c2_to_1):
    c2_to_3 = c2_off - c2_to_1
    return [[TP[0], c1_to_2, c1_to_3], [c2_to_1, TP[1], c2_to_3], [c3_to_1, c3_to_2, TP[2]]]


# Completion 1: use spec1 (FP1 = 50)  -> C2->C1 = 40
T1 = full_table(FP_spec[0] - c3_to_1)
# Completion 2: use spec3 (FP3 = 93.5) -> C2->C3 = 68.5
T2 = full_table(c2_off - (FP_spec[2] - c1_to_3))
for name, T in [("spec1-completion", T1), ("spec3-completion", T2)]:
    print(f"  {name}: " + " | ".join(str([float(v) for v in row]) for row in T))

# Q1
print("  -- Q1 (fraction of ICU flags that are not ICU)")
q1_direct = FP_spec[2] / (TP[2] + FP_spec[2])
q1_t1 = (T1[0][2] + T1[1][2]) / (T1[0][2] + T1[1][2] + T1[2][2])
print(f"  direct from sens3/spec3: {float(q1_direct):.5f} -> {floor(100 * q1_direct)}")
print(f"  from table filled with spec1: {float(q1_t1):.5f} -> {floor(100 * q1_t1)}")
# integer tables consistent with ALL data after 2-dp rounding of specs
consistent = []
for c21 in range(0, int(c2_off) + 1):
    T = full_table(Fr(c21))
    FP = [T[1][0] + T[2][0], T[0][1] + T[2][1], T[0][2] + T[1][2]]
    neg = [n2 + n3, n1 + n3, n1 + n2]
    if all(round(float(1 - FP[i] / neg[i]), 2) == float(spec[i]) for i in range(3)):
        consistent.append((c21, FP[2], floor(100 * FP[2] / (FP[2] + TP[2]))))
print(f"  integer tables consistent with every stated number (C2->C1, FP3, Q1): {consistent}")
answer("B1.Q1", floor(100 * q1_direct), "direct; table-with-spec1 reading gives 42")

# Q2
print("  -- Q2 (hospitalised patients not sent home)")
q2 = spec[0]
q2_t1 = 1 - (T1[1][0] + T1[2][0]) / (n2 + n3)
q2_t2 = 1 - (T2[1][0] + T2[2][0]) / (n2 + n3)
print(f"  = specificity of class 1 = {q2} ; table checks: {q2_t1}, {float(q2_t2):.4f}")
answer("B1.Q2", floor(100 * q2))

# Q3
print("  -- Q3 (min expected cost; FN=8, FP=1, prevalence 0.15)")
pi3 = Fr(15, 100)
ptsROC = {"A": (Fr(2, 100), Fr(52, 100)), "B": (Fr(5, 100), Fr(68, 100)), "C": (Fr(8, 100), Fr(76, 100)),
          "D": (Fr(11, 100), Fr(80, 100)), "E": (Fr(14, 100), Fr(86, 100)), "F": (Fr(22, 100), Fr(91, 100))}
costs = {k: 8 * pi3 * (1 - tpr) + 1 * (1 - pi3) * fpr for k, (fpr, tpr) in ptsROC.items()}
for k, c in costs.items():
    print(f"  Point {k}: cost/patient = {float(c):.4f}")
answer("B1.Q3", "Point " + min(costs, key=costs.get), "option 5")

# Q4
print("  -- Q4 (s_new = s_old + 1.5(2b-1), b indep of s_old given y; RDT sens .85 spec .88)")
nd = NormalDist()
mus = [nd.inv_cdf(float(t)) - nd.inv_cdf(float(f)) for f, t in ptsROC.values()]
mu = sum(mus) / len(mus)
print(f"  binormal fit to figure: separation mu = {mu:.3f} SDs (per-point {np.round(mus, 2)})")


def Q(z):
    return 1 - nd.cdf(z)


delta, sb, fb = 1.5, 0.85, 0.12
print(f"  old AUC (binormal) = {nd.cdf(mu / sqrt(2)):.4f}")
for sigma in [0.1, 0.5, 1.0, 2.0, 5.0]:
    worst, best_gain, curve = 1.0, 0.0, []
    for tau in np.linspace(-12 * sigma - 6, 12 * sigma + mu * sigma + 6, 6001)[::-1]:
        fpr = fb * Q((tau - delta) / sigma) + (1 - fb) * Q((tau + delta) / sigma)
        tpr = sb * Q((tau - delta) / sigma - mu) + (1 - sb) * Q((tau + delta) / sigma - mu)
        curve.append((fpr, tpr))
        if 1e-6 < fpr < 1 - 1e-6:
            gain = tpr - nd.cdf(mu + nd.inv_cdf(fpr))
            worst, best_gain = min(worst, gain), max(best_gain, gain)
    fr, tr = np.array(curve).T
    auc_new = float(np.sum((fr[1:] - fr[:-1]) * (tr[1:] + tr[:-1]) / 2))
    print(f"  score SD={sigma:>4}: TPR gain at equal FPR ranges over [{worst:+.2e}, {best_gain:+.3f}]; new AUC = {auc_new:.4f}")
# pathological counterexample: classes already perfectly separated
rng = np.random.default_rng(1)
m = 200000
neg = rng.uniform(0, 1, m); pos = rng.uniform(1, 2, m)
bneg = rng.random(m) < fb; bpos = rng.random(m) < sb


def auc(sp, sn):
    allv = np.concatenate([sp, sn])
    r = allv.argsort().argsort() + 1
    return (r[:len(sp)].sum() - len(sp) * (len(sp) + 1) / 2) / (len(sp) * len(sn))


print(f"  caveat: perfectly separated old score -> AUC old={auc(pos, neg):.3f}, "
      f"new={auc(pos + delta * (2 * bpos - 1), neg + delta * (2 * bneg - 1)):.3f}")
answer("B1.Q4", "option 2 (improves consistently)", "holds for the binormal curve in the figure at every score scale")

# Q5
print("  -- Q5 (what can move the whole ROC curve up-left?)")
rng = np.random.default_rng(2)


def cohort(nn, prev, extra_feats=False, drop_icu=0.0):
    y = rng.random(nn) < prev
    s = rng.normal(0, 1, nn) + 2.07 * y
    if extra_feats:
        s = s + rng.normal(0, 1, nn) + 1.5 * y + rng.normal(0, 1, nn) + 1.5 * y
    if drop_icu:
        keep = ~(y & (rng.random(nn) < drop_icu))
        s, y = s[keep], y[keep]
    return s, y


scen = {
    "baseline (15%)": cohort(400000, 0.15),
    "1 prevalence 22%": cohort(400000, 0.22),
    "3 two new features": cohort(400000, 0.15, extra_feats=True),
    "4 sqrt transform": (lambda s, y: (np.sqrt(s - s.min()), y))(*cohort(400000, 0.15)),
    "5 bigger cohort": cohort(800000, 0.15),
    "6 drop random ICU": cohort(400000, 0.15, drop_icu=0.3),
}
for k, (s, y) in scen.items():
    print(f"  {k:<20} AUC = {auc(s[y], s[~y]):.4f}")
print("  2 (lower t2) just moves to another point on the SAME curve.")
answer("B1.Q5", "option 3 (new predictive features)")

# Q6
print("  -- Q6 (claims)")
rng = np.random.default_rng(3)
P = rng.normal(0, 3, (20000, 2))
w1, w2, w3 = rng.normal(size=(3, 3))
f = lambda w: P @ w[:2] + w[2]
cascade = np.where(f(w1) < 0, 1, np.where(f(w2) >= 0, 3, 2))
print(f"  cascade Y: every point gets exactly one label -> labels used {sorted(set(cascade))}, no conflicts possible")
v12, v23, v31 = f(w1) > 0, f(w2) > 0, f(w3) > 0     # pairwise winners
votes = np.stack([(~v12).astype(int) + v31, v12.astype(int) + (~v23), v23.astype(int) + (~v31)])
cycles = int(np.sum(votes.max(0) == 1))
print(f"  pairwise Z: {cycles} of {len(P)} points get a 1-1-1 voting cycle -> needs tie-breaking")
print("  Claim 1 needs BOTH Y and Z to be able to conflict -> false (Y is a cascade).")
print("  Claim 2: a dataset that Y classifies perfectly leaves Z nothing to beat -> 'strictly greater on any' is false.")
print("  loss on a point with margin y*f = -5:  SQ =", (1 - (-5)) ** 2, ", HG =", max(0, 1 + 5),
      " (SQ quadratic -> less robust; Claim 4 false, Claim 3's outlier part true)")
for pp in [0.6, 0.7, 0.9]:
    fs = np.linspace(-5, 5, 100001)
    risk_log = pp * np.log1p(np.exp(-fs)) + (1 - pp) * np.log1p(np.exp(fs))
    risk_hg = pp * np.maximum(0, 1 - fs) + (1 - pp) * np.maximum(0, 1 + fs)
    flog, fhg = fs[risk_log.argmin()], fs[risk_hg.argmin()]
    print(f"  P(y=+1|x)={pp}: logistic minimiser -> sigmoid(f*)={1 / (1 + exp(-flog)):.3f}; "
          f"hinge minimiser f*={fhg:.2f} (sigmoid={1 / (1 + exp(-fhg)):.3f})")
answer("B1.Q6", "options 3 and 5 (Claims 3, 5)")

# Q7
print("  -- Q7 (expected misclassification cost)")
cost = [[0, 10, 100], [50, 0, 20], [500, 100, 0]]
vals = []
for c21 in np.linspace(float(FP_spec[0] - c3_to_1) - 3.5, float(FP_spec[0] - c3_to_1), 8):
    T = full_table(Fr(c21).limit_denominator(1000))
    vals.append(float(sum(T[i][j] * cost[i][j] for i in range(3) for j in range(3)) / 1000))
x1 = sum(T1[i][j] * cost[i][j] for i in range(3) for j in range(3)) / 1000
x2 = sum(T2[i][j] * cost[i][j] for i in range(3) for j in range(3)) / 1000
print(f"  spec1-completion: {float(x1)};  spec3-completion: {float(x2)};  "
      f"range over all in-between completions: [{min(vals):.3f}, {max(vals):.3f}]")
answer("B1.Q7", floor(x1), "same floor under every completion")


# =============================================================================
header("B2 WonkaRank")
ing = {1: (1, 1, 0, 0), 2: (1, 1, 1, 1), 3: (1, 0, 1, 1), 4: (0, 1, 1, 1), 5: (1, 1, 0, 1),
       6: (0, 0, 1, 1), 7: (1, 0, 0, 0), 8: (1, 1, 0, 0), 9: (0, 1, 1, 0), 10: (0, 1, 0, 0)}
rel = {1: 10, 2: 0, 3: 0, 4: 0, 5: 3, 6: 0, 7: 0, 8: 5, 9: 2, 10: 0}
R = sum(1 for v in rel.values() if v > 0)


def dcg(order):
    return sum(rel[d] / log2(i + 2) for i, d in enumerate(order))


def rank(score):
    return sorted(ing, key=lambda d: (-score(d), d))


d1 = dcg([5, 3, 1, 9, 8])
print(f"  Q1 DCG@5 = {d1:.5f}")
answer("B2.Q1", floor(d1))

sA = lambda d: 2 if ing[d][0] and ing[d][1] else 0
sB = lambda d: 2 if ing[d][0] and ing[d][1] else (1 if ing[d][0] or ing[d][1] else 0)
for nm, s in [("A", sA), ("B", sB)]:
    top = rank(s)[:8]
    hits = sum(rel[d] > 0 for d in top)
    print(f"  Q2 strategy {nm}: top8={top} P@8={Fr(hits, 8)} R@8={Fr(hits, R)}")
answer("B2.Q2", "option 4 (B improves both)")

best_order = max(permutations([1, 5, 8, 9]), key=dcg)
q3opts = {1: [1, 5, 8, 9], 2: [8, 1, 5, 9], 3: [1, 8, 5, 9], 4: [5, 9, 1, 8], 5: [1, 8, 9, 5], 6: [9, 5, 8, 1]}
for k, o in q3opts.items():
    print(f"  Q3 option {k} {o}: DCG@4 = {dcg(o):.4f}")
answer("B2.Q3", f"option {[k for k, o in q3opts.items() if tuple(o) == best_order][0]} {list(best_order)}")

W = (3, 3, 1, 1)
scores = {
    "A": lambda d: sum(x * w for x, w in zip(ing[d], W)),
    "B": lambda d: sum(min(1, x) * min(1, w) for x, w in zip(ing[d], W)),
    "C": lambda d: sum(x * w for x, w in zip(ing[d], W)) - sum(ing[d]),
    "D": lambda d: Fr(sum(x * w for x, w in zip(ing[d], W)), 1 + sum(ing[d])),
}
p3 = {}
for k, s in scores.items():
    top = rank(s)[:3]
    p3[k] = Fr(sum(rel[d] > 0 for d in top), 3)
    print(f"  Q4 Score_{k}: top3={top} P@3={p3[k]}")
mx = max(p3.values())
answer("B2.Q4", "Score_" + ",".join(k for k, v in p3.items() if v == mx) + " only (option 4)")

p = [Fr(8, 10), Fr(6, 10), Fr(4, 10), Fr(2, 10), Fr(1, 10)]
top5 = rank(scores["A"])[:5]
pir = sum(pi_ for pi_, d in zip(p, top5) if rel[d] > 0) / R
print(f"  Q5 Score_A top5={top5}; PI-Recall@5 = {pir} (exact)")
answer("B2.Q5", floor(100 * pir))


# =============================================================================
header("B3 Convolution")


def conv(x, h, pad=0, padval=0, stride=1):
    xp = [padval] * pad + list(x) + [padval] * pad
    k = len(h)
    # y_i = sum_j h_j x_{i+k-j}  (1-based)  ==  reversed kernel slid along x
    return [sum(h[j] * xp[i + k - 1 - j] for j in range(k)) for i in range(0, len(xp) - k + 1, stride)]


assert conv([2, 4, 6, 8], [1, -1]) == [2, 2, 2]  # worked example in the paper
y1 = conv([1, 3, 2, 4], [2, 1], pad=1, padval=2, stride=2)
print(f"  Q1 output = {y1}   (without reversing: {[2 * a + 1 * b for a, b in zip([2, 3, 4], [1, 2, 2])]})")
answer("B3.Q1", f"A {y1}")

rng = np.random.default_rng(4)
const_sigs = [[c] * 5 for c in (-3, 0, 2, 7)]
lin_sigs = [[int(a) + int(v) * i for i in range(6)] for a, v in rng.integers(-9, 10, (20, 2))]

print("  Q2 (S = sum y; need S(const)=0, |S(x)| small, |S(z)| large)")
x2, z2 = [2, 4, 6, 8, 10], [2, 6, 3, 10, 4]
k2 = {"A": [1, 0, -1], "B": [2, -3, 2], "C": [1, 1, -2], "D": [1, -2, 1], "E": [0, -1, 1], "F": [-2, 4, -2]}
ok2 = []
for k, h in k2.items():
    Sc = [sum(conv(s, h)) for s in const_sigs]
    Sx, Sz = sum(conv(x2, h)), sum(conv(z2, h))
    S_ramp = max(abs(sum(conv([a + v * i for i in range(5)], h))) for a in (0, 2) for v in (1, 2, 5))
    good = all(v == 0 for v in Sc) and abs(Sz) > S_ramp
    print(f"    {k} {h}: S(const)={Sc}, S(x)={Sx}, S(z)={Sz}, max|S| over smooth ramps={S_ramp} -> {'OK' if good else 'no'}")
    if good:
        ok2.append(k)
answer("B3.Q2", ",".join(ok2))

print("  Q3 (S=0 for constant velocity, S(x)<0 decelerating, S(w)>0 accelerating)")
x3, w3_ = [1, 5, 8, 10, 11], [1, 2, 4, 7, 11]
k3 = {"A": [-1, 0, 1], "B": [-1, 2, -1], "C": [1, -1, 0], "D": [0, 1, -2], "E": [1, -2, 1], "F": [3, -6, 3]}
ok3 = []
for k, h in k3.items():
    cv = all(sum(conv(s, h)) == 0 for s in lin_sigs + const_sigs)
    Sx, Sw = sum(conv(x3, h)), sum(conv(w3_, h))
    good = cv and Sx < 0 and Sw > 0
    print(f"    {k} {h}: const-velocity->0? {cv}, S(x)={Sx}, S(w)={Sw} -> {'OK' if good else 'no'}")
    if good:
        ok3.append(k)
answer("B3.Q3", ",".join(ok3))

print("  Q4 (S_abs = 0 for constants and smooth z, large for spike x)")
x4, z4 = [1, 2, 8, 2, 1, 2], [1, 3, 5, 7, 9, 11]
k4 = {"A": [1, 1, -2], "B": [-1, 0, 1], "C": [2, -3, 1], "D": [1, -1, 0], "E": [-1, 2, -1], "F": [1, -2, 1]}
ok4 = []
for k, h in k4.items():
    sab = lambda s: sum(abs(v) for v in conv(s, h))
    zero_ok = all(sab(s) == 0 for s in const_sigs + [z4] + lin_sigs)
    good = zero_ok and sab(x4) > 0
    print(f"    {k} {h}: S_abs(z)={sab(z4)}, S_abs(x)={sab(x4)}, zero on all lines? {zero_ok} -> {'OK' if good else 'no'}")
    if good:
        ok4.append(k)
answer("B3.Q4", ",".join(ok4))

print("  Q5 (y = 0 for every symmetric length-4 signal; y(z) != 0)")
k5 = {"A": [1, 1, 1, -1], "B": [1, -1, 1, -1], "C": [-1, 2, 1, 1], "D": [2, 1, -1, -2], "E": [1, -1, -1, 0], "F": [1, 0, 0, -1]}
sym = [[a, b_, b_, a] for a, b_ in rng.integers(-9, 10, (50, 2))] + [[2, 5, 5, 2]]
ok5 = []
for k, h in k5.items():
    zero_sym = all(conv(s, h) == [0] for s in sym)
    yz = conv([1, 2, 3, -1], h)[0]
    good = zero_sym and yz != 0
    print(f"    {k} {h}: zero on all symmetric? {zero_sym}, y(z)={yz} -> {'OK' if good else 'no'}")
    if good:
        ok5.append(k)
# blind spot: every 4-tap kernel has an asymmetric signal with y=0
for k in ok5:
    h = k5[k]
    blind = next(s for s in product(range(-2, 3), repeat=4)
                 if list(s) != list(s)[::-1] and conv(list(s), h) == [0])
    print(f"    note: {k} also outputs 0 on the asymmetric signal {list(blind)}")
answer("B3.Q5", ",".join(ok5))


# =============================================================================
header("B4 Model Compression")
X = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 1]], float)
y = np.array([1, 0, 0, 0, 0, 1])
known = {"A": {0: 2, 2: -1, 3: -1, 4: -1}, "B": {0: 3, 1: -5, 3: -1, 5: 1}}
res = {}
for nm, kv in known.items():
    rows = sorted(kv)
    w = np.linalg.solve(X[rows], np.array([kv[r] for r in rows], float))
    s = X @ w
    acc = Fr(int(np.sum((s > 0).astype(int) == y)), 6)
    res[nm] = (acc, w)
    print(f"  Q1 option {nm}: w={w}, s={s}, accuracy={acc}")
wstar = max(res.values(), key=lambda t: t[0])[1]
answer("B4.Q1", floor(round(float(wstar @ wstar), 9)))

X7 = np.array([[-1, 0, 0, 0, 0, 0, 3], [0, -1, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, -2],
               [0, 0, 0, -1, 0, 0, 6], [0, 0, 0, 0, -1, 0, 7], [0, 0, 0, 0, 0, 1, -6],
               [1, 1, 1, 1, 1, 5, -9]])
w7 = np.array([-1, -1, -1, -1, -1, 1, 0])
y7 = np.array([1, 1, 1, 1, 1, 1, 0])
accs = {}
for j, k in combinations(range(7), 2):
    w = w7.copy(); w[[j, k]] = 0
    accs[(j + 1, k + 1)] = int(np.sum(((X7 @ w) > 0).astype(int) == y7))
bestacc = max(accs.values())
winners = [pr for pr, a in accs.items() if a == bestacc]
print(f"  Q2 unpruned accuracy {int(np.sum(((X7 @ w7) > 0).astype(int) == y7))}/7; best pruned {bestacc}/7 by {winners}")
jk = winners[0]
answer("B4.Q2", sum(jk), f"pair {jk}")

w = w7.copy(); w[[jk[0] - 1, jk[1] - 1]] = 0
s = X7 @ w
accb = {bb: int(np.sum(((s + bb) > 0).astype(int) == y7)) for bb in range(-5, 6)}
print(f"  Q3 pruned scores {s.tolist()}; accuracy by b: {accb}")
mx = max(accb.values())
bstar = max(bb for bb, a in accb.items() if a == mx)   # largest b among ties
answer("B4.Q3", sum(jk) * abs(bstar), f"b*={bstar}")


# =============================================================================
header("SUMMARY")
for label, value in ANSWERS:
    print(f"  {label:<7} {value}")
