# Set 01: Evaluation metrics

**Week 1** · 5 problems · target time 35 min · moves: M1, M3, M4, M5

> Write a **guess** in the margin before computing, then solve on paper. Check answers in `notebooks/01_metrics.ipynb` (spoiler-free checker). Read `solutions/01-metrics.md` only after you've checked.

---

### 1.1 Same model, two cities [3 pts]

A screening model has **sensitivity 0.90** and **specificity 0.95**. It is deployed unchanged in two cities. In City P, 2% of people have the condition. In City Q, 20% do.

**Output:** Report ⌊100 × precision⌋ in City P and in City Q (two integers).

**Follow-up (MCQ):** Which of these changes between the cities?
A. Only the ROC curve  B. Only precision  C. Both  D. Neither

---

### 1.2 AUC by counting [3 pts]

The **AUC** equals the probability that a randomly chosen positive gets a higher score than a randomly chosen negative. Ties count as ½.

| Positives | 0.90 | 0.80 | 0.55 | 0.30 | |
|---|---|---|---|---|---|
| **Negatives** | 0.70 | 0.60 | 0.40 | 0.20 | 0.10 |

**Output:**
(a) The AUC.
(b) The AUC after every score is replaced by $s^2$.
(c) The AUC after every score is replaced by $(s - 0.5)^2$.

---

### 1.3 Fraud desk capacity [3 pts]

A bank processes 10,000 transactions a day, and 1% are fraud. Investigators can review **at most 300 flagged transactions per day**. These operating points lie on the model's ROC curve:

| Point | P | Q | R | S | T |
|---|---|---|---|---|---|
| FPR | 0.005 | 0.01 | 0.02 | 0.03 | 0.05 |
| TPR | 0.50 | 0.65 | 0.80 | 0.88 | 0.93 |

**Output:** Find the point that catches the most fraud within capacity. Then report ⌊100 × precision⌋ at that point.

---

### 1.4 One bad day [3 pts]

Two forecasting models make these errors (prediction − truth) over 5 days:

- Model A: `[2, -2, 2, -2, 2]`
- Model B: `[0, 0, 0, 0, 10]`

**Output:**
(a) Give the MAE and RMSE of each model. Which metric prefers A?
(b) You may add one constant $c$ to all of Model B's predictions. Which $c$ minimises B's RMSE, and which $c$ minimises B's MAE? Report both values of $c$ and the minimised RMSE.

---

### 1.5 Read the convention [3 pts]

A 3-class confusion matrix is shown with **rows = predicted class** and **columns = actual class**. Read that again.

|  | Actual 1 | Actual 2 | Actual 3 |
|---|---|---|---|
| **Predicted 1** | 40 | 5 | 5 |
| **Predicted 2** | 10 | 30 | 10 |
| **Predicted 3** | 0 | 5 | 45 |

**Output:**
(a) Give the recall and precision of class 2.
(b) Report ⌊100 × macro-F1⌋, where macro-F1 is the plain average of the three per-class F1 scores.
(c) Report ⌊100 × accuracy⌋.
