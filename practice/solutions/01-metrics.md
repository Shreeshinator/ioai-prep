# Set 01 solutions: Evaluation metrics

> Make a real attempt first (10–15 min per problem). Then open **one** hint, try again, and only then open the next. If a word or symbol in a problem is new to you, open Hint 1 straight away: notation is not something to struggle with. You can check a final answer without spoilers in `notebooks/01_metrics.ipynb`.

---

### 1.1 Same model, two cities

<details><summary>Hint 1: understand the question</summary>

"Sensitivity 0.90" is a statement about *sick* people only: of the sick, 90% get flagged. "Specificity 0.95" is about *healthy* people only: of the healthy, 95% are correctly *not* flagged. Precision asks about a third group: of the people who were **flagged**, what fraction are actually sick? Which groups do the flagged people come from?
</details>

<details><summary>Hint 2: the key idea</summary>

Percentages of percentages get confusing. Replace them with **counts**: pretend City P has exactly 1,000 people and work out how many people land in each box.
</details>

<details><summary>Hint 3: set it up</summary>

City P: 1,000 people, of whom 2% = 20 are sick and 980 are healthy. Fill in this table, then do the same for City Q.

| | Flagged | Not flagged |
|---|---|---|
| Sick (20) | ? | ? |
| Healthy (980) | ? | ? |
</details>

<details><summary>Answer</summary>

City P: **26**. City Q: **81**. Follow-up: **B** (only precision changes).
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: turn rates into counts (City P, 1,000 people).**
- Sick = 2% of 1,000 = 20. Sensitivity 0.90, so flagged sick = 0.90 × 20 = **18** (true positives).
- Healthy = 980. Specificity 0.95, so 95% are *not* flagged, and the other 5% *are* flagged. Flagged healthy = 0.05 × 980 = **49** (false positives).

**Step 2: precision is "of the flagged, how many are sick?"**
Flagged = 18 + 49 = 67. Precision = 18/67 = 0.2687, so ⌊100 × 0.2687⌋ = **26**.

Stop and notice: the model is "90% sensitive", yet only about 1 in 4 flags is correct. That's because there are so many healthy people (980) that even a small 5% false-alarm rate produces more flags (49) than the sick group can (18).

**Step 3: City Q, same method.** Sick = 200, so TP = 180. Healthy = 800, so FP = 0.05 × 800 = 40. Precision = 180/220 = 0.818, giving **81**.

**Step 4: the follow-up.** An ROC curve plots TPR against FPR.
- TPR is sensitivity = TP ÷ (number of sick). It is computed *inside the sick group only*.
- FPR = FP ÷ (number of healthy). It is computed *inside the healthy group only*.

Changing *how many* sick people there are doesn't change what fraction of them get flagged. So TPR and FPR, and therefore the ROC curve, are unchanged. Precision divides by *all flagged people*, which mixes the two groups, so it does change. Answer: **B**.

**What to remember:** Rates conditioned on the true class (TPR, FPR, sensitivity, specificity) don't care about prevalence. Anything that divides by a predicted count (precision) does. When rates get confusing, imagine 1,000 people.

**Common trap:** reading "90% sensitive" as "90% of flags are right."
</details>

---

### 1.2 AUC by counting

<details><summary>Hint 1: understand the question</summary>

The definition is given to you: AUC = the fraction of (positive, negative) pairs where the positive scores higher. How many such pairs are there?
</details>

<details><summary>Hint 2: the key idea</summary>

You don't need to draw any curve. Just **count wins**. For each positive score, count how many negatives it beats.

For parts (b) and (c), ask: *does the transformation change which of two scores is bigger?*
</details>

<details><summary>Hint 3: set it up</summary>

There are 4 positives × 5 negatives = 20 pairs. Make a table: one row per positive, columns "beats how many negatives?" and "ties?".

For (c), first compute the new score for all 9 numbers, then count again.
</details>

<details><summary>Answer</summary>

(a) **0.75** (b) **0.75** (c) **0.525**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: count the pairs.** Every positive is paired with every negative: 4 × 5 = 20 pairs.

**Step 2: count the wins.** Negatives: 0.70, 0.60, 0.40, 0.20, 0.10.

| Positive | Beats | Wins |
|---|---|---|
| 0.90 | all five | 5 |
| 0.80 | all five | 5 |
| 0.55 | 0.40, 0.20, 0.10 | 3 |
| 0.30 | 0.20, 0.10 | 2 |

