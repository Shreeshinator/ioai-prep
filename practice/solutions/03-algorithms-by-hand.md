# Set 03 solutions: Algorithms by hand

> Make a real attempt first (10–15 min per problem). Then open **one** hint, try again, and only then open the next. If a word in a problem is new to you, open Hint 1 straight away: it defines the terms, and definitions are not something to struggle with. You can check a final answer without spoilers in `notebooks/03_algorithms.ipynb`.

---

### 3.1 Which distance?

<details><summary>Hint 1: understand the question</summary>

**k-NN** ("k nearest neighbours") with k = 3 means: find the 3 labelled points closest to the query and let them vote. The query is (0, 0), so for each point Δx and Δy are just its own coordinates. Example for (3, 0): Euclidean √(3² + 0²) = 3, and Manhattan |3| + |0| = 3.

**Euclidean** distance is the straight-line distance, as a bird flies. **Manhattan** distance is the distance you'd walk on a city grid, where you can only move along the streets (horizontally and vertically).

What does "the 3 nearest" mean if the 3rd and 4th points are exactly the same distance away?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M1 (Read the definition, not your memory)**. The two distances are different definitions, so they can rank the points in a different order. Make one table with a row per point: Euclidean distance, Manhattan distance, label. Then sort by each distance separately.

For any tie, ask: *could* the tie-break change the vote? Try it both ways.
</details>

<details><summary>Hint 3: set it up</summary>

(2, 2): Euclidean √8 ≈ 2.83, Manhattan 2 + 2 = 4. Fill in the rest.

| Point | Euclidean | Manhattan | Label |
|---|---|---|---|
| (3, 0) | 3 | 3 | red |
| (2, 2) | 2.83 | 4 | blue |
| (0, −3) | ? | ? | red |
| (−2, 2) | ? | ? | blue |
| (5, 5) | ? | ? | blue |
</details>

<details><summary>Answer</summary>

(a) **blue** (b) **red**. There is a tie for 3rd place under both distances, but it doesn't matter: the tied points share a label, and the two nearest points already form a 2-of-3 majority.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: every distance from (0, 0).**

| Point | Euclidean | Manhattan | Label |
|---|---|---|---|
| (3, 0) | √9 = 3 | 3 + 0 = 3 | red |
| (2, 2) | √8 ≈ 2.83 | 2 + 2 = 4 | blue |
| (0, −3) | √9 = 3 | 0 + 3 = 3 | red |
| (−2, 2) | √8 ≈ 2.83 | 2 + 2 = 4 | blue |
| (5, 5) | √50 ≈ 7.07 | 5 + 5 = 10 | blue |

**Step 2: (a) Euclidean.** Sorted: (2, 2) and (−2, 2) at 2.83 (both blue), then (3, 0) and (0, −3) at 3 (both red), then (5, 5) at 7.07. The 3 nearest are the two blues plus one of the two reds. Vote: blue 2, red 1, so **blue**.

**Step 3: (b) Manhattan.** Sorted: (3, 0) and (0, −3) at 3 (both red), then (2, 2) and (−2, 2) at 4 (both blue), then (5, 5) at 10. The 3 nearest are the two reds plus one of the two blues. Vote: red 2, blue 1, so **red**.

**Step 4: do the ties matter?** Under both distances, 3rd place is a tie between two points. Check whether the choice could change the answer:
- The two tied points have the *same* label, so whichever one you pick, the vote is identical.
- Even if they had different labels, nothing would change: the two nearest points already agree, which is 2 votes out of 3 before the third point is counted.

So the tie is real but harmless. A tie *would* matter if the two nearest points disagreed (one red, one blue) and the tied third-place points had different labels. Then the tie-break alone would decide the answer, and you'd need the exam's tie rule.

**Step 5: why the two distances disagree.** The diagonal points (2, 2) and (−2, 2) are close in a straight line (2.83), but far on a grid, because you must walk 2 across *and* 2 up (4). The points on the axes, (3, 0) and (0, −3), are 3 away either way. So Euclidean favours the diagonal blues, and Manhattan favours the axis reds. The choice of distance is a modelling decision, and here it flips the prediction.

**What to remember:** execute exactly the distance you're given: different distances can produce different neighbours. When there's a tie, don't ignore it and don't panic. Check whether either tie-break could change the vote.

**Common trap:** using Euclidean distance out of habit in part (b). Another is declaring "there's a tie, so the answer is undefined" without checking whether the tie matters.
</details>

---

### 3.2 Bad start

