"""
Numerical checks for SOLUTIONS.md: INAIO 2026 Stage 1 paper (18 Jan 2026).

Run it with:   python3 -I verify.py

Each section recomputes one question from the numbers printed in the paper,
prints the intermediate values that the worked solutions quote, and ends with
check(...) lines that compare the result against the answer table.
A "MISMATCH" line means SOLUTIONS.md and this script disagree. The script
exits with status 1 if any check fails.

Only the standard library is used. Floors near an integer are computed with
exact fractions where floating-point rounding could flip them
(e.g. 100 * (1 - 0.8) = 19.999... in floating point).
"""

import itertools
import math
import sys
from fractions import Fraction as Fr

FAILS = []


def check(label, got, expected):
    ok = got == expected
    print(f"  [{'OK' if ok else 'MISMATCH'}] {label}: got {got!r}, expected {expected!r}")
    if not ok:
        FAILS.append(label)


def header(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# ======================================================================
# SECTION A1
# ======================================================================

# ----------------------------------------------------------------------
header("A1 Smart Student Search: Jaro / edit distance examples and option checks")
# ----------------------------------------------------------------------
# The paper's "Jaro Distance" is really a similarity: 1 means identical.
# Matching window: floor(max(|x|,|y|)/2) - 1.  t = half the number of
# matched characters that are out of order.


def jaro(x, y):
    if x == "" and y == "":
        return 1.0
    window = max(len(x), len(y)) // 2 - 1
    window = max(window, 0)
    x_hit = [False] * len(x)
    y_hit = [False] * len(y)
    m = 0
    for i, ch in enumerate(x):
        lo, hi = max(0, i - window), min(len(y), i + window + 1)
        for j in range(lo, hi):
            if not y_hit[j] and y[j] == ch:
                x_hit[i] = y_hit[j] = True
                m += 1
                break
    if m == 0:
        return 0.0
    xs = [c for c, h in zip(x, x_hit) if h]
    ys = [c for c, h in zip(y, y_hit) if h]
    t = sum(a != b for a, b in zip(xs, ys)) / 2
    return (m / len(x) + m / len(y) + (m - t) / m) / 3


def edit_distance(x, y):
    prev = list(range(len(y) + 1))
    for i in range(1, len(x) + 1):
        cur = [i] + [0] * len(y)
        for j in range(1, len(y) + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (x[i - 1] != y[j - 1]))
        prev = cur
    return prev[-1]


print("  JD(Aryan, Arya)   =", round(jaro("Aryan", "Arya"), 4))
print("  JD(MARTHA, MARHTA)=", round(jaro("MARTHA", "MARHTA"), 4))
print("  JD(9C, 9D)        =", round(jaro("9C", "9D"), 4))
print("  JD(Shah, Sha)     =", round(jaro("Shah", "Sha"), 4))
print("  ED(Aryan, Arjun)  =", edit_distance("Aryan", "Arjun"))
check("JD(Aryan,Arya) = 14/15", round(jaro("Aryan", "Arya"), 6), round(14 / 15, 6))
check("JD(MARTHA,MARHTA) = 17/18", round(jaro("MARTHA", "MARHTA"), 6), round(17 / 18, 6))
check("JD(9C,9D) = 2/3 (so option B gives a non-zero score across sections)",
      round(jaro("9C", "9D"), 6), round(2 / 3, 6))
check("ED(Aryan,Arjun) = 2", edit_distance("Aryan", "Arjun"), 2)

ind = lambda a, b: 1 if a == b else 0
sims = {
    "A": lambda s, t: ind(s[0], t[0]) * (jaro(s[1], t[1]) + jaro(s[2], t[2])) / 2,
    "B": lambda s, t: jaro(s[0], t[0]) * math.exp(-(1 - jaro(s[1], t[1])) - 2 * (1 - jaro(s[2], t[2]))),
    "C": lambda s, t: ind(s[0], t[0]) * math.exp(-2 * (1 - jaro(s[1], t[1])) - (1 - jaro(s[2], t[2]))),
    "D": lambda s, t: ind(s[0], t[0]) * math.exp(-edit_distance(s[1], t[1])) * math.exp(-2 * edit_distance(s[2], t[2])),
    "E": lambda s, t: ind(s[0], t[0]) * (2 * len(t[1]) * jaro(s[1], t[1]) + len(t[2]) * jaro(s[2], t[2]))
                      / (2 * len(t[1]) + len(t[2])),
    "F": lambda s, t: ind(s[0], t[0]) * (2 * jaro(s[1], t[1]) + jaro(s[2], t[2])),
}
base = ("9C", "Aryan", "Shah")
typo_first = ("9C", "Arya", "Shah")    # first name missing one letter
typo_last = ("9C", "Aryan", "Sha")     # last name missing one letter (the symmetry counterexample for E)
other_sec = ("9D", "Aryan", "Shah")    # same names, different section
print("  option | Sim(s,s) | other section | first-name typo | last-name typo | Sim(s,t) vs Sim(t,s)")
for k, f in sims.items():
    print(f"    {k}    | {f(base, base):.4f}   | {f(base, other_sec):.4f}        | "
          f"{f(base, typo_first):.4f}          | {f(base, typo_last):.4f}         | "
          f"{f(base, typo_last):.4f} vs {f(typo_last, base):.4f}")
# Rule 4 needs equal-sized mistakes. Use a 1-letter substitution in a 5-letter field for both.
f5a, f5b = "Aryan", "Aryun"
s4 = ("9C", f5a, "Kumar")
t_first = ("9C", f5b, "Kumar")
t_last = ("9C", f5a, "Kumur")
print("  equal-size typo test (one substitution in a 5-letter field):")
for k in "ACDE":
    print(f"    {k}: first-name typo -> {sims[k](s4, t_first):.4f}, last-name typo -> {sims[k](s4, t_last):.4f}")
check("only option C satisfies all five rules (E fails symmetry: 0.9808 vs 0.9762)",
      (round(sims["E"](base, typo_last), 4), round(sims["E"](typo_last, base), 4)), (0.9808, 0.9762))
check("option F can exceed 1 (identical IDs give 3)", sims["F"](base, base), 3.0)

# ----------------------------------------------------------------------
header("A1 Recursive V-67 Outbreak")
# ----------------------------------------------------------------------
N, M = 8, 8
print(f"  day 0: N={N}, M={M}")
for day in range(3):
    X = 2 * N + 4 * M
    N, M = N / 2 + X / 2, M / 2 + X / 4    # half recover, plus new arrivals
    print(f"  day {day + 1}: X(prev)={X:g}, N={N:g}, M={M:g}")
check("N3 + M3", N + M, 281.0)

# ----------------------------------------------------------------------
header("A1 Pikachu's Path to Victory (knight on 5x5, (0,0) -> (4,4))")
# ----------------------------------------------------------------------
moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
best = 0


def dfs(p, vis):
    global best
    if p == (4, 4):
        best = max(best, len(vis))
        return
    for dx, dy in moves:
        q = (p[0] + dx, p[1] + dy)
        if 0 <= q[0] < 5 and 0 <= q[1] < 5 and q not in vis:
            vis.add(q)
            dfs(q, vis)
            vis.remove(q)


dfs((0, 0), {(0, 0)})
even = sum((r + c) % 2 == 0 for r in range(5) for c in range(5))
print(f"  squares with r+c even: {even}, odd: {25 - even}")
check("max pads (exhaustive DFS)", best, 25)

# The explicit 25-pad path printed in SOLUTIONS.md (step number at each square).
grid = [
    [1, 20, 15, 8, 3],
    [14, 9, 2, 21, 16],
    [19, 22, 13, 4, 7],
    [10, 5, 24, 17, 12],
    [23, 18, 11, 6, 25],
]
pos = {grid[r][c]: (r, c) for r in range(5) for c in range(5)}
legal = all(
    sorted((abs(pos[i + 1][0] - pos[i][0]), abs(pos[i + 1][1] - pos[i][1]))) == [1, 2]
    for i in range(1, 25)
)
check("printed path: every step is a knight move, uses 1..25 once, starts (0,0), ends (4,4)",
      (legal, sorted(pos) == list(range(1, 26)), pos[1], pos[25]), (True, True, (0, 0), (4, 4)))

# ======================================================================
# SECTION A2
# ======================================================================

# ----------------------------------------------------------------------
header("A2 Phulera Godown Showdown")
# ----------------------------------------------------------------------
xs = [40, 120, 200, 80]
ys = [180, 80, 140, 20]
Gs = (100, 110)                      # midpoint of the median ranges [80,120] x [80,140]
Gp = (sum(xs) / 4, sum(ys) / 4)      # means (110, 105)
D = math.dist(Gs, Gp)
print(f"  Gs={Gs}, Gp={Gp}, D={D:.4f}")
# Extra: brute-force both argmins on a fine grid to confirm the formulas.
l1 = lambda u, pts: sum(abs(u - p) for p in pts)
xmin = min(l1(u, xs) for u in range(0, 241))
ymin = min(l1(u, ys) for u in range(0, 241))
xr = [u for u in range(0, 241) if l1(u, xs) == xmin]
yr = [u for u in range(0, 241) if l1(u, ys) == ymin]
print(f"  L1 minimisers: x in [{xr[0]},{xr[-1]}], y in [{yr[0]},{yr[-1]}]")
kl = lambda u, pts: sum(p * math.log(p / u) + (u - p) for p in pts)
kx = min((kl(u / 10, xs), u / 10) for u in range(1, 2400))[1]
ky = min((kl(u / 10, ys), u / 10) for u in range(1, 2400))[1]
print(f"  generalised-KL minimiser (grid step 0.1): ({kx}, {ky})")
for u in (100, 110, 120):
    print(f"    x-part of KL objective at u={u}: {kl(u, xs):.3f}")
check("L1 ranges", (xr[0], xr[-1], yr[0], yr[-1]), (80, 120, 80, 140))
check("KL argmin", (kx, ky), (110.0, 105.0))
check("floor(D)", math.floor(D), 11)

# ----------------------------------------------------------------------
header("A2 Blind Board Gambit")
# ----------------------------------------------------------------------


def pw(R, S):
    """P(player rated R beats player rated S)."""
    return 1 / (1 + 10 ** ((S - R) / 400))


G = {"A": 2000, "B": 1800, "C": 1600}
An = {"X": 1900, "Y": 1700, "Z": 1500}
for d in (-500, -300, -100, 100, 300):
    print(f"  P(win) with rating difference {d:+d}: {pw(d, 0):.4f}")


def match(g, a):
    """P(Anand wins >= 2 of 3 boards) when Gukesh plays order g and Anand plays order a."""
    ps = [pw(An[a[i]], G[g[i]]) for i in range(3)]
    tot = 0
    for res in itertools.product([0, 1], repeat=3):
        pr = 1
        for r, p in zip(res, ps):
            pr *= p if r else 1 - p
        if sum(res) >= 2:
            tot += pr
    return tot


gorders = [o for o in itertools.permutations("ABC") if o != ("A", "B", "C")]
scores = {a: sum(match(g, a) for g in gorders) / 5 for a in itertools.permutations("XYZ")}
print("  Anand order -> average over Gukesh's 5 non-canonical orders | P(win) vs canonical (A,B,C)")
for a, s in sorted(scores.items(), key=lambda kv: -kv[1]):
    print(f"    {a}: {s:.4f} | {match(('A', 'B', 'C'), a):.4f}")
abest = max(scores, key=scores.get)
# Extra: the symmetry shortcut. Summed over ALL 6 Gukesh orders, every Anand order
# meets every possible pairing exactly once, so the total is the same constant.
totals = {a: sum(match(g, a) for g in itertools.permutations("ABC")) for a in itertools.permutations("XYZ")}
print(f"  sum over all 6 Gukesh orders (should be constant): {sorted(round(v, 10) for v in set(totals.values()))}")
check("all-6 total is the same for every Anand order", len({round(v, 10) for v in totals.values()}), 1)
check("best order = the one that does WORST against (A,B,C)",
      abest, min(itertools.permutations("XYZ"), key=lambda a: match(("A", "B", "C"), a)))
p = match(("C", "A", "B"), abest)
print(f"  Anand plays {abest}; actual Gukesh order (C,A,B); p = {p:.4f}")
check("Anand's choice", abest, ("Y", "Z", "X"))
check("floor(100 p)", math.floor(100 * p), 43)

# ----------------------------------------------------------------------
header("A2 Crude Curve Forecast")
# ----------------------------------------------------------------------
# Read off the graph: P(3)=34, P(9)=14, P(15)=42 (peaks 3,15,27 -> period 12),
# jump 40 -> 60 at t=30, P(48)=72, trough ~56 near t=57, P(60) ~ 70.
T = 15 - 3
B = Fr(42 - 34, 15 - 3)                 # P(15) - P(3) = 12B
A = Fr(34 + 14, 2) - 6 * B              # P(3) + P(9) = 2A + 12B
E = 34 - A - 3 * B
Dj = 60 - 40
print(f"  T={T}, B={B}, A={A}, E={E}, D={Dj}")
# C from P(60) = A + 60B + C(1 - e^-12) + D + E sin(10 pi)  ~ 80 + C  and graph value ~70
C_est = 70 - (float(A) + 60 * float(B) + Dj)
print(f"  C from P(60)~70: {C_est:.2f}")
A, B, C, D, E = 20, 2 / 3, -10, 20, 12
P = lambda t: A + B * t + C * (1 - math.exp(-(t - 48))) * (t >= 48) + D * (t >= 30) + E * math.sin(2 * math.pi * t / 12)
print("  model vs graph:", [(t, round(P(t), 2)) for t in (0, 3, 9, 15, 21, 27, 29.999, 30, 48, 51, 57, 60)])
print(f"  P(75) = {P(75)!r}  (just ABOVE 92 because -10(1 - e^-27) = -10 + tiny)")
check("floor(P(75))", math.floor(P(75)), 92)

# ----------------------------------------------------------------------
header("A2 Catalyst Constraint")
# ----------------------------------------------------------------------
best = max(((16 * ca - 2 * ca * ca) + (24 * (5 - ca) - 3 * (5 - ca) ** 2), ca) for ca in [i / 1000 for i in range(5001)])
print(f"  grid search (step 0.001): total {best[0]:.4f} at c_A = {best[1]}")
# Exact: substitute c_B = 5 - c: total = -5c^2 + 22c + 45, vertex at c = 22/10.
c = Fr(22, 10)
tot = -5 * c * c + 22 * c + 45
print(f"  exact vertex: c_A = {c} , c_B = {5 - c}, total = {tot} = {float(tot)}")
print(f"  marginal gains at optimum: {16 - 4 * c} and {24 - 6 * (5 - c)}; unconstrained optimum needs 4 + 4 = 8 > 5")
check("floor(total)", math.floor(tot), 69)

# ----------------------------------------------------------------------
header("A2 Pit-Stop Paradox")
# ----------------------------------------------------------------------
nr = [(0.45, 0.25), (0.30, 0.80), (0.10, 0.10), (0.15, 0.55)]   # (P(strategy), P(H wins)) no rain
r = [(0.05, 0.50), (0.10, 0.05), (0.10, 0.95), (0.75, 0.60)]    # rain
ph = 0.5 * sum(a * b for a, b in nr) + 0.5 * sum(a * b for a, b in r)
pp = 0.5 * sum(a * b for a, b in nr[1:]) + 0.5 * sum(a * b for a, b in r[1:])
print(f"  P(H wins) = {ph:.4f}, P(>=1 pitted and H wins) = {pp:.5f}, ratio = {pp / ph:.4f}")
# Extra: natural frequencies with 4000 imaginary races (all counts are whole numbers).
races = {"no rain": 2000, "rain": 2000}
wins_total = wins_neither = 0
for name, tab in (("no rain", nr), ("rain", r)):
    counts = [round(races[name] * a) for a, _ in tab]
    wins = [round(n * b) for n, (_, b) in zip(counts, tab)]
    print(f"    {name}: strategies {counts}, H wins {wins}")
    wins_total += sum(wins)
    wins_neither += wins[0]
print(f"    H wins {wins_total}, of which 'neither pitted' {wins_neither}")
check("floor(100 * ratio)", math.floor(100 * Fr(wins_total - wins_neither, wins_total)), 86)

# ======================================================================
# SECTION B1  Code Triage
# ======================================================================
header("B1 Code Triage")
# Counts out of 1000 patients, rows = ACTUAL class, columns = PREDICTED class.
cm = {(1, 1): 510, (1, 2): 70, (1, 3): 20,
      (2, 1): 29, (2, 2): 210, (2, 3): 61,
      (3, 1): 10, (3, 2): 10, (3, 3): 80}
ben = {(1, 1): 100, (1, 2): 50, (1, 3): 0,
       (2, 1): 0, (2, 2): 100, (2, 3): 50,
       (3, 1): 0, (3, 2): 50, (3, 3): 200}
for c, n in [(1, 600), (2, 300), (3, 100)]:
    tp = cm[(c, c)]
    fp = sum(cm[(a, c)] for a in (1, 2, 3) if a != c)
    print(f"  class {c}: sens {tp / n:.4f}, spec {(1000 - n - fp) / (1000 - n):.4f}")
# Extra: the class-2 split is pinned down only up to rounding.
# Spec_1 = 0.90 exactly gives (2->1, 2->3) = (30, 60); Spec_3 = 0.91 exactly gives (29, 61).
for a21, a23 in ((29, 61), (30, 60)):
    cm2 = dict(cm)
    cm2[(2, 1)], cm2[(2, 3)] = a21, a23
    s1 = Fr(400 - a21 - 10, 400)
    s3 = Fr(900 - 20 - a23, 900)
    benefit = Fr(sum(cm2[k] * ben[k] for k in cm2), 1000)
    print(f"  split {a21}/{a23}: spec1 {float(s1):.4f}, spec3 {float(s3):.4f}, benefit {float(benefit)}")
    check(f"Q7 floor(benefit) with split {a21}/{a23}", math.floor(benefit), 95)
print("  triage benefit (29/61 split):", sum(cm[k] * ben[k] for k in cm) / 1000)
check("Q1 floor(100 (1 - sens3))", math.floor(100 * (1 - Fr(80, 100))), 20)
check("Q2 floor(100 sens1)", math.floor(100 * Fr(510, 600)), 85)
flagged = {}
for nm, f, t in [("A", .02, .6), ("B", .04, .72), ("C", .05, .78), ("D", .08, .84), ("E", .12, .88), ("F", .2, .92)]:
    flagged[nm] = (round(20 * t + 180 * f, 4), t)
    print(f"  ICU flagged/day at {nm}: 20*{t} + 180*{f} = {flagged[nm][0]}")
check("Q3 best point with <= 25 flagged/day",
      max((t, nm) for nm, (fl, t) in flagged.items() if fl <= 25)[1], "C")

# ======================================================================
# SECTION B2  WonkaRank
# ======================================================================
header("B2 WonkaRank")
# ingredient vector (C, H, K, M) and relevance
Dd = {1: (1, 1, 0, 0, 10), 2: (1, 1, 1, 0, 0), 3: (1, 0, 1, 0, 0), 4: (0, 1, 0, 0, 0), 5: (1, 1, 0, 1, 3),
      6: (0, 0, 1, 1, 0), 7: (1, 0, 0, 0, 0), 8: (1, 1, 0, 0, 5), 9: (0, 1, 1, 0, 3)}
relevant = {i for i in Dd if Dd[i][4] > 0}
R = len(relevant)

# Q1
bought = [2, 3, 5, 6, 7, 8]
rec5 = Fr(len(relevant & set(bought[:5])), R)
check("Q1 floor(100 Recall@5)", math.floor(100 * rec5), 25)

# Q2 (extra): Strategy A vs B
sA = {i: 2 if Dd[i][0] and Dd[i][1] else 0 for i in Dd}
sB = {i: 2 if Dd[i][0] and Dd[i][1] else (1 if Dd[i][0] or Dd[i][1] else 0) for i in Dd}
pr = {}
for name, s in (("A", sA), ("B", sB)):
    ret = {i for i in Dd if s[i] > 0}
    hit = len(ret & relevant)
    pr[name] = (Fr(hit, len(ret)), Fr(hit, R))
    print(f"  Strategy {name}, retrieved = score > 0: {sorted(ret)}  P = {hit}/{len(ret)}, R = {hit}/{R}")
rankA = sorted(Dd, key=lambda i: (-sA[i], i))
rankB = sorted(Dd, key=lambda i: (-sB[i], i))
print(f"  ranked (ID tie-break): A {rankA}\n                          B {rankB}")
for k in range(1, 10):
    ha = len(set(rankA[:k]) & relevant)
    hb = len(set(rankB[:k]) & relevant)
    tag = "same" if ha == hb else ("B better on both" if hb > ha else "A better")
    print(f"    k={k}: relevant in top-k  A {ha}, B {hb}  ({tag})")
check("Q2 (score>0 reading): B recall up AND precision down (option 1)",
      (pr["B"][1] > pr["A"][1], pr["B"][0] < pr["A"][0]), (True, True))

# Q3
dcg = lambda L: sum(Dd[d][4] / math.log2(i + 2) for i, d in enumerate(L))
print(f"  position weights 1/log2(i+1): {[round(1 / math.log2(i + 1), 4) for i in range(1, 5)]}")
print(f"  DCG A [5,1,8,2] = {dcg([5, 1, 8, 2]):.4f},  DCG B [8,5,1,2] = {dcg([8, 5, 1, 2]):.4f}")
check("Q3 DCG(B) > DCG(A)", dcg([8, 5, 1, 2]) > dcg([5, 1, 8, 2]), True)

# Q4
W = (3, 3, 1, 1)
fs = {"A": lambda d: sum(a * b for a, b in zip(d, W)),
      "B": lambda d: sum(min(1, a) * min(1, b) for a, b in zip(d, W)),
      "C": lambda d: sum(a * b for a, b in zip(d, W)) - sum(d),
      "D": lambda d: sum(a * b for a, b in zip(d, W)) / (1 + sum(d))}
p2 = {}
for k, f in fs.items():
    print(f"  Score_{k}: " + ", ".join(f"D{i}={f(Dd[i][:4]):.3g}" for i in Dd))
    rank = sorted(Dd, key=lambda i: (-f(Dd[i][:4]), i))
    p2[k] = sum(Dd[i][4] > 0 for i in rank[:2]) / 2
    print(f"    top-2 {rank[:2]}, P@2 = {p2[k]}")
check("Q4 functions with the highest P@2", [k for k in p2 if p2[k] == max(p2.values())], ["D"])

# Q5
rank = sorted(Dd, key=lambda i: (-fs["A"](Dd[i][:4]), i))
pv = [.5, .5, .3, .3, .2]
pir = Fr(sum(Fr(str(p)) * (Dd[i][4] > 0) for p, i in zip(pv, rank[:5])), R)
print(f"  Score_A ranking {rank}; top-5 {rank[:5]}; PI-Recall@5 = {pir} = {float(pir)}")
check("Q5 floor(100 PI-Recall@5)", math.floor(100 * pir), 27)

# ======================================================================
# SECTION B3  Convolution
# ======================================================================
header("B3 Pattern Pursuit (convolution)")


def conv(x, h, stride=1):
    """Paper's definition: y_i = sum_j h_j * x_{i+k-j} (kernel is reversed)."""
    k = len(h)
    return [sum(h[j] * x[i + k - 1 - j] for j in range(k)) for i in range(0, len(x) - k + 1, stride)]


q1 = conv([3, 2, 1, 3, 4, 3], [1, 2], 2)
print(f"  Q1: stride-1 output {conv([3, 2, 1, 3, 4, 3], [1, 2])}, stride-2 output {q1}")
check("Q1", q1, [8, 5, 11])

print("  Q2/Q3 kernels: S(x smooth), S(z fluct) | S(x accel), S(w decel) | S(constant)")
for h in ([1, 1, 1], [-1, 0, 1], [1, -2, 1], [-1, 1, 0], [0, 1, 0], [1, 0, -1], [0, 1, -1]):
    print(f"    {h}: {sum(conv([2, 4, 6, 8, 10], h))}, {sum(conv([2, 6, 3, 10, 4], h))} | "
          f"{sum(conv([1, 2, 4, 7, 11], h))}, {sum(conv([1, 5, 8, 10, 11], h))} | {sum(conv([5] * 5, h))}")
tel = lambda x: (x[-1] - x[-2]) - (x[1] - x[0])
check("Q2 telescoped S for [1,-2,1] on x and z", (tel([2, 4, 6, 8, 10]), tel([2, 6, 3, 10, 4])), (0, -10))
check("Q3 telescoped S for [1,-2,1] on x and w", (tel([1, 2, 4, 7, 11]), tel([1, 5, 8, 10, 11])), (3, -3))
print(f"  limitation: S for [1,-2,1] on the very jumpy [2,10,2,10,2,10] = {sum(conv([2, 10, 2, 10, 2, 10], [1, -2, 1]))}")

print("  Q4 kernels: S_abs(x spike), S_abs(z smooth), S_abs(constant), plain S(x spike)")
for h in ([1, 1, 1], [-1, 2, -1], [-1, 0, 1], [0, 1, 0], [1, -1, 1], [0, 1, -1]):
    y = conv([2, 3, 8, 3, 2, 3], h)
    print(f"    {h}: {sum(map(abs, y))}, {sum(map(abs, conv([2, 3, 4, 5, 6, 7], h)))}, "
          f"{sum(map(abs, conv([5] * 6, h)))}, {sum(y)}   y(x) = {y}")
check("Q4 [-1,2,-1]: S_abs spike 20, smooth 0; plain S would be 0",
      (sum(map(abs, conv([2, 3, 8, 3, 2, 3], [-1, 2, -1]))), sum(map(abs, conv([2, 3, 4, 5, 6, 7], [-1, 2, -1]))),
       sum(conv([2, 3, 8, 3, 2, 3], [-1, 2, -1]))), (20, 0, 0))

print("  Q5 kernels: y(x symmetric), y(z asymmetric), h1+h4, h2+h3")
ok5 = []
for name, h in zip("ABCDEF", ([-1, 2, -1, 0], [1, -1, -1, 1], [1, -2, 1, 0], [1, -1, 1, -1], [1, -2, 0, -1], [1, 0, -1, 0])):
    print(f"    {name} {h}: {conv([2, 5, 5, 2], h)}, {conv([1, 2, 3, -1], h)}, {h[0] + h[3]}, {h[1] + h[2]}")
    if h[0] + h[3] == 0 and h[1] + h[2] == 0:
        ok5.append(name)
check("Q5 kernels that send EVERY symmetric signal to 0", ok5, ["D"])
print(f"  limitation: D on the asymmetric [0,0,1,1] gives {conv([0, 0, 1, 1], [1, -1, 1, -1])}")

# ======================================================================
# SECTION B4  Model Compression
# ======================================================================
header("B4 Model Compression")
# Q1
X6 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 1]]
y6 = [1, 0, 1, 0, 1, 1]
wA = (2, -1, 1, -1)   # rows 1,3,4 give w1,w3,w4; row 5 gives w1+w2 = 1
wB = (3, -5, -1, -1)  # rows 1,2,4 give w1,w2,w4; row 6 gives w1+w3+w4 = 1
for name, w, known in (("A", wA, {1: 2, 3: 1, 4: -1, 5: 1}), ("B", wB, {1: 3, 2: -5, 4: -1, 6: 1})):
    s = [sum(a * b for a, b in zip(row, w)) for row in X6]
    agree = all(s[i - 1] == v for i, v in known.items())
    acc = sum((si > 0) == bool(t) for si, t in zip(s, y6))
    print(f"  w^{name} = {w}: full scores {s}, matches given values: {agree}, accuracy {acc}/6, l1 = {sum(map(abs, w))}")