Total = 15, so AUC = 15/20 = **0.75**.

**Step 3: (b) squaring.** Does squaring ever swap the order of two scores? For *positive* numbers, a > b > 0 means a² > b² (e.g. 0.9 > 0.8 → 0.81 > 0.64). A function that always preserves order like this is called **monotone increasing**. Every comparison in Step 2 comes out the same, so AUC = **0.75**.

**Step 4: (c) (s − 0.5)².** This measures *distance from 0.5*, so 0.9 and 0.1 both become 0.16. Order is **not** preserved. Compute the new scores:
- Positives: 0.90 → 0.16, 0.80 → 0.09, 0.55 → 0.0025, 0.30 → 0.04
- Negatives: 0.70 → 0.04, 0.60 → 0.01, 0.40 → 0.01, 0.20 → 0.09, 0.10 → 0.16

Count again, with a tie worth ½:

| Positive | Beats | Ties | Wins |
|---|---|---|---|
| 0.16 | 0.04, 0.01, 0.01, 0.09 | 0.16 | 4.5 |
| 0.09 | 0.04, 0.01, 0.01 | 0.09 | 3.5 |
| 0.0025 | none | — | 0 |
| 0.04 | 0.01, 0.01 | 0.04 | 2.5 |

Total = 10.5, so AUC = 10.5/20 = **0.525**, almost a coin flip.

**What to remember:** AUC only looks at the **order** of the scores. Any monotone increasing transform leaves it unchanged. A transform that scrambles the order can destroy it.

**Common trap:** assuming "any transformation changes the curve" or "no transformation does." Always ask whether the order is preserved.
</details>

---

### 1.3 Fraud desk capacity

<details><summary>Hint 1: understand the question</summary>

The limit is on the *number of flagged transactions*: at most 300. Which transactions get flagged? Both kinds: real frauds the model catches and legitimate ones it wrongly flags.
</details>

<details><summary>Hint 2: the key idea</summary>

Convert each point's rates into **counts per day**. How many frauds and how many legitimate transactions are there each day?
</details>

<details><summary>Hint 3: set it up</summary>

Per day there are 100 frauds and 9,900 legitimate transactions.

Flagged = (frauds caught) + (legit wrongly flagged) = 100 × TPR + 9,900 × FPR.

Compute this for each point.
</details>

<details><summary>Answer</summary>

Point **R**. Precision **28**.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: counts per day.** 1% of 10,000 = 100 frauds, leaving 9,900 legitimate.

**Step 2: flagged count at each point.** Frauds caught = 100 × TPR. Legit flagged = 9,900 × FPR.

| Point | Frauds caught | Legit flagged | Total flagged |
|---|---|---|---|
| P | 50 | 49.5 | 99.5 |
| Q | 65 | 99 | 164 |
| R | 80 | 198 | **278** |
| S | 88 | 297 | 385 |
| T | 93 | 495 | 588 |

**Step 3: apply the constraint.** P, Q and R fit under 300. Of those, R catches the most fraud (80), so choose **R**.

**Step 4: precision at R.** 80 of the 278 flags are real fraud: 80/278 = 0.2878, giving **28**.

**What to remember:** capacity limits are about **counts**. Count = rate × size of the group the rate applies to. The negative group is huge (9,900), so even small FPRs dominate the flag count.

**Common trap:** comparing the FPR directly to 300/10,000 = 3%. That ignores the frauds, which take up review slots too.
</details>

---

### 1.4 One bad day

<details><summary>Hint 1: understand the question</summary>

MAE is the average of |error|. RMSE is the square root of the average of error². Compute both for each model. What does *squaring* do to one big error compared with several small ones?
</details>

<details><summary>Hint 2: the key idea (part b)</summary>

Adding $c$ to every prediction changes every error from $e$ to $e - c$. Try a few values of $c$ (0, 1, 2, 3) for Model B and watch how RMSE and MAE behave. Which "centre" of the list [0, 0, 0, 0, 10] does each one pick?
</details>

<details><summary>Hint 3: set it up (part b)</summary>

For RMSE, minimise $f(c) = \sum (e_i - c)^2$. This is a quadratic in $c$: expand it and find its lowest point.