<details><summary>Hint 1: understand the question</summary>

A **centroid** is the centre of a cluster: the mean (average) of its points. Example: the centroid of {1, 2, 3} is (1 + 2 + 3)/3 = 2. **SSE** adds up (point − its centroid)² over all points. For {1, 2, 3} with centroid 2, SSE = 1 + 0 + 1 = 2. Lower SSE means tighter clusters.

On a number line with centroids at 1 and 2, which points are closer to 1 than to 2? Where exactly is the boundary between "closer to 1" and "closer to 2"?
</details>

<details><summary>Hint 2: the key idea</summary>

In 1-D, the boundary between two centroids is their **midpoint**: everything to the left of it goes to the left centroid. So each round is: find the midpoint, split the sorted list there, and take the mean of each side. Repeat until the split stops changing. Keep a table with one row per round and columns for the centroids, the midpoint, the left cluster, the right cluster and the new centroids.

For (c): k-means is trying to make SSE small. Compare the SSE of the two runs.
</details>

<details><summary>Hint 3: set it up</summary>

(a) Round 1: centroids 1 and 2, midpoint 1.5. Left = {1}, right = {2, 3, 8, 9, 10, 25}. New centroids: 1 and (2 + 3 + 8 + 9 + 10 + 25)/6 = 57/6 = 9.5. Now repeat with 1 and 9.5.

(b) Round 1: centroids 1 and 25, midpoint 13.
</details>

<details><summary>Answer</summary>

(a) Final centroids **2 and 13**, SSE **196**.
(b) Final centroids **5.5 and 25**, SSE **77.5**.
(c) Run **(b)** found the better clustering (lower SSE). k-means only finds a *local* minimum, so the starting centroids change where it ends up.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the midpoint shortcut.** Take centroids a < b. The midpoint (a + b)/2 is the one place that is equally far from both. Move left of it and you get closer to a and farther from b; move right and the opposite happens. So a point goes to the left centroid exactly when it is left of the midpoint. The problem adds a tie rule: a point *exactly* on the midpoint goes left. That rule is part of the definition (M1), so as you run, check whether any point ever lands exactly on a midpoint.

**Step 2: (a) start at 1 and 2.**

| Round | Centroids | Midpoint | Left cluster | Right cluster | New centroids |
|---|---|---|---|---|---|
| 1 | 1, 2 | 1.5 | {1} | {2, 3, 8, 9, 10, 25} | 1, 57/6 = 9.5 |
| 2 | 1, 9.5 | 5.25 | {1, 2, 3} | {8, 9, 10, 25} | 6/3 = 2, 52/4 = 13 |
| 3 | 2, 13 | 7.5 | {1, 2, 3} | {8, 9, 10, 25} | 2, 13 |

Round 3's clusters are the same as round 2's, so the centroids will never move again. The run has **converged** at **2 and 13**. No point ever sat exactly on a midpoint, so the tie rule never fired.

SSE:
- Left: (1 − 2)² + (2 − 2)² + (3 − 2)² = 1 + 0 + 1 = 2
- Right: (8 − 13)² + (9 − 13)² + (10 − 13)² + (25 − 13)² = 25 + 16 + 9 + 144 = 194
- Total: **196**

**Step 3: (b) start at 1 and 25.**

| Round | Centroids | Midpoint | Left cluster | Right cluster | New centroids |
|---|---|---|---|---|---|
| 1 | 1, 25 | 13 | {1, 2, 3, 8, 9, 10} | {25} | 33/6 = 5.5, 25 |
| 2 | 5.5, 25 | 15.25 | {1, 2, 3, 8, 9, 10} | {25} | 5.5, 25 |

Converged at **5.5 and 25**. Again, no point was ever exactly on a midpoint.

SSE: the distances from 5.5 are 4.5, 3.5, 2.5, 2.5, 3.5, 4.5, and 25 is 0 from its own centroid.
2 × (4.5² + 3.5² + 2.5²) = 2 × (20.25 + 12.25 + 6.25) = 2 × 38.75 = **77.5**.

**Step 4: why the two steps make sense (M6: what does the argmin pick?).** The **argmin** of a quantity is the choice that makes it smallest. k-means is trying to make SSE as small as possible, and each step picks the argmin for one part while holding the other part fixed:
- The assign step sends each point to the centroid with the smallest squared distance: the argmin over centroids.
- The update step moves each centroid to the location that makes its cluster's sum of squared distances smallest. That location is the **mean**. You showed this in 1.4: squared loss is minimised by the mean.