check("Q1 floor(||w*||_1)", sum(map(abs, wA)), 5)

# Q2 / Q3
X = [[-1, 0, 0, 0, 0, 0, 3], [0, -1, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, -2], [0, 0, 0, -1, 0, 0, 6],
     [0, 0, 0, 0, -1, 0, 7], [0, 0, 0, 0, 0, 1, -6], [1, 1, 1, 1, 1, 5, -9]]
w = [-1, -1, -1, -1, -1, 1, 0]
y = [1, 1, 1, 1, 1, 1, 0]


def acc(w, b=0):
    return sum((sum(a * c for a, c in zip(r, w)) + b > 0) == bool(t) for r, t in zip(X, y))


print(f"  unpruned scores {[sum(a * c for a, c in zip(r, w)) for r in X]}, accuracy {acc(w)}/7")
res = []
for j, k in itertools.combinations(range(7), 2):
    w2 = w[:]
    w2[j] = w2[k] = 0
    res.append((acc(w2), (j + 1) * (k + 1), (j + 1, k + 1)))
res.sort(reverse=True)
print("  best pruning pairs (accuracy, product, pair):", res[:4])
check("Q2 unique best pair", (res[0][2], res[0][0], res[1][0] < res[0][0]), ((6, 7), 6, True))
w2 = w[:]
w2[5] = w2[6] = 0
print(f"  pruned scores {[sum(a * c for a, c in zip(r, w2)) for r in X]}")
bias = [(b, acc(w2, b)) for b in range(-3, 4)]
print("  accuracy by bias b:", bias)
top = max(a for _, a in bias)
bstar = min((abs(b), b) for b, a in bias if a == top)[1]
check("Q3 b*", bstar, 1)
check("Q3 j*k* + |b*|", res[0][1] + abs(bstar), 43)

# ----------------------------------------------------------------------
print()
if FAILS:
    print(f"{len(FAILS)} check(s) FAILED: {FAILS}")
    sys.exit(1)
print("All checks passed.")