For MAE, minimise $g(c) = \sum |e_i - c|$. Ask what happens to $g$ when you move $c$ a little to the right.
</details>

<details><summary>Answer</summary>

(a) A: MAE 2, RMSE 2. B: MAE 2, RMSE √20 ≈ 4.47. RMSE prefers A; MAE rates them equal.
(b) RMSE is minimised at $c = 2$ (RMSE becomes **4**). MAE is minimised at $c = 0$.
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: (a)**
- A: every |error| is 2, so MAE = 2. Every error² is 4, so RMSE = √4 = 2.
- B: |errors| sum to 10, so MAE = 10/5 = 2. Errors² sum to 100, so RMSE = √(100/5) = √20 ≈ 4.47.

MAE calls it a tie. RMSE says A is much better, because squaring turns the single 10 into 100, which outweighs everything else.

**Step 2: (b) RMSE.** Minimising RMSE is the same as minimising the sum of squares (square root and dividing by 5 don't change *where* the minimum is):

$f(c) = 4(0-c)^2 + (10-c)^2 = 4c^2 + 100 - 20c + c^2 = 5c^2 - 20c + 100.$

A quadratic $ac^2 + bc + k$ with $a > 0$ is lowest at $c = -b/(2a) = 20/10 = 2$. That is the **mean** of the errors, (0+0+0+0+10)/5 = 2. The new errors are [−2, −2, −2, −2, 8], with squares 4+4+4+4+64 = 80, so RMSE = √(80/5) = √16 = **4**.

**Step 3: (b) MAE.** Start at $c = 0$. If you nudge $c$ right by a small amount δ:
- the four errors at 0 each get *worse* by δ: +4δ
- the error at 10 gets *better* by δ: −δ

The net change is +3δ, so moving right hurts. Moving left makes all five worse. So $c = 0$ is best, which is the **median** of the errors.

**What to remember:** squared loss is minimised by the **mean**, absolute loss by the **median**. A single outlier drags the mean but barely moves the median. (The Jan 18 Godown problem is built on exactly this.)

**Common trap:** assuming the shift that's best for one metric is best for every metric.
</details>

---

### 1.5 Read the convention

<details><summary>Hint 1: understand the question</summary>

Here, **rows are predicted** and **columns are actual**. Recall for class 2 asks: of the items that *actually are* class 2, what fraction did we catch? Do you need a row or a column for "actually class 2"?
</details>

<details><summary>Hint 2: the key idea</summary>

- Recall uses the **actual** total, which here is a **column** sum.
- Precision uses the **predicted** total, which here is a **row** sum.

Compute every row and column total first.
</details>

<details><summary>Hint 3: set it up</summary>

Column totals (actual): 50, 40, 60. Row totals (predicted): 50, 50, 50. The diagonal holds the correct predictions: 40, 30, 45. For each class:
- recall = diagonal ÷ column total
- precision = diagonal ÷ row total
- F1 = 2PR/(P+R)
</details>

<details><summary>Answer</summary>

(a) Recall **0.75**, precision **0.60**. (b) **76** (c) **76**
</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: totals.**
- Actual class 1 (column 1): 40 + 10 + 0 = 50
- Actual class 2: 5 + 30 + 5 = 40
- Actual class 3: 5 + 10 + 45 = 60
- Each row sums to 50.

**Step 2: class 2.** Recall = 30/40 = **0.75**. Precision = 30/50 = **0.60**.
F1 = 2 × 0.75 × 0.6 / (0.75 + 0.6) = 0.9/1.35 = 0.667.

**Step 3: the other classes.**

| Class | Recall | Precision | F1 |
|---|---|---|---|
| 1 | 40/50 = 0.8 | 40/50 = 0.8 | 0.8 |
| 3 | 45/60 = 0.75 | 45/50 = 0.9 | 2(0.75)(0.9)/1.65 = 0.818 |

**Step 4: macro-F1** = (0.8 + 0.667 + 0.818)/3 = 0.7616, giving **76**.
**Accuracy** = (40 + 30 + 45)/150 = 115/150 = 0.767, giving **76**.

**What to remember:** before computing anything, find out which axis is "actual". Recall divides by the actual total, precision by the predicted total.

**Common trap:** using the usual "rows = actual" layout from memory gives recall₂ = 30/50 = 0.6, which is wrong. The Jan 18 paper used rows = predicted, just like this problem.
</details>