So SSE goes down or stays the same at every step, which is why the algorithm always stops. Nothing promises it stops at the *best* answer, though.

**Step 5: (c) which run is better, and why did (a) get stuck?** Run (b) has SSE 77.5, far lower than 196. In fact 77.5 is the best possible here: check every way to cut the sorted list into a left group and a right group, and nothing beats it.

Run (a) got stuck at 2 and 13. Every point is already nearest to its own centroid, and each centroid is already the mean of its cluster, so neither step can change anything, even though a better clustering exists. This is a **local minimum**: no move the algorithm can make improves things, but a better answer exists somewhere else. Picture a ball resting in a small dip on a hillside. It can't roll uphill to reach the deep valley below.

Notice what run (a) paid for: the point 25 is 12 away from centroid 13, so it alone contributes 144 of the 196. Squared distance punishes far points heavily, and that's why the better solution gives the outlier 25 a cluster of its own.

**What to remember:** each k-means step lowers SSE, but it only finds a local minimum, so where it ends depends on where it starts. In practice you run it from several starts and keep the run with the lowest SSE. Compare clusterings by SSE, the quantity k-means is actually minimising.

**Common trap:** stopping after one round while the centroids are still moving. Another is assuming whatever k-means returns is the best possible clustering.
</details>

---

### 3.3 Best first split

<details><summary>Hint 1: understand the question</summary>

**Gini impurity** measures how mixed a node is. With class fractions p_yes and p_no, Gini = 1 − p_yes² − p_no². Two quick examples:
- a pure node (4 yes, 0 no): 1 − 1² − 0² = 0
- a 50/50 node: 1 − 0.25 − 0.25 = 0.5

So 0 means "all one class", and bigger means more mixed. It also has a plain meaning: pick two samples from the node at random (putting the first back before picking the second). They have the same class with probability p_yes² + p_no², so Gini is the chance the two picks have *different* classes.

Before computing anything: which of A, B, C looks best by eye? Look at split B. Is either child's yes/no mix any different from the parent's?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M6 (What does the argmin pick?)**: the tree picks the split with the *lowest* score, which is the same as the biggest gain. So compute the score of every split.

"Size-weighted" means each child counts in proportion to how many samples it holds:
score = (n_left/10) × Gini(left) + (n_right/10) × Gini(right).

Keep fractions exact until the end. The answer is ⌊1000 × gain⌋, so rounding early can change the last digit.
</details>

<details><summary>Hint 3: set it up</summary>

Parent: 6 yes and 4 no, so Gini = 1 − 0.6² − 0.4² = 0.48.

Split A: the left child (4, 0) has 4 samples, the right child (2, 4) has 6 samples. The right child's fractions are 2/6 = 1/3 and 4/6 = 2/3. Compute both Ginis and weight them by 4/10 and 6/10. Then do B and C the same way.
</details>

<details><summary>Answer</summary>

Feature **A**. ⌊1000 × gain⌋ = **213**.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the parent.** 6 yes, 4 no: Gini = 1 − 0.36 − 0.16 = **0.48**.

**Step 2: score each split.**

*Split A.* Left (4, 0), 4 samples: pure, so Gini 0. Right (2, 4), 6 samples: 1 − (1/3)² − (2/3)² = 1 − 1/9 − 4/9 = 4/9 ≈ 0.444.
Score = (4/10)(0) + (6/10)(4/9) = 24/90 = 4/15 ≈ 0.2667.

*Split B.* Each child is (3, 2) with 5 samples: 1 − 0.36 − 0.16 = 0.48.
Score = 0.48, so the gain is 0. Each child has the same 60/40 mix as the parent, so the split has taught you nothing.

*Split C.* Left (5, 1), 6 samples: 1 − 25/36 − 1/36 = 10/36 ≈ 0.278. Right (1, 3), 4 samples: 1 − 1/16 − 9/16 = 6/16 = 0.375.
Score = (6/10)(10/36) + (4/10)(6/16) = 1/6 + 3/20 = 19/60 ≈ 0.3167.

| Split | Score | Gain = 0.48 − score |
|---|---|---|
| A | 4/15 ≈ 0.2667 | 16/75 ≈ 0.2133 |
| B | 0.48 | 0 |
| C | 19/60 ≈ 0.3167 | ≈ 0.1633 |

**Step 3: pick the argmin.** The lowest score (equivalently, the biggest gain) is **A**.
Gain = 12/25 − 4/15 = 36/75 − 20/75 = 16/75 = 0.21333…, so ⌊1000 × 0.21333⌋ = **213**.

**Step 4: stop and notice.** Suppose each child simply predicts its majority class, and count the mistakes:
- A: the left child predicts yes (0 wrong), the right child predicts no (2 wrong). 2 mistakes.
- C: the left child predicts yes (1 wrong), the right child predicts no (1 wrong). 2 mistakes.

Counting mistakes can't tell A and C apart. Gini can, because it doesn't just count errors: it rewards how pure each child is. A's left child is perfectly pure, so that branch of the tree is already finished.

**What to remember:** Gini = 1 − Σp², the chance that two random picks disagree. A split's score is the size-weighted average of its children's Gini, and the tree picks the lowest score (the biggest gain). A split whose children keep the parent's mix gains nothing.

**Common trap:** forgetting to weight by child size. A plain average gives A a score of (0 + 4/9)/2 = 0.222 and a "gain" of 257, which is wrong. Also watch for reporting the score (266) instead of the gain, and for rounding the score to 0.27 too early, which gives 210.
</details>

---

### 3.4 Single vs complete linkage

<details><summary>Hint 1: understand the question</summary>

To merge clusters you need a distance between two *groups* of points, not just two points. The rule for that is called the **linkage**. Try it on {0, 1} and {4, 5} before running anything:
- **single** linkage uses the *closest* pair, one point from each group;
- **complete** linkage uses the *farthest* pair.

What does each give?

Two more terms. The record of every merge, drawn as a tree, is a **dendrogram**. The **height** of a merge is the cluster distance at which it happened. "Cut at height 4" means: undo every merge that happened above height 4. The groups left over are the clusters.
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M1 (Read the definition, not your memory)**: run the procedure literally. At each step, list the distance between every pair of current clusters (using the linkage rule), merge the closest pair, and write down the height. Run single and complete side by side.
</details>

<details><summary>Hint 3: set it up</summary>

The first three merges are the same under both linkages: {0, 1} at height 1, {4, 5} at height 1, then {11, 13} at height 2.

Three clusters remain: {0, 1}, {4, 5} and {11, 13}. Compute all three pairwise distances under single linkage, then under complete linkage.
</details>

<details><summary>Answer</summary>

(a) Single: **6**. Complete: **13**.
(b) Single: **2** clusters. Complete: **3** clusters.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: the first merges.** At the start, every point is its own cluster. For two one-point clusters, the closest pair and the farthest pair are the same pair, so single and complete agree. On a line, the closest points are neighbours. The gaps between neighbours are:

0–1: 1, 1–4: 3, 4–5: 1, 5–11: 6, 11–13: 2.

- The two smallest gaps are both 1: merge {0, 1} at height 1 and {4, 5} at height 1. The order doesn't matter, because the two merges involve different points.
- Next, check every pair of current clusters. Under single linkage {0, 1} to {4, 5} is 3, and under complete linkage it is 5. Nothing is closer than {11} to {13}, at 2. Merge {11, 13} at height 2.

**Step 2: three clusters left.** Call them P = {0, 1}, Q = {4, 5}, R = {11, 13}.

| Pair | Single (closest pair) | Complete (farthest pair) |
|---|---|---|
| P–Q | 1 ↔ 4: 3 | 0 ↔ 5: 5 |
| Q–R | 5 ↔ 11: 6 | 4 ↔ 13: 9 |
| P–R | 1 ↔ 11: 10 | 0 ↔ 13: 13 |

Both linkages merge P and Q next: single at height 3, complete at height 5.

**Step 3: the final merge.** {0, 1, 4, 5} with {11, 13}:
- Single: the closest pair is 5 ↔ 11, so height **6**.
- Complete: the farthest pair is 0 ↔ 13, so height **13**.

The full record:

| Merge | Single height | Complete height |
|---|---|---|
| {0} + {1} | 1 | 1 |
| {4} + {5} | 1 | 1 |
| {11} + {13} | 2 | 2 |
| {0, 1} + {4, 5} | 3 | 5 |
| {0, 1, 4, 5} + {11, 13} | **6** | **13** |

**Step 4: (b) cut at height 4.** Keep the merges below height 4 and undo the rest. No merge happens at exactly 4, so there's no doubt about which side any merge falls on.
- Single: the merges at 1, 1, 2 and 3 are kept; the merge at 6 is undone. Clusters: {0, 1, 4, 5} and {11, 13}. That's **2** clusters.
- Complete: the merges at 1, 1 and 2 are kept; the merges at 5 and 13 are undone. Clusters: {0, 1}, {4, 5}, {11, 13}. That's **3** clusters.

A quick count to check: each kept merge turns two clusters into one, so clusters = 6 points − (merges kept). Single: 6 − 4 = 2. Complete: 6 − 3 = 3.

**Step 5: what this shows.** On a line, single linkage simply merges the neighbour gaps from smallest to largest, so its final height is the biggest gap (6). Complete linkage's final merge always includes the two extreme points, so its final height is the full span of the data (13 − 0 = 13). Single linkage *chains* groups together through just one close pair: 1 and 4 are only 3 apart, so {0, 1} and {4, 5} join early. Complete linkage needs *every* pair to be close, so it prefers compact clusters.

**What to remember:** the linkage rule *is* the definition of "distance between groups". Change it and the whole tree changes. Single = closest pair (chains), complete = farthest pair (compact). To cut a dendrogram at height h, undo every merge above h.

**Common trap:** using the distance between cluster *centres* from memory. That is a different linkage, and it gives a final height of 9.5 (between centres 2.5 and 12), which matches neither answer.
</details>

---

### 3.5 PCA in 2-D

<details><summary>Hint 1: understand the question</summary>

Several terms here may be new. None of them is the puzzle, so here they are.
- **Centred**: the x-values average to 0, and so do the y-values.
- **First principal component (PC1)**: the direction through the origin along which the points are most spread out.
- **Scatter matrix**: the 2×2 table of sums $\begin{bmatrix}\sum x^2 & \sum xy\\ \sum xy & \sum y^2\end{bmatrix}$. Σx² measures the spread along x and Σy² the spread along y. Σxy is positive when x and y tend to have the same sign, i.e. the cloud tilts up to the right.
- **Matrix times a direction**: $\begin{bmatrix}a & b\\ c & d\end{bmatrix}$ times (v₁, v₂) gives (a v₁ + b v₂, c v₁ + d v₂).
- **Eigenvector**: a direction that the matrix only *stretches*, without turning it. The output points the same way as the input, just λ times as long. That stretch factor λ is the **eigenvalue**. Tiny example with $M = \begin{bmatrix}2 & 0\\ 0 & 3\end{bmatrix}$: (1, 0) becomes (2, 0) = 2 × (1, 0), so (1, 0) is an eigenvector with eigenvalue 2. But (1, 1) becomes (2, 3), which points a different way, so (1, 1) is not an eigenvector.
- **Trace** = a + d, the sum of the diagonal. **Determinant** (det) = ad − bc. For the tiny M: trace 5, det 6, and λ² − 5λ + 6 = (λ − 2)(λ − 3) gives eigenvalues 2 and 3, as expected.

Now sketch the five points. Which way does the cloud stretch? Is that direction steeper or flatter than the line y = x?
</details>

<details><summary>Hint 2: the key idea</summary>

Move **M10 (Kill options with counterexamples)**: use your sketch to rule out options before computing anything. Is the cloud tilted? Is it steeper or flatter than 45°? (x runs from −2 to 2, but y only from −1 to 1.)

To decide between the options that survive: compute the scatter matrix, solve the quadratic for λ₁, and find the eigenvector's slope v₂/v₁. A line through the origin with slope m makes an angle θ with the x-axis where tan θ = m (tan is "rise over run" for that angle). Useful values: tan 30° = 1/√3 ≈ 0.577, and tan 45° = 1.
</details>

<details><summary>Hint 3: set it up</summary>

Σx² = 4 + 1 + 0 + 1 + 4 = 10, Σy² = 4, Σxy = 6. So the matrix is $\begin{bmatrix}10 & 6\\ 6 & 4\end{bmatrix}$, with trace 14 and det = 10 × 4 − 6 × 6 = 4. Solve λ² − 14λ + 4 = 0.

For the eigenvector, write out "matrix times (v₁, v₂) = λ₁ × (v₁, v₂)" and use the first row: 10v₁ + 6v₂ = λ₁v₁.
</details>

<details><summary>Answer</summary>

(a) **32°** (b) **97**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: check it's centred, and sketch.** x: (−2 − 1 + 0 + 1 + 2)/5 = 0. y: (−1 − 1 + 0 + 1 + 1)/5 = 0. Centred, as stated. The points rise from bottom-left to top-right, but x runs from −2 to 2 while y only runs from −1 to 1.

**Step 2: kill options first (M10).**
- **0° and 90°**: the cloud clearly tilts up to the right (Σxy = 6 > 0), so the best direction is neither axis. Killed.
- **45° and 58°**: the near points (1, 1) and (−1, −1) lie on y = x, but the far points (2, 1) and (−2, −1) lie on the flatter line y = x/2, at about 27°. The far points are farther out, so they pull harder on the direction of greatest spread. The best line should be flatter than y = x, below 45°. That kills 45°, and 58° (steeper still) with it.

Two survivors: 22° and 32°. Your intuition says "somewhere between 27° and 45°", which points to 32°. Now confirm it.

**Step 3: build the scatter matrix.**

| Point | x² | y² | xy |
|---|---|---|---|
| (−2, −1) | 4 | 1 | 2 |
| (−1, −1) | 1 | 1 | 1 |
| (0, 0) | 0 | 0 | 0 |
| (1, 1) | 1 | 1 | 1 |
| (2, 1) | 4 | 1 | 2 |
| **Sum** | **10** | **4** | **6** |

So the matrix is $S = \begin{bmatrix}10 & 6\\ 6 & 4\end{bmatrix}$.

**Step 4: the eigenvalues.** Trace = 10 + 4 = 14. Det = 10 × 4 − 6 × 6 = 4. So λ² − 14λ + 4 = 0.

Quadratic formula: λ = (14 ± √(196 − 16))/2 = (14 ± √180)/2 = 7 ± √45. By hand: 6.7² = 44.89, so √45 ≈ 6.708. That gives λ₁ ≈ 13.708 and λ₂ ≈ 0.292.

Why does that quadratic hold? "S times v = λ times v" means two equations: (10 − λ)v₁ + 6v₂ = 0 and 6v₁ + (4 − λ)v₂ = 0. Each one is a line through the origin in the (v₁, v₂) plane. Two such lines share a point other than (0, 0) only if they are the same line, which means their coefficients are in proportion: (10 − λ)(4 − λ) = 6 × 6. Expanding gives λ² − 14λ + 40 − 36 = 0, which is λ² − (trace)λ + det = 0.

**Step 5: the eigenvector for λ₁.** Use the first equation: (10 − 13.708)v₁ + 6v₂ = 0, so v₂/v₁ = 3.708/6 = **0.618**. PC1 is the line through the origin with slope 0.618.

Check that S only stretches this direction: S × (1, 0.618) = (10 + 6 × 0.618, 6 + 4 × 0.618) = (13.708, 8.472). And 13.708 × (1, 0.618) = (13.708, 8.472). Same direction, 13.708 times longer. (As it happens, 0.618 = (√5 − 1)/2, which is related to the golden ratio.)

**Step 6: turn the slope into an angle.** The angle θ satisfies tan θ = 0.618. Without a calculator: tan 30° = 1/√3 ≈ 0.577 (from the 30-60-90 triangle with sides 1, √3, 2), and tan 45° = 1. The slope 0.618 is a little more than 0.577 and less than 1, so θ is a little more than 30° and less than 45°. Of the survivors, only **32°** fits. (With a calculator: θ ≈ 31.7°.)

**Step 7: (b) fraction of variance.** **Variance** is the average squared distance from the mean. Variance would divide every sum by 5, but that scales both λ's by the same amount and cancels in the fraction, so you can use the scatter matrix directly.

λ₁/(λ₁ + λ₂) = 13.708/14 = 0.979, so **97**.

Why is λ₁ + λ₂ exactly 14? Any quadratic with roots λ₁ and λ₂ can be written (λ − λ₁)(λ − λ₂) = λ² − (λ₁ + λ₂)λ + λ₁λ₂. Compare with λ² − 14λ + 4: the roots add up to the trace, 14. And the trace is Σx² + Σy² = Σ(x² + y²), the total of the squared distances from the centre: the total spread in all directions. So PC1 captures 13.708 of the 14 units of spread, and PC2 only 0.292. That fits the sketch: the five points lie almost on a line.

**What to remember:** PC1 is the direction of greatest spread. For a 2×2 scatter matrix, get λ from λ² − (trace)λ + det = 0, then the slope v₂/v₁ from one row of "S v = λ v". Fraction explained = λ₁ ÷ trace. Sketch first and kill options: the answer leans toward the axis with more spread.

**Common trap:** writing the slope upside down. v₁/v₂ = 1/0.618 = 1.618 gives about 58°, which is exactly the distractor in the options. Slope is rise over run, v₂/v₁. The kill step catches this mistake: 58° is steeper than 45°, which the sketch already ruled out.
</details>
